"""Raised Laguerre kernels L_N^{(alpha)} for the summation-by-parts route.

Reports, for alpha = 2 and 3,

    c_alpha  = sup_u  |L_N^{(alpha)}(u)| u^{alpha/2+1/4} e^{-u/2} / N^{alpha/2-1/4}
    I_alpha(u0) = int_{u0}^{4.05N} e^{-u/2} |L_N^{(alpha)}(u)| du

The second is the cost of the once-integrated (summation-by-parts) estimate
    |int E K_n| <= sup|V| * int e^{-u/2}|L_{n-1}^{(3)}|,      V = primitive of E,
which under RH obeys |V(u)| <= (sum_rho |rho|^{-2}) e^{u/2} + O(u).
"""

import numpy as np

_L10 = 250.0 * np.log(10.0)


def M_alpha(N, alpha, u):
    """e^{-u/2} L_N^{(alpha)}(u), rescaled recurrence."""
    u = np.asarray(u, dtype=float)
    sc = -u / 2.0
    m0 = np.ones_like(u)
    m1 = (alpha + 1.0) - u
    if N == 0:
        return np.exp(sc)
    for k in range(1, N):
        m2 = ((2.0 * k + alpha + 1.0 - u) * m1 - (k + alpha) * m0) / (k + 1.0)
        m0, m1 = m1, m2
        big = np.maximum(np.abs(m0), np.abs(m1))
        hot = big > 1e250
        if hot.any():
            m0[hot] *= 1e-250
            m1[hot] *= 1e-250
            sc[hot] += _L10
    return m1 * np.exp(np.clip(sc, -700.0, 700.0))


if __name__ == "__main__":
    print("Plancherel-Rotach constants  c_alpha = sup |M| u^{a/2+1/4} / N^{a/2-1/4}")
    for alpha in (2, 3):
        for N in (50, 100, 200, 400, 800):
            u = np.linspace(0.5, 4.05 * N, 600000)
            M = np.abs(M_alpha(N, alpha, u))
            c = np.max(M * u ** (alpha / 2 + 0.25)) / N ** (alpha / 2 - 0.25)
            print(f"  alpha={alpha}  N={N:>4}  c={c:.4f}")

    print("\nI_alpha(u0) = int_{u0}^{4.05N} e^{-u/2}|L_N^{(alpha)}| du")
    print(f"{'alpha':>6}{'N':>6}{'u0=1':>14}{'u0=10':>14}{'u0=100':>14}"
          f"{'  I(1)/N^p':>14}")
    for alpha in (2, 3):
        p = alpha / 2 - 0.25 + max(0.0, 0.0)   # predicted: N^{alpha/2-1/4}
        for N in (50, 100, 200, 400, 800):
            out = []
            for u0 in (1.0, 10.0, 100.0):
                u = np.linspace(u0, 4.05 * N, 600000)
                out.append(np.trapz(np.abs(M_alpha(N, alpha, u)), u))
            print(f"{alpha:>6}{N:>6}{out[0]:>14.3f}{out[1]:>14.3f}"
                  f"{out[2]:>14.3f}{out[0]/N**p:>14.4f}")

    print("\nu0-decay check: I_alpha(u0) should scale like u0^{-(alpha-2)/2-1/4}")
    for alpha in (2, 3):
        N = 400
        for u0 in (1.0, 10.0, 100.0, 1000.0):
            u = np.linspace(u0, 4.05 * N, 600000)
            v = np.trapz(np.abs(M_alpha(N, alpha, u)), u)
            print(f"  alpha={alpha} N={N} u0={u0:>7.0f}  I={v:>12.4f}"
                  f"   I*u0^{{{(alpha-2)/2+0.25:.2f}}}={v*u0**((alpha-2)/2+0.25):>12.4f}")
