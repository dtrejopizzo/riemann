#!/usr/bin/env python3
"""Verify the exact coupled-generator formula for the mu derivative package."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(ROOT))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_018_boundary_characteristic_probe import transfer  # noqa: E402
from P76_035_safe_log_derivative_probe import transfer_prime  # noqa: E402
from P76_011_loewner_identity_probe import symbols  # noqa: E402


PLANTED = ("14.134725141734693790", "0.30", "5.0")
POINTS = [mp.mpc(0, "0.6"), mp.mpc(0, "1.0"), mp.mpc(0, "2.0")]


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def sine_symbol(t: mp.mpf, L: mp.mpf, lam: mp.mpf, planted):
    value = symbols(t, L, lam)[0]
    if planted is None:
        return value
    gamma0, beta, strength = (mp.mpf(x) for x in planted)
    spectral_point = gamma0 - 1j * beta
    planted_sine = mp.quad(lambda y: mp.sin(t * y) * mp.cos(spectral_point * y), [0, L])
    return value + strength * 2 * mp.re(planted_sine)


def package(H, idx, L, mu, planted):
    lam = mp.mpf(6)
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    inner = idx[1:-1]
    d = [2 * mp.pi * n / L for n in inner]
    D = mp.diag(d)
    db_idx = idx[-1]
    db = 2 * mp.pi * db_idx / L
    s = mp.matrix([sine_symbol(dj, L, lam, planted) for dj in d])
    one = mp.matrix([1 for _ in d])
    u = mp.lu_solve(A, s)
    v = mp.lu_solve(A, one)
    sb = sine_symbol(db, L, lam, planted)
    Rb = (D - db * mp.eye(D.rows)) ** -1
    source = s - sb * one
    g = Rb * source
    c = mp.lu_solve(A, g)
    p = (v.T * g)[0]
    q = (u.T * g)[0]
    aa = 2 / L + 4 * p / L**2
    bb = -2 * sb / L - 4 * q / L**2
    alpha = 4 * (v.T * c)[0] / L**2
    beta = -4 * (u.T * c)[0] / L**2
    h = aa * u + bb * v
    y = mp.lu_solve(A, h + alpha * s + beta * one)
    return {
        "A": A,
        "inner": inner,
        "db_idx": db_idx,
        "db": db,
        "d": d,
        "u": u,
        "v": v,
        "c": c,
        "h": h,
        "y": y,
        "a": aa,
        "b": bb,
        "alpha": alpha,
        "beta": beta,
    }


def cauchy_sum(vec, d, z):
    return mp.fsum(vec[j] / (z - d[j]) for j in range(len(d)))


def cauchy_sum_prime(vec, d, z):
    return mp.fsum(-vec[j] / (z - d[j]) ** 2 for j in range(len(d)))


def generated_derivatives(pkg, z):
    F = 1 + cauchy_sum(pkg["h"], pkg["d"], z) + mp.fsum(
        pkg["h"][j] / (pkg["d"][j] - pkg["db"]) for j in range(len(pkg["d"]))
    )
    Fp = cauchy_sum_prime(pkg["h"], pkg["d"], z)
    Fmu = cauchy_sum(pkg["y"], pkg["d"], z) + mp.fsum(
        pkg["y"][j] / (pkg["d"][j] - pkg["db"]) for j in range(len(pkg["d"]))
    )
    Fpmu = cauchy_sum_prime(pkg["y"], pkg["d"], z)
    T = F / (z - pkg["db"])
    Tp = Fp / (z - pkg["db"]) - F / (z - pkg["db"]) ** 2
    dmuT = Fmu / (z - pkg["db"])
    dmuTp = Fpmu / (z - pkg["db"]) - Fmu / (z - pkg["db"]) ** 2
    dmu_log = Fpmu / F - Fp * Fmu / (F * F)
    return T, Tp, dmuT, dmuTp, dmu_log


def direct_quantities(H, idx, L, mu, z):
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    x = mp.lu_solve(A, b)
    t = transfer(z, idx[-1], idx[1:-1], x, L)
    tp = transfer_prime(z, idx[-1], idx[1:-1], x, L)
    dx = mp.lu_solve(A, x)
    d = [2 * mp.pi * n / L for n in idx[1:-1]]
    dmu_t = -mp.fsum(dx[j] / (z - d[j]) for j in range(len(d)))
    dmu_tp = mp.fsum(dx[j] / (z - d[j]) ** 2 for j in range(len(d)))
    dmu_log = dmu_tp / t - tp * dmu_t / (t * t)
    return t, tp, dmu_t, dmu_tp, dmu_log


def run_case(label, planted):
    mp.mp.dps = 70
    H, idx, L = build_mp(6, 8, 70, planted=planted)
    mu = mp.mpf("0")
    pkg = package(H, idx, L, mu, planted)
    rows = []
    for z in POINTS:
        t, tp, dmut_gen, dmutp_gen, dmulog_gen = generated_derivatives(pkg, z)
        tp_over_t = tp / t
        _td, _tpd, dmut_fd, dmutp_fd, dmulog_fd = direct_quantities(H, idx, L, mu, z)
        rows.append(
            {
                "z": serialize(z),
                "rel_dmu_T_error": serialize(abs(dmut_gen - dmut_fd) / max(1, abs(dmut_fd))),
                "rel_dmu_Tp_error": serialize(abs(dmutp_gen - dmutp_fd) / max(1, abs(dmutp_fd))),
                "rel_dmu_log_error": serialize(abs(dmulog_gen - dmulog_fd) / max(1, abs(dmulog_fd))),
                "abs_F": serialize(abs((z - pkg["db"]) * t)),
                "abs_F_mu": serialize(abs((z - pkg["db"]) * dmut_gen)),
                "abs_log_derivative": serialize(abs(tp_over_t)),
                "abs_dmu_log_derivative": serialize(abs(dmulog_gen)),
            }
        )
    return {
        "label": label,
        "rows": rows,
        "a_abs": serialize(abs(pkg["a"])),
        "b_abs": serialize(abs(pkg["b"])),
        "alpha_abs": serialize(abs(pkg["alpha"])),
        "beta_abs": serialize(abs(pkg["beta"])),
    }


def main():
    result = {
        "statement": "E78.103 coupled-generator mu-derivative audit",
        "date": "2026-07-19",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
    }
    out_path = Path(__file__).with_name("E78_103_coupled_generator_dmu_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
