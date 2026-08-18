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


def main():
    result = {
        "statement": (
            "Exact polar decomposition of delta_safe_u into modulus gain and "
            "angular correction"
        ),
        "sources": {
            build: str(PHASE77 / f"E77_5ac_theta_logderiv_coupling_{build}.json")
            for build in ("zeta", "plant")
        },
        "builds": {},
    }

    for build in ("zeta", "plant"):
        case = load_case(build)
        points = {(p["sigma"], p["step_N"], p["tag"]): p for p in case["points"]}
        rows = []
        max_rel_angle = 0.0
        min_mod_share = None
        for delta in case["deltas"]:
            sigma = delta["sigma"]
            N = delta["N"]
            old = points[(sigma, N, "old")]
            new = points[(sigma, N, "new")]
            u_old = cval(old["u"])
            u_new = cval(new["u"])
            abs_old = abs(u_old)
            abs_new = abs(u_new)
            s_old = u_old.imag / abs_old
            s_new = u_new.imag / abs_new

            modulus_term = 2.0 * (abs_new - abs_old) * s_new
            angular_term = 2.0 * abs_old * (s_new - s_old)
            reconstructed = modulus_term + angular_term
            exact = delta["delta_u_safe"]

            if exact != 0.0:
                rel_angle = abs(angular_term) / abs(exact)
                mod_share = modulus_term / exact
                max_rel_angle = max(max_rel_angle, rel_angle)
                min_mod_share = mod_share if min_mod_share is None else min(min_mod_share, mod_share)
            else:
                rel_angle = None
                mod_share = None

            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "delta_safe_u": exact,
                    "modulus_term": modulus_term,
                    "angular_term": angular_term,
                    "reconstructed_delta": reconstructed,
                    "reconstruction_error": abs(reconstructed - exact),
                    "old_abs_u": abs_old,
                    "new_abs_u": abs_new,
                    "old_im_share": s_old,
                    "new_im_share": s_new,
                    "modulus_share_of_delta": mod_share,
                    "relative_angular_correction": rel_angle,
                }
            )

        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max(r["reconstruction_error"] for r in rows),
            "max_relative_angular_correction": max_rel_angle,
            "min_modulus_share_of_delta": min_mod_share,
        }

    out_path = HERE / "E78_32_delta_safeu_polar_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
