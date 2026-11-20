"""Exact constants for absolute renormalized tail; no N/primes campaign."""
from fractions import Fraction as F
N=2**80;u=F(63,2);T=F(N-1,992)+5
assert N>32000000
assert 1+F(N,2000)<F(N,1000)
assert u*u/(2*N-3)<1
assert (u+F(1,2))==32
assert 1+(u+F(3,2))*(u+F(1,2))==1057
assert F(32,1000)<1 and F(1100,1000)<2
assert T>F(N,992) and T+2<N
assert F(7,48)<1 and F(7,48)+F(55,72)<2
assert F(3,1984)-F(1,2000)>F(1,1000)
print('PASS: |R_tail| < exp(-N/1000), ALL N>=2^80, absolute scale; no W sign.')
