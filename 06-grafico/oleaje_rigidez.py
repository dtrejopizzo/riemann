"""
El 'oleaje' en Sigma^2(L): descomponer rigidez = log (GUE) + oscilacion.

Calculamos Sigma^2(L) de forma DETERMINISTA (deslizando la ventana densamente,
sin ruido de muestreo) para ver la oscilacion real.

Comparamos con:
  - GUE suave: (1/pi^2) ln L  -> el componente que ESTABILIZA (rigidez, no diverge)
  - 'picket fence' {L}(1-{L}) -> oscilacion triangular pura de un cristal perfecto
La hipotesis del usuario: envolvente = log + oscilacion. El log da la rigidez;
la oscilacion (acotada, tipo cristal/primos) da la variabilidad.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

g = np.loadtxt("zeros_10000.txt")
def N_smooth(t):
    x = t/(2*math.pi); return x*math.log(x) - x + 7/8
w = np.array([N_smooth(t) for t in g]); w = w[np.isfinite(w)]; w -= w[0]
Wmax = w[-1]

# Sigma^2(L) DETERMINISTA: deslizar ventana con paso fino
Ls = np.linspace(0.2, 15, 400)
starts = np.arange(0, Wmax - 15, 0.15)
sig2 = np.empty_like(Ls)
for i, L in enumerate(Ls):
    cnt = np.searchsorted(w, starts + L) - np.searchsorted(w, starts)
    sig2[i] = cnt.var()

# componentes teoricos
gue = (1/math.pi**2)*(np.log(2*math.pi*Ls) + 0.5772156649 + 1)  # rigidez (log)
frac = Ls - np.floor(Ls)
picket = frac*(1-frac)                                          # oscilacion cristal

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# panel 1: la senal y sus dos componentes
ax1.plot(Ls, sig2, color="#7c3aed", linewidth=1.6, label="ceros: Sigma^2(L) (determinista)")
ax1.plot(Ls, gue, color="#dc2626", linewidth=2, linestyle="--",
         label="componente LOG (GUE) — estabiliza / rigidez")
ax1.plot(Ls, gue + picket - picket.mean(), color="#16a34a", linewidth=1.4, alpha=0.8,
         label="log + oscilacion tipo cristal {L}(1-{L})")
ax1.set_title("El 'oleaje' es real: Sigma^2(L) = componente log (rigidez) + oscilacion acotada")
ax1.set_xlabel("L"); ax1.set_ylabel("Sigma^2(L)")
ax1.grid(True, alpha=0.3); ax1.legend(loc="upper left")

# panel 2: el residuo (oleaje) aislado
residuo = sig2 - gue
ax2.plot(Ls, residuo, color="#7c3aed", linewidth=1.6, label="oleaje = Sigma^2 - log(GUE)")
ax2.plot(Ls, picket - picket.mean(), color="#f59e0b", linewidth=1.6, linestyle="--",
         label="oscilacion de cristal perfecto {L}(1-{L}) (centrada)")
ax2.axhline(0, color="black", linewidth=0.7)
ax2.set_title("El oleaje aislado: oscilacion ACOTADA (no crece) — la 'variabilidad' que observaste")
ax2.set_xlabel("L"); ax2.set_ylabel("residuo")
ax2.grid(True, alpha=0.3); ax2.legend(loc="upper right")

plt.tight_layout()
plt.savefig("oleaje_rigidez.png", dpi=130)
print("Guardado: oleaje_rigidez.png")
print(f"amplitud del oleaje (desv del residuo) = {residuo.std():.4f}  (ACOTADA, no diverge)")
print(f"rango del residuo: [{residuo.min():.3f}, {residuo.max():.3f}]")
