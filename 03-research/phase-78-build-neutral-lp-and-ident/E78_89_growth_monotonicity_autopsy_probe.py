#!/usr/bin/env python3
"""Probe for E78.89: growth-quotient monotonicity autopsy."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE = Path(__file__).resolve().parent
GROWTH_PATH = BASE / "E78_88_modulus_growth_split_results.json"
OUT_PATH = BASE / "E78_89_growth_monotonicity_autopsy_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def main() -> None:
    rows = json.loads(GROWTH_PATH.read_text())["rows"]
    by_n: dict[int, dict[str, dict[str, float | int | str]]] = {}
    for row in rows:
        by_n.setdefault(row["N"], {})[row["sigma"]] = row

    comparisons = []
    diffs = []
    all_decrease = True
    for N in sorted(by_n):
        left = by_n[N]["1.0"]
        right = by_n[N]["3.0"]
        growth_diff = right["growth_quotient"] - left["growth_quotient"]
        weighted_diff = (
            right["weighted_modulus_quotient"] - left["weighted_modulus_quotient"]
        )
        decreases = growth_diff <= 0
        all_decrease = all_decrease and decreases
        comparisons.append(
            {
                "N": N,
                "growth_left": left["growth_quotient"],
                "growth_right": right["growth_quotient"],
                "growth_diff_right_minus_left": growth_diff,
                "growth_decreases": decreases,
                "weighted_left": left["weighted_modulus_quotient"],
                "weighted_right": right["weighted_modulus_quotient"],
                "weighted_diff_right_minus_left": weighted_diff,
                "new_im_share_left": left["new_im_share"],
                "new_im_share_right": right["new_im_share"],
            }
        )
        diffs.append(growth_diff)

    result = {
        "statement": (
            "Audit showing that the isolated growth quotient is not sigma-"
            "monotone on the certified ladder, even though the weighted "
            "modulus quotient remains sigma-decreasing."
        ),
        "sources": {
            "modulus_growth_split": str(GROWTH_PATH),
        },
        "all_growth_pairs_decrease": all_decrease,
        "growth_diff_stats": stats(diffs),
        "largest_growth_violation": max(comparisons, key=lambda row: row["growth_diff_right_minus_left"]),
        "largest_growth_drop": min(comparisons, key=lambda row: row["growth_diff_right_minus_left"]),
        "comparisons": comparisons,
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
