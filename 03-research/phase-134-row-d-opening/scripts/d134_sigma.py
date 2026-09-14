"""Phase 134: the Schur complement Sigma(T) of P124.013 (2.4), in the NAMED
Tate basis (phi_+, phi_-), phi_sigma(t) = e^{sigma t/2} 1_{I_T}.

Reuses phase-124's laboratory `p124_lab.py` unchanged for the assembly.
Three things are measured, none of them a proof:

  (1) the SWAP LAW.  The reflection R: F(t) -> F(-t) preserves I_T, preserves
      the Weil form (W_fin is symmetric, K(|t|) is even, the polar packet is
      symmetric) and preserves the primitive space, while exchanging
      phi_+ <-> phi_-.  Hence Sigma(T) must commute with the swap sigma of
      Paper 45 Remark 8.2, i.e. Sigma(T) must be a symmetric 2x2 matrix with
      EQUAL DIAGONAL ENTRIES, eigenvectors (1,1) (even) and (1,-1) (odd).
      This is Theorem D.2(b) of Paper 46; the script only checks it.

  (2) The Tate BLOCK -- written frak-B_T in Paper 46, NOT B_T, which there
      denotes Paper 45 Thm 8.1's ruling plane -- is not the hyperbolic Tate
      plane.  The hyperbolic form is the POLAR packet alone; the block is
      polar + <A_T phi_.,phi_.> and has no predetermined signature.  Printed.

  (3) MONOTONICITY of lambda_min Sigma(T) in T: measured, not proved (the
      border vectors phi_sigma^{(T)} themselves move with T, so the usual
      Schur monotonicity argument does not apply).

VARIATIONAL CAVEAT (Paper 46 Warning 4.5a).  This script uses p124_lab's
piecewise-constant Galerkin space, which is a SUBSPACE of the test space.
lambda_min(L_T) is a Rayleigh minimum over that subspace and Sigma_T(z) is
itself an infimum over P_T, so BOTH are variational UPPER bounds: a negative
computed value certifies a genuine direction, a positive one certifies
NOTHING.  Only the swap defect (an identity check) and the sign of det(block)
(assembled from exact integrals) are used for anything in Paper 46.

NUMERICS ILLUSTRATE AND FALSIFY.  THEY PROVE NOTHING.
"""
import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.normpath(os.path.join(HERE, "..", "..",
                                    "phase-124-direct-first-contact", "scripts"))
sys.path.insert(0, LAB)
import p124_lab as lab            # noqa: E402


def named_blocks(asm):
    """L, X, B in the NAMED border basis: the rows of asm['Tate'] are the
    coefficient vectors of M_u, and their Gram representers are the phi_u."""
    Gram, W, A, Tate = asm['Gram'], asm['W'], asm['A'], asm['Tate']
    Z = lab.primitive_basis(Tate, Gram)
    Y = np.linalg.solve(Gram, Tate.T)        # columns = phi_u in the cell basis
    L = Z.T @ A @ Z
    L = 0.5 * (L + L.T)
    X = Z.T @ W @ Y
    B = Y.T @ W @ Y
    return 0.5 * (L + L.T), X, 0.5 * (B + B.T), asm['us']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="zeta", choices=["zeta", "xi_a"])
    ap.add_argument("--a", type=float, default=0.35)
    ap.add_argument("--refine", type=int, default=2)
    ap.add_argument("--tmin", type=float, default=0.72)
    ap.add_argument("--tmax", type=float, default=2.2)
    ap.add_argument("--steps", type=int, default=12)
    args = ap.parse_args()

    model = lab.model_zeta() if args.model == "zeta" else lab.model_xi_a(args.a)
    print("model = %s   (border order: u = %s)" % (model.name, "see below"))
    prev = None
    for T in np.linspace(args.tmin, args.tmax, args.steps):
        asm = lab.assemble(model, float(T), refine=args.refine)
        L, X, B, us = named_blocks(asm)
        S, kern, lminL, nsmall = lab.schur(L, X, B)
        evS = np.linalg.eigvalsh(S)
        # swap check: the reflection pairs u with -u; with us ordered
        # [+u_1..+u_k, -u_1..-u_k], the swap is the block exchange.
        k = len(us) // 2
        P = np.zeros((2 * k, 2 * k))
        P[:k, k:] = np.eye(k)
        P[k:, :k] = np.eye(k)
        swap_def = float(np.abs(P @ S @ P - S).max()) / max(np.abs(S).max(), 1e-300)
        mono = "" if prev is None else ("  d(lam_min)=%+.3e" % (evS.min() - prev))
        prev = evS.min()
        print("T=%.4f dimP=%3d lam_min(L)=%+.4e |Pi_ker X|=%.1e "
              "lam_min(Sigma)=%+.4e  swap_defect=%.2e%s"
              % (T, L.shape[0], lminL, kern, evS.min(), swap_def, mono))
        if abs(T - args.tmin) < 1e-12:
            np.set_printoptions(precision=5, suppress=False)
            print("   us = %s" % (us,))
            print("   frak-B_T (the Tate BLOCK, not the ruling plane) =\n%s" % (B,))
            print("   Sigma(T) =\n%s" % (S,))
    print("\nNumerics illustrate and falsify; they prove nothing.")


if __name__ == "__main__":
    main()
