"""
El espectro de 10000 ceros de Riemann: buscando el orden en el caos.

Tres vistas:

  (A) Los ceros crudos y la envolvente TRIVIAL N(T) ~ (T/2pi)log(T/2pi).
      El espaciado medio se achica como 2pi/log(T). Hay que QUITAR esto.

  (B) UNFOLDING: normalizamos cada cero por su posicion esperada N(gamma),
      de modo que el espaciado medio pase a ser 1. Sobre los espaciados
      normalizados s, el histograma se compara con:
        - GUE (matrices aleatorias hermitianas): hay REPULSION de niveles,
          P(s) -> 0 cuando s -> 0. Este es el patron real (Montgomery-Odlyzko).
        - Poisson (puntos al azar): P(s) = e^{-s}, sin repulsion.
      Si los ceros siguen GUE, el 'caos' es en realidad un cristal difuso:
      los ceros se EVITAN entre si, como autovalores de un operador autoadjunto.

  (C) Transformada del proceso de ceros: la parte oscilante tiene picos en
      t = log(p^k), los LOGARITMOS de las potencias de primo. Dual exacto del
      grafico 'primos_predicen_ceros': los ceros tambien 'saben' los primos.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

# ---------- cargar ceros ----------
gammas = np.loadtxt("zeros_10000.txt")
N = len(gammas)
print(f"{N} ceros cargados. gamma_1={gammas[0]:.4f}, gamma_N={gammas[-1]:.4f}")

# ---------- (A) envolvente trivial: N(T) teorico ----------
def N_teorico(t):
    x = t / (2 * math.pi)
    return x * math.log(x) - x + 7.0 / 8.0

# ---------- (B) unfolding ----------
# cada cero gamma_k se mapea a su cuenta esperada; asi el espaciado medio -> 1
unfolded = np.array([N_teorico(g) for g in gammas])
spacings = np.diff(unfolded)
spacings = spacings[np.isfinite(spacings)]
print(f"espaciado normalizado: media={spacings.mean():.4f} (deberia ~1), "
      f"desv={spacings.std():.4f}")

# curvas teoricas
s = np.linspace(0, 4, 400)
# GUE (surmise de Wigner para beta=2)
P_gue = (32 / math.pi**2) * s**2 * np.exp(-4 * s**2 / math.pi)
# Poisson
P_poisson = np.exp(-s)

# ---------- (C) transformada: ceros -> primos ----------
# suma sobre ceros de cos(u * gamma), que resuena en u = log(n)
us = np.linspace(0.5, 3.6, 3000)   # u = log(x); log 2=0.69, log3=1.10, ...
# usamos solo los primeros ~2000 ceros (los de altura moderada) para nitidez
G = gammas[:2000]
spec = np.array([np.abs(np.sum(np.exp(-1j * u * G))) for u in us])

# posiciones esperadas de picos: log de potencias de primo
primos = [2, 3, 5, 7, 11, 13]
picos_u = []
for p in primos:
    k = 1
    while p**k <= 40:
        picos_u.append((math.log(p**k), p, k))
        k += 1

# ---------- figura ----------
fig = plt.figure(figsize=(15, 12))

# (A)
axA = fig.add_subplot(3, 1, 1)
Ts = np.linspace(gammas[0], gammas[-1], 500)
axA.plot(gammas, np.arange(1, N + 1), color="#dc2626", linewidth=1.5,
         label="conteo real de ceros")
axA.plot(Ts, [N_teorico(t) for t in Ts], color="#16a34a", linewidth=1.5,
         linestyle="--", label="envolvente teorica N(T)=(T/2pi)log(T/2pi)")
axA.set_title(f"(A) Los {N} ceros crudos siguen la envolvente trivial N(T) — hay que quitarla")
axA.set_xlabel("gamma (altura del cero)")
axA.set_ylabel("nro. de cero")
axA.grid(True, alpha=0.3)
axA.legend(loc="upper left")

# (B)
axB = fig.add_subplot(3, 1, 2)
axB.hist(spacings, bins=60, range=(0, 4), density=True, color="#93c5fd",
         edgecolor="#2563eb", alpha=0.8, label="ceros de Riemann (10000)")
axB.plot(s, P_gue, color="#dc2626", linewidth=2.5, label="GUE (matrices aleatorias) — REPULSION")
axB.plot(s, P_poisson, color="#6b7280", linewidth=2, linestyle="--", label="Poisson (al azar) — sin repulsion")
axB.set_title("(B) EL ORDEN EN EL CAOS: los espaciados siguen GUE, no Poisson. Los ceros se REPELEN.")
axB.set_xlabel("espaciado normalizado s (media = 1)")
axB.set_ylabel("densidad P(s)")
axB.set_xlim(0, 4)
axB.grid(True, alpha=0.3)
axB.legend(loc="upper right")

# (C)
axC = fig.add_subplot(3, 1, 3)
axC.plot(us, spec, color="#7c3aed", linewidth=1.2, label="| suma_ceros exp(-i u gamma) |")
for (u, p, k) in picos_u:
    if us[0] <= u <= us[-1]:
        axC.axvline(u, color="#f59e0b", linewidth=1.2, linestyle=":", alpha=0.9)
        lbl = f"log {p}" if k == 1 else f"log {p}^{k}"
        axC.annotate(lbl, xy=(u, spec.max()*0.9), rotation=90,
                     fontsize=8, color="#b45309", va="top", ha="right")
axC.set_title("(C) La transformada de los ceros tiene picos en log(p^k): los ceros 'saben' los primos")
axC.set_xlabel("u = log(x)")
axC.set_ylabel("magnitud")
axC.grid(True, alpha=0.3)
axC.legend(loc="upper right")

plt.tight_layout()
plt.savefig("espectro_ceros.png", dpi=130)
print("Guardado: espectro_ceros.png")

# reporte estadistico
from math import sqrt
# fraccion de espaciados chicos (repulsion): GUE predice muy pocos < 0.3
frac_chicos = np.mean(spacings < 0.3)
print(f"Fraccion de espaciados < 0.3: {frac_chicos:.4f} "
      f"(Poisson daria ~{1-math.exp(-0.3):.3f}, GUE mucho menos -> repulsion)")
