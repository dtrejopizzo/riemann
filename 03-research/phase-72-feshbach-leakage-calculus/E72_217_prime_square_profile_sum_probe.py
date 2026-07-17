#!/usr/bin/env python3
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402


WINDOWS = [12, 16, 20, 24, 28, 32, 36, 48, 64, 96]


def sums(lam, cut=0.60):
    L = 2.0 * np.log(lam)
    maxn = int(lam * lam)
    ans = [[0.0, 0.0], [0.0, 0.0]]
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            u = y / L
            beta2 = lp * lp / pm
            block = 0 if u <= cut else 1
            ans[block][0] += beta2
            ans[block][1] += beta2 * np.sqrt(max(0.0, 1.0 - u))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return L, ans


def run():
    print("E72.217 prime-square profile sum probe")
    print("S0=sum beta2, Sphi=sum beta2 sqrt(1-logn/L)")
    print("lam L block S0 Sphi Sphi/L Sphi/L2 boundCoef")
    print("boundCoef = 1.5*Sphi/L^2, so Res2 <= boundCoef/c_C^2")
    for lam in WINDOWS:
        L, ans = sums(lam)
        for block in [0, 1]:
            s0, sp = ans[block]
            coef = 1.5 * sp / (L * L)
            print(
                f"{lam:3.0f} {L:6.3f} {block:5d} "
                f"{s0:.6e} {sp:.6e} {sp/L:.6e} {sp/(L*L):.6e} {coef:.6e}"
            )


if __name__ == "__main__":
    run()
