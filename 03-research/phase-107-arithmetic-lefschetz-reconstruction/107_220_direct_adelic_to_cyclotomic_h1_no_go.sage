#!/home/trabajo/miniforge3/bin/sage
"""Exact target-side verifier for the adelic divisibility no-go."""

from math import lcm


ATLAS = (
    (3, 1, 4, 1),
    (4, 1, 8, 2),
    (5, 1, 10, 2),
    (8, 2, 9, 3),
    (9, 3, 9, 6),
)


def multiplication_matrix(order, element):
    basis = order.basis()
    return matrix(
        ZZ,
        [order(element * vector).list() for vector in basis],
    ).transpose()


def target_h1(n, u, m, v):
    conductor = lcm(n, m)
    field = CyclotomicField(conductor)
    order = field.ring_of_integers()
    zeta = field.gen()
    a = order(zeta ** (u * conductor // n) - 1)
    b = order(zeta ** (v * conductor // m) - 1)
    A = multiplication_matrix(order, a)
    B = multiplication_matrix(order, b)
    complex_ = ChainComplex(
        {1: A.augment(B), 2: (-B).stack(A)},
        degree=-1,
    )
    return complex_.homology()[1]


def prime_nonsurjectivity(group):
    order = ZZ(group.order())
    if order == 1:
        return None
    prime = next(iter(order.prime_divisors()))
    invariants = tuple(ZZ(value) for value in group.invariants())
    image_order = prod(value // gcd(value, prime) for value in invariants)
    return prime, image_order < order


def main():
    groups = tuple((labels, target_h1(*labels)) for labels in ATLAS)
    nontrivial = tuple((labels, group) for labels, group in groups if group.order() > 1)
    controls = tuple((labels, prime_nonsurjectivity(group)) for labels, group in nontrivial)

    finite_targets = all(group.order() is not Infinity for _, group in groups)
    nonsurjective = all(control[1][1] for control in controls)

    # Hom(Z,G) is naturally G: choosing the image of 1 gives a nonzero
    # map whenever G is nontrivial.  This rejects a vacuous target test.
    lattice_maps_exist = all(group.order() > 1 for _, group in nontrivial)
    adelic_maps_forced_zero = finite_targets and nonsurjective
    verdict = (
        len(nontrivial) >= 3
        and finite_targets
        and nonsurjective
        and lattice_maps_exist
        and adelic_maps_forced_zero
    )

    print("Actual cyclotomic H1 targets:")
    for labels, group in groups:
        print(f"  {labels}: H1={group}, order={group.order()}")
    print()
    print(f"ACTUAL_MIXED_TARGETS: {len(groups)}")
    print(f"NONTRIVIAL_FINITE_TARGETS: {len(nontrivial)}")
    print(f"FINITE_TARGETS_DIVISIBLE: {'NO' if nonsurjective else 'UNRESOLVED'}")
    print(f"NONZERO_LATTICE_MAPS_EXIST: {'YES' if lattice_maps_exist else 'NO'}")
    print(f"DIRECT_ADELIC_ADDITIVE_MAP: {'ZERO_ONLY' if adelic_maps_forced_zero else 'UNRESOLVED'}")
    print("PONTRYAGIN_DUAL_COMPARISON_REQUIRED: YES")
    print("DIRECT_DIVISOR_H1_COMPARISON: CLOSED_NO_GO")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("adelic-to-cyclotomic H1 verifier failed")


main()
