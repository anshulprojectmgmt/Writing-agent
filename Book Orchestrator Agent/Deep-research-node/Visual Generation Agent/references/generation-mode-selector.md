# Visual Generation Mode Selector

Run only for subsections with no usable EXTRACTED primary-source visual.

## Modes

### DATA_EXPLAINER
Pick when the subsection's main value comes from verified numbers, comparison, trend, scale, or measurable change.
- +1 important verified numbers/data exist.
- +1 a chart/comparison would make the insight clearer than prose.

### TOPIC_EXPLAINER
Pick when the reader needs to understand how something works, changes, connects, or flows.
- +1 there is a mechanism/process/relationship to explain.
- +1 a diagram can show the idea in under 10 seconds.

### HUMOUR_METAPHOR
Pick when an abstract or counter-intuitive idea becomes easier through a familiar analogy.
- +1 a familiar analogy makes the concept easier to grasp.
- +1 the analogy can stay factually faithful without exaggeration.

## Selection

Score each mode 0–2. Highest score wins.

Tie-break order:
`DATA_EXPLAINER -> TOPIC_EXPLAINER -> HUMOUR_METAPHOR`

Hard overrides:
- central verified statistic/comparison -> DATA_EXPLAINER;
- primarily explains how something works -> TOPIC_EXPLAINER unless data clearly dominates;
- HUMOUR_METAPHOR only when the metaphor explains the idea, not merely entertains;
- do not force humour into serious safety/legal/security/trust material when it would trivialize the claim.

## Output

For every approved subsection record:

`GENERATION_REQUIRED: YES | NO`
`DATA_SCORE: 0-2`
`TOPIC_SCORE: 0-2`
`HUMOUR_SCORE: 0-2`
`SELECTED_MODE: DATA_EXPLAINER | TOPIC_EXPLAINER | HUMOUR_METAPHOR | NONE`
`REASON: <one sentence>`

Generation requirement is decided before mode scoring:
- any usable EXTRACTED source candidate -> NO by default;
- SOURCE-LINKED only -> YES;
- NOT FOUND -> YES.
