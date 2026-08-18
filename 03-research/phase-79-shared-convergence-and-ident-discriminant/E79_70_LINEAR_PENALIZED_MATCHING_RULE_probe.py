#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
E69 = ROOT / "E79_69_relational_matching_selector_results.json"
OUT = ROOT / "E79_70_linear_penalized_matching_rule_results.json"


# First exact audited solution found by the search sweep.
COEFFS = {
    "mismatch": 1.0,
    "cardinality": -1.0,
    "span": 0.78,
    "gaps": -0.64,
    "start": 0.36,
}


def features(support):
    return {
        "cardinality": len(support),
        "span": max(support) - min(support) + 1,
        "gaps": (max(support) - min(support) + 1) - len(support),
        "start": min(support),
    }


def score(mismatch, support):
    f = features(support)
    return (
        COEFFS["mismatch"] * mismatch
        + COEFFS["cardinality"] * f["cardinality"]
        + COEFFS["span"] * f["span"]
        + COEFFS["gaps"] * f["gaps"]
        + COEFFS["start"] * f["start"]
    )


def main():
    e69 = json.loads(E69.read_text())
    rows = []
    exact = 0
    for row in e69["rows"]:
        candidates = {}
        for name in ["suffix", "pair", "triple"]:
            candidates[name] = {
                "support": row[name]["support"],
                "mismatch": row[name]["mismatch"],
                "score": score(row[name]["mismatch"], row[name]["support"]),
                **features(row[name]["support"]),
                "exact_match": row[name]["exact_match"],
            }
        best_name, best_data = min(candidates.items(), key=lambda kv: kv[1]["score"])
        best_exact = best_data["support"] == row["target_support"]
        exact += int(best_exact)
        rows.append(
            {
                "N": row["N"],
                "target_support": row["target_support"],
                "candidates": candidates,
                "best_rule": {
                    "name": best_name,
                    **best_data,
                    "best_exact_match": best_exact,
                },
            }
        )

    result = {
        "statement": "E79.70 linear penalized rule on the E79.69 tiny family",
        "source": str(E69),
        "coefficients": COEFFS,
        "rows": rows,
        "exact_match_count": exact,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
