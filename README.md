<div align="center">

# AIwithDhruv Skills

**38 production-ready AI agent skills — one command installs all of them.**

[![Skills](https://img.shields.io/badge/skills-38-blueviolet?style=flat-square)](https://github.com/aiagentwithdhruv/skills)
[![Compatible](https://img.shields.io/badge/agents-40%2B-blue?style=flat-square)](https://agentskills.io)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![skills.sh](https://img.shields.io/badge/listed%20on-skills.sh-black?style=flat-square)](https://skills.sh/aiagentwithdhruv/skills)

Lead generation · Email automation · Browser automation · Video & content · Infrastructure

Built and battle-tested by [Dhruv Tomar](https://www.linkedin.com/in/aiwithdhruv/) — Applied AI Engineer & AI Automation Consultant

</div>

---

## Install

```bash
# Install all 38 skills
npx skills add aiagentwithdhruv/skills

# Install a specific skill
npx skills add aiagentwithdhruv/skills --skill scrape-leads

# Install globally (works across all your projects)
npx skills add aiagentwithdhruv/skills -g -a claude-code
```

Works with **Claude Code, Cursor, GitHub Copilot, Codex, Windsurf, Cline** and [40+ other agents](https://agentskills.io).

---

## What's Inside

### Lead Generation & Sales (8 skills)

| Skill | What it does |
|-------|--------------|
| [`scrape-leads`](scrape-leads/) | Scrape & verify business leads via Apify + LLM classification + Google Sheets output |
| [`gmaps-leads`](gmaps-leads/) | Google Maps B2B scraping with deep website enrichment & contact extraction |
| [`classify-leads`](classify-leads/) | LLM classification — SaaS vs agency, product vs service, any complex distinction |
| [`casualize-names`](casualize-names/) | Format names for cold email personalization (Bob not Robert, Acme not ACME Corp) |
| [`create-proposal`](create-proposal/) | Generate PandaDoc proposals programmatically from client data |
| [`upwork-apply`](upwork-apply/) | Automate Upwork job applications with tailored proposals |
| [`onboarding-kickoff`](onboarding-kickoff/) | Post-sale client onboarding — CRM update, welcome email, kickoff message, campaign setup |
| [`generate-report`](generate-report/) | Generate structured deliverable reports (PDF, markdown, Google Docs) |

### Email & Campaigns (6 skills)

| Skill | What it does |
|-------|--------------|
| [`gmail-inbox`](gmail-inbox/) | Manage multiple Gmail accounts with unified tooling — read, label, archive, search |
| [`gmail-label`](gmail-label/) | Auto-label and organize Gmail at scale with rule-based classification |
| [`instantly-campaigns`](instantly-campaigns/) | Create cold email campaigns in Instantly with A/B variants — from Google Sheet to live campaign |
| [`instantly-autoreply`](instantly-autoreply/) | AI-powered auto-replies for cold email inboxes |
| [`welcome-email`](welcome-email/) | Welcome email sequences for new leads or customers |
| [`send-telegram`](send-telegram/) | Send Telegram messages, alerts, and notifications programmatically |

### Content & Video (9 skills)

| Skill | What it does |
|-------|--------------|
| [`video-edit`](video-edit/) | Full toolkit — silence removal, auto-captions, vertical crop, YouTube clipping, compression |
| [`image-to-video`](image-to-video/) | Animate images with AI — Kling 3.0, Hailuo, Luma Ray3, Runway Gen-4.5, and 8 more |
| [`youtube-outliers`](youtube-outliers/) | Monitor YouTube competitors and track viral videos in any niche |
| [`cross-niche-outliers`](cross-niche-outliers/) | Find viral videos from adjacent niches to extract content hooks |
| [`title-variants`](title-variants/) | Generate YouTube title variants from outlier analysis — bulk output to Google Sheets |
| [`thumbnail-generator`](thumbnail-generator/) | AI image prompt generator for YouTube thumbnails, LinkedIn posts, course banners |
| [`recreate-thumbnails`](recreate-thumbnails/) | Face-swap thumbnails with AI — adapt any viral thumbnail to your face |
| [`pan-3d-transition`](pan-3d-transition/) | 3D parallax transitions for video content |
| [`nano-banana-images`](nano-banana-images/) | Batch AI image generation via Nano Banana API |

### Browser Automation (1 skill)

| Skill | What it does |
|-------|--------------|
| [`ghost-browser`](ghost-browser/) | Human-like browser automation — LinkedIn posting, web scraping, job applications, demos |

> See the full GitHub repo: [aiagentwithdhruv/ghost-browser](https://github.com/aiagentwithdhruv/ghost-browser) · 15 scripts · 3,000+ lines · anti-detection built in

### Research & Community (3 skills)

| Skill | What it does |
|-------|--------------|
| [`skool-monitor`](skool-monitor/) | Monitor Skool community posts for lead generation opportunities |
| [`skool-rag`](skool-rag/) | Build a RAG pipeline from Skool community content |
| [`literature-research`](literature-research/) | Deep academic and web research with synthesis and citation |

### Infrastructure & Deployment (5 skills)

| Skill | What it does |
|-------|--------------|
| [`aws-production-deploy`](aws-production-deploy/) | Full AWS deployment — Docker, ECR, ECS Fargate, ALB, ElastiCache, CloudWatch, Grafana |
| [`modal-deploy`](modal-deploy/) | Deploy Python services to Modal cloud in minutes |
| [`add-webhook`](add-webhook/) | Create Modal webhooks for n8n event-driven workflows |
| [`local-server`](local-server/) | Run a local orchestration server for development and testing |
| [`design-website`](design-website/) | AI-assisted website design and scaffold generation |

### Diagramming & Visuals (2 skills)

| Skill | What it does |
|-------|--------------|
| [`excalidraw-diagram`](excalidraw-diagram/) | Create Excalidraw diagrams from plain-English descriptions |
| [`excalidraw-visuals`](excalidraw-visuals/) | Advanced Excalidraw visuals — architecture diagrams, flowcharts, system designs |

### Utilities (4 skills)

| Skill | What it does |
|-------|--------------|
| [`mac-control`](mac-control/) | Control macOS applications and system via automation |
| [`whisper-voice`](whisper-voice/) | Local speech-to-text transcription with Whisper — no cloud, no cost |
| [`skill-builder`](skill-builder/) | Scaffold new skills following this library's standard format |
| [`euron-qa`](euron-qa/) | QA automation for the Euron learning platform |

---

## How Skills Work

Each skill is a `SKILL.md` file with YAML frontmatter + instructions. When you install a skill, your AI agent reads the frontmatter at startup and activates the skill automatically when the task matches.

```
scrape-leads/
├── SKILL.md          ← Frontmatter + step-by-step instructions
└── scripts/
    ├── scrape_apify.py
    ├── classify_leads_llm.py
    ├── enrich_emails.py
    └── update_sheet.py
```

No config files. No build steps. No package.json. Just drop the folder in `.claude/skills/` and it works.

---

## Composition Chains

Skills are designed to chain together. Common pipelines:

```
# Full client onboarding
gmaps-leads → classify-leads → casualize-names → instantly-campaigns → welcome-email

# Content pipeline
cross-niche-outliers → title-variants → thumbnail-generator → video-edit

# Lead enrichment
scrape-leads → classify-leads → casualize-names

# Inbox management
gmail-inbox → gmail-label
```

---

## Author

**Dhruv Tomar** — Applied AI Engineer & AI Automation Consultant

- LinkedIn: [linkedin.com/in/aiwithdhruv](https://www.linkedin.com/in/aiwithdhruv/)
- GitHub: [github.com/aiagentwithdhruv](https://github.com/aiagentwithdhruv)
- YouTube: [youtube.com/@aiwithdhruv](https://www.youtube.com/@aiwithdhruv)

---

## License

MIT — use freely, contribute back.
