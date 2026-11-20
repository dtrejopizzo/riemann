"""Exact polynomial certificate on the whole quadrant x>=1, y>=21.
No sampling of parameters; Fraction arithmetic only.
"""
from fractions import Fraction as F
from math import comb, factorial

def clean(p): return {m:c for m,c in p.items() if c}
def const(c): return {(0,0):F(c)} if c else {}
def add(p,q):
    r=p.copy()
    for m,c in q.items(): r[m]=r.get(m,F())+c
    return clean(r)
def scale(p,c): return clean({m:v*c for m,v in p.items()})
def mul(p,q):
    r={}
    for (a,b),c in p.items():
        for (d,e),v in q.items():
            m=(a+d,b+e);r[m]=r.get(m,F())+c*v
    return clean(r)
def power(p,k):
    r=const(1)
    for _ in range(k):r=mul(r,p)
    return r
def shift(p):
    r={}
    for (a,b),c in p.items():
        for i in range(a+1):
            for j in range(b+1):
                m=(i,j)
                r[m]=r.get(m,F())+c*comb(a,i)*comb(b,j)*21**(b-j)
    return clean(r)
x={(1,0):F(1)};y={(0,1):F(1)}
b=add(scale(y,2),const(-3))
# First-mode derivatives p=P/(2b), q=Q/b^2, r=R/b^3, s=S/b^4.
P=add(add(scale(power(y,2),8),scale(y,-30)),const(15))
Q=add(add(scale(power(y,3),16),scale(power(y,2),-48)),scale(y,60))
R=add(scale(mul(y,power(b,3)),8),scale(mul(y,add(scale(y,2),const(3))),-48))
S=add(scale(mul(y,power(b,4)),16),scale(mul(y,add(add(scale(power(y,2),4),scale(y,24)),const(9))),96))
def clear(terms,degree):
    out={}
    for coef,xdeg,ip,iq,ir,is_ in terms:
        denom=ip+2*iq+3*ir+4*is_
        assert denom<=degree
        term=power(x,xdeg)
        for pol,k in [(P,ip),(Q,iq),(R,ir),(S,is_),(b,degree-denom)]:
            term=mul(term,power(pol,k))
        out=add(out,scale(term,F(8*coef,2**ip)))
    return out
Cterms=[(1,0,3,0,0,0),(1,1,2,1,0,0),(-1,0,1,1,0,0),(-1,1,1,0,1,0),(1,1,0,2,0,0)]
# J=(xq-p) C' - xr C, expanded exactly.
Jterms=[(-4,0,3,1,0,0),(2,0,2,0,1,0),
        (-2,1,3,0,1,0),(2,1,2,2,0,0),(1,1,2,0,0,1),(-2,1,1,1,1,0),
        (2,2,1,3,0,0),(-1,2,1,1,0,1),(1,2,1,0,2,0)]
Cnum=add(clear(Cterms,4),scale(mul(mul(add(const(1),x),power(y,3)),power(b,4)),-32))
Jnum=add(clear(Jterms,7),scale(mul(mul(power(x,2),power(y,4)),power(b,7)),-256))
for label,p in [('C0-4(1+x)y^3',Cnum),('J0-32x^2y^4',Jnum)]:
    coeff=shift(p)
    assert coeff and all(c>0 for c in coeff.values())
    assert coeff.get((0,0),F())>0
    print('PASS whole-quadrant positive coefficients:',label,len(coeff))

# Complete theta tail, derivatives of Rtheta of orders0,...,4.
assert sum((F(3)**k/factorial(k) for k in range(8)),F())>16
assert F(4,3)**6/16**7<F(1,2)
E=F(6400,9)*3**6*21**4/F(2**84)
assert E<F(1,10**12)
z=F(63)
assert 81+F(270,z)+F(195,z*z)+F(20,z**3)<100
eps=F(1,10**12);eta=F(1,10**10)
assert eps+7*eps**2+12*eps**3+6*eps**4<eta
assert 2520*eta<21
assert 328400*eta<21
print('PASS full-theta derivatives and perturbation margins on x>=1, y>=21')
