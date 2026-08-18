"""W2 task (3) support: lamM_aa / eigM_tt / normM_at / lam_min_norm at refine
8,16,32,64 across EVERY reachable prime-power step (all 25 in
W2_common.PRIME_POWER_STEPS), single rtol=1e-11 (the default; the rtol
sensitivity itself was already swept on 5 steps in W2_sweep.py/W2_sweep.json).
This is the breadth-across-thresholds grid the coercivity regression
(lambda_min(M_aa) vs log(1/delta_j)) needs -- W2_sweep.py's "deep" grid only
covers 5 cheap steps.

Command:
    python3 W2_sweep_refine.py
Writes W2_sweep_refine.json incrementally.
"""
import json, sys, time
import W2_common as W2
import W2_sweep as S

REFS = [8, 16, 32, 64]

if __name__ == '__main__':
    out = []
    t0 = time.time()
    for qo, qn in W2.PRIME_POWER_STEPS:
        for refine in REFS:
            rec = S.one(qo, qn, refine, 1e-11)
            out.append(rec)
            print(f"{qo:>3},{qn:<3} r={refine:>3} na={rec['na']:3d} nt={rec['nt']} "
                  f"lam={rec['lam_min_norm_ref']:.6e} lamM_aa={rec['lamM_aa']:.6e} "
                  f"eigM_tt={rec['eigM_tt']} normM_at={rec['normM_at']:.4e} "
                  f"delta={rec['delta']:.5f} ({rec['time']:.1f}s, total {time.time()-t0:.0f}s)")
            sys.stdout.flush()
            json.dump(out, open('W2_sweep_refine.json', 'w'), indent=1)
    print(f"done, {len(out)} records, {time.time()-t0:.0f}s")
