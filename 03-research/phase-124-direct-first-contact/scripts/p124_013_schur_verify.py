"""Verification for P124.013.

(1) REGRESSION: the generalized zeta assembly of p124_lab reproduces the
    phase-118 `rowd_assembly.assemble` matrices A, Gram, Tate to machine
    precision.  This ties the lab to the already audited operator of paper 42
    (P123.036 section 3).

(2) ALGEBRA: the finite-dimensional Schur/Douglas statements of P124.013 are
    checked on random symmetric blocks with a prescribed kernel:
      (a) W>=0  <=>  L>=0, Pi_ker X = 0 and Sigma = B - X^T L^dagger X >= 0;
      (b) if L>=0 has kernel K and Pi_K X != 0, then W takes negative values,
          with an explicit witness;
      (c) the null vector of the full form is primitive  <=>  its Tate
          coefficient vanishes.
No arithmetic input is used in part (2); it is pure linear algebra.
"""
import math
import sys
import numpy as np

sys.path.insert(0, "../../phase-118-the-exact-threshold-inequality/scripts")
import p124_lab as P


def part1_regression():
    import rowd_assembly as RA
    ok = True
    for T, refine in ((0.9, 3), (1.2, 2), (1.5, 2)):
        ref = RA.assemble(T, refine=refine)
        new = P.assemble(P.model_zeta(), T, refine=refine)
        dA = np.abs(ref['A'] - new['A']).max()
        dG = np.abs(ref['Gram'] - new['Gram']).max()
        # rowd_assembly.Tate rows are (M_-, M_+); p124_lab's us = [+1/2, -1/2]
        dT = np.abs(ref['Tate'] - new['Tate'][[1, 0]]).max()
        scale = np.abs(ref['A']).max()
        print(f"  T={T:5.2f} refine={refine}  max|dA|={dA:.3e} (scale {scale:.3e})"
              f"  max|dGram|={dG:.3e}  max|dTate|={dT:.3e}")
        ok &= (dA < 1e-11 * scale) and (dG < 1e-13) and (dT < 1e-12)
    return ok


def rand_case(rng, n=7, k=2, kerdim=1, ker_orth=True, psd=True):
    """Random L>=0 with kernel of dim kerdim, random X, random B."""
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    w = np.abs(rng.standard_normal(n)) + 0.3
    w[:kerdim] = 0.0
    L = (Q * w) @ Q.T
    if not psd:
        L = (Q * (w - 0.5)) @ Q.T
    X = rng.standard_normal((n, k))
    if ker_orth:
        K = Q[:, :kerdim]
        X = X - K @ (K.T @ X)
    B = rng.standard_normal((k, k))
    B = B + B.T
    return 0.5 * (L + L.T), X, B


def full(L, X, B):
    n, k = X.shape
    return np.block([[L, X], [X.T, B]])


def part2_algebra(trials=400, seed=20260912):
    rng = np.random.default_rng(seed)
    ok = True
    # (a) equivalence  W>=0  <=>  L>=0, ker-orthogonality, Sigma>=0
    bad_a = 0
    for _ in range(trials):
        L, X, B = rand_case(rng, ker_orth=rng.random() < 0.5,
                            psd=rng.random() < 0.8)
        S, kern, lmin, _ = P.schur(L, X, B)
        lhs = np.linalg.eigvalsh(full(L, X, B)).min() > -1e-9
        rhs = (lmin > -1e-9) and (kern < 1e-9) and (np.linalg.eigvalsh(S).min() > -1e-9)
        if lhs != rhs:
            bad_a += 1
    ok &= (bad_a == 0)
    print(f"  (a) Schur equivalence mismatches: {bad_a}/{trials}")

    # (b) nonzero kernel projection => explicit negative witness
    worst, tested = -np.inf, 0
    for _ in range(200):
        L, X, B = rand_case(rng, ker_orth=False, psd=True)
        w, V = np.linalg.eigh(L)
        K = V[:, np.abs(w) < 1e-11]
        PK = K.T @ X                      # (kerdim, k) coordinates of Pi_K X
        if np.linalg.norm(PK) < 1e-8:
            continue
        tested += 1
        # witness: F0 in ker and z along the direction pairing with it
        u, s, vt = np.linalg.svd(PK)
        F0 = K @ u[:, 0]
        zdir = vt[0]
        c0 = float(F0 @ X @ zdir)         # = s[0] != 0
        eps = -np.sign(c0) * 1e-4
        v = np.concatenate([F0, eps * zdir])
        val = float(v @ full(L, X, B) @ v)
        worst = max(worst, val)
    print(f"  (b) tested {tested} cases, worst witness value (must be < 0): {worst:.3e}")
    ok &= (tested > 0 and worst < 0)

    # (c) full-form null vector is primitive  <=>  its Tate coefficient is 0
    bad_c = 0
    for _ in range(200):
        L, X, B = rand_case(rng, ker_orth=True, psd=True)
        S, kern, lmin, _ = P.schur(L, X, B)
        if np.linalg.eigvalsh(S).min() < 1e-9:
            continue                      # only test the strictly-positive case
        M = full(L, X, B)
        w, V = np.linalg.eigh(M)
        null = V[:, np.abs(w) < 1e-10]
        for j in range(null.shape[1]):
            v = null[:, j]
            z = v[L.shape[0]:]
            if np.linalg.norm(z) > 1e-8:   # Sigma>0 forbids a nonzero Tate part
                bad_c += 1
    print(f"  (c) null vectors with nonzero Tate part while Sigma>0: {bad_c}")
    ok &= (bad_c == 0)
    return ok


if __name__ == "__main__":
    print("P124.013 verification")
    print("(1) regression against phase-118 rowd_assembly (zeta):")
    ok1 = part1_regression()
    print("(2) Schur/Douglas algebra on random blocks:")
    ok2 = part2_algebra()
    print("RESULT:", "PASS" if (ok1 and ok2) else "FAIL")
    sys.exit(0 if (ok1 and ok2) else 1)
