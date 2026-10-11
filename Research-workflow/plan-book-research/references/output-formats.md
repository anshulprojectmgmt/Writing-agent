# Canonical Research Contracts

## Contents

1. Shared mission and editorial standard
2. Question Map acceptance and evolution
3. Run configuration and search providers
4. Source discovery, screening and traceability
5. Stage outputs and worker handoffs
6. Native Google Docs and portable delivery

## 1. Shared mission and editorial standard

**Define plausible futures through diverse professional perspectives.** Present signals and evidence support reasoning about driving forces, future products/behaviors, competing outcomes, second-order consequences and constraints. These are thinking dimensions, not compulsory headings.

Write for the supplied audience and book scope. Keep verified facts, emerging signals, source interpretations, researcher inference and speculation distinguishable through natural wording and a compact evidence record. Do not equate a prediction with a fact, or a simulated professional lens with a real interview.

**Substance without bloat:** give consequential insights, mechanisms, examples and disagreements the space they merit. Keep routine context brief. Each paragraph must add understanding, evidence or reasoning. Bold meaningful takeaways selectively. Remove repeated ideas, ceremonial introductions, generic transitions, obvious observations and repeated caveats. Combine headings/fields when useful; never fill them with invented material. Word counts guide effort, not padding. Preserve reasoning, uncertainty and counterarguments while compressing.

Before accepting or saving each stage, ask: What matters most? What repeats? What adds no understanding? What deserves more explanation, and what deserves less? Edit accordingly. Apply this standard to skill instructions too.

## 2. Question Map acceptance and evolution

Background starts with flexible guiding questions about meaning/significance, developments, changing forces, uncertainty and deeper inquiry. No fixed initial question count or detailed map is required. Give these prompts provisional BQ IDs for source associations; carry their links into the expert map.

Before expert research, inspect every top-level entry. Accept it only if it:
- Is an open-ended question, not a topic label, keyword cluster or search string.
- Explores consequential future change through its professional perspective.
- Is broad enough to support discovery rather than merely retrieve a named fact or test one use case.
- Has a clear reason its answer could alter understanding of the topic.

A question mark alone does not establish validity. Reject "Memory", "personal agent memory pricing" and "Find three agent products". A current-state question or holiday-booking check can be a supporting investigation beneath "How will personal agents evolve as products and change value, differentiation, distribution and competition?" Rewrite rejected top-level entries before launching expert research.

Use stable Q001-style IDs. A compact map needs:

| Q ID | Broad research question | Role/parent | Why consequential | Source/insight links | Status |
|---|---|---|---|---|---|
| Q001 | Future-oriented open question | P01 or parent Q | Implication | S/E IDs | open / partial / informed |

Future questions may remain uncertain even when well investigated; "informed" does not mean the future is settled. Supporting questions may be narrower. Search strings belong only in temporary retrieval logs beneath a question, never in a Term Map or Query Map.

At each pass, review additions, changed assumptions, merges and questions that lost relevance. Record only material revisions with their reason and prior ID/alias. Do not reuse a retired ID or discard its source associations. New insights may create new questions; retain the insight and link it before handoff. Every retained source connects to at least one BQ/Q, including counterarguments.

## 3. Run configuration and search providers

Record this portable configuration in the frame and each worker brief:

```yaml
run_id: topic-date
search_provider: native       # native | exa | compare
exa_authorization:
  authorized: false
  run_id: null
  user_instruction: null      # exact instruction naming Exa for this run
effective_search_provider: native
```

| Requested mode | Required decision before retrieval |
|---|---|
| native or omitted | Use native ChatGPT web search; do not call Exa |
| exa | Verify explicit user authorization naming Exa for this run and available connected tools |
| compare | Verify the same authorization; use equivalent question-led searches through native and Exa, deduplicate, compare usefulness |
| exa/compare without authorization | Leave Exa disabled; use native and disclose invalid configuration; if the user made non-native execution indispensable, return a blocker |
| Authorized Exa unavailable | Disclose unavailable tools; use native only if compatible with the user's fallback instructions, otherwise return a blocker |
| Unknown mode | Correct configuration before retrieval; never silently enable another provider |

"Use Exa for this research" or "Compare Exa with ChatGPT Search" qualifies. "Research deeply", "best sources" and "all available tools" do not. Authorization is run-specific and never carries forward. A configuration flag alone is not user authorization; confirm the recorded instruction applies to the current task/run.

Do not automatically call Exa during any stage, silently activate it after weak native results, invent credentials or assume connection. Discover available tools before use. Prefer a suitable connected plugin; do not separately use the Exa API without explicit authorization. Add no mandatory Exa dependency and no Tavily/Firecrawl integration. Provider ranking supports discovery, not article-quality judgment. Record requested/effective modes and any disclosed fallback.

## 4. Source discovery, screening and traceability

### Preserve the ten-category Source Ladder

| Rung | Category | Discovery emphasis |
|---|---|---|
| 1 | Consulting & Analyst | Market arguments, surveys, assumptions and methods |
| 2 | VC / Investor Research | Emerging models and ecosystems; investment incentives |
| 3 | Academic / Research | Original measured findings and mechanisms; relevant research pages/papers |
| 4 | Practitioner & Product | Firsthand PM, UX, engineering and deployment accounts |
| 5 | Big Platforms & Major Products | Official blogs/docs, founder/leader writing, keynotes and strategic signals |
| 6 | Case Studies | Named products/deployments; distinguish pilot, scale and measured outcomes |
| 7 | Ethics / Regulatory | Primary policy, jurisdiction-specific regulation, safety and governance |
| 8 | Trend & Futures | Dated forecasts, roadmaps and alternative futures |
| 9 | Newsletters & Long-form | Thoughtful essays, interviews/podcasts, critique and original arguments |
| 10 | General / Recent News | Developments, failures, criticism and original reporting; follow primary evidence |

Consider every category for blind spots. Record a compact result/relevance note per category, but investigate only where intellectually useful. Depth need not be uniform; there is no five-per-rung, five-platform or fifty-finding quota. Do not count a category as searched when merely considered.

Prioritize primary company/product evidence from relevant firms such as OpenAI, Anthropic, Google/DeepMind, Meta, Microsoft, Amazon, Apple and others warranted by the questions. Use blogs, documentation, technical reports, public keynotes, founder essays and IR transcripts. Company forecasts are strategy signals, not established future outcomes. Academic work remains valuable for original measured findings, without becoming the default source for current shipping behavior. Source lists are suggestions, not compulsory provider checklists.

### Three lightweight gates

1. **Relevance:** materially helps answer a guiding/research question.
2. **Intellectual value:** adds original reasoning, credible observations, mechanisms, concrete examples, useful future possibilities, distinctions or serious counterarguments.
3. **Evidence quality:** identify facts, firsthand observation, measured research, opinion or speculation; assess scope, methods, incentives and provenance.

Internally classify sources considered for use as **Deep Read**, **Selective Read** or **Skip**. Record a short rationale for consequential selection/rejection decisions; no numerical rubric or mandatory card for every result. Retain strong primary evidence or serious counterarguments even when ranked low. Do not rely on snippets for material claims. Read important arguments deeply enough to preserve their reasoning.

### Two output layers

**Reading layer:** substantive notes grouped by ideas/themes, inline clickable source citations and selective bold takeaways. For a major insight cover central idea, motivation/reasoning, supporting evidence/examples, future implications, writer's value and limitations in coherent paragraphs. These dimensions are a quality check, not six repeated headings. Minor sources may support a short sentence.

**Traceability layer:** compact appendix or structured handoff embedded in the stage artifact. Use Q/BQ for questions, P for professional roles, S for sources, E for important observations/insights and G for gaps. Allocate exclusive namespaces to parallel workers; preserve existing IDs/aliases.

Keep these compact records where applicable:
- Source: S ID, canonical URL/title, author/organization, publication date (unknown if unavailable), access date, source category/type, disposition/rationale, Q/BQ links and provenance limits.
- Insight: E ID, claim/idea, supporting S/Q links, evidence versus inference/speculation, material uncertainty and observation period where different from publication.
- Coverage: category, investigated / checked-no-useful-result / blocked / considered-not-pursued, actual result or reason.
- Search log: Q/BQ, provider, date, actual retrieval operation, material result/null/blocked status. Keep bounded notes, not an exhaustive dump of search hits.

Canonicalize URLs and shared claims. Multiple outlets repeating one announcement are not independent corroboration. Keep original historic evidence IDs/labels when referencing prior artifacts; attach reassessments rather than rewriting history. New outputs use these lean records rather than the old mandatory evidence-card fields.

## 5. Stage outputs and worker handoffs

Each accepted stage needs a dedicated format below. Required information must be present, but headings can combine naturally and empty sections should be omitted. Store step, round, focus, status, next dependency and artifact links in the compact index/appendix rather than above every paragraph.

| Stage | Human-facing output | Compact handoff/appendix |
|---|---|---|
| 01 Frame | Topic, future objective, audience/scope, horizon and assumptions | Frozen decisions, mode, provider record, run folder and artifact index |
| 02 Background | Brief narrative: significance, developments/examples, forces, uncertainties and promising deeper dimensions; usually up to 1,000–1,500 words when warranted, no minimum | Provisional guiding-question/source links, ten-category relevance/coverage notes |
| 03 Expert panel | Roles and what each distinct lens can reveal | P ID, generic role, justified specialization if any, selection rationale/blind spot |
| 04 Question Map | Broad future questions through each role | Stable Q IDs, rationale/parents, validation/revision notes, source links where available |
| 05 Expert research | Role-specific argument, thematic substantive notes, future possibilities, counterarguments and writing opportunities | Current question statuses/revisions, screened sources, coverage and concise search/provenance notes |
| 06 Synthesis 1 | Integrated vision of tomorrow using the structure below | Cross-perspective relationships, question updates, significant gaps or no-targeted-work decision |
| 07 Gap decision | Only consequential gaps and why they matter; brief no-gap decision is valid | G/Q, prior evidence, priority, owner, evidence need and exit condition |
| 08 Targeted research (conditional) | New insight/evidence, changed answers and remaining uncertainty | G/Q outcomes, actual searches/nulls, exit-condition status |
| 09 Final synthesis (conditional) | Revised integrated picture from combined evidence | Strengthened/weakened/reversed views with reasons, question/gap outcomes |
| 10 Final package | Linked reading guide, strongest future insights, chapter connections and material uncertainty | Reconciled stage/source index, current map/history, save/check status and skipped-stage reasons |

### Flexible synthesis structure

Lead with **the most consequential shift** and explain its evidence/mechanism. Develop themes that earn space:
- Future product forms, interactions and behaviors.
- Driving forces, dependencies and who captures value.
- Plausible alternative scenarios and distinguishing signals.
- Cross-perspective agreements, real disagreements and second-order consequences.
- Non-obvious connections, new markets and chapter opportunities.
- Material uncertainty, strongest counterarguments and observable conditions that would change the view.

Group or omit unearned headings; there are no compulsory counts of themes, models, scenarios or chapter alternatives. Cite material claims. Label researcher-created models and speculative possibilities. Avoid repeated concept explanations and reused examples. Maintain a small relationship map only where it clarifies dependencies or tensions. Check provenance, alternatives, disagreement, question coverage and editorial quality in a compact acceptance record; do not append a large twelve-field completeness form.

### Fresh worker brief

```text
Task/mode: future-oriented objective; background/expert/targeted/synthesis
Role: generic professional lens, specialization only if justified
Frame: topic, audience, scope, horizon/as-of date, frozen decisions
Questions: guiding BQs or broad validated Q IDs/text; G/exit conditions if targeted
Read: exact artifact paths/snapshot, shared contract, relevant book context
Write: exclusive artifact path(s); never the planner's running index
IDs: allocated namespace and prior IDs to preserve
Provider: requested/effective provider; run-specific Exa authorization record
Done: dedicated stage output, substantive notes, compact traceability and checks
```

Use fresh contexts and immutable handoffs; run independent expert work in parallel when supported. Return artifact paths, question/gap status, material limitations and next handoff. The planner alone merges the canonical map/index and saves accepted stage documents.

## 6. Native Google Docs and portable delivery

Create one dedicated run folder and a separate native Google Doc for every completed stage. Keep parallel investigations as clearly separated expert sections in the corresponding numbered stage document, preserving full substantive notes. Record skipped conditional stages in the index; do not create empty step documents. The final package links accepted stages, avoiding repeated full reports.

Use the current Google Drive/Docs skill for the native creation route. Use Title, Heading 1 and Heading 2 styles, short readable paragraphs, moderate spacing, selective bold and clickable citations. Insert page breaks between major expert sections when useful. Group findings by ideas, not categories; keep process/evidence metadata in compact appendices. Do not simulate formatting with raw Markdown headings, spacer paragraphs, repeated blank lines or evidence IDs dominating the narrative.

After saving, verify content, native MIME type, actual heading styles/links and run-folder membership before recording success. Update existing stage docs by ID. Keep portable Markdown and structured handoffs for migration; when native persistence is unavailable, disclose the limitation and use an authorized equivalent destination.

This workflow adapts question-grounded multi-perspective exploration inspired by Stanford OVAL Co-STORM; it does not install or claim execution of that engine. Legacy Broad Research/Research Analysis skills elsewhere in the repository remain separate workflows. Their card quotas and fixed synthesis templates do not apply to these three skills; use this canonical reference.

