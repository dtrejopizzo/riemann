#!/usr/bin/env python3
"""Certificates for D.110 stratified residuation polar dynamics."""

from math import isclose, sqrt


def dims(p: int, a: int, r: int) -> int:
    return a * p**r - p + 1


def polar_raise(vector, new_dim):
    """Polar part of [I; replicated final row] on the neutral chamber."""
    old_dim = len(vector)
    multiplicity = new_dim - old_dim + 1
    out = vector[:-1] + [vector[-1] / sqrt(multiplicity)] * multiplicity
    assert len(out) == new_dim
    return out


def inner(a, b):
    return sum(x * y for x, y in zip(a, b))


def main() -> None:
    # Exact p=2, N=4, M=8 neutral-chamber Jacobian:
    # (c0,c1,c2) -> (c0,c1,c2,c2,c2,c2,c2).
    d, D = 3, 7
    m = D - d + 1
    columns = [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    ]
    gram = [[inner(columns[i], columns[j]) for j in range(d)]
            for i in range(d)]
    assert gram == [[1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, float(m)]]

    polar_columns = [columns[0], columns[1],
                     [x / sqrt(m) for x in columns[2]]]
    polar_gram = [[inner(polar_columns[i], polar_columns[j])
                   for j in range(d)] for i in range(d)]
    for i in range(d):
        for j in range(d):
            assert isclose(polar_gram[i][j], float(i == j),
                           rel_tol=0, abs_tol=1e-14)

    # Cofinal fixed-distance overlaps of iterated polar maps.
    p, a, steps = 4, 3, 3
    target = p ** (-steps / 2)
    errors = []
    for t in (1, 3, 6, 10):
        d0 = dims(p, a, t)
        # Only the last coordinate is spread at each step.  Track its value
        # and the coordinate sum exactly, avoiding exponentially large
        # vectors.
        coordinate_sum = sqrt(d0)
        last_value = 1 / sqrt(d0)
        old_dim = d0
        for j in range(steps):
            new_dim = dims(p, a, t + j + 1)
            multiplicity = new_dim - old_dim + 1
            coordinate_sum += last_value * (sqrt(multiplicity) - 1)
            last_value /= sqrt(multiplicity)
            old_dim = new_dim
        final_dim = dims(p, a, t + steps)
        overlap = coordinate_sum / sqrt(final_dim)
        errors.append(abs(overlap - target))
    assert all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
    assert errors[-1] < 2e-4

    # The local Poisson-minus-identity symbol changes sign.
    rho = 0.5
    at_zero = (1 - rho * rho) / (1 - 2 * rho + rho * rho) - 1
    at_pi = (1 - rho * rho) / (1 + 2 * rho + rho * rho) - 1
    assert at_zero > 0
    assert at_pi < 0

    print("D110 stratified polar certificates: PASS")
    print("residuation Gram diagonal:", [gram[i][i] for i in range(d)])
    print("cofinal overlap target/errors:", target, errors)
    print("Poisson-minus-I endpoint signs:", at_zero, at_pi)


if __name__ == "__main__":
    main()
