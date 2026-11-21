# AllBlock

Sammelt die bekannten öffentlichen DNS-Blocklisten für **AdGuard Home** und **Pi-hole** an einem Ort.
Jede Quelle wird normalisiert, dedupliziert und nach Kategorie sortiert.

- **Einzellisten:** jede Quelle als eigene, bereinigte Datei
- **Gesamtliste pro Kategorie:** alle Quellen einer Kategorie in einer Datei zusammengefasst, ohne Duplikate
- **Zwei Formate:** reine Domains (`.txt`) und Adblock-Syntax (`.adblock.txt`, `||domain^`)
- **Automatisch aktualisiert:** GitHub Actions baut die Listen zweimal täglich neu

> 📊 Eine aktuelle Übersicht mit Eintragszahlen, Status und Links zu **allen Einzellisten** steht im
> [STATUS.md](STATUS.md).

## Gesamtlisten pro Kategorie

| Kategorie | ID | Inhalt | Quellen | Download |
|---|---|---|---:|---|
| **Werbung** | `ads` | Werbe-Server, Ad-Networks, Pop-ups, mobile Werbung | 18 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/ads.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/ads.adblock.txt) |
| **Tracking & Telemetrie** | `tracking` | Tracker, Analytics, Session-Replay, Telemetrie von Geräten und Betriebssystemen | 24 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/tracking.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/tracking.adblock.txt) |
| **Malware & Threat Intelligence** | `malware` | Malware-Verteilung, C2-Server, Ransomware, Stalkerware, Malvertising | 12 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/malware.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/malware.adblock.txt) |
| **Phishing** | `phishing` | Phishing-Seiten und Credential-Harvesting | 5 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/phishing.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/phishing.adblock.txt) |
| **Scam & Betrug** | `scam` | Fake-Shops, Betrugsseiten, Spam, Redirect-Fallen | 8 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/scam.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/scam.adblock.txt) |
| **Cryptomining** | `cryptomining` | Browser-Miner und Cryptojacking | 3 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/cryptomining.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/cryptomining.adblock.txt) |
| **Erwachseneninhalte** | `adult` | Pornografie und NSFW-Inhalte | 7 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/adult.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/adult.adblock.txt) |
| **Glücksspiel** | `gambling` | Online-Casinos, Sportwetten | 4 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/gambling.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/gambling.adblock.txt) |
| **Social Media** | `social` | Soziale Netzwerke (Facebook, Instagram, TikTok, X, …) | 5 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/social.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/social.adblock.txt) |
| **Fake News** | `fakenews` | Bekannte Desinformationsseiten | 2 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/fakenews.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/fakenews.adblock.txt) |
| **Piraterie & Torrents** | `piracy` | Warez-, Streaming- und Torrent-Seiten | 3 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/piracy.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/piracy.adblock.txt) |
| **DoH / VPN / Proxy-Bypass** | `bypass` | Verhindert, dass Geräte den DNS-Filter über DoH, VPN oder Proxys umgehen | 3 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/bypass.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/bypass.adblock.txt) |
| **All-in-One** | `multi` | Große kuratierte Kombilisten (Werbung, Tracking, Malware) | 5 | [Domains](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/multi.txt) · [Adblock](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/multi.adblock.txt) |

Einzellisten liegen unter
`https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/<kategorie>/<id>.txt`,
zum Beispiel [`lists/multi/hagezi-pro.txt`](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/multi/hagezi-pro.txt).

### Größenordnung (Stand 21.11.2026)

| Kategorie | Domains | | Kategorie | Domains |
|---|---:|---|---|---:|
| malware | ~4,1 Mio. | | multi | ~730.000 |
| adult | ~1,2 Mio. | | gambling | ~720.000 |
| ads | ~1,0 Mio. | | tracking | ~380.000 |
| scam | ~890.000 | | piracy | ~67.000 |
| phishing | ~730.000 | | social | ~36.000 |

> ⚠️ **Arbeitsspeicher:** Sehr große Listen wie `malware` mit über 4 Mio. Einträgen brauchen viel RAM.
> Auf einem Raspberry Pi mit wenig Speicher besser die Einzellisten oder `multi` nehmen statt alles zu abonnieren.

## Einrichtung

### AdGuard Home
*Filter → DNS-Sperrlisten → Sperrliste hinzufügen → Benutzerdefinierte Liste hinzufügen* und die
**`.adblock.txt`**-URL der gewünschten Kategorie eintragen.

### Pi-hole
*Adlists* (v5) bzw. *Lists* (v6) öffnen und die URL eintragen, danach **Gravity aktualisieren**
(`pihole -g`). Die **`.txt`**-Variante funktioniert mit jeder Pi-hole-Version. Pi-hole v6 versteht auch
die `.adblock.txt`-Variante, die zusätzlich Subdomains sperrt.

### Welches Format?

| Datei | Syntax | Wirkung |
|---|---|---|
| `*.txt` | `example.com` | reine Domainliste; bei Pi-hole wird nur genau diese Domain gesperrt |
| `*.adblock.txt` | `\|\|example.com^` | sperrt die Domain **inklusive aller Subdomains** |

Viele Quellen, etwa HaGeZi, OISD und die Adblock-Listen, sind als Wildcard-Listen gedacht. Für AdGuard Home
ist deshalb `.adblock.txt` die beste Wahl.

## Wie es funktioniert

```
sources.toml ──► scripts/build.py ──► Repository (main)
                 │ Download (parallel, 3 Versuche)       ├─ lists/<kategorie>/<id>.txt
                 │ Formaterkennung: hosts / Domains /    ├─ combined/<kategorie>.txt
                 │   Adblock / Wildcard / URLs / dnsmasq ├─ combined/<kategorie>.adblock.txt
                 │ Normalisierung + Validierung          ├─ stats.json
                 │ Ausnahmen (@@) & allowlist.txt        └─ STATUS.md
                 └ Deduplizierung
```

- **Ausfallsicherheit:** Ist eine Quelle nicht erreichbar oder liefert sie plötzlich weniger als 50 % der
  bisherigen Einträge, wird die zuletzt erfolgreich gebaute Version weiterverwendet. Im
  [STATUS.md](STATUS.md) ist sie dann mit ⚠️ markiert.
- **Alles im Repo:** Die generierten Listen liegen direkt in [`combined/`](combined) und [`lists/`](lists)
  auf `main` und werden vom Workflow automatisch committet, sobald sich etwas ändert.
- **GitHub-Dateilimit:** Dateien über 95 MB werden automatisch in `*.part1.txt`, `*.part2.txt`, … aufgeteilt.

### Lokal bauen

```bash
python scripts/build.py              # alle Kategorien → combined/ und lists/
python scripts/build.py --only ads   # nur bestimmte Kategorien
```

Benötigt nur Python ≥ 3.11, keine zusätzlichen Pakete.

### Quelle hinzufügen

In `sources.toml` einen Block in der passenden Kategorie ergänzen:

```toml
[[categories.ads.sources]]
id = "meine-liste"
name = "Meine Liste"
url = "https://example.com/hosts.txt"
homepage = "https://example.com"
```

Eine neue Kategorie entsteht durch einen neuen `[categories.<id>]`-Block mit `title` und `description`.
Nach einem Push auf `main` startet der Build automatisch.

### False Positives

Domains in [`allowlist.txt`](allowlist.txt) werden aus **allen** Listen entfernt.

## Quellen & Lizenzen

Dieses Projekt erstellt keine eigenen Sperreinträge, sondern fasst die Arbeit der folgenden Projekte
zusammen. Vielen Dank an alle Maintainer:

[HaGeZi](https://github.com/hagezi/dns-blocklists) ·
[OISD](https://oisd.nl) ·
[StevenBlack](https://github.com/StevenBlack/hosts) ·
[AdGuard](https://github.com/AdguardTeam/AdGuardSDNSFilter) ·
[Firebog / WaLLy3K](https://firebog.net) ·
[The Block List Project](https://github.com/blocklistproject/Lists) ·
[ShadowWhisperer](https://github.com/ShadowWhisperer/BlockLists) ·
[Lightswitch05](https://github.com/lightswitch05/hosts) ·
[Perflyst](https://github.com/Perflyst/PiHoleBlocklist) ·
[Dandelion Sprout](https://github.com/DandelionSprout/adfilt) ·
[malware-filter](https://gitlab.com/malware-filter) ·
[Phishing.Database](https://github.com/mitchellkrogza/Phishing.Database) ·
[jarelllama](https://github.com/jarelllama/Scam-Blocklist) ·
[Sinfonietta](https://github.com/Sinfonietta/hostfiles) ·
[AdAway](https://adaway.org) ·
[Peter Lowe](https://pgl.yoyo.org/adservers/) ·
[Dan Pollock](https://someonewhocares.org/hosts/) ·
[hBlock](https://github.com/hectorm/hblock) ·
[WindowsSpyBlocker](https://github.com/crazy-max/WindowsSpyBlocker) ·
[Frogeye](https://hostfiles.frogeye.fr) ·
[Disconnect](https://disconnect.me) ·
[OpenPhish](https://openphish.com) ·
und weitere, siehe [`sources.toml`](sources.toml).

Jede Liste unterliegt der Lizenz ihres Urhebers (u. a. GPL-3.0, MIT, CC BY-SA, Unlicense; einige nur
für die nicht-kommerzielle Nutzung). Die Einzel- und Gesamtlisten nennen in ihrem Kopf jeweils die
Quellen. Der Code dieses Repositories (Build-Skript, Workflow) steht unter der [MIT-Lizenz](LICENSE).
