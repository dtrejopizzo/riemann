#!/usr/bin/env python3
import math
import cmath


def tail_kernel(L, M, z, w, mmax=250000):
    total = 0j
    ez = 1.0 - cmath.exp(z * L)
    for m in range(M + 1, mmax + 1):
        for sgn in (-1, 1):
            mm = sgn * m
            dm = 2.0 * math.pi * mm / L
            total += ez / ((1j * z - dm) * (w * w + dm * dm))
    return total


def run():
    print("E72.392 tail kernel scale probe")
    print("   L      M       |T|/e^(aL)    scaled=M^2/L^2")
    z = 0.25 + 3.0j
    w = 0.25 + 2.0j
    alpha = z.real
    for L in [8.0, 10.0, 12.0, 16.0, 20.0]:
        for mult in [1.0, 1.5, 2.0]:
            M = int(math.ceil(mult * L ** 1.5))
            R = tail_kernel(L, M, z, w)
            T = abs(2j * w * R / L)
            base = T / math.exp(alpha * L)
            scaled = base * M * M / (L * L)
            print(f"{L:5.1f} {M:6d} {base:14.3e} {scaled:14.3e}")


if __name__ == "__main__":
    run()
