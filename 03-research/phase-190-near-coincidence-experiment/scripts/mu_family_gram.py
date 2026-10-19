"""CA_C_007: family infimum in the correct (Gram) norm: min over span{c m^{-1/2} on m<=etaM, free above} of s'A s / s'G s."""
import sys, numpy as np, scipy.linalg as sl
from profile import Profile
from am import *
T0=float(sys.argv[1]); P=Profile(T0,1.0); etas=[float(e) for e in sys.argv[2].split(',')]; Ms=[int(t) for t in sys.argv[3].split(',')]
lat=sys.argv[4] if len(sys.argv)>4 else 'Z'
for M in Ms:
    if lat=='Z':
        ints=np.arange(1,M+1).astype(float); pos,w,_=lambda_comb(int(M*np.exp(2*T0))+2)
    else:
        X=M*np.exp(2*T0)+2; ps=primes_upto(int(X)+2).astype(float)
        if lat=='3.1': ps[ps==3]=3.1
        if lat=='jit': ps=ps*np.exp(np.random.default_rng(0).uniform(-0.02,0.02,len(ps)))
        ints=beurling_integers(ps,M); pos,w=[],[]
        for q in ps:
            qa=q
            while qa<=X: pos.append(np.log(qa)); w.append(2*np.log(q)/np.sqrt(qa)); qa*=q
        o=np.argsort(pos); pos=np.array(pos)[o]; w=np.array(w)[o]
    x=np.log(ints); n=len(ints); A=AM(P,x,pos,w).A; G=P.c0(np.abs(x[:,None]-x[None,:]))
    row=[]
    for eta in etas:
        k=np.searchsorted(ints,eta*M,side='right'); B=np.zeros((n,n-k+1)); B[:k,0]=ints[:k]**-0.5
        for j in range(k,n): B[j,j-k+1]=ints[j]**-0.5
        H=B.T@A@B; Gs=B.T@G@B; t=np.trace(Gs)/len(Gs)
        row.append([sl.eigh(H,Gs+r*t*np.eye(len(Gs)),eigvals_only=True)[0] for r in (1e-8,1e-11)])
    full=sl.eigh(A,G+1e-10*np.trace(G)/n*np.eye(n),eigvals_only=True)[0]
    print(f"{lat} T0={T0} M={M} n={n} full={full:.3e} "+' '.join(f"eta={e}:{r[0]:.3e}/{r[1]:.3e}" for e,r in zip(etas,row)),flush=True)
