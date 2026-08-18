#!/home/trabajo/miniforge3/bin/sage
"""Exact Sage verifier for cyclotomically twisted cellular H1."""

from math import gcd


ATLAS = (
    (3, 1, 1),
    (4, 1, 2),
    (5, 1, 2),
    (6, 1, 1),
    (8, 2, 4),
    (9, 3, 6),
    (10, 1, 3),
    (12, 2, 3),
)


def multiplication_matrix(order, element):
    basis = order.basis()
    columns = [order(element * vector).list() for vector in basis]
    return matrix(ZZ, columns).transpose()


def finite_group_order(group):
    value = group.order()
    if value is Infinity:
        raise ValueError("expected finite twisted homology")
    return ZZ(value)


def expected_norm(n, u, v):
    d = gcd(gcd(u, v), n)
    m = n // d
    return ZZ(cyclotomic_polynomial(m)(1)) ** (euler_phi(n) // euler_phi(m))


def check_row(n, u, v):
    field = CyclotomicField(n)
    order = field.ring_of_integers()
    zeta = field.gen()
    a = order(zeta**u - 1)
    b = order(zeta**v - 1)

    horizontal = multiplication_matrix(order, a)
    vertical = multiplication_matrix(order, b)
    d1 = horizontal.augment(vertical)
    d2 = (-vertical).stack(horizontal)
    chain_ok = d1 * d2 == 0

    complex_ = ChainComplex({1: d1, 2: d2}, degree=-1)
    homology = complex_.homology()
    h0_order = finite_group_order(homology[0])
    h1_order = finite_group_order(homology[1])
    h2_zero = homology[2].order() == 1

    ideal_norm = ZZ(order.ideal([a, b]).norm())
    formula_norm = expected_norm(n, u, v)
    return {
        "label": (n, u, v),
        "chain": chain_ok,
        "h0": h0_order,
        "h1": h1_order,
        "h2_zero": h2_zero,
        "ideal": ideal_norm,
        "formula": formula_norm,
    }


def main():
    rows = tuple(check_row(*entry) for entry in ATLAS)

    # The trivial character is checked separately because its homology is free.
    trivial = ChainComplex(
        {
            1: zero_matrix(ZZ, 1, 2),
            2: zero_matrix(ZZ, 2, 1),
        },
        degree=-1,
    ).homology()
    trivial_ranks = tuple(
        sum(1 for invariant in trivial[i].invariants() if invariant == 0)
        for i in range(3)
    )

    # A real mutation, not a symbolic flag: changing the Koszul sign must
    # produce a nonzero composite on the first prime-power example.
    n, u, v = ATLAS[0]
    field = CyclotomicField(n)
    order = field.ring_of_integers()
    zeta = field.gen()
    horizontal = multiplication_matrix(order, order(zeta**u - 1))
    vertical = multiplication_matrix(order, order(zeta**v - 1))
    mutated_composite = horizontal.augment(vertical) * vertical.stack(horizontal)
    mutation_rejected = mutated_composite != 0

    chain_ok = all(row["chain"] for row in rows)
    hodge_orders = all(row["h0"] == row["h1"] for row in rows)
    ideal_match = all(
        row["h0"] == row["ideal"] == row["formula"] for row in rows
    )
    h2_ok = all(row["h2_zero"] for row in rows)
    trivial_ok = trivial_ranks == (1, 2, 1)
    verdict = (
        chain_ok
        and hodge_orders
        and ideal_match
        and h2_ok
        and trivial_ok
        and mutation_rejected
    )

    print("Cyclotomic twisted rows:")
    for row in rows:
        n, u, v = row["label"]
        print(
            f"  n={n}, u={u}, v={v}: "
            f"|H0|={row['h0']}, |H1|={row['h1']}, "
            f"Norm(I)={row['ideal']}"
        )
    print()
    print(f"ACTUAL_CYCLOTOMIC_LEVELS: {len(rows)}")
    print(f"KOSZUL_CHAIN_IDENTITY: {'YES' if chain_ok else 'NO'}")
    print(f"TRIVIAL_CHARACTER_RANKS: {trivial_ranks}")
    print(f"TWISTED_H2_ZERO: {'YES' if h2_ok else 'NO'}")
    print(f"H0_H1_TORSION_ORDERS_EQUAL: {'YES' if hodge_orders else 'NO'}")
    print(f"CYCLOTOMIC_NORM_FORMULA: {'YES' if ideal_match else 'NO'}")
    print(f"SIGN_MUTATION_REJECTED: {'YES' if mutation_rejected else 'NO'}")
    print("FINITE_ROOTED_MIDDLE_COHOMOLOGY: CONSTRUCTED")
    print("DIVISOR_SHEAF_H1: NOT_CONSTRUCTED")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("cyclotomic twisted H1 verifier failed")


main()
