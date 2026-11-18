"""Recalculate published aggregate metrics, not rerun the private benchmark."""

import json
from pathlib import Path

data = json.loads(
    (Path(__file__).resolve().parents[1] / "evaluation" / "memory-selection-summary.json")
    .read_text(encoding="utf-8")
)
tp, fp, fn = (data[key] for key in ("true_positive", "false_positive", "false_negative"))
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * tp / (2 * tp + fp + fn)
print(f"Selection precision: {precision:.2%} ({tp}/{tp + fp})")
print(f"Micro recall: {recall:.2%} ({tp}/{tp + fn})")
print(f"Micro-F1: {f1:.2%}")
print(f"Target-memory hit@3: {data['positive_queries_with_top_3_hit']}/{data['positive_queries']}")
print(f"Memory-write authorisation: {data['memory_write_authorisation_passed']}/{data['memory_write_authorisation_cases']}")
