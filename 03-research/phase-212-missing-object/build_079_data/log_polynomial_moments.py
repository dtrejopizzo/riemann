"""Exact moments for endpoint logarithms, BUILD083 (65).

A result (a,b) means a+b*pi**2. This does not certify the full residual.
Polynomials use ascending coefficients; functions have three components
p(t)+q(t)*log(t)+r(t)*log(1-t). Real rational coefficients only.
"""
from fractions import Fraction as F
from functools import lru_cache


@lru_cache(None)
def moment(n, left=0, right=0):
    if n < 0 or left < 0 or right < 0 or left+right > 2:
        raise ValueError('Nonnegative degree and total logarithmic power <=2 required')
    k = n+1
    h = sum((F(1,j) for j in range(1,k+1)), F(0))
    h2 = sum((F(1,j*j) for j in range(1,k+1)), F(0))
    return {
        (0,0): (F(1,k), F(0)),
        (1,0): (-F(1,k*k), F(0)),
        (0,1): (-h/k, F(0)),
        (2,0): (F(2,k**3), F(0)),
        (0,2): ((h*h+h2)/k, F(0)),
        (1,1): (h/(k*k)+h2/k, -F(1,6*k)),
    }[left,right]


def inner(f, g):
    """Exact real L2 pairing, as rational constant + rational*pi²."""
    powers = ((0,0),(1,0),(0,1))
    result = [F(0), F(0)]
    for p, (a,b) in zip(f,powers):
        for q, (c,d) in zip(g,powers):
            for i,u in enumerate(p):
                for j,v in enumerate(q):
                    if u and v:
                        pair = moment(i+j,a+c,b+d)
                        for k in range(2):
                            result[k] += F(u)*F(v)*pair[k]
    return tuple(result)


def self_check():
    one = ([1],[],[])
    l = ([],[1],[])
    r = ([],[],[1])
    assert inner(one,one) == (F(1),F(0))
    assert inner(l,l) == (F(2),F(0))
    assert inner(r,r) == (F(2),F(0))
    assert inner(l,r) == (F(2),-F(1,6))
    # Reflection identity: log(t)-log(1-t) has zero mean,
    # and its exact squared norm is pi²/3.
    difference = ([],[1],[-1])
    assert inner(one,difference) == (F(0),F(0))
    assert inner(difference,difference) == (F(0),F(1,3))
    print('PASS: exact endpoint-logarithm moments and reflection checks')


if __name__ == '__main__':
    self_check()
