"""W2 supplementary check: does the block-level decay (lamM_aa, min(eigM_tt),
||M_at||, Schur-min) show the SAME refine=512 flattening that RESUME (c-NEW)
found for lam_min_norm on step (2,3) (W0_deep_refine.json: flattens to a
positive limit ~3.65e-4), or does it look like steady power decay? This
bears directly on whether "coercivity of M_aa" should be read as "eventually
constant" or "eventually vanishing but slower than the Tate block" -- W1 owns
settling the float64-conditioning-artifact question in general; this is a
narrow, cheap, step-(2,3)-only extension of W2's own block quantities to the
same refine reached by W0_deep_refine.py, for direct comparison.

Command: python3 W2_deep_check.py
"""
import json, time, sys
import W2_sweep as S

out = []
for rf in [8,16,32,64,128,256,512]:
    t0=time.time()
    rec = S.one(2,3,rf,1e-11)
    out.append(rec)
    print(f"r={rf:4d} lam={rec['lam_min_norm_ref']:.6e} lamM_aa={rec['lamM_aa']:.6e} "
          f"eigM_tt={rec['eigM_tt']} normM_at={rec['normM_at']:.4e} "
          f"schurM={rec['schurM_tt_minus']} minA0={rec['minA0']:.3e} ({time.time()-t0:.1f}s)")
    sys.stdout.flush()
    json.dump(out, open('W2_deep_check.json','w'), indent=1)
print("done")
