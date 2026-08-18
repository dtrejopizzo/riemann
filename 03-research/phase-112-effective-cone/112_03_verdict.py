#!/usr/bin/env python3
"""Verifier for 112.03 -- re-runs the phase's prior verifiers."""
import subprocess, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ok = True
for s in ("112_01_the_candidate_cone.py", "112_02_is_it_the_right_cone.py"):
    r = subprocess.run([sys.executable, s], capture_output=True, text=True)
    good = r.returncode == 0 and "VERDICT: ALL CHECKS PASS" in r.stdout
    ok &= good
    print("[%s] %s exits 0 with ALL CHECKS PASS" % ("PASS" if good else "FAIL", s))
print("\nVERDICT: %s" % ("ALL CHECKS PASS" if ok else "FAILURES PRESENT"))
sys.exit(0 if ok else 1)
