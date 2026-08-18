#!/usr/bin/env python3
"""
115.09 -- Los dos dibujos de 115_08 (paneles F y G), por separado y en grande.

  115_09_fig_primos_polar.png   primos en polar (p, p rad)
  115_09_fig_girasol_aureo.png  girasol (sqrt n, n*2pi/phi^2)

Mismo mecanismo en los dos -- fracciones continuas -- y dos numeros
distintos: los brazos de los primos los cuentan los denominadores de 2pi
(6, 44, 710), los del girasol los de phi (Fibonacci: 13, 21, 34).
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


# ---------------------------------------------------------- primos en polar
P = criba(1_400_000).astype(np.float64)[:100_000]   # los primeros 100 000 primos
fig, ax = lienzo(
    f"Primos en coordenadas polares: $(r,\\theta)=(p,\\ p\\ \\mathrm{{rad}})$",
    f"Los primeros {len(P)} primos (hasta {int(P[-1])}).  Los rayos no son un "
    "patron de los primos: "
    "son el reloj de $2\\pi$.",
    "Cada rayo corresponde a una fraccion continua de $2\\pi=6.28318\\ldots$  "
    "El convergente $6/1$ da 6 brazos; $44/7$ da 44;\n"
    "$710/113$ da 710.  Dentro de cada familia faltan los rayos "
    "de residuos no coprimos con el denominador: ahi actua Dirichlet.")
ax.scatter(P * np.cos(P), P * np.sin(P), s=.10, color=C_BLUE, alpha=.80,
           linewidths=0)
p1 = os.path.join(HERE, "115_09_fig_primos_polar.png")
fig.savefig(p1, dpi=230)
print("[fig]", p1, len(P), "primos")

# --------------------------------------------------------- girasol aureo
NG = 4000
n = np.arange(1, NG + 1)
th = n * 2 * math.pi / PHI ** 2
fig, ax = lienzo(
    "Girasol aureo: $(r,\\theta)=(\\sqrt{n},\\ n\\cdot 2\\pi/\\varphi^{2})$",
    f"{NG} puntos.  El mismo mecanismo que el dibujo de los primos, con "
    "$\\varphi$ en lugar de $2\\pi$.",
    "Los brazos que ve el ojo son 13, 21, 34 — denominadores de Fibonacci, "
    "los convergentes de $\\varphi$.  Y son debiles:\n"
    "$q^2|\\varphi-p/q|$ nunca baja de $1/\\sqrt{5}=0.447$ (piso de Hurwitz), "
    "mientras $2\\pi$ llega a $0.007$ en $710/113$.\n"
    "Por eso los rayos de los primos son nitidos y estos brazos se "
    "reacomodan a cada escala: $\\varphi$ es el peor aproximable que existe.")
ax.scatter(np.sqrt(n) * np.cos(th), np.sqrt(n) * np.sin(th), s=13,
           color=C_ORANGE, alpha=.92, linewidths=0)
p2 = os.path.join(HERE, "115_09_fig_girasol_aureo.png")
fig.savefig(p2, dpi=230)
print("[fig]", p2, NG, "puntos")
