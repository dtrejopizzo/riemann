#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"


def load_json(name: str):
    return json.loads((PHASE77 / name).read_text())


def build_rows():
    qdata = load_json("E77_5y_q_functional_identity_results.json")
    out = {}
    for case in qdata["cases"]:
        rows = []
        for row in case["rows"]:
            q_ref = row["Q_reference"]
            q_ext = row["Q_external_component"]
            q_logt = row["Q_logt_component"]
            c_n = row["C_N"]
            c_np2 = row["C_N_plus_2"]
            d_c = c_n - c_np2
            denom = abs(q_ext) + abs(q_logt)
            logt_cancel = abs(q_ref) / denom
            reconstructed_q = (row["N"] ** 2) * d_c
            rows.append(
                {
                    "sigma": row["sigma"],
                    "N": row["N"],
                    "mod4": row["mod4"],
                    "R_N": row["R_N"],
                    "R_N_plus_2": row["R_N_plus_2"],
                    "C_N": c_n,
                    "C_N_plus_2": c_np2,
                    "Delta_C": d_c,
                    "abs_Delta_C": abs(d_c),
                    "Q_reference": q_ref,
                    "Q_ext": q_ext,
                    "Q_logT": q_logt,
                    "denominator": denom,
                    "LOGT_CANCEL": logt_cancel,
                    "reconstructed_Q": reconstructed_q,
                    "reconstruction_error": abs(q_ref - reconstructed_q),
                    "curvature_over_denom": abs(d_c) / denom,
                }
            )
        out[case["label"]] = rows
    return out


def summarize(rows):
    out = {}
    for sigma in sorted({row["sigma"] for row in rows}, key=float):
        bucket = [row for row in rows if row["sigma"] == sigma]
        out[sigma] = {
            "min_logt_cancel": min(row["LOGT_CANCEL"] for row in bucket),
            "max_logt_cancel": max(row["LOGT_CANCEL"] for row in bucket),
            "min_abs_Delta_C": min(row["abs_Delta_C"] for row in bucket),
            "max_abs_Delta_C": max(row["abs_Delta_C"] for row in bucket),
            "min_denom": min(row["denominator"] for row in bucket),
            "max_denom": max(row["denominator"] for row in bucket),
        }
    return out


def main():
    builds = build_rows()
    result = {
        "statement": (
            "Exact curvature identity Q_N = N^2 (C_N - C_{N+2}) with "
            "C_N = N R_N and LOGT_CANCEL = |Q_N|/(|Q_ext|+|Q_logT|)"
        ),
        "sources": {
            "q_identity": str(PHASE77 / "E77_5y_q_functional_identity_results.json"),
        },
        "builds": {},
    }
    for label, rows in builds.items():
        result["builds"][label] = {
            "rows": rows,
            "summary_by_sigma": summarize(rows),
            "max_reconstruction_error": max(row["reconstruction_error"] for row in rows),
        }

    out_path = HERE / "E78_19_section_lag_curvature_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
