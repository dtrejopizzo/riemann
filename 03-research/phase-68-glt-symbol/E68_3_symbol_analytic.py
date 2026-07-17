"""
E68.3 -- audit the 1D symbol as the correct spectral object, and identify it analytically.

Audit (reconcile E67.18 vs E68.1-2):
  - 1D position-AVERAGED symbol sigma(theta) = sum_d (mean_j M[j,j+d]) e^{i d theta} satisfies the
    Szego distribution law (E67.18):  measure{sigma<0} = ind_-/N.  <-- re-verify cleanly.
  - 2D local symbol does NOT (E68.1-2).  So the 1D averaged symbol is the correct spectral object.

Step 2 (analytic form): extract sigma_A, sigma_P and test whether sigma_P(theta) traces
-zeta'/zeta along the critical line, i.e. the symbol variable theta maps to height t near t0.
If so, Omega_7 <=> sigma_A - sigma_P >= 0 is an explicit inequality on -Xi'/Xi along the line.
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

def avg_symbol(M, th):
    N=M.shape[0]; s=np.zeros(len(th),dtype=complex)
    for d in range(-(N-1),N):
        s+=np.mean([M[j,j+d] for j in range(max(0,-d),min(N,N-d))])*np.exp(1j*d*th)
    return np.real(s)

def main():
    t0,y,N=100.0,1.0,16
    z0=mp.mpc(mp.mpf(str(t0)),-mp.mpf(str(y)))
    th=np.linspace(-np.pi,np.pi,2000)
    print(f"z0={t0}-{y}i  N={N}\n")

    print("(AUDIT) 1D averaged symbol: measure{sigma<0} vs ind_-/N")
    for tag,xd in [("zeta",None),("offline b=0.8",planted(z0,mp.mpf('0.8')+mp.mpc(0,1)*mp.mpf(str(t0))))]:
        A_N,Plam,J=H.arithmetic_jets(z0,N,xd)
        A=mp2np(H.herm(A_N)); P=mp2np(H.herm(Plam))
        sig=avg_symbol(A,th)-avg_symbol(P,th)
        Jn=mp2np(H.herm(J)); Jn=0.5*(Jn+Jn.conj().T); eig=np.linalg.eigvalsh(Jn)
        print(f"   [{tag}] measure{{sigma<0}}={np.mean(sig<-1e-9):.3f}  ind_-/N={np.mean(eig<-1e-9):.3f}"
              f"  min sigma={sig.min():+.4f}  (match => 1D symbol is the spectral object)")

    print("\n(STEP 2) analytic identification of the prime symbol sigma_P(theta):")
    A_N,Plam,_=H.arithmetic_jets(z0,N,None)
    P=mp2np(H.herm(Plam))
    sP=avg_symbol(P,th)
    # candidate: -zeta'/zeta along the critical line 1/2 + i*t, t = t0 + a*theta (linear height map)
    # fit the height-scale a by matching the shape; here compare qualitative range/structure.
    print(f"   sigma_P range: [{sP.min():.3f}, {sP.max():.3f}]")
    # sample -zeta'/zeta on the line near t0 and compare magnitude scales
    for a in (1.0, 2.0, 5.0):
        ts = t0 + a*th
        vals = []
        for t in ts[::200]:
            s = mp.mpf(1)/2 + mp.mpc(0,1)*mp.mpf(str(float(t)))
            zz = complex(-mp.zeta(s,1,1)/mp.zeta(s))   # -zeta'/zeta(s)
            vals.append(zz.real)
        vals=np.array(vals)
        # crude correlation with sigma_P subsampled
        sp_sub = sP[::200][:len(vals)]
        c = np.corrcoef(sp_sub, vals[:len(sp_sub)])[0,1] if len(sp_sub)>2 else np.nan
        print(f"   height map t=t0+{a}*theta:  Re(-zeta'/zeta) range [{vals.min():.3f},{vals.max():.3f}]"
              f"  corr(sigma_P, Re) = {c:+.3f}")

if __name__ == "__main__":
    main()
