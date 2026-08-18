"""Refinement convergence of the exact threshold target.

lam_min_norm = lambda_min( S_E^{-1/2} (S_E - Z_E*Z_E - b_E*A_0^dag b_E) S_E^{-1/2} )
             = 1 - ||Theta_N||^2 .
Galerkin restriction gives an UPPER bound on the true minimum, so the
question is whether the sequence in `refine` settles above 0.
"""
import sys, math
import numpy as np
import rowd_threshold as RT

steps = [(2,3),(3,4),(4,5),(5,7),(7,8),(8,9),(9,11),(13,16),(16,17),(23,25),(31,32),(32,37)]
refs  = [4,8,12,16,24,32]
print(f"{'q_old':>5}{'q_new':>6} " + "".join(f"{r:>10}" for r in refs) + "   trend")
for qo,qn in steps:
    row=[]
    for r in refs:
        try:
            bk = RT.threshold_blocks(qo,qn,refine=r)
            st = RT.schur_target(bk)
            row.append(st['lam_min_norm'])
        except Exception as e:
            row.append(float('nan'))
    d = row[-1]-row[-2]
    print(f"{qo:>5}{qn:>6} " + "".join(f"{v:10.5f}" for v in row) + f"   d={d:+.5f}")
    sys.stdout.flush()
