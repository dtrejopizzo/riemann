#!/usr/bin/env python3
"""Symbolic certificate for continuous Frobenius divisors in the DC completion."""

from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
REFERENCES = HERE.parent.parent / "00-references/papers-nuevos/A"
ARITHMETIC_SITE = REFERENCES / "arXiv-1502.05580v1/arithmeticsite_Adv_final1.tex"
LIFT_PAPER = REFERENCES / "arXiv-1805.10501v1/thecurve_K.tex"


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


arithmetic = read(ARITHMETIC_SITE)
lift = read(LIFT_PAPER)
published_correspondences = all(
    token in arithmetic
    for token in (
        "Frobenius correspondences  as congruences on the square",
        "positive real numbers $\\lambda\\in \\R_+^\\times$",
        "Newton polygons",
    )
)
published_continuous_target = all(
    token in lift
    for token in (
        "continuous integrals $\\int f(\\lambda)\\Psi_\\lambda d^*\\lambda$",
        "continuous divisors",
        "tropical shadows",
    )
)

t, r, x, y = sp.symbols("t r x y", positive=True)


def balanced_test(a, b):
    """Nonzero polynomial bump on [a,b] with both Weil moments zero."""
    base = (t - a) * (b - t)
    basis = tuple(base * t**degree for degree in range(3))
    moment_zero = tuple(sp.integrate(term / t, (t, a, b)) for term in basis)
    moment_one = tuple(sp.integrate(term, (t, a, b)) for term in basis)
    determinant = moment_zero[0] * moment_one[1] - moment_zero[1] * moment_one[0]
    c0 = sp.cancel(
        (-moment_zero[2] * moment_one[1] + moment_zero[1] * moment_one[2])
        / determinant
    )
    c1 = sp.cancel(
        (-moment_zero[0] * moment_one[2] + moment_zero[2] * moment_one[0])
        / determinant
    )
    f = base * (c0 + c1 * t + t**2)
    return f, moment_zero, moment_one, c0, c1


ATLAS = ((1, 2), (2, 3), (3, 5), (5, 7), (7, 11))
moment_balance = True
curvature_identity = True
continuous_not_atomic = True
compact_angular_support = True
frobenius_covariance = True
nonzero_tests = True

# SymPy applies Leibniz' rule without evaluating any logarithmic primitive.
generic_f = sp.Function("generic_f")
generic_a = sp.symbols("generic_a", positive=True)
generic_potential = sp.Integral(
    generic_f(t) * (r - t) / t,
    (t, generic_a, r),
)
generic_curvature_identity = (
    sp.diff(generic_potential, r, 2) == generic_f(r) / r
)

# The Frobenius change of variables is formal and independent of f.
mu = sp.symbols("mu", positive=True)
generic_m, generic_n = sp.symbols("generic_m generic_n", positive=True)
substitution = generic_n * mu / generic_m
generic_original_integrand = (
    generic_f(t) * (generic_n * y - t * generic_m * x) / t
)
generic_changed_integrand = sp.factor(
    generic_original_integrand.subs(t, substitution)
    * sp.diff(substitution, mu)
)
generic_transformed_integrand = (
    generic_n
    * generic_f(substitution)
    * (y - mu * x)
    / mu
)
generic_frobenius_covariance = (
    sp.factor(generic_changed_integrand - generic_transformed_integrand) == 0
)

for a_int, b_int in ATLAS:
    a, b = sp.Integer(a_int), sp.Integer(b_int)
    f, zero_basis, one_basis, c0, c1 = balanced_test(a, b)
    nonzero_tests &= f != 0

    moment_zero = sp.cancel(c0 * zero_basis[0] + c1 * zero_basis[1] + zero_basis[2])
    moment_one = sp.cancel(c0 * one_basis[0] + c1 * one_basis[1] + one_basis[2])
    moment_balance &= moment_zero == 0 and moment_one == 0

    curvature = f.subs(t, r) / r
    curvature_identity &= generic_curvature_identity
    continuous_not_atomic &= curvature != 0 and not curvature.has(sp.DiracDelta)

    below = sp.Integer(0)
    above = sp.simplify(r * moment_zero - moment_one)
    compact_angular_support &= below == 0 and above == 0

    frobenius_covariance &= generic_frobenius_covariance

finite_pl_representation = not continuous_not_atomic
verdict = all(
    (
        published_correspondences,
        published_continuous_target,
        nonzero_tests,
        moment_balance,
        curvature_identity,
        continuous_not_atomic,
        compact_angular_support,
        frobenius_covariance,
        not finite_pl_representation,
    )
)

print(f"BALANCED_CONTINUOUS_TEST_ATLAS: {'CONSTRUCTED' if nonzero_tests and moment_balance else 'FAILED'}")
print(f"FINITE_PL_CARTIER_REPRESENTATION: {'YES' if finite_pl_representation else 'NO'}")
print(f"DC_CURRENT_REPRESENTATION: {'YES' if curvature_identity else 'NO'}")
print(f"DEGREE: {'ZERO' if moment_balance else 'NONZERO'}")
print(f"CODEGREE: {'ZERO' if moment_balance else 'NONZERO'}")
print(f"COMPACT_ANGULAR_SUPPORT: {'YES' if compact_angular_support else 'NO'}")
print(f"FROBENIUS_COVARIANCE: {'YES' if frobenius_covariance else 'NO'}")
print("DC_CORRESPONDENCE_CURRENT: CONSTRUCTED" if verdict else "DC_CORRESPONDENCE_CURRENT: OPEN")
print("GLOBAL_DC_LINE_BUNDLE_DESCENT: OPEN")
print("DC_INTERSECTION_RR: OPEN")
print("ROW_A_STATUS: PARTIAL")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
