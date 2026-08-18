"""Exact linear-algebra checks for the real numerical RR quotient."""

from fractions import Fraction


def b_rr(x, y, c=Fraction(7, 5)):
    return c * (x[0] * y[1] + x[1] * y[0])


c = Fraction(7, 5)
e1 = (Fraction(1), Fraction(0))
e2 = (Fraction(0), Fraction(1))
H = (Fraction(1), Fraction(1))
primitive = (Fraction(3), Fraction(-3))

assert b_rr(e1, e1, c) == 0
assert b_rr(e2, e2, c) == 0
assert b_rr(e1, e2, c) == c
assert b_rr(H, H, c) == 2 * c > 0
assert b_rr(H, primitive, c) == 0
assert b_rr(primitive, primitive, c) == -18 * c < 0

# If both pairings with the two coordinate directions vanish, both degree
# coordinates vanish.  This is the radical calculation in dimension two.
for a in range(-5, 6):
    for b in range(-5, 6):
        x = (Fraction(a), Fraction(b))
        radical = b_rr(x, e1, c) == 0 and b_rr(x, e2, c) == 0
        assert radical == (a == 0 and b == 0)

print("VERDICT: REAL RR NUMERICAL QUOTIENT IS THE HYPERBOLIC PLANE")
