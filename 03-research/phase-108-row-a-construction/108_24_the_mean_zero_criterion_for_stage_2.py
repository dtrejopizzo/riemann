#!/usr/bin/env python3
"""Verifier for 108.24 - the mean-zero criterion for Stage 2: exact
   cancellation of the a-independent divergent constant on balanced
   profiles, and the criterion operating on an invariant and a
   non-invariant illustrative witness.  numpy only."""
import numpy as np, sys
FAIL = []
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

GRID = np.linspace(0.0, 1.0, 80001)   # symmetric about 0.5, includes endpoints

# --- illustrative model: D(T) unbounded a-independent divergence, L_g(a,T)
#     -> L_g(a) an entire-in-a-style closed object, symmetric about a=0.5
#     (standing in for 108_11's L_g / 108_06's c_g; not a literal
#     recomputation of either, clearly a model).
def D(T): return np.log(T)
def L_g_limit(a): return np.cos(2*np.pi*(a-0.5))          # even about a=0.5
def L_g(a, T): return L_g_limit(a) * (1 - 1.0/T)           # -> L_g_limit(a)

def Sigma(phi_fn, T):
    return np.trapz(phi_fn(GRID)*(D(T) + L_g(GRID, T)), GRID)

def integral(fn_of_a):
    return np.trapz(fn_of_a(GRID), GRID)

# --- balanced profile #1: odd about a=0.5 (by construction), designed to
#     pair to EXACTLY zero against the even L_g_limit -- an exact symmetry,
#     not a numerical coincidence.
def even_bump(a, w=0.18):
    return np.exp(-((a-0.5)**2)/(2*w**2))

def phi_zero(a):
    a = np.asarray(a, dtype=float)
    return (a-0.5)*even_bump(a)   # odd about 0.5

# --- balanced profile #2: even about a=0.5 minus its mean, designed to pair
#     to a nonzero value against L_g_limit (even * even = even, generically
#     nonzero integral).
def phi_nonzero_raw(a):
    return even_bump(a, w=0.10)

mean_raw = integral(phi_nonzero_raw)
def phi_nonzero(a):
    return phi_nonzero_raw(a) - mean_raw   # now mean zero by subtraction

# --- non-balanced control: plain even bump, mean != 0 ---------------------
def phi_control(a):
    return even_bump(a, w=0.10)

int_phi_zero      = integral(phi_zero)
int_phi_nonzero   = integral(phi_nonzero)
int_phi_control   = integral(phi_control)
check("phi_zero is balanced (odd symmetry => exact zero mean)",
      abs(int_phi_zero) < 1e-12, f"{int_phi_zero:.2e}")
check("phi_nonzero is balanced (mean subtracted by construction)",
      abs(int_phi_nonzero) < 1e-12, f"{int_phi_nonzero:.2e}")
check("phi_control is NOT balanced (control case)",
      abs(int_phi_control) > 1e-3, f"{int_phi_control:.4f}")

# --- (A) exact cancellation identity: Sigma(phi_balanced,T) = int(phi*L_g(.,T))
Ts = np.array([10.0, 1e3, 1e6, 1e9, 1e12])
for name, phi_fn in (("phi_zero", phi_zero), ("phi_nonzero", phi_nonzero)):
    Sig = np.array([Sigma(phi_fn, T) for T in Ts])
    Lpart = np.array([np.trapz(phi_fn(GRID)*L_g(GRID, T), GRID) for T in Ts])
    ok = np.allclose(Sig, Lpart, atol=1e-9)
    check(f"[{name}] exact cancellation: Sigma(phi,T) = int(phi*L_g(.,T)) "
          f"at every T (D(T) term vanishes identically)", ok,
          f"max abs diff {np.max(np.abs(Sig-Lpart)):.2e}")

# --- (B) Criterion 3.1 operating: the two witnesses -----------------------
Lambda0_zero    = Sigma(phi_zero, 1e12)      # T large: approximates the limit
Lambda0_nonzero = Sigma(phi_nonzero, 1e12)
closed_zero    = integral(lambda a: phi_zero(a)*L_g_limit(a))
closed_nonzero = integral(lambda a: phi_nonzero(a)*L_g_limit(a))

check("Criterion 3.1, invariant witness: Lambda_g^0(phi_zero) = 0 "
      "('not detected non-invariant')",
      abs(Lambda0_zero) < 1e-9 and abs(closed_zero) < 1e-12,
      f"Lambda0={Lambda0_zero:.3e} closed_form={closed_zero:.3e}")
check("Criterion 3.1, non-invariant witness: Lambda_g^0(phi_nonzero) != 0 "
      "('certified non-invariant'), matches closed form",
      abs(Lambda0_nonzero) > 1e-3 and abs(Lambda0_nonzero-closed_nonzero) < 1e-6,
      f"Lambda0={Lambda0_nonzero:.6f} closed_form={closed_nonzero:.6f}")

# T -> infinity convergence check (genuine limit, not just large-T snapshot)
Sig_seq_nonzero = np.array([Sigma(phi_nonzero, T) for T in Ts])
converging = np.max(np.abs(np.diff(Sig_seq_nonzero))) < np.abs(Sig_seq_nonzero[0])
check("Lambda_g^0(phi_nonzero) sequence in T is Cauchy / converging (not "
      "just evaluated at one large T)",
      abs(Sig_seq_nonzero[-1]-Sig_seq_nonzero[-2]) < 1e-8,
      f"values: {[round(float(x),8) for x in Sig_seq_nonzero]}")

# --- (C) non-balanced control diverges ------------------------------------
Sig_control = np.array([Sigma(phi_control, T) for T in Ts])
slope = np.polyfit(np.log(Ts), Sig_control, 1)[0]
check("non-balanced control profile: Sigma(phi_control,T) diverges, slope "
      "vs log T matches int(phi_control) (the balanced restriction is "
      "load-bearing, not cosmetic)",
      abs(slope-int_phi_control) < 5e-3,
      f"fitted slope={slope:.6f} int(phi)={int_phi_control:.6f}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
