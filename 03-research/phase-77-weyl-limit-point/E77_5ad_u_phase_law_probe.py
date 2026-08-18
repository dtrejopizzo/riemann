#!/usr/bin/env python3
"""E77.5ad sector diagnostics for u=-theta'/(1-theta)."""

from __future__ import annotations

import argparse
import json
import math
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


def point_index(case):
    out = {}
    for p in case["points"]:
        if p["tag"] == "new":
            out[(p["sigma"], p["step_N"])] = p
    return out


def analyse_case(case):
    points = point_index(case)
    rows = []
    for q in case["qrows"]:
        p = points[(q["sigma"], q["N"])]
        u = cval(p["u"])
        abs_u = abs(u)
        im_share = u.imag / abs_u if abs_u else float("inf")
        re_share = u.real / abs_u if abs_u else float("inf")
        phase_error = float(q["new_u_arg"]) - math.pi / 2 if q["new_u_arg"] is not None else float("nan")
        sector_margin = u.imag - abs(u.real)
        vertical_model = -2 * abs_u
        safe_u = float(p["safe_u"])
        rows.append(
            {
                "sigma": q["sigma"],
                "N": q["N"],
                "mod4": q["mod4"],
                "u_re": u.real,
                "u_im": u.imag,
                "u_abs": abs_u,
                "arg_minus_pi_over_2": phase_error,
                "im_share": im_share,
                "re_share": re_share,
                "sector_margin": sector_margin,
                "safe_u": safe_u,
                "signed_vertical_model_safe_u": vertical_model,
                "signed_vertical_model_rel_error": abs(vertical_model - safe_u) / max(1e-300, abs(safe_u)),
                "Q_theta": q["Q_theta"],
            }
        )
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
                    "min_sector_margin": min(r["sector_margin"] for r in br),
                    "max_abs_phase_error": max(abs(r["arg_minus_pi_over_2"]) for r in br),
                    "min_im_share": min(r["im_share"] for r in br),
                    "max_signed_vertical_model_rel_error": max(r["signed_vertical_model_rel_error"] for r in br),
                    "rows": br,
                }
            )
    return {"label": case["label"], "rows": rows, "profiles": profiles}


def run(paths):
    return {
        "statement": "U phase sector law diagnostics",
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
            HERE / "E77_5ac_theta_logderiv_coupling_zeta.json",
            HERE / "E77_5ac_theta_logderiv_coupling_plant.json",
        ],
    )
    parser.add_argument("--output", type=Path, default=HERE / "E77_5ad_u_phase_law_results.json")
    args = parser.parse_args()
    result = run(args.inputs)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for prof in case["profiles"]:
            print(
                f"SIGMA {prof['sigma']} mod{prof['mod4']} "
                f"minMargin={prof['min_sector_margin']:.9g} "
                f"maxPhaseErr={prof['max_abs_phase_error']:.9g} "
                f"minImShare={prof['min_im_share']:.9g} "
                f"maxVertErr={prof['max_signed_vertical_model_rel_error']:.9g}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
