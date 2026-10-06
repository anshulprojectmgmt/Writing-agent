# Visual Research V2 adapter

Read:
- Skill: `Book Orchestrator Agent/Deep-research-node/Visual Research Agent/SKILL.md`
- Instruction: `Book Orchestrator Agent/Deep-research-node/Visual Research Agent/instruction.md`
- Visual Review format: `Book Orchestrator Agent/Deep-research-node/Visual Research Agent/references/visual-review-format.md`
- Evaluator skill: `Book Orchestrator Agent/Deep-research-node/Evaluate/SKILL.md`
- Evaluator rubric: `Book Orchestrator Agent/Deep-research-node/Evaluate/references/rubrics/visual_research.yaml`

This role runs only after the current Deep Research Package passes.

Allowed primary-source pool per subsection:
1. sources mapped to that subsection in Research Mapping;
2. a primary source added by Deep Research specifically to resolve that subsection's mapped GAP.

Do not introduce unrelated image sources.

Select candidates using only:
1. directly explains the subsection;
2. contains meaningful data, mechanism, or comparison;
3. strong enough to improve the chapter.

Selection happens before extraction. Do not reject a qualifying candidate because it is technical, embedded in a PDF/page, needs cropping, lacks a standalone URL, or is inconvenient to extract.

Create a Visual Review covering every approved subsection. Save faithful exact-source assets to the Deep Research `Visual Assets` folder when possible. A qualifying candidate that cannot be persisted stays FOUND + SOURCE-LINKED with exact source/locator.

Every FOUND candidate begins PENDING. AI RECOMMEND/SKIP is advisory only; human KEEP/EXCLUDE is final.

Decision-application mode may update only Human Decision fields using exact user-provided VIS IDs. Never rerun discovery merely to apply decisions.

Evaluate Visual Review with `visual_research`. Do not advance while visual evaluation fails or any human decision remains PENDING.

Return metadata only. Controller owns durable state and routing.
