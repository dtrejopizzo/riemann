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
            "Exact quotient-skew form of denominator phase rigidity for "
            "(1-theta_{N+2})/(1-theta_N)"
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
        max_phase_error = 0.0
        max_skew = 0.0
        for sigma, sigma_rows in by_sigma.items():
            sigma_rows.sort(key=lambda p: p["section_N"])
            for old, new in zip(sigma_rows, sigma_rows[1:]):
                old_den = cval(old["one_minus_theta"])
                new_den = cval(new["one_minus_theta"])
                q = new_den / old_den
                phase = cmath.phase(q)
                skew = q.imag / q.real if q.real != 0 else math.inf
                phase_from_skew = math.atan(skew) if math.isfinite(skew) else math.copysign(math.pi / 2, skew)
                err = abs(phase - phase_from_skew)
                max_phase_error = max(max_phase_error, err)
                max_skew = max(max_skew, abs(skew) if math.isfinite(skew) else math.inf)
                rows.append(
                    {
                        "sigma": sigma,
                        "N": old["section_N"],
                        "to_N": new["section_N"],
                        "quotient_re": q.real,
                        "quotient_im": q.imag,
                        "quotient_abs": abs(q),
                        "phase_step": phase,
                        "abs_phase_step": abs(phase),
                        "skew_im_over_re": skew,
                        "abs_skew_im_over_re": abs(skew) if math.isfinite(skew) else math.inf,
                        "phase_from_skew": phase_from_skew,
                        "phase_reconstruction_error": err,
                    }
                )

        result["builds"][build] = {
            "rows": rows,
            "max_phase_reconstruction_error": max_phase_error,
            "max_abs_skew": max_skew,
        }

    out_path = HERE / "E78_39_den_quotient_skew_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
