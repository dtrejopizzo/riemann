#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.8 -- canonical-product determinant probe.
#
# E71.6 showed that the raw sine-comb numerator does not converge to Xi under a scalar
# normalization.  The next natural Hurwitz object is a real-rooted canonical product over the
# finite CCM spectrum:
#
#   D_N(t) = Π_{r>0, r in sp(H_N)} (1 - t^2/r^2).
#
# This script compares:
#   all-roots product: canonical, but includes finite-section extra roots;
#   locked-roots product: diagnostic cheating control using known zeta windows.
#
# If all-roots fails while locked-roots tracks Xi locally, the missing object is a relative
# determinant/renormalization that cancels the finite-section background spectrum.
# ======================================================================================
import importlib.util
from pathlib import Path
import numpy as np
import mpmath as mp

mp.mp.dps = 40

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("e71_2", HERE / "E71_2_convergence_detector.py")
e71_2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e71_2)

ZEROS = e71_2.ZEROS

def Xi_norm(t):
    s = mp.mpf("0.5") + 1j * mp.mpf(str(t))
    xi = mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    s0 = mp.mpf("0.5")
    xi0 = mp.mpf("0.5") * s0 * (s0 - 1) * mp.power(mp.pi, -s0 / 2) * mp.gamma(s0 / 2) * mp.zeta(s0)
    return float(mp.re(xi / xi0))

def roots_for(lam, N, hmax=55):
    M, idx, L = e71_2.build_QW(lam, N, planted=None)
    _, V = np.linalg.eigh(M)
    xi = V[:, 0]
    xi = (xi + xi[::-1]) / 2
    return e71_2.roots_of_f(xi, idx, L, smax=hmax)

def product_values(ts, roots):
    roots = np.asarray([r for r in roots if r > 1e-9], dtype=float)
    vals = []
    for t in ts:
        factors = 1.0 - (t * t) / (roots * roots)
        vals.append(float(np.prod(factors)))
    return np.array(vals)

def locked_roots(roots, radius=1e-3, k=5):
    out = []
    for z in ZEROS[:k]:
        near = roots[np.abs(roots - z) < radius]
        if len(near) == 1:
            out.append(float(near[0]))
    return np.array(out)

def rel_errors(vals, target):
    err = vals - target
    return np.linalg.norm(err) / np.linalg.norm(target), np.max(np.abs(err)) / np.max(np.abs(target))

def run(lam=5.0, Ns=(18, 40), hmax=55, tmax=12.0):
    # Stay below the first zero: this tests determinant shape without crossing singular sign changes.
    ts = np.linspace(0.0, tmax, 160)
    target = np.array([Xi_norm(t) for t in ts], dtype=float)
    print(f"grid: [0,{tmax}] below first zero, hmax={hmax}")
    print("   N  #roots #locked     all_relL2    all_relSup    lock_relL2   lock_relSup")
    for N in Ns:
        roots = roots_for(lam, N, hmax=hmax)
        all_vals = product_values(ts, roots)
        locked = locked_roots(roots, radius=1e-3, k=5)
        lock_vals = product_values(ts, locked) if len(locked) else np.full_like(target, np.nan)
        all_l2, all_sup = rel_errors(all_vals, target)
        if len(locked):
            lock_l2, lock_sup = rel_errors(lock_vals, target)
        else:
            lock_l2, lock_sup = np.nan, np.nan
        print(
            f"{N:4d} {len(roots):7d} {len(locked):7d}"
            f" {all_l2:13.6e} {all_sup:13.6e}"
            f" {lock_l2:13.6e} {lock_sup:13.6e}"
        )
        print(f"      roots[:12]={np.array2string(roots[:12], precision=4)}")
        print(f"      locked   ={np.array2string(locked, precision=6)}")

if __name__ == "__main__":
    print("=" * 90)
    print(" E71.8 -- canonical-product determinant probe")
    print("=" * 90)
    run()
    print("\nREADING")
    print("  The all-roots product is canonical but includes finite-section background roots.")
    print("  The locked-roots product is a cheating diagnostic: if it behaves better, the missing")
    print("  object is a relative determinant that cancels background roots without knowing zeros.")
