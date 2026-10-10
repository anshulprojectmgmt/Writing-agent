---
name: plan-book-research
description: Plan and coordinate question-map-based nonfiction book research for Anshul, from framing and broad background through human expert perspectives, parallel research, two synthesis passes, and a final research package. Use when asked to plan research, run full chapter research, or coordinate a book topic investigation.
---

# Plan Book Research

Read [the canonical output contracts](references/output-formats.md) before writing any stage or worker brief. Keep this as the only shared formatting reference; do not copy it into the other skills.

## Operating rules

- Use a **Question Map**, never a Query Map. Stable Q IDs drive persona selection, search, evidence, answers, synthesis, and gaps. Create broad questions before background research; expand them with expert questions after reading the background. Search strings are temporary retrieval operations under a Q ID, never the organizing map. Do not introduce a term, synonym, or keyword map as an organizing stage.
- Anchor the work in generative AI wherever supported. Let the supplied book profile, audience, scope, and frozen decisions drive the lens. For Products of Tomorrow, investigate future digital products for its broad audience; do not invent a PM-only audience, four-pillar framework, or personal-life-only scope. Do not assume unavailable profile or style files exist.
- Run autonomously when asked for a full run. Stop at a checkpoint only if the user explicitly requests stepwise mode or an indispensable input cannot be inferred. State reasonable assumptions and continue. A proposed reframe is a visible alternative, not an unsolicited stop or silent change of scope.
- Interpret final publication as delivering the research package. Do not externally post, send, or publish it unless separately authorized.
- Adapt Co-STORM's grounded questions, diverse role perspectives, evolving knowledge map, and gap loop to ordinary agents and available retrieval tools. Do not claim to have executed Stanford's Python engine. See the adaptation provenance in the canonical reference.

## Separate contexts and ownership

Act as coordinator and the **single writer of the canonical running document**. If invoked in the user's main conversation, launch a fresh planner instance of this skill and give it the distilled task brief; keep the user's main conversation for communication and receiving results. The planner owns scheduling and running-document updates, not a separate evaluator role.

Launch every background researcher, question-generating expert, expert researcher, targeted researcher, and synthesis worker with `fork_turns: "none"` or the environment's equivalent fresh context. Never inherit the entire chat. Supply a minimal self-contained brief and explicit artifact paths. Synthesis is the same researcher role in a different fresh instance; launch a new instance for each pass. Do not reuse a researching agent for synthesis. If independent agent contexts are unavailable, disclose the limitation; use separate artifact handoffs and distinguish sequential fallback from actual parallel execution.

Workers write only their own assigned artifacts. They return paths and structured results, and never append to the running document. Read and merge those results yourself. Pass immutable snapshots to simultaneous workers. Limit concurrency to available slots; run batches if necessary.

## Execute the workflow

1. **Frame.** Write the frame and running-document skeleton: exact topic, goal, audience, scope, GenAI angle, time horizon, assumptions, frozen decisions, mode, destination, ID namespaces, and stage paths. Write the initial broad Question Map including shipped products, mechanisms, user behavior, economics, privacy/trust, failure, and competing explanations.
2. **Background.** Launch a fresh `$research-book-topic` instance in background mode. Require all ten Source Ladder rungs attempted and a target of five strong findings per rung, including academic and general/recent news. Read its three-section brief, cards, and coverage notes; record honest shortfalls without padding. Capture 3–5 named shipping products and the senior-PM blind spot check.
3. **Select human expert personas.** Ground a diverse panel in the background. Use concrete human company-role archetypes such as a consumer-agent PM at a major platform, a startup founder, a UX researcher, a privacy counsel, or an investor. Record company context, role, perspective, expertise, relevant Q IDs, likely blind spots, and selection rationale. Include competing incentives and an opposing stand where credible. Do not impersonate named people or treat a simulated persona as a real interview or source.
4. **Generate expert questions.** Launch fresh persona instances to read the frame, initial Question Map, and background artifact and propose grounded questions. Merge duplicates without losing dissent; keep parent Q IDs and provenance. Require questions that could change the thesis, surface constraints, or distinguish observed behavior from positioning. Produce the expanded Question Map and knowledge-map links.
5. **Parallel expert research, round 1.** Assign bounded Q IDs to fresh `$research-book-topic` expert-mode workers. Give each the common background, its persona, focus, evidence namespace, question snapshot, and output path. Require all-rung coverage attempts with deeper work where relevant; do not demand another 50 findings from every expert. Merge evidence, shared-source dependencies, answer status, and cross-links under stable IDs.
6. **Synthesis 1.** Launch a fresh `$synthesize-book-research` instance with every research artifact, frame, question snapshot, and book state if supplied. Require Framing Check, seven sections, concept registry, completeness summary, and a gap handoff. Read the output; record proposed alternative frames visibly while keeping the authorized frame unless the user chose otherwise.
7. **Gaps.** Turn material unresolved Q IDs, contradictions, low-confidence claims, disconfirmation needs, and coverage shortfalls into ranked gap records. For each: why it matters, evidence needed, responsible persona, targeted Q IDs, and exit condition. Prefer gaps that could change the conclusion over decorative breadth. Do not manufacture gaps to justify more work.
8. **Targeted research, round 2.** Launch fresh `$research-book-topic` targeted-mode workers with the relevant gap, prior evidence pointers, and explicit falsification/confirmation needs. Record answered, partially answered, or unresolved results and null searches. Avoid repeating round 1; new evidence must link to Q/G/E IDs.
9. **Synthesis 2.** Launch another fresh `$synthesize-book-research` instance with background, all expert briefs, both rounds, synthesis 1, ranked gaps, and the updated Question Map. Require a final synthesis based on the combined evidence, a change log, and honest residual uncertainty. If no material gap warrants additional retrieval, mark round 2 as no additional research warranted and still perform fresh final synthesis.
10. **Final research package.** Reconcile every Q ID and artifact path, check completeness using the canonical contract, and deliver the running document plus background, expert answers, both synthesis passes, gap outcomes, source/evidence index, and final summary. Explain unresolved gaps and what would change the conclusion. Do not hide shortfalls or imply all questions are settled.

## Worker brief and handoff

Use the canonical worker-brief schema. Include objective, role/mode, exact Q IDs, relevant context, constraints, read paths, output path, source/evidence namespace, output contract, and completion definition. Put durable context in files rather than inherited chat. Require workers to report inaccessible sources, actual searches and dates, null results, provenance, and next-stage handoff paths.

Before accepting a result, check its own stage contract, source-backed claims, question/evidence links, source labels/cards, date honesty, deduplication, and declared coverage. Request correction from that worker when necessary; perform these checks within the normal planner/researcher work, without a separate evaluator stage.

Use the available file destination and persistence tools. Honor an exact supplied destination. Render HTML only when required for a Google Doc or HTML delivery, using the canonical rules; otherwise keep portable Markdown artifacts. Return concrete paths/links and the final research status.
