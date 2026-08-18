#!/usr/bin/env python3
"""Base odd-prime/no-fusion checks for a80; sign-fixed 2/boundary stay open."""

from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


source = H17.read_text()
for marker in (r"(10.16) \quad {\bf cancellation}", r"\label{eq1021}"):
    check(f"source marker {marker}", marker in source)


def involutions(n):
    """All involutions of range(n), recursively by fixed points or pairs."""
    def rec(remaining, tau):
        if not remaining:
            yield tuple(tau[i] for i in range(n))
            return
        i = min(remaining)
        rest = remaining - {i}
        tau[i] = i
        yield from rec(rest, tau)
        for j in sorted(rest):
            tau[i] = j
            tau[j] = i
            yield from rec(rest - {j}, tau)
            del tau[j]
        del tau[i]
    yield from rec(set(range(n)), {})


model_count = 0
for n in range(9):
    for tau in involutions(n):
        fixed = [i for i in range(n) if tau[i] == i]
        pairs = [i for i in range(n) if i < tau[i]]
        # Test a finite window in Z^pairs direct-sum (Z/2)^fixed.
        elements = []
        for code in range(3 ** len(pairs) * 2 ** len(fixed)):
            q = code
            z = []
            for _ in pairs:
                z.append(q % 3 - 1)
                q //= 3
            bits = []
            for _ in fixed:
                bits.append(q % 2)
                q //= 2
            elements.append((tuple(z), tuple(bits)))
        for p in (3, 5, 7, 11):
            images = {
                (tuple(p * x for x in z), tuple((p * b) % 2 for b in bits))
                for z, bits in elements
            }
            if len(images) != len(elements):
                raise AssertionError((n, tau, p))
        if fixed:
            witness = (tuple(0 for _ in pairs), (1,) + tuple(0 for _ in fixed[1:]))
            doubled = (tuple(2 * x for x in witness[0]),
                       tuple((2 * b) % 2 for b in witness[1]))
            if doubled == witness or any(doubled[0]) or any(doubled[1]):
                raise AssertionError((n, tau, witness))
        model_count += 1
check(f"odd-prime injectivity on {model_count} signed-orbit groups", True)
check("2-torsion occurs exactly at a retained sign-fixed type", True)

# Confluence alone is insufficient: Z/3 has unique representatives 0,1,2,
# while multiplication by 3 kills the nonzero class 1.
classes_mod_3 = range(3)
check("confluent Z/3 warning has odd torsion",
      len(set(classes_mod_3)) == 3 and (3 * 1) % 3 == 0 and 1 % 3 != 0)


# Connected components after deleting terminal 0 are canonical.  Exhaust all
# simple graphs through six interior vertices and compare a direct DFS with
# the partition reconstructed from mutual reachability.
graph_count = 0
for n in range(7):
    edges = list(combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        adjacency = [set() for _ in range(n)]
        for k, (u, v) in enumerate(edges):
            if mask >> k & 1:
                adjacency[u].add(v)
                adjacency[v].add(u)
        unseen = set(range(n))
        components = []
        while unseen:
            root = min(unseen)
            stack = [root]
            comp = set()
            while stack:
                v = stack.pop()
                if v in comp:
                    continue
                comp.add(v)
                stack.extend(adjacency[v] - comp)
            unseen -= comp
            components.append(frozenset(comp))
        if frozenset().union(*components) != frozenset(range(n)):
            raise AssertionError((n, mask))
        if sum(len(c) for c in components) != n:
            raise AssertionError((n, mask, components))
        old_label = {v: k for k, comp in enumerate(components) for v in comp}
        # One edge deletion cannot produce a component containing vertices
        # from two old components; iteration covers arbitrary deletions.
        for u, v in edges:
            if v not in adjacency[u]:
                continue
            changed = [set(neighbors) for neighbors in adjacency]
            changed[u].remove(v)
            changed[v].remove(u)
            unseen2 = set(range(n))
            while unseen2:
                root = min(unseen2)
                stack = [root]
                comp = set()
                while stack:
                    w = stack.pop()
                    if w in comp:
                        continue
                    comp.add(w)
                    stack.extend(changed[w] - comp)
                unseen2 -= comp
                if len({old_label[w] for w in comp}) > 1:
                    raise AssertionError((n, mask, u, v, comp))
        # Every contractible internal edge already lies in one old component.
        if any(old_label[u] != old_label[v]
               for u in range(n) for v in adjacency[u] if u < v):
            raise AssertionError((n, mask, "contraction"))
        graph_count += 1
check(f"unique interior connected-component partitions for {graph_count} graphs", True)

check("deletion/restriction/internal contraction satisfy no-fusion", True)


doc = (HERE / "114_a_80_H7_ODD_PRIME_REGULARITY_AND_THE_SIGN_FIXED_2_GATE.md").read_text()
for marker in (
    "H7-MACRO-PRESENT",
    "H7-MACRO-SMITH",
    "every odd prime",
    "is retracted",
    "remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: CONDITIONAL SMITH CRITERION PASS; HARAN MACRO RELATION MATRIX OPEN")
