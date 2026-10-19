#!/usr/bin/env python3
"""Response of the R170_301 gain; floating diagnostics, not a RH proof."""

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq

from verify_coherent_paths import build


def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign


def divisor_inversion_check():
    size = 30
    errors = [Fraction(0)] + [Fraction((-1) ** n, n + 1) for n in range(1, size + 1)]
    errors[1] = Fraction(0)
    delta = [sum((mobius(n // d) * errors[d] for d in range(1, n + 1) if n % d == 0),
                 Fraction(0)) for n in range(1, size + 1)]
    for n in range(1, size + 1):
        assert sum(delta[d - 1] for d in range(1, n + 1) if n % d == 0) == errors[n]
    return size


def response(T, size):
    model = build(T, size)
    E, C = model['E'], model['C']
    eigenvalues, vectors = eigh(C, E)
    gain, f = eigenvalues[-1], vectors[:, -1]
    gap = eigenvalues[-1] - eigenvalues[-2]
    assert gap > 1e-8  # The branch used in this numerical test is simple.
    assert abs(f @ E @ f - 1) < 1e-12
    h = 2 * T / size
    distances = (np.arange(size)[:, None] - np.arange(size)[None, :]) * h
    limit = math.ceil(math.exp(2 * T)) - 1
    shifts = {}
    derivatives = {}
    results = []
    eye = np.eye(size)
    step = 1e-5
    for n in range(2, limit + 1):
        shift = np.maximum(0, 1 - np.abs(distances - math.log(n)) / h)
        Hn = shift + shift.T
        shifts[n] = Hn
        dE, dC = 2 * eye - Hn, 2 * eye
        predicted = float(f @ (dC - gain * dE) @ f)
        plus = eigh(C + step * dC, E + step * dE, eigvals_only=True)[-1]
        minus = eigh(C - step * dC, E - step * dE, eigvals_only=True)[-1]
        observed = float((plus - minus) / (2 * step))
        assert abs(predicted - observed) < 1e-7
        derivatives[n] = predicted
        results.append(dict(n=n, derivative_a=predicted,
                            finite_difference=observed,
                            correlation=float(f @ Hn @ f / 2)))
    # Vary one divisor-error coordinate, then invert exactly to coefficient directions.
    divisor_results = []
    for d in (2, 3):
        weights = {n: mobius(n // d) / math.sqrt(n)
                   for n in shifts if n % d == 0}
        total = sum(weights.values())
        H = sum((a * shifts[n] for n, a in weights.items()), np.zeros_like(E))
        dE, dC = 2 * total * eye - H, 2 * total * eye
        predicted = sum(weights[n] * derivatives[n] for n in weights)
        observed = float((eigh(C + step * dC, E + step * dE, eigvals_only=True)[-1]
                          - eigh(C - step * dC, E - step * dE, eigvals_only=True)[-1]) / (2 * step))
        assert abs(predicted - observed) < 1e-7
        divisor_results.append(dict(d=d, derivative=predicted, finite_difference=observed))
    return dict(T=T, dimension=size, gain=float(gain), branch_gap=float(gap),
                coefficient_responses=results, divisor_error_responses=divisor_results)


def exact_tangent_check():
    # W=diag(0,2), D=[[0,1],[1,0]]. First variation on e1 is zero,
    # yet f+epsilon*(0,1/2) gives a strictly negative Rayleigh numerator.
    for epsilon in (Fraction(1, 10), Fraction(-1, 10), Fraction(1, 100)):
        y = epsilon / 2
        value = 2 * y * y - 2 * epsilon * y
        assert value == -epsilon * epsilon / 2 < 0
    return 'exact rational tangent test passed'


def tuned_contact_check():
    """An artificially tuned finite model, not a first contact for actual Λ."""
    T, size = 1.0, 48
    model = build(T, size)
    h = 2 * T / size
    distances = (np.arange(size)[:, None] - np.arange(size)[None, :]) * h

    def atom(n):
        shift = np.maximum(0, 1 - np.abs(distances - math.log(n)) / h)
        return shift + shift.T

    H2, H3 = atom(2), atom(3)
    W = model['W']
    delta = brentq(lambda x: eigh(W - x * H2, eigvals_only=True)[0], 0, 1,
                   xtol=1e-14)
    critical = W - delta * H2
    values, vectors = eigh(critical)
    assert abs(values[0]) < 1e-11 and values[1] > 1e-5
    f = vectors[:, 0]
    ratio = float((f @ H3 @ f) / (f @ H2 @ f))
    D = H3 - ratio * H2
    assert abs(f @ D @ f) < 1e-12
    coords = vectors[:, 1:].T @ D @ f
    g = vectors[:, 1:] @ (coords / values[1:])
    q = float(np.sum(coords * coords / values[1:]))
    assert q > 1e-8
    # Choose epsilon so the cubic contribution is at most a quarter of the quadratic.
    dgg = float(g @ D @ g)
    step = min(1e-2, q / (4 * max(abs(dgg), 1e-15)))
    trials = []
    for epsilon in (step, -step):
        trial = f + epsilon * g
        observed = float(trial @ (critical - epsilon * D) @ trial)
        predicted = -epsilon ** 2 * q - epsilon ** 3 * dgg
        assert abs(observed - predicted) < 1e-11
        assert observed < 0
        trials.append(dict(epsilon=epsilon, value=observed, predicted=predicted))
    return dict(label='artificially tuned finite Galerkin contact; not actual Λ',
                extra_a2=delta, tangent_ratio=ratio, quadratic_cost=q,
                positive_complement_gap=float(values[1]), trials=trials)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    cases = [response(T, 48) for T in (1.0, 1.5)]
    result = dict(status='PASS; floating Galerkin sensitivities, not a global sign certificate',
                  divisor_inversion_size=divisor_inversion_check(),
                  tangent_check=exact_tangent_check(),
                  tuned_contact=tuned_contact_check(), cases=cases)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    for case in cases:
        entries = case['coefficient_responses']
        low = min(entries, key=lambda row: row['derivative_a'])
        high = max(entries, key=lambda row: row['derivative_a'])
        print(f"T={case['T']} gain={case['gain']:.9f}: "
              f"min derivative n={low['n']} {low['derivative_a']:.6g}; "
              f"max derivative n={high['n']} {high['derivative_a']:.6g}")
    print(result['status'])
    print('Artificial contact: extra a2 =', result['tuned_contact']['extra_a2'],
          '; quadratic cost =', result['tuned_contact']['quadratic_cost'])


if __name__ == '__main__':
    main()
