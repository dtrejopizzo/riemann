#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
E70 = ROOT / "E79_70_linear_penalized_matching_rule_results.json"
OUT = ROOT / "E79_72_normalized_gain_cost_rule_results.json"


BASE = {
    "mismatch": 1.0,
    "cardinality": -1.0,
    "span": 0.78,
    "gaps": -0.64,
    "start": 0.36,
}


def normalized_coeffs():
    # Using span = card + gaps for every support.
    return {
        "mismatch": 1.0,
        "cardinality": BASE["cardinality"] + BASE["span"],
        "gaps": BASE["span"] + BASE["gaps"],
        "start": BASE["start"],
    }


def score_reduced(coeffs, cand):
    return (
        coeffs["mismatch"] * cand["mismatch"]
        + coeffs["cardinality"] * cand["cardinality"]
        + coeffs["gaps"] * cand["gaps"]
        + coeffs["start"] * cand["start"]
    )


def exact_count(rows, coeffs):
    exact = 0
    picked = {}
    for row in rows:
        vals = []
        for name, cand in row["candidates"].items():
            vals.append((score_reduced(coeffs, cand), name, cand["support"]))
        vals.sort()
        best = vals[0]
        ok = best[2] == row["target_support"]
        exact += int(ok)
        picked[row["N"]] = {"name": best[1], "support": best[2], "exact": ok}
    return exact, picked


def main():
    e70 = json.loads(E70.read_text())
    rows = e70["rows"]
    reduced = normalized_coeffs()
    exact, picks = exact_count(rows, reduced)

    # Small local box around the reduced coefficients to test robustness.
    grid = []
    exact_count_box = 0
    for card in [i / 100 for i in range(-40, -4, 2)]:
        for gaps in [i / 100 for i in range(0, 31, 2)]:
            for start in [i / 100 for i in range(15, 56, 2)]:
                coeffs = {
                    "mismatch": 1.0,
                    "cardinality": card,
                    "gaps": gaps,
                    "start": start,
                }
                e, p = exact_count(rows, coeffs)
                rec = {
                    "coefficients": coeffs,
                    "exact_match_count": e,
                    "picks": p,
                }
                grid.append(rec)
                if e == len(rows):
                    exact_count_box += 1

    grid.sort(key=lambda r: -r["exact_match_count"])

    result = {
        "statement": "E79.72 normalized gain-cost rule",
        "source": str(E70),
        "base_coefficients": BASE,
        "reduced_coefficients": reduced,
        "base_reduced_exact_match_count": exact,
        "base_reduced_picks": picks,
        "local_box_summary": {
            "total_points": len(grid),
            "exact_5_of_5_points": exact_count_box,
        },
        "examples_exact": [g for g in grid if g["exact_match_count"] == len(rows)][:25],
        "top_configs": grid[:25],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
