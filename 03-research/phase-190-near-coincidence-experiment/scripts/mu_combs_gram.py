"""CA_C_007: family infimum (Gram norm) on the integer lattice for modified combs."""
import sys, numpy as np, scipy.linalg as sl
from profile import Profile
from am import *
T0=float(sys.argv[1]); P=Profile(T0,1.0); etas=[float(e) for e in sys.argv[2].split(',')]; Ms=[int(t) for t in sys.argv[3].split(',')]
cases={'Lambda':{}, 'v2x1.1':{'perturb':(2,1.1)}, 'v2x0.9':{'perturb':(2,0.9)}, 'v2x0':{'perturb':(2,0.0)}, 'v2x3':{'perturb':(2,3.0)},
       'v3x2':{'perturb':(3,2.0)}, 'v3x0':{'perturb':(3,0.0)}, 'v5x0':{'perturb':(5,0.0)}, 'v5x3':{'perturb':(5,3.0)}, 'v4x0':{'perturb':(4,0.0)}}
for name in sys.argv[4].split(','):
  for M in Ms:
    m=np.arange(1,M+1).astype(float); x=np.log(m); pos,w,_=lambda_comb(int(M*np.exp(2*T0))+2,**cases[name])
    A=AM(P,x,pos,w).A; G=P.c0(np.abs(x[:,None]-x[None,:])); row=[]
    for eta in etas:
        k=int(eta*M); B=np.zeros((M,M-k+1)); B[:k,0]=m[:k]**-0.5
        for j in range(k,M): B[j,j-k+1]=m[j]**-0.5
        Gs=B.T@G@B; row.append(sl.eigh(B.T@A@B,Gs+1e-10*np.trace(Gs)/len(Gs)*np.eye(len(Gs)),eigvals_only=True)[0])
    full=sl.eigh(A,G+1e-10*np.trace(G)/M*np.eye(M),eigvals_only=True)[0]
    print(f"{name:7s} M={M} full={full:.3e} "+' '.join(f"eta={e}:{r:.3e}" for e,r in zip(etas,row)),flush=True)
