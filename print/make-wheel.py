#!/usr/bin/env python3
"""Generate the printable wheel sheets.

    python print/make-wheel.py

Writes wheel-*.svg into this folder. No dependencies. Regenerate after
changing a table name so the wheel and tables/README.md stay in step.
"""
import colorsys
import math
import os

OUT = os.path.dirname(os.path.abspath(__file__))

ALL = [
    'Mundane Terrain', 'Magical Terrain', 'Dramatic Features', 'Peoples',
    'Avatars', 'Sources of Magic', 'Significant Species', 'Events',
    'Disasters', 'Significant Locales', 'Magical Structures',
    'Artifacts & Relics', 'Significant Beings', 'Species', 'Inhabitants',
]

# Per-Age segment sets. See tables/WHEEL.md for the reasoning: a wheel that
# can land on Artifacts in the Primordial Age produces a shrug.
AGE_I = ['Mundane Terrain', 'Magical Terrain', 'Dramatic Features',
         'Sources of Magic']
AGE_II = AGE_I + ['Peoples', 'Avatars', 'Significant Species',
                  'Significant Beings', 'Disasters', 'Events']
AGE_III = [s for s in AGE_II if s != 'Mundane Terrain'] + [
    'Magical Structures', 'Significant Locales', 'Artifacts & Relics']

SIZE = 820           # wheel box, px
R = 360              # wheel radius
HUB = 34             # blank centre, also the label start offset
LABEL_GAP = 46       # where labels begin, measured from centre
TOP = 56             # headroom for the title
CX = SIZE / 2
CY = SIZE / 2 + TOP


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))


def wedge(r, a0, a1):
    """Pie slice path from the centre, angles in degrees, 0 = east."""
    x0, y0 = CX + r * math.cos(math.radians(a0)), CY + r * math.sin(math.radians(a0))
    x1, y1 = CX + r * math.cos(math.radians(a1)), CY + r * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return (f'M {CX:.2f} {CY:.2f} L {x0:.2f} {y0:.2f} '
            f'A {r:.2f} {r:.2f} 0 {large} 1 {x1:.2f} {y1:.2f} Z')


def fill(i, n):
    """Even hue sweep, held light enough that black text stays legible."""
    r, g, b = colorsys.hls_to_rgb((i / n) * 0.86, 0.74, 0.62)
    return '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))


def label(text, mid_deg, font_size):
    """Radial label running outward. Segments on the left half get rotated
    180 degrees and right-anchored so no text ends up upside down."""
    flip = 90 < (mid_deg % 360) < 270
    rot = mid_deg + 180 if flip else mid_deg
    x = -LABEL_GAP if flip else LABEL_GAP
    anchor = 'end' if flip else 'start'
    return (f'<g transform="translate({CX},{CY}) rotate({rot:.2f})">'
            f'<text x="{x}" y="0" font-size="{font_size}" text-anchor="{anchor}" '
            f'dominant-baseline="middle">{text}</text></g>')


def build(labels, title, note):
    labels = [esc(x) for x in labels]
    n = len(labels)
    step = 360.0 / n
    font_size = 21 if n <= 6 else (18 if n <= 10 else 15)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE + 72}" '
        f'width="7.5in" height="{7.5 * (SIZE + 72) / SIZE:.2f}in" role="img" '
        f'aria-label="{esc(title)}, a spinner with {n} segments">',
        '<style>'
        'text{font-family:Georgia,"Iowan Old Style",serif;fill:#1a1208}'
        '.seg{stroke:#1a1208;stroke-width:2.2}'
        '.ttl{font-size:26px;font-weight:700;text-anchor:middle}'
        '.note{font-size:14px;text-anchor:middle;fill:#4a3c28}'
        '</style>',
        '<rect width="100%" height="100%" fill="#fbf7ef"/>',
        f'<text class="ttl" x="{CX}" y="40">{esc(title)}</text>',
    ]
    for i in range(n):
        a0 = -90 + i * step
        parts.append(f'<path class="seg" d="{wedge(R, a0, a0 + step)}" '
                     f'fill="{fill(i, n)}"/>')
    for i, text in enumerate(labels):
        parts.append(label(text, -90 + (i + 0.5) * step, font_size))
    parts += [
        f'<circle cx="{CX}" cy="{CY}" r="{HUB}" fill="#fbf7ef" '
        f'stroke="#1a1208" stroke-width="2.2"/>',
        f'<circle cx="{CX}" cy="{CY}" r="4.5" fill="#1a1208"/>',
        f'<path d="M {CX - 17} {CY - R - 30} L {CX + 17} {CY - R - 30} '
        f'L {CX} {CY - R + 6} Z" fill="#1a1208"/>',
        f'<text class="note" x="{CX}" y="{SIZE + 62}">{esc(note)}</text>',
        '</svg>',
    ]
    return '\n'.join(parts)


SHEETS = [
    ('wheel-all-fifteen.svg', ALL, 'The Wheel',
     'Spin, then roll or pick on the table it lands on. Or ignore it and use your own idea. '
     'Making something up is always allowed.'),
    ('wheel-age-i-primordial.svg', AGE_I, 'The Wheel — Age I, Primordial',
     'Land, and the power running under it. Nothing sentient exists yet.'),
    ('wheel-age-ii-prehistoric.svg', AGE_II, 'The Wheel — Age II, Prehistoric',
     'Peoples emerge and legends begin.'),
    ('wheel-age-iii-ancient.svg', AGE_III, 'The Wheel — Age III, Ancient',
     'Terrain is set and expensive. Organisation is cheap.'),
]


def main():
    for filename, labels, title, note in SHEETS:
        with open(os.path.join(OUT, filename), 'w', encoding='utf-8') as fh:
            fh.write(build(labels, title, note))
        print(f'  {filename:<34} {len(labels):>2} segments')
    print('  Age IV uses the fifteen-segment sheet.')


if __name__ == '__main__':
    main()
