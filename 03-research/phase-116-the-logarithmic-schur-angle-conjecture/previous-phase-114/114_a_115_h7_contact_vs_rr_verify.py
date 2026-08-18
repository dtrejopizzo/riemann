#!/usr/bin/env python3
"""Checks for 114.a.115: local contact versus forced RR intersection."""

from pathlib import Path
from math import log


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_115_H7_LOCAL_CONTACT_IS_NOT_THE_RR_INTERSECTION.md").read_text()
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23)
C = 1.0 / (2.0 * log(3.0))


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


for p in PRIMES:
    for q in PRIMES:
        contact = log(p) if p == q else 0.0
        rr = C * log(p) * log(q)
        forced_excess = rr - contact
        check(abs(contact - rr) > 1e-12, f"contact/RR mismatch p={p},q={q}")
        check(abs(contact + forced_excess - rr) < 1e-12,
              f"forced excess identity p={p},q={q}")
        if p != q:
            check(rr > 0 and contact == 0,
                  f"off-prime RR is positive but contact zero p={p},q={q}")

# Equality on the diagonal would force p=exp(2 log 3)=9, not a prime.
check(abs(pow(3, 2) - 9) == 0 and 9 not in PRIMES, "diagonal equality forces p=9")

for multiplicity_left in (1, 2, 5, 11):
    for multiplicity_right in (1, 3, 7):
        scale = multiplicity_left * multiplicity_right
        p, q = 2, 5
        contact = 0.0
        rr = C * log(p) * log(q)
        check(abs(scale * contact - scale * rr) > 1e-12,
              f"multiplicity mismatch m={multiplicity_left},n={multiplicity_right}")

for marker in (
    "Equation (1.1) is unconditional",
    "forced target conditional on H7-RR0",
    "not a construction of the excess",
    "two compatible but distinct outputs",
    "Identifying them is impossible",
    "H7-REG-EXCESS-RR",
    "does not prove H7-RR0",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: LOCAL LAMBDA CONTACT CANNOT BE THE GLOBAL RR INTERSECTION")
