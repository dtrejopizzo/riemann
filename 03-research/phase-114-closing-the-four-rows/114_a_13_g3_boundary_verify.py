#!/usr/bin/env python3
"""Finite checks for the universal non-additive collapse in 114.a.13."""

from math import isclose, sqrt
from random import Random


def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}" + (f"   {detail}" if detail else ""))
    if not condition:
        raise AssertionError(label)


def s(v):
    # A test form with both signs.
    x, y, z = v
    return x * x + y * y - 2 * z * z


def J(v, qh=2.0):
    # Return the scalar coefficient of h; q(a h)=a^2 q(h).
    return sqrt(max(s(v), 0.0) / qh)


rng = Random(11413)
vectors = [tuple(rng.uniform(-5, 5) for _ in range(3)) for _ in range(500)]

print("A. Pointwise domination")
check("A1 q(J(v)) = max(s(v),0) >= s(v)",
      all(isclose(J(v) ** 2 * 2.0, max(s(v), 0.0), abs_tol=1e-11)
          and J(v) ** 2 * 2.0 + 1e-11 >= s(v) for v in vectors))

print("\nB. Positive homogeneity")
scales = [0.0, 0.1, 0.5, 1.0, 2.0, 10.0]
check("B1 J(t v)=t J(v) for t>=0",
      all(isclose(J(tuple(t * x for x in v)), t * J(v), abs_tol=1e-11)
          for v in vectors for t in scales))

print("\nC. Non-additivity and sign collapse")
e1, e2 = (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)
lhs = J(e1) + J(e2)
rhs = J(tuple(a + b for a, b in zip(e1, e2)))
check("C1 J(e1)+J(e2) != J(e1+e2)", not isclose(lhs, rhs),
      f"lhs={lhs:.6f}, rhs={rhs:.6f}")
check("C2 J(-v)=J(v)",
      all(isclose(J(tuple(-x for x in v)), J(v), abs_tol=1e-11) for v in vectors))

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
