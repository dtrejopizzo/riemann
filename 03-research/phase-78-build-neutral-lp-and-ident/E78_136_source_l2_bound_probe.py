#!/usr/bin/env python3
"""Audit the l2-kernel reduction for SAFE-Y-BOUND using existing burden data."""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "E78_104_coupled_dmu_burden_results.json"


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def kernel_constants(L: mp.mpf, sigma_min: mp.mpf, n_terms: int = 400):
    def mesh(n):
        return 2 * mp.pi * n / L

    c0_sq = (
        1 / (sigma_min**2 + mesh(0) ** 2)
        + mp.fsum([2 / (sigma_min**2 + mesh(n) ** 2) for n in range(1, n_terms + 1)])
    )
    c1_sq = (
        1 / (sigma_min**2 + mesh(0) ** 2) ** 2
        + mp.fsum([2 / (sigma_min**2 + mesh(n) ** 2) ** 2 for n in range(1, n_terms + 1)])
    )
    cb_sq = L**2 / 24
    return mp.sqrt(c0_sq), mp.sqrt(c1_sq), mp.sqrt(cb_sq)


def main():
    mp.mp.dps = 50
    data = json.loads(SOURCE.read_text())
    L = 2 * mp.log(6)
    c_y, c_yp, c_ybd = kernel_constants(L, mp.mpf("0.6"))
    cases = []
    for case in data["cases"]:
        rows = []
        for row in case["rows"]:
            y_norm = mp.mpf(row["y_norm"])
            ratio_y = mp.mpf(row["max_abs_Y"]) / y_norm
            ratio_yp = mp.mpf(row["max_abs_Yp"]) / y_norm
            rows.append(
                {
                    "N": row["N"],
                    "max_abs_Y_over_y_norm": serialize(ratio_y),
                    "max_abs_Yp_over_y_norm": serialize(ratio_yp),
                    "C_Y": serialize(c_y),
                    "C_Yp": serialize(c_yp),
                    "C_Ybd_exact": serialize(c_ybd),
                    "Y_margin": serialize(c_y - ratio_y),
                    "Yp_margin": serialize(c_yp - ratio_yp),
                }
            )
        cases.append({"label": case["label"], "rows": rows})
    result = {
        "statement": "E78.136 source l2 reduction audit",
        "source_results": str(SOURCE),
        "quantity": "uniform l2 kernel constants for Y and Y' on the safe compact, plus exact boundary-kernel constant",
        "cases": cases,
    }
    out_path = HERE / "E78_136_source_l2_bound_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
