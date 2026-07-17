#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.6 -- characteristic-function convergence probe.
#
# E71.5 reduces the CAND-1 closure to local uniform convergence of real-rooted CCM
# characteristic functions to Xi.  This script builds the natural entire function
#
#   Phi_N(s) = (2/sqrt(L)) sin(sL/2) Σ_k xi_k/(s-d_k),  d_k=2πk/L,
#
# and fits a single scalar normalization against Xi on a real grid.  This is diagnostic only:
# fitting against Xi is not a proof.  The goal is to see whether zero locking is accompanied by
# function-level convergence or whether amplitude/extra-zero effects remain.
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

def Xi(t):
    s = mp.mpf("0.5") + 1j * mp.mpf(str(t))
    return complex(mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s))

def ccm_vector(lam, N):
    M, idx, L = e71_2.build_QW(lam, N, planted=None)
    _, V = np.linalg.eigh(M)
    xi = V[:, 0]
    xi = (xi + xi[::-1]) / 2
    return xi, idx, L

def sinc_ratio(s, d, L):
    x = s - d
    out = np.empty_like(x, dtype=np.complex128)
    small = np.abs(x) < 1e-8
    sinval = np.sin(s * L / 2.0)
    out[~small] = sinval[~small] / x[~small]
    if np.any(small):
        # d=2*pi*k/L, so sin(sL/2)/(s-d) -> (L/2)cos(dL/2) = (L/2)(-1)^k.
        k = np.rint(d[small] * L / (2 * np.pi)).astype(int)
        out[small] = (L / 2.0) * ((-1.0) ** k)
    return out

def Phi_values(ts, xi, idx, L):
    d = 2 * np.pi * idx / L
    vals = []
    for t in ts:
        s = complex(t)
        ratios = sinc_ratio(np.full_like(d, s, dtype=np.complex128), d, L)
        vals.append((2.0 / np.sqrt(L)) * np.dot(xi, ratios))
    return np.array(vals, dtype=np.complex128)

def fit_scalar(phi, target):
    return np.vdot(phi, target) / np.vdot(phi, phi)

def run(lam=5.0, Ns=(14, 18, 24, 40), tmax=42.0, ngrid=260):
    ts = np.linspace(0.0, tmax, ngrid)
    target = np.array([Xi(t) for t in ts], dtype=np.complex128)
    scale = np.max(np.abs(target))
    print(f"grid: [0,{tmax}] with {ngrid} points, max|Xi|={scale:.6e}")
    print("   N      |c|        relL2        relSup       maxAbsErr")
    for N in Ns:
        xi, idx, L = ccm_vector(lam, N)
        phi = Phi_values(ts, xi, idx, L)
        c = fit_scalar(phi, target)
        err = c * phi - target
        rel_l2 = np.linalg.norm(err) / np.linalg.norm(target)
        rel_sup = np.max(np.abs(err)) / scale
        print(f"{N:4d} {abs(c):10.3e} {rel_l2:12.6e} {rel_sup:12.6e} {np.max(np.abs(err)):12.6e}")

if __name__ == "__main__":
    print("=" * 90)
    print(" E71.6 -- characteristic-function convergence probe")
    print("=" * 90)
    run()
    print("\nREADING")
    print("  A single fitted scalar is allowed only as a diagnostic.  Closure requires a canonical")
    print("  normalization and locally uniform convergence, not a least-squares fit to Xi.")
