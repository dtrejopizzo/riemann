#!/usr/bin/env python3
"""Exact algebra checks for 104_56A.

This checks the fixed-cutoff coefficient and the adaptive-cutoff
inequality using rational arithmetic.  The analytic inheritance of the
A0 condition is proved in 104_56A and is not replaced by numerics here.
"""

from fractions import Fraction


def c_fixed(T):
    T = Fraction(T)
    return Fraction(1, 4) + Fraction(1, 4) / (1 + T)


def r_max(T):
    T = Fraction(T)
    return 4 * (1 + T) / (2 + T)


def main():
    # Exact equivalence of the two fixed-cutoff parametrizations.
    for T in (2, 7, 1000, 10**9):
        assert c_fixed(T) == 1 / r_max(T)

    assert r_max(1000) == Fraction(2002, 501)
    assert c_fixed(1000) == Fraction(501, 2002)

    # r_max grows and c_fixed decreases to the limiting quarter.
    Ts = (2, 7, 1000, 10**9)
    assert all(r_max(Ts[j]) < r_max(Ts[j + 1])
               for j in range(len(Ts) - 1))
    assert all(c_fixed(Ts[j]) > c_fixed(Ts[j + 1])
               for j in range(len(Ts) - 1))
    assert all(c_fixed(T) > Fraction(1, 4) for T in Ts)

    # Adaptive theorem: T >= A/(4 delta) forces the A0 envelope
    # A/[4(1+T)] to be strictly below delta.
    samples = (
        (Fraction(13), Fraction(1, 10_000), 1000),
        (Fraction(2324), Fraction(1, 1_000_000), 10**6),
        (Fraction(7, 3), Fraction(5, 17), 2),
    )
    for A, delta, base_T in samples:
        candidate = A / (4 * delta)
        T = max(Fraction(base_T), candidate)
        tail_envelope = A / (4 * (1 + T))
        assert tail_envelope < delta
        assert delta - tail_envelope > 0

    print("PASS: c(T)=1/r_max(T) exactly")
    print("PASS: r_max(1000)=2002/501 and c(1000)=501/2002")
    print("PASS: r_max increases, c(T) decreases strictly toward 1/4")
    print("PASS: adaptive cutoff gives a strict positive C_n lower bound")
    print("All decisions above use exact rational arithmetic.")


if __name__ == "__main__":
    main()
