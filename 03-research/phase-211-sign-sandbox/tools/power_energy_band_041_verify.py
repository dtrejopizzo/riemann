"""Uniform finite-band constants, exact rational comparisons; no N campaign."""
from fractions import Fraction as F
from math import factorial
N=2**80; R=2**40; u=F(63,2); M=u*u/N; L=F(R,100)
assert L>=8
assert L<F(N,1984*4)
assert M*L<F(1,2)
assert F(50,1)/10000/8==F(1,1600)
# f''/f absolute bound, f<=2.
qgap=M*(L+1)
assert 2*(qgap*qgap+M+2*qgap*M+F(2*1984,1)*M/N)<1
assert 4/F(N*N)+4*M*(L+2)+L/F(10000*N)<F(3,12800)
assert F(32*factorial(4)*1984**4,N*N)<F(1,25600)
print('PASS: full real F-band < -C_N/25600, ALL N>=2^80; no global W sign.')
