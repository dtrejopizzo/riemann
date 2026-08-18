#!/usr/bin/env python3
"""Exact finite audit for a73; H7-RF-DEEP remains open."""

from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def partitions(items):
    """Canonical tuples of sorted blocks for every set partition."""
    items = tuple(items)
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for part in partitions(rest):
        yield ((first,),) + part
        for index in range(len(part)):
            blocks = list(part)
            blocks[index] = tuple(sorted((first,) + blocks[index]))
            yield tuple(sorted(blocks))


def relation(part):
    same = set()
    for block in part:
        same.update(tuple(sorted(pair)) for pair in combinations(block, 2))
    return same


def signature(root, part, n, q=11):
    same = relation(part)
    pair_values = []
    for pair in combinations(range(n), 2):
        is_same = pair in same
        if root == 1:
            pair_values.append(8 % q if is_same else 2)
        else:
            pair_values.append(2 if is_same else 8 % q)
    return tuple([1] * n + pair_values)


def reduced_key(root, part, n):
    discrete = all(len(block) == 1 for block in part)
    universal = len(part) == 1
    if (root == 1 and discrete) or (root == 2 and universal):
        return ("pure", 1, n)
    if (root == 1 and universal) or (root == 2 and discrete):
        return ("pure", 2, n)
    return ("nested", root, part)


bell = (1, 1, 2, 5, 15, 52, 203, 877)
for n in range(1, 8):
    parts = sorted(set(partitions(range(n))))
    check(f"Bell number n={n}", len(parts) == bell[n])
    terms = [(root, part) for root in (1, 2) for part in parts]
    by_signature = {}
    for root, part in terms:
        by_signature.setdefault(signature(root, part, n), set()).add(
            reduced_key(root, part, n)
        )
    check(f"pair probes recover reduced depth-two terms n={n}",
          all(len(keys) == 1 for keys in by_signature.values()))
    reduced_count = len({reduced_key(root, part, n) for root, part in terms})
    check(f"signature count equals reduced count n={n}",
          len(by_signature) == reduced_count)


# Scaling by ell in q != ell cannot merge any signature.
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
auxiliary = (11, 17)
n = 6
parts = sorted(set(partitions(range(n))))
terms = [(root, part) for root in (1, 2) for part in parts]
for ell in primes:
    q = next(q0 for q0 in auxiliary if q0 != ell)
    scaled = {}
    for root, part in terms:
        sig = tuple(ell * value % q for value in signature(root, part, n, q))
        scaled.setdefault(sig, set()).add(reduced_key(root, part, n))
    check(f"depth-two prime cancellation ell={ell}, q={q}",
          ell % q != 0 and all(len(keys) == 1 for keys in scaled.values()))


doc = (HERE / "114_a_73_H7_DEPTH_TWO_NESTED_FIBERS_ARE_PRIME_REGULAR.md").read_text()
for marker in ("H7-RF-DEEP", "does not assert H7-RF-DEEP", "cut-commutativity"):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: ALL DEPTH-TWO READ-ONCE FIBERS ARE PRIME-REGULAR; H7-RF-DEEP OPEN")
