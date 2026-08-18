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
            "Audit of sign-coherent balance: when Q_ext and Q_logT have the same sign, "
            "|Q_ext-Q_logT|/|Q_ext| = |1 - |Q_logT|/|Q_ext||"
        ),
        "source": str(PHASE77 / "E77_5y_q_functional_identity_results.json"),
        "builds": {},
    }

    for case in qdata["cases"]:
        rows = []
        for row in case["rows"]:
            q_ext = row["Q_external_component"]
            q_log = row["Q_logt_component"]
            q_ref = row["Q_reference"]
            ratio = abs(q_log) / abs(q_ext) if q_ext else None
            same_sign = (q_ext == 0) or (q_log == 0) or ((q_ext > 0) == (q_log > 0))
            defect_over_ext = abs(q_ref) / abs(q_ext) if q_ext else None
            coherent_reconstruction = abs(1 - ratio) if ratio is not None else None
            rows.append(
                {
                    "sigma": row["sigma"],
                    "N": row["N"],
                    "mod4": row["mod4"],
                    "Q_ext": q_ext,
                    "Q_logT": q_log,
                    "Q_reference": q_ref,
                    "same_sign": same_sign,
                    "ratio_abs_logt_over_ext": ratio,
                    "defect_over_ext": defect_over_ext,
                    "coherent_reconstruction": coherent_reconstruction,
                    "coherent_reconstruction_error": (
                        abs(defect_over_ext - coherent_reconstruction)
                        if same_sign and defect_over_ext is not None and coherent_reconstruction is not None
                        else None
                    ),
                }
            )
        result["builds"][case["label"]] = {
            "rows": rows,
            "same_sign_count": sum(1 for r in rows if r["same_sign"]),
            "opposite_sign_count": sum(1 for r in rows if not r["same_sign"]),
            "max_coherent_reconstruction_error": max(
                (
                    r["coherent_reconstruction_error"]
                    for r in rows
                    if r["coherent_reconstruction_error"] is not None
                ),
                default=0.0,
            ),
        }

    out_path = HERE / "E78_21_sign_coherent_balance_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
