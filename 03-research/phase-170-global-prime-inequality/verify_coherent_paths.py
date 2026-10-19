#!/usr/bin/env python3
"""Galerkin diagnostics for R170_301; NOT an interval certificate.

Uses normalized cell indicators on (-T,T). Archimedean matrix entries
come from the exact displacement kernel, integrated in floating point.
Inverse matrices refer to the Galerkin model, not to compressed inverses
of the infinite-dimensional operator. Only algebra and consistency are
tested here; positive trial matrices do not prove W_T >= 0.
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh, solve, toeplitz


M0 = -float(np.euler_gamma) - math.pi / 2 - 3 * math.log(2) - math.log(math.pi)


def kernel(u):
    return math.exp(-u / 2) / (-math.expm1(-2 * u))


def prime_powers(T):
    limit = math.ceil(math.exp(2 * T))
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            for n in range(p * p, limit + 1, p):
                sieve[n] = False
    result = []
    for p in range(2, limit + 1):
        if sieve[p]:
            n = p
            while n <= limit and math.log(n) < 2 * T:
                result.append((n, p, math.log(p) / math.sqrt(n)))
                n *= p
    return sorted(result)


def arch_matrix(T, size):
    h = 2 * T / size
    first = np.empty(size)
    err = 0.0
    integral, e = quad(lambda u: u * kernel(u) if u else 0.5,
                       0, h, epsabs=1e-12, epsrel=1e-12)
    tail = math.atanh(math.exp(-h / 2)) + math.atan(math.exp(-h / 2))
    first[0] = 2 * integral / h + 2 * tail
    err = max(err, 2 * e / h)
    for d in range(1, size):
        lo, mid, hi = (d - 1) * h, d * h, (d + 1) * h
        left, e1 = quad(
            lambda u: kernel(u) * (u - lo) / h if u else 0.5 / h,
            lo, mid, epsabs=1e-12, epsrel=1e-12)
        right, e2 = quad(lambda u: kernel(u) * (hi - u) / h,
                         mid, hi, epsabs=1e-12, epsrel=1e-12)
        first[d] = -left - right
        err = max(err, e1 + e2)
    return toeplitz(first), err


def build(T, size, replace_weights=None):
    h = 2 * T / size
    gamma, quadrature_estimate = arch_matrix(T, size)
    points = np.linspace(-T, T, size + 1)
    c = 2 * np.diff(np.sinh(points / 2)) / math.sqrt(h)
    s = 2 * np.diff(np.cosh(points / 2)) / math.sqrt(h)
    records = prime_powers(T) if replace_weights is None else replace_weights
    distances = (np.arange(size)[:, None] - np.arange(size)[None, :]) * h
    J = np.zeros((size, size))
    by_prime = {}
    A = 0.0
    for n, p, a in records:
        shift = np.maximum(0, 1 - np.abs(distances - math.log(n)) / h)
        atom = a * (shift + shift.T)
        J += atom
        by_prime[p] = by_prime.get(p, np.zeros_like(J)) + atom
        A += a
    ident = np.eye(size)
    B = gamma + 2 * A * ident + 2 * np.outer(c, c)
    E = B - J
    C = (2 * A - M0) * ident + 2 * np.outer(s, s)
    W_original = gamma + M0 * ident - J + 2 * np.outer(c, c) - 2 * np.outer(s, s)
    assert np.max(np.abs(E - C - W_original)) < 1e-11
    alpha = 2 * (math.atanh(math.exp(-T)) + math.atan(math.exp(-T)))
    assert eigh(gamma, eigvals_only=True)[0] >= alpha - 1e-10
    assert eigh(E, eigvals_only=True)[0] >= alpha - 1e-10
    # Independent support/correlation check on the normalized indicator.
    # Its exact quadratic value cannot depend on the cell refinement.
    constant = np.ones(size) / math.sqrt(size)
    direct_gamma = arch_matrix(T, 1)[0][0, 0]
    direct_prime = 2 * sum(a * max(0, 1 - math.log(n) / (2 * T))
                           for n, _, a in records)
    direct_polar = 16 * math.sinh(T / 2) ** 2 / T
    direct_W = direct_gamma + M0 - direct_prime + direct_polar
    assert abs(constant @ gamma @ constant - direct_gamma) < 1e-10
    assert abs(constant @ J @ constant - direct_prime) < 1e-10
    assert abs(constant @ W_original @ constant - direct_W) < 1e-10
    return dict(T=T, size=size, B=B, E=E, C=C, J=J, W=W_original,
                A=A, alpha=alpha, by_prime=by_prime,
                quadrature_estimate=quadrature_estimate)


def inverse_sqrt(matrix):
    values, vectors = eigh(matrix)
    assert values[0] > 0
    return (vectors * values ** -0.5) @ vectors.T


def diagnose(model):
    B, E, C, J = (model[key] for key in ('B', 'E', 'C', 'J'))
    alpha, A = model['alpha'], model['A']
    Bh = inverse_sqrt(B)
    cv, cu = eigh(C)
    Ch = (cu * np.sqrt(cv)) @ cu.T
    R = Bh @ J @ Bh
    rv, ru = eigh(R)
    r_bound = 2 * A / (2 * A + alpha)
    assert max(abs(rv)) <= r_bound + 1e-10
    Y = Bh @ Ch
    K = Ch @ solve(E, Ch, assume_a='pos')
    spectral = Y.T @ ((ru * (1 / (1 - rv))) @ ru.T) @ Y
    resolvent_error = float(np.linalg.norm(K - spectral, 2))
    assert resolvent_error < 1e-10
    # Positive pairs (orders 2j and 2j+1), keeping all mixed paths.
    pairs = 6
    scalar_partial = np.zeros_like(rv)
    power = np.ones_like(rv)
    for _ in range(pairs):
        increment = power * (1 + rv)
        assert np.min(increment) >= -1e-14
        scalar_partial += increment
        power *= rv * rv
    partial = Y.T @ ((ru * scalar_partial) @ ru.T) @ Y
    tail = (K - partial + (K - partial).T) / 2
    tail_values = eigh(tail, eigvals_only=True)
    bound = float(cv[-1] / alpha * r_bound ** (2 * pairs))
    assert tail_values[0] > -1e-10
    assert tail_values[-1] <= bound + 1e-10
    # Rayleigh quotient on the finite trial space: a diagnostic only.
    gain = float(eigh(C, E, eigvals_only=True)[-1])
    mixed = None
    if 2 in model['by_prime'] and 3 in model['by_prime']:
        Binv = Bh @ Bh
        cross = Binv @ model['by_prime'][2] @ Binv @ model['by_prime'][3] @ Binv
        mixed = float(np.linalg.norm(cross, 2))
        assert mixed > 1e-12
    return dict(
        T=model['T'], dimension=model['size'],
        lowest_trial_W=float(eigh(model['W'], eigvals_only=True)[0]),
        largest_trial_gain=gain,
        R_norm=float(max(abs(rv))), R_norm_bound=r_bound,
        coherent_2_then_3_path_norm=mixed,
        inverse_identity_error=resolvent_error,
        positive_pair_count=pairs,
        pair_tail_norm=float(tail_values[-1]), pair_tail_bound=bound,
        max_quad_error_estimate=model['quadrature_estimate'],
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    cases = [diagnose(build(T, size))
             for T in (0.5, math.log(5) / 2, 1.0, 1.5)
             for size in (24, 48)]
    # A falsifier for the idea that construction alone forces contractivity.
    falsifier = diagnose(build(1.0, 48, [(2, 2, 100.0)]))
    assert falsifier['largest_trial_gain'] > 1.1
    assert falsifier['lowest_trial_W'] < -1
    result = dict(
        status='PASS: floating Galerkin diagnostics, NOT a positivity certificate',
        cases=cases, arbitrary_weight_falsifier=falsifier,
        limitations=[
            'No interval arithmetic or infinite-dimensional Galerkin remainder.',
            'Quadrature error estimates are not rigorous enclosures.',
            'Finite inverses are not compressions of the continuum inverse.',
            'Positive trial W matrices do not prove positivity on the full form domain.',
        ],
    )
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    for case in cases:
        print(f"T={case['T']:.6f} N={case['dimension']:2d} "
              f"lambda_trial={case['lowest_trial_W']:.6g} "
              f"gain_trial={case['largest_trial_gain']:.9f} "
              f"mixed_2_3={case['coherent_2_then_3_path_norm']}")
    print('Falsifier gain:', falsifier['largest_trial_gain'])
    print(result['status'])


if __name__ == '__main__':
    main()
