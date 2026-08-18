#!/usr/bin/env python3
"""Verifier for 113.99 -- re-runs every verifier in the phase.

113_13 sums Lambda(n) to 2e5 at four probes and computes 60 zeta zeros at
dps=30, and 113_14/113_15 compute zeros too, so the timeout is generous.
Pass a prefix to run a subset, e.g.  python3 113_99_verify_all.py 113_1
"""
import subprocess
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

SCRIPTS = (
    "113_01_the_local_integral_for_schwartz_data.py",
    "113_02_the_global_sum.py",
    "113_03_the_construction.py",
    "113_04_verdict.py",
    "113_05_canonical_conventions.py",
    "113_06_the_canonical_weil_decomposition.py",
    "113_07_the_identity_functional_is_a_norm.py",
    "113_08_the_two_rulings_and_the_index_engine.py",
    "113_09_the_radical_is_the_xi_ideal.py",
    "113_10_the_degree_map_and_the_effective_cone.py",
    "113_11_the_section_functor.py",
    "113_12_the_trace_and_the_duality.py",
    "113_13_the_assembly_and_the_missing_gap.py",
    "113_14_the_two_analytic_gaps.py",
    "113_15_the_four_row_ledger.py",
)

pref = sys.argv[1] if len(sys.argv) > 1 else ""
ok = True
total = 0
for s in SCRIPTS:
    if not s.startswith(pref):
        continue
    if not os.path.exists(s):
        print("[FAIL] %-52s [MISSING]" % s)
        ok = False
        continue
    try:
        r = subprocess.run([sys.executable, s], capture_output=True, text=True,
                           timeout=3600)
        npass = r.stdout.count("[PASS]")
        nfail = r.stdout.count("[FAIL]")
        good = r.returncode == 0 and "VERDICT: ALL CHECKS PASS" in r.stdout
    except subprocess.TimeoutExpired:
        npass, nfail, good = -1, -1, False
    ok &= good
    total += max(npass, 0)
    print("[%s] %-52s %3d passed, %d failed"
          % ("PASS" if good else "FAIL", s, npass, nfail))

print("\n%d individual checks across the phase." % total)
print("VERDICT: %s" % ("ALL CHECKS PASS" if ok else "FAILURES PRESENT"))
sys.exit(0 if ok else 1)
