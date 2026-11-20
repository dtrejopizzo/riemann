"""quadrature check: rebuild Arch with doubled u-nodes and compare lambda_min (T=3.6, level 1)."""
import numpy as np, hp
from hp import *
T=3.6; B=Basis(mesh(T,0.5,0.3,0.3*np.exp(-2*T)),6)
wt={'v':lambda ns,v,T:v,'k1':lambda ns,v,T:v*np.cos(np.pi*np.log(ns)/(4*T))}
Z,A,S=build(T,B,wt)
A2=Z.T@build_arch_fast(B,T,qu=60)@Z; A2=(A2+A2.T)/2
print('max|dA|',abs(A-A2).max())
for k in S: print(k,np.linalg.eigvalsh(A-S[k])[0],np.linalg.eigvalsh(A2-S[k])[0])
