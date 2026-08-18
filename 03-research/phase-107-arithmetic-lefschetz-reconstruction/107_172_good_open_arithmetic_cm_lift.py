#!/home/trabajo/miniforge3/bin/python
"""Exact Sage falsifier for the good-open arithmetic CM lift."""

from sage.all import EllipticCurve, GF, NumberField, PolynomialRing, QQ


E = EllipticCurve([0, -1, 1, -7, 10])
F5 = GF(5)
control = EllipticCurve(F5, [0, 0, 0, 1, 1])
reduction = EllipticCurve(F5, list(E.ainvs()))

R = PolynomialRing(QQ, "x")
x = R.gen()
K = NumberField(x**2 + 3 * x + 5, "alpha")
alpha = K.gen()

primes_over_5 = K.primes_above(5)
alpha_primes = [P for P in primes_over_5 if alpha in P]
conjugate_primes = [P for P in primes_over_5 if alpha not in P]

minimal_data_ok = (
    E.is_global_minimal_model()
    and E.discriminant() == -11**3
    and E.conductor() == 11**2
    and len(E.local_data()) == 1
    and int(E.local_data()[0].prime().gens_reduced()[0]) == 11
)
cm_ok = E.has_cm() and E.cm_discriminant() == -11
split_ok = (
    len(primes_over_5) == 2
    and all(P.norm() == 5 for P in primes_over_5)
    and len(alpha_primes) == 1
    and len(conjugate_primes) == 1
    and K.ideal(alpha) == alpha_primes[0]
)
reduction_ok = (
    reduction.cardinality() == 9
    and reduction.trace_of_frobenius() == -3
    and reduction.is_isomorphic(control)
    and not reduction.is_supersingular()
)
alpha_ok = (
    alpha.trace() == -3
    and alpha.norm() == 5
    and list(alpha.minpoly()) == [5, 3, 1]
)

s_prev2, s_prev1 = 2, -3
intersection_ok = True
for n in range(1, 17):
    if n == 1:
        s_n = s_prev1
    else:
        s_n = -3 * s_prev1 - 5 * s_prev2
        s_prev2, s_prev1 = s_prev1, s_n

    kernel_rank = (alpha**n - 1).norm()
    point_count = control.cardinality(extension_degree=n)
    expected = 5**n + 1 - s_n
    determinant = 4 * 5**n - s_n**2
    row_ok = kernel_rank == expected == point_count and determinant >= 0
    intersection_ok = intersection_ok and row_ok
    print(
        f"N={n}_KERNEL_RANK={kernel_rank}_POINTS={point_count}"
        f"_GRAM_DET={determinant}_OK={'YES' if row_ok else 'NO'}"
    )

verdict = all(
    [minimal_data_ok, cm_ok, split_ok, reduction_ok, alpha_ok, intersection_ok]
)

print(f"GLOBAL_MINIMAL_BAD_ONLY_AT_11: {'YES' if minimal_data_ok else 'NO'}")
print(f"CM_BY_DISCRIMINANT_MINUS_11: {'YES' if cm_ok else 'NO'}")
print(f"FIVE_SPLITS_WITH_DISTINGUISHED_ALPHA_PRIME: {'YES' if split_ok else 'NO'}")
print(f"REDUCTION_IS_FIXED_ORDINARY_CONTROL: {'YES' if reduction_ok else 'NO'}")
print(f"ALPHA_TRACE_NORM_POLYNOMIAL: {'YES' if alpha_ok else 'NO'}")
print(f"FINITE_FLAT_KERNEL_RANKS_MATCH_NN: {'YES' if intersection_ok else 'NO'}")
print("ARITHMETIC_BASE: SPEC_OK_INVERT_11")
print("FULL_SPEC_Z_MODEL: NO")
print("ROW_C_RIEMANN_ZETA: OPEN")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
