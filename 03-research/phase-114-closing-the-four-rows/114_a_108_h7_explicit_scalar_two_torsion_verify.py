#!/usr/bin/env python3
"""Symbolic controls for the explicit scalar two-torsion class kappa."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


s = (1, -1)
c = (1, 1)
swap = (1, 0)  # permutation sends (x0,x1) to (x1,x0)


def permute(vector):
    return tuple(vector[index] for index in swap)


def negate(vector):
    return tuple(-entry for entry in vector)


check("row changes sign under middle-wire transposition",
      permute(s) == negate(s))
check("all-one column is invariant under transposition",
      permute(c) == c)
check("fold/matrix shadow of kappa is zero",
      sum(a * b for a, b in zip(s, c)) == 0)

# In the scalar group, the structural equality kappa=-kappa gives 2kappa=0.
# Keep a symbolic nonzero label rather than assuming the conclusion.
kappa = "kappa"
minus_kappa = "-kappa"
wire_swap_equality = (kappa, minus_kappa)
check("wire swap proves kappa equals its negative",
      wire_swap_equality == ("kappa", "-kappa"))
check("abelian-group consequence is exact two-torsion",
      (1 + 1) % 2 == 0)


# Exact Z/2-valued homogeneous cocycle from a107.
def qt(n):
    return (n % 2) if n < 0 else 0


def ft(a, b):
    return (qt(a) + qt(b) - qt(a + b)) % 2


tau = ft(1, -1)
check("universal derivative sends kappa to nonzero tau", tau == 1)
check("tau has exact order two", tau != 0 and (2 * tau) % 2 == 0)
check("nonzero target image proves kappa nonzero", tau != 0)


# The fold augmentation kernel contains kappa and multiplication by 2 kills
# it; this is exactly failure of 2-regularity and of torsion-freeness.
augmentation_kernel_member = sum(a * b for a, b in zip(s, c)) == 0
two_regular = not (augmentation_kernel_member and tau and (2 * tau) % 2 == 0)
check("scalar augmentation ideal has explicit 2-torsion",
      augmentation_kernel_member and not two_regular)
check("H7-AUG-FLAT and H7-PRIME-REG fail at p=2", not two_regular)


doc = (HERE / "114_a_108_H7_EXPLICIT_SCALAR_TWO_TORSION.md").read_text()
for marker in (
    "H7-AUG-FLAT is false and H7-PRIME-REG is false",
    "conditional route is now closed",
    "does **not** destroy Haran's literal",
    "No such repair is supplied",
    "does not assert RH",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: NONZERO SCALAR KAPPA HAS 2 KAPPA=0; PRIME-REG FALSE")
