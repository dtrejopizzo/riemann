#!/usr/bin/env python3
"""Audit the angular loss in the source-offground-norm route."""

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
    rows = []
    for n_modes in (6, 8, 10, 12):
        H, idx, L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        vals, vecs = mp.eigsy(A)
        d = [2 * mp.pi * n / L for n in idx[1:-1]]
        one = mp.matrix([1 for _ in d])
        coeff0 = (vecs[:, 0].T * one)[0]
        off1 = mp.lu_solve(A, one) - coeff0 / vals[0] * vecs[:, 0]
        off1_norm = vnorm(off1)
        point_rows = []
        for z in POINTS:
            r = mp.matrix([1 / (z - dj) for dj in d])
            rcoeff0 = (vecs[:, 0].T * r)[0]
            g = mp.lu_solve(A, r) - rcoeff0 / vals[0] * vecs[:, 0]
            pair = (g.T * off1)[0]
            g_norm = vnorm(g)
            cosine = abs(pair) / (g_norm * off1_norm)
            point_rows.append(
                {
                    "z": serialize(z),
                    "pair_abs": serialize(abs(pair)),
                    "cauchy_norm": serialize(g_norm),
                    "source_norm": serialize(off1_norm),
                    "normalized_correlation": serialize(cosine),
                }
            )
        rows.append({"N": n_modes, "points": point_rows})
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.116 source angle autopsy audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "quantity": "cos_N(z) = |<g_z,off_1>| / (||g_z|| ||off_1||)",
    }
    out_path = Path(__file__).with_name("E78_116_source_angle_autopsy_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
