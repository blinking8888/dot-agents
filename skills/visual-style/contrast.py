#!/usr/bin/env python3
"""WCAG 2.x contrast check. Usage: contrast.py FG BG [FG BG ...]
Colours as #RRGGBB, or #RRGGBB@ALPHA (0-1) for a colour blended over the BG.
Exits 1 if any pair is below 4.5:1 (body text). 3:1 is the floor for
large text (>=24px, or >=19px bold) and UI parts (borders, icons, focus rings)."""
import sys


def rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def lum(c):
    c = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def parse(fg, bg):
    b = rgb(bg)
    if "@" in fg:
        hexpart, a = fg.split("@")
        a = float(a)
        f = [a * x + (1 - a) * y for x, y in zip(rgb(hexpart), b)]
    else:
        f = rgb(fg)
    return f, b


def ratio(fg, bg):
    f, b = parse(fg, bg)
    hi, lo = sorted((lum(f), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def main(args):
    if not args or len(args) % 2:
        sys.exit(__doc__)
    ok = True
    for fg, bg in zip(args[::2], args[1::2]):
        r = ratio(fg, bg)
        grade = "AA" if r >= 4.5 else "large/UI only" if r >= 3 else "FAIL"
        ok &= r >= 4.5
        print("%-16s on %-8s %5.2f:1  %s" % (fg, bg, r, grade))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main(sys.argv[1:])
