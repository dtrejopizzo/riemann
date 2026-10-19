"""Difference comb Lambda_Q - Lambda_K (K = Q(sqrt-5)), n<=200, exact; classification of n by factorisation."""
import os; os.environ['COMB'] = 'Q'
import cert_epstein as C
from sympy import factorint
import math
K = C._LK(500); Q = C.LQ
def v(d): return sum(float(q) * math.log(p) for p, q in d.items())
rows = []
for n in range(2, 201):
    dq, dk = v(Q.get(n, {})), v(K.get(n, {}))
    if abs(dq - dk) > 1e-12: rows.append((n, dict(factorint(n)), round(dq, 4), round(dk, 4), round(dq - dk, 4)))
for r in rows: print(*r)
