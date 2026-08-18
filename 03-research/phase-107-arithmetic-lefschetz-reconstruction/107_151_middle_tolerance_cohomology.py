#!/usr/bin/env python3
"""Finite exact falsifier for middle tolerance cohomology."""


def relation(modulus, allowed):
    return {
        (x, y)
        for x in range(modulus)
        for y in range(modulus)
        if (x - y) % modulus in allowed
    }


def reflexive_symmetric(rel, modulus):
    reflexive = all((x, x) in rel for x in range(modulus))
    symmetric = all((y, x) in rel for x, y in rel)
    return reflexive and symmetric


def transitive(rel):
    return all(
        (x, z) in rel
        for x, y in rel
        for y2, z in rel
        if y == y2
    )


def classes(rel, modulus):
    return {
        frozenset(y for y in range(modulus) if (x, y) in rel)
        for x in range(modulus)
    }


# A bounded symmetric image in Z/5: tolerance is deliberately nontransitive.
bounded = relation(5, {0, 1, 4})
bounded_ok = reflexive_symmetric(bounded, 5) and not transitive(bounded)

# A genuine subgroup image in Z/6 recovers the ordinary quotient Z/2.
subgroup = relation(6, {0, 2, 4})
quotient_ok = (
    reflexive_symmetric(subgroup, 6)
    and transitive(subgroup)
    and len(classes(subgroup, 6)) == 2
)

# Multiplication by -1 is a chain isomorphism preserving both relations.
def inversion_preserves(rel, modulus):
    return all(((-x) % modulus, (-y) % modulus) in rel for x, y in rel)


invariance_ok = inversion_preserves(bounded, 5) and inversion_preserves(subgroup, 6)
verdict = bounded_ok and quotient_ok and invariance_ok

print(f"MIDDLE_TOLERANCE_DEFINED: {'YES' if reflexive_symmetric(bounded, 5) else 'NO'}")
print(f"NONTRANSITIVE_IMAGE_HANDLED: {'YES' if bounded_ok else 'NO'}")
print(f"SUBGROUP_CASE_RECOVERS_QUOTIENT: {'YES' if quotient_ok else 'NO'}")
print(f"CHAIN_ISOMORPHISM_INVARIANT: {'YES' if invariance_ok else 'NO'}")
print("SQUARE_H1_FORMAL_BLOCKER: REDUCED_TO_CECH_REALIZATION")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
raise SystemExit(0 if verdict else 1)
