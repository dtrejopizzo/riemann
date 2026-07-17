#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.4 -- Riesz-window stability diagnostic.
#
# Nearest-root matching can alias when finite sections add or move roots.  For a self-adjoint
# approximation, the resolvent/Riesz statement is better tested by isolating intervals around each
# target zero and counting the spectral rank in each interval.
#
# For real finite spectra:
#   rank P_j = (1/2πi) ∮_{Γ_j} Tr((z-H)^(-1)) dz
# is just the number of eigenvalues in the isolating window I_j.
# ======================================================================================
import importlib.util
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("e71_2", HERE / "E71_2_convergence_detector.py")
e71_2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e71_2)

ZEROS = e71_2.ZEROS

def zero_windows(k=5):
    zs = ZEROS[:k]
    windows = []
    for j, z in enumerate(zs):
        if j == 0:
            left = 0.5 * z
        else:
            left = 0.5 * (zs[j - 1] + z)
        if j == k - 1:
            # Use the next known zero to close the last window when available.
            right = 0.5 * (z + ZEROS[k])
        else:
            right = 0.5 * (z + zs[j + 1])
        windows.append((left, right))
    return windows

def roots_for(lam, N, planted=None, k=5):
    M, idx, L = e71_2.build_QW(lam, N, planted)
    _, V = np.linalg.eigh(M)
    xi = V[:, 0]
    xi = (xi + xi[::-1]) / 2
    smax = zero_windows(k)[-1][1] + 1.0
    return e71_2.roots_of_f(xi, idx, L, smax=smax)

def status_code(status):
    return {"LOCK": "L", "MISS": "-", "MULTI": "X"}[status]

def window_report(roots, k=5):
    rows = []
    for j, ((left, right), z) in enumerate(zip(zero_windows(k), ZEROS[:k]), start=1):
        inside = roots[(roots > left) & (roots < right)]
        if len(inside) == 1:
            err = float(abs(inside[0] - z))
            margin = float(min(inside[0] - left, right - inside[0]))
            status = "LOCK"
        elif len(inside) == 0:
            err = np.nan
            margin = 0.0
            status = "MISS"
        else:
            err = float(np.min(np.abs(inside - z)))
            margin = 0.0
            status = "MULTI"
        rows.append((j, float(z), float(left), float(right), int(len(inside)), err, margin, status))
    return rows

def micro_report(roots, radius=1e-3, k=5):
    rows = []
    for j, z in enumerate(ZEROS[:k], start=1):
        inside = roots[np.abs(roots - z) < radius]
        if len(inside) == 1:
            err = float(abs(inside[0] - z))
            status = "LOCK"
        elif len(inside) == 0:
            err = np.nan
            status = "MISS"
        else:
            err = float(np.min(np.abs(inside - z)))
            status = "MULTI"
        rows.append((j, float(z), int(len(inside)), err, status))
    return rows

def run_case(tag, lam, Ns, planted=None, k=5):
    print(f"\n### {tag} | lambda={lam}, planted={planted} ###")
    print("   N  ok-locks  statuses       maxerr(locked)")
    all_rows = []
    for N in Ns:
        roots = roots_for(lam, N, planted=planted, k=k)
        rows = window_report(roots, k=k)
        locked = [r for r in rows if r[-1] == "LOCK"]
        ok = sum(1 for r in rows if r[-1] == "LOCK" and r[5] < 1e-5)
        maxerr = max([r[5] for r in locked], default=np.nan)
        statuses = "".join(status_code(r[-1]) for r in rows)
        print(f"{N:4d} {ok:9d}/{k}  {statuses:12s} {maxerr:14.6e}")
        all_rows.append((N, rows))
    return all_rows

def run_micro_case(tag, lam, Ns, planted=None, radius=1e-3, k=5):
    print(f"\n### micro-contour scan: {tag} | lambda={lam}, radius={radius:g}, planted={planted} ###")
    print("   N  locks  statuses       maxerr(locked)")
    all_rows = []
    for N in Ns:
        roots = roots_for(lam, N, planted=planted, k=k)
        rows = micro_report(roots, radius=radius, k=k)
        locked = [r for r in rows if r[-1] == "LOCK"]
        maxerr = max([r[3] for r in locked], default=np.nan)
        statuses = "".join(status_code(r[-1]) for r in rows)
        print(f"{N:4d} {len(locked):6d}/{k}  {statuses:12s} {maxerr:14.6e}")
        all_rows.append((N, rows))
    return all_rows

def run_combined_case(tag, lam, Ns, planted=None, radius=1e-3, k=5):
    print(f"\n### {tag} | lambda={lam}, planted={planted} ###")
    cached = []
    for N in Ns:
        cached.append((N, roots_for(lam, N, planted=planted, k=k)))

    print("\nWide zero-gap windows")
    print("   N  ok-locks  statuses       maxerr(locked)")
    wide_rows = []
    for N, roots in cached:
        rows = window_report(roots, k=k)
        locked = [r for r in rows if r[-1] == "LOCK"]
        ok = sum(1 for r in rows if r[-1] == "LOCK" and r[5] < 1e-5)
        maxerr = max([r[5] for r in locked], default=np.nan)
        statuses = "".join(status_code(r[-1]) for r in rows)
        print(f"{N:4d} {ok:9d}/{k}  {statuses:12s} {maxerr:14.6e}")
        wide_rows.append((N, rows))

    print(f"\nMicro contours, radius={radius:g}")
    print("   N  locks  statuses       maxerr(locked)")
    micro_rows = []
    for N, roots in cached:
        rows = micro_report(roots, radius=radius, k=k)
        locked = [r for r in rows if r[-1] == "LOCK"]
        maxerr = max([r[3] for r in locked], default=np.nan)
        statuses = "".join(status_code(r[-1]) for r in rows)
        print(f"{N:4d} {len(locked):6d}/{k}  {statuses:12s} {maxerr:14.6e}")
        micro_rows.append((N, rows))

    return wide_rows, micro_rows

def print_last_detail(label, all_rows):
    N, rows = all_rows[-1]
    print(f"\nDetail at largest N for {label} (N={N})")
    print(" j    zero        window-left  window-right  rank      err        margin   status")
    for j, z, left, right, rank, err, margin, status in rows:
        err_s = "nan" if np.isnan(err) else f"{err:.6e}"
        print(f"{j:2d} {z:10.6f} {left:12.6f} {right:13.6f} {rank:5d} {err_s:>11s} {margin:9.4f} {status}")

if __name__ == "__main__":
    np.set_printoptions(suppress=False, linewidth=160)
    print("=" * 90)
    print(" E71.4 -- Riesz-window stability diagnostic")
    print("=" * 90)
    Ns = [14, 18, 20, 24, 30, 36, 40]
    true_rows, _ = run_combined_case("zeta true", 5.0, Ns, planted=None, radius=1e-3)
    off_rows, _ = run_combined_case("planted off-line", 5.0, Ns, planted=(25.0, 0.30, 5.0), radius=1e-3)
    print_last_detail("zeta true wide-window", true_rows)
    print_last_detail("planted off-line wide-window", off_rows)
    print("\nREADING")
    print("  Wide Voronoi windows are too coarse: finite CCM spectra can contain extra roots in the")
    print("  same zero gap.  The useful Riesz diagnostic is a small contour around the target zero.")
    print("  In the micro-contour scan, true zeta locks while the planted perturbation misses except")
    print("  when it pulls a root close to the planted height.")
