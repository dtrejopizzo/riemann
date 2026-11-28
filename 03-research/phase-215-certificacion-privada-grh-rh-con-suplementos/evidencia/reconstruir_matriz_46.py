"""Independent Arb quadrature reconstruction; NOT itself an inertia certificate.

Computes ball matrices with the manuscript's conservative quadrature remainder.
The analytic remainder and subsequent inertia must be checked separately.
Run with python3; writes JSON next to this file. No source paper is modified.
"""
import json
import time
from pathlib import Path
from flint import arb, acb, arb_mat, ctx

ctx.prec = 640
OUT = Path(__file__).resolve().parent
T = arb(5).log()/2
A = 2*arb(2).log()/arb(2).sqrt()+2*arb(3).log()/arb(3).sqrt()+arb(2).log()
def m(t):
    return acb(arb(1)/4,t/2).digamma().real-arb.pi().log()
si = m(arb(240))-A
nodes = [arb.legendre_p_root(46,k,weight=True) for k in range(46)]
scales = [(arb(2*n+1)).sqrt()*(-1)**(n//2) for n in range(330)]
G = [arb_mat(165,140),arb_mat(165,140)]
start = time.monotonic()
resets = 0
for panel in range(480):
    columns = [[],[]]
    weighted = [[],[]]
    for node,weight in nodes:
        tau = arb(panel)/2+(node+1)/4
        x = T*tau
        vals = [x.sin()/x,(x.sin()/x-x.cos())/x]
        for n in range(1,329):
            y = (2*n+1)/x*vals[-1]-vals[-2]
            if not y.rad() < arb('1e-75'):
                factor = (arb.pi()/(2*x)).sqrt()
                vals[-1] = factor*x.bessel_j(arb(n)+arb('0.5'))
                y = factor*x.bessel_j(arb(n)+arb('1.5'))
                resets += 1
            vals.append(y)
        assert all(v.rad() < arb('1e-60') for v in vals)
        g = si-m(tau)
        for n,lam in [(2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())]:
            g += 2*lam/arb(n).sqrt()*(tau*arb(n).log()).cos()
        w = g*weight/4*2*T/arb.pi()
        for parity in range(2):
            col = [vals[n]*scales[n] for n in range(parity,330,2)]
            columns[parity].append(col)
            weighted[parity].append([v*w for v in col[:140]])
    for parity in range(2):
        G[parity] += arb_mat(columns[parity]).transpose()*arb_mat(weighted[parity])
    if panel % 20 == 0:
        print(f'panel={panel}/480 elapsed={time.monotonic()-start:.1f}s',flush=True)

def encode(v):
    return v.str(210)
data = dict(precision=640,panels=480,nodes=46,bessel_resets=resets,
            remainder_status='Assumed 2e-42 per matrix entry; analytic proof audited separately',
            T=encode(T),A=encode(A),s_infty=encode(si),elapsed=time.monotonic()-start,
            matrices=[[[encode(M[i,j]+arb(0,'2e-42')) for j in range(140)]
                       for i in range(165)] for M in G])
(OUT/'matrices_46_arb.json').write_text(json.dumps(data,indent=2))
print('Matrices saved; inertia NOT YET VERIFIED.',flush=True)
