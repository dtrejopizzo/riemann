#!/usr/bin/env python3
"""Probe for E78.91: exact numerator-denominator radial gap for u-shell growth."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


BASE78 = Path(__file__).resolve().parent
BASE77 = BASE78.parent / "phase-77-weyl-limit-point"
ZETA_PATH = BASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json"
PLANT_PATH = BASE77 / "E77_5ac_theta_logderiv_coupling_plant.json"
GROWTH_PATH = BASE78 / "E78_88_modulus_growth_split_results.json"
OUT_PATH = BASE78 / "E78_91_u_radial_gap_results.json"


def stats(values: list[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "min": min(values),
        "median": median(values),
        "max": max(values),
    }


def load_rows(path: Path) -> dict[tuple[str, int, str], dict]:
    case = json.loads(path.read_text())["cases"][0]
    return {
        (str(row["sigma"]), row["step_N"], row["tag"]): row
        for row in case["points"]
    }


def cplx(z: dict[str, str]) -> complex:
    return complex(float(z["re"]), float(z["im"]))


def build_rows(by: dict[tuple[str, int, str], dict], weighted=None) -> list[dict]:
    out = []
    for sigma in ["1.0", "3.0"]:
        for N in [8, 10, 12, 14, 16, 18, 20]:
            old = by.get((sigma, N, "old"))
            new = by.get((sigma, N, "new"))
            if not old or not new:
                continue

            u_old_abs = float(old["u_abs"])
            u_new_abs = float(new["u_abs"])
            a_old = cplx(old["theta_prime"])
            a_new = cplx(new["theta_prime"])
            b_old = cplx(old["one_minus_theta"])
            b_new = cplx(new["one_minus_theta"])

            q_a = a_new / a_old
            q_b = b_new / b_old
            abs_q_a = abs(q_a)
            abs_q_b = abs(q_b)
            abs_q_u = u_new_abs / u_old_abs
            radial_gap = abs_q_a - abs_q_b
            reconstructed_abs_q_u = abs_q_a / abs_q_b
            reconstruction_error = abs(abs_q_u - reconstructed_abs_q_u)

            row = {
                "sigma": sigma,
                "N": N,
                "abs_q_a": abs_q_a,
                "abs_q_b": abs_q_b,
                "abs_q_u": abs_q_u,
                "radial_gap": radial_gap,
                "reconstructed_abs_q_u": reconstructed_abs_q_u,
                "reconstruction_error": reconstruction_error,
            }
            if weighted is not None and (sigma, N) in weighted:
                row["weighted_modulus_quotient"] = weighted[(sigma, N)]
            out.append(row)
    return out


def main() -> None:
    zeta_rows = load_rows(ZETA_PATH)
    plant_rows = load_rows(PLANT_PATH)
    weighted = {
        (row["sigma"], row["N"]): row["weighted_modulus_quotient"]
        for row in json.loads(GROWTH_PATH.read_text())["rows"]
    }

    zeta = build_rows(zeta_rows, weighted=weighted)
    plant = build_rows(plant_rows)

    result = {
        "statement": (
            "Exact radial-gap law for u-shell growth: "
            "|u_new|/|u_old| = |q_a|/|q_b|, so the growth sign is controlled "
            "by the numerator-denominator radial gap |q_a|-|q_b|."
        ),
        "sources": {
            "theta_coupling_zeta": str(ZETA_PATH),
            "theta_coupling_plant": str(PLANT_PATH),
            "modulus_growth_split": str(GROWTH_PATH),
        },
        "builds": {
            "zeta": {
                "max_reconstruction_error": max(row["reconstruction_error"] for row in zeta),
                "summary": {
                    "abs_q_a": stats([row["abs_q_a"] for row in zeta]),
                    "abs_q_b": stats([row["abs_q_b"] for row in zeta]),
                    "radial_gap": stats([row["radial_gap"] for row in zeta]),
                    "abs_q_u": stats([row["abs_q_u"] for row in zeta]),
                },
                "rows": zeta,
            },
            "plant": {
                "max_reconstruction_error": max(row["reconstruction_error"] for row in plant),
                "summary": {
                    "abs_q_a": stats([row["abs_q_a"] for row in plant]),
                    "abs_q_b": stats([row["abs_q_b"] for row in plant]),
                    "radial_gap": stats([row["radial_gap"] for row in plant]),
                    "abs_q_u": stats([row["abs_q_u"] for row in plant]),
                },
                "rows": plant,
            },
        },
    }
    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
