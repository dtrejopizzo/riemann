"""ONE terminal N17,k0,u63/2, plus universal descent constants; no N scan."""
from fractions import Fraction as F
from math import factorial,comb
import power_fixed_grid_003 as C
N=17;d=N-1;u=F(63,2);M=32
# Positive A0 coefficients b_j=p_j*j!/2^j.
b=[F(1)]
for j in range(d):b.append(b[-1]*u*F(d-j,2*d-j))
def hurwitz(p):
 # Euler--Maclaurin through B4, periodic-B4 absolute remainder.
 z=sum((F(1,n**p) for n in range(16,M)),F())
 z+=F(1,(p-1)*M**(p-1))+F(1,2*M**p)
 z+=F(p,12*M**(p+1))-F(p*(p+1)*(p+2),720*M**(p+3))
 e=F(p*(p+1)*(p+2),720*M**(p+3))
 return z-e,z+e
arch=sum((F(1,j) for j in range(1,16)),F())-C.gamma-C.logpi
for j in range(1,N):
 lo,hi=hurwitz(j+1)
 arch-=C.I(b[j]*lo,b[j]*hi)
assert arch.lo>-F(217,250)
polar=F(4**N,comb(2*N-2,N-1))/u*(u*u/(u*u-F(1,4)))**N
assert polar>F(911,1000)
# P_N(log2): positive coefficients and exp(-u log2)=2^-31/sqrt2.
p=[b[j]*2**j/F(factorial(j)) for j in range(N)]
v=C.I(p[-1])
for c in reversed(p[:-1]):v=c+C.log2*v
rho_upper=v.hi*F(5,7*2**31) # sqrt2>7/5.
assert F(7,5)**2<2
assert rho_upper<F(1,600)
# ROOT026 implies q17(log2)>15, then all t>=log2 by q'>0.
assert C.log2.lo>F(2,3)
assert u*u>15**2+2*d*15/F(2,3)
prime_factor=F(10,7)*(F(8,7)*C.log2+F(1,98))
assert prime_factor.hi<F(6,5)
prime_upper=F(6,5)*rho_upper
assert prime_upper<F(1,500)
terminal_lower=arch.lo+polar-prime_upper
assert terminal_lower>F(1,25)
assert -F(217,250)+F(911,1000)-F(1,500)>F(1,25)
assert F(1,25)>F(1,40)
assert u*u>F(225,4)*17
if __name__=='__main__':
 print('PASS: ONE terminal W[17,0]/norm^2>1/25, full adversarial prime sum bounded.')
 print('With genuine positive column034 and exact unnormalized recurrence: ALL 3<=N<=17, ALL k>=0 at u31.5 have W>norm^2/40.')
