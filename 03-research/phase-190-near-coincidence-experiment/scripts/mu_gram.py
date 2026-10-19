"""CA_C_007: Rayleigh quotients of A_M against l2 norm and against the Gram norm ||F||^2 = s^T G s, G=[c0(log m/k)]."""
import sys, numpy as np, scipy.linalg as sl
from profile import Profile
from am import *
T0=float(sys.argv[1]); eta=float(sys.argv[2]); Ms=[int(t) for t in sys.argv[3].split(',')]
P=Profile(T0,1.0)
for M in Ms:
    m=np.arange(1,M+1); x=np.log(m); pos,w,_=lambda_comb(int(M*np.exp(2*T0))+2)
    A=AM(P,x,pos,w).A; D=x[:,None]-x[None,:]; G=P.c0(np.abs(D))
    ev=np.linalg.eigvalsh(G); 
    k=int(eta*M); B=np.zeros((M,M-k+1)); B[:k,0]=m[:k]**-0.5
    for j in range(k,M): B[j,j-k+1]=m[j]**-0.5
    # minimizer in l2 on family and its Gram norm
    vals,vecs=sl.eigh(B.T@A@B,B.T@B); s=B@vecs[:,0]
    print(f"M={M} G eig min/max {ev[0]:.2e}/{ev[-1]:.2e}; family l2-min mu={vals[0]:.3e}, its ||F||^2/||s||^2={s@G@s/(s@s):.3e}, Rayleigh vs ||F||^2 ={s@A@s/(s@G@s):.3e}; tail-only? mass on m<=etaM: {np.sum(s[:k]**2)/np.sum(s**2):.3e}",flush=True)
    # true Rayleigh on family span wrt Gram, with ridge
    Gs=B.T@G@B; r=1e-10*np.trace(Gs)/len(Gs)
    v2=sl.eigh(B.T@A@B,Gs+r*np.eye(len(Gs)),eigvals_only=True)[0]
    print(f"   family min of s'As/s'Gs (ridge {r:.1e}) = {v2:.3e}",flush=True)
