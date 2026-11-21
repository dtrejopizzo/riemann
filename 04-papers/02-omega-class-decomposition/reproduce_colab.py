"""
reproduce_colab.py

Short single-file version of reproduce.py for the paper
  "The omega-class decomposition of Dirichlet polynomials:
   elementary bounds and computations"
by David Alejandro Trejo Pizzo.

For one value of N it evaluates the class sums

    S_k(t;N) = sum_{2 <= n <= N, omega(n) = k} n^{-1/2-it},   k = 1..K_N,

on the grid t_j = N/10 + j*dt, dt = pi/log N, t_j <= N, and prints the grid
means and grid maxima of |S_k|^2, the grid maximum of 1+r = |D|^2/sum_k|S_k|^2
and the comparison value sum_{omega(n)=k} 1/n of the mean value theorem.

The maxima printed here are maxima over the grid points only (the values in
parentheses in Table 1 of the paper).  The refinement between grid points,
the figures and the JSON file are done by reproduce.py.

Dependencies: numpy.  N = 10^4 takes about a minute; the cost grows
like N^2 log N.
"""
import math

import numpy as np

N = 10_000        # 50_000, 100_000, 150_000 for the other rows of Table 1
CHUNK = 64        # t-values per block


def omega_array(N):
    """omega(n) = number of distinct prime factors, n = 0..N."""
    omega = np.zeros(N + 1, dtype=np.int32)
    sieve = np.ones(N + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, N + 1):
        if sieve[p]:
            sieve[p * p::p] = False
            omega[p::p] += 1
    return omega


def main(N):
    om = omega_array(N)[2:]
    n = np.arange(2, N + 1, dtype=np.float64)
    logn = np.log(n)
    K = int(om.max())
    W = np.zeros((N - 1, K))
    W[np.arange(N - 1), om - 1] = n ** -0.5

    dt = math.pi / math.log(N)
    ts = N / 10.0 + dt * np.arange(int(math.floor(0.9 * N / dt)) + 1)
    S = np.empty((len(ts), K), dtype=np.complex128)
    for a in range(0, len(ts), CHUNK):
        ph = np.outer(ts[a:a + CHUNK], logn)
        S[a:a + CHUNK] = np.cos(ph) @ W - 1j * (np.sin(ph) @ W)

    P = np.abs(S) ** 2
    one_plus_r = np.abs(S.sum(axis=1)) ** 2 / P.sum(axis=1)
    B = P.max()
    print(f"N = {N}, K_N = {K}, {len(ts)} grid points, dt = {dt:.6f}")
    print(f"grid maximum of max_k |S_k|^2 = {B:.2f}  (class k = {int(P.max(axis=0).argmax()) + 1}),"
          f"  log B/log N = {math.log(B) / math.log(N):.4f}")
    print(f"grid maximum of 1+r = {one_plus_r.max():.3f}  (K_N = {K})")
    print(" k   terms   sum 1/n   grid mean   grid max   at t")
    for k in range(K):
        i = int(P[:, k].argmax())
        m = om == k + 1
        print(f"{k + 1:2d} {int(m.sum()):7d} {(1.0 / n[m]).sum():9.4f} {P[:, k].mean():11.4f}"
              f" {P[i, k]:10.2f}   {ts[i]:.3f}")


if __name__ == "__main__":
    main(N)
