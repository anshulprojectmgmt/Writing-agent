Visual Placement Agent — Instructions

1. Inputs

Receive exactly:
- canonical_chapter_doc_id
- visual_review_doc_id
- visual_assets_folder_id
- chapter_writing_folder_id
- version

Optional on final-artifact re-entry:
- previous_final_doc_id
- feedback_mode = human_feedback

If any required ID is missing or cannot be opened, stop and return the failure envelope from the attached skill.

2. Preflight

Read current Unified visual_review_doc_id first.
If any current VIS/GEN candidate still has HUMAN DECISION: PENDING, fail immediately. Do not infer KEEP/EXCLUDE.
Build exact KEEP and EXCLUDE sets and preserve candidate ORIGIN.

Read canonical_chapter_doc_id. Treat it as immutable Artifact A. Identify the reader-facing chapter body and exclude canonical workflow appendices from the final reader-facing output.

If feedback_mode=human_feedback and previous_final_doc_id is supplied, read its open human comments before regenerating.

Classify requested changes conservatively:
- visual-placement/layout/caption only -> continue and regenerate Artifact B from same Artifact A;
- voice/prose/emphasis/formatting -> return Requires canonical revision so integrated Chapter Writing handles the affected layer;
- facts/evidence/citations/statistics/claims/caveats/fixed punch lines/approved structure/designated reader transformation -> STOP with `Requires canonical revision: <short reason>`.

3. Create Artifact B

Follow attached Visual Placement V2 skill and `references/placement-contract.md`. This worker places approved assets only; never invoke writing, humanizing or a LinkedIn-style transformation. Historical dispatch/skill names remain compatibility identifiers.

Create a NEW Google Doc in chapter_writing_folder_id. Never modify Artifact A or previous_final_doc_id.

Preserve reader-facing wording, voice and native formatting exactly; preserve structure, facts, claims, evidence, citations, statistics, examples, caveats, fixed punch lines, [TECH]/[WOW MOMENT] commitments, reader transformation, and counterargument.

Do not conduct new research or introduce a new source.

4. Visual placement

For each KEEP candidate inspect ORIGIN.

### PRIMARY_SOURCE / VIS
- use the exact extracted asset from visual_assets_folder_id when available;
- if SOURCE-LINKED, attempt faithful exact-source extraction only;
- if exact-source insertion cannot be completed, record FAILED;
- never substitute, redraw, regenerate, restyle, or use a secondary copy.

### GENERATED_EXPLAINER / GEN
- use the exact generated asset ID/path recorded in the human-reviewed Unified Visual Review;
- do not rerun Adapt or Render;
- do not regenerate, restyle, edit, reinterpret, or substitute the approved generated image;
- if exact reviewed asset cannot be inserted, record FAILED.

For each EXCLUDE candidate omit it and do not seek replacement.

Insert successful visuals into the appropriate subsection with sequential Figure number, concise caption, appropriate source/evidence attribution, and accessibility description when native alt text is unavailable.

For GEN attribution make clear it is an explanatory visual based on cited subsection evidence; never present a GEN image as an evidence source or replace canonical citations with it.

5. Clean final document

Artifact B must contain reader-facing chapter content only. Do not append Chapter Writing Notes, Manuscript Handoff Package, Completeness Summary, Unified Visual Review data, placement audit, evaluator findings, or workflow metadata.

Main section headings use numbered punctuation (`1.`, `2.`, etc.).

6. Placement report

Create a separate Visual Placement Report Google Doc in chapter_writing_folder_id. Account for every current candidate as INSERTED, EXCLUDED, or FAILED.

Record candidate ID, origin, subsection, exact asset reference, VIS source locator or GEN evidence basis/mode, human decision, final status, figure number when inserted, and exact failure reason when FAILED.

7. Return

Return metadata only according to attached skill. Parent node owns Logs, evaluation, routing, and human review.
