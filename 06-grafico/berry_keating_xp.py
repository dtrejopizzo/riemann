"""
Modelo xp de Berry-Keating: H = (xp + px)/2, discretizado como matriz hermitica.

Pregunta: la 'regulacion' de este Hamiltoniano candidato, reproduce la
estadistica GUE (repulsion + rigidez) que medimos en los ceros?

Construimos H = (X P + P X)/2 con P = -i d/dx (hermitico) en una grilla,
diagonalizamos, desdoblamos empiricamente y comparamos la distribucion de
espaciados contra GUE, Poisson y los ceros reales.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

# ---------- construir xp hermitico ----------
Ngrid = 3000
a, b = 0.5, 60.0
x = np.linspace(a, b, Ngrid)
dx = x[1] - x[0]

# P = -i * D,  D antisimetrico (diferencias centradas) -> P hermitico
D = np.zeros((Ngrid, Ngrid))
idx = np.arange(Ngrid - 1)
D[idx, idx + 1] = 1.0 / (2 * dx)
D[idx + 1, idx] = -1.0 / (2 * dx)
P = -1j * D
X = np.diag(x)
H = 0.5 * (X @ P + P @ X)
H = 0.5 * (H + H.conj().T)  # forzar hermiticidad numerica

print("Diagonalizando xp...")
E = np.linalg.eigvalsh(H)
E = np.sort(E.real)
# quedarnos con el bulk (sacar bordes contaminados)
E = E[E > 5]
E = E[E < E.max() * 0.6]
print(f"{len(E)} autovalores en el bulk")

# ---------- desdoblado empirico (ajuste polinomico a la escalera) ----------
n = np.arange(len(E))
coef = np.polyfit(E, n, 8)
unf = np.polyval(coef, E)
sp_xp = np.diff(unf)
sp_xp = sp_xp[(sp_xp > 0) & (sp_xp < 6)]
sp_xp /= sp_xp.mean()

# ---------- ceros reales ----------
g = np.loadtxt("zeros_10000.txt")
def N_smooth(t):
    xx = t/(2*math.pi); return xx*math.log(xx) - xx + 7/8
wz = np.array([N_smooth(t) for t in g])
sp_z = np.diff(wz); sp_z = sp_z[np.isfinite(sp_z)]; sp_z /= sp_z.mean()

# ---------- curvas ----------
s = np.linspace(0, 4, 400)
P_gue = (32/math.pi**2) * s**2 * np.exp(-4*s**2/math.pi)
P_poi = np.exp(-s)

fig, ax = plt.subplots(figsize=(13, 7))
ax.hist(sp_xp, bins=50, range=(0,4), density=True, color="#fbbf24",
        alpha=0.55, label=f"espectro xp de Berry-Keating ({len(sp_xp)} niveles)")
ax.hist(sp_z, bins=50, range=(0,4), density=True, histtype="step",
        color="#2563eb", linewidth=2, label="ceros de Riemann (10000)")
ax.plot(s, P_gue, color="#dc2626", linewidth=2.5, label="GUE (repulsion)")
ax.plot(s, P_poi, color="#6b7280", linewidth=2, linestyle="--", label="Poisson (integrable)")
ax.set_title("xp de Berry-Keating vs ceros: reproduce la MEDIA N(T) pero NO la estadistica GUE")
ax.set_xlabel("espaciado normalizado s")
ax.set_ylabel("densidad P(s)")
ax.set_xlim(0, 4)
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig("berry_keating_xp.png", dpi=130)
print("Guardado: berry_keating_xp.png")

# diagnostico: fraccion de espaciados chicos (repulsion?)
print(f"xp:    frac(s<0.3) = {np.mean(sp_xp<0.3):.3f}")
print(f"ceros: frac(s<0.3) = {np.mean(sp_z<0.3):.3f}")
print(f"(GUE ~0.01 con repulsion; Poisson ~0.26 sin repulsion; "
      f"picket-fence ~0 pero por rigidez cristalina, no por repulsion)")
