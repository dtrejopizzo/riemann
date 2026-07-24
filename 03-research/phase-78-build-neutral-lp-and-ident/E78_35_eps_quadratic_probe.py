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


def as_vec(z: complex):
    return (z.real, z.imag)


def rot90_clockwise(v):
    x, y = v
    return (y, -x)


def main():
    result = {
        "statement": (
            "Exact quadratic form for eps_N as half the squared distance "
            "between normalized theta'_N and rotated normalized (1-theta_N)"
        ),
        "sources": {
            build: str(PHASE77 / f"E77_5ac_theta_logderiv_coupling_{build}.json")
            for build in ("zeta", "plant")
        },
        "builds": {},
    }

    for build in ("zeta", "plant"):
        case = load_case(build)
        rows = []
        max_error = 0.0
        max_quadratic = 0.0
        for pt in case["points"]:
            theta_prime = cval(pt["theta_prime"])
            den = cval(pt["one_minus_theta"])
            u = cval(pt["u"])
            u_abs = abs(u)
            eps = 1.0 - (u.imag / u_abs if u_abs else 0.0)

            a_abs = abs(theta_prime)
            b_abs = abs(den)
            a_hat = (theta_prime.real / a_abs, theta_prime.imag / a_abs)
            b_hat = (den.real / b_abs, den.imag / b_abs)
            jb_hat = rot90_clockwise(b_hat)
            dx = a_hat[0] - jb_hat[0]
            dy = a_hat[1] - jb_hat[1]
            quadratic = 0.5 * (dx * dx + dy * dy)
            err = abs(quadratic - eps)
            max_error = max(max_error, err)
            max_quadratic = max(max_quadratic, quadratic)

            rows.append(
                {
                    "sigma": pt["sigma"],
                    "step_N": pt["step_N"],
                    "section_N": pt["section_N"],
                    "tag": pt["tag"],
                    "eps": eps,
                    "quadratic_defect": quadratic,
                    "reconstruction_error": err,
                    "a_hat": [a_hat[0], a_hat[1]],
                    "j_b_hat": [jb_hat[0], jb_hat[1]],
                }
            )

        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max_error,
            "max_quadratic_defect": max_quadratic,
        }

    out_path = HERE / "E78_35_eps_quadratic_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
