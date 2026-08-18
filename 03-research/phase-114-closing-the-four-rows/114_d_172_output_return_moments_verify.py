#!/usr/bin/env python3
"""Finite audit of the positive output return expansion in D.172."""
import math
import numpy as np


def mobius(n):
    p = 2
    count = 0
    m = n
    while p * p <= m:
        if m % p == 0:
            m //= p
            count += 1
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        count += 1
    return -1 if count % 2 else 1


def mangoldt(n):
    return sum(mobius(d) * math.log(n // d)
               for d in range(1, n + 1) if n % d == 0)


def psqrt(a):
    d, u = np.linalg.eigh((a + a.T) / 2)
    return u @ np.diag(np.sqrt(np.maximum(d, 0))) @ u.T


def main():
    rng = np.random.default_rng(172)
    u, _ = np.linalg.qr(rng.normal(size=(6, 6)))
    K = u @ np.diag([.91, .7, .4, .2, .05, 0.0]) @ u.T
    y = rng.normal(size=(6, 2)) / 8
    D = np.eye(6) - K
    exact = y.T @ np.linalg.inv(D) @ y
    partial = np.zeros((2, 2))
    power = np.eye(6)
    for _ in range(400):
        partial += y.T @ power @ y
        power = power @ K
    assert np.linalg.norm(partial - exact) < 2e-13

    # Observability factor with alternating integer/half powers.
    Kh = psqrt(K)
    obs = np.zeros((2, 2))
    power = np.eye(6)
    for _ in range(400):
        z = power @ y
        obs += z.T @ z
        power = Kh @ power
    assert np.linalg.norm(obs - exact) < 2e-13

    # A spectral layer is bounded by a return moment.
    vals, vecs = np.linalg.eigh(D)
    delta = .31
    P = vecs[:, vals <= delta] @ vecs[:, vals <= delta].T
    F = y.T @ P @ y
    k = int(1 / delta)
    ck = y.T @ np.linalg.matrix_power(K, k) @ y
    assert np.linalg.eigvalsh((1 - delta) ** (-k) * ck - F).min() > -2e-13

    # Exact central Möbius convolution for every finite label.
    for n in range(2, 300):
        rhs = sum(mobius(d) / math.sqrt(d)
                  * math.log(n // d) / math.sqrt(n // d)
                  for d in range(1, n + 1) if n % d == 0)
        assert abs(rhs - mangoldt(n) / math.sqrt(n)) < 2e-14

    # Geometric safe-tail scalar check.
    q = .7
    m = 12
    assert abs(sum(q**j for j in range(m, 10000)) - q**m / (1 - q)) < 2e-15
    print("return capacity eigenvalues =", np.linalg.eigvalsh(exact))
    print("D172 output return-moment expansion: PASS")


if __name__ == "__main__":
    main()
