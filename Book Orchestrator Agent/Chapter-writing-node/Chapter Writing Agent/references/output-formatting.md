# Chapter output formatting — approved production presentation

## Authority

Read `presentation-contract.md` and `presentation-profile.json` in full. They encode the corrected Personal Agents presentation and override older Gumloop HTML templates. Do not mix the old Arial/crimson/H2/H3 template with this profile. Keep the exact bundled storytelling and writing skill snapshots unchanged; this reference controls native book-document presentation.

## Reader-facing document

Use native Google Docs styles and text runs, not literal Markdown or Unicode bold. Apply formatting within the writing worker; never defer it to Visual Placement.

| Element | Native style | Font/size | Spacing above/below |
| --- | --- | --- | --- |
| Chapter title | TITLE | Georgia 26 pt | 16/16 pt |
| Main section | HEADING_1 | Georgia 17 pt | 22/10 pt |
| Subsection | HEADING_2 | Georgia 13 pt | 14/7 pt |
| Body | NORMAL_TEXT | Georgia 12 pt | 0/7 pt |

Use black text, body line spacing 115%, heading line spacing 120%; keep headings with the following paragraph. The baseline body size was inherited and unavailable in readback: 12 pt is the explicit production default, not a claimed measurement. Do not add crimson or background highlights. Preserve meaningful native bold and italic. Do not invent a chapter number when none is supplied.

Main headings use `1. 🧭 Approved title`, `2. 🔗 Approved title`, etc. Select an icon suited to each main section's meaning, not a repeating decorative pattern. Preserve title wording and order. Subheadings are unnumbered: `What belongs in memory?`, never `3.1 What belongs in memory?`. Internal IDs and [TECH]/[WOW MOMENT] markers belong in the coverage map; retain their substantive commitments and fixed punchlines, but do not expose workflow labels in reader headings. Preserve an explicitly approved unnumbered ending when the structural brief requires it and record that author decision; do not improvise exceptions.

Use normal paragraph spacing, not empty spacer paragraphs, typed rules or HTML whitespace tricks. Paragraphs normally develop one idea in 3–7 sentences; deliberate short bridges and fixed punchlines are permitted. Do not stack short sentences as separate paragraphs to imitate a social post.

## Opening emphasis and lists

Select existing load-bearing opening claims/comparison phrases at important argument turns. Apply native bold to those exact words at the paragraph beginning; leave setup, evidence narration and ordinary bridges plain. Keep useful middle/end emphasis. Do not insert miniheading labels, repeat the next sentence, bold every paragraph or apply density quotas. Whole ordinary paragraphs are not bold. Fixed punchlines remain verbatim and bold.

Use native explanatory bullets for genuinely parallel ideas, comparisons or action questions. Each important item begins with a meaningful bold lead-in and continues with a full explanation/question. Tiny two-word fragments do not qualify. Inspect opportunities throughout the chapter, not just a token end list. Maximum two lists per section unless the author instructs otherwise. Never nest lists as a layout device.

## Evidence and citations

Keep evidence inside the developing argument. Italicise concise source/study attribution where helpful, without whole-paragraph italics or overlapping bold/italic. Preserve the finding, citation text, number, scope and caveat. Reader parenthetical citations remain plain and unlinked under this profile. Retain every exact source URL, clickable in the Handoff citation table, with the claim/section locator. Do not delete or swap sources when removing link styling. No evidence coloring, highlighting or underline.

## Working appendices

Append `Chapter Writing Notes`, `Manuscript Handoff Package`, then `Completeness Summary`. These are separate from reader prose and are removed only by Visual Placement when creating B. Use Arial 11 pt working text and native tables, never code fences.

Notes table: Section | Evidence Used | Gaps Managed | Tension Logged | Cut Decisions. One row per approved section in order. Follow with labeled Transformation Point, Voice Pass, Formatting Audit and Book Profile Source. Include internal mapping IDs/commitment tags, reference source hashes, argument decisions, humanizer changes and honest limitations.

Handoff: word count; section word counts; complete citation table (citation text | source URL | claim/section locator); evidence coverage map; gaps requiring author decision; suggested line edits. Source URLs remain clickable here. Never turn a missing required table into labeled prose and claim full formatting compliance.

Completeness Summary table: Check | Result. Include protected structure, punchlines, transformation, tension, evidence/citations, language, story integrity and native presentation results. Header shading may be light neutral gray; no evidence highlighting.

Store the presentation plan and native-validator proof as execution evidence, tied to the actual Doc ID/revision. Exact post-write revisions are stored in durable state/report, not inserted through a self-invalidating cycle into the same Doc. The in-Doc plan may contain stable paragraph locators; bind its revision in the exported execution envelope after the last write.

## Mandatory verification

Run `scripts/validate_chapter_presentation.py` on actual complete native Docs JSON and the revision-bound plan, after all writes. Confirm complete heading sequence/levels/typography, planned icons, selected opening bold, explanatory native bullets/lead-ins, plain reader citations and source URL retention. Fix conversion errors in the same unpublished Doc. Worker-only tests require this too; absence of a downstream evaluator does not waive it.

The script verifies observable placement, not literary quality. Independently inspect whether emphasis and lists serve the argument and whether facts, caveats, fixed phrases and useful middle emphasis survive. Inspect exported pages when layout/page fit is material. Do not accept generic feature counts as proof. No new workflow node or Visual Placement rewriting is authorized by this reference.
