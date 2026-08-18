#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"


def load_case(build: str):
    path = PHASE77 / f"E77_5ac_theta_logderiv_coupling_{build}.json"
    return json.loads(path.read_text())["cases"][0]


def cval(z):
    return complex(float(z["re"]), float(z["im"]))


def main():
    result = {
        "statement": (
            "Exact phase form of denominator-direction chord defect for "
            "normalized (1-theta_N)"
        ),
        "sources": {
            build: str(PHASE77 / f"E77_5ac_theta_logderiv_coupling_{build}.json")
            for build in ("zeta", "plant")
        },
        "builds": {},
    }

    for build in ("zeta", "plant"):
        case = load_case(build)
        pts = [p for p in case["points"] if p["tag"] == "new"]
        by_sigma = {}
        for pt in pts:
            by_sigma.setdefault(pt["sigma"], []).append(pt)

        rows = []
        max_error = 0.0
        max_abs_phase_step = 0.0
        for sigma, sigma_rows in by_sigma.items():
            sigma_rows.sort(key=lambda p: p["section_N"])
            for old, new in zip(sigma_rows, sigma_rows[1:]):
                b_old = cval(old["one_minus_theta"]) / float(old["one_minus_theta_abs"])
                b_new = cval(new["one_minus_theta"]) / float(new["one_minus_theta_abs"])
                ratio = b_new / b_old
                phase_step = cmath.phase(ratio)
                dirdef = 1.0 - (b_old.real * b_new.real + b_old.imag * b_new.imag)
                reconstructed = 1.0 - math.cos(phase_step)
                half_square = 2.0 * math.sin(phase_step / 2.0) ** 2
                err = abs(reconstructed - dirdef)
                max_error = max(max_error, err)
                max_abs_phase_step = max(max_abs_phase_step, abs(phase_step))
                rows.append(
                    {
                        "sigma": sigma,
                        "N": old["section_N"],
                        "to_N": new["section_N"],
                        "phase_step": phase_step,
                        "abs_phase_step": abs(phase_step),
                        "dirdef_b": dirdef,
                        "reconstructed_dirdef": reconstructed,
                        "half_angle_form": half_square,
                        "reconstruction_error": err,
                    }
                )

        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max_error,
            "max_abs_phase_step": max_abs_phase_step,
        }

    out_path = HERE / "E78_38_den_phase_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
