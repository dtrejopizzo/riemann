#!/usr/bin/env python3
"""
The degenerate borderline (Example deg) and threshold growth.

nu_m = (1-1/m) delta_0 + (1/m) Lebesgue[0,1]  ->  nu_inf = delta_0 (rank-one limit).
We compute the smallest eigenvalue of the order-N Hankel moment matrix of nu_m and
show it decays with m (the order-N positivity threshold T_0(N) grows), illustrating
the degenerate-limit case of the HR stability theorem and the shape of zeta's hierarchy.
"""
import numpy as np
from math import comb

def moments_nu(m, N):
    # moment_j = (1-1/m)*0^j + (1/m)*int_0^1 x^j dx ; 0^0=1
    mu = np.empty(2*N+1)
    for j in range(2*N+1):
        leb = 1.0/(j+1)
        point = 1.0 if j == 0 else 0.0
        mu[j] = (1-1.0/m)*point + (1.0/m)*leb
    return mu

def hankel_min_eig(m, N):
    mu = moments_nu(m, N)
    H = np.array([[mu[a+b] for b in range(N+1)] for a in range(N+1)])
    return float(np.linalg.eigvalsh((H+H.T)/2)[0])

if __name__ == "__main__":
    print(" order-N Hankel smallest eigenvalue of nu_m (degenerate limit nu_inf=delta_0):")
    print(f"   {'m':>6} " + "".join(f"   N={N}" for N in [2,3,4]))
    for m in [4, 16, 64, 256, 1024]:
        row = "  ".join(f"{hankel_min_eig(m,N):8.2e}" for N in [2,3,4])
        print(f"   {m:>6}  {row}")
    print(" higher order N => smaller min eigenvalue at fixed m: threshold T_0(N) grows in N.")
