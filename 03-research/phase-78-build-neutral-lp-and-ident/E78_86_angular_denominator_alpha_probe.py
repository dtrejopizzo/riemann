#!/usr/bin/env python3
"""Probe for E78.86: exact alpha-law for the angular denominator factor."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE = Path(__file__).resolve().parent
EPS_PATH = BASE / "E78_33_angular_eps_results.json"
SPLIT_PATH = BASE / "E78_85_modulus_quotient_split_results.json"
OUT_PATH = BASE / "E78_86_angular_denominator_alpha_results.json"
TOL = 1e-12


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def main() -> None:
    eps_data = json.loads(EPS_PATH.read_text())
    split_data = json.loads(SPLIT_PATH.read_text())

    eps_rows = {
        (row["sigma"], row["N"]): row
        for row in eps_data["builds"]["zeta"]["rows"]
    }
    split_rows = split_data["rows"]

    rows = []
    alpha_values = []
    abs_alpha_values = []
    factor_errors = []
    share_errors = []
    bounds = []

    for row in split_rows:
        key = (row["sigma"], row["N"])
        eps_row = eps_rows[key]

        modulus_term = eps_row["modulus_term"]
        angular_term = eps_row["angular_term"]
        old_abs_u = eps_row["old_abs_u"]
        eps_drift = eps_row["eps_drift"]

        alpha_exact = angular_term / modulus_term
        alpha_from_eps = 2.0 * old_abs_u * eps_drift / modulus_term
        alpha_error = abs(alpha_exact - alpha_from_eps)

        factor = row["angular_den_factor"]
        factor_from_alpha = 1.0 / (1.0 + alpha_exact)
        factor_error = abs(factor - factor_from_alpha)

        share = row["modulus_share_of_delta"]
        share_error = abs(share - factor_from_alpha)

        abs_alpha = abs(alpha_exact)
        if abs_alpha < 1.0:
            lower = 1.0 / (1.0 + abs_alpha)
            upper = 1.0 / (1.0 - abs_alpha)
        else:
            lower = None
            upper = None

        rows.append(
            {
                "sigma": row["sigma"],
                "N": row["N"],
                "alpha_exact": alpha_exact,
                "alpha_from_eps": alpha_from_eps,
                "alpha_error": alpha_error,
                "abs_alpha": abs_alpha,
                "angular_den_factor": factor,
                "factor_from_alpha": factor_from_alpha,
                "factor_error": factor_error,
                "modulus_share_of_delta": share,
                "share_error": share_error,
                "lower_envelope_from_abs_alpha": lower,
                "upper_envelope_from_abs_alpha": upper,
                "quotient": row["quotient"],
                "modulus_quotient": row["modulus_quotient"],
            }
        )

        alpha_values.append(alpha_exact)
        abs_alpha_values.append(abs_alpha)
        factor_errors.append(factor_error)
        share_errors.append(share_error)
        if lower is not None and upper is not None:
            bounds.append(lower - TOL <= factor <= upper + TOL)

    result = {
        "statement": (
            "Exact alpha-law for the angular denominator factor: "
            "alpha_N = angular_term_N/modulus_term_N = "
            "2|u_N|(eps_N-eps_N+2)/modulus_term_N and "
            "angular_den_factor_N = 1/(1+alpha_N)."
        ),
        "sources": {
            "angular_eps": str(EPS_PATH),
            "modulus_quotient_split": str(SPLIT_PATH),
        },
        "max_alpha_error": max(row["alpha_error"] for row in rows),
        "max_factor_error": max(factor_errors),
        "max_share_error": max(share_errors),
        "summary": {
            "alpha_exact": stats(alpha_values),
            "abs_alpha": stats(abs_alpha_values),
            "angular_den_factor": stats([row["angular_den_factor"] for row in rows]),
        },
        "all_envelope_checks_pass": all(bounds),
        "rows": rows,
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
