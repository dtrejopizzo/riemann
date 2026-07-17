"""
E95 — origin of the V_+ positivity cascade (Phase 62, MW-5 crossing attempt).

E94: A is PSD on V_+ (J's +i eigenspace) for zeta, but GAPLESS — the V_+ spectrum is an
exponential cascade ~ e^{-c k} down to machine zero. Crossing the wall = giving that margin a
uniform e^{-cL} bound WITHOUT zero locations. First question: what DRIVES the cascade?

A = Larch - Lprime (Doob-conjugated). Decompose the V_+ form into its pieces and ask which one
produces the cascade, and whether the cascade RATE depends on lambda the way the band L=2 ln lam
predicts (so it could be a prime/archimedean fact, not a zero fact).

Tests:
  (1) cascade rate: fit log10(ev_k) vs k on the positive V_+ spectrum of A (zeta). slope = -rate.
  (2) decompose on V_+:  Larch|V+  vs  Lprime|V+  vs  A|V+ . Which carries the cascade?
      (is the smallness of small eigenvalues a near-cancellation Larch~Lprime, or intrinsic?)
  (3) lambda-scaling of the rate and of ev_min vs L=2 ln lam: is log ev_min ~ -c L (prime-side
      predictable) or erratic (zero-side)?
DH falsador for contrast. Honesty: dps>=40; no proof; report verbatim.
"""
import os, sys, numpy as np, mpmath as mp
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61); os.chdir(_P61)
from engine_cache import get_matrices
import E94_Jcompat as e94

mp.mp.dps = 40


def to_np(M, dim):
    return np.array([[float(M[i, j]) for j in range(dim)] for i in range(dim)])


def vplus_spectrum(Mat1, J1):
    w, V = np.linalg.eig(J1)
    plus = [k for k in range(len(w)) if w[k].imag > 0.5]
    P = V[:, plus]
    H = P.conj().T @ Mat1 @ P
    H = (H + H.conj().T) / 2
    return np.sort(np.linalg.eigvalsh(H))


def keep_block(M, idx):
    z = idx.index(0); keep = [i for i in range(len(idx)) if i != z]
    return M[np.ix_(keep, keep)], keep


def analyze(lam, N, kind):
    La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40)
    dim = len(idx)
    Anp, Lanp, Lpnp = to_np(A, dim), to_np(La, dim), to_np(Lp, dim)
    J = e94.Jmat(idx)
    A1, keep = keep_block(Anp, idx); J1 = J[np.ix_(keep, keep)]
    La1 = Lanp[np.ix_(keep, keep)]; Lp1 = Lpnp[np.ix_(keep, keep)]
    evA = vplus_spectrum(A1, J1)
    pos = evA[evA > 1e-12]
    # cascade rate: log10(ev) vs rank index over the positive cascade
    lr = np.log10(pos)
    k = np.arange(len(pos))
    rate = np.polyfit(k, lr, 1)[0] if len(pos) > 2 else float('nan')
    nneg = int((evA < -1e-12).sum())
    # decompose: norms of Larch|V+ and Lprime|V+ vs A|V+ (cancellation diagnostic)
    evLa = vplus_spectrum(La1, J1); evLp = vplus_spectrum(Lp1, J1)
    canc = (np.linalg.norm(evLa) + np.linalg.norm(evLp)) / max(np.linalg.norm(evA), 1e-30)
    L = float(2 * np.log(lam))
    print(f"  [{kind:4s} lam={lam:4.1f} L={L:4.2f}] V+ cascade rate(log10/step)={rate:+.3f}  "
          f"ev_min(+)={pos.min():.2e} ev_max={pos.max():.2f}  nneg(>1e-12)={nneg}  "
          f"||Larch|+||+||Lpr|+|| / ||A|+|| = {canc:.2f}")
    return L, np.log10(pos.min()), rate, nneg


def run(grid):
    print("E95 — V_+ cascade origin. rate=slope of log10(ev) vs rank; canc>>1 => Larch~Lprime cancel")
    rows = {'zeta': [], 'DH': []}
    for kind in ('zeta', 'DH'):
        print(f"\n--- {kind} ---")
        for lam, N in grid:
            rows[kind].append(analyze(lam, N, kind))
    # lambda-scaling: log ev_min vs L
    print("\nSCALING log10(ev_min) vs L=2 ln lam  (linear => ev_min ~ e^{-cL}, prime-predictable):")
    for kind in ('zeta', 'DH'):
        Ls = np.array([r[0] for r in rows[kind]]); lm = np.array([r[1] for r in rows[kind]])
        c = np.polyfit(Ls, lm, 1)
        resid = np.std(lm - np.polyval(c, Ls))
        print(f"  {kind}: log10(ev_min) ~ {c[0]:+.3f}*L + {c[1]:+.2f}   (rate c={-c[0]*np.log(10):+.3f}/nat)  "
              f"fit-resid={resid:.3f}  => {'CLEAN e^-cL (prime-like)' if resid<0.5 else 'erratic (zero-like)'}")


if __name__ == '__main__':
    grid = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    run(grid)
