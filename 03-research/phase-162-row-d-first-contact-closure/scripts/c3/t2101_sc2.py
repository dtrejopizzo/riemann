import sys,numpy as np
from t2101_single_atom import *
K=int(sys.argv[1]); x=float(sys.argv[2]); ss=[float(v) for v in sys.argv[3:]]
for s in ss:
    T=Tstar(K,x,s); d=data(T,K,x,s); print(x,s,round(T,6),'%.2e'%d['mu2'],'%+.3e'%d['ov'],flush=True)
