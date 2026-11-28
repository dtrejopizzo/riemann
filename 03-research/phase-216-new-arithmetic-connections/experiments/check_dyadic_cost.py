"""Finite checks of algebraic ingredients; no claim to construct G_Q2 computationally."""
from fractions import Fraction
from math import factorial
import json
from pathlib import Path

def valuation2(n):
    assert n
    v=0
    while n%2==0: n//=2; v+=1
    return v

rows=[]
for k in range(1,101):
    x=Fraction(2**k,factorial(k))
    assert x.denominator%2
    rows.append({'k':k,'v2_scaled_divided_power':k-valuation2(factorial(k))})
for u in [3,7]:
    for x in range(4):
        for y in range(4):
            for z in range(4):
                assert not ((x|y|z)&1 and (z*z-u*x*x-u*y*y)%4==0)
# The alternating defect is the cocycle (1-chi)/2, and 2*defect is a coboundary.
for chi in range(1,32,2):
    for psi in range(1,32,2):
        delta=lambda a:(1-a)//2
        assert delta(chi*psi)==delta(chi)+chi*delta(psi)
        assert 2*delta(chi)==1-chi
out={'scope':'Factorial denominator upper bound, primitive mod4 obstruction and cocycle identity. General proof in ROUND-003-DYADIC.md.','checks':{'factorials':100,'primitive_mod4_candidates':128,'cocycle_pairs':256},'factorial_rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 100 factorial valuations, 128 mod4 candidates, 256 cocycle identities')
