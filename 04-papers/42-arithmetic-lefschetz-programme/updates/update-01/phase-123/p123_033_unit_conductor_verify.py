#!/usr/bin/env python3
"""Exact finite unit-group regression for P123.033; no nuclear trace claim."""
from fractions import Fraction as F
from math import gcd


def convolve(a, b, modulus):
    out = {u:F(0) for u in a}
    for u, x in a.items():
        for v, y in b.items():
            out[u*v % modulus] += x*y
    return out


cases = 0
for p in (2,3,5):
    for level in range(1,4):
        modulus = p**level
        units = [u for u in range(1,modulus) if gcd(u,p)==1]
        projectors = []
        for r in range(level+1):
            subgroup = units if r == 0 else [u for u in units if (u-1) % p**r == 0]
            projectors.append({u:F(int(u in subgroup),len(subgroup)) for u in units})
        kernel = {u:F(0) for u in units}
        for u in units:
            if u == 1:
                continue
            diff, valuation = u-1, 0
            while diff % p == 0:
                diff //= p
                valuation += 1
            weight = F(p**valuation,len(units))
            kernel[u] += weight
            kernel[1] -= weight
        formula = {u:sum(projectors[r][u] for r in range(level))-level*int(u==1)
                   for u in units}
        assert kernel == formula, (p,level)
        assert all(x==0 for x in convolve(kernel, projectors[0],modulus).values())
        for a in range(1,level+1):
            layer = {u:projectors[a][u]-projectors[a-1][u] for u in units}
            assert convolve(kernel,layer,modulus) == {u:-a*x for u,x in layer.items()}
        cases += 1
print(f'PASS {cases} finite unit groups: kernel formula and all conductor layers')
print('SCOPE: exact rational finite groups; no cutoff normalization or common shadow verified')
