"""
E67.16 -- classical structure of A_N, P_lambda, D_N: Hankel? Toeplitz? recurrence?

If A_N / P_lambda are Hankel (entries depend on j+k) they are MOMENT matrices of a measure
-> orthogonal polynomials -> three-term recurrence -> Jacobi-matrix resolvent (closed form,
Christoffel-Darboux).
If Toeplitz (entries depend on j-k) they have a SYMBOL -> Szego / Borodin-Okounkov closed
forms for determinants and resolvent traces.
Either would give R_N(z;q)=Tr(G_q(z-D_N)^{-1}) a structural closed form, turning the Quantum
Forcing statement from a restatement of Omega_7 into a real reduction.

We measure, for each matrix M, the relative deviation from perfect Hankel and Toeplitz:
  hankel_dev = std over anti-diagonals / overall scale
  toeplitz_dev = std over diagonals / overall scale
and print a few entries to see the pattern. No zeros are used except through the harness.
"""
import os, sys
import numpy as np
import mpmath as mp

H8 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, H8)
import h8lab as H
mp.mp.dps = 40

def mp2np(Mx):
    return np.array([[complex(Mx[i,j]) for j in range(Mx.cols)] for i in range(Mx.rows)], dtype=complex)

def hankel_dev(M):
    N = M.shape[0]; devs = []; scale = np.mean(np.abs(M))+1e-30
    for s in range(0, 2*N-1):
        vals = [M[j, s-j] for j in range(max(0,s-N+1), min(s, N-1)+1)]
        if len(vals) > 1: devs.append(np.std(vals))
    return np.mean(devs)/scale

def toeplitz_dev(M):
    N = M.shape[0]; devs = []; scale = np.mean(np.abs(M))+1e-30
    for d in range(-(N-1), N):
        vals = [M[j, j+d] for j in range(max(0,-d), min(N, N-d))]
        if len(vals) > 1: devs.append(np.std(vals))
    return np.mean(devs)/scale

def report(name, M):
    Mn = M / (np.abs(M[0,0])+1e-30)
    print(f"  {name:20s}  hankel_dev={hankel_dev(M):.3f}   toeplitz_dev={toeplitz_dev(M):.3f}")
    return Mn

def main():
    t0, y, N = 100.0, 1.0, 10
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    A_N, Plam, J = H.arithmetic_jets(z0, N, None)
    A = mp2np(H.herm(A_N)); P = mp2np(H.herm(Plam)); Jf = mp2np(H.herm(J))
    W = mp2np(H.inv_sqrt(H.herm(A_N)))
    D = W @ Jf @ W

    print(f"z0={t0}-{y}i  N={N}   (dev=0 means perfect structure)\n")
    print("Raw jets:")
    report("A_N (arch)", A)
    report("P_lambda (prime)", P)
    report("J=A_N-P_lambda", Jf)
    print("\nWhitened:")
    report("D_N (whitened defect)", D)

    print("\nAbsolute-value magnitude of P_lambda entries |P[j,k]| (look for j-k pattern):")
    Pabs = np.abs(P)
    for j in range(min(6,N)):
        print("   " + " ".join(f"{Pabs[j,k]:7.3f}" for k in range(min(6,N))))

    # Check: does |P[j,k]| depend mainly on |j-k| (Toeplitz-in-magnitude)?
    print("\nMean |P[j,k]| by band d=k-j (Toeplitz-in-magnitude test):")
    for d in range(0, min(6,N)):
        vals = [np.abs(P[j,j+d]) for j in range(N-d)]
        print(f"   d={d}: mean={np.mean(vals):.4f}  std={np.std(vals):.4f}  rel={np.std(vals)/(np.mean(vals)+1e-30):.3f}")

    # Christoffel-Darboux / three-term recurrence probe on the whitened defect:
    # if D_N is (close to) a Jacobi/banded matrix in some basis, off-band decay is fast.
    print("\nOff-diagonal decay of D_N by band (|D[j,j+d]| averaged):")
    for d in range(0, min(7,N)):
        vals = [np.abs(D[j,j+d]) for j in range(N-d)]
        print(f"   d={d}: mean|D|={np.mean(vals):.4f}")

if __name__ == "__main__":
    main()
