#!/usr/bin/env python3
import itertools
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_158_prime_cell_psd_probe import q_matrix  # noqa: E402
from E72_159_prime_block_psd_probe import relative_matrix  # noqa: E402


def relative_cells(lam, idx, L, bq, c_model, cut=0.60):
    cells = [[], []]
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            weight = lp * (pm ** -0.5)
            block = 0 if y <= cut * L else 1
            raw = bq.T @ (-weight * q_matrix(idx, L, y)) @ bq
            cells[block].append((pm, y, weight, relative_matrix(raw, c_model)))
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return cells


def cycle_trace(cells, degree):
    total = 0.0
    mats = [c[3] for c in cells]
    for tup in itertools.product(range(len(mats)), repeat=degree):
        prod = mats[tup[0]]
        for i in tup[1:]:
            prod = prod @ mats[i]
        total += np.trace(prod)
    return float(np.real(total))


def run():
    print("E72.174 trace cycle identity probe")
    print("verifies Tr((sum_a A_a)^r)=sum_{a1..ar}Tr(A_a1...A_ar)")
    for lam, n_modes in [(6, 18), (8, 24)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        cells = relative_cells(lam, idx, L, bq, c_model, 0.60)
        for block_id, block_cells in enumerate(cells):
            kblock = sum((c[3] for c in block_cells), np.zeros_like(block_cells[0][3]))
            print(f"lambda={lam:.0f} block={block_id} cells={len(block_cells)}")
            for degree in [2, 3]:
                direct = float(np.trace(np.linalg.matrix_power(kblock, degree)))
                expanded = cycle_trace(block_cells, degree)
                err = abs(direct - expanded)
                scale = max(1.0, abs(direct), abs(expanded))
                print(
                    f"  r={degree} direct={direct:+.12e} "
                    f"cycle={expanded:+.12e} relErr={err/scale:.3e}"
                )
            sys.stdout.flush()


if __name__ == "__main__":
    run()
