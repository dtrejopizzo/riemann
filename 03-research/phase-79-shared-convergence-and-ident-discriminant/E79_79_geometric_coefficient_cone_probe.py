#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "E79_76_frontier_ratio_rule_results.json"
OUT = ROOT / "E79_79_geometric_coefficient_cone_results.json"


def support_stats(support):
    start = support[0]
    card = len(support)
    span = support[-1] - support[0] + 1
    return start - card, span


def main():
    data = json.loads(SRC.read_text())
    rows = [row for row in data["rows"] if row["N"] in [10, 12, 16]]

    admissible = []
    for ai in range(81):
        a = ai / 100.0
        for bi in range(81):
            b = bi / 100.0
            ok = True
            for row in rows:
                low = row["low"]
                high = row["high"]
                low_u, low_v = support_stats(low["support"])
                high_u, high_v = support_stats(high["support"])
                delta_cost = a * (high_u - low_u) + b * (high_v - low_v)
                choose_high = row["delta_mismatch"] > delta_cost
                if choose_high != row["winner_is_high"]:
                    ok = False
                    break
            if ok:
                admissible.append({"a": a, "b": b})

    # Summarize b-range for each sampled a.
    bands = {}
    for rec in admissible:
        bands.setdefault(rec["a"], []).append(rec["b"])
    band_summary = {
        str(a): {"min_b": min(bs), "max_b": max(bs), "count": len(bs)}
        for a, bs in sorted(bands.items())
    }

    result = {
        "statement": "E79.79 geometric coefficient cone",
        "source": str(SRC),
        "admissible_count": len(admissible),
        "contains_current_point": any(rec["a"] == 0.36 and rec["b"] == 0.14 for rec in admissible),
        "sample_admissible": admissible[:200],
        "band_summary": band_summary,
        "inequalities": {
            "N10": "-a + 3b > 0.02078053689550286",
            "N12": "2a - 3b < 0.3307238267039273",
            "N16": "a < 0.3786042592168566",
        },
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
