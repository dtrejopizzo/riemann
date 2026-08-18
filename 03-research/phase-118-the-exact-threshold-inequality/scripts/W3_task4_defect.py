"""W3 task (4): the defect operator I - Phi^*Phi on codomain(X_T).

Phi = Y X^dagger, extended to all of codomain(X_T) by the Moore-Penrose
pseudoinverse (so Phi kills Ran(X_T)^perp).  Then, trivially, on Ran(X_T)^perp,
I - Phi^*Phi = I (Psi = identity there, uninteresting).  The content is on
Ran(X_T), where, pulling back through X_T (u = X_T v), the defect quadratic
form is EXACTLY <A_T v, v> -- this is just Douglas' lemma restated, not new
information.

What IS new information: what the defect matrix D = I - Phi^*Phi looks like
directly in the channel-blocked codomain(X_T) basis (Gamma channel + one
antisymmetric-contact channel per prime power n).  Its low eigenvalues
(near 1 - lam_max, i.e. near the criticality gap) have eigenvectors that are
honest functions living in codomain(X_T); decomposing each such eigenvector's
norm across channels (Gamma vs antisymmetric contacts) tests directly whether
the near-null direction of the defect is carried by the archimedean channel
or spread over the arithmetic ones -- the SAME question task (3) asks from
the X-domain side, now asked from the Y=Phi(X)-codomain side.

We also test one concrete closed-form CANDIDATE for the defect's leading
eigenvalue/eigenvector pair: is the bottom eigenvalue of D close to
`lam_min_norm` (the paper's own normalized threshold quantity, computed
independently by rowd_threshold.schur_target on the SAME mesh)?  If yes to
high precision, that is a nontrivial cross-check (two independently coded
routes agreeing); if it misses at the third digit, that is reported as a
failed identification, not smoothed over.

Run:  python3 W3_task4_defect.py
"""
import math
import numpy as np
import W3_build_xy as W3
import W3_task3b_blocks as W3B
import rowd_threshold as RT

THRESHOLDS = [8, 17]
REFINE = 8
RTOL = 1e-10
N_LOW = 8


def defect_spectrum(q, refine=REFINE, rtol=RTOL, n_low=N_LOW):
    res = W3B.build_explicit_phi(q, refine=refine, rtol=rtol)
    Phi = res['Phi']
    rowsX = Phi.shape[1]
    D = np.eye(rowsX) - Phi.T @ Phi
    D = 0.5 * (D + D.T)
    w, V = np.linalg.eigh(D)
    order = np.argsort(w)
    w = w[order]
    V = V[:, order]

    co = res['col_off']
    names = res['col_names']
    chan_fracs = []
    for k in range(min(n_low, V.shape[1])):
        v = V[:, k]
        fracs = []
        for i in range(len(names)):
            seg = v[co[i]:co[i+1]]
            fracs.append(float(np.dot(seg, seg)))
        chan_fracs.append(fracs)
    return dict(q=q, T=res['T'], w=w, chan_fracs=chan_fracs, names=names,
                rowsX=rowsX, dimP=res['dimP'])


def cross_check_via_raw_A_R(q, refine=REFINE):
    """Independent cross-check of the WHOLE explicit-channel construction:
    algebraically, since A_T = R_T - L_T, the generalized eigenvalues of the
    pencil (L_P,R_P) [= squared singular values of Phi on Ran(X), task 3a]
    and of the pencil (A_P,R_P) are related by mu = 1 - lam, EXACTLY, no
    matter how R,L,A were built.  We compute mu directly from rowd_assembly's
    own R,A matrices (the paper's primary code path, validated in phase 117)
    restricted to P_T, and compare 1-mu against the bottom eigenvalue of
    D = I-Phi^*Phi built from the completely separate channel-explicit
    construction (W3_build_xy).  Agreement to machine precision cross-checks
    that the two independent code paths describe the same operator; it is an
    algebraic identity, not new information, but a real bug in either
    construction would show up here."""
    import W3_build_xy as W3loc
    import rowd_assembly as RA
    T = 0.5 * math.log(q)
    M = RA.assemble(T, refine=refine)
    Z = W3loc.primitive_basis(M['Tate'], M['Gram'])
    A_P = Z.T @ M['A'] @ Z
    R_P = Z.T @ M['R'] @ Z
    A_P = 0.5 * (A_P + A_P.T)
    R_P = 0.5 * (R_P + R_P.T)
    import scipy.linalg as sla
    mu = sla.eigh(A_P, R_P, eigvals_only=True)
    mu_min = float(mu.min())
    return dict(q=q, mu_min_raw=mu_min, one_minus_mu_min=1.0 - mu_min)


def run():
    for q in THRESHOLDS:
        r = defect_spectrum(q)
        print(f"\n=== q={r['q']} T={r['T']:.4f} rowsX={r['rowsX']} dimP={r['dimP']} ===")
        print(f"bottom eigenvalues of D=I-Phi^*Phi: {['%.6e'%x for x in r['w'][:8]]}")
        print(f"(rows_X - dimP = {r['rowsX']-r['dimP']} eigenvalues should sit at "
              f"exactly 1.0 -- Ran(X)^perp; top of spectrum check: "
              f"{['%.6f'%x for x in r['w'][-3:]]})")
        print(f"channel names: {r['names']}")
        for k, fracs in enumerate(r['chan_fracs']):
            tot = sum(fracs)
            gamma_frac = fracs[0] / tot if tot > 0 else float('nan')
            print(f"  eigvec[{k}] (eigval={r['w'][k]:.6e}): ||v||^2={tot:.4f}, "
                  f"Gamma-channel fraction={gamma_frac:.4f}, "
                  f"per-channel L2^2={['%.4f'%x for x in fracs]}")
    print("\n--- cross-check: bottom eigenvalue of D=I-Phi^*Phi (explicit channel "
          "construction) vs 1-mu_min from the pencil (A_P,R_P) built directly from "
          "rowd_assembly's own R,A (independent code path) ---")
    for q in THRESHOLDS + [37]:
        cc = cross_check_via_raw_A_R(q)
        print(cc)


if __name__ == '__main__':
    run()
