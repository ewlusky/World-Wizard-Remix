# World Wizard Remix

A collaborative, Age-structured worldbuilding game for 2–7 players. No GM. No preset world. Just a hex map, some index cards, and the accumulated weight of everything your group has made — and broken.

> *You are a Steward. Not a character. Not a Game Master. A caretaker of a world in progress.*

**Status:** rules complete, unplaytested in this form. Public as a design track, not a finished game.

---

## ⚠️ Attribution, up front

**This is a hack of [Worldwizard](https://lampblack-brimstone.itch.io/worldwizard) by Jason Lutes, published by [Lampblack & Brimstone](https://lampblack-brimstone.itch.io/).** The Steward role, the hex map, the Action Point economy, and the Age progression all come from their game. **Go buy it — it's $5 on itch.io.**

Worldwizard is itself built on *Dawn of Worlds* by N. Bob Pesall, which it credits. This is a hack of a hack, which is how this corner of the hobby has always worked.

"Remix" is in the title because that is the established convention for a declared hack: it puts the derivative status where nobody has to go looking for it. Full accounting of what came from where is in [CREDITS.md](CREDITS.md). Lampblack & Brimstone have not endorsed this and are not affiliated with it.

---

## What this is for

The original solves worldbuilding for people who showed up wanting to worldbuild. This variant was built for a table where not everyone did — where the blank map plus "invent something" was the obstacle rather than the invitation.

Most of what has been added exists to serve that: the wheel, the right to skip a turn, the Quiet Turn, and a table of a hundred entries behind every prompt. The reasoning is in [ADR-001](design/ADR-001-the-low-barrier-turn.md), and it is the load-bearing idea in the whole design.

## How to navigate

**Start here:** [`print/player-reference.md`](print/player-reference.md) is the entire game on one sheet.

| Folder | What's in it |
|---|---|
| [`rulebook/`](rulebook/) | The rules. All four Ages, the AP economy, Language, reference, log sheet |
| [`tables/`](tables/) | **15 tables × 100 entries**, plus [supplementary](tables/supplementary.md) rolls and [the wheel mapping](tables/WHEEL.md) |
| [`languages/`](languages/) | **Twelve fully constructed tongues** — phonology, grammar, names, vocabulary, phrases, idioms |
| [`print/`](print/) | The one-page reference and four printable wheel sheets |
| [`design/`](design/) | Direction, open questions, and decision records |
| [`playtest/`](playtest/) | What to test first, and what to watch for |
| [`reference/`](reference/) | Notes on games researched during design |

## Core concept

Players take turns spending Action Points to shape land, birth peoples, invoke magic, name each other's creations, or complicate their own. The world grows across Ages, each closer in than the last — a millennium is nothing in Age I; by the final Age a season changes everything.

The map is a first-class game object. It accumulates weight. Things that fade leave marks. Words outlive the people who coined them, and a name stays spelled the way it was first written even after nobody says it that way.

## What is settled, and what is not

**Settled:** the title and attribution. The [licence](LICENSE) — all rights reserved for now, deliberately, revisited when the game is playable end to end. That accessibility is a design pillar, not a nicety. That there is no simplified variant, because quarantining the gentle rules defeats them.

**Not settled:** whether it is six Ages or seven. Whether AP should be a per-turn pool instead of per-Age. Whether the wheel ships as a wheel, a card deck, or instructions. Whether the hidden Age-end, the Kith layer, and the other mechanics in [`design/DESIGN-DIRECTION.md`](design/DESIGN-DIRECTION.md) survive contact with a table.

Those need play, not more writing. See [`playtest/`](playtest/).

## Quick links

[Design direction](design/DESIGN-DIRECTION.md) · [Open questions](design/OPEN-QUESTIONS.md) · [ADR-001: the low-barrier turn](design/ADR-001-the-low-barrier-turn.md) · [Changelog](CHANGELOG.md)
