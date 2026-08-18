"""
Los ceros de Riemann y los numeros pares en el MISMO plano complejo.

- Numeros pares (2,4,6,...): son REALES -> viven sobre el eje horizontal (Im=0).
- Ceros no triviales de zeta: son COMPLEJOS  rho = 1/2 +- i*gamma
  -> viven sobre la recta vertical Re = 1/2 (la recta critica).

Objetos de naturaleza distinta: unos sobre el eje real, otros sobre una
recta vertical. Por eso los primos/pares NO 'caen' sobre la recta 1/2:
son numeros reales; los que caen ahi son los ceros.
"""
import mpmath as mp
import matplotlib.pyplot as plt

mp.mp.dps = 30

# --- Primeros 20 ceros no triviales: parte imaginaria gamma ---
gammas = [float(mp.zetazero(n).imag) for n in range(1, 21)]
print("Primeros 20 gammas:")
for i, g in enumerate(gammas, 1):
    print(f"  cero {i}: 0.5 + i*{g:.4f}")

# cada cero viene con su conjugado: 1/2 + i*gamma  y  1/2 - i*gamma
zeros_re = [0.5] * (2 * len(gammas))
zeros_im = gammas + [-g for g in gammas]

# --- Primeros 20 pares sobre el eje real ---
pares = [2 * n for n in range(1, 21)]
pares_im = [0] * len(pares)

# --- Figura ---
fig, ax = plt.subplots(figsize=(13, 10))

# banda critica 0 <= Re <= 1
ax.axvspan(0, 1, color="#fde68a", alpha=0.25, label="banda critica  0 ≤ Re ≤ 1")
# recta critica Re = 1/2
ax.axvline(0.5, color="#16a34a", linewidth=1.5, linestyle="--", label="recta critica  Re = 1/2")
# ejes
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="gray", linewidth=0.6)

# ceros de zeta
ax.scatter(zeros_re, zeros_im, s=70, color="#dc2626", zorder=5,
           label="ceros de ζ(s)  =  1/2 ± i·γ")

# numeros pares
ax.scatter(pares, pares_im, s=70, color="#2563eb", marker="s", zorder=5,
           label="números pares (reales, Im = 0)")

# etiquetas de algunos ceros
for g in gammas[:6]:
    ax.annotate(f"γ={g:.2f}", xy=(0.5, g), xytext=(0.5 + 1.2, g),
                fontsize=8, color="#dc2626", va="center")

ax.set_xlim(-2, 42)
ax.set_ylim(-55, 55)
ax.set_xlabel("parte real  (Re)")
ax.set_ylabel("parte imaginaria  (Im)")
ax.set_title("Ceros de Riemann vs números pares en el plano complejo\n"
             "(los ceros en la recta vertical 1/2; los pares sobre el eje real)")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig("ceros_vs_pares_plano.png", dpi=130)
print("\nGuardado: ceros_vs_pares_plano.png")
