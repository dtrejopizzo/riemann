#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"


def load_json(name: str):
    return json.loads((PHASE77 / name).read_text())


def main():
    qdata = load_json("E77_5y_q_functional_identity_results.json")
    result = {
        "statement": (
            "Audit of balanced-denominator geometry for "
            "|Q_ext| + |Q_logT| through the ratio |Q_logT|/|Q_ext|"
        ),
        "source": str(PHASE77 / "E77_5y_q_functional_identity_results.json"),
        "builds": {},
    }

    for case in qdata["cases"]:
        label = case["label"]
        rows = []
        for row in case["rows"]:
            q_ext = abs(row["Q_external_component"])
            q_log = abs(row["Q_logt_component"])
            ratio = q_log / q_ext if q_ext else None
            denom = q_ext + q_log
            rows.append(
                {
                    "sigma": row["sigma"],
                    "N": row["N"],
                    "mod4": row["mod4"],
                    "abs_Q_ext": q_ext,
                    "abs_Q_logT": q_log,
                    "ratio_logt_over_ext": ratio,
                    "denominator": denom,
                    "denominator_over_ext": denom / q_ext if q_ext else None,
                    "denominator_over_logt": denom / q_log if q_log else None,
                    "logt_cancel": abs(row["Q_reference"]) / denom,
                }
            )
        summary = {}
        for sigma in sorted({r["sigma"] for r in rows}, key=float):
            bucket = [r for r in rows if r["sigma"] == sigma]
            summary[sigma] = {
                "min_ratio_logt_over_ext": min(r["ratio_logt_over_ext"] for r in bucket),
                "max_ratio_logt_over_ext": max(r["ratio_logt_over_ext"] for r in bucket),
                "min_denom_over_ext": min(r["denominator_over_ext"] for r in bucket),
                "max_denom_over_ext": max(r["denominator_over_ext"] for r in bucket),
                "min_denom_over_logt": min(r["denominator_over_logt"] for r in bucket),
                "max_denom_over_logt": max(r["denominator_over_logt"] for r in bucket),
            }
        result["builds"][label] = {"rows": rows, "summary_by_sigma": summary}

    out_path = HERE / "E78_20_balanced_denominator_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
