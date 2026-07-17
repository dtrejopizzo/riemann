"""
E68.2 -- does an interior, symmetric-window local symbol pass the GLT distribution law?

E68.1's naive per-row symbol failed for zeta (measure{kappa<0}=0.45 but ind_-=0), likely from edge
rows using few/asymmetric bands. GLT symbols are bulk objects. Here:
  - restrict to interior positions j in [w, N-1-w];
  - use a SYMMETRIC band window d in [-w, w] with a smooth (Hann) taper;
  - kappa(x_j, theta) = sum_{d=-w}^{w} taper(d) M[j,j+d] e^{i d theta}.
If zeta then gives measure{kappa<0} ~ 0 (matching ind_-=0), the GLT reading survives and just needed a
proper bulk extraction. If it still shows a sizeable negative region for zeta, the object is NOT
cleanly GLT and E67.20's optimism was premature.
"""
import os, sys
import numpy as np
import mpmath as mp

H8 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, H8)
import h8lab as H
mp.mp.dps = 40

def mp2np(M):
    return np.array([[complex(M[i,j]) for j in range(M.cols)] for i in range(M.rows)], dtype=complex)

def planted(z0, rho):
    s0=mp.mpf(1)/2+mp.mpc(0,1)*z0; r,rc=rho,1-rho
    def g(j,s): return {0:(s-r)*(s-rc),1:(s-r)+(s-rc),2:mp.mpf(2)}.get(j,mp.mpf(0))
    return lambda k: sum(mp.binomial(k,j)*mp.zeta(s0,1,j)*g(k-j,s0) for j in range(k+1))

def interior_symbol(M, w, ntheta=128):
    N=M.shape[0]; th=np.linspace(-np.pi,np.pi,ntheta,endpoint=False)
    taper=np.array([0.5*(1+np.cos(np.pi*d/(w+1))) for d in range(-w,w+1)])  # Hann
    rows=range(w, N-w)
    K=[]
    for j in rows:
        s=np.zeros(ntheta,dtype=complex)
        for idx,d in enumerate(range(-w,w+1)):
            s+=taper[idx]*M[j,j+d]*np.exp(1j*d*th)
        K.append(np.real(s))
    return np.array(K)  # (interior rows) x ntheta

def analyze(z0,N,w,Xi_deriv,tag):
    A_N,Plam,J=H.arithmetic_jets(z0,N,Xi_deriv)
    A=mp2np(H.herm(A_N)); P=mp2np(H.herm(Plam))
    KA=interior_symbol(A,w); KP=interior_symbol(P,w); K=KA-KP
    Jn=mp2np(H.herm(J)); Jn=0.5*(Jn+Jn.conj().T)
    eig=np.linalg.eigvalsh(Jn)
    print(f"  [{tag}]  min kappa={K.min():+.4f}  measure{{kappa<0}}={np.mean(K<-1e-6):.3f}"
          f"   ind_-/N={np.mean(eig<-1e-9):.3f}")

def main():
    t0,y,N=100.0,1.0,24
    z0=mp.mpc(mp.mpf(str(t0)),-mp.mpf(str(y)))
    print(f"z0={t0}-{y}i  N={N}\n")
    for w in (4,6,8):
        print(f"window w={w} (interior rows {w}..{N-1-w}, symmetric Hann taper):")
        analyze(z0,N,w,None,"zeta")
        analyze(z0,N,w,planted(z0,mp.mpf('0.8')+mp.mpc(0,1)*mp.mpf(str(t0))),"offline b=0.8")
        print()
    print("Verdict: if zeta measure{kappa<0} -> ~0 as w grows, GLT survives; else object not cleanly GLT.")

if __name__ == "__main__":
    main()
