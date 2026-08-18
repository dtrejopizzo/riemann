"""
Zeta como oscilador, comportamiento hasta t = 100.000.

Una traza densa de Z(t) en [0, 100000] es una mancha (hay ~150.000 ceros),
asi que mostramos el comportamiento con:

  Fila 1 (ancho completo): patron GLOBAL hasta t=100000
     - N(t) ~ (t/2pi) ln(t/2pi): cuantos ceros hay hasta altura t
     - espaciado medio 2pi/ln(t/2pi): la oscilacion se aprieta con t

  Fila 2: cuatro VENTANAS-zoom de la onda real Z(t) centradas en
     t ~ 100, 1000, 10000, 100000. Cada una muestra ~12 ceros. Se ve que
     la onda sigue siendo MARGINAL (cruza cero) pero mas apretada al subir.
"""
import math
import mpmath as mp
import matplotlib.pyplot as plt

mp.mp.dps = 30

# ---------- Fila 1: patron global (analitico, barato) ----------
def N_teorico(t):
    if t < 2 * math.pi:
        return 0.0
    x = t / (2 * math.pi)
    return x * math.log(x) - x + 7.0 / 8.0

def espaciado(t):
    return 2 * math.pi / math.log(t / (2 * math.pi))

T_MAX = 100000
tg = [T_MAX * k / 1000 for k in range(1, 1001)]
N_vals = [N_teorico(t) for t in tg]
esp_vals = [espaciado(t) for t in tg]

# ---------- Fila 2: ventanas-zoom de Z(t) real ----------
centros = [100, 1000, 10000, 100000]

def ventana(centro, n_ceros=12):
    # ancho ~ n_ceros espaciados medios
    ancho = n_ceros * espaciado(centro)
    t0 = max(1.0, centro - ancho / 2)
    t1 = centro + ancho / 2
    pts = 700
    ts = [t0 + (t1 - t0) * k / pts for k in range(pts + 1)]
    Z = [float(mp.siegelz(t)) for t in ts]
    return ts, Z

print("Calculando ventanas-zoom (Z de Riemann-Siegel)...")
ventanas = {}
for c in centros:
    ventanas[c] = ventana(c)
    print(f"  t ~ {c}: espaciado medio de ceros = {espaciado(c):.3f}")

# ---------- Figura ----------
fig = plt.figure(figsize=(15, 11))
gs = fig.add_gridspec(3, 4, height_ratios=[1.1, 1.1, 0.05])

# N(t)
ax1 = fig.add_subplot(gs[0, 0:2])
ax1.plot(tg, N_vals, color="#7c3aed", linewidth=2)
ax1.set_title("N(t): cantidad de ceros hasta altura t")
ax1.set_xlabel("t"); ax1.set_ylabel("nro. de ceros")
ax1.grid(True, alpha=0.3)
ax1.annotate(f"~{int(N_vals[-1]):,} ceros\nhasta t=100.000",
             xy=(T_MAX, N_vals[-1]), xytext=(0.45, 0.55),
             textcoords="axes fraction",
             arrowprops=dict(arrowstyle="->", color="black"))

# espaciado
ax2 = fig.add_subplot(gs[0, 2:4])
ax2.plot(tg, esp_vals, color="#16a34a", linewidth=2)
ax2.set_title("Espaciado medio entre ceros: la oscilacion se APRIETA con t")
ax2.set_xlabel("t"); ax2.set_ylabel(r"$2\pi/\ln(t/2\pi)$")
ax2.grid(True, alpha=0.3)

# ventanas-zoom
colores = ["#2563eb", "#0891b2", "#db2777", "#dc2626"]
for i, c in enumerate(centros):
    ax = fig.add_subplot(gs[1, i])
    ts, Z = ventanas[c]
    ax.plot(ts, Z, color=colores[i], linewidth=1.0)
    ax.axhline(0, color="black", linewidth=0.7)
    ax.set_title(f"Z(t) cerca de t = {c:,}")
    ax.set_xlabel("t")
    if i == 0:
        ax.set_ylabel("Z(t)")
    ax.grid(True, alpha=0.3)

fig.suptitle("Zeta como oscilador marginal hasta t = 100.000  —  patron global + ventanas de la onda real",
             fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig("zeta_barkhausen_100k.png", dpi=130)

print(f"\nN(100000) teorico = {N_vals[-1]:,.0f} ceros")
print(f"espaciado en t=100:    {espaciado(100):.3f}")
print(f"espaciado en t=100000: {espaciado(100000):.3f}")
