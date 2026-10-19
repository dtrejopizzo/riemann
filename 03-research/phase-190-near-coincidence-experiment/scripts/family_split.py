"""CA_C_007: split of the eta-family into bulk vector u=m^{-1/2}1_{m<=etaM} and tail block; Gram-normalized values. Lattices Z, 3.1, jit."""
import sys, numpy as np, scipy.linalg as sl
from profile import Profile
from am import *
T0=0.3; P=Profile(T0,1.0); eta=float(sys.argv[1]) if __name__=='__main__' else 0.9
def system(lat,M):
    X=M*np.exp(2*T0)+2; ps=primes_upto(int(X)+2).astype(float)
    if lat=='3.1': ps[ps==3]=3.1
    if lat=='jit': ps=ps*np.exp(np.random.default_rng(0).uniform(-0.02,0.02,len(ps)))
    ints=np.arange(1,M+1).astype(float) if lat=='Z' else beurling_integers(ps,M)
    pos,w=[],[]
    for q in ps:
        qa=q
        while qa<=X: pos.append(np.log(qa)); w.append(2*np.log(q)/np.sqrt(qa)); qa*=q
    o=np.argsort(pos); return ints,np.array(pos)[o],np.array(w)[o]
if __name__=="__main__":
  for lat in ['Z','3.1','jit']:
   for M in [200,400,800]:
     ints,pos,w=system(lat,M); x=np.log(ints); n=len(ints); A=AM(P,x,pos,w).A; G=P.c0(np.abs(x[:,None]-x[None,:]))
     k=np.searchsorted(ints,eta*M,side='right'); u=np.zeros(n); u[:k]=ints[:k]**-0.5
     At,Gt=A[k:,k:],G[k:,k:]; tail=sl.eigh(At,Gt+1e-10*np.trace(Gt)/len(Gt)*np.eye(len(Gt)),eigvals_only=True)[0]
     print(f"{lat:4s} M={M} bulk Q(u)/|F_u|^2={u@A@u/(u@G@u):.3e} (Q(u)={u@A@u:.3f}) tail-only min={tail:.3e}",flush=True)
