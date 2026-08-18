"""
Por que 'probar que los ceros ON-LINE son positivos' NO prueba RH.

Contribucion de un cero a lambda_n (con sus simetricos por la ecuacion funcional).
Un cero fuera de la linea viene en cuadruple: beta+i*g, beta-i*g, (1-beta)+i*g, (1-beta)-i*g.

  - beta = 0.5 (ON-LINE):  contribucion SIEMPRE >= 0  (trivial, |1-1/rho|=1)
  - beta = 0.7 (OFF-LINE): contribucion se hace NEGATIVA para algun n
    -> ESE es el termino que romperia la positividad de Li.

Moraleja: la positividad de los ON-LINE es automatica e inutil.
RH = descartar los OFF-LINE. Tu argumento no los toca.
"""
import numpy as np

g = 14.134725   # altura de ejemplo (1er cero)

def contrib(beta, g, nmax=200):
    # cuadruple de ceros: beta±ig y (1-beta)±ig
    betas = sorted(set([beta, 1-beta]))
    rhos = []
    for b in betas:
        rhos += [complex(b, g), complex(b, -g)]
    rhos = np.array(rhos)
    a = 1 - 1/rhos
    out = np.empty(nmax)
    an = np.ones_like(a)
    for n in range(1, nmax+1):
        an = an * a
        out[n-1] = np.sum(1 - an).real
    return out

on  = contrib(0.5, g)   # sobre la linea
off = contrib(0.7, g)   # fuera de la linea

print("beta=0.5 (ON-LINE):")
print(f"   minimo de la contribucion en n=1..200 = {on.min():.4f}  (en n={on.argmin()+1})")
print(f"   -> siempre >= 0 ? {np.all(on >= -1e-9)}")
print()
print("beta=0.7 (OFF-LINE):")
print(f"   minimo de la contribucion en n=1..200 = {off.min():.4f}  (en n={off.argmin()+1})")
print(f"   -> se hace NEGATIVA ? {np.any(off < 0)}")
print()
print("CLAVE: la positividad ON-LINE es automatica (no prueba nada).")
print("El unico termino peligroso es el OFF-LINE, que tu argumento NO analiza.")
print("Descartar ESE termino para todo cero posible = RH = abierto.")

import matplotlib.pyplot as plt
ns = np.arange(1, 201)
fig, ax = plt.subplots(figsize=(13,6))
ax.plot(ns, on, color="#16a34a", lw=2, label="cero ON-LINE (beta=0.5): siempre >= 0")
ax.plot(ns, off, color="#dc2626", lw=2, label="cero OFF-LINE (beta=0.7): se hace NEGATIVO")
ax.axhline(0, color="black", lw=0.8)
ax.set_title("Un cero fuera de la linea es lo unico que puede romper la positividad de Li")
ax.set_xlabel("n"); ax.set_ylabel("contribucion a lambda_n")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig("porque_offline.png", dpi=130)
print("\nGuardado: porque_offline.png")
