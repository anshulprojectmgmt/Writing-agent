---
name: evaluate-skill-v2
description: Evaluates a pipeline node's Google Doc section by section — scores it, inserts findings, then attaches native comments last. Use after any pipeline node completes.
---

# Evaluate

A bounded subagent — runs once and returns. Never pauses for a human,
posts to Slack, touches a tracking sheet, or revises content. Your only
job: **is this content good enough, section by section, and by how
much?** Not *how* to fix it — a failing score with a locatable,
factual account of what failed is your entire deliverable; `diagnose`
takes it from there.

Score and comment are both keyed to the **section**, never the whole
document. Don't form a "the doc overall" impression at any point —
score section by section and let Step 5's roll-up produce the total.

**Critical ordering rule:** all content insertion (Step 3) happens
first, in full, before any commenting (Step 4) begins — and nothing
ever writes to the doc again once Step 4 starts. Comments anchor only
to a finding's own bullet text, inserted fresh in Step 3 for exactly
this purpose — never to a span inside the original section content.
Breaking either half of this — writing to the doc after a comment
exists, or anchoring a comment to pre-existing text — is what Google
Docs shows as "Original content deleted": the comment becomes
unclickable and untraceable, even when the rewritten text is
identical, because the underlying text run gets deleted and recreated.
This ordering and this anchor rule are not style preferences.

**Direction rule:** read, evaluate, and find every insertion index
**top to bottom** (Steps 1–2). Write to the doc **bottom to top** —
both inserting findings blocks (Step 3) and attaching comments
(Step 4) start at the last section in the doc and end at the first.
Inserting from the bottom means each write only shifts text *below*
it, so every index found above it in the top-down pass stays valid.

## Input
- `main_doc_link` (or `main_doc_id`) — the doc to evaluate. Always
  live and commentable.
- `node_name` — required; selects the rubric and expected sections.
- `drive_folder_link` — where to save the report. Optional: if
  omitted, return the report inline instead (see Final Output).

Rubrics are never passed in — see Step 0.

---

## Step 0 — Load the rubric

Load `references/rubrics/{node_name}.yaml` (schema in
`references/rubrics/README.md`). If no file matches, or `node_name` is
empty/malformed, stop and return `status: no_rubric` with a reasoning
line naming the problem — do not guess at criteria.

Each rubric section has: `match` (`fixed` — literal heading to locate;
`dynamic` — a check template applied once per matching sub-section
found), `weight` (the only way importance is expressed), `purpose` (why
this section exists, per the originating skill's own text), a
`dimensions` block (up to five: `structural`, `content_completeness`,
`quality`, `purpose_alignment`, `consistency` — each with its own
weight and `checks`), and optional `red_flags`.

**Two different kinds of dimension, treated two different ways:**

- **Objective — `structural`, `content_completeness`.** These are not
  scored as a fraction and do not contribute to the weighted average
  at all. They function as a **gate**: every check either holds or it
  doesn't, exactly as the rubric states it (including any exception
  the check's own wording already allows — see Step 2b). Any
  unjustified failure sends the section's score straight to 0 —
  nothing else about the section matters once this happens.
- **Subjective — `quality`, `purpose_alignment`, `consistency`.** These
  are graded, not gated — scored as the fraction of `checks` that hold,
  using real judgment, and combined by weight into the section's score
  *only if the objective gate passed*.

This split governs how Step 2 scores each dimension — see below.

---

## Step 1 — Locate every expected section

Read the doc once to map it against the rubric: find each `fixed`
section's heading; find every actual instance of each `dynamic`
pattern. A `fixed` section that's entirely absent scores 0 — it still
feeds the Step 5 roll-up at its own weight, nothing more.

In this same top-to-bottom read, record each section's **insertion
index** — the start index of the line where its findings block will
go, per Step 3's insertion-point rule. These indexes are found once,
here, top to bottom; Step 3 uses them bottom to top. Each one becomes
that section's `index` in Step 3's `insertions` list.

---

## Step 2 — Score every section, dimension by dimension

For each section, in doc order — **this step only scores and drafts
findings text; it does not write anything to the doc yet.**

**2a. Read only that section.** Don't let other parts of the doc bleed
into its score.

**2b. Run the objective gate first — before any scoring happens.**

For every check inside `structural` and `content_completeness`:

- **A check only counts as failed if there's no valid justification for
  it.** "Valid" means exactly what that specific check's own wording
  already allows — many checks have this built in (e.g. "any skipped
  rung has a specific stated reason, not left blank" — a skip *with* a
  stated reason is not a failure). Where a check has no such built-in
  exception, treat any unmet check as an unqualified failure. Never
  invent a leniency the check's own wording doesn't state.
- **If every objective check across both dimensions holds (or is
  validly justified): the gate passes.** Move to subjective scoring
  below — the section's score will come entirely from there.
- **If even one objective check genuinely fails: the section's score
  is 0.** Not a cap, not a fraction — zero, full stop. Skip the
  weighted-average computation entirely; nothing about the subjective
  dimensions changes this. Still draft a finding explaining exactly
  which check failed and why (2c) — the score is fixed, but the reason
  still needs to be locatable.

A matched `red_flag` (where the rubric defines one) is treated with
this same severity — score 0, for the same reason: it means the
section's real requirement wasn't met, only its surface appearance
was, and no amount of strength elsewhere changes that.

**If the gate passed, score the subjective dimensions** (`quality`,
`purpose_alignment`, `consistency`) as the fraction of each dimension's
`checks` that hold, using real judgment (3 of 4 met = 0.75). A
dimension with no `checks` for this section is skipped, not scored
blind. The section's score is the weighted average of whichever
subjective dimensions are populated — objective dimensions contribute
nothing to this average; they've already done their job as a gate.

`dynamic` sections: run this full process (gate, then scoring) on each
matching instance separately, then average the instance scores for the
section template's overall score.

**2c. Draft the findings for this section as text** — do not write to
the doc yet, just prepare what Step 3 will insert. One finding per
dimension that failed or partially passed, plus a general one always
(a clean section still gets one, naming what worked). Follow
**Finding Rules** below for every one.

---

## Finding Rules

Every finding, in the exact template Step 3 inserts — **three bullets,
nothing else. No header line, no score, no divider, no version label
wrapping it:**

```
• Topic: [exact section name]
• Comment: [one short, plain-language sentence stating the issue]
• Dimension: [Structural | Content Completeness | Quality | Purpose Alignment | Consistency]
```

1. **Exactly these three bullets, in this order, every time** — nothing
   added above or below them (no "EVALUATOR FINDINGS" title, no score
   line, no version label). The Topic is the exact section name and
   nothing else — no `(v1)` or any other version tag.
2. **The Comment is one sentence. Short, concrete, to the point** — not
   a paragraph, not a list of sub-issues. If a section has three
   distinct problems, that's three separate three-bullet findings, one
   after another, each with its own one-sentence Comment — never one
   long Comment covering all of them.
3. **Name the specific thing, and where it is.** Both parts are
   required: an exact fact (a number, a named item, a term, a count —
   something that could be wrong or right, not just felt) *and* its
   exact location (which paragraph, which bullet, which claim — not
   just the section, which the Topic bullet already gives you).
   "The introduction is unclear" fails this twice: no fact, no location
   more precise than the section itself. "Paragraph 2 claims 40% market
   share but cites no source" passes: a specific number, a specific
   claim, a findable spot.
4. **Never use unqualified**: "could be stronger," "lacks depth,"
   "somewhat generic," "needs more detail," "could be improved" — only
   acceptable immediately followed by the specific referent that earns
   the phrase, and even then, keep it to the one sentence.
5. **The copy-paste test — run it on every Comment before moving on,
   not just as a mental guideline.** Could this exact sentence be
   pasted onto a different chapter's version of the same section and
   still make sense unchanged? If yes, it's too generic — stop, find
   the one fact and location from rule 3 you skipped, and rewrite
   around that before writing the next finding.
6. **Factual and observational, never prescriptive** — "this stat has
   no source" is in scope; "add a peer-reviewed source" is
   `diagnose`'s job, not yours.

**Weak (fails rules 3 and 5 — no fact, no location, would paste onto
any chapter's version of this section unchanged):**
```
• Topic: 2. Query Map
• Comment: The Query Map section could be more thorough.
• Dimension: Content Completeness
```

**Strong (names the exact fact and its location, tied to this doc
alone):**
```
• Topic: 2. Query Map
• Comment: Query Map lists 6 term categories but has no CONTRARIAN TERMS category, which the rubric requires.
• Dimension: Content Completeness
```

This exact three-bullet template is used **everywhere a finding
appears** — the doc's inserted findings block (Step 3), the native
comment text (Step 4), and the report (Saving). Never a longer or
differently-labeled version in any of the three places.

A finding breaking any rule isn't lower quality — it's incomplete.
Rewrite it before moving on.

---

## Step 3 — Insert every appended findings block (one content pass, before any comments)

Now that every section is scored and every finding is drafted, insert
all of them into the doc **in a single pass, section by section, but
as one continuous operation with no commenting mixed in.**

**Insert bottom to top.** Start with the last section in the doc and
work upward, ending with the first section. Use the insertion indexes
recorded top to bottom in Step 1 — because each insertion only shifts
text below it, the indexes of every section still above it remain
correct. Never insert top to bottom.

For each section, insert every finding for that section at the
section's **insertion point** (defined below) as **one clearly bounded
group — a divider line immediately above the first finding and another
immediately below the last, with nothing from the section's normal
content inside those two lines**.

**Insertion point — strict rule.** A "line" here means one paragraph
in the Google Doc.

1. Find the section's **last line of content** — the last non-blank
   line before the next section's heading (or before the end of the
   doc, for the last section).
2. Leave exactly **one** blank line after it untouched.
3. Insert the findings block at the **second line after the last
   content line** — i.e. at the start index of that line.

Example: the section's content ends at line 23 → line 24 is the one
blank line left in place → the findings block starts at line 25.

- If there is only one blank line before the next heading, line 25 is
  where that heading starts — insert there, and end that block's
  content with `\n` so the heading is pushed below the block instead
  of joining the last divider line.
- If there is no blank line at all after the content, use the start
  index of the line right after the content, and start that block's
  content with `\n` (creating the one blank line) and end it with `\n`.
  The findings block never touches the section's content directly.

**Last insertion — special case.** Google Docs rejects `insert_at` at
the document's end index (`endIndex`) — valid indexes are 1 to
`endIndex - 1`. For the last section in the doc, "line 25" usually
doesn't exist (the doc ends on the one blank line after the content),
so its computed index equals `endIndex` and the insert fails. So when
an insertion index is the last one in the doc (≥ `endIndex`):

- **Index:** the end index of the section's last content paragraph
  (its last non-blank paragraph) — this is where the blank line after
  it starts, and it is always below `endIndex`.
- **Content:** `"\n"` + the block. The leading `\n` keeps the one blank
  line, so the divider still lands on the second line after the
  content, like every other section.
- If there is no blank line at all after the content (the last content
  paragraph is the doc's final paragraph), use `endIndex - 1` and start
  the content with `"\n\n"` instead.

`endIndex` comes from `read_doc`: it is the `endIndex` of the last
element in `body.content`. `decoded_content` is a list — read it as
`decoded_content[0]['body']['content']`.

Findings — and therefore the comments anchored to them — go **only at
the section's end**. Never at the beginning of a section, never between
its heading and its content, never in the middle of its content. No
exceptions.

**Fixed block structure — exactly this, every time:**

```
──────────────────────────
• Topic: 3. Source Ladder Findings (Rungs 1-10)
• Comment: Rungs 2, 7, 8, 9, and 10 fall below the skill's ≥5 findings-per-rung minimum (4, 4, 4, 2, and 3 respectively) with no stated reason for the shortfall, so the content-completeness gate fails.
• Dimension: Content Completeness
──────────────────────────
```

- **Divider:** exactly 26 `─` characters (U+2500) on a line of their
  own — one above the first finding, one below the last.
- **Bullets:** the `•` character typed as plain text plus one space —
  not a Google Docs list.
- **Labels:** exactly `Topic:`, `Comment:`, `Dimension:`, in that
  order, one per line.
- **Several findings in one section:** one blank line between them,
  all inside the same single pair of dividers.
- **Plain text only** — no bold, italics, headings, or links.
- **Font color `#C00000`** on the whole block, dividers included.

The two divider lines mark the exact start and end of the group — this
is what actually stops it from reading as if it flows into the
surrounding content, since color by itself isn't a reliable enough
signal on its own (it can still blend in depending on the doc's
existing colors or how a given renderer displays it). The `#C00000`
color and the dividers reinforce each other, neither replaces the
other.

The three-bullet groups inside the boundary still follow Finding Rules
exactly — no title line, no score line, no divider *between*
individual findings within the same group. The two divider lines are
the outer boundary of the whole section's group, not a wrapper around
each finding separately.

Never let two different sections' findings share one pair of dividers
— one section, one bounded group, every time.

**How to insert — decide everything first, then run one loop.**

1. **Decide every exact index.** From Step 1's top-to-bottom read,
   take each section's insertion index — the start index of the
   insertion line (line 25 in the example above). For the last
   section, check its index against the doc's `endIndex` and apply the
   last-insertion special case above.
2. **Write every block's exact text.** One block per section, in the
   fixed block structure above, character for character. No leading
   newline — the divider lands exactly on the insertion line. Several
   findings in one section are separated by one blank line (`\n\n`)
   inside the same pair of dividers.
3. **Insert all blocks bottom to top** with this code — fill
   `insertions` with one `(index, content)` pair per section:

```python
from gumloop import Gumloop
client = Gumloop()

doc_id = "<main_doc_id>"

# One (index, content) pair per section, decided in steps 1-2 above.
insertions = [
    (865, (
        "──────────────────────────\n"
        "• Topic: 3. Source Ladder Findings (Rungs 1-10)\n"
        "• Comment: Rungs 2, 7, 8, 9, and 10 fall below the skill's ≥5 findings-per-rung minimum (4, 4, 4, 2, and 3 respectively) with no stated reason for the shortfall, so the content-completeness gate fails.\n"
        "• Dimension: Content Completeness\n"
        "──────────────────────────"
    )),
    # (index, content) for every other section ...
]

# Bottom to top: highest index first.
for index, content in sorted(insertions, key=lambda x: x[0], reverse=True):
    result = client.mcp.execute("gdocs", "update_doc", {
        "doc_id": doc_id,
        "operation": "insert_at",
        "index": index,
        "content": content,
        "content_format": "plain",
        "fontColor": "#C00000",
    }).results[0]

    print("Index:", index, "Status:", result.status)
    print(result.decoded_content if hasattr(result, 'decoded_content') else result)
    if result.status != "success":
        break  # stop at the first failure — see below
```

Sorting by index, highest first, is what makes this bottom to top:
each insertion only shifts text below it, so every index still waiting
in the list stays correct.

**If an insert fails, stop — never retry it later with the same
index.** The loop breaks at the first failure. Every block not yet
inserted sits above the ones already in, so their indexes are still
correct: fix the failed entry and rerun the loop with only the
remaining entries. Retrying a failed index *after* other blocks have
gone in above it lands the block in the middle of a paragraph.

**Do not place any comments during this step.** This is purely a
content-insertion pass. Once every section's block is inserted and the
doc is saved in this state, move to Step 4 — and nothing after this
point writes new text into the doc.

---

## Step 4 — Attach comments (the final pass — no writes after this)

For each finding block inserted in Step 3, **bottom to top** — start
with the last section's block and work upward to the first section's;
within a block holding several findings, start with the last finding
and work upward to the first:

1. **Select the finding's own three bullets** — the text just inserted
   in Step 3 at the section's end (its insertion point), not any span
   inside the original section content and not the section's divider
   lines. This is the only thing a comment ever anchors to.
2. **Attach a native Google Doc comment to that selection**, using the
   exact same finding text already visible in the bullets — the
   comment is a mirror of what's already on the page, not new content.

That's the entire step. There is no highlighting, no separate pass over
the original content, and no second anchor point to manage — one
finding, one inserted block, one comment on that block. The distinct
text color from Step 3 is what makes a finding visually stand out on
the page; the comment's only job is to make that same finding open-able
and trackable from the Comments panel.

**Leave every comment open — never mark one resolved.** Never remove,
resolve, or edit an existing comment or findings block from a prior
evaluation — add fresh ones alongside.

**This is the last operation of the entire skill.** Once Step 4 begins,
nothing else writes to the doc — that's what keeps every comment's
anchor valid and clickable instead of becoming "Original content
deleted."

---

## Step 5 — Roll up the score

No section can fail the whole document alone through its `weight`
value — but a section that failed its objective gate contributes 0 to
the roll-up regardless of weight, since its score is 0, not a fraction.
A single such section pulls the weighted average down by exactly its
own weight's worth — same mechanics as any other score, just a score
that happens to be 0. Compute every time:
```
final_score = Σ (section_score × section_weight) / Σ (section_weight)
```
`dynamic` sections contribute their averaged score once, at their full
weight — not once per instance.

Example: Block 0 (0.20, scored 0.9), Block 1 (0.20, 0.8), Block 2 subs
(0.50, averaged 0.75), WOW MOMENT (0.06, 1.0), [TECH] (0.04, 0.9):
```
final_score = (0.9×0.20 + 0.8×0.20 + 0.75×0.50 + 1.0×0.06 + 0.9×0.04) / 1.0 = 0.811
```

Record any section scoring below 0.5 as `low_scoring_sections` —
informational only, not a second gate.

`final_score ≥ pass_threshold` → `status: passed`; otherwise `failed`.
Equal counts as passing. Go to Saving either way — no diagnosis, no
retry.

---

## Saving the evaluation report

**This is a strict, ordered procedure — four separate steps, each one
verified before the next begins. Do not skip a step, merge two steps
into one action, substitute a different method for any step, or
produce the final Doc by any other path.** If `drive_folder_link` is
given, this exact sequence is mandatory:

**Step A — Author the file.**
1. Write the complete report content — status + final score at top, any
   section below 0.5 called out next, then per section (doc order):
   name, score, and every finding on it, in the exact three-bullet
   template from Finding Rules. Should mirror the doc's findings blocks
   exactly — a compilation, not a fresh summary.
2. Save this as an actual `.md` file named `evaluation_report.md`.
3. **Verify the file was actually created** before moving to Step B —
   do not proceed on the assumption that authoring succeeded.

**Step B — Upload it.**
1. Upload the `evaluation_report.md` file from Step A into
   `drive_folder_link`, as a file upload — not retyped, not
   summarized, the same file.
2. **Verify the upload produced a real file in that folder** before
   moving to Step C. If the folder can't be resolved by URL, fall back
   to its `folder_id` — this substitution is allowed; skipping the
   upload step itself is not.

**Step C — Convert it.**
1. Convert the uploaded `.md` file into a Google Doc, in the same
   folder as the upload.
2. **Verify the conversion produced an actual Google Doc with a real
   doc ID** before moving to Step D. A conversion that silently fails
   or times out is not something to paper over — treat it as a failed
   run for this report (see below), not as license to skip ahead.

**Step D — Use the result.**
1. Use the converted Doc's link as `evaluation_report_link` in Final
   Output. Never a link to the `.md` file from Step A, never a link
   constructed or guessed, never a placeholder — only the real link the
   conversion in Step C actually returned.

**What "following the procedure" explicitly rules out:**
- Writing the report content directly into a new Google Doc, skipping
  the `.md` file entirely — even though the end state might look
  similar, this isn't the same path and isn't acceptable.
- Returning `evaluation_report_inline` when `drive_folder_link` was
  actually given — inline is only for when no folder was provided at
  all, never a fallback for convenience.
- Treating any of Steps A–C as optional because the next step "would
  probably work anyway."

**If any step's verification fails**, stop and report which step
failed and why — do not continue to the next step on an unverified
assumption, and do not fabricate a link. Never overwrite or delete a
prior report; don't version-number it.

If `drive_folder_link` was not given at all, skip this entire
procedure and return the report inline as `evaluation_report_inline`
instead.

---

## Final Output

```
RESULT
status: passed | failed | no_rubric
node_name: [node evaluated]
final_score: [omitted if no_rubric]
threshold: [omitted if no_rubric]
low_scoring_sections: [{section_name, score} for scores < 0.5 — informational]
section_scores: [{section_name, score} for every section — names and numbers, not comment text]
comments_placed: [count placed in Step 4]
evaluation_report_link: [Doc link, if drive_folder_link given]
evaluation_report_inline: [report content, if not given]
reasoning: [only if no_rubric — which node_name had no rubric, or what was wrong with it]
```

Handed directly to `diagnose` on `failed` — `section_scores` says
where to look; the doc's findings blocks and comments already say why.

---

## Boundaries
- Never writes to the doc after Step 4 begins, for any reason — this is what keeps comments navigable instead of orphaned.
- Never inserts findings or attaches comments top to bottom — evaluation and index-finding run top to bottom; every write to the doc (Step 3 insertions, Step 4 comments) runs bottom to top.
- Never highlights or applies background color to a span in the original content, and never anchors a comment there — comments anchor only to a finding's own bullets, freshly inserted in Step 3 (see the ordering rule above).
- Never inserts a findings block — and so never places a comment — anywhere except the section's end, at the Step 3 insertion point (one blank line after the section's last content line; e.g. content ends at line 23 → block starts at line 25). Never at the beginning or in the middle of a section.
- Never loops, retries, or re-evaluates internally — a revision check is a fresh call.
- Never decides patch vs. escalate or handles `human_feedback` — not this skill's job.
- Never treats an objective-dimension check as a matter of judgment, a fraction, or something a strong subjective score can offset — it's a gate exactly as Step 2b describes: any unjustified failure sets the section to 0, and no invented leniency beyond what the check's own wording allows.
- Never writes a Comment longer than one sentence — split into multiple findings instead.
- Never relies on color alone for visual distinction — every section's findings group is also bounded by a divider line above and below it.
- Never inserts findings blocks one by one as they're drafted — every index and every block's text is decided first, then all blocks go in through the Step 3 Python loop, highest index first.
- Never wraps an individual finding in its own title, score line, or divider — three bullets only, everywhere a finding appears. The one pair of divider lines per section (Step 3) bounds the whole group, not each finding within it.
- Never puts full finding text in `RESULT` — that stays compact metadata.
