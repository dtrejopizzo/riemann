#!/usr/bin/env python3
"""Exact rational checks for the finite M1 max-energy stop gate.

This is not a numerical test of A1.  It checks the signs and the finite
boundary in 104_11, equations (6), (8), and (15a), on nontrivial rational
atomic measures and a nonmonotone polynomial weight.
"""

from fractions import Fraction as F


def p_eval(p, x):
    out = F(0)
    for coefficient in reversed(p):
        out = out * x + coefficient
    return out


def p_add(p, q):
    size = max(len(p), len(q))
    return [
        (p[k] if k < len(p) else F(0))
        + (q[k] if k < len(q) else F(0))
        for k in range(size)
    ]


def p_mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def p_derivative(p):
    return [F(k) * p[k] for k in range(1, len(p))]


def p_integral(p, left, right):
    return sum(
        coefficient * (right ** (k + 1) - left ** (k + 1)) / F(k + 1)
        for k, coefficient in enumerate(p)
    )


def prefix_integral(atoms, X, weight, mode):
    """Integrate E*w or E^2*w', where E=A-(x-1), exactly."""
    total = F(0)
    mass = F(0)
    left = F(1)
    derivative = p_derivative(weight)
    for point, atom_mass in atoms + [(X, F(0))]:
        e_poly = [mass + 1, -1]
        if mode == "linear":
            integrand = p_mul(e_poly, weight)
        elif mode == "square_derivative":
            integrand = p_mul(p_mul(e_poly, e_poly), derivative)
        else:
            raise ValueError(mode)
        total += p_integral(integrand, left, point)
        mass += atom_mass
        left = point
    return total


def max_double(atoms, weight):
    return sum(
        mass_x * mass_y * p_eval(weight, max(x, y))
        for x, mass_x in atoms
        for y, mass_y in atoms
    )


def mu_nu_cross(atoms, X, weight):
    primitive_total = p_integral(weight, F(1), X)
    out = F(0)
    for point, mass in atoms:
        tail = primitive_total - p_integral(weight, F(1), point)
        out += mass * ((point - 1) * p_eval(weight, point) + tail)
    return out


def check_measure(atoms, X, weight):
    mu_mu = max_double(atoms, weight)
    cross = mu_nu_cross(atoms, X, weight)
    nu_nu_half = p_integral(p_mul([-1, 1], weight), F(1), X)
    q_expanded = (mu_mu - 2 * cross + 2 * nu_nu_half) / 2

    total_mass = sum(mass for _, mass in atoms)
    e_X = total_mass - X + 1
    q_energy = (
        e_X * e_X * p_eval(weight, X)
        - prefix_integral(atoms, X, weight, "square_derivative")
    ) / 2
    assert q_expanded == q_energy

    first_moment = sum(
        mass * (point - 1) * p_eval(weight, point)
        for point, mass in atoms
    )
    s_value = first_moment - mu_mu / 2
    linear = -prefix_integral(atoms, X, weight, "linear")
    assert s_value + q_energy == linear
    return q_energy, linear


def check_hessian(eta, X, weight):
    cumulative = F(0)
    left = F(1)
    square_derivative = F(0)
    derivative = p_derivative(weight)
    for point, atom_mass in eta + [(X, F(0))]:
        square_derivative += cumulative * cumulative * p_integral(
            derivative, left, point
        )
        cumulative += atom_mass
        left = point
    lhs = max_double(eta, weight)
    rhs = cumulative * cumulative * p_eval(weight, X) - square_derivative
    assert lhs == rhs
    return lhs, rhs


def main():
    X = F(11)
    # w(x)=5-3x+2x^2-x^3 is deliberately nonmonotone on the interval.
    weight = [F(5), F(-3), F(2), F(-1)]
    mu = [(F(2), F(2)), (F(3), F(1)), (F(5), F(4)), (F(8), F(3))]
    eta_zero_mass = [(F(2), F(3)), (F(4), F(-5)), (F(7), F(2))]
    eta_with_boundary = [(F(2), F(3)), (F(4), F(-1)), (F(7), F(2))]

    q_value, linear = check_measure(mu, X, weight)
    hz = check_hessian(eta_zero_mass, X, weight)
    hb = check_hessian(eta_with_boundary, X, weight)
    print("Q_X(mu-dx) =", q_value)
    print("S_X+Q_X = -integral(Ew) =", linear)
    print("zero-mass Hessian identity =", hz[0])
    print("nonzero-boundary Hessian identity =", hb[0])
    print("EXACT_RATIONAL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
