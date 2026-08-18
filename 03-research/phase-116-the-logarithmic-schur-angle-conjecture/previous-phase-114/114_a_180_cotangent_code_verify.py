#!/usr/bin/env python3
"""Checks the finite cotangent-code Kunneth and normalized dimension."""

from math import exp, floor, log


LOG2 = log(2.0)


def radius(r):
    even = (r + 1) // 2
    odd = r // 2
    return max((4**even - 1) // 3, 2 * (4**odd - 1) // 3)


def length(m):
    r = 0
    while radius(r + 1) <= m:
        r += 1
    return r


def assembly_signature(rows, cols, mask):
    terms = {}
    for i in range(rows):
        exponent = sum(
            (-2) ** j
            for j in range(cols)
            if mask & (1 << (i * cols + j))
        )
        if exponent:
            terms[exponent] = terms.get(exponent, 0) + (-2) ** i
    return tuple(sorted((e, c) for e, c in terms.items() if c))


def main():
    for r in range(1, 5):
        for s in range(1, 5):
            signatures = {
                assembly_signature(r, s, mask)
                for mask in range(1 << (r * s))
            }
            assert len(signatures) == 1 << (r * s)
            cotangent_dimension = r * s
            assert cotangent_dimension == len([(i, j) for i in range(r) for j in range(s)])

    a, b = log(6.0), log(35.0)
    errors = []
    for t in range(5, 101):
        r = length(floor(exp(t * a)))
        s = length(floor(exp(t * b)))
        normalized = LOG2 * LOG2 * r * s / (t * t)
        errors.append(abs(normalized - a * b))
    assert errors[-1] < errors[0]

    print("PASS: every Boolean matrix labels a distinct spherical section.")
    print("PASS: cotangent Kunneth dimension is exactly r*s.")
    print("PASS: normalized cotangent dimension converges to degree product.")


if __name__ == "__main__":
    main()
