"""Exact tests of the affine action on integer-valued polynomial lattices."""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path

def binom(x,j):
 y=F(1)
 for k in range(j): y*=x-k
 return y/factorial(j)
checks=0
for p in (3,5,7):
 for n in range(1,9):
  for u in range(1,2*p):
   if u%p==0: continue
   for c in range(p+1):
    for j in range(n+1):
     values=[u**n*binom(F(k+c,u),j) for k in range(j+1)]
     coeff=[]
     while values:
      coeff.append(values[0]); values=[values[k+1]-values[k] for k in range(len(values)-1)]
     assert all(a.denominator%p for a in coeff)
     assert coeff[j]==u**(n-j)
     if j: assert coeff[j-1]==u**(n-j)*(c+F((j-1)*(1-u),2))
     checks+=1
result={'action':'u^n P((t+c)/u)','primes':[3,5,7],'degrees':[1,8],'columns_checked':checks,'result':'PASS'}
print(json.dumps(result,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
