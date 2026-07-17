#!/usr/bin/env python3
import cmath
import math
import mpmath as mp


def confluent_matrix(a, m):
    return mp.matrix(
        [
            [
                ((-1) ** q) * mp.binomial(p + q, p) / ((2 * a) ** (p + q + 1))
                for p in range(m)
            ]
            for q in range(m)
        ]
    )


def qjet_coeff(a, k, m):
    return mp.matrix([((-1) ** q) / ((a + k) ** (q + 1)) for q in range(m)])


def hermite_norm(coeffs):
    total = mp.mpf("0")
    for i, c in enumerate(coeffs):
        total += abs(c) / math.factorial(i)
    return total


def local_norm(a, k, m):
    h = mp.lu_solve(confluent_matrix(a, m), qjet_coeff(a, k, m))
    return hermite_norm([h[i] for i in range(m)])


def run():
    mp.mp.dps = 100
    print("E73.031 absolute geometry route falsifier")
    print("Fixed off-line node: e^(sigma L) times confluent geometry grows exponentially.")
    print(" sigma      t   gamma    m      localNorm       L      weighted")
    for sigma in [0.05, 0.10, 0.20]:
        a = mp.mpc(sigma, 14.0)
        k = mp.mpc(0.0, 21.0)
        m = 3
        loc = local_norm(a, k, m)
        for L in [5, 10, 20, 40, 80]:
            weighted = mp.e ** (sigma * L) * loc
            print(
                f"{sigma:6.2f} {14.0:6.1f} {21.0:7.1f} {m:4d} "
                f"{mp.nstr(loc, 10):>14s} {L:7.1f} {mp.nstr(weighted, 12):>14s}"
            )


if __name__ == "__main__":
    run()
