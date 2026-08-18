#!/usr/bin/env python3
"""Probe for E78.94: exact polarization of U-RADIAL-GAP."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE78 = Path(__file__).resolve().parent
BASE77 = BASE78.parent / "phase-77-weyl-limit-point"
ZETA_PATH = BASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json"
PLANT_PATH = BASE77 / "E77_5ac_theta_logderiv_coupling_plant.json"
OUT_PATH = BASE78 / "E78_94_gap_polarization_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def load_points(path: Path) -> dict[tuple[str, int, str], dict]:
    case = json.loads(path.read_text())["cases"][0]
    return {
        (str(row["sigma"]), row["step_N"], row["tag"]): row
        for row in case["points"]
    }


def build_rows(points: dict[tuple[str, int, str], dict]) -> list[dict]:
    rows = []
    for sigma in ["1.0", "3.0"]:
        for N in [8, 10, 12, 14, 16, 18, 20]:
            old = points.get((sigma, N, "old"))
            new = points.get((sigma, N, "new"))
            if not old or not new:
                continue

            abs_q_a = float(new["theta_prime_abs"]) / float(old["theta_prime_abs"])
            abs_q_b = float(new["one_minus_theta_abs"]) / float(old["one_minus_theta_abs"])
            numerator_radial_gain = abs_q_a - 1.0
            denominator_radial_deficit = 1.0 - abs_q_b
            u_radial_gap = abs_q_a - abs_q_b
            reconstruction_error = abs(
                u_radial_gap
                - (numerator_radial_gain + denominator_radial_deficit)
            )

            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "abs_q_a": abs_q_a,
                    "abs_q_b": abs_q_b,
                    "numerator_radial_gain": numerator_radial_gain,
                    "denominator_radial_deficit": denominator_radial_deficit,
                    "u_radial_gap": u_radial_gap,
                    "reconstruction_error": reconstruction_error,
                }
            )
    return rows


def main() -> None:
    zeta_rows = build_rows(load_points(ZETA_PATH))
    plant_rows = build_rows(load_points(PLANT_PATH))

    result = {
        "statement": (
            "Exact polarization of the U-radial gap into numerator radial gain "
            "plus denominator radial deficit."
        ),
        "sources": {
            "theta_coupling_zeta": str(ZETA_PATH),
            "theta_coupling_plant": str(PLANT_PATH),
        },
        "builds": {
            "zeta": {
                "max_reconstruction_error": max(row["reconstruction_error"] for row in zeta_rows),
                "summary": {
                    "numerator_radial_gain": stats([row["numerator_radial_gain"] for row in zeta_rows]),
                    "denominator_radial_deficit": stats([row["denominator_radial_deficit"] for row in zeta_rows]),
                    "u_radial_gap": stats([row["u_radial_gap"] for row in zeta_rows]),
                },
                "rows": zeta_rows,
            },
            "plant": {
                "max_reconstruction_error": max(row["reconstruction_error"] for row in plant_rows),
                "summary": {
                    "numerator_radial_gain": stats([row["numerator_radial_gain"] for row in plant_rows]),
                    "denominator_radial_deficit": stats([row["denominator_radial_deficit"] for row in plant_rows]),
                    "u_radial_gap": stats([row["u_radial_gap"] for row in plant_rows]),
                },
                "rows": plant_rows,
            },
        },
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
