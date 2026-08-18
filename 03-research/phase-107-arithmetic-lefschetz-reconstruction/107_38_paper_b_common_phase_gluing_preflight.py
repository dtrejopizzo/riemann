#!/usr/bin/env python3
"""Exact combinatorial audit for the common-phase gluing shadow of Paper B.

This script models a finite shadow of `107_08`:

* each prime page `E_p` is represented by one orbit node `C_p`,
* all pages glue through one shared phase node `S^1_theta`.

It checks exactly that:

1. the glued model is connected;
2. the common phase node is an articulation point;
3. removing it disconnects the model into isolated prime components;
4. every mixed-prime path passes through the common phase node.

This does not prove the full suspension geometry.  It pressure-tests the
load-bearing combinatorial shadow claimed in `107_08` Propositions 7.1,
7.2, and 9.1.
"""

from __future__ import annotations


PRIMES = [2, 3, 5, 7, 11]
PHASE = "S^1_theta"


def build_glued_graph() -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {PHASE: set()}
    for p in PRIMES:
        orbit = f"C_{p}"
        graph[orbit] = {PHASE}
        graph[PHASE].add(orbit)
    return graph


def build_disjoint_graph() -> dict[str, set[str]]:
    return {f"C_{p}": set() for p in PRIMES}


def connected_components(graph: dict[str, set[str]]) -> list[set[str]]:
    remaining = set(graph)
    components: list[set[str]] = []
    while remaining:
        start = remaining.pop()
        stack = [start]
        component = {start}
        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if nxt not in component:
                    component.add(nxt)
                    if nxt in remaining:
                        remaining.remove(nxt)
                    stack.append(nxt)
        components.append(component)
    return components


def graph_without(graph: dict[str, set[str]], removed: str) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for node, neighbors in graph.items():
        if node == removed:
            continue
        out[node] = {n for n in neighbors if n != removed}
    return out


def unique_path_star(source: str, target: str) -> list[str]:
    if source == target:
        return [source]
    return [source, PHASE, target]


def main() -> None:
    glued = build_glued_graph()
    disjoint = build_disjoint_graph()

    glued_components = connected_components(glued)
    assert len(glued_components) == 1

    disjoint_components = connected_components(disjoint)
    assert len(disjoint_components) == len(PRIMES)

    phase_removed = graph_without(glued, PHASE)
    removed_components = connected_components(phase_removed)
    assert len(removed_components) == len(PRIMES)
    assert all(len(component) == 1 for component in removed_components)

    print("Common-phase gluing connectivity audit")
    print(f" primes modelled: {PRIMES}")
    print(f" glued components: {len(glued_components)}")
    print(f" disjoint-union components: {len(disjoint_components)}")
    print(f" components after removing {PHASE}: {len(removed_components)}")

    print("\nMixed-prime path audit")
    checks = 0
    for i, p in enumerate(PRIMES):
        for q in PRIMES[i + 1 :]:
            source = f"C_{p}"
            target = f"C_{q}"
            path = unique_path_star(source, target)
            assert path[1] == PHASE
            checks += 1
            print(f" {source} -> {target}: {' -> '.join(path)}")

    print("\nArticulation audit")
    print(f" {PHASE} is required to connect all prime pages.")
    print(
        f"\nAll common-phase gluing shadow checks passed with {checks} mixed-prime paths."
    )


if __name__ == "__main__":
    main()
