# Memory selection evaluation

This page explains the selected memory evaluation results shown in the portfolio. The evaluation was run offline against controlled cases for the Sport Facility project's memory subsystem.

## Scope and results

- The full held-out dataset contained 61 cases covering multiple aspects of memory and context behaviour.
- Across 25 memory-selection queries, the effective results contained 17 relevant selected items, four selected items outside the expected set and no missed expected items. This gives a micro-precision of 17 / 21, or 80.95%, and a micro-recall of 17 / 17, or 100%.
- Micro-F1 was calculated from those counts: 2 × 17 / (2 × 17 + 4 + 0), or 89.47%.
- In all 16 queries with at least one expected memory, the ranking output included an expected memory in its top three positions. The benchmark's function labels this Recall@3; the test is more precisely a query-level hit@3 because it checks whether any expected item appears.
- All 14 controlled memory-write authorisation cases passed. A case was counted as correct only if both the decision and the corresponding recorded backend write behaviour matched the expected result.

## Interpretation

The ranking hit rate, item-level micro metrics and authorisation checks answer different questions. The micro counts above are based on effective memories after the memory gate; the query-level hit@3 is based on the ranker's output before the gate.

The sample is small and the data is controlled. These results do not establish performance on unseen production traffic, overall assistant accuracy, real-world security or user satisfaction. The original source code and raw cases are not published as part of this showcase.
