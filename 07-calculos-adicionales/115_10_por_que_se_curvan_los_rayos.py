#!/usr/bin/env python3
"""
115.10 -- Por que todos los rayos del dibujo polar tienen la MISMA forma.

Observacion: en 115_09_fig_primos_polar.png cada rayo nace en el origen,
se estira, y sobre el final se dobla un poco -- y todos se doblan igual.

Esto no es una impresion: es exacto y se puede predecir sin ajustar nada.

  710 = 113*2pi + delta,   delta = +6.0294e-05 rad

Avanzar p en 710 gira el punto en delta.  Como delta no depende del rayo,
los 280 rayos son la MISMA curva rotada: un arco de espiral de Arquimedes
  r = 710*(theta - theta_a)/delta.

Salidas:
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


P = criba(1_400_000)[:100_000]          # los mismos 100 000 primos del dibujo
PMAX = int(P[-1])
Q, K = 710, 113                          # convergente 710/113 de 2pi
DELTA = Q - K * TWOPI

say("=" * 70)
say("1. EL NUMERO QUE GOBIERNA TODO EL DIBUJO")
say("=" * 70)
say(f"  113 * 2pi = {K*TWOPI:.9f}")
say(f"  710       = 710")
say(f"  delta     = 710 - 113*2pi = {DELTA:+.6e} rad")
say("  Avanzar p en 710 unidades gira el punto exactamente delta radianes.")
say("  delta NO depende del rayo: por eso los rayos son congruentes.")
say()

# ---------------------------------------------------------------- el colapso
a = P % Q
theta = np.mod(P, TWOPI)
theta_a = np.mod(a, TWOPI)
dth = np.mod(theta - theta_a + math.pi, TWOPI) - math.pi   # desenrollado
pred = DELTA * (P - a) / Q
res = dth - pred
say("=" * 70)
say("2. LOS 280 RAYOS SON LA MISMA CURVA (prediccion sin ajustar nada)")
say("=" * 70)
say(f"  prediccion:  dtheta(p) = delta*(p - p mod 710)/710")
say(f"  desvio maximo sobre los {len(P)} primos: {np.abs(res).max():.3e} rad")
say(f"  (el ancho de un rayo es 2pi/710 = {TWOPI/Q:.3e} rad — "
    f"{TWOPI/Q/max(np.abs(res).max(),1e-300):.1e} veces mayor)")
say("  No es que se parezcan: coinciden a precision de maquina.")
say()

bend = DELTA * PMAX / Q
say("=" * 70)
say("3. CUANTO SE DOBLAN")
say("=" * 70)
say(f"  al borde del dibujo (p = {PMAX}):")
say(f"     giro acumulado = {bend:.6f} rad = {math.degrees(bend):.3f} grados")
say(f"     ancho de un rayo = {TWOPI/Q:.6f} rad")
say(f"     => {bend/(TWOPI/Q):.2f} anchos de rayo, y en el mismo sentido "
    "para los 280")
say("  Eso es exactamente 'todos tienen la misma onda y al final se doblan'.")
say()

# ------------------------------------------------------- cuantos rayos hay
ocup = np.unique(a)
copr = np.array([x for x in range(Q) if math.gcd(x, Q) == 1])
say("=" * 70)
say("4. CUANTOS RAYOS, Y CUAL ES LA UNICA PARTE QUE SI ES DE LOS PRIMOS")
say("=" * 70)
say(f"  clases mod 710 ocupadas por los primos: {len(ocup)}")
say(f"  phi(710) = {len(copr)}   (710 = 2*5*71)")
faltan = sorted(set(ocup) - set(copr.tolist()))
say(f"  ocupadas que NO son coprimas con 710: {faltan}  "
    "(los propios 2, 5, 71)")
say("  Con TODOS los enteros habria 710 rayos.  Los primos usan 280:")
say("  los 430 que faltan son las clases con factor comun con 710.")
say("  Eso -- y solo eso -- es lo que el dibujo dice de los primos.")
say("  Que los 280 brillen parejo es el teorema de Dirichlet.")
say()

# -------------------------------------- por que cambia el dibujo al alejarse
say("=" * 70)
say("5. POR QUE EL DIBUJO CAMBIA DE FAMILIA SEGUN EL RADIO")
say("=" * 70)
convs = [(6, 1), (19, 3), (25, 4), (44, 7), (333, 53), (710, 113)]
rows = []
for Qc, Kc in convs:
    d = Qc - Kc * TWOPI
    rc = TWOPI / abs(d)          # radio donde la deriva = un ancho de rayo
    rows.append((Qc, Kc, d, rc))
    say(f"  {Qc:>4d}/{Kc:<4d} delta={d:+.4e}  se desarma en r ~ {rc:>12,.0f}")
say(f"  el dibujo llega a r = {PMAX:,}")
say("  Por eso: cerca del centro mandan las familias 6 y 44 (se desarman")
say("  enseguida), afuera manda la de 710, y recien pasando r ~ 10^5 la de")
say("  710 empieza a doblarse visiblemente.  Nada de esto es de los primos:")
say("  son los convergentes de 2pi.")
say()

# ================================================================== FIGURA
fig, axes = plt.subplots(2, 2, figsize=(12.6, 10.4))

# --- A: un rayo, y otro rayo girado encima: son congruentes ---
ax = axes[0, 0]
m3 = a == 3
ax.scatter(P[m3] * np.cos(P[m3]), P[m3] * np.sin(P[m3]), s=16, color=C_BLUE,
           alpha=.9, linewidths=0, zorder=4)
sline = np.linspace(3, PMAX, 2000)
thl = np.mod(3, TWOPI) + DELTA * (sline - 3) / Q
ax.plot(sline * np.cos(thl), sline * np.sin(thl), color=C_BLUE, lw=1.0,
        alpha=.5, zorder=3)
# el rayo a=11, girado sobre el a=3: cae exactamente encima
m11 = a == 11
rot = np.mod(3, TWOPI) - np.mod(11, TWOPI)
th11 = np.mod(P[m11], TWOPI) + rot
ax.scatter(P[m11] * np.cos(th11), P[m11] * np.sin(th11), s=42,
           facecolors="none", edgecolors=C_ORANGE, linewidths=.9, zorder=5)
ax.scatter([0], [0], s=18, color=INK3, zorder=6)
ax.set_aspect("equal"); ax.axis("off")
ax.text(0.0, -0.04, "azul: el rayo $p\\equiv3$ (mod 710), con su espiral\n"
        "$r=710(\\theta-\\theta_a)/\\delta$ dibujada encima\n\n"
        "naranja: el rayo $p\\equiv11$, girado.  Cae exacto:\n"
        "no es parecido, es el mismo arco",
        transform=ax.transAxes, fontsize=8.5, color=INK2, va="top")
ax.set_title("A. Un rayo es un arco de espiral de Arquimedes\n"
             "y todos los demas son ese mismo arco, rotado",
             fontsize=9.5, color=INK, loc="left")

# --- B: el colapso de los 280 rayos ---
ax = axes[0, 1]
sub = np.linspace(0, len(P) - 1, 20000).astype(int)
ax.scatter(P[sub], np.degrees(dth[sub]), s=1.2, color=C_BLUE, alpha=.5,
           linewidths=0)
xs = np.linspace(0, PMAX, 200)
ax.plot(xs, np.degrees(DELTA * xs / Q), color=C_ORANGE, lw=1.4, ls="--")
ax.text(0.05e6, 5.4, "prediccion $\\delta\\,p/710$ — sin ajustar nada",
        color=C_ORANGE, fontsize=8.5)
ax.text(0.05e6, 4.6, f"desvio maximo: {np.abs(res).max():.1e} rad\n"
        f"(el ancho de un rayo es {TWOPI/Q:.2e})", color=INK3, fontsize=8.5)
ax.set_xlabel("$p$  (= radio en el dibujo)")
ax.set_ylabel("giro del rayo respecto de su origen  [grados]")
ax.set_title("B. Los 280 rayos, superpuestos: una sola curva\n"
             "no se parecen — son congruentes a precision de maquina",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- C: cuantos rayos, y cuales faltan ---
ax = axes[1, 0]
cnt = np.bincount(a, minlength=Q)
esco = np.array([math.gcd(x, Q) == 1 for x in range(Q)])
ax.bar(np.arange(Q)[esco], cnt[esco], width=1.0, color=C_BLUE, linewidth=0)
ax.bar(np.arange(Q)[~esco], cnt[~esco], width=1.0, color=C_ORANGE, linewidth=0)
ax.axhline(len(P) / len(copr), color=INK3, ls=":", lw=1.4)
ax.text(8, len(P) / len(copr) * 1.72,
        f"{len(copr)} clases coprimas con $710=2\\cdot5\\cdot71$: los rayos que se ven",
        color=C_BLUE, fontsize=8.5)
ax.text(8, len(P) / len(copr) * 1.56,
        f"{Q-len(copr)} clases con factor comun: vacias — los rayos que faltan",
        color=C_ORANGE, fontsize=8.5)
ax.text(8, len(P) / len(copr) * 1.40,
        f"Dirichlet: {len(P)}/{len(copr)} = {len(P)/len(copr):.0f} primos por rayo, "
        "todos parejos", color=INK3, fontsize=8.5)
ax.set_ylim(0, len(P) / len(copr) * 1.92)
ax.set_xlabel("clase de resto mod 710")
ax.set_ylabel("primos en la clase")
ax.set_title("C. Lo unico que el dibujo dice de los primos\n"
             f"de 710 rayos posibles se ocupan {len(ocup)}",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7, axis="y")

# --- D: radio de coherencia de cada familia ---
ax = axes[1, 1]
qq = np.array([q for q, _, _, _ in rows], dtype=float)
rr = np.array([rc for _, _, _, rc in rows])
ax.plot(qq, rr, "o-", color=C_BLUE, ms=7, mec=SURFACE, mew=1.5)
for (Qc, Kc, d, rc) in rows:
    ax.annotate(f"{Qc}/{Kc}", (Qc, rc), textcoords="offset points",
                xytext=(6, -10), color=C_BLUE, fontsize=8)
ax.axhline(PMAX, color=C_ORANGE, ls="--", lw=1.5)
ax.text(6.5, PMAX * 1.35, f"borde del dibujo, r = {PMAX:,}", color=C_ORANGE,
        fontsize=8.5)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("familia: numerador del convergente de $2\\pi$")
ax.set_ylabel("radio donde la familia se desarma  $2\\pi/|\\delta|$")
ax.set_title("D. Por que el dibujo cambia con el radio\n"
             "6 y 44 mandan en el centro; 710 afuera, y ahi ya se dobla",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7, which="both")

fig.suptitle("Por que todos los rayos tienen la misma forma: "
             "$710-113\\cdot2\\pi=+6.03\\times10^{-5}$ rad, "
             "el mismo giro para los 280",
             fontsize=11.5, color=INK, x=0.008, ha="left", y=0.995)
fig.tight_layout(rect=[0, 0, 1, 0.955])
p = os.path.join(HERE, "115_10_fig_rayos.png")
fig.savefig(p, dpi=180)
say(f"[fig] {p}")

with open(os.path.join(HERE, "115_10_resultados.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
