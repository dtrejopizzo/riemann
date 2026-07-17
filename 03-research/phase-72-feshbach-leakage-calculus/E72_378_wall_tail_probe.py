#!/usr/bin/env python3
import math
import cmath


def packet(t, L):
    if abs(t) > L:
        return 0.0
    y = abs(t)
    return (1 - y / L) ** 2 * (1 + 0.2 * math.cos(3 * y))


def F(w, L, steps=5000):
    h = 2 * L / steps
    total = 0j
    for k in range(steps):
        t = -L + (k + 0.5) * h
        total += cmath.exp(w * t) * packet(t, L) * h
    return total


def wall_coeff(c, T, u, L, steps=6000):
    h = 2 * T / steps
    total = 0j
    for k in range(steps):
        tau = -T + (k + 0.5) * h
        total += F(c + 1j * tau, L) * cmath.exp(-1j * tau * u) * h
    return total / (2 * math.pi)


def sample_variation_g(c, L, steps=12000):
    h = 2 * L / steps
    vals = []
    for k in range(steps + 1):
        t = -L + k * h
        vals.append(math.exp(c * t) * packet(t, L))
    return sum(abs(vals[k + 1] - vals[k]) for k in range(steps))


def local_modulus(c, L, u, delta, steps=1000):
    center = math.exp(c * u) * packet(u, L)
    m = 0.0
    for k in range(steps + 1):
        t = u - delta + 2 * delta * k / steps
        if -L <= t <= L:
            m = max(m, abs(math.exp(c * t) * packet(t, L) - center))
    return m


def tail_bound(c, L, u, T, delta):
    g_u = math.exp(c * u) * packet(u, L)
    d = min(u + L, L - u)
    omega = local_modulus(c, L, u, delta)
    var = sample_variation_g(c, L)
    # A deliberately transparent constant, not optimized.
    C = 8.0
    return C * omega * math.log(2 + T * delta) + C * var / (T * delta) + C * abs(g_u) / (T * d)


def run():
    print("E72.378 finite-height wall-tail probe")
    print(" L    c     u      T        err          bound        ratio")
    cases = [
        (4.0, 0.8, 0.7, 40.0),
        (4.0, 0.8, 0.7, 80.0),
        (5.0, 1.0, 1.5, 60.0),
        (5.0, 1.0, 1.5, 120.0),
    ]
    for L, c, u, T in cases:
        coeff = wall_coeff(c, T, u, L)
        target = math.exp(c * u) * packet(u, L)
        err = abs(coeff - target)
        delta = 1 / math.sqrt(T)
        bd = tail_bound(c, L, u, T, delta)
        ratio = err / bd if bd else float("nan")
        print(f"{L:3.1f} {c:4.1f} {u:5.2f} {T:7.1f} {err:12.3e} {bd:12.3e} {ratio:9.3e}")


if __name__ == "__main__":
    run()
