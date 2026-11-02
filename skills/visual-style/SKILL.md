---
name: visual-style
description: House visual style (palette, fonts, contrast rules) for anything made to be looked at. Use when building or styling a web page or UI, a document or PDF, slides, or a chart.
---

A minimal, **legible** style: dark navy, one amaranth accent, system fonts. A project's own `AGENTS.md` design rules win where they conflict; everything they leave open comes from here.

## Palette

| Token | Hex | Role |
|---|---|---|
| navy | `#010228` | Screen background. Text on print pages and on coloured fills |
| ice | `#DBF5FA` | Text on navy |
| amaranth | `#DD2D4A` | **The** accent. Also means error |
| cyan | `#00B4D8` | Inline links, info, focus ring, data series |
| yellow | `#FFD60A` | Warning |
| green | `#3AB795` | Success |

Use only the colours the piece needs. Make in-between tones from ice at reduced opacity, never a new hue:

- Card / raised surface: ice at 6%
- Divider (decorative): ice at 15%
- Control border (inputs, toggles): ice at 40% or more (3:1)
- Muted text: ice at 70%

**Accent budget**: amaranth goes on 1–3 elements per view, the one thing the eye should land on first (the primary button, the key number, the active item). Because amaranth also means error, the accent and an error never share a view without a label telling them apart.

**Colour is never the only signal.** Pair every status colour with a word or icon.

## Contrast

Floors (WCAG AA): **4.5:1** for body text, **3:1** for large text (≥24px, or ≥19px bold) and UI parts (control borders, icons, focus rings). Measured pairs:

| Pair | Ratio | Use |
|---|---|---|
| ice on navy | 17.7 | Body text |
| ice 70% on navy | 8.6 | Muted text |
| cyan / green / yellow on navy | 8.2 / 8.1 / 14.3 | Any text |
| amaranth on navy | 4.4 | Large/bold text, fills, borders, icons only |
| white `#FFFFFF` on amaranth | 4.6 | Button labels, bold. (Ice on amaranth is 4.1, too low) |
| navy on cyan / green / yellow | 8.2 / 8.1 / 14.3 | Badges and status fills |
| navy on white | 20.2 | Print body text |
| amaranth on white | 4.6 | Print headings, rules, accent text |
| cyan / green on white | 2.5 | Fills with navy text only, never as text |

## Themes

- **Screen** (pages, apps, dashboards, slides): navy background, ice text.
- **Print** (PDF, docx, reports, anything likely printed): white or ice page, navy text, amaranth accent. Links are navy and underlined; cyan, green and yellow appear only as fills or chart marks.

## Type

- Text: `"Helvetica Neue", Helvetica, Arial, sans-serif`
- Code, numbers in tables, identifiers: `ui-monospace, Menlo, Consolas, "DejaVu Sans Mono", monospace`
- System fonts only. Load no web fonts.
- Four sizes: small, body, heading, display, each step ×1.25–1.5. Two weights: 400 and 700.
- Body line-height 1.5; line length 60–75ch.
- Links on screen: cyan, underlined.

## Space and form

- Spacing on an 8px grid (4px for tight spots). Separate with whitespace first, a divider second.
- One corner radius (6px) or square corners throughout.
- Flat: no gradients, no drop shadows, no emoji as icons. Every element carries information.
- Interactive elements show a 2px cyan focus ring.

## Done

The work is done when **every** text/background and UI/background pair actually used has been run through the checker and meets its floor:

```bash
python3 ~/.gemini/skills/visual-style/contrast.py "#DBF5FA" "#010228" "#DBF5FA@0.7" "#0e1033"
```

Arguments are FG BG pairs; `#RRGGBB@0.7` blends that colour over the BG. Report the pairs and ratios. A pair graded `large/UI only` passes only where it is used for large text or UI parts.
