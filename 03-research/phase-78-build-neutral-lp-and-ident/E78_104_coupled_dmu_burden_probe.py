#!/usr/bin/env python3
"""Localize the coupled d_mu burden among F_b, c_b, and y_b."""

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
SIGMAS = [mp.mpf("0.6"), mp.mpf("1.0"), mp.mpf("2.0")]


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
        y = mp.lu_solve(A, h + alpha * s + beta * one)
        h_bd = mp.fsum(h[j] / (d[j] - db) for j in range(len(d)))
        y_bd = mp.fsum(y[j] / (d[j] - db) for j in range(len(d)))
        min_abs_F = mp.inf
        max_abs_Fp = mp.mpf("0")
        max_abs_Y = mp.mpf("0")
        max_abs_Yp = mp.mpf("0")
        max_abs_Fmu = mp.mpf("0")
        for sigma in SIGMAS:
            z = 1j * sigma
            Hc = mp.fsum(h[j] / (z - d[j]) for j in range(len(d)))
            Hcp = mp.fsum(-h[j] / (z - d[j]) ** 2 for j in range(len(d)))
            Yc = mp.fsum(y[j] / (z - d[j]) for j in range(len(d)))
            Ycp = mp.fsum(-y[j] / (z - d[j]) ** 2 for j in range(len(d)))
            F = 1 + Hc + h_bd
            Fmu = Yc + y_bd
            min_abs_F = min(min_abs_F, abs(F))
            max_abs_Fp = max(max_abs_Fp, abs(Hcp))
            max_abs_Y = max(max_abs_Y, abs(Yc))
            max_abs_Yp = max(max_abs_Yp, abs(Ycp))
            max_abs_Fmu = max(max_abs_Fmu, abs(Fmu))
        rows.append(
            {
                "N": n_modes,
                "min_abs_F": serialize(min_abs_F),
                "max_abs_Fp": serialize(max_abs_Fp),
                "c_norm": serialize(vnorm(c)),
                "h_norm": serialize(vnorm(h)),
                "y_norm": serialize(vnorm(y)),
                "max_abs_Y": serialize(max_abs_Y),
                "max_abs_Yp": serialize(max_abs_Yp),
                "max_abs_Fmu": serialize(max_abs_Fmu),
                "alpha_abs": serialize(abs(alpha)),
                "beta_abs": serialize(abs(beta)),
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.104 coupled d_mu burden localization",
        "date": "2026-07-19",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
    }
    out_path = Path(__file__).with_name("E78_104_coupled_dmu_burden_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
