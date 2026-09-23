import math, numpy as np, track1 as t, sys
import mpmath as mp
mp.mp.dps=15
gam={k:float(mp.zetazero(k).imag) for k in (1,2,5,10)}
print('ordinates',gam,flush=True)
print('--- Table 1: g0 = gamma_1, vary a ---',flush=True)
g0=gam[1]
for a in (0.0,0.05,0.1,0.2,0.3,0.45):
    row=[]
    for K in (120,200,300):
        T,_=t.tstar(a,g0,K=K,lo=0.05,hi=2.5,tol=5e-4,taumax=8000.)
        row.append('K=%d:%s'%(K,'%.4f'%T if T else 'none'))
    print('a=%.2f '%a+'  '.join(row),flush=True)
print('--- Table 2: a=0.30, vary g0 ---',flush=True)
for k in (1,2,5,10):
    g0=gam[k]; row=[]
    for K in (200,320):
        T,_=t.tstar(0.30,g0,K=K,lo=0.05,hi=3.0,tol=5e-4,taumax=max(8000.,60*g0))
        row.append('K=%d:%s'%(K,'%.4f'%T if T else 'none'))
    print('gamma_%d=%.4f  '%(k,g0)+'  '.join(row)+'   half-log(g0/2pi)=%.4f'%(0.5*math.log(g0/(2*math.pi))),flush=True)
