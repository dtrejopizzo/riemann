#!/usr/bin/env python3
"""Exact algebra checks for the epsilon-flow observability stop-gate.

All identities used for PASS/FAIL are evaluated with ``Fraction``.  The
script checks

* the Laguerre three-term recurrence giving Q=-M_x;
* the same epsilon-flow for the explicit pole coefficients;
* the rational generating function of the backward-transported prefix;
* the exact hard-edge leakage of the finite flag at its base M.

It is a companion check, not a proof of A1 or RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


Poly = list[Fraction]
Laurent = dict[int, Fraction]


def trim(poly: Poly) -> Poly:
    out = poly[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_add(left: Poly, right: Poly, scale: Fraction = Fraction(1)) -> Poly:
    out = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += scale * value
    return trim(out)


def poly_scale(poly: Poly, scale: Fraction) -> Poly:
    return trim([scale * value for value in poly])


def poly_mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def poly_pow(poly: Poly, exponent: int) -> Poly:
    out = [Fraction(1)]
    base = poly[:]
    power = exponent
    while power:
        if power & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        power >>= 1
    return out


def laguerre(n: int) -> Poly:
    return [
        Fraction((-1) ** degree * comb(n, degree), factorial(degree))
        for degree in range(n + 1)
    ]


def x_times(poly: Poly) -> Poly:
    return [Fraction(0)] + poly


def prefix(n: int) -> Poly:
    out = [Fraction(0)]
    for degree in range(n):
        out = poly_add(out, laguerre(degree))
    return out


def divide_one_minus_z(poly: Poly) -> Poly:
    """Return h with (1-z)h=poly; require poly(1)=0."""
    if sum(poly, Fraction(0)) != 0:
        raise AssertionError("polynomial is not divisible by 1-z")
    if len(poly) == 1:
        return [Fraction(0)]
    out = [Fraction(0)] * (len(poly) - 1)
    out[0] = poly[0]
    for degree in range(1, len(out)):
        out[degree] = poly[degree] + out[degree - 1]
    if poly[-1] != -out[-1]:
        raise AssertionError("division remainder")
    return trim(out)


def rational_series(numerator: Poly, denominator: Poly, terms: int) -> Poly:
    if denominator[0] == 0:
        raise ZeroDivisionError("zero constant denominator")
    out = [Fraction(0)] * terms
    for degree in range(terms):
        rhs = numerator[degree] if degree < len(numerator) else Fraction(0)
        for offset in range(1, min(degree, len(denominator) - 1) + 1):
            rhs -= denominator[offset] * out[degree - offset]
        out[degree] = rhs / denominator[0]
    return out


def direct_backward_coefficient(n: int, k: int, epsilon: Fraction) -> Fraction:
    """Integral e^{-(1-eps)x} L_{n-1}^{(1)}(x)L_k(x) dx."""
    rate = 1 - epsilon
    if rate <= 0:
        raise ValueError("the coefficient integral requires epsilon < 1")
    product = poly_mul(prefix(n), laguerre(k))
    total = Fraction(0)
    for degree, coefficient in enumerate(product):
        total += coefficient * factorial(degree) / rate ** (degree + 1)
    return total


def backward_series(n: int, epsilon: Fraction, terms: int) -> Poly:
    # D=1-eps+eps*z and N=-eps+(1+eps)*z.  The generating
    # function is (D^n-N^n)/((1-z)D^n).
    denominator_linear = [1 - epsilon, epsilon]
    numerator_linear = [-epsilon, 1 + epsilon]
    denominator = poly_pow(denominator_linear, n)
    difference = poly_add(
        denominator, poly_pow(numerator_linear, n), scale=Fraction(-1)
    )
    numerator = divide_one_minus_z(difference)
    return rational_series(numerator, denominator, terms)


def laurent_add(left: Laurent, right: Laurent, scale: Fraction = Fraction(1)) -> Laurent:
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, Fraction(0)) + scale * coefficient
        if out[exponent] == 0:
            del out[exponent]
    return out


def laurent_scale(poly: Laurent, scale: Fraction) -> Laurent:
    return {exponent: scale * coefficient for exponent, coefficient in poly.items() if scale * coefficient}


def laurent_derivative(poly: Laurent) -> Laurent:
    return {
        exponent - 1: exponent * coefficient
        for exponent, coefficient in poly.items()
        if exponent * coefficient
    }


def pole_coefficient(n: int) -> Laurent:
    # (epsilon-1)^n / epsilon^(n+1)
    return {
        degree - n - 1: Fraction(comb(n, degree) * (-1) ** (n - degree))
        for degree in range(n + 1)
    }


def q_on_coefficients(coefficients: list[Fraction]) -> list[Fraction]:
    """Coefficient action of Q=-M_x in the ordinary Laguerre basis."""
    out = [Fraction(0)] * (len(coefficients) + 1)
    for k, value in enumerate(coefficients):
        out[k] -= (2 * k + 1) * value
        if k:
            out[k - 1] += k * value
        out[k + 1] += (k + 1) * value
    return out


def flag_projection(vector: list[Fraction], base: int) -> list[Fraction]:
    """L2 projection onto span{sum_{j<base}L_j,L_base,L_{base+1},...}."""
    out = vector[:]
    average = sum(vector[:base], Fraction(0)) / base
    out[:base] = [average] * base
    return out


def squared_norm(vector: list[Fraction]) -> Fraction:
    return sum((value * value for value in vector), Fraction(0))


def verify_laguerre_recurrence(limit: int = 14) -> None:
    zero = [Fraction(0)]
    for n in range(limit + 1):
        rhs = poly_add(
            poly_scale(laguerre(n + 1), Fraction(n + 1)),
            poly_scale(laguerre(n), Fraction(-(2 * n + 1))),
        )
        if n:
            rhs = poly_add(rhs, poly_scale(laguerre(n - 1), Fraction(n)))
        if trim(rhs) != trim(poly_scale(x_times(laguerre(n)), Fraction(-1))):
            raise AssertionError(("Laguerre recurrence", n, rhs, zero))


def verify_pole_flow(limit: int = 14) -> None:
    for n in range(limit + 1):
        rhs = laurent_add(
            laurent_scale(pole_coefficient(n + 1), Fraction(n + 1)),
            laurent_scale(pole_coefficient(n), Fraction(-(2 * n + 1))),
        )
        if n:
            rhs = laurent_add(rhs, laurent_scale(pole_coefficient(n - 1), Fraction(n)))
        lhs = laurent_derivative(pole_coefficient(n))
        if lhs != rhs:
            raise AssertionError(("pole flow", n, lhs, rhs))


def verify_backward_generating_function() -> None:
    for epsilon in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
        for n in range(1, 7):
            generated = backward_series(n, epsilon, 14)
            direct = [direct_backward_coefficient(n, k, epsilon) for k in range(14)]
            if generated != direct:
                raise AssertionError(("backward series", epsilon, n))

    # The n=1 coefficients are exactly (-eps)^k/(1-eps)^(k+1).
    for epsilon in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
        generated = backward_series(1, epsilon, 12)
        expected = [(-epsilon) ** k / (1 - epsilon) ** (k + 1) for k in range(12)]
        if generated != expected:
            raise AssertionError(("n=1 closed form", epsilon))


def verify_flag_leakage(base: int = 150) -> None:
    prefix_coefficients = [Fraction(1)] * base
    q_prefix = q_on_coefficients(prefix_coefficients)
    projected = flag_projection(q_prefix, base)
    residual = [left - right for left, right in zip(q_prefix, projected)]
    if squared_norm(residual) != base * (base - 1):
        raise AssertionError(("flag leakage", squared_norm(residual)))

    # Q p_M = M(L_M-L_{M-1}); P_flag Qp_M=-p_M+M L_M.
    expected_q = [Fraction(0)] * (base + 1)
    expected_q[base - 1] = -base
    expected_q[base] = base
    if q_prefix != expected_q:
        raise AssertionError("Q prefix formula")
    expected_projection = [Fraction(-1)] * base + [Fraction(base)]
    if projected != expected_projection:
        raise AssertionError("compressed Q prefix formula")


def main() -> None:
    verify_laguerre_recurrence()
    verify_pole_flow()
    verify_backward_generating_function()
    verify_flag_leakage()

    print("PASS: -x L_n=(n+1)L_{n+1}-(2n+1)L_n+nL_{n-1}")
    print("PASS: pole coefficients obey the identical epsilon flow")
    print("PASS: backward-prefix rational generating function (exact Fraction)")
    print("PASS: for M=150, ||(I-P_flag)Q p_M||^2=M(M-1)=22350")
    print("THRESHOLD: r=epsilon/(1-epsilon) is <,=,> 1 at epsilon <,=,> 1/2")
    print("ENDPOINT: for n=1 and epsilon=1/2, |a_k|=2 and sum_{k<N}|a_k|^2=4N")
    print("STOP: H_flag is not Q-invariant; logarithmic Delta A weights do not move r=1")


if __name__ == "__main__":
    main()
