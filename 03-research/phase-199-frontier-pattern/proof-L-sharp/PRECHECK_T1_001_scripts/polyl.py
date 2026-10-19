# Closed forms on |z|=1, z=e^{iθ}, θ∈(0,2π): Li1, Li2, L1=Σ log n z^n/n, L2=Σ log n z^n/n^2, vectorised in double
import mpmath as mp, numpy as np
mp.mp.dps=50
KS=70
EG=float(mp.euler); G1=float(mp.stieltjes(1))
cz2=[float(mp.zeta(2-k)) if k!=1 else 0.0 for k in range(KS)]
dz1=[float(mp.zeta(1-k,derivative=1)) if k>=1 else 0.0 for k in range(KS)]
dz2=[float(mp.zeta(2-k,derivative=1)) if k!=1 else 0.0 for k in range(KS)]
eps=mp.mpf(10)**-20
with mp.workdps(80):
    F=lambda e: mp.gamma(-1-e)-1/e
    g0=float((F(eps)+F(-eps))/2); g1=float((F(eps)-F(-eps))/(2*eps))
fact=[float(mp.factorial(k)) for k in range(KS)]
def _ser(coef,w,k0):
    s=0; p=np.ones_like(w)
    out=np.zeros_like(w)
    for k in range(KS):
        if k>=k0: out=out+coef[k]*p/fact[k]
        p=p*(-w)
    return out
def funcs(theta):
    """theta array; returns Li1,Li2,L1,L2 at e^{iθ}"""
    th=np.mod(theta,2*np.pi); flip=th>np.pi; t=np.where(flip,2*np.pi-th,th)  # use conj symmetry
    w=-1j*t.astype(complex); lw=np.log(w)
    Li1=-np.log(1-np.exp(1j*t))
    Li2=cz2[0]+w*(lw-1)+_ser(cz2,w,2)
    L1=0.5*lw**2+EG*lw+EG**2/2+np.pi**2/12+G1-_ser(dz1,w,1)
    L2=-float(mp.zeta(2,derivative=1))-w*(0.5*lw**2+g0*lw+g1+G1)-_ser(dz2,w,2)
    res=[Li1,Li2,L1,L2]
    return [np.where(flip,np.conj(r),r) for r in res]
if __name__=='__main__':
    for th in [0.3,1.0,2.5,3.1,4.0,6.0]:
        z=mp.expj(th)
        ref=[mp.polylog(1,z),mp.polylog(2,z)]
        # L1,L2 via nsum with Abel-free: use mp.diff on lerch zeta / polylog in s
        ref.append(-mp.diff(lambda s: mp.polylog(s,z),1)); ref.append(-mp.diff(lambda s: mp.polylog(s,z),2))
        v=funcs(np.array([th]))
        print(th,[abs(complex(a)-b[0]) for a,b in zip(ref,v)])
