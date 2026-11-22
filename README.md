# AllBlock

Alle bekannten DNS-Blocklisten für **AdGuard Home** und **Pi-hole**, nach Kategorien sortiert und dedupliziert.

Stand: **22.11.2026 19:13 UTC** · 99 Quellen · **8,298,571** eindeutige Domains

> **AdGuard Home:** Link der Adblock-Liste kopieren → *Filter → DNS-Sperrlisten → Sperrliste hinzufügen*  
> **Pi-hole:** Link der Domain-Liste kopieren → *Lists / Adlists* → danach `pihole -g`

## Gesamtlisten pro Kategorie

Alle Quellen einer Kategorie zusammengefasst, ohne doppelte Einträge.

| Kategorie | Domains | Domain-Liste | Adblock-Liste |
|---|---:|---|---|
| **Werbung** | 997,268 | [ads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/ads.txt) | [ads.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/ads.adblock.txt) |
| **Tracking & Telemetrie** | 378,857 | [tracking.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/tracking.txt) | [tracking.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/tracking.adblock.txt) |
| **Malware & Threat Intelligence** | 4,376,766 | [malware.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/malware.txt) | [malware.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/malware.adblock.txt) |
| **Phishing** | 730,676 | [phishing.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/phishing.txt) | [phishing.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/phishing.adblock.txt) |
| **Scam & Betrug** | 889,279 | [scam.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/scam.txt) | [scam.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/scam.adblock.txt) |
| **Cryptomining** | 12,062 | [cryptomining.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/cryptomining.txt) | [cryptomining.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/cryptomining.adblock.txt) |
| **Erwachseneninhalte** | 1,183,869 | [adult.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/adult.txt) | [adult.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/adult.adblock.txt) |
| **Glücksspiel** | 733,180 | [gambling.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/gambling.txt) | [gambling.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/gambling.adblock.txt) |
| **Social Media** | 35,899 | [social.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/social.txt) | [social.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/social.adblock.txt) |
| **Fake News** | 2,194 | [fakenews.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/fakenews.txt) | [fakenews.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/fakenews.adblock.txt) |
| **Piraterie & Torrents** | 67,669 | [piracy.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/piracy.txt) | [piracy.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/piracy.adblock.txt) |
| **DoH / VPN / Proxy-Bypass** | 17,152 | [bypass.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/bypass.txt) | [bypass.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/bypass.adblock.txt) |
| **All-in-One** | 727,357 | [multi.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/multi.txt) | [multi.adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/combined/multi.adblock.txt) |

## Einzelne Quellen

Jede Quelle als eigene, bereinigte Liste. *Original* verweist auf die Liste des Urhebers.

### Werbung

Werbe-Server, Ad-Networks, Pop-ups, mobile Werbung

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [AdGuard DNS filter](https://github.com/AdguardTeam/AdGuardSDNSFilter) | 191,606 | [adguard-dns-filter.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/adguard-dns-filter.txt) | [Original](https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt) |
| [AdAway default blocklist](https://adaway.org) | 6,540 | [adaway.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/adaway.txt) | [Original](https://adaway.org/hosts.txt) |
| [Peter Lowe's Ad and tracking server list](https://pgl.yoyo.org/adservers/) | 3,554 | [peter-lowe.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/peter-lowe.txt) | [Original](https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext) |
| [EasyList (Firebog Pi-hole-Format)](https://firebog.net) | 51,631 | [firebog-easylist.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/firebog-easylist.txt) | [Original](https://v.firebog.net/hosts/Easylist.txt) |
| [Admiral anti-adblock (Firebog)](https://firebog.net) | 1,653 | [firebog-admiral.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/firebog-admiral.txt) | [Original](https://v.firebog.net/hosts/Admiral.txt) |
| [Fabrice Prigent – Ads (Firebog)](https://firebog.net) | 4,269 | [firebog-prigent-ads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/firebog-prigent-ads.txt) | [Original](https://v.firebog.net/hosts/Prigent-Ads.txt) |
| [anudeepND adservers](https://github.com/anudeepND/blacklist) | 42,358 | [anudeep-adservers.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/anudeep-adservers.txt) | [Original](https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt) |
| [FadeMind UncheckyAds](https://github.com/FadeMind/hosts.extras) | 9 | [unchecky-ads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/unchecky-ads.txt) | [Original](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts) |
| [Dan Pollock's hosts (someonewhocares)](https://someonewhocares.org/hosts/) | 13,090 | [someonewhocares.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/someonewhocares.txt) | [Original](https://someonewhocares.org/hosts/zero/hosts) |
| [MVPS HOSTS](https://winhelp2002.mvps.org) | 8,730 | [mvps.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/mvps.txt) | [Original](https://winhelp2002.mvps.org/hosts.txt) |
| [AdGuard Mobile Ads (r-a-y)](https://github.com/r-a-y/mobile-hosts) | 936 | [adguard-mobile-ads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/adguard-mobile-ads.txt) | [Original](https://raw.githubusercontent.com/r-a-y/mobile-hosts/master/AdguardMobileAds.txt) |
| [Lightswitch05 Ads & Tracking Extended](https://github.com/lightswitch05/hosts) | 429,282 | [developerdan-ads-tracking.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/developerdan-ads-tracking.txt) | [Original](https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt) |
| [ShadowWhisperer Ads](https://github.com/ShadowWhisperer/BlockLists) | 30,004 | [shadowwhisperer-ads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/shadowwhisperer-ads.txt) | [Original](https://raw.githubusercontent.com/ShadowWhisperer/BlockLists/master/Lists/Ads) |
| [Dandelion Sprout Game Console Adblock List](https://github.com/DandelionSprout/adfilt) | 16 | [game-console-adblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/game-console-adblock.txt) | [Original](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/GameConsoleAdblockList.txt) |
| [HaGeZi Pop-Up Ads](https://github.com/hagezi/dns-blocklists) | 73,234 | [hagezi-popupads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/hagezi-popupads.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/popupads.txt) |
| [Disconnect.me Ads](https://disconnect.me) | 2,700 | [disconnect-ads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/disconnect-ads.txt) | [Original](https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt) |
| [The Block List Project – Ads](https://github.com/blocklistproject/Lists) | 235,897 | [blocklistproject-ads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/blocklistproject-ads.txt) | [Original](https://blocklistproject.github.io/Lists/ads.txt) |
| [GoodbyeAds](https://github.com/jerryn70/GoodbyeAds) | 277,774 | [goodbyeads.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/ads/goodbyeads.txt) | [Original](https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds.txt) |

### Tracking & Telemetrie

Tracker, Analytics, Session-Replay, Geräte-/Betriebssystem-Telemetrie

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [EasyPrivacy (Firebog)](https://firebog.net) | 43,263 | [firebog-easyprivacy.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/firebog-easyprivacy.txt) | [Original](https://v.firebog.net/hosts/Easyprivacy.txt) |
| [FadeMind add.2o7Net](https://github.com/FadeMind/hosts.extras) | 2,030 | [fademind-2o7net.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/fademind-2o7net.txt) | [Original](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts) |
| [Frogeye First-Party Trackers](https://hostfiles.frogeye.fr) | 15,175 | [frogeye-firstparty.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/frogeye-firstparty.txt) | [Original](https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt) |
| [WindowsSpyBlocker – spy](https://github.com/crazy-max/WindowsSpyBlocker) | 347 | [windowsspyblocker.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/windowsspyblocker.txt) | [Original](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt) |
| [Perflyst SmartTV](https://github.com/Perflyst/PiHoleBlocklist) | 498 | [perflyst-smarttv.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/perflyst-smarttv.txt) | [Original](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt) |
| [Perflyst Android Tracking](https://github.com/Perflyst/PiHoleBlocklist) | 80 | [perflyst-android.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/perflyst-android.txt) | [Original](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt) |
| [Perflyst Amazon Fire TV](https://github.com/Perflyst/PiHoleBlocklist) | 16 | [perflyst-firetv.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/perflyst-firetv.txt) | [Original](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt) |
| [Perflyst Session Replay](https://github.com/Perflyst/PiHoleBlocklist) | 24 | [perflyst-sessionreplay.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/perflyst-sessionreplay.txt) | [Original](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SessionReplay.txt) |
| [ShadowWhisperer Tracking](https://github.com/ShadowWhisperer/BlockLists) | 134,219 | [shadowwhisperer-tracking.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/shadowwhisperer-tracking.txt) | [Original](https://raw.githubusercontent.com/ShadowWhisperer/BlockLists/master/Lists/Tracking) |
| [Disconnect.me Tracking](https://disconnect.me) | 34 | [disconnect-tracking.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/disconnect-tracking.txt) | [Original](https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt) |
| [Lightswitch05 Tracking Aggressive](https://github.com/lightswitch05/hosts) | 171,820 | [developerdan-tracking-aggressive.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/developerdan-tracking-aggressive.txt) | [Original](https://www.github.developerdan.com/hosts/lists/tracking-aggressive-extended.txt) |
| [The Block List Project – Tracking](https://github.com/blocklistproject/Lists) | 143,876 | [blocklistproject-tracking.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/blocklistproject-tracking.txt) | [Original](https://blocklistproject.github.io/Lists/tracking.txt) |
| [The Block List Project – Smart TV](https://github.com/blocklistproject/Lists) | 77 | [blocklistproject-smarttv.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/blocklistproject-smarttv.txt) | [Original](https://blocklistproject.github.io/Lists/smart-tv.txt) |
| [HaGeZi Native Tracker – Windows/Office](https://github.com/hagezi/dns-blocklists) | 395 | [hagezi-native-windows.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-windows.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.winoffice.txt) |
| [HaGeZi Native Tracker – Apple](https://github.com/hagezi/dns-blocklists) | 105 | [hagezi-native-apple.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-apple.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.apple.txt) |
| [HaGeZi Native Tracker – Amazon](https://github.com/hagezi/dns-blocklists) | 380 | [hagezi-native-amazon.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-amazon.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.amazon.txt) |
| [HaGeZi Native Tracker – Samsung](https://github.com/hagezi/dns-blocklists) | 201 | [hagezi-native-samsung.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-samsung.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.samsung.txt) |
| [HaGeZi Native Tracker – Xiaomi](https://github.com/hagezi/dns-blocklists) | 411 | [hagezi-native-xiaomi.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-xiaomi.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.xiaomi.txt) |
| [HaGeZi Native Tracker – Huawei](https://github.com/hagezi/dns-blocklists) | 148 | [hagezi-native-huawei.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-huawei.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.huawei.txt) |
| [HaGeZi Native Tracker – LG webOS](https://github.com/hagezi/dns-blocklists) | 461 | [hagezi-native-lgwebos.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-lgwebos.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.lgwebos.txt) |
| [HaGeZi Native Tracker – TikTok](https://github.com/hagezi/dns-blocklists) | 553 | [hagezi-native-tiktok.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-tiktok.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.tiktok.txt) |
| [HaGeZi Native Tracker – Roku](https://github.com/hagezi/dns-blocklists) | 64 | [hagezi-native-roku.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-roku.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.roku.txt) |
| [HaGeZi Native Tracker – Vivo](https://github.com/hagezi/dns-blocklists) | 302 | [hagezi-native-vivo.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-vivo.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.vivo.txt) |
| [HaGeZi Native Tracker – OPPO/Realme](https://github.com/hagezi/dns-blocklists) | 532 | [hagezi-native-oppo-realme.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/tracking/hagezi-native-oppo-realme.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/native.oppo-realme.txt) |

### Malware & Threat Intelligence

Malware-Verteilung, C2-Server, Ransomware, Stalkerware, Malvertising

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [malware-filter URLhaus Filter](https://gitlab.com/malware-filter/urlhaus-filter) | 2,167 | [urlhaus-filter.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/urlhaus-filter.txt) | [Original](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-hosts.txt) |
| [HaGeZi Threat Intelligence Feeds](https://github.com/hagezi/dns-blocklists) | 1,979,852 | [hagezi-tif.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/hagezi-tif.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/tif.txt) |
| [Dandelion Sprout Anti-Malware List](https://github.com/DandelionSprout/adfilt) | 11,686 | [dandelion-antimalware.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/dandelion-antimalware.txt) | [Original](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt) |
| [Fabrice Prigent – Malware (Firebog)](https://firebog.net) | 239,641 | [firebog-prigent-malware.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/firebog-prigent-malware.txt) | [Original](https://v.firebog.net/hosts/Prigent-Malware.txt) |
| [RPiList Malware (Firebog)](https://firebog.net) | 761,609 | [firebog-rpilist-malware.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/firebog-rpilist-malware.txt) | [Original](https://v.firebog.net/hosts/RPiList-Malware.txt) |
| [FadeMind add.Risk](https://github.com/FadeMind/hosts.extras) | 2,189 | [fademind-risk.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/fademind-risk.txt) | [Original](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts) |
| [Disconnect.me Malvertising](https://disconnect.me) | 2,735 | [disconnect-malvertising.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/disconnect-malvertising.txt) | [Original](https://s3.amazonaws.com/lists.disconnect.me/simple_malvertising.txt) |
| [Echap Stalkerware Indicators](https://github.com/AssoEchap/stalkerware-indicators) | 929 | [stalkerware.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/stalkerware.txt) | [Original](https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts) |
| [ShadowWhisperer Malware](https://github.com/ShadowWhisperer/BlockLists) | 29,527 | [shadowwhisperer-malware.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/shadowwhisperer-malware.txt) | [Original](https://raw.githubusercontent.com/ShadowWhisperer/BlockLists/master/Lists/Malware) |
| [The Block List Project – Malware](https://github.com/blocklistproject/Lists) | 2,655,820 | [blocklistproject-malware.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/blocklistproject-malware.txt) | [Original](https://blocklistproject.github.io/Lists/malware.txt) |
| [The Block List Project – Ransomware](https://github.com/blocklistproject/Lists) | 1,904 | [blocklistproject-ransomware.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/blocklistproject-ransomware.txt) | [Original](https://blocklistproject.github.io/Lists/ransomware.txt) |
| [The Block List Project – Abuse](https://github.com/blocklistproject/Lists) | 435,106 | [blocklistproject-abuse.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/malware/blocklistproject-abuse.txt) | [Original](https://blocklistproject.github.io/Lists/abuse.txt) |

### Phishing

Phishing-Seiten und Credential-Harvesting

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [malware-filter Phishing Filter](https://gitlab.com/malware-filter/phishing-filter) | 16,602 | [phishing-filter.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/phishing/phishing-filter.txt) | [Original](https://malware-filter.gitlab.io/malware-filter/phishing-filter-hosts.txt) |
| [Phishing.Database – aktive Domains](https://github.com/mitchellkrogza/Phishing.Database) | 386,608 | [phishing-database-active.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/phishing/phishing-database-active.txt) | [Original](https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-domains-ACTIVE.txt) |
| [OpenPhish Community Feed](https://openphish.com) | 276 | [openphish.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/phishing/openphish.txt) | [Original](https://openphish.com/feed.txt) |
| [RPiList Phishing (Firebog)](https://firebog.net) | 153,858 | [firebog-rpilist-phishing.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/phishing/firebog-rpilist-phishing.txt) | [Original](https://v.firebog.net/hosts/RPiList-Phishing.txt) |
| [The Block List Project – Phishing](https://github.com/blocklistproject/Lists) | 190,193 | [blocklistproject-phishing.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/phishing/blocklistproject-phishing.txt) | [Original](https://blocklistproject.github.io/Lists/phishing.txt) |

### Scam & Betrug

Fake-Shops, Betrugsseiten, Spam, Redirect-Fallen

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [HaGeZi Fake (Fake-Shops, Scam)](https://github.com/hagezi/dns-blocklists) | 10,774 | [hagezi-fake.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/scam/hagezi-fake.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/fake.txt) |
| [Spam404](https://github.com/Spam404/lists) | 8,140 | [spam404.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/scam/spam404.txt) | [Original](https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt) |
| [durablenapkin Scam Blocklist](https://github.com/durablenapkin/scamblocklist) | 2,127 | [durablenapkin-scam.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/scam/durablenapkin-scam.txt) | [Original](https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/hosts.txt) |
| [jarelllama Scam Blocklist](https://github.com/jarelllama/Scam-Blocklist) | 468,729 | [jarelllama-scam.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/scam/jarelllama-scam.txt) | [Original](https://raw.githubusercontent.com/jarelllama/Scam-Blocklist/main/lists/wildcard_domains/scams.txt) |
| [ShadowWhisperer Scam](https://github.com/ShadowWhisperer/BlockLists) | 6,185 | [shadowwhisperer-scam.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/scam/shadowwhisperer-scam.txt) | [Original](https://raw.githubusercontent.com/ShadowWhisperer/BlockLists/master/Lists/Scam) |
| [The Block List Project – Scam](https://github.com/blocklistproject/Lists) | 8,527 | [blocklistproject-scam.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/scam/blocklistproject-scam.txt) | [Original](https://blocklistproject.github.io/Lists/scam.txt) |
| [The Block List Project – Fraud](https://github.com/blocklistproject/Lists) | 285,200 | [blocklistproject-fraud.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/scam/blocklistproject-fraud.txt) | [Original](https://blocklistproject.github.io/Lists/fraud.txt) |
| [The Block List Project – Redirect](https://github.com/blocklistproject/Lists) | 108,685 | [blocklistproject-redirect.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/scam/blocklistproject-redirect.txt) | [Original](https://blocklistproject.github.io/Lists/redirect.txt) |

### Cryptomining

Browser-Miner und Cryptojacking

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list) | 312 | [nocoin.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/cryptomining/nocoin.txt) | [Original](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt) |
| [Fabrice Prigent – Crypto (Firebog)](https://firebog.net) | 11,490 | [firebog-prigent-crypto.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/cryptomining/firebog-prigent-crypto.txt) | [Original](https://v.firebog.net/hosts/Prigent-Crypto.txt) |
| [The Block List Project – Crypto](https://github.com/blocklistproject/Lists) | 1,274 | [blocklistproject-crypto.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/cryptomining/blocklistproject-crypto.txt) | [Original](https://blocklistproject.github.io/Lists/crypto.txt) |

### Erwachseneninhalte

Pornografie und NSFW-Inhalte

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [HaGeZi NSFW](https://github.com/hagezi/dns-blocklists) | 87,389 | [hagezi-nsfw.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/adult/hagezi-nsfw.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/nsfw.txt) |
| [OISD NSFW](https://oisd.nl) | 498,523 | [oisd-nsfw.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/adult/oisd-nsfw.txt) | [Original](https://nsfw.oisd.nl/domainswild) |
| [Sinfonietta pornography-hosts](https://github.com/Sinfonietta/hostfiles) | 61,154 | [sinfonietta-porn.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/adult/sinfonietta-porn.txt) | [Original](https://raw.githubusercontent.com/Sinfonietta/hostfiles/master/pornography-hosts) |
| [StevenBlack Extension – Porn](https://github.com/StevenBlack/hosts) | 76,810 | [stevenblack-porn.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/adult/stevenblack-porn.txt) | [Original](https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn-only/hosts) |
| [chadmayfield Porn Top 1M](https://github.com/chadmayfield/my-pihole-blocklists) | 11,868 | [chadmayfield-porn.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/adult/chadmayfield-porn.txt) | [Original](https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list) |
| [ShadowWhisperer Adult](https://github.com/ShadowWhisperer/BlockLists) | 213,982 | [shadowwhisperer-adult.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/adult/shadowwhisperer-adult.txt) | [Original](https://raw.githubusercontent.com/ShadowWhisperer/BlockLists/master/Lists/Adult) |
| [The Block List Project – Porn](https://github.com/blocklistproject/Lists) | 953,393 | [blocklistproject-porn.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/adult/blocklistproject-porn.txt) | [Original](https://blocklistproject.github.io/Lists/porn.txt) |

### Glücksspiel

Online-Casinos, Sportwetten, Glücksspiel

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [HaGeZi Gambling](https://github.com/hagezi/dns-blocklists) | 710,363 | [hagezi-gambling.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/gambling/hagezi-gambling.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/gambling.txt) |
| [Sinfonietta gambling-hosts](https://github.com/Sinfonietta/hostfiles) | 2,690 | [sinfonietta-gambling.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/gambling/sinfonietta-gambling.txt) | [Original](https://raw.githubusercontent.com/Sinfonietta/hostfiles/master/gambling-hosts) |
| [StevenBlack Extension – Gambling](https://github.com/StevenBlack/hosts) | 6,744 | [stevenblack-gambling.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/gambling/stevenblack-gambling.txt) | [Original](https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-only/hosts) |
| [The Block List Project – Gambling](https://github.com/blocklistproject/Lists) | 342,623 | [blocklistproject-gambling.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/gambling/blocklistproject-gambling.txt) | [Original](https://blocklistproject.github.io/Lists/gambling.txt) |

### Social Media

Soziale Netzwerke (Facebook, Instagram, TikTok, X, …)

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [HaGeZi Social Networks](https://github.com/hagezi/dns-blocklists) | 8,336 | [hagezi-social.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/social/hagezi-social.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/social.txt) |
| [Sinfonietta social-hosts](https://github.com/Sinfonietta/hostfiles) | 3,808 | [sinfonietta-social.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/social/sinfonietta-social.txt) | [Original](https://raw.githubusercontent.com/Sinfonietta/hostfiles/master/social-hosts) |
| [StevenBlack Extension – Social](https://github.com/StevenBlack/hosts) | 3,808 | [stevenblack-social.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/social/stevenblack-social.txt) | [Original](https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/social-only/hosts) |
| [The Block List Project – Facebook](https://github.com/blocklistproject/Lists) | 22,362 | [blocklistproject-facebook.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/social/blocklistproject-facebook.txt) | [Original](https://blocklistproject.github.io/Lists/facebook.txt) |
| [The Block List Project – TikTok](https://github.com/blocklistproject/Lists) | 3,725 | [blocklistproject-tiktok.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/social/blocklistproject-tiktok.txt) | [Original](https://blocklistproject.github.io/Lists/tiktok.txt) |

### Fake News

Bekannte Desinformations- und Fake-News-Seiten

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [StevenBlack Extension – Fakenews](https://github.com/StevenBlack/hosts) | 2,187 | [stevenblack-fakenews.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/fakenews/stevenblack-fakenews.txt) | [Original](https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-only/hosts) |
| [marktron fakenews](https://github.com/marktron/fakenews) | 2,194 | [marktron-fakenews.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/fakenews/marktron-fakenews.txt) | [Original](https://raw.githubusercontent.com/marktron/fakenews/master/fakenews) |

### Piraterie & Torrents

Warez-, Streaming- und Torrent-Seiten

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [HaGeZi Anti-Piracy](https://github.com/hagezi/dns-blocklists) | 64,647 | [hagezi-anti-piracy.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/piracy/hagezi-anti-piracy.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/anti.piracy.txt) |
| [The Block List Project – Piracy](https://github.com/blocklistproject/Lists) | 2,154 | [blocklistproject-piracy.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/piracy/blocklistproject-piracy.txt) | [Original](https://blocklistproject.github.io/Lists/piracy.txt) |
| [The Block List Project – Torrent](https://github.com/blocklistproject/Lists) | 2,620 | [blocklistproject-torrent.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/piracy/blocklistproject-torrent.txt) | [Original](https://blocklistproject.github.io/Lists/torrent.txt) |

### DoH / VPN / Proxy-Bypass

Verhindert das Umgehen des DNS-Filters über DoH-Resolver, VPNs, Proxies

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [HaGeZi DoH/VPN/TOR/Proxy Bypass](https://github.com/hagezi/dns-blocklists) | 16,720 | [hagezi-doh-vpn-proxy.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/bypass/hagezi-doh-vpn-proxy.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/doh-vpn-proxy-bypass.txt) |
| [HaGeZi Encrypted DNS Servers](https://github.com/hagezi/dns-blocklists) | 3,569 | [hagezi-doh.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/bypass/hagezi-doh.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/doh.txt) |
| [dibdot DoH Domains](https://github.com/dibdot/DoH-IP-blocklists) | 1,422 | [dibdot-doh.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/bypass/dibdot-doh.txt) | [Original](https://raw.githubusercontent.com/dibdot/DoH-IP-blocklists/master/doh-domains.txt) |

### All-in-One

Große kuratierte Kombi-Listen (Werbung + Tracking + Malware)

| Quelle | Domains | Download | Original |
|---|---:|---|---|
| [StevenBlack Unified Hosts](https://github.com/StevenBlack/hosts) | 76,103 | [stevenblack-unified.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/multi/stevenblack-unified.txt) | [Original](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts) |
| [OISD Big](https://oisd.nl) | 220,281 | [oisd-big.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/multi/oisd-big.txt) | [Original](https://big.oisd.nl/domainswild) |
| [HaGeZi Multi PRO](https://github.com/hagezi/dns-blocklists) | 242,058 | [hagezi-pro.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/multi/hagezi-pro.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/pro.txt) |
| [HaGeZi Multi ULTIMATE](https://github.com/hagezi/dns-blocklists) | 285,120 | [hagezi-ultimate.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/multi/hagezi-ultimate.txt) | [Original](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/ultimate.txt) |
| [hBlock](https://github.com/hectorm/hblock) | 485,383 | [hblock.txt](https://raw.githubusercontent.com/AndersEben/AllBlock/main/lists/multi/hblock.txt) | [Original](https://hblock.molinero.dev/hosts_domains.txt) |

---


Jede Liste unterliegt der Lizenz ihres Urhebers. Automatisch aktualisiert, 2× täglich.
