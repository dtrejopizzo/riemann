#!/usr/bin/env python3
"""Exact rational checks for 104_60.

The analytic density criterion is proved in the document.  This checker
audits the rational off-line quartet w=2i and the saturated one-sided
barrier with the subexponential test scale b_n=n^2.
"""

from fractions import Fraction as F


def gaussian_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def gaussian_inv(a):
    norm = a[0] * a[0] + a[1] * a[1]
    return (a[0] / norm, -a[1] / norm)


def gaussian_pow(a, n):
    if n < 0:
        return gaussian_pow(gaussian_inv(a), -n)
    out = (F(1), F(0))
    base = a
    while n:
        if n & 1:
            out = gaussian_mul(out, base)
        base = gaussian_mul(base, base)
        n //= 2
    return out


def quartet_q(n):
    w = (F(0), F(2))
    return F(4) - 2 * (gaussian_pow(w, n)[0]
                       + gaussian_pow(w, -n)[0])


def quartet_d(n):
    return 4 * quartet_q(n)


def saturated_barrier(n):
    """H_{n,b} for D=4Q and b_n=n^2, exactly."""
    defect = max(F(0), -quartet_d(n))
    scale = F(n * n)
    return defect / (scale + defect)


def main():
    # Exact sign classification: the bad indices are precisely 0 mod 4.
    for n in range(1, 257):
        expected_bad = n % 4 == 0
        assert (quartet_d(n) < 0) == expected_bad
        assert (saturated_barrier(n) > 0) == expected_bad

    # The smallest bad normalized defect occurs at n=4 in the sampled
    # range; its barrier is 225/257.  The document proves exponential
    # growth, so the bad-class barrier tends to one.
    assert -quartet_d(4) / F(4 * 4) == F(225, 32)
    assert saturated_barrier(4) == F(225, 257)
    for n in range(4, 257, 4):
        assert saturated_barrier(n) >= F(225, 257)

    # Exact finite averages are bounded away from zero, while the bad
    # count is exactly floor(N/4).  Display convergence toward 1/4.
    rows = []
    for N in (16, 32, 64, 128, 256):
        bad_count = sum(quartet_d(n) < 0 for n in range(1, N + 1))
        assert bad_count == N // 4
        avg = sum((saturated_barrier(n) for n in range(1, N + 1)), F()) / N
        assert avg >= F(N // 4, N) * F(225, 257)
        assert avg < F(1, 4)
        rows.append((N, avg))

    # The averages increase along these dyadic rows and are already close
    # to the exact limiting density 1/4.
    assert all(rows[j][1] < rows[j + 1][1]
               for j in range(len(rows) - 1))
    assert F(1, 4) - rows[-1][1] < F(1, 1000)

    print("PASS: D_n^O<0 exactly on n=0 mod 4 (n<=256 checked)")
    print("PASS: H_4=225/257 and every sampled bad barrier is at least H_4")
    for N, avg in rows:
        # The Fraction is retained for every assertion.  Printing its exact
        # numerator at N=256 would exceed Python's safe integer-string limit.
        print(f"N={N:3d} exact-rational average decimal={float(avg):.12f}")
    print("PASS: dyadic averages approach the off-line density 1/4")
    print("All sign decisions use exact rational Gaussian arithmetic.")


if __name__ == "__main__":
    main()
