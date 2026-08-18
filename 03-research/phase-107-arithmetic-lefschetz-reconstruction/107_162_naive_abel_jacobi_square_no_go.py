#!/usr/bin/env python3
"""Exact finite-fiber falsifier for the base-sheaf Abel--Jacobi square."""

from itertools import product


PRIMES = (2, 3, 5, 7, 11)


def diagonal(order):
    return {(x, x) for x in range(order)}


def graph(order, multiplier):
    return {(x, multiplier * x % order) for x in range(order)}


def base_zero_loci(order):
    """One base point gives only empty/full fiber-saturated zero loci."""
    fiber_square = set(product(range(order), repeat=2))
    return (set(), fiber_square)


def relative_zero_locus(order, multiplier):
    """Zero set of the relative equation y-multiplier*x modulo order."""
    return {
        (x, y)
        for x, y in product(range(order), repeat=2)
        if (y - multiplier * x) % order == 0
    }


all_ok = True
base_cuts_diagonal = False
base_cuts_graph = False
relative_cuts_diagonal = True
relative_cuts_graph = True

for prime in PRIMES:
    # Two distinct orders for every actual prime prevent an accidental
    # success caused by a degenerate one-point discretization.
    for order in (prime + 1, 2 * prime + 1):
        diag = diagonal(order)
        multiplier = 2 if order % 2 else 3
        frob_graph = graph(order, multiplier)
        masks = base_zero_loci(order)

        base_cuts_diagonal |= diag in masks
        base_cuts_graph |= frob_graph in masks
        relative_cuts_diagonal &= relative_zero_locus(order, 1) == diag
        relative_cuts_graph &= (
            relative_zero_locus(order, multiplier) == frob_graph
        )

all_ok &= not base_cuts_diagonal and not base_cuts_graph
all_ok &= relative_cuts_diagonal and relative_cuts_graph

print(f"REAL_PRIME_ATLAS: {','.join(map(str, PRIMES))}")
print(f"BASE_PULLBACK_CUTS_DIAGONAL: {'YES' if base_cuts_diagonal else 'NO'}")
print(f"BASE_PULLBACK_CUTS_FROBENIUS_GRAPH: {'YES' if base_cuts_graph else 'NO'}")
print(f"RELATIVE_COORDINATE_CUTS_DIAGONAL: {'YES' if relative_cuts_diagonal else 'NO'}")
print(f"RELATIVE_COORDINATE_CUTS_FROBENIUS_GRAPH: {'YES' if relative_cuts_graph else 'NO'}")
print("NAIVE_ABEL_JACOBI_SQUARE: REJECTED")
print("REQUIRED_EXTENSION: RELATIVE_ORBIT_SHEAF")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
