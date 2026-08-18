#!/usr/bin/env python3
"""Finite exhaustive checks for the negabinary assembly block."""

from itertools import product


def subset_sums(digits):
    return {
        sum(bit * digit for bit, digit in zip(bits, digits))
        for bits in product((0, 1), repeat=len(digits))
    }


def assembly_signature(matrix, row_digits, col_digits):
    """Polynomial exponent -> coefficient, omitting exponent zero."""
    polynomial = {}
    for i, row in enumerate(matrix):
        exponent = sum(bit * digit for bit, digit in zip(row, col_digits))
        if exponent == 0:
            continue
        polynomial[exponent] = polynomial.get(exponent, 0) + row_digits[i]
    return tuple(sorted(polynomial.items()))


def matrices(r, s):
    for flat in product((0, 1), repeat=r * s):
        yield tuple(tuple(flat[i * s + j] for j in range(s)) for i in range(r))


def main():
    for r in range(1, 9):
        digits = [(-2) ** i for i in range(r)]
        sums = subset_sums(digits)
        assert len(sums) == 2**r
        assert sums == set(range(min(sums), max(sums) + 1))
        maximum = max(abs(x) for x in sums)
        if r >= 2:
            assert 2 ** (r - 1) <= maximum < 2 ** (r + 1) / 3

    # Exhaustive injectivity.  The largest case has 2^16 matrices; the
    # general result is the reconstruction proof in the companion note.
    for r, s in [(1, 1), (2, 3), (3, 3), (3, 4), (4, 4)]:
        row_digits = [(-2) ** i for i in range(r)]
        col_digits = [(-2) ** j for j in range(s)]
        signatures = {
            assembly_signature(matrix, row_digits, col_digits)
            for matrix in matrices(r, s)
        }
        assert len(signatures) == 2 ** (r * s), (r, s, len(signatures))

    print("PASS: negabinary subset sums are unique contiguous intervals.")
    print("PASS: assembly signatures distinguish every tested binary matrix.")
    print("PASS: the certified mixed family has exactly 2^(r*s) elements.")


if __name__ == "__main__":
    main()
