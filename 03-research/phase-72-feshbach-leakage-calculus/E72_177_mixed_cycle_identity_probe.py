#!/usr/bin/env python3
import itertools
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_174_trace_cycle_identity_probe import relative_cells  # noqa: E402


def brute_mixed(cells0, cells1, r, s):
    mats0 = [c[3] for c in cells0]
    mats1 = [c[3] for c in cells1]
    total = 0.0
    for tup0 in itertools.product(range(len(mats0)), repeat=r):
        left = mats0[tup0[0]]
        for i in tup0[1:]:
            left = left @ mats0[i]
        for tup1 in itertools.product(range(len(mats1)), repeat=s):
            prod = left
            for i in tup1:
                prod = prod @ mats1[i]
            total += np.trace(prod)
    return float(np.real(total))


def run():
    print("E72.177 mixed cycle identity probe")
    print("verifies Tr(K0^r K1^s)=sum Tr(A0...A0 A1...A1)")
    for lam, n_modes in [(6, 18), (8, 24)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        cells0, cells1 = relative_cells(lam, idx, L, bq, c_model, 0.60)
        k0 = sum((c[3] for c in cells0), np.zeros_like(cells0[0][3]))
        k1 = sum((c[3] for c in cells1), np.zeros_like(cells1[0][3]))
        print(f"lambda={lam:.0f} cells0={len(cells0)} cells1={len(cells1)}")
        for r, s in [(1, 1), (2, 1), (1, 2)]:
            direct = float(np.trace(np.linalg.matrix_power(k0, r) @ np.linalg.matrix_power(k1, s)))
            expanded = brute_mixed(cells0, cells1, r, s)
            err = abs(direct - expanded)
            scale = max(1.0, abs(direct), abs(expanded))
            print(
                f"  r={r} s={s} direct={direct:+.12e} "
                f"cycle={expanded:+.12e} relErr={err/scale:.3e}"
            )
        sys.stdout.flush()


if __name__ == "__main__":
    run()
