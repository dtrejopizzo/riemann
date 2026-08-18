#!/usr/bin/env python3
"""E79.96 - Derived audit of the rank-one escape normalization.

This probe reads existing certified JSON artifacts only.  It does not rebuild
any matrix data.  It checks three things:

1. escape_ratio = escape_scale / mesh_radius exactly on the E79.90 ladder;
2. the E78.155 rank-one predictor kappa_hat = qTx/c + mean(d) differs from
   escape_scale only by the normalized mean(d) shift;
3. that shift is tiny for zeta and order-one for the planted main control.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name: str):
    return json.loads((HERE / name).read_text())


def main():
    res90 = load("E79_90_escape_balance_split_results.json")
    res91 = load("E79_91_escape_denominator_results.json")

    report = {
        "statement": "E79.96 rank-one escape normalization audit",
        "sources": [
            "E79_90_escape_balance_split_results.json",
            "E79_91_escape_denominator_results.json",
        ],
        "cases": [],
    }

    for case90, case91 in zip(res90["cases"], res91["cases"]):
        rows = []
        max_identity_err = 0.0
        max_shift_rel = 0.0
        min_shift_rel = None
        for row90, row91 in zip(case90["rows"], case91["rows"]):
            n = int(row90["N"])
            escape_scale = float(row90["escape_scale"])
            mesh_radius = float(row90["mesh_radius"])
            escape_ratio = float(row90["escape_ratio"])
            abs_qtx = float(row91["abs_qTx"])
            abs_c = float(row91["abs_c"])
            mean_d = (n - 1) * math.pi / 6.0
            kappa_hat = abs_qtx / abs_c + mean_d
            identity_err = abs(escape_ratio - escape_scale / mesh_radius)
            shift_rel = mean_d / escape_scale
            khat_rel_gap = kappa_hat / escape_scale - 1.0

            max_identity_err = max(max_identity_err, identity_err)
            max_shift_rel = max(max_shift_rel, shift_rel)
            min_shift_rel = shift_rel if min_shift_rel is None else min(min_shift_rel, shift_rel)

            rows.append(
                {
                    "N": n,
                    "escape_ratio": row90["escape_ratio"],
                    "escape_scale_over_mesh": f"{escape_scale / mesh_radius:.15g}",
                    "identity_error": f"{identity_err:.3e}",
                    "mean_d_over_escape_scale": f"{shift_rel:.15g}",
                    "kappa_hat_over_mesh": f"{kappa_hat / mesh_radius:.15g}",
                    "kappa_hat_relative_gap_vs_escape_ratio": f"{khat_rel_gap:.15g}",
                }
            )

        report["cases"].append(
            {
                "label": case90["label"],
                "rows": rows,
                "summary": {
                    "max_identity_error": f"{max_identity_err:.3e}",
                    "min_mean_d_over_escape_scale": f"{min_shift_rel:.15g}",
                    "max_mean_d_over_escape_scale": f"{max_shift_rel:.15g}",
                },
            }
        )

    out = HERE / "E79_96_rank_one_escape_normalization_results.json"
    out.write_text(json.dumps(report, indent=2))
    print(out)


if __name__ == "__main__":
    main()
