---
name: chapter-clean-evaluate-v1
description: Report-only evaluator for Chapter Writing artifacts. Scores either the canonical Anshul-style chapter or the final LinkedIn-style + visuals chapter without modifying or commenting on the chapter document. All findings live in a separate evaluation report.
---

# CHAPTER CLEAN EVALUATE

## Role

Evaluate Chapter Writing artifacts without changing them.

This evaluator exists specifically because chapter documents are reader/author artifacts and must remain clean. Unlike the pipeline's legacy evaluator, this skill never inserts findings blocks and never attaches evaluator comments to the chapter Doc.

## Inputs

Required:
- `doc_id`
- `version`
- `folder_id`
- `node_name` — `chapter_writing` or `chapter_writing_final`

For `chapter_writing_final`, also require:
- `canonical_chapter_doc_id`
- `visual_review_doc_id`
- `placement_report_doc_id`

## Rubric loading

Load `references/rubrics/{node_name}.yaml`.
If it does not exist, return no_rubric failure. Never guess.

## Scoring

Evaluate section by section.

Objective dimensions:
- structural
- content_completeness

If any objective check in a rubric section fails without an exception stated in the check, that section scores 0.

Subjective dimensions:
- quality
- purpose_alignment
- consistency

When objective gates pass, score each populated subjective dimension by the fraction of checks that hold, then combine by the dimension weights.

Dynamic rubric sections are scored once per matching instance and averaged.

Final score is the weighted average of rubric-section scores. Compare to pass_threshold.

A rubric red flag zeros the affected section unless the rubric explicitly says otherwise.

## Cross-document final evaluation

For `chapter_writing_final`, read:
- final Artifact B (`doc_id`)
- canonical Artifact A (`canonical_chapter_doc_id`)
- Visual Review (`visual_review_doc_id`)
- Visual Placement Report (`placement_report_doc_id`)

Use them only to verify structure/evidence preservation and visual decision accounting. Do not alter any of them.

## Findings

Draft concise, locatable findings for every failed/partial dimension and one general finding for clean sections.

All findings go only into the evaluation report.

## No-write rule

Never write to doc_id.
Never write to canonical_chapter_doc_id.
Never write to visual_review_doc_id.
Never write to placement_report_doc_id.
Never add comments to any source artifact.

## Evaluation report

Create a separate native Google Doc in folder_id containing:
- evaluated artifact and node_name
- status
- final_score
- pass_threshold
- low-scoring sections
- section/instance scores
- findings in document order
- for final evaluation: explicit style, cleanliness, structure/evidence-preservation, and visual-accounting results.

## Output

Success:
{
  "version":"<version>",
  "doc_id":"<evaluation_report_doc_id>",
  "comment":"Score = <score>, <pass|failed>"
}

No rubric/failure returns doc_id null with a short Failed comment. Never fabricate IDs or scores.

## Mandatory integrated execution and preservation gates

Read the updated Chapter Writing SKILL.md and every mandatory writing/voice/output reference plus skill-sources.json. For Artifact A, verify contract version 1 and all five checks against Notes, actual prose and native/rendered formatting. Missing provenance, skipped steps, templated previews or unverified formatting blocks a pass regardless of weighted score. Self-declaration alone is insufficient. Include checked paths/hashes, matching Artifact A ID and five check results in the separate evaluation report. Controller copies only verified metadata into durable state.

For Artifact B, compare reader-facing wording and native emphasis with A, excluding workflow appendices and inserted figure captions/accessibility descriptions. Visual Placement may not perform another voice rewrite. Preserve author-approved functional icons. Report any drift. A missing/stale integrated execution receipt blocks final pass. Keep source documents unchanged.

### Execution receipt in the canonical evaluation report

After creating the independent report, include one machine-readable JSON receipt with `report_doc_id` equal to that report's actual ID, `artifact_doc_id` equal to A, `artifact_revision_id` from native Doc readback, `status` (passed or failed), and `checks`. Each of the five checks has `{passed: <boolean>, evidence: <specific section/paragraph or rendering/readback locator>}`. Include dependency paths/source hashes in the references_verified evidence. Create/verify the report before filling its real ID; never guess an ID or issue all-true flags without inspection. Missing or failed execution/preservation gates force evaluation status failed irrespective of weighted score. Final report verifies the same matching receipt against current A.
