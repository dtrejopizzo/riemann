#!/usr/bin/env python3
"""Checks for 104_100: functional symmetry and the two-sheet correction.

The local quartet and sheet identities are exact algebraically (verified
numerically to roundoff). The final block evaluates only the explicit gamma
factor with a Stirling expansion; it is a diagnostic for the proved
asymptotic, not a computation involving zeta zeros.
"""

from __future__ import annotations

import cmath
import math


def monodromy_character_check() -> None:
    """R, C and RC all preserve the +2*pi*i logarithmic increment."""

    radius = 0.37
    theta0 = 0.23
    theta1 = theta0 + 2.0 * math.pi
    logr = math.log(radius)

    # Continuous (unwrapped) local logarithms for z, -z,
    # conjugate(log(conjugate z)), and conjugate(log(-conjugate z)).
    def values(theta: float) -> tuple[complex, complex, complex, complex]:
        base = complex(logr, theta)
        reflected = complex(logr, theta + math.pi)
        conjugated = complex(logr, theta)
        reflected_conjugated = complex(logr, theta - math.pi)
        return base, reflected, conjugated, reflected_conjugated

    vv0 = values(theta0)
    vv1 = values(theta1)
    target = 2j * math.pi
    for before, after in zip(vv0, vv1):
        assert abs((after - before) - target) < 2e-15
    print("R, C, and RC monodromy increments: all +2*pi*i")


def two_sheet_algebra_check() -> None:
    z = complex(1.37, -2.19)
    multiplicity = 4
    d = math.pi * multiplicity
    plus = z + 1j * d
    minus = z - 1j * d
    average = 0.5 * (abs(plus) ** 2 + abs(minus) ** 2)
    difference = abs(plus) ** 2 - abs(minus) ** 2
    assert abs(average - (abs(z) ** 2 + d * d)) < 2e-13
    assert abs(difference - 4.0 * d * z.imag) < 2e-13
    print(f"two-sheet diagonal={d*d:.12g}, signed difference={difference:.12g}")


def finite_arithmetic_reflection_check() -> None:
    """The finite reflected average is only Re/Im Pythagoras."""

    coefficients = {2: 0.7, 3: -0.2, 5: 1.1, 11: -0.6}

    def phi(s: complex) -> complex:
        return sum(a * n ** (-s) for n, a in coefficients.items())

    for t in (0.3, 2.7, 11.0):
        s = complex(0.5, t)
        value = phi(s)
        reflected = phi(1.0 - s)
        assert abs(reflected - value.conjugate()) < 2e-15
        symmetric = 0.5 * (value + reflected)
        antisymmetric = 0.5 * (value - reflected)
        assert abs(symmetric.imag) < 2e-15
        assert abs(antisymmetric.real) < 2e-15
        assert abs(abs(value) ** 2
                   - abs(symmetric) ** 2 - abs(antisymmetric) ** 2) < 2e-15
    print("finite arithmetic reflection: exact Re/Im Pythagoras")


def quartet_value(s: complex, b: float, gamma: float) -> complex:
    z = s - 0.5
    numerator = ((z - 1j * gamma) ** 2 - b * b)
    numerator *= ((z + 1j * gamma) ** 2 - b * b)
    return -numerator / (b * b * (4.0 * gamma * gamma + b * b))


def exact_completion_falsifier_check() -> None:
    b = 0.2
    gamma = 7.0
    multiplicity = 3
    s0 = complex(0.5, gamma)

    # Functional equation and real type.
    probes = [
        complex(0.71, 0.3),
        complex(-0.2, 1.1),
        complex(1.8, -2.4),
    ]
    for s in probes:
        q = quartet_value(s, b, gamma)
        assert abs(quartet_value(1.0 - s, b, gamma) - q) < 2e-11
        assert abs(quartet_value(s.conjugate(), b, gamma) - q.conjugate()) < 2e-11

    assert abs(quartet_value(s0, b, gamma) + 1.0) < 2e-13

    roots = [
        complex(0.5 + b, gamma),
        complex(0.5 - b, gamma),
        complex(0.5 + b, -gamma),
        complex(0.5 - b, -gamma),
    ]
    for root in roots:
        assert abs(quartet_value(root, b, gamma)) < 2e-10

    # At Q(s0)=-1 the symmetric log boundary values of Q^m are +/-pi*i*m.
    c = -math.pi * multiplicity / gamma
    correction = c * (s0 - 0.5)
    log_plus = 1j * math.pi * multiplicity
    log_minus = -1j * math.pi * multiplicity
    phi_plus = log_plus + correction
    phi_minus = log_minus + correction
    assert abs(phi_plus) < 2e-15
    assert abs(phi_minus + 2j * math.pi * multiplicity) < 2e-15

    avg = 0.5 * (abs(phi_plus) ** 2 + abs(phi_minus) ** 2)
    midpoint = correction
    expected = abs(midpoint) ** 2 + (math.pi * multiplicity) ** 2
    assert abs(avg - expected) < 2e-12
    print("functional quartet: one sheet=0, opposite sheet=2*pi*m (exact model)")


def loggamma_stirling(z: complex) -> complex:
    """Stirling log-Gamma through z^-9; z stays in the upper half-plane."""

    inv = 1.0 / z
    # Bernoulli correction sum B_{2k}/(2k(2k-1) z^(2k-1)).
    correction = (
        inv / 12.0
        - inv ** 3 / 360.0
        + inv ** 5 / 1260.0
        - inv ** 7 / 1680.0
        + inv ** 9 / 1188.0
    )
    return ((z - 0.5) * cmath.log(z) - z
            + 0.5 * math.log(2.0 * math.pi) + correction)


def log_abs_completion(t: float) -> float:
    s = complex(0.5, t)
    log_c = (-math.log(2.0) + cmath.log(s) + cmath.log(s - 1.0)
             - 0.5 * s * math.log(math.pi) + loggamma_stirling(0.5 * s))
    return log_c.real


def gamma_energy_scale_check() -> None:
    previous_ratio_error = None
    for t in (50.0, 200.0, 1000.0, 5000.0):
        lc = log_abs_completion(t)
        ratio_error = abs(lc / t + math.pi / 4.0)
        centered = lc + math.pi * t / 4.0 - 1.75 * math.log(t)
        energy_density = (-lc) ** 2 / (t * t + 0.25)
        # The logarithmic correction is still visible at t=50; the density
        # increases to pi^2/16.  A coarse positive floor is enough here.
        assert energy_density > 0.40
        if previous_ratio_error is not None:
            assert ratio_error < previous_ratio_error
        previous_ratio_error = ratio_error
        print(
            f"t={t:7.1f}  log|C|/t={lc/t:+.12f}  "
            f"centered={centered:+.9f}  density={energy_density:.9f}"
        )
    assert previous_ratio_error is not None and previous_ratio_error < 0.004
    print(f"target -pi/4={-math.pi/4.0:+.12f}; target density pi^2/16={math.pi**2/16:.9f}")


def main() -> None:
    monodromy_character_check()
    two_sheet_algebra_check()
    finite_arithmetic_reflection_check()
    exact_completion_falsifier_check()
    gamma_energy_scale_check()
    print("all 104_100 checks passed")


if __name__ == "__main__":
    main()
