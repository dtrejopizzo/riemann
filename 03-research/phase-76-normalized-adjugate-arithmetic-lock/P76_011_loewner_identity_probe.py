#!/usr/bin/env python3
"""Verify H=2 diag(C)-(2/L)Loew(S) from independent CCM integrals."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp, primes_upto


def weil_functional(f, f0, fp0, L, lam):
    w02 = mp.quad(lambda y: f(y) * (mp.exp(y / 2) + mp.exp(-y / 2)), [0, L])

    def wr_integrand(y):
        if y == 0:
            return (fp0 + f0 / 2) / 2
        return (mp.exp(y / 2) * f(y) - f0) / (2 * mp.sinh(y))

    wr = (
        (mp.log(4 * mp.pi) + mp.euler) * f0 / 2
        + mp.quad(wr_integrand, [0, L])
        + f0 * mp.log(mp.tanh(L / 2)) / 2
    )
    arith = mp.mpf(0)
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = mp.log(p)
        pm = p
        exponent = 1
        while pm <= maxn:
            arith += lp * mp.power(pm, mp.mpf("-0.5")) * f(exponent * lp)
            pm *= p
            exponent += 1
    return w02 - wr - arith


def symbols(t, L, lam):
    S = weil_functional(lambda y: mp.sin(t * y), mp.mpf(0), t, L, lam)
    C = weil_functional(lambda y: mp.cos(t * y), mp.mpf(1), mp.mpf(0), L, lam)
    Sp = weil_functional(lambda y: y * mp.cos(t * y), mp.mpf(0), mp.mpf(1), L, lam)
    return S, C, Sp


def run():
    mp.mp.dps = 60
    lam = mp.mpf(6)
    H, idx, L = build_mp(6, 3, 60)
    data = [symbols(2 * mp.pi * n / L, L, lam) for n in idx]
    model = mp.matrix(H.rows)
    for i, ni in enumerate(idx):
        di = 2 * mp.pi * ni / L
        for j, nj in enumerate(idx):
            if i == j:
                model[i, j] = 2 * data[i][1] - 2 * data[i][2] / L
            else:
                dj = 2 * mp.pi * nj / L
                loewner = (data[i][0] - data[j][0]) / (di - dj)
                model[i, j] = -2 * loewner / L
    defect = mp.sqrt(sum(abs(H[i, j] - model[i, j]) ** 2 for i in range(H.rows) for j in range(H.cols)))
    scale = mp.sqrt(sum(abs(H[i, j]) ** 2 for i in range(H.rows) for j in range(H.cols)))

    vals, vecs = mp.eigsy(H)
    xi = vecs[:, 0]
    loew_xi = (L / 2) * (2 * mp.diag([x[1] for x in data]) - H) * xi
    nodal = mp.matrix(H.rows, 1)
    for i, ni in enumerate(idx):
        di = 2 * mp.pi * ni / L
        value = data[i][2] * xi[i]
        for j, nj in enumerate(idx):
            if i == j:
                continue
            dj = 2 * mp.pi * nj / L
            value += (data[i][0] - data[j][0]) * xi[j] / (di - dj)
        nodal[i] = value
    node_error = mp.sqrt(sum(abs(nodal[i] - loew_xi[i]) ** 2 for i in range(H.rows)))

    print("P76.011 Loewner interpolation identity")
    print("matrix_relative_defect", mp.nstr(defect / scale, 10))
    print("nodal_identity_error", mp.nstr(node_error, 10))
    print("ground_mu", mp.nstr(vals[0], 12))
    gamma = mp.mpf("14.134725141734693790")
    sg, cg, spg = symbols(gamma, L, lam)
    print("S(gamma)", mp.nstr(sg, 12))
    print("C(gamma)", mp.nstr(cg, 12))
    print("Sprime(gamma)", mp.nstr(spg, 12))


if __name__ == "__main__":
    run()
