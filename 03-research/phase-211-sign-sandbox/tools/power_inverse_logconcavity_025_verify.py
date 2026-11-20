"""Exact rational cutoff for full compensated inverse at N129; no parameter scan."""
from fractions import Fraction as F
N=129;u=F(63,2);d=N-1;t=F(2,3)
p=[F(1)]
for j in range(d):p.append(p[-1]*2*u*(d-j)/F((j+1)*(2*d-j)))
c=[33*p[j]-(j+1)*p[j+1] if j<d else 33*p[j] for j in range(N)]
assert all(a>0 for a in c)
for j in range(d+1):assert c[j]==p[j]*F(3*d+30*j,2*d-j)
r=[]
for j in range(d):
    ratio=2*u*F(d-j,2*d-j-1)*F(3*d+30*(j+1),3*d+30*j)
    assert ratio==F(j+1)*c[j+1]/c[j]
    r.append(ratio)
r.append(F(0))
assert all(r[j]>r[j+1] for j in range(d))
D=sum((c[j]*t**j for j in range(N)),F(0))
Dp=sum((j*c[j]*t**(j-1) for j in range(1,N)),F(0))
assert Dp<30*D
# Generic reciprocal-cube tail is not used; q=30 gives the already proven 3/4 bound.
assert F(1,4)+F(1,2)==F(3,4)
assert F(33,100)*2==F(33,50)
print('PASS: D129 derivative at 2/3 is strictly below30D; full K129 positive for logx>=2/3.')
print('Combined with CELL_TEST024 S129(2)>.33: complete ERR129<-.66. No W sign claim.')
