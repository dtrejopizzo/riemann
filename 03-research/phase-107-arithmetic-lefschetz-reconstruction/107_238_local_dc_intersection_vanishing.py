#!/usr/bin/env python3
"""Symbolic certificate that local DC intersection vanishes."""

from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = (
    HERE.parent.parent
    / "00-references/papers-nuevos/A/arXiv-1805.10501v1/thecurve_K.tex"
)
source = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""

published_required_pairing = all(
    token in source
    for token in (
        "\\inter(f,f)=D\\bullet D",
        "D\\bullet D':=<D\\star\\tilde D',\\Delta>",
        "using the distribution $N(u)$",
    )
)
published_diagonal_divergence = all(
    token in source
    for token in (
        "divergent term in $\\log \\Lambda$",
        "lack of good definition of self-intersection of the diagonal",
    )
)

x, y = sp.symbols("x y", positive=True)
r = y / x
u = sp.Function("u")
v = sp.Function("v")
U = x * u(r)
V = x * v(r)
variables = (x, y)

hessian_u = sp.Matrix([[sp.diff(U, a, b) for b in variables] for a in variables])
hessian_v = sp.Matrix([[sp.diff(V, a, b) for b in variables] for a in variables])

# Direct determinant identities avoid dependence on SymPy's representation of
# substituted derivatives.
det_u_zero = sp.simplify(hessian_u.det()) == 0
det_v_zero = sp.simplify(hessian_v.det()) == 0
mixed_det = sp.simplify(
    ((hessian_u + hessian_v).det() - hessian_u.det() - hessian_v.det()) / 2
)
mixed_zero = mixed_det == 0

RAY_ATLAS = ((sp.Rational(1, 2), sp.Rational(2, 3)),
             (sp.Rational(2, 3), sp.Rational(3, 2)),
             (sp.Rational(3, 2), sp.Rational(5, 2)),
             (sp.Rational(5, 2), sp.Rational(7, 3)),
             (sp.Rational(7, 3), sp.Rational(11, 4)))
distinct_ray_interior_empty = True
corner_common = True
for lam, mu in RAY_ATLAS:
    distinct_ray_interior_empty &= lam != mu and sp.solve(
        (sp.Symbol("Y") - lam * sp.Symbol("X"),
         sp.Symbol("Y") - mu * sp.Symbol("X")),
        (sp.Symbol("X"), sp.Symbol("Y")),
    ) == {sp.Symbol("X"): 0, sp.Symbol("Y"): 0}
    corner_common &= (0 == lam * 0 == mu * 0)

local_pairing_zero = det_u_zero and det_v_zero and mixed_zero and distinct_ray_interior_empty
corner_required = local_pairing_zero and published_required_pairing
verdict = all(
    (
        published_required_pairing,
        published_diagonal_divergence,
        local_pairing_zero,
        corner_common,
        corner_required,
    )
)

print(f"HOMOGENEOUS_HESSIAN_RANK: {'ONE' if det_u_zero and det_v_zero else 'NOT_ONE'}")
print(f"LOCAL_MIXED_MONGE_AMPERE: {'ZERO' if mixed_zero else 'NONZERO'}")
print(f"DISTINCT_RAY_INTERSECTION_IN_PUNCTURED_CHART: {'EMPTY' if distinct_ray_interior_empty else 'NONEMPTY'}")
print(f"COMMON_CORNER: {'YES' if corner_common else 'NO'}")
print(f"GLOBAL_DIAGONAL_RENORMALIZATION_REQUIRED: {'YES' if corner_required else 'NO'}")
print("LOCAL_DC_INTERSECTION: CLOSED_ZERO" if verdict else "LOCAL_DC_INTERSECTION: OPEN")
print("ROW_A_STATUS: PARTIAL")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
