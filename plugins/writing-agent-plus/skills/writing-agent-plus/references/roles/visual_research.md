# Visual Extraction adapter

Read:
- Skill: `Book Orchestrator Agent/Deep-research-node/Visual Research Agent/SKILL.md`
- Instruction: `Book Orchestrator Agent/Deep-research-node/Visual Research Agent/instruction.md`
- Source review format basis: `Book Orchestrator Agent/Deep-research-node/Visual Research Agent/references/visual-review-format.md`
- Evaluator skill: `Book Orchestrator Agent/Deep-research-node/Evaluate/SKILL.md`
- Evaluator rubric: `Book Orchestrator Agent/Deep-research-node/Evaluate/references/rubrics/visual_research.yaml`

This is the second durable Deep Research sub-agent and runs only after the current Deep Research Package passes.

Allowed primary-source pool per subsection:
1. sources mapped to that subsection in Research Mapping;
2. a primary source added by Deep Research specifically to resolve that subsection's mapped GAP.

Do not introduce unrelated image sources.

Select candidates using only:
1. directly explains the subsection;
2. contains meaningful data, mechanism, or comparison;
3. strong enough to improve the chapter.

Selection happens before extraction. Do not reject a qualifying candidate because it is technical, embedded in a PDF/page, needs cropping, lacks a standalone URL, or is inconvenient to extract.

Create a Source Visual Review covering every approved subsection. Save faithful exact-source assets to the Deep Research `Visual Assets` folder when possible. A qualifying candidate that cannot be persisted stays FOUND + SOURCE-LINKED with exact source/locator.

Source Visual Review is an internal V3 artifact. It is evaluated against the existing `visual_research` rubric, then handed to Visual Generation. It is not the final human review in new V3 runs.

Do not generate, redraw, restyle or substitute any image. Do not apply new V3 human decisions here. Human VIS+GEN decisions belong to the Visual Generation role after Unified Visual Review is built.

Historical pre-V3 source-only decision mode remains supported only when the parent explicitly identifies a legacy source-only review.

Return metadata only. Controller owns durable state and routing.
