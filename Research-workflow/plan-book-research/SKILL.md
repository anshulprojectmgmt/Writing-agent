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
2. **Background.** Assign a fresh `research-book-topic` worker a lightweight brief: meaning and significance, important developments, changing forces, uncertainties and dimensions needing deeper inquiry. Consider all ten Source Ladder categories for blind spots; investigate in proportion to value, with no finding quotas. Request a concise narrative, usually up to 1,000–1,500 words when warranted and shorter when sufficient. Read examples and sources, not merely a capability inventory.
3. **Select experts.** Choose complementary professional roles from the background, usually four to six when justified. Default to Product Manager, UX Researcher, Designer, Engineer, Economist, Business/Marketing/Sales Leader, Risk & Governance Specialist or a relevant Domain Specialist. Specialize only for a substantive reason. **Never put company names in role or persona identities.** Record rationale and likely blind spots; these are analytic lenses, not real interviews.
4. **Develop the Question Map.** Ask fresh expert instances for broad future-oriented questions through their professional lens. Merge overlaps while preserving disagreement and provenance. Apply the acceptance gate before assigning research. Narrow use cases such as a holiday may support an investigation, but must not define an entire expert perspective.
5. **Expert research.** Assign a fresh worker per role, with common background, its broad questions, source/evidence namespace, provider record and exclusive path. Require source screening and substantive notes that preserve authors' reasoning. Permit important new questions during research. Merge question revisions, source dependencies and statuses without erasing dissent.
6. **Synthesis 1.** Assign a fresh `synthesize-book-research` worker all accepted expert outputs and the current map. Integrate their implications into a picture of tomorrow, with mechanisms, dependencies, alternative futures, meaningful disagreements, chapter opportunities and consequential gaps.
7. **Gap decision.** Rank only gaps that could change a major conclusion, scenario or chapter argument. Specify question, significance, missing evidence, owner and exit condition. Coverage omissions alone do not require further retrieval. If no consequential gap warrants work, record the decision and proceed to final packaging.
8. **Targeted research, conditional.** For justified gaps, launch fresh workers with prior evidence and exit conditions. Return changed answers, counterevidence, actual attempts/null results and residual uncertainty. Do not repeat broad research for procedural completeness.
9. **Final synthesis, conditional.** After targeted research, use a fresh worker to integrate the combined evidence and record changed conclusions. If no targeted pass was needed, promote accepted synthesis 1 as final after checks; do not create a redundant second synthesis.
10. **Final package.** Reconcile the current map/history, background, panel, questions, expert notes, synthesis, gap decisions/outcomes and source index. Provide a linked reading guide, defensible insights, uncertainty and what could change the view. Mark skipped conditional stages in the index rather than creating empty reports.

Use the dedicated stage formats and worker brief in the shared contract. Accept outputs only after checking question validity, future-first purpose, citations/provenance, source screening, evidence-versus-inference distinctions and editorial quality. Correct failures within the existing roles; do not add an evaluator skill or stage.

## Save accepted stages

Create a dedicated Google Drive folder per run and save each completed stage as a separate native Google Doc. Combine parallel outputs within their numbered stage document without discarding substantive notes. Update accepted documents by ID rather than creating duplicate versions. Use the environment's current Google Drive/Docs skills for native creation and formatting.

Keep operational metadata in a compact appendix/index and readable arguments in the main text. Verify saved content, native document type and folder membership; record actual links/status before advancing. Preserve portable Markdown handoffs. Disclose failed writes or unavailable adapters without claiming persistence. The final package links earlier stage documents rather than repeating all their prose.

