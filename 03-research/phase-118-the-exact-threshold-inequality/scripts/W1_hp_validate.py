"""W1: validate the high-precision pipeline (W1_hp_lib/W1_hp_threshold) against
the established float64 pipeline (rowd_assembly/rowd_threshold) at small
refine, and check the Euler-Maclaurin Psi (float64) against the direct-sum
Psi (mpmath) agree.

Run:  python3 W1_hp_validate.py
"""
import time
import mpmath as mp
import numpy as np

import rowd_assembly as RA
import rowd_threshold as RT
import W1_hp_lib as L
import W1_hp_threshold as HT


def check_psi():
    print("== Psi kernel: float64 Euler-Maclaurin vs mpmath direct sum ==")
    mp.mp.dps = 40
    for D in [0.0, 1e-3, 0.01, 0.1, 0.5, 1.0, 3.7, 17.3]:
        f64 = RA.psi_kernel(D)
        hp = L.psi_kernel_mp(mp.mpf(D)) if D > 0 else L.psi_kernel_mp(mp.mpf(0))
        diff = abs(mp.mpf(f64) - hp)
        print(f"  D={D:<10} float64={f64:.15e}  mp(dps=40)={mp.nstr(hp,20)}  |diff|={mp.nstr(diff,3)}")


def check_blocks(q_old, q_new, refine, dps):
    print(f"\n== step ({q_old},{q_new}) refine={refine} dps={dps} ==")
    t0 = time.time()
    bk64 = RT.threshold_blocks(q_old, q_new, refine=refine)
    st64 = RT.schur_target(bk64)
    print(f"  float64: lam_min_norm={st64['lam_min_norm']:.10e} minA0={st64['minA0']:.6e} "
          f"minSE={st64['minSE']:.6e} rankSE={st64['rank_SE']} dimC={bk64['dimC']} dimA={bk64['dimA']} "
          f"({time.time()-t0:.2f}s)")

    mp.mp.dps = dps + 20
    t0 = time.time()
    bkhp = HT.threshold_blocks_mp(q_old, q_new, refine=refine)
    print(f"  hp assemble: dimC={bkhp['dimC']} dimA={bkhp['dimA']} dimP={bkhp['dimP']} "
          f"cells={bkhp['cells']} ({time.time()-t0:.2f}s)")
    t0 = time.time()
    r1 = HT.route1_direct(bkhp, rtol_A0=mp.mpf('1e-11'), eps_list=[mp.mpf(10)**-e for e in (6,8,10,12)])
    print(f"  route1 (dps={dps}): lam_cutoff={mp.nstr(r1['lam_min_norm_cutoff'],dps)}  "
          f"minA0={mp.nstr(r1['minA0'],dps)}  minSE={mp.nstr(r1['minSE'],dps)}  ({time.time()-t0:.2f}s)")
    for eps, val in r1['lam_min_norm_eps'].items():
        print(f"    eps={mp.nstr(eps,3)}  lam_min_norm(eps)={mp.nstr(val,dps)}")

    t0 = time.time()
    r2 = HT.route2_regularized(bkhp, eps_list=[mp.mpf(10)**-e for e in (6,8,10,12)])
    print(f"  route2 (dps={dps}): minR0={mp.nstr(r2['minR0'],dps)} minSE={mp.nstr(r2['minSE'],dps)} "
          f"minD0={mp.nstr(r2['minD0'],dps)}  ({time.time()-t0:.2f}s)")
    for eps, val in r2['lam_min_Ceps'].items():
        print(f"    eps={mp.nstr(eps,3)}  lam_min(Ceps)={mp.nstr(val,dps)}")

    print(f"  cross-check vs float64: hp_cutoff={mp.nstr(r1['lam_min_norm_cutoff'],12)} "
          f"vs float64={st64['lam_min_norm']:.10e}  "
          f"relerr={mp.nstr(abs(r1['lam_min_norm_cutoff']-mp.mpf(st64['lam_min_norm']))/abs(mp.mpf(st64['lam_min_norm'])),3)}")
    return bk64, st64, bkhp, r1, r2


if __name__ == '__main__':
    check_psi()
    for refine in (4, 8):
        check_blocks(2, 3, refine, dps=30)
