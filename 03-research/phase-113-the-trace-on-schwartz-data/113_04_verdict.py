#!/usr/bin/env python3
"""Verifier for 113.04 -- verdict.

Re-runs 113_01-113_03 as subprocesses (must all pass), then illustrates the
generic-independence plausibility argument of SS2 on a finite-dimensional
model: three GENERIC linear functionals on R^5 have a nontrivial common
kernel (dimension >= 2); three functionals built to be linearly DEPENDENT
do not add a genuinely new constraint. This is an illustration of the
structural point, not a proof of SS2's claim about the actual (f,g) space.
"""
import os
import subprocess
import sys

import numpy as np

PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print("[%s] %s  %s" % ("PASS" if ok else "FAIL", name, detail))


os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 70)
print("Re-running 113_01, 113_02, 113_03 as subprocesses")
print("=" * 70)
for script in ("113_01_the_local_integral_for_schwartz_data.py",
               "113_02_the_global_sum.py",
               "113_03_the_construction.py"):
    r = subprocess.run([sys.executable, script], capture_output=True, text=True,
                        timeout=300)
    ok = r.returncode == 0 and "VERDICT: ALL CHECKS PASS" in r.stdout
    check("%s exits 0 with ALL CHECKS PASS" % script, ok)

print()
print("=" * 70)
print("Illustration: three linear functionals on R^5")
print("=" * 70)
rng = np.random.default_rng(20260803)

# Three GENERIC (independent) functionals: common kernel has dimension
# 5 - 3 = 2 (generically), i.e. a nontrivial (>0-dimensional) solution space.
A = rng.normal(size=(3, 5))
u, s, vt = np.linalg.svd(A)
null_dim_generic = int(np.sum(s < 1e-9)) + (5 - len(s))
check("three GENERIC linear functionals on R^5: nontrivial common kernel",
      null_dim_generic >= 2,
      "kernel dimension = %d (expected 2)" % null_dim_generic)

# Three functionals built to be DEPENDENT (the third is a combination of the
# first two): the effective rank is only 2, so the "third condition" adds
# nothing -- this is the failure mode SS2 says has not been ruled out, shown
# here only as what it would look like if it happened.
B = rng.normal(size=(2, 5))
dependent_third = 0.7 * B[0] - 1.3 * B[1]
A_dep = np.vstack([B, dependent_third])
rank_dep = np.linalg.matrix_rank(A_dep, tol=1e-9)
check("control: a THIRD functional dependent on the first two adds no constraint",
      rank_dep == 2,
      "effective rank = %d (expected 2, not 3)" % rank_dep)

# And confirm independence is the generic case: resample many random triples,
# almost all have full rank 3 (i.e. dependency, as in the control above, is
# a measure-zero coincidence, not the default outcome).
indep_count = 0
trials = 200
for _ in range(trials):
    M = rng.normal(size=(3, 5))
    if np.linalg.matrix_rank(M, tol=1e-9) == 3:
        indep_count += 1
check("random triples of functionals are independent with overwhelming frequency",
      indep_count == trials,
      "%d/%d trials gave full rank 3" % (indep_count, trials))

print()
print("Summary: %d passed, %d failed" % (len(PASS), len(FAIL)))
if FAIL:
    print("FAILED:", FAIL)
    print("VERDICT: FAILURES PRESENT")
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")
sys.exit(0)
