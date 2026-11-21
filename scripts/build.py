#!/usr/bin/env python3
"""AllBlock builder.

Lädt alle Blocklisten aus sources.toml, normalisiert sie auf reine Domains,
dedupliziert und schreibt:

  <out>/lists/<kategorie>/<id>.txt       einzelne Quelle (Domains)
  <out>/combined/<kategorie>.txt          Gesamtliste der Kategorie (Domains)
  <out>/combined/<kategorie>.adblock.txt  Gesamtliste der Kategorie (||domain^)
  <out>/stats.json                        Statistik + Status jeder Quelle
  <out>/STATUS.md                         Übersicht mit Links und Zählern

Schlägt der Download einer Quelle fehl (oder liefert sie weniger als die
Hälfte der vorherigen Einträge), wird die zuletzt erfolgreich gebaute
Version aus <out>/lists weiterverwendet.

Nur Standardbibliothek, Python >= 3.11.
"""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import ipaddress
import json
import os
import re
import shutil
import sys
import time
import tomllib
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
USER_AGENT = "Mozilla/5.0 (compatible; AllBlock-builder/1.0)"
TIMEOUT = 90
RETRIES = 3
MIN_RATIO = 0.5  # neue Liste muss mind. 50 % der alten Größe haben
MAX_FILE_BYTES = 95 * 1024 * 1024  # GitHub lehnt Dateien > 100 MB ab

DOMAIN_RE = re.compile(
    r"^(?=.{1,253}$)(?:[a-z0-9_](?:[a-z0-9_-]{0,61}[a-z0-9_])?\.)+"
    r"(?:[a-z]{2,63}|xn--[a-z0-9-]{1,59})$"
)
HOSTS_IPS = {"0.0.0.0", "127.0.0.1", "::", "::1", "::0", "0:0:0:0:0:0:0:0", "255.255.255.255"}
IGNORED = {
    "localhost", "localhost.localdomain", "local", "broadcasthost", "ip6-localhost",
    "ip6-loopback", "ip6-localnet", "ip6-mcastprefix", "ip6-allnodes", "ip6-allrouters",
    "ip6-allhosts", "0.0.0.0", "localdomain",
}
# Adblock: ||domain^ optional mit harmlosen Modifiern
ADBLOCK_RE = re.compile(r"^\|\|([^\s/^$|]+)\^?(?:\$(.*))?$")
ADBLOCK_OK_MODIFIERS = {"", "important", "all", "document", "doc", "popup", "third-party", "3p"}


def header_lines(title: str, description: str, count: int, sources: list[str], repo: str, comment: str) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"Title: AllBlock – {title}",
        f"Description: {description}",
        f"Last modified: {now}",
        f"Entries: {count}",
        f"Homepage: https://github.com/{repo}",
        "Sources:",
        *[f"  - {s}" for s in sources],
    ]
    return "".join(f"{comment} {l}\n" for l in lines) + f"{comment}\n"


def is_valid_domain(d: str) -> bool:
    if d in IGNORED or not DOMAIN_RE.match(d):
        return False
    try:
        ipaddress.ip_address(d)
        return False
    except ValueError:
        return True


def clean_domain(raw: str) -> str | None:
    d = raw.strip().strip(".").lower()
    if d.startswith("*."):
        d = d[2:]
    elif d.startswith("."):
        d = d.lstrip(".")
    if not d or "*" in d:
        return None
    if not d.isascii():
        try:
            d = d.encode("idna").decode("ascii")
        except UnicodeError:
            return None
    return d if is_valid_domain(d) else None


def parse_list(text: str) -> tuple[set[str], set[str]]:
    """Gibt (blockierte Domains, Ausnahmen) zurück."""
    blocked: set[str] = set()
    allowed: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line[0] in "#!;[":
            continue
        # Inline-Kommentare
        if " #" in line:
            line = line.split(" #", 1)[0].strip()
        if "\t#" in line:
            line = line.split("\t#", 1)[0].strip()

        if line.startswith("@@"):
            m = ADBLOCK_RE.match(line[2:])
            if m and (d := clean_domain(m.group(1))):
                allowed.add(d)
            continue

        if line.startswith("||"):
            m = ADBLOCK_RE.match(line)
            if not m:
                continue
            mods = {x.strip().lower() for x in (m.group(2) or "").split(",")}
            if not mods <= ADBLOCK_OK_MODIFIERS:
                continue
            if d := clean_domain(m.group(1)):
                blocked.add(d)
            continue

        # Kosmetische/sonstige Adblock-Regeln überspringen
        if any(tok in line for tok in ("##", "#@#", "#?#", "#$#", "$$")) or line.startswith(("|", "/")):
            continue

        # URLs (z. B. OpenPhish)
        if "://" in line:
            host = urlsplit(line).hostname
            if host and (d := clean_domain(host)):
                blocked.add(d)
            continue

        # dnsmasq address=/domain/0.0.0.0
        if line.startswith(("address=/", "server=/", "local=/")):
            parts = line.split("/")
            if len(parts) >= 2 and (d := clean_domain(parts[1])):
                blocked.add(d)
            continue

        parts = line.split()
        if len(parts) >= 2 and parts[0] in HOSTS_IPS:
            for p in parts[1:]:
                if d := clean_domain(p):
                    blocked.add(d)
        elif len(parts) == 1:
            if d := clean_domain(parts[0]):
                blocked.add(d)
    return blocked, allowed


def download(url: str) -> str:
    last_err: Exception | None = None
    for attempt in range(1, RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                data = resp.read()
                if resp.headers.get("Content-Encoding") == "gzip" or data[:2] == b"\x1f\x8b":
                    data = gzip.decompress(data)
            return data.decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError, OSError, EOFError) as e:
            last_err = e
            if attempt < RETRIES:
                time.sleep(3 * attempt)
    raise RuntimeError(f"{type(last_err).__name__}: {last_err}")


@dataclass
class Source:
    category: str
    id: str
    name: str
    url: str
    homepage: str = ""
    domains: set[str] = field(default_factory=set)
    status: str = "pending"
    error: str = ""


def read_domain_file(path: Path) -> set[str]:
    """Liest eine zuvor gebaute Liste (inkl. aufgeteilter .partN.txt-Dateien)."""
    files = [path] if path.exists() else sorted(path.parent.glob(f"{path.stem}.part*.txt"))
    return {l.strip() for f in files for l in f.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")}


def fetch_source(src: Source, previous: set[str]) -> Source:
    try:
        blocked, allowed = parse_list(download(src.url))
        domains = blocked - allowed
        if not domains:
            raise RuntimeError("keine gültigen Domains gefunden")
        if previous and len(domains) < len(previous) * MIN_RATIO:
            raise RuntimeError(f"nur {len(domains)} statt zuvor {len(previous)} Einträge – verdächtig")
        src.domains, src.status = domains, "ok"
    except Exception as e:  # noqa: BLE001
        src.error = str(e)[:300]
        if previous:
            src.domains, src.status = previous, "stale"
        else:
            src.status = "failed"
    sym = {"ok": "✓", "stale": "~", "failed": "✗"}[src.status]
    print(f"  {sym} {src.category}/{src.id}: {len(src.domains):,}" + (f"  ({src.error})" if src.error else ""), flush=True)
    return src


def load_allowlist() -> set[str]:
    path = ROOT / "allowlist.txt"
    if not path.exists():
        return set()
    return {d for l in path.read_text(encoding="utf-8").splitlines() if (d := clean_domain(l.split("#", 1)[0]))}


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_list(path: Path, header: str, lines: list[str]) -> list[Path]:
    """Schreibt eine Liste; ist sie größer als MAX_FILE_BYTES (GitHub-Limit 100 MB),
    wird sie in <name>.part1.txt, <name>.part2.txt, … aufgeteilt."""
    total = len(header.encode()) + sum(len(l) + 1 for l in lines)
    if total <= MAX_FILE_BYTES:
        write(path, header + "\n".join(lines) + ("\n" if lines else ""))
        return [path]
    base = path.name.removesuffix(".txt")
    budget = MAX_FILE_BYTES - len(header.encode()) - 1024
    parts, chunk, size = [], [], 0
    for l in lines:
        if size + len(l) + 1 > budget and chunk:
            parts.append(chunk)
            chunk, size = [], 0
        chunk.append(l)
        size += len(l) + 1
    if chunk:
        parts.append(chunk)
    paths = []
    for i, chunk in enumerate(parts, 1):
        p = path.with_name(f"{base}.part{i}.txt")
        write(p, header.replace("Title: AllBlock – ", f"Title: AllBlock (Teil {i}/{len(parts)}) – ", 1)
              + "\n".join(chunk) + "\n")
        paths.append(p)
    return paths


def fmt_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=str(ROOT / "sources.toml"))
    ap.add_argument("--out", default=str(ROOT))
    ap.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", "AndersEben/AllBlock"))
    ap.add_argument("--branch", default="main", help="Branch, auf dem die Listen veröffentlicht werden")
    ap.add_argument("--only", nargs="*", help="Nur diese Kategorien bauen")
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    out = Path(args.out)
    cfg = tomllib.loads(Path(args.config).read_text(encoding="utf-8"))
    categories: dict = cfg["categories"]
    if args.only:
        categories = {k: v for k, v in categories.items() if k in args.only}

    sources = [
        Source(category=cat, id=s["id"], name=s["name"], url=s["url"], homepage=s.get("homepage", ""))
        for cat, c in categories.items()
        for s in c.get("sources", [])
    ]
    ids = [f"{s.category}/{s.id}" for s in sources]
    if len(ids) != len(set(ids)):
        print("Fehler: doppelte Quellen-IDs in sources.toml", file=sys.stderr)
        return 2

    # Vorherige Ergebnisse als Fallback einlesen
    previous = {f"{s.category}/{s.id}": read_domain_file(out / "lists" / s.category / f"{s.id}.txt") for s in sources}

    print(f"Lade {len(sources)} Quellen in {len(categories)} Kategorien …", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        sources = list(pool.map(lambda s: fetch_source(s, previous[f"{s.category}/{s.id}"]), sources))

    allow = load_allowlist()

    # Ausgabe neu aufbauen (alte Kategorien/Quellen entfernen)
    for sub in ("lists", "combined"):
        shutil.rmtree(out / sub, ignore_errors=True)

    raw = f"https://raw.githubusercontent.com/{args.repo}/{args.branch}"
    stats: dict = {"generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "categories": {}}
    readme_rows: list[str] = []
    readme_details: list[str] = []
    grand_total: set[str] = set()

    for cat, c in categories.items():
        cat_sources = [s for s in sources if s.category == cat]
        combined: set[str] = set()
        src_stats = []
        for s in cat_sources:
            doms = s.domains - allow
            src_stats.append({"id": s.id, "name": s.name, "url": s.url, "status": s.status,
                              "entries": len(doms), "error": s.error})
            if not doms:
                continue
            combined |= doms
            files = write_list(out / "lists" / cat / f"{s.id}.txt",
                               header_lines(s.name, f"{c['title']} – normalisierte Kopie von {s.url}",
                                            len(doms), [s.url], args.repo, "#"),
                               sorted(doms))
            st_files = [p.relative_to(out).as_posix() for p in files]
            src_stats[-1]["files"] = st_files

        names = [f"{s.name} ({s.url})" for s in cat_sources if s.domains]
        sorted_combined = sorted(combined)
        dom_files = write_list(out / "combined" / f"{cat}.txt",
                               header_lines(c["title"], c["description"], len(combined), names, args.repo, "#"),
                               sorted_combined)
        abp_files = write_list(out / "combined" / f"{cat}.adblock.txt",
                               header_lines(c["title"], c["description"], len(combined), names, args.repo, "!"),
                               [f"||{d}^" for d in sorted_combined])
        grand_total |= combined

        def links(label: str, paths: list[Path]) -> str:
            if len(paths) == 1:
                return f"[{label}]({raw}/{paths[0].relative_to(out).as_posix()})"
            return label + " " + " ".join(
                f"[Teil {i}]({raw}/{p.relative_to(out).as_posix()})" for i, p in enumerate(paths, 1))

        size = sum(p.stat().st_size for p in dom_files)
        stats["categories"][cat] = {
            "title": c["title"], "entries": len(combined),
            "files": [p.relative_to(out).as_posix() for p in dom_files + abp_files],
            "sources": src_stats,
        }
        readme_rows.append(
            f"| **{c['title']}** (`{cat}`) | {len(combined):,} | {fmt_size(size)} | "
            f"{links('Domains', dom_files)} · {links('Adblock', abp_files)} |"
        )
        det = [f"### {c['title']} (`{cat}`)", "", c["description"], "",
               "| Quelle | Einträge | Status | Liste |", "|---|---:|:---:|---|"]
        for s, st in zip(cat_sources, src_stats):
            icon = {"ok": "✅", "stale": "⚠️", "failed": "❌"}[s.status]
            link = " ".join(f"[{Path(f).name}]({raw}/{f})" for f in st.get("files", [])) or "–"
            name = f"[{s.name}]({s.homepage})" if s.homepage else s.name
            det.append(f"| {name} | {st['entries']:,} | {icon} | {link} |")
        readme_details += det + [""]

    stats["unique_total"] = len(grand_total)
    write(out / "stats.json", json.dumps(stats, indent=2, ensure_ascii=False) + "\n")

    ok = sum(s.status == "ok" for s in sources)
    stale = sum(s.status == "stale" for s in sources)
    failed = sum(s.status == "failed" for s in sources)
    readme = "\n".join([
        "# AllBlock – Status der Listen",
        "",
        f"Stand: **{stats['generated']}** · {len(sources)} Quellen ({ok} ✅ · {stale} ⚠️ veraltet · {failed} ❌) · "
        f"**{len(grand_total):,}** eindeutige Domains insgesamt",
        "",
        f"Diese Datei wird automatisch erzeugt. Projekt & Doku: https://github.com/{args.repo}",
        "",
        "## Gesamtlisten pro Kategorie",
        "",
        "| Kategorie | Domains | Größe | Download |",
        "|---|---:|---:|---|",
        *readme_rows,
        "",
        "## Einzellisten",
        "",
        *readme_details,
    ])
    write(out / "STATUS.md", readme)

    print(f"\nFertig: {ok} ok, {stale} veraltet, {failed} fehlgeschlagen – {len(grand_total):,} eindeutige Domains.")
    for cat, cs in stats["categories"].items():
        print(f"  {cat:14} {cs['entries']:>10,}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
