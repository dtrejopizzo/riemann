import math,sys,numpy as np,core,os
import scipy.linalg as sla
# (a) mu table values
print("== mu(T) (codim-4), K=240 ==")
mus=[]
for T in np.arange(0.66,0.861,0.01):
    l,p,_=core.lam_min(T,240,codim=4); mus.append((T,l)); print(f"{T:.3f} {l: .6e} {p}")
import numpy as np
A=np.array(mus); 
for lo,hi in [(0.69,0.81),(0.69,0.86),(0.70,0.80)]:
    i=np.argmin(abs(A[:,0]-lo)); j=np.argmin(abs(A[:,0]-hi))
    print(f"mean c_mu[{lo},{hi}] = {-(math.log(A[j,1])-math.log(A[i,1]))/(A[j,0]-A[i,0]):.2f}")
print("== lambda(T) mean c over sub-ranges, K=240 ==")
lams=[]
for T in np.arange(0.40,0.6932,0.01):
    l,p,_=core.lam_min(T,240); lams.append((T,l))
B=np.array(lams)
for lo,hi in [(0.40,0.55),(0.56,0.6931),(0.60,0.6931),(0.40,0.6931)]:
    i=np.argmin(abs(B[:,0]-lo)); j=np.argmin(abs(B[:,0]-hi))
    print(f"mean c[{lo},{hi}] = {-(math.log(B[j,1])-math.log(B[i,1]))/(B[j,0]-B[i,0]):.2f}")
