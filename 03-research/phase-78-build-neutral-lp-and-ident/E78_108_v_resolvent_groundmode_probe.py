#!/usr/bin/env python3
"""Audit whether A^{-2}1 is ground-mode dominated."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(ROOT))

from P76_002_mp_entry_audit import build_mp  # noqa: E402


PLANTED = ("14.134725141734693790", "0.30", "5.0")


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def vnorm(vec: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vec[j]) ** 2 for j in range(vec.rows)))


def run_case(label, planted):
    mp.mp.dps = 50
    rows = []
    for n_modes in (6, 8, 10, 12):
        H, idx, _L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        vals, vecs = mp.eigsy(A)
        one = mp.matrix([1 for _ in range(A.rows)])
        resolvent = mp.lu_solve(A, mp.lu_solve(A, one))
        total = vnorm(resolvent)
        proj0 = abs((vecs[:, 0].T * resolvent)[0]) / total
        proj01 = mp.sqrt(
            abs((vecs[:, 0].T * resolvent)[0]) ** 2 + abs((vecs[:, 1].T * resolvent)[0]) ** 2
        ) / total
        mode0 = abs((vecs[:, 0].T * one)[0]) / (vals[0] ** 2)
        mode1 = abs((vecs[:, 1].T * one)[0]) / (vals[1] ** 2)
        rows.append(
            {
                "N": n_modes,
                "Ainv2_one_norm": serialize(total),
                "mode0_scalar": serialize(mode0),
                "mode1_scalar": serialize(mode1),
                "proj0": serialize(proj0),
                "proj01": serialize(proj01),
                "gap_ratio_nu1_over_nu0": serialize(vals[1] / vals[0]),
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.108 v-resolvent ground-mode dominance audit",
        "date": "2026-07-19",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
    }
    out_path = Path(__file__).with_name("E78_108_v_resolvent_groundmode_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
