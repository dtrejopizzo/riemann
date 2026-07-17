#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.12 -- zero-independent finite-section persistence filter.
#
# Static backgrounds (pole mesh, sine comb, arch/free product) failed.  This tests a dynamic
# background principle:
#
#   physical divisor = roots persistent under finite-section refinement N;
#   background       = roots drifting with N.
#
# Clustering uses only roots from CCM finite sections.  Known zeta zeros are printed only after the
# fact as an audit label, not as input to the clustering.
# ======================================================================================
import importlib.util
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("e71_2", HERE / "E71_2_convergence_detector.py")
e71_2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e71_2)

ZEROS = e71_2.ZEROS

def roots_for(lam, N, planted=None, hmax=55):
    M, idx, L = e71_2.build_QW(lam, N, planted)
    _, V = np.linalg.eigh(M)
    xi = V[:, 0]
    xi = (xi + xi[::-1]) / 2
    return e71_2.roots_of_f(xi, idx, L, smax=hmax)

def cluster_observations(observations, radius=1e-3):
    # observations: list of (N, root)
    observations = sorted(observations, key=lambda x: x[1])
    clusters = []
    for N, root in observations:
        placed = False
        for cl in clusters:
            center = np.mean([r for _, r in cl])
            if abs(root - center) <= radius:
                cl.append((N, root))
                placed = True
                break
        if not placed:
            clusters.append([(N, root)])
    out = []
    for cl in clusters:
        Ns = sorted({N for N, _ in cl})
        vals = np.array([r for _, r in cl])
        out.append({
            "center": float(np.mean(vals)),
            "spread": float(np.max(vals) - np.min(vals)) if len(vals) else 0.0,
            "count": len(cl),
            "Ns": Ns,
        })
    return sorted(out, key=lambda c: (-c["count"], c["center"]))

def nearest_zero(center):
    idx = int(np.argmin(np.abs(ZEROS - center)))
    return idx + 1, float(ZEROS[idx]), float(abs(ZEROS[idx] - center))

def run_case(tag, lam=5.0, Ns=(14,18,20,24,30,36,40), planted=None, radius=1e-3, min_count=3):
    print(f"\n### {tag} | lambda={lam}, planted={planted}, radius={radius:g} ###")
    observations = []
    for N in Ns:
        roots = roots_for(lam, N, planted=planted)
        for root in roots:
            observations.append((N, float(root)))
        print(f"  N={N:2d}: #roots={len(roots):2d}, roots[:8]={np.array2string(roots[:8], precision=4)}")

    clusters = cluster_observations(observations, radius=radius)
    persistent = [c for c in clusters if c["count"] >= min_count]
    print(f"\nPersistent clusters (count >= {min_count})")
    print(" center        count spread       Ns                  nearest zeta zero")
    for c in persistent[:16]:
        j, z, err = nearest_zero(c["center"])
        print(
            f"{c['center']:10.6f} {c['count']:6d} {c['spread']:10.3e}"
            f"  {str(c['Ns']):20s}  gamma{j} err={err:.6e}"
        )
    return persistent

if __name__ == "__main__":
    print("=" * 90)
    print(" E71.12 -- finite-section persistence filter")
    print("=" * 90)
    run_case("zeta true", planted=None)
    run_case("planted off-line", planted=(25.0, 0.30, 5.0))
    print("\nREADING")
    print("  Clustering used no zero locations.  The nearest-zeta column is only an audit label.")
    print("  A useful relative determinant may keep persistent clusters and quotient drifting roots.")
