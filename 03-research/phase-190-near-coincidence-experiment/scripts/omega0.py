"""(Omega_0): clamped ground mode of P_T = (1/4 - d^2) H^2_0(I_T) for the archimedean form, and the prime sum S(T) = sum v_n c_phi(log n).
Galerkin basis G_j(t) = (1-(t/T)^2)^2 P_j(t/T) (even j), F_j = (1/4 - d^2) G_j, polynomials on [-T,T].
Forms: Gram <F_i,F_j>; archimedean  a_inf(F_i,F_j) = C0 <F_i,F_j> + int_0^inf [c_ij(0) - c_ij(u)] K(u) du (even part of c_ij), with
c_ij piecewise polynomial computed exactly (polynomial arithmetic), K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)); Gauss-Legendre in u.
Prime sum: sum_n v_n c_phi(log n), n<e^{2T}."""
import numpy as np, json, sys
from numpy.polynomial import polynomial as Pn, legendre as L
from scipy.special import digamma
from profile import C0
def K(u): return 0.5/np.sinh(u/2) + 0.5/np.cosh(u/2)
def basis(T, N):
    """returns list of polynomial coefficient arrays (in t) for F_j = (1/4 - d^2) G_j, G_j=(1-(t/T)^2)^2 P_j(t/T), j even <2N"""
    Fs = []
    for j in range(0, 2*N, 2):
        Pj = L.leg2poly(np.eye(2*N)[j])          # Legendre P_j in x=t/T
        Pj_t = np.array([c/T**i for i, c in enumerate(Pj)])
        env = Pn.polypow(np.array([1, 0, -1/T**2]), 2)
        G = Pn.polymul(env, Pj_t)
        F = Pn.polysub(0.25*G, Pn.polyder(G, 2))
        Fs.append(np.trim_zeros(F, 'b'))
    return Fs
def corr_poly(F, H, T):
    """c(u) = int_{-T}^{T} F(t) H(t-u) dt for u in [0,2T]: a polynomial in u on each piece? F,H polynomials on [-T,T], zero outside.
    For u>=0: t ranges over [u-T, T]; c(u) = int_{u-T}^{T} F(t)H(t-u) dt  is a polynomial in u (single piece on [0,2T])."""
    # represent H(t-u) as polynomial in t with coefficients polynomials in u: use symbolic via numpy 2D arrays
    # Simpler: evaluate numerically with Gauss-Legendre in t at required u (exact for polynomials with enough nodes).
    deg = len(F) + len(H)
    xg, wg = np.polynomial.legendre.leggauss(deg//2 + 4)
    def c(u):
        a, b = u - T, T
        t = 0.5*(b-a)*xg + 0.5*(b+a)
        return 0.5*(b-a)*np.sum(wg*Pn.polyval(t, F)*Pn.polyval(t-u, H))
    return c
def forms(T, N, comb):
    Fs = basis(T, N); n = len(Fs)
    # u-quadrature for the Levy integral on [0,2T] (smooth integrand) plus tail: int_{2T}^inf K = log coth(T/2) + pi - 2 arctan e^T
    ug, wu = np.polynomial.legendre.leggauss(200); u = T*(ug+1); wu = wu*T
    tail = np.log(1/np.tanh(T/2)) + np.pi - 2*np.arctan(np.exp(T))
    Gr = np.zeros((n, n)); Ar = np.zeros((n, n)); Pr = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            cij = corr_poly(Fs[i], Fs[j], T); cji = corr_poly(Fs[j], Fs[i], T)
            c0 = cij(0.0)
            ce = np.array([0.5*(cij(uu) + cji(uu)) for uu in u])    # even part
            lev = np.sum(wu*(c0 - ce)*K(u)) + c0*tail
            Gr[i, j] = Gr[j, i] = c0
            Ar[i, j] = Ar[j, i] = C0*c0 + lev
            ps = sum(wn*0.5*(cij(xn) + cji(xn)) for xn, wn in comb if xn < 2*T)
            Pr[i, j] = Pr[j, i] = ps
    return Gr, Ar, Pr
def ground(T, N, comb):
    Gr, Ar, Pr = forms(T, N, comb)
    from scipy.linalg import eigh
    lc, Vc = np.linalg.eigh(Gr); keep = lc > 1e-13*lc[-1]; W = Vc[:, keep]/np.sqrt(lc[keep])
    B = W.T@Ar@W; lb, Vb = np.linalg.eigh(B); phi = W@Vb[:, 0]
    mu0 = lb[0]; S = phi@Pr@phi
    # full form bottom on the same space (for comparison)
    Bf = W.T@(Ar - Pr)@W; lf = np.linalg.eigvalsh(Bf)[0]
    return dict(mu0=float(mu0), S=float(S), a_T_phi0=float(mu0 - S), lamA_galerkin=float(lf), dim=int(keep.sum()))
if __name__ == '__main__':
    from am import lambda_comb, poisson_comb
    Ts = np.arange(0.40, 1.101, 0.05)
    combs = {'Lambda': lambda_comb(20)}
    combs['a_3'] = lambda_comb(20, delete_below=3); combs['a_5'] = lambda_comb(20, delete_below=5)
    combs['amp2_0.05'] = lambda_comb(20, amp2=0.05); combs['amp2_0.5'] = lambda_comb(20, amp2=0.5)
    combs['pert2_+1e-2'] = lambda_comb(20, perturb=(2, 1.01)); combs['pert2_-1e-2'] = lambda_comb(20, perturb=(2, 0.99))
    for s in range(3): combs[f'poisson_{s}'] = poisson_comb(2.5, 1.0, s)
    res = {}
    for T in Ts:
        row = {}
        for N in (14, 20):
            for name, (pos, w, _) in combs.items():
                row[(name, N)] = ground(T, N, list(zip(pos, w)))
        res[round(float(T), 3)] = {f'{k[0]}_N{k[1]}': v for k, v in row.items()}
        L14, L20 = row[('Lambda', 14)], row[('Lambda', 20)]
        print('T=%.2f mu0=%.6f (N14 %.6f) S=%.6f a_T(phi0)=%.3e  lamA_gal=%.3e | a_3: S=%.4f margin=%.3e | poisson0 margin=%.3e' % (T, L20['mu0'], L14['mu0'], L20['S'], L20['a_T_phi0'], L20['lamA_galerkin'], row[('a_3',20)]['S'], row[('a_3',20)]['a_T_phi0'], row[('poisson_0',20)]['a_T_phi0']), flush=True)
        json.dump(res, open('../data/omega0.json', 'w'), indent=1)
