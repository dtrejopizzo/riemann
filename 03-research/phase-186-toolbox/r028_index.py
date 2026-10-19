#!/usr/bin/env python3
"""R186_028 — negative index of a_T on L^2(I_T): decomposition by parity and pole.

Forma (Paper 47 thm:A / eq:Aform / lem:K / thm:S(iii)):
  a_T(F) = C_0||F||^2 + int_0^oo K(u)(||F||^2 - C_F(u)) du - sum_{n in N_T} v_n C_F(log n) = Gamma(F) + Pi_T(F),
  K(u) = 2e^{-u/2}/(1-e^{-2u}),  C_0 = psi(1/4) - log pi,  v_n = 2 Lambda(n)/sqrt n,  N_T = {n : log n < 2T},
  C_F(u) = int F(t)F(t-u) dt (simetrizada),  tau(r) = int_r^oo K = log coth(r/4) + pi - 2 arctan e^{r/2}.
Forma completa (eq:W, thm:parityschur(o)):  W_T = a_T + 2 l_ev^2 - 2 l_odd^2,
  l_ev(F) = <F, cosh(t/2) 1_I>,  l_odd(F) = <F, sinh(t/2) 1_I>,  A = l_ev + l_odd,  B = l_ev - l_odd.
Galerkin: orthonormal Legendre of degree < N on I_T (all in x-space, Gauss quadrature exact on polynomials;
the only non-polynomial integral is the one in u against K, analytic on [0,2T]).

Output: by parity sector, n_-(Gamma), n_-(a_T), n_-(a_T|P_T) (lambda_A), polar capacities
g_par = a_T(h_par) + 2 eps_par (Paper 47 prop:polarcap), sigma_par = l_par^T a_T^{-1} l_par = 1/a_T(h_par),
the eigenvalues of S_k = T a_T^{-1} T^T in three normalizations of T, and the component of the negative
direction on the Tate modes.

Usage:  python3 r028_index.py [N=60]      (main table + 1-D sweep in T)
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import digamma
import scipy.linalg as sl

C0 = digamma(0.25) - np.log(np.pi)          # -5.3721834...

def K(u): return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))
def tau(r): return np.log(1 / np.tanh(r / 4)) + np.pi - 2 * np.arctan(np.exp(r / 2))

def contacts(T):
    out = []
    for n in range(2, 400):
        if np.log(n) >= 2 * T: break
        p = next(q for q in range(2, n + 1) if n % q == 0); m = n
        while m % p == 0: m //= p
        if m == 1: out.append((n, np.log(n), 2 * np.log(p) / np.sqrt(n)))
    return out

class Window:
    def __init__(self, T, N=60, nu=400, nt=None):
        self.T, self.N = T, N
        nt = nt or N + 24
        self.xt, self.wt = NL.leggauss(nt)             # quadrature in t (exact degree < 2nt)
        self.xu, self.wu = NL.leggauss(nu)             # quadrature in u on (0, 2T)
        # orthonormal basis phi_k(t) = sqrt((2k+1)/2T) P_k(t/T)
        self.nrm = np.sqrt((2 * np.arange(N) + 1) / (2 * T))
        I = np.eye(N)
        # bilinear autocorrelation C(u)_{ij} = int_{-T+u}^{T} phi_i(t) phi_j(t-u) dt, symmetrized
        def Cs(u):
            lo, hi = -T + u, T
            if hi <= lo: return np.zeros((N, N))
            t = (hi + lo) / 2 + (hi - lo) / 2 * self.xt; w = self.wt * (hi - lo) / 2
            P1 = self.phi(t); P2 = self.phi(t - u)
            C = (P1 * w[:, None]).T @ P2
            return (C + C.T) / 2
        # Gamma = C_0 I + int_0^{2T} K(u)(I - C(u)) du + tau(2T) I
        us = T + T * self.xu; wus = self.wu * T
        G = np.zeros((N, N))
        for u, w in zip(us, wus): G += w * K(u) * (I - Cs(u))
        self.Gam = C0 * I + G + tau(2 * T) * I
        self.Pi = np.zeros((N, N)); self.cont = contacts(T)
        for n, l, v in self.cont: self.Pi -= v * Cs(l)
        self.A = self.Gam + self.Pi
        # polar and Tate functionals (coefficient vectors)
        t = T * self.xt; w = self.wt * T; P = self.phi(t)
        self.lev = (P * w[:, None]).T @ np.cosh(t / 2); self.lodd = (P * w[:, None]).T @ np.sinh(t / 2)
        self.tp = self.lev + self.lodd; self.tm = self.lev - self.lodd     # A = <F,e^{t/2}>, B = <F,e^{-t/2}>
        self.W = self.A + 2 * np.outer(self.lev, self.lev) - 2 * np.outer(self.lodd, self.lodd)
        self.ev = np.arange(N) % 2 == 0; self.od = ~self.ev

    def phi(self, t):
        V = NL.legvander(t / self.T, self.N - 1)
        return V * self.nrm

def ninf(M): return int((np.linalg.eigvalsh((M + M.T) / 2) < 0).sum())

def null_basis(rows):
    R = np.atleast_2d(np.array(rows)); _, s, Vt = np.linalg.svd(R); return Vt[R.shape[0]:].T

def sector(Wd, M, par):
    """Data for a sector: n_-(M|sector), lambda_min(M|ker l_par), sigma = l^T M^{-1} l, a(h) = 1/sigma."""
    idx = Wd.ev if par == 'ev' else Wd.od
    l = (Wd.lev if par == 'ev' else Wd.lodd)[idx]
    Ms = M[np.ix_(idx, idx)]
    Z = null_basis([l]); lamQ = np.linalg.eigvalsh(Z.T @ Ms @ Z)
    sig = l @ np.linalg.solve(Ms, l)
    return dict(nneg=ninf(Ms), nnegQ=int((lamQ < 0).sum()), lamQ=lamQ[0], sigma=sig, ah=1 / sig)

def main(N=60):
    Ts = [0.36, 0.45, np.log(3) / 2, 0.62, np.log(2), 0.75, np.log(5) / 2]
    print(f"# Legendre Galerkin dim N={N};  C_0={C0:.7f}")
    print("# 1. inertia by sector:  Gamma (archimedean, no pole) and a_T = Gamma + Pi_T, on L^2(I_T) and on P_T")
    print("#    T      primos | n-(Gam) ev od | n-(Gam|P) ev od | n-(a_T) ev od | n-(a_T|P) ev od | lam_A(ev)   lam_A(od)  | lam_W")
    rows = {}
    for T in Ts:
        Wd = Window(T, N)
        ge, go = sector(Wd, Wd.Gam, 'ev'), sector(Wd, Wd.Gam, 'od')
        ae, ao = sector(Wd, Wd.A, 'ev'), sector(Wd, Wd.A, 'od')
        lamW = np.linalg.eigvalsh(Wd.W)[0]
        rows[T] = (Wd, ge, go, ae, ao)
        print(f"  {T:.4f}  {[n for n,_,_ in Wd.cont]!s:10s}|   {ge['nneg']}  {go['nneg']}    |    {ge['nnegQ']}  {go['nnegQ']}     |   {ae['nneg']}  {ao['nneg']}    |    {ae['nnegQ']}  {ao['nnegQ']}     | {ae['lamQ']:+.3e} {ao['lamQ']:+.3e} | {lamW:+.2e}")
    print("\n# 2. polar capacities (Paper 47 prop:polarcap: g_par = a_T(h_par) + 2 eps_par) and the eigenvalue -1")
    print("#    T     | a(h_ev)   a(h_odd)  | g_ev      g_odd    | 1/(l W^-1 l): ev  odd | eig S (A,B): 2sig_e 2sig_o | 2/(g_ev-2) | Gamma: Gam(h_ev) Gam(h_odd)")
    for T, (Wd, ge, go, ae, ao) in rows.items():
        gev, godd = ae['ah'] + 2, ao['ah'] - 2
        # check: g_par = 1/(l^T W_par^{-1} l) when W_par is invertible
        We = Wd.W[np.ix_(Wd.ev, Wd.ev)]; Wo = Wd.W[np.ix_(Wd.od, Wd.od)]
        rho_e = Wd.lev[Wd.ev] @ np.linalg.solve(We, Wd.lev[Wd.ev]); rho_o = Wd.lodd[Wd.od] @ np.linalg.solve(Wo, Wd.lodd[Wd.od])
        Tm = np.vstack([Wd.tp, Wd.tm]); S1 = Tm @ np.linalg.solve(Wd.A, Tm.T); e1 = np.linalg.eigvalsh(S1)
        print(f"  {T:.4f} | {ae['ah']:+.5f}  {ao['ah']:+.5f} | {gev:+.3e} {godd:+.3e} | {1/rho_e:+.3e} {1/rho_o:+.3e} | {e1[0]:+.6f} {e1[1]:+.6f} | {2/(gev-2):+.6f} | {ge['ah']:+.4f} {go['ah']:+.4f}")
    print("\n# 3. three normalizations of T_k (rows = functionals):  (A,B) ; (l_ev,l_odd) ; (A,B)/||e^{+-t/2}1_I||")
    for T, (Wd, ge, go, ae, ao) in rows.items():
        Ai = np.linalg.inv(Wd.A)
        out = []
        for name, Tm in (("(A,B)", np.vstack([Wd.tp, Wd.tm])), ("(ev,odd)", np.vstack([Wd.lev, Wd.lodd])),
                         ("(A,B)/norm", np.vstack([Wd.tp, Wd.tm]) / np.sqrt(2 * np.sinh(T)))):
            e = np.linalg.eigvalsh(Tm @ Ai @ Tm.T); out.append(f"{name}: {e[0]:+.5f},{e[1]:+.5f}")
        print(f"  {T:.4f}  " + "   ".join(out) + f"   [sigma_e={ae['sigma']:+.5f} sigma_o={ao['sigma']:+.5f}]")
    print("\n# 4. negative direction of a_T: parity and component on the Tate modes (cosines in L^2(I_T))")
    print("#    T     | lam_1(a_T)  | par  | cos(v,cosh 1_I) cos(v,e^{t/2}1_I) cos(v,sinh 1_I) | cos(v,h_ev) | a_T(cosh1_I)/||.||^2  a_T(sinh1_I)/||.||^2")
    for T, (Wd, ge, go, ae, ao) in rows.items():
        lam, V = np.linalg.eigh(Wd.A); v = V[:, 0]
        pe = np.linalg.norm(v[Wd.ev]); par = 'ev' if pe > 0.99 else ('od' if pe < 0.01 else 'mixed')
        cs = lambda c: abs(v @ c) / np.linalg.norm(c)
        # h_ev = a_T^{-1} l_ev / sigma_e  (even sector)
        h = np.zeros(Wd.N); h[Wd.ev] = np.linalg.solve(Wd.A[np.ix_(Wd.ev, Wd.ev)], Wd.lev[Wd.ev])
        qc = (Wd.lev @ Wd.A @ Wd.lev) / (Wd.lev @ Wd.lev); qs = (Wd.lodd @ Wd.A @ Wd.lodd) / (Wd.lodd @ Wd.lodd)
        print(f"  {T:.4f} | {lam[0]:+.4f}    | {par:5s}| {cs(Wd.lev):.5f}         {cs(Wd.tp):.5f}         {cs(Wd.lodd):.1e}        | {cs(h):.5f}     | {qc:+.4f}            {qs:+.4f}")
    print("\n# 5. 1-D sweep (N=40): Rayleigh quotients of Gamma and a_T on cosh 1_I and sinh 1_I; n_-(Gamma|L2), n_-(a_T|L2)")
    print("#    T     Gam(cosh)  a_T(cosh)  Gam(sinh)  a_T(sinh) | n-(Gam) n-(a_T) | n-(a_T|P)  lam_A")
    for T in np.arange(0.25, 0.86, 0.05):
        Wd = Window(T, 40)
        R = lambda M, c: (c @ M @ c) / (c @ c)
        ae, ao = sector(Wd, Wd.A, 'ev'), sector(Wd, Wd.A, 'od')
        print(f"  {T:.3f}  {R(Wd.Gam, Wd.lev):+.4f}   {R(Wd.A, Wd.lev):+.4f}   {R(Wd.Gam, Wd.lodd):+.4f}   {R(Wd.A, Wd.lodd):+.4f}  |   {ninf(Wd.Gam)}       {ninf(Wd.A)}     |    {ae['nnegQ']+ao['nnegQ']}     {min(ae['lamQ'], ao['lamQ']):+.2e}")
    print("\n# 6. checks: a_T(e^{t/2}1_I) at 1/2 log5 (R186_026: -5.592), lam_A(1/2 log3) (Paper 47: 9.45e-4), convergence in N")
    for Nn in (30, 45, 60, 80):
        W5 = Window(np.log(5) / 2, Nn); W3 = Window(np.log(3) / 2, Nn)
        a5 = W5.tp @ W5.A @ W5.tp
        a3 = min(sector(W3, W3.A, 'ev')['lamQ'], sector(W3, W3.A, 'od')['lamQ'])
        e1 = np.linalg.eigvalsh(np.vstack([W5.tp, W5.tm]) @ np.linalg.solve(W5.A, np.vstack([W5.tp, W5.tm]).T))
        print(f"  N={Nn}: a_T(e^(t/2)1_I)(1/2log5) = {a5:+.6f}   lam_A(1/2log3) = {a3:+.5e}   eig S(1/2log5) = {e1[0]:+.7f}, {e1[1]:+.6f}   n-(a_T) = {ninf(W5.A)}, {ninf(W3.A)}")


def extra():
    """7. 1-D thresholds: T_Gam (Gamma(cosh 1_I)=0), polar capacities of Gamma (death of A_oo = Gamma + pole), n_-(Gamma|P) at 0.80 vs 1/2 log5."""
    print("# 7a. Gamma(cosh(t/2)1_I)/||.||^2 for small T (n_-(a_T|L2) >= 1 as soon as it is < 0; Pi_T <= 0 on positive functions)")
    for T in (0.02, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25):
        Wd = Window(T, 30); print(f"  T={T:.2f}: {(Wd.lev @ Wd.Gam @ Wd.lev)/(Wd.lev @ Wd.lev):+.5f}")
    print("# 7b. polar capacities of Gamma: g^Gam_par = Gamma(h_par) + 2 eps_par;  lam_min(A_oo|L2) = lam_min(Gamma + 2 l_ev^2 - 2 l_odd^2)")
    print("#     T     g^Gam_ev    g^Gam_odd   lam_min(A_oo|L2)  n-(A_oo|L2)")
    for T in (0.34, 0.36, 0.38, 0.40, 0.42, 0.44, 0.46, 0.48):
        Wd = Window(T, 40); ge, go = sector(Wd, Wd.Gam, 'ev'), sector(Wd, Wd.Gam, 'od')
        Ainf = Wd.Gam + 2 * np.outer(Wd.lev, Wd.lev) - 2 * np.outer(Wd.lodd, Wd.lodd)
        print(f"  {T:.2f}   {ge['ah']+2:+.5f}   {go['ah']-2:+.5f}   {np.linalg.eigvalsh(Ainf)[0]:+.3e}        {ninf(Ainf)}")
    print("# 7c. n_-(Gamma|P_T) by sector near 0.80 (R155_047: 1 at 0.80; thm:index excludes two short intervals)")
    for T in (0.78, 0.80, 0.802, 0.8047, 0.81):
        Wd = Window(T, 50); ge, go = sector(Wd, Wd.Gam, 'ev'), sector(Wd, Wd.Gam, 'od')
        print(f"  T={T:.4f}: n-(Gam|P) ev={ge['nnegQ']} od={go['nnegQ']}   lam_min(Gam|Q_ev)={ge['lamQ']:+.3e}  lam_min(Gam|Q_od)={go['lamQ']:+.3e}")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'extra': extra()
    else: main(int(sys.argv[1]) if len(sys.argv) > 1 else 60)
