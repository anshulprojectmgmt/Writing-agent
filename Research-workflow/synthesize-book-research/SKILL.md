---
name: synthesize-book-research
description: Analyze combined nonfiction research into a Research Analysis-derived seven-section synthesis with a framing check, mental models, mechanisms, evidence judgments, live tensions, disconfirmation, chapter ideas and a falsifier; integrate expert perspectives into a credible vision of tomorrow. Use for initial/final book synthesis or making sense of source-heavy research.
---

# Synthesize Book Research

Read [the canonical output contracts](../plan-book-research/references/output-formats.md), especially the future-first guide, synthesis section specifications and provenance/adaptation table.

## Foundation: the existing Research Analysis skill

Adapt the author's [Research Analysis skill](https://github.com/anshulprojectmgmt/Writing-agent/blob/3e47309c5d25d4493fb5e844caba992c20fb7602/Book%20Orchestrator%20Agent/research-analysis-node/Research%20Analysis%20Agent/SKILL.md) and its [output-formatting reference](https://github.com/anshulprojectmgmt/Writing-agent/blob/3e47309c5d25d4493fb5e844caba992c20fb7602/Book%20Orchestrator%20Agent/research-analysis-node/Research%20Analysis%20Agent/references/output-formatting.md). The operational adaptation is specified here and in the shared contract; workers do not need to fetch legacy files on every run.

Preserve its intellectual work: **test the framing, extract concepts and mental models, explain mechanisms, judge evidence, preserve disagreement, seek disconfirmation and turn research into chapter possibilities**. Restore the Framing Check and seven core sections. Improve their future orientation and native-document delivery; do not replace them with a generic forecast essay.

The original skill's query map, PM-only assumptions, fixed item counts, automatic rejection of practitioner opinion, Gumloop-only HTML/spacer delivery and reframe-as-mandatory-stop do not govern this workflow. Apply the adaptations explicitly documented in the shared contract. A thoughtful opinion can be valuable reasoning without becoming observed evidence.

## Inputs and independent context

Use a fresh synthesis instance, distinct from the planner and researchers, with `fork_turns: "none"` or equivalent when supported. Supply exact artifact paths and concise task-local context, not inherited chat. Read:
- Frame, audience/scope, time horizon and frozen decisions.
- Accepted background narrative, examples and source notes.
- Every expert investigation, their professional roles and question rationales.
- Current Question Map/history, source/insight index and all-ten-rung coverage records.
- Prior synthesis and gap outcomes for final synthesis.
- Book state/outline if supplied: settled terminology, rejected frames, carried tensions and chapter themes.

Note missing/thin input honestly; do not infer unread contents. Do not treat duplicated sources across expert reports as independent agreement. Return unread essential artifacts for correction; proceed with nonessential omissions visibly qualified.

Use a **Question Map, never a Term Map or Query Map**. Preserve Q/S/E/G links; revise questions where integration exposes new uncertainties or possibilities. Keep the current authorized scope unless the user changes it.

## Future-first integration

Use the shared reasoning guide to move from evidence to a vision of tomorrow. For each major argument identify its present signals, driving force or changed constraint, plausible future form, consequence and alternative/breaking condition. These are thinking dimensions, not five repeated fields.

Connect expert lenses rather than summarize them separately. Ask how engineering capability changes design possibilities, how user behavior changes product value, how distribution/economics affect adoption, and how governance changes permissible autonomy. Explain relationships and dependencies. Identify emerging product/interaction forms, new behaviors/markets, second-order consequences and non-obvious connections. Develop competing scenarios where useful; do not force one deterministic prediction or unsupported probabilities.

Evidence constrains imagination without replacing it. **The future outcome is an inference even when the underlying facts are strong.** Absence of mass adoption today limits present claims; it does not automatically disqualify a plausible future. Label speculative leaps and their assumptions.

## Draft using the Research Analysis structure

### Framing Check

Open with five short blocks: stated question; actual question; assumption underneath; constraint test; one serious alternative frame. Then state **FRAMING: HOLDS** or **FRAMING: REFRAME PROPOSED**. Test what made the current product/practice rational, what changed and whether an alternative explains the evidence better.

Keep this usually under 200 words, without suppressing an important qualification. In autonomous mode, surface the proposed alternative and continue under the authorized frame; do not silently adopt it. In user-requested stepwise mode, follow the specified checkpoint. Never reopen frozen decisions without new evidence.

### 1. Central Concept

State the main shift and the combined insight in two or three coherent paragraphs where useful. Explain what is changing, why it matters and what core tension shapes tomorrow. Anchor it in combined evidence, not a single exciting forecast. Include source links.

### 2. Themes

Develop recurring arguments and future implications that earn space. For each use a short heading, plain-language explanation, substantive reasoning, a concrete example and sources. Distinguish independent reinforcement from repeated vendor messaging. Cover future product forms, behaviors, scenarios, value capture and second-order effects where the evidence/analysis supports them. No theme-count quota; fewer strong themes beat filler.

### 3. Mental Models

Extract transferable frameworks or distinctions that help the writer reason about new cases. Explain the model, its usefulness for the future and its limits, with correct provenance. Prefer named source models when useful; label researcher-created models explicitly. Do not invent a branded framework merely to fill the section.

### 4. Technical Concepts

Explain mechanisms/architectures or relevant named theories/studies: **What it is; Why it matters; Source/Provenance**. Add **What changed** where supported: the prior constraint, enabling change and where the mechanism still breaks. Relate the mechanism to future capability or product form. Define unfamiliar terms once; do not turn the section into a glossary.

### 5. What to Retain, Downgrade, or Remove

Apply the confidence judgment described in the shared contract. Retain well-supported evidence and clearly justified reasoning; downgrade emerging, narrow, dependent or speculative claims; remove unsupported factual claims and redundant/low-value material. Give attribution/reasons. Account explicitly for important prior claims whose interpretation changes.

Then preserve **Live Tensions**: strongest sourced Side A and Side B, why unresolved and chapter use. Do not manufacture disagreement or flatten it to favor the thesis.

Then give **Disconfirming Evidence**: concrete conditions that would weaken the central argument, actual question-led searches or source inspections/results (including nulls), and a pointer to the conclusion's falsifier. Use prior research if it genuinely addresses the challenge; otherwise do a small focused check or identify a material gap. Never claim searches not run.

### 6. Chapter Synthesis Ideas

Give earned narrative options with **Core framing** and **Chapter flow: Opening → sections → Closing**. Connect to supplied Products of Tomorrow themes/chapters. Identify useful hooks, surprising examples, arguments or distinctions rather than merely restating findings. Do not introduce new factual claims or force three/four alternatives.

### 7. Final Conclusion

Close the loop with a defensible, evidence-informed view of the future and its conditions. Anchor factual premises in retained evidence; label scenario/inference as such. Explain residual uncertainty without hedging every sentence. End with a specific **What would change this conclusion** condition and sources.

### 8. Research Gaps & Opportunities — only when warranted

Identify unanswered questions that could materially change a scenario, conclusion or chapter. Explain significance, current evidence/search results and chapter guidance. Hand off G/Q IDs, evidence needed, suggested role and exit condition to the planner. Do not manufacture a targeted round.

If a core section has no justified material, retain its heading with a brief honest explanation; do not invent content. Section 8 is omitted when unearned. Counts and length guidance never justify padding.

## Deduplicate before judgment

Maintain a small concept registry during drafting. Give each idea one full home:
- Mechanism/theory with a how-it-works answer → Technical Concepts.
- Transferable framework/distinction → Mental Models.
- Recurring argument → Themes.

Check aliases, synonymous concepts and reused examples. Elsewhere reference the home instead of re-explaining. Include the Framing Check and Section 5 in this check; repeated coverage must not become multiple evidential claims. Preserve useful concept/force/outcome relationships in the compact knowledge map.

## Retrieval, pass-specific handoff and acceptance

Normally integrate supplied research. All background, expert and targeted passes must attempt **all ten Source Ladder rungs**, without skipped rungs or finding quotas. Inspect their coverage before acceptance. A synthesis-level provenance/disconfirmation spot check is not a substitute for an omitted research rung; report omissions to the planner for correction.

Use native search by default. Validate explicit current-run Exa authorization and tool availability before any Exa call; follow the shared provider table. Return substantial new retrieval to the targeted-research stage.

**Initial synthesis:** deliver the Framing Check, sections 1–7, optional section 8, concept registry, question/relationship updates and ranked gaps/no-gap decision.

**Final synthesis:** use a new instance and the combined evidence, including the no-additional-retrieval decision if applicable. Rebuild the integrated view, retaining useful ideas without copying the first pass mechanically. Record strengthened, weakened, reversed or unchanged conclusions with reasons and E/Q links. A fresh final synthesis is required; a second targeted retrieval pass is conditional.

Apply the editorial pass without dropping important reasoning or required sections. Typical 1,500–3,000 words is guidance; more is justified by substantial arguments, fewer by narrower input. Put the compact twelve-field Completeness Summary in the appendix, not the reading flow. Verify actual section presence, word count, provenance, source independence, deduplication, tensions, disconfirmation, falsifier and question/gap status before returning.

Save only assigned artifacts; the planner owns the running index and native Google Docs persistence. Use native heading styles, readable spacing, selective bold and clickable citations per the shared contract. Do not reproduce the legacy HTML spacer template blindly.

