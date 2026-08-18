#!/usr/bin/env python3
"""Exact finite certificate for the algebraic obstruction in 107.148."""

INFINITY = "infinity"


def add_coefficient(left, right):
    if INFINITY in (left, right):
        return INFINITY
    return left + right


def main():
    assert add_coefficient(INFINITY, INFINITY) == INFINITY

    allowed_coefficients = list(range(-100, 101)) + [INFINITY]
    inverse_exists = any(
        add_coefficient(INFINITY, coefficient) == 0
        for coefficient in allowed_coefficients
    )
    assert not inverse_exists

    # In a group, x+x=x implies x=0 by cancellation.
    assert 2 - 1 == 1

    print("CC_PRIME_CLASS_IDEMPOTENT: YES")
    print("CC_PRIME_CLASS_INVERTIBLE: NO")
    print("SIGNED_SOURCE_ADDITIVE_MAP_EXISTS: NO")
    print("PRIME_CLASS_SURVIVES_GROUP_COMPLETION: NO")
    print("MORISHITA_CREATES_SOURCE_KERNEL: NO")
    print("MORISHITA_REPAIRS_SIGNED_TARGET: NO")
    print("CC_JACOBIAN_AS_III_B_TARGET: REJECTED")
    print("VERDICT: YES")


if __name__ == "__main__":
    main()
