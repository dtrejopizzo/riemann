"""
E101 — Task B (Connes route): relative determinant / spectral shift vs a no-oscillation model.

Connes: replace the (impossible) finite-window GAP by a relative determinant
   D_lambda(z) = det_2( (I - z K_lambda)(I - z K_lambda^0)^{-1} ),
finite part at z=1; predict ZETA bounded, DH drift ~ lambda^{2 beta - 1}.

Implementation via the GENERALIZED spectrum (handles L_arch not being PD): the natural
normalization is the generalized eigenproblem  L_prime x = mu L_arch x  (E96: mu_max=1 for zeta).
The relative finite part is
   S_lambda(eps) = sum_j [ log|1 - mu_j + eps| - log|1 - mu_j^0 + eps| ],
where mu_j are the arithmetic generalized eigenvalues and mu_j^0 those of the NO-OSCILLATION model
L_prime^0 (von Mangoldt Lambda(n) replaced by the smooth PNT density: sum over ALL integers n>=2
with weight n^{-1/2}, same main term, no prime/zero fluctuation).

  ZETA: S_lambda should stay BOUNDED in lambda (no off-line pole).
  DH  : S_lambda should DRIFT (its off-line zero is a pole at 2 beta-1 > 0).
Honesty: dps>=40 for the matrices; generalized eig via scipy (complex allowed); DH mandatory.
"""
import os, sys, numpy as np, mpmath as mp
import scipy.linalg as sla
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61); os.chdir(_P61)
from engine_cache import get_matrices
import engine_cache as ec

mp.mp.dps = 40


def to_np(M, dim):
    return np.array([[float(M[i, j]) for j in range(dim)] for i in range(dim)])


def Lprime_smooth(lam, N):
    """no-oscillation model: Lambda(n) -> 1 over ALL integers n>=2 (smooth PNT density, no zeros)."""
    L = float(2 * mp.log(mp.mpf(lam))); idx = list(range(-N, N + 1)); dim = len(idx)
    mx = int(lam * lam)
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            q = ec.q_func(idx[a], idx[b], L)          # same window kernel as the engine
            s = mp.mpf(0)
            for nn in range(2, mx + 1):
                s += (mp.mpf(nn) ** mp.mpf('-0.5')) * q(mp.log(nn))
            M[a, b] = s; M[b, a] = s
    return to_np(M, dim)


def gen_mu(Lp, La):
    """generalized eigenvalues of L_prime x = mu L_arch x (L_arch indefinite -> use sla.eig)."""
    w = sla.eig(Lp, La, right=False)
    return w[np.isfinite(w)]


def edge_excess(mu):
    """mass of the spectrum PAST the contractive edge mu=1 = the off-line poles (Connes finite part
    localized at z=1). Real part beyond 1 + any imaginary part (complex mu = off-line zeros)."""
    return float(np.sum(np.maximum(0.0, mu.real - 1.0)) + np.sum(np.abs(mu.imag)))


def run(grid):
    print("E101 — edge structure of the generalized spectrum (L_prime, L_arch): mu_max & past-edge mass")
    rows = {}
    for kind in ('zeta', 'DH'):
        print(f"\n--- {kind} ---")
        MM = []; EX = []
        for lam, N in grid:
            La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40); dim = len(idx)
            La = to_np(La, dim); Lp = to_np(Lp, dim)
            mu = gen_mu(Lp, La)
            mumax = float(mu.real.max())
            ncx = int(np.sum(np.abs(mu.imag) > 1e-6))
            ex = edge_excess(mu)                       # mass past the contractive edge mu=1
            MM.append(mumax); EX.append(ex)
            print(f"  lam={lam:4.1f}  mu_max={mumax:+8.4f}  past-edge mass={ex:8.3f}  #complex mu={ncx}")
        rows[kind] = (np.array([g[0] for g in grid]), np.array(MM), np.array(EX))
    print("\nEDGE DRIFT (log mu_max-excess vs t=log lambda):  zeta contractive (mu_max=1), DH off-line pole")
    for kind in ('zeta', 'DH'):
        lams, MM, EX = rows[kind]
        exc = np.maximum(MM - 1.0, 1e-9)
        sl = np.polyfit(np.log(lams), np.log(exc), 1)[0] if np.any(MM > 1.01) else 0.0
        print(f"  {kind}: mu_max range[{MM.min():.3f},{MM.max():.3f}]  "
              f"{'CONTRACTIVE (mu_max=1, bounded)' if MM.max()<1.1 else f'DRIFTS, (mu_max-1)~lambda^{sl:.2f} (=> 2beta-1)'}")


if __name__ == '__main__':
    grid = [(9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    run(grid)
