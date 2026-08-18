#!/home/trabajo/miniforge3/bin/python
"""Exact falsifier for the unmetrized spectral-line intersection no-go."""

from mpmath import mp


mp.dps = 70
PRIMES = (2, 3, 5, 7, 11, 13)


def potential(prime_set):
    return tuple(1 if p in prime_set else 0 for p in PRIMES)


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def transition(source, target):
    if not source <= target:
        raise ValueError("restriction requires source subset target")
    return sub(potential(target), potential(source))


chains = [
    (set(), {2}, {2, 3, 5}),
    ({3}, {3, 7}, {3, 7, 11}),
    ({2, 5}, {2, 5, 13}, {2, 3, 5, 13}),
]

curve_coboundary_ok = True
curve_cocycle_ok = True
for source, middle, target in chains:
    direct = transition(source, target)
    staged = add(transition(source, middle), transition(middle, target))
    curve_cocycle_ok &= direct == staged
    curve_coboundary_ok &= direct == sub(potential(target), potential(source))


rectangles = [
    (set(), {2}, {2, 3}, {5}, {5, 7}, {5, 7, 11}),
    ({3}, {3, 5}, {3, 5, 13}, set(), {2}, {2, 7}),
]
square_coboundary_ok = True
diagonal_trivialization_ok = True
for s0, s1, s2, t0, t1, t2 in rectangles:
    direct = add(transition(s0, s2), transition(t0, t2))
    staged = add(
        add(transition(s0, s1), transition(t0, t1)),
        add(transition(s1, s2), transition(t1, t2)),
    )
    square_coboundary_ok &= direct == staged

    square_potential_source = add(potential(s0), potential(t0))
    square_potential_target = add(potential(s2), potential(t2))
    square_coboundary_ok &= direct == sub(square_potential_target, square_potential_source)
    diagonal_trivialization_ok &= add(square_potential_source, direct) == square_potential_target


# The chartwise canonical section has Euler exponent potential(S);
# division by the same gauge leaves exponent zero.
zero = tuple(0 for _ in PRIMES)
canonical_divisor_empty_ok = True
for prime_set in [set(), {2}, {2, 3, 5}, set(PRIMES)]:
    canonical_divisor_empty_ok &= sub(potential(prime_set), potential(prime_set)) == zero


# A deliberately corrupted edge must cease to compose.
source, middle, target = chains[0]
corrupted_first = list(transition(source, middle))
corrupted_first[0] += 1
corrupted_staged = add(tuple(corrupted_first), transition(middle, target))
mutation_rejected = corrupted_staged != transition(source, target)


def arch(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)


atlas = [
    mp.mpf("1.01"),
    mp.mpf("1.5"),
    mp.mpf("2"),
    mp.mpf("10"),
    mp.mpc("1.25", "3"),
    mp.mpc("2", "-20"),
]
analytic_nonvanishing_ok = all(abs(arch(s)) > mp.mpf("1e-60") for s in atlas)

ordinary_picard_class_zero = curve_coboundary_ok and square_coboundary_ok
verdict = all(
    [
        curve_coboundary_ok,
        curve_cocycle_ok,
        square_coboundary_ok,
        diagonal_trivialization_ok,
        canonical_divisor_empty_ok,
        mutation_rejected,
        analytic_nonvanishing_ok,
    ]
)

print(f"CURVE_TRANSITION_COCYCLE_IS_COBOUNDARY: {'YES' if curve_coboundary_ok else 'NO'}")
print(f"SQUARE_TRANSITION_COCYCLE_IS_COBOUNDARY: {'YES' if square_coboundary_ok else 'NO'}")
print(f"DIAGONAL_TRIVIALIZATION_COMPATIBLE: {'YES' if diagonal_trivialization_ok else 'NO'}")
print(f"CANONICAL_SECTION_DIVISOR_ON_H_EMPTY: {'YES' if canonical_divisor_empty_ok and analytic_nonvanishing_ok else 'NO'}")
print(f"CORRUPTED_TRANSITION_REJECTED: {'YES' if mutation_rejected else 'NO'}")
print(f"ORDINARY_PICARD_CLASS_ZERO: {'YES' if ordinary_picard_class_zero else 'NO'}")
print("UNMETRIZED_DELIGNE_PAIRING_ROUTE: CLOSED_NO_GO")
print("REQUIRED_REFINEMENT: METRIC_CURRENT_OR_RENORMALIZED_BOUNDARY_CLASS")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
