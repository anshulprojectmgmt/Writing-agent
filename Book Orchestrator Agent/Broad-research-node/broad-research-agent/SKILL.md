---
name: broad-research-skill-v3
description: Research a future-oriented nonfiction book chapter with a question-led map and all ten Source Ladder rungs. Curate 3–4 deep insights per verified article, preserve valuable original figures, and produce TWO polished standalone HTML research reports — source-first and question-first — using the same evidence. Use for research chapters, technology futures, agents, and Products of Tomorrow.
---

# Broad Research Skill v3 (two curated HTML outputs)

Produces two research-grade, polished, standalone HTML briefs from one source-grounded chapter research pass.
This is the **first step** of the book writing process.
Three phases: **A. Discovery and question map** → **B. Full-source curation and visual audit** → **C. Two HTML outputs (source-first, then question-first)**. Read `references/curated-research-dual-html-v3.md` BEFORE beginning; where it differs, its v3 rules override the legacy single-Doc rules.

---

## References

- `references/curated-research-dual-html-v3.md` — **mandatory v3 specification** for question-led discovery, per-article 3–4 curated insights, original article figures, source-quality gates, dual beautiful offline HTMLs, and quality tests. It overrides conflicting legacy output/length instructions.
- `references/book-profile.md` — defines audience (PMs), the four-pillar framework (Adaptive UX, Agents, Emotional Intelligence, Trust), and scope (personal-life product contexts).
- `references/writing-style.md` — defines voice ("smart friend over coffee"), jargon-explanation rules, analogy-first structure, sentence rhythm, and formatting constraints. Applies to this brief **in part, not in whole**: its "What to Avoid" rules apply everywhere (see Filler Control below), its craft principles apply only to the `WHY IT MATTERS` field of each finding's evidence card — and its Formatting Rules, humour and sentence-rhythm guidance do **not** apply here, because this is a reference document that gets scanned out of order, not book prose. Layout for the TWO required standalone HTML reports is governed by `references/curated-research-dual-html-v3.md`; `references/output-formatting.md` governs only an optional legacy Google Docs conversion.
- `references/output-formatting.md` — defines the **legacy Google Docs HTML** markup for the generated brief: how the Research Objective, the Query Map, and the Source Ladder Findings — each finding with its labels and evidence card merged in — must be marked up (never how the content is worded). This brief is delivered as HTML, not Markdown. CSS does not survive the Google Docs conversion, so all spacing comes from `<p>&nbsp;</p>` spacer paragraphs and never from `style` attributes. Use the legacy document converter rules only if the user separately requests a Google Doc; never for the mandatory standalone HTML reports.

---

## GenAI Lens *(standing rule — applies to every step below)*

This book's domain is generative AI, so every research pass — however broadly the chapter topic is phrased — must be anchored to the generative-AI-specific angle (naming current genAI companies, products, and terminology where a genuine one exists) rather than treated as a generic business/product topic.

---

# A. RESEARCH

---

## Adaptive Depth

Search ALL ten Source Ladder rungs in full chapter research; do not silently skip one. Attempt at least five genuinely strong, distinct sources per rung where available, but never pad with generic or weak articles. If fewer qualify, disclose the rung shortfall. For narrow requests, keep all rung headings and mark those not applicable. The v3 curation and image audit in `references/curated-research-dual-html-v3.md` determine which sources actually appear.

Keep source-quality labels, blind-spot checks, specific verifiable claims, and confidence assessments. Fit the final source-first explanation to 3–4 most useful insights per article (generally 200–260 words), rather than preserving all findings verbatim.

## Filler Control

Filler control is a **quality floor**, not a quantity ceiling.
The goal is to remove weak material — not to limit how many strong findings are reported.

**Preserve important insight, not every paragraph of the source.** Extract the full evidence privately, then show only the distinctive 3–4 insights a reader needs. Use editorial judgment; more text is not automatically greater depth.

Drop a finding only if it:
- Makes a generic claim with no named source, study, or example behind it
- Repeats something already captured in a stronger finding
- Is clearly marketing copy with no independent verification

**How a kept finding is written** — apply the "What to Avoid" rules from
`references/writing-style.md` to every finding of this brief, card fields included.
They are sourcing rules as much as style rules:
- **No hype language** ("revolutionary," "game-changing," "transformative") unless a specific named example immediately backs it.
- **No generic examples.** Name the company or drop the example — the same test as the first drop rule above.
- **No empty academic hedging.** State evidence limitations and uncertainty explicitly in the source interpretation and question synthesis; retain `CONFIDENCE` and `AUTHORITY` for the audit.
- **No passive inflation.** A claim has to stay checkable against its source.
- **Explain jargon on first use**, per the same file. The reader of this brief is the PM reader of the book.

**Per-rung research targets (quality gated):**
- Investigate at least five genuinely distinctive qualified sources per rung where they exist; if fewer exist, disclose the shortfall rather than padding.
- Rung 5: seek at least five distinct relevant major platform primary sources.
- Rung 6: seek at least five named, verifiable case studies.
- Each accepted source gets one source ID and a curated 3–4-insight card, not one card per trivial claim.

---

## Tools

Use available web search and full-page extraction tools, and inspect embedded figures/PDFs when needed. Prefer primary sources and original data. **Exa is OFF by default:** invoke Exa only when the user explicitly requests it for that research run. The user’s account may have different tools; adapt safely without assuming a particular provider.

---

## Step 1 — Ground Floor Check

> **"What products with real users are already doing some version of this — even partially, even under a different name?"**

List 3-5 named products. If nothing comes to mind, that is itself a signal.

**Check generative AI products specifically first** — ChatGPT, Claude,
Gemini, Copilot, and AI-agent features inside existing products — before
broadening to non-AI products, per the GenAI Lens rule above.

---

## Step 2 — Question Map (user-facing; NOT a query map)

After initial foundational research and named product examples, create two levels of FUTURE-FIRST research questions: (1) foundational user/problem/product/market questions, and (2) professional-role perspectives including PM, UXR, design, engineering, finance, economics, marketing/sales/distribution, risk/governance, and leadership. Each expert must examine the plausible future from their professional role, using real current examples and basic research. Include competing possible futures, uncertainties and disconfirming evidence. Use stable IDs (Q01 etc.). See `references/curated-research-dual-html-v3.md`.

Keep synonyms, technical, business, ethics, and contrarian search terms internally only as search scaffolding; **do not output a term map or query map**. Both HTML files are built from the resulting question map and common curated source evidence.

## Step 2 — Source Ladder

Run rungs in order. Higher rungs = more authoritative and citable.

**Rung 1 — Consulting & Analyst:** `[topic/synonyms] McKinsey OR BCG OR Gartner OR Forrester OR Deloitte OR IDC OR "451 Research" OR Omdia OR "CB Insights" 2024 2025 2026`

**Rung 2 — VC / Investor Research:** `[topic] site:a16z.com OR site:nfx.com OR site:sequoiacap.com OR site:radicalventures.com OR site:conviction.com`

**Rung 3 — Academic / Research:** `[topic/technical terms] site:arxiv.org OR site:acm.org OR site:scholar.google.com 2023 2024 2025`

Named venues to use for targeted queries (more citable than a generic arXiv search):
- **General AI/ML:** NeurIPS, ICML, ICLR, AAAI, IJCAI
- **NLP:** ACL, EMNLP, NAACL
- **Vision:** CVPR, ICCV, ECCV
- **HCI (relevant for PM/product chapters):** ACM CHI, CSCW
- **AI Ethics & Governance:** **FAccT** (ACM Conference on Fairness, Accountability, and Transparency) and **AIES** (AAAI/ACM AI, Ethics, and Society) — **highest-priority.** FAccT is the one venue that does double duty across this rung and Rung 7 (ethics/regulatory): it draws ML researchers, lawyers, sociologists, economists, and policymakers together, and corporate responsible-AI teams increasingly treat it as a barometer of external expectations.

**Rung 4 — Practitioner & Product:** `[topic/product terms] product manager OR UX OR engineering OR "how we built" 2024 2025`

**Rung 5 — Big Platforms & Major Products:** Primary voice preferred (founder blog, official blog, keynote transcript, earnings call)

Prioritise primary voice — the company or founder speaking directly — over press summaries. Run three targeted searches, not one generic one: official blog/news, founder/CEO voice, and vision/roadmap signals.

**Standing primary source checklist** — always scan these for AI-adjacent chapters:

**1. Official Company Blogs & News Pages**
| Company | URL |
|---|---|
| OpenAI | `openai.com/news` |
| Meta AI | `ai.meta.com/blog` |
| Google DeepMind | `deepmind.google/discover/blog` |
| Google AI | `blog.google/technology/ai` |
| Anthropic | `anthropic.com/news` |
| Microsoft AI | `blogs.microsoft.com/ai` |
| Amazon / AWS AI | `aws.amazon.com/blogs/machine-learning` |
| Apple ML | `machinelearning.apple.com` |
| xAI (Grok) | `x.ai/news` |
| Mistral | `mistral.ai/news` |
| NVIDIA | `blogs.nvidia.com` |
| Salesforce (Agentforce) | `salesforce.com/news` |
| Databricks | `databricks.com/blog` |
| Hugging Face | `huggingface.co/blog` |
| DeepSeek | `deepseek.com` |
| Moonshot AI (Kimi) | `moonshot.cn` |
| Zhipu AI | `zhipuai.cn` |
| Alibaba Qwen | `qwenlm.github.io` |

**2. Founder & CEO Personal Writing**
| Person | Company | Where they write |
|---|---|---|
| Sam Altman | OpenAI | `blog.samaltman.com` |
| Dario Amodei | Anthropic | `darioamodei.com` |
| Mark Zuckerberg | Meta | Threads / Facebook posts + Meta blog |
| Satya Nadella | Microsoft | LinkedIn + Microsoft Blog |
| Demis Hassabis | Google DeepMind | DeepMind blog (rare essays) |
| Sundar Pichai | Alphabet/Google | `blog.google` + keynotes |
| Elon Musk | xAI | `twitter.com/elonmusk` |
| Jensen Huang | NVIDIA | NVIDIA blog + keynote transcripts |
| Yann LeCun | Meta AI | `twitter.com/ylecun` + academic papers |
| Andy Jassy | Amazon | `aboutamazon.com/news` + shareholder letters |
| Arthur Mensch | Mistral | `mistral.ai` + interviews |

**3. Long-Form Interviews & Podcasts**
| Podcast | Notable guests | Where to find |
|---|---|---|
| Lex Fridman Podcast | Altman, Zuckerberg, Hassabis, Musk, LeCun | `lexfridman.com/podcast` |
| Dwarkesh Patel Podcast | Altman, Zuckerberg, Amodei, LeCun | `dwarkeshpatel.com` |
| No Priors (Sarah Guo + Elad Gil) | OpenAI, Anthropic, Google leaders | Apple / Spotify |
| 20VC (Harry Stebbings) | AI CEOs and investors | `thetwentyminutevc.com` |
| The Logan Bartlett Show | AI founders | Spotify / Apple |
| Hard Fork (NYT — Roose & Metz) | AI executives | NYT Podcasts |
| Eye on AI (Craig Smith) | Researchers & executives | `eye-on.ai` |
| BG2 Pod (Gurley + Gerstner) | AI strategy + big tech | Spotify / Apple |
| Acquired | Company deep-dives incl. NVIDIA, OpenAI, Microsoft | Spotify / Apple / YouTube |
| All-In Podcast | Chamath, Sacks, Friedberg, Calacanis | Spotify / Apple / YouTube |

**4. Keynotes & Conference Talks**
| Event | Company | Where to find |
|---|---|---|
| OpenAI DevDay | OpenAI | `openai.com/events` + YouTube |
| Meta Connect | Meta | `metaconnect.com` + YouTube |
| Google I/O | Google | `io.google` + YouTube |
| Google Cloud Next | Google | YouTube |
| Microsoft Build | Microsoft | `build.microsoft.com` + YouTube |
| Amazon re:Invent | Amazon | YouTube |
| NVIDIA GTC | NVIDIA | `nvidia.com/gtc` + YouTube |
| TED / TED AI | All major companies | `ted.com/topics/artificial+intelligence` |
| World Economic Forum (Davos) | All CEOs | `weforum.org/videos` |

**5. Earnings Calls & Investor Relations**
| Source | Notes |
|---|---|
| Seeking Alpha | Full transcripts, searchable — `seekingalpha.com` |
| The Motley Fool | Cleaned-up transcripts — `fool.com/earnings` |
| Meta IR | `investor.meta.com` |
| Microsoft IR | `ir.microsoft.com` |
| Alphabet IR | `abc.xyz/investor` |
| Amazon IR | `ir.aboutamazon.com` |
| Apple IR | `investor.apple.com` |
| NVIDIA IR | `investor.nvidia.com` |
| Salesforce IR | `investor.salesforce.com` |
| Bloomberg / Reuters | Summary coverage with direct CEO quotes |

**6. Social Media & Real-Time Signals**
| Handle | Platform | Signal type |
|---|---|---|
| `@sama` (Sam Altman) | Twitter/X | Roadmap hints, philosophy |
| `@ylecun` (Yann LeCun) | Twitter/X | Technical debate, AI vision |
| Mark Zuckerberg | Threads | Meta product vision |
| `@DarioAmodei` | Twitter/X | Safety + capability framing |
| `@satyanadella` | Twitter/X + LinkedIn | Microsoft AI direction |
| `@demishassabis` | Twitter/X | DeepMind research framing |
| `@gdb` (Greg Brockman) | Twitter/X | OpenAI engineering vision |
| `@karpathy` (Andrej Karpathy) | Twitter/X | Deep technical + product thinking |

**7. Policy, Testimony & Regulatory Documents**
| Source | Where to find |
|---|---|
| US Senate / House AI hearings | `congress.gov` + YouTube |
| EU AI Act consultations | `digital-strategy.ec.europa.eu` |
| White House AI materials | `whitehouse.gov/ostp` |
| FTC AI reports | `ftc.gov/reports` |
| Company safety/policy papers | `anthropic.com/policy`, `openai.com/safety` |
| OECD AI Policy Observatory | `oecd.ai` |
| UK AI Security Institute (AISI) | `aisi.gov.uk` |
| G7 Hiroshima AI Process | g7hiroshima-ai-process reporting via OECD |

**8. Research Papers & Technical Blogs**
| Source | URL |
|---|---|
| arXiv AI section | `arxiv.org/list/cs.AI/recent` |
| Google Research | `research.google/pubs` |
| Meta AI Research | `ai.meta.com/research` |
| OpenAI Research | `openai.com/research` |
| Anthropic Research | `anthropic.com/research` |
| Microsoft Research | `microsoft.com/en-us/research` |
| Hugging Face Papers | `huggingface.co/papers` |

**9. Tier-1 Tech Journalism** *(secondary — use for corroboration, not primary source)*
| Publication | Notes |
|---|---|
| The Information | Deep sourced enterprise AI reporting |
| Wired | Long-form features on AI companies |
| MIT Technology Review | Research + commercial AI intersection |
| The Verge | Consumer AI products + executive interviews |
| Bloomberg Technology | Business + strategy framing |
| Financial Times | Executive quotes + regulatory angle |

**Rung 6 — Case Studies:** `[topic/product terms] case study OR "lessons learned" OR "what we shipped" 2023 2024 2025`

**Rung 7 — Ethics / Regulatory:** `[topic/ethics terms] privacy OR consent OR governance OR regulation 2024 2025`

**Rung 8 — Trend & Futures:** `[topic/business terms] future OR roadmap OR "next 3 years" OR prediction 2025 2026`

**Rung 9 — Newsletters & Long-form:** `[topic/synonyms] Substack OR newsletter OR "things I've learned"`

Named newsletters worth anchoring queries around:
- **Lenny's Newsletter** — the readership overlaps directly with a PM-audience book; useful for both content and "what does this audience already believe" framing
- **Ben's Bites** — AI/founders angle, strong on cap-table and moat framing
- **Latent Space** — AI-engineer community, technical depth
- **Import AI** (Jack Clark) / **Interconnects** (Allen Institute) — research-practitioner crossover
- **The Pragmatic Engineer** (Gergely Orosz) — engineering-culture angle

**Rung 10 — General / Recent News:** `[topic] 2025 OR 2026` — run only if material gaps remain.

---

## Step 3 — Source Quality Labels

For every finding, add a label line inline, directly under the finding's title:
```
SOURCE TYPE: Primary / Academic / Analyst / VC / Practitioner / News / Company Marketing / Opinion
AUTHORITY: High / Medium / Low
FRESHNESS: {actual publication date}
USE: Cite / Background / Ignore
```

The labels live on the finding itself. There is no separate Source Quality
Labels section in the output.

---

## Step 3b — Blind Spot Check

> **"What major product, company, platform, or pattern is NOT in my research that a senior PM in this space would immediately name?"**

Run one targeted search. Anything it surfaces that passes Filler Control is
added as a finding in the rung its source belongs to — with its own labels and
evidence card fields, numbered like every other finding in that rung. There is
no separate Blind Spot Check section in the output. If nothing surfaces,
nothing is added.

---

## Step 4 — Source evidence, deep reading, and curation

Retain the evidence card fields for internal auditing (specific CLAIM; WHY IT MATTERS; CONFIDENCE; source-quality metadata and URL). Deep-read selected full articles, collect important structures, figures, comparisons, and caveats; then publish only their 3–4 highest-value insights with meaningful explanation. A selected **article** is the source-first unit (R1.1, R1.2, etc.), not a disconnected claim or a question. Capture original source images where relevant, and explain constraints if unavailable. Follow the complete `references/curated-research-dual-html-v3.md` protocol.

# B. TWO MANDATORY HTML OUTPUTS

The complete rendering and validation contract lives in `references/curated-research-dual-html-v3.md`. Apply it fully; these v3 instructions replace the old single-Google-Doc output contract.

### Output 1 — Source-first research
A polished self-contained HTML report organized **Rung 1–10 → Article ID → 3–4 curated, valuable explanatory insights → original relevant figures and useful tables → one brief future implication**. Present one article at a time with next/previous navigation; never organize this output by question. Retain all 10 rung identities, honest gap notes, exact source links, readable tables and original figure attribution.

### Output 2 — Question-first research
A **second, separately downloadable, polished self-contained HTML** organized **Foundational and professional-role question groups → each question answered directly and deeply**. Synthesize evidence ACROSS the same curated articles; retain the important article-level mechanisms, distinctions, frameworks, images and supporting data, disagreement and uncertainty. **Never degrade Output 2 to a short answer plus link list.** Question-first is not a rearrangement of article cards.

### Delivery and validation
- Produce **both files** as standalone HTML, with inline CSS/JS and appropriately embedded original article images. Mobile/desktop check, figure rendering and legibility, functioning links/nav, all source IDs, and question/source traceability are mandatory.
- Return **two file links** and short verification information. Use the supplied Drive folder, if any, as the upload destination for BOTH files; do not invent another folder. Without a Drive folder, produce downloadable files in the current supported environment.
- Do not force the legacy no-CSS Google Docs converter format onto the two HTMLs; use `references/output-formatting.md` only when a Google Doc is explicitly requested as an EXTRA export.
- Report inability to render, retrieve, upload, or install clearly; never claim success without verifying.
