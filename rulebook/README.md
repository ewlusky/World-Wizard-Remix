# Rulebook

This is the **v2.2.1 baseline**, ported here on 2026-08-09 from the family edition where the game actually gets played.

It is deliberately *not* yet the published edition. The divergences that make this a separate game — a longer Age ladder, a per-turn AP pool, the hidden Age end, the Kith layer, LANGUAGE as its own action family — are tracked in [`../design/DESIGN-DIRECTION.md`](../design/DESIGN-DIRECTION.md) and get applied here one at a time, each with a changelog entry. Porting the working text first means every future change is a visible diff against something that has been played, instead of a rewrite from memory.

Two things were changed in the port, both deliberate:

- **World-neutral.** The family edition's examples referenced its own setting. The published game ships no preset world, so examples here are generic.
- **Name-free.** The source carried designer's notes addressed to specific people. Those are private and were not brought across.

## Contents

| File | What's in it |
|---|---|
| [01-how-to-play.md](01-how-to-play.md) | The one-minute rules, and how a turn actually works at the table (including the wheel) |
| [03-the-ap-economy.md](03-the-ap-economy.md) | AP, the Price of Passing, Complicate, the Weave Bonus, the Quiet Turn. **Applies in every Age.** |
| [04-reference.md](04-reference.md) | Stewardship, Development Levels, Alignment, War, Deeds, Currents and Nexuses |
| [05-ending-an-age.md](05-ending-an-age.md) | The Survival Round and what happens to magic between Ages |
| [06-log-sheet.md](06-log-sheet.md) | Blank tables for recording play |

**The four Ages**, each with its own action list:

| Age | AP | Tally | File |
|---|---|---|---|
| I. Primordial | 1d6 + 3 | 16 | [07-age-i-primordial.md](07-age-i-primordial.md) |
| II. Prehistoric | 2d6 | 14 | [02-actions.md](02-actions.md) |
| III. Ancient | 2d6 | 12 | [08-age-iii-ancient.md](08-age-iii-ancient.md) |
| IV. Present | 2d6 | 10 | [09-age-iv-present.md](09-age-iv-present.md) |

Age II keeps the filename `02-actions.md` because it is the most fully developed Age and the pattern the others were refactored to match.

Random-generation content lives in [`../tables/`](../tables/) — 15 tables, 100 entries each. The constructed languages live in [`../languages/`](../languages/).

## The Ages, as of the baseline

Four Ages. Roll AP once per Age and spend it across that whole Age.

| Age | Your AP | Tally | What happens |
|---|---|---|---|
| I. Primordial | 1d6 + 3 | 16 | Geography forms, magic sources appear |
| II. Prehistoric | 2d6 | 14 | Peoples emerge, legends begin |
| III. Ancient | 2d6 | 12 | Civilizations rise, magic institutionalized |
| IV. Present | 2d6 | 10 | Recent history, the stage is set |

**All four Ages are ported.** Ages I, III and IV were restructured into the icon families used in Age II — the refactor the family edition's own design notes proposed and never got to. No action, cost, or effect was changed in doing it; the grouping is the only difference.

Rolling content lives in [`../tables/`](../tables/): fifteen d100 tables plus [supplementary](../tables/supplementary.md) for the action-specific rolls (Spark Domains, Beyond the Veil, Disaster Scope, the faction generator, magical anomalies and catastrophes). Constructed languages are in [`../languages/`](../languages/).
