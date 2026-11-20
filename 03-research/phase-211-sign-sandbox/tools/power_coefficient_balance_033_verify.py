"""One motivated Erlang coefficient cutoff22; no new N or cutoff search."""
from fractions import Fraction as F
from math import factorial
import power_fixed_grid_003 as C
import power_arch_exact_032_verify as A
u=F(63,2);J=22
arch=A.D0
for j in range(1,J+1):
    lo,hi,_=A.hurwitz(j+1);coeff=(u/2)**j
    arch-=C.I(coeff*lo,coeff*hi)
polar=2*sum((u**j*((u-F(1,2))**(-j-1)+(u+F(1,2))**(-j-1)) for j in range(J+1)),F())
def poly(t):
    z=C.I(0)
    for j in range(J,-1,-1):z=z*t+u**j/factorial(j)
    return z
prime23=2*C.log2*poly(C.log2)/2**32+2*C.logq(3)*poly(C.logq(3))/3**32
upper=arch+polar-prime23
assert upper.hi<-F(3,500)
# All q>=4 have negative comb sign; absolute upper uses Lambda<=log q.
L=C.logq(4).hi
assert 32*C.logq(4).lo>J+1
Iv=F(1,31*4**31);tail=F(0)
for ell in range(1,J+2):
    Iv=L**ell/F(31*4**31)+F(ell,31)*Iv
    endpoint=L**ell/4**32
    tail+=2*u**(ell-1)/factorial(ell-1)*(endpoint+Iv)
assert (upper-C.I(0,tail)).lo>-F(1,100)
# Fourier of even S22 at tau=u, computed exactly using z=(1+i)/2.
re,im=F(1),F(0)
for _ in range(J+1):re,im=(re-im)/2,(re+im)/2
assert im==-F(1,4096)
assert 2*im/u==-F(1,2048)/u
print('PASS: -1/100 < EXTENDED line-functional(S22) < -3/500, full arithmetic comb retained.')
print('S22 Fourier(tau=u)<0: not an admissible autocorrelation and not a counterexample to real W.')
