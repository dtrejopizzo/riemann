"""Finite-mode lower bound for q+B on the three fixed regional tests.

The omitted reflected archimedean modes are nonnegative. This certifies
only the fixed three-dimensional subspace, not its complement or global sign.
"""
import argparse
import json
from pathlib import Path
from math import factorial
import mpmath as mm
from regional_upper import build, add, mul, integral, shift

parser = argparse.ArgumentParser()
parser.add_argument('--interval',action='store_true')
parser.add_argument('--modes',type=int,default=128)
args = parser.parse_args()
assert args.modes>0
folder = Path(__file__).parent
seed = json.loads((folder/'regional_seed.json').read_text())
ctx = mm.iv if args.interval else mm.mp
ctx.dps = 70
T = ctx.mpf(4)/5
zero,one = ctx.mpf(0),ctx.mpf(1)
_,basis = build(ctx,seed['degree'],interval=args.interval)
polys = []
for k in range(3):
    p = [zero]
    for n,b in enumerate(basis):
        p = add(p,[ctx.mpf(seed['coefficients'][n][k])/seed['denominator']*c for c in b])
    polys.append(p)
n = len(polys)
gram = [[T*integral(mul(p,q),zero,one) for q in polys] for p in polys]
C0 = -ctx.euler-ctx.pi/2-3*ctx.log(2)-ctx.log(ctx.pi)
A = [[C0*gram[i][j] for j in range(n)] for i in range(n)]
glue = [[zero for _ in range(n)] for _ in range(n)]
for number,prime in [(2,2),(3,3),(4,2)]:
    d = ctx.log(number)/T
    weight = ctx.log(prime)/ctx.sqrt(number)
    reflected = [[c*((-1)**k) for k,c in enumerate(shift(p,d))] for p in polys]
    difference = [add(p,[-c for c in r]) for p,r in zip(polys,reflected)]
    for i,p in enumerate(polys):
        for j,q in enumerate(polys):
            if number==2:
                cross = integral(mul(p,shift(q,-d)),d,one)
                cross += integral(mul(q,shift(p,-d)),d,one)
                A[i][j] -= weight*T*cross
                A[i][j] -= weight*T*integral(mul(p,q),zero,d)
                value = integral(mul(difference[i],difference[j]),zero,d)
            else:
                A[i][j] -= weight*gram[i][j]
                value = 2*integral(mul(p,q),zero,d-one)
                value += integral(mul(difference[i],difference[j]),d-one,one)
            glue[i][j] += weight*T*value/2
for i in range(n):
    for j in range(n): A[i][j] += glue[i][j]

for mode in range(args.modes):
    a = ctx.mpf(2*mode)+one/2
    beta = a*T
    exponential = ctx.exp(-beta)
    moments = [(1-exponential)/beta]
    for k in range(1,max(map(len,polys))):
        moments.append((k*moments[-1]-exponential)/beta)
    laplace = [sum(c*moments[k] for k,c in enumerate(p)) for p in polys]
    particular = []
    for p in polys:
        h = [zero]*len(p)
        for k,c in enumerate(p):
            for r in range(k+1):
                h[k-r] += c*((-1)**r)*factorial(k)/factorial(k-r)/beta**(r+1)
        particular.append(h)
    for i,p in enumerate(polys):
        for j,q in enumerate(polys):
            toeplitz = integral(mul(p,particular[j]),zero,one)
            toeplitz += integral(mul(q,particular[i]),zero,one)
            toeplitz -= particular[j][0]*laplace[i]+particular[i][0]*laplace[j]
            A[i][j] += 2*gram[i][j]/a-T*T*(toeplitz+laplace[i]*laplace[j])

def ldl(matrix):
    L = [[ctx.mpf(int(i==j)) for j in range(n)] for i in range(n)]
    pivots = []
    for k in range(n):
        d = matrix[k][k]-sum(L[k][i]**2*pivots[i] for i in range(k))
        pivots.append(d)
        if args.interval: assert d.a>0,(k,str(d))
        for j in range(k+1,n):
            L[j][k]=(matrix[j][k]-sum(L[j][i]*L[k][i]*pivots[i] for i in range(k)))/d
    return pivots

report = dict(mode='INTERVAL' if args.interval else 'EXPLORATORY',modes=args.modes,
              lower_matrix=[[str(x) for x in row] for row in A],
              lower_ldl=[str(x) for x in ldl(A)],
              glue_ldl=[str(x) for x in ldl(glue)])
if args.interval:
    report['status']='PASS'
    (folder/'regional_compensation_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
else:
    import numpy as np
    report['lower_eigenvalues']=np.linalg.eigvalsh(np.array(A,dtype=float)).tolist()
print(json.dumps(report,indent=2),flush=True)
