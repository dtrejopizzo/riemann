"""Rational constants only; full-kernel inequalities are proved analytically in the memo."""
from fractions import Fraction as F
u=F(63,2);s=u+F(1,2)
assert s==32 and u+F(3,2)==33
assert s-u==F(1,2)
assert F(1,4)+F(1,2)==F(3,4)
assert 1-F(3,4)==F(1,4)
assert 1+F(3,4)==F(7,4)
assert u*s==1008
assert 1008*F(1,2**31)*(1+F(2,30))<F(1,4)
assert 1+F(1,2**32)*(1+F(2,31))<2
print('PASS: constants for complete inverse positivity region and global N=2 case')
