#!/usr/bin/env python3
"""Verifier for 108.25 - Stage 1 reformulated: re-runs the verifiers this
   synthesis depends on as subprocesses, then one fresh independent
   cross-check of the exact-cancellation mechanism.  numpy only."""
import numpy as np, subprocess, sys, os

FAIL = []
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

HERE = os.path.dirname(os.path.abspath(__file__))

SCRIPTS = [
    "108_05_mellin_duality_of_the_graded_family.py",
    "108_21_stage_1_final.py",
    "108_22_extension_by_continuity_fails.py",
    "108_23_smeared_pairing_convergence_and_dichotomy.py",
    "108_24_the_mean_zero_criterion_for_stage_2.py",
]

print("=== re-running dependency verifiers as subprocesses ===")
results = []
for s in SCRIPTS:
    path = os.path.join(HERE, s)
    exists = os.path.isfile(path)
    if not exists:
        results.append((s, False, "FILE NOT FOUND"))
        continue
    p = subprocess.run([sys.executable, path], cwd=HERE,
                        capture_output=True, text=True, timeout=600)
    ok = (p.returncode == 0)
    tail = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ""
    results.append((s, ok, tail))

for s, ok, tail in results:
    check(f"subprocess exit 0: {s}", ok, tail)

print()
print("=== consolidated table ===")
for s, ok, tail in results:
    print(f"  {'PASS' if ok else 'FAIL':4s}  {s}")
print()

# --- fresh, independent cross-check of the exact-cancellation mechanism ---
# A THIRD model pair (D(T), L_g), distinct from 108_23's (log T, sin) and
# 108_24's (log T, cos, symmetric): here D(T) = sqrt(T) (a different growth
# rate entirely) and L_g(a) a non-symmetric entire-style function, to make
# sure the exact cancellation is not an artifact of one growth rate or one
# symmetric choice of L_g.
GRID = np.linspace(0.0, 1.0, 60001)
def D3(T): return np.sqrt(T)
def L_g3_limit(a): return np.exp(0.3*a)*np.sin(3*np.pi*a + 0.7)  # no special symmetry
def L_g3(a, T): return L_g3_limit(a)*(1 - 1.0/T)

def Sigma3(phi_fn, T):
    return np.trapz(phi_fn(GRID)*(D3(T) + L_g3(GRID, T)), GRID)

def integral(fn_of_a):
    return np.trapz(fn_of_a(GRID), GRID)

def bump(a, c, w):
    return np.exp(-((a-c)**2)/(2*w**2))

def phi_balanced(a):
    a = np.asarray(a, dtype=float)
    raw = bump(a, 0.35, 0.08) - 0.6*bump(a, 0.75, 0.10)
    return raw - integral(lambda x: bump(x, 0.35, 0.08) - 0.6*bump(x, 0.75, 0.10))

def phi_unbalanced(a):
    return bump(np.asarray(a, dtype=float), 0.5, 0.15)

int_bal = integral(phi_balanced)
int_unbal = integral(phi_unbalanced)
check("fresh model: phi_balanced has zero mean", abs(int_bal) < 1e-12,
      f"{int_bal:.2e}")
check("fresh model: phi_unbalanced has nonzero mean (control)",
      abs(int_unbal) > 1e-3, f"{int_unbal:.4f}")

Ts = np.array([10.0, 1e3, 1e6, 1e9])
Sig_bal = np.array([Sigma3(phi_balanced, T) for T in Ts])
Lpart_bal = np.array([np.trapz(phi_balanced(GRID)*L_g3(GRID, T), GRID) for T in Ts])
check("fresh model: exact cancellation Sigma(phi_balanced,T) = int(phi*L_g3(.,T)) "
      "at every T, sqrt(T)-growth D(T) and non-symmetric L_g3",
      np.allclose(Sig_bal, Lpart_bal, atol=1e-9),
      f"max abs diff {np.max(np.abs(Sig_bal-Lpart_bal)):.2e}")

Sig_unbal = np.array([Sigma3(phi_unbalanced, T) for T in Ts])
slope_sqrtT = np.polyfit(np.sqrt(Ts), Sig_unbal, 1)[0]
check("fresh model: Sigma(phi_unbalanced,T) diverges like sqrt(T)*int(phi), "
      "confirming the mechanism generalizes beyond the log-T model",
      abs(slope_sqrtT-int_unbal) < 1e-2,
      f"fitted slope={slope_sqrtT:.6f} int(phi)={int_unbal:.6f}")

limit_bal = integral(lambda a: phi_balanced(a)*L_g3_limit(a))
check("fresh model: Sigma(phi_balanced,T) -> int(phi*L_g3_limit) as T->infty",
      abs(Sig_bal[-1]-limit_bal) < 1e-2,
      f"Sigma(T=1e9)={Sig_bal[-1]:.6f} limit={limit_bal:.6f}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
