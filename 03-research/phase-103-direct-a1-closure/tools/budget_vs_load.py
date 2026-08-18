"""Budget versus absolute load for the direct A1 certificate.

The direct certificate (phase-102 `226`, phase-103 guide eq. (3)) is

    C_n(T_n) = (3/4) A_n - n - int_0^{T_n} E(e^u) K_n(u) du  >= 0,
    K_n(u) = e^{-u} L_{n-1}^{(2)}(u),   E(e^u) = psi(e^u) - e^u.

Because psi vanishes on [1,2), E(e^u) = -e^u for 0 <= u < log 2, and

    int_0^{log 2} E(e^u) K_n(u) du = -(n+1) + L_n^{(1)}(log 2)   exactly,

since (d/du) L_n^{(1)} = -L_{n-1}^{(2)} and L_n^{(1)}(0) = n+1.  Hence the
certificate is exactly

    int_{log 2}^{T_n} E(e^u) K_n(u) du  <=  BUDGET_n,
    BUDGET_n := (3/4) A_n + 1 - L_n^{(1)}(log 2).                    (*)

This script compares BUDGET_n with
  (i)  a numerical value of the left side (obtained from lambda_n by the
       diagnostic Cauchy extractor; see zeta_tools.py for its finite-disk
       zero-free precondition),
  (ii) the absolute load  int W(u) e^{-u} |L_{n-1}^{(2)}(u)| du  for the
       envelope family W(u) = e^{u/2} u^a, i.e. |psi(x)-x| <= sqrt(x)(log x)^a.
"""

import math
import numpy as np
import sys

sys.path.insert(0, ".")
from zeta_tools import li_lambda
from arch_and_margin import lambda_arch
from laguerre_geometry import M_scaled


def L1_at(n, x):
    """L_n^{(1)}(x) by recurrence."""
    a, b = 1.0, 2.0 - x
    if n == 0:
        return a
    for k in range(1, n):
        a, b = b, ((2.0 * k + 2.0 - x) * b - (k + 1.0) * a) / (k + 1.0)
    return b


def load_a(N, a, u0=math.log(2.0), pts=600000):
    """int_{u0}^{4.05N} u^a e^{-u/2} |L_N^{(2)}(u)| du = int u^a |M_N| du."""
    u = np.linspace(u0, 4.05 * N + 20.0, pts)
    return np.trapz(u ** a * np.abs(M_scaled(N, u)), u)


if __name__ == "__main__":
    NMAX = 800
    lam = li_lambda(NMAX, r=0.995, M=1 << 19)

    print("DIAGNOSTIC tail integral J_n = int_{log2}^inf E(e^u) K_n(u) du")
    print("   from  lambda_n^prime = 1 - L_n^{(1)}(log 2) - J_n\n")
    hdr = (f"{'n':>5} {'BUDGET_n':>12} {'J_n(true)':>12} {'a=0':>11} "
           f"{'a=1/2':>11} {'a=1':>12} {'a=2':>13}")
    print(hdr)
    print("-" * len(hdr))
    rows = [8, 10, 12, 16, 20, 30, 40, 60, 80, 120, 200, 300, 400, 600, 800]
    tab = []
    for n in rows:
        A = lambda_arch(n)
        Lp = L1_at(n, math.log(2.0))
        budget = 0.75 * A + 1.0 - Lp
        lprime = lam[n - 1] - A
        J = 1.0 - Lp - lprime
        N = n - 1
        l0 = load_a(N, 0.0)
        lh = load_a(N, 0.5)
        l1 = load_a(N, 1.0)
        l2 = load_a(N, 2.0)
        tab.append((n, budget, J, l0, lh, l1, l2))
        print(f"{n:>5} {budget:>12.3f} {J:>12.4f} {l0:>11.2f} {lh:>11.2f} "
              f"{l1:>12.2f} {l2:>13.2f}")

    print("\nscaling of the absolute loads (fit  load ~ C N^p):")
    arr = np.array(tab)
    Ns = arr[:, 0] - 1
    for j, name, av in ((3, "a=0", 0.0), (4, "a=1/2", 0.5), (5, "a=1", 1.0),
                        (6, "a=2", 2.0)):
        p, c = np.polyfit(np.log(Ns[-5:]), np.log(arr[-5:, j]), 1)
        print(f"  W = e^{{u/2}} u^{{{name}}}:  load ~ {math.exp(c):.3f} * N^{p:.4f}"
              f"   (predicted p = {av + 0.5:.2f})")
    p, c = np.polyfit(np.log(Ns[-6:]), np.log(arr[-6:, 1]), 1)
    print(f"  BUDGET_n ~ {math.exp(c):.3f} * N^{p:.4f}  (predicted ~ (3/8) n log n)")

    print("\nratio load/BUDGET (a=2 is the Schoenfeld/RH envelope "
          "|psi(x)-x| <= (1/8pi) sqrt(x) log^2 x):")
    for (n, budget, J, l0, lh, l1, l2) in tab:
        print(f"  n={n:>4}  a=0: {l0/budget:>8.3f}   a=1/2: {lh/budget:>8.3f}"
              f"   a=1: {l1/budget:>8.3f}   a=2(x 1/8pi): "
              f"{l2/(8*math.pi)/budget:>10.3f}")
