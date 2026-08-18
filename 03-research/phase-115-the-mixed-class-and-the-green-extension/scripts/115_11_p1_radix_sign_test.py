"""
POINT 1 -- the radix-sign test of 115_09 section 3, test 2.

CLAIM UNDER TEST (115_09 Conjecture): the graded pieces of the semi-local
cutoff (115_09 Prop. 3, shells indexed by v_p) correspond to the digit places
of row (a)'s negabinary code.  Row (a)'s code is radix -2, i.e. place value
(-2)^j = (-1)^j 2^j, an ALTERNATING sign in the digit index j.  The shell
grading as stated carries no alternation.  The conjecture survives only if the
sign alternation has a counterpart in the coupling between shells, which is
produced by the Fourier transform on Q_2 (the only thing that is not diagonal
in the v_2 grading).

So: compute the coupling matrix of the Fourier transform in the shell basis and
compare its sign pattern with (-1)^j.

Setup.  Haar measure on Q_2 normalised so that Z_2 has measure 1.
  ball   B_v   = 2^v Z_2,            meas = 2^{-v}
  shell  e_v   = 1_{2^v Z_2^x} = 1_{B_v} - 1_{B_{v+1}},   meas = 2^{-v-1}
  FT:    hat(1_{B_v}) = 2^{-v} 1_{B_{-v}}
  hence  hat(e_v) = 2^{-v} 1_{B_{-v}} - 2^{-v-1} 1_{B_{-v-1}}

Value of hat(e_v) on the shell of valuation u:
  1_{B_{-v}}   is 1 iff u >= -v
  1_{B_{-v-1}} is 1 iff u >= -v-1
"""
from fractions import Fraction as F

V = 6
vals = list(range(-V, V+1))

def hat_e_on_shell(v, u):
    """value of hat(e_v) at a point of valuation u"""
    t = F(0)
    if u >= -v:     t += F(1, 2**v) if v >= 0 else F(2**(-v), 1)
    if u >= -v-1:   t -= (F(1, 2**(v+1)) if v+1 >= 0 else F(2**(-v-1), 1))
    return t

def pairing(v, u):
    """<hat(e_v), e_u> = (value on shell u) * meas(shell u)"""
    m = F(1, 2**(u+1)) if u+1 >= 0 else F(2**(-u-1), 1)
    return hat_e_on_shell(v, u) * m

print("Sign pattern of  <hat(e_v), e_u>   (rows v, cols u), '.' = 0\n")
hdr = "   v\\u " + "".join("%4d" % u for u in vals)
print(hdr); print("   " + "-"*(len(hdr)-3))
for v in vals:
    row = ""
    for u in vals:
        p = pairing(v, u)
        row += "   %s" % ('+' if p > 0 else ('-' if p < 0 else '.'))
    print("   %4d %s" % (v, row))

print("\nStructure found:")
neg = [(v,u) for v in vals for u in vals if pairing(v,u) < 0]
pos = [(v,u) for v in vals for u in vals if pairing(v,u) > 0]
print("  negatives lie exactly on  u + v = %s" % sorted({u+v for v,u in neg}))
print("  positives lie exactly on  u + v >= %s" % min(u+v for v,u in pos))
print("  zeros     lie exactly on  u + v <= %s" % max([u+v for v in vals for u in vals if pairing(v,u)==0], default=None))

print("\nComparison with radix -2:")
print("  negabinary place value (-2)^j = (-1)^j 2^j  ->  sign alternates with j:")
print("     j      :", "".join("%4d" % j for j in range(8)))
print("     sign   :", "".join("%4s" % ('+' if (-1)**j > 0 else '-') for j in range(8)))
print("  shell coupling sign along a row (v fixed, u increasing):")
v0 = 0
print("     u      :", "".join("%4d" % u for u in vals))
print("     sign   :", "".join("%4s" % ('+' if pairing(v0,u)>0 else ('-' if pairing(v0,u)<0 else '.')) for u in vals))

print("""
VERDICT
  The Fourier coupling between shells has exactly ONE negative band, the
  antidiagonal u+v = -1, with '+' strictly above it and 0 strictly below.
  That is a single sign flip at a fixed offset, NOT a sign alternating with
  the digit index.  Radix -2 requires (-1)^j, i.e. a flip at EVERY step.
  The two patterns do not agree.
""")
