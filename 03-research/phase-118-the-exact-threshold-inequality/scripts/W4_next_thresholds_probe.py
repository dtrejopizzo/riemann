"""W4 exploratory probe (FLOATING POINT ONLY -- not a certificate).

Command:
  cd .../phase-118-the-exact-threshold-inequality/scripts
  python3 W4_next_thresholds_probe.py

Purpose: use the SPEC exact-step machinery (rowd_threshold.threshold_blocks /
schur_target, unmodified) to see whether lam_min_norm stays nonnegative, and
how it trends under mesh refinement, at the steps beyond the certified
T=log2 endpoint: (q_old,q_new) = (4,5),(5,7),(7,8),(8,9),(9,11),(11,13).
T_new = (1/2) log q_new.  Also reports the minimizing (near-null) direction's
support to see where it concentrates (old core vs corona; Tate-adjacent or
Gamma-bulk).
"""
import math
import numpy as np
import rowd_threshold as RT

steps = [(4,5),(5,7),(7,8),(8,9),(9,11),(11,13),(13,16)]
refs = [4,8,12,16,24,32]

print(f"{'q_old':>5}{'q_new':>6}{'T_new':>10} " + "".join(f"{r:>10}" for r in refs) + "   trend")
for qo, qn in steps:
    row = []
    for r in refs:
        try:
            bk = RT.threshold_blocks(qo, qn, refine=r)
            st = RT.schur_target(bk)
            row.append(st['lam_min_norm'])
        except Exception as e:
            row.append(float('nan'))
    Tn = 0.5*math.log(qn)
    d = row[-1]-row[-2] if len(row) >= 2 else float('nan')
    print(f"{qo:>5}{qn:>6}{Tn:>10.5f} " + "".join(f"{v:10.5f}" for v in row) + f"   d={d:+.5f}")
