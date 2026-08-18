#!/usr/bin/env python3
"""Exact certificates for the constrained Schur/inertia identity in D.47."""

from __future__ import annotations

import sympy as sp


def inertia_symmetric(a: sp.Matrix) -> tuple[int, int, int]:
    """Inertia from exact eigenvalues for the small rational certificates below."""
    positive = negative = zero = 0
    for eigenvalue, multiplicity in a.eigenvals().items():
        sign = sp.signsimp(eigenvalue)
        if sign.is_positive:
            positive += multiplicity
        elif sign.is_negative:
            negative += multiplicity
        elif sign.is_zero:
            zero += multiplicity
        else:
            numeric = complex(sp.N(eigenvalue, 80))
            assert abs(numeric.imag) < 1e-60
            if numeric.real > 0:
                positive += multiplicity
            elif numeric.real < 0:
                negative += multiplicity
            else:
                zero += multiplicity
    return positive, negative, zero


def certify(a: sp.Matrix, m: sp.Matrix) -> None:
    g = sp.simplify(m * a.inv() * m.T)
    assert g.det() != 0
    r = sp.simplify(a.inv() * m.T * g.inv())
    assert sp.simplify(m * r) == sp.eye(m.rows)

    kcols = sp.Matrix.hstack(*m.nullspace())
    assert sp.simplify(kcols.T * a * r) == sp.zeros(kcols.cols, r.cols)
    assert sp.simplify(r.T * a * r) == sp.simplify(g.inv())

    ak = sp.simplify(kcols.T * a * kcols)
    ia = inertia_symmetric(a)
    ig = inertia_symmetric(g)
    ik = inertia_symmetric(ak)
    assert tuple(ik[j] + ig[j] for j in range(3)) == ia
    print(f"PASS In(A)={ia}, In(G)={ig}, In(A|ker M)={ik}")


def main() -> None:
    a = sp.diag(5, 3, -2, -4, -7)

    # An indefinite boundary Green matrix checks the full subtraction law.
    m_indef = sp.Matrix([[1, 0, 1, 0, 0], [0, 1, 0, 1, 0]])
    certify(a, m_indef)

    # Hodge index one plus a hyperbolic boundary Green matrix leaves a
    # negative primitive kernel.
    a_hodge = sp.diag(5, -3, -2, -4, -7)
    m_hodge = sp.Matrix([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]])
    certify(a_hodge, m_hodge)


if __name__ == "__main__":
    main()
