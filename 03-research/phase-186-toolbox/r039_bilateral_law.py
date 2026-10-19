# R186_039 — bilateral law: which Shannon number governs λ_A?  (self-contained; reuses r034_det.py)
# python3 r039_bilateral_law.py [M=40]
# For a grid of windows T it computes: λ_A (Legendre Galerkin, variational upper bound), N_Sh = Shannon number
# of the negative set {σ_T<0}, N(T*) = #zeros of ζ with γ ≤ T* = 2π e^{2T} (Zhu), #β_j of the pencil (Neg,Pos)|𝒫_T
# at distance < 1e-3 from 1, the Rayleigh quotient of 𝔞_T on the first prolate of the negative set projected
# onto 𝒫_T ("Landau–Widom leading term" model), and fits of −log λ_A against four candidate laws.
import sys, numpy as np
from numpy.polynomial import legendre as NL
import r034_det as R

GAMMA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
         52.970321, 56.446248, 59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158, 75.704691, 77.144840]

def prolate(T, M, comps, nq=200):
    """S = R_T 1_{neg}(D) R_T (symbol 1 on the negative set): multi-interval time-band eigenvalues."""
    xg, wg = NL.leggauss(nq); S = np.zeros((M, M))
    for lo, hi in comps:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        S += np.einsum('klt,t->kl', R.fhat(T, M, t), w) / np.pi
    return S

def window(T, M, nu=400):
    A, A0, ta, tb = R.build_x(T, M, nu)
    comps, zs = R.neg_set(T)
    N = R.build_neg(T, M, comps); Pos = A + N
    Z = R.null_basis([ta, tb]); AP, NP, PP = Z.T @ A @ Z, Z.T @ N @ Z, Z.T @ Pos @ Z
    evA, VA = np.linalg.eigh(AP); lamA = evA[0]
    Lc = np.linalg.cholesky(PP); Li = np.linalg.inv(Lc); beta = np.linalg.eigvalsh(Li @ NP @ Li.T)
    meas = sum(b - a for a, b in comps); NSh = 2 * T * 2 * meas / (2 * np.pi)
    Tstar = 2 * np.pi * np.exp(2 * T); NZ = sum(g <= Tstar for g in GAMMA)
    # prolates of the negative set and the "leading term" model
    S = prolate(T, M, comps); lam, U = np.linalg.eigh(S); lam, U = lam[::-1], U[:, ::-1]
    u0 = Z.T @ U[:, 0]; u0 /= np.linalg.norm(u0)             # first prolate projected onto P_T (orthonormal Legendre coordinates)
    ray0 = u0 @ AP @ u0; neg0 = u0 @ NP @ u0; pos0 = u0 @ PP @ u0
    k = int(np.ceil(NSh))                                   # projected Shannon subspace
    Uk = np.linalg.qr(Z.T @ U[:, :k])[0]
    evk = np.linalg.eigvalsh(Uk.T @ AP @ Uk)
    return dict(T=T, lamA=lamA, nextA=evA[1:4], NSh=NSh, NZ=NZ, Tstar=Tstar, meas=meas, ncomp=len(comps),
                beta=beta[::-1], near=int((1 - beta < 1e-3).sum()), prol=lam[:k + 3], ray0=ray0, neg0=neg0, pos0=pos0,
                k=k, evk=evk, nminus=int((evA < 0).sum()))

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    Ts = [0.36, 0.45, 0.5 * np.log(3), 0.62, np.log(2), 0.75, 0.5 * np.log(5)]
    rows = []
    for T in Ts:
        r = window(T, M); rows.append(r)
        print(f"\n=== T = {T:.4f}  M = {M}  contacts {[n for n,_ in R.contacts(T)]}  negative comps. = {r['ncomp']}  |{{σ<0}}| = {r['meas']:.3f}")
        print(f"  λ_A = {r['lamA']:+.3e}  (next {np.array2string(r['nextA'], precision=2)})   n_-(𝔞|P) = {r['nminus']}")
        print(f"  N_Sh = {r['NSh']:.2f}   T* = {r['Tstar']:.2f}   N(T*) = {r['NZ']}   #β a <1e-3 de 1 = {r['near']}   1-β: {np.array2string(1-r['beta'][:5], precision=2)}")
        print(f"  prolates of the negative set λ_j: {np.array2string(r['prol'], precision=4)}")
        print(f"  first prolate projected onto P_T: 𝔞_T(u0) = {r['ray0']:+.3f} = Pos {r['pos0']:.3f} − Neg {r['neg0']:.3f}   (LW model: Neg≈s_-, Pos≈0 ⇒ negative)")
        print(f"  𝔞_T on the projected Shannon subspace (dim {r['k']}): eigenvalues {np.array2string(r['evk'], precision=3)}")
    print("\n=== Fits  −log λ_A = a·X + b  (least squares; 7 windows; max relative residual in −log λ_A)")
    y = np.array([-np.log(r['lamA']) for r in rows])
    cands = {'N_Sh': np.array([r['NSh'] for r in rows]),
             'N_Sh·log N_Sh': np.array([r['NSh'] * np.log(max(r['NSh'], 1.0001)) for r in rows]),
             'e^{2T}': np.array([np.exp(2 * r['T']) for r in rows]),
             'N(T*)·2T (≈ Zhu, N≤4: log N not usable)': np.array([r['NZ'] * 2 * r['T'] for r in rows]),
             'T e^{2T²} (Gaussian heuristic for |{σ<0}|)': np.array([r['T'] * np.exp(2 * r['T'] ** 2) for r in rows])}
    print("   T:        " + "  ".join(f"{r['T']:.3f}" for r in rows)); print("   −log λ_A: " + "  ".join(f"{v:5.1f}" for v in y))
    for name, X in cands.items():
        A = np.vstack([X, np.ones_like(X)]).T; (a, b), res, *_ = np.linalg.lstsq(A, y, rcond=None)
        pred = a * X + b; print(f"   {name:48s} a = {a:7.3f}  b = {b:7.2f}  max resid = {np.abs(pred-y).max():5.2f}  rel = {(np.abs(pred-y)/y).max():.2f}")
    print("   N(T*) vs #β≈1: " + "  ".join(f"{r['NZ']}/{r['near']}" for r in rows))
    print("   N_Sh:          " + "  ".join(f"{r['NSh']:.1f}" for r in rows))
