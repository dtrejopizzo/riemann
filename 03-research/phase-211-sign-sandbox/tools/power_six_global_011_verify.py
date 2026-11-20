"""Exact rational six-pole global certificate; no floating point or special functions."""
from fractions import Fraction as F
from math import comb,factorial
import power_fixed_grid_003 as C
u=F(63,2);n=6
mzero=-C.gamma-C.pi/2-3*C.log2-C.logpi
assert mzero.lo>-F(5373,1000)
# Psi derivatives at 16: direct sum through M and integral tail.
M=2000;ps={}
for j in range(1,n):
 part=sum((C.I(F(1,k**(j+1))) for k in range(16,M+1)),C.I(0))
 tail=C.I(F(1,j*(M+1)**j),F(1,j*M**j))
 ps[j]=(-1)**(j+1)*factorial(j)*(part+tail)
r=F(32,31)
bands=[sum((F(1,k) for k in range(1,16)),F(0))-C.gamma-C.logpi+4*u/(u*u-F(1,4))]
for k in range(1,n):
 arch=sum((ps[j]*F(1,2**(j+1))*(2*u)**j*F(comb(k-1,j-1),factorial(j)) for j in range(1,k+1)),C.I(0))
 polar=2*u/(u*u-F(1,4))*(-1)**k*(r**k+r**(-k))
 bands.append(arch+polar)
T=[[bands[abs(i-j)]-(F(3,25) if i==j else 0) for j in range(n)] for i in range(n)]
for k in range(n):
 p=T[k][k];assert p.lo>0,(k,p)
 for i in range(k+1,n):
  for j in range(i,n):T[i][j]=T[j][i]=T[i][j]-T[i][k]*T[j][k]/p
# |Polar|<norm^2 in the base model.
AA=F(63,31**2)*sum((F(32,31)**(2*j) for j in range(n)),F(0))
BB=F(63,32**2)*sum((F(31,32)**(2*j) for j in range(n)),F(0))
assert 4*AA*BB<1
# Scalar multiplier negative sector, only 25 panels.
def lower(x):
 return -F(5373,1000)+sum((F(x)/(F(4*k+1,4)*(4*F(4*k+1,4)**2+x)) for k in range(16)),F(0))
c=F(1,20)
pts=[F(0),F(1,4),1,2,3,4,6,8,10]+list(range(12,25))+[28,32,40,49]
assert lower(49)>c
for a,b in zip(pts,pts[1:]):assert b*max(F(0),c-lower(a))<9,(a,b)
K=((1+49/(u*u))**n-1)/49
assert F(3,25)-c-9*K-F(n,4)/(u*u)>F(3,500)
# Weighted all-pass estimate with sigma=3u/4: each Fourier multiplier<=7,
# and initial squared L2 norm<=4. B6=4 sum49^j.
B=(49**n-1)//12
assert B==1153440600
assert 4*B<68000**2
# exponent sigma+1/2>24; Lambda<=log.
assert 3*u/4+F(1,2)>24
prime=F(68000,2**24)*(F(7,10)+F(14,230)+F(2,529))
assert prime<F(1,250)
assert c-F(1,250)>F(1,25)
print('PASS: exact APbase>3/25, polar norm, 25 scalar panels, filter margin>3/500, prime cost<1/250.')
print('Global conclusion: W[f]>(1/25)||f||^2 on every six-real-pole space with poles>=63/2.')
