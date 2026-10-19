import numpy as np,sys
from numpy.polynomial import legendre as L
from r183_030_inertia import build, Lam
from scipy.linalg import null_space,eigh
M=int(sys.argv[2]); Ts=[float(t) for t in sys.argv[1].split(",")]; K=[1,2,3,4,6,8]
def hvals(c,T,x):
    u=x/T; V=np.array([L.legval(u,np.eye(M)[j]) for j in range(M)]); dV=np.array([L.legval(u,L.legder(np.eye(M)[j])) for j in range(M)])
    b=(1-u**2)**2; db=-4*u*(1-u**2); return c@(0.5*V*b-(dV*b+V*db)/T)
def minvec(W,G,cp):
    Z=null_space(cp[None,:]); Wz=Z.T@W@Z; Gz=Z.T@G@Z
    d,U=np.linalg.eigh(Gz); k=d>1e-13*d.max(); Q=U[:,k]/np.sqrt(d[k])
    e,V=np.linalg.eigh(Q.T@Wz@Q); return e, Z@Q@V
for T in Ts:
    A,G,GH,cp,cl=build(T,M,None)
    ns=[n for n in range(2,2000) if np.log(n)<2*T and Lam(n)>0]
    Pn={}
    for n in ns:
        W1=build(T,M,[n])[0]; Pn[n]=W1-A
    W=A+sum(Pn.values(),np.zeros_like(A))
    e,V=minvec(W,GH,cp); h=V[:,0]
    ea,Va=minvec(A,GH,cp); ha=Va[:,0]
    x=np.linspace(-T,T,4001); hv=hvals(h,T,x); par=np.sum(hv*hv[::-1])/np.sum(hv*hv)
    s=np.linspace(0,40,801); F=np.abs(np.exp(1j*np.outer(s,x))@hv)**2; F/=F.sum()
    pk=s[np.argmax(F)]; mean=np.sum(s*F); bw=np.sqrt(np.sum((s-mean)**2*F))
    ov=abs(ha@GH@h)
    def costs(v):  # contribution of each n: v^T P_n v ; c(log n)= -sqrt(n)/(2Lam) * that
        return {n:v@Pn[n]@v for n in ns}
    cs=costs(h); csa=costs(ha)
    xa=hvals(ha,T,x); Fa=np.abs(np.exp(1j*np.outer(s,x))@xa)**2; pka=s[np.argmax(Fa)]
    WA=Va.T@W@Va; red=[np.linalg.eigvalsh(WA[:k,:k])[0] for k in K]
    ca={n:-csa[n]*np.sqrt(n)/(2*Lam(n)) for n in ns if Lam(n)>0 and n in (2,3,5,7)}
    print(f"  T={T:.3f} arch-mode peak={pka:.2f} c_ha(log p)="+" ".join(f"{n}:{ca[n]:+.3f}" for n in ca)+" | lmin on span(k arch modes) k="+str(K)+": "+" ".join(f"{r:+.2e}" for r in red),flush=True)
    MT=ha@A@ha+sum(csa.values())
    # also model with ha restricted by the arithmetic: Rayleigh of W on ha = MT
    print(f"T={T:.4f} M={M} lmin={e[0]:+.4e} l2={e[1]:+.3e} par={par:+.2f} pk={pk:.2f} pk*T={pk*T:.2f} bw={bw:.2f} Einf(h*)={h@A@h:+.4f} | "+
      " ".join(f"P{n}={cs[n]:+.4f}(c={-cs[n]*np.sqrt(n)/(2*Lam(n)):+.3f})" for n in ns[:8])+
      f" || arch: Einf(ha)={ea[0]:+.4e} <ha,h*>={ov:.4f} M(T)=W[ha]={MT:+.4e} primes(ha)={sum(csa.values()):+.4f}",flush=True)
