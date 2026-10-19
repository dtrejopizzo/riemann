#!/usr/bin/env python3
"""
115.10 -- Why all the rays of the polar drawing have the SAME shape.

Observation: in 115_09_fig_primos_polar.png each ray starts at the origin,
stretches out and bends a little near the end -- and all bend the same way.

This is not an impression: it is exact and predictable with nothing fitted.

  710 = 113*2pi + delta,   delta = +6.0294e-05 rad

Advancing p by 710 rotates the point by delta.  Since delta does not depend
on the ray, the 280 rays are the SAME curve rotated: an Archimedean spiral arc
  r = 710*(theta - theta_a)/delta.

Outputs:
  115_10_fig_rayos.png
  115_10_resultados.txt
"""

import math
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
C_BLUE, C_ORANGE, C_AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, INK3 = "#141413", "#3d3d3a", "#73726c"
SURFACE, GRIDC = "#fcfcfb", "#e3e2dd"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "axes.edgecolor": GRIDC,
    "axes.labelcolor": INK2, "xtick.color": INK3, "ytick.color": INK3,
    "text.color": INK, "font.size": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "grid.color": GRIDC, "grid.linewidth": 0.6, "lines.linewidth": 2.0,
})

TWOPI = 2 * math.pi
out = []
def say(s=""):
    out.append(s); print(s)


def criba(n):
    sieve = np.ones(n // 2, dtype=bool)
    for i in range(3, int(n ** .5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False
    return np.r_[2, 2 * np.nonzero(sieve)[0][1:] + 1]


P = criba(1_400_000)[:100_000]          # the same 100,000 primes as the drawing
PMAX = int(P[-1])
Q, K = 710, 113                          # convergent 710/113 of 2pi
DELTA = Q - K * TWOPI

say("=" * 70)
say("1. THE NUMBER THAT GOVERNS THE WHOLE DRAWING")
say("=" * 70)
say(f"  113 * 2pi = {K*TWOPI:.9f}")
say(f"  710       = 710")
say(f"  delta     = 710 - 113*2pi = {DELTA:+.6e} rad")
say("  Advancing p by 710 rotates the point by exactly delta radians.")
say("  delta does NOT depend on the ray: hence the rays are congruent.")
say()

# ---------------------------------------------------------------- the collapse
a = P % Q
theta = np.mod(P, TWOPI)
theta_a = np.mod(a, TWOPI)
dth = np.mod(theta - theta_a + math.pi, TWOPI) - math.pi   # unwrapped
pred = DELTA * (P - a) / Q
res = dth - pred
say("=" * 70)
say("2. THE 280 RAYS ARE THE SAME CURVE (prediction with nothing fitted)")
say("=" * 70)
say(f"  prediction:  dtheta(p) = delta*(p - p mod 710)/710")
say(f"  maximal deviation over the {len(P)} primes: {np.abs(res).max():.3e} rad")
say(f"  (the width of a ray is 2pi/710 = {TWOPI/Q:.3e} rad, "
    f"{TWOPI/Q/max(np.abs(res).max(),1e-300):.1e} times larger)")
say("  They do not merely resemble each other: they agree to machine precision.")
say()

bend = DELTA * PMAX / Q
say("=" * 70)
say("3. HOW MUCH THEY BEND")
say("=" * 70)
say(f"  at the edge of the drawing (p = {PMAX}):")
say(f"     accumulated turn = {bend:.6f} rad = {math.degrees(bend):.3f} degrees")
say(f"     width of a ray = {TWOPI/Q:.6f} rad")
say(f"     => {bend/(TWOPI/Q):.2f} ray widths, in the same direction "
    "for all 280")
say("  This is exactly 'they all have the same wave and bend at the end'.")
say()

# ------------------------------------------------------- how many rays
ocup = np.unique(a)
copr = np.array([x for x in range(Q) if math.gcd(x, Q) == 1])
say("=" * 70)
say("4. HOW MANY RAYS, AND THE ONLY PART THAT IS ABOUT THE PRIMES")
say("=" * 70)
say(f"  classes mod 710 occupied by primes: {len(ocup)}")
say(f"  phi(710) = {len(copr)}   (710 = 2*5*71)")
faltan = sorted(set(ocup) - set(copr.tolist()))
say(f"  occupied classes NOT coprime to 710: {faltan}  "
    "(the primes 2, 5, 71 themselves)")
say("  With ALL integers there would be 710 rays.  The primes use 280:")
say("  the 430 missing ones are the classes sharing a factor with 710.")
say("  That -- and only that -- is what the drawing says about the primes.")
say("  That the 280 shine evenly is Dirichlet's theorem.")
say()

# -------------------------------------- why the drawing changes with distance
say("=" * 70)
say("5. WHY THE DRAWING CHANGES FAMILY WITH THE RADIUS")
say("=" * 70)
convs = [(6, 1), (19, 3), (25, 4), (44, 7), (333, 53), (710, 113)]
rows = []
for Qc, Kc in convs:
    d = Qc - Kc * TWOPI
    rc = TWOPI / abs(d)          # radius where the drift = one ray width
    rows.append((Qc, Kc, d, rc))
    say(f"  {Qc:>4d}/{Kc:<4d} delta={d:+.4e}  breaks up at r ~ {rc:>12,.0f}")
say(f"  the drawing reaches r = {PMAX:,}")
say("  Hence: near the centre the families 6 and 44 dominate (they break up")
say("  quickly), further out the family 710 dominates, and only beyond r ~ 10^5")
say("  does 710 start to bend visibly.  None of this is about the primes:")
say("  these are the convergents of 2pi.")
say()

# ================================================================== FIGURE
fig, axes = plt.subplots(2, 2, figsize=(12.6, 10.4))

# --- A: one ray, and another ray rotated onto it: they are congruent ---
ax = axes[0, 0]
m3 = a == 3
ax.scatter(P[m3] * np.cos(P[m3]), P[m3] * np.sin(P[m3]), s=16, color=C_BLUE,
           alpha=.9, linewidths=0, zorder=4)
sline = np.linspace(3, PMAX, 2000)
thl = np.mod(3, TWOPI) + DELTA * (sline - 3) / Q
ax.plot(sline * np.cos(thl), sline * np.sin(thl), color=C_BLUE, lw=1.0,
        alpha=.5, zorder=3)
# the ray a=11, rotated onto a=3: it falls exactly on top
m11 = a == 11
rot = np.mod(3, TWOPI) - np.mod(11, TWOPI)
th11 = np.mod(P[m11], TWOPI) + rot
ax.scatter(P[m11] * np.cos(th11), P[m11] * np.sin(th11), s=42,
           facecolors="none", edgecolors=C_ORANGE, linewidths=.9, zorder=5)
ax.scatter([0], [0], s=18, color=INK3, zorder=6)
ax.set_aspect("equal"); ax.axis("off")
ax.text(0.0, -0.04, "blue: the ray $p\\equiv3$ (mod 710), with its spiral\n"
        "$r=710(\\theta-\\theta_a)/\\delta$ drawn on top\n\n"
        "orange: the ray $p\\equiv11$, rotated.  It fits exactly:\n"
        "not similar, the same arc",
        transform=ax.transAxes, fontsize=8.5, color=INK2, va="top")
ax.set_title("A. A ray is an arc of an Archimedean spiral\n"
             "and all the others are the same arc, rotated",
             fontsize=9.5, color=INK, loc="left")

# --- B: collapse of the 280 rays ---
ax = axes[0, 1]
sub = np.linspace(0, len(P) - 1, 20000).astype(int)
ax.scatter(P[sub], np.degrees(dth[sub]), s=1.2, color=C_BLUE, alpha=.5,
           linewidths=0)
xs = np.linspace(0, PMAX, 200)
ax.plot(xs, np.degrees(DELTA * xs / Q), color=C_ORANGE, lw=1.4, ls="--")
ax.text(0.05e6, 5.4, "prediction $\\delta\\,p/710$, nothing fitted",
        color=C_ORANGE, fontsize=8.5)
ax.text(0.05e6, 4.6, f"maximal deviation: {np.abs(res).max():.1e} rad\n"
        f"(the width of a ray is {TWOPI/Q:.2e})", color=INK3, fontsize=8.5)
ax.set_xlabel("$p$  (= radius in the drawing)")
ax.set_ylabel("turn of the ray relative to its origin  [degrees]")
ax.set_title("B. The 280 rays superposed: a single curve\n"
             "not similar: congruent to machine precision",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- C: how many rays, and which are missing ---
ax = axes[1, 0]
cnt = np.bincount(a, minlength=Q)
esco = np.array([math.gcd(x, Q) == 1 for x in range(Q)])
ax.bar(np.arange(Q)[esco], cnt[esco], width=1.0, color=C_BLUE, linewidth=0)
ax.bar(np.arange(Q)[~esco], cnt[~esco], width=1.0, color=C_ORANGE, linewidth=0)
ax.axhline(len(P) / len(copr), color=INK3, ls=":", lw=1.4)
ax.text(8, len(P) / len(copr) * 1.72,
        f"{len(copr)} classes coprime to $710=2\\cdot5\\cdot71$: the visible rays",
        color=C_BLUE, fontsize=8.5)
ax.text(8, len(P) / len(copr) * 1.56,
        f"{Q-len(copr)} classes with a common factor: empty, the missing rays",
        color=C_ORANGE, fontsize=8.5)
ax.text(8, len(P) / len(copr) * 1.40,
        f"Dirichlet: {len(P)}/{len(copr)} = {len(P)/len(copr):.0f} primes per ray, "
        "all even", color=INK3, fontsize=8.5)
ax.set_ylim(0, len(P) / len(copr) * 1.92)
ax.set_xlabel("residue class mod 710")
ax.set_ylabel("primes in the class")
ax.set_title("C. The only thing the drawing says about the primes\n"
             f"of 710 possible rays, {len(ocup)} are occupied",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7, axis="y")

# --- D: coherence radius of each family ---
ax = axes[1, 1]
qq = np.array([q for q, _, _, _ in rows], dtype=float)
rr = np.array([rc for _, _, _, rc in rows])
ax.plot(qq, rr, "o-", color=C_BLUE, ms=7, mec=SURFACE, mew=1.5)
for (Qc, Kc, d, rc) in rows:
    ax.annotate(f"{Qc}/{Kc}", (Qc, rc), textcoords="offset points",
                xytext=(6, -10), color=C_BLUE, fontsize=8)
ax.axhline(PMAX, color=C_ORANGE, ls="--", lw=1.5)
ax.text(6.5, PMAX * 1.35, f"edge of the drawing, r = {PMAX:,}", color=C_ORANGE,
        fontsize=8.5)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("family: numerator of the convergent of $2\\pi$")
ax.set_ylabel("radius where the family breaks up  $2\\pi/|\\delta|$")
ax.set_title("D. Why the drawing changes with the radius\n"
             "6 and 44 dominate at the centre; 710 further out, where it already bends",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7, which="both")

fig.suptitle("Why all the rays have the same shape: "
             "$710-113\\cdot2\\pi=+6.03\\times10^{-5}$ rad, "
             "the same turn for all 280",
             fontsize=11.5, color=INK, x=0.008, ha="left", y=0.995)
fig.tight_layout(rect=[0, 0, 1, 0.955])
p = os.path.join(HERE, "115_10_fig_rayos.png")
fig.savefig(p, dpi=180)
say(f"[fig] {p}")

with open(os.path.join(HERE, "115_10_resultados.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
