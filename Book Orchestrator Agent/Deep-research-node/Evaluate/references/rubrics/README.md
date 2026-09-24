# Rubric references

One rubric file per node, named to match `node_name` exactly (plus
`.yaml`):

| `node_name` | file |
|---|---|
| `broad_research` | `broad_research.yaml` |
| `chapter_blueprint` | `chapter_blueprint.yaml` |
| `chapter_writing` | `chapter_writing.yaml` |
| `deep_research` | `deep_research.yaml` |
| `research_analysis` | `research_analysis.yaml` |
| `research_mapping` | `research_mapping.yaml` |

## Model: five dimensions, extracted from the skill itself

Anchored 0/0.5/1.0 judgment calls produced vague comments — "coverage
is a bit narrow" is technically an anchor-grounded score, but it isn't
a comment anyone can act on. The fix: every section is checked against
five **named, checkable dimensions**, and the checklist inside each
dimension is pulled from what the *originating skill's own text* says
that section must do — not invented independently by whoever wrote the
rubric.

## The five dimensions

Applied consistently to every section, so scores stay comparable
across sections and across nodes. Not every section needs every
dimension populated — a dimension with no checks for a given section is
simply skipped for that section (its weight is dropped, the rest
renormalize) rather than scored on nothing.

**Two dimensions are objective — a gate, not a scored dimension:**

1. **Structural** — mechanically checkable, no judgment. Present,
   correctly labeled, has the required sub-fields, counts, or format.
2. **Content Completeness** — not formatting, but substance: does the
   section contain everything the skill's own process says it must
   produce for *this specific* input (not a generic minimum).

These two never contribute a fraction to the section's score — they
gate it. Every check either holds or it doesn't, including any
exception the check's own wording already allows (e.g. "any skipped
rung has a specific stated reason" — a justified skip is not a
failure). Where a check has no such built-in exception, any unmet
check is an unqualified failure. **If every objective check passes, the
gate opens and the section is scored from its subjective dimensions
alone. If even one genuinely fails, the section's score is 0** — not a
cap, not a deduction, zero — regardless of how well the subjective
dimensions would otherwise have scored. A matched `red_flag` carries
this same severity, for the same reason: a real, checkable requirement
wasn't met, and no amount of good judgment elsewhere changes that.

**Three dimensions are subjective — genuine judgment, not a checklist:**

3. **Quality / Specificity** — of what's present, is it specific and
   doing real work, or generic and swappable with any other chapter's
   version of the same section?
4. **Purpose Alignment** — every section exists to do a specific job
   for whoever reads it next in the pipeline. This dimension checks
   whether the section actually *does* that job — a testable claim,
   not a vibe.
5. **Consistency / Traceability** *(only where relevant — mainly
   summary/rollup sections)* — does this section's claims about other
   parts of the doc actually match those other parts?

## Schema

```yaml
pass_threshold: 0.85

sections:
  - id: section_id
    name: "1. Exact Heading Text"       # fixed: literal heading text.
                                          # dynamic: a label describing
                                          # the pattern being matched.
    match: fixed | dynamic
    weight: 0.08                         # this section's share of
                                          # final_score — the only way
                                          # importance is expressed;
                                          # no section can override
                                          # the whole document's score.
    purpose: "A sentence, extracted from the skill's own text (quoted
              or closely paraphrased), stating why this section exists
              and what job it's supposed to do for the next reader.
              Every comment on this section must be traceable back to
              this line."
    dimensions:
      structural:
        weight: 0.25                     # dimension weights within a
        checks:                          # section should sum to ~1.0;
          - "..."                        # evaluate normalizes if not
      content_completeness:
        weight: 0.30
        checks:
          - "..."
      quality:
        weight: 0.25
        checks:
          - "..."
      purpose_alignment:
        weight: 0.20
        checks:
          - "..."
      # consistency: only present on sections where it applies
    red_flags:                           # optional, section-scoped
      - "a specific tell that sends this section's score to 0"
```

- A section's score is the weighted average of its populated
  dimensions; a document's `final_score` is the weighted average of
  its sections — same two-level roll-up as before, just with real
  structure inside the section level now instead of a single holistic
  anchor judgment.
- `purpose` is not decorative — see `references/rubrics/README.md`'s
  companion instruction in the main `SKILL.md` ("Comment Rules"):
  every comment placed on a section must reference what that section's
  `purpose` line says it's for, so a comment is always answering "does
  this section do its actual job," not "is this section nice."
- `checks` inside each dimension should be specific enough that two
  different evaluation runs would check the same thing the same way —
  if a check requires independent interpretation to even know what
  it's asking, it's too vague to be a check; rewrite it as something
  concrete (a count, a named requirement, a yes/no fact).

If `evaluate` is called with a `node_name` that has no matching file
here, it returns `status: no_rubric` rather than guessing at criteria.
