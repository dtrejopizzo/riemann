#!/usr/bin/env python3
"""Probe for E78.92: exact weighted modulus quotient split through U-RADIAL-GAP."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE78 = Path(__file__).resolve().parent
BASE77 = BASE78.parent / "phase-77-weyl-limit-point"
ZETA_PATH = BASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json"
POLAR_PATH = BASE78 / "E78_32_delta_safeu_polar_results.json"
QUOT_PATH = BASE78 / "E78_83_weighted_quotient_results.json"
GROWTH_PATH = BASE78 / "E78_88_modulus_growth_split_results.json"
OUT_PATH = BASE78 / "E78_92_weighted_gap_split_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def cplx(z: dict[str, str]) -> complex:
    return complex(float(z["re"]), float(z["im"]))


def main() -> None:
    case = json.loads(ZETA_PATH.read_text())["cases"][0]
    points = {
        (str(row["sigma"]), row["step_N"], row["tag"]): row
        for row in case["points"]
    }
    polar = {
        (row["sigma"], row["N"]): row
        for row in json.loads(POLAR_PATH.read_text())["builds"]["zeta"]["rows"]
    }
    weighted_q = {
        (row["sigma"], row["N"]): row["minus_SAFEDELTA"]
        for row in json.loads(QUOT_PATH.read_text())["rows"]
    }
    weighted_mod = {
        (row["sigma"], row["N"]): row["weighted_modulus_quotient"]
        for row in json.loads(GROWTH_PATH.read_text())["rows"]
    }

    rows = []
    prefactors = []
    gaps = []
    errors = []

    for sigma in ["1.0", "3.0"]:
        for N in [8, 10, 12, 14, 16, 18, 20]:
            old = points[(sigma, N, "old")]
            new = points[(sigma, N, "new")]

            a_old = cplx(old["theta_prime"])
            a_new = cplx(new["theta_prime"])
            b_old = cplx(old["one_minus_theta"])
            b_new = cplx(new["one_minus_theta"])

            abs_q_b = abs(b_new / b_old)
            radial_gap = abs(a_new / a_old) - abs_q_b
            minus_safedelta = weighted_q[(sigma, N)]
            u_old_abs = float(old["u_abs"])
            s_new = polar[(sigma, N)]["new_im_share"]

            prefactor = (
                N * minus_safedelta * abs_q_b / (2.0 * u_old_abs * s_new)
            )
            weighted_modulus = weighted_mod[(sigma, N)]
            reconstructed = prefactor / radial_gap
            error = abs(reconstructed - weighted_modulus)

            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "weighted_modulus_quotient": weighted_modulus,
                    "prefactor": prefactor,
                    "u_radial_gap": radial_gap,
                    "reconstructed_weighted_modulus_quotient": reconstructed,
                    "reconstruction_error": error,
                    "abs_q_b": abs_q_b,
                    "u_old_abs": u_old_abs,
                    "minus_SAFEDELTA": minus_safedelta,
                    "new_im_share": s_new,
                }
            )
            prefactors.append(prefactor)
            gaps.append(radial_gap)
            errors.append(error)

    result = {
        "statement": (
            "Exact split of the weighted modulus quotient into a prefactor "
            "divided by the U-radial gap."
        ),
        "sources": {
            "theta_coupling_zeta": str(ZETA_PATH),
            "delta_safeu_polar": str(POLAR_PATH),
            "weighted_quotient": str(QUOT_PATH),
            "modulus_growth_split": str(GROWTH_PATH),
        },
        "max_reconstruction_error": max(errors),
        "summary": {
            "prefactor": stats(prefactors),
            "u_radial_gap": stats(gaps),
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
