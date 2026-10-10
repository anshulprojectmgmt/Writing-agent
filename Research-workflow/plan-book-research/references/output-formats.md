# Canonical Research Output Contracts

## Contents

1. Shared identifiers and provenance
2. Frame, Question Map, knowledge map, and running document
3. Worker briefs and stage handoffs
4. Background, expert, and targeted research formats
5. Source Ladder and evidence cards
6. Synthesis structure and completeness
7. Gap records and final research package
8. Portable delivery and adaptation provenance

## 1. Shared identifiers and provenance

Use Q001, Q002, etc. for questions; E-BG-001 or E-EX01-001 etc. for evidence; S001 etc. for canonical sources; P01 etc. for personas; G001 etc. for gaps; C001 etc. for concepts. Allocate namespaces before parallel work to avoid collisions. Preserve IDs across rounds; record aliases when merging duplicates. Keep source/evidence indexes with source URL, title, author/company, publication date, access date, source type, associated Q/E IDs, and provenance limitations. Canonicalize tracking URLs. Two outlets repeating the same company announcement are one underlying claim, not two independent confirmations.

Distinguish source statements, measured observations, inference, persona interpretation, and author synthesis. Cite URLs alongside E/S IDs so the research can be audited without platform-specific citation markup. Keep original evidence labels/cards intact; attach later classification revisions with reasons. Never change freshness to the access date or invent publication dates, numbers, names, quotes, sources, or null-result certainty.

## 2. Frame, Question Map, knowledge map, and running document

### Frame

Record topic verbatim; objective; audience; book profile and GenAI angle; personal-life/product scope; included/excluded territory; time horizon and as-of date; expected chapter contribution; assumptions; supplied/frozen decisions; execution mode (autonomous by default, stepwise only on explicit request); destination; running-document path; and stage artifact paths.

### Question Map — mandatory before background, expanded after expert questions

| Q ID | Question | Parent Q | Why it matters | Perspective/owner | Evidence needed | Relevant rungs | E/S links | Status |
|---|---|---|---|---|---|---|---|---|
| Q001 | A specific answerable question | none or Q ID | Chapter implication | Broad/background or P ID | What would establish or weaken the answer | 1–10 as appropriate | IDs | open/partial/answered |

Begin with broad questions about shipping products, user needs and actual behavior, mechanisms, economics, privacy/consent/trust, failure and counterevidence, and future claims. After background, expand using diverse expert questions grounded in actual findings. Merge semantic duplicates; preserve disagreement and child relationships. Link every search and evidence card to a Q ID. Search strings may appear in an attempt log under a question; they must never replace questions or form a Query Map section or a term/synonym/keyword map.

### Knowledge map

Maintain concept/question/evidence relationships as a table: `Node ID | Concept or question | Related node ID | Relationship | Supporting E IDs | Confidence/uncertainty`. Use relationships such as enables, constrains, depends on, contradicts, illustrates, or remains unresolved. Distinguish sourced relationships from synthesis inference. Update after expert question integration and each synthesis; do not duplicate questions to represent the same relationship. A compact diagram may supplement the table when useful, but do not substitute an uncited diagram for evidence.

### Canonical running document — one planner writer

Keep these exact headings: Frame; Stage Status & Artifact Index; Question Map; Expert Panel & Assignments; Knowledge Map; Source & Evidence Index; Synthesis 1 Handoff; Research Gaps & Round 2; Synthesis 2 Handoff; Final Research Package & Completeness. Record stage status, timestamps, paths/links, decisions, limitations, and next steps. Workers write independent artifacts; only the planner merges snapshots/results here. Include alternative framing proposals and their status without overwriting the authorized scope.

Deliver one self-contained running research document per project. Embed the complete stage outputs, including background evidence cards, expert briefs, both synthesis passes, and follow-up findings, as clearly named sections or appendices. Worker artifacts are intermediate handoffs; links to temporary files alone do not satisfy completion. Retain the stage-specific formats inside the combined document and place a concise final reading guide near the top.

## 3. Worker briefs and stage handoffs

Provide each fresh worker this compact contract:

```text
Task: [objective and mode]
Role: [researcher; background/expert/targeted/synthesis; persona when applicable]
Frame: [topic, audience, GenAI lens, scope, time horizon, frozen decisions]
Questions: [exact Q IDs and question text; gaps/exit conditions when applicable]
Read: [exact frame/map/background/prior evidence/book-state paths]
Write: [exclusive worker artifact paths; never the running document]
IDs: [allocated E/S namespace or existing IDs to reference]
Contract: [this canonical reference path and relevant sections]
Constraints: [real sources, all-rung attempt policy, evidence quality, limits]
Done: [required sections, answer status, coverage, cards, sources, handoff]
```

Launch with `fork_turns: "none"` or equivalent. No full chat inheritance, prior private reasoning, or narrative of conclusions to reproduce. Rebuild context from the listed artifacts. Return `artifact paths | assigned Q IDs and status | new E IDs | unresolved issues | next-stage handoff`. If a worker could not read a required file, say so.

Stage contracts:

| Stage | Required output |
|---|---|
| Frame | Frame, initial broad Question Map, path/index skeleton |
| Background | Three-section brief, ten-rung attempt/shortfall notes, complete cards |
| Expert selection | P ID, concrete company-role archetype, rationale, incentives, blind spots, assigned Q IDs |
| Expert questions | New/child Q text, parent, why material, grounding E IDs, evidence needed, perspective |
| Expert research 1 | Expert brief, assigned answers, new cards, ten-rung attempt log |
| Synthesis 1 | Fixed synthesis, registry, knowledge-map update, completeness, ranked gap handoff |
| Gaps | G/Q IDs, priority, evidence need, owner, exit condition |
| Targeted research 2 | Targeted brief, outcomes, new cards, revised statuses, attempt/null log |
| Synthesis 2 | Final fixed synthesis, registry, updated map, gap outcomes, changes, completeness |
| Final package | Reconciled index and running document, deliverable links, final status and limitations |

Check contracts in the planner/researcher's normal work; do not insert a separate evaluator stage.

## 4. Background, expert, and targeted research formats

### Background — exactly three sections

Title: `[Topic] — Background Research — [as-of date]`.

1. **Research Objective**: frame, scope, assumptions, GenAI lens, audience, and 3–5 named existing products from the ground-floor check. Include blind spot question/method if useful.
2. **Question Map**: initial broad Q IDs, answer statuses, evidence pointers, and relevant questions added while retrieving. Keep process logs here or within rung notes, not a new fourth section.
3. **Source Ladder Findings (Rungs 1–10)**: all ten named headings in order, findings with labels/cards and Q links. Include coverage/shortfall notes and blind spot additions within the relevant rung. Target five strong nonduplicate findings per rung; Rung 5 needs at least five relevant major-platform findings, Rung 6 five named verifiable cases. More strong findings are welcome. If evidence is insufficient, explicitly document the achieved count, actual attempts, blocked sources, reason, and chapter implication. Do not fabricate, pad, silently skip, or count cross-references as findings.

### Expert research — exact headings

Perspective & Assigned Questions; Question Answers; Source Ladder Findings (Rungs 1–10); Coverage & Search Attempts; Handoff.

State P ID and simulated company-role lens, not a real interview. For each Q: direct answer, supporting E/S IDs and URLs, counterevidence, confidence, limits, status. Cite relevant background evidence by its existing ID; add only genuine new findings. Keep all ten rung headings and attempt/relevance notes, focusing depth on the assigned questions. Do not recreate 50 findings per expert. In Handoff list unresolved Q IDs, candidate child questions, conflicts, and next evidence needs.

### Targeted research — exact headings

Gap & Exit Condition; Targeted Question Answers; New or Reassessed Evidence; Coverage & Search Attempts; Outcome & Handoff.

Record G/Q IDs, prior evidence, answer changes and supporting E IDs, exit condition reached/partial/not reached, null results, and unresolved implications. Coverage contains an explicit row for all ten rungs with actual attempt/result or documented irrelevant-to-question rationale; do not omit academic or general news. Do not repeat the background quota. Preserve original cards and add separately labelled reassessment notes when warranted.

For all modes, attempt logs contain `Q ID | rung | date | source channel/search used | pages checked | finding/null/blocked/relevance result`. A documented relevance test is an attempt, not permission to erase a rung. Keep the background's five-per-rung goal and gaps visible even if focused workers add fewer cards.

## 5. Source Ladder and evidence cards

| Rung | Exact heading | Source channels and emphasis |
|---|---|---|
| 1 | Consulting & Analyst | McKinsey, BCG, Gartner, Forrester, Deloitte, IDC, 451 Research, Omdia, CB Insights; inspect methods and market-estimate variability |
| 2 | VC / Investor Research | a16z, NFX, Sequoia, Radical Ventures, Conviction; label investor incentives |
| 3 | Academic / Research | Original papers/research pages; CHI, CSCW, FAccT, AIES, NeurIPS, ICML, ICLR, ACL/EMNLP/NAACL and other relevant venues; FAccT/AIES for trust/ethics; academic papers secondary to company sources for shipping facts |
| 4 | Practitioner & Product | Named PM/UX/engineering accounts, technical documentation and how-we-built posts; distinguish observed work from opinion |
| 5 | Big Platforms & Major Products | Official company blog/news; founder/CEO voice; vision/roadmap signals—attempt all three channels, not a generic search alone |
| 6 | Case Studies | Named verifiable shipped products, deployments, lessons and outcomes; distinguish pilots from scale |
| 7 | Ethics / Regulatory | Primary regulators, laws, guidance, company safety/policy documents; privacy, consent, governance; identify jurisdiction/version |
| 8 | Trend & Futures | Roadmaps and forecasts; date them and label predictions as predictions |
| 9 | Newsletters & Long-form | Lenny's Newsletter, Ben's Bites, Latent Space, Import AI, Interconnects, Pragmatic Engineer, relevant interviews/podcasts; discovery and contextual perspectives |
| 10 | General / Recent News | Always attempt; current general/tech reporting for developments, failures, criticism, and corroboration; follow it back to primary sources |

Prioritize primary company blogs for current product claims. Scan relevant official channels among OpenAI, Anthropic, Google/DeepMind, Meta, Microsoft, Amazon/AWS, Apple, xAI, Mistral, NVIDIA, Salesforce, Databricks, Hugging Face, DeepSeek, Moonshot/Kimi, Zhipu, and Qwen. Use founder writing, public keynotes (DevDay, Connect, I/O, Build, re:Invent, GTC), long-form interviews, shareholder letters/IR transcripts, social posts, policy/testimony, and technical research where questions warrant them. Verify current channels and relevance rather than treating this list as fixed factual coverage. Use primary regulators such as FTC, EU, OECD, Congress, and UK AISI as relevant. Journalism (Reuters, Bloomberg, FT, The Information, Wired, MIT Technology Review, The Verge) is secondary for company facts but may supply original reporting. No rung is automatically authoritative just because of its position.

### Original evidence card — mandatory on every finding

```text
{E ID} — {Title}
SOURCE TYPE: Primary / Academic / Analyst / VC / Practitioner / News / Company Marketing / Opinion
AUTHORITY: High / Medium / Low
FRESHNESS: {actual publication date, or unknown}
USE: Cite / Background / Ignore
{One summary paragraph naming author/publication and context}
CLAIM: {one specific falsifiable statement distinct from the summary}
WHY IT MATTERS: {concrete relevance for the chapter and intended book audience}
CONFIDENCE: High / Medium / Low
{source URL}
Question links: {Q IDs}
Source/provenance links: {S ID; relevant limits or dependency}
```

The URL is the card's source; do not replace it with a redundant SOURCE field. Keep source-quality labels inline on the finding, not in a separate labels section. Plain/direct wording applies everywhere; the WHY IT MATTERS field carries interpretation. A source with a strong announcement but no behavioral evidence may have high authority on availability and low confidence on demand. A cross-reference carries no duplicate labels/card and is not an independent finding. Record raw weaker candidates as discarded/ignored in attempt logs when useful rather than padding the findings.

## 6. Synthesis structure and completeness

Title: `[Topic] — Research Synthesis — Pass [1/2]`.

### Framing Check — opening block, under 200 words

Five short blocks of 1–3 sentences: The stated question; The actual question; The assumption underneath; The constraint test (what made current practice rational, does it still hold, what changed); One serious alternative frame (or honest failed challenge). Then `FRAMING: HOLDS` or `FRAMING: REFRAME PROPOSED`. In autonomous mode disclose and record an alternative without stopping or silently adopting it; explicit stepwise mode follows the user's checkpoint instructions.

### Seven core sections — exact order and headings

1. **Central Concept**: 2–3 clear paragraphs covering the major aspects and combined insight; end with Sources. Make the core tension intelligible alone.
2. **Themes**: 4–6 when supported. Each has a 2–5-word heading, one-line italic plain-language explanation, 3–5 sentences in 2–3 paragraphs, a separate Example bullet, a Sources bullet, and a horizontal rule between themes. If evidence supports fewer, document the shortfall rather than inventing themes.
3. **Mental Models**: reusable frameworks or distinctions, preferring those named by sources. Give 2–3 paragraphs, contrasts as bullets when relevant, Why it matters and Source lines, and rules between entries. Label invented author framings explicitly.
4. **Technical Concepts**: each has bullet fields What it is (one sentence), Why it matters (one sentence), Source/Provenance (correct theory/paper attribution). Add What changed (constraint and where it breaks) only if supported; do not speculate.
5. **What to Retain, Downgrade, or Remove**: three labelled lists with source attribution and downgrade/removal reasons; account explicitly for prior evidenced claims. Then Live Tensions (usually 1–3): bold poles, strongest Side A and Side B with their own sources, Why it stays open, Chapter use. State honestly if none. Then Disconfirming Evidence: 2–3 specific weakening conditions, actual Searches run/results including nulls under Q IDs, and pointer to Section 7's falsifier. Keep judgment next to what it judges.
6. **Chapter Synthesis Ideas**: 3–4 supported structural alternatives. Each has Core framing (2–3 sentences), Chapter flow bullets Opening, Sections 1–3 (Section 4 if useful), Closing (1–2 sentences each). Suggest narrative structures without introducing new factual claims.
7. **Final Conclusion**: 2–3 short paragraphs converging on a defensible claim derived wholly from Retain material; make the culminating takeaway a standalone paragraph. Include Sources and a final one-sentence What would change this conclusion falsifier with an observable breaking condition.

Optional **8. Research Gaps & Opportunities** only if material gaps remain: bold specific unanswered question; 2–3 sentences of significance; Web search findings from 1–3 actual searches or prior targeted evidence, including nulls; Updated guidance for the chapter. Omit if not earned, not an empty heading. Keep operational G/Q assignments in the gap handoff rather than turning synthesis into bookkeeping.

### Concept registry and knowledge map sidecar

`C ID | canonical concept | aliases | single home section | example used | E/Q links | cross-reference locations`. Allocate one full write-up only. Mechanism/theory → Section 4; transferable framework/distinction → Section 3; recurring argument → Section 2. Cross-reference elsewhere, including Framing Check and Section 5. Check synonymous duplicates and reused examples before Section 5. Add knowledge-map relationships and question answer updates using Section 2's map format.

### Completeness Summary — append after substantive sections

```text
COMPLETENESS SUMMARY
Sections written: [1–7, plus 8 if included]
Section 8 included: [yes / no—reason if omitted]
Word count: [actual count]
Duplication check run: [yes—N merges / yes—none found]
Retain / Downgrade / Remove counts: [R: n, D: n, Rm: n]
Input completeness: [full / thin—missing elements]
Framing verdict: [HOLDS / REFRAME PROPOSED—summary]
Live tensions logged: [N—titles / none found]
Disconfirming searches run: [N—findings / none of substance]
Falsifier stated in Section 7: [yes / no]
Section 4 "What changed" lines: [N of M concepts]
Book state document: [read and reconciled / not supplied]
```

Keep these twelve original fields. Add pass-specific Q/G coverage or artifact limitations only after them. Count rather than estimate words and list real checks, not aspirational completion. A missing required field is a correction task, not a reason to mark complete. Typical target: 1,500–3,000 words, 3,000–4,000 when warranted; framing and judgment can add about 400–600 words without crowding substantive sections.

## 7. Gap records and final research package

Gap handoff table: `G ID | Q ID(s) | gap/unsettled claim | why material | existing E IDs | priority | evidence needed | suggested P owner | exit condition | round 2 outcome | residual limitation`. Rank by potential to alter the thesis, impact on chapter usefulness, and feasibility; do not fabricate gaps. An unsuccessful targeted search can leave the gap open. Record known-access limitations separately from evidence absence.

Synthesis 2 change log: `claim/Q ID | prior assessment | final assessment | new E IDs | strengthened/weakened/reversed/unchanged | reason`. Reconcile closed, partial, open questions and changed concept relationships.

Final package must include the running document, frame, initial and expanded Question Map/history, background with all ten rungs, human persona panel and grounded expert questions, all round 1 briefs, synthesis 1, gaps, targeted round 2 outcomes or justified no-additional-research status, synthesis 2 with concept registry/knowledge map and completeness, source/evidence index, and final change/coverage status. Every artifact must have a concrete path/link. Summarize defensible conclusions, material uncertainty, actual rung counts/shortfalls, residual gaps, and the falsifier. Deliver research for review/use; do not externally post it by implication.

## 8. Portable delivery and adaptation provenance

Default to durable Markdown artifacts using the environment's available persistence tools. Honor exact supplied destinations; do not guess another folder. Research output files are not skill bundle files. Avoid assumptions about Gumloop, Google Drive, external credentials, or book-profile/style files. If HTML or Google Docs is explicitly requested and tools are available, render the complete content without changing claims: use semantic headings/paragraphs/lists, no CSS/class/style attributes, `<p>&nbsp;</p>` spacer paragraphs, escape `&` to `&amp;` and em dashes to `&mdash;`. Read long body content from files into variables rather than retyping it in tool calls. Verify the saved content and correct a placeholder document in place. Return concrete deliverable links, not an unverified completion claim.

Preserve the source broad-research skill's ten rungs, ground-floor/blind-spot checks, label vocabulary, merged evidence cards, filler-control floor, and background five-per-rung target. Replace its Query Map entirely with a question-first map, obsolete hardcoded years with the run's actual horizon, optional academic/news omissions with all-rung attempts, and platform-specific HTML/Gumloop-only delivery with portable output. Preserve the source analysis skill's Framing Check, seven sections, concept deduplication, live tensions, disconfirmation, falsifier, and twelve-field completeness; adapt the reframe stop to user-selected autonomous/stepwise mode and remove separate evaluator dependency.

Original source skills inspected at Writing-agent revision `c6ae6dd69718e95cb3bf7a68ebb19afbdb6b56ae`:

- [Broad Research](https://github.com/anshulprojectmgmt/Writing-agent/blob/c6ae6dd69718e95cb3bf7a68ebb19afbdb6b56ae/Book%20Orchestrator%20Agent/Broad-research-node/broad-research-agent/SKILL.md), including its `references/output-formatting.md`.
- [Research Analysis](https://github.com/anshulprojectmgmt/Writing-agent/blob/c6ae6dd69718e95cb3bf7a68ebb19afbdb6b56ae/Book%20Orchestrator%20Agent/research-analysis-node/Research%20Analysis%20Agent/SKILL.md), including its `references/output-formatting.md`.

Condense Co-STORM ideas rather than installing or claiming execution of its engine. Ground the adaptation in official Stanford OVAL source:

- [Expert generation](https://github.com/stanford-oval/storm/blob/main/knowledge_storm/collaborative_storm/modules/expert_generation.py): diverse role perspectives guided by background; focused opposing stands/stakeholders. Adapt these to human company-role archetypes, not named-person impersonation.
- [Grounded question answering](https://github.com/stanford-oval/storm/blob/main/knowledge_storm/collaborative_storm/modules/grounded_question_answering.py): derive retrieval operations from each question, answer with grounded citations, preserve question metadata and relevance/limitations.
- [Warm-start hierarchical discussion](https://github.com/stanford-oval/storm/blob/main/knowledge_storm/collaborative_storm/modules/warmstart_hierarchical_chat.py): use common background, multiple perspectives, and a growing knowledge map to ask materially advancing questions.

These are workflow inspirations. The three skills implement artifact handoffs and ordinary agent/retrieval work, not Stanford's Python repository runtime.
