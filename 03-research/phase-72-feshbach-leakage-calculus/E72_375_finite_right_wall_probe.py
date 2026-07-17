#!/usr/bin/env python3
import cmath
import math
import mpmath as mp


def von_mangoldt(n):
    x = n
    p0 = None
    exp = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            p0 = p
            while x % p == 0:
                x //= p
                exp += 1
            break
        p += 1 if p == 2 else 2
    if p0 is None:
        return math.log(n)
    if x != 1:
        return 0.0
    return math.log(p0)


def Tfun(a, u):
    return u * cmath.sinh(a * u)


def D(a, z, w):
    den = w * w - z * z
    if abs(den) < 1e-9:
        h = 1e-6 * (1 + abs(w))
        return D(a, z, w + h)
    return (cmath.cosh(a * z) * Tfun(a, w) - Tfun(a, z) * cmath.cosh(a * w)) / den


def G(w, L):
    return cmath.exp(w * L / 2) * (1 + 0.2 * w * w)


def H(z, w, L):
    a = L / 2
    return 4 * cmath.exp(a * (z - w)) * D(a, z, w) * G(w, L)


def A_right(c, t):
    s = 0.5 + c + 1j * t
    return (
        1 / s
        + 1 / (s - 1)
        - 0.5 * math.log(math.pi)
        + 0.5 * complex(mp.digamma(s / 2))
    )


def prime_trunc(c, t, nmax):
    s = 0.5 + c + 1j * t
    total = 0j
    for n in range(2, nmax + 1):
        lam = von_mangoldt(n)
        if lam:
            total += lam * cmath.exp(-s * math.log(n))
    return total


def integrate(fn, tmax, steps):
    h = 2 * tmax / steps
    total = 0j
    for k in range(steps):
        t = -tmax + (k + 0.5) * h
        total += fn(t) * h
    return total


def run():
    print("E72.375 finite right-wall identity probe")
    print(" L    c    T   N       direct              split               relErr")
    cases = [
        (3.0, 0.2 + 0.6j, 1.7, 4.0, 80),
        (4.0, -0.1 + 0.8j, 1.8, 4.5, 120),
        (5.0, 0.3 + 0.4j, 1.9, 5.0, 160),
    ]
    steps = 5000
    for L, z, c, tmax, nmax in cases:
        hfun = lambda t: H(z, c + 1j * t, L)
        direct = integrate(
            lambda t: hfun(t) * (A_right(c, t) - prime_trunc(c, t, nmax)),
            tmax,
            steps,
        ) / (2 * math.pi)
        arch = integrate(lambda t: hfun(t) * A_right(c, t), tmax, steps) / (2 * math.pi)
        prime = 0j
        for n in range(2, nmax + 1):
            lam = von_mangoldt(n)
            if lam:
                u = math.log(n)
                coeff = lam * n ** (-0.5 - c)
                fourier = integrate(lambda t, u=u: hfun(t) * cmath.exp(-1j * t * u), tmax, steps)
                prime += coeff * fourier / (2 * math.pi)
        split = arch - prime
        rel = abs(direct - split) / max(1.0, abs(direct), abs(split))
        print(f"{L:3.1f} {c:4.1f} {tmax:4.1f} {nmax:3d} {direct:18.8e} {split:18.8e} {rel:10.3e}")


if __name__ == "__main__":
    run()
