"""
Zeta como forma de onda de oscilador (lectura Barkhausen).

Panel A: la funcion Z(t) de Riemann-Siegel.
    Es REAL sobre la recta critica y |Z(t)| = |zeta(1/2 + it)|.
    Es, literalmente, la FORMA DE ONDA del oscilador: cruza cero exactamente
    en cada cero de zeta (gamma = 14.13, 21.02, 25.01, ...). Los picos entre
    ceros son el "patron de maxima" que se busca.

Panel B: |zeta(sigma + it)| para sigma = 0.3, 0.5, 0.7.
    SOLO en sigma = 1/2 la curva TOCA el cero (resonancia perfecta).
    Fuera de la recta, |zeta| nunca baja a cero -> no hay oscilacion marginal.
    Esa es la condicion de Barkhausen: el modulo se anula solo en el filo 1/2.
"""
import mpmath as mp
import matplotlib.pyplot as plt

mp.mp.dps = 25  # precision

T_MAX = 50.0
N = 1500
ts = [T_MAX * k / N for k in range(1, N + 1)]

# --- Panel A: Z(t) de Riemann-Siegel (forma de onda real) ---
Z = [float(mp.siegelz(t)) for t in ts]

# primeros ceros no triviales conocidos (parte imaginaria gamma)
gammas = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
          37.586178, 40.918719, 43.327073, 48.005151, 49.773832]

# --- Panel B: |zeta(sigma + it)| para tres lineas verticales ---
sigmas = [(0.3, "#2563eb", "sigma = 0.3  (dentro)"),
          (0.5, "#16a34a", "sigma = 0.5  (recta critica)"),
          (0.7, "#dc2626", "sigma = 0.7  (afuera)")]
abs_zeta = {}
for sig, _, _ in sigmas:
    abs_zeta[sig] = [float(abs(mp.zeta(mp.mpc(sig, t)))) for t in ts]

# --- Figura ---
fig, (axA, axB) = plt.subplots(2, 1, figsize=(14, 11))

# Panel A
axA.plot(ts, Z, color="#7c3aed", linewidth=1.4, label="Z(t) de Riemann-Siegel")
axA.axhline(0, color="black", linewidth=0.8)
for g in gammas:
    if g <= T_MAX:
        axA.axvline(g, color="#f59e0b", linewidth=1.0, linestyle=":", alpha=0.8)
axA.plot([], [], color="#f59e0b", linestyle=":", label="ceros de zeta (gamma)")
axA.set_title("Zeta como forma de onda:  Z(t) cruza cero EXACTAMENTE en cada cero de zeta")
axA.set_xlabel("t  (altura sobre la recta critica)")
axA.set_ylabel("Z(t)")
axA.grid(True, alpha=0.3)
axA.legend(loc="upper right")

# Panel B
for sig, color, etiqueta in sigmas:
    axB.plot(ts, abs_zeta[sig], color=color, linewidth=1.5, label=etiqueta)
for g in gammas:
    if g <= T_MAX:
        axB.axvline(g, color="#f59e0b", linewidth=0.8, linestyle=":", alpha=0.5)
axB.axhline(0, color="black", linewidth=0.8)
axB.set_title("|zeta(sigma + it)|:  SOLO en sigma = 1/2 la onda toca el cero (condicion de Barkhausen)")
axB.set_xlabel("t")
axB.set_ylabel("|zeta(sigma + it)|")
axB.set_ylim(0, 3)
axB.grid(True, alpha=0.3)
axB.legend(loc="upper right")

plt.tight_layout()
plt.savefig("zeta_barkhausen.png", dpi=130)

# reporte: minimos de |zeta| en cada sigma
print("Minimo de |zeta| en 0 < t <= 50:")
for sig, _, _ in sigmas:
    m = min(abs_zeta[sig])
    print(f"  sigma={sig}:  min |zeta| = {m:.4f}")
