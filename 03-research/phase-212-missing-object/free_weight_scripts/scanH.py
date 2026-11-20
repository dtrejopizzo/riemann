"""separate interior resolution (H, p) from edge grading (hmin): usage scanH.py T p sigma c H1,H2,..."""
import sys, time, numpy as np
from hp import *
T=float(sys.argv[1]); p=int(sys.argv[2]); sig=float(sys.argv[3]); c=float(sys.argv[4])
wt={'v':lambda ns,v,T:v,'k1.0':lambda ns,v,T:v*np.cos(np.pi*np.log(ns)/(4*T))}
for H in [float(s) for s in sys.argv[5].split(',')]:
    t0=time.time(); B=Basis(mesh(T,H,sig,c*np.exp(-2*T)),p); Z,A,S=build(T,B,wt)
    print(f"T={T} H={H} p={p} c={c} N={B.N} "+" ".join(f"{k}:{np.linalg.eigvalsh(A-S[k])[0]:+.4e}" for k in S),f"{time.time()-t0:.0f}s",flush=True)
