"""W3 task (2), full sweep: ||Phi|| at every prime-power threshold up to 37,
at refine 8/16/32, as a function of the pseudo-inverse rtol cutoff.

Uses ONLY the "cheap" Rayleigh-quotient route of W3_task2_phi_norm.py
(||Phi||^2 = lambda_max(R_P^{dag/2} L_P R_P^{dag/2})), which was already
cross-checked against the full explicit channel-built SVD route in
W3_task2_phi_norm.py at refine 4,8 (agreement to <1e-6 relative, printed
"YES" at every threshold/rtol there).  The explicit route is combinatorially
expensive at refine 16/32 (it materializes the full L^2(R)-codomain matrices,
tens of thousands of rows) and is not needed for this quantity: R_P, L_P
themselves are already validated to machine precision against X^*X, Y^*Y in
W3_task1_verify.py, independent of how Phi is subsequently computed from them.

Run:  python3 W3_task2b_phi_norm_fast.py
"""
import math
import numpy as np
import W3_build_xy as W3
from W3_task2_phi_norm import phi_norm_cheap, PRIME_POWER_THRESHOLDS, RTOLS


def run(refines=(8, 16, 32), thresholds=PRIME_POWER_THRESHOLDS, rtols=RTOLS):
    rows = []
    print(f"{'q':>4} {'refine':>6} {'dimP':>5} {'rtol':>8} {'rank(R_P)':>9} "
          f"{'||Phi||^2':>12} {'||Phi||':>10}")
    for refine in refines:
        for q in thresholds:
            T = 0.5 * math.log(q)
            ch = W3.build_channels(T, refine=refine)
            Z = W3.primitive_basis(ch['Tate'], ch['Gram'])
            rc = W3.restrict_channels(ch, Z)
            R_P, L_P = rc['R_P'], rc['L_P']
            for rtol in rtols:
                val, rk = phi_norm_cheap(R_P, L_P, rtol)
                nrm = math.sqrt(max(val, 0.0))
                print(f"{q:>4} {refine:>6} {rc['dimP']:>5} {rtol:>8.0e} {rk:>9} "
                      f"{val:12.8f} {nrm:10.8f}")
                rows.append(dict(q=q, refine=refine, dimP=rc['dimP'], rtol=rtol,
                                  rank_RP=rk, phi2=val, phi=nrm))
    return rows


if __name__ == '__main__':
    import json
    rows = run()
    with open('W3_task2b_phi_norm.json', 'w') as f:
        json.dump(rows, f, indent=1)
