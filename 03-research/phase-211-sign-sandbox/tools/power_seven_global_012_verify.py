"""Exact rational seven-pole certificate, direct deficit and weighted trace."""
from fractions import Fraction as F
from math import comb, factorial
import power_fixed_grid_003 as C

u=F(63,2); n=7
mzero=-C.gamma-C.pi/2-3*C.log2-C.logpi
assert mzero.lo>-F(5373,1000)
M=2000; ps={}
for r in range(1,n):
    total=sum((C.I(F(1,k**(r+1))) for k in range(16,M+1)),C.I(0))
    tail=C.I(F(1,r*(M+1)**r),F(1,r*M**r))
    ps[r]=(-1)**(r+1)*factorial(r)*(total+tail)
bands=[sum((F(1,k) for k in range(1,16)),F())-C.gamma-C.logpi+4*u/(u*u-F(1,4))]
ratio=F(32,31)
for k in range(1,n):
    arch=sum((ps[r]*F(comb(k-1,r-1),2*factorial(r))*u**r
              for r in range(1,k+1)),C.I(0))
    polar=2*u/(u*u-F(1,4))*(-1)**k*(ratio**k+ratio**(-k))
    bands.append(arch+polar)
mat=[[bands[abs(i-j)]-(F(69,1000) if i==j else 0) for j in range(n)] for i in range(n)]
for k in range(n):
    pivot=mat[k][k]
    assert pivot.lo>0,(k,pivot)
    for i in range(k+1,n):
        for j in range(i,n):
            mat[i][j]=mat[j][i]=mat[i][j]-mat[i][k]*mat[k][j]/pivot
AA=F(63,31**2)*sum((ratio**(2*j) for j in range(n)),F())
BB=F(63,32**2)*sum((ratio**(-2*j) for j in range(n)),F())
assert 4*AA*BB<1

def lower(x):
    return -F(5373,1000)+sum((x/(F(4*k+1,4)*(4*F(4*k+1,4)**2+x)) for k in range(16)),F())
c=F(1,100)
assert lower(49)>F(1,20)>c
for j in range(196):
    left=F(j,4);right=F(j+1,4)
    deficit=max(F(),c-lower(left))*((1+right/u**2)**n-1)
    assert deficit<F(57,1000),(j,deficit)
assert F(69,1000)-c-F(57,1000)-F(n,4)/u**2>0

alpha=F(2,3)
trace=sum((sum((F(comb(j,k)**2)*alpha**(2*k) for k in range(j+1)),F())/
            (1-alpha)**(2*j+1) for j in range(n)),F())
assert trace==176673441
assert 4*trace<26600**2
assert F(7,5)**2<2
assert F(7,10)+F(14,200)+F(2,400)==F(31,40)
prime=F(26600)*F(5,7)*F(31,40*2**21)
assert prime<F(1,125)
assert c-prime>F(1,500)
print('PASS: AP base>.069; direct deficit<.057; trace=176673441; W>1/500 for all seven poles>=31.5')
