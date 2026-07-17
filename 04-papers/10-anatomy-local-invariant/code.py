#!/usr/bin/env python3
"""
Front 2 / B2 closure: the ground-state autocorrelation c_0(u) and its real zeros.

The B2 converse holds in a window iff c_0(log n) != 0 for the non-prime-power n.  We test:
  (a) pure Gaussian ground state (lowest mode)         -> c_0 should be ZERO-FREE (converse holds outright);
  (b) excited (Hermite_k) ground state                 -> finitely many zeros; locate them (expect near band edge);
  (c) vary width sigma                                 -> zeros MOVE (non-stationary => all-windows converse).

c_0(u) = \int g_0(t) g_0(t-u) dt, g_0 = H_k(t/sigma) exp(-t^2/2 sigma^2).
"""
import numpy as np
from numpy.polynomial.hermite_e import hermeval

def hermite_phys(k, x):
    # physicists' Hermite via recurrence
    if k == 0: return np.ones_like(x)
    if k == 1: return 2*x
    Hkm1, Hk = np.ones_like(x), 2*x
    for n in range(1, k):
        Hkm1, Hk = Hk, 2*x*Hk - 2*n*Hkm1
    return Hk

def ground_state(t, sigma, coeffs):
    """g_0 = sum_k coeffs[k] H_k(t/sigma) exp(-t^2/2 sigma^2)."""
    g = np.zeros_like(t)
    for k, c in enumerate(coeffs):
        if c != 0:
            g += c*hermite_phys(k, t/sigma)
    return g*np.exp(-t**2/(2*sigma**2))

def autocorr(u_grid, sigma, coeffs, t_grid):
    g = ground_state(t_grid, sigma, coeffs); dt = t_grid[1]-t_grid[0]
    c0 = np.empty_like(u_grid)
    for i, u in enumerate(u_grid):
        gu = ground_state(t_grid-u, sigma, coeffs)
        c0[i] = np.sum(g*gu)*dt
    return c0

def real_zeros(u_grid, c0):
    s = np.sign(c0); idx = np.where(np.diff(s) != 0)[0]
    zs = []
    for i in idx:
        # linear interp
        u0, u1 = u_grid[i], u_grid[i+1]; y0, y1 = c0[i], c0[i+1]
        zs.append(u0 - y0*(u1-u0)/(y1-y0))
    return np.array(zs)

if __name__ == "__main__":
    t = np.linspace(-60, 60, 24000)
    u = np.linspace(0, 12, 4000)   # u = log n range; band edge ~ a few
    print("="*80)
    print(" B2 closure: real zeros of the ground-state autocorrelation c_0(u), u in [0,12]")
    print("="*80)

    print("\n (a) PURE GAUSSIAN ground state (lowest mode), sigma=1.5,2,3:")
    for sigma in [1.5, 2.0, 3.0]:
        c0 = autocorr(u, sigma, [1.0], t)
        zs = real_zeros(u, c0)
        print(f"   sigma={sigma}:  #real zeros in [0,12] = {len(zs)}   (c0>0 everywhere: {np.all(c0>0)})")

    print("\n (b) PURE EXCITED modes H_k (autocorr = Laguerre L_k(u^2/2s^2)e^{-u^2/4s^2}, k zeros), sigma=2:")
    for k in [2, 4, 6]:
        coeffs = [0.0]*k + [1.0]
        c0 = autocorr(u, 2.0, coeffs, t)
        zs = real_zeros(u, c0)
        zstr = ", ".join(f"{z:.3f}" for z in zs[:8])
        print(f"   H_{k}:  #real zeros={len(zs)}  zeros u=[{zstr}]")

    print("\n (c) NON-STATIONARITY: track the real zeros of c_0 (pure H_4) vs sigma:")
    print(f"   {'sigma':>7}   first three real zeros u*")
    for sigma in [1.4,1.6,1.8,2.0,2.2,2.5,3.0]:
        c0 = autocorr(u, sigma, [0,0,0,0,1.0], t)
        zs = real_zeros(u, c0)
        zstr = "  ".join(f"{z:.3f}" for z in zs[:3])
        print(f"   {sigma:>7.2f}   {zstr}")
    print("="*80)
    print(" Expect: (a) zero-free => converse outright; (b) few zeros near edge; (c) u* MOVES with sigma.")
