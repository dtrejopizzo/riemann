#!/usr/bin/env python3
"""E77.5ab scaling diagnostics for the Schur anchor denominator."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_cases(paths):
    cases = []
    for path in paths:
        data = json.loads(path.read_text(encoding="ascii"))
        cases.extend(data["cases"])
    return cases


def local_slope(a, b, field):
    xa = abs(a[field])
    xb = abs(b[field])
    if xa == 0 or xb == 0:
        return None
    return math.log(xb / xa) / math.log(b["N"] / a["N"])


def analyse_case(case):
    rows = []
    for row in case["qrows"]:
        denom = row["one_minus_theta_abs_new"]
        rows.append(
            {
                "sigma": row["sigma"],
                "N": row["N"],
                "mod4": row["mod4"],
                "denom_abs": denom,
                "N_denom_abs": row["N"] * denom,
                "N2_denom_abs": row["N"] * row["N"] * denom,
                "Q_theta": row["Q_theta"],
                "Q_logT": row["Q_logT_reconstructed"],
                "theta_share": row["Q_theta"] / row["Q_logT_reconstructed"]
                if row["Q_logT_reconstructed"]
                else float("inf"),
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
                        "denom_power_slope": local_slope(prev, cur, "denom_abs"),
                        "Qtheta_power_slope": local_slope(prev, cur, "Q_theta"),
                        "delta_theta_share": cur["theta_share"] - prev["theta_share"],
                    }
                )
            profiles.append(
                {
                    "sigma": sigma,
                    "mod4": mod4,
                    "denom_first": br[0]["denom_abs"],
                    "denom_last": br[-1]["denom_abs"],
                    "N_denom_first": br[0]["N_denom_abs"],
                    "N_denom_last": br[-1]["N_denom_abs"],
                    "denom_range": max(r["denom_abs"] for r in br) - min(r["denom_abs"] for r in br),
                    "theta_share_first": br[0]["theta_share"],
                    "theta_share_last": br[-1]["theta_share"],
                    "rows": br,
                    "steps": steps,
                }
            )
    return rows, profiles


def run(paths):
    result = {"statement": "Anchor denominator magnitude scaling", "sources": [str(p) for p in paths], "cases": []}
    for case in load_cases(paths):
        rows, profiles = analyse_case(case)
        result["cases"].append({"label": case["label"], "rows": rows, "profiles": profiles})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputs",
        type=Path,
        nargs="+",
        default=[
            HERE / "E77_5aa_schur_logt_functional_zeta.json",
            HERE / "E77_5aa_schur_logt_functional_plant.json",
        ],
    )
    parser.add_argument("--output", type=Path, default=HERE / "E77_5ab_anchor_denominator_law_results.json")
    args = parser.parse_args()
    result = run(args.inputs)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for prof in case["profiles"]:
            print(
                f"SIGMA {prof['sigma']} mod{prof['mod4']} "
                f"den={prof['denom_first']:.6g}->{prof['denom_last']:.6g} "
                f"Nden={prof['N_denom_first']:.6g}->{prof['N_denom_last']:.6g} "
                f"share={prof['theta_share_first']:.6g}->{prof['theta_share_last']:.6g}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
