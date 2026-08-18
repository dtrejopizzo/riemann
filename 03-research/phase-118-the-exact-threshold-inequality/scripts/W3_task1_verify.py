"""W3 task (1): verify X_T^*X_T = R_T, Y_T^*Y_T = L_T, X_T^*X_T - Y_T^*Y_T = A_T
to machine precision, on the full mesh AND after restriction to P_T.

Run:  python3 W3_task1_verify.py
"""
import math
import numpy as np
import W3_build_xy as W3
import rowd_assembly as RA

PRIME_POWER_THRESHOLDS = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]


def run(refines=(4, 8), thresholds=PRIME_POWER_THRESHOLDS):
    print(f"{'q':>4} {'refine':>6} {'Ncells':>7} {'dimP':>5} "
          f"{'|XtX-R|':>12} {'|YtY-L|':>12} {'|diff-A|':>12} "
          f"{'scaleR':>9} {'scaleL':>9} {'scaleA':>9}")
    rows = []
    for refine in refines:
        for q in thresholds:
            T = 0.5 * math.log(q)
            ch = W3.build_channels(T, refine=refine)
            v = W3.verify_full(ch)
            Z = W3.primitive_basis(ch['Tate'], ch['Gram'])
            dimP = Z.shape[1]
            # restricted check: Z^T(XtX)Z should equal Z^T R Z etc (corollary,
            # but check explicitly with the actually-restricted blocks too)
            rc = W3.restrict_channels(ch, Z)
            Xblocks_P = [rc['Xg_P']] + [rc['ant_P'][n] for n in rc['ns']]
            Yblocks_P = [rc['Y0_P']] + [rc['sym_P'][n] for n in rc['ns']]
            XtX_P = sum(B.T @ B for B in Xblocks_P)
            YtY_P = sum(B.T @ B for B in Yblocks_P)
            res_R_P = float(np.abs(XtX_P - rc['R_P']).max())
            res_L_P = float(np.abs(YtY_P - rc['L_P']).max())
            res_A_P = float(np.abs((XtX_P - YtY_P) - rc['A_P']).max())
            print(f"{q:>4} {refine:>6} {ch['N']:>7} {dimP:>5} "
                  f"{v['resid_XtX_R']:>12.3e} {v['resid_YtY_L']:>12.3e} "
                  f"{v['resid_diff_A']:>12.3e} {v['scale_R']:>9.3f} "
                  f"{v['scale_L']:>9.3f} {v['scale_A']:>9.3f}   "
                  f"[P_T: {res_R_P:.2e} {res_L_P:.2e} {res_A_P:.2e}]")
            rows.append(dict(q=q, refine=refine, N=ch['N'], dimP=dimP, **v,
                              res_R_P=res_R_P, res_L_P=res_L_P, res_A_P=res_A_P))
    return rows


if __name__ == '__main__':
    run()
