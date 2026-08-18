#!/usr/bin/env python3
"""Audit the paired first-resolvent gate for the second-resolvent tail."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(ROOT))

from P76_002_mp_entry_audit import build_mp  # noqa: E402


PLANTED = ("14.134725141734693790", "0.30", "5.0")
POINTS = [mp.mpc(0, "0.6"), mp.mpc(0, "1.0"), mp.mpc(0, "2.0")]


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def vnorm(vec: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vec[j]) ** 2 for j in range(vec.rows)))


def run_case(label, planted):
    mp.mp.dps = 50
    H, idx, L = build_mp(6, 8, 50, planted=planted)
    A = H[1:-1, 1:-1]
    vals, vecs = mp.eigsy(A)
    d = [2 * mp.pi * n / L for n in idx[1:-1]]
    one = mp.matrix([1 for _ in d])
    coeff0 = (vecs[:, 0].T * one)[0]
    ground1 = coeff0 / vals[0] * vecs[:, 0]
    off1 = mp.lu_solve(A, one) - ground1
    ground2 = coeff0 / (vals[0] ** 2) * vecs[:, 0]
    tail2 = mp.lu_solve(A, mp.lu_solve(A, one)) - ground2
    rows = []
    for z in POINTS:
        r = mp.matrix([1 / (z - dj) for dj in d])
        rcoeff0 = (vecs[:, 0].T * r)[0]
        rground1 = rcoeff0 / vals[0] * vecs[:, 0]
        roff1 = mp.lu_solve(A, r) - rground1
        lhs = (r.T * tail2)[0]
        rhs = (roff1.T * off1)[0]
        rows.append(
            {
                "z": serialize(z),
                "pair_tail_abs": serialize(abs(lhs)),
                "identity_rel_error": serialize(abs(lhs - rhs) / max(1, abs(lhs))),
                "paired_cauchy_bound": serialize(vnorm(roff1) * vnorm(off1)),
                "cauchy_first_resolvent_offground_ratio": serialize(
                    vnorm(roff1) / max(vnorm(rground1), mp.mpf("1e-80"))
                ),
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.111 paired first-resolvent gate audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "identity": "<r, (I-P0)A^-2 1> = <(I-P0)A^-1 r, (I-P0)A^-1 1>",
    }
    out_path = Path(__file__).with_name("E78_111_paired_first_resolvent_gate_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
