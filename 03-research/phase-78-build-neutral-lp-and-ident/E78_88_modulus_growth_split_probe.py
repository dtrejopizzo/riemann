#!/usr/bin/env python3
"""Probe for E78.88: exact growth/sector split of the modulus quotient."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE = Path(__file__).resolve().parent
POLAR_PATH = BASE / "E78_32_delta_safeu_polar_results.json"
SPLIT_PATH = BASE / "E78_85_modulus_quotient_split_results.json"
OUT_PATH = BASE / "E78_88_modulus_growth_split_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def main() -> None:
    polar = json.loads(POLAR_PATH.read_text())["builds"]["zeta"]["rows"]
    split = {
        (row["sigma"], row["N"]): row
        for row in json.loads(SPLIT_PATH.read_text())["rows"]
    }

    rows = []
    growth_values = []
    sector_values = []
    recon_errors = []
    weighted_recon_errors = []

    for row in polar:
        key = (row["sigma"], row["N"])
        split_row = split[key]

        delta_abs = row["new_abs_u"] - row["old_abs_u"]
        minus_safedelta = split_row["quotient"] * row["delta_safe_u"]
        new_share = row["new_im_share"]
        N = row["N"]

        modulus_quotient = split_row["modulus_quotient"]

        growth_quotient = N * minus_safedelta / (2.0 * delta_abs)
        sector_factor = 1.0 / (N * new_share)
        reconstructed_modulus_quotient = growth_quotient * sector_factor
        reconstruction_error = abs(
            reconstructed_modulus_quotient - modulus_quotient
        )

        weighted_modulus_quotient = N * modulus_quotient
        weighted_reconstructed = growth_quotient / new_share
        weighted_reconstruction_error = abs(
            weighted_reconstructed - weighted_modulus_quotient
        )

        rows.append(
            {
                "sigma": row["sigma"],
                "N": N,
                "modulus_quotient": modulus_quotient,
                "growth_quotient": growth_quotient,
                "sector_factor": sector_factor,
                "new_im_share": new_share,
                "reconstructed_modulus_quotient": reconstructed_modulus_quotient,
                "reconstruction_error": reconstruction_error,
                "weighted_modulus_quotient": weighted_modulus_quotient,
                "weighted_reconstructed": weighted_reconstructed,
                "weighted_reconstruction_error": weighted_reconstruction_error,
            }
        )
        growth_values.append(growth_quotient)
        sector_values.append(sector_factor)
        recon_errors.append(reconstruction_error)
        weighted_recon_errors.append(weighted_reconstruction_error)

    result = {
        "statement": (
            "Exact split of the modulus quotient into a growth quotient "
            "times a sector factor 1/(N*new_im_share)."
        ),
        "sources": {
            "delta_safeu_polar": str(POLAR_PATH),
            "modulus_quotient_split": str(SPLIT_PATH),
        },
        "max_reconstruction_error": max(recon_errors),
        "max_weighted_reconstruction_error": max(weighted_recon_errors),
        "summary": {
            "growth_quotient": stats(growth_values),
            "sector_factor": stats(sector_values),
            "weighted_modulus_quotient": stats(
                [row["weighted_modulus_quotient"] for row in rows]
            ),
        },
        "rows": rows,
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
