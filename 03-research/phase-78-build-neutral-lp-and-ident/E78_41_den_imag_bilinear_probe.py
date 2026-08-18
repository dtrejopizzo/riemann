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
            "Exact bilinear formula for Im((1-theta_{N+2})/(1-theta_N)) as a "
            "symplectic quotient"
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
        max_abs_bilinear = 0.0
        for sigma, sigma_rows in by_sigma.items():
            sigma_rows.sort(key=lambda p: p["section_N"])
            for old, new in zip(sigma_rows, sigma_rows[1:]):
                old_den = cval(old["one_minus_theta"])
                new_den = cval(new["one_minus_theta"])
                q = new_den / old_den
                bilinear = det2(new_den, old_den) / (abs(old_den) ** 2)
                err = abs(q.imag - bilinear)
                max_error = max(max_error, err)
                max_abs_bilinear = max(max_abs_bilinear, abs(bilinear))
                rows.append(
                    {
                        "sigma": sigma,
                        "N": old["section_N"],
                        "to_N": new["section_N"],
                        "quotient_im": q.imag,
                        "bilinear_im_formula": bilinear,
                        "reconstruction_error": err,
                        "old_den_abs_sq": abs(old_den) ** 2,
                        "symplectic_numerator": det2(new_den, old_den),
                    }
                )

        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max_error,
            "max_abs_bilinear_im": max_abs_bilinear,
        }

    out_path = HERE / "E78_41_den_imag_bilinear_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
