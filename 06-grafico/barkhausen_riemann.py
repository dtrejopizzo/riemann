"""
The Barkhausen analogy: the zeta zeros as modes of an oscillator.

Each zero rho = beta + i*gamma contributes to the prime count a mode
    x^rho / x^(1/2) = e^{(beta - 1/2) u} * e^{i gamma u}   con u = ln x
that is, a linear mode e^{sigma u} e^{i omega u} with:
    sigma = beta - 1/2   (envelope rate)
    omega = gamma        (frequency)

- beta > 1/2 : envelope grows  -> DIVERGES (unstable)
- beta < 1/2 : envelope decays  -> DIES  (overdamped)
- beta = 1/2 : constant envelope -> SUSTAINED OSCILLATION (Barkhausen / RH)
"""
import math
import matplotlib.pyplot as plt

gamma = 14.134725  # frequency of the first nontrivial zeta zero
u = [k * 0.002 for k in range(0, 1500)]  # u = ln x

def modo(beta):
    return [math.exp((beta - 0.5) * uu) * math.cos(gamma * uu) for uu in u]

def envolvente(beta):
    return [math.exp((beta - 0.5) * uu) for uu in u]

casos = [
    (0.70, "#dc2626", r"$\beta = 0.70$  →  DIVERGES (unstable)"),
    (0.50, "#16a34a", r"$\beta = 0.50$  →  SUSTAINED oscillation  (Barkhausen = RH)"),
    (0.30, "#2563eb", r"$\beta = 0.30$  →  DIES (overdamped)"),
]

fig, ax = plt.subplots(figsize=(13, 8))

for beta, color, etiqueta in casos:
    m = modo(beta)
    env = envolvente(beta)
    ax.plot(u, m, color=color, linewidth=1.8, label=etiqueta)
    ax.plot(u, env, color=color, linewidth=1.0, linestyle="--", alpha=0.5)
    ax.plot(u, [-e for e in env], color=color, linewidth=1.0, linestyle="--", alpha=0.5)

ax.axhline(0, color="black", linewidth=0.8)
ax.set_title("Zeta modes as an oscillator:  only beta = 1/2 meets the Barkhausen condition")
ax.set_xlabel(r"$u = \ln x$")
ax.set_ylabel(r"normalised contribution  $e^{(\beta-1/2)u}\cos(\gamma u)$")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("barkhausen_riemann.png", dpi=130)

print("gamma (1st zero) =", gamma)
for beta, _, _ in casos:
    env_final = math.exp((beta - 0.5) * u[-1])
    print(f"beta={beta}:  envelope at u={u[-1]:.1f}  ->  {env_final:.3f}")
