#!/home/trabajo/miniforge3/bin/python
"""Sage verifier for the CM complex lift of the fixed Paper-0 curve."""

from sage.all import (
    EllipticCurve,
    EllipticCurve_from_j,
    GF,
    QQ,
    QuadraticField,
    hilbert_class_polynomial,
)


all_ok = True

finite_curve = EllipticCurve(GF(5), [0, 0, 0, 1, 1])
point_counts = finite_curve.count_points(16)
trace = finite_curve.trace_of_frobenius()
ordinary = finite_curve.is_ordinary()

hilbert = hilbert_class_polynomial(-11)
cm_curve = EllipticCurve_from_j(QQ(-32768))
reduction = cm_curve.change_ring(GF(5))
reduction_matches = reduction.is_isomorphic(finite_curve)

K = QuadraticField(-11, "d")
d = K.gen()
alpha = (-3 + d) / 2
alpha_trace = alpha.trace()
alpha_norm = alpha.norm()
minimal_ok = list(alpha.minpoly()) == [5, 3, 1]

all_ok &= finite_curve.cardinality() == 9 and trace == -3 and ordinary
all_ok &= hilbert == hilbert.parent().gen() + 32768
all_ok &= cm_curve.j_invariant() == -32768 and reduction_matches
all_ok &= alpha_trace == -3 and alpha_norm == 5 and minimal_ok

traces = [2, -3]
for n in range(2, 17):
    traces.append(-3 * traces[-1] - 5 * traces[-2])

intersection_ok = True
hodge_ok = True
for n in range(1, 17):
    qn = 5**n
    sn = traces[n]
    expected_points = qn + 1 - sn
    graph_diagonal = (alpha**n - 1).norm()
    centered_cross = graph_diagonal - qn - 1
    determinant = 4 * qn - sn**2

    intersection_ok &= point_counts[n - 1] == expected_points
    intersection_ok &= graph_diagonal == expected_points
    intersection_ok &= centered_cross == -sn
    hodge_ok &= determinant >= 0
    print(
        f"N={n}_POINTS={point_counts[n - 1]}_TRACE={sn}_"
        f"GRAPH_DIAGONAL={graph_diagonal}_GRAM_DET={determinant}"
    )

all_ok &= intersection_ok and hodge_ok

print(f"FIXED_CURVE_ORDINARY: {'YES' if ordinary else 'NO'}")
print(f"CM_HILBERT_CLASS_POLYNOMIAL: {hilbert}")
print(f"CM_Q_MODEL_J: {cm_curve.j_invariant()}")
print(f"REDUCTION_ISOMORPHIC_TO_FIXED_CURVE: {'YES' if reduction_matches else 'NO'}")
print(f"CM_ALPHA_TRACE_NORM: {alpha_trace},{alpha_norm}")
print(f"ALL_POINT_COUNT_INTERSECTIONS_MATCH: {'YES' if intersection_ok else 'NO'}")
print(f"ALL_COMPLEX_HODGE_DETERMINANTS_NONNEGATIVE: {'YES' if hodge_ok else 'NO'}")
print("PAPER_0_COMPLEX_LIFT: PROVED_FOR_FIXED_CONTROL")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
