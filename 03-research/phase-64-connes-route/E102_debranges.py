"""
E102 — Task C (Connes route): de Branges / canonical-system structure. First pass.

Connes: from the intrinsic Jacobi form the Weyl m-function m_lambda(z); test m Herglotz <=>
S_lambda=(m-i)/(m+i) Schur/contractive; build canonical system JY'=zH(x)Y, H>=0. A proof that
S_lambda is contractive from an Euler-product/adelic unitary colligation is the genuine route; DH
should fail because it lacks that colligation.

CAVEAT we test head-on: a FINITE self-adjoint Jacobi (b_k>0 real) gives m Herglotz and H_k>=0
AUTOMATICALLY -- so the finite window cannot discriminate zeta from DH at that level. The real
discriminator must be the operator whose spectrum is the ZEROS (not the Weil-form Jacobi). We
therefore also test the scaling operator H_x (E3 CCM, spectrum=zeros) for SPECTRAL REALITY:
  zeta  -> real spectrum (zeros on line)  <=> m_{H_x} Herglotz / structure function Hermite-Biehler
  DH    -> complex spectrum (off-line zeros) <=> Herglotz/HB FAILS.

Outputs:
 (1) Weil-form Jacobi -> m, Schur S: confirm Herglotz/contractive (baseline; expect BOTH pass).
 (2) canonical-system Hamiltonian H_k from Jacobi: confirm H_k>=0 (baseline; expect BOTH pass).
 (3) H_x scaling operator: fraction of spectrum that is REAL, and max |Im eigenvalue|
     -> the actual zeta-vs-DH discriminator (Hermite-Biehler content).
"""
import os, sys, numpy as np, mpmath as mp
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61); os.chdir(_P61)
from engine_cache import get_matrices

mp.mp.dps = 40


def lanczos(A, q0, m):
    n = A.rows; Q = [q0 / mp.sqrt((q0.T * q0)[0])]
    alpha = []; beta = []; qprev = mp.zeros(n, 1); b = mp.mpf(0)
    for j in range(m):
        Aq = A * Q[j]; a = (Q[j].T * Aq)[0]; alpha.append(a)
        r = Aq - a * Q[j] - (b * qprev if j > 0 else mp.zeros(n, 1))
        for qi in Q: r = r - (qi.T * r)[0] * qi
        b = mp.sqrt((r.T * r)[0])
        if b < mp.mpf(10) ** (-mp.mp.dps + 5) or j == m - 1: break
        beta.append(b); qprev = Q[j]; Q.append(r / b)
    return [float(x) for x in alpha], [float(x) for x in beta]


def weil_jacobi(lam, N, kind):
    La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40); n = A.rows
    q0 = mp.matrix([[mp.mpf(1) + mp.mpf('0.7') * (2 * i - (n - 1))] for i in range(n)])
    return lanczos(A, q0, n)


def m_function(alpha, beta, z):
    """Weyl m(z)=<e0,(J-z)^{-1}e0> via continued fraction (backward recursion)."""
    m = len(alpha); f = 0.0 + 0j
    for k in range(m - 1, -1, -1):
        b2 = (beta[k - 1] ** 2) if k > 0 else 1.0
        f = b2 / (alpha[k] - z - f) if k > 0 else 1.0 / (alpha[k] - z - f)
    return f


def herglotz_schur_test(alpha, beta):
    # sample upper half plane; Herglotz <=> Im m(z)>0 for Im z>0; Schur S=(m-i)/(m+i), |S|<=1
    ok_h = True; ok_s = True; maxS = 0.0
    for x in np.linspace(-3, 3, 13):
        for y in (0.2, 0.5, 1.0):
            z = x + 1j * y; m = m_function(alpha, beta, z)
            if m.imag < -1e-9: ok_h = False
            S = abs((m - 1j) / (m + 1j)); maxS = max(maxS, S)
            if S > 1 + 1e-9: ok_s = False
    return ok_h, ok_s, maxS


def canonical_H_psd(alpha, beta):
    """canonical-system Hamiltonian blocks from the Jacobi; check each 2x2 H_k>=0.
    Standard map: H_k = [[1/w_k, 0],[0, w_k]]-type positive blocks built from the b_k>0 (real Jacobi)
    => automatically PSD. We report the min block eigenvalue (should be >0 for both)."""
    w = np.array([1.0] + [float(b) for b in beta])
    mins = []
    for wk in w:
        Hk = np.array([[1.0 / max(wk, 1e-30), 0.0], [0.0, wk]])
        mins.append(np.linalg.eigvalsh(Hk).min())
    return min(mins)


# --- scaling operator H_x (E3 CCM, spectrum=zeros): the actual discriminator ---
def von_mangoldt(K):
    Lam = np.zeros(K + 1); s = np.ones(K + 1, bool); s[:2] = False
    for p in range(2, int(K ** 0.5) + 1):
        if s[p]: s[p * p::p] = False
    for p in np.nonzero(s)[0]:
        pk = p; lp = np.log(p)
        while pk <= K: Lam[pk] = lp; pk *= p
    return Lam


def Hx_spectrum(lam, N, K, kind):
    L = 2.0 * np.log(lam); n = np.arange(-N, N + 1); dim = 2 * N + 1
    Lam = von_mangoldt(K); ks = np.arange(1, K + 1); coef = Lam[1:K + 1] / np.sqrt(ks)
    if kind == 'DH':
        chi = np.array([{1: 1, 2: 1, 3: -1, 4: -1, 0: 0}[k % 5] for k in ks]); coef = coef * chi
    b = np.array([(1.0 / L) * np.sum(coef * np.sin(2 * np.pi * ks * nn / L)) for nn in n])
    QW = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            QW[i, j] = np.log(lam) * 0.5 if i == j else (b[i] - b[j]) / (n[i] - n[j])
    QW = (QW + QW.T) / 2
    delta = np.ones(dim) / np.sqrt(L)
    y = np.linalg.lstsq(QW, delta, rcond=None)[0]; xi = y / (delta @ y)
    Dlog = np.diag(2 * np.pi * n / L)
    Hx = Dlog - np.outer(Dlog @ xi, delta)
    ev = np.linalg.eigvals(Hx)
    band = ev[(ev.real > 5) & (ev.real < 50)]
    if band.size == 0: return float('nan'), float('nan')
    frac_real = float(np.mean(np.abs(band.imag) < 0.5))
    return frac_real, float(np.max(np.abs(band.imag)))


def run(grid):
    print("E102 — de Branges/canonical system. Baseline (1)(2) expected to pass for BOTH (finite")
    print("self-adjoint Jacobi). Discriminator (3) = spectral reality of H_x (spectrum=zeros).")
    for kind in ('zeta', 'DH'):
        print(f"\n--- {kind} ---")
        for lam, N in grid:
            al, be = weil_jacobi(lam, N, kind)
            okh, oks, maxS = herglotz_schur_test(al, be)
            hmin = canonical_H_psd(al, be)
            print(f"  lam={lam:4.1f}: (1) m Herglotz={okh} Schur |S|max={maxS:.3f} contractive={oks}"
                  f"   (2) min canonical block eig={hmin:.3e} (H>=0)")
    print("\n(3) H_x scaling operator spectral reality (the real discriminator):")
    for kind in ('zeta', 'DH'):
        for lam, N, K in [(11.0, 40, 500), (20.0, 60, 800)]:
            fr, mim = Hx_spectrum(lam, N, K, kind)
            print(f"  [{kind:4s} lam={lam}] frac real (band)={fr:.2f}  max|Im eig|={mim:.3f}  "
                  f"=> {'real spectrum (HB ok)' if mim < 0.5 else 'complex modes (HB fails)'}")


if __name__ == '__main__':
    grid = [(11.0, 18), (15.0, 20), (21.0, 22)]
    run(grid)
