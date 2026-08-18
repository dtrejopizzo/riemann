#!/usr/bin/env python3
"""E77.5ae cone-equivalent sector certificate diagnostics."""

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


def local_power(prev, cur, field):
    a = abs(prev[field])
    b = abs(cur[field])
    if a == 0 or b == 0:
        return None
    return math.log(b / a) / math.log(cur["N"] / prev["N"])


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
        u = cval(p["u"])
        im = u.imag
        re = u.real
        cone = im * im - re * re
        rows.append(
            {
                "sigma": p["sigma"],
                "N": p["step_N"],
                "mod4": p["step_N"] % 4,
                "u_re": re,
                "u_im": im,
                "im_positive": im > 0,
                "cone_numerator": cone,
                "cone_positive": cone > 0,
                "cone_normalized": cone / (abs(u) ** 2) if abs(u) else float("inf"),
                "N2_cone_numerator": p["step_N"] ** 2 * cone,
                "N3_cone_numerator": p["step_N"] ** 3 * cone,
            }
        )
    profiles = []
    for sigma in sorted({r["sigma"] for r in rows}, key=float):
        for mod4 in [0, 2]:
            br = sorted([r for r in rows if r["sigma"] == sigma and r["mod4"] == mod4], key=lambda r: r["N"])
            if not br:
                continue
            steps = []
            for prev, cur in zip(br, br[1:]):
                steps.append(
                    {
                        "from_N": prev["N"],
                        "to_N": cur["N"],
                        "cone_power_slope": local_power(prev, cur, "cone_numerator"),
                        "N2_cone_delta": cur["N2_cone_numerator"] - prev["N2_cone_numerator"],
                        "N3_cone_delta": cur["N3_cone_numerator"] - prev["N3_cone_numerator"],
                    }
                )
            profiles.append(
                {
                    "sigma": sigma,
                    "mod4": mod4,
                    "all_im_positive": all(r["im_positive"] for r in br),
                    "all_cone_positive": all(r["cone_positive"] for r in br),
                    "min_cone_numerator": min(r["cone_numerator"] for r in br),
                    "min_cone_normalized": min(r["cone_normalized"] for r in br),
                    "first_N2_cone": br[0]["N2_cone_numerator"],
                    "last_N2_cone": br[-1]["N2_cone_numerator"],
                    "first_N3_cone": br[0]["N3_cone_numerator"],
                    "last_N3_cone": br[-1]["N3_cone_numerator"],
                    "rows": br,
                    "steps": steps,
                }
            )
    return {"label": case["label"], "rows": rows, "profiles": profiles}


def run(paths):
    return {
        "statement": "Cone certificate Im(u)>0 and Im(u)^2-Re(u)^2>0",
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
    parser.add_argument("--output", type=Path, default=HERE / "E77_5ae_sector_certificate_results.json")
    args = parser.parse_args()
    result = run(args.inputs)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for prof in case["profiles"]:
            print(
                f"SIGMA {prof['sigma']} mod{prof['mod4']} "
                f"im+={prof['all_im_positive']} cone+={prof['all_cone_positive']} "
                f"minCone={prof['min_cone_numerator']:.9g} "
                f"minNorm={prof['min_cone_normalized']:.9g} "
                f"N2={prof['first_N2_cone']:.9g}->{prof['last_N2_cone']:.9g}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
