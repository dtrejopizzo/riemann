# robustness of the Type I root in s2 under the frequency cutoff tmax and Gauss panel order. UNCERTIFIED.
import sys, numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
import t1601_nodal_rerun as B, t2001_typeI_search as M
s3=float(sys.argv[1]); tmax=float(sys.argv[2]); ng=int(sys.argv[3]); K=34
x,w=leggauss(ng); lo=np.arange(0,tmax,0.5); B._X=((lo[:,None]+0.25*(x+1)).ravel(),np.tile(0.25*w,len(lo)))
orig=M.pieces; M.pieces=lambda T,K,tmax_=tmax: orig(T,K,tmax_)
def Tstar(s2,T0):
    f=lambda T: M.data(T,K,s2,s3)['lam']; return brentq(f,T0-0.004,T0+0.004,xtol=1e-13)
T0=float(sys.argv[4])
h=lambda s2: M.data(Tstar(s2,T0),K,s2,s3)['ov']
sc=brentq(h,0.9990,1.0,xtol=1e-12); print(f"| {s3} | {tmax} | {ng} | {sc:.8f} | {Tstar(sc,T0):.8f} |",flush=True)
