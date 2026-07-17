#!/usr/bin/env python3
import math
import cmath


def von_mangoldt(n):
    x = n
    p = 2
    found = None
    while p * p <= x:
        if x % p == 0:
            found = p
            while x % p == 0:
                x //= p
            break
        p += 1 if p == 2 else 2
    if found is None:
        return math.log(n)
    return math.log(found) if x == 1 else 0.0


def B(t, L):
    if t < 0 or t > L:
        return 0.0
    return (1 - t / L) ** 2 * (1 + 0.25 * math.cos(2.5 * t))


def g(t, L, c):
    if abs(t) > L:
        return 0.0
    return math.exp(c * t) * B(abs(t), L)


def D_T(x, T):
    if abs(x) < 1e-12:
        return T / math.pi
    return math.sin(T * x) / (math.pi * x)


def wall_coeff_direct(u, L, c, T, steps=5000):
    h = 2 * L / steps
    total = 0.0
    for k in range(steps):
        t = -L + (k + 0.5) * h
        total += g(t, L, c) * D_T(t - u, T) * h
    return total


def prime_error(L, c, T, steps=5000):
    nmax = int(math.exp(L))
    err = 0.0
    main = 0.0
    finite = 0.0
    for n in range(2, nmax + 1):
        lam = von_mangoldt(n)
        if not lam:
            continue
        u = math.log(n)
        coeff = lam * n ** (-0.5 - c)
        wc = wall_coeff_direct(u, L, c, T, steps=steps)
        finite += coeff * wc
        main += lam * n ** (-0.5) * B(u, L)
    err = finite - main
    return err, finite, main


def weighted_local_modulus(L, c, T, delta, samples=80):
    nmax = int(math.exp(L))
    omega = 0.0
    mass = 0.0
    for n in range(2, nmax + 1):
        lam = von_mangoldt(n)
        if not lam:
            continue
        u = math.log(n)
        b0 = B(u, L)
        local = 0.0
        for j in range(samples + 1):
            t = max(0.0, min(L, u - delta + 2 * delta * j / samples))
            local = max(local, abs(B(t, L) - b0))
        omega += lam * n ** (-0.5) * local
        mass += lam * n ** (-0.5) * abs(b0)
    return math.log(2 + T * delta) * (omega + c * delta * mass), mass


def crude_wall_variation(L, c, steps=12000):
    h = 2 * L / steps
    vals = [g(-L + k * h, L, c) for k in range(steps + 1)]
    return sum(abs(vals[k + 1] - vals[k]) for k in range(steps))


def run():
    print("E72.379 weighted wall quadrature probe")
    print(" L    c     T       errPrime      nearWeighted    crudeVar      mass")
    for L, c, T in [(4.0, 0.8, 40.0), (4.0, 1.2, 40.0), (5.0, 0.8, 60.0), (5.0, 1.2, 60.0)]:
        err, _, _ = prime_error(L, c, T, steps=3500)
        delta = 1 / math.sqrt(T)
        near, mass = weighted_local_modulus(L, c, T, delta)
        crude = crude_wall_variation(L, c)
        print(f"{L:3.1f} {c:4.1f} {T:7.1f} {abs(err):12.3e} {near:13.3e} {crude:11.3e} {mass:9.3e}")


if __name__ == "__main__":
    run()
