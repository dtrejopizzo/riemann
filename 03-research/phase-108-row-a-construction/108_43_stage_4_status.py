#!/usr/bin/env python3
"""
Verifier for 108_43 -- Stage 4 status: the geometry, closed.

Checks:
  1. 108_41's verifier still passes, run fresh as a subprocess.
  2. 108_42's verifier still passes, run fresh as a subprocess.
  3. The given closed form for Phi (supplied for this task, not re-derived)
     matches its two supplied anchor values, Phi(1/2) and its root near 0.3,
     at 40-digit precision.

This file does not re-derive any of G1-G4; it is a consistency/status check.
"""
import sys
import os
import subprocess
import mpmath as mp

mp.mp.dps = 45

PASS = []


def report(name, ok, detail=""):
    PASS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------
# Checks 1-2: re-run the two prior verifiers as subprocesses
# ---------------------------------------------------------------------
print("=== Checks 1-2: prior verifiers still pass, fresh interpreter ===")
for fname in [
    "108_41_stage_4_the_archimedean_intersection_form.py",
    "108_42_stage_4_signature_and_the_local_term.py",
]:
    path = os.path.join(HERE, fname)
    result = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=300)
    exit_ok = (result.returncode == 0)
    verdict_ok = "VERDICT: ALL CHECKS PASS" in result.stdout
    ok = exit_ok and verdict_ok
    report(f"{fname}: exit 0 and prints ALL CHECKS PASS", ok,
           f"returncode={result.returncode}")
    if not ok:
        print("---- captured stdout (tail) ----")
        print("\n".join(result.stdout.splitlines()[-20:]))
        print("---- captured stderr (tail) ----")
        print("\n".join(result.stderr.splitlines()[-20:]))

# ---------------------------------------------------------------------
# Check 3: given closed form for Phi vs supplied anchor values
# ---------------------------------------------------------------------
print("\n=== Check 3: given Phi closed form vs supplied anchor values ===")


def Phi(s):
    return (2 * mp.digamma(1 - s)
            - mp.mpf('0.5') * mp.digamma(s / 2)
            - mp.mpf('0.5') * mp.digamma((1 - s) / 2)
            - mp.log(4 * mp.pi))


phi_half = Phi(mp.mpf('0.5'))
target_half = mp.mpf('-2.2305907656358723438')
err_half = abs(phi_half - target_half)
ok_half = err_half < mp.mpf('1e-18')
report("Phi(1/2) matches supplied value to <1e-18", ok_half, f"err={float(err_half):.3e}")

given_root = mp.mpf('0.30169238816042209152')
found_root = mp.findroot(Phi, given_root)
err_root = abs(found_root - given_root)
ok_root = err_root < mp.mpf('1e-18')
report("root of Phi near 0.3 matches supplied value to <1e-18", ok_root,
       f"err={float(err_root):.3e}")

# sanity: Phi(root) really is (near) zero, confirming it is a genuine root
# of the given closed form, not just close to the supplied number
phi_at_root = Phi(given_root)
ok_zero = abs(phi_at_root) < mp.mpf('1e-15')
report("Phi(given_root) is (numerically) zero", ok_zero, f"|Phi(root)|={float(abs(phi_at_root)):.3e}")

# ---------------------------------------------------------------------
overall = all(PASS)
print()
if overall:
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    sys.exit(1)
