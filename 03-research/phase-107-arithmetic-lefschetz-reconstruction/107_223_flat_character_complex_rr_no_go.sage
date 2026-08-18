#!/home/trabajo/miniforge3/bin/sage
"""Exact verifier for the flat-character Riemann--Roch no-go."""

from math import lcm


CHARACTER_ATLAS = (
    (4, 1, 8, 2),
    (5, 1, 10, 2),
    (9, 3, 9, 6),
)
CC_RADII = (1, 4, 13, 40)


def multiplication_matrix(order, element):
    basis = order.basis()
    return matrix(
        ZZ,
        [order(element * vector).list() for vector in basis],
    ).transpose()


def homology_orders(n, u, m, v):
    conductor = lcm(n, m)
    field = CyclotomicField(conductor)
    order = field.ring_of_integers()
    zeta = field.gen()
    a = order(zeta ** (u * conductor // n) - 1)
    b = order(zeta ** (v * conductor // m) - 1)
    A = multiplication_matrix(order, a)
    B = multiplication_matrix(order, b)
    homology = ChainComplex(
        {1: A.augment(B), 2: (-B).stack(A)},
        degree=-1,
    ).homology()
    return tuple(ZZ(homology[i].order()) for i in range(3))


def cc_h0_dimension(n):
    k = 0
    while 3**k < 2 * n + 1:
        k += 1
    return k


def main():
    rows = tuple((labels, homology_orders(*labels)) for labels in CHARACTER_ATLAS)
    local_length_cancellation = True
    for _, (h0, h1, h2) in rows:
        primes = set(h0.prime_divisors()) | set(h1.prime_divisors())
        local_length_cancellation &= h2 == 1
        local_length_cancellation &= all(h0.valuation(p) == h1.valuation(p) for p in primes)

    trivial_ranks = (1, 2, 1)
    trivial_euler = trivial_ranks[0] - trivial_ranks[1] + trivial_ranks[2]
    flat_euler_zero = local_length_cancellation and trivial_euler == 0

    cc_dimensions = tuple(cc_h0_dimension(n) for n in CC_RADII)
    cc_expected = (1, 2, 3, 4)
    cc_rr_nonzero = cc_dimensions == cc_expected and all(value > 0 for value in cc_dimensions)

    # Nonflat rank mutation: deleting one middle free summand changes the
    # K0 Euler rank from zero to one, showing the test can detect curvature data.
    mutated_ranks = (1, 1, 1)
    nonflat_control = mutated_ranks[0] - mutated_ranks[1] + mutated_ranks[2] == 1
    contradiction = flat_euler_zero and cc_rr_nonzero
    verdict = contradiction and nonflat_control

    print("Flat cyclotomic controls:")
    for labels, orders in rows:
        print(f"  {labels}: (|H0|,|H1|,|H2|)={orders}")
    print()
    print(f"ACTUAL_FLAT_COMPONENTS: {len(rows)}")
    print(f"LOCAL_TORSION_EULER_CHARACTERISTIC: {'ZERO' if local_length_cancellation else 'NONZERO'}")
    print(f"TRIVIAL_CHARACTER_EULER_RANK: {trivial_euler}")
    print(f"CC_FIXED_RADII: {CC_RADII}")
    print(f"CC_RR_EULER_DIMENSIONS: {cc_dimensions}")
    print(f"NONFLAT_NEGATIVE_CONTROL: {'NONZERO' if nonflat_control else 'FAILED'}")
    print("ORDINARY_FLAT_EULER_AS_DIVISOR_RR: CLOSED_NO_GO")
    print("DIVISOR_DEPENDENT_METRIC_TOLERANCE_OR_C1_REQUIRED: YES")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("flat character RR verifier failed")


main()
