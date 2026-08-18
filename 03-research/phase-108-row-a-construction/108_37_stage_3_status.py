#!/usr/bin/env python3
"""Verifier for 108.37 - re-runs the Stage 3 chain."""
import subprocess, sys, pathlib
here=pathlib.Path(__file__).parent
chain=["108_34_the_shell_functional_gamma_p_k.py",
       "108_35_the_log_p_normalization.py",
       "108_36_the_assembly_is_the_logarithmic_derivative.py"]
FAIL=[]
for c in chain:
    p=here/c
    if not p.exists():
        print(f"[FAIL] {c} missing"); FAIL.append(c); continue
    r=subprocess.run([sys.executable,str(p)],capture_output=True,text=True,timeout=900)
    ok = r.returncode==0 and "ALL CHECKS PASS" in r.stdout
    print(f"[{'ok ' if ok else 'FAIL'}] {c} exit={r.returncode}")
    if not ok: FAIL.append(c)
print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
