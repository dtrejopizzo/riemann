"""W1 task 1: refinement sweep of lam_min_norm for the cheap steps.

Command:
    python3 W1_convergence_run.py

Writes W1_convergence.json (in this scripts/ dir) with, for each
(q_old,q_new) in {(2,3),(3,4),(4,5),(5,7),(7,8)} and refine in
{4,8,12,16,24,32,48,64,96,128}: lam_min_norm, cells, dimA, wall time.
rtol for the pseudo-inverse cutoff in A_0 is left at rowd_threshold's
default (1e-11) here -- sensitivity to that choice is task 2, done in a
separate script (W1_pinv_sweep_run.py).
"""
import json, time, sys
import rowd_threshold as RT

STEPS = [(2, 3), (3, 4), (4, 5), (5, 7), (7, 8)]
REFS = [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]

if __name__ == '__main__':
    out = {}
    t_start = time.time()
    for qo, qn in STEPS:
        key = f"{qo},{qn}"
        out[key] = []
        for r in REFS:
            t0 = time.time()
            bk = RT.threshold_blocks(qo, qn, refine=r)
            st = RT.schur_target(bk)
            t1 = time.time()
            rec = dict(refine=r, cells=bk['cells'], dimA=bk['dimA'],
                       dimC=bk['dimC'], lam_min_norm=st['lam_min_norm'],
                       rank_SE=st['rank_SE'], res_r=st['res_r'],
                       res_b=st['res_b'], minA0=st['minA0'],
                       minSE=st['minSE'], time=t1 - t0)
            out[key].append(rec)
            print(f"{qo:>3},{qn:<3} refine={r:>4} cells={bk['cells']:>5} "
                  f"lam={st['lam_min_norm']:.8e}  t={t1-t0:6.2f}s "
                  f"(total {time.time()-t_start:7.1f}s)")
            sys.stdout.flush()
    with open('W1_convergence.json', 'w') as f:
        json.dump(out, f, indent=1)
    print("wrote W1_convergence.json")
