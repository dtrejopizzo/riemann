#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.3 -- convergence-rate probe for the CCM/CAND-1 front.
#
# Purpose:
#   Measure the finite-section convergence profile without changing the E71.2 engine.
#   This is deliberately diagnostic, not a proof.  The proof target is resolvent
#   convergence; this script reports whether the numerical behavior looks like:
#     (a) N-section saturation at fixed lambda,
#     (b) improvement as lambda grows,
#     (c) planted off-line floor.
# ======================================================================================
import importlib.util
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("e71_2", HERE / "E71_2_convergence_detector.py")
e71_2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e71_2)

ZEROS = e71_2.ZEROS

def spectrum_errors(lam, N, planted=None, k=5):
    M, idx, L = e71_2.build_QW(lam, N, planted)
    _, V = np.linalg.eigh(M)
    xi = V[:, 0]
    xi = (xi + xi[::-1]) / 2
    roots = e71_2.roots_of_f(xi, idx, L, smax=float(ZEROS[k - 1] + 8))
    errs = e71_2.matched_err(roots, ZEROS[:k])
    return roots, errs

def consecutive_count(errs, eps):
    out = 0
    for err in errs:
        if err < eps:
            out += 1
        else:
            break
    return out

def fixed_lambda_scan(lam=5.0, Ns=(10, 14, 18, 20, 24, 30, 36, 40), planted=None, k=5):
    rows = []
    for N in Ns:
        roots, errs = spectrum_errors(lam, N, planted=planted, k=k)
        rows.append((N, len(roots), errs))
    return rows

def lambda_horizon_scan(lams=(3.0, 3.7, 5.0, 7.0), k=5, eps=1e-5):
    rows = []
    for lam in lams:
        # Enough poles to cover the kth zero plus margin in the d_k mesh.
        N = int(np.ceil((float(ZEROS[k - 1]) + 8.0) * np.log(lam) / np.pi)) + 8
        roots, errs = spectrum_errors(lam, N, planted=None, k=k)
        rows.append((lam, N, len(roots), consecutive_count(errs, eps), errs))
    return rows

def print_fixed(tag, rows):
    print(f"\n### fixed-lambda scan: {tag} ###")
    print("   N  #roots      maxerr(first5)      errs(first5)")
    for N, nroots, errs in rows:
        print(f"{N:4d} {nroots:7d}   {np.nanmax(errs):14.6e}   {np.array2string(errs, precision=6)}")

def print_horizon(rows, eps):
    print(f"\n### lambda horizon scan, eps={eps:g} ###")
    print(" lambda    N  #roots  consecutive<eps   maxerr(first5)   errs(first5)")
    for lam, N, nroots, nconsec, errs in rows:
        print(
            f"{lam:6.2f} {N:4d} {nroots:7d} {nconsec:16d}"
            f"   {np.nanmax(errs):14.6e}   {np.array2string(errs, precision=6)}"
        )

if __name__ == "__main__":
    np.set_printoptions(suppress=False, linewidth=160)
    print("=" * 90)
    print(" E71.3 -- convergence-rate/PNT diagnostic for CAND-1")
    print("=" * 90)
    true_rows = fixed_lambda_scan(planted=None)
    off_rows = fixed_lambda_scan(planted=(25.0, 0.30, 5.0))
    print_fixed("zeta true, lambda=5", true_rows)
    print_fixed("planted off-line, lambda=5", off_rows)
    horizon_rows = lambda_horizon_scan(eps=1e-5)
    print_horizon(horizon_rows, eps=1e-5)
    print("\nREADING")
    print("  - Fixed lambda is a finite-section problem; errors can alias/non-monotonically saturate.")
    print("  - Lambda growth is the CCM convergence horizon; a proof needs a resolvent bound, not just PNT size.")
    print("  - Planted off-line data should keep a nonzero floor under the same scan.")
