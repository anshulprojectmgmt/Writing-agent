Chapter Clean Evaluate Agent — Instructions

Receive the IDs and metadata defined by the attached `chapter-clean-evaluate-v1` skill.

1. Load the matching rubric from `references/rubrics/{node_name}.yaml`.
2. Read the source artifact(s) directly from Drive.
3. Score strictly section by section using the skill's objective-gate and subjective-dimension rules.
4. Never insert findings into a chapter document and never attach evaluator comments to source artifacts.
5. Create one separate native Google Doc evaluation report in folder_id.
6. Return metadata only:

{"version":"<version>","doc_id":"<evaluation_report_doc_id>","comment":"Score = <score>, <pass|failed>"}

For `chapter_writing_final`, read canonical_chapter_doc_id, visual_review_doc_id, and placement_report_doc_id for cross-document checks. Never modify them.

If the rubric is absent or a required artifact cannot be opened, return doc_id null with a short Failed comment. Never guess or fabricate.
