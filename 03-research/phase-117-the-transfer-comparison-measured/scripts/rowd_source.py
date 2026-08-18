"""The Gamma-Tate source defect  D_N = E_{Gamma T,N} - ||L_N||^2  on E_N=L^2(0,delta_N).

Leakage coefficients follow the construction already used in
phase-116 current-chat/work/urg_negative_test.py.  All forms are assembled in
closed form with the same Psi kernel as the physical side, so the two sides are
directly comparable.
"""
import math
from collections import defaultdict
import numpy as np

import rowd_assembly as RA


def leakage_coefficients(N):
    lam = RA.von_mangoldt(N)
    divs = [[] for _ in range(N + 1)]
    for d in range(1, N + 1):
        for n in range(d, N + 1, d):
            divs[n].append(d)
    powers, prev = [], np.zeros(N + 1)
    prev[1] = 1.0
    for _k in range(1, int(math.log(N, 2)) + 1):
        cur = np.zeros(N + 1)
        for n in range(2, N + 1):
            cur[n] = sum(prev[d] * lam[n // d] for d in divs[n])
        powers.append(cur)
        prev = cur
    out, logN = [], math.log(N)
    for k, lk in enumerate(powers, start=1):
        coeff = defaultdict(float)
        for m in range(1, N + 1):
            xm = lk[m] / (math.sqrt(m) * logN**k)
            if xm == 0.0:
                continue
            for n in range(2, N + 1):
                if lam[n] == 0.0 or m % n == 0:
                    continue
                g = math.gcd(m, n)
                a, b = m // g, n // g
                coeff[(a, b)] += lam[n] * xm / math.sqrt(n)
        if coeff:
            out.append(coeff)
    return out


def tate_gram(L, R):
    return np.array([[math.exp(R) - math.exp(L), R - L],
                     [R - L, math.exp(-L) - math.exp(-R)]], dtype=float)


def source_defect(N, ncell):
    """Matrices (Gamma+Tate, L2) of the source model on `ncell` equal cells of
    (0, delta_N).  Returns (E_GammaT, LtL) so that D_N = E_GammaT - LtL."""
    delta = 0.5 * math.log((N + 1) / N)
    edges = np.linspace(0.0, delta, ncell + 1)
    c0, d0 = edges[:-1], edges[1:]

    coeffs = leakage_coefficients(N)
    Lw = -math.log(N)
    Rw = math.log(N / 2) + delta
    Ginv = np.linalg.inv(tate_gram(Lw, Rw))

    EG = np.zeros((ncell, ncell))
    LL = np.zeros((ncell, ncell))

    for coeff in coeffs:
        shifts = np.array([math.log(a / b) for (a, b) in coeff])
        vals = np.array([v for v in coeff.values()])
        # every basis cell i, shifted by each rational position
        C = (c0[:, None] + shifts[None, :]).ravel()      # (ncell*nsh,)
        D = (d0[:, None] + shifts[None, :]).ravel()
        W = np.tile(vals, (ncell, 1)).ravel()
        idx = np.repeat(np.arange(ncell), len(shifts))

        # --- L2 Gram of the leakage outputs
        lo = np.maximum(C[:, None], C[None, :])
        hi = np.minimum(D[:, None], D[None, :])
        ov = np.maximum(hi - lo, 0.0) * (W[:, None] * W[None, :])
        LL += np.add.reduceat(
            np.add.reduceat(ov, np.arange(0, len(C), len(shifts)), axis=0),
            np.arange(0, len(C), len(shifts)), axis=1)

        # --- Gamma energy, same Psi kernel as the physical side
        allD = np.concatenate([(C[:, None] - C[None, :]).ravel(),
                               (C[:, None] - D[None, :]).ravel(),
                               (D[:, None] - C[None, :]).ravel(),
                               (D[:, None] - D[None, :]).ravel()])
        tab = RA.psi_table(allD)

        def P(X):
            k = np.round(np.abs(X), 12)
            o = np.empty_like(k); f = o.ravel()
            for i, kk in enumerate(k.ravel()):
                f[i] = tab[kk]
            return o
        Gm = (P(C[:, None] - C[None, :]) - P(C[:, None] - D[None, :])
              - P(D[:, None] - C[None, :]) + P(D[:, None] - D[None, :]))
        Gm = Gm * (W[:, None] * W[None, :])
        EG += np.add.reduceat(
            np.add.reduceat(Gm, np.arange(0, len(C), len(shifts)), axis=0),
            np.arange(0, len(C), len(shifts)), axis=1)

        # --- Tate terminal (2-dim, conservative)
        mp = 2.0 * (np.exp(D / 2) - np.exp(C / 2)) * W
        mm = 2.0 * (np.exp(-C / 2) - np.exp(-D / 2)) * W
        Mp = np.add.reduceat(mp, np.arange(0, len(C), len(shifts)))
        Mm = np.add.reduceat(mm, np.arange(0, len(C), len(shifts)))
        Mo = np.vstack([Mp, Mm])                       # (2, ncell)
        EG += Mo.T @ Ginv @ Mo

    return EG, LL
