import sys; sys.path.insert(0,'.')
import numpy as np, scipy.linalg as sl
from profile import Profile
from am import *
T0=float(sys.argv[1]); eta=float(sys.argv[2])
P=Profile(T0,1.0)
for M in [int(t) for t in sys.argv[3].split(',')]:
    m=np.arange(1,M+1); x=np.log(m); pos,w,_=lambda_comb(int(M*np.exp(2*T0))+2)
    A=AM(P,x,pos,w).A
    k=int(eta*M); B=np.zeros((M,M-k+1)); B[:k,0]=m[:k]**-0.5
    for j in range(k,M): B[j,j-k+1]=m[j]**-0.5
    G=B.T@B; H=B.T@A@B
    mu=sl.eigh(H,G,eigvals_only=True)[0]; lam=np.linalg.eigvalsh(A)[0]
    print(f"T0={T0} eta={eta} M={M} mu={mu:.3e} lam_min={lam:.3e} flat Q/|s|^2={(B[:,0]+B[:,1:].sum(1))@A@(B[:,0]+B[:,1:].sum(1))/np.sum(m**-1.):.3e}",flush=True)
