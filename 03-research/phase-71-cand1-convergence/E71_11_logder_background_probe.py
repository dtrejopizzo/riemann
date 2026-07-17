#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.11 -- log-derivative background probe for the CCM Weyl m-function.
#
# E71.10 identifies the right finite object as
#   m_N(s)=Σ xi_k/(s-d_k),  d_k=2πk/L.
#
# This script compares Xi'/Xi on a zero-free interval [0,12] with:
#   1. log derivative of the all-root canonical product;
#   2. pole-relative log derivative P'/P - Q'/Q, i.e. m_N'/m_N;
#   3. sine-depoled log derivative d/ds log(sin(sL/2)m_N(s)).
#
# All three are zero-location-free once xi_N is computed from QW.  This is a diagnostic for the
# canonical background_N in E71.10.
# ======================================================================================
import importlib.util
from pathlib import Path
import numpy as np
import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("e71_2", HERE / "E71_2_convergence_detector.py")
e71_2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e71_2)

def xi_completed(t):
    s = mp.mpf("0.5") + 1j * mp.mpf(str(t))
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def xi_logder(t):
    tt = mp.mpf(str(t))
    return float(mp.re(mp.diff(lambda u: mp.log(xi_completed(u)), tt)))

def ccm_data(lam, N, hmax=55):
    M, idx, L = e71_2.build_QW(lam, N, planted=None)
    _, V = np.linalg.eigh(M)
    xi = V[:, 0]
    xi = (xi + xi[::-1]) / 2
    roots = e71_2.roots_of_f(xi, idx, L, smax=hmax)
    d = 2 * np.pi * idx / L
    return xi, idx, d, L, roots

def even_logder_from_positive_roots(ts, roots):
    roots = np.asarray([r for r in roots if r > 1e-10], dtype=float)
    vals = []
    for t in ts:
        vals.append(float(np.sum((-2.0 * t) / (roots * roots - t * t))))
    return np.array(vals)

def m_logder(ts, xi, d):
    vals = []
    for t in ts:
        den = t - d
        m = np.sum(xi / den)
        mpv = -np.sum(xi / (den * den))
        vals.append(float(np.real(mpv / m)))
    return np.array(vals)

def sine_depoled_logder(ts, xi, d, L):
    vals = m_logder(ts, xi, d)
    corr = []
    for t in ts:
        x = t * L / 2.0
        if abs(np.sin(x)) < 1e-8:
            corr.append(np.nan)
        else:
            corr.append((L / 2.0) / np.tan(x))
    return vals + np.array(corr)

def rel_errors(vals, target):
    mask = np.isfinite(vals) & np.isfinite(target)
    err = vals[mask] - target[mask]
    return np.linalg.norm(err) / np.linalg.norm(target[mask]), np.max(np.abs(err)) / np.max(np.abs(target[mask]))

def run(lam=5.0, Ns=(18, 40), tmin=0.4, tmax=12.0, ngrid=180):
    # Avoid t=0 and the pole mesh/sine singularities by using a shifted grid.
    ts = np.linspace(tmin, tmax, ngrid)
    target = np.array([xi_logder(t) for t in ts], dtype=float)
    print(f"grid: [{tmin},{tmax}], {ngrid} points; target max={np.max(np.abs(target)):.6e}")
    print("   N  #roots   all_L2     poleRel_L2  sineDep_L2   all_sup    poleRel_sup sineDep_sup")
    for N in Ns:
        xi, idx, d, L, roots = ccm_data(lam, N)
        all_ld = even_logder_from_positive_roots(ts, roots)
        pole_rel = m_logder(ts, xi, d)
        sine_dep = sine_depoled_logder(ts, xi, d, L)
        all_l2, all_sup = rel_errors(all_ld, target)
        pr_l2, pr_sup = rel_errors(pole_rel, target)
        sd_l2, sd_sup = rel_errors(sine_dep, target)
        print(
            f"{N:4d} {len(roots):7d}"
            f" {all_l2:10.3e} {pr_l2:12.3e} {sd_l2:11.3e}"
            f" {all_sup:10.3e} {pr_sup:12.3e} {sd_sup:11.3e}"
        )

if __name__ == "__main__":
    print("=" * 90)
    print(" E71.11 -- log-derivative background probe for CCM m-function")
    print("=" * 90)
    run()
    print("\nREADING")
    print("  all      = log derivative of product over CCM roots.")
    print("  poleRel  = m_N'/m_N = P_N'/P_N - Q_N'/Q_N.")
    print("  sineDep  = d/ds log(sin(sL/2)m_N(s)).")
    print("  A useful background should reduce the error without fitting to Xi.")
