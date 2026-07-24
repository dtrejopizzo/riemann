#!/usr/bin/env python3
"""Split y_b into intrinsic h-source and scalar alpha/beta source."""

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
        c = mp.lu_solve(A, g)
        p = (v.T * g)[0]
        q = (u.T * g)[0]
        aa = 2 / L + 4 * p / L**2
        bb = -2 * sb / L - 4 * q / L**2
        alpha = 4 * (v.T * c)[0] / L**2
        beta = -4 * (u.T * c)[0] / L**2
        h = aa * u + bb * v
        src_ab = alpha * s + beta * one
        y_h = mp.lu_solve(A, h)
        y_ab = mp.lu_solve(A, src_ab)
        y = y_h + y_ab
        rows.append(
            {
                "N": n_modes,
                "h_norm": serialize(vnorm(h)),
                "src_ab_norm": serialize(vnorm(src_ab)),
                "y_h_norm": serialize(vnorm(y_h)),
                "y_ab_norm": serialize(vnorm(y_ab)),
                "y_norm": serialize(vnorm(y)),
                "y_ab_over_y": serialize(vnorm(y_ab) / vnorm(y)),
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.105 y-source split audit",
        "date": "2026-07-19",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
    }
    out_path = Path(__file__).with_name("E78_105_y_source_split_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
