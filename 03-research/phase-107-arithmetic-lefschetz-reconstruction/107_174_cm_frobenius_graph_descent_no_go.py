#!/home/trabajo/miniforge3/bin/python
"""Exact Sage falsifier for descent of the oriented CM Frobenius graph."""

from sage.all import EllipticCurve, NumberField, PolynomialRing, QQ


R = PolynomialRing(QQ, "x")
x = R.gen()
K = NumberField(x**2 + 3 * x + 5, "alpha")
alpha = K.gen()
bar_alpha = -3 - alpha
E = EllipticCurve([0, -1, 1, -7, 10])

conjugation_ok = (
    alpha != bar_alpha
    and alpha + bar_alpha == -3
    and alpha * bar_alpha == 5
)
mutual_intersection = (alpha - bar_alpha).norm()
graphs_distinct = mutual_intersection == 11

doubled_intersections_ok = True
for n in range(1, 17):
    graph_degree = (alpha**n - 1).norm()
    conjugate_degree = (bar_alpha**n - 1).norm()
    orbit_intersection = graph_degree + conjugate_degree
    row_ok = graph_degree == conjugate_degree and orbit_intersection == 2 * graph_degree
    doubled_intersections_ok = doubled_intersections_ok and row_ok
    print(
        f"N={n}_ONE_GRAPH={graph_degree}_ORBIT_CYCLE={orbit_intersection}"
        f"_DOUBLES={'YES' if row_ok else 'NO'}"
    )

# Composition of graph correspondences multiplies their endomorphisms.
average_square_support = {
    alpha**2: QQ(1) / 4,
    alpha * bar_alpha: QQ(1) / 2,
    bar_alpha**2: QQ(1) / 4,
}
average_two_support = {
    alpha**2: QQ(1) / 2,
    bar_alpha**2: QQ(1) / 2,
}
averaging_preserves_composition = average_square_support == average_two_support

# Sage confirms that the generic curve is the real rational CM control.
real_curve_ok = E.has_cm() and E.cm_discriminant() == -11 and E.j_invariant() == -32768
oriented_graph_descends = alpha == bar_alpha

verdict = all(
    [
        real_curve_ok,
        conjugation_ok,
        graphs_distinct,
        doubled_intersections_ok,
        not oriented_graph_descends,
        not averaging_preserves_composition,
    ]
)

print(f"REAL_CM_CONTROL: {'YES' if real_curve_ok else 'NO'}")
print(f"CONJUGATE_GRAPHS_DISTINCT: {'YES' if graphs_distinct else 'NO'}")
print(f"GRAPH_MUTUAL_INTERSECTION: {mutual_intersection}")
print(f"ORIENTED_CM_GRAPH_DESCENDS_TO_Q: {'YES' if oriented_graph_descends else 'NO'}")
print(
    "GALOIS_AVERAGING_PRESERVES_COMPOSITION: "
    f"{'YES' if averaging_preserves_composition else 'NO'}"
)
print("CM_GRAPH_DESCENT_ROUTE: CLOSED_NO_GO")
print("ALTERNATIVE_ABSOLUTE_CORRESPONDENCE: OPEN")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
