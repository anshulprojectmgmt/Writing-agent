---
name: broad-research-skill-v2
description: Research a nonfiction book chapter topic from real sources. Produces a structured research brief in three sections — research objective, query map, and Source Ladder findings (Rungs 1-10) — where every finding carries its own source quality labels and evidence card (claim, why it matters, confidence). Use when starting a new chapter, when notes feel thin, or when the user says "research this topic". First step of the book writing process — its output feeds book-agent-research-analysis.
---

# Broad Research Skill (HTML output)

Produces a source-grounded research brief for a book chapter.
This is the **first step** of the book writing process.
Two phases: **A. Research** (find material) → **B. Output** (organize it, and render it as HTML).

---

## References

- `references/book-profile.md` — defines audience (PMs), the four-pillar framework (Adaptive UX, Agents, Emotional Intelligence, Trust), and scope (personal-life product contexts).
- `references/writing-style.md` — defines voice ("smart friend over coffee"), jargon-explanation rules, analogy-first structure, sentence rhythm, and formatting constraints. Applies to this brief **in part, not in whole**: its "What to Avoid" rules apply everywhere (see Filler Control below), its craft principles apply only to the `WHY IT MATTERS` field of each finding's evidence card — and its Formatting Rules, humour and sentence-rhythm guidance do **not** apply here, because this is a reference document that gets scanned out of order, not book prose. Layout is governed by `references/output-formatting.md` alone.
- `references/output-formatting.md` — defines the **HTML** markup for the generated brief: how the Research Objective, the Query Map, and the Source Ladder Findings — each finding with its labels and evidence card merged in — must be marked up (never how the content is worded). This brief is delivered as HTML, not Markdown. CSS does not survive the Google Docs conversion, so all spacing comes from `<p>&nbsp;</p>` spacer paragraphs and never from `style` attributes. Apply this at the formatting step in **B. OUTPUT FORMAT** below, after the brief's content is fully drafted.

---

## GenAI Lens *(standing rule — applies to every step below)*

This book's domain is generative AI, so every research pass — however broadly the chapter topic is phrased — must be anchored to the generative-AI-specific angle (naming current genAI companies, products, and terminology where a genuine one exists) rather than treated as a generic business/product topic.

---

# A. RESEARCH

---

## Adaptive Depth

Run every rung for full chapter research.
For narrow topics, skip irrelevant rungs and say what was skipped — a skipped
rung keeps its heading in Section 3 with a `Note:` paragraph giving the reason.

**Never skip for full chapter research:**
- Source Ladder
- Source Quality Labels (Step 3) — every finding must be labelled
- Blind Spot Check (Step 3b)
- Evidence Card fields (Step 4) — every finding must carry them

**Use judgment:**
- Go deep when the rung is central to the chapter.
- Skip when the rung is genuinely irrelevant.
- Use adjacent terminology when the user's framing is not market vocabulary.
- Flag weak evidence instead of pretending certainty.

---

## Filler Control

Filler control is a **quality floor**, not a quantity ceiling.
The goal is to remove weak material — not to limit how many strong findings are reported.

**Do not suppress or omit a finding because it feels like "too much."**
If it is important, include it.

Drop a finding only if it:
- Makes a generic claim with no named source, study, or example behind it
- Repeats something already captured in a stronger finding
- Is clearly marketing copy with no independent verification

**How a kept finding is written** — apply the "What to Avoid" rules from
`references/writing-style.md` to every finding of this brief, card fields included.
They are sourcing rules as much as style rules:
- **No hype language** ("revolutionary," "game-changing," "transformative") unless a specific named example immediately backs it.
- **No generic examples.** Name the company or drop the example — the same test as the first drop rule above.
- **No academic hedging** ("it could be argued that," "some might suggest"). Uncertainty belongs in the `CONFIDENCE` and `AUTHORITY` fields, never smuggled into the claim itself.
- **No passive inflation.** A claim has to stay checkable against its source.
- **Explain jargon on first use**, per the same file. The reader of this brief is the PM reader of the book.

**Per-rung minimums:**
- **Every rung: at least 5 findings.**
- Rung 5 (big platforms): at least 5 findings — one per major platform active in this space.
- Rung 6 (case studies): at least 5 named, verifiable examples.

---

## Tools

| Tool | Use for |
|------|---------|
| **web_search** -firecrawl | Use for Source Ladder searches (Rungs 1-7). Best for authoritative pages, adjacent terminology, and recent publications. |
| **web_extract** | Extract full content from a specific URL when a page looks promising but the search snippet is insufficient. |

---

## Step 1 — Ground Floor Check

> **"What products with real users are already doing some version of this — even partially, even under a different name?"**

List 3-5 named products. If nothing comes to mind, that is itself a signal.

**Check generative AI products specifically first** — ChatGPT, Claude,
Gemini, Copilot, and AI-agent features inside existing products — before
broadening to non-AI products, per the GenAI Lens rule above.

---

## Step 2 — Query Map

```
PRIMARY TERM: [User's exact topic]
SYNONYMS: [Alternate market terms]
TECHNICAL TERMS: [Named AI / technical concepts — favor genAI-specific
  vocabulary: LLMs, agents, fine-tuning, RAG, context windows,
  hallucination, alignment, etc., per the GenAI Lens rule]
PRODUCT TERMS: [How this appears in shipping products]
BUSINESS TERMS: [How executives, VCs, or analysts describe it]
ETHICS TERMS: [Privacy, permission, trust, governance terms]
CONTRARIAN TERMS: [Failure, criticism, risk, backlash terms]
```

---

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

## Step 4 — Evidence Cards (merged into each finding)

Every finding carries its own evidence card. The card is not a separate
section: its fields sit inside the finding, between the finding's summary and
its link. A complete finding is:
```
{ID} — {Title}
SOURCE TYPE: … | AUTHORITY: … | FRESHNESS: … | USE: …
{Summary: the finding and its context, as one paragraph}
CLAIM: [The specific, falsifiable claim]
WHY IT MATTERS: [Why this matters for this chapter and PM audience]
CONFIDENCE: High / Medium / Low
{URL}
```

The finding's link is the card's source — the card no longer carries a separate
`SOURCE` field. The summary paragraph names the author or publication; the link
gives the address.

The summary and `CLAIM` do different jobs. The summary is the finding in
context; `CLAIM` is the one falsifiable statement pulled out of it. Do not
repeat the summary as the claim.

`WHY IT MATTERS` is the one interpretive field on the card, so write it under
`references/writing-style.md` — plain language, concrete over abstract, and the
test that a sharp PM would read it and say "yes, that's new and I can use it."
`CLAIM` stays falsifiable and `CONFIDENCE` stays as data; voice does not enter
those two, nor the summary or the labels.

A cross-reference entry — a finding that only points at another finding —
carries no labels and no card fields.

---

# B. OUTPUT FORMAT

## Document Title
`{Skill_Name}_v{Version}_{Topic_Name}` — e.g. `Broad-Research-Skill_v1_Learning-and-Growth`

The brief has exactly three sections and ends after Section 3:

### 1. Research Objective
### 2. Query Map (from Step 2)
### 3. Source Ladder Findings (Rungs 1-10)
Every finding carries its source quality labels (Step 3) and its evidence card
fields (Step 4). Blind Spot Check additions (Step 3b) sit in their rungs as
ordinary findings. A rung below its minimum, or skipped, carries a `Note:`
paragraph giving the reason.

All three sections are findings and data: keep them plain and precise. Voice
from `references/writing-style.md` applies only to each finding's
`WHY IT MATTERS` field.

## Render & Deliver

Your input includes `drive_folder_link` — the exact Drive folder to use.
Do not resolve, create, or guess at a different location.

**1. Produce the complete brief** — Sections 1-3, nothing after Section 3.

**2. Render the brief as HTML per `references/output-formatting.md`.** Apply its
markup to every section — Research Objective, Query Map, and Source Ladder
Findings, each finding with its labels and evidence card fields — without
changing any wording, claim, label, or URL from Step 1. This is a markup pass
only.

The output is **HTML, not Markdown**. Three rules decide whether it renders:

- **No CSS.** No `style` attributes, no `<style>` blocks, no `class`. They are
  stripped during conversion, and writing them creates a false impression that
  spacing is handled.
- **Every blank line is a `<p>&nbsp;</p>` spacer paragraph.** Whitespace and
  newlines in the source HTML are ignored by the converter. The spacer is the
  only spacing mechanism that survives.
- **Escape `&` as `&amp;`** in all content, and write em dashes as `&mdash;`.

**3. Write the HTML to a file** in the sandbox, e.g. `/home/user/brief.html`.
Build it in parts if that is easier; concatenate to one file before the next
step.

**4. Create the Google Doc from code, reading that file into a variable.**

> **Never pass the HTML as a literal tool-call parameter.** A brief runs to tens
> of thousands of characters. Typing it into a tool call means re-emitting the
> whole document as tokens, which truncates, fails, and leads to placeholder
> text being sent instead. The document body must reach the tool as a **variable
> read from the file**, never as text you retype. Do not print the HTML to
> inspect it, and do not try to copy it out of a previous output — open the file
> and pass the handle's contents.

```python
with open('/home/user/brief.html') as f:
    content = f.read()

from gumloop import Gumloop
client = Gumloop()

result = client.mcp.execute("gdocs", "create_doc", {
    "title": "{Skill_Name}_v{Version}_{Topic_Name}",
    "content_format": "html",
    "content": content,
    "folder_id": "{the folder id from drive_folder_link}"
}).results[0]

print("status:", result.status)
if result.status != "success":
    print("error:", result.error)
print(result.decoded_content)
```

Nothing is written anywhere outside that folder.

If the created document ever ends up holding placeholder text, do not create
another one. Fix the same document in place with `update_doc`, passing
`operation: "replace"` and the content read from the file exactly as above.

**5. Return only the Doc ID.** Not the content, not a summary — the Doc ID is
your entire output.