#!/usr/bin/env python3
"""Exact auxiliary checks; the memo proves all-N formulas analytically."""
from fractions import Fraction as F
from math import factorial

def p(d):
    return [F(factorial(2*d-j),2**(d-j)*factorial(d-j)*factorial(j)) for j in range(d+1)]
def der(a): return [(j+1)*a[j+1] for j in range(len(a)-1)]
def at(a,j): return a[j] if j<len(a) else F(0)
for n in (1,2,3,7,211):
    a=p(n); ap=der(a); app=der(ap)
    r=[at(a,j)-2*at(ap,j)+at(app,j) for j in range(n+1)]
    if n>=2:
        for j in range(n+1):
            assert r[j]/a[j]==F(j*(j+1)-2*n,(2*n-j)*(2*n-j-1))
        b=p(n-1); c=p(n-2)
        assert a==[(2*n-1)*at(b,j)+(at(c,j-2) if j>=2 else F(0)) for j in range(n+1)]
        assert r==[(at(c,j-2) if j>=2 else F(0))-at(b,j) for j in range(n+1)]
    b=p(n-1)
    assert [at(ap,j)-at(a,j) for j in range(n+1)]==[-at(b,j-1) if j>=1 else F(0) for j in range(n+1)]
    for j in range(1,n+1): assert a[j]/b[j-1]==F(2*n-j,j)
assert 21**2-21-(2*211-3)==1
assert F(63,2)*F(2,3)==21
print('PASS: exact identities, endpoints, and arithmetic-contact threshold211')
