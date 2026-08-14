# Changelog

All notable rule changes and design decisions are recorded here.

---

## [pre-alpha] — 2026-08-09

### Added
- **`tables/` — 15 tables, 100 entries each, 1,500 total.** Ported from the master document behind the printed binder, via a parser that walks the Word XML table structure so counts and cell boundaries are exact. Five tables split across page breaks in the source were merged back. Index and voice guide in `tables/README.md`.
- **`languages/` — the twelve constructed tongues**, one file each plus an index. Phonology, grammar rules, naming conventions, core vocabulary, phrases, idioms, and the real-world root inspiration per language.
- **`rulebook/` — the v2.2.1 baseline**, in six files: how to play, actions, the AP economy, reference, ending an Age, log sheet. Ported world-neutral and name-free.
- **`tables/WHEEL.md`** — the wheel's segment-to-table mapping and suggested per-Age segment sets.
- **`design/ADR-001-the-low-barrier-turn.md`** — records that lowering the barrier to taking a turn is a design pillar, and that the wheel, the right to skip, and the Quiet Turn are one system serving it.
- `.gitignore` for `_source/`, which holds the original paid Worldwizard PDFs. This repo is public; those must not be redistributed here.

### Changed
- `design/DESIGN-DIRECTION.md` gains the accessibility value as value 0, and the wheel as a key mechanic. It previously never mentioned the wheel at all, despite that being the mechanic a new player meets first.
- LANGUAGE is no longer described as content to be drafted. The twelve languages are finished; only the actions are missing, and they should be built to fit the languages rather than the reverse.

### Resolved
- **Family variant** question closed in favour of a single ruleset that scales. A quarantined "simplified" mode reintroduces the self-consciousness the accessibility rules exist to remove.

### Also added, same day — all four Ages now ported
- **`rulebook/07-age-i-primordial.md`**, **`08-age-iii-ancient.md`**, **`09-age-iv-present.md`**. Ages III and IV existed only in the older ruleset document, not in the vault. All three were restructured into the icon families used in Age II, which is the refactor the family edition's own design notes proposed and never got to. No action, cost, or effect changed; grouping is the only difference, and each file says so.
- **`tables/supplementary.md`** — the action-specific tables the main fifteen do not cover: Wellspring Types, Spark Domains, Beyond the Veil, **Disaster Scope**, the faction generator, magical anomalies, magical catastrophes. Disaster Scope matters most: the Price of Passing rolls it every time, and the rulebook was already linking to a table that did not exist here yet.
- Age II keeps the filename `02-actions.md` and gains its Age header, AP, Tally and cross-Age navigation.

The rulebook is now playable start to finish.

### Then, same day — the Language family, and things you can put on a table
- **`rulebook/10-language.md`** — 📜 LANGUAGE, the last undesigned action family, now written. Seven actions and the Compendium, available in every Age. Built to fit the twelve tongues that already existed rather than inventing a system and retrofitting them. Notable pieces: **Gift a Name** (name another Steward's creation in your tongue — the cheapest cooperative move in the game), **Sound-Shift leaves the old form on the map** because ink does not drift, and **Invent Writing permanently freezes a tongue**, trading change for permanence.
- **`print/`** — [player-reference.md](print/player-reference.md), the whole game on one sheet, plus **four printable wheel sheets** as SVG with per-Age segment sets, and `make-wheel.py` that generates them with no dependencies. The wheel has been the design's central mechanic all along with no artifact to show for it.
- **`playtest/README.md`** rewritten around what to actually test: play it as written before touching the AP economy or the Age ladder, and watch the most hesitant player at the table, because the accessibility spine cannot be tested by people who enjoy open creative prompts. A session where everyone had fun and nobody used those rules has not tested them.
- Root `README.md` rewritten — it still claimed the rename was pending and did not know `languages/` or `print/` existed.

### Resolved
- All four **Language** open questions: own family; a split forks the tongue and the old form stays on the map; writing freezes drift; and **no mechanical reward for speaking coined words aloud**, because paying players to perform taxes exactly the person ADR-001 protects.

---

## [pre-alpha] — 2026-04-19

### Added
- Initial repo scaffold forked from *The Unending Sea* family game v2.2.1
- Design direction captured in `design/DESIGN-DIRECTION.md`
- Open questions captured in `design/OPEN-QUESTIONS.md`
- Reference notes from game research (Dawn of Worlds, Microscope, The Quiet Year, Wanderhome, and others) in `reference/`

### Inherited from family game v2.2.1
- Core AP economy (2d6 per Age, Price of Passing, Weave Bonus ⭐)
- Action families: LAND / LIFE / MAGIC / COMPLICATE / OTHER
- Quiet Turn (free, no AP, no tally)
- Survival Round with "Fades get a final legendary act"
- Stewardship, War table with Invest, Currents/Nexuses

### Divergences from family game
- Ages: targeting 6–7 with logarithmic "Now" scaling (vs. 4 flat)
- AP economy: likely per-turn pool with anti-hoarding bonus (vs. per-Age 2d6)
- Age end: Frost Shepherds hidden countdown card (vs. tally-to-14 vote)
- Additional action families: LANGUAGE (TBD)
- Additional mechanics: Kith layer, Legacy Threads, Palette, Oracle's Handful, Holiday between Ages, Genus Loci, Pushing
