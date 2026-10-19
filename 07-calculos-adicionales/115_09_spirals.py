#!/usr/bin/env python3
"""
115.09 -- The two drawings of 115_08 (panels F and G), separately and enlarged.

  115_09_fig_primos_polar.png   primes in polar coordinates (p, p rad)
  115_09_fig_girasol_aureo.png  sunflower (sqrt n, n*2pi/phi^2)

Same mechanism in both -- continued fractions -- with two different
numbers: the arms of the primes are counted by the denominators of 2pi
(6, 44, 710), those of the sunflower by those of phi (Fibonacci: 13, 21, 34).
"""

import math
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

C_BLUE, C_ORANGE = "#2a78d6", "#eb6834"
INK, INK2, INK3 = "#141413", "#3d3d3a", "#73726c"
SURFACE = "#fcfcfb"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "text.color": INK, "font.size": 10,
})

PHI = (1.0 + math.sqrt(5.0)) / 2.0


def criba(n):
    sieve = np.ones(n // 2, dtype=bool)
    for i in range(3, int(n ** .5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False
    return np.r_[2, 2 * np.nonzero(sieve)[0][1:] + 1]


def lienzo(titulo, bajada, pie):
    fig = plt.figure(figsize=(8.4, 9.2))
    ax = fig.add_axes([0.02, 0.055, 0.96, 0.845])
    ax.set_aspect("equal")
    ax.axis("off")
    fig.text(0.035, 0.965, titulo, fontsize=14.5, color=INK, va="top")
    fig.text(0.035, 0.932, bajada, fontsize=10, color=INK2, va="top")
    fig.text(0.035, 0.030, pie, fontsize=9, color=INK3, va="bottom")
    return fig, ax


# ---------------------------------------------------------- primes in polar coordinates
P = criba(1_400_000).astype(np.float64)[:100_000]   # the first 100,000 primes
fig, ax = lienzo(
    f"Primes in polar coordinates: $(r,\\theta)=(p,\\ p\\ \\mathrm{{rad}})$",
    f"The first {len(P)} primes (up to {int(P[-1])}).  The rays are not a "
    "pattern of the primes: "
    "they are the clock of $2\\pi$.",
    "Each ray family corresponds to a continued-fraction convergent of $2\\pi=6.28318\\ldots$  "
    "The convergent $6/1$ gives 6 arms; $44/7$ gives 44;\n"
    "$710/113$ gives 710.  Within each family the rays of residues "
    "not coprime to the denominator are missing: that is where Dirichlet acts.")
ax.scatter(P * np.cos(P), P * np.sin(P), s=.10, color=C_BLUE, alpha=.80,
           linewidths=0)
p1 = os.path.join(HERE, "115_09_fig_primos_polar.png")
fig.savefig(p1, dpi=230)
print("[fig]", p1, len(P), "primes")

# --------------------------------------------------------- golden sunflower
NG = 4000
n = np.arange(1, NG + 1)
th = n * 2 * math.pi / PHI ** 2
fig, ax = lienzo(
    "Golden sunflower: $(r,\\theta)=(\\sqrt{n},\\ n\\cdot 2\\pi/\\varphi^{2})$",
    f"{NG} points.  The same mechanism as the drawing of the primes, with "
    "$\\varphi$ in place of $2\\pi$.",
    "The arms the eye sees are 13, 21, 34: Fibonacci denominators, "
    "the convergents of $\\varphi$.  And they are weak:\n"
    "$q^2|\\varphi-p/q|$ never drops below $1/\\sqrt{5}=0.447$ (Hurwitz floor), "
    "while $2\\pi$ reaches $0.007$ at $710/113$.\n"
    "Hence the rays of the primes are sharp and these arms "
    "rearrange at each scale: $\\varphi$ is the worst approximable number.")
ax.scatter(np.sqrt(n) * np.cos(th), np.sqrt(n) * np.sin(th), s=13,
           color=C_ORANGE, alpha=.92, linewidths=0)
p2 = os.path.join(HERE, "115_09_fig_girasol_aureo.png")
fig.savefig(p2, dpi=230)
print("[fig]", p2, NG, "points")
