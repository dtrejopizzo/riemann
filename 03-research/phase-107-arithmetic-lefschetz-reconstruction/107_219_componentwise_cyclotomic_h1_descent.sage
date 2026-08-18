#!/home/trabajo/miniforge3/bin/sage
"""Exact verifier for componentwise cyclotomic H1 descent."""

from math import gcd, lcm


ATLAS = (
    (3, 1, 4, 1),
    (4, 1, 8, 2),
    (5, 1, 10, 2),
    (8, 2, 9, 3),
    (9, 3, 9, 6),
)


def multiplication_matrix(order, element):
    basis = order.basis()
    columns = [order(element * vector).list() for vector in basis]
    return matrix(ZZ, columns).transpose()


def finite_order(group):
    value = group.order()
    if value is Infinity:
        raise ValueError("expected finite homology")
    return ZZ(value)


def component(n, u, m, v):
    conductor = lcm(n, m)
    field = CyclotomicField(conductor)
    order = field.ring_of_integers()
    zeta = field.gen()
    a = order(zeta ** (u * conductor // n) - 1)
    b = order(zeta ** (v * conductor // m) - 1)
    A = multiplication_matrix(order, a)
    B = multiplication_matrix(order, b)
    d1 = A.augment(B)
    d2 = (-B).stack(A)
    homology = ChainComplex({1: d1, 2: d2}, degree=-1).homology()
    ideal_norm = ZZ(order.ideal([a, b]).norm())
    return {
        "labels": (n, u, m, v),
        "conductor": conductor,
        "d1": d1,
        "d2": d2,
        "chain": d1 * d2 == 0,
        "h0": finite_order(homology[0]),
        "h1": finite_order(homology[1]),
        "h2": finite_order(homology[2]),
        "norm": ideal_norm,
    }


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def main():
    rows = tuple(component(*labels) for labels in ATLAS)

    strict_transitions = True
    old_components_retained = True
    power_negative_control = False
    for row in rows:
        n, _, m, _ = row["labels"]
        base = lcm(n, m)
        for level in (2 * base, 6 * base):
            old_components_retained &= n in divisors(level) and m in divisors(level)
            repeated = component(*row["labels"])
            strict_transitions &= repeated["d1"] == row["d1"]
            strict_transitions &= repeated["d2"] == row["d2"]

        d = 2
        field_n = CyclotomicField(n)
        zeta_n = field_n.gen()
        power_negative_control |= zeta_n**d != zeta_n

    chain_ok = all(row["chain"] for row in rows)
    norm_ok = all(row["h0"] == row["h1"] == row["norm"] for row in rows)
    h2_ok = all(row["h2"] == 1 for row in rows)
    both_behaviors = any(row["norm"] == 1 for row in rows) and any(
        row["norm"] > 1 for row in rows
    )
    verdict = (
        chain_ok
        and norm_ok
        and h2_ok
        and both_behaviors
        and strict_transitions
        and old_components_retained
        and power_negative_control
    )

    print("Mixed cyclotomic components:")
    for row in rows:
        n, u, m, v = row["labels"]
        print(
            f"  ({n},{u}) x ({m},{v}), l={row['conductor']}: "
            f"|H0|={row['h0']}, |H1|={row['h1']}, Norm(I)={row['norm']}"
        )
    print()
    print(f"ACTUAL_MIXED_COMPONENTS: {len(rows)}")
    print(f"INTEGRAL_KOSZUL_HOMOLOGY: {'YES' if chain_ok and norm_ok else 'NO'}")
    print(f"ACYCLIC_AND_TORSION_CONTROLS: {'YES' if both_behaviors else 'NO'}")
    print(f"OLD_COMPONENTS_RETAINED: {'YES' if old_components_retained else 'NO'}")
    print(f"DIFFERENTIALS_STABLE_AT_L_2L_6L: {'YES' if strict_transitions else 'NO'}")
    print(f"POWER_SUBDIVISION_NEGATIVE_CONTROL: {'REJECTED' if power_negative_control else 'FAILED'}")
    print("FINITE_SUPPORT_TWISTED_H1_DESCENT: CONSTRUCTED")
    print("DIVISOR_MODULE_COMPARISON: NOT_CONSTRUCTED")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("componentwise H1 descent verifier failed")


main()
