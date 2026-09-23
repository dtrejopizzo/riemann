"""r8a_01: certified UPPER bound on n_-(A_inf | P_T^{par}), one parity sector, one window.

usage: python3 r8a_01_upper.py <T as decimal string or 'log2'|'halflog3'> <par 0|1> [K K2 cN [grid]]
       grid = 'default' (28 bands, the archived runs) | 'fine' (adaptive grid below tau = 8 with
       chord error ~ 2e-3, 16 geometric bands on [8.2, tau_N], exact m'' bound m2sup_band_exact);
       'fine' writes r8a_01_<T>_par<p>_fine.json and never overwrites the default outputs.

Method (R155_052 sec.2):
  1. piecewise-linear minorant s <= m on |tau| < tau_N (chords on bands, with the rigorous
     offset M2 Delta^2/8 where sup m'' > 0; constant C0 on the first band), constant
     c_N = m_lo(tau_N) beyond.  Gamma_T >= L := (1/2pi) int s |F^|^2 as forms on L^2(I_T).
  2. bordered form on L^2_par(I_T) + R with the sector constraint g (cosh or sinh):
     n_-(L | g^perp) = n_-(B) - 1.
  3. Haynsworth on E_K + R  (+)  E_K^perp:  B_22 = P^perp L P^perp >= gamma := c_N - W Lambda_K(c_N),
     W = c_N - min s; then n_-(B) = n_-(B_11 - B_12 B_22^{-1} B_21) <= n_-(B_11 - Gram/gamma),
     Gram = Gram matrix of {P^perp M e_i (i<K, i = par mod 2), P^perp g}, M = c_N - L >= 0,
     computed through the Legendre coefficients K <= l < K2 with the tails
       sum_{l>=K2} M_il M_jl  in  +- rho sqrt(M_ii M_jj),  rho = W Lambda_{K2}(c_N),
       sum_{l>=K2} M_il g_l   in  +- sqrt(rho M_ii) ||P^perp_{K2} g||.
     Sign: the Y-column of e_i is -P^perp M e_i and that of the border is +P^perp g, so the (e_i, xi)
     entry of the Schur bound is g_i + <P^perp M e_i, P^perp g>/gamma (fixed 2026-09-22; R155_052 L. 2.4).
  4. n_-(R) <= r+1 certified by interval Cholesky of U^T R U on the complementary subspace U.
Then n_-(A_inf | P_T^{par}) <= n_-(L | g^perp) <= r.
"""
import sys, os, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from r8a_lib import *

def window(s):
    if s == 'log2':
        return iv.log(iv.mpf(2)), float(np.log(2))
    if s == 'halflog3':
        return iv.log(iv.mpf(3)) / iv.mpf(2), float(0.5 * np.log(3))
    return iv.mpf(s), float(s)

def band_points(tauN):
    pts = [0.15, 0.3, 0.5, 0.75, 1.0, 1.3, 1.6, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
    geo = list(np.geomspace(9.0, tauN, 8))
    return [repr(round(p, 6)) for p in pts + geo[:-1]] + [repr(round(tauN, 6))]

def band_points_fine(tauN, eps=2e-3, cap=0.2):
    """band edges for grid='fine': step min(cap, sqrt(8 eps/|m''|)) on (0, 8] (m'' from the exact
    series, float -- the grid is data only, every certified number is recomputed on it in
    intervals), then 16 geometric edges on [8.2, tauN]."""
    a = np.arange(0, 200000) + 0.25
    def m2(t):
        s = t * t / 4.0
        return np.sum(a * (a * a - 3 * s) / (2 * (a * a + s) ** 3))
    pts = []; t = 0.0
    while t < 8.0:
        d = min(cap, np.sqrt(8 * eps / max(abs(m2(t)), abs(m2(t + 0.01)), 1e-9)))
        t = t + d; pts.append(round(min(t, 8.0), 4))
    geo = list(np.geomspace(8.2, tauN, 16))
    return [repr(p) for p in pts] + [repr(round(p, 6)) for p in geo[:-1]] + [repr(round(tauN, 6))]

def main(Tstr, par, K=22, K2=36, cN_target=16.0, grid='default'):
    t0 = time.time()
    T, Tf = window(Tstr)
    C0 = C0_interval()
    tauN = cN_target / Tf
    taus = band_points(tauN) if grid == 'default' else band_points_fine(tauN)   # tau_1 < ... < tau_N
    m2sup = m2sup_band if grid == 'default' else m2sup_band_exact
    N = len(taus)
    mvals = [m_interval(t, C0) for t in taus]     # intervals
    cN = iv.mpf(mp.mpf(mvals[-1].a))              # last-band constant: lower end of m(tau_N)
    # linear pieces on bands [tau_a, tau_{a+1}], a = 0..N-1, tau_0 = 0:  s = alpha_a + beta_a |tau|
    edges = [iv.mpf(0)] + [iv.mpf(t) for t in taus]
    mlo = [C0] + [iv.mpf(mp.mpf(v.a)) for v in mvals]   # lower ends (m(0) = C0 exact)
    alpha, beta, smin, offsets = [], [], cN, []
    for a in range(N):
        ta, tb = edges[a], edges[a + 1]
        if a == 0:
            al, be, off = C0, iv.mpf(0), iv.mpf(0)          # constant C0 <= m on the first band
        else:
            M2 = m2sup(mp.mpf(ta.a), mp.mpf(tb.b))
            off = iv.mpf(0) if M2 <= 0 else iv.mpf(M2) * (tb - ta) ** 2 / iv.mpf(8)
            be = (mlo[a + 1] - mlo[a]) / (tb - ta)
            al = mlo[a] - off - be * ta
        # endpoint values (linear) must be <= cN so that the multiplier cN - s is >= 0
        va, vb = al + be * ta, al + be * tb
        assert va.b <= cN.a + 1e-30 and vb.b <= cN.a + 1e-30, (a, va, vb, cN)
        smin = iv.mpf(min(mp.mpf(smin.a), mp.mpf(va.a), mp.mpf(vb.a)))
        alpha.append(al); beta.append(be); offsets.append(off)
    W = cN - smin
    # Bessel moments at c_a = T tau_a  (a = 0..N; c_0 = 0 handled as zero)
    cs = [T * iv.mpf(t) for t in taus]
    BM = BesselMoments(cs, K2)
    idx = list(range(par, K2, 2)); iK = [i for i in idx if i < K]; iT = [i for i in idx if i >= K]
    two_pi = iv.mpf(2) / iv.pi
    def nrm(i, l):
        return two_pi * iv.sqrt(iv.mpf((2 * i + 1) * (2 * l + 1))) * (iv.mpf(1) if ((l - i) // 2) % 2 == 0 else iv.mpf(-1))
    # L_{il} = cN delta_il + nrm * [ sum_a alpha_a (I0_{a+1}-I0_a) + (beta_a/T)(I1_{a+1}-I1_a) - cN I0_N ]
    Lrow = {}
    Rdiag_all = {}                                # R_j(c_N) for all j < K2 (both parities), for Lambda_K, Lambda_K2
    tt = time.time()
    for j in range(K2):
        I0, I1 = BM.moments(j, j)
        Rdiag_all[j] = two_pi * iv.mpf(2 * j + 1) * I0[-1]
        if j % 2 == par and j < K:
            Lrow[(j, j)] = (I0, I1)
    for i in iK:
        for l in idx:
            if l < i:
                continue
            if (i, l) not in Lrow:
                Lrow[(i, l)] = BM.moments(i, l)
    print("moments done: %.1fs" % (time.time() - tt), flush=True)
    def Lentry(i, l):
        I0, I1 = Lrow[(min(i, l), max(i, l))]
        acc = iv.mpf(0)
        prev0, prev1 = iv.mpf(0), iv.mpf(0)
        for a in range(N):
            acc = acc + alpha[a] * (I0[a] - prev0) + (beta[a] / T) * (I1[a] - prev1)
            prev0, prev1 = I0[a], I1[a]
        acc = acc - cN * I0[-1]
        v = nrm(i, l) * acc
        if i == l:
            v = v + cN
        return v
    Lm = {}
    for i in iK:
        for l in idx:
            Lm[(i, l)] = Lentry(i, l)
    def M(i, l):
        return (cN if i == l else iv.mpf(0)) - Lm[(i, l)]
    # tail bounds
    LamK = two_pi * cs[-1] - sum((Rdiag_all[j] for j in range(K)), iv.mpf(0))
    LamK2 = two_pi * cs[-1] - sum((Rdiag_all[j] for j in range(K2)), iv.mpf(0))
    LamK = iv.mpf([0, LamK.b]); LamK2 = iv.mpf([0, LamK2.b])
    gamma = cN - W * LamK
    rho = W * LamK2
    assert gamma.a > 0, gamma
    gc = g_coeffs(T, K2, par); gn2 = gnorm2(T, par)
    gtail_K2 = gn2 - sum((gc[l] ** 2 for l in idx), iv.mpf(0)); gtail_K2 = iv.mpf([0, gtail_K2.b])
    gtail_K = gn2 - sum((gc[l] ** 2 for l in iK), iv.mpf(0))
    n = len(iK) + 1
    Rm = [[iv.mpf(0)] * n for _ in range(n)]
    for p, i in enumerate(iK):
        for q, j in enumerate(iK):
            if q < p:
                continue
            gram = sum((M(i, l) * M(j, l) for l in iT), iv.mpf(0))
            eps = rho * iv.sqrt(iv.mpf([0, max(M(i, i).b, 0)]) * iv.mpf([0, max(M(j, j).b, 0)]))
            gram = gram + iv.mpf([-eps.b, eps.b])
            v = Lm[(i, j)] - gram / gamma
            Rm[p][q] = v; Rm[q][p] = v
        gram = sum((M(i, l) * gc[l] for l in iT), iv.mpf(0))
        eps = iv.sqrt(rho * iv.mpf([0, max(M(i, i).b, 0)])) * iv.sqrt(gtail_K2)
        gram = gram + iv.mpf([-eps.b, eps.b])
        # border coupling: the Y-column of e_i is -P^perp M e_i, that of the border is +P^perp g,
        # so their Gram entry is -<P^perp M e_i, P^perp g> and the Schur bound ADDS gram/gamma
        # (R155_052 Lemma 2.4; the archived runs subtracted it -- effect <= 1e-33, see there).
        v = gc[i] + gram / gamma
        Rm[p][n - 1] = v; Rm[n - 1][p] = v
    Rm[n - 1][n - 1] = -gtail_K / gamma
    # certification
    Rmid = np.array([[mid(x) for x in row] for row in Rm])
    wmax = max(wid(x) for row in Rm for x in row)
    ev, U = np.linalg.eigh(Rmid)
    result = None
    for r in range(0, 4):
        Usub = U[:, r + 1:]
        C = congruence(Usub, Rm)
        if cholesky_pd(C):
            # certified lower bound on the smallest eigenvalue of U^T R U by bisection
            lo_, hi_ = 0.0, float(ev[r + 1])
            for _ in range(30):
                mu = 0.5 * (lo_ + hi_)
                if cholesky_pd(C, iv.mpf(repr(mu))):
                    lo_ = mu
                else:
                    hi_ = mu
            result = dict(certified_upper_bound_sector=r, margin_lambda_min_UtRU=lo_)
            break
    out = dict(T=Tstr, par=par, K=K, K2=K2, grid=grid, N_bands=N, gtail_K_hi=hi(gtail_K), tau_N=taus[-1], cN=mid(cN), W=mid(W),
               gamma=mid(gamma), LamK_hi=hi(LamK), LamK2_hi=hi(LamK2), rho_hi=hi(rho),
               offsets_max=max(hi(o) for o in offsets), max_interval_width_R=wmax,
               R_eigs_midpoint=[float(x) for x in ev[:5]], result=result, runtime_s=time.time() - t0)
    print(json.dumps(out, indent=1))
    tag = Tstr.replace('.', 'p')
    suffix = '' if grid == 'default' else '_' + grid
    if (K, K2, cN_target) != (22, 36, 16.0):
        suffix += '_K%d_K2%d_c%g' % (K, K2, cN_target)
    fn = os.path.join(HERE, "r8a_01_%s_par%d%s.json" % (tag, par, suffix))
    if grid == 'default' and os.path.exists(fn):
        fn = fn[:-5] + "_rerun.json"                 # never overwrite an archived output
    json.dump(out, open(fn, "w"), indent=1)
    return out

if __name__ == '__main__':
    Tstr = sys.argv[1]; par = int(sys.argv[2])
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 22
    K2 = int(sys.argv[4]) if len(sys.argv) > 4 else 36
    cN = float(sys.argv[5]) if len(sys.argv) > 5 else 16.0
    grid = sys.argv[6] if len(sys.argv) > 6 else 'default'
    assert grid in ('default', 'fine')
    main(Tstr, par, K, K2, cN, grid)
