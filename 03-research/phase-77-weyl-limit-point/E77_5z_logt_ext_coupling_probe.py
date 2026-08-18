#!/usr/bin/env python3
"""E77.5z signed Q_logT/Q_ext coupling diagnostics."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def slope(prev, cur, field):
    a = abs(prev[field])
    b = abs(cur[field])
    if a == 0 or b == 0:
        return None
    return math.log(b / a) / math.log(cur["N"] / prev["N"])


def analyse_case(case):
    rows = []
    for row in case["rows"]:
        qext = row["Q_external_component"]
        qlog = row["Q_logt_component"]
        q = row["Q_reference"]
        rows.append(
            {
                **row,
                "A_log_over_ext": qlog / qext if qext else float("inf"),
                "defect_over_ext": q / qext if qext else float("inf"),
                "abs_defect_over_ext": abs(q / qext) if qext else float("inf"),
            }
        )
    profiles = []
    for sigma in sorted({r["sigma"] for r in rows}, key=float):
        srows = [r for r in rows if r["sigma"] == sigma]
        for mod4 in [0, 2]:
            br = sorted([r for r in srows if r["mod4"] == mod4], key=lambda r: r["N"])
            if not br:
                continue
            a_vals = [r["A_log_over_ext"] for r in br]
            defect_vals = [r["defect_over_ext"] for r in br]
            steps = []
            for prev, cur in zip(br, br[1:]):
                steps.append(
                    {
                        "from_N": prev["N"],
                        "to_N": cur["N"],
                        "delta_A": cur["A_log_over_ext"] - prev["A_log_over_ext"],
                        "delta_defect_over_ext": cur["defect_over_ext"] - prev["defect_over_ext"],
                        "defect_slope": slope(prev, cur, "abs_defect_over_ext"),
                    }
                )
            profiles.append(
                {
                    "sigma": sigma,
                    "mod4": mod4,
                    "A_first": a_vals[0],
                    "A_last": a_vals[-1],
                    "A_range": max(a_vals) - min(a_vals),
                    "defect_first": defect_vals[0],
                    "defect_last": defect_vals[-1],
                    "defect_range": max(defect_vals) - min(defect_vals),
                    "max_abs_defect_over_ext": max(abs(x) for x in defect_vals),
                    "rows": [
                        {
                            "N": r["N"],
                            "Q": r["Q_reference"],
                            "Q_ext": r["Q_external_component"],
                            "Q_logT": r["Q_logt_component"],
                            "A": r["A_log_over_ext"],
                            "defect_over_ext": r["defect_over_ext"],
                        }
                        for r in br
                    ],
                    "steps": steps,
                }
            )
    return rows, profiles


def run(input_path):
    data = json.loads(input_path.read_text(encoding="ascii"))
    result = {
        "statement": "Signed log-transfer/external coupling profiles",
        "source": str(input_path),
        "cases": [],
    }
    for case in data["cases"]:
        rows, profiles = analyse_case(case)
        result["cases"].append({"label": case["label"], "rows": rows, "profiles": profiles})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=HERE / "E77_5y_q_functional_identity_results.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5z_logt_ext_coupling_results.json")
    args = parser.parse_args()
    result = run(args.input)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for prof in case["profiles"]:
            if prof["sigma"] in {"1.0", "3.0"}:
                print(
                    f"SIGMA {prof['sigma']} mod{prof['mod4']} "
                    f"A {prof['A_first']:.6g}->{prof['A_last']:.6g} "
                    f"Arange={prof['A_range']:.6g} "
                    f"def {prof['defect_first']:.6g}->{prof['defect_last']:.6g} "
                    f"maxAbsDef={prof['max_abs_defect_over_ext']:.6g}",
                    flush=True,
                )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
