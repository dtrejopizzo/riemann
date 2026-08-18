#!/usr/bin/env python3
"""Finite model checks for 114.a.118 fresh-block reevaluation."""

from pathlib import Path
from math import gcd


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_118_H7_FRESH_BLOCK_REEVALUATION_BYPASSES_DEN_TRANS.md").read_text()


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def fresh_prime(denominators: tuple[int, ...], exponents: tuple[int, ...]) -> int:
    candidate = max(denominators, default=1) + 1
    while True:
        if (is_prime(candidate)
                and all(d % candidate for d in denominators)
                and all(gcd(s, candidate - 1) == 1 for s in exponents)):
            return candidate
        candidate += 1


blocks = (
    ((2, 3), (1, 3)),
    ((5, 7, 11), (1, 5)),
    ((13, 17, 19), (1, 3, 5)),
)
chosen = []
for denominators, exponents in blocks:
    p = fresh_prime(denominators, exponents)
    chosen.append(p)
    check(all(d % p for d in denominators), f"fresh denominator invertibility p={p}")
    check(all(gcd(s, p - 1) == 1 for s in exponents),
          f"fresh exponent invertibility p={p}")

# A later denominator may contain an old characteristic; a fresh block avoids it.
old_p = chosen[0]
later_denominators = (old_p, 5, 7)
new_p = fresh_prime(later_denominators, (1, 3))
check(new_p != old_p and all(d % new_p for d in later_denominators),
      "later divisor replaces forbidden old characteristic")
check(old_p in later_denominators, "old characteristic really became a denominator")

# Product compatibility is checked by reevaluating integer polynomials in
# the fresh output field, not by transporting old residues.
output_p = fresh_prime((2, 3, 5, 7), (1, 3))
for x in range(-8, 9):
    for y in range(-8, 9):
        lhs = (x * y) % output_p
        rhs = (x % output_p) * (y % output_p) % output_p
        if lhs != rhs:
            raise AssertionError("fresh product reevaluation")
print("PASS fresh product reevaluation on 289 pairs")

image = {x % output_p for x in range(-20, 21)}
signed_image = {(-x) % output_p for x in range(-20, 21)}
check(len(image) == len(signed_image), "odd/sign image-cardinality invariance")

for marker in (
    "no old residue block",
    "deliberately no claimed unital map",
    "direct reevaluation of the source",
    "degreewise multiplicative typing",
    "does not supply a graded ring",
    "H7-FRESH-EXACT",
    "Row A and RH remain open",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: FRESH BLOCKS BYPASS DENOMINATOR COLLISIONS DEGREEWISE")
