#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"


def load_case(build: str):
    path = PHASE77 / f"E77_5ac_theta_logderiv_coupling_{build}.json"
    return json.loads(path.read_text())["cases"][0]


def cval(z):
    return complex(float(z["re"]), float(z["im"]))


def det2(a: complex, b: complex) -> float:
    return a.imag * b.real - a.real * b.imag


def main():
    result = {
        "statement": (
            "Exact increment-area form of the denominator symplectic numerator: "
            "det(d_{N+2}, d_N) = det(Delta d_N, d_N)"
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
        max_abs_increment = 0.0
        for sigma, sigma_rows in by_sigma.items():
            sigma_rows.sort(key=lambda p: p["section_N"])
            for old, new in zip(sigma_rows, sigma_rows[1:]):
                d_old = cval(old["one_minus_theta"])
                d_new = cval(new["one_minus_theta"])
                delta = d_new - d_old
                direct = det2(d_new, d_old)
                increment_area = det2(delta, d_old)
                err = abs(direct - increment_area)
                max_error = max(max_error, err)
                max_abs_increment = max(max_abs_increment, abs(increment_area))
                rows.append(
                    {
                        "sigma": sigma,
                        "N": old["section_N"],
                        "to_N": new["section_N"],
                        "direct_symplectic_numerator": direct,
                        "increment_area_numerator": increment_area,
                        "reconstruction_error": err,
                        "delta_d_abs": abs(delta),
                        "old_d_abs": abs(d_old),
                    }
                )

        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max_error,
            "max_abs_increment_area": max_abs_increment,
        }

    out_path = HERE / "E78_42_den_increment_area_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
