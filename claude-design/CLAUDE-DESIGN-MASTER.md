# Claude Design — Complete Reference & Prompting Guide

> **Source:** Two YouTube transcripts (April 2026)
> - Video 1 (`_0fvC-9TjIk`): Full Claude Design walkthrough — features, UI, export, limits
> - Video 2 (`TcFeSjwTo7g`): Live build — landing page in 20 minutes with video background
> **Use this:** Paste into any Claude session before designing UI. Or run `/claude-design` to invoke.

---

## What Is Claude Design?

A new product from Anthropic that solves the **design consistency problem** in vibe coding. Before Claude Design, every project you spun up had its own random aesthetic. Claude Design lets you:

1. **Create a design system** (colors, fonts, components, spacing) — from scratch or from existing code
2. **Generate any design** (website, web app, mobile app, slide deck, Instagram image) using that design system
3. **Export the design** as HTML/CSS/JS prototype, PDF/PPT, Canva file, or hand off to Claude Code

**Critical distinction:** Output is a **prototype**, not production code. You still need to convert HTML/CSS to React/Vue/native. Slides export as-is.

---

## The Two Object Types

| Type | Color | Purpose |
|------|-------|---------|
| **Design System** | Orange | The reusable visual language (colors, type, components) |
| **Design** | Gray | A single artifact (page, deck, app screen) using a design system |

You create design systems in `Design Systems` tab. You create designs anywhere — but tying them to a system gives consistency.

---

## How to Create a Design System

Inputs you can give (only Company Name + Blurb is required):

1. **Text:** Company name + what you want to build (website + mobile app, etc.)
2. **GitHub repo:** Claude reads existing code, extracts design tokens
3. **Local code folder:** Drag UI folder, Claude extracts patterns
4. **Figma file:** Attach for visual extraction
5. **Brand assets:** Logo (fastest win — colors auto-extracted), fonts, images

**Quickest win:** Drop your logo. Claude pulls colors from it automatically.

After generation, you get:
- A sample page (landing page if that's what you asked for)
- All UI components (buttons, badges, headings, cards) shown individually
- Review each: ✓ "Looks good" or "Needs work" with description
- Code organized by components + readme + page

---

## 5 Ways to Edit a Design

| # | Method | When to Use |
|---|--------|-------------|
| 1 | **Prompt** (left panel) | Big structural changes ("make heading smaller") |
| 2 | **Edit mode** | Direct visual tweaks — click element, change font/color/size. No AI involved. Applies to code instantly. |
| 3 | **Comment mode** | Single comment → send to Claude, OR batch multiple comments → send all at once |
| 4 | **Tweak** | Fine-grain control for things not in edit panel (letter spacing, full color scheme switch). Replaces what a designer would do in Figma. |
| 5 | **Draw mode** | Sketch on the page, type instruction, Claude takes screenshot + applies change |

---

## Export Options

### For Web Designs (HTML/CSS/JS)
- **Download as ZIP:** Includes README with agent instructions for production conversion
- **Standalone HTML:** Removes React build dependency — single file works directly
- **Handoff to Claude Code:** Generates a single prompt that fetches design files + reads README + implements in your existing repo
- **Send to Claude Code Web:** Cloud version (less common)

### For Slides
- **Direct PDF / PPT export** — production-ready
- **Send to Canva** — edit there

**Important:** Web prototypes use React under the hood with build step. Not production code. You must reimplement in your real stack.

---

## Usage Limits (Critical)

- **Claude Design has its own quota** — separate from Claude.ai and Claude Code
- Even on **Max ($200/mo)** plan, limits run out fast (creator hit limit after 4 design systems + 3 designs)
- Resets weekly (Tuesdays)
- Currently in testing phase — limits expected to merge with main usage later

**Plan accordingly:** Don't waste tokens on small iterations. Use edit mode (no AI) for visual tweaks.

---

## The 20-Minute Workflow (Video 2 — Real Build)

### What was built
Transformed AI Automation Society website with parallax-style scrolling, 3D card sections, video hero background.

### Step-by-step pattern

**Step 1: Define brand & vibe (use Claude.ai chat first)**
- Describe product, audience, mood
- Ask Claude for: image prompt + video prompt for hero background
- Generate image with Nano Banana 2 (16:9 ratio)
- Animate with Kling 2.0 (use image as first + last frame, no camera movement)

**Step 2: Open Claude Design → New Prototype → High-fidelity**
- Choose "no design system" if starting fresh brand
- Name it (e.g., "LOL website")

**Step 3: Sketch the hero (optional but powerful)**
- Use draw mode to sketch boxes: hero video bg, hero text, subtext, navbar (logo, shop)
- Label each box — Claude reads sketch literally

**Step 4: Drag in MP4**
- Cap: ~30-40MB, ~15-20 seconds max
- Will auto-loop in hero

**Step 5: Paste brand identity text**
- Visual identity, sections, footer, color guidance, copy tone
- ~20-30 lines of context

**Step 6: Send & iterate**
- Claude scaffolds full page
- Refine with the 5 edit methods

---

## Master Prompt Template (Copy-Paste)

```
I'm building [PRODUCT TYPE — landing page / SaaS dashboard / mobile app / slide deck].

BRAND:
- Name: [name]
- Audience: [audience]
- Vibe: [3 adjectives — e.g., "calm, premium, sleepy"]
- Colors: [hex codes or "extract from attached logo"]
- Typography: [serif / sans / mono / specific font]

ASSETS PROVIDED:
- [Logo file]
- [Hero video MP4 — describe what it shows]
- [Sketch of hero layout]
- [Brand identity text — pasted as artifact]

PAGE STRUCTURE:
1. Hero — full-bleed video background, headline left, CTA below
2. [Section 2 — e.g., "feature grid 3-column with 3D card hover"]
3. [Section 3 — e.g., "social proof carousel"]
4. [Section 4 — e.g., "pricing 3 tiers"]
5. Footer — minimal, brand mark + 4 links

INTERACTIONS:
- Scroll-triggered animations on cards
- Smooth parallax on hero
- Hover states with subtle lift

COPY:
- Write all copy yourself in [brand voice — e.g., "warm, conversational, no jargon"]
- Headline ≤ 8 words
- Subtext ≤ 20 words

OUT OF SCOPE:
- No newsletter signup forms
- No lengthy "About" section
- No stock photo people

Build the full page. If you have ambiguity, ask before assuming.
```

---

## Design System Prompt Template

```
Create a design system for [COMPANY NAME].

CONTEXT:
- Industry: [e.g., wellness tea brand]
- Vibe: [3 adjectives]
- Target: [website + mobile app / web app + slide deck]

EXTRACT FROM:
- Logo: [attached]
- Existing code: [GitHub repo URL OR Figma OR drag folder]

OUTPUT NEEDED:
- Color palette (primary, secondary, accent, neutrals, semantic states)
- Typography scale (display, h1-h6, body, caption, mono)
- Spacing scale (4px multiples)
- Component library (button variants, input states, card styles, badges, modals)
- Sample landing page using all of the above
```

---

## When to Use Claude Design vs Alternatives

| Tool | Best For | Avoid When |
|------|---------|-----------|
| **Claude Design** | Brand-consistent prototypes across web + slides + mobile, design system extraction from existing code | You need production React app from one prompt (use Bolt/Lovable/v0) |
| **v0.dev** | Quick shadcn/ui React components | You want full design system, not just components |
| **Lovable** | One-shot full-stack apps | You need design consistency across multiple artifacts |
| **Figma + Claude Code** | Pixel-perfect handoff to dev | You don't have a designer |
| **Bolt.new** | Full-stack starter projects | You want design polish first |

---

## Karpathy Rules Applied to Claude Design

1. **Don't assume** — If brand vibe is unclear, ask before generating. Show 3 directions.
2. **Don't hide confusion** — Flag missing assets ("I don't have a logo — should I generate placeholder colors or wait?")
3. **Surface tradeoffs** — "I can match your existing code 1:1 (boring) or evolve the system (risk: feels different). Which?"
4. **Minimal diffs** — When editing, change ONLY what was asked. Don't restyle other sections.
5. **No unintended modifications** — If user comments on hero, don't touch footer.

---

## How Beneficial Is This?

**For our products (IndianWhisper, Angelina, QuotaHit, DWERP):**

| Use Case | Time Saved | Quality |
|----------|-----------|---------|
| IndianWhisper landing page V2 | 20 min vs 2 days | Higher polish |
| QuotaHit dashboard redesign | 1 hr vs 1 week | Consistent across 32 pages |
| AIwithDhruv portfolio refresh | 30 min vs 4 hrs | Brand-locked |
| MSBC client pitch decks | Generate from existing brand | Visual consistency across 5 decks |
| Workshop slides ($149 product) | 15 min vs 3 hrs | Looks expensive |

**Key win:** Once you create a design system from one product (e.g., AIwithDhruv brand), every future asset (slides, blog headers, app screens, social cards) inherits the same visual language. **Brand consistency at zero marginal effort.**

**Limitation:** Output isn't production code for web. Slides export clean. Web needs reimplementation. Treat it as a high-fidelity prototype tool, not a deploy-ready code generator.

---

## Workflow Recipe for IndianWhisper Launch (44-Day Sprint)

```
Day 1:
  - Open Claude Design
  - Create design system from indianwhisper.com existing code
  - Approve component library

Day 2:
  - Generate: Product Hunt gallery image
  - Generate: 5 social cards (LinkedIn, Twitter, Instagram, YouTube thumbnail, Reddit banner)
  - Generate: 3-slide pitch deck for Deepgram sponsor outreach
  - Generate: Workshop landing page ("Build AI Agents in a Weekend")

Day 3:
  - Refine + export
  - Hand off web items to Claude Code for production conversion
  - Slides used as-is

Total time: ~6 hours for ~15 brand-consistent assets that would take 2 weeks manually.
```

---

## Quick Reference Card

```
CREATE DESIGN SYSTEM:
  Design Systems tab → Create → drop logo + paste blurb → wait

CREATE DESIGN:
  Designs tab → Create → select system from dropdown → prompt

EDIT:
  Prompt | Edit (no AI) | Comment (single/batch) | Tweak (fine-grain) | Draw (sketch)

EXPORT:
  Web: ZIP / Standalone HTML / Handoff to Claude Code
  Slides: PDF / PPT / Canva

LIMITS:
  Separate from Claude Code quota. Even Max plan is tight. Resets Tuesdays.
```

---

*Compiled from full transcripts of both videos. Use this file as the system context anytime you're using Claude Design.*
