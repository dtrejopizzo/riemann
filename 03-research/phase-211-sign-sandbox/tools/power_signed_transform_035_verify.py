"""Symbolic identities only: no numerical dimension or coefficient campaign."""
import sympy as S
from fractions import Fraction as Q
import power_fixed_grid_003 as C
d,r,R,j,A=S.symbols('d r R j A', positive=True)
tail=A*(1+r*(r-1)/(2*(2*d-r)))
nexta=A*2*(d-r)/(2*d-r)
nexttail=nexta*(1+(r+1)*r/(2*(2*d-r-1)))
point=A*r*(r-1)*(r+1)/(2*(2*d-r)*(2*d-r-1))
assert S.factor(tail-nexttail-point)==0
poly=S.summation(j*(j*j-1),(j,1,R))
assert S.factor(poly-R*(R-1)*(R+1)*(R+2)/4)==0
# Adjacent ratios for v=w/j and a, formal in d/r.
assert S.factor(2*(d-r)/(2*d-r-1)-(2*(d-r)/(2*d-r))*(2*d-r)/(2*d-r-1))==0
# Generic cosh-positive MODEL limitation, not the actual arithmetic datum.
assert (51-76*C.log2).hi<0
print('PASS: symbolic tail/CDF and quartic-prefix identities; no evaluated N or m.')
print('Generic cosh-model sign check only; no claim about arithmetic W.')
