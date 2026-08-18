"""
Rigidez espectral: la firma del 'mecanismo de regulacion'.

Numero-varianza Sigma^2(L) = varianza de la cantidad de ceros (desdoblados)
en un intervalo de longitud L.
  - Poisson (al azar, SIN regulacion): Sigma^2(L) = L   (crece lineal)
  - GUE (CON regulacion / repulsion): Sigma^2(L) ~ (1/pi^2) ln(L)  (crece log)

Si los ceros son rigidos (log en vez de lineal), el sistema RESISTE las
fluctuaciones: es el AGC / la autorregulacion que impide crecimiento y colapso.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

gammas = np.loadtxt("zeros_10000.txt")

# desdoblar: N(T) suave -> puntos con espaciado medio 1
def N_smooth(t):
    x = t / (2*math.pi)
    return x*math.log(x) - x + 7.0/8.0
w = np.array([N_smooth(g) for g in gammas])   # posiciones desdobladas
w = w[np.isfinite(w)]
w = w - w[0]
Wmax = w[-1]
print(f"{len(w)} ceros desdoblados, rango total = {Wmax:.0f} (espaciado medio 1)")

# Sigma^2(L): para cada L, muchos intervalos aleatorios, varianza del conteo
Ls = np.linspace(0.5, 30, 60)
sigma2 = []
rng = np.random.default_rng(0)
for L in Ls:
    starts = rng.uniform(0, Wmax - L, size=4000)
    counts = np.array([np.searchsorted(w, s+L) - np.searchsorted(w, s) for s in starts])
    sigma2.append(counts.var())
sigma2 = np.array(sigma2)

# curvas teoricas
poisson = Ls
gue = (1/math.pi**2) * (np.log(2*math.pi*Ls) + 0.5772156649 + 1)

fig, ax = plt.subplots(figsize=(13, 7))
ax.plot(Ls, sigma2, "o", color="#7c3aed", markersize=5, label="ceros de Riemann (10000)")
ax.plot(Ls, gue, color="#dc2626", linewidth=2.5, label="GUE  ~ (1/pi^2) ln L   (CON regulacion)")
ax.plot(Ls, poisson, color="#6b7280", linewidth=2, linestyle="--", label="Poisson  = L   (SIN regulacion)")
ax.set_title("Rigidez espectral: los ceros resisten las fluctuaciones (crecen como ln L, no como L)")
ax.set_xlabel("L  (longitud del intervalo, en espaciados medios)")
ax.set_ylabel("numero-varianza  Sigma^2(L)")
ax.set_ylim(0, 12)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("rigidez.png", dpi=130)
print("Guardado: rigidez.png")

# reporte
for L in [5, 10, 20]:
    i = np.argmin(np.abs(Ls-L))
    print(f"L={L:2d}:  ceros Sigma^2={sigma2[i]:5.2f}   GUE={gue[i]:5.2f}   Poisson={poisson[i]:5.2f}")
