#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_137_cell_balance_probe import make_q, primes_upto, build_parts, orient  # noqa: E402


def prime_orbits(lam):
    out = []
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        k = 1
        while pm <= maxn:
            out.append((k * lp, lp * (pm ** -0.5), p, k))
            pm *= p
            k += 1
    return sorted(out)


def orbit_matrix(idx, L, length, weight):
    n = len(idx)
    mat = np.zeros((n, n))
    for a in range(n):
        for b in range(a, n):
            q = make_q(idx[a], idx[b], L)
            val = weight * q(length)
            mat[a, b] = mat[b, a] = val
    return mat


def w02_matrix(idx, L):
    n = len(idx)
    mat = np.zeros((n, n))
    for a in range(n):
        for b in range(a, n):
            q = make_q(idx[a], idx[b], L)
            val, _ = quad(lambda y: q(y) * (np.exp(y / 2) + np.exp(-y / 2)), 0, L, limit=200)
            mat[a, b] = mat[b, a] = val
    return mat


def run_case(lam, n_modes, gamma):
    h, w02, wr, prime, d, L = build_parts(lam, n_modes)
    idx = np.arange(-n_modes, n_modes + 1)
    vals, vecs = eigh(h)
    xi = orient(vecs[:, 0])
    e = 1.0 / (-gamma - d)
    e = e / norm(e)
    target = float(np.dot(e, w02 @ xi))
    total_prime = float(np.dot(e, prime @ xi))
    partial = 0.0
    records = []
    for length, weight, p, k in prime_orbits(lam):
        mat = orbit_matrix(idx, L, length, weight)
        contrib = float(np.dot(e, mat @ xi))
        partial += contrib
        residual = target - partial
        records.append((length / L, p, k, contrib, residual))
    return L, target, total_prime, records


def run():
    print("E73.139 prime-orbit cancellation probe")
    print("Tracks residual <e,W02 xi> - partial_sum <e,Prime_orbit xi>.")
    print(" lam     L gamma  targetB totalPrimeB  bestResB best_u  finalResB")
    for lam, n_modes in [(20, 24), (24, 28)]:
        for gamma in [GAMMAS[0], GAMMAS[1]]:
            L, target, total_prime, records = run_case(lam, n_modes, gamma)
            best = min(records, key=lambda r: abs(r[4]))
            final_res = target - total_prime
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(abs(target), L):8.3f} {bexp(abs(total_prime), L):11.3f}"
                f" {bexp(abs(best[4]), L):9.3f} {best[0]:6.3f}"
                f" {bexp(abs(final_res), L):9.3f}"
            )
            # Print a sparse trace at quartiles of the ordered orbit list.
            for frac in [0.25, 0.50, 0.75, 1.00]:
                j = min(int(frac * len(records)) - 1, len(records) - 1)
                u, p, k, contrib, residual = records[j]
                print(
                    f"    u={u:5.3f} p={p:3d} k={k:2d}"
                    f" contribB={bexp(abs(contrib), L):8.3f}"
                    f" residualB={bexp(abs(residual), L):8.3f}"
                )


if __name__ == "__main__":
    run()

