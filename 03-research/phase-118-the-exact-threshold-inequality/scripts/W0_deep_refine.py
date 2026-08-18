"""Coordinator: settle whether lam_min_norm -> 0 or to a positive limit.
Pushes refinement far past the r<=128 of W1_convergence.json.
run:  python3 W0_deep_refine.py
"""
import json, time, sys
import numpy as np
import rowd_threshold as RT

STEPS = [(2,3),(3,4),(5,7)]
REFS  = [64,96,128,192,256,384,512]
out={}
for qo,qn in STEPS:
    rows=[]
    for r in REFS:
        t0=time.time()
        try:
            bk=RT.threshold_blocks(qo,qn,refine=r)
            st=RT.schur_target(bk)
        except Exception as e:
            print(f"{qo},{qn} r={r} FAILED {e}"); sys.stdout.flush(); break
        rows.append(dict(refine=r,cells=bk['cells'],lam=st['lam_min_norm'],
                         minA0=st['minA0'],t=time.time()-t0))
        print(f"{qo},{qn} r={r:4d} cells={bk['cells']:5d} lam={st['lam_min_norm']:.6e} "
              f"minA0={st['minA0']:.3e} ({time.time()-t0:.1f}s)"); sys.stdout.flush()
    out[f"{qo},{qn}"]=rows
    json.dump(out,open('W0_deep_refine.json','w'),indent=1)
print("done")
