"""Exact constants and the magnitude of ONE actual gamma joint tail, N129."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
ell=1+C.gamma/2-C.log2-C.logpi/2
assert ell.lo>F(1,50)
assert C.gamma.hi<1 and C.log2.hi<F(7,10) and C.logpi.hi<F(6,5)
# The negative constant in the floor-error bound is <9:
assert 4+F(7,10)+F(1+1+F(14,10)+F(6,5),2)+F(7,4)<9
T=4096
assert F(1,50)-(48*F(7,10)+9)/T>F(9,1000)
assert 4*C.log2.hi<3
u=F(63,2);d=128
p=[F(1)]
for j in range(d):p.append(p[-1]*2*u*(d-j)/F((j+1)*(2*d-j)))
c=[33*p[j]-(j+1)*p[j+1] if j<d else 33*p[j] for j in range(d+1)]
assert all(a>0 for a in c)
t0=F(2,3)
assert sum((j*c[j]*t0**(j-1) for j in range(1,d+1)),F())<30*sum((c[j]*t0**j for j in range(d+1)),F())
L=12*C.log2.hi
value=F(0)
for a in reversed(c):value=value*L+a
G_upper=value/T**32
joint_tail_upper=F(7,4)*G_upper*(T*(L+2)+3*T*T)
assert 0<joint_tail_upper<F(1,10**36)
# Explicit positive lower certificate (.009/4)*integral G; its scale is tiny.
q=[F(0)]*(d+1);q[-1]=c[-1]/31
for j in range(d-1,-1,-1):q[j]=(c[j]+(j+1)*q[j+1])/31
value=F(0)
for a in reversed(q):value=value*L+a
lower_certificate_upper=F(9,4000)*value/T**31
assert 0<lower_certificate_upper<F(4,10**45)
print('PASS: ell>1/50; Omega>9/1000 for all t>=4096 off integer singularities.')
print('PASS: ONE actual gamma tail N129 satisfies 0<joint_tail<1e-36; no interior or W sign claim.')
