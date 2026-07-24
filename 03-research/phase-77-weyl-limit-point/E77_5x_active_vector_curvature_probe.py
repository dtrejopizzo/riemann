#!/usr/bin/env python3
"""E77.5x signed curvature diagnostics for active-vector paths."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def c(row):
    return complex(float(row["re"]), float(row["im"]))


def vec(row):
    return [c(z) for z in row["aligned_unit"]]


def dot(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(t, a):
    return [t * x for x in a]


def norm(a):
    return abs(dot(a, a)) ** 0.5


def serial(x):
    return format(float(x), ".17g")


def branch_rows(rows, sigma, mod4):
    return sorted([r for r in rows if r["sigma"] == sigma and r["mod4"] == mod4], key=lambda r: r["N"])


def tangent_records(case):
    out = []
    for sigma in sorted({r["sigma"] for r in case["rows"]}):
        for mod4 in [0, 2]:
            br = branch_rows(case["rows"], sigma, mod4)
            for a, b in zip(br, br[1:]):
                va, vb = vec(a), vec(b)
                t = sub(vb, va)
                out.append(
                    {
                        "kind": "branch_tangent",
                        "sigma": sigma,
                        "mod4": mod4,
                        "from_N": a["N"],
                        "to_N": b["N"],
                        "from_Q": a["Q"],
                        "to_Q": b["Q"],
                        "tangent_norm": serial(norm(t)),
                        "signed_anchor": serial(dot(va, t).imag),
                    }
                )
            for a, b, cc in zip(br, br[1:], br[2:]):
                va, vb, vc = vec(a), vec(b), vec(cc)
                curv = add(sub(vc, scale(2, vb)), va)
                out.append(
                    {
                        "kind": "branch_second_difference",
                        "sigma": sigma,
                        "mod4": mod4,
                        "from_N": a["N"],
                        "mid_N": b["N"],
                        "to_N": cc["N"],
                        "from_Q": a["Q"],
                        "mid_Q": b["Q"],
                        "to_Q": cc["Q"],
                        "curvature_norm": serial(norm(curv)),
                        "signed_curvature": serial(dot(vb, curv).imag),
                        "q_second_difference": serial(float(cc["Q"]) - 2 * float(b["Q"]) + float(a["Q"])),
                    }
                )
    return out


def cross_defects(case):
    out = []
    by_key = {(r["sigma"], r["N"]): r for r in case["rows"]}
    for sigma in sorted({r["sigma"] for r in case["rows"]}):
        for n in sorted(r["N"] for r in case["rows"] if r["sigma"] == sigma and r["mod4"] == 2):
            left = by_key.get((sigma, n - 2))
            mid = by_key.get((sigma, n))
            right = by_key.get((sigma, n + 2))
            if not (left and mid and right):
                continue
            defect = sub(vec(mid), scale(0.5, add(vec(left), vec(right))))
            out.append(
                {
                    "kind": "cross_mod_midpoint_defect",
                    "sigma": sigma,
                    "N": n,
                    "left_Q": left["Q"],
                    "mid_Q": mid["Q"],
                    "right_Q": right["Q"],
                    "defect_norm": serial(norm(defect)),
                    "signed_defect": serial(dot(vec(mid), defect).imag),
                    "q_midpoint_defect": serial(float(mid["Q"]) - 0.5 * (float(left["Q"]) + float(right["Q"]))),
                }
            )
    return out


def load_case(path):
    data = json.loads(path.read_text(encoding="ascii"))
    return data["cases"][0]


def run(zeta_path, plant_path):
    result = {"statement": "Signed curvature of phase-aligned active-vector paths", "cases": []}
    for path in [zeta_path, plant_path]:
        case = load_case(path)
        diagnostics = tangent_records(case) + cross_defects(case)
        result["cases"].append({"label": case["label"], "diagnostics": diagnostics})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--zeta", type=Path, default=HERE / "E77_5w_complex_active_vector_zeta.json")
    parser.add_argument("--plant", type=Path, default=HERE / "E77_5w_complex_active_vector_plant_n18.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5x_active_vector_curvature_results.json")
    args = parser.parse_args()
    result = run(args.zeta, args.plant)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for d in case["diagnostics"]:
            if d["sigma"] == "3.0":
                print(json.dumps(d), flush=True)
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
