import math, core
T=math.log(2); w2,w3=core.wgt(2),core.wgt(3)
print("quadrature sensitivity at K=320 (lmin of A_log2, and x0min):")
for tm,np_,ng in [(4000,400,24),(8000,400,24),(4000,600,24),(4000,400,32),(20000,600,32)]:
    B=core.Body(T,320,taumax=tm,npan=np_,ng=ng)
    print(f"  taumax={tm} npan={np_} ng={ng}: lmin={B.lmin(1.,{2:-2*w2,3:-2*w3}):.10e}  x0min={B.lmin(1.,{}):.10f}")
# Richardson in K on lmin and on band upper edge
import numpy as np
from scipy.optimize import brentq
ks=[]; ls=[]; ups=[]
for K in (160,240,320,480,640):
    B=core.Body(T,K)
    l=B.lmin(1.,{2:-2*w2,3:-2*w3})
    f=lambda v: B.lmin(1.,{2:-2*w2,3:-2*v})
    up=brentq(f,w3,w3+2e-5,xtol=1e-14)
    ks.append(K); ls.append(l); ups.append(up)
    print(f"K={K}: lmin={l:.8e} upper edge={up:.12f} margin={up-w3:.6e}")
# fit l = a + b/K
A=np.vstack([np.ones(len(ks)),1/np.array(ks,float)]).T
print("extrap lmin (a+b/K):",np.linalg.lstsq(A,np.array(ls),rcond=None)[0])
print("extrap upper edge   :",np.linalg.lstsq(A,np.array(ups),rcond=None)[0])
