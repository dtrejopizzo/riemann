"""One directed COMPLETE test K_129(1), with the infinite Moebius tail enclosed."""
from fractions import Fraction as F
import power_fixed_grid_003 as C

N=129;u=F(63,2);s=F(32);d=N-1;M=64
p=[F(1)]
for j in range(d):
    p.append(p[-1]*2*u*(N-1-j)/F((j+1)*(2*N-2-j)))
a=[s*p[j]-(j+1)*p[j+1] if j<d else s*p[j] for j in range(N)]
b=[p[j]+a[j] for j in range(N)]
assert all(z>0 for z in b)
def moebius(n):
    sign=1;prime=2
    while prime*prime<=n:
        if n%prime==0:
            n//=prime;sign=-sign
            if n%prime==0:return 0
        prime+=1
    if n>1:sign=-sign
    return sign
def poly(x):
    out=C.I(0)
    for coeff in reversed(b):out=out*x+coeff
    return out
partial=C.I(0)
for m in range(1,M+1):
    mu=moebius(m)
    if mu:partial+=mu*poly(C.logq(m))/m**32
assert 6*C.log2.lo>4>=F(d,32)
L=F(21,5)
assert C.logq(M).hi<L
integrals=[F(1,31*M**31)]
for j in range(1,N):
    integrals.append(F(1,31*M**31)*L**j+F(j,31)*integrals[-1])
tail=sum((coeff*integ for coeff,integ in zip(b,integrals)),F())
assert tail<F(1,10**10)
assert partial.lo-tail>-F(1,250)
assert partial.hi+tail<-F(1,251)
print('PASS: -1/250 < COMPLETE K_129(1) < -1/251; entire m>=65 tail < 1/10^10')
print('Diagnostic outward enclosure:',float(partial.lo-tail),float(partial.hi+tail))
