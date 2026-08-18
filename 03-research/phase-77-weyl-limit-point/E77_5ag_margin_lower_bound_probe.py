#!/usr/bin/env python3
"""E77.5ag lower-bound gate for normalized sector margin."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def cval(z):
    return complex(float(z["re"]), float(z["im"]))


def margin(u):
    den = abs(u) ** 2
    if den == 0:
        return float("inf")
    return (u.imag * u.imag - u.real * u.real) / den


def rows_from_case(case, threshold):
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
        m = margin(u)
        rows.append(
            {
                "sigma": p["sigma"],
                "N": p["step_N"],
                "mod4": p["step_N"] % 4,
                "margin": m,
                "margin_minus_threshold": m - threshold,
                "passes_threshold": m >= threshold,
                "u_re": u.real,
                "u_im": u.imag,
            }
        )
    return sorted(rows, key=lambda r: (float(r["sigma"]), r["N"]))


def load_all(paths, threshold):
    out = []
    for path in paths:
        data = json.loads(path.read_text(encoding="ascii"))
        for case in data["cases"]:
            rows = rows_from_case(case, threshold)
            failures = [r for r in rows if not r["passes_threshold"]]
            worst = min(rows, key=lambda r: r["margin"]) if rows else None
            out.append(
                {
                    "label": case["label"],
                    "source": str(path),
                    "threshold": threshold,
                    "all_pass": not failures,
                    "first_failure": failures[0] if failures else None,
                    "worst_row": worst,
                    "rows": rows,
                }
            )
    return out


def run(paths, threshold):
    return {
        "statement": "M_N >= threshold lower-bound gate",
        "threshold": threshold,
        "cases": load_all(paths, threshold),
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
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--output", type=Path, default=HERE / "E77_5ag_margin_lower_bound_results.json")
    args = parser.parse_args()
    result = run(args.inputs, args.threshold)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        w = case["worst_row"]
        status = "PASS" if case["all_pass"] else "FAIL"
        print(
            f"CASE {case['label']} {status} worst sigma={w['sigma']} N={w['N']} "
            f"mod{w['mod4']} margin={w['margin']:.9g} margin-th={w['margin_minus_threshold']:.9g}",
            flush=True,
        )
        if case["first_failure"]:
            f = case["first_failure"]
            print(
                f"FIRST_FAIL sigma={f['sigma']} N={f['N']} mod{f['mod4']} margin={f['margin']:.9g}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
