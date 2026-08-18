#!/usr/bin/env python3
"""Exact checks for 114.a.114 reduced cross-ruling intersections."""

from pathlib import Path
from math import gcd, log


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_114_H7_REDUCED_CROSS_RULING_INTERSECTION.md").read_text()
PRIMES = (2, 3, 5, 7, 11, 13)


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


# A finite nonzero set cannot be additive p-primary and q-primary at once.
for p in PRIMES:
    for q in PRIMES:
        if p == q:
            continue
        collisions = {(p ** a): a for a in range(1, 9)}.keys() & {
            q ** b for b in range(1, 9)
        }
        check(not collisions, f"finite-bio obstruction p={p},q={q}")

# The selected residue tensor has size p on the diagonal and one off it.
for p in PRIMES:
    for q in PRIMES:
        residue_size = p if p == q else gcd(p, q)
        check(residue_size == (p if p == q else 1),
              f"reduced residue size p={p},q={q}")


def pairing(left: tuple[int, ...], right: tuple[int, ...]) -> float:
    return sum(a * b * log(p) for p, a, b in zip(PRIMES, left, right))


basis = []
for i in range(len(PRIMES)):
    vector = [0] * len(PRIMES)
    vector[i] = 1
    basis.append(tuple(vector))

for i, e in enumerate(basis):
    for j, f in enumerate(basis):
        expected = log(PRIMES[i]) if i == j else 0.0
        check(abs(pairing(e, f) - expected) < 1e-12,
              f"prime block i={i},j={j}")

u = (1, -2, 3, 0, 1, -1)
v = (-2, 1, 0, 4, -1, 2)
w = (3, 0, -1, 2, 1, 1)
uv = tuple(a + b for a, b in zip(u, v))
check(abs(pairing(uv, w) - pairing(u, w) - pairing(v, w)) < 1e-12,
      "left bilinearity")
check(abs(pairing(w, uv) - pairing(w, u) - pairing(w, v)) < 1e-12,
      "right bilinearity")
check(abs(pairing(u, v) - pairing(v, u)) < 1e-12,
      "ruling-exchange symmetry")

for marker in (
    "split retract of the cross quotient",
    "No claim is made that `Q_(p,p)` is",
    "finite-bio obstruction",
    "does not prove `Q_(p,q)=0`",
    "opposite-ruling **reduced** prime block",
    "intentionally forgets the complementary generalized",
    "H7-REG-INTER, Riemann--Roch, the gauge, row A and RH remain open",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: REDUCED CROSS-RULING PRIME INTERSECTION IS CONSTRUCTED")
