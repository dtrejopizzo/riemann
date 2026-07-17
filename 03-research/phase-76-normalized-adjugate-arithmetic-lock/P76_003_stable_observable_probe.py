#!/usr/bin/env python3
"""Compare three product-free formulas for the normalized lock observable."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp, vec_norm


def cauchy_row(gamma, idx, L):
    return mp.matrix([1 / (gamma - 2 * mp.pi * n / L) for n in idx])


def bordered_matrix(K, r):
    n = K.rows
    B = mp.matrix(n + 1)
    for i in range(n):
        for j in range(n):
            B[i, j] = K[i, j]
        B[i, n] = r[i]
        B[n, i] = r[i]
    B[n, n] = 0
    return B


def characteristic_derivative(mu, vals):
    out = mp.mpf(1)
    for j in range(1, vals.rows):
        out *= mu - vals[j]
    return out


def run():
    mp.mp.dps = 80
    H, idx, L = build_mp(lam_int=6, n_modes=5, dps=80)
    vals, vecs = mp.eigsy(H)
    mu = vals[0]
    xi = vecs[:, 0]
    gamma = mp.mpf("14.134725141734693790")
    r = cauchy_row(gamma, idx, L)
    rnorm2 = vec_norm(r) ** 2

    a_eigen = abs((r.T * xi)[0]) ** 2 / rnorm2

    K = mu * mp.eye(H.rows) - H
    B = bordered_matrix(K, r)
    pprime = characteristic_derivative(mu, vals)
    a_border = -mp.det(B) / (pprime * rnorm2)

    # The residue error is O(delta/gap).  Taking delta=gap*1e-20 resolves
    # the limit while staying far above the 80-digit arithmetic floor.
    gap = vals[1] - vals[0]
    delta = gap * mp.mpf("1e-20")
    scalar_resolvent = (r.T * ((mu + delta) * mp.eye(H.rows) - H) ** -1 * r)[0]
    a_residue = delta * scalar_resolvent / rnorm2

    print("P76.003 stable observable probe")
    print("mu", mp.nstr(mu, 16))
    print("gap", mp.nstr(gap, 16))
    print("A_eigen", mp.nstr(a_eigen, 20))
    print("A_border", mp.nstr(a_border, 20))
    print("A_residue", mp.nstr(a_residue, 20))
    print("border_abs_error", mp.nstr(abs(a_border - a_eigen), 8))
    print("residue_abs_error", mp.nstr(abs(a_residue - a_eigen), 8))


if __name__ == "__main__":
    run()
