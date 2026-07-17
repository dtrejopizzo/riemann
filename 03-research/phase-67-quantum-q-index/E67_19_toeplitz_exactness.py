"""
E67.19 -- is the Toeplitz structure asymptotically exact, and what is the touch point?

Foundational check for the symbol picture (E67.16-18). Two questions:

(A) Does toeplitz_dev(A_N), toeplitz_dev(P_lambda) DECREASE as N grows? If yes, the jets are
    asymptotically Toeplitz, so "sigma_A >= sigma_P <=> RH" is rigorous in the limit, not a
    band-averaging artifact. If it plateaus, the detector is heuristic.

(B) For zeta, locate the touch point theta* = argmin sigma(theta) and fit the LOCAL behavior
    sigma(theta) ~ sigma_min + c (theta - theta*)^2. A clean quadratic touch is a Fisher-Hartwig
    'zero-type' singularity of order 1; that fixes which FH asymptotics govern the marginal case.
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

def toeplitz_dev(M):
    N=M.shape[0]; devs=[]; scale=np.mean(np.abs(M))+1e-30
    for d in range(-(N-1),N):
        vals=[M[j,j+d] for j in range(max(0,-d),min(N,N-d))]
        if len(vals)>1: devs.append(np.std(vals))
    return np.mean(devs)/scale

def symbol(M, th):
    N=M.shape[0]; s=np.zeros(len(th),dtype=complex)
    for d in range(-(N-1),N):
        s += np.mean([M[j,j+d] for j in range(max(0,-d),min(N,N-d))])*np.exp(1j*d*th)
    return np.real(s)

def main():
    t0,y=100.0,1.0
    z0=mp.mpc(mp.mpf(str(t0)),-mp.mpf(str(y)))
    print(f"z0={t0}-{y}i\n")
    print("(A) Toeplitz deviation vs N (want decreasing -> asymptotically Toeplitz):")
    print("   N     dev(A_N)   dev(P_lambda)")
    for N in (6,8,10,12,14,16):
        A_N,Plam,_=H.arithmetic_jets(z0,N,None)
        A=mp2np(H.herm(A_N)); P=mp2np(H.herm(Plam))
        print(f"  {N:3d}    {toeplitz_dev(A):.4f}     {toeplitz_dev(P):.4f}")

    print("\n(B) zeta symbol touch point (sigma = sigma_A - sigma_P):")
    N=16
    A_N,Plam,_=H.arithmetic_jets(z0,N,None)
    A=mp2np(H.herm(A_N)); P=mp2np(H.herm(Plam))
    th=np.linspace(-np.pi,np.pi,4000)
    sig=symbol(A,th)-symbol(P,th)
    i0=int(np.argmin(sig)); th0=th[i0]; smin=sig[i0]
    print(f"   theta* = {th0:+.4f}   sigma_min = {smin:+.5f}")
    # local quadratic fit around the minimum
    win=(np.abs(th-th0)<0.25)
    c=np.polyfit(th[win]-th0, sig[win], 2)
    print(f"   local fit sigma ~ {c[0]:.3f}(theta-theta*)^2 + {c[1]:+.3f}(theta-theta*) + {c[2]:+.4f}")
    print(f"   curvature (2a) = {2*c[0]:.3f}  -> {'clean quadratic touch (FH zero order 1)' if c[0]>0 and abs(c[1])<0.5 else 'check'}")
    print(f"   min over circle stays >= 0: {smin>=-1e-6}")

if __name__ == "__main__":
    main()
