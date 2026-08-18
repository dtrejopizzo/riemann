"""Laguerre lobe geometry and load scales for the phase-103 direct route.

Everything is computed through the scaled function

    M_N(u) = e^{-u/2} L_N^{(2)}(u),

which satisfies the same three-term recurrence as L_N^{(2)} and stays of
size O(N^{3/4} u^{-5/4}) in the oscillatory bulk 0 < u < 4N, so it is
representable in double precision where L_N^{(2)} itself is not.

Reported quantities

  1. PR constant      sup_u  |M_N(u)| u^{5/4} / N^{3/4}
  2. bulk zero spacing of L_N^{(2)} near u = xN
  3. "RH load"        int_{u0}^{inf} e^{-u/2} |L_N^{(2)}(u)| du = int |M_N|
  4. "VK load"        int_{aN}^{bN} |L_N^{(2)}(u)| du  (log10 scale)
  5. kernel L1 mass   int_0^inf e^{-u} |L_N^{(2)}(u)| du
"""

import numpy as np


_LOGBIG = 500.0 * np.log(10.0)


def M_scaled(N, u):
    """e^{-u/2} L_N^{(2)}(u) by the three-term recurrence (vectorised in u).

    The recurrence is run on a dynamically rescaled pair so that the huge
    intermediate range of e^{-u/2} L_k^{(2)}(u) (which underflows badly for
    u >~ 1490 if the naive scaling is used) never leaves double range.
    Returns e^{-u/2} L_N^{(2)}(u) itself, which is O(N^{3/4} u^{-5/4}) in the
    bulk and therefore harmless.
    """
    u = np.asarray(u, dtype=float)
    sc = -u / 2.0                     # log of the factor still owed
    m0 = np.ones_like(u)
    m1 = 3.0 - u
    if N == 0:
        return np.exp(sc)
    for k in range(1, N):
        m2 = ((2.0 * k + 3.0 - u) * m1 - (k + 2.0) * m0) / (k + 1.0)
        m0, m1 = m1, m2
        big = np.maximum(np.abs(m0), np.abs(m1))
        hot = big > 1e250
        if hot.any():
            m0[hot] *= 1e-250
            m1[hot] *= 1e-250
            sc[hot] += 250.0 * np.log(10.0)
    return m1 * np.exp(np.clip(sc, -_LOGBIG, _LOGBIG))


def logM_scaled(N, u):
    """log|e^{-u/2} L_N^{(2)}(u)| with no range restriction (returns log, sign)."""
    u = np.asarray(u, dtype=float)
    sc = -u / 2.0
    m0 = np.ones_like(u)
    m1 = 3.0 - u
    for k in range(1, N):
        m2 = ((2.0 * k + 3.0 - u) * m1 - (k + 2.0) * m0) / (k + 1.0)
        m0, m1 = m1, m2
        big = np.maximum(np.abs(m0), np.abs(m1))
        hot = big > 1e250
        if hot.any():
            m0[hot] *= 1e-250
            m1[hot] *= 1e-250
            sc[hot] += 250.0 * np.log(10.0)
    return np.log(np.abs(m1) + 1e-300) + sc, np.sign(m1)


def sign_changes(u, f):
    s = np.sign(f)
    idx = np.nonzero(s[:-1] * s[1:] < 0)[0]
    # linear interpolation for the crossing
    return u[idx] - f[idx] * (u[idx + 1] - u[idx]) / (f[idx + 1] - f[idx])


def logsumexp_integral(u, logw, sign_ok=True):
    """log of int exp(logw(u)) du on a uniform grid, by trapezoid in log space."""
    h = u[1] - u[0]
    mx = logw.max()
    return mx + np.log(np.trapz(np.exp(logw - mx), dx=h))


if __name__ == "__main__":
    print("=== 1. Plancherel-Rotach constant:  sup |M_N(u)| u^{5/4} / N^{3/4} ===")
    for N in (20, 50, 100, 200, 400, 800):
        u = np.linspace(1.0, 4.0 * N, 400000)
        M = M_scaled(N, u)
        c = np.max(np.abs(M) * u ** 1.25) / N ** 0.75
        # also restricted to the bulk interior
        m = (u > 0.05 * N) & (u < 3.9 * N)
        cb = np.max(np.abs(M[m]) * u[m] ** 1.25) / N ** 0.75
        print(f"  N={N:>4}  c_full={c:.4f}   c_bulk={cb:.4f}")

    print("\n=== 2. bulk zero spacing of L_N^{(2)} near u = xN "
          "(predicted 2pi/sqrt((4-x)/x)) ===")
    for N in (100, 400, 1600):
        u = np.linspace(1.0, 4.0 * N, 2000000)
        z = sign_changes(u, M_scaled(N, u))
        print(f"  N={N:>5}  #zeros={len(z)} (=N)  ", end="")
        for x in (0.5, 1.0, 2.0, 3.0):
            k = np.searchsorted(z, x * N)
            if 1 <= k < len(z) - 1:
                sp = z[k + 1] - z[k]
                pred = 2 * np.pi / np.sqrt((4.0 - x) / x)
                print(f"x={x}: {sp:.3f}/{pred:.3f}  ", end="")
        print()

    print("\n=== 3. RH-quality load   int_{u0}^{4N} e^{-u/2}|L_N^{(2)}| du ===")
    print("    (this is the cost when |psi(e^u)-e^u| <= e^{u/2})")
    for N in (20, 50, 100, 200, 400, 800, 1600):
        u = np.linspace(1.0, 4.05 * N, 800000)
        M = np.abs(M_scaled(N, u))
        I = np.trapz(M, u)
        print(f"  N={N:>5}   load={I:>12.3f}   load/N^{{3/4}}={I/N**0.75:>8.4f}"
              f"   load/N^{{1/2}}={I/N**0.5:>8.4f}")

    print("\n=== 4. VK-route absolute load   log10 int_{aN}^{bN} |L_N^{(2)}| du ===")
    print("    (bulk factor e^{u/2} is not cancelled once |.| is taken)")
    for N in (20, 50, 100, 200, 400):
        for (a, b) in ((2.0, 3.0), (3.0, 4.0)):
            u = np.linspace(a * N, b * N, 400000)
            lw = np.log(np.abs(M_scaled(N, u)) + 1e-300) + u / 2.0
            lg = logsumexp_integral(u, lw) / np.log(10.0)
            print(f"  N={N:>4} [{a}N,{b}N]  log10 load={lg:>10.3f}"
                  f"   (a*N/2)/log10 = {a*N/2/np.log(10):>10.3f}")

    print("\n=== 5. kernel mass   int_0^{inf} e^{-u}|L_N^{(2)}(u)| du ===")
    for N in (20, 50, 100, 200, 400, 800):
        u = np.linspace(1e-6, 4.2 * N, 800000)
        val = np.trapz(np.abs(M_scaled(N, u)) * np.exp(-u / 2.0), u)
        print(f"  N={N:>4}  mass={val:>10.4f}   mass/log N={val/np.log(N):>8.4f}")
