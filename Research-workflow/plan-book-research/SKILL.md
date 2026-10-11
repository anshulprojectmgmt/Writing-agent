---
name: plan-book-research
description: Plan and coordinate future-oriented nonfiction research for Products of Tomorrow, from lightweight background and professional perspectives to question-led investigations, synthesis and conditional gap research. Use to plan research, run a book-topic workflow or coordinate chapter research.
---

# Plan Book Research

Read [the canonical contracts](references/output-formats.md) before creating stage outputs or worker briefs. This is the single shared reference for questions, search authorization, source screening, output formats and delivery.

## Mission and controls

Explore how the topic could evolve: present signals, driving forces, future products and behaviors, competing scenarios, second-order consequences and constraints. Treat these as thinking dimensions, not required headings. Follow the supplied book profile, broad audience, scope and frozen decisions; do not invent a PM-only audience or unprovided frameworks. Facts ground imagination; they do not prohibit it. Distinguish verified evidence, emerging signals, interpretation and speculation.

Use a **Question Map, never a Term Map or Query Map**. Begin background with the topic and lightweight guiding prompts, not a compulsory initial question set. Before expert research, apply the question acceptance gate in the shared contract. Require broad, open-ended, consequential, future-oriented top-level questions; rewrite topics, keyword clusters and narrow retrieval tasks. Preserve stable Q IDs and question-to-source links as the map evolves.

Set `search_provider: native` by default. Enable `exa` or `compare` only after checking explicit Exa authorization for this individual run and available tools. Pass the authorization record to every worker; never infer it from "deep research" or "all available tools", activate it because native results are weak, or carry it into another run. Follow the shared provider decision table.

Run autonomously unless the user requests checkpoints. Delivering the research package does not authorize external publication. Apply the shared editorial pass to skill edits and research outputs: emphasize important insights, preserve reasoning and cut repetition, padding and trivial explanation.

## Independent execution

Keep one planner as owner of the running index and canonical map. In a main user conversation, launch a fresh planner when supported; use the main conversation for communication. Launch background, question-generation, expert, targeted and synthesis workers in fresh contexts with `fork_turns: "none"` or equivalent. Supply distilled briefs and exact artifact paths, never full-chat inheritance.

Run independent question-generation and expert investigations in parallel within available slots. Give each professional role its own context and output, even when scheduling in batches. Use immutable input snapshots; workers write only exclusive assigned artifacts and never the running index. Use a fresh synthesis worker for each pass. If independent contexts or parallelism are unavailable, disclose the limitation and use artifact-based sequential handoffs without claiming isolation or concurrency.

## Workflow

1. **Frame.** Record topic, future-oriented objective, audience, scope, time horizon/as-of date, assumptions, frozen decisions, execution mode, destination, search-provider authorization and artifact index. No detailed initial Question Map is required.
2. **Background.** Assign a fresh `research-book-topic` worker a lightweight brief: meaning and significance, important developments, changing forces, uncertainties and dimensions needing deeper inquiry. Attempt all ten Source Ladder rungs using actual searches or source inspection; vary depth by value, with no finding quotas and no skipped rungs. Request a concise narrative, usually up to 1,000–1,500 words when warranted and shorter when sufficient. Read examples and sources, not merely a capability inventory.
3. **Select experts.** Use the two-level selection process below, grounded in the accepted background. Select complementary perspectives, usually four to six when justified; no panel-size quota. Record the generic role, any justified domain specialization, selection rationale and blind spots. **Never put company names in role or persona identities.** These are analytic lenses, not real interviews.
4. **Develop the Question Map.** Use the grounded expert-question process below. Each fresh expert must read the frame, background narrative, cited examples and relevant source notes before proposing broad future questions. Require visible background anchors and a short explanation of what future change the question explores. Merge overlaps while preserving dissent, apply the question acceptance gate, then assign research. Narrow cases such as a holiday are supporting investigations, not entire perspectives.
5. **Expert research.** Assign a fresh worker per role, with common background, its broad questions, source/evidence namespace, provider record and exclusive path. Require all ten rung attempts, source screening and substantive notes that preserve authors' reasoning. Permit important new questions during research. Merge question revisions, source dependencies and statuses without erasing dissent.
6. **Synthesis 1.** Assign a fresh `synthesize-book-research` worker all accepted background/expert outputs, current map and supplied book state. Require the Research Analysis-derived Framing Check and seven-section synthesis in the shared contract, with future forms, mechanisms, competing scenarios, second-order effects and chapter opportunities. Preserve conceptual and evidential judgment rather than replacing it with a generic future essay.
7. **Gap decision.** Rank only gaps that could change a major conclusion, scenario or chapter argument. Specify question, significance, missing evidence, owner and exit condition. No useful result after a real rung attempt does not automatically create a substantive gap. An unattempted rung is a process omission requiring correction before acceptance, regardless of whether it seems likely to change the thesis. If no consequential gap warrants targeted work, record the decision, skip Step 08 and proceed to the fresh final synthesis at Step 09.
8. **Targeted research, conditional.** For justified gaps, launch fresh workers with prior evidence and exit conditions. Return changed answers, counterevidence, actual attempts/null results and residual uncertainty. Attempt every rung for the targeted questions, without repeating the background report or adding finding quotas.
9. **Final synthesis.** Use a fresh synthesis worker to integrate the combined evidence and record changed conclusions, using the same seven-section contract. If no targeted retrieval was warranted, supply the no-gap decision and do a fresh integration/challenge pass without manufacturing new research. Keep first-pass and final judgments distinct; a fresh synthesis can expose connections that another retrieval pass would not.
10. **Final package.** Reconcile the current map/history, background, panel, questions, expert notes, synthesis, gap decisions/outcomes and source index. Provide a linked reading guide, defensible insights, uncertainty and what could change the view. Mark an unwarranted targeted-research step as skipped in the index rather than creating an empty report; final synthesis still runs.

Use the dedicated stage formats and worker brief in the shared contract. Accept outputs only after checking question validity, future-first purpose, citations/provenance, source screening, evidence-versus-inference distinctions and editorial quality. Correct failures within the existing roles; do not add an evaluator skill or stage.

## Expert selection: two levels

**Level 1 — Generic professional role.** Start with a broad human role: Product Manager, UX Researcher, Product/Interaction Designer, Software/AI Engineer, Economist, Business Leader, Marketing Leader, Sales Leader, Risk & Governance Specialist or Domain Specialist. Select roles because they reveal different parts of the topic's future, not because they sound realistic. Economics, user behavior, product form and technical feasibility are distinct lenses; several interchangeable commercial roles may not be needed.

**Level 2 — Domain-specific professional role.** Specialize only when the background reveals a domain problem that the generic lens would miss. AI's employment effects may justify a **Labor Economist**; economy-wide effects a **Macroeconomist**; financial-services economics a **BFSI Economist**. Record the Level 1 parent and why the specialization changes the investigation. Do not add a specialty merely for specificity, seniority or persona realism.

For each expert, record `P ID | Level 1 role | Level 2 specialization or none | future contribution | background anchors | distinct perspective/blind spot`. Check overlap and omitted consequential perspectives. Company names can appear in source anchors and research subjects, never in the professional identity.

Give every selected expert the same mission: **Explore and define the future of the topic through your professional perspective. Investigate today's signals, what is changing, plausible future states, shaping forces, new products/behaviors/markets and consequences.** The role determines the lens, not a narrower final objective.

## Expert questions: grounded in background, open to discovery

Give each fresh question-generating expert the exact paths to the frame, accepted background, source index/substantive notes, panel rationale and any existing questions. Require it to read the background and its concrete illustrations before writing. If an essential artifact is unreadable, return the limitation for correction; do not invent grounding or claim to have read it.

1. Identify developments, pain points, mechanisms, contradictions and missing dimensions that matter through this role. Distinguish observed evidence from the background researcher's interpretation.
2. Ask how these starting conditions could evolve. Use the shared **future-first reasoning guide**: signal → changing force/constraint → future product/behavior/market → consequence → alternative or uncertainty. Evidence anchors questions; it does not predetermine answers.
3. Propose broad umbrella questions with enough room for original inquiry. For each include `question | professional lens | background anchor/example or explicitly uncovered dimension | why consequential | future change to explore`. Supporting questions can emerge later; do not pre-build a long narrow checklist.
4. Apply the top-level acceptance gate and reject topic labels, retrieval instructions, unsupported premises or a use case presented as the entire role. Merge semantic duplicates across roles without erasing different causal explanations or opposing incentives.

**Personal Agents examples — adapt, do not mechanically copy:**

| Professional role | Broad future question | Background material to examine |
|---|---|---|
| Product Manager | How will personal agents evolve as products, and transform value, differentiation, distribution and competition? | Existing product forms, strategic direction, service access, business incentives and unresolved adoption |
| UX Researcher | How will human needs, expectations and behaviors evolve as people delegate activities and decisions to personal agents? | Observed pain, actual delegation choices, trust/control, longitudinal use and whose needs remain unmet |
| Designer | What will future human-agent interactions look and feel like, and what might replace or transform today's app interfaces? | Current interaction patterns, approval/recovery examples, intent expression and changing mental models |
| AI Engineer | What will future agents be capable of, and which advances, constraints and architectures will shape their evolution? | Tool use, memory, interoperability, evaluation, failure and emerging capability signals |
| Economist | How could personal agents change value creation, market structures and the relationship between consumers and businesses? | Intermediation, search/transaction costs, pricing, incentives and access restrictions |
| Business Leader | What business models, ecosystems and competitive structures might emerge? | Distribution, partnerships, platform control, emerging revenue models and competing strategies |

For example, documented approval checkpoints can motivate a Designer question about evolving control interfaces. They do not justify assuming users want full autonomy. A holiday scenario can illustrate delegation and recovery underneath a broad question; it is not proof of user pain or the scope of the whole investigation.

Accept the question-generation output only if its grounding is visible, the questions explore the future through the role, and new/unexpected directions remain possible. Revisit the map after each research pass.

## Save accepted stages

Create a dedicated Google Drive folder per run and save each completed stage as a separate native Google Doc. Combine parallel outputs within their numbered stage document without discarding substantive notes. Update accepted documents by ID rather than creating duplicate versions. Use the environment's current Google Drive/Docs skills for native creation and formatting.

Keep operational metadata in a compact appendix/index and readable arguments in the main text. Verify saved content, native document type and folder membership; record actual links/status before advancing. Preserve portable Markdown handoffs. Disclose failed writes or unavailable adapters without claiming persistence. The final package links earlier stage documents rather than repeating all their prose.

