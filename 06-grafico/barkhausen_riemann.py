"""
La analogia de Barkhausen: los ceros de zeta como modos de un oscilador.

Cada cero rho = beta + i*gamma aporta al conteo de primos un modo
    x^rho / x^(1/2) = e^{(beta - 1/2) u} * e^{i gamma u}   con u = ln x
es decir un modo lineal e^{sigma u} e^{i omega u} con:
    sigma = beta - 1/2   (tasa de la envolvente)
    omega = gamma        (frecuencia)

- beta > 1/2 : envolvente crece  -> DIVERGE (inestable)
- beta < 1/2 : envolvente decae  -> MUERE  (sobreamortiguado)
- beta = 1/2 : envolvente constante -> OSCILACION SOSTENIDA (Barkhausen / RH)
"""
import math
import matplotlib.pyplot as plt

gamma = 14.134725  # frecuencia del primer cero no trivial de zeta
u = [k * 0.002 for k in range(0, 1500)]  # u = ln x

def modo(beta):
    return [math.exp((beta - 0.5) * uu) * math.cos(gamma * uu) for uu in u]

def envolvente(beta):
    return [math.exp((beta - 0.5) * uu) for uu in u]

casos = [
    (0.70, "#dc2626", r"$\beta = 0.70$  →  DIVERGE (inestable)"),
    (0.50, "#16a34a", r"$\beta = 0.50$  →  OSCILA sostenido  (Barkhausen = RH)"),
    (0.30, "#2563eb", r"$\beta = 0.30$  →  MUERE (sobreamortiguado)"),
]

fig, ax = plt.subplots(figsize=(13, 8))

for beta, color, etiqueta in casos:
    m = modo(beta)
    env = envolvente(beta)
    ax.plot(u, m, color=color, linewidth=1.8, label=etiqueta)
    ax.plot(u, env, color=color, linewidth=1.0, linestyle="--", alpha=0.5)
    ax.plot(u, [-e for e in env], color=color, linewidth=1.0, linestyle="--", alpha=0.5)

ax.axhline(0, color="black", linewidth=0.8)
ax.set_title("Modos de zeta como un oscilador:  solo beta = 1/2 cumple la condicion de Barkhausen")
ax.set_xlabel(r"$u = \ln x$")
ax.set_ylabel(r"contribucion normalizada  $e^{(\beta-1/2)u}\cos(\gamma u)$")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("barkhausen_riemann.png", dpi=130)

print("gamma (1er cero) =", gamma)
for beta, _, _ in casos:
    env_final = math.exp((beta - 0.5) * u[-1])
    print(f"beta={beta}:  envolvente en u={u[-1]:.1f}  ->  {env_final:.3f}")
