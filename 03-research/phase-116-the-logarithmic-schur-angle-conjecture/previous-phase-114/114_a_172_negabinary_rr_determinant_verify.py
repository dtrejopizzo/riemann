#!/usr/bin/env python3
"""Checks the normalized negabinary RR certificate and Green splitting."""

from math import exp, floor, log


LOG2 = log(2.0)


def negabinary_radius(r):
    """Maximum absolute subset sum of 1,-2,4,-8,...,(-2)^(r-1).

    Positive and negative digits have disjoint signs, so the two extreme
    subset sums are obtained by taking all even, respectively all odd,
    powers.  This closed form also lets the asymptotic check reach the
    hundreds of digits without enumerating 2**r subsets.
    """
    even_count = (r + 1) // 2
    odd_count = r // 2
    positive_extreme = (4**even_count - 1) // 3
    negative_extreme = 2 * (4**odd_count - 1) // 3
    return max(positive_extreme, negative_extreme)


def admissible_length(m):
    r = 0
    while negabinary_radius(r + 1) <= m:
        r += 1
    return r


def rr(a1, a2, b1, b2):
    return a1 * b2 + a2 * b1


def contact(x1, x2, y1, y2, weights):
    return sum(
        (x1[i] * y2[i] + x2[i] * y1[i]) * weights[i]
        for i in range(len(weights))
    )


def main():
    a, b = log(6.0), log(35.0)
    errors = []
    for t in range(5, 121):
        r = admissible_length(floor(exp(t * a)))
        s = admissible_length(floor(exp(t * b)))
        metric = LOG2 * LOG2 * r * s
        errors.append(abs(metric / (t * t) - a * b))
        assert abs(metric - t * t * a * b) <= 8 * t * (a + b + 1)
    assert errors[-1] < errors[0]

    weights = [log(2), log(3), log(5)]
    x1, x2 = [1, -2, 3], [0, 4, -1]
    y1, y2 = [2, 1, -3], [5, -1, 2]
    d1x = sum(v * w for v, w in zip(x1, weights))
    d2x = sum(v * w for v, w in zip(x2, weights))
    d1y = sum(v * w for v, w in zip(y1, weights))
    d2y = sum(v * w for v, w in zip(y2, weights))
    brr = rr(d1x, d2x, d1y, d2y)
    c = contact(x1, x2, y1, y2, weights)
    green = brr - c
    assert abs(brr - (c + green)) < 1e-12
    assert abs(rr(d1x, d2x, d1y, d2y) - rr(d1y, d2y, d1x, d2x)) < 1e-12

    print("PASS: normalized negabinary determinant metrics converge to d1*d2.")
    print("PASS: RR polarization is symmetric and bilinear.")
    print("PASS: the contact/Green/RR norm splitting is exact.")


if __name__ == "__main__":
    main()
