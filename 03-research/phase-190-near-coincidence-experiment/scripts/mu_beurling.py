"""CA_C_007: family infimum mu_M(eta) and lambda_min for Z and for Beurling systems with the same construction."""
import sys, numpy as np, scipy.linalg as sl
from profile import Profile
from am import *
T0=float(sys.argv[1]); eta=float(sys.argv[2]); Ms=[int(t) for t in sys.argv[3].split(',')]
P=Profile(T0,1.0)
def gens(name,X):
    ps=primes_upto(int(X)+2).astype(float)
    if name=='Z': return ps
    if name=='sqrt5': return np.concatenate([[np.sqrt(5)],ps[ps>=3]])
    if name=='3.1': q=ps.copy(); q[q==3]=3.1; return q
    if name=='jit': rng=np.random.default_rng(0); return ps*np.exp(rng.uniform(-0.02,0.02,len(ps)))
def comb(qs,X):
    pos,w=[],[]
    for q in qs:
        qa=q
        while qa<=X: pos.append(np.log(qa)); w.append(2*np.log(q)/np.sqrt(qa)); qa*=q
    pos,w=np.array(pos),np.array(w); o=np.argsort(pos); return pos[o],w[o]
for name in sys.argv[4].split(','):
  for M in Ms:
    X=M*np.exp(2*T0)+2; qs=gens(name,X)
    ints=beurling_integers(qs,M); x=np.log(ints); pos,w=comb(qs,X)
    A=AM(P,x,pos,w).A; n=len(ints); k=np.searchsorted(ints,eta*M,side='right')
    B=np.zeros((n,n-k+1)); B[:k,0]=ints[:k]**-0.5
    for j in range(k,n): B[j,j-k+1]=ints[j]**-0.5
    mu=sl.eigh(B.T@A@B,B.T@B,eigvals_only=True)[0]; lam=np.linalg.eigvalsh(A)[0]
    print(f"{name:6s} T0={T0} eta={eta} M={M} n={n} mu={mu:.3e} lam_min={lam:.3e}",flush=True)
