#!/usr/bin/env python3
"""Directed concentration bound for the explicit 200-Legendre low space."""
import os
from flint import arb,ctx
ctx.prec=256

T=arb(5).log()/2; R=arb(150); c=T*R; N=int(os.environ.get('D93_N','170'))
# Fourier transform of the normalized n-th Legendre function contains the
# spherical Bessel j_n.  Its Poisson integral gives, for 0<=s<=c,
# |j_n(s)| <= sqrt(pi) s^n /(2^(n+1) Gamma(n+3/2)).
b=arb.pi().sqrt()*c**N/(arb(2)**(N+1)*arb.gamma(arb(N)+arb('1.5')))
term=(2*N+1)*b*b
# Consecutive majorant terms have ratio c^2/((2n+1)(2n+3)), decreasing in n.
ratio=c*c/(arb(2*N+1)*arb(2*N+3))
tail_trace=2*c/arb.pi()*term/(1-ratio)
qgap=arb('0.22')-(arb('0.22')+arb('8.315'))*tail_trace
print('c =',c)
print('first Bessel majorant =',b)
print('geometric ratio upper =',ratio)
print('Q band-concentration norm upper <= trace =',tail_trace)
print('joint-multiplier Q lower =',qgap)
assert ratio < arb('0.13')
assert tail_trace < arb('1e-6')
assert qgap > arb('0.219')
print('PASS explicit Legendre complement concentration certificate')
