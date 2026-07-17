"""
E94 — J-COMPATIBILITY and the correct quaternionic Hodge-Riemann positivity (Phase 62, MW-5).

E93 surprise: the symmetric part of A*J is exactly [A,J]/2 (since (AJ)^T = -JA). For ZETA its
eigenvalues are tiny (+-0.38) while a random-symmetric matrix with the SAME parity symmetry gives
+-5.3. I.e. ZETA's Weil matrix nearly COMMUTES with the quaternionic structure J (J^2=-1),
random does NOT. [A,J]=0 is the J-compatibility that defines a (weight-1) Hodge structure; it is
strictly stronger than the parity symmetry A_{-m,-n}=A_{mn} (which random also has).

This script:
  (1) quantifies r(lam) = ||[A,J]|| / ||A||  for zeta / random-sym / DH across lam.
      Hypothesis: r_zeta -> 0 (J-compatible), r_random ~ O(1), r_DH ~ O(1).
  (2) if zeta is J-compatible, complexify and split H^1 into the +-i eigenspaces of J;
      the HR/polarization test is: is the Hermitian form A definite on V_+ (the +i eigenspace)?
      Report signature on V_+ for zeta vs random vs DH.

NON-CIRCULARITY: if J-compatibility + V_+ definiteness hold for zeta but NOT for random-sym,
the positivity is an ARITHMETIC property of A (consistent with, but not yet a proof of, Weil
positivity). If random ALSO passes, it is ALGEBRAIC (would cross). Either way it is informative.
DH must fail. Honesty: dps>=40; no proof claimed; report verbatim.
"""
import os, sys, numpy as np, mpmath as mp
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61); os.chdir(_P61)
from engine_cache import get_matrices

mp.mp.dps = 40


def Jmat(idx):
    dim = len(idx); J = np.zeros((dim, dim))
    for a, n in enumerate(idx):
        if n != 0:
            J[idx.index(-n), a] = 1.0 if n > 0 else -1.0
    return J


def parity_random(idx, seed=0):
    rng = np.random.default_rng(seed); dim = len(idx); M = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(i, dim):
            v = rng.standard_normal(); M[i, j] = v; M[j, i] = v
    for i in range(dim):
        for j in range(dim):
            M[idx.index(-idx[i]), idx.index(-idx[j])] = M[i, j]
    return M


def jcompat(Anp, idx):
    J = Jmat(idx)
    z = idx.index(0); keep = [i for i in range(len(idx)) if i != z]
    A1 = Anp[np.ix_(keep, keep)]; J1 = J[np.ix_(keep, keep)]
    comm = A1 @ J1 - J1 @ A1
    return np.linalg.norm(comm) / np.linalg.norm(A1), A1, J1


def vplus_signature(A1, J1):
    """split into +-i eigenspaces of J1 (J1^2=-1, real => eigvals +-i); restrict A1 to V_+,
    report the signature of the Hermitian form there."""
    w, V = np.linalg.eig(J1)
    plus = [k for k in range(len(w)) if w[k].imag > 0.5]
    P = V[:, plus]                      # columns span V_+ (complex)
    Hp = P.conj().T @ A1 @ P            # Hermitian form A on V_+
    Hp = (Hp + Hp.conj().T) / 2
    ev = np.linalg.eigvalsh(Hp)
    npos = int((ev > 1e-9).sum()); nneg = int((ev < -1e-9).sum()); nz = len(ev) - npos - nneg
    return npos, nz, nneg, ev


def run(lam, N):
    La, Lp, A, L, idx = get_matrices(lam, N, 'zeta', dps=40)
    dim = len(idx)
    mats = {'ZETA': np.array([[float(A[i, j]) for j in range(dim)] for i in range(dim)])}
    Ld, Lpd, Ad, _, idxd = get_matrices(lam, N, 'DH', dps=40)
    mats['DH'] = np.array([[float(Ad[i, j]) for j in range(dim)] for i in range(dim)])
    mats['RANDOM'] = parity_random(idx, 0)
    print(f"\nlam={lam} N={N} dim={dim}")
    for lab, M in mats.items():
        r, A1, J1 = jcompat(M, idx)
        npos, nz, nneg, ev = vplus_signature(A1, J1)
        definite = (npos == 0 or nneg == 0)
        print(f"  [{lab:7s}] ||[A,J]||/||A|| = {r:.4f}   V_+ sig (pos,0,neg)=({npos},{nz},{nneg}) "
              f"=> {'DEFINITE (HR-polarized)' if definite else 'indefinite'}")
    return


if __name__ == '__main__':
    grid = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E94 — J-compatibility ||[A,J]||/||A|| and HR positivity on V_+ (quaternionic J^2=-1)")
    print("     hypothesis: zeta J-compatible (r->0) & definite on V_+; random/DH not.")
    for lam, N in grid:
        run(lam, N)
