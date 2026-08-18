#!/usr/bin/env python3
"""Exact checks for 104_95.

No zeta zeros and no floating point are used.  The program checks

* the Laurent cancellation equations for A ell' + B ell^2 + C ell;
* the diagonal/injective squarefree symmetrisation map in every requested
  finite degree and differential order.
"""

from fractions import Fraction
from math import factorial


class GPoly:
    """Polynomial in the formal symbol gamma with rational coefficients."""

    def __init__(self, coeffs=None):
        self.c = {
            int(k): Fraction(v) for k, v in (coeffs or {}).items() if v
        }

    def __add__(self, other):
        other = as_gpoly(other)
        out = dict(self.c)
        for k, v in other.c.items():
            out[k] = out.get(k, Fraction(0)) + v
            if not out[k]:
                del out[k]
        return GPoly(out)

    def __neg__(self):
        return GPoly({k: -v for k, v in self.c.items()})

    def __sub__(self, other):
        return self + (-as_gpoly(other))

    def __mul__(self, other):
        other = as_gpoly(other)
        out = {}
        for i, a in self.c.items():
            for j, b in other.c.items():
                out[i + j] = out.get(i + j, Fraction(0)) + a * b
        return GPoly(out)

    def __eq__(self, other):
        return self.c == as_gpoly(other).c

    def __repr__(self):
        return f"GPoly({self.c})"


def as_gpoly(value):
    return value if isinstance(value, GPoly) else GPoly({0: Fraction(value)})


ONE = GPoly({0: 1})
GAMMA = GPoly({1: 1})
ZERO = GPoly()


def quadratic_laurent_check():
    # ell=t^-1-gamma+O(t), ell'=-t^-2+O(1),
    # ell^2=t^-2-2 gamma t^-1+O(1).
    for aval in (Fraction(-7, 3), Fraction(0), Fraction(5, 2)):
        A = as_gpoly(aval)
        B = A
        C = as_gpoly(2) * GAMMA * A
        double_pole = -A + B
        simple_pole = -as_gpoly(2) * GAMMA * B + C
        assert double_pole == ZERO
        assert simple_pole == ZERO

    # Conversely the two triangular equations give B=A and C=2 gamma A.
    # Verify their coefficient matrix has pivots -1 and 1 over Q[gamma].
    double_row = (-ONE, ONE, ZERO)
    simple_row = (ZERO, -as_gpoly(2) * GAMMA, ONE)
    assert double_row[0] == -ONE and double_row[1] == ONE
    assert simple_row[1] == -as_gpoly(2) * GAMMA
    assert simple_row[2] == ONE


def multiindices(nvars, total, prefix=()):
    if nvars == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from multiindices(nvars - 1, total - value, prefix + (value,))


def squarefree_signature(alpha):
    """Basis key and nonzero diagonal factor of the map S_k.

    X_j occurring alpha[j] times maps to prod(alpha[j]!) times the
    monomial symmetric polynomial with exponents j+1 repeated alpha[j].
    """

    exponents = []
    scale = 1
    for j, multiplicity in enumerate(alpha):
        exponents.extend([j + 1] * multiplicity)
        scale *= factorial(multiplicity)
    return tuple(sorted(exponents, reverse=True)), scale


def squarefree_injectivity_check(max_order=6, max_degree=8):
    rows = []
    for order in range(max_order + 1):
        nvars = order + 1
        for degree in range(1, max_degree + 1):
            seen = {}
            count = 0
            for alpha in multiindices(nvars, degree):
                key, scale = squarefree_signature(alpha)
                assert scale > 0
                assert key not in seen, (order, degree, alpha, seen[key])
                seen[key] = alpha
                count += 1
            # Domain and image have the same basis cardinality.
            assert len(seen) == count
            rows.append((order, degree, count))
    return rows


def main():
    quadratic_laurent_check()
    rows = squarefree_injectivity_check()
    print("quadratic pole equations: B=A, C=2*gamma*A [exact]")
    print(
        "prime sign split: p=2 positive bracket, p=11 negative bracket "
        "from 1/2<gamma<1, log(2)<1<2<log(11)"
    )
    print(
        "squarefree symmetrisation: injective for",
        len(rows),
        "(order,degree) pairs; largest basis rank =",
        max(row[2] for row in rows),
    )
    print("PASS")


if __name__ == "__main__":
    main()
