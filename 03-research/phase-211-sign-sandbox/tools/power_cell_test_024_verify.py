"""One exact first-cell test N=129, including the entire Moebius tail."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
N=129;d=N-1;u=F(63,2);M=64
p=[F(1)]
for j in range(d):p.append(p[-1]*2*u*(N-1-j)/F((j+1)*(2*N-2-j)))
q=[F() for _ in range(N)]
q[d]=p[d]/31
for j in range(d-1,-1,-1):q[j]=(p[j]+(j+1)*q[j+1])/31
assert all(z>0 for z in p+q)
for j in range(N):assert 31*q[j]-((j+1)*q[j+1] if j<d else 0)==p[j]
def moebius(n):
    sign=1;prime=2
    while prime*prime<=n:
        if n%prime==0:
            n//=prime;sign=-sign
            if n%prime==0:return 0
        prime+=1
    if n>1:sign=-sign
    return sign
def poly(coeffs,x):
    out=C.I(0)
    for coeff in reversed(coeffs):out=out*x+coeff
    return out
integral=C.I(0);endpoint=C.I(0);endpoint1=C.I(0)
for m in range(1,M+1):
    mu=moebius(m)
    if not mu:continue
    l=C.logq(m);l2m=l+C.log2
    integral+=F(mu,m**32)*(poly(q,l)-poly(q,l2m)/2**31)
    endpoint+=F(mu,2**32*m**32)*poly(p,l2m)
    endpoint1+=F(mu,m**32)*poly(p,l)
cell=integral-F(3,4)*endpoint
arithmetic_cell=integral-C.log2*endpoint
mass_cell=endpoint1-endpoint/2
assert 6*C.log2.lo>4>=F(d,32)
L=F(21,5)
assert C.logq(M).hi<L
ig=[F(1,31*M**31)]
for j in range(1,N):ig.append(F(1,31*M**31)*L**j+F(j,31)*ig[-1])
tailP=sum((a*b for a,b in zip(p,ig)),F())
tail=2*tailP
assert tail<F(1,10**10)
assert cell.lo-tail>F(31,100)
assert cell.hi+tail<F(8,25)
assert arithmetic_cell.lo-tail>F(33,100)
assert arithmetic_cell.hi+tail<F(1,3)
assert mass_cell.lo-tail>F(1,2)
assert mass_cell.hi+tail<F(3,5)
print('PASS: full first-cell K*C_B > .31; arithmetic S_129(2) > .33; mass cell > .5')
print('First-cell integral K*C_B:',float(cell.lo-tail),float(cell.hi+tail))
print('Arithmetic cell S_129(2):',float(arithmetic_cell.lo-tail),float(arithmetic_cell.hi+tail))
print('Weighted MASS first cell:',float(mass_cell.lo-tail),float(mass_cell.hi+tail))
print('J_129(2) enclosure:',float(endpoint.lo-tailP),float(endpoint.hi+tailP))
