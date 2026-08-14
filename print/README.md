# Print

Things you put on a table.

| File | What it is |
|---|---|
| [player-reference.md](player-reference.md) | The whole game on one sheet. Turn sequence, the four Ages, the economy, Survival Round, War, Language. Everything else is lookup. |
| [wheel-all-fifteen.svg](wheel-all-fifteen.svg) | 🎡 The wheel, all fifteen tables. Use for Age IV, or any Age if you would rather not swap sheets. |
| [wheel-age-i-primordial.svg](wheel-age-i-primordial.svg) | Four segments. Land and magic only, because nothing sentient exists yet. |
| [wheel-age-ii-prehistoric.svg](wheel-age-ii-prehistoric.svg) | Ten segments. |
| [wheel-age-iii-ancient.svg](wheel-age-iii-ancient.svg) | Twelve. Mundane Terrain drops out, structures and artifacts come in. |
| [make-wheel.py](make-wheel.py) | Generates all four sheets. No dependencies. |

## The wheel sheets

Sized at 7.5 inches, so they print on US Letter or A4 with a margin. Print, mount on card, and put a spinner through the centre — the hub is left blank for a split pin or a bottle-top arrow. The pointer at the top is printed on the sheet, so the wheel can also be spun as a loose disc under a fixed arrow.

Segments are per-Age because a wheel that can land on Artifacts & Relics in the Primordial Age produces a shrug rather than an idea. Reasoning in [`../tables/WHEEL.md`](../tables/WHEEL.md).

**A spinner is not the only way.** Fifteen index cards shuffled into a deck does the same job, is cheaper to make, and is easier to weight per Age — just remove the cards that do not apply. Whether the published edition ships a wheel, a deck, or instructions for making either is still open.

## Regenerating

```
python print/make-wheel.py
```

Run it after renaming a table so the wheel and the tables stay in step. Labels are shortened where a full table name would not fit a segment: "Significant Locales" on the wheel is [Table 10: Significant Locales & Items](../tables/10-significant-locales-items.md).

## What is not here yet

- A blank hex map. The family edition used the maps that ship with the original game, which are not ours to redistribute. This edition needs its own, at 50×30 and 75×40.
- The Compendium sheet for [📜 Language](../rulebook/10-language.md) — three columns, word / meaning / who said it first. Currently just an instruction.
- A printable Log sheet. [`rulebook/06-log-sheet.md`](../rulebook/06-log-sheet.md) has the tables but is not laid out for printing.
