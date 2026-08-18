#!/usr/bin/env python3
"""Probe for E78.93: compare rigidity of U-RADIAL-GAP vs PREF_N."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE78 = Path(__file__).resolve().parent
BASE77 = BASE78.parent / "phase-77-weyl-limit-point"
SPLIT_PATH = BASE78 / "E78_92_weighted_gap_split_results.json"
PLANT_THETA_PATH = BASE77 / "E77_5ac_theta_logderiv_coupling_plant.json"
PHASE_G_PATH = BASE77 / "E77_5g_schur_phase_increment_results.json"
OUT_PATH = BASE78 / "E78_93_gap_vs_prefactor_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def cplx(z: dict[str, str]) -> complex:
    return complex(float(z["re"]), float(z["im"]))


def monotone_nonincreasing(values: list[float]) -> bool:
    return all(values[i + 1] <= values[i] for i in range(len(values) - 1))


def main() -> None:
    zeta_rows = json.loads(SPLIT_PATH.read_text())["rows"]

    zeta_summary = {}
    for sigma in ["1.0", "3.0"]:
        sigma_rows = [row for row in zeta_rows if row["sigma"] == sigma]
        sigma_rows.sort(key=lambda row: row["N"])
        zeta_summary[sigma] = {
            "gap_values": [row["u_radial_gap"] for row in sigma_rows],
            "prefactor_values": [row["prefactor"] for row in sigma_rows],
            "gap_monotone_nonincreasing": monotone_nonincreasing(
                [row["u_radial_gap"] for row in sigma_rows]
            ),
            "prefactor_monotone_nonincreasing": monotone_nonincreasing(
                [row["prefactor"] for row in sigma_rows]
            ),
        }

    plant_points = json.loads(PLANT_THETA_PATH.read_text())["cases"][0]["points"]
    plant_points = {
        (str(row["sigma"]), row["step_N"], row["tag"]): row
        for row in plant_points
    }
    phase_g_case = json.loads(PHASE_G_PATH.read_text())["cases"][1]
    flat_increments = {}
    for block in phase_g_case["increments"]:
        N = block["from_N"]
        for row in block["sigmas"]:
            sigma = str(float(row["sigma"]))
            flat_increments[(sigma, N)] = row

    plant_rows = []
    for sigma in ["1.0", "3.0"]:
        for N in [8, 10, 12, 14, 16, 18, 20]:
            old = plant_points.get((sigma, N, "old"))
            new = plant_points.get((sigma, N, "new"))
            inc = flat_increments.get((sigma, N))
            if not old or not new or not inc:
                continue

            a_old = cplx(old["theta_prime"])
            a_new = cplx(new["theta_prime"])
            b_old = cplx(old["one_minus_theta"])
            b_new = cplx(new["one_minus_theta"])
            abs_q_b = abs(b_new / b_old)
            gap = abs(a_new / a_old) - abs_q_b

            u_old_abs = float(old["u_abs"])
            u_new = cplx(new["u"])
            s_new = u_new.imag / abs(u_new)
            minus_safedelta = -float(inc["delta_safe_derivative"])
            pref = (
                float("nan")
                if s_new == 0
                else N * minus_safedelta * abs_q_b / (2.0 * u_old_abs * s_new)
            )

            plant_rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "u_radial_gap": gap,
                    "prefactor": pref,
                    "minus_SAFEDELTA": minus_safedelta,
                    "new_im_share": s_new,
                }
            )

    result = {
        "statement": (
            "Audit that U-RADIAL-GAP is the rigid half of the weighted-gap "
            "split, while PREF_N remains oscillatory and falsifier-unstable."
        ),
        "sources": {
            "weighted_gap_split": str(SPLIT_PATH),
            "theta_coupling_plant": str(PLANT_THETA_PATH),
            "phase_g": str(PHASE_G_PATH),
        },
        "zeta": {
            "summary": zeta_summary,
            "gap_stats": stats([row["u_radial_gap"] for row in zeta_rows]),
            "prefactor_stats": stats([row["prefactor"] for row in zeta_rows]),
        },
        "plant": {
            "gap_stats": stats([row["u_radial_gap"] for row in plant_rows]),
            "prefactor_stats": stats([row["prefactor"] for row in plant_rows]),
            "rows": plant_rows,
        },
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
