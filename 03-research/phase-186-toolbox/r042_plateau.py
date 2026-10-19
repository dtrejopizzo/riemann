#!/usr/bin/env python3
"""R186_042 — Plateau of the pencil (Neg_T, Pos_T)|P_T: constant-weight models, components of the negative
set and exact formula in the eigenbasis of Neg.  Self-contained (imports r034_det: Legendre Galerkin).

For each window T:
  (1) components J_i of U = {sigma_T < 0}; prints 2c_i = T|J_i| (standard c_i = T|J_i|/2), N_i = 2c_i/pi, S_U = R 1_U(D) R (indicator),
      lambda_j(S_U), 1 - lambda_0(S_U), comparison with a single interval of the same measure;
  (2) pencil models on P_T:
        REAL : (Neg, Pos)                 true sigma_- and sigma_+
        M0   : (s_- S_U, s_+ (1 - S_U))   constant weights (commute in L^2(I_T)): beta_j = (s_-/s_+) lam_j/(1-lam_j)
        M2   : (Neg, s_+ (1 - S_U))       real sigma_-, constant sigma_+
        M3   : (s_- S_U, Pos)             constant sigma_-, real sigma_+
      s_- := tr Neg / tr S_U, s_+ := tr Pos_M / tr(1 - S_U)_M (equal Galerkin traces);
  (3) check of Thm 2.2: beta_j of the pencil = eigenvalues of (diag nu, P) with P_kl = <phi_k, Pos phi_l>
      in the eigenbasis of Neg;
  (4) subspace of modulated exponentials at the component centers: lambda_min(a_T|span)/lambda_A.
Usage: python3 r042_plateau.py [M=40]
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import r034_det as R

def build_ind(T, M, comps, nq=200):
    """S_U = R 1_U(D) R in the Legendre basis (U symmetric: comps at tau>0)."""
    xg, wg = NL.leggauss(nq); S = np.zeros((M, M))
    for lo, hi in comps:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        S += np.einsum('klt,t->kl', R.fhat(T, M, t), w) / np.pi
    return S

def pencil(NP, PP):
    L = np.linalg.cholesky(PP); Li = np.linalg.inv(L); B = Li @ NP @ Li.T
    return np.sort(np.linalg.eigvalsh((B + B.T) / 2))[::-1]

def stair(beta, k=6):
    b = beta[:k]; g = 1 - b
    return ["%.2e" % x for x in g], ["%.2f" % d for d in np.diff(-np.log(np.abs(g)))] if np.all(g > 0) else "(beta>1)"

def run(T, M):
    A, A0, ta, tb = R.build_x(T, M, 400)
    comps, zs = R.neg_set(T)
    Neg = R.build_neg(T, M, comps); Pos = A + Neg
    SU = build_ind(T, M, comps)
    Z = R.null_basis([ta, tb])
    lamS = np.sort(np.linalg.eigvalsh(SU))[::-1]
    meas = sum(b - a for a, b in comps); NSh = 2 * T * 2 * meas / (2 * np.pi)
    # single interval of the same total measure (2*meas in R): [-meas, meas]
    S1 = build_ind(T, M, [(0.0, meas)]); lam1 = np.sort(np.linalg.eigvalsh(S1))[::-1]
    print(f"\n=== T = {T:.5f}  M = {M}  contacts {[n for n,_ in R.contacts(T)]}  #comp = {len(comps)}  |U+| = {meas:.3f}  N_Sh = {NSh:.3f} (tr S_U = {np.trace(SU):.3f})")
    ci = [T * (b - a) for a, b in comps]
    print("  components: " + ", ".join(f"[{a:.2f},{b:.2f}] c={c:.2f} N={c/np.pi:.2f} s_max={(-R.sigma_T(T, np.linspace(a,b,201))).max():.2f}" for (a, b), c in zip(comps, ci)))
    print(f"  lambda_j(S_U) = {np.round(lamS[:10], 4).tolist()}  #>1/2 = {(lamS>0.5).sum()}   1-lambda_0 = {1-lamS[0]:.3e}")
    print(f"  single interval, c = {T*meas:.2f}: lambda_0 = {lam1[0]:.6f}, 1-lambda_0 = {1-lam1[0]:.3e}  (Slepian 4 sqrt(pi) c^(1/2) e^(-2c) = {4*np.sqrt(np.pi)*np.sqrt(T*meas)*np.exp(-2*T*meas):.3e});  #>1/2 = {(lam1>0.5).sum()}")
    s_m = np.trace(Neg) / np.trace(SU); s_p = np.trace(Pos) / np.trace(np.eye(M) - SU)
    print(f"  s_- = tr Neg/tr S_U = {s_m:.3f}   s_+ = tr Pos_M/tr(1-S_U)_M = {s_p:.3f}   umbral s_+/(s_+ + s_-) = {s_p/(s_p+s_m):.3f}")
    models = {'REAL': (Neg, Pos), 'M0': (s_m * SU, s_p * (np.eye(M) - SU)), 'M2': (Neg, s_p * (np.eye(M) - SU)), 'M3': (s_m * SU, Pos)}
    out = {}
    for name, (N_, P_) in models.items():
        NP, PP = Z.T @ N_ @ Z, Z.T @ P_ @ Z
        if np.linalg.eigvalsh(PP)[0] <= 0: print(f"  {name}: Pos not positive definite on P_T"); continue
        beta = pencil(NP, PP); lamA = np.linalg.eigvalsh(Z.T @ (P_ - N_) @ Z)[0]
        g, d = stair(beta)
        print(f"  {name:4s}: beta_max = {beta[0]:.8f}  1-beta_max = {1-beta[0]:+.3e}  #beta>1 = {(beta>1).sum()}  lambda_min(Pos-Neg|P) = {lamA:+.3e}  1-beta_j = {g}  steps = {d}")
        out[name] = beta
    # M0 closed formula in L^2(I_T)
    b0 = (s_m / s_p) * lamS / (1 - lamS)
    print(f"  M0 in L2 (closed form): beta_j = (s_-/s_+) lam_j/(1-lam_j) = {np.round(b0[:6], 4).tolist()}  vs Galerkin L2 {np.round(pencil(s_m*SU, s_p*(np.eye(M)-SU))[:6], 4).tolist()}")
    # Thm 2.2: eigenbasis of Neg
    nu, Phi = np.linalg.eigh(Neg); Pm = Phi.T @ Pos @ Phi
    ZP = Phi.T @ Z                       # P_T in the eigencoordinates of Neg
    beta22 = pencil(ZP.T @ np.diag(nu) @ ZP, ZP.T @ Pm @ ZP)
    print(f"  Thm 2.2 (pencil (diag nu, P) in the eigenbasis of Neg): 1-beta_max = {1-beta22[0]:.4e}  (direct {1-out['REAL'][0]:.4e});  nu_j(Neg) = {np.round(np.sort(nu)[::-1][:5],4).tolist()}  s_- lam_j(S_U) = {np.round(s_m*lamS[:5],4).tolist()}  Neg<=s_max S_U: ok")
    # (4) modulated exponentials at the centers
    xg, wg = NL.leggauss(2 * M); y = T * xg; w = T * wg; F = R.legbasis(T, M, y)
    cols = []
    for a, b in comps:
        tc = (a + b) / 2
        cols.append((F * w) @ np.cos(tc * y)); cols.append((F * w) @ np.sin(tc * y))
    E = np.array(cols).T                                    # Legendre coordinates of e^{±i tc x} (Galerkin projection)
    E = Z @ (Z.T @ E)                                       # projection onto P_T
    q, _ = np.linalg.qr(E); q = q[:, :np.linalg.matrix_rank(E)]
    AE = q.T @ A @ q; PE = q.T @ Pos @ q
    lamE = np.linalg.eigvalsh(AE)[0]; lamA = out['REAL']
    print(f"  span{{e^(±i tau_i x)}} ∩ P_T (dim {q.shape[1]}): lambda_min(a_T|span) = {lamE:+.3e}  vs lambda_A = {np.linalg.eigvalsh(Z.T@A@Z)[0]:+.3e};  1-beta_max|span = {1-pencil(q.T@Neg@q, PE)[0]:+.3e}")


if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    for T in (0.62, np.log(2), 0.75, 0.5 * np.log(5), 0.85):
        run(T, M)

# ---------------- extensions (round 19): per-component steps and well-resolved S_U ----------------
def build_form(T, M, pieces, nq=200):
    """(1/pi) int_0^oo f(tau) phi^_k phi^_l over pieces [(lo,hi,f)] with f callable or constant."""
    xg, wg = NL.leggauss(nq); out = np.zeros((M, M))
    for lo, hi, f in pieces:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        v = f(t) if callable(f) else f * np.ones_like(t)
        out += np.einsum('klt,t->kl', R.fhat(T, M, t), v * w) / np.pi
    return out

def step_models(T, M):
    """M2': sigma_+ -> mean per positive component on [0, tau_last]; M3': sigma_- -> mean per component; M23': both."""
    A, A0, ta, tb = R.build_x(T, M, 400); comps, zs = R.neg_set(T)
    Neg = R.build_neg(T, M, comps); Pos = A + Neg; Z = R.null_basis([ta, tb])
    pos_comps = [(comps[i][1], comps[i + 1][0]) for i in range(len(comps) - 1)]
    sp = lambda t: R.sigma_T(T, t); sm = lambda t: -R.sigma_T(T, t)
    mean = lambda f, lo, hi: f(np.linspace(lo, hi, 2001)).mean()
    Pos_in = build_form(T, M, [(lo, hi, sp) for lo, hi in pos_comps])
    Pos_st = build_form(T, M, [(lo, hi, mean(sp, lo, hi)) for lo, hi in pos_comps])
    Neg_st = build_form(T, M, [(lo, hi, mean(sm, lo, hi)) for lo, hi in comps])
    models = {"M2'": (Neg, Pos - Pos_in + Pos_st), "M3'": (Neg_st, Pos), "M23'": (Neg_st, Pos - Pos_in + Pos_st)}
    print(f"\n--- per-component steps, T = {T:.5f}, M = {M}: sigma_- levels = {[round(mean(sm,lo,hi),3) for lo,hi in comps]}")
    print(f"    sigma_+ levels between components = {[round(mean(sp,lo,hi),3) for lo,hi in pos_comps]}")
    for name, (N_, P_) in models.items():
        NP, PP = Z.T @ N_ @ Z, Z.T @ P_ @ Z
        beta = pencil(NP, PP); g, d = stair(beta)
        print(f"  {name:4s}: beta_max = {beta[0]:.6f}  1-beta_max = {1-beta[0]:+.3e}  #beta>1 = {(beta>1).sum()}  1-beta_j = {g}")

def SU_resolved(T, Mfac=1.3):
    comps, zs = R.neg_set(T, tmax=400.0)
    tmax = comps[-1][1]; M = int(Mfac * T * tmax) + 30
    S = np.zeros((M, M)); xg, wg = NL.leggauss(120)
    for lo, hi in comps:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        S += np.einsum('klt,t->kl', R.fhat(T, M, t), w) / np.pi
    lam = np.sort(np.linalg.eigvalsh(S))[::-1]; meas = sum(b - a for a, b in comps)
    Ni = [T * (b - a) / np.pi for a, b in comps]
    print(f"\n--- resolved S_U: T = {T:.4f}  M = {M}  #comp = {len(comps)}  tau_last = {tmax:.1f}  N_Sh = {2*T*meas/np.pi:.2f}  tr = {np.trace(S):.2f}  N_i: max {max(Ni):.2f} mean {np.mean(Ni):.2f}")
    print(f"    lambda_j(S_U) = {np.round(lam[:12],4).tolist()}  #>1/2 = {(lam>0.5).sum()}  #>0.9 = {(lam>0.9).sum()}  1-lambda_0 = {1-lam[0]:.3e}")

if __name__ == '__main__' and len(sys.argv) > 2 and sys.argv[2] == 'ext':
    for T in (0.75, 0.5 * np.log(5)): step_models(T, int(sys.argv[1]))
    for T in (0.5 * np.log(5), 0.85, 0.9, 1.0): SU_resolved(T)
