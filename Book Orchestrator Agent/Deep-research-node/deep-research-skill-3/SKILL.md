---
name: deep-research-skill-3
description: "Use this skill to expand the evidence already assigned during Research Mapping and resolve identified GAPs. This skill builds a citation-backed evidence package for chapter writing by deepening commitments to assigned evidence — finding stronger supporting details, building citation trails, and resolving research gaps. It covers reading assigned evidence, resolving gaps, building evidence packages, and building gap packages. It does not redesign the chapter, assign new research items beyond gap resolution, write chapter prose, or expand chapter scope. The final output is a citation-backed evidence package ready for chapter writing."
---

# DEEP RESEARCH SKILL

---

## OBJECTIVE

Expand the evidence already assigned during Research Mapping and resolve identified GAPs.

**The Chapter Blueprint has already committed to the structure.**
**The Research Mapping phase has already committed to the evidence.**

Your job is to deepen those commitments and build a citation-backed evidence package for writing.

**Do not:**
- Redesign the chapter
- Assign new research items unless required to resolve a GAP
- Write chapter prose
- Expand chapter scope

Output should contain evidence, citations, facts, metrics, quotes, mechanisms, caveats, and source trails only.

---

## INPUTS

### Required

| Field | Type | Required | Description |
|---|---|---|---|
| `broad_research_doc_id` | Doc ID | Required | The Google Doc produced by the `broad-research` skill for this chapter topic. Use the most recently updated version, not necessarily `v1`, in case it's been revised since. |
| `research_mapping_doc_id` | Doc ID | Required | The Final Chapter Blueprint (Mapped Version) produced by `mapping-research-to-chapter` — contains the Evidence Assignments, GAP Flags, and Coverage Summary this skill works from. Use the most recently updated version, not necessarily `v1`: if `chapter-revision-skill` has patched it since, take the latest version instead of the original. |
| `deep_research_folder_id` | Folder ID | Required | The Drive subfolder under the main agent's workspace where this skill's output gets saved. |

**Also needed:**

**Book Profile**

Use for:
- Audience
- Depth level
- Writing goals
- Reader sophistication

---

## CORE PRINCIPLE

### Deepen Commitments, Don't Expand Scope

**The Blueprint has already decided:**
- What belongs in the chapter
- What belongs in each section
- What belongs in each subsection

**The Mapping phase has already decided:**
- Which research assets support each subsection

**Your responsibility is to:**
- Go deeper into assigned evidence
- Find stronger supporting details
- Build citation trails
- Resolve research gaps

---

## WHAT TO RESEARCH

Work through every subsection in blueprint order.

For each subsection there are two possible inputs:

**Assigned Evidence**
Evidence already mapped to the subsection — research deeper into these items.

**GAP Flags**
Missing evidence identified during Research Mapping — research specifically to resolve these gaps.

---

## STEP 1 — READ ASSIGNED EVIDENCE

For every assigned evidence item, identify:
- Source
- Publication
- Author
- URL
- Original research notes
- Confidence level

**Then deepen the evidence. Look for:**

- **Facts** — Specific findings and observations
- **Statistics** — Metrics, percentages, benchmarks, outcomes
- **Mechanisms** — How something works, why it works, what caused the result
- **Quotes** — Short, directly usable quotes
- **Outcomes** — Business impact, product impact, user impact, organizational impact
- **Surprising Details** — Counterintuitive findings, unexpected observations, non-obvious insights
- **Caveats** — Limitations, failure modes, criticisms, contradictory evidence

---

## STEP 2 — RESOLVE GAPS

**For every GAP determine:**

**What Is Missing?**

**What Evidence Type Is Needed?**

Examples:
- Named Example
- Statistic
- Case Study
- Academic Finding
- Expert Signal
- Historical Reference
- Framework

**Search specifically for that evidence. Prefer by tier:**

- **Tier 1** — Peer-reviewed papers, meta-analyses, original research, institutional studies, government publications
- **Tier 2** — Industry reports, enterprise studies, benchmark reports
- **Tier 3** — Expert interviews, founder insights, practitioner analysis
- **Tier 4** — News articles, commentary, opinion pieces *(only if stronger evidence is unavailable)*

---

## STEP 3 — BUILD EVIDENCE PACKAGE

**For every assigned evidence item provide:**

### Citation
- Author
- Publication
- Year
- URL

### Deep Bullets

- **Specific Fact** — A concrete fact
- **Mechanism** — How or why it works
- **Statistic** — If available
- **Quote** — If available *(keep concise)*
- **Surprising Detail** — Counterintuitive finding or observation
- **Caveat** — Limitation or opposing evidence

---

## STEP 4 — BUILD GAP PACKAGE

**For every GAP:**

### If Resolved

**GAP FILLED**
- Original GAP
- Source — Publication and URL
- Citation — Author / Publication / Year / URL
- Deep Bullets
  - Supporting fact
  - Supporting evidence
  - Supporting statistic
  - Caveat

### If Unresolved

**GAP UNRESOLVED**
- Original GAP
- Searches Conducted — What was searched
- Findings — What was found
- Recommendation — Choose one:
  - Cut claim
  - Soften claim
  - Mark uncertainty
  - Leave for future research

---

## OUTPUT FORMAT

Draft the package's content against the structure below — this is the
content spec, not the delivery format. The finished document is worked from
side by side with the mapped blueprint during chapter writing, not read
once, so when the content is complete it is rendered as HTML and delivered
as a Google Doc per **Render & Deliver** below, using
`references/output-formatting.md` for the markup. Nothing here is saved as a
standalone `.md` file.

---

# DEEP RESEARCH PACKAGE

**Chapter:** [Chapter Name]

---

### [N.X] — [SUBSECTION NAME]

**EVIDENCE**

[Evidence Item Name]

**Citation**
Author / Publication / Year / URL

**Deep Bullets**
- → Specific fact, statistic, or finding
- → Mechanism or explanation
- → Direct quote (if available)
- → Surprising detail
- → Caveat or counterpoint

---

**GAP FILLED**

[Original GAP]

**Source**
Publication / URL

**Citation**
Author / Publication / Year / URL

**Deep Bullets**
- → Supporting fact
- → Supporting evidence
- → Supporting statistic
- → Caveat

---

**GAP UNRESOLVED**

[Original GAP]

**Searches Conducted**
[List]

**Recommendation**
Cut / Soften / Mark Uncertainty

---

*Repeat for every subsection.*

*Skip subsections marked* `EVIDENCE: NONE` *unless a GAP exists.*

---

## RESEARCH SUMMARY

As above, this is the content spec — the metrics table becomes a real Doc
table at the **Render & Deliver** step, per `references/output-formatting.md`:

| Metric | Count |
|---|---|
| Total Evidence Items Expanded | N |
| GAPs Resolved | N |
| GAPs Partially Resolved | N |
| GAPs Unresolved | N |

**Strongest New Findings**
[List]

**Strongest Statistics**
[List]

**Strongest Case Studies**
[List]

**Strongest Academic Findings**
[List]

**Remaining Research Needs**
[List]

---

## WRITING HANDOFF

The final output should provide everything required for chapter writing.

**Every important claim should have:**
- Supporting evidence
- Citation trail
- Facts
- Statistics
- Quotes
- Caveats

ready for direct use in the writing phase.

---

## OUTPUT RULES

**Do not:**
- Redesign the blueprint
- Modify sections or subsections
- Assign evidence to new locations
- Write chapter prose
- Summarize entire topics
- Conduct broad topic research

**Research only:**
- Assigned evidence items
- Identified GAPs

The final deliverable should be a citation-backed evidence package ready for chapter writing.

---

## Render & Deliver

This skill only ever produces `v1` — it runs once per chapter. All
revisions from reviewer feedback are handled entirely by
`chapter-revision-skill`, which owns versioning (`v2` onward) for every
skill's output. Nothing here reads or writes a version tracker.

Your input includes `deep_research_folder_id` — the exact Drive folder to
use. Do not resolve, create, or guess at a different location.

**1. Produce the complete Deep Research Package**, including the Research
Summary above.

**2. Render the package as HTML per `references/output-formatting.md`.**
Apply its markup to every block — the document title and chapter field,
every subsection, every EVIDENCE block with its citation and deep bullets,
every GAP FILLED and GAP UNRESOLVED block, the Research Summary's metrics
table and five labeled lists, and the Writing Handoff — without changing any
fact, statistic, mechanism, quote, caveat, citation field, search log, or
recommendation from Step 1. This is a markup pass only.

The output is **HTML, not Markdown**. Three rules decide whether it renders:

- **No CSS.** No `style` attributes, no `<style>` blocks, no `class`. They
  are stripped during conversion, and writing them creates a false
  impression that spacing, shading, or the FILLED/UNRESOLVED distinction is
  handled.
- **Every blank line is a `<p>&nbsp;</p>` spacer paragraph.** Whitespace and
  newlines in the source HTML are ignored by the converter. The spacer is
  the only spacing mechanism that survives — and it is what keeps every
  evidence item name from running into its citation, and every citation from
  running into its deep bullets.
- **Escape `&` as `&amp;`** in all content, and write em dashes as
  `&mdash;`.

The typed `---` rules and `→` bullet markers in the Output Format above are
chat-draft conventions. They do not survive: rules become `<hr>`, and deep
bullets become real `<ul>`/`<li>` lists whose kind (`Fact`, `Mechanism`,
`Statistic`, `Quote`, `Surprising detail`, `Caveat`) is a bold label on each
item — see the reference file for each template.

**3. Write the HTML to a file** in the sandbox, e.g.
`/home/user/deep-research.html`. Build it in parts if that is easier;
concatenate to one file before the next step.

**4. Create the Google Doc from code, reading that file into a variable.**

> **Never pass the HTML as a literal tool-call parameter.** A deep research
> package runs long once every assigned item across 10–20+ subsections
> carries a citation and six deep bullets. Typing it into a tool call means
> re-emitting the whole document as tokens, which truncates, fails, and
> leads to placeholder text being sent instead. The document body must reach
> the tool as a **variable read from the file**, never as text you retype.
> Do not print the HTML to inspect it, and do not try to copy it out of a
> previous output — open the file and pass the handle's contents.

```python
with open('/home/user/deep-research.html') as f:
    content = f.read()

from gumloop import Gumloop
client = Gumloop()

result = client.mcp.execute("gdocs", "create_doc", {
    "title": "{Chapter Name} — Deep Research Package",
    "content_format": "html",
    "content": content,
    "folder_id": "{deep_research_folder_id}"
}).results[0]

print("status:", result.status)
if result.status != "success":
    print("error:", result.error)
print(result.decoded_content)
```

Nothing is written anywhere outside that folder.

If the created document ever ends up holding placeholder text, do not create
another one. Fix the same document in place with `update_doc`, passing
`operation: "replace"` and the content read from the file exactly as above.

**5. Return only the Doc link.** Not the content, not a summary — the Doc
link is your entire output. Nothing else gets returned, and nothing gets
saved or uploaded anywhere outside `deep_research_folder_id`.

---

## References

- `references/output-formatting.md` — defines the **HTML** markup for the
  generated Deep Research Package: how the document title and chapter field,
  each `N.X —` subsection, each EVIDENCE block with its item name, citation
  and labeled deep bullets, each GAP FILLED and GAP UNRESOLVED block, the
  Research Summary's metrics table and its five labeled lists, and the
  Writing Handoff must be marked up (never how the content is worded). This
  package is delivered as HTML, not Markdown, following the same procedure
  as the Broad Research, Research Analysis, Chapter Blueprint, and Research
  Mapping skills' own `output-formatting.md` files. CSS does not survive the
  Google Docs conversion, so all spacing comes from `<p>&nbsp;</p>` spacer
  paragraphs and never from `style` attributes, and `<blockquote>` does not
  survive either, so source quotes stay inline inside their bullet. Unlike
  its sibling skills, this one promotes `N.X —` subsection titles to real
  `<h3>` headings — the subsection is this document's only navigational
  spine, and jumping to one is the whole reason a writer opens the Doc; the
  reference file explains the divergence. Apply this at the formatting step
  in **Render & Deliver** above, after the package and the Research Summary
  are fully drafted.

---

## Output

| Field | Type | Description |
|---|---|---|
| `deep_research_doc_id` | Doc ID | The Google Doc ID of the complete Deep Research Package (evidence expanded, GAPs resolved where possible), saved to `deep_research_folder_id`. This is the skill's entire return value — no content, summary, or research-summary table is returned alongside it. |
