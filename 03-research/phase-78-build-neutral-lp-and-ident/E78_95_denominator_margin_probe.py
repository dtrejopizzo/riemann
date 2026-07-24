#!/usr/bin/env python3
"""Probe for E78.95: denominator deficit dominates numerator loss."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE = Path(__file__).resolve().parent
POLAR_PATH = BASE / "E78_94_gap_polarization_results.json"
OUT_PATH = BASE / "E78_95_denominator_margin_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def monotone_nonincreasing(values: list[float]) -> bool:
    return all(values[i + 1] <= values[i] for i in range(len(values) - 1))


def monotone_nondecreasing(values: list[float]) -> bool:
    return all(values[i + 1] >= values[i] for i in range(len(values) - 1))


def augment(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        num_loss = max(0.0, -row["numerator_radial_gain"])
        margin = row["denominator_radial_deficit"] - num_loss
        exact_when_nonpositive = row["numerator_radial_gain"] <= 0
        exact_err = (
            abs(margin - row["u_radial_gap"]) if exact_when_nonpositive else 0.0
        )
        out.append(
            {
                **row,
                "numerator_loss": num_loss,
                "denominator_margin": margin,
                "exact_when_numerator_gain_nonpositive": exact_when_nonpositive,
                "exact_reconstruction_error_when_applicable": exact_err,
            }
        )
    return out


def sigma_summary(rows: list[dict], sigma: str) -> dict:
    sigma_rows = [row for row in rows if row["sigma"] == sigma]
    sigma_rows.sort(key=lambda row: row["N"])
    den = [row["denominator_radial_deficit"] for row in sigma_rows]
    loss = [row["numerator_loss"] for row in sigma_rows]
    margin = [row["denominator_margin"] for row in sigma_rows]
    return {
        "denominator_deficit_monotone_nondecreasing": monotone_nondecreasing(den),
        "numerator_loss_monotone_nondecreasing": monotone_nondecreasing(loss),
        "margin_monotone_nonincreasing": monotone_nonincreasing(margin),
        "rows": sigma_rows,
    }


def main() -> None:
    data = json.loads(POLAR_PATH.read_text())["builds"]
    zeta = augment(data["zeta"]["rows"])
    plant = augment(data["plant"]["rows"])

    result = {
        "statement": (
            "Exact margin form of the U-radial gap: denominator deficit minus "
            "numerator loss."
        ),
        "sources": {
            "gap_polarization": str(POLAR_PATH),
        },
        "builds": {
            "zeta": {
                "max_exact_reconstruction_error_when_applicable": max(
                    row["exact_reconstruction_error_when_applicable"] for row in zeta
                ),
                "summary": {
                    "numerator_loss": stats([row["numerator_loss"] for row in zeta]),
                    "denominator_margin": stats([row["denominator_margin"] for row in zeta]),
                },
                "sigma": {
                    "1.0": sigma_summary(zeta, "1.0"),
                    "3.0": sigma_summary(zeta, "3.0"),
                },
            },
            "plant": {
                "max_exact_reconstruction_error_when_applicable": max(
                    row["exact_reconstruction_error_when_applicable"] for row in plant
                ),
                "summary": {
                    "numerator_loss": stats([row["numerator_loss"] for row in plant]),
                    "denominator_margin": stats([row["denominator_margin"] for row in plant]),
                },
                "all_nonnegative": all(row["denominator_margin"] >= 0 for row in plant),
                "rows": plant,
            },
        },
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
