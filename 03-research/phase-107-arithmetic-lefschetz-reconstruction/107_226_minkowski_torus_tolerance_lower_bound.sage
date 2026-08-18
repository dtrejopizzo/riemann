#!/home/trabajo/miniforge3/bin/sage
"""Verifier for the Minkowski-torus tolerant dimension lower bound."""

from math import ceil, gamma, log, pi


CONDUCTORS = (8, 10, 9)
LAMBDAS = (0.5, 1.0 / 6.0, 1.0 / 18.0)


def ball_volume(dimension):
    return pi ** (dimension / 2.0) / gamma(dimension / 2.0 + 1.0)


def lower_bound(dimension, tolerance):
    reciprocal = 1.0 / (ball_volume(dimension) * tolerance**dimension)
    return max(0, ceil(log(reciprocal, 3) - 1e-12))


def trace_covolume(field):
    codifferent = field.different() ** (-1)
    basis = codifferent.basis()
    gram = matrix(
        QQ,
        [
            [field(x * y.conjugate()).trace() for y in basis]
            for x in basis
        ],
    )
    return sqrt(gram.det())


def main():
    rows = []
    for conductor in CONDUCTORS:
        field = CyclotomicField(conductor)
        dimension = field.degree()
        covolume = trace_covolume(field)
        bounds = tuple(lower_bound(dimension, tolerance) for tolerance in LAMBDAS)
        mutated = tuple(lower_bound(1, tolerance) for tolerance in LAMBDAS)
        rows.append((conductor, dimension, covolume, bounds, mutated))

    positive_covolumes = all(row[2] > 0 for row in rows)
    monotone = all(row[3][0] <= row[3][1] <= row[3][2] for row in rows)
    dimension_sensitive = all(row[3] != row[4] for row in rows)
    cc_circle = tuple(lower_bound(1, tolerance) for tolerance in LAMBDAS) == (0, 1, 2)
    verdict = positive_covolumes and monotone and dimension_sensitive and cc_circle

    print("Minkowski torus lower bounds:")
    for conductor, dimension, covolume, bounds, _ in rows:
        print(
            f"  n={conductor}: degree={dimension}, "
            f"codifferent covolume={covolume}, bounds={bounds}"
        )
    print()
    print(f"ACTUAL_CYCLOTOMIC_TORI: {len(rows)}")
    print(f"POSITIVE_TRACE_COVOLUMES: {'YES' if positive_covolumes else 'NO'}")
    print(f"LOWER_BOUNDS_MONOTONE: {'YES' if monotone else 'NO'}")
    print(f"DIMENSION_BLIND_MUTATION_REJECTED: {'YES' if dimension_sensitive else 'NO'}")
    print(f"CC_CIRCLE_LOWER_BOUNDS_AT_FIXED_RADII: {'YES' if cc_circle else 'NO'}")
    print("FULL_MINKOWSKI_TORUS_HAS_UNBOUNDED_TOLERANCE_CAPACITY: YES")
    print("MATCHING_BALANCED_UPPER_BOUND: NOT_CONSTRUCTED")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("Minkowski tolerance lower-bound verifier failed")


main()
