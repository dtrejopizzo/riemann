#!/usr/bin/env python3
"""E77.5ah rational numerators for the quadratic u-cone."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def cval(z):
    return complex(float(z["re"]), float(z["im"]))


def load_cases(paths):
    cases = []
    for path in paths:
        data = json.loads(path.read_text(encoding="ascii"))
        cases.extend(data["cases"])
    return cases


def row_from_point(p):
    theta = cval(p["theta"])
    thetap = cval(p["theta_prime"])
    x, y = theta.real, theta.imag
    pp, q = thetap.real, thetap.imag
    a = 1.0 - x
    b = -y
    denom = a * a + b * b
    real_num = pp * a + q * b
    imag_num = pp * b - q * a
    cone_num = imag_num * imag_num - 3.0 * real_num * real_num
    u = cval(p["u"])
    re_recon = -real_num / denom
    im_recon = imag_num / denom
    recon_error = max(abs(re_recon - u.real), abs(im_recon - u.imag)) / max(1.0, abs(u))
    return {
        "sigma": p["sigma"],
        "N": p["step_N"],
        "mod4": p["step_N"] % 4,
        "denom": denom,
        "real_num": real_num,
        "imag_num": imag_num,
        "cone_num": cone_num,
        "imag_num_positive": imag_num > 0,
        "cone_num_positive": cone_num >= 0,
        "reconstruction_error": recon_error,
        "normalized_margin": cone_num / (imag_num * imag_num + real_num * real_num)
        if (imag_num * imag_num + real_num * real_num)
        else float("inf"),
    }


def analyse_case(case):
    rows = []
    seen = set()
    for p in case["points"]:
        if p["tag"] != "new":
            continue
        key = (p["sigma"], p["step_N"])
        if key in seen:
            continue
        seen.add(key)
        rows.append(row_from_point(p))
    profiles = []
    for sigma in sorted({r["sigma"] for r in rows}, key=float):
        for mod4 in [0, 2]:
            br = sorted([r for r in rows if r["sigma"] == sigma and r["mod4"] == mod4], key=lambda r: r["N"])
            if not br:
                continue
            profiles.append(
                {
                    "sigma": sigma,
                    "mod4": mod4,
                    "all_imag_num_positive": all(r["imag_num_positive"] for r in br),
                    "all_cone_num_positive": all(r["cone_num_positive"] for r in br),
                    "min_imag_num": min(r["imag_num"] for r in br),
                    "min_cone_num": min(r["cone_num"] for r in br),
                    "min_normalized_margin": min(r["normalized_margin"] for r in br),
                    "max_reconstruction_error": max(r["reconstruction_error"] for r in br),
                    "rows": br,
                }
            )
    return {"label": case["label"], "rows": rows, "profiles": profiles}


def run(paths):
    return {
        "statement": "Quadratic cone rational numerators for u",
        "sources": [str(p) for p in paths],
        "cases": [analyse_case(case) for case in load_cases(paths)],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputs",
        type=Path,
        nargs="+",
        default=[
            HERE / "E77_5ag_margin_lower_bound_zeta_sigma1_n24.json",
            HERE / "E77_5ac_theta_logderiv_coupling_plant.json",
        ],
    )
    parser.add_argument("--output", type=Path, default=HERE / "E77_5ah_quadratic_cone_certificate_results.json")
    args = parser.parse_args()
    result = run(args.inputs)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for prof in case["profiles"]:
            print(
                f"SIGMA {prof['sigma']} mod{prof['mod4']} "
                f"S+={prof['all_imag_num_positive']} C+={prof['all_cone_num_positive']} "
                f"minS={prof['min_imag_num']:.9g} minC={prof['min_cone_num']:.9g} "
                f"minM={prof['min_normalized_margin']:.9g} "
                f"err={prof['max_reconstruction_error']:.3e}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
