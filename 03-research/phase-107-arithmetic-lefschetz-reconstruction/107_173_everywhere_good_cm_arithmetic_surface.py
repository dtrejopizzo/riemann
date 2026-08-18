#!/home/trabajo/miniforge3/bin/python
"""Exact Sage falsifier for the everywhere-good CM arithmetic surface."""

from sage.all import EllipticCurve, NumberField, PolynomialRing, QQ


R = PolynomialRing(QQ, "x")
x = R.gen()
K = NumberField(x**2 + 3 * x + 5, "alpha")
alpha = K.gen()

S = PolynomialRing(K, "z")
z = S.gen()
L = K.extension(z**2 - (2 * alpha + 3), "w")
w = L.gen()
a = L(alpha)

old_curve = EllipticCurve(L, [0, -1, 1, -7, 10])
good_curve = EllipticCurve(L, [0, a, w, -a - 1, 0])

field_ok = (
    L.absolute_degree() == 4
    and L.relative_degree() == 2
    and w**2 == 2 * a + 3
    and (2 * a + 3) ** 2 == -11
    and w**12 == -11**3
)
integral_ok = all(c.is_integral() for c in good_curve.ainvs())
model_ok = (
    good_curve.discriminant() == 1
    and good_curve.j_invariant() == -32768
    and good_curve.is_isomorphic(old_curve)
)

isomorphism_data = {
    tuple(phi.tuple()) for phi in old_curve.isomorphisms(good_curve)
}
explicit_change_ok = (w, -a - 3, L(0), L(-6)) in isomorphism_data
everywhere_good_ok = (
    len(good_curve.local_data()) == 0
    and good_curve.conductor().is_one()
)

s_prev2, s_prev1 = 2, -3
kernel_ok = True
for n in range(1, 17):
    if n == 1:
        s_n = s_prev1
    else:
        s_n = -3 * s_prev1 - 5 * s_prev2
        s_prev2, s_prev1 = s_prev1, s_n
    rank = (alpha**n - 1).norm()
    expected = 5**n + 1 - s_n
    row_ok = rank == expected
    kernel_ok = kernel_ok and row_ok
    print(f"N={n}_KERNEL_RANK={rank}_EXPECTED={expected}_OK={'YES' if row_ok else 'NO'}")

verdict = all(
    [field_ok, integral_ok, model_ok, explicit_change_ok, everywhere_good_ok, kernel_ok]
)

print(f"QUARTIC_FIELD_RELATIONS: {'YES' if field_ok else 'NO'}")
print(f"INTEGRAL_WEIERSTRASS_COEFFICIENTS: {'YES' if integral_ok else 'NO'}")
print(f"UNIT_DISCRIMINANT_MODEL: {'YES' if model_ok else 'NO'}")
print(f"EXPLICIT_CM_MODEL_ISOMORPHISM: {'YES' if explicit_change_ok else 'NO'}")
print(f"EVERYWHERE_GOOD_REDUCTION: {'YES' if everywhere_good_ok else 'NO'}")
print(f"ALL_GRAPH_KERNEL_DEGREES_MATCH: {'YES' if kernel_ok else 'NO'}")
print("ARITHMETIC_SURFACE_BASE: SPEC_O_L")
print("BASE_IS_SPEC_Z: NO")
print("RIEMANN_ZETA_SOURCE_REALIZED: NO")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
