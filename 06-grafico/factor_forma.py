"""
Factor de forma espectral K(tau): el diagnostico central del caos cuantico.

K(tau) = (1/N) | sum_j exp(i 2pi tau w_j) |^2   sobre los ceros desdoblados w_j.

Firma del CAOS CUANTICO (Bohigas-Giannoni-Schmit):
  - 'rampa' lineal K(tau) ~ tau para tau < 1  (correlaciones GUE)
  - 'meseta' K(tau) ~ 1 para tau > 1          (rigidez, tiempo de Heisenberg)
A tau chico, las desviaciones estan gobernadas por los PRIMOS (orbitas
periodicas, aproximacion diagonal de Berry).

Si los ceros muestran rampa+meseta, son un espectro de caos cuantico:
autovalores de un operador autoadjunto de un sistema clasico caotico.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

g = np.loadtxt("zeros_10000.txt")
def N_smooth(t):
    x = t/(2*math.pi); return x*math.log(x) - x + 7/8
w = np.array([N_smooth(t) for t in g]); w = w[np.isfinite(w)]
N = len(w)

# K(tau) cruda
taus = np.linspace(0.001, 2.5, 4000)
K = np.empty_like(taus)
for i, tau in enumerate(taus):
    K[i] = np.abs(np.sum(np.exp(1j*2*np.pi*tau*w)))**2 / N

# suavizado (media movil) para ver rampa+meseta bajo el ruido
def smooth(y, win):
    k = np.ones(win)/win
    return np.convolve(y, k, mode="same")
Ks = smooth(K, 80)

# GUE teorico: K_connected(tau) = min(tau,1); K = min(tau,1) + delta-parte
gue = np.minimum(taus, 1.0)

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(taus, K, color="#c4b5fd", linewidth=0.5, alpha=0.6, label="K(tau) cruda (10000 ceros)")
ax.plot(taus, Ks, color="#7c3aed", linewidth=2.2, label="K(tau) suavizada")
ax.plot(taus, gue, color="#dc2626", linewidth=2.2, linestyle="--",
        label="GUE: rampa min(tau,1) + meseta")
ax.axvline(1.0, color="#16a34a", linewidth=1.2, linestyle=":", label="tau=1 (tiempo de Heisenberg)")
ax.set_title("Factor de forma K(tau): RAMPA + MESETA = firma de caos cuantico en los ceros")
ax.set_xlabel("tau  (tiempo, en unidades del tiempo de Heisenberg)")
ax.set_ylabel("K(tau)")
ax.set_ylim(0, 1.6)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right")

plt.tight_layout()
plt.savefig("factor_forma.png", dpi=130)
print("Guardado: factor_forma.png")

# diagnostico rampa
for t in [0.25, 0.5, 0.75, 1.0, 1.5, 2.0]:
    i = np.argmin(np.abs(taus-t))
    print(f"  tau={t:.2f}:  K={Ks[i]:.3f}   GUE={gue[i]:.3f}")
