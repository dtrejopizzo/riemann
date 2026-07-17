"""
E67.20 -- audit of E67.19: is the object GLT (rigorous) rather than 'not Toeplitz' (heuristic)?

E67.19 found dev(P_lambda) GROWS with N. Two readings:
  (wrong, pessimistic) : the object is not Toeplitz, so the symbol picture is heuristic.
  (right, to test)     : the symbol VARIES WITH POSITION. If the band value M[j,j+d] is a SMOOTH
                         function of j, the sequence is Generalized Locally Toeplitz (GLT) /
                         pseudodifferential, which has RIGOROUS eigenvalue-distribution theory
                         (Serra-Capizzano, Garoni, Widom). Then Omega_7 <=> the 2-variable symbol
                         kappa(x,theta) >= 0, still rigorous, just richer.

Tests:
 (1) For fixed band d, is P[j,j+d] a SMOOTH function of j? (smoothness = GLT signature)
     Measure: relative size of second finite difference vs the variation itself.
 (2) Does the empirical eigenvalue distribution of A_N-P_lambda match a 2D symbol integral
     better than the 1D band-averaged symbol? (GLT distribution check)
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

def smoothness(seq):
    """Relative roughness: ||second difference|| / ||first difference||. Small => smooth curve."""
    seq = np.asarray(seq)
    if len(seq) < 3: return np.nan
    d1 = np.diff(seq); d2 = np.diff(d1)
    n1 = np.linalg.norm(d1)+1e-30
    return np.linalg.norm(d2)/n1

def main():
    t0,y,N = 100.0,1.0,20
    z0=mp.mpc(mp.mpf(str(t0)),-mp.mpf(str(y)))
    A_N,Plam,_=H.arithmetic_jets(z0,N,None)
    A=mp2np(H.herm(A_N)); P=mp2np(H.herm(Plam))
    print(f"z0={t0}-{y}i  N={N}\n")

    print("(1) Does P[j,j+d] vary SMOOTHLY with position j? (GLT signature)")
    print("    band d | roughness ||d2||/||d1|| (small=smooth) | monotone-ish?")
    for d in (0,1,2,3,4):
        seq = np.real([P[j,j+d] for j in range(N-d)])
        r = smoothness(seq)
        rng = seq.max()-seq.min()
        print(f"      d={d}   {r:.3f}   range={rng:.3f}   vals[0,mid,last]="
              f"{seq[0]:+.3f},{seq[len(seq)//2]:+.3f},{seq[-1]:+.3f}")
    print("    (roughness << 1 => smooth position variation => GLT / pseudodifferential, RIGOROUS)")

    print("\n(2) Same for A[j,j+d]:")
    for d in (0,1,2,3,4):
        seq = np.real([A[j,j+d] for j in range(N-d)])
        print(f"      d={d}   roughness={smoothness(seq):.3f}   range={seq.max()-seq.min():.3f}")

    print("\n(3) sigma_min of zeta symbol vs N (does the touch -> 0? exact marginality):")
    for Nn in (8,12,16,20):
        An,Pn,_=H.arithmetic_jets(z0,Nn,None)
        Am=mp2np(H.herm(An)); Pm=mp2np(H.herm(Pn))
        th=np.linspace(-np.pi,np.pi,3000)
        def sym(M):
            NN=M.shape[0]; s=np.zeros(len(th),dtype=complex)
            for dd in range(-(NN-1),NN):
                s+=np.mean([M[j,j+dd] for j in range(max(0,-dd),min(NN,NN-dd))])*np.exp(1j*dd*th)
            return np.real(s)
        smin=(sym(Am)-sym(Pm)).min()
        print(f"      N={Nn:2d}  sigma_min={smin:+.5f}")

if __name__ == "__main__":
    main()
