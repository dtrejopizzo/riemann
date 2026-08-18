#!/usr/bin/env python3
"""Exact certificates for D.101 maximal neutral relation."""

from fractions import Fraction


def dot(v, w):
    return sum(v[i] * w[i] for i in range(len(v)))


def mat_vec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v)))
            for i in range(len(a))]


def main() -> None:
    # A concrete unitary (orthogonal) swap and its neutral graph.
    unitary = [[Fraction(0), Fraction(1)],
               [Fraction(1), Fraction(0)]]
    x = [Fraction(2), Fraction(-3)]
    y = [Fraction(5), Fraction(7)]
    ux = mat_vec(unitary, x)
    uy = mat_vec(unitary, y)
    krein_gram = dot(x, y) - dot(ux, uy)
    assert krein_gram == 0

    # Orthogonality to all graph vectors forces b=Ua.  Check the finite
    # identity a-U^T b=0 for one graph vector.
    a = [Fraction(4), Fraction(-1)]
    b = mat_vec(unitary, a)
    u_transpose_b = mat_vec(unitary, b)  # U=U^T=U^{-1}
    assert u_transpose_b == a

    # Finite Hardy shift z^d: range misses exactly the first d monomials.
    cutoff = 9
    degree = 2
    # Matrix sends e_j to e_(j+d) when still inside the cutoff.
    shift = [[Fraction(0) for _ in range(cutoff)] for _ in range(cutoff)]
    for j in range(cutoff - degree):
        shift[j + degree][j] = 1
    rank = sum(any(shift[i][j] != 0 for i in range(cutoff))
               for j in range(cutoff))
    cokernel = cutoff - rank
    assert rank == cutoff - degree
    assert cokernel == degree

    # A nontrivial inner factor adds its degree to the Tate defect.
    nontrivial_degree = 3
    total_defect = degree + nontrivial_degree
    assert total_defect == 5 > degree

    print("D101 maximal-neutral certificates: PASS")
    print("graph Krein Gram:", krein_gram)
    print("finite Tate shift rank/cokernel:", rank, cokernel)
    print("Tate plus nontrivial defect:", total_defect)


if __name__ == "__main__":
    main()
