#!/usr/bin/env python3
"""Finite-set shadow of the prime-ruling span composition no-go."""


X = ("eta", 2, 3, 5, 7)


def ruling(p):
    """Relation shadow of x_p times X, oriented left to right."""
    return {(p, y) for y in X}


def compose(left, right):
    """First left, then right."""
    return {(x, z) for x, y in left for y2, z in right if y == y2}


print("A. Prime ruling composition")
for p in (2, 3, 5, 7):
    for q in (2, 3, 5, 7):
        assert compose(ruling(p), ruling(q)) == ruling(p)
print("  R_p followed by R_q retains the left endpoint p")

print("\nB. Failure of commutativity for distinct primes")
for p in (2, 3, 5, 7):
    for q in (2, 3, 5, 7):
        if p != q:
            assert compose(ruling(p), ruling(q)) != compose(ruling(q), ruling(p))
print("  R_p o R_q differs from R_q o R_p whenever p != q")

print("\nC. Failure of label faithfulness")
assert compose(ruling(2), ruling(3)) == compose(ruling(2), ruling(5))
assert compose(ruling(3), ruling(2)) == ruling(3)
print("  different multiplicative labels collapse even before symmetrization")

print("\nVERDICT: I7 PRIME-RULING SPAN NO-GO CHECKS PASS")
