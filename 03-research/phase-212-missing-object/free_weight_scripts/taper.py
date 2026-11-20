"""lambda_min of the tapered form: weights v_n*cos(k*pi*log n/(4T)).  usage: taper.py T1,T2,... N1,N2,... k1,k2,..."""
import sys, numpy as np
from forms import *
Ts=[float(x) for x in sys.argv[1].split(',')]; Ns=[int(x) for x in sys.argv[2].split(',')]; ks=[float(x) for x in sys.argv[3].split(',')]
for T in Ts:
  for N in Ns:
    M0,Cn,ns,v=build(T,N,nu=max(240,6*N))
    x=np.log(ns)/(2*T)
    print(f"T={T} N={N}  "+"  ".join(f"k{k}:{lam(M0,Cn,v*np.cos(k*np.pi*x/2))[0]:+.6e}" for k in ks),flush=True)
