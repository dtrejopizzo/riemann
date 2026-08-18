#!/usr/bin/env python3
"""Split y_h into the a_b u and b_b v branches."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(ROOT))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_011_loewner_identity_probe import symbols  # noqa: E402


PLANTED = ("14.134725141734693790", "0.30", "5.0")


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def vnorm(vec: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vec[j]) ** 2 for j in range(vec.rows)))


def sine_symbol(t: mp.mpf, L: mp.mpf, lam: mp.mpf, planted):
    value = symbols(t, L, lam)[0]
    if planted is None:
        return value
    gamma0, beta, strength = (mp.mpf(x) for x in planted)
    spectral_point = gamma0 - 1j * beta
    planted_sine = mp.quad(lambda y: mp.sin(t * y) * mp.cos(spectral_point * y), [0, L])
    return value + strength * 2 * mp.re(planted_sine)


def run_case(label, planted):
    mp.mp.dps = 50
    lam = mp.mpf(6)
    rows = []
    for n_modes in (6, 8, 10, 12):
        H, idx, L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        inner = idx[1:-1]
        d = [2 * mp.pi * n / L for n in inner]
        D = mp.diag(d)
        db = 2 * mp.pi * idx[-1] / L
        s = mp.matrix([sine_symbol(dj, L, lam, planted) for dj in d])
        one = mp.matrix([1 for _ in d])
        u = mp.lu_solve(A, s)
        v = mp.lu_solve(A, one)
        sb = sine_symbol(db, L, lam, planted)
        Rb = (D - db * mp.eye(D.rows)) ** -1
        g = Rb * (s - sb * one)
        p = (v.T * g)[0]
        q = (u.T * g)[0]
        aa = 2 / L + 4 * p / L**2
        bb = -2 * sb / L - 4 * q / L**2
        y_u = mp.lu_solve(A, aa * u)
        y_v = mp.lu_solve(A, bb * v)
        y_h = y_u + y_v
        rows.append(
            {
                "N": n_modes,
                "au_norm": serialize(vnorm(aa * u)),
                "bv_norm": serialize(vnorm(bb * v)),
                "y_u_norm": serialize(vnorm(y_u)),
                "y_v_norm": serialize(vnorm(y_v)),
                "y_h_norm": serialize(vnorm(y_h)),
                "y_v_over_y_h": serialize(vnorm(y_v) / vnorm(y_h)),
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.106 h-source v-branch dominance audit",
        "date": "2026-07-19",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
    }
    out_path = Path(__file__).with_name("E78_106_h_source_v_dominance_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
