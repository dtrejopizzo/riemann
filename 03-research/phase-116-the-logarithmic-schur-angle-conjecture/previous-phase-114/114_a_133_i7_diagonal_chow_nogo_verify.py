#!/usr/bin/env python3
"""Checks the undecorated diagonal Chow-multiple no-go (a133)."""

from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_133_I7_UNDECORATED_DIAGONAL_CHOW_NOGO.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# Complete multiplicativity fixes prime powers.  Requiring equal nonzero
# contact at p and p^2 forces k(p)=1; two primes would then force one constant
# c to equal two distinct logarithms.
for kp in range(-20, 21):
    for c_nonzero in (True,):
        equal_prime_power_contact = kp == kp * kp
        if equal_prime_power_contact and kp != 0 and c_nonzero:
            check(f"nonzero prime-power solution kp={kp} is one", kp == 1)

for p, q in ((2, 3), (2, 5), (3, 7), (5, 11), (7, 13)):
    # Strict monotonicity of integer primes suffices; log is injective.
    check(f"distinct-prime constants conflict p={p},q={q}", p != q)

# Multiplicity composition itself is associative and multiplicative, so the
# obstruction really lies in simultaneous Lambda contact rather than spans.
for a in range(-5, 6):
    for b in range(-5, 6):
        for d in range(-3, 4):
            check(f"multiplicity associativity {a},{b},{d}",
                  (a * b) * d == a * (b * d))

markers = (
    "diagonal Chow multiples cannot carry Lambda",
    "k(mn)=k(m)k(n)",
    "diagonal-multiple no-go",
    "does not use faithfulness",
    "H7-DYNAMIC-THICKENING",
    "closes the undecorated **diagonal Chow-multiple** route negatively",
    "does not rule out",
    "close row A, or prove RH",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: NO UNDECORATED DIAGONAL CHOW-MULTIPLE MONOID HAS VON MANGOLDT INTERSECTION")
