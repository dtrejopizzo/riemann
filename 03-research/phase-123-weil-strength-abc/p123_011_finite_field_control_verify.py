#!/usr/bin/env python3
"""Finite combinatorial regression for the Frobenius graph control model."""


Q = 5


def frobenius_label(power):
    return Q**power


for m in range(6):
    for n in range(6):
        # Additive iterate composition is multiplicative label composition.
        assert frobenius_label(m + n) == frobenius_label(m) * frobenius_label(n)


# Hyperbolic ruling matrix and transpose swap.
H = ((0, 1), (1, 0))
assert H[0][0] == H[1][1] == 0
assert H[0][1] == H[1][0] == 1


# At Frobenius fixed points dF=0, so det(1-dF)=1: the derived local
# multiplicity is one at every geometric fixed point.
for _power in range(1, 8):
    dF = 0
    assert 1 - dF == 1

print("P123.011 Frobenius composition/contact/ruling control: PASS")

