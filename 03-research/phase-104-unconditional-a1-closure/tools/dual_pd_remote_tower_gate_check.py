#!/usr/bin/env python3
"""Finite checks for 104_91 (numpy only).

The analytic statements in the note are proved there. This script checks
the finite dual identity, positive-definite matrices for a sample selector,
and the algebra of the remote-prime-tower countermodel.
"""

from math import log, pi, sqrt

import numpy as np


def mangoldt_sieve(limit):
    values = np.zeros(limit + 1, dtype=float)
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        if p * p <= limit:
            prime[p * p : limit + 1 : p] = False
        power = p
        while power <= limit:
            values[power] = log(p)
            if power > limit // p:
                break
            power *= p
    return values


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def next_prime(n):
    p = max(2, n + 1)
    while not is_prime(p):
        p += 1
    return p


def cauchy_midpoints(count):
    # Uniform angular measure under s=1/(1-z) becomes the Cauchy law nu.
    theta = 2.0 * pi * (np.arange(count) + 0.5) / count
    return 0.5 / np.tan(theta / 2.0)


def sample_selector(t):
    return 1.0 / (1.0 + t * t)


def kernel_values(t, phi, y):
    return np.cos(np.outer(y, t)) @ phi / len(t)


def check_dual_identity():
    X = 60
    theta_count = 1 << 15
    quadrature_count = 320
    t = cauchy_midpoints(theta_count)
    phi = sample_selector(t)
    c = float(phi.mean())

    # Gauss--Legendre integration in y for the continuous comparator.
    nodes, weights = np.polynomial.legendre.leggauss(quadrature_count)
    Y = log(X)
    y = 0.5 * Y * (nodes + 1.0)
    wy = 0.5 * Y * weights

    lam = mangoldt_sieve(X)
    ms = np.flatnonzero(lam > 0.0)
    logs = np.log(ms.astype(float))
    coeff = lam[ms] / logs

    # K at all discrete and continuous frequencies.
    K_m = kernel_values(t, phi, logs)
    K_y = kernel_values(t, phi, y)

    rhs_discrete = np.sum(coeff * (ms ** -0.5 * K_m - c / ms))
    rhs_continuous = np.sum(
        wy * (c - np.exp(y / 2.0) * K_y) / y
    )
    rhs = float(rhs_discrete + rhs_continuous)

    # Directly average u_X. Chunk the t-array to keep memory bounded.
    direct = 0.0
    chunk = 512
    for start in range(0, theta_count, chunk):
        tc = t[start : start + chunk]
        phic = phi[start : start + chunk]
        prime_part = (
            np.cos(np.outer(tc, logs))
            @ (coeff * ms ** -0.5)
            - np.sum(coeff / ms)
        )
        integrand = (
            1.0 - np.exp(y[None, :] / 2.0)
            * np.cos(np.outer(tc, y))
        ) / y[None, :]
        comparator = integrand @ wy
        direct += float(np.sum(phic * (prime_part + comparator)))
    direct /= theta_count
    assert abs(direct - rhs) < 2.0e-9, (direct, rhs)

    # Sample positive-definite matrices for K and k-K.
    frequencies = np.array([0.0, log(2.0), log(3.0), log(5.0), log(7.0)])
    differences = (frequencies[:, None] - frequencies[None, :]).ravel()
    K = kernel_values(t, phi, differences).reshape((5, 5))
    base = np.exp(
        -np.abs(frequencies[:, None] - frequencies[None, :]) / 2.0
    )
    eig_k = np.linalg.eigvalsh((K + K.T) / 2.0)
    complement = base - K
    eig_c = np.linalg.eigvalsh((complement + complement.T) / 2.0)
    assert eig_k.min() > -2.0e-12, eig_k
    assert eig_c.min() > -2.0e-12, eig_c
    return direct, rhs, eig_k.min(), eig_c.min()


def A(a):
    return 6**a + 1 - 3**a - 2**a


def check_remote_tower():
    rows = []
    for M in (100, 1000, 10000):
        P = next_prime(M)
        assert P > M and P > 6
        for a in range(1, 13):
            assert A(a) == (3**a - 1) * (2**a - 1)
            assert A(a) > 0
            b = log(P) * (P / 6.0) ** (a / 2.0) * A(a)
            assert b > 0.0

        sigma = 0.5 + log(6.0) / (2.0 * log(P))
        delta = log(1.5) / (2.0 * log(P))
        beta = 0.5 + delta
        defect = log(beta / (1.0 - beta))
        closed = log((log(P) + log(1.5)) / (log(P) - log(1.5)))
        assert 0.5 < beta < 1.0
        assert 0.5 < sigma < 1.0
        assert abs(defect - closed) < 2.0e-15

        # r_P(1-s)=1-r_P(s), and T_P(s)=6^{-r_P(s)}.
        s = 0.73 + 1.17j
        r = lambda z: 0.5 + log(P) / log(6.0) * (z - 0.5)
        T = lambda z: sqrt(P / 6.0) * np.exp(-z * log(P))
        assert abs(r(1.0 - s) - (1.0 - r(s))) < 2.0e-14
        assert abs(T(s) - np.exp(-r(s) * log(6.0))) < 2.0e-14

        # The added real zeros q=2,3 map to 1/2 +/- delta.
        s2 = 0.5 + log(6.0) / log(P) * (log(2.0) / log(6.0) - 0.5)
        s3 = 0.5 + log(6.0) / log(P) * (log(3.0) / log(6.0) - 0.5)
        assert abs(s2 - (0.5 - delta)) < 2.0e-15
        assert abs(s3 - (0.5 + delta)) < 2.0e-15

        # All altered norms exceed the prescribed exact prefix.
        altered = [P**a for a in range(1, 5)]
        assert min(altered) > M
        rows.append((M, P, sigma, beta, defect))
    return rows


def main():
    direct, rhs, eig_k, eig_c = check_dual_identity()
    rows = check_remote_tower()
    print("104_91 checker: PASS")
    print(f"dual identity: direct={direct:.12e}, Stieltjes={rhs:.12e}")
    print(f"sample PD minima: K={eig_k:.3e}, k-K={eig_c:.3e}")
    for M, P, sigma, beta, defect in rows:
        print(
            f"M={M:5d} P={P:5d} sigma={sigma:.9f} "
            f"beta={beta:.9f} D_P={defect:.9e}"
        )


if __name__ == "__main__":
    main()
