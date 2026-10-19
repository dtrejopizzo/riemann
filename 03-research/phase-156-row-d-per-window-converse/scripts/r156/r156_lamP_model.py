"""R156_001 DIAGNOSTIC: the relaxed primitive class K^prim (P47 eq:Kprim, rem:Kprim) in the prime-free model.
For real F, c_F in K^prim iff F in P_T, or A=A'=0, or B=B'=0 (A'=int tF e^{t/2}, B'=int tF e^{-t/2}).
On {A=0} the pole term vanishes, so W=a there. Prints Galerkin bottoms of a on P_T, on ker{A,A'}, on ker{A}, and of W on L2.
Usage: python3 r156_lamP_model.py T N [--noprimes]"""
import sys, numpy as np, math
from numpy.polynomial.legendre import leggauss
from r156_green_matrix import build, basis, restricted_min
T = float(sys.argv[1]); N = int(sys.argv[2]); pr = '--noprimes' not in sys.argv
a, Wm, A, B = build(T, N, pr)
x, w = leggauss(N + 44); t = T * x; wt = T * w; E = basis(t, T, N)
Ap = E @ (wt * t * np.exp(t / 2))
print(f"T={T} N={N} primes={pr}")
print("  bottom a on P_T        :", f"{restricted_min(a, np.vstack([A, B])):+.10f}")
print("  bottom a on ker{A,A'}  :", f"{restricted_min(a, np.vstack([A, Ap])):+.10f}")
print("  bottom a(=W) on ker{A} :", f"{restricted_min(a, A[None, :]):+.10f}")
print("  bottom W on L2         :", f"{np.linalg.eigvalsh(Wm)[0]:+.10f}")
