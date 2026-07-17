"""
E96 — is the V_+ positivity an EULER (multiplicativity) comparison? (Phase 62, MW-5 crossing).

E95: A|V+ PSD for zeta is intrinsic (no cancellation), gapless cascade rate ~1.40 (lambda-indep);
DH has genuine negatives. Since A = Larch - Lprime and the ARCHIMEDEAN part Larch is the SAME
gamma-factor for zeta and DH, the entire zeta-vs-DH difference is in Lprime|V+. So the crossing
question sharpens to a COMPARISON OF FORMS on V_+:

    A|V+ >= 0   <=>   Larch|V+  >=  Lprime|V+   (as Hermitian forms on V_+).

If for zeta  Lprime^zeta|V+ <= Larch|V+  but for DH  Lprime^DH|V+ does NOT,
then the EULER PRODUCT (multiplicativity of zeta's coefficients, absent in DH) is what bounds the
prime form below the archimedean form. That would be a zero-FREE mechanism (it only uses the
coefficients), i.e. a genuine crossing candidate. cf. [[riemann-phase61-euler-mechanism]].

Tests:
  (0) confirm Larch is identical for zeta and DH.
  (1) spectra of Larch|V+, Lprime^zeta|V+, Lprime^DH|V+ (PSD? sign?).
  (2) generalized eigenvalues of (Lprime|V+, Larch|V+): mu_k = solve Lprime x = mu Larch x.
      A|V+ >= 0  <=>  max_k mu_k <= 1.  Report max mu for zeta vs DH.
      The crossing hope: max mu_zeta <= 1 provable from |a_n|<=Lambda(n) Euler bound; max mu_DH > 1.
Honesty: dps>=40; no proof; report verbatim; DH mandatory.
"""
import os, sys, numpy as np, mpmath as mp
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61); os.chdir(_P61)
from engine_cache import get_matrices
import scipy.linalg as sla
import E94_Jcompat as e94

mp.mp.dps = 40


def to_np(M, dim):
    return np.array([[float(M[i, j]) for j in range(dim)] for i in range(dim)])


def vplus_project(Mat1, J1):
    w, V = np.linalg.eig(J1)
    P = V[:, [k for k in range(len(w)) if w[k].imag > 0.5]]
    H = P.conj().T @ Mat1 @ P
    return (H + H.conj().T) / 2


def kb(M, idx):
    z = idx.index(0); keep = [i for i in range(len(idx)) if i != z]
    return M[np.ix_(keep, keep)]


def run(lam, N):
    Laz, Lpz, Az, L, idx = get_matrices(lam, N, 'zeta', dps=40)
    Lad, Lpd, Ad, _, idxd = get_matrices(lam, N, 'DH', dps=40)
    dim = len(idx)
    J = e94.Jmat(idx); J1 = kb(J, idx)
    Laznp, Ladnp = to_np(Laz, dim), to_np(Lad, dim)
    arch_diff = np.max(np.abs(Laznp - Ladnp))
    # project to V_+
    LaP = vplus_project(kb(Laznp, idx), J1)
    LpzP = vplus_project(kb(to_np(Lpz, dim), idx), J1)
    LpdP = vplus_project(kb(to_np(Lpd, dim), idx), J1)
    # spectra
    def sig(H):
        ev = np.linalg.eigvalsh(H)
        return (int((ev > 1e-12).sum()), int((np.abs(ev) <= 1e-12).sum()), int((ev < -1e-12).sum()))
    # generalized eigenvalues Lprime x = mu Larch x on the well-conditioned subspace of Larch
    # (Larch|V+ is itself cascade-singular; restrict to its top eigenspace where it is PD)
    def maxmu(LpP, tol=1e-6):
        wa, Ua = np.linalg.eigh(LaP)
        good = wa > tol * wa.max()           # subspace where Larch is safely PD
        U = Ua[:, good]; Da = wa[good]
        Lp_r = U.conj().T @ LpP @ U
        Larch_r = np.diag(Da)
        evals = sla.eigvalsh(Lp_r, Larch_r)
        return float(np.max(evals.real)), int(good.sum())
    muz_max, kz = maxmu(LpzP)
    mud_max, kd = maxmu(LpdP)
    print(f"\nlam={lam} N={N} dim={dim}  (Larch zeta==DH? max|diff|={arch_diff:.1e})")
    print(f"  sig Larch|V+      (p,0,n) = {sig(LaP)}")
    print(f"  sig Lprime^zeta|V+        = {sig(LpzP)}    sig Lprime^DH|V+ = {sig(LpdP)}")
    print(f"  sig A^zeta|V+             = {sig(LaP-LpzP)}    sig A^DH|V+      = {sig(LaP-LpdP)}")
    print(f"  GEN-EIG mu on Larch-PD subspace (k={kz}):  A|V+>=0 <=> max mu <=1")
    print(f"    zeta: max mu = {muz_max:+.4f}   {'OK PSD' if muz_max<=1+1e-3 else 'VIOLATED'}")
    print(f"    DH  : max mu = {mud_max:+.4f}   {'OK PSD' if mud_max<=1+1e-3 else 'VIOLATED (off-line)'}")
    return muz_max, mud_max


if __name__ == '__main__':
    grid = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E96 — V_+ positivity as Euler comparison Larch|V+ >= Lprime|V+ ; max mu <=1 <=> PSD")
    Z, D = [], []
    for lam, N in grid:
        z, d = run(lam, N); Z.append(z); D.append(d)
    print(f"\nSUMMARY  max mu over lam:  zeta in [{min(Z):.4f},{max(Z):.4f}]   DH in [{min(D):.4f},{max(D):.4f}]")
    print(f"  zeta {'stays <=1 (PSD, Euler-bounded)' if max(Z)<=1+1e-6 else 'exceeds 1'};  "
          f"DH {'exceeds 1 (off-line breaks comparison)' if max(D)>1+1e-6 else 'stays <=1'}")
