"""A_n = lambda_n^arch, lambda_n, and the strong-margin ratio.

Phase-102 archimedean term:

    A_n = 1 - (n/2)(gamma + log 4pi) + S_n ,
    S_n = sum_{r odd >= 1} q_n(1/r),   q_n(x) = (1-x)^n - 1 + n x .

Equivalently (doc 217, eq. 3)

    S_n = sum_{k=2}^{n} (-1)^k C(n,k) (1 - 2^{-k}) zeta(k),

but that finite form has terms of size C(n,n/2) ~ 2^n and is numerically
useless past n ~ 20.  The odd-r form has *nonnegative* terms (q_n >= 0 on
[0,1]) and is stable, so it is the one used here; truncating it always gives
a rigorous lower bound for S_n, hence for A_n.
"""

import math
import numpy as np

GAMMA = 0.57721566490153286061


def q_series(n, x, kmax=80):
    """q_n(x) = sum_{k>=2} C(n,k)(-x)^k, for x small."""
    c = n * (n - 1) / 2.0
    p = x * x
    tot = 0.0
    for k in range(2, kmax + 1):
        t = c * p
        tot += t if k % 2 == 0 else -t
        if abs(t) < 1e-24 * max(abs(tot), 1e-300):
            break
        c *= (n - k) / (k + 1.0)
        p *= x
    return tot


def q_direct(n, r):
    return math.expm1(n * math.log1p(-1.0 / r)) + n / r


def _odd_tail_power(R, k):
    """sum over odd r > R-2 (i.e. r = R, R+2, ...) of r^{-k}, Euler-Maclaurin."""
    g = R ** (-float(k))
    return (R ** (1.0 - k) / (2.0 * (k - 1))
            + 0.5 * g
            + (k / 6.0) * g / R
            - (k * (k + 1) * (k + 2) / 180.0) * g / R ** 3)


def lambda_arch(n, rswitch=None, rmax=None, ktail=40):
    if rswitch is None:
        rswitch = max(8, 4 * n)
    if rmax is None:
        rmax = max(400, 60 * n)
    if rswitch % 2 == 0:
        rswitch += 1
    if rmax % 2 == 0:
        rmax += 1
    s = n - 1.0                                   # r = 1
    for r in range(3, rswitch + 1, 2):
        s += q_direct(n, r)
    for r in range(rswitch + 2, rmax + 1, 2):
        s += q_series(n, 1.0 / r)
    # exact tail:  sum_{r odd > rmax} sum_{k>=2} C(n,k)(-1/r)^k
    R = rmax + 2.0
    c = n * (n - 1) / 2.0
    for k in range(2, ktail + 1):
        t = c * _odd_tail_power(R, k)
        s += t if k % 2 == 0 else -t
        if abs(t) < 1e-18:
            break
        c *= (n - k) / (k + 1.0)
    return 1.0 - (n / 2.0) * (GAMMA + math.log(4.0 * math.pi)) + s


if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    from zeta_tools import li_lambda

    print("check A_8  =", f"{lambda_arch(8):.12f}",
          " certified [0.02089993302762, 0.02089993302764]")

    NMAX = 1200
    lam = li_lambda(NMAX, r=0.995, M=1 << 19)
    lam_b = li_lambda(NMAX, r=0.985, M=1 << 19)

    rows = list(range(1, 21)) + [25, 30, 40, 50, 60, 80, 100, 150, 200,
                                 300, 400, 500, 600, 800, 1000, 1200]
    print(f"\n{'n':>5} {'lambda_n':>15} {'A_n':>15} {'lam_n^prime':>13} "
          f"{'lam-A/2':>13} {'lam/A':>8} {'2A/n-log n':>11} {'err':>9}")
    for n in rows:
        if n > NMAX:
            continue
        A = lambda_arch(n)
        L = lam[n - 1]
        err = abs(L - lam_b[n - 1])
        print(f"{n:>5} {L:>15.8f} {A:>15.8f} {L-A:>13.6f} {L-A/2:>13.6f} "
              f"{(L/A if A else float('nan')):>8.4f} "
              f"{2*A/n - math.log(n):>11.6f} {err:>9.1e}")

    # asymptotic fit  A_n = (n/2)(log n + c1) + c2*log n + c3
    ns = np.array([m for m in range(200, NMAX + 1, 10)], dtype=float)
    As = np.array([lambda_arch(int(m)) for m in ns])
    X = np.column_stack([ns / 2 * np.log(ns), ns / 2, np.log(ns),
                         np.ones_like(ns)])
    coef, *_ = np.linalg.lstsq(X, As, rcond=None)
    print("\nfit  A_n ~ a*(n/2)log n + b*(n/2) + c*log n + d")
    print("     a=%.8f  b=%.8f  c=%.6f  d=%.6f" % tuple(coef))
    print("     -log(2pi) = %.8f   -(1+log 2pi)/1 = %.8f"
          % (-math.log(2 * math.pi), -(1 + math.log(2 * math.pi))))
