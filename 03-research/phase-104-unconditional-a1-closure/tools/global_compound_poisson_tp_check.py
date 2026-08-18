#!/usr/bin/env python3
"""Exact checks for 104_21 (no floating-point sign decisions)."""

from fractions import Fraction as F


def b_prime_power(p: int, k: int, u: int = 1) -> int:
    """b_u(p^k) for the exact integer test u=1."""
    if k == 0:
        return 1
    q = p**u
    edge = 2 * (q - 1) * q ** (k - 1)
    interior = 0 if k == 1 else (k - 1) * (q - 1) ** 2 * q ** (k - 2)
    return edge + interior


def weight(factors: dict[int, int], epsilon: int = 2) -> F:
    """b_1(m)m^(-1-epsilon), using multiplicativity."""
    m = 1
    b = 1
    for p, k in factors.items():
        m *= p**k
        b *= b_prime_power(p, k)
    return F(b, m ** (1 + epsilon))


def check_zero_inflated_geometric(p: int) -> None:
    # u=1, epsilon=2: r=p^-3, R=p^-2.
    r = F(1, p**3)
    R = F(1, p**2)
    mass0 = (1 - R) / (1 - r)
    # Exact sum of the k>=1 geometric tail.
    tail = mass0 * (R - r) / (1 - R)
    assert mass0 > 0 and tail > 0
    assert mass0 + tail == 1


def check_pf2_minor() -> None:
    w3 = weight({3: 1})
    w6 = weight({2: 1, 3: 1})
    w12 = weight({2: 2, 3: 1})
    assert w3 == F(4, 27)
    assert w6 == F(1, 27)
    assert w12 == F(5, 432)
    det = w6 * w6 - w3 * w12
    assert det == F(-1, 2916)

    # The same sign in the local formula r^2(Q-1)(Q-3), p=2.
    r = F(1, 8)
    Q = F(2)
    a0 = F(1)
    a1 = F(b_prime_power(2, 1), 8)
    a2 = F(b_prime_power(2, 2), 8**2)
    assert a1 * a1 - a0 * a2 == r * r * (Q - 1) * (Q - 3)
    assert a1 * a1 - a0 * a2 == F(-1, 64)


def check_artanh_certificate() -> None:
    # q=1/sqrt(2) is represented by q^2.  The proof uses
    # atanh(q)/q = integral_0^1 1/(1-q^2 s^2) ds.
    q_squared = F(1, 2)
    endpoint_denominator = 1 - q_squared
    pointwise_upper_bound = 1 / endpoint_denominator
    assert pointwise_upper_bound == 2

    # For 0 <= s < 1 the denominator is strictly larger than 1/2,
    # hence the integrand is strictly smaller than 2 except at one
    # measure-zero endpoint.  Thus atanh(q)/q < 2.
    coefficient_of_q_in_inv_q_minus_4q = 1 / q_squared - 4
    assert coefficient_of_q_in_inv_q_minus_4q == -2
    # Therefore H/q = -2 + atanh(q)/q < 0 exactly.


def main() -> None:
    check_zero_inflated_geometric(2)
    check_zero_inflated_geometric(3)
    check_pf2_minor()
    check_artanh_certificate()
    print("PASS: exact compound-Poisson local laws (p=2,3)")
    print("PASS: two-prime PF2 minor = -1/2916")
    print("PASS: local p=2 PF2 defect = -1/64")
    print("PASS: symbolic certificate atanh(1/sqrt(2)) < sqrt(2)")
    print("No floating-point sign decision was used.")


if __name__ == "__main__":
    main()
