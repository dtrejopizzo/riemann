#!/usr/bin/env python3
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


def coeff_norm(a, k, m):
    h = mp.lu_solve(confluent_matrix(a, m), qjet_coeff(a, k, m))
    return hermite_norm([h[i] for i in range(m)])


def run():
    mp.mp.dps = 200
    print("E73.029 high precision confluent multiplicity probe")
    print(" sigma      t   delta    m        normH        log10(normH)")
    cases = [(mp.mpf("0.2"), mp.mpf("50.0"), mp.mpf("3.0")),
             (mp.mpf("0.2"), mp.mpf("50.0"), mp.mpf("0.5")),
             (mp.mpf("0.05"), mp.mpf("50.0"), mp.mpf("0.5"))]
    for sigma, t, delta in cases:
        a = sigma + 1j * t
        k = 1j * (t + delta)
        for m in [4, 8, 12, 16, 20, 24, 28]:
            try:
                val = coeff_norm(a, k, m)
                print(
                    f"{float(sigma):6.2f} {float(t):6.1f} {float(delta):7.2f} {m:4d} "
                    f"{mp.nstr(val, 12):>12s} {float(mp.log10(val)):16.6f}"
                )
            except ZeroDivisionError:
                print(
                    f"{float(sigma):6.2f} {float(t):6.1f} {float(delta):7.2f} {m:4d} "
                    f"{'mp-singular':>12s} {'nan':>16s}"
                )


if __name__ == "__main__":
    run()
