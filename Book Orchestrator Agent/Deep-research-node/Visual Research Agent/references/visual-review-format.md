# Visual Review V2 — Output Format

Use one clean Google Doc covering every approved subsection in chapter order.

## Document header

# <Chapter> — Visual Review <Version>

Status: HUMAN REVIEW REQUIRED

Selection rule used for every candidate:
1. directly explains the subsection;
2. contains meaningful data, mechanism, or comparison;
3. strong enough that it should improve the chapter.

Primary-source lineage: Research Mapping sources for the subsection plus a primary source added by Deep Research only when resolving that subsection's mapped GAP.

## Per subsection

### <N.X> — <Subsection title>

If candidates exist, repeat this block for each candidate:

VIS ID: VIS-###
IMAGE STATUS: FOUND
SOURCE TITLE / OWNER: <title / owner>
PRIMARY SOURCE: <exact URL>
FIGURE / ASSET LOCATOR: <figure number, page/section, chart title, screenshot locator>
WHAT IT SHOWS: <one concise description>
DIRECT SUBSECTION FIT: <why it directly explains this subsection>
DATA / MECHANISM / COMPARISON: <what meaningful visual information it contains>
CHAPTER VALUE: <why it should improve the chapter>
AI RECOMMENDATION: RECOMMEND | SKIP
EXTRACTION STATUS: EXTRACTED | SOURCE-LINKED
DRIVE ASSET: <asset id/path when extracted, otherwise N/A>
HUMAN DECISION: PENDING | KEEP | EXCLUDE

If no candidate qualifies:

IMAGE STATUS: NOT FOUND
INSPECTED PRIMARY SOURCES:
- <url>
- <url>
REASON: <why nothing in those sources passed the three selection rules>

## Summary

At the end include:
- Total subsections inspected
- Total FOUND candidates
- Total NOT FOUND subsections
- EXTRACTED candidates
- SOURCE-LINKED candidates
- Human KEEP count
- Human EXCLUDE count
- Human PENDING count

## Rules

- Never omit a subsection.
- Never convert extraction failure into NOT FOUND.
- Never introduce a secondary-source or generated substitute.
- Keep exact URLs visible and clickable.
- Human Decision is the authoritative final selection field.
