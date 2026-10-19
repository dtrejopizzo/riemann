import sys,numpy as np
from t2101_single_atom import *
K=int(sys.argv[1]); x=float(sys.argv[2])
ss=[0.3,0.5,0.7,0.8,0.9,0.95,1.0,1.05,1.1,1.2,1.4,1.7,2.0,2.5,3.0]
prev=None
for s in ss:
    T=Tstar(K,x,s)
    if T is None: print(x,s,None,flush=True); prev=None; continue
    d=data(T,K,x,s); print(x,s,round(T,6),'%.2e'%d['mu2'],'%+.3e'%d['ov'],flush=True)
    if prev and np.sign(prev[1])!=np.sign(d['ov']):
        h=lambda u: data(Tstar(K,x,u),K,x,u)['ov']
        try:
            sc=brentq(h,prev[0],s,xtol=1e-10); print('  SC',x,sc,Tstar(K,x,sc),flush=True)
        except Exception as e: print('  fail',e)
    prev=(s,d['ov'])
