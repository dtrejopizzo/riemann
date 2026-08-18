#!/usr/bin/env python3
"""Audit whether SOURCE-PAIR-ANGLE is governed by the mode-2 Cauchy amplitude."""

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


def vnorm(v: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def run_case(label, planted):
    mp.mp.dps = 50
    rows = []
    for n_modes in (8, 12):
        H, idx, L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        vals, vecs = mp.eigsy(A)
        d = [2 * mp.pi * n / L for n in idx[1:-1]]
        one = mp.matrix([1 for _ in d])
        coeff0 = (vecs[:, 0].T * one)[0]
        off1 = mp.lu_solve(A, one) - coeff0 / vals[0] * vecs[:, 0]
        off1_norm = vnorm(off1)
        omega2_ratio = abs((vecs[:, 2].T * off1)[0]) / off1_norm
        point_rows = []
        for z in POINTS:
            r = mp.matrix([1 / (z - dj) for dj in d])
            rcoeff0 = (vecs[:, 0].T * r)[0]
            g = mp.lu_solve(A, r) - rcoeff0 / vals[0] * vecs[:, 0]
            g_norm = vnorm(g)
            gamma2_ratio = abs((vecs[:, 2].T * g)[0]) / g_norm
            pair = (g.T * off1)[0]
            angle = abs(pair) / (g_norm * off1_norm)
            point_rows.append(
                {
                    "z": serialize(z),
                    "mode2_cauchy_ratio": serialize(gamma2_ratio),
                    "mode2_source_ratio": serialize(omega2_ratio),
                    "angle": serialize(angle),
                    "mode2_product": serialize(gamma2_ratio * omega2_ratio),
                }
            )
        rows.append({"N": n_modes, "points": point_rows})
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.120 mode-2 Cauchy amplitude audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "quantity": "angle ~= (mode-2 fraction of g_z) * (mode-2 fraction of off_1)",
    }
    out_path = Path(__file__).with_name("E78_120_mode2_cauchy_amplitude_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
