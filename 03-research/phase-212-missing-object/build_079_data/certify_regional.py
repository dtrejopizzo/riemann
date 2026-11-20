"""Interval certificate for a three-dimensional negative subspace of q_T.

This proves no positivity statement for a_T. No eigenvalues or quadrature
are used in the certificate; rational seeds are fixed in regional_seed.json.
"""
import json
from pathlib import Path
import mpmath as mm
from regional_upper import build

folder = Path(__file__).parent
seed = json.loads((folder/'regional_seed.json').read_text())
mm.iv.dps = 70
ctx = mm.iv
M, _ = build(ctx,seed['degree'],interval=True)
integers = seed['coefficients']
U = [[ctx.mpf(c)/seed['denominator'] for c in row] for row in integers]
n = seed['columns']
degree = seed['degree']
upper = [[sum(U[i][a]*M[i][j]*U[j][b] for i in range(degree) for j in range(degree))
          for b in range(n)] for a in range(n)]
L = [[ctx.mpf(int(i==j)) for j in range(n)] for i in range(n)]
pivots = []
for k in range(n):
    pivot = -upper[k][k]-sum(L[k][i]**2*pivots[i] for i in range(k))
    assert pivot.a>0, (k,pivot)
    pivots.append(pivot)
    for j in range(k+1,n):
        L[j][k] = (-upper[j][k]-sum(L[j][i]*L[k][i]*pivots[i] for i in range(k)))/pivot

a,b,c = integers[:3]
minor = (a[0]*(b[1]*c[2]-b[2]*c[1])
         -a[1]*(b[0]*c[2]-b[2]*c[0])
         +a[2]*(b[0]*c[1]-b[1]*c[0]))
assert minor != 0
dominance = [-upper[i][i]-sum(abs(upper[i][j]) for j in range(n) if j!=i)
             for i in range(n)]
assert all(value.a > (ctx.mpf(1)/600).b for value in dominance)
report = dict(status='PASS',scope='three-dimensional negative subspace of regional q_T only',
              T='4/5',interval_dps=ctx.dps,integer_minor=minor,
              negative_upper_ldl_pivots=[str(p) for p in pivots],
              gershgorin_lower_bounds=[str(value.a) for value in dominance],
              coefficient_coercivity='1/600',
              upper_matrix=[[str(v) for v in row] for row in upper])
(folder/'regional_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
