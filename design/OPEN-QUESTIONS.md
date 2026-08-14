# Open Questions

*Decisions not yet made. Each entry should get its own ADR in this folder when resolved.*

---

## Structural

- **6 Ages or 7?** Do Classical and Medieval need to be separate? Does the final Age need a different mechanical texture (the game "knows" it's ending)?
- **AP economy: per-turn or per-Age?** Per-turn pool with anti-hoarding (DoW model) vs. keeping 2d6-per-Age and adjusting scale. Needs playtesting on 6–7 Age structure.
- **Player count.** Currently tuned for 3 (family). Does it work for 2? 5? 6? Where does it break?
- **Session length.** One Age per session? Multiple turns across sessions? How does the Frost Shepherds card work across multiple sessions?

## Language family

✅ **RESOLVED 2026-08-09 — the family is written: [`../rulebook/10-language.md`](../rulebook/10-language.md).** Seven actions, available in every Age, built to fit the twelve tongues that already existed.

- ~~**Own action family (📜) or a cross-cutting modifier?**~~ **Own family.** Assign a Tongue, Coin a Word, Gift a Name, Sound-Shift, Take a Loanword, Invent Writing, Let a Tongue Die.
- ~~**Sound-shifts across Ages.**~~ **A split forks the tongue** — both Stewards shift independently from then on and the branches diverge for the rest of the game. **The old form stays on the map**; only the Compendium gets the new one, and both are canon. **When a People Fades**, their words remain but become unreadable unless the tongue was written; words already taken as loanwords by other peoples survive and are the only living trace.
- ~~**Writing systems.**~~ **Writing freezes a tongue.** A written language can never Sound-Shift again. Permanence bought with change, and it makes an unwritten language something that takes everything with it when it goes.
- ~~**Polyglot play.** Should speaking in-world coined words at the table do anything mechanically?~~ **No, on principle.** Paying players to perform aloud taxes precisely the person [ADR-001](ADR-001-the-low-barrier-turn.md) exists to protect: saying a word you invented in front of people is a harder ask than inventing it, and pricing it turns a shy table into a quiet table that is also now losing. Say the words if you enjoy saying them; nothing depends on it.

**Still open here:** whether the Compendium wants a printed sheet or stays an instruction, and whether a coined word should interact with Legacy Threads once those exist.

## Rules details

- **Frost Shepherds + multi-session play.** Where does the unflipped card stack live between sessions?
- **Kith lineages.** How exactly does a Kith "persist via lineage"? Can their family line become a named People? When does a Kith line become too prominent to stay Kith?
- **Pushing: once per Age per Steward, or once per Age total?** Total feels more precious; per Steward is more evenly distributed.
- **Oracle's Handful: what if two Stewards name the same Abundance?** Stack, or replace?
- **Genus Loci: can a place be spoken through more than once across multiple Ages?** Does it accumulate a voice, or reset?
- **Complicate + Survival Round.** If a complication directly causes the creation to roll lower in the Survival Round, is that a feature or a bug? (Probably a feature — own it.)

## Product

- **Name.** "WorldWizard" is working title. More evocative options?
- **Starter world.** Does the game ship with a sample Primordial setup, or is it pure scaffolding?
- **Map medium.** Hex paper, region cards, or medium-agnostic? The family game uses physical hex paper on a whiteboard — does the published game assume that, recommend it, or leave it open?
- ~~**Family variant.** Explicit "simplified" variant for younger/casual players in the back of the book? Or a single ruleset that scales?~~ ✅ **RESOLVED 2026-08-09 by [ADR-001](ADR-001-the-low-barrier-turn.md): a single ruleset that scales.** A quarantined "simplified" variant reintroduces exactly the self-consciousness the wheel and the Quiet Turn exist to remove. The accessibility affordances live in the core turn sequence, available to everyone, marked as nobody's easy mode.
- **License.** CC-BY-SA, full commercial copyright, something else?
- **Companion app tier.** Free QR-code tier vs. paid unlock for richer features — where's the line?

---

## ✅ RESOLVED: the name (opened and closed 2026-08-07)

**Renamed to World Wizard Remix.** "Remix" is the standard TTRPG convention for a declared hack — it signals derivative status in the title itself, which is the honest position. Combined with CREDITS.md and the link to buy the original, this is settled. Candidate names below are kept only in case a fully-original title is ever wanted.

### Original problem

This project could not be published as "WorldWizard." That is the title of the game it hacks — [Worldwizard by Lampblack & Brimstone](https://lampblack-brimstone.itch.io/worldwizard), $5 on itch.io, 1-8 players.

Titles are not copyrightable, but shipping a same-genre, same-format, print-and-play worldbuilding game under an identical name is a trademark problem and, more simply, the wrong thing to do. Attribution is in [CREDITS.md](../CREDITS.md), and the repo is now `World-Wizard-Remix`.

### Candidate names

Drawn from what this variant actually adds — the accumulating map, the Kith, language that drifts and dies, and the shrinking Now.

| Name | Where it comes from |
|---|---|
| **Made and Broken** | Straight from the README: *"the accumulated weight of everything your group has made — and broken"* |
| **What the Map Remembers** | The map is canon; things that fade leave marks |
| **The Shrinking Now** | The logarithmic Age structure, which is the biggest single divergence |
| **Kithmaking** | The Kith layer — ordinary mortals weighted equally with gods |
| **The Long Fade** | Fade-rather-than-elimination, and languages dying |
| **Everything We Made** | Warmer, family-table register |

### Also to decide

- ~~**Email Lampblack & Brimstone.**~~ ✅ **DECIDED 2026-08-09: not doing it, at least not now, possibly never.** Nothing here depends on their answer. The "Remix" title and `CREDITS.md` already declare the derivative status, name the designer, and point buyers at the original, which is the whole of the obligation. Reaching out was only ever an optional upgrade from correct to friendly. Revisit only if there is a commercial release, where a courtesy note becomes worth sending on its own merits.
- ~~**License.**~~ ✅ **DECIDED 2026-08-09: explicit all-rights-reserved, written into [`../LICENSE`](../LICENSE), and revisited when the game is playable end to end.** An open licence is a one-way door: permissions can be added later but never withdrawn. Nobody forks an unfinished game, so opening up now would buy no contributors while closing off the commercial option. The point of writing it down rather than leaving the field blank is that an absent LICENSE reads as an oversight; "not yet" is a decision and should look like one. The future fork, once the game is playable: **CC BY-SA 4.0 or the ORC licence** if the goal is community hacks, **rights reserved plus a paid release** if the goal is to sell it. Sole copyright ownership means both stay available via dual licensing.
