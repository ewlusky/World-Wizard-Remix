# Playtest

The rulebook is complete on paper and unproven at a table. Everything in here exists to find out which parts are actually wrong.

## What to test first

The rulebook is a faithful port of a ruleset built for four Ages and a per-Age AP pool. [`design/DESIGN-DIRECTION.md`](../design/DESIGN-DIRECTION.md) wants six or seven Ages and a per-turn pool instead. **Do not change either until a session has been played as written.** The point of porting the working version first was to have a baseline to measure against, and rewriting it from a hunch throws that away.

Two things are most likely to break, and both need a table rather than an argument:

1. **The AP economy.** 2d6 for a whole Age was tuned for four Ages and three players. Watch for anyone stuck at zero AP for more than two turns, or sitting on unspent AP at the Age's end.
2. **The Age ladder.** Whether Ancient and Present are distinct enough to be separate Ages, or whether the back half of the game wants more rungs.

## The observation that matters most

Per [ADR-001](../design/ADR-001-the-low-barrier-turn.md), the accessibility spine — 🎡 Spin, the right to skip, the Quiet Turn — is a design pillar. It cannot be tested by people who enjoy open creative prompts, because they will never exercise it.

**So watch the most hesitant player at the table.** Not the youngest, not the newest to games: whoever is least comfortable inventing something on demand while others wait. Specifically:

- Do they use the wheel? Do they use it *without* being prompted to?
- Does using it feel to them like the easy mode, or like a normal choice? Ask afterwards, in those words.
- Do they ever skip a turn? If they never do, is that because they never wanted to, or because it still felt like it needed a reason?
- Do they take Quiet Turns, and do they seem to count them as real turns?

If the hesitant player is engaged for the whole session and never once reached for any of the three, that is a finding — either they did not need them or the rules did not make them visible enough. Both are worth knowing.

A session where everyone had fun and nobody used the accessibility rules has **not** tested the accessibility rules.

## Per-session report

One file each, named `YYYY-MM-DD-age-[N]-session-[NN].md`.

Capture:

- **Table** — how many players, how many were new to the game, how many were new to worldbuilding at all
- **Age and turns played**
- **Spin vs Choose** — rough tally. Who used which, and did anyone switch as the session went on?
- **Quiet Turns and skips** — how many, by whom
- **AP** — anyone starved, anyone flush, anyone hoarding
- **What stalled** — the specific turn where things went slow, and what the player was stuck on
- **Mechanics that earned their place** — Complicate, Weave stars, Price of Passing, Gift a Name
- **Mechanics nobody touched** — equally important, and easier to miss
- **Rules looked up mid-play** — every lookup is a page that is not clear enough
- **Map state** — photograph it

## Notes on running one

The map wants to live somewhere people walk past, not somewhere a session gets convened. A game designed for drive-by turns will report differently if it is played as a scheduled sit-down, so record which you did.

There is no requirement that this be tested with the same group twice, or with any particular group at all. A single Age played with strangers online who have never met the map is a legitimate and probably more informative test than a full campaign with people who already know how it is supposed to go.
