#!/usr/bin/env python3
"""Audit the geometric certificate for the Cauchy-side first resolvent."""

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
        gap = abs(vals[0] / vals[1])
        point_rows = []
        for z in POINTS:
            b = mp.matrix([1 / (z - dj) for dj in d])
            coeff0 = (vecs[:, 0].T * b)[0]
            ground = coeff0 / vals[0] * vecs[:, 0]
            off = mp.lu_solve(A, b) - ground
            ratio = vnorm(off) / max(vnorm(ground), mp.mpf("1e-80"))
            geom = vnorm(b - coeff0 * vecs[:, 0]) / max(abs(coeff0), mp.mpf("1e-80"))
            cert = gap * geom
            point_rows.append(
                {
                    "z": serialize(z),
                    "first_resolvent_offground_ratio": serialize(ratio),
                    "geometric_ratio": serialize(geom),
                    "certificate_bound": serialize(cert),
                    "certificate_over_actual": serialize(cert / max(ratio, mp.mpf("1e-80"))),
                    "overlap_abs": serialize(abs(coeff0)),
                }
            )
        rows.append(
            {
                "N": n_modes,
                "gap_factor_abs_nu0_over_nu1": serialize(gap),
                "points": point_rows,
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.112 Cauchy-side first-resolvent geometric certificate audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "bound": "||(I-P0)A^-1 b|| / ||P0 A^-1 b|| <= |nu0/nu1| * ||(I-P0)b|| / |<v0,b>|",
    }
    out_path = Path(__file__).with_name("E78_112_cauchy_first_resolvent_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
