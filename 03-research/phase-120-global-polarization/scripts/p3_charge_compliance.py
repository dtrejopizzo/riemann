#!/usr/bin/env python3
"""Reconnaissance for the independently defined P3 charge-compliance Gram.

The matrix is positive by construction. Numerical eigenvalues are only an
audit of the implementation; they are not a row-(d) certificate.
"""

import math
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma


def primes_upto(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


PRIME_LIMIT = 1_000_000
prime_sum = math.fsum(math.log(p) / (p * (p - 1)) for p in primes_upto(PRIME_LIMIT))
kappa = float(0.5772156649015328606 + prime_sum)


def weight(gamma):
    return 1 / (2 * math.pi * (gamma * gamma + 0.25))


def gamma_gram(gamma):
    return float(np.real(digamma(0.25 + 0.5j * gamma)) - digamma(0.25))


def compliance(ell, em):
    def integrand(gamma):
        return math.sqrt(weight(gamma + ell) * weight(gamma + em)) / (kappa + gamma_gram(gamma))

    value, error = quad(integrand, -np.inf, np.inf, epsabs=2e-11, epsrel=2e-11, limit=500)
    assert error < 2e-9
    return value


def amplitude(q):
    # q is a prime power; recover its underlying prime.
    for p in primes_upto(int(q)):
        x = p
        j = 1
        while x < q:
            x *= p
            j += 1
        if x == q:
            return math.log(p) / math.sqrt(2 * math.pi) * p ** (-j / 2)
    raise ValueError(f"not a prime power: {q}")


def gram(labels):
    ells = [math.log(q) for q in labels]
    amps = [amplitude(q) for q in labels]
    out = np.empty((len(labels), len(labels)), dtype=float)
    for i in range(len(labels)):
        for j in range(i, len(labels)):
            value = amps[i] * amps[j] * compliance(ells[i], ells[j])
            out[i, j] = out[j, i] = float(value)
    return out


print(f"kappa_infty (primes <= {PRIME_LIMIT}, positive omitted tail): {kappa:.16f}")
for labels in ([2, 3], [2, 3, 4]):
    matrix = gram(labels)
    eig = np.linalg.eigvalsh(matrix)
    print(f"\nS={labels}")
    print(np.array2string(matrix, precision=12, suppress_small=False))
    print("eigenvalues:", np.array2string(eig, precision=12, suppress_small=False))
    assert eig[0] > -1e-11
