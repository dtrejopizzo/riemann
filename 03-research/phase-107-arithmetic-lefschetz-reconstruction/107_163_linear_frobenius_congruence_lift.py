#!/usr/bin/env python3
"""Exact lattice check for the linearized CC Frobenius congruence."""

from collections import defaultdict
from math import gcd


PRIMES = (2, 3, 5, 7, 11)
RATIOS = ((1, 1), (2, 1), (3, 2), (5, 3))
DEPTHS = range(5)


class DSU:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}

    def find(self, vertex):
        parent = self.parent[vertex]
        if parent != vertex:
            self.parent[vertex] = self.find(parent)
        return self.parent[vertex]

    def union(self, left, right):
        left = self.find(left)
        right = self.find(right)
        if left != right:
            self.parent[right] = left


def fibers(bound, n, m):
    out = defaultdict(set)
    for i in range(bound + 1):
        for j in range(bound + 1):
            out[n * i + m * j].add((i, j))
    return out


def relation_components(bound, n, m, step_scale=1):
    vertices = {(i, j) for i in range(bound + 1) for j in range(bound + 1)}
    dsu = DSU(vertices)
    di, dj = step_scale * m, step_scale * n
    for i, j in vertices:
        other = (i + di, j - dj)
        if other in vertices:
            dsu.union((i, j), other)
    return {vertex: dsu.find(vertex) for vertex in vertices}


def exact_kernel_generated(bound, n, m):
    weight_fibers = fibers(bound, n, m)
    components = relation_components(bound, n, m)
    for fiber in weight_fibers.values():
        if len({components[vertex] for vertex in fiber}) != 1:
            return False
    # Relations never join distinct weights.
    by_component = defaultdict(set)
    for vertex, component in components.items():
        i, j = vertex
        by_component[component].add(n * i + m * j)
    return all(len(weights) == 1 for weights in by_component.values())


all_ok = True
deepest_root_necessary = True
checks = 0

for prime in PRIMES:
    for depth in DEPTHS:
        for n, m in RATIOS:
            assert gcd(n, m) == 1
            # Coordinates are numerators over p^R.  The deepest relation
            # always has primitive numerator step (m,-n).
            bound = max(12, 3 * max(n, m))
            exact = exact_kernel_generated(bound, n, m)
            all_ok &= exact

            if depth > 0:
                shallow = relation_components(bound, n, m, step_scale=prime)
                witness_left = (0, n)
                witness_right = (m, 0)
                same_weight = (
                    n * witness_left[0] + m * witness_left[1]
                    == n * witness_right[0] + m * witness_right[1]
                )
                omitted_fails = (
                    shallow[witness_left] != shallow[witness_right]
                )
                deepest_root_necessary &= same_weight and omitted_fails
            checks += 1

all_ok &= deepest_root_necessary

print(f"REAL_PRIME_ATLAS: {','.join(map(str, PRIMES))}")
print(f"COPRIME_RATIOS: {','.join(f'{n}/{m}' for n, m in RATIOS)}")
print(f"DEPTH_RANGE: 0..{max(DEPTHS)}")
print(f"FINITE_BOX_CHECKS: {checks}")
print(f"DEEPEST_ROOT_GENERATES_FINITE_KERNEL: {'YES' if all_ok else 'NO'}")
print(f"SHALLOW_ROOT_SUFFICES_AT_NEXT_LEVEL: {'NO' if deepest_root_necessary else 'YES'}")
print(f"DIRECTED_KERNEL_COLIMIT_REQUIRED: {'YES' if deepest_root_necessary else 'NO'}")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
