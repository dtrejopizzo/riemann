#!/usr/bin/env python3
"""E79.54 - zeta-anchored projected level template audit."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "E79_52_two_mode_sigma_template_results.json"
SIGMAS = [0.75, 1.0, 1.5, 2.0]
SIGMA_C = 1.375


def main():
    data = json.loads(SRC.read_text())
    zeta = next(case for case in data["cases"] if case["label"] == "zeta")
    alpha = sum(row["N"] * float(row["coefficients"]["slope"]) for row in zeta["rows"]) / len(zeta["rows"])
    gamma = sum(row["N"] * float(row["coefficients"]["curvature_mode"]) for row in zeta["rows"]) / len(zeta["rows"])

    out = {
        "statement": "E79.54 projected level template audit",
        "source": str(SRC),
        "alpha_zeta_mean": alpha,
        "gamma_zeta_mean": gamma,
        "sigma_center": SIGMA_C,
        "cases": [],
    }

    for case in data["cases"]:
        rows = []
        for row in case["rows"]:
            N = row["N"]
            ys = [float(row["mismatches"][str(s)]) for s in SIGMAS]
            transported = [(alpha / N) * s + (gamma / N) * (s - SIGMA_C) ** 2 for s in SIGMAS]
            level = sum(y - t for y, t in zip(ys, transported)) / len(SIGMAS)
            fit = [t + level for t in transported]
            errs = [y - f for y, f in zip(ys, fit)]
            scale = max(abs(y) for y in ys) or 1.0
            max_err = max(abs(e) for e in errs) / scale
            rms_err = (sum(e * e for e in errs) / len(errs)) ** 0.5 / scale
            rows.append(
                {
                    "N": N,
                    "support_abs": row["support_abs"],
                    "level": level,
                    "fit": fit,
                    "errors": errs,
                    "normalized_max_error": max_err,
                    "normalized_rms_error": rms_err,
                }
            )
        out["cases"].append({"label": case["label"], "rows": rows})

    out_path = HERE / "E79_54_projected_level_template_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print("alpha", alpha, "gamma", gamma)
    for case in out["cases"]:
        print(case["label"])
        for row in case["rows"]:
            print(
                f" N={row['N']:2d} max={row['normalized_max_error']:.6g} "
                f"rms={row['normalized_rms_error']:.6g} level={row['level']:.6g}"
            )
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
