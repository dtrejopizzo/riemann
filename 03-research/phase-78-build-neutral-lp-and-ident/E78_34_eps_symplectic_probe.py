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
    return a.real * b.imag - a.imag * b.real


def main():
    result = {
        "statement": (
            "Exact symplectic formula for eps_N = 1 - Im(u_N)/|u_N| as "
            "1 minus normalized determinant of (theta'_N, 1-theta_N)"
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
        min_det_norm = None
        max_eps = 0.0
        for pt in case["points"]:
            theta_prime = cval(pt["theta_prime"])
            den = cval(pt["one_minus_theta"])
            u = cval(pt["u"])
            u_abs = abs(u)
            im_share = u.imag / u_abs if u_abs else 0.0
            eps = 1.0 - im_share
            norm = abs(theta_prime) * abs(den)
            det_norm = det2(theta_prime, den) / norm if norm else 0.0
            reconstructed_eps = 1.0 - det_norm
            err = abs(reconstructed_eps - eps)
            max_error = max(max_error, err)
            max_eps = max(max_eps, eps)
            min_det_norm = det_norm if min_det_norm is None else min(min_det_norm, det_norm)
            rows.append(
                {
                    "sigma": pt["sigma"],
                    "step_N": pt["step_N"],
                    "section_N": pt["section_N"],
                    "tag": pt["tag"],
                    "eps": eps,
                    "det_norm": det_norm,
                    "reconstructed_eps": reconstructed_eps,
                    "reconstruction_error": err,
                    "theta_prime_abs": abs(theta_prime),
                    "one_minus_theta_abs": abs(den),
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max_error,
            "min_det_norm": min_det_norm,
            "max_eps": max_eps,
        }

    out_path = HERE / "E78_34_eps_symplectic_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
