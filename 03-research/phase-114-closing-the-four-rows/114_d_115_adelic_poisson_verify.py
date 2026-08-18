#!/usr/bin/env python3
"""Exact certificates for D.115 adelic Poisson/Markov audit."""

from fractions import Fraction


def divisor_count(n: int) -> int:
    return sum(n % d == 0 for d in range(1, n + 1))


def mangoldt_support(n: int) -> bool:
    """Whether n is a power of one prime (value itself is not needed)."""
    if n < 2:
        return False
    prime = None
    m = n
    d = 2
    while d * d <= m:
        if m % d == 0:
            if prime is not None and prime != d:
                return False
            prime = d
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        if prime is not None and prime != m:
            return False
        prime = m
    return prime is not None


def main() -> None:
    # Exact L2-unboundedness ratio for triangular Fourier packets.
    # ||phi||_2^2=2/3, N packets of width epsilon, and N unit samples.
    epsilon = Fraction(1, 100)
    n_packets = 17
    ambient_norm_sq = Fraction(2, 3) * n_packets * epsilon
    sampled_norm_sq = Fraction(n_packets)
    ratio_sq = sampled_norm_sq / ambient_norm_sq
    assert ratio_sq == Fraction(3, 2) / epsilon == 150

    # Positive zeta-square covariance gives d(n), not Lambda support.
    assert divisor_count(6) == 4
    assert not mangoldt_support(6)
    assert divisor_count(8) == 4
    assert mangoldt_support(8)

    # Rank-two conditioning cannot alter a quadratic form on ker L.
    # Finite exact toy: L selects the first two coordinates.
    x = [Fraction(0), Fraction(0), Fraction(2), Fraction(-3), Fraction(5)]
    # K=I and K_cond=diag(0,0,1,1,1).
    original = sum(v * v for v in x)
    conditioned = sum(v * v for v in x[2:])
    assert original == conditioned == 38

    # A positive covariance followed by a logarithmic derivative need not
    # stay positive: scalar path z(t)=1+t has (log z)''<0 at zero.
    log_second_derivative_at_zero = Fraction(-1)
    assert log_second_derivative_at_zero < 0

    print("D115 adelic Poisson certificates: PASS")
    print("periodization squared-norm ratio:", ratio_sq)
    print("d(6) versus Mangoldt support:", divisor_count(6), mangoldt_support(6))
    print("rank-two conditioning primitive value:", conditioned)
    print("logarithmic-derivative positivity toy:", log_second_derivative_at_zero)


if __name__ == "__main__":
    main()
