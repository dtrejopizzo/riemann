#!/usr/bin/env python3
"""Audit the exact mode-2 overlap identity for the Cauchy amplitude."""

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


def run_case(label, planted):
    mp.mp.dps = 50
    rows = []
    for n_modes in (8, 12):
        H, idx, L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        vals, vecs = mp.eigsy(A)
        d = [2 * mp.pi * n / L for n in idx[1:-1]]
        point_rows = []
        for z in POINTS:
            r = mp.matrix([1 / (z - dj) for dj in d])
            rcoeff0 = (vecs[:, 0].T * r)[0]
            g = mp.lu_solve(A, r) - rcoeff0 / vals[0] * vecs[:, 0]
            gamma2 = (vecs[:, 2].T * g)[0]
            overlap = (vecs[:, 2].T * r)[0] / vals[2]
            point_rows.append(
                {
                    "z": serialize(z),
                    "rel_identity_error": serialize(abs(gamma2 - overlap) / max(1, abs(gamma2))),
                    "gamma2_abs": serialize(abs(gamma2)),
                    "v2_overlap_abs": serialize(abs((vecs[:, 2].T * r)[0])),
                    "nu2_abs": serialize(abs(vals[2])),
                }
            )
        rows.append({"N": n_modes, "points": point_rows})
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.121 mode-2 overlap identity audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "identity": "gamma_2(z) = <v_2,r_z> / nu_2",
    }
    out_path = Path(__file__).with_name("E78_121_mode2_overlap_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
