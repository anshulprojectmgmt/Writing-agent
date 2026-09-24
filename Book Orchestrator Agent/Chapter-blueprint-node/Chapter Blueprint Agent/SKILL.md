---
name: chapter-blueprint-5
description: "Design the complete chapter blueprint in a single pass — two sequential commitments followed by a self-critique. Block 1 produces three structural alternatives (skeleton only) for the user to choose from. Block 2 expands the chosen alternative into full sub-sections and content ideas. No evidence assignment — that is handled by mapping-research-to-chapter. Use when the user says 'blueprint this chapter', 'design the chapter', or has finished research and is ready to plan."
---

# Chapter Blueprint

Three blocks. No evidence. No review.

**Block 0** — Chapter Foundation. Define purpose, argument, transformation, tension, counterargument, and promise before designing structure.

**Block 1** — Three structural alternatives in skeleton format. Each grounded in a named pattern from references/structural-patterns.md. User picks one.

**Block 2** — Full expansion of the chosen alternative. Ideas only.

**Evidence discipline in Block 2:**
- Do NOT directly mention any evidence, resources, citations, or named studies in Block 2 sub-section descriptions
- Convey the concept, contrast, analogy, or framework only
- Evidence citing and resource attribution happens in the next skill (mapping-research-to-chapter)

Evidence mapping and flow review are separate skills that run after this one.
Use `mapping-research-to-chapter` next — it takes the approved Block 2 blueprint and
assigns evidence from the broad-research output to each sub-section.

---

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `broad_research_doc_id` | Doc ID | Required | The Google Doc produced by the `broad-research` skill for this chapter topic. |
| `chapter_blueprint_doc_id` | Doc ID | Optional | The existing chapter-blueprint Google Doc, if one already exists for this chapter and this is a revision. Omit if there is nothing to revise yet. |
| `chapter_blueprint_folder_id` | Folder ID | Required | The Drive subfolder under the main agent's workspace where this chapter's blueprint doc lives / gets saved. |

**What you need beyond the inputs above:**
- research-analysis output (primary) — read this for ideas and inspiration.
  Do not treat research items as evidence to be assigned. Treat them as raw
  material that tells you what is possible to write about.
- `broad_research_doc_id` (secondary) — also read this as an input. If
  research-analysis doesn't exist yet for this chapter, read broad-research
  directly instead. If research-analysis exists but is missing or too thin
  on something you need while blueprinting (a concept, angle, or example),
  look it up in broad-research rather than inventing it — its raw findings
  are more granular than the compressed synthesis.
- Book profile (audience, purpose, tone) — provided by the caller or given
  directly by the user.
- Structural patterns from `references/structural-patterns.md` (bundled).
- Section design guide from `references/section-design-guide.md` (bundled).

Block 2 is a structural exercise. Evidence comes later.

---

## BLOCK 0 — Chapter Foundation

Before producing structural alternatives, define the chapter's core DNA.
This block ensures every structural option serves the same argument.

| Element | Define |
|---------|--------|
| **Chapter Purpose** | Why does this chapter exist? |
| **Core Argument** | "The chapter argues that..." |
| **Reader Transformation** | Before (what reader believes) → After (what reader should believe) |
| **Primary Tension** | What problem, contradiction, or misconception drives the chapter? |
| **Main Counterargument** | What would a smart skeptic argue? |
| **Chapter Promise** | What value does the reader gain? |

---

## BLOCK 1 — Structural Alternatives

### Before producing alternatives

Read `references/structural-patterns.md` fully.

**Optional supplementary input — research-analysis Chapter Synthesis
Ideas.** If a research-analysis output exists for this chapter, skim its
Chapter Synthesis Ideas section before selecting patterns. Treat these
as *modification material*, not as patterns in their own right:
- A synthesis idea can inform *how* you adapt a named structural pattern
  (e.g. it suggests a stronger opening hook, a different grouping of
  themes, or a sharper angle for the tension) — but it never replaces
  the requirement to name and ground each option in a real pattern from
  references/structural-patterns.md.
- If a synthesis idea doesn't fit naturally as a modification to any
  pattern, don't force it in — structural-patterns.md remains the source
  of truth for architecture.
- If no research-analysis output exists yet, skip this and proceed with
  references/structural-patterns.md alone.

For each alternative, select a source pattern from that file. Each option
must be grounded in a named pattern. You are not inventing structures from
scratch — you are selecting the best-fit pattern for each angle, then
modifying it to fit the chapter's specific argument and audience.

Produce three structural alternatives. Each is a skeleton — section names and
one-line jobs only. No sub-sections. No bullets. No evidence.

The three options must be genuinely different from each other:
- Different source patterns OR the same pattern with meaningfully different
  modifications (different emotional arc, different technology positioning,
  different ethics handling)
- Different positions for the technology section (early vs late)
- Different ways of handling the honest tension or counterargument

### Mandatory rules for every option

Before presenting any option, verify all five rules. Fix silently if any fail.

1. **Name the source pattern.** Every option must state which pattern it
   derives from (e.g. "Pattern A — modified") and list every modification
   made. If two options use the same pattern, their modifications must be
   substantively different.

2. **Technology section is required.** Every option must include a `[TECH]`
   section. Its sole job is to give the reader vocabulary they can use —
   named technical concepts in plain English, connected to product behaviour.
   WOW MOMENT lives here. If the chosen pattern does not include a technology
   section, insert one and state where and why.

3. **No two consecutive sections do the same emotional job.** Label the
   emotional job of each section. If two adjacent labels are the same or
   nearly the same, merge or redesign one before presenting.

4. **The before/after contrast lives in exactly one section.** Name which
   section owns it. Do not let it bleed into adjacent sections.

5. **Every section earns its place.** For each section ask: if I removed
   this section, would the reader lose something they cannot get from any
   other section? If the answer is no, redesign or merge it.

6. **Section names are questions, ≤5-6 words.** Section names in Block 1
   and sub-section names in Block 2 must be phrased as questions (e.g. "Why
   has personalization hit a ceiling?" not "Personalization's Ceiling").
   Limit to 5–6 words max. This applies to every option, every section,
   and every sub-section without exception.

### Output format

Three alternatives, presented in chat for the user to choose from — this is
the format for that conversation, not the Doc's delivery format. The
saved Doc renders the eventually-chosen/mixed alternative as a real table
per `references/output-formatting.md` once Block 2 is complete; nothing
here is saved as a standalone `.md` file. Each alternative is presented as
a table with one row per section (5–8 sections).

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OPTION A — [Name / Angle in 3–5 words]
[One short sentence describing the reader's journey through this option.]

| # | Section | Core Idea or Concept | What It's About | What is the Conclusion |
|---|---------|---------------------|----------------|-------------------|
| 1 | **[Section name]** | [unique 2-7 word label specific to this section's logic — NOT a generic question, but the actual concept it teaches] | [what this section does — one clause] | [the specific conclusion for this chapter topic] |
| 2 | **[Section name]** | [unique 2-7 word label specific to this section's logic] | [what this section does — one clause] | [the specific conclusion for this chapter topic] |
| 3 | **[TECH] [Section name]** | [unique 2-7 word label specific to this section's logic] | [what this section does — one clause] | [the specific conclusion for this chapter topic] |
| ... | ... | ... | ... | ... |
| N | **[Section name]** | [unique 2-7 word label specific to this section's logic] | [what this section does — one clause] | [the specific conclusion for this chapter topic] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Repeat for Options B and C. Each option uses the same table structure
but fills in different section names and different "What Is the Conclusion" content.

After presenting all three, say:
"Pick an option, mix elements from two, or tell me what to change —
then I will expand it fully in Block 2."

**Wait for the user's response before proceeding to Block 2.**

---

## BLOCK 2 — Full Expansion

Expand the chosen structural alternative into full sub-sections and content ideas.

### What to read

Read the research-analysis output to understand the conceptual territory —
what kinds of ideas, analogies, frameworks, and contrasts the research
surfaced. Use it as inspiration for what each sub-section should cover
conceptually, not as a source of examples to cite. Do not map specific
research findings, citations, named products, or case studies into
sub-section descriptions — that is handled by the research-mapping skill
that runs after this one. If no research-analysis output exists yet for
this chapter, read the broad-research output directly instead. If
research-analysis exists but doesn't cover something a sub-section needs
(a concept, contrast, or example), check the broad-research output for it
before inventing one — its raw findings go deeper than the synthesis.

### Output format

Draft the content against the structure below — this is the content spec,
not the delivery format. Once complete, it is rendered as HTML and
delivered as a Google Doc per **Render & Deliver** below, using
`references/output-formatting.md` for the markup; nothing here is saved as
a standalone `.md` file. One entry per section in the order chosen in
Block 1.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**N — [SECTION NAME]**
[One line — what is the conclusion for this section]

**N.1 — [SUB-SECTION NAME, phrased as question ≤5-6 words]**
[1-2 line description of what this sub-section covers conceptually — the concept, contrast, analogy, or framework it introduces. No research citations or product examples.]

**N.2 — [SUB-SECTION NAME, phrased as question ≤5-6 words]**
[1-2 line description of what this sub-section covers conceptually.]

**N.X — [WOW MOMENT / SUB-SECTION NAME, phrased as question ≤5-6 words]**
[A flag indicating this sub-section features a surprising, sourced finding that proves the architecture is real. Describe what it demonstrates conceptually — do not cite the finding itself.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Rules

**Structure:**
- Every section starts with a one-line conclusion (what the reader should know after this section).
- Every sub-section has a bold name followed by a 1-2 line description.
- At least one section must contain a WOW MOMENT sub-section — label it.
- Sub-sections are not optional. Every section needs at least two.
  If you cannot find two distinct beats, merge the section with another.

**Ideas-only discipline (structural descriptions only):**
- Sub-section descriptions describe what the sub-section covers conceptually —
  the concept, contrast, analogy, or framework it introduces.
- Do NOT include specific research findings, citations, named products,
  case studies, or evidence in Block 2 sub-section descriptions. Evidence
  mapping is a separate step that runs after the blueprint is approved.
- If you cannot describe what a sub-section does without reaching for a
  specific research citation, the sub-section needs a clearer conceptual
  job — merge or redesign it.
- Do not assign evidence tags. Do not reference [HERO] or [USE] items.
- Do not reference the annotated research file.

**Anti-redundancy check (run silently before outputting):**
- No two sections have the same emotional job
- The before/after contrast appears in only one section
- The technology section introduces vocabulary not present anywhere else

If any check fails, fix the structure before outputting.

**Technology section requirement:**
The `[TECH]` section from Block 1 must expand into sub-sections that:
- Name 1–3 specific technical concepts relevant to the chapter topic
- Explain each in plain English (what it is, what it enables in product)
- Include a WOW MOMENT sub-section — a named research finding or
  benchmark that surprises a knowledgeable reader
- Leave the reader with vocabulary they can use in a meeting

See `references/section-design-guide.md` for the full Technology Beneath specification.

---

## Completeness Summary

Immediately before saving, append a short machine-readable summary block —
this lets the evaluator run its cheap structural checks without
re-reading the full blueprint:

```
COMPLETENESS SUMMARY
Sections: [N]
Sub-sections per section: [counts]
WOW MOMENT present: [yes — section N.X / no]
[TECH] section present: [yes / no]
Anti-redundancy check: [pass — no issues / issues found and fixed: ...]
Evidence-free check: [pass — no citations/products/case studies present / issues found]
```

---

## Render & Deliver

Your input includes `chapter_blueprint_folder_id` — the exact Drive folder
to use. Do not resolve, create, or guess at a different location.

**1. Produce the complete blueprint**, meaning Block 0, the chosen/mixed
Block 1 alternative as decided in chat, the full Block 2 expansion, and the
Completeness Summary above.

**2. Render the blueprint as HTML per `references/output-formatting.md`.**
Apply its markup to every block — the document title, Block 0, Block 1's
tables, Block 2's sections and sub-sections, and the Completeness Summary —
without changing any wording, element name, conclusion, description,
pattern name, or modification note from Step 1. This is a markup pass only.

The output is **HTML, not Markdown**. Three rules decide whether it renders:

- **No CSS.** No `style` attributes, no `<style>` blocks, no `class`. They
  are stripped during conversion, and writing them creates a false
  impression that spacing, shading, or the WOW‑MOMENT color distinction is
  handled.
- **Every blank line is a `<p>&nbsp;</p>` spacer paragraph.** Whitespace and
  newlines in the source HTML are ignored by the converter. The spacer is
  the only spacing mechanism that survives — and it is what keeps every
  `N —` title from running into its conclusion, and every `N.X —` title
  from running into its description.
- **Escape `&` as `&amp;`** in all content, and write em dashes as
  `&mdash;`.

**3. Write the HTML to a file** in the sandbox, e.g.
`/home/user/blueprint.html`. Build it in parts if that is easier;
concatenate to one file before the next step.

**4. Create the Google Doc from code, reading that file into a variable.**

> **Never pass the HTML as a literal tool-call parameter.** A full Block 2
> expansion can run long once rendered as HTML with three skeleton tables
> from Block 1 included. Typing it into a tool call means re-emitting the
> whole document as tokens, which truncates, fails, and leads to
> placeholder text being sent instead. The document body must reach the
> tool as a **variable read from the file**, never as text you retype. Do
> not print the HTML to inspect it, and do not try to copy it out of a
> previous output — open the file and pass the handle's contents.

```python
with open('/home/user/blueprint.html') as f:
    content = f.read()

from gumloop import Gumloop
client = Gumloop()

result = client.mcp.execute("gdocs", "create_doc", {
    "title": "{Chapter Topic} — Chapter Blueprint",
    "content_format": "html",
    "content": content,
    "folder_id": "{chapter_blueprint_folder_id}"
}).results[0]

print("status:", result.status)
if result.status != "success":
    print("error:", result.error)
print(result.decoded_content)
```

Nothing is written anywhere outside that folder.

If the created document ever ends up holding placeholder text, do not
create another one. Fix the same document in place with `update_doc`,
passing `operation: "replace"` and the content read from the file exactly
as above.

**5. Return only the Doc link.** Not the content, not a summary — the Doc
link is your entire output. Nothing else gets returned, and nothing gets
saved or uploaded anywhere outside `chapter_blueprint_folder_id`.

---

## References

- `references/structural-patterns.md` — the named structural patterns each
  Block 1 option must be grounded in.
- `references/section-design-guide.md` — the full Technology Beneath
  specification referenced from Block 2's technology section requirement.
- `references/output-formatting.md` — defines the **HTML** markup for the
  generated blueprint: how the document title, Block 0's labeled fields,
  Block 1's option headings and skeleton tables, Block 2's sections and
  sub-sections (including the `[WOW MOMENT]` tag), and the Completeness
  Summary must be marked up (never how the content is worded). This
  blueprint is delivered as HTML, not Markdown, following the same
  procedure as the Broad Research and Research Analysis skills' own
  `output-formatting.md` files. CSS does not survive the Google Docs
  conversion, so all spacing comes from `<p>&nbsp;</p>` spacer paragraphs
  and never from `style` attributes. Apply this at the formatting step in
  **Render & Deliver** above, after Block 2 and the Completeness Summary
  are fully drafted.

---

## Output

| Field | Type | Description |
|---|---|---|
| `chapter_blueprint_doc_id` | Doc ID | The Google Doc ID of the Block 2 chapter blueprint, saved to `chapter_blueprint_folder_id`. This is the skill's entire return value — no content, summary, or completeness table is returned alongside it. |