---
name: synthesize-book-research
description: Turn source-heavy nonfiction book research into a seven-section synthesis with a framing check, deduplicated concepts, live tensions, disconfirmation, a falsifier, and question-linked gaps. Use for either synthesis pass in plan-book-research, or when asked to make sense of research, assess evidence, or prepare findings for chapter development.
---

# Synthesize Book Research

Read [the canonical output contracts](../plan-book-research/references/output-formats.md) before drafting. Resolve this path from this skill directory; do not copy the reference.

## Context and invariants

Execute as the researcher role in a **new fresh separate context**, distinct from research workers and the planner. Use a new instance for synthesis 1 and another for synthesis 2; never inherit all chat or reuse a prior worker. For actual launches require `fork_turns: "none"` or equivalent with minimal task-local artifact briefs. Read all supplied research artifacts before drafting; use book state to reconcile frozen decisions, settled terminology, rejected frames, and carried tensions.

Use a **Question Map**, never a Query Map. Q IDs drive evidence grouping, knowledge-map links, conclusions, gaps, and handoffs. Preserve links from questions to E/S IDs and sources; report answer status and unresolved questions. Lower-level searches may be used under explicit Q IDs for provenance or disconfirmation, without introducing a term, synonym, or keyword map. Do not mistake repeated coverage of one source for independent corroboration.

Follow the supplied book frame, audience, and scope; favor GenAI-specific interpretation where genuinely supported. For Products of Tomorrow, write for its broad audience without invented pillars or a PM-only constraint. Translate research bookkeeping into plain writing judgments while keeping inline source links and evidence IDs traceable. Note incomplete input and continue honestly; do not invent missing studies or judgments.

## Draft and challenge

1. Open with the canonical **Framing Check**, under 200 words: stated question, actual question, assumption underneath, constraint test, serious alternative frame, and HOLDS/REFRAME PROPOSED verdict. In autonomous mode show a proposed alternative and continue under the authorized frame; never silently substitute it or stop unrequested. In explicit stepwise mode return it to the planner for the requested checkpoint before a dependent reframe. Do not reopen frozen decisions without new evidence.
2. Build a concept registry covering Framing Check and Sections 1–5. Assign each named or synonymous concept one full write-up: a built mechanism/theory goes to Technical Concepts; a transferable framework/distinction to Mental Models; a recurring argument to Themes. Elsewhere cross-reference without repeating explanation or the same signature example. Run a duplication pass before Section 5 and record merges.
3. Write the seven exact core sections and their canonical field/length rules: Central Concept; Themes; Mental Models; Technical Concepts; What to Retain, Downgrade, or Remove; Chapter Synthesis Ideas; Final Conclusion. Include inline citations supporting material claims. Keep a source's measured result distinct from author interpretation.
4. In Section 5 account for evidenced claims: retain strong backing, downgrade early/thin/academic-only adoption assertions, explicitly remove unsupported marketing, unverifiable figures, and unobserved demand. Do not silently drop claims previously labelled evidenced. Treat practitioners as sources for their observations, not automatic proof of broader behavior. Explain classification changes against original evidence labels rather than overwriting the original cards.
5. Preserve real **Live Tensions** with strongest Side A/Side B cases and their sources, why unresolved, and chapter use. Do not invent a tension, force a resolution, or split settled evidence into false balance. State honestly when none is supported.
6. Add **Disconfirming Evidence** beside the Section 5 judgment: two or three specific conditions that would weaken the frame, actual question-linked searches/results including null results, and a pointer to Section 7's falsifier. Run 1–3 targeted searches against the Central Concept if none already address the needed conditions; write new evidence cards in the assigned synthesis support artifact. Do not make a separate evaluator role or stage.
7. Build Section 7's defensible conclusion entirely from Retain-level material and state one specific observable falsifier. Chapter ideas in Section 6 suggest structures only; do not introduce new research claims.
8. Include Section 8 Research Gaps & Opportunities only for material unresolved gaps. Preserve Q/G IDs, significance, evidence needed, suggested owner and exit condition in the separate gap handoff, even when the prose does not expose process scaffolding. Do not perform the entire next targeted round here; return its bounded questions to the planner.

Aim for 1,500–3,000 words, allowing 3,000–4,000 when warranted by gaps and chapter flows. Allow roughly 400–600 extra words for framing and judgment rather than compressing substantive sections to fit. Keep judgment next to the material judged and write plain, direct prose. Record empty disconfirmation/tension results honestly rather than manufacturing content.

## Pass-specific handoff

For **synthesis 1**, deliver synthesis, concept registry, question-answer/knowledge map update, and ranked gap handoff for round 2. Include evidence conflicts, background coverage shortfalls, and what could change the conclusion.

For **synthesis 2**, read background, all expert and targeted briefs, synthesis 1, gap outcomes, and updated Question Map. Rebuild the synthesis from combined evidence rather than merely editing the earlier text. Deliver final synthesis, concept registry, closed/partial/open question status, gap outcomes, and a change log of strengthened, weakened, reversed, or unchanged claims with E IDs. If evidence remains missing, state the limitation and its chapter implication. Do not promise that additional retrieval settled all questions.

Append the canonical Completeness Summary, verify section presence, citations, deduplication, tension/disconfirmation status, and falsifier before returning. These are researcher checks, not a separate evaluator. Save assigned artifacts only; the planner alone updates the running document. Return artifact paths and framing/gap status. Use available persistence tools and honor explicit destinations; render HTML/Google Docs only through the canonical formatting and delivery rules when requested.
