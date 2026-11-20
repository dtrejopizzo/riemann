import numpy as np, math, mpmath as mp
from prolate_defect import prolate, evalP
def omc(k,c,dps,nodes=20):
    with mp.workdps(dps):
        c=mp.mpf(c); X_,W_=np.polynomial.laguerre.laggauss(nodes); tot=mp.mpf(0)
        for x,w in zip(X_,W_):
            s=c+mp.mpf(x)/2; ks,Dd=prolate(s,dps=dps,parity=k%2,nfun=k//2+1)
            p1=evalP(ks,Dd[k//2],mp.mpf(1)); tot+=mp.mpf(w)*mp.exp(mp.mpf(x))*(2*p1**2/s)/2
        return -mp.expm1(-tot)
