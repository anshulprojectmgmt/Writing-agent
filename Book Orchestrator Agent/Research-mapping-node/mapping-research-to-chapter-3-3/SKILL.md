---
name: mapping-research-to-chapter-3-3
description: Maps research evidence to the approved chapter blueprint. Takes the ideas-only blueprint from chapter-blueprint and the broad-research output, scores every research item on quality and section purpose fit, and assigns the best-fit items to each sub-section. Produces the Final Chapter Blueprint with evidence woven into each sub-section. Subsumes review-score-refine — no separate scoring step needed before this. Use after chapter-blueprint Block 2 is approved.
icon: map
color: Teal
---

# Mapping Research to Chapter

The blueprint has committed to ideas. This skill wires the evidence.

Takes the approved ideas-only blueprint and the broad-research output.
For every sub-section, finds the research items that best serve that
sub-section's specific purpose — not the globally strongest items, but
the most purpose-fit items. Scores on quality AND section fit. Outputs
the Final Chapter Blueprint with evidence woven in.

This skill subsumes review-score-refine. No separate annotation step
is needed before this. All scoring happens here, in the context of
the chapter structure that already exists.

---

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `broad_research_doc_id` | Doc ID | Required | The Google Doc produced by the `broad-research` skill for this chapter topic. |
| `chapter_blueprint_doc_id` | Doc ID | Required | The approved Block 2 output from `chapter-blueprint` — use the most recently updated version, not necessarily `v1`. |
| `research_mapping_folder_id` | Folder ID | Required | The Drive subfolder under the main agent's workspace where this skill's output gets saved. |

---

## What you need

- Approved chapter blueprint (`chapter_blueprint_doc_id` above).
- Broad-research output (`broad_research_doc_id` above).
- Book profile (audience, purpose, tone) — provided by the caller or given directly by the user.

---

## The Core Principle

**Evidence is assigned by purpose fit, not by global quality rank.**

Read each sub-section's purpose first. Then ask of every
research item — does this item give this sub-section what it needs to do
its job for the reader? Purpose fit is the primary filter. Quality is the
tiebreaker between two similarly-fitting items.

---

## Process

Run all steps in order. Do not show the internal scoring working in chat —
only show the Final Blueprint and the coverage summary.

---

### Step 1 — Read the blueprint

Read every section and sub-section from the approved blueprint.
For each sub-section, extract and hold in memory:

- Its name
- Its one-clause purpose (what it does for the reader)
- Its emotional job (what the reader feels after it)
- The type of evidence it needs — classify as one of:
  - **Named example** — a specific company, product, or event that
    illustrates the idea
  - **Statistic or metric** — a number that makes the scale or impact
    concrete
  - **Case study** — a fuller story with a before/after or outcome
  - **Academic or research finding** — a sourced study or paper
  - **Expert or platform signal** — a CEO statement, analyst claim,
    or industry position
  - **Historical reference** — a past event that established a precedent
  - **Framework or concept** — a named model the reader can carry and use
  - **Creative beat** — analogy, humor, author's own reasoning (no
    external evidence needed — mark as EVIDENCE: none)

This evidence-type classification is the matching key. A sub-section
that needs a Named Example is not well served by a Statistic — even
if the statistic is high-quality.

---

### Step 2 — Read and catalogue the research

Read the broad-research output fully. For every named item — company example,
finding, concept, framework, platform statement, statistic, legal reference —
catalogue it with:

- Its name (what it is called)
- Its type (same taxonomy as above: Named Example, Statistic, etc.)
- Its source URL (as cited in broad-research)
- **Its full set of usable points** — fetch the cited source URL and read
  it. Broad-research's own write-up is a one-line compression; the final
  blueprint needs the actual content. Extract every distinct point in
  that source that could plausibly serve a sub-section — not just the
  single insight broad-research already surfaced. A source with real
  depth (a case study, a report) may yield 2-4 usable points; a thin
  source (a single stat) may only yield one. Do not invent points beyond
  what the source or broad-research's write-up actually says.
- Its quality across six dimensions (score each 0–2 internally):

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| **Credibility** — will it make the reader believe? | Unsourced or dubious | Plausible, named source | Verifiable, authoritative |
| **Conceptual value** — does it teach something new and make the reader pause? | Already known / Generic | Somewhat new / Mildly interesting | Genuinely new, counterintuitive, or memorable |
| **Recency** — is this current enough to trust and not date the book? | Outdated or superseded by newer developments | A few years old but still broadly accurate | Current, reflects the latest available data/events |
| **Specificity** — does it have concrete detail? | Vague | Some specifics | Named outcomes, numbers, mechanisms |
| **PM-actionability** — does it give a PM a decision or question? | None | Vague guidance | Clear, direct implication |
| **Narrative fit** — does it strengthen the chapter's arc? | Breaks flow | Neutral | Reinforces the argument |

Max quality score = 12. Do not show this table in chat.
Use quality scores only as tiebreakers between purpose-fit items.

If a source URL is unreachable (dead link, paywalled, login-gated),
fall back to broad-research's own write-up for that item and note
internally that points are limited to what broad-research captured.

---

### Step 3 — Match by purpose fit

Work through each sub-section in blueprint order.

For each sub-section:

1. State its evidence-type need (from Step 1).
2. Scan all research items of that type first.
3. Ask of each candidate: does this item directly serve what this
   sub-section is trying to do for the reader?

**Purpose fit is HIGH when:**
- The item's type matches what the sub-section needs
- Its core insight directly supports the sub-section's argument
- Placing it here would make the argument more credible, specific,
  or surprising — without changing the argument

**Purpose fit is MED when:**
- The item partially fits — it supports the idea but is not the
  strongest available match
- The item could serve this sub-section or another one
- It adds context but does not directly carry the argument

**Purpose fit is LOW when:**
- The item's insight belongs to a different section's argument
- It is high quality but wrong for this sub-section's job
- Placing it here would feel forced or require the argument to
  bend toward the evidence

Assignment rules:
- Assign 1–3 HIGH or MED items per sub-section
- Prefer HIGH fits. Only assign MED if no HIGH is available.
- Do not assign LOW items regardless of quality score
- When two items tie on purpose fit, use quality score to choose
- **Once an item is assigned, present its points, not just the item.**
  Go through the full set of points catalogued for that item in Step 2
  and pull forward only the points that actually serve this
  sub-section's job — not every point the source contains. Points are
  a presentational breakdown of what's inside an assigned item, so the
  user can send a specific point to deep-research later; fit and quality
  scoring stay at the item level.
- For each point pulled forward, write a **one-line "how it serves"**
  explanation specific to that point — not a single explanation for
  the item as a whole.
- A research item can be assigned to more than one sub-section if
  it genuinely serves both — but flag this and confirm it is not
  a redundancy problem
- **When the same source is used across multiple sub-sections, ensure
  each location uses a distinct point from it.** Do not repeat the same
  point or framing in two places. If a source is used in two places, the
  "how it serves" explanation and the specific point quoted must differ
  in each location. If the same point would need to be repeated, find a
  better alternative source for one of the locations instead.

---

### Step 4 — Flag GAPs

A GAP is a sub-section where the research cannot provide what the
argument needs.

A GAP must describe what is specifically missing — not just "no evidence."

**Bad GAP flag:** "no evidence for this sub-section"

**Good GAP flags:**
- "needs a named example of inner context handled with consent and
  user controls — current research has no clean case study for this"
- "needs a platform signal from a non-Western market to support the
  India-specific closing — not in research"
- "needs a specific metric or outcome for the streaming example in
  section 2 — currently unnamed and unquantified"

GAP flags become the direct input queue for deep-research.

---

### Step 5 — Build the Final Blueprint

Re-render the complete approved blueprint with evidence lines woven
into each sub-section, immediately after its content bullets.

Do not show Step 1–4 working. Only show the Final Blueprint and
the summary.

---

## Output format

Draft the Final Blueprint's content against the structure below — this is
the content spec, not the delivery format. The finished document is meant to
be worked from while writing the chapter and while queueing deep-research,
not read once, so when the content is complete it is rendered as HTML and
delivered as a Google Doc per **Render & Deliver** below, using
`references/output-formatting.md` for the markup. Nothing here is saved as a
standalone `.md` file.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL CHAPTER BLUEPRINT
Chapter: [Chapter title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### [N] — [SECTION NAME]
Purpose: [one clause from blueprint]

**N.1 — [SUB-SECTION NAME]**
*[what it does — from blueprint]*

• [content bullet — from blueprint, unchanged]
• [content bullet — from blueprint, unchanged]
• [content bullet — from blueprint, unchanged]

**Evidence — "[Item Name]"** *(Fit: HIGH)*
- [Point 1, written out in full — from broad-research or the source it
  cites] → *How it serves:* [one-line explanation specific to this point]
- [Point 2, if this item has more than one usable point for this
  sub-section] → *How it serves:* [explanation specific to this point]
🔗 Source: [URL, as cited in broad-research]

**Evidence — "[Item Name 2]"** *(Fit: MED)*
- [Point, written out in full] → *How it serves:* [explanation]
🔗 Source: [URL]

> ⚠️ **GAP:** [Specific description of what evidence type is missing] → *for deep-research*

---

**N.2 — [SUB-SECTION NAME]**
*[what it does]*

• [content bullet]
• [content bullet]

**Evidence — "[Item Name]"** *(Fit: HIGH)*
- [Point, written out in full] → *How it serves:* [explanation]
🔗 Source: [URL]

> ✅ **GAP: none**

---

**N.X — [SUB-SECTION NAME]** *(Creative beat — analogy / humor / author framework)*
*[what it does]*

• [content bullet]

> 🎨 **EVIDENCE: none** — creative beat, no source required

---

### PUNCH LINE
> "[from blueprint, unchanged]"

<!-- CHAPTER-LEVEL FEEDBACK -->
<!-- Single comment for the overall chapter: -->
> "[from blueprint, unchanged]"
```

**Rules for the output:**
- Copy content bullets from the blueprint exactly — do not rewrite them
- Every sub-section must have at least one evidence block, a GAP blockquote, or a creative-beat marker. Nothing left blank.
- Each evidence block covers one assigned item: its name, its fit (HIGH/MED), the full points pulled forward from it (each with its own "How it serves"), and its source URL
- A sub-section can have more than one evidence block if more than one item was assigned
- Points must be written out in full — not compressed into a single generic line — using the actual content from broad-research or the source URL it cites
- Every evidence block ends with a 🔗 Source line carrying the real URL
- GAPs are always in a blockquote prefixed with ⚠️ **GAP:**
- Creative beats use a blockquote with 🎨 **EVIDENCE: none**
- GAP descriptions must name the specific evidence type needed
- Do not invent evidence items or points. Only assign items and points that exist in the broad-research output or the source URL it cites.
- Do not assign an item to a sub-section where it does not fit because it has no better home. An unplaceable item stays unplaced.

---

## Coverage summary

After the Final Blueprint, append a structured coverage summary using formatted tables.
As above, this is the content spec — the three tables become real Doc tables
at the **Render & Deliver** step, per `references/output-formatting.md`:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COVERAGE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Metrics
| Category | Count |
|----------|-------|
| Total sub-sections | N |
| Fully evidenced (HIGH fit) | N |
| Partial (MED fit only) | N |
| Creative beats (no source) | N |
| GAPs for deep-research | N |

### GAPs
| Sub-section | What's Missing |
|-------------|---------------|
| N.X — [sub-section name] | [one-line description] |

### Unplaced Items
| Item | Reason Excluded |
|------|----------------|
| "[item name]" | [why it did not fit anywhere] |
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
The unplaced items list tells the user what the research covered that
did not make it into the chapter. They can decide whether to add a
sub-section, swap an existing item, or let it go.
---

## Render & Deliver

Your input includes `research_mapping_folder_id` — the exact Drive folder to
use. Do not resolve, create, or guess at a different location.

**1. Produce the complete Final Blueprint**, including the Coverage Summary
above.

**2. Render the Final Blueprint as HTML per `references/output-formatting.md`.**
Apply its markup to every block — the document title, every section and
sub-section, every evidence block and its points, every GAP flag and
creative-beat marker, the punch line, the chapter-level feedback, and the
Coverage Summary's three tables — without changing any content bullet,
evidence point, "how it serves" explanation, fit label, GAP description, or
source URL from Step 1. This is a markup pass only.

The output is **HTML, not Markdown**. Three rules decide whether it renders:

- **No CSS.** No `style` attributes, no `<style>` blocks, no `class`. They
  are stripped during conversion, and writing them creates a false
  impression that spacing, shading, or the HIGH/MED and GAP distinctions are
  handled.
- **Every blank line is a `<p>&nbsp;</p>` spacer paragraph.** Whitespace and
  newlines in the source HTML are ignored by the converter. The spacer is
  the only spacing mechanism that survives — and it is what keeps every
  sub-section title from running into its purpose line, and every evidence
  block from running into the GAP flag beneath it.
- **Escape `&` as `&amp;`** in all content, and write em dashes as
  `&mdash;`.

The Markdown blockquotes (`>`), typed `━━━` rules, and `•` bullets in the
Output Format above are chat-draft conventions. They do not survive: GAP,
no-GAP, and creative-beat lines become bold-labeled paragraphs, rules become
`<hr>`, and bullets become real `<ul>`/`<li>` lists — see the reference file
for each template.

**3. Write the HTML to a file** in the sandbox, e.g.
`/home/user/final-blueprint.html`. Build it in parts if that is easier;
concatenate to one file before the next step.

**4. Create the Google Doc from code, reading that file into a variable.**

> **Never pass the HTML as a literal tool-call parameter.** A final
> blueprint runs long once every evidence point is written out in full
> across 10–20+ sub-sections. Typing it into a tool call means re-emitting
> the whole document as tokens, which truncates, fails, and leads to
> placeholder text being sent instead. The document body must reach the tool
> as a **variable read from the file**, never as text you retype. Do not
> print the HTML to inspect it, and do not try to copy it out of a previous
> output — open the file and pass the handle's contents.

```python
with open('/home/user/final-blueprint.html') as f:
    content = f.read()

from gumloop import Gumloop
client = Gumloop()

result = client.mcp.execute("gdocs", "create_doc", {
    "title": "{Chapter Title} — Final Chapter Blueprint",
    "content_format": "html",
    "content": content,
    "folder_id": "{research_mapping_folder_id}"
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
saved or uploaded anywhere outside `research_mapping_folder_id`.

---

## References

- `references/output-formatting.md` — defines the **HTML** markup for the
  generated Final Chapter Blueprint: how the document title, each `N —`
  section and its purpose line, each `N.X —` sub-section with its content
  bullets, each `Evidence — "…"` block with its fit label, points, "how it
  serves" clauses and source link, the ⚠️ GAP / ✅ GAP: none / 🎨 EVIDENCE:
  none lines, the punch line, the chapter-level feedback, and the Coverage
  Summary's three tables must be marked up (never how the content is
  worded). This blueprint is delivered as HTML, not Markdown, following the
  same procedure as the Broad Research, Research Analysis, and Chapter
  Blueprint skills' own `output-formatting.md` files. CSS does not survive
  the Google Docs conversion, so all spacing comes from `<p>&nbsp;</p>`
  spacer paragraphs and never from `style` attributes, and `<blockquote>`
  does not survive either, so the skill's blockquote markers become
  bold-labeled paragraphs. Apply this at the formatting step in **Render &
  Deliver** above, after the Final Blueprint and the Coverage Summary are
  fully drafted.

---

## Output

| Field | Type | Description |
|---|---|---|
| `chapter_blueprint_doc_id` | Doc ID | The Google Doc ID of the Final Chapter Blueprint (evidence-mapped), saved to `research_mapping_folder_id`. This is the skill's entire return value — no content, summary, or coverage table is returned alongside it. |
