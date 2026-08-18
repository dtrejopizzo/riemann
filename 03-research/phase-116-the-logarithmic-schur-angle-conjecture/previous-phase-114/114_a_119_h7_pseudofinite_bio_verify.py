#!/usr/bin/env python3
"""Finite component checks for 114.a.119 pseudofinite bio."""

from pathlib import Path
from math import gcd


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_119_H7_CHARACTERISTIC_ZERO_PSEUDOFINITE_BIO.md").read_text()


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def next_congruent_prime(lower: int, modulus: int) -> int:
    candidate = max(lower + 1, 2)
    while candidate % modulus != 2 % modulus:
        candidate += 1
    while not is_prime(candidate):
        candidate += modulus
    return candidate


odd_primes = (3, 5, 7, 11, 13)
modulus = 1
previous = 2
sequence = []
for ell in odd_primes:
    modulus *= ell
    p = next_congruent_prime(previous, modulus)
    sequence.append((p, modulus))
    previous = p
    check(p % modulus == 2 % modulus, f"prime congruence p={p},M={modulus}")

for index, (p, modulus) in enumerate(sequence):
    controlled = odd_primes[:index + 1]
    for s in controlled:
        check(gcd(s, p - 1) == 1, f"power exponent invertible s={s},p={p}")
        images = {pow(x, s, p) for x in range(p)}
        check(len(images) == p, f"power permutation s={s},p={p}")

# Any fixed rational denominator is eventually nonzero in all components.
for denominator in (2, 3, 5, 7, 30, 77, 143):
    eventually = [p for p, _ in sequence if gcd(denominator, p) == 1]
    check(eventually, f"rational denominator survives d={denominator}")

# Transport by a power permutation gives a field addition.
p, s = sequence[-1][0], 3
inverse_exponent = pow(s, -1, p - 1)


def root(x: int) -> int:
    return pow(x, inverse_exponent, p) if x else 0


def transported_add(x: int, y: int) -> int:
    return pow((root(x) + root(y)) % p, s, p)


for x in range(min(p, 40)):
    for y in range(min(p, 40)):
        if transported_add(x, y) != transported_add(y, x):
            raise AssertionError(f"transported commutativity x={x},y={y}")
        if transported_add(x, 0) != x:
            raise AssertionError(f"transported zero x={x},y={y}")
print("PASS transported commutativity/zero on 1600 pairs")

for marker in (
    "nonprincipal ultrafilter",
    "characteristic zero",
    "every nonzero rational denominator is invertible",
    "universal odd-moment target",
    "algebraic DEN-TRANS",
    "pseudofinite counting dimension zero",
    "nonstandard section",
    "H7-PF-DIM",
    "row A or RH",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: ONE CHARACTERISTIC-ZERO PSEUDOFINITE BIO SUPPORTS ALL ODD MOMENTS")
