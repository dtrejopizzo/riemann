#!/usr/bin/env python3
"""Probe for E78.87: audited endpoint reduction for the modulus quotient."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE = Path(__file__).resolve().parent
SPLIT_PATH = BASE / "E78_85_modulus_quotient_split_results.json"
OUT_PATH = BASE / "E78_87_modulus_quotient_endpoint_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def main() -> None:
    rows = json.loads(SPLIT_PATH.read_text())["rows"]
    by_n: dict[int, dict[str, dict[str, float | int | str]]] = {}
    for row in rows:
        by_n.setdefault(row["N"], {})[row["sigma"]] = row

    comparisons = []
    endpoint_values = []
    all_decrease = True

    for N in sorted(by_n):
        row_1 = by_n[N]["1.0"]
        row_3 = by_n[N]["3.0"]
        decreases = row_3["modulus_quotient"] <= row_1["modulus_quotient"]
        all_decrease = all_decrease and decreases
        endpoint_values.append(row_1["modulus_quotient"])
        comparisons.append(
            {
                "N": N,
                "sigma_left": "1.0",
                "sigma_right": "3.0",
                "modulus_quotient_left": row_1["modulus_quotient"],
                "modulus_quotient_right": row_3["modulus_quotient"],
                "difference_right_minus_left": (
                    row_3["modulus_quotient"] - row_1["modulus_quotient"]
                ),
                "decreases": decreases,
            }
        )

    worst_row = max(rows, key=lambda row: row["modulus_quotient"])

    result = {
        "statement": (
            "Audit of the left-endpoint reduction candidate for the modulus "
            "quotient branch."
        ),
        "sources": {
            "modulus_quotient_split": str(SPLIT_PATH),
        },
        "all_audited_pairs_decrease": all_decrease,
        "endpoint_summary_sigma_1": stats(endpoint_values),
        "worst_audited_row": worst_row,
        "comparisons": comparisons,
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
