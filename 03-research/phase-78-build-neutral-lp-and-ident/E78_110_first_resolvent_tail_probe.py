#!/usr/bin/env python3
"""Audit the first-resolvent tail gate for A^{-2}1."""

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

        coeff0 = (vecs[:, 0].T * one)[0]
        ground1 = coeff0 / vals[0] * vecs[:, 0]
        res1 = mp.lu_solve(A, one)
        off1 = res1 - ground1

        ground2 = coeff0 / (vals[0] ** 2) * vecs[:, 0]
        res2 = mp.lu_solve(A, res1)
        tail2 = res2 - ground2

        ratio1 = vnorm(off1) / max(vnorm(ground1), mp.mpf("1e-80"))
        ratio2 = vnorm(tail2) / max(vnorm(ground2), mp.mpf("1e-80"))
        certificate = abs(vals[0] / vals[1]) * ratio1

        rows.append(
            {
                "N": n_modes,
                "nu0": serialize(vals[0]),
                "nu1": serialize(vals[1]),
                "gap_factor_abs_nu0_over_nu1": serialize(abs(vals[0] / vals[1])),
                "first_resolvent_offground_ratio": serialize(ratio1),
                "second_resolvent_tail_ratio": serialize(ratio2),
                "certificate_bound": serialize(certificate),
                "certificate_over_actual": serialize(certificate / max(ratio2, mp.mpf('1e-80'))),
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.110 first-resolvent tail gate audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "bound": "||tail(A^-2 1)|| / ||ground(A^-2 1)|| <= |nu0/nu1| * ||off(A^-1 1)|| / ||ground(A^-1 1)||",
    }
    out_path = Path(__file__).with_name("E78_110_first_resolvent_tail_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
