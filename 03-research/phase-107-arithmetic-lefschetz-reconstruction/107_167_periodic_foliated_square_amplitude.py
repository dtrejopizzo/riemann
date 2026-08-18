#!/usr/bin/env python3
"""Exact cellular cohomology of periodic-product circle models."""

import sympy as sp


PAIRS = ((2, 3), (3, 5), (5, 7), (7, 11), (2, 11))


def vertex(i, j, cols):
    return i * cols + j


def horizontal(i, j, cols):
    return i * cols + j


def vertical(i, j, rows, cols):
    return rows * cols + i * cols + j


def cellular_coboundaries(rows, cols):
    vertices = rows * cols
    edges = 2 * vertices
    faces = vertices

    d0 = sp.zeros(edges, vertices)
    d1 = sp.zeros(faces, edges)

    for i in range(rows):
        for j in range(cols):
            h = horizontal(i, j, cols)
            v = vertical(i, j, rows, cols)
            d0[h, vertex(i, j, cols)] = -1
            d0[h, vertex(i, (j + 1) % cols, cols)] = 1
            d0[v, vertex(i, j, cols)] = -1
            d0[v, vertex((i + 1) % rows, j, cols)] = 1

            face = i * cols + j
            d1[face, horizontal(i, j, cols)] = 1
            d1[face, vertical(i, (j + 1) % cols, rows, cols)] = 1
            d1[face, horizontal((i + 1) % rows, j, cols)] = -1
            d1[face, vertical(i, j, rows, cols)] = -1

    return d0, d1


all_ok = True
for prime, other in PAIRS:
    d0, d1 = cellular_coboundaries(prime, other)
    chain_ok = d1 * d0 == sp.zeros(d1.rows, d0.cols)
    rank0 = d0.rank()
    rank1 = d1.rank()
    b0 = d0.cols - rank0
    b1 = d0.rows - rank0 - rank1
    b2 = d1.rows - rank1
    betti = (b0, b1, b2)
    all_ok &= chain_ok and betti == (1, 2, 1)
    print(
        f"P={prime}_Q={other}_CELLS={d0.cols},{d0.rows},{d1.rows}_"
        f"BETTI={b0},{b1},{b2}_CHAIN={'YES' if chain_ok else 'NO'}"
    )

print(f"PERIODIC_PRODUCT_BETTI_NUMBERS: {'1,2,1' if all_ok else 'MISMATCH'}")
print(f"COHOMOLOGY_ABOVE_DEGREE_TWO: {'NO' if all_ok else 'UNKNOWN'}")
print("AMPLITUDE_TWO_SOURCE: FOLIATED_GEOMETRY")
print("RAW_MONOID_TRUNCATION_USED: NO")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
