#!/usr/bin/env python3
"""R186_040 — Head-block theory of the pencil (Neg_T, Pos_T) on P_T.   (self-contained; imports r034_det.py)

Usage: python3 r040_head.py [M=40] [M_big=60]      (approx. 1-3 min total)

For each window T it computes:
  (1) generalized pencil  Neg_T u = beta Pos_T u  on P_T (scipy eigh);  H_T := {u_j : 1 - beta_j < delta}  (delta = e^-1, 1e-3)
      and, for each head direction: parity, peak frequency of |u^|^2, spectral centroid, spectral mass inside/outside
      of {sigma_T<0}, mass per negative component, overlap with the Shannon subspace (prolates of S_T) and with the
      space of piecewise Tate exponentials E_k (R186_024);
  (2) exact decomposition  1 - beta_j = (Pos - Neg)(u_j)/Pos(u_j)  with
      Pos = Pos_inf + Pos_P  (symbols m·1_{sigma>0},  -comb·1_{sigma>0}),  Neg = Neg_inf + Neg_P  (symbols -m·1_{sigma<0}, comb·1_{sigma<0}),
      Pos = Pos_near + Pos_far (|tau| < tau_last  /  |tau| > tau_last),
      and the unweighted version: leakage L_out = (1/pi) int_{sigma>0} |u^|^2  and the averages  sbar_+ = Pos/L_out,  sbar_- = Neg/L_in;
  (3) ladder -log(1 - beta_j) against the ladder of the prolates of S_T (full negative set), of the first interval only,
      and the Slepian asymptotic  log((1-lam_n)/(1-lam_{n-1})) = log(8c/n),  c = T·tau_1;
  (4) count of nearly-balanced directions against N(T*) (Zhu, T* = 2 pi e^{2T}), N_Sh, number of negative components,
      components with partial Shannon number >= 1/2, and the Jensen budget  T·tau/pi;
  (5) version without lambda_A (from sigma and Slepian): pencil (Neg,Pos) restricted to the Shannon subspace of S_T in P_T and
      Rayleigh quotient of a_T on the projected prolates.
Windows: 0.36, 0.45, 1/2 log 3, 0.62, log 2, 0.75, 1/2 log 5 (M) and 0.9, 1.0 (M_big; falsifier, double precision:
          1 - beta_j reliable only above ~1e-10; the count with threshold 1e-3 and e^-1 and the high ladder steps if that holds too).
"""
import sys, numpy as np, scipy.linalg as sla
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn
import r034_det as R

GAMMA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
         52.970321, 56.446248, 59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158, 75.704691, 77.144840,
         79.337375, 82.910381, 84.735493, 87.425275, 88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851]

def comb(T, tau):
    tau = np.atleast_1d(np.asarray(tau, float)); s = np.zeros_like(tau)
    for n, lp in R.contacts(T): s += 2 * lp / np.sqrt(n) * np.cos(tau * np.log(n))
    return s

def neg_set_full(T, h=2e-3):
    """{sigma_T<0} in [0, 1.1·2pi e^A] (prop:band: tau_last <= tau_lo < 2pi e^A e^{1/tau+...})."""
    A = sum(2 * lp / np.sqrt(n) for n, lp in R.contacts(T))
    tmax = 1.1 * 2 * np.pi * np.exp(A) + 10
    comps, zs = R.neg_set(T, tmax=tmax, h=h)
    return comps, zs

def op_on_set(T, M, comps, weight, nq=200):
    """(1/2pi) int_R  weight(tau) 1_{comps}(|tau|) phi^_k phi^_l  = (1/pi) int_0^oo (even)."""
    xg, wg = NL.leggauss(nq); N = np.zeros((M, M))
    for lo, hi in comps:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        N += np.einsum('klt,t->kl', R.fhat(T, M, t), weight(t) * w) / np.pi
    return N

def uhat2(T, c, tau):
    """|u^(tau)|^2 for orthonormal Legendre coefficients c (normalization (1/2pi) int |u^|^2 = ||u||^2)."""
    M = len(c); ck = np.sqrt((2 * np.arange(M) + 1) * 2 * T)
    J = np.array([spherical_jn(k, tau * T) for k in range(M)])
    val = ((c * ck)[:, None] * (1j ** np.arange(M))[:, None] * J).sum(0)
    return np.abs(val) ** 2

def tate_blocks(T, M, k):
    """E_k = span{e^{+-x/2} 1_B : B block} (R186_024), Legendre coordinates (truncated to degree < M)."""
    edges = np.linspace(-T, T, k + 1); xg, wg = NL.leggauss(80); cols = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        y = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg; F = R.legbasis(T, M, y)
        cols.append((F * w) @ np.exp(y / 2)); cols.append((F * w) @ np.exp(-y / 2))
    return np.array(cols).T

def window(T, M, nu=400, delta=np.exp(-1), verbose=True):
    A, A0, ta, tb = R.build_x(T, M, nu); Pr = A - A0
    comps, zs = neg_set_full(T); tau_last = comps[-1][1]
    Neg = op_on_set(T, M, comps, lambda t: -R.sigma_T(T, t)); Pos = A + Neg
    NegInf = op_on_set(T, M, comps, lambda t: -R.m_arch(t)); NegP = op_on_set(T, M, comps, lambda t: comb(T, t))
    PosInf = A0 + NegInf; PosP = Pr + NegP               # Pos_inf = R[m 1_{s>0}]R,  Pos_P = R[-comb 1_{s>0}]R
    gaps = [(comps[i][1], comps[i + 1][0]) for i in range(len(comps) - 1)]
    PosNear = op_on_set(T, M, gaps, lambda t: R.sigma_T(T, t)); PosFar = Pos - PosNear
    S = op_on_set(T, M, comps, lambda t: np.ones_like(t))          # time-band of the negative set
    S1 = op_on_set(T, M, comps[:1], lambda t: np.ones_like(t))     # first interval only
    Z = R.null_basis([ta, tb]); P = lambda X: Z.T @ X @ Z
    AP, NP, PP = P(A), P(Neg), P(Pos)
    beta, Y = sla.eigh(NP, PP); beta, Y = beta[::-1], Y[:, ::-1]   # beta_1 >= beta_2 >= ...
    lamA = np.linalg.eigvalsh(AP)[0]
    meas = sum(b - a for a, b in comps); NSh = 2 * T * meas / np.pi
    Tstar = 2 * np.pi * np.exp(2 * T); NZ = sum(g <= Tstar for g in GAMMA)
    nSh_comp = [2 * T * (b - a) / np.pi for a, b in comps]
    # prolates of S_T (L2) and Shannon subspace within P_T
    lamS, US = np.linalg.eigh(S); lamS, US = lamS[::-1], US[:, ::-1]
    lamS1 = np.linalg.eigvalsh(S1)[::-1]
    lamSP, USP = np.linalg.eigh(P(S)); lamSP, USP = lamSP[::-1], USP[:, ::-1]
    k = int(np.ceil(NSh)); Uk = np.linalg.qr(Z.T @ US[:, :k])[0]   # prolates projected onto P_T, orthonormalized
    # pencil restricted to the Shannon subspace (without lambda_A): beta^Sh
    betaSh = sla.eigh(Uk.T @ NP @ Uk, Uk.T @ PP @ Uk, eigvals_only=True)[::-1]
    rayS = [(USP[:, n] @ AP @ USP[:, n]) for n in range(k)]
    E5 = tate_blocks(T, M, 5); E9 = tate_blocks(T, M, 9)
    def proj_mass(c, B):          # mass of c in span(B) (Legendre coordinates)
        Q = np.linalg.qr(B)[0]; return np.linalg.norm(Q.T @ c) ** 2
    tgrid = np.linspace(0, tau_last + 20, int((tau_last + 20) / 0.01) + 1)
    head = []
    nhead = max(int((1 - beta < delta).sum()), 1)
    for j in range(min(nhead + 2, len(beta))):
        y = Y[:, j]; y = y / np.linalg.norm(y); c = Z @ y
        pos, neg = y @ PP @ y, y @ NP @ y
        d = dict(j=j + 1, beta=beta[j], one_minus=1 - beta[j], pos=pos, neg=neg,
                 pos_inf=y @ P(PosInf) @ y, pos_P=y @ P(PosP) @ y, neg_inf=y @ P(NegInf) @ y, neg_P=y @ P(NegP) @ y,
                 pos_near=y @ P(PosNear) @ y, pos_far=y @ P(PosFar) @ y,
                 even=np.linalg.norm(c[0::2]) ** 2, L_in=y @ P(S) @ y)
        d['L_out'] = 1 - d['L_in']; d['sbar_plus'] = pos / d['L_out']; d['sbar_minus'] = neg / d['L_in']
        u2 = uhat2(T, c, tgrid); d['peak'] = tgrid[np.argmax(u2)]
        d['centroid'] = (tgrid * u2).sum() / u2.sum()
        d['mass_comp'] = [ (np.trapz(u2[(tgrid >= a) & (tgrid <= b)], tgrid[(tgrid >= a) & (tgrid <= b)]) / np.pi) for a, b in comps]
        d['in_Sh'] = np.linalg.norm(Uk.T @ y) ** 2
        d['in_ShP'] = np.linalg.norm(USP[:, :k].T @ y) ** 2
        d['in_E5'] = proj_mass(c, E5); d['in_E9'] = proj_mass(c, E9)
        d['in_prol_j'] = [abs(US[:, n] @ c) ** 2 for n in range(min(k + 2, M))]
        head.append(d)
    out = dict(T=T, M=M, lamA=lamA, beta=beta, comps=comps, zs=zs, tau_last=tau_last, meas=meas, NSh=NSh, Tstar=Tstar, NZ=NZ,
               nSh_comp=nSh_comp, lamS=lamS, lamS1=lamS1, lamSP=lamSP, betaSh=betaSh, rayS=rayS, head=head, nhead=nhead, k=k)
    if verbose: report(out)
    return out

def report(o):
    T, beta, comps = o['T'], o['beta'], o['comps']
    name = {0.5 * np.log(3): '1/2 log 3', 0.5 * np.log(5): '1/2 log 5', np.log(2): 'log 2'}.get(T, '%.4f' % T)
    print(f"\n==================== T = {name} = {T:.5f}   M = {o['M']}   contacts {[n for n,_ in R.contacts(T)]}")
    print(f"negative set: {len(comps)} components, |{{s<0}}| = {o['meas']:.3f}, tau_last = {o['tau_last']:.3f}, N_Sh = {o['NSh']:.2f}, "
          f"T* = {o['Tstar']:.2f}, N(T*) = {o['NZ']}, Jensen budget T·tau_last/pi = {T*o['tau_last']/np.pi:.2f}, T·T*/pi = {T*o['Tstar']/np.pi:.2f}")
    print("   components (a,b | partial N_Sh): " + ", ".join(f"({a:.2f},{b:.2f}|{n:.2f})" for (a, b), n in zip(comps, o['nSh_comp'])))
    print(f"   #comp with partial N_Sh >= 1/2: {sum(n >= 0.5 for n in o['nSh_comp'])};  >= 1: {sum(n >= 1 for n in o['nSh_comp'])}")
    om = 1 - beta
    print(f"lambda_A = {o['lamA']:+.3e};  1-beta_j (j=1..8): " + " ".join(f"{v:.2e}" for v in om[:8]))
    print(f"   #(1-beta<1e-3) = {(om<1e-3).sum()}   #(1-beta<e^-1) = {(om<np.exp(-1)).sum()}   #(1-beta<1/2) = {(om<0.5).sum()}   #beta>1 = {(beta>1).sum()}")
    steps = np.log(om[1:9] / om[:8]); print("   ladder: steps log((1-b_{j+1})/(1-b_j)) = " + " ".join(f"{s:.2f}" for s in steps[:o['nhead']+1]))
    lS = o['lamS']; print(f"   prolates of S_T (full negative set): lam = " + " ".join(f"{v:.4f}" for v in lS[:o['k']+2]))
    print("      steps log((1-lam_n)/(1-lam_{n-1})) = " + " ".join(f"{s:.2f}" for s in np.log((1 - lS[1:o['k']+2]) / (1 - lS[:o['k']+1]))))
    lS1 = o['lamS1']; c1 = T * comps[0][1]
    print(f"   prolates of the first interval (c = T·tau_1 = {c1:.3f}): lam = " + " ".join(f"{v:.4f}" for v in lS1[:5])
          + " ; steps = " + " ".join(f"{s:.2f}" for s in np.log((1 - lS1[1:5]) / (1 - lS1[:4]))) + " ; Slepian log(8c/n) = "
          + " ".join(f"{np.log(8*c1/n):.2f}" for n in range(1, 5)))
    print(f"   pencil restricted to the projected Shannon subspace (dim {o['k']}, without lambda_A): 1-beta^Sh = "
          + " ".join(f"{1-v:.2e}" for v in o['betaSh'][:4]) + " ; Rayleigh a_T on prolates of S|P: " + " ".join(f"{v:+.3f}" for v in o['rayS'][:6]))
    print("   --- head (threshold e^-1): j | 1-b | Pos = Pos_inf + Pos_P | Neg = Neg_inf + Neg_P | Pos_near/Pos_far | parity | peak | centr | L_in | sbar+ | sbar- | mass in Sh(L2)/Sh(P)/E5/E9")
    for d in o['head']:
        print(f"   {d['j']:2d} | {d['one_minus']:.2e} | {d['pos']:.4f} = {d['pos_inf']:+.4f} {d['pos_P']:+.4f} | {d['neg']:.4f} = {d['neg_inf']:+.4f} {d['neg_P']:+.4f} | "
              f"{d['pos_near']:.4f}/{d['pos_far']:.4f} | {d['even']:.3f} | {d['peak']:5.2f} | {d['centroid']:6.2f} | {d['L_in']:.4f} | {d['sbar_plus']:.3f} | {d['sbar_minus']:.3f} | "
              f"{d['in_Sh']:.4f}/{d['in_ShP']:.4f}/{d['in_E5']:.3f}/{d['in_E9']:.3f}")
        print("        |u^|^2 mass per negative component: " + " ".join(f"{m:.3f}" for m in d['mass_comp']) + "   | in prolates j=0..: " + " ".join(f"{m:.3f}" for m in d['in_prol_j'][:6]))

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    Mb = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    rows = []
    for T in [0.36, 0.45, 0.5 * np.log(3), 0.62, np.log(2), 0.75, 0.5 * np.log(5)]:
        rows.append(window(T, M))
    print("\n\n######## FALSIFIER: T = 0.9, 1.0 (double precision, M = %d; only the count and high steps are reliable) ########" % Mb)
    for T in [0.9, 1.0]:
        rows.append(window(T, Mb))
    import os
    zf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zeros150.npy')
    gam = list(np.load(zf)) if os.path.exists(zf) else GAMMA
    run_zero_checks(rows, gam)
    for f in sys.argv[3:]: postprocess_mp(f, gam)
    print("\n=== Summary of counts:  T | N(T*) | #comp | #comp(N_Sh,i>=1/2) | N_Sh | #(1-b<1e-3) | #(1-b<e^-1) | #(1-b<1/2) | T·tau_last/pi")
    for o in rows:
        om = 1 - o['beta']
        print(f"   {o['T']:.4f} | {o['NZ']:2d} | {len(o['comps']):2d} | {sum(n>=0.5 for n in o['nSh_comp']):2d} | {o['NSh']:5.2f} | {(om<1e-3).sum():2d} | {(om<np.exp(-1)).sum():2d} | {(om<0.5).sum():2d} | {o['T']*o['tau_last']/np.pi:5.2f}")

# ---------------------------------------------------------------------------------------------------------------
# Redirection R186_112: vanishing at zeros, part above T*, and postprocessing of the mp runs (r040_head_mp.py)
# ---------------------------------------------------------------------------------------------------------------
def zero_check(T, M, cvec, comps, gam, lamA_dir=None, verbose_label=''):
    """For a vector (Legendre coords., ||u||=1): a_T(u) = sum_rho |u^(gamma)|^2 = 2 sum_{gamma>0} |u^(gamma)|^2 (lem:roughEF, Paper 47).
    Returns: sum over gamma <= T*, sum over the 150 zeros, tail by density (1/pi) int_{gamma_150}^oo m |u^|^2,
    and the decomposition of the geometric side: a_{<T*} = (1/pi) int_0^{T*} sigma |u^|^2, a_{>T*}, a_{>tau_last} (= Pos_far)."""
    Tstar = 2 * np.pi * np.exp(2 * T); tau_last = comps[-1][1]
    g2 = uhat2(T, cvec, np.array(gam)); s_low = 2 * g2[np.array(gam) <= Tstar].sum(); s_150 = 2 * g2.sum()
    xg0, wg0 = NL.leggauss(300)
    def integ(a, b, n=None):            # panels of length <= 8 with 300 Gauss nodes each
        s1 = s2 = 0.0; npan = max(1, int(np.ceil((b - a) / 8.0))); ed = np.linspace(a, b, npan + 1)
        for lo, hi in zip(ed[:-1], ed[1:]):
            t = (hi + lo) / 2 + (hi - lo) / 2 * xg0; w = (hi - lo) / 2 * wg0; u2 = uhat2(T, cvec, t)
            s1 += (R.sigma_T(T, t) * u2 * w).sum() / np.pi; s2 += (R.m_arch(t) * u2 * w).sum() / np.pi
        return s1, s2
    a_lo, _ = integ(0, Tstar); a_mid, _ = integ(Tstar, tau_last)
    # tail > tau_last: sigma>0, |u^|^2 ~ 1/tau^2: integrate piecewise up to 1e5 and estimate the remainder
    a_far = 0.0; m_far150 = 0.0
    def integ_log(a, b):                # tail: (1/pi) int_a^b sigma|u^|^2, m|u^|^2 with substitution t = e^s (log panels)
        s1 = s2 = 0.0; ed = np.exp(np.linspace(np.log(a), np.log(b), int(np.ceil((np.log(b) - np.log(a)) / 0.05)) + 1))
        for lo, hi in zip(ed[:-1], ed[1:]):
            ss, mm = integ(lo, hi); s1 += ss; s2 += mm
        return s1, s2
    a_far, _ = integ_log(tau_last, 2e5 * max(1.0, tau_last / 100))
    _, m_far150 = integ_log(gam[-1], 2e5 * max(1.0, tau_last / 100))
    return dict(s_low=s_low, s_150=s_150, tail_dens=m_far150, a_lo=a_lo, a_mid=a_mid, a_far=a_far, Tstar=Tstar)

def run_zero_checks(rows, gam):
    print("\n=== Vanishing at zeros (lem:roughEF): a_T(u_j) = (1-beta_j)·Pos(u_j) against 2·sum_{gamma<=T*}|u^(gamma)|^2 and 2·sum_{150 zeros};"
          " geometric side split into [0,T*], [T*,tau_last], [tau_last,oo)")
    for o in rows:
        T, M = o['T'], o['M']; A, A0, ta, tb = R.build_x(T, M, 400); comps = o['comps']
        Neg = op_on_set(T, M, comps, lambda t: -R.sigma_T(T, t)); Pos = A + Neg
        Z = R.null_basis([ta, tb]); beta, Y = sla.eigh(Z.T @ Neg @ Z, Z.T @ Pos @ Z); beta, Y = beta[::-1], Y[:, ::-1]
        print(f"--- T = {T:.4f}  T* = {2*np.pi*np.exp(2*T):.1f}   j | 1-beta | a_T(u) | 2sum(g<=T*) | 2sum_150 | tail dens. | a_[0,T*] | a_[T*,tau_last] | a_far | |u^(g_k)|^2, g_k<=T*")
        for j in range(min(o['nhead'] + 2, 10)):
            y = Y[:, j] / np.linalg.norm(Y[:, j]); c = Z @ y; pos = y @ (Z.T @ Pos @ Z) @ y; a = (1 - beta[j]) * pos
            r = zero_check(T, M, c, comps, gam); vals = uhat2(T, c, np.array([g for g in gam if g <= r['Tstar']]))
            print(f"   {j+1:2d} | {1-beta[j]:.2e} | {a:+.3e} | {r['s_low']:.2e} | {r['s_150']:.3e} | {r['tail_dens']:.2e} | {r['a_lo']:+.3e} | {r['a_mid']:+.3e} | {r['a_far']:.3e} | "
                  + " ".join(f"{v:.1e}" for v in vals))

def postprocess_mp(npz, gam):
    d = np.load(npz); T, M = float(d['T']), int(d['M']); comps = [tuple(x) for x in d['comps']]; om = d['om']
    print(f"\n=== mp (dps 40) T = {T}  M = {M}: lambda_A = {d['lamA']:.4e};  1-beta_j = " + " ".join(str(s) for s in d['om_str'][:12]))
    print("   pasos: " + " ".join(f"{np.log(om[j+1]/om[j]):.2f}" for j in range(11)))
    for thr in (1e-4, 1e-3, 1e-2, np.exp(-1)): print(f"   #(1-beta<{thr:.2g}) = {(om < thr).sum()}", end=';')
    Tstar = 2 * np.pi * np.exp(2 * T); print(f"   N(T*) = {sum(g <= Tstar for g in gam)}   N_Sh = {2*T*sum(b-a for a,b in comps)/np.pi:.2f}   #comp = {len(comps)}")
    S = op_on_set(T, M, comps, lambda t: np.ones_like(t))
    print("   j | 1-beta | par | pico | centroide | L_in | 2sum(g<=T*)|u^|^2 | 2sum_150 | a_[0,T*] | a_[T*,tau_last] | a_far || |u^(g_k)|^2 en g_k<=T*")
    tgrid = np.linspace(0, 80, 8001)
    for j, c in enumerate(d['vecs'][:12]):
        u2 = uhat2(T, c, tgrid); r = zero_check(T, M, c, comps, gam); vals = uhat2(T, c, np.array([g for g in gam if g <= Tstar]))
        print(f"   {j+1:2d} | {d['om_str'][j]} | {np.linalg.norm(c[0::2])**2:.2f} | {tgrid[np.argmax(u2)]:5.2f} | {(tgrid*u2).sum()/u2.sum():5.2f} | {c @ S @ c:.3f} | "
              f"{r['s_low']:.2e} | {r['s_150']:.2e} | {r['a_lo']:+.2e} | {r['a_mid']:+.2e} | {r['a_far']:.2e} || " + " ".join(f"{v:.1e}" for v in vals))
