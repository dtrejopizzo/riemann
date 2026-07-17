#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.13 -- persistent-divisor product probe.
#
# E71.12 found zero-independent persistent clusters.  This script forms a provisional
# "physical" product over persistent cluster centers and compares it to Xi/Xi(0), below the
# first zero.  This is not a proof object: persistence must eventually be replaced by an intrinsic
# Riesz/Fredholm projection.
# ======================================================================================
import importlib.util
from pathlib import Path
import numpy as np
import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent

spec12 = importlib.util.spec_from_file_location("e71_12", HERE / "E71_12_persistence_filter.py")
e71_12 = importlib.util.module_from_spec(spec12)
spec12.loader.exec_module(e71_12)

spec8 = importlib.util.spec_from_file_location("e71_8", HERE / "E71_8_canonical_product_probe.py")
e71_8 = importlib.util.module_from_spec(spec8)
spec8.loader.exec_module(e71_8)

def persistent_centers(lam=5.0, Ns=(14,18,20,24,30,36,40), planted=None, radius=1e-3, min_count=3):
    observations = []
    for N in Ns:
        roots = e71_12.roots_for(lam, N, planted=planted)
        for root in roots:
            observations.append((N, float(root)))
    clusters = e71_12.cluster_observations(observations, radius=radius)
    return np.array([c["center"] for c in clusters if c["count"] >= min_count], dtype=float), clusters

def rel_errors(vals, target):
    err = vals - target
    return np.linalg.norm(err) / np.linalg.norm(target), np.max(np.abs(err)) / np.max(np.abs(target))

def run_case(tag, planted=None, tmax=12.0):
    ts = np.linspace(0.0, tmax, 160)
    target = np.array([e71_8.Xi_norm(t) for t in ts], dtype=float)
    centers, clusters = persistent_centers(planted=planted)
    prod = e71_8.product_values(ts, centers)
    l2, sup = rel_errors(prod, target)
    print(f"\n### {tag} | planted={planted} ###")
    print(f"#persistent={len(centers)}  relL2={l2:.6e}  relSup={sup:.6e}")
    print(f"centers={np.array2string(centers[:16], precision=6)}")

if __name__ == "__main__":
    print("=" * 90)
    print(" E71.13 -- persistent-divisor product probe")
    print("=" * 90)
    run_case("zeta true", planted=None)
    run_case("planted off-line", planted=(25.0, 0.30, 5.0))
    print("\nREADING")
    print("  The product uses only persistence clusters, not known zero locations.")
    print("  A proof needs an intrinsic operator projection producing this divisor.")
