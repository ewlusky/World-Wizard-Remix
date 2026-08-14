# 📜 LANGUAGE

The sixth action family, and the one this edition is built around.

[`../languages/`](../languages/) holds twelve fully constructed tongues — phonology, grammar, naming conventions, vocabulary, phrases, idioms. That content came first. These actions were written to fit it, which is the right order: an action that could not operate on Velthari or Brakthal as written would be the wrong action.

LANGUAGE is available in **every Age**. It is the only family that is, because language is the one thing in the game that survives everything else.

## The Compendium

Keep one page separate from the map. Every word coined during play goes on it, with three columns: **the word**, **what it means**, **who said it first**.

The Compendium is the second permanent artifact of the game, alongside the map. Its whole point is that it outlives its speakers. When a People Fades, their entries stay. When a word passes into another tongue, both entries stay. By the final Age it should read like a glossary assembled by someone who could no longer ask anyone what half of it meant.

## Actions

| Action | AP | What you do |
|---|---|---|
| **Assign a Tongue** | 1 | Bind a People you Steward to one of the twelve languages, or declare a new one and name it. From now on, every name for them and theirs follows that tongue's phonology. |
| **Coin a Word** | 1 | Name something on the map in a tongue you Steward. Add it to the Compendium. The name is now what that thing is called, by everyone, forever. |
| **Gift a Name** | 1 (+1†) | Coin a word for something **another Steward** made. Their thing, your language. |
| **Sound-Shift** | 1 | A tongue drifts. Pick a rule and apply it. Existing words keep their old forms on the map; the new forms go in the Compendium. Both are canon. |
| **Take a Loanword** | **gain +1** | Your People adopt a word from a tongue that is not theirs, because they had contact and were changed by it. Once per pair of tongues per Age. |
| **Invent Writing** | 2 | A tongue becomes written. See below — this has a permanent consequence. |
| **Let a Tongue Die** | **gain +2** | Only when the last People who spoke it Fades. See below. |

† waived, and the other Steward gets +1 AP, if they agree. See [the Weave Bonus](03-the-ap-economy.md#the-weave-bonus).

## Gift a Name is the good one

Naming your own mountain is worldbuilding. Naming *someone else's* mountain, in your language, is history — because now their thing carries a word from your people, and anyone looking at the map can see that those two things touched.

It is also the cheapest cooperative move in the game. Ask first, get the star, pay nothing.

## Sound-Shift

Trigger it when something happens that would plausibly change how a People speak: a split, a migration, a conquest, an isolation, a few thousand years.

Pick one rule and apply it consistently. Each language file lists its own phonology, so the honest shifts are the ones that language would actually make. Some that work anywhere:

- a consonant softens between vowels
- long vowels collapse to short
- a final syllable drops
- two sounds that were different merge
- stress moves, and the unstressed syllable erodes

**The old form stays on the map.** This is the mechanic's whole reason for existing. Ink does not shift. A hex labelled with a name in a form nobody says any more is exactly how real maps work, and it is free history — someone will eventually ask why the river is spelled like that.

**When a People splits into two, the tongue forks.** Both Stewards apply their own shift going forward, and the two branches diverge for the rest of the game.

## Invent Writing

**A written tongue can no longer Sound-Shift.** Its forms are fixed at the moment of writing.

That is the trade. Writing buys permanence and costs change: the tongue stops drifting, its Compendium entries stop being provisional, and its words survive the death of everyone who spoke them. An unwritten tongue stays alive and keeps moving, and takes everything with it when it goes.

Neither is better. A written language that outlives its speakers becomes a scholarly problem in a later Age; an unwritten one becomes a rumour.

## Let a Tongue Die

Available **only** when the last People who spoke a tongue Fades in [the Survival Round](05-ending-an-age.md). It is not a move you can make for the AP.

When it happens:

- Every word already coined **stays on the map and in the Compendium.**
- Mark those Compendium entries. They are still legible if the tongue was written, and unreadable if it was not.
- **No one may Coin a Word in that tongue again.** Ever.
- Words already borrowed into other tongues by Loanword survive, and are now the only living trace.

The Steward who loses the tongue gains **+2 AP** and should write one line in the Compendium about the last thing anyone said in it.

## On speaking in-world words aloud

**There is deliberately no mechanical reward for pronouncing coined words at the table.**

This came up as an open question and the answer is no, on principle. A rule that pays players for performing out loud taxes the exact person the rest of this game bends over backwards to include — see [ADR-001](../design/ADR-001-the-low-barrier-turn.md). Speaking a word you invented in front of other people is a harder ask than inventing it, and making it worth AP turns a shy table into a quiet table that is now also losing.

Say the words if you enjoy saying them. Nothing depends on it.

## Porting note

New in this edition. The family edition had no LANGUAGE family; `design/DESIGN-DIRECTION.md` listed it as the one action family still to be designed, while the twelve languages had already been written. These actions close that gap and answer four of the open questions: sound-shifts on a split (the tongue forks), what a Fade leaves behind (unreadable words, and loanwords as the living trace), what writing changes (it freezes drift), and whether speaking aloud should pay (it should not).
