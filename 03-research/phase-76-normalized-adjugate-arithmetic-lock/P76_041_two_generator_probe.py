#!/usr/bin/env python3
"""Verify the exact two-generator formula for T and T'/T."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_011_loewner_identity_probe import symbols
from P76_018_boundary_characteristic_probe import transfer
from P76_035_safe_log_derivative_probe import transfer_prime


def run():
    mp.mp.dps = 80
    H, idx, L = build_mp(6, 9, 80)
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    inner = idx[1:-1]
    d = [2 * mp.pi * n / L for n in inner]
    D = mp.diag(d)
    symbol = mp.matrix([symbols(dn, L, mp.mpf(6))[0] for dn in d])
    one = mp.matrix([1 for _ in d])
    u = A ** -1 * symbol
    v = A ** -1 * one
    db_idx = idx[-1]
    db = 2 * mp.pi * db_idx / L
    sb = symbols(db, L, mp.mpf(6))[0]
    Rb = (D - db * mp.eye(D.rows)) ** -1
    source = symbol - sb * one
    p = (v.T * Rb * source)[0]
    q = (u.T * Rb * source)[0]
    aa = 2 / L + 4 * p / L**2
    bb = -2 * sb / L - 4 * q / L**2
    ub = mp.fsum(u[j] / (d[j] - db) for j in range(len(d)))
    vb = mp.fsum(v[j] / (d[j] - db) for j in range(len(d)))

    print("P76.041 two-generator identity")
    print("z                    relTError       relLogError")
    for z in (mp.mpf("3.25"), mp.mpc("4", ".3"), mp.mpc(0, "1"), mp.mpc(0, "2")):
        U = mp.fsum(u[j] / (z - d[j]) for j in range(len(d)))
        V = mp.fsum(v[j] / (z - d[j]) for j in range(len(d)))
        Up = mp.fsum(-u[j] / (z - d[j]) ** 2 for j in range(len(d)))
        Vp = mp.fsum(-v[j] / (z - d[j]) ** 2 for j in range(len(d)))
        F = 1 + aa * (U + ub) + bb * (V + vb)
        Fp = aa * Up + bb * Vp
        direct_t = transfer(z, db_idx, inner, A ** -1 * mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)]), L)
        direct_tp = transfer_prime(z, db_idx, inner, A ** -1 * mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)]), L)
        generated_t = F / (z - db)
        generated_log = Fp / F - 1 / (z - db)
        print(
            f"{mp.nstr(z,10):20s} {mp.nstr(abs(generated_t-direct_t)/max(1,abs(direct_t)),8):>14}"
            f" {mp.nstr(abs(generated_log-direct_tp/direct_t)/max(1,abs(direct_tp/direct_t)),8):>17}"
        )


if __name__ == "__main__":
    run()
