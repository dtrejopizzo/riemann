# =============================================================================
#  Paper 04 -- Partial sums of the Davenport-Heilbronn function at the
#              ordinates of its off-line zeros
#
#  Self-contained script (numpy, scipy, mpmath, matplotlib; no external data).
#  It produces every number, table and figure of the paper:
#
#    A  coefficients, functional equation, the four off-line zeros
#    B  exact partial sums D_DH(t;N), N = 10^4..10^9, by the Hurwitz zeta
#       identity (8); least-squares slopes; checks of Propositions 2.3, 6.1
#    C  direct double-precision summation compared with B (Appendix A)
#    D  scan of t in [100,200]: window maxima, kurtosis, resonance score,
#       prime-phase statistics at the largest local maxima
#    E  omega-class strata at N = 10^6
#    F  figures
#
#  Usage:   python reproduce_colab.py            (paper values)
#           python reproduce_colab.py --quick    (direct sums to 10^7, scan to 10^6)
#  Output:  results/results.txt and figures/*.pdf
# =============================================================================

import math
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")      # the parallelism is over values of t
from multiprocessing import Pool

import numpy as np
from scipy import stats
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
QUICK = "--quick" in sys.argv
NMAX_DIRECT = 10**7 if QUICK else 10**9      # part C
NMAX_SCAN = 10**6 if QUICK else 10**7        # part D
T1, T2, DT = 100.0, 200.0, 0.05              # scan window and step
SEED = 20240531                              # random multiplicative function
EPS = 0.01                                   # perturbation of kappa

KAPPA = (math.sqrt(10 - 2 * math.sqrt(5)) - 2) / (math.sqrt(5) - 1)
ABAR = (3 + KAPPA) / 5                       # mean of A(x) over a period
ZEROS_GUESS = [(0.8085, 85.70), (0.6508, 114.16), (0.5744, 166.48), (0.7243, 176.70)]
ORDINATES = [g for _, g in ZEROS_GUESS]      # rounded ordinates used throughout
N_GRID = [10**k for k in range(4, 10)]

_log = []


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    _log.append(s)


# ---------------------------------------------------------------- part A ----
def a_res(kappa=None):
    """(a_1,a_2,a_3,a_4) = (1, kappa, -kappa, -1); a_n depends on n mod 5, a_5=0."""
    k = mp.mpf(kappa) if kappa is not None else (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    return [mp.mpf(1), k, -k, mp.mpf(-1)]


def L_dh(s, coeff=None):
    a = coeff or a_res()
    return 5 ** (-s) * sum(a[r - 1] * mp.zeta(s, mp.mpf(r) / 5) for r in range(1, 5))


def tail_dh(s, N, coeff=None):
    """sum_{n>N} a_n n^{-s} for 5 | N (meromorphic continuation in s)."""
    assert N % 5 == 0
    a = coeff or a_res()
    return 5 ** (-s) * sum(a[r - 1] * mp.zeta(s, mp.mpf(N + r) / 5) for r in range(1, 5))


def part_A():
    mp.mp.dps = 30
    out("== A. coefficients, functional equation, zeros")
    out("kappa =", mp.nstr(a_res()[1], 15), "  a_1..a_5 = 1, kappa, -kappa, -1, 0")
    s = mp.mpc("0.3", "7")
    lhs = (mp.pi / 5) ** (-s / 2) * mp.gamma((s + 1) / 2) * L_dh(s)
    rhs = (mp.pi / 5) ** (-(1 - s) / 2) * mp.gamma((2 - s) / 2) * L_dh(1 - s)
    out("functional equation at s=0.3+7i: |lhs-rhs|/|lhs| =", mp.nstr(abs(lhs - rhs) / abs(lhs), 3))
    zs = []
    for sig, g in ZEROS_GUESS:
        z = mp.findroot(L_dh, mp.mpc(sig, g))
        zs.append(z)
        out("zero  %s + %s i   |L(1/2+i*%.2f)| = %s   |L(1/2+i*gamma)| = %s" % (
            mp.nstr(z.real, 10), mp.nstr(z.imag, 10), g,
            mp.nstr(abs(L_dh(mp.mpc(0.5, g))), 8), mp.nstr(abs(L_dh(mp.mpc(0.5, z.imag))), 8)))
    out("growth factor 10^(5*0.3085) = %.2f" % 10 ** (5 * 0.3085))
    return zs


# ---------------------------------------------------------------- part B ----
def exact_curve(t, Ns):
    mp.mp.dps = 30
    s = mp.mpc(0.5, t)
    L0 = L_dh(s)
    return L0, [L0 - tail_dh(s, N) for N in Ns]


def part_B():
    out("\n== B. exact partial sums at the rounded ordinates (Hurwitz identity)")
    res = {}
    for (sig, g) in ZEROS_GUESS:
        L0, D = exact_curve(g, N_GRID)
        mags = np.array([float(abs(d)) for d in D])
        r = stats.linregress(np.log(np.array(N_GRID, float)), np.log(mags))
        s = mp.mpc(0.5, g)
        out("t = %.2f  |L| = %.6f" % (g, float(abs(L0))))
        out("   |D(t;N)|, N=1e4..1e9: " + " ".join("%.6f" % m for m in mags))
        out("   slope %.6f +/- %.6f  R2 %.3f  p %.3f  mean %.4f  CV %.2f%%  |D(1e9)|/|D(1e4)| %.4f  "
            "(alpha_pred - slope)/se = %.0f" % (
                r.slope, r.stderr, r.rvalue ** 2, r.pvalue, mags.mean(),
                100 * mags.std() / mags.mean(), mags[-1] / mags[0], (sig - 0.5 - r.slope) / r.stderr))
        # Proposition 2.3 and Proposition 6.1
        for N, d in zip(N_GRID, D):
            err = float(abs(L0 - d))
            b23 = (1 + KAPPA) * (1 + float(abs(s)) / 0.5) * N ** -0.5
            E = L0 - d - ABAR * mp.mpf(N) ** (-s)
            b61 = ABAR * float(abs(s) * abs(s + 1)) * N ** -1.5 / 1.5
            out("   N=1e%d  |L-D| = %.3e  bound(2.3) = %.3e   |L-D-Abar N^-s| = %.3e  bound(6.1) = %.3e  "
                "sqrt(N)|L-D| = %.4f" % (round(math.log10(N)), err, b23, float(abs(E)), b61, err * N ** 0.5))
            assert err <= b23 and float(abs(E)) <= b61
        res[g] = (complex(L0), [complex(d) for d in D])
    out("Abar = (3+kappa)/5 = %.6f" % ABAR)
    return res


# ---------------------------------------------------------------- part C ----
def direct_curve(t):
    """Double-precision terms; each block of 10^7 terms is summed with math.fsum."""
    base = np.array([1.0, KAPPA, -KAPPA, -1.0, 0.0])
    CH = 10**7
    a = np.tile(base, CH // 5)
    outv = {}
    acc = 0j
    for blk in range(0, NMAX_DIRECT, CH):
        n = np.arange(blk + 1, blk + CH + 1, dtype=np.float64)
        ph = t * np.log(n)
        w = a / np.sqrt(n)
        re = w * np.cos(ph)
        im = -w * np.sin(ph)
        for N in N_GRID:
            if blk < N <= blk + CH:
                outv[N] = acc + complex(math.fsum(re[:N - blk]), math.fsum(im[:N - blk]))
        acc = acc + complex(math.fsum(re), math.fsum(im))
    return outv


def part_C(exact):
    out("\n== C. direct double-precision summation versus the exact values (N <= %.0e)" % NMAX_DIRECT)
    with Pool(4) as pool:
        curves = pool.map(direct_curve, ORDINATES)
    allerr = []
    for g, cv in zip(ORDINATES, curves):
        errs = []
        for N, d in zip(N_GRID, exact[g][1]):
            if N in cv:
                errs.append(abs(cv[N] - d) / abs(d))
        allerr += errs
        out("t = %.2f  relative errors: " % g + " ".join("%.1e" % e for e in errs))
    out("median %.1e   max %.1e   cases %d" % (np.median(allerr), max(allerr), len(allerr)))


# ---------------------------------------------------------------- part D ----
G = {}


def sieve(N):
    """omega(n), squarefree flag, a random completely multiplicative +-1 function."""
    om = np.zeros(N + 1, dtype=np.int8)
    sqf = np.ones(N + 1, dtype=bool)
    f = np.ones(N + 1, dtype=np.int8)
    rng = np.random.default_rng(SEED)
    primes = []
    for p in range(2, N + 1):
        if om[p] == 0:
            primes.append(p)
            om[p::p] += 1
            e = 1 if rng.random() < 0.5 else -1
            if p * p <= N:
                sqf[p * p::p * p] = False
            if e == -1:
                q = p
                while q <= N:
                    f[q::q] *= -1
                    q *= p
    return om, sqf, f, np.array(primes)


def scan_worker(t):
    logn, W, cps = G["logn"], G["W"], G["cps"]
    res = np.zeros((W.shape[0], len(cps)), dtype=complex)
    acc = np.zeros(W.shape[0], dtype=complex)
    lo = 0
    for j, hi in enumerate(cps):
        ph = t * logn[lo:hi]
        c, s_ = np.cos(ph), np.sin(ph)
        acc = acc + W[:, lo:hi] @ c - 1j * (W[:, lo:hi] @ s_)
        res[:, j] = acc
        lo = hi
    return res


def window_limit_worker(t):
    mp.mp.dps = 15
    s = mp.mpc(0.5, t)
    chi5 = [mp.mpf(1), mp.mpf(-1), mp.mpf(-1), mp.mpf(1)]
    return (float(abs(mp.zeta(s))), float(abs(L_dh(s, chi5))), float(abs(L_dh(s))),
            float(abs(L_dh(s, a_res(KAPPA + EPS)))))


def kurt(x):
    x = np.asarray(x)
    return float(np.mean((x - x.mean()) ** 4) / x.var() ** 2)


def local_max_top(mag, k=20):
    idx = np.where((mag[1:-1] > mag[:-2]) & (mag[1:-1] >= mag[2:]))[0] + 1
    return idx[np.argsort(mag[idx])[::-1][:k]]


def prime_R(tgrid, primes, sign):
    """Mean resultant length of the phases arg(a_p) - t log p over primes with a_p != 0."""
    m = sign != 0
    lp = np.log(primes[m].astype(float))
    sg = sign[m].astype(float)
    R = np.array([abs(np.sum(sg * np.exp(-1j * t * lp))) for t in tgrid]) / m.sum()
    return R, int(m.sum())


def part_D():
    out("\n== D. scan of t in [%g,%g], step %g, N <= %.0e" % (T1, T2, DT, NMAX_SCAN))
    N = NMAX_SCAN
    om, sqf, frand, primes = sieve(N)
    n = np.arange(1, N + 1)
    res5 = n % 5
    dh = np.array([0.0, 1.0, KAPPA, -KAPPA, -1.0])[res5]
    dhe = np.array([0.0, 1.0, KAPPA + EPS, -KAPPA - EPS, -1.0])[res5]
    chi = np.array([0.0, 1.0, -1.0, -1.0, 1.0])[res5]
    rs = 1.0 / np.sqrt(n)
    names = ["zeta", "L(s,chi5)", "f_rand", "L_DH", "L_DH^(eps)"]
    G["W"] = np.vstack([rs, chi * rs, frand[1:] * rs, dh * rs, dhe * rs])
    G["logn"] = np.log(n.astype(float))
    kmax = round(math.log10(N))
    cps = [int(round(10 ** (4 + j / 2))) for j in range(0, 2 * (kmax - 4) + 1)]
    G["cps"] = cps
    tgrid = np.round(np.arange(T1, T2 + DT / 2, DT), 6)
    with Pool(min(20, os.cpu_count())) as pool:
        R = np.array(pool.map(scan_worker, tgrid, chunksize=8))      # (t, function, checkpoint)
        lim = np.array(pool.map(window_limit_worker, tgrid, chunksize=16))
    cp = np.array(cps, float)
    # zeta with the term N^{1/2-it}/(1/2-it) removed
    main = cp[None, :] ** (0.5 - 1j * tgrid[:, None]) / (0.5 - 1j * tgrid[:, None])
    mags = {nm: np.abs(R[:, i, :]) for i, nm in enumerate(names)}
    mags["zeta, main term removed"] = np.abs(R[:, 0, :] - main)
    order = ["zeta", "zeta, main term removed", "L(s,chi5)", "f_rand", "L_DH", "L_DH^(eps)"]
    limits = {"zeta, main term removed": lim[:, 0].max(), "L(s,chi5)": lim[:, 1].max(),
              "L_DH": lim[:, 2].max(), "L_DH^(eps)": lim[:, 3].max()}
    out("checkpoints N:", cps)
    out("-- window maxima M_F(N) and the two fits of log M_F (least squares in log N, resp. sqrt(log N))")
    x1, x2 = np.log(cp), np.sqrt(np.log(cp))
    for nm in order:
        M = mags[nm].max(axis=0)
        y = np.log(M)
        r1, r2 = stats.linregress(x1, y), stats.linregress(x2, y)
        rss1 = np.sum((y - r1.intercept - r1.slope * x1) ** 2)
        rss2 = np.sum((y - r2.intercept - r2.slope * x2) ** 2)
        daic = len(cp) * math.log(rss1 / rss2)
        out("%-24s M: %s" % (nm, " ".join("%.4f" % v for v in M)))
        out("%-24s alpha = %.4f +/- %.4f   dAIC(power - sqrtlog) = %+.2f   limit max|F(1/2+it)| = %s" % (
            "", r1.slope, r1.stderr, daic, ("%.4f" % limits[nm]) if nm in limits else "-"))
    j6 = cps.index(10**6)
    out("-- kurtosis and resonance score (max/median) of |D_F(t;10^6)| on the grid")
    for nm in order:
        v = mags[nm][:, j6]
        out("%-24s kurtosis %.2f   RS %.2f   max %.3f  median %.3f" % (nm, kurt(v), v.max() / np.median(v), v.max(), np.median(v)))
    # prime phases, N = 10^6
    out("-- prime phases at N = 10^6: mean resultant length R, p = exp(-M R^2)")
    pr = primes[primes <= 10**6]
    signs = {"zeta": np.ones(len(pr)), "L(s,chi5)": np.array([0, 1, -1, -1, 1])[pr % 5],
             "L_DH": np.array([0, 1, 1, -1, -1])[pr % 5]}
    Rp = {}
    for nm in ["zeta", "L(s,chi5)", "L_DH"]:
        Rt, M = prime_R(tgrid, pr, signs[nm])
        Rp[nm] = Rt
        p = np.exp(-M * Rt ** 2)
        top = local_max_top(mags[nm][:, j6])
        out("%-10s M=%d  top-20 local maxima of |D_F(t;10^6)|: mean R %.4f  p<0.05: %d/20  p<0.001: %d/20   "
            "all %d grid points: mean R %.4f  p<0.05: %.1f%%  p<0.001: %.1f%%" % (
                nm, M, Rt[top].mean(), (p[top] < 0.05).sum(), (p[top] < 0.001).sum(),
                len(tgrid), Rt.mean(), 100 * (p < 0.05).mean(), 100 * (p < 0.001).mean()))
        out("           t of the 20 maxima: " + " ".join("%.2f" % v for v in np.sort(tgrid[top])))
    q = Rp["zeta"] * np.abs(1 - 1j * tgrid)
    out("zeta: R*|1-it| over the grid: min %.3f  mean %.3f  max %.3f" % (q.min(), q.mean(), q.max()))
    for half, sl in (("[100,150)", tgrid < 150), ("[150,200]", tgrid >= 150)):
        pz = np.exp(-len(pr) * Rp["zeta"][sl] ** 2)
        out("zeta, t in %s: p<0.05 at %.1f%% of the grid points" % (half, 100 * (pz < 0.05).mean()))
    out("-- single ordinates")
    for t in [84.2, 85.7, 90.0, 300.0, 1000.0]:
        row = []
        for nm in ["zeta", "L(s,chi5)", "L_DH"]:
            Rt, M = prime_R([t], pr, signs[nm])
            row.append("%s R=%.5f p=%.2g" % (nm, Rt[0], math.exp(-M * Rt[0] ** 2)))
        out("t=%7.2f  1/|1-it|=%.5f   " % (t, 1 / abs(1 - 1j * t)) + "   ".join(row))
    # wide curve of R for the figure
    tw = np.arange(20.0, 400.01, 0.5)
    curve = {nm: prime_R(tw, pr, signs[nm])[0] for nm in signs}
    return dict(om=om[:10**6 + 1], sqf=sqf[:10**6 + 1], tw=tw, curve=curve, npr=len(pr))


# ---------------------------------------------------------------- part E ----
def part_E(d):
    out("\n== E. omega-class strata, N = 10^6")
    N = 10**6
    om, sqf = d["om"], d["sqf"]
    n = np.arange(N + 1)
    a = np.array([0.0, 1.0, KAPPA, -KAPPA, -1.0])[n % 5]
    a[0] = 0
    nz = (a != 0)
    ln = np.log(np.maximum(n, 1).astype(float))
    sg = np.sign(a)
    out("-- mean resultant length of theta_n = arg(a_n) - t log n")
    for t in [114.16, 166.48]:
        rows = [("all n, 5 not | n", nz)] + [("squarefree, omega=%d" % k, nz & sqf & (om == k)) for k in (1, 2, 3, 4)]
        for lab, m in rows:
            M = int(m.sum())
            Rv = abs(np.sum(sg[m] * np.exp(-1j * t * ln[m]))) / M
            out("t=%.2f  %-22s M=%7d  R=%.2e  p=%.2f" % (t, lab, M, Rv, math.exp(-M * Rv * Rv)))
        out("t=%.2f  bound of Proposition 5.2: 5|t|log N/(2N) = %.2e" % (t, 5 * t * math.log(N) / (2 * N)))
    t = 85.7
    term = np.zeros(N + 1, dtype=complex)
    term[1:] = a[1:] * n[1:] ** -0.5 * np.exp(-1j * t * ln[1:])
    vec = {}
    for lab, base in (("squarefree n", sqf.copy()), ("all n", np.ones(N + 1, bool))):
        base[0] = False
        S = [term[base & (om == k)].sum() for k in range(0, 8)]
        tot = sum(S)
        e = sum(abs(x) ** 2 for x in S)
        out("-- classes at t=85.7, %s" % lab)
        for k, x in enumerate(S):
            if abs(x) > 0:
                out("   k=%d  |S_k| = %.3f  arg = %7.1f deg" % (k, abs(x), math.degrees(math.atan2(x.imag, x.real))))
        out("   |sum| = %.4f   (sum|S_k|^2)^(1/2) = %.4f   calR = %.4f   r = calR^2-1 = %.4f" % (
            abs(tot), math.sqrt(e), abs(tot) / math.sqrt(e), abs(tot) ** 2 / e - 1))
        vec[lab] = S
    d2 = math.degrees(math.atan2(vec["squarefree n"][2].imag, vec["squarefree n"][2].real))
    d3 = math.degrees(math.atan2(vec["squarefree n"][3].imag, vec["squarefree n"][3].real))
    sep = abs(d2 - d3) % 360
    out("   angle between S_2 and S_3 (squarefree): %.1f deg" % min(sep, 360 - sep))
    return vec["squarefree n"]


# ---------------------------------------------------------------- part F ----
def part_F(exact, d, Sflat):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": 0.3})
    fd = os.path.join(HERE, "figures")
    os.makedirs(fd, exist_ok=True)
    Nh = [5 * int(round(10 ** (4 + j / 4) / 5)) for j in range(0, 21)]
    curves = {}
    for g in ORDINATES:
        L0, D = exact_curve(g, Nh)
        curves[g] = (complex(L0), np.array([complex(x) for x in D]))
    # Figure 1
    g = ORDINATES[0]
    L0, D = curves[g]
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    ax.semilogx(Nh, np.abs(D), "o-", ms=3.5, lw=1, label=r"$|D_{\rm DH}(85.70;N)|$")
    ax.axhline(abs(L0), color="k", ls="--", lw=0.8, label=r"$|L_{\rm DH}(\frac{1}{2}+85.70\,i)|$")
    ax.set_xlabel("$N$")
    ax.set_ylim(0.345, 0.365)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(fd, "partial_sums_rho1.pdf"))
    plt.close(fig)
    # Figure 2
    fig, axs = plt.subplots(2, 2, figsize=(6.6, 4.6), sharex=True)
    for ax, g, lab in zip(axs.flat, ORDINATES, [r"$\rho_1$", r"$\rho_2$", r"$\rho_3$", r"$\rho_4$"]):
        L0, D = curves[g]
        ax.semilogx(Nh, np.abs(D), "o-", ms=3, lw=1)
        ax.axhline(abs(L0), color="k", ls="--", lw=0.8)
        ax.set_title("%s,  $t=%.2f$" % (lab, g), fontsize=10)
    for ax in axs[1]:
        ax.set_xlabel("$N$")
    fig.tight_layout()
    fig.savefig(os.path.join(fd, "partial_sums_four_zeros.pdf"))
    plt.close(fig)
    # Figure 3
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    tw = d["tw"]
    ax.semilogy(tw, d["curve"]["zeta"], lw=0.9, label=r"$\zeta$")
    ax.semilogy(tw, d["curve"]["L(s,chi5)"], lw=0.7, label=r"$L(s,\chi_5)$")
    ax.semilogy(tw, d["curve"]["L_DH"], lw=0.7, label=r"$L_{\rm DH}$")
    ax.semilogy(tw, 1 / np.abs(1 - 1j * tw), "k--", lw=0.9, label=r"$1/|1-it|$")
    ax.axhline(math.sqrt(math.log(20) / d["npr"]), color="gray", ls=":", lw=0.9)
    ax.set_xlabel("$t$")
    ax.set_ylabel("$R$")
    ax.legend(ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(fd, "prime_phase_R.pdf"))
    plt.close(fig)
    # Figure 4
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    pos = 0j
    for k, x in enumerate(Sflat):
        if abs(x) == 0:
            continue
        ax.annotate("", xy=((pos + x).real, (pos + x).imag), xytext=(pos.real, pos.imag),
                    arrowprops=dict(arrowstyle="->", color="C%d" % k, lw=1.4))
        mid = pos + x / 2
        ax.text(mid.real, mid.imag, " $k=%d$" % k, color="C%d" % k, fontsize=9)
        pos += x
    ax.annotate("", xy=(pos.real, pos.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="k", lw=2))
    ax.text(pos.real / 2, pos.imag / 2, r"  $D^\flat$", fontsize=9)
    ax.set_xlim(-2.8, 1.6)
    ax.set_ylim(-1.2, 2.6)
    ax.set_aspect("equal")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    fig.tight_layout()
    fig.savefig(os.path.join(fd, "omega_class_vectors.pdf"))
    plt.close(fig)
    # Figure 5
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    Na = np.array(Nh, float)
    for g, lab in zip(ORDINATES, [r"$\rho_1$", r"$\rho_2$", r"$\rho_3$", r"$\rho_4$"]):
        L0, D = curves[g]
        ax.loglog(Nh, np.abs(L0 - D), "o", ms=3, label="%s, $t=%.2f$" % (lab, g))
    ax.loglog(Nh, ABAR * Na ** -0.5, "k--", lw=0.9, label=r"$\bar A\,N^{-1/2}$")
    ax.set_xlabel("$N$")
    ax.set_ylabel(r"$|L_{\rm DH}(\frac{1}{2}+it)-D_{\rm DH}(t;N)|$")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(fd, "convergence_rate.pdf"))
    plt.close(fig)
    out("\n== F. figures written to figures/")


if __name__ == "__main__":
    t0 = time.time()
    part_A()
    exact = part_B()
    print("[%.0f s]" % (time.time() - t0), flush=True)
    part_C(exact)
    print("[%.0f s]" % (time.time() - t0), flush=True)
    d = part_D()
    print("[%.0f s]" % (time.time() - t0), flush=True)
    Sflat = part_E(d)
    part_F(exact, d, Sflat)
    out("\ntotal time %.0f s" % (time.time() - t0))
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    name = "results_quick.txt" if QUICK else "results.txt"
    with open(os.path.join(HERE, "results", name), "w") as fh:
        fh.write("\n".join(_log) + "\n")
