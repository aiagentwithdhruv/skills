# AIwithDhruv — Agent Skills Library

> 38 production-ready AI agent skills for lead generation, email automation, content creation, browser automation, and infrastructure deployment.

Built and battle-tested by [Dhruv Tomar](https://www.linkedin.com/in/aiwithdhruv/) — Applied AI Engineer & AI Automation Consultant.

## Install

```bash
# Install a specific skill
npx skills add aiagentwithdhruv/skills --skill scrape-leads

# Install all skills
npx skills add aiagentwithdhruv/skills
```

Works with Claude Code, Cursor, Copilot, Codex, and [40+ other agents](https://agentskills.io).

---

## Skills (38)

### Lead Generation & Sales
| Skill | Description |
|-------|-------------|
| [scrape-leads](scrape-leads/) | Scrape & verify business leads via Apify + LLM classification + Google Sheets |
| [gmaps-leads](gmaps-leads/) | Google Maps B2B lead scraping with website enrichment & contact extraction |
| [classify-leads](classify-leads/) | LLM-based lead classification (SaaS vs agency, product vs service) |
| [casualize-names](casualize-names/) | Format names for personalized outreach (Bob not Robert) |
| [create-proposal](create-proposal/) | Generate PandaDoc proposals programmatically |
| [upwork-apply](upwork-apply/) | Automate Upwork job applications with tailored proposals |
| [onboarding-kickoff](onboarding-kickoff/) | Post-sale client onboarding automation |
| [generate-report](generate-report/) | Generate structured deliverable reports |

### Email & Campaigns
| Skill | Description |
|-------|-------------|
| [gmail-inbox](gmail-inbox/) | Manage multiple Gmail accounts with unified tooling |
| [gmail-label](gmail-label/) | Auto-label and organize Gmail at scale |
| [instantly-campaigns](instantly-campaigns/) | Create cold email campaigns in Instantly with A/B testing |
| [instantly-autoreply](instantly-autoreply/) | AI-powered auto-replies for cold email inboxes |
| [welcome-email](welcome-email/) | Welcome email sequences for new leads or customers |
| [send-telegram](send-telegram/) | Send Telegram messages and alerts programmatically |

### Content & Video
| Skill | Description |
|-------|-------------|
| [video-edit](video-edit/) | Full video editing — silence removal, captions, vertical crop, compression |
| [image-to-video](image-to-video/) | Animate images with AI — Kling, Hailuo, Luma, Runway, and 8 more tools |
| [pan-3d-transition](pan-3d-transition/) | 3D parallax transitions for video content |
| [recreate-thumbnails](recreate-thumbnails/) | Face-swap thumbnails with AI |
| [cross-niche-outliers](cross-niche-outliers/) | Find viral videos across niches for content strategy |
| [youtube-outliers](youtube-outliers/) | Monitor YouTube competitors and track viral videos |
| [title-variants](title-variants/) | Generate YouTube title variants from outlier analysis |
| [thumbnail-generator](thumbnail-generator/) | AI thumbnail generation pipeline |
| [nano-banana-images](nano-banana-images/) | Batch AI image generation via Nano Banana |

### Browser Automation
| Skill | Description |
|-------|-------------|
| [ghost-browser](ghost-browser/) | Human-like browser automation — LinkedIn, web scraping, job apps, demos |

### Research & Community
| Skill | Description |
|-------|-------------|
| [skool-monitor](skool-monitor/) | Monitor Skool community posts for lead opportunities |
| [skool-rag](skool-rag/) | Build a RAG pipeline from Skool community content |
| [literature-research](literature-research/) | Deep academic and web research with synthesis |

### Infrastructure & Deployment
| Skill | Description |
|-------|-------------|
| [add-webhook](add-webhook/) | Create Modal webhooks for n8n event-driven workflows |
| [modal-deploy](modal-deploy/) | Deploy Python services to Modal cloud |
| [local-server](local-server/) | Run a local orchestration server for testing |
| [aws-production-deploy](aws-production-deploy/) | Production AWS deployment (ECS, ECR, ALB) |
| [design-website](design-website/) | AI-assisted website design and scaffolding |

### Diagramming & Visuals
| Skill | Description |
|-------|-------------|
| [excalidraw-diagram](excalidraw-diagram/) | Create Excalidraw diagrams from descriptions |
| [excalidraw-visuals](excalidraw-visuals/) | Advanced Excalidraw visual creation |

### Utilities
| Skill | Description |
|-------|-------------|
| [mac-control](mac-control/) | Control macOS apps and system via automation |
| [whisper-voice](whisper-voice/) | Local speech-to-text transcription with Whisper |
| [euron-qa](euron-qa/) | QA automation for the Euron platform |
| [skill-builder](skill-builder/) | Scaffold new skills following this library's standard |

---

## About

These skills follow the [Agent Skills specification](https://agentskills.io). Each skill is:
- Self-contained (SKILL.md + optional scripts/)
- Production-tested across real client projects
- Compatible with Claude Code, Cursor, and 40+ agents

**Author:** Dhruv Tomar — [LinkedIn](https://www.linkedin.com/in/aiwithdhruv/) · [GitHub](https://github.com/aiagentwithdhruv) · [YouTube](https://www.youtube.com/@aiwithdhruv)

## License

MIT
