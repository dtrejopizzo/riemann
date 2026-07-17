#!/usr/bin/env python3
"""Separate support-scale and Fourier-cutoff effects in the lock observable."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp, vec_norm


GAMMA_TEXT = "14.134725141734693790"


def observables(lam, n_modes, dps=60):
    H, idx, L = build_mp(lam, n_modes, dps)
    vals, vecs = mp.eigsy(H)
    xi = vecs[:, 0]

    def qnorm(t):
        r = mp.matrix([1 / (t - 2 * mp.pi * n / L) for n in idx])
        return abs((r.T * xi)[0]) / vec_norm(r)

    gamma = mp.mpf(GAMMA_TEXT)
    q = qnorm(gamma)
    qnear = qnorm(gamma + mp.mpf("0.125"))
    return L, vals[0], vals[1] - vals[0], q, qnear


def run():
    print("P76.004 two-scale probe")
    print("lam N dim      L          mu          gap       qgamma       qnear    select")
    for lam, cutoffs in ((4, (3, 4)), (6, (4, 5)), (8, (5, 6))):
        for n_modes in cutoffs:
            L, mu, gap, q, qnear = observables(lam, n_modes)
            print(
                f"{lam:3d} {n_modes:2d} {2*n_modes+1:3d} {mp.nstr(L,7):>8}"
                f" {mp.nstr(mu,6):>12} {mp.nstr(gap,6):>12}"
                f" {mp.nstr(q,6):>12} {mp.nstr(qnear,6):>12}"
                f" {mp.nstr(q/max(qnear,mp.mpf('1e-100')),6):>10}"
            )


if __name__ == "__main__":
    run()
