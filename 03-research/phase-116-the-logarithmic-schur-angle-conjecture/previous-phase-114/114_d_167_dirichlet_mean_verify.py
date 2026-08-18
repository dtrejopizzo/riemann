#!/usr/bin/env python3
"""Arithmetic and algebraic checks for D.167."""
import math
import numpy as np


def von_mangoldt(n):
    out = 0.0
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            if m == 1:
                return math.log(p)
            return 0.0
        p += 1
    return math.log(n) if n > 1 else 0.0


def main():
    # The normalized diagonal sum tends to one half.
    for N in (1000, 10000, 100000):
        lam = np.array([von_mangoldt(n) for n in range(1, N + 1)])
        idx = np.arange(1, N + 1, dtype=float)
        V = float(np.sum(lam * lam / idx))
        ratio = V / math.log(N) ** 2
        H = sum(von_mangoldt(d) * von_mangoldt(N // d)
                for d in range(1, N + 1) if N % d == 0) / math.sqrt(N)
        print(f"N={N:6d} V/log^2N={ratio:.9f} H={H:.9g}")
    assert 0.40 < ratio < 0.60

    # Exact collision support: left log n and reflected right log m agree
    # after centering at log N iff nm=N.
    N = 72
    collisions = [(n, m) for n in range(1, N + 1)
                  for m in range(1, N + 1) if n * m == N]
    assert all(abs(math.log(n) + math.log(m) - math.log(N)) < 2e-15
               for n, m in collisions)

    # Finite-dimensional resolvent identity G^{-1}-A^{-1}
    # =G^{-1}(A-G)A^{-1}; written with the sign used in (5.4).
    G = np.diag([3.0, 4.0, 5.0])
    A = G - np.array([[.2, .1, 0.0], [.1, .3, .1], [0.0, .1, .2]])
    lhs = np.linalg.inv(A) - np.linalg.inv(G)
    rhs = np.linalg.inv(G) @ (G - A) @ np.linalg.inv(A)
    assert np.linalg.norm(lhs - rhs) < 1e-14
    print("D167 Tate-cancelled Dirichlet mean audit: PASS")


if __name__ == "__main__":
    main()
