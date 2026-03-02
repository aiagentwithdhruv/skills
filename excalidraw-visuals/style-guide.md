# Excalidraw Visuals Style Guide

This is the definitive visual specification for all AI-generated Excalidraw-style visuals. Every detail here exists to reduce variance between generations.

## The Golden Rule

**Pass the style reference image on EVERY generation.** This is the single biggest lever for visual consistency. The style reference lives at:

```
brand-assets/excalidraw-style-reference.png
```

Always include: `--input "brand-assets/excalidraw-style-reference.png"`

This image shows the model exactly what the target aesthetic looks like -- font, colors, shapes, icons, and spacing all in one place.

---

## Font Specification

The #1 source of inconsistency is font variation. Lock this down hard.

**Target font feel:** Neat architect's handwriting. Not sloppy, not perfect. Consistent letter sizes, slightly rounded strokes, medium weight. Think: a designer sketching on a whiteboard with a thick marker -- legible, intentional, but clearly hand-drawn.

**Prompt language to use every time:**
```
All text uses neat, consistent architect-style handwriting -- legible, slightly rounded letters with medium stroke weight. Letter sizes are uniform within each label. Titles are bold and larger. Body labels are smaller but equally neat. This is NOT sloppy handwriting -- it looks like a designer wrote it with a thick marker.
```

**What to avoid in prompts:**
- Never say "Comic Sans", "Comic Neue", or "Virgil" -- these trigger wildly different interpretations
- Never say "messy" or "loose" handwriting
- Never say "handwritten font" without specifying the style

---

## Color System

Colors are assigned by semantic meaning, not randomly. This prevents the model from inventing new color combos each time.

### Primary Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary accent | Soft blue | #a5d8ff | Main elements, primary boxes, key concepts |
| Secondary accent | Warm yellow | #ffec99 | Supporting elements, secondary info, highlights |
| Success/output | Soft green | #b2f2bb | Results, outputs, completed states, positive |
| Warning/attention | Coral/salmon | #ffa8a8 | Alerts, problems, pain points, "before" states |
| Tertiary accent | Light purple | #d0bfff | Optional third category, connections, meta-info |
| Text | Dark charcoal | #343a40 | All text and labels |
| Lines/arrows | Dark gray | #495057 | All connector lines, arrows, borders |
| Background | White | #ffffff | Always clean white, no texture |

### Color Assignment Rules

When building prompts, explicitly assign colors to elements:
- **Flows (left to right):** Blue (input) -> Yellow (process) -> Green (output)
- **Comparisons (side by side):** Coral (old/bad/slow) vs Green (new/good/fast)
- **Hub and spoke:** Blue (center hub), mixed colors for spokes
- **Hierarchies (top to bottom):** Blue (top level), Yellow (middle), Green (bottom)
- **Lists/grids:** Alternate colors row by row for visual rhythm

Never let the model choose colors. Always specify: "The [element] box is filled with soft blue (#a5d8ff)."

---

## Shape Specification

### Boxes/Containers
- Rounded rectangles with visible corner rounding
- 2-3px dark gray (#495057) stroke/outline
- Pastel fill from the color palette above (not fully opaque -- roughly 60-70% opacity feel)
- Consistent size for elements at the same hierarchy level
- Generous internal padding around text

### Arrows/Connectors
- Hand-drawn style -- slightly curved or wobbly, not ruler-straight
- Dark gray (#495057) stroke, 2px weight
- Arrowheads are simple triangles, not ornate
- Arrows flow in clear, readable directions (left-to-right or top-to-bottom preferred)

### Circles
- Used sparingly for numbered steps or key focal points
- Same stroke and fill rules as boxes
- Keep small to medium size

---

## Icon & Illustration Style

This defines how to draw people, agents, objects, and abstract concepts. Consistency here is critical.

### People / Users
- Simple stick figures with round heads
- No facial features (no eyes, mouth, nose)
- Single-color dark gray outlines
- Arms and legs are simple lines
- Can hold objects (laptop, phone, document)

### AI Agents / Robots
- Simple round head with two dot eyes and a small antenna
- Rectangular body, stick arms/legs
- Same dark gray outline as people
- Distinguish from humans with the antenna or a small gear icon on the body
- NOT cute/cartoonish -- clean and minimal

### Computers / Servers
- Simple rectangle with a slightly smaller rectangle inside (screen)
- Clean line drawing, no 3D perspective
- Dark gray outline, pastel fill

### Documents / Files
- Rectangle with a folded corner (top-right)
- Dark gray outline, white or light fill
- Can have 2-3 horizontal lines inside to suggest text

### Gears / Automation
- Simple gear shape (circle with teeth)
- Dark gray outline, can be filled with accent color
- Use to represent processes, automation, settings

### Arrows / Flow
- Curved hand-drawn arrows for connections
- Straight-ish arrows for sequences
- Always dark gray

### Abstract Concepts
- Use labeled boxes instead of trying to illustrate abstract ideas
- Better to have a clean box with "API" than a bad drawing of a cloud
- When in doubt, use a simple icon + label, not a complex illustration

---

## Layout Templates

Use these standard layouts. Always specify the layout type in the prompt so the model doesn't invent its own.

### 1. Left-to-Right Flow
Best for: processes, sequences, transformations
```
[Input] --> [Process] --> [Output]
```
Prompt language: "Layout flows left to right. On the far left, show [X]. An arrow points right to [Y] in the center. Another arrow points right to [Z] on the far right."

### 2. Hub and Spoke
Best for: capabilities, features radiating from a central concept
```
        [Spoke 1]
           |
[Spoke 4]--[HUB]--[Spoke 2]
           |
        [Spoke 3]
```
Prompt language: "Center the [HUB] as a large box in the middle. Radiating outward, show [N] smaller boxes arranged evenly around it, each connected by an arrow pointing from the hub outward."

### 3. Top-to-Bottom Hierarchy
Best for: levels, layers, progressive depth
```
[Level 1 - widest]
    |
[Level 2 - medium]
    |
[Level 3 - narrowest]
```
Prompt language: "Three horizontal tiers stacked vertically. The top tier is [X], the middle tier is [Y], the bottom tier is [Z]. Each tier is a wide rounded rectangle. Arrows point downward between tiers."

### 4. Side-by-Side Comparison
Best for: before/after, old vs new, option A vs option B
```
[Option A]    |    [Option B]
  ...         |      ...
  ...         |      ...
```
Prompt language: "Split the image into two equal halves with a vertical dividing line. The left side shows [A], the right side shows [B]. Label the left side [A title] and the right side [B title]."

### 5. Numbered Steps List
Best for: frameworks, checklists, ordered instructions
```
1. [Step one]
2. [Step two]
3. [Step three]
```
Prompt language: "A vertical list of [N] numbered steps. Each step is a rounded rectangle with a colored circle containing the number on the left, and the step text inside the rectangle. Steps are stacked vertically with small gaps."

### 6. Cycle / Loop
Best for: feedback loops, iterative processes
```
    [Step 1]
   /         \
[Step 4]   [Step 2]
   \         /
    [Step 3]
```
Prompt language: "A circular cycle with [N] steps arranged in a circle. Curved arrows connect each step to the next, flowing clockwise. The cycle title is in the center."

---

## Text Minimization Rules

AI image models misspell words. The fewer words, the fewer errors.

### Hard Limits
- **Titles:** Max 5 words. Prefer 3.
- **Box labels:** Max 3 words. Prefer 1-2.
- **Annotations/callouts:** Max 4 words.
- **Total text in entire image:** Aim for under 30 words. Absolute max 50.

### Strategies to Reduce Text
1. Use icons instead of words (gear icon instead of "Automation")
2. Use abbreviations when obvious (API, AI, DB, CLI)
3. Remove articles (a, the, an)
4. Remove prepositions when meaning is clear from arrows/layout
5. Use symbols: arrows instead of "leads to", checkmarks instead of "complete"

### Spelling Protection
- Before finalizing the prompt, count every word that will appear as text in the image
- Flag any word over 8 characters -- these are most likely to be misspelled
- If a long word is essential, consider abbreviating or breaking into shorter words
- Common misspelling risks: "Automation" -> use "Automate", "Configuration" -> use "Config", "Instructions" -> use just an icon

---

## Sophistication Layer

These elements make our visuals look slightly more polished than basic Excalidraw while keeping the hand-drawn feel.

### What Makes It "Slightly More Sophisticated"
- **Colored fills in boxes** -- basic Excalidraw is often just outlines. We use pastel fills.
- **Consistent spacing** -- elements are evenly distributed, not randomly placed
- **Visual hierarchy** -- titles are clearly larger/bolder than labels
- **Intentional color coding** -- colors mean something, not random
- **Clean whitespace** -- generous margins, nothing cramped
- **Subtle thickness variation** -- titles have thicker strokes, labels have thinner strokes

### What Keeps It "Hand-Drawn"
- Lines are slightly imperfect (not ruler-straight)
- Shapes have visible hand-drawn stroke texture
- Text has handwriting character (not typed)
- Arrows curve naturally
- Nothing is pixel-perfect aligned

### What to NEVER Include
- Drop shadows
- Gradients
- 3D effects
- Realistic illustrations or photos
- Corporate clip art
- Stock imagery
- Heavy borders or outlines
- Dark or colored backgrounds

---

## Prompt Construction Checklist

Before sending any prompt to the API, verify:

- [ ] Style reference image is included via `--input`
- [ ] Layout template is specified (which of the 6 types?)
- [ ] Every box/element has an assigned color from the palette
- [ ] Every text label is 3 words or fewer
- [ ] Total word count in the image is under 50
- [ ] Long words (8+ characters) are flagged and shortened if possible
- [ ] Spatial positions are explicit ("on the left", "top center", "bottom right")
- [ ] Icon/illustration style follows the vocabulary above
- [ ] The diagram tells a clear story with a single visual flow direction
