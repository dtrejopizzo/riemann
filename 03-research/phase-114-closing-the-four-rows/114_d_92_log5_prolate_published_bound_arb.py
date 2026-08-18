#!/usr/bin/env python3
"""Directed evaluation of a published non-asymptotic PSWF bound.

Karnik--Romberg--Davenport, *Improved bounds for the eigenvalues of prolate
spheroidal wave functions and discrete prolate spheroidal sequences*,
Corollary 1 (arXiv:2006.00427), proves for k>=ceil(2c/pi)

 lambda_k(c) <= 10 exp(-(k-ceil(2c/pi)-6)/
                         ((2/pi^2) log(100c/pi+25))).

Their c equals R*T for the interval [-T,T] and angular band [-R,R].
"""
from flint import arb,ctx
ctx.prec=192
T=arb(5).log()/2; R=arb(150); c=R*T; k=95
shannon=2*c/arb.pi()
print('c, 2c/pi =',c,shannon)
assert shannon > 76 and shannon < 77
den=2/(arb.pi()**2)*(100*c/arb.pi()+25).log()
bound=10*(-arb(k-77-6)/den).exp()
threshold=arb('0.22')/(arb('8.315')+arb('0.22'))
qgap=arb('0.22')-(arb('0.22')+arb('8.315'))*bound
print('published lambda_95 upper =',bound)
print('required threshold =',threshold)
print('resulting prolate-complement lower =',qgap)
assert bound < threshold
assert qgap > arb('0.1')
print('PASS published PSWF bound certifies the prolate complement')
