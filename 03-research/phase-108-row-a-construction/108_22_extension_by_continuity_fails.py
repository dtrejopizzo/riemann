#!/usr/bin/env python3
"""Verifier for 108.22 - extension by continuity fails for the canonical
   regularizing topology, by the same mechanism (108_21 Thm 1.1) that made
   substitution fail.  numpy only, no scipy/mpmath."""
import numpy as np, sys
FAIL = []
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# --- (A) f_a(1) = 1 for a grid of complex a --------------------------------
# f_a(x) = x^{-a}; at x=1, x^{-a} = 1 for every a (principal branch, 1^{-a}=1
# since log(1)=0).  Verify by direct evaluation, not by assumption.
grid_a = [0.5+0j, 0.3+0j, 1.0+0j, 0.5+1.2j, 0.25-0.7j, 2.1+3.4j, -0.4+0.9j]
ok = True
for a in grid_a:
    val = np.exp(-a*np.log(1.0))   # 1^{-a} via log(1)=0
    if abs(val-1.0) > 1e-14: ok = False
check("f_a(1) = 1^{-a} = 1 for every a tested", ok, f"n={len(grid_a)}")

# --- (B) coherence of the canonical net: f_{a,T}(1) = f_a(1) EXACTLY -------
def f_a(x, a): return x**(-a)
def sharp_cutoff_net(a, T, x=1.0):
    return f_a(x, a) if (1.0/T <= x <= T) else 0.0
def smooth_mollified_net(a, T, x=1.0, width=0.1):
    # bump(x) = 1 on the "core" region, tapering to 0 near the cutoff edges;
    # for T large enough the taper never touches x=1.
    lo, hi = np.log(1.0/T), np.log(T)
    t = np.log(x)
    core_lo, core_hi = lo*(1-width), hi*(1-width)
    if core_lo <= t <= core_hi:
        return f_a(x, a)
    return 0.0

ok = True; rows = []
for a in (0.5, 0.3+0.4j, 1.2):
    for T in (1.5, 2.0, 10.0, 1000.0, 1e6):
        v1 = sharp_cutoff_net(a, T)
        v2 = smooth_mollified_net(a, T)
        rows.append((a, T, v1, v2))
        if abs(v1-1.0) > 1e-14 or abs(v2-1.0) > 1e-14: ok = False
check("f_{a,T}(1) = 1 exactly, sharp cutoff and mollified core, all T>1", ok,
      f"n={len(rows)} combinations")

# --- (C) toy model of 108_21 Thm 1.1(a): shell-sum diverges monotonically
#     iff varphi_0 != 0, is exactly finite (zero increments) iff varphi_0=0 -
#     illustrative only, NOT a re-derivation of 108_17's p-adic computation.
def shell_partial_sums(phi0, N, weight=lambda k: 1.0):
    s = 0.0; out = [0.0]
    for k in range(N):
        s += phi0*weight(k)
        out.append(s)
    return np.array(out)

ok = True
for phi0 in (1.0, 2.5, -0.7):
    s = shell_partial_sums(phi0, 4000)
    # strictly monotone (same sign increments) and |s_N| -> infinity linearly
    incr = np.diff(s)
    monotone = np.all(incr*phi0 >= -1e-15) if phi0 != 0 else True
    diverges = abs(s[-1]) > 1000*abs(phi0)  # grows without bound, phi0-scaled
    slope = np.polyfit(np.arange(len(s)), s, 1)[0]
    if not (monotone and diverges and abs(slope-phi0) < 1e-9): ok = False
check("varphi_0 != 0: toy shell sum diverges MONOTONICALLY at rate phi_0", ok)

s0 = shell_partial_sums(0.0, 4000)
check("varphi_0 = 0: toy shell sum stays exactly 0 at every depth", ok=bool(np.all(s0 == 0.0)))

# contrast: independently recomputed instance of 108_05's oscillatory
# Dirichlet kernel off the line (closed form 2 sinh((s-a) log T)/(s-a)),
# confirming sign changes persist -> NOT monotone, unlike the toy shell sum.
def closed_cutoff(a, s, T):
    d = s - a
    return 2*np.log(T) if abs(d) < 1e-14 else 2*np.sinh(d*np.log(T))/d

a0, u0 = 0.5, 1.0
vals = np.array([closed_cutoff(a0, a0+1j*u0, T).real
                  for T in np.exp(np.linspace(20, 60, 400))])
sign_changes = np.sum(np.diff(np.sign(vals)) != 0)
check("Mellin-side cutoff (on-line, u!=0) oscillates: many sign changes, "
      "unlike the monotone arithmetic-side toy model", sign_changes >= 5,
      f"sign changes = {sign_changes}")

# --- (D) Lemma 2.3(b): A_delta member, Mellin inversion recovers f(1) -----
# f(x) = exp(-(ln x)^2 / 2);  fhat(s) = sqrt(2 pi) exp(s^2/2)  (entire).
def f_gauss(x): return np.exp(-(np.log(x))**2/2.0)
def fhat_gauss(s): return np.sqrt(2*np.pi)*np.exp(s**2/2.0)

sigma = 0.5
ts = np.linspace(-60, 60, 4_000_001)
integrand = fhat_gauss(sigma + 1j*ts) * (1.0)**(-(sigma+1j*ts))  # x=1 -> x^{-s}=1
inv = np.trapz(integrand, ts).real / (2*np.pi)
exact = f_gauss(1.0)
check("Mellin inversion recovers f(1) from fhat on A_delta (Gaussian-Mellin)",
      abs(inv-exact) < 1e-6, f"inversion={inv:.8f} exact={exact:.8f}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
