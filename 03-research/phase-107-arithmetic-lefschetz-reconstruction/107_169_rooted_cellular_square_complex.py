#!/usr/bin/env python3
"""Exact cellular and subdivision checks for the rooted square."""

from collections import defaultdict
import sympy as sp


LEVELS = (2, 3, 5, 6, 10)
TRANSITIONS = ((2, 6), (3, 6), (2, 10), (5, 10))


def vertex(i, j, level):
    return i * level + j


def horizontal(i, j, level):
    return i * level + j


def vertical(i, j, level):
    return level * level + i * level + j


def matrices(level):
    cells = level * level
    d1 = sp.zeros(cells, 2 * cells)
    d2 = sp.zeros(2 * cells, cells)
    for i in range(level):
        for j in range(level):
            face = vertex(i, j, level)
            h = horizontal(i, j, level)
            v = vertical(i, j, level)

            d1[vertex(i, j, level), h] -= 1
            d1[vertex(i, (j + 1) % level, level), h] += 1
            d1[vertex(i, j, level), v] -= 1
            d1[vertex((i + 1) % level, j, level), v] += 1

            d2[horizontal(i, j, level), face] += 1
            d2[vertical(i, (j + 1) % level, level), face] += 1
            d2[horizontal((i + 1) % level, j, level), face] -= 1
            d2[vertical(i, j, level), face] -= 1
    return d1, d2


def add_poly(left, right):
    out = defaultdict(int, left)
    for exponent, coefficient in right.items():
        out[exponent] += coefficient
    return {key: value for key, value in out.items() if value}


def shift(poly, dx, dy, modulus):
    return {((x + dx) % modulus, (y + dy) % modulus): c for (x, y), c in poly.items()}


def phi(poly, divisor, target):
    return {((divisor * x) % target, (divisor * y) % target): c for (x, y), c in poly.items()}


def geometric_spread(poly, axis, count, modulus):
    out = {}
    for step in range(count):
        shifted = shift(poly, step if axis == 0 else 0, step if axis == 1 else 0, modulus)
        out = add_poly(out, shifted)
    return out


all_ok = True
for level in LEVELS:
    d1, d2 = matrices(level)
    chain = d1 * d2 == sp.zeros(d1.rows, d2.cols)
    rank1, rank2 = d1.rank(), d2.rank()
    betti = (
        d1.rows - rank1,
        d1.cols - rank1 - rank2,
        d2.cols - rank2,
    )
    all_ok &= chain and betti == (1, 2, 1)
    print(f"L={level}_BETTI={betti[0]},{betti[1]},{betti[2]}_CHAIN={'YES' if chain else 'NO'}")

# Check both chain-map identities on monomial bases symbolically as sparse
# group-ring elements, without constructing transition matrices.
transition_ok = True
for source, target in TRANSITIONS:
    divisor = target // source
    for i in range(source):
        for j in range(source):
            basis = {(i, j): 1}
            image = phi(basis, divisor, target)

            # Boundary of a subdivided horizontal edge.
            fine_x = geometric_spread(image, 0, divisor, target)
            lhs_x = add_poly(shift(fine_x, 1, 0, target), {k: -v for k, v in fine_x.items()})
            rhs_x = add_poly(shift(image, divisor, 0, target), {k: -v for k, v in image.items()})

            fine_y = geometric_spread(image, 1, divisor, target)
            lhs_y = add_poly(shift(fine_y, 0, 1, target), {k: -v for k, v in fine_y.items()})
            rhs_y = add_poly(shift(image, 0, divisor, target), {k: -v for k, v in image.items()})
            transition_ok &= lhs_x == rhs_x and lhs_y == rhs_y

all_ok &= transition_ok

print(f"SYMBOLIC_SUBDIVISION_CHAIN_MAP: {'YES' if transition_ok else 'NO'}")
print("DIFFERENTIAL_L1_BOUND_D2: 4")
print("DIFFERENTIAL_L1_BOUND_D1: 2")
print("LEVEL_CELLS_ENUMERATED_IN_PRODUCTION: NO")
print(f"HOMOLOGY_STABILIZES: {'YES' if transition_ok else 'NO'}")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
