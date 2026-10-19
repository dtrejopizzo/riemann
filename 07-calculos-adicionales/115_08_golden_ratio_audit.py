#!/usr/bin/env python3
"""
115.08 -- Audit of the "golden ratio" in sigma = e^{-(log 2)^2}.

Question:  sigma = 0.618503...  and  1/phi = 0.618034...
           A hidden identity, or a near-coincidence?

Answered with three measurements (fig 1) and three tests on actual
arithmetic data (fig 2).  No fitting, no free factors.

Outputs:
  115_08_fig1_sigma_vs_phi.png
  115_08_fig2_phi_en_primos_y_ceros.png
  115_08_resultados.txt
"""

import itertools
import math
import os

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- palette
C_BLUE, C_ORANGE, C_AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, INK3 = "#141413", "#3d3d3a", "#73726c"
SURFACE, GRIDC = "#fcfcfb", "#e3e2dd"

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "axes.edgecolor": GRIDC, "axes.labelcolor": INK2,
    "xtick.color": INK3, "ytick.color": INK3,
    "text.color": INK, "font.size": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "grid.color": GRIDC, "grid.linewidth": 0.6,
    "lines.linewidth": 2.0,
})

# ---------------------------------------------------------- constants
LOG2 = math.log(2.0)
SIGMA = math.exp(-LOG2 ** 2)            # the constant of 115_04
PHI = (1.0 + math.sqrt(5.0)) / 2.0
INV_PHI = 1.0 / PHI
REL = abs(SIGMA - INV_PHI) / INV_PHI    # relative separation

out = []
def say(s=""):
    out.append(s)
    print(s)

say("=" * 68)
say("1. THE TWO NUMBERS, TO FULL PRECISION")
say("=" * 68)
say(f"  log 2            = {LOG2:.17f}")
say(f"  (log 2)^2        = {LOG2**2:.17f}")
say(f"  sigma = e^-(l2)^2= {SIGMA:.17f}")
say(f"  1/phi            = {INV_PHI:.17f}")
say(f"  sigma - 1/phi    = {SIGMA - INV_PHI:.3e}")
say(f"  relative error   = {REL:.4e}   ({100*REL:.4f} %)")
say()
say("  sigma = 1/phi  <=>  (log 2)^2 = log phi:")
say(f"     (log 2)^2 = {LOG2**2:.15f}")
say(f"     log phi   = {math.log(PHI):.15f}")
say(f"     differ by {math.log(PHI)-LOG2**2:.3e}  -> NOT the same number.")
say("  They agree to 3 significant digits; they differ in the 4th.")
say()

# ------------------------------------------------------------- PANEL A
# sigma_b = exp(-(log b)^2): where the 2 really comes from.
B_STAR = math.exp(math.sqrt(math.log(PHI)))   # base where sigma_b = 1/phi
say("=" * 68)
say("2. WHERE THE 2 COMES FROM:  N_t counts DIGITS IN BASE 2")
say("=" * 68)
say("  r(m) ~ log m / log b  with b the base of the digital code.")
say("  With a generic base b:  sigma_b = exp(-(log b)^2).")
say(f"  sigma_2      = {SIGMA:.9f}")
say(f"  sigma_b=1/phi at b* = {B_STAR:.9f}   (not 2, but 2.0011)")
say("  => the golden value is not reached at the base of the code, but")
say("     0.05% further.  The 'appearance' is that log2 ~ sqrt(log phi).")
say()

# ------------------------------------------------------------- PANEL B
# How many simple constants fall equally close to sigma?
def catalogo_famosas():
    base = {
        "2": 2.0, "3": 3.0, "5": 5.0, "7": 7.0,
        "pi": math.pi, "e": math.e, "gamma": 0.5772156649015329,
        "sqrt2": math.sqrt(2), "sqrt3": math.sqrt(3), "sqrt5": math.sqrt(5),
        "ln2": LOG2, "ln3": math.log(3), "phi": PHI,
        "zeta3": 1.2020569031595943, "G": 0.9159655941772190,
    }
    vals = {}
    it = list(base.items())
    for (na, a), (nb, b) in itertools.product(it, it):
        cands = [(f"{na}+{nb}", a + b), (f"{na}-{nb}", a - b),
                 (f"{na}*{nb}", a * b), (f"{na}/{nb}", a / b),
                 (f"sqrt({na}*{nb})", math.sqrt(a * b)),
                 (f"{na}^(1/{nb})", a ** (1.0 / b))]
        try:
            cands.append((f"exp(-{na}/{nb})", math.exp(-a / b)))
            cands.append((f"{na}^-{nb}", a ** (-b)))
        except OverflowError:
            pass
        for name, v in cands:
            if math.isfinite(v) and 0.0 < v < 10.0:
                vals[name] = v
                vals["1/" + name] = 1.0 / v
    return np.array(sorted(set(round(v, 12) for v in vals.values()))), vals


def catalogo_cuadraticos(hmax=12):
    """(p + q*sqrt(d))/s, small height: the 'nice' algebraic numbers of degree<=2."""
    vals = []
    for d in (2, 3, 5, 6, 7, 10, 13):
        rd = math.sqrt(d)
        for p in range(-hmax, hmax + 1):
            for q in range(-hmax, hmax + 1):
                for s in range(1, hmax + 1):
                    v = (p + q * rd) / s
                    if 0.3 < v < 1.2:
                        vals.append(v)
    return np.array(sorted(set(np.round(vals, 12))))


fam_arr, fam_map = catalogo_famosas()
cua_arr = catalogo_cuadraticos()

rs = np.logspace(-6, -1.3, 260)
cnt_fam = np.array([np.sum(np.abs(fam_arr - SIGMA) / SIGMA < r) for r in rs])
cnt_cua = np.array([np.sum(np.abs(cua_arr - SIGMA) / SIGMA < r) for r in rs])
n_fam_at = int(np.sum(np.abs(fam_arr - SIGMA) / SIGMA < REL))
n_cua_at = int(np.sum(np.abs(cua_arr - SIGMA) / SIGMA < REL))

vecinos = sorted(
    [(abs(v - SIGMA) / SIGMA, n, v) for n, v in fam_map.items()
     if abs(v - SIGMA) / SIGMA < 3 * REL])[:10]

say("=" * 68)
say("3. CALIBRATION: HOW RARE IS IT TO BE WITHIN 0.076% OF A CONSTANT?")
say("=" * 68)
say(f"  catalogue A ({len(fam_arr)} values: simple combinations of pi,e,phi,")
say(f"    sqrt2,ln2,gamma,zeta3,...)  -> {n_fam_at} fall as close to sigma as 1/phi")
say(f"  catalogue B ({len(cua_arr)} values: (p+q*sqrt d)/s, height<=12)")
say(f"    -> {n_cua_at} fall as close to sigma as 1/phi")
say()
say("  Neighbours of sigma within 3x that distance (catalogue A):")
for rel, n, v in vecinos:
    say(f"    {n:>18s} = {v:.9f}   rel {rel:.2e}")
say()
say("  That is: at this precision the golden ratio is not a distinguished neighbour.")
say("  It has competition, and the eye picks the one it already knew.")
say()

# ------------------------------------------------------------- PANEL C
# Hard consequence: if sigma were 1/phi, the theorem of 115_04 would fail.
say("=" * 68)
say("4. DECIDING TEST: FORCE sigma = 1/phi AND SEE WHETHER THE THEOREM SURVIVES")
say("=" * 68)
say("  115_04:  h0_t - h2_t = N_t * log(1/sigma).")
say("  The theorem requires this to be (log2)^2 N_t = t^2 ab, with NO spurious factor.")
FACTOR = math.log(PHI) / LOG2 ** 2
say(f"  With sigma = e^-(log2)^2 :  log(1/sigma)/(log2)^2 = 1.000000000  (exact)")
say(f"  With sigma = 1/phi       :  log(phi)  /(log2)^2 = {FACTOR:.9f}")
say(f"  -> spurious factor of {100*(FACTOR-1):.4f} % at every t.")
say("  Since N_t ~ t^2 ab/(log2)^2, the ABSOLUTE error grows like t^2:")
ts = np.arange(1, 201)
ab = 1.0
N_t = ts.astype(float) ** 2 * ab / LOG2 ** 2
err_phi = N_t * abs(math.log(PHI) - LOG2 ** 2)
say(f"     t=10   -> discrepancy {err_phi[9]:.3f}")
say(f"     t=100  -> discrepancy {err_phi[99]:.3f}")
say(f"     t=200  -> discrepancy {err_phi[199]:.3f}   (and diverges)")
say("  The covolume leaves NO choice: 1/phi breaks the exact equality that")
say("  is the whole content of 115_04.  sigma is forced, and it is not phi.")
say()

# ============================================================== FIGURE 1
fig1, axes = plt.subplots(1, 3, figsize=(13.6, 4.3))

# --- A ---
ax = axes[0]
bb = np.linspace(1.55, 2.75, 600)
ax.plot(bb, np.exp(-np.log(bb) ** 2), color=C_BLUE, zorder=3)
ax.axhline(INV_PHI, color=C_ORANGE, ls="--", lw=1.6, zorder=2)
ax.plot([2.0], [SIGMA], "o", ms=8, color=C_BLUE, mec=SURFACE, mew=2, zorder=5)
ax.plot([B_STAR], [INV_PHI], "o", ms=8, color=C_ORANGE, mec=SURFACE, mew=2, zorder=5)
ax.annotate(f"base 2 (the binary code)\n$\\sigma={SIGMA:.6f}$",
            xy=(2.0, SIGMA), xytext=(2.10, 0.74), color=C_BLUE, fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=C_BLUE, lw=1))
ax.annotate(f"$1/\\varphi={INV_PHI:.6f}$\nreached at $b={B_STAR:.4f}$",
            xy=(2.35, INV_PHI), xytext=(2.30, 0.50), color=C_ORANGE, fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=C_ORANGE, lw=1))
# magnifier: at this scale the two points coincide; zoom 500x
axi = ax.inset_axes([0.10, 0.08, 0.36, 0.30])
bz = np.linspace(1.9985, 2.0035, 200)
axi.plot(bz, np.exp(-np.log(bz) ** 2), color=C_BLUE, lw=1.6)
axi.axhline(INV_PHI, color=C_ORANGE, ls="--", lw=1.2)
axi.plot([2.0], [SIGMA], "o", ms=5, color=C_BLUE, mec=SURFACE, mew=1)
axi.plot([B_STAR], [INV_PHI], "o", ms=5, color=C_ORANGE, mec=SURFACE, mew=1)
axi.set_xticks([2.000, 2.002]); axi.set_yticks([])
axi.tick_params(labelsize=7)
axi.set_title("zoom $\\times$500", fontsize=7.5, color=INK3, pad=2)
for sp in axi.spines.values():
    sp.set_color(GRIDC)
axi.spines["top"].set_visible(True); axi.spines["right"].set_visible(True)
ax.set_xlabel("base $b$ of the digital code")
ax.set_ylabel("$\\sigma_b=e^{-(\\log b)^2}$")
ax.set_title("A. The 2 comes from counting binary digits\nthe golden value sits at b=2.0011, not b=2",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- B ---
ax = axes[1]
ax.step(rs, cnt_fam, where="post", color=C_BLUE, label="simple constants")
ax.step(rs, cnt_cua, where="post", color=C_AQUA, label="quadratics of height$\\leq$12")
ax.axvline(REL, color=C_ORANGE, lw=1.6, ls="--")
ax.annotate("$1/\\varphi$ is\nhere", xy=(REL, 24), xytext=(REL * 0.28, 26),
            color=C_ORANGE, fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=C_ORANGE, lw=1))
ax.plot([2.63e-4], [1], "o", ms=7, color=INK3, mec=SURFACE, mew=1.5, zorder=6)
ax.annotate("$e^{-\\gamma/\\zeta(3)}$ is 3 times\nCLOSER than $1/\\varphi$",
            xy=(2.63e-4, 1), xytext=(1.6e-6, 5.0), color=INK3, fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=INK3, lw=1))
ax.text(4.5e-3, 7.5, "simple constants", color=C_BLUE, fontsize=8.5, ha="right")
ax.text(4.5e-3, 33, "quadratics $(p+q\\sqrt{d})/s$", color=C_AQUA,
        fontsize=8.5, ha="right")
ax.set_xscale("log"); ax.set_xlim(1e-6, 5e-3); ax.set_ylim(0, 40)
ax.set_xlabel("relative distance to $\\sigma$")
ax.set_ylabel("number of constants closer to $\\sigma$")
ax.set_title(f"B. At that distance there are already {n_fam_at+n_cua_at} candidates\nthe golden ratio is not distinguished",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- C ---
ax = axes[2]
ax.plot(ts, err_phi, color=C_ORANGE)
ax.plot(ts, np.zeros_like(ts, dtype=float), color=C_BLUE)
ax.set_ylim(-4, 70)
ax.text(ts[-1] * .98, 48, "with $\\sigma=1/\\varphi$: error $\\sim t^2$, diverges ",
        color=C_ORANGE, fontsize=8.5, va="top", ha="right")
ax.text(ts[-1] * .98, 2.0, "with $\\sigma=e^{-(\\log 2)^2}$: error ZERO, exact for all $t$",
        color=C_BLUE, fontsize=8.5, va="bottom", ha="right")
ax.set_xlabel("scale $t$")
ax.set_ylabel("$|(h^0_t-h^2_t)-\\frac{t^2}{2}B_{int}|$")
ax.set_title("C. The golden ratio breaks the theorem\nspurious factor 0.158%, error $\\sim t^2$",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

fig1.suptitle("$\\sigma=e^{-(\\log 2)^2}=0.618503\\ldots$  against  $1/\\varphi=0.618034\\ldots$   "
              "— agree to 3 digits, differ in the 4th",
              fontsize=11.5, color=INK, x=0.008, ha="left", y=0.995)
fig1.tight_layout(rect=[0, 0, 1, 0.94])
p1 = os.path.join(HERE, "115_08_fig1_sigma_vs_phi.png")
fig1.savefig(p1, dpi=170)
say(f"[fig] {p1}")

# ============================================================== FIGURE 2
say()
say("=" * 68)
say("5. AND IN THE PRIMES / THE ZEROS?  THREE TESTS ON ACTUAL DATA")
say("=" * 68)

# ---- zeta zeros (Riemann-Siegel with C0 correction, vectorised) ----
TWOPI = 2 * math.pi


def rs_theta(t):
    return (t / 2) * np.log(t / TWOPI) - t / 2 - math.pi / 8 \
        + 1 / (48 * t) + 7 / (5760 * t ** 3)


def zeros_up_to(T_MAX, step=0.0015, t0=10.0):
    """Zeros of Z on segments where N=floor(sqrt(t/2pi)) is constant.

    Each segment [2pi N^2, 2pi (N+1)^2) is vectorised without masks and
    processed separately, so memory stays bounded even for large T_MAX.
    """
    zs = []
    prev_t = prev_Z = None
    Nmax = int(math.floor(math.sqrt(T_MAX / TWOPI)))
    for Nseg in range(1, Nmax + 1):
        a = max(t0, TWOPI * Nseg ** 2)
        b = min(T_MAX, TWOPI * (Nseg + 1) ** 2)
        if b <= a:
            continue
        t = np.arange(a, b, step)
        if t.size < 2:
            continue
        th = rs_theta(t)
        Z = np.zeros_like(t)
        for n in range(1, Nseg + 1):               # main sum, N constant
            Z += np.cos(th - t * math.log(n)) / math.sqrt(n)
        Z *= 2.0
        u = np.sqrt(t / TWOPI)
        p = u - Nseg
        C0 = np.cos(TWOPI * (p * p - p - 1 / 16.0)) / np.cos(TWOPI * p)
        C0 = np.where(np.isfinite(C0), C0, 0.0)    # removable 0/0 at p=1/4,3/4
        Z += (1.0 if Nseg % 2 == 1 else -1.0) * u ** (-0.5) * C0
        if prev_t is not None:                     # seam between segments
            t = np.r_[prev_t, t]
            Z = np.r_[prev_Z, Z]
        k = np.nonzero(np.sign(Z[:-1]) != np.sign(Z[1:]))[0]
        zs.append(t[k] - Z[k] * (t[k + 1] - t[k]) / (Z[k + 1] - Z[k]))
        prev_t, prev_Z = t[-1], Z[-1]
    return np.concatenate(zs)


cache = os.path.join(HERE, "115_08_zeros.npy")
T_MAX = 75000.0
if os.path.exists(cache):
    gam = np.load(cache)
else:
    gam = zeros_up_to(T_MAX)
    np.save(cache, gam)

# check: against the Riemann-von Mangoldt formula and against mpmath
NT = rs_theta(T_MAX) / math.pi + 1
say(f"  zero check: found {len(gam)}, theoretical N(T) {NT:.1f}")
import mpmath
mpmath.mp.dps = 15
for j in (0, 9, 99, 999):
    if j < len(gam):
        ref = float(mpmath.im(mpmath.zetazero(j + 1)))
        say(f"    gamma_{j+1:<4d} computed {gam[j]:.6f}  exact {ref:.6f}"
            f"  err {abs(gam[j]-ref):.1e}")

d = np.diff(gam)
dens = np.log(gam[:-1] / (2 * math.pi)) / (2 * math.pi)   # von Mangoldt
s = d * dens                                              # normalised spacings
r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
r_mean, r_err = r.mean(), r.std() / math.sqrt(len(r))
R_GUE, R_POI = 0.5996, 0.3863
say(f"  zeros used: {len(gam)} (up to gamma={gam[-1]:.1f}); <s> = {s.mean():.4f}")
say()
say("  --- THE DATUM THAT SEEMS TO SUPPORT IT ---")
say(f"  statistic r (ratio of consecutive spacings), WHOLE sample:")
say(f"     measured {r_mean:.4f} +/- {r_err:.4f}")
say(f"     GUE     {R_GUE:.4f}   <-- at {abs(r_mean-R_GUE)/r_err:.1f} sigmas")
say(f"     1/phi   {INV_PHI:.4f}   <-- at {abs(r_mean-INV_PHI)/r_err:.1f} sigmas (!)")
say(f"     Poisson {R_POI:.4f}")
say("  At this height the measured value is CLOSER to 1/phi than to GUE.")
say("  Stopping here, 'the golden ratio appears in the zeros'.  One must not")
say("  stop: the statistic r depends on height.")
say()

# drift with height: the arithmetic corrections are O(1/log(gamma/2pi))
gm = gam[:-2]
B = 12
bins = np.array_split(np.arange(len(r)), B)
xb = np.array([1.0 / np.log(gm[i].mean() / TWOPI) for i in bins])
yb = np.array([r[i].mean() for i in bins])
eb = np.array([r[i].std() / math.sqrt(len(i)) for i in bins])
coef, cov = np.polyfit(xb, yb, 1, w=1.0 / eb, cov=True)
inter, inter_err = coef[1], math.sqrt(cov[1, 1])
say("  <r> per height band (x = 1/log(gamma/2pi)):")
for i, x, y, e in zip(bins, xb, yb, eb):
    say(f"     gamma ~ {gm[i].mean():8.0f}   1/L={x:.4f}   <r>={y:.4f} +/- {e:.4f}")
say(f"  linear fit, extrapolated to infinite height (1/L -> 0):")
say(f"     <r>_inf = {inter:.4f} +/- {inter_err:.4f}")
say(f"     GUE     = {R_GUE:.4f}  -> compatible at {abs(inter-R_GUE)/inter_err:.1f} sigmas")
say(f"     1/phi   = {INV_PHI:.4f}  -> EXCLUDED at {abs(inter-INV_PHI)/inter_err:.1f} sigmas")
coef2, cov2 = np.polyfit(xb, yb, 2, w=1.0 / eb, cov=True)
i2, i2e = coef2[2], math.sqrt(cov2[2, 2])
chi1 = float(np.sum(((yb - np.polyval(coef, xb)) / eb) ** 2)) / (len(xb) - 2)
chi2 = float(np.sum(((yb - np.polyval(coef2, xb)) / eb) ** 2)) / (len(xb) - 3)
say(f"  check with a quadratic term in 1/L (in case of curvature):")
say(f"     <r>_inf = {i2:.4f} +/- {i2e:.4f}     chi2/dof: linear {chi1:.2f}, quadratic {chi2:.2f}")
say("  The excess over GUE decays like 1/log(height): it is the finite-height")
say("  arithmetic correction (Bogomolny-Keating), not a constant.")
say("  phi is not a limit; it is a transient value.")
say()

# ---- primes ----
def criba(n):
    sieve = np.ones(n // 2, dtype=bool)
    for i in range(3, int(n ** .5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False
    p = 2 * np.nonzero(sieve)[0][1::] + 1
    return np.r_[2, p]

P = criba(2_000_000).astype(np.float64)
say(f"  primes used: {len(P)} up to {int(P[-1])}")

def weyl(alpha, P):
    ph = 2 * np.pi * alpha * P
    cs = np.cumsum(np.cos(ph)) ; sn = np.cumsum(np.sin(ph))
    n = np.arange(1, len(P) + 1)
    return np.sqrt(cs ** 2 + sn ** 2) / n

idx = np.unique(np.geomspace(10, len(P), 400).astype(int)) - 1
w_phi = weyl(PHI, P)[idx]
w_sq2 = weyl(math.sqrt(2), P)[idx]
w_hal = weyl(0.5, P)[idx]
say(f"  Weyl sum |1/N sum e(alpha p)| at N={len(P)}:")
say(f"     alpha=phi    {w_phi[-1]:.5f}")
say(f"     alpha=sqrt2  {w_sq2[-1]:.5f}   <-- phi behaves the same: generic")
say(f"     alpha=1/2    {w_hal[-1]:.5f}   <-- this is what a real resonance looks like")

fig2, axes = plt.subplots(2, 3, figsize=(16.5, 9.0))

# --- D: zero spacings ---
ax = axes[0, 0]
ax.hist(s, bins=45, density=True, color=C_BLUE, alpha=.30, edgecolor=SURFACE, lw=.6)
xs = np.linspace(0, 3.2, 400)
ax.plot(xs, 32 / math.pi ** 2 * xs ** 2 * np.exp(-4 * xs ** 2 / math.pi),
        color=C_BLUE, label="GUE")
ax.plot(xs, np.exp(-xs), color=INK3, lw=1.4, ls=":", label="Poisson")
for v, lab in ((INV_PHI, "$1/\\varphi$"), (PHI, "$\\varphi$")):
    ax.axvline(v, color=C_ORANGE, ls="--", lw=1.3)
    ax.text(v, 0.93, lab, color=C_ORANGE, fontsize=10, ha="center",
            transform=ax.get_xaxis_transform())
ax.text(1.35, .82, "GUE", color=C_BLUE, fontsize=9)
ax.text(0.35, .55, "Poisson", color=INK3, fontsize=9)
ax.set_xlim(0, 3.2)
ax.set_xlabel("normalised spacing between zeros")
ax.set_ylabel("density")
ax.set_title(f"D. {len(gam)} zeros of $\\zeta$: the law is GUE\nnothing happens at $\\varphi$ or $1/\\varphi$",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- D2: drift of the statistic r  (the deciding panel) ---
ax = axes[0, 1]
ax.errorbar(xb, yb, yerr=eb, fmt="o", ms=6, color=C_BLUE, ecolor=C_BLUE,
            elinewidth=1.4, capsize=3, mec=SURFACE, mew=1.2, zorder=4)
xf = np.linspace(0, xb.max() * 1.06, 50)
ax.plot(xf, np.polyval(coef, xf), color=C_BLUE, lw=1.6, ls="-", zorder=3)
ax.axhline(R_GUE, color=C_AQUA, lw=1.6)
ax.axhline(INV_PHI, color=C_ORANGE, lw=1.6, ls="--")
ax.errorbar([0], [inter], yerr=[inter_err], fmt="s", ms=8, color=C_BLUE,
            mec=SURFACE, mew=1.5, ecolor=C_BLUE, capsize=4, zorder=5)
ax.text(0.004, R_GUE - 0.0045, "  GUE  0.5996", color=C_AQUA, fontsize=8.5, va="top")
ax.text(0.004, INV_PHI - 0.0006, "  $1/\\varphi$  0.6180", color=C_ORANGE,
        fontsize=8.5, va="top")
ax.annotate(f"extrapolated to infinite\nheight: {inter:.4f}$\\pm${inter_err:.4f}",
            xy=(0, inter), xytext=(0.052, 0.5960), color=C_BLUE, fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=C_BLUE, lw=1.2))
ax.set_xlim(-0.006, xb.max() * 1.06)
ax.set_xlabel("$1/\\log(\\gamma/2\\pi)$   (left = higher on the critical line)")
ax.set_ylabel("$\\langle r\\rangle$")
ax.set_title("D2. DECIDING: the golden value DRIFTS\nit moves with height and ends at GUE, not at $\\varphi$",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- E: Weyl sums over primes ---
ax = axes[0, 2]
NN = idx + 1
ax.plot(NN, w_hal, color=C_ORANGE)
ax.plot(NN, w_phi, color=C_BLUE)
ax.plot(NN, w_sq2, color=C_AQUA)
ax.plot(NN, 1 / np.sqrt(NN), color=INK3, ls=":", lw=1.4)
ax.set_xscale("log"); ax.set_yscale("log")
ax.text(NN[-1], w_hal[-1] * 1.35, "$\\alpha=1/2$: real resonance, no decay ",
        color=C_ORANGE, fontsize=8.5, ha="right", va="bottom")
ax.text(9e2, 0.055, "$N^{-1/2}$ = pure noise", color=INK3, fontsize=8.5)
ax.text(1.1e1, 1.1e-3, "$\\alpha=\\varphi$ (blue) and $\\alpha=\\sqrt{2}$ (green):\n"
        "overlap, both generic", color=C_BLUE, fontsize=8.5, va="bottom")
ax.set_xlabel("number of primes $N$")
ax.set_ylabel("$|N^{-1}\\sum_{p\\leq p_N} e(\\alpha p)|$")
ax.set_title("E. $\\varphi$ against the primes: indistinguishable from $\\sqrt{2}$\na resonance would look like the orange curve",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7, which="both")

# --- F: polar spiral of primes ---
ax = axes[1, 0]
Ps = P[P < 300000]
ax.scatter(Ps * np.cos(Ps), Ps * np.sin(Ps), s=.22, color=C_BLUE,
           alpha=.75, linewidths=0)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title(f"F. {len(Ps)} primes in polar coordinates $(p,\\ p\\ \\mathrm{{rad}})$: arms and rays\n"
             "counted by $6,\\ 44,\\ 710$, denominators of $2\\pi$",
             fontsize=9.5, color=INK, loc="left")

# --- G: golden sunflower ---
ax = axes[1, 1]
n = np.arange(1, 3001)
th = n * 2 * math.pi / PHI ** 2
ax.scatter(np.sqrt(n) * np.cos(th), np.sqrt(n) * np.sin(th), s=4.5,
           color=C_ORANGE, alpha=.9, linewidths=0)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("G. Sunflower $(\\sqrt{n},\\ n\\cdot 2\\pi/\\varphi^2)$: same mechanism\n"
             "counted by $13,\\ 21,\\ 34$, denominators of $\\varphi$",
             fontsize=9.5, color=INK, loc="left")


# --- H: why the spirals of F belong to 2pi and not to phi ---
def convergentes(alpha, n=10):
    a, x, res = [], alpha, []
    h1, h2, k1, k2 = 1, 0, 0, 1
    for _ in range(n):
        ai = math.floor(x)
        a.append(ai)
        h1, h2 = ai * h1 + h2, h1
        k1, k2 = ai * k1 + k2, k1
        res.append((h1, k1))
        f = x - ai
        if f < 1e-13:
            break
        x = 1.0 / f
    return res


ax = axes[1, 2]
for alpha, col in ((TWOPI, C_BLUE), (PHI, C_ORANGE)):
    cv = convergentes(alpha, 9)
    q = np.array([k for _, k in cv], dtype=float)
    q2err = np.array([k * k * abs(alpha - h / k) for h, k in cv])
    ax.plot(q, q2err, "o-", color=col, ms=5, mec=SURFACE, mew=1.2)
    for (h, k), y in zip(cv, q2err):
        if (alpha == TWOPI and k in (1, 7, 113)) or (alpha == PHI and k in (3, 21)):
            ax.annotate(f"{h}/{k}", (k, y), textcoords="offset points",
                        xytext=(3, 5), color=col, fontsize=7.5)
ax.axhline(1 / math.sqrt(5), color=INK3, ls=":", lw=1.4)
ax.set_ylim(4e-3, 4.0)
ax.text(1.6e2, 3.4, "$1/\\sqrt{5}$: the Hurwitz floor.\n$\\varphi$ sits on it:\n"
        "the worst approximable number", color=INK3, fontsize=8, va="top")
ax.text(1.6e0, 1.4e-2, "$2\\pi$ drops to $0.007$ at $710/113$:\n"
        "a resonance 60 times\nstronger than any of $\\varphi$",
        color=C_BLUE, fontsize=8.5)
ax.text(1.15, 0.90, "$\\varphi$", color=C_ORANGE, fontsize=10)
ax.text(1.15, 0.115, "$2\\pi$", color=C_BLUE, fontsize=10)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("denominator $q$ of the convergent")
ax.set_ylabel("$q^2\\,|\\alpha-p/q|$   (low = strong resonance)")
ax.set_title("H. The cause of both drawings, measured\n"
             "$\\varphi$ = weakest resonances; $2\\pi$ = strong resonances",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7, which="both")

fig2.suptitle("Looking for $\\varphi$ in actual data:  the only trace (D2) dissolves "
              "with height;  the arms of the primes are counted by $2\\pi$, not $\\varphi$",
              fontsize=11.5, color=INK, x=0.008, ha="left", y=0.995)
fig2.tight_layout(rect=[0, 0, 1, 0.945])
p2 = os.path.join(HERE, "115_08_fig2_phi_en_primos_y_ceros.png")
fig2.savefig(p2, dpi=170)
say(f"[fig] {p2}")

with open(os.path.join(HERE, "115_08_resultados.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
