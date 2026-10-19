#!/usr/bin/env python3
"""Exact finite regressions. Not certificates of topology, descent, or RH."""
from fractions import Fraction as Q
from math import gcd
from random import Random


def cf(c=0, d=None):
    return Q(c), {Q(k): Q(v) for k, v in (d or {}).items() if v}


def ca(a, b):
    c, d = a
    e, f = b
    return cf(c + e, {k: d.get(k, 0) + f.get(k, 0) for k in d.keys() | f.keys()})


def cm(a, b):
    c, d = a
    e, f = b
    return cf(c * e, {k: c*f.get(k, 0) + e*d.get(k, 0) + d.get(k, 0)*f.get(k, 0)
                     for k in d.keys() | f.keys()})


def alpha(q, a):
    c, d = a
    return cf(c, {q*k: v for k, v in d.items()})


ZERO = cf()
ONE = {Q(1): cf(1)}


def clean(a):
    return {q: c for q, c in a.items() if c != ZERO}


def mul(a, b):
    out = {}
    for q, c in a.items():
        for r, d in b.items():
            out[q*r] = ca(out.get(q*r, ZERO), cm(c, alpha(q, d)))
    return clean(out)


def beta(a, x):
    return {q: alpha(a, c) for q, c in x.items()}


def star(x):
    return {1/q: alpha(1/q, c) for q, c in x.items()}


def unit(q):
    return {Q(q): cf(1)}


x = {Q(2): cf(3, {1: 4, 3: -2}), Q(1, 3): cf(0, {2: 7})}
y = {Q(1): cf(-1, {3: 5}), Q(3): cf(2, {1: -4})}
z = {Q(1, 2): cf(1, {2: 3})}
a, b, gamma, delta = Q(5), Q(7), Q(2), Q(3)
assert mul(x, ONE) == mul(ONE, x) == x
assert mul(mul(x, y), z) == mul(x, mul(y, z))
assert star(mul(x, y)) == mul(star(y), star(x))
assert beta(gamma*a, x) == mul(mul(unit(gamma), beta(a, x)), unit(1/gamma))
# Lift change intertwines the twisted right action.
assert mul(mul(x, beta(gamma*a, y)), unit(gamma)) == mul(mul(x, unit(gamma)), beta(a, y))
# Tensor and simultaneous lift-change coherence.
assert mul(mul(x, unit(gamma)), beta(a, mul(y, unit(delta)))) == \
       mul(mul(x, beta(gamma*a, y)), unit(gamma*delta))
assert mul(mul(x, beta(a, y)), beta(a*b, z)) == mul(x, beta(a, mul(y, beta(b, z))))
# The old C0 ideal remains an ideal in this finite-support coefficient model.
ideal = {Q(2): cf(0, {1: 2, 3: 4})}
assert all(c[0] == 0 for c in mul(x, ideal).values())
assert all(c[0] == 0 for c in mul(ideal, x).values())
print('PASS exact multiplier-containing crossed-product and bimodule identities')


def vp(x, p):
    x = Q(x)
    n, d = abs(x.numerator), x.denominator
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def rational_part(a, S):
    q = Q(1)
    for p in S:
        q *= Q(p) ** vp(a[p], p)
    return q


def normform(a, S):
    q = rational_part(a, S)
    return {v: x/q for v, x in a.items()}


def lift(a, S, T):
    q = rational_part(a, S)
    return dict(a) | {p: q for p in T if p not in S}


def module(a, S):
    q = abs(a['inf'])
    for p in S:
        q *= Q(p) ** (-vp(a[p], p))
    return q


rng = Random(123020)
S, T, U = (2,), (2, 3), (2, 3, 5)
for _ in range(100):
    a = {'inf': Q(rng.choice([-7, 2, 5]), rng.choice([1, 3])),
         2: Q(rng.choice([2, 3, 4, 7]), rng.choice([1, 2, 8]))}
    b = {'inf': Q(3), 2: Q(5, 4)}
    g = Q(2) ** rng.randint(-4, 4)
    ga = {v: g*x for v, x in a.items()}
    assert normform(a, S) == normform(ga, S)
    la, lga = lift(a, S, T), lift(ga, S, T)
    assert lga == {v: g*x for v, x in la.items()}
    assert lift(la, T, U) == lift(a, S, U)
    assert normform(la, T) == normform(a, S) | {3: Q(1)}
    assert module(la, T) == module(a, S)
    ab = {v: a[v]*b[v] for v in a}
    lb = lift(b, S, T)
    assert lift(ab, S, T) == {v: la[v]*lb[v] for v in la}
    for yy in [Q(1), Q(3), Q(1, 3), Q(9, 2)]:
        assert (vp(yy, 3) >= 0) == (vp(yy/rational_part(a, S), 3) >= 0)
# Original bad map fails; repaired map passes on the very same lifts.
e = {'inf': Q(1), 2: Q(1)}
g = {'inf': Q(2), 2: Q(2)}
assert normform(e | {3: Q(1)}, T) != normform(g | {3: Q(1)}, T)
assert normform(lift(e, S, T), T) == normform(lift(g, S, T), T)
print('PASS exact normalized chart, gauge, triple, Tate and compact-unit identities')

# C2 graph algebra: coordinatewise effectivity differs from source squares.
def c2mul(a, b):
    return a[0]*b[0]+a[1]*b[1], a[0]*b[1]+a[1]*b[0]
assert c2mul((1, -1), (1, -1)) == (2, -2)
assert (1 + -1, 1 - -1) == (0, 2)  # eigenvalues of e-t
assert (0 + 1, 0 - 1) == (1, -1)   # eigenvalues of effective t
phis = {2: [1, 1], 4: [1, 0, 1], 3: [1, 1, 1], 6: [1, -1, 1]}
vals = {n: sum(c) for n, c in phis.items()}
assert vals == {2: 2, 4: 2, 3: 3, 6: 1}
assert gcd(vals[2], vals[2]) == vals[4]
assert gcd(vals[2], vals[3]) == vals[6]
print('PASS exact cone counterexample and existing cyclotomic coefficient checks')
print('SCOPE: finite regressions only; no full-Hom descent, integral realization, RR or sign claim')
