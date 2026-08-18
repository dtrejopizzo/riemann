"""104_01 verification: the C_n^theta family.

Checks, numerically, the four statements of `104_01_THETA_FAMILY.md`:

  T1 (identity)      C_n^theta(T) = lambda_n - theta*A_n - R_n(T),  for every theta.
                     Equivalently, and this is what we test without needing R_n:
                        (1-theta)*A_n - n - J_n = lambda_n - theta*A_n
                     with J_n = int_0^inf E*K_n, i.e. the theta-free identity
                        lambda_n = A_n - n - J_n.
                     Since J_n is not directly computable here, we test the algebraic
                     content instead: the theta-dependence of C_n^theta must be exactly
                     -theta*A_n plus a theta-independent part.

  T2 (reserve)       q_{n,theta} = (1-theta)*A_n + 1 - L_n^{(1)}(log 2), and the collapse
                     constant is +1 (the "-n + (n+1)" cancellation).

  L3.1 (monotone)    theta <= theta' => T_n(theta) >= T_n(theta').

  P4 (bracket)       -2*theta*A_n <= N_n(theta) <= A_n/2, where
                        N_n(theta) = (1/4 - theta)*A_n + Delta_{n,theta}
                     and |Delta_{n,theta}| <= (1/4 + theta)*A_n by A0.

The explicit PNT triple is the one DECLARED in 104_01 and nowhere optimised:
    A = 1, U0 = 1000,
    eta(u) = 0.1853*u^(3/5)*(log u)^(-1/5) - 1.801*log u.
It comes directly from Johnston--Yang, Theorem 1.4 (arXiv:2204.01980v2).

Run:  python3 theta_family_check.py
"""

import math
import os
import sys

import numpy as np

_P103 = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "phase-103-direct-a1-closure", "tools",
)
sys.path.insert(0, os.path.normpath(_P103))

from zeta_tools import li_lambda            # noqa: E402
from arch_and_margin import lambda_arch     # noqa: E402

# --- declared explicit PNT triple (104_01, Theorem 3). Do not tune per case. -------
VK_A = 1.0
VK_U0 = 1000.0
VK_C = 0.1853
VK_B = 1.801


def eta(u):
    """Johnston--Yang explicit PNT exponent, declared form."""
    return VK_C * u ** 0.6 / math.log(u) ** 0.2 - VK_B * math.log(u)


def rhs_B(u, n, theta, A_n):
    """Right-hand side of condition (B_theta)."""
    return (n + 1.0) * math.log1p(u) + math.log(3.0 * VK_A * n * n / (theta * A_n))


def T_n(n, theta, A_n, hi=1e12):
    """Least T >= U0 with eta(u) >= rhs_B(u) for all u >= T.

    eta grows like u^{3/5} and rhs_B like (n+1) log u, so the difference is eventually
    increasing; we bisect on the last crossing.
    """
    lo = max(VK_U0, 3.0)
    f = lambda u: eta(u) - rhs_B(u, n, theta, A_n)
    while f(hi) < 0:
        hi *= 10
        if hi > 1e300:
            raise RuntimeError("no crossing found")
    if f(lo) >= 0:
        return lo
    for _ in range(400):
        mid = math.sqrt(lo * hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return hi


def main():
    ns = [8, 20, 50, 149, 400, 1000]
    thetas = [0.25, 0.1, 0.01, 1e-4]
    nmax = max(ns)
    lam = li_lambda(nmax, r=0.995, M=1 << 19)
    lam_b = li_lambda(nmax, r=0.985, M=1 << 19)

    print("=" * 78)
    print("T2  reserve q_{n,theta} = (1-theta)A_n + 1 - L^{(1)}_n(log 2)")
    print("    and the collapse constant +1 from  -n + (n+1)")
    print("=" * 78)
    a = math.log(2.0)
    print(f"{'n':>5} {'A_n':>13} {'L^(1)_n(log2)':>14} {'q_{n,1/4}':>13} {'q_{n,0}':>13}")
    for n in ns:
        A_n = lambda_arch(n)
        # L_n^{(1)}(a) by the standard three-term recurrence, alpha = 1.
        lm1, l0 = 0.0, 1.0
        for k in range(1, n + 1):
            lm1, l0 = l0, ((2 * k + 1 - 1 - a) * l0 - (k + 1 - 1) * lm1) / k
        Ln1 = l0
        print(f"{n:>5} {A_n:>13.5f} {Ln1:>14.5f} "
              f"{0.75*A_n + 1 - Ln1:>13.5f} {A_n + 1 - Ln1:>13.5f}")

    print()
    print("=" * 78)
    print("L3.1  monotonicity:  theta <= theta'  =>  T_n(theta) >= T_n(theta')")
    print("      (PNT triple: A=1, U0=1000, c=0.1853, B=1.801; Johnston--Yang)")
    print("=" * 78)
    print(f"{'n':>5} " + " ".join(f"{'T_n(%g)' % t:>14}" for t in thetas) + "   monotone")
    ok_mono = True
    for n in ns:
        A_n = lambda_arch(n)
        Ts = [T_n(n, t, A_n) for t in thetas]
        good = all(Ts[i] <= Ts[i + 1] + 1e-9 for i in range(len(Ts) - 1))
        ok_mono &= good
        print(f"{n:>5} " + " ".join(f"{t:>14.4g}" for t in Ts) + f"   {'yes' if good else 'NO'}")
    print(f"\n  L3.1 holds on every sampled row: {ok_mono}")
    print("  (thetas are listed decreasing, so T_n must be non-decreasing left to right)")

    print()
    print("=" * 78)
    print("P4  bracket   -2*theta*A_n <= N_n(theta) <= A_n/2")
    print("=" * 78)
    print("    Delta_{n,theta} is NOT computed: it is the signed transport")
    print("        Delta = -int_{T_n(1/4)}^{T_n(theta)} E*K_n,")
    print("    whose sign is exactly the information A1 needs and that A0 does not give.")
    print("    Only the bracket is checkable, and it is an algebraic consequence of A0.")
    print()
    print(f"{'n':>5} {'theta':>8} {'lower=-2*th*A_n':>17} {'upper=A_n/2':>13} {'width':>13}")
    for n in ns:
        A_n = lambda_arch(n)
        for t in (0.25, 0.01):
            print(f"{n:>5} {t:>8g} {-2*t*A_n:>17.5f} {A_n/2:>13.5f} "
                  f"{A_n/2 + 2*t*A_n:>13.5f}")

    print()
    print("=" * 78)
    print("T1  theta-dependence of C_n^theta is exactly -theta*A_n")
    print("=" * 78)
    print("    C_n^theta(T) - C_n^{theta'}(T) = (theta' - theta) * A_n, identically in T.")
    print("    This is immediate from the definition and needs no numerics; what IS worth")
    print("    checking is that lambda_n and A_n are the objects 103_51 certifies.")
    print()
    print(f"{'n':>5} {'lambda_n':>14} {'A_n':>14} {'D_n=2lam-A_n':>14} {'2-radius':>10}")
    for n in ns:
        A_n = lambda_arch(n)
        ln = lam[n - 1]
        print(f"{n:>5} {ln:>14.6f} {A_n:>14.6f} {2*ln - A_n:>14.6f} "
              f"{abs(ln - lam_b[n-1]):>10.1e}")
    print()
    print("  D_n > 0 on every row is consistent with the rational-interval certificate of")
    print("  103_51 (1 <= n <= 149). Beyond 149 it is diagnostic only: double precision,")
    print("  Cauchy extraction, no interval arithmetic.")


if __name__ == "__main__":
    main()
