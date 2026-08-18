#!/usr/bin/env python3
"""Probe for E78.96: denominator deficit as normalized quadratic margin."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import median


HERE = Path(__file__).resolve().parent
MARGIN_PATH = HERE / "E78_95_denominator_margin_results.json"
BASE77 = HERE.parent / "phase-77-weyl-limit-point"
ZETA_PATH = BASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json"
PLANT_PATH = BASE77 / "E77_5ac_theta_logderiv_coupling_plant.json"
OUT_PATH = HERE / "E78_96_den_deficit_quadratic_bridge_results.json"


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


def as_complex(obj: dict[str, str]) -> complex:
    return complex(float(obj["re"]), float(obj["im"]))


def ordered_margin_rows(build: str, margin: dict) -> list[dict]:
    if build == "zeta":
        rows = margin[build]["sigma"]["1.0"]["rows"] + margin[build]["sigma"]["3.0"]["rows"]
    else:
        rows = margin[build]["rows"]
    return sorted(rows, key=lambda row: (float(row["sigma"]), row["N"]))


def main() -> None:
    margin = json.loads(MARGIN_PATH.read_text())["builds"]
    raw = {
        "zeta": load_points(ZETA_PATH),
        "plant": load_points(PLANT_PATH),
    }

    result = {
        "statement": (
            "Exact bridge from denominator radial deficit to the normalized "
            "negative quadratic margin of the shell denominator quotient."
        ),
        "sources": {
            "theta_coupling_zeta": str(ZETA_PATH),
            "theta_coupling_plant": str(PLANT_PATH),
            "denominator_margin": str(MARGIN_PATH),
        },
        "builds": {},
    }

    for build in ("zeta", "plant"):
        rows = []
        max_err = 0.0
        for mrow in ordered_margin_rows(build, margin):
            sigma = mrow["sigma"]
            N = mrow["N"]
            old = raw[build][(sigma, N, "old")]
            new = raw[build][(sigma, N, "new")]

            d_old = as_complex(old["one_minus_theta"])
            d_new = as_complex(new["one_minus_theta"])
            q_b = d_new / d_old
            w_b = q_b - 1.0

            abs_q_b = abs(q_b)
            neg_quad = -(2.0 * w_b.real + abs(w_b) ** 2)
            reconstructed = neg_quad / (1.0 + abs_q_b)
            err = abs(reconstructed - mrow["denominator_radial_deficit"])
            max_err = max(max_err, err)

            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "q_b_re": q_b.real,
                    "q_b_im": q_b.imag,
                    "abs_q_b": abs_q_b,
                    "w_b_re": w_b.real,
                    "w_b_im": w_b.imag,
                    "negative_quadratic_margin": neg_quad,
                    "denominator_radial_deficit": mrow["denominator_radial_deficit"],
                    "normalized_quadratic_margin": reconstructed,
                    "normalizing_factor": 1.0 + abs_q_b,
                    "reconstruction_error": err,
                    "quadratic_minus_weighted_loss": neg_quad
                    - (1.0 + abs_q_b) * mrow["numerator_loss"],
                }
            )

        result["builds"][build] = {
            "max_reconstruction_error": max_err,
            "summary": {
                "normalizing_factor": stats([row["normalizing_factor"] for row in rows]),
                "negative_quadratic_margin": stats(
                    [row["negative_quadratic_margin"] for row in rows]
                ),
                "quadratic_minus_weighted_loss": stats(
                    [row["quadratic_minus_weighted_loss"] for row in rows]
                ),
            },
            "rows": rows,
        }

    OUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
