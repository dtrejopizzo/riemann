"""r8a_02: certified LOWER bound n_-(A_inf | P_T^{par}) >= 1, one sector, one window.

usage: python3 r8a_02_lower.py <T string or 'log2'|'halflog3'> <par 0|1> [N panels]

Bordered form B(F,xi) = Gamma_T[F] + 2 xi <F,g>  on L^2_par(I_T) + R, g = cosh(t/2) or sinh(t/2):
n_-(Gamma_T | g^perp) = n_-(B) - 1  (algebraic bordered-inertia lemma, R155_052 Lemma 2.1).
Exhibit a 2-dimensional negative-definite subspace of B inside span{F, h} + R, with F, h
explicit polynomials of degree < N (F ~ Galerkin bottom eigenvector of the sector, h ~ Legendre
truncation of g).  All entries enclosed by the interval machinery of scripts/r4a/r4a_lib.py
(Paper 47 thm:w11 proof): exact interval autocorrelation, affine sandwich of K, closed-form
constants; the PRIME ATOMS ARE SWITCHED OFF (A_inf, not W_T), and the pole term is NOT used:
the archimedean form Gamma_T[F] = C0 c(0) + int_0^{2T}(c(0)-c)K + c(0) int_{2T}^inf K is read
from the pieces.  <F,g> = (A(F) +/- B(F))/2 from the exact moment series.  Requires T < 0.88137.
"""
import sys, os, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'r4a'))
import r4a_lib as lib
from r8a_lib import iv, mp, cholesky_pd, congruence, mid, wid, lo, hi
from scipy.special import spherical_jn, digamma

def window(s):
    if s == 'log2':
        return '0.693147180559945309417232121458176568075500134360255254120680009493393621969694715605863326996418687542001481021', float(np.log(2))
    if s == 'halflog3':
        return '0.549306144334054845697622618461262852323745278911374725867347171417926749219582177811213571892176238405425355', float(0.5 * np.log(3))
    return s, float(s)

def gamma_fourier(T, N):
    """DIAGNOSTIC float Galerkin matrix of Gamma_T in the Legendre basis (for choosing F only)."""
    m = lambda t: np.real(digamma(0.25 + 0.5j * np.asarray(t, float))) - np.log(np.pi)
    C0 = float(digamma(0.25) - np.log(np.pi))
    i = np.arange(N); ph = np.where((i[:, None] - i[None, :]) % 2 == 0, (-1.0) ** ((i[None, :] - i[:, None]) // 2), 0.0)
    G = np.zeros((N, N)); edges = [0, 6.29, 20, 60, 200, 600, 2000, 6000, 15000, 40000]
    GL = np.polynomial.legendre.leggauss(600)
    for a, b in zip(edges[:-1], edges[1:]):
        tau = 0.5 * (b - a) * GL[0] + 0.5 * (b + a); w = 0.5 * (b - a) * GL[1]
        J = np.array([spherical_jn(k, tau * T) for k in range(N)])
        G += (J * (w * (m(tau) - C0))) @ J.T
    X = edges[-1]; tail = 0.5 * (np.log(X / (2 * np.pi)) - C0 + 1) / (T * T * X)
    G += tail * np.where((i[:, None] - i[None, :]) % 4 == 0, 1.0, np.where((i[:, None] - i[None, :]) % 4 == 2, -1.0, 0.0))
    return C0 * np.eye(N) + (2 * T / np.pi) * np.sqrt((2 * i[:, None] + 1) * (2 * i[None, :] + 1)) * ph * G

def main(Tstr, par, N=18, panels=3000):
    t0 = time.time()
    Tdec, Tf = window(Tstr)
    # --- float choice of F (Galerkin bottom of the sector) and h (truncated g)
    G = gamma_fourier(Tf, N)
    x, w = np.polynomial.legendre.leggauss(200); t = Tf * x; w = Tf * w
    V = np.array([np.sqrt((2 * k + 1) / (2 * Tf)) * np.polynomial.legendre.legval(x, np.eye(N)[k]) for k in range(N)]).T
    gfun = np.cosh(t / 2) if par == 0 else np.sinh(t / 2)
    gc = (V * (w * gfun)[:, None]).sum(0)
    idx = np.arange(par, N, 2)
    Gs = G[np.ix_(idx, idx)]; gs = gc[idx]; q = gs / np.linalg.norm(gs)
    Z = np.linalg.svd(q[None, :], full_matrices=True)[2][1:].T
    ev, U = np.linalg.eigh(Z.T @ Gs @ Z)
    Fs = Z @ U[:, 0]
    F = np.zeros(N); F[idx] = Fs; h = np.zeros(N); h[idx] = gs
    print("Galerkin (DIAGNOSTIC) sector bottom at N=%d: %.6f" % (N, ev[0]), flush=True)
    # --- rigorous enclosures
    LF = lib.LevyForm(Tdec, N, panels=panels)
    LF.atoms = []                                   # archimedean form only
    def Gam(vec):
        pc = LF.pcoef([float(v) for v in vec])
        val, d = LF.W([float(v) for v in vec])
        gam = LF.C0 * d['c0'] + d['INT'] + d['c0'] * LF.Ktail
        A, B = LF.moments(pc)
        gpair = (A + B) / iv.mpf(2) if par == 0 else (A - B) / iv.mpf(2)
        return gam, gpair
    gF, pF = Gam(F); gh, ph_ = Gam(h); gp, _ = Gam(F + h); gm, _ = Gam(F - h)
    gFh = (gp - gm) / iv.mpf(4)
    B3 = [[gF, gFh, pF], [gFh, gh, ph_], [pF, ph_, iv.mpf(0)]]
    print("Gamma[F] = [%.10f, %.10f]  <F,g> = [%.3e, %.3e]" % (lo(gF), hi(gF), lo(pF), hi(pF)), flush=True)
    print("Gamma[h] = [%.6f, %.6f]  <h,g> = [%.6f, %.6f]  Gamma(F,h) = [%.6f, %.6f]" % (lo(gh), hi(gh), lo(ph_), hi(ph_), lo(gFh), hi(gFh)))
    Bm = np.array([[mid(x) for x in r] for r in B3])
    e3, U3 = np.linalg.eigh(Bm)
    ok = False
    if e3[1] < 0:
        C = congruence(U3[:, :2], [[-x for x in r] for r in B3])
        ok = cholesky_pd(C)
    out = dict(T=Tstr, par=par, N=N, panels=panels, galerkin_bottom_DIAG=float(ev[0]),
               GammaF=[lo(gF), hi(gF)], Fg=[lo(pF), hi(pF)], Gammah=[lo(gh), hi(gh)], hg=[lo(ph_), hi(ph_)],
               GammaFh=[lo(gFh), hi(gFh)], B3_eigs_mid=[float(x) for x in e3],
               certified_two_negative=ok, certified_lower_bound_sector=(1 if ok else 0),
               F_legendre_coeffs=[float(v) for v in F], runtime_s=time.time() - t0)
    print(json.dumps({k: v for k, v in out.items() if k != 'F_legendre_coeffs'}, indent=1))
    json.dump(out, open(os.path.join(HERE, "r8a_02_%s_par%d.json" % (Tstr.replace('.', 'p'), par)), "w"), indent=1)
    return out

if __name__ == '__main__':
    Tstr = sys.argv[1]; par = int(sys.argv[2])
    N = int(sys.argv[3]) if len(sys.argv) > 3 else 18
    panels = int(sys.argv[4]) if len(sys.argv) > 4 else 3000
    main(Tstr, par, N, panels)
