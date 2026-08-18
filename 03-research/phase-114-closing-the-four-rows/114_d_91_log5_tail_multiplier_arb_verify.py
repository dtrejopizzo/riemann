#!/usr/bin/env python3
"""Directed tail lower bound for the complete log(5)/2 multiplier.

For z=1/4+i*tau/2, DLMF 5.11.2 with n=1 and its stated complex
remainder bound gives

 Re psi(z) >= log|z| - Re(1/(2z))
              - sec(arg(z)/2)^3 /(12 |z|^2).

In the right half-plane sec(arg(z)/2)^3 <= 2 sqrt(2).  Every remaining
quantity in the lower bound is monotone for tau>=150.
"""
from flint import arb, ctx
ctx.prec=192

R=arb(150); x=arb(1)/4; y=R/2; r2=x*x+y*y; r=r2.sqrt()
A=arb(2).log()/arb(2).sqrt()
A+=arb(3).log()/arb(3).sqrt()
A+=arb(2).log()/2
remainder=2*arb(2).sqrt()/(12*r2)
g=r.log()-x/(2*r2)-remainder-arb.pi().log()-2*A
# From the absolutely convergent digamma series,
# d/dy Re psi(x+iy)=sum 2y(n+x)/((n+x)^2+y^2)^2 >= 0 for y>=0.
# Hence its global minimum on this vertical line is psi(1/4), whose special
# value is -EulerGamma-pi/2-3log(2).  Bounding every cosine by one gives a
# global lower bound -M for the complete multiplier.
M=arb.const_euler()+arb.pi()/2+3*arb(2).log()+arb.pi().log()+2*A
print('radius at tau=150 =',r)
print('sum contact coefficients =',A)
print('digamma remainder upper =',remainder)
print('global complete-multiplier tail lower =',g)
print('global multiplier negative-part upper M =',M)
assert g > arb('0.22')
assert M < arb('8.315')
print('PASS r_X(tau) > 0.22 for every |tau| >= 150')
print('PASS r_X(tau) > -8.315 for every real tau')
