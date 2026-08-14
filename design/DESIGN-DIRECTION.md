# Design Direction

> *This document is the living spine of the WorldWizard publishable edition. It captures what we're building, why, and how it diverges from the family game. Update it when decisions are made; consult it before adding mechanics.*

---

## What kind of game this is

A collaborative worldbuilding game played across multiple sessions on a physical hex map. No GM. No pre-written world. Players are Stewards — each Steward owns their creations, shapes them over Ages, and watches them live or fade.

It lives in the genre of *Dawn of Worlds*, *Microscope*, *The Quiet Year*, and *Wanderhome* — but it has a different shape: longer, slower, more material (the physical map accumulates real history), and with a Language mechanic that gives Peoples voices that evolve and die.

---

## The core design values

0. **Taking a turn must be easy to start.** A blank map plus "invent something" is the hardest prompt in the game, and some players freeze in front of it. The wheel, the right to skip, and the Quiet Turn exist to narrow the first decision so the player gets to the enjoyable second one. This is listed first because it is the oldest value in the design and the one most likely to be optimized away by someone who cannot see what it holds up. See [ADR-001](ADR-001-the-low-barrier-turn.md).
1. **The map is canon.** Anything drawn on the map is real. The game's history lives in the physical artifact, not in notes.
2. **Mess is interesting.** The best mechanics are the ones that make creations *more complicated*, not more powerful. Complicate rewards trouble. Price of Passing rewards risk.
3. **Small things matter.** A named Kith (ordinary mortal) does more worldbuilding work than a thousand-year dynasty. Design for the ground level, not just the gods.
4. **Reserves are poetic.** Some mysteries should stay unresolved. Design rewards for *deepening* a mystery, not resolving it.
5. **The language of the world belongs to the world.** Players who coin words during play contribute to an in-world vocabulary that outlives individual Peoples.

---

## The Age structure

### Logarithmic scaling — the "Now" shrinks each Age

| Age | Name (working) | "Now" = one turn |
|-----|----------------|-----------------|
| I   | Primordial     | Eons |
| II  | Prehistoric    | Millennia |
| III | Ancient        | Centuries |
| IV  | Classical      | Generations |
| V   | Medieval       | Decades |
| VI  | Modern         | Years |
| VII | Current Day    | Seasons |

Actions must feel true to their Age's Now scale. An Age II action that plants a forest fits. An Age VI action that plants a forest is a Quiet Turn detail, not a full action.

**Open:** 6 Ages or 7? Whether to compress Classical/Medieval is a pacing question — needs playtesting.

---

## Action families

| Family | Icon | What it does |
|--------|------|--------------|
| LAND | 🌍 | Shape terrain, add or enchant features |
| LIFE | 🧬 | Birth peoples, create avatars, expand territory, deeds, group endeavors |
| MAGIC | ✨ | Invest Sparks, open Breaches, bind spirits |
| LANGUAGE | 📜 | Coin words, gift names, evolve speech, let a language die — **[written](../rulebook/10-language.md)** |
| COMPLICATE | 🪞 | Add a flaw/contradiction/mystery/rift/limitation/sorrow to your own creation for +1 AP |
| OTHER | 💥 | Pass (disaster on your own stuff for more AP), meta-actions |

COMPLICATE is promoted from "tucked into OTHER" in the family game to its own family here. It's one of the defining mechanics.

**✅ LANGUAGE is written** — see [`../rulebook/10-language.md`](../rulebook/10-language.md). Seven actions built to fit the twelve existing tongues in [`../languages/`](../languages/) rather than the reverse: Assign a Tongue, Coin a Word, Gift a Name, Sound-Shift, Take a Loanword, Invent Writing, Let a Tongue Die. Available in every Age, because language is the one thing that survives everything else.

Three pieces of it are load-bearing and should not be trimmed:

- **Gift a Name** lets you name *another Steward's* creation in your tongue. It is the cheapest cooperative action in the game and it writes contact between peoples directly onto the map.
- **Sound-Shift leaves the old form on the map.** Ink does not drift. A hex labelled in a form nobody says any more is free history and costs nothing to produce.
- **Writing freezes a tongue.** A written language can never Sound-Shift again. That is the trade: permanence for change. It also answers the writing-systems open question with a real mechanical consequence instead of a flavour note.

---

## Key mechanics to build

### 🎡 The Wheel (already built and played — needs a shipped form)
A physical spinner whose segments are table names. Spin it and it tells you *which table* to consult; roll on it, pick from it, or ignore it. Presented as a permanent equal fork with 🎯 Choose, never as a beginner ramp. This is the mechanic a new player meets first and the entry point the whole accessibility spine hangs off. Mapping and per-Age segment sets in [`../tables/WHEEL.md`](../tables/WHEEL.md); rationale in [ADR-001](ADR-001-the-low-barrier-turn.md). **Open:** printed wheel, card deck, or build-your-own instructions.

### The Frost Shepherds (Age end is hidden)
At Age start, deal N face-down index cards (N = target tally). Shuffle one ⚡ **Age Turns** card into the last 5. Flip one per turn. When ⚡ comes up, play that turn out, then run the Survival Round. A Steward may spend 3 AP to peek and reorder the stack (prophecy). *(Adapted from The Quiet Year.)*

### The Oracle's Handful (Age-opening ritual)
Before any turns of a new Age:
1. Name the **Now** (confirm the Age's time scale)
2. Name the **Abundance** (what this Age gives freely; −1 AP to invoke, min 1)
3. Name the **Scarcity** (what this Age withholds; +1 AP to invoke)
4. Each Steward folds a **Palette slip**: ⭕ More of this / ❌ Not this Age. Reveal together.
5. Each Steward speaks one **First Word** for the Age aloud. Write all three.
*(Palette from Microscope; Abundance/Scarcity from The Quiet Year.)*

### The Kith layer
Every Age, each Steward names at least one **Kith** — an ordinary named mortal with a job and one trouble. Not a hero. Not a People. A person. Kith persist across Ages via lineages. They anchor gods-eye play in real lived-in lives. *(From Wanderhome.)*

### Legacy Threads
After every round of turns, whoever took the most interesting action names a **Legacy** — a word or phrase on an index card placed on the map. Next round, any action touching the Legacy earns an automatic ⭐. Legacies accumulate into the Age's thematic spine. *(From Microscope.)*

### Pushing
Once per Age, any Steward may **Push** another's proposed action before it's inked. The actor revises or stands firm. If they stand firm: silent group vote, majority wins, ties go to the actor. *(From Microscope.)*

### Holiday between Ages
Between the Survival Round and the next Age's Oracle's Handful: each Steward narrates one sentence about how the peoples of the world mark the transition. No AP. No mechanics. The Age's coda. *(From Wanderhome.)*

### Genus Loci turns
Once per Age, any Steward may spend 1 AP to SPEAK AS a place — three sentences in the Log: what it wants, what it fears, who it remembers. That place is marked Genus Loci; future actions involving it earn ⭐. *(From Ex Novo.)*

---

## What we're keeping from the family game

- **Price of Passing** (d4 pick-four, Bold the hex, write in detail) — excellent design, keep exactly
- **Weave Bonus** (⭐ + cooperating Steward gets +1 AP) — the heartbeat mechanic
- **Quiet Turn** (free detail adds, no AP, no tally)
- **Stewardship** as the ownership concept
- **War table** with Invest (2d6, +/−1 per AP)
- **Currents / Nexuses** as magical infrastructure
- **Survival Round** (Thrives / In Danger / Fades with final legendary act)

## What we're revising

- **2d6 AP for the whole Age** → per-turn AP pool with anti-hoarding rule (end turn at ≤5 → cumulative +1 next roll, up to +3). Scales across 6–7 Ages; Dawn of Worlds proved this works.
- **Tally-to-14 vote** → Frost Shepherds hidden countdown
- **Alignment (Good/Lawful/Neutral/Chaotic/Evil)** → likely retired; complications-and-histories do this work better
- **Development Levels (Nascent/Developing/Advanced)** → expand to match 6–7 Ages; Advanced is no longer the ceiling

---

## The companion app (future)

A PWA (no install, QR code in the box). Structured per-turn prompts → readable compendium → export to markdown → AI transforms to Obsidian vault or any other format. The app captures; AI organizes. Scope: AP tracker, dice + table roller, running compendium, shareable export. See `companion/` when that work starts.
