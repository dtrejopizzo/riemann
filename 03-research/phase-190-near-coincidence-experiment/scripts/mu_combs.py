"""CA_C_007: family infimum on the integer lattice for modified combs (lattice = log m, m<=M fixed)."""
import sys, numpy as np, scipy.linalg as sl
from profile import Profile
from am import *
T0=float(sys.argv[1]); eta=float(sys.argv[2]); Ms=[int(t) for t in sys.argv[3].split(',')]
P=Profile(T0,1.0)
cases={'Lambda':{}, 'v3x2':{'perturb':(3,2.0)}, 'v3x0':{'perturb':(3,0.0)}, 'v5x0':{'perturb':(5,0.0)},
       'v2x1.01':{'perturb':(2,1.01)}, 'v2x0.99':{'perturb':(2,0.99)}, 'a3':{'delete_below':3}, 'v7x0':{'perturb':(7,0.0)}}
for name in sys.argv[4].split(','):
  for M in Ms:
    m=np.arange(1,M+1); x=np.log(m); pos,w,_=lambda_comb(int(M*np.exp(2*T0))+2,**cases[name])
    A=AM(P,x,pos,w).A; k=int(eta*M)
    B=np.zeros((M,M-k+1)); B[:k,0]=m[:k]**-0.5
    for j in range(k,M): B[j,j-k+1]=m[j]**-0.5
    mu=sl.eigh(B.T@A@B,B.T@B,eigvals_only=True)[0]; lam=np.linalg.eigvalsh(A)[0]
    print(f"{name:8s} M={M} mu={mu:.3e} lam_min={lam:.3e}",flush=True)
