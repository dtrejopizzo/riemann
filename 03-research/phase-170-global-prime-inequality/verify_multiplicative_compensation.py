#!/usr/bin/env python3
"""Algebra checks for R170_501; no certificate of Weil positivity."""

import argparse
import cmath
from fractions import Fraction
import json
import math
from pathlib import Path

import numpy as np


def mangoldt(n):
    for p in range(2, n + 1):
        if n % p == 0:
            rest = n
            while rest % p == 0:
                rest //= p
            return math.log(p) if rest == 1 else 0.0
    return 0.0


def twist_check():
    maximum = 0.0
    for theta in (-1.25, 0.0, 0.3, 2.0):
        for n in range(1, 81):
            lhs = sum(mangoldt(d) * cmath.exp(1j * theta * math.log(d))
                      * cmath.exp(1j * theta * math.log(n // d))
                      for d in range(1, n + 1) if n % d == 0)
            rhs = math.log(n) * cmath.exp(1j * theta * math.log(n))
            error = abs(lhs - rhs)
            maximum = max(maximum, error)
            assert error < 1e-12
    return maximum


def phase_orbit(H, X, theta):
    values, vectors = np.linalg.eigh(X)
    U = (vectors * np.exp(1j * theta * values)) @ vectors.T.conj()
    return U.conj().T @ H @ U, U


def compensation_check():
    H = np.diag([0.0, 2.0, 5.0])
    X = np.array([[0, 1/2, 1/3], [1/2, 0, 1/4], [1/3, 1/4, 0]])
    V = 1j * (H @ X - X @ H)
    R = X @ H @ X - (H @ X @ X + X @ X @ H) / 2
    P = np.diag([1.0, 0.0, 0.0])
    inverse_on_complement = np.diag([0.0, 1/2, 1/5])
    schur = P @ V @ inverse_on_complement @ V @ P
    residual = float(np.linalg.norm(P @ R @ P - schur, 2))
    assert residual < 1e-14
    exact = 2 * Fraction(1, 2) ** 2 + 5 * Fraction(1, 3) ** 2
    assert exact == Fraction(19, 18)
    assert abs(R[0, 0] - float(exact)) < 1e-14
    theta = 1e-3
    plus, U = phase_orbit(H, X, theta)
    minus, _ = phase_orbit(H, X, -theta)
    first = (plus - minus) / (2 * theta)
    second_coefficient = (plus + minus - 2 * H) / (2 * theta ** 2)
    assert np.linalg.norm(first - V, 2) < 1e-6
    assert np.linalg.norm(second_coefficient - R, 2) < 1e-6
    transported_kernel = U.conj().T @ np.array([1.0, 0.0, 0.0])
    assert np.linalg.norm(plus @ transported_kernel) < 1e-13
    return dict(schur_residual=residual, exact_compensation=str(exact),
                first_derivative_error=float(np.linalg.norm(first - V, 2)),
                second_coefficient_error=float(np.linalg.norm(second_coefficient - R, 2)))


def negative_orbit_check():
    H = np.diag([-1.0, 2.0, 5.0])
    X = np.array([[0, 1/2, 1/3], [1/2, 0, 1/4], [1/3, 1/4, 0]])
    spectra = []
    for theta in (0.0, 0.3, 1.2, -2.0):
        orbit, _ = phase_orbit(H, X, theta)
        values = np.linalg.eigvalsh(orbit)
        assert np.max(np.abs(values - [-1, 2, 5])) < 1e-12
        spectra.append(dict(theta=theta, eigenvalues=values.tolist()))
    return spectra


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = dict(
        status='PASS: covariance/compensation checks; no arithmetic sign law proved',
        maximum_twisted_divisor_error=twist_check(),
        contact_compensation=compensation_check(),
        negative_spectrum_orbits=negative_orbit_check(),
        scope='Finite matrix models test operator algebra, not a continuum Galerkin enclosure.',
    )
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'])
    print('Exact contact compensation:', result['contact_compensation']['exact_compensation'])
    print('Schur residual:', result['contact_compensation']['schur_residual'])
    print('Negative eigenvalue persists in all four unitary orbits.')


if __name__ == '__main__':
    main()
