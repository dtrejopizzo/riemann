#!/home/trabajo/miniforge3/bin/sage
"""Exact lattice verifier for codifferent cyclotomic Serre duality."""

from math import lcm


ATLAS = (
    (4, 1, 8, 2),
    (5, 1, 10, 2),
    (9, 3, 9, 6),
)


def basis_matrix(field, basis):
    return matrix(QQ, [field(element).vector() for element in basis]).transpose()


def integral_matrix(matrix_):
    return all(entry.denominator() == 1 for entry in matrix_.list())


def check_component(n, u, m, v):
    conductor = lcm(n, m)
    field = CyclotomicField(conductor)
    order = field.ring_of_integers()
    zeta = field.gen()
    a = field(zeta ** (u * conductor // n) - 1)
    b = field(zeta ** (v * conductor // m) - 1)
    ideal = field.ideal(a, b)
    different = field.different()
    codifferent = different**(-1)
    dual_h1_lattice = ideal**(-1) * codifferent

    order_basis = order.basis()
    codifferent_basis = codifferent.basis()
    dual_basis = dual_h1_lattice.basis()
    ideal_basis = ideal.integral_basis()

    B_order = basis_matrix(field, order_basis)
    B_codifferent = basis_matrix(field, codifferent_basis)
    B_dual = basis_matrix(field, dual_basis)
    B_ideal = basis_matrix(field, ideal_basis)

    codifferent_in_dual = B_dual.inverse() * B_codifferent
    ideal_in_order = B_order.inverse() * B_ideal
    trace_duality = matrix(
        QQ,
        [[field(x * y).trace() for y in codifferent_basis] for x in order_basis],
    )

    norm = ZZ(ideal.norm())
    return {
        "labels": (n, u, m, v),
        "conductor": conductor,
        "norm": norm,
        "discriminant": abs(ZZ(field.discriminant())),
        "codifferent_integral": integral_matrix(codifferent_in_dual),
        "ideal_integral": integral_matrix(ideal_in_order),
        "dual_index": abs(ZZ(codifferent_in_dual.det())),
        "h0_index": abs(ZZ(ideal_in_order.det())),
        "trace_integral": integral_matrix(trace_duality),
        "trace_unimodular": abs(ZZ(trace_duality.det())) == 1,
    }


def main():
    rows = tuple(check_component(*labels) for labels in ATLAS)
    inclusions = all(row["codifferent_integral"] and row["ideal_integral"] for row in rows)
    equal_indices = all(
        row["dual_index"] == row["h0_index"] == row["norm"] for row in rows
    )
    perfect_trace = all(row["trace_integral"] and row["trace_unimodular"] for row in rows)
    naive_self_duality_rejected = all(row["discriminant"] > 1 for row in rows)
    verdict = inclusions and equal_indices and perfect_trace and naive_self_duality_rejected

    print("Codifferent duality rows:")
    for row in rows:
        print(
            f"  {row['labels']}, l={row['conductor']}: "
            f"N(I)={row['norm']}, dual index={row['dual_index']}, "
            f"disc={row['discriminant']}"
        )
    print()
    print(f"ACTUAL_CYCLOTOMIC_DUALITY_COMPONENTS: {len(rows)}")
    print(f"CODIFFERENT_LATTICE_INCLUSION: {'YES' if inclusions else 'NO'}")
    print(f"H0_AND_DUAL_H1_INDICES_EQUAL: {'YES' if equal_indices else 'NO'}")
    print(f"TRACE_PAIRING_PERFECT: {'YES' if perfect_trace else 'NO'}")
    print(f"NAIVE_OK_SELF_DUALITY: {'REJECTED' if naive_self_duality_rejected else 'UNRESOLVED'}")
    print("COMPONENTWISE_SERRE_DUALITY: CONSTRUCTED")
    print("GLOBAL_CANONICAL_DIVISOR_COMPARISON: NOT_CONSTRUCTED")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("codifferent duality verifier failed")


main()
