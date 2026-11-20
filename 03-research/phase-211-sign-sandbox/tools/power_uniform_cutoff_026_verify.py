"""Only endpoint and algebraic constants for the uniform analytic cutoff; no row scan."""
from fractions import Fraction as F
from math import comb
u2=F(3969,4)
assert u2-F(9,4)==990
# Shifted derivative polynomial is positive for all x>=5.
coeff=[-194481,-778365,192276,880]
shift=[sum(coeff[k]*comb(k,j)*5**(k-j) for k in range(j,4)) for j in range(4)]
assert shift==[830594,1210395,205476,880]
assert all(z>0 for z in shift)
for d in (2,128):
    q2=F(9,4)+u2/F(2*d-1)
    den=u2-q2
    assert den>0
    assert 9*d*d*q2<den*den
assert 0<F(1,30)-F(1,693)<F(2,3)
assert F(2079,2)==F(33)*F(63,2)
assert F(1,4)+F(1,2)==F(3,4)
print('PASS: uniform Riccati endpoint constants and shifted derivative polynomial; no row-by-row certificates')
