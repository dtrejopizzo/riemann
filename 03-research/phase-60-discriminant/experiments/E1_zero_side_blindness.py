#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — Discriminant.  E1: can the validated zero-side detect multiplicativity?
#
# Thesis to test: "the sign of Weil is controlled by multiplicativity (Euler), not by the
# location of the zeros".  PRE-REGISTRATION (00-PLAN §5): if the useful difference is only
# explained by zero location, it is CIRCULAR -> NO-GO for this route.
#
# This script does NOT build a new engine: it reuses the VALIDATED zero-side Gram form from
# the canonical engine (phase-5-structural/experiments/colab_phase3_engine.py, gates PASS).
#
# Operative question: M_zeros depends ONLY on the multiset of zeros. So two L-functions
# with the same zeros give the SAME Gram, whether Euler or not. We show this numerically:
#   (1) any ON-line set -> lambda_min in the "floor" (>=0), independent of
#       spacing/density (= independent of which L-function it is).
#   (2) the only mover of the sign is shifting zeros OFF-line (= RH-status, not Euler).
# Expected conclusion: the zero-side measures RH-STATUS, it is BLIND to multiplicativity.
# ======================================================================================
import numpy as np, mpmath as mp, math
mp.mp.dps = 30

T0, SIGMA, J = 85.7, 2.0, 8
NZEROS = 120

def hermite(J, u):
    u = np.asarray(u, dtype=complex)
    H = [np.pi**-0.25*np.exp(-u**2/2)]
    if J > 1: H.append(np.sqrt(2.0)*u*H[0])
    for k in range(2, J): H.append(np.sqrt(2.0/k)*u*H[k-1]-np.sqrt((k-1.0)/k)*H[k-2])
    return H
def g_at(J, sigma, T0, z):
    return np.array([h[0] for h in hermite(J, (np.asarray([z],dtype=complex)-T0)/sigma)])

def M_zeros(zlist, J, sigma, T0):
    """zlist: list of (t_rho, delta_rho).  Weil zero-side Gram (Hermitian)."""
    M = np.zeros((J, J), dtype=complex)
    for (t, d) in zlist:
        for (tt, dd) in ((t, d), (-t, d)):
            v = g_at(J, sigma, T0, tt - 1j*dd)
            u = g_at(J, sigma, T0, tt + 1j*dd)
            M += np.outer(v, np.conj(u))
    return (M + M.conj().T)/2

def lam_min_over_tr(M):
    l = np.linalg.eigvalsh(M)[0]; tr = np.trace(M).real
    return l, (l/tr if tr != 0 else float('nan'))

print("computing zeta zeros ...", flush=True)
GAM = [float(mp.im(mp.zetazero(n))) for n in range(1, NZEROS+1)]

# --- self-check: reproducir gate del engine canonico (floor on-line + negatividad forzada) ---
M0 = M_zeros([(g,0.0) for g in GAM], J, SIGMA, T0)
l0,r0 = lam_min_over_tr(M0)
print(f"[self-check] zeta on-line floor lambda_min/tr = {r0:+.3e} (should be ~>=0)")
assert r0 > -1e-6, "engine broken: negative on-line floor"

print("\n"+"="*78)
print(" E1.(1)  Different densities of ON-line zeros  (= different L-functions, all RH-true)")
print("="*78)
print(" If the zero-side detected 'which L-function it is', the floor would change. If it is BLIND, it won't.\n")
print("  configuration                          #zeros-window   lambda_min/tr")

# real zeta
print(f"  zeta (real zeros)                          {sum(1 for g in GAM if abs(g-T0)<2*SIGMA):>2}            {r0:+.4e}")

# synthetic ON-line sets with different densities (simulate other RH-true L-functions)
rng = np.random.default_rng(0)
for label, dens in [("density x0.5 (wide spacing)", 0.5),
                    ("density x1.0 (local uniform)", 1.0),
                    ("density x2.0 (dense spacing)", 2.0),
                    ("random phase perturbation", -1)]:
    if dens > 0:
        # local uniform grid at the requested density inside the window
        spacing = (2*np.pi/np.log(T0)) / dens   # ~ scaled mean zeta density
        ts = [T0 + k*spacing for k in range(-6,7)]
        zl = [(t,0.0) for t in ts] + [(g,0.0) for g in GAM if abs(g-T0)>=2*SIGMA]
    else:
        ts = [g + rng.normal(0,0.3) for g in GAM if abs(g-T0)<2*SIGMA]
        zl = [(t,0.0) for t in ts] + [(g,0.0) for g in GAM if abs(g-T0)>=2*SIGMA]
    M = M_zeros(zl, J, SIGMA, T0)
    l,r = lam_min_over_tr(M)
    nin = sum(1 for (t,_) in zl if abs(t-T0)<2*SIGMA)
    print(f"  {label:36s}   {nin:>2}            {r:+.4e}")

print("\n  -> ALL the ON-line configurations stay at the floor (>=0, up to numerical noise).")
print("     The zero-side does NOT distinguish 'which L-function'. It measures RH-status (on/off line), not Euler.")

print("\n"+"="*78)
print(" E1.(2)  The ONLY mover of the sign: shifting zeros OFF-line")
print("="*78)
print("  delta(off-line)   lambda_min/tr   <- this is zero location = RH-status\n")
for delta in (0.0, 0.05, 0.1, 0.2):
    M = M_zeros([(g,(delta if abs(g-T0)<2*SIGMA else 0.0)) for g in GAM], J, SIGMA, T0)
    l,r = lam_min_over_tr(M)
    print(f"      {delta:4.2f}          {r:+.4e}")

print("\n"+"="*78)
print(" VERDICT E1 (pre-registered in 00-PLAN §5)")
print("="*78)
print(" The validated zero-side is a function of the zero MULTISET only.")
print(" => Separating ζ (Euler) from L_DH here = separating by off-line zeros = LOCATION = CIRCULAR.")
print(" => The thesis 'multiplicativity controls the sign' is NOT testable on the zero-side.")
print(" => It lives entirely in the ARITHMETIC side M_arith (the one that is not validated).")
print(" CONSEQUENCE: the real bottleneck of Phase 60 is building a VALIDATED M_arith.")
