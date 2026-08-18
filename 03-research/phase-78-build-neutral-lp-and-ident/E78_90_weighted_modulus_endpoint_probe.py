#!/usr/bin/env python3
"""Probe for E78.90: audited constant envelope for the weighted modulus endpoint."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE = Path(__file__).resolve().parent
GROWTH_PATH = BASE / "E78_88_modulus_growth_split_results.json"
COUPLING_PATH = BASE / "E78_77_safeu_base_coupling_results.json"
OUT_PATH = BASE / "E78_90_weighted_modulus_endpoint_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def corr(xs: list[float], ys: list[float]) -> float:
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / len(xs)
    sx = (sum((x - mx) ** 2 for x in xs) / len(xs)) ** 0.5
    sy = (sum((y - my) ** 2 for y in ys) / len(ys)) ** 0.5
    return cov / (sx * sy)


def main() -> None:
    growth_rows = [
        row
        for row in json.loads(GROWTH_PATH.read_text())["rows"]
        if row["sigma"] == "1.0"
    ]
    common_rows = [
        row
        for row in growth_rows
        if row["N"] <= 18
    ]
    coupling_rows = {
        (row["sigma"], row["N"]): row
        for row in json.loads(COUPLING_PATH.read_text())["rows"]
    }

    endpoint_values = [row["weighted_modulus_quotient"] for row in growth_rows]
    common_values = [row["weighted_modulus_quotient"] for row in common_rows]

    radial_fields = [
        "safeu_amplitude_A_N",
        "basepoint_reserve",
        "tail_over_A",
        "A_over_base",
        "tail_over_base",
    ]
    correlations = {}
    for field in radial_fields:
        xs = [coupling_rows[("1.0", row["N"])][field] for row in common_rows]
        ys = [row["weighted_modulus_quotient"] for row in common_rows]
        correlations[field] = corr(xs, ys)

    result = {
        "statement": (
            "Audit of the left-endpoint weighted modulus quotient "
            "W_N(1.0)=N*MODULUS-QUOTIENT_N(1.0)."
        ),
        "sources": {
            "modulus_growth_split": str(GROWTH_PATH),
            "safeu_base_coupling": str(COUPLING_PATH),
        },
        "endpoint_summary_sigma_1": stats(endpoint_values),
        "common_summary_sigma_1_N_le_18": stats(common_values),
        "worst_endpoint_row": max(growth_rows, key=lambda row: row["weighted_modulus_quotient"]),
        "radial_correlation_autopsy_on_common_ladder": correlations,
        "rows_sigma_1": growth_rows,
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
