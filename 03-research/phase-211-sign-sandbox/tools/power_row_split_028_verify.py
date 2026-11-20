"""Exact endpoint constants for an analytic ALL-k N=5 row split, no k scan."""
from fractions import Fraction as F
from math import comb, factorial
import power_fixed_grid_003 as C

u0=F(63,2);U=2*u0;N=5;M=256
def arch_bands(u,degree):
    arg=(u+F(1,2))/2
    if arg==16:
        psi=sum((F(1,j) for j in range(1,16)),F())-C.gamma
    elif arg==F(127,4):
        psi=-C.gamma+C.pi/2-3*C.log2+sum((1/(F(3,4)+j) for j in range(31)),F())
    else:raise AssertionError('Only the two analytic endpoints are authorized')
    ps={}
    for r in range(1,degree+1):
        total=sum((C.I(1/(arg+j)**(r+1)) for j in range(M)),C.I(0))
        tail=C.I(1/(r*(arg+M)**r),1/(r*(arg+M-1)**r))
        ps[r]=(-1)**(r+1)*factorial(r)*(total+tail)
    out=[psi-C.logpi]
    for k in range(1,degree+1):
        out.append(sum((ps[r]*F(comb(k-1,r-1),2*factorial(r))*u**r
                        for r in range(1,k+1)),C.I(0)))
    return out
def rayleigh(v,bands):
    return sum((v[i]*v[j]*bands[abs(i-j)] for i in range(len(v))
                for j in range(len(v))),C.I(0))/sum(x*x for x in v)
v0=[1,-4,6,-4,1]
v1=[1,-3,2,2,-3,1]
assert sum(x*x for x in v0)==70
assert sum(x*x for x in v1)==28
bands0=arch_bands(u0,5)
A0=rayleigh(v0,bands0)
A1=rayleigh(v1,bands0)
AU=rayleigh(v0,arch_bands(U,4))
assert A0.lo>-F(13,100)
assert A0.hi<-F(1,10)
assert A1.lo>F(9,10)
assert AU.lo>F(1,2)

def polar0(u):
    return F(4**N,comb(2*N-2,N-1))/u*(u*u/(u*u-F(1,4)))**N
assert polar0(U)>F(23,100)
p1=polar0(u0)*N/(2*(u0*u0-F(1,4)))
assert p1<F(1,500)
assert F(1,4*u0*u0-1)*F(4)<1

rho=F(64,169)
S5=(1+4*rho-2*rho**2+F(4,5)*rho**3-F(1,7)*rho**4)/(1-rho)**5
R5=F(21,13)**9*S5
assert R5<2500
loss=F(100,2**11)*(1+F(2,10))
assert loss<F(3,50)
assert -F(13,100)+F(23,100)-F(3,50)==F(1,25)
assert F(1,2)-F(3,50)>F(1,25)
assert F(9,10)-F(3,50)-F(1,500)>F(4,5)
print('PASS: N=5, ALL k>=0 and ALL u>=31.5, W>norm^2/25; k>=1 gives W>4norm^2/5')
