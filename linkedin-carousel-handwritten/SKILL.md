---

> **BEFORE generating any image prompt, read `STYLE-LOCKED.md` in this folder.** It holds the locked palette (#18D1E0), portrait spec, and the ambient block (coffee mug, cap-off pen, paper clips) that must never be dropped.
name: linkedin-carousel-handwritten
description: Generate weekly long-form LinkedIn carousel posts with hand-drawn notebook-style slides — the proven 7-slide format optimized for the 2026 LinkedIn algorithm. Produces post copy + 7 Gemini-ready slide prompts + posting strategy + DM script + cross-platform repurposing in one go. Use when Dhruv asks for a weekly carousel, "Build-in-Public" educational post, or wants to teach a methodology / system / framework in long-form. Pairs with handdrawn-diagram skill for style consistency.
---

# LinkedIn Carousel — Handwritten Weekly Post

## Goal

Turn one technical lesson, methodology, or system Dhruv has shipped in production into a complete LinkedIn carousel post that:

1. Stops the scroll on the first slide
2. Holds dwell time across all 7 slides
3. Converts comments into qualified DMs
4. Builds the AIwithDhruv brand library week over week
5. Compounds via cross-posting to X, Instagram, YouTube

Every output of this skill follows the SAME visual + structural pattern — that's how the channel develops a recognizable rhythm. Audience starts to anticipate the format.

---

## When to Invoke

Trigger phrases from Dhruv:

- "Write a LinkedIn carousel about [topic]"
- "Make this a weekly carousel post"
- "Turn this methodology into a notebook carousel"
- "Build the Sunday/Tuesday post"
- "Use the carousel skill"

Default cadence: **once per week, posted Tuesday or Wednesday at 9-10 AM IST.**

---

## Series Identity (Locked)

| Field | Value |
|------|------|
| Series name | **Build-in-Public Diaries — Notebook Edition** |
| Episode prefix | `Diary #N` (continuous numbering across all carousels) |
| Cadence | 1 per week, Tuesday OR Wednesday, 9-10 AM IST |
| Slide count | 7 (algorithm-optimal — outperforms 5 slides by 18%) |
| Aspect | 4:5 vertical for each slide |
| Format | Upload as PDF document post (LinkedIn renders as native carousel — gets 6.6% engagement, highest format) |
| Voice | First-person from Dhruv ("I shipped", "we built", "what I learned") |
| Brand palette | Black marker + cyan #00D4FF + yellow highlighter + pastel sticky notes (yellow, light blue, pink, light green, light purple) |
| Style anchor | Real notebook page on wooden desk — photo of a real whiteboard, NOT digital illustration |

---

## The Proven 7-Slide Formula

Each slide has a single job. Don't blur the jobs.

| # | Slide Job | What's On It | Visual Hero |
|---|-----------|--------------|-------------|
| 1 | **Hook + Thesis** | Title, subtitle, 3 thesis statements, "what fails / what ships" two-column, swipe arrow | Big bold title + cyan-underlined thesis boxes |
| 2 | **The Framework** | The N-step methodology as a flow diagram (boxes connected by arrows) | Horizontal flow with arrows |
| 3 | **The Workflow** | The N-gate / N-rule workflow that runs every commit/task | Horizontal arrow with vertical gates/checkpoints |
| 4 | **The Team / Stack** | The N-agent or N-tool architecture as an org chart or constellation | Org chart or constellation diagram |
| 5 | **The Proof** | One real shipped example with timeline + outcome + numbers | Mini-timeline with checkmarks + outcome box |
| 6 | **The Lesson** | One sentence everyone can take away + "what to do next" | Big quote-style lesson + one action item |
| 7 | **CTA** | Comment FRAMEWORK + Follow + Share — with author signature | Big "COMMENT → FRAMEWORK" hero box + arrow + author Polaroid |

**Why 7 slides:** LinkedIn 2026 algorithm rewards 7-slide carousels with 18% more reach than other lengths. Each swipe = dwell time = distribution. Slides 5 and 6 are the algorithm boost vs the 5-slide version — they keep viewers swiping past the danger zone (35% click-through penalty if they drop off too early).

**Word count rule:** ≤30 words per slide. The notebook style + sticky notes carry the visual story.

---

## Required Inputs (Ask Before Drafting)

If any are missing, ASK Dhruv before generating anything:

1. **Topic / lesson** — what one thing has he shipped that he wants to teach?
2. **Episode number** — check the running count (default: next sequential)
3. **The thesis** — 3 honest statements about what fails vs what ships
4. **The methodology** — the N-step framework (e.g., 6-phase build)
5. **The workflow** — the N-rule/N-gate system that enforces it
6. **The team / stack** — the N-agent or N-tool architecture
7. **A real shipped example** — with a real timeline + real outcome (not hypothetical)
8. **The lesson** — one sentence anyone can apply
9. **The CTA word** — what should commenters write to trigger the DM? (default: "FRAMEWORK")
10. **Public revenue numbers OK?** — default NO unless explicit opt-in

Don't fabricate. If the example doesn't exist, ask for one. Honesty is the brand.

---

## Style Constants (NEVER Change These)

This block goes at the top of EVERY slide prompt. Identical across all 7 slides — that's how the carousel feels like one notebook.

```
═══════ STYLE CONSTANTS — APPLY TO EVERY SLIDE ═══════

Hand-drawn whiteboard infographic on white lined notebook paper, sitting on a natural wooden desk surface visible at the edges. Black marker lines, cyan (#00D4FF) marker highlights, yellow highlighter on key numbers. Real marker ink texture, natural paper grain. Photo of a real whiteboard after a brainstorming session. 4:5 aspect ratio for LinkedIn carousel.

PAPER + SURFACE:
- White lined notebook paper, subtle horizontal lines visible
- Spiral notebook ring binding visible along the LEFT EDGE of the paper
- Natural wooden desk grain visible at all four edges of the paper
- Slight paper texture, subtle natural shadow on right edge

PALETTE (strict — never deviate):
- Black marker for text and outlines
- Cyan #00D4FF for headers, underlines, brand elements, checkmarks, key terms
- Yellow highlighter for numbers and stats
- Pastel sticky notes — yellow (hero feature), light blue (tech/skills), pink (data/memory/persistence), light green (products/quantity), light purple (integrations/connections)

BRANDING (required in 3+ spots on EVERY slide):
1. TOP-RIGHT: "AiwithDhruv" in bold cyan marker inside a hand-drawn rounded rectangle badge with rough edges
2. CENTER: faint diagonal "AiwithDhruv" watermark in light grey marker across the page (very subtle, doesn't compete with content)
3. BOTTOM-RIGHT: "AiwithDhruv" with cyan lightning bolt + "AD" monogram inside a hand-drawn circle + "@aiwithdhruv · github.com/aiagentwithdhruv"

AMBIENT DETAILS (every slide gets these):
- Subtle coffee ring stain somewhere on the page
- Paper clip or piece of tape on 1-2 sticky notes
- Blue ballpoint pen lying diagonally across the wooden desk at one edge
- Small marker doodle stars and tiny arrow doodles in empty whitespace
- Slight eraser smudge in one margin
- Slightly imperfect handwriting — readable but real

ANTI-PATTERNS (never do these — break any one and the slide loses authenticity):
- NO computer/digital fonts — every word hand-drawn
- NO Canva-template look or polished marketing-design feel
- NO graphic-design slide aesthetic
- NO stock-photo people, clipart, emoji, 3D rendered elements
- NO portraits except on Slide 7 (the CTA slide), and only as a small Polaroid taped to the page
- NO color outside the palette above
- NEVER use the word "infographic" anywhere visible (triggers digital look)
- NO Photoshop-perfect sticky notes — they must look like real physical sticky notes photographed on the page (slight curl at corners, real shadow, random tilt 4-10°)
- NO computer icons — every icon hand-sketched with marker
- NO portraits or faces unless explicitly listed in the slide
- NO empty mockups — every visual element has content inside

═══════ END STYLE CONSTANTS ═══════
```

---

## Per-Slide Prompt Templates

Replace everything in `[BRACKETS]` with topic-specific content. Each prompt below is COMPLETE and self-contained — paste with the Style Constants block above.

### Slide 1 — Hook + Thesis

```
[paste STYLE CONSTANTS]

═══ SLIDE 1 OF 7 — HOOK + THESIS ═══

=== TOP TITLE BAR ===
Hand-written bold title across the top, large lettering: "[TITLE — ALL CAPS, 4-6 WORDS MAX]"
Below it, smaller handwritten subtitle: "[SUBTITLE — proof line, e.g., 'Notes from 20+ shipped systems']"
Bold cyan marker underline stroke under the title.
TOP-RIGHT: "AiwithDhruv" cyan badge + "Diary #[N]" written below in small handwriting.

=== CENTER — "THE THESIS" (largest section, takes the middle of the page) ===
Header: "THE THESIS" with a hand-drawn circle around it, slightly oval and imperfect.

Three stacked truth statements, each inside a hand-drawn box with a small bullet circle in front:

Box 1 (top): "[THESIS STATEMENT 1 — what's broken]"
   — Cyan marker underline under the strongest 2-3 words
   — Small sketched [ICON] doodle next to it

Box 2 (middle): "[THESIS STATEMENT 2 — the contrast]"
   — Yellow highlighter rectangle behind the entire phrase
   — Small sketched [ICON] doodle

Box 3 (bottom): "[THESIS STATEMENT 3 — the punchline]"
   — Cyan marker underline under the strongest 2-3 words
   — Tiny sketched [ICON] doodle

Below the three boxes, a hand-drawn arrow pointing right with handwritten label: "what actually ships →"

=== LEFT COLUMN — "WHAT FAILS" ===
Header: "WHAT FAILS" inside a hand-drawn box
A short hand-drawn checklist with X marks next to each, and small sketched icons:
   ✗ [Failure mode 1]    (small sketched icon)
   ✗ [Failure mode 2]    (small sketched icon)
   ✗ [Failure mode 3]    (small sketched icon)
   ✗ [Failure mode 4]    (small sketched icon)
   ✗ [Failure mode 5]    (small sketched icon)

=== RIGHT COLUMN — "WHAT SHIPS" ===
Header: "WHAT SHIPS" inside a hand-drawn box
A short hand-drawn checklist with cyan checkmarks next to each, and small sketched icons:
   ✓ [Working pattern 1]    (small sketched icon)
   ✓ [Working pattern 2]    (small sketched icon)
   ✓ [Working pattern 3]    (small sketched icon)
   ✓ [Working pattern 4]    (small sketched icon)
   ✓ [Working pattern 5]    (small sketched icon)

=== FLASH CARDS scattered around like sticky notes, tilted at slight angles 4-10° ===

YELLOW sticky note (upper-left edge, tape on top edge):
"[BIG STAT]"
"[short context]"
"[scope]"
Small star doodle.

LIGHT BLUE sticky note (right margin, paper clip on top-left):
"[FRAMEWORK SIZE]"
"[license/access]"
"[what's inside]"
Small sketched .md document icon.

PINK sticky note (near bottom-left of thesis):
"[PROOF POINT]"
"[why it matters]"
"[scale]"
Small sketched icon.

LIGHT GREEN sticky note (near right side bottom):
"[OUTCOME]"
"[time to value]"
"[before vs after]"
Small sketched rocket doodle.

=== BOTTOM CENTER — Stats Row ===
Three items in a row, each with a hand-drawn circle around the number and yellow highlighter behind:
"[STAT 1]"     "[STAT 2]"     "[STAT 3]"
Small star doodles around each stat.

=== BOTTOM LEFT — Mini preview flow ===
A small hand-drawn process arrow showing the framework end-to-end:
"[Step 1]" → "[Step 2]" → "[Step 3]" → "[Step 4]" → "[Step 5]" → "[Step 6]" → "SHIP"
Each label inside a small box with hand-drawn arrows between them. Cyan marker underline under the most important step.

=== BOTTOM RIGHT — Author + Branding ===
"AiwithDhruv" with cyan lightning bolt
"@aiwithdhruv  ·  github.com/aiagentwithdhruv"
"AD" monogram in a hand-drawn circle
Tiny "→ swipe for the system" with a small sketched arrow

=== STYLE — CRITICAL ===
Real black marker on white paper. Slight messiness. Authentic notebook page. Title must be unmistakably readable on a phone screen at thumbnail size (200px wide). Apply all STYLE CONSTANTS above. Apply all ANTI-PATTERNS above. Photo of a real whiteboard, NOT digital illustration.
```

---

### Slide 2 — The Framework (Methodology)

```
[paste STYLE CONSTANTS]

═══ SLIDE 2 OF 7 — THE FRAMEWORK ═══

=== TOP TITLE BAR ===
Hand-written bold title: "[FRAMEWORK NAME, e.g., 'THE 6-PHASE BUILD']"
Below it, smaller handwritten subtitle: "[one-line consequence, e.g., 'skip a phase = the bug ships']"
Cyan marker underline under the title.
TOP-RIGHT: "AiwithDhruv" cyan badge + "Slide 2 of 7" written below.

=== CENTER — THE FLOW (largest section) ===
[N] hand-drawn boxes connected left-to-right by hand-drawn arrows, like a process flow diagram. Each box hand-drawn with imperfect edges. Arrows sketched freehand with arrowheads.

Box 1: "[STEP 1]"
Box 2: "[STEP 2]"
Box 3: "[STEP 3]"
[continue for all N steps]
Cyan marker underline under the most critical box.

Below the row of boxes, a hand-drawn arrow continues right to:
"→ SHIP" (with a small hand-sketched rocket doodle and yellow highlighter behind "SHIP")

=== LEFT COLUMN — "WHY THIS ORDER?" ===
Header: "WHY THIS ORDER?" inside a hand-drawn box
[N] handwritten reasons, each with a small dash and a tiny sketched icon:
   — [Step 1] kills "[failure mode 1]"    (sketched icon)
   — [Step 2] kills "[failure mode 2]"    (sketched icon)
   [continue for all N]

=== RIGHT COLUMN — "REAL EXAMPLE" ===
Header: "REAL EXAMPLE: [PROJECT NAME]" inside a hand-drawn box
A small hand-drawn timeline showing a real shipped project:
   ✓ [Step 1] → [duration]
   ✓ [Step 2] → [duration]
   [continue for all N steps]
Below the checklist: small sketched output box labeled "PROD ✓" with yellow highlighter.

=== FLASH CARDS scattered (3-4 sticky notes) ===
[See Slide 1 template for color guide and tilt rules]
Each flash card adds context, doesn't repeat content.

=== BOTTOM CENTER — Stats Row ===
"[Stat 1]"     "[Stat 2]"     "[Stat 3]"
Yellow highlighter behind each, hand-drawn circles around numbers.

=== BOTTOM RIGHT — Branding ===
[Standard branding block — see STYLE CONSTANTS]
Tiny "→ swipe for the workflow" with a small sketched arrow

=== STYLE — CRITICAL ===
Apply all STYLE CONSTANTS. The N boxes must be visually clear and readable on a phone at thumbnail size. The most critical box stands out via cyan underline. Real marker, not digital.
```

---

### Slide 3 — The Workflow (Gates / Rules)

```
[paste STYLE CONSTANTS]

═══ SLIDE 3 OF 7 — THE WORKFLOW ═══

=== TOP TITLE BAR ===
Hand-written bold title: "[WORKFLOW NAME, e.g., 'THE 5 ANTI-DRIFT GATES']"
Below it, smaller handwritten subtitle: "[one-line rule, e.g., 'every commit passes all 5 — in order — no exceptions']"
Cyan marker underline under the title.
TOP-RIGHT: "AiwithDhruv" cyan badge + "Slide 3 of 7" written below.

=== CENTER — THE GATE FLOW (largest section) ===
A long horizontal hand-drawn arrow running LEFT to RIGHT across the middle.
LEFT label: "[STARTING STATE, e.g., 'TASK START']"
RIGHT label: "[ENDING STATE, e.g., 'MAIN BRANCH']" (with a small sketched flag icon)

[N] hand-drawn vertical gate-shapes (simple fence posts or door-frames) drawn over the arrow at evenly-spaced intervals. Each gate numbered 1-N with its name written above:

GATE 1: "[GATE NAME 1]"
GATE 2: "[GATE NAME 2]"
[continue for all N]

Each gate number has a cyan marker circle around it.

=== LEFT COLUMN — "WHAT EACH GATE CHECKS" ===
Header: "WHAT EACH GATE CHECKS" inside a hand-drawn box
[N] short rule blocks with a small sketched icon next to each:
   1. [GATE NAME]   (icon)
      "[rule 1] · [rule 2] · [rule 3]"
   [continue for all N]

=== RIGHT COLUMN — "WHEN A GATE FAILS" ===
Header: "WHEN A GATE FAILS" inside a hand-drawn box
A small hand-drawn flowchart:
   "Gate FAILS"
        ↓
   "STOP. fix. re-run."
        ↓
   "log to errors.md"   (cyan underline)
        ↓
   "1 rule born"        (yellow highlight)
Below: "[the system gets stronger every failure — or your version of this lesson]"

=== FLASH CARDS scattered (3-4 sticky notes, see color guide) ===

=== BOTTOM CENTER — Stats Row ===
"[Stat 1]"     "[Stat 2]"     "[Stat 3]"

=== BOTTOM RIGHT — Branding ===
[Standard branding block]
Tiny "→ swipe for the team" with a small sketched arrow

=== STYLE — CRITICAL ===
Horizontal arrow with N numbered gates is the visual hero. Must read like a process timeline an engineer would sketch. Gates = simple hand-drawn fence posts over the arrow line, NOT digital icons.
```

---

### Slide 4 — The Team / Stack (Architecture)

```
[paste STYLE CONSTANTS]

═══ SLIDE 4 OF 7 — THE TEAM / STACK ═══

=== TOP TITLE BAR ===
Hand-written bold title: "[STACK NAME, e.g., 'THE 7-AGENT STACK']"
Below it, smaller handwritten subtitle: "[one-line rule, e.g., 'hard role boundaries · zero overlap · no agent merges to main']"
Cyan marker underline under the title.
TOP-RIGHT: "AiwithDhruv" cyan badge + "Slide 4 of 7" written below.

=== CENTER — THE ORG CHART / CONSTELLATION (largest section) ===
A hand-drawn org chart (if hierarchical) or constellation (if flat). All boxes hand-drawn with imperfect edges. Lines connecting them sketched freehand.

[For hierarchical:]
TOP BOX (largest, with cyan marker underline + small crown doodle):
"[LEAD ROLE NAME] — [TITLE]"
   subtitle inside box: "[what they own]"

[N-1] boxes below, connected to the lead box:
BOX 1: "[ROLE 1] — [DOMAIN]"   (sketched icon)
BOX 2: "[ROLE 2] — [DOMAIN]"   (sketched icon)
[continue]

[For flat constellation:]
[N] boxes scattered as a constellation with sketched lines between related ones.

=== LEFT COLUMN — "THE RULES" ===
Header: "HARD RULES" inside a hand-drawn box
[N] handwritten rules, each with a small dash and a sketched icon:
   — [Rule 1]    (sketched icon)
   — [Rule 2]    (sketched icon)
   [continue]

=== RIGHT COLUMN — "THE HANDOFF" ===
Header: "THE HANDOFF" inside a hand-drawn box
A small hand-drawn vertical flow:
   "[Step 1]"
      ↓
   "[Step 2]"   (cyan underline if critical)
      ↓
   "[Step 3]"
   [continue, ending in "→ SHIPPED" or "→ MAIN"]

Below the flow: "[one-line consequence]"

=== FLASH CARDS scattered (3-4 sticky notes, see color guide) ===

=== BOTTOM CENTER — Stats Row ===
"[Stat 1]"     "[Stat 2]"     "[Stat 3]"

=== BOTTOM RIGHT — Branding ===
[Standard branding block]
Tiny "→ swipe for the proof" with a small sketched arrow

=== STYLE — CRITICAL ===
The org chart / constellation must feel like a real founder sketched it on a whiteboard while explaining the team. NOT a corporate org chart. Boxes imperfect, lines sketched not ruler-straight, names hand-printed in marker.
```

---

### Slide 5 — The Proof (Real Shipped Example)

```
[paste STYLE CONSTANTS]

═══ SLIDE 5 OF 7 — THE PROOF ═══

=== TOP TITLE BAR ===
Hand-written bold title: "PROOF: [PROJECT NAME]"
Below it, smaller handwritten subtitle: "[real outcome, e.g., 'shipped in 8 days · 0 production bugs']"
Cyan marker underline under the title.
TOP-RIGHT: "AiwithDhruv" cyan badge + "Slide 5 of 7" written below.

=== CENTER — THE TIMELINE (largest section) ===
A hand-drawn horizontal timeline running LEFT to RIGHT showing the real days/weeks of the project.
Each milestone marked with a circle on the timeline + handwritten label above.

Day 1: "[milestone 1]"
Day [N]: "[milestone 2]"
[continue with real days]
Day [final]: "[SHIP]" (with a small sketched rocket and yellow highlighter)

Below the timeline, a "BEFORE → AFTER" comparison:
   BEFORE: "[old state, real]"   →   AFTER: "[new state, real]"

=== LEFT COLUMN — "WHAT WENT RIGHT" ===
Header: "WHAT WORKED" inside a hand-drawn box
3-4 handwritten observations with cyan checkmarks:
   ✓ [Real win 1]
   ✓ [Real win 2]
   ✓ [Real win 3]
   ✓ [Real win 4]

=== RIGHT COLUMN — "WHAT BROKE" ===
Header: "WHAT BROKE (and what we learned)" inside a hand-drawn box
2-3 honest losses with X marks + the lesson:
   ✗ [Real failure 1] → "now we [fix]"
   ✗ [Real failure 2] → "now we [fix]"
   ✗ [Real failure 3] → "now we [fix]"

(Honesty is the brand — show real failures, not vanity.)

=== FLASH CARDS scattered (3-4 sticky notes, see color guide) ===

YELLOW sticky note: "REAL NUMBERS"
"[real metric 1]"
"[real metric 2]"

LIGHT BLUE sticky note: "REAL TIMELINE"
"[start date] → [ship date]"
"[N] days end-to-end"

PINK sticky note: "REAL FAILURE"
"[1 honest failure]"
"now in errors.md"

LIGHT GREEN sticky note: "REAL OUTCOME"
"[real outcome]"
"[real follow-on]"

=== BOTTOM CENTER — Stats Row ===
Three real numbers from the project, each circled with yellow highlight:
"[real stat 1]"     "[real stat 2]"     "[real stat 3]"

=== BOTTOM RIGHT — Branding ===
[Standard branding block]
Tiny "→ swipe for the lesson" with a small sketched arrow

=== STYLE — CRITICAL ===
This slide is the proof. Use ONLY real numbers, real days, real outcomes. NO hypotheticals. NO rounded vanity numbers. If the project shipped in 8 days, write 8 — not "in a week". Honesty is the brand multiplier.
```

---

### Slide 6 — The Lesson (One Line + One Action)

```
[paste STYLE CONSTANTS]

═══ SLIDE 6 OF 7 — THE LESSON ═══

=== TOP TITLE BAR ===
Hand-written bold title: "THE LESSON"
Below it, smaller handwritten subtitle: "[one-line frame, e.g., 'what to take · what to skip']"
Cyan marker underline under the title.
TOP-RIGHT: "AiwithDhruv" cyan badge + "Slide 6 of 7" written below.

=== CENTER — THE BIG QUOTE (largest section) ===
A LARGE handwritten quote in the middle of the page, in bold black marker with cyan-marker emphasis on the strongest 2-3 words. The quote is the takeaway anyone can apply, even if they don't read slides 1-5.

Quote: "[BIG LESSON IN 8-15 WORDS — e.g., 'The model is the easy part. The operating system around it is everything.']"

Beneath the quote, in smaller handwriting: "— Dhruv"

A hand-drawn quote-mark or speech-bubble flourish around the quote.

=== LEFT COLUMN — "WHAT TO STEAL" ===
Header: "STEAL THIS" inside a hand-drawn box
3 short take-aways with cyan checkmarks:
   ✓ [Steal 1 — what they should copy from this system]
   ✓ [Steal 2]
   ✓ [Steal 3]

=== RIGHT COLUMN — "WHAT TO SKIP" ===
Header: "SKIP THIS" inside a hand-drawn box
2-3 honest skips with X marks:
   ✗ [Skip 1 — what's specific to Dhruv's setup, not portable]
   ✗ [Skip 2]
   ✗ [Skip 3]

=== ONE-ACTION CALLOUT (under the quote) ===
A hand-drawn arrow pointing down to a small box:
"DO ONE THING TODAY: [SPECIFIC ACTION, e.g., 'Write your project's CLAUDE.md before your next commit']"

The text inside the box is bold, with cyan underline under the action verb.

=== FLASH CARDS scattered (2-3 sticky notes — keep this slide breathy, less crowded) ===

YELLOW sticky note (upper-left):
"NO PERFECT"
"only shipped"
"or not shipped"

LIGHT BLUE sticky note (lower-right):
"START SMALL"
"1 phase"
"1 rule"
"1 commit"

=== BOTTOM CENTER — Stats Row ===
Skip the stats row on this slide — keep visual breathing room around the quote. Replace with a single horizontal line of 3 small star doodles.

=== BOTTOM RIGHT — Branding ===
[Standard branding block]
Tiny "→ swipe for the framework" with a small sketched arrow

=== STYLE — CRITICAL ===
The big quote is the visual hero. Generous whitespace around it. Don't crowd this slide — it's the breath before the CTA. The "DO ONE THING TODAY" callout is the second visual anchor.
```

---

### Slide 7 — CTA (Comment + Follow + Share)

```
[paste STYLE CONSTANTS]

═══ SLIDE 7 OF 7 — CTA ═══

=== TOP TITLE BAR ===
Hand-written bold title: "WANT THE FULL FRAMEWORK?"
Below it, smaller handwritten subtitle: "[FRAMEWORK SIZE, e.g., '170 files · MIT licensed · everything I use to ship']"
Cyan marker underline under the title.
TOP-RIGHT: "AiwithDhruv" cyan badge + "Slide 7 of 7" written below.

=== CENTER — THE CTA HERO (largest section) ===
A LARGE hand-drawn box in the center of the page (rounded corners, slightly imperfect, drawn in bold black marker). Inside the box, in big handwritten letters with cyan marker:

"COMMENT  →  [CTA WORD, default 'FRAMEWORK']"

Below "[CTA WORD]" inside the same box, in smaller handwriting:
"I'll DM you the full .md file"

A bold cyan marker arrow OUTSIDE the box pointing INTO the box (entering from the left). Thick imperfect strokes.

To the RIGHT of the box, a sketched smiley face doodle giving a thumbs up. Tiny cyan highlight on the thumbs up.

=== LEFT COLUMN — "WHAT'S INSIDE" ===
Header: "WHAT'S INSIDE THE FRAMEWORK" inside a hand-drawn box
6-8 handwritten items with cyan checkmarks and tiny sketched icons:
   ✓ [Item 1]    (sketched icon)
   ✓ [Item 2]    (sketched icon)
   [continue]

=== RIGHT COLUMN — "3 SMALL ASKS" ===
Header: "3 SMALL ASKS" inside a hand-drawn box

Three handwritten asks, each with a hand-drawn number circle and an icon:

1. "COMMENT '[CTA WORD]'"    (sketched speech-bubble icon)
   "for the .md file"

2. "FOLLOW @aiwithdhruv"     (sketched bell-with-plus icon)
   "for the next 4 systems"

3. "SHARE w/ 1 founder"      (sketched share-arrow icon)
   "who's stuck rebuilding what's already built"

Cyan marker underline under "[CTA WORD]", "FOLLOW", and "SHARE".

=== POLAROID PHOTO (NEW — improved over slide-5 portrait of v1) ===
Bottom-right corner: a small REAL Polaroid-style photo of Dhruv (use his actual photo, with rounded white border + small caption strip below) physically taped to the notebook page with two pieces of washi tape at the corners. The Polaroid is tilted ~7° clockwise like it was just placed there.
Caption strip below the Polaroid (handwritten on the white border):
"— Dhruv, see you in the DMs"

If a real photo of Dhruv is not available in the prompt context, fall back to the hand-sketched portrait per handdrawn-diagram skill author-portrait formula.

=== FLASH CARDS scattered (3-4 sticky notes) ===

YELLOW sticky note (upper-left):
"FREE"
"MIT licensed"
"no email gate"
Small sketched unlocked-padlock doodle.

LIGHT BLUE sticky note (mid-right):
"[FRAMEWORK SIZE]"
"battle-tested"
"on [N] shipped systems"
Small sketched .md document icon.

PINK sticky note (lower-left):
"FAILURE LEDGER"
"= the moat"
"can't be copied"
Small sketched lock icon.

LIGHT GREEN sticky note (lower-right):
"PAY IT FORWARD"
"if it saves you a week"
"share w/ 1 founder"
Small sketched gift-box doodle.

=== BOTTOM CENTER — Stats Row ===
Three items in a row, each circled with yellow highlight:
"[Free / size]"     "[License / access]"     "[Cost to use]"
Small star doodles around each stat.

=== BOTTOM RIGHT — Branding (LARGER on this slide) ===
"AiwithDhruv" + cyan lightning bolt
"@aiwithdhruv  ·  github.com/aiagentwithdhruv"
"AD" monogram in a hand-drawn circle
"— Dhruv" handwritten signature with a small flourish

=== STYLE — CRITICAL ===
The "COMMENT → [CTA WORD]" box is the conversion magnet. First thing the eye lands on after the headline. Big, bold, surrounded by whitespace. The arrow pointing into the box is the second focal point. Polaroid is the third. Everything else supports the conversion ask.

Polaroid integration: the photo must look like a real polaroid printed and taped to the notebook page — visible rounded white border, slight grain, real shadow from the page lighting. NOT a digital frame. NOT a sketch. A real photo of Dhruv if available.
```

---

## The Post Copy Formula

LinkedIn post copy that goes WITH the carousel. The carousel is the visual; the post copy is the hook + thesis + CTA.

```
[HOOK — 1-2 lines, brutal honest claim or counterintuitive truth]

[CONTEXT — 2-3 lines, what credibility lets you make this claim]

[TENSION — 1-2 lines, what most teams get wrong]

[REVEAL — 1 line, "Six things separated shipping from stalling:"]

1. [Phase line — what slide 2 covers, in 1 line]
2. [Workflow line — what slide 3 covers, in 1 line]
3. [Team line — what slide 4 covers, in 1 line]
4. [Earned-rules line — short]
5. [Failure-ledger line — short]
6. [Scaffold line — short]

[CONSEQUENCE — 1 line, e.g., "It's the difference between code that runs and code that ships."]

[OFFER — 2-3 lines, what's in the framework, why it's free, the ask]

Comment "[CTA WORD]" below and I'll DM you the full end-to-end .md file.

[CLOSER — 1 line, pay it forward / honest signoff]

— Dhruv
```

**Word count target:** 220-280 words. Anything over 300 starts to lose mobile-feed retention.

**Format rules:**
- One sentence per line for first 5 lines (mobile readability)
- One blank line between every paragraph
- Use Unicode em-dash "—" sparingly (1-2 per post max)
- No emojis in body copy (B2B audience, breaks the serious-builder tone)
- Hashtags: 3-5 max, all relevant. Default: #BuildInPublic #AIwithDhruv #ClaudeCode

---

## Algorithm-Aware Posting Strategy

Researched April 2026 LinkedIn algorithm. Three rules drive distribution:

**Rule 1 — Click-through must stay above 35% per slide.**
Below that = visibility penalty. The 7-slide format is calibrated to keep momentum: each slide has one strong visual element + minimal text + a "→ swipe for [next]" arrow at the bottom-right.

**Rule 2 — Dwell time is the algorithm's primary signal.**
Each swipe = dwell time = distribution boost. The 7-slide format generates 18% more reach than 5-slide because of cumulative dwell.

**Rule 3 — Document/PDF posts get 2.1x engagement vs image carousels.**
Always upload as a PDF document post (combine the 7 slides in Canva → export as PDF → upload to LinkedIn as document). LinkedIn renders PDFs as native carousels with better algorithm treatment than image-by-image carousels.

### First-hour playbook (where the algorithm decides if you go viral or die)

| Time | Action |
|------|--------|
| T+0 to T+15 min | Reply to every comment with a substantive 2-3 line answer. NOT "thanks!" |
| T+15 to T+30 min | DM 5-10 trusted founders/peers with: "Posted this 30 min ago, would love your honest reaction." |
| T+30 to T+60 min | Post YOUR OWN comment adding a 9th item to "WHAT'S INSIDE THE FRAMEWORK" — bumps comment count + gives latecomers a reason to react |
| T+1 to T+24 hr | Reply to every "[CTA WORD]" comment within 60 min with the .md file via DM |

### Day, time, cadence

- **Day:** Tuesday OR Wednesday (not Monday, not Friday — both are noise / disengagement days)
- **Time:** 9:00-10:30 AM IST (catches India morning + EU late-night + US prep window)
- **Cadence:** 1 carousel per week, same day every week, builds anticipation
- **Pin to profile** for 7 days minimum (compounds via profile-view discovery)

### The DM script (write once, paste forever)

```
Hey {first name} 👋

Here's the full framework as a single .md file — paste it into Cursor / Claude Code / Windsurf and it just works.

[attach: aiwithdhruv-{topic}-framework.md]

If it saves you time, the only ask is: share with one other founder who'd benefit. That's how this stays free.

Building anything specific? Happy to point you to the right section.

— Dhruv
```

### Cross-platform 24-hour cycle

| T+ | Platform | Action |
|----|----------|--------|
| T+0 | LinkedIn | Carousel post goes live (PDF document) |
| T+2 hrs | X / Twitter | Screenshot Slide 1 → post with same hook + "full breakdown on LinkedIn" link |
| T+4 hrs | Instagram | Slide 4 (the team/stack) → post with same CTA |
| T+24 hrs | YouTube | 2-min Short reading the thesis aloud + screen-share of the carousel |
| T+48 hrs | LinkedIn | Follow-up post: "[N] of you asked for the framework. Here's the most-asked-about section: [single deep dive]" |

---

## Recommended Improvements (Researched + Iterated)

These are the upgrades baked into THIS skill that go beyond the original v1 carousel:

### 1. Real Polaroid photo on Slide 7 (NEW)
Instead of a hand-sketched portrait (risk: looks generic AI-illustration), use a REAL photo of Dhruv styled as a Polaroid taped to the notebook page. Best of both worlds — real face for trust + on-brand notebook aesthetic. Hand-sketched portrait is the fallback only if no real photo is in context.

### 2. Episode numbering (NEW)
Every carousel gets a continuous "Diary #N" number in the top-right of Slide 1. Builds sequence/anticipation — viewers start to track the series.

### 3. Color-anchored sticky notes (NEW)
Each slide gets ONE signature sticky note color as a recognition anchor:
- Slide 1: yellow (hero feature)
- Slide 2: light blue (tech/methodology)
- Slide 3: pink (data/persistence/rules)
- Slide 4: light green (team/quantity)
- Slide 5: light purple (proof/connections)
- Slide 6: yellow (lesson — full circle to slide 1)
- Slide 7: all 4 colors (CTA — maximum visual signal)

### 4. Spiral binding on left edge (NEW)
Every slide gets visible spiral notebook ring binding on the LEFT EDGE. Repeated motif across all 7 slides → makes the carousel feel like ONE notebook viewers are flipping through.

### 5. Slide-specific swipe arrow (NEW)
Each slide's bottom-right has a "→ swipe for [next slide topic]" annotation. Drives click-through above the 35% algorithm threshold.

### 6. Stats row standardization (NEW)
Every slide except slide 6 has a 3-stat row at the bottom center. Yellow highlighter behind each, hand-drawn circles. Skipping the stats row on Slide 6 (the lesson) gives that slide visual breathing room — makes the quote land harder.

### 7. PDF document upload (NEW)
Combine the 7 slides in Canva → export as PDF → upload to LinkedIn as document post (NOT as 7 separate images). Researched advantage: 2.1x engagement, 3.4x reach, 27% higher completion rate vs image carousels.

### 8. The "→ SHIP" anchor on Slide 1 + Slide 2
Both slides end with the same hand-drawn "→ SHIP" arrow + rocket doodle. Repeated visual rhyme = recognition.

---

## Composable With

| Skill | When to use together |
|-------|---------------------|
| `handdrawn-diagram` | For single-image hero diagrams (README, YouTube thumbnail). This carousel skill is the long-form weekly version of handdrawn-diagram. |
| `thumbnail-generator` | For the YouTube companion video's cinematic thumbnail (different aesthetic — cinematic photo, not handdrawn). |
| `nano-banana-images` | If a slide needs a hyper-realistic photo element (e.g., the Slide 7 Polaroid photo). |
| `social-media-agent` | For automated cross-posting to X, Instagram, YouTube via Blotato. |
| `linkedin-content` | For shorter standalone posts (single image, no carousel) — different format. |

---

## Process (Every Time)

1. **Identify the topic** — what one lesson / methodology / system is the focus?
2. **Confirm the 9 inputs** — see "Required Inputs" above. Ask before drafting.
3. **Write the post copy** — using the formula above. Hook + 6 separators + CTA. Show Dhruv for approval BEFORE generating slides.
4. **Generate Slide 1** — show Dhruv for approval. If it lands, generate Slides 2-7.
5. **Save all 7 slide prompts** to a single MD file at `/tmp/{topic}-carousel-{date}.md` for easy copy-paste into Gemini.
6. **Wait for Dhruv** to generate each slide image in Gemini and review them as a set.
7. **Combine in Canva** as a 7-slide PDF document (free) → upload to LinkedIn as document post.
8. **Schedule** for next Tuesday OR Wednesday 9-10 AM IST via LinkedIn native scheduler.
9. **Run the first-hour playbook** when it goes live.
10. **Track metrics** for next week's iteration: comments, DM requests, profile visits, consulting inquiries converted.

---

## Schema

### Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `topic` | string | Yes | The one lesson/methodology/system to teach |
| `episode_number` | int | Yes | Continuous "Diary #N" count |
| `thesis` | array of 3 strings | Yes | The 3 thesis statements |
| `methodology` | object | Yes | The N-step framework with name + steps |
| `workflow` | object | Yes | The N-rule/N-gate workflow with name + rules |
| `team` | object | Yes | The N-agent/N-tool architecture with name + members |
| `proof` | object | Yes | One real shipped example with timeline + outcome + numbers |
| `lesson` | string | Yes | One sentence (8-15 words) takeaway |
| `cta_word` | string | No | Comment trigger word (default: "FRAMEWORK") |
| `polaroid_photo_path` | string | No | Path to real photo of Dhruv (default: hand-sketched fallback) |
| `revenue_disclosure_ok` | boolean | No | Default: false |

### Outputs

| Name | Type | Description |
|------|------|-------------|
| `post_copy` | string | LinkedIn post copy ready to paste |
| `slide_prompts` | array of 7 strings | Gemini-ready prompts for each slide |
| `dm_script` | string | Pre-filled DM template for "[CTA WORD]" commenters |
| `cross_platform_pack` | object | X tweet + Instagram caption + YouTube short script |
| `posting_checklist` | string | The first-hour playbook + cross-platform 24h cycle |

### Credentials

None required (generates prompts + copy, not images or actual posts).

### Cost

Free (prompt generation only — image generation via Gemini is free, posting via LinkedIn native is free).

---

## Why This Skill Exists

Every Sunday/Tuesday Dhruv has one new shipped system worth teaching. Without a structured pipeline:
- The lesson doesn't get packaged
- The post takes 3 hours of design work
- The visual style drifts week over week
- The carousel feels improvised, not branded

With this skill: ONE conversation produces ONE carousel post + 7 slide prompts + DM script + posting playbook + cross-platform pack. The visual style is locked. The format compounds.

50 carousels in, anyone evaluating Dhruv as a consultant or hire has scrolled through 50 weekly proofs of how he ships. That's a 100x stronger signal than any pitch deck.

The compounding play: each carousel is a public artifact of methodology. The DM funnel converts 1-3% of "FRAMEWORK" commenters into qualified consulting calls. At scale, this is the inbound engine.

---

## Quick Reference — File Locations

| Asset | Path |
|------|------|
| This skill | `aiwithdhruv-skills/linkedin-carousel-handwritten/SKILL.md` |
| Style reference | `handdrawn-diagram/SKILL.md` (sister skill) |
| Brand palette ref | memory: `brand_palette.md` |
| Team LinkedIn URLs | memory: `team_linkedin_profiles.md` |
| Content voice rule | memory: `feedback_content_voice.md` |
| Auto-publish rule | memory: `feedback_never_auto_publish.md` |
| Handwritten flow rule | memory: `feedback_handwritten_flow.md` |
| Output prompts location | `/tmp/{topic}-carousel-{YYYY-MM-DD}.md` |
| Polaroid photo source | `~/Downloads/dhruv-polaroid-headshot.jpg` (Dhruv to provide) |
