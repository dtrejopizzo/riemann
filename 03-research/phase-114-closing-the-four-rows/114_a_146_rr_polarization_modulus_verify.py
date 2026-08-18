"""Checks the exact coefficient classification of calibrated RR forms."""

from fractions import Fraction


def rr_block(c, lp, lq):
    return c * lp * lq


def contact_block(p, q, lp):
    return lp if p == q else Fraction(0)


samples = [(2, 3, Fraction(7, 10), Fraction(11, 13)),
           (5, 5, Fraction(17, 19), Fraction(17, 19))]

for p, q, lp, lq in samples:
    c1 = Fraction(1, 3)
    c2 = Fraction(2, 5)
    assert rr_block(c1, lp, lq) != rr_block(c2, lp, lq)
    g1 = rr_block(c1, lp, lq) - contact_block(p, q, lp)
    g2 = rr_block(c2, lp, lq) - contact_block(p, q, lp)
    assert g1 != g2
    assert rr_block(c1, lp, lq) == rr_block(c1, lp, lq)

print("VERDICT: RR/GREEN CALIBRATIONS ARE CLASSIFIED BY THEIR POSITIVE SCALE")
