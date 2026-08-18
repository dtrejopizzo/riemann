"""Check of Theorem 2 of 103_04: the RH bound for J_n against the budget q(n).

  |J_n| <= (i) elementary + (ii) low zeros + (iii) high zeros

  (i)   1.911 * int_{log2}^{4N} e^{-u}|L_N^{(2)}| du
  (ii)  (log^2 Y / 2pi) * I_2(log 2),          Y = max(20, sqrt(n))
  (iii) 2 * sigma(Y) * I_3(log 2),             sigma(Y) <= (log Y + 1 - log 2pi)/(pi Y)

  q(n) = 0.75*A_n + 1 - L_n^{(1)}(log 2)
"""

import math
import numpy as np
import sys

sys.path.insert(0, ".")
from arch_and_margin import lambda_arch
from raised_kernel import M_alpha
from budget_vs_load import L1_at

LOG2 = math.log(2.0)


def I_alpha(N, alpha, u0=LOG2, pts=400000):
    u = np.linspace(u0, 4.05 * N + 20.0, pts)
    return np.trapz(np.abs(M_alpha(N, alpha, u)), u)


def elementary(N, pts=400000):
    u = np.linspace(LOG2, 4.05 * N + 20.0, pts)
    return np.trapz(np.abs(M_alpha(N, 2, u)) * np.exp(-u / 2.0), u)


def sigma(Y):
    return (math.log(Y) + 1.0 - math.log(2 * math.pi)) / (math.pi * Y)


if __name__ == "__main__":
    print(f"{'n':>6}{'q(n)':>12}{'(i)elem':>11}{'(ii)low':>11}{'(iii)high':>11}"
          f"{'total':>12}{'total/q':>10}{'elem/N^.75':>12}")
    for n in (10, 20, 40, 80, 150, 300, 600, 800):
        N = n - 1
        A = lambda_arch(n)
        q = 0.75 * A + 1.0 - L1_at(n, LOG2)
        el = 1.911 * elementary(N)
        Y = max(20.0, math.sqrt(n))
        lo = (math.log(Y) ** 2 / (2 * math.pi)) * I_alpha(N, 2)
        hi = 2.0 * sigma(Y) * I_alpha(N, 3)
        tot = el + lo + hi
        print(f"{n:>6}{q:>12.2f}{el:>11.2f}{lo:>11.2f}{hi:>11.2f}"
              f"{tot:>12.2f}{tot/q:>10.3f}{elementary(N)/N**0.75:>12.4f}")
