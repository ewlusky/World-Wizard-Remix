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

### Still missing
- Age-specific action tables for Ages I, III and IV. The port covers the Prehistoric Age, which is the most developed in the source and the pattern the others were being refactored toward.

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
