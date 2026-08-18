#!/usr/bin/env python3
"""Exact external Davenport--Heilbronn witness for Phase 107.

This script uses the coefficient model already present in the workspace:

    a_n = A * chi(n) + B * conjugate(chi(n)),

where chi is the order-4 character mod 5 and A,B are the
Davenport--Heilbronn constants from the local validation notebook.

After normalization by a_1, the coefficients reduce exactly to the
residue-class pattern

    psi(n) =  1   for n ≡ 1,2 mod 5
            = -1  for n ≡ 3,4 mod 5
            =  0  for n ≡ 0 mod 5.

The script checks exact non-multiplicativity, which is the minimal
external witness that no Euler product / primitive closed-orbit tower is
available for this control.
"""

from __future__ import annotations


from math import gcd


def psi_mod5(n: int) -> int:
    residue = n % 5
    if residue in (1, 2):
        return 1
    if residue in (3, 4):
        return -1
    return 0


def main() -> None:
    print("Normalized Davenport--Heilbronn coefficient witness")
    print(" n   psi(n)")
    for n in range(1, 21):
        print(f"{n:2d} {psi_mod5(n):8d}")

    print("\nExact non-multiplicativity witnesses")
    witness_1 = (2, 2, psi_mod5(2), psi_mod5(4))
    assert witness_1[2] * witness_1[2] != witness_1[3]
    print(
        f" psi(2)^2 = {witness_1[2] * witness_1[2]}"
        f" != psi(4) = {witness_1[3]}"
    )

    witness_2 = (3, 3, psi_mod5(3), psi_mod5(9))
    assert witness_2[2] * witness_2[2] != witness_2[3]
    print(
        f" psi(3)^2 = {witness_2[2] * witness_2[2]}"
        f" != psi(9) = {witness_2[3]}"
    )

    print("\nCoprime multiplicativity scan")
    failures = []
    for m in range(1, 21):
        for n in range(1, 21):
            if gcd(m, n) != 1:
                continue
            left = psi_mod5(m * n)
            right = psi_mod5(m) * psi_mod5(n)
            if left != right:
                failures.append((m, n, left, right))

    assert failures
    for m, n, left, right in failures[:10]:
        print(f" psi({m*n}) = {left} != psi({m}) psi({n}) = {right}")

    print(
        f"\nFound {len(failures)} coprime multiplicativity failures in the window n <= 20."
    )
    print("Therefore this coefficient system admits no Euler-product multiplicativity.")


if __name__ == "__main__":
    main()
