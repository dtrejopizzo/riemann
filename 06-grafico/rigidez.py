"""
Spectral rigidity: the signature of the 'regulation mechanism'.

Number variance Sigma^2(L) = variance of the number of (unfolded) zeros
in an interval of length L.
  - Poisson (random, NO regulation): Sigma^2(L) = L   (linear growth)
  - GUE (WITH regulation / repulsion): Sigma^2(L) ~ (1/pi^2) ln(L)  (log growth)

If the zeros are rigid (log instead of linear), the system RESISTS
fluctuations: it is the AGC / self-regulation preventing growth and collapse.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

gammas = np.loadtxt("zeros_10000.txt")

# unfold: smooth N(T) -> points with mean spacing 1
def N_smooth(t):
    x = t / (2*math.pi)
    return x*math.log(x) - x + 7.0/8.0
w = np.array([N_smooth(g) for g in gammas])   # unfolded positions
w = w[np.isfinite(w)]
w = w - w[0]
Wmax = w[-1]
print(f"{len(w)} unfolded zeros, total range = {Wmax:.0f} (mean spacing 1)")

# Sigma^2(L): for each L, many random intervals, variance of the count
Ls = np.linspace(0.5, 30, 60)
sigma2 = []
rng = np.random.default_rng(0)
for L in Ls:
    starts = rng.uniform(0, Wmax - L, size=4000)
    counts = np.array([np.searchsorted(w, s+L) - np.searchsorted(w, s) for s in starts])
    sigma2.append(counts.var())
sigma2 = np.array(sigma2)

# theoretical curves
poisson = Ls
gue = (1/math.pi**2) * (np.log(2*math.pi*Ls) + 0.5772156649 + 1)

fig, ax = plt.subplots(figsize=(13, 7))
ax.plot(Ls, sigma2, "o", color="#7c3aed", markersize=5, label="Riemann zeros (10000)")
ax.plot(Ls, gue, color="#dc2626", linewidth=2.5, label="GUE  ~ (1/pi^2) ln L   (WITH regulation)")
ax.plot(Ls, poisson, color="#6b7280", linewidth=2, linestyle="--", label="Poisson  = L   (NO regulation)")
ax.set_title("Spectral rigidity: the zeros resist fluctuations (growth like ln L, not L)")
ax.set_xlabel("L  (interval length, in mean spacings)")
ax.set_ylabel("number variance  Sigma^2(L)")
ax.set_ylim(0, 12)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("rigidez.png", dpi=130)
print("Saved: rigidez.png")

# report
for L in [5, 10, 20]:
    i = np.argmin(np.abs(Ls-L))
    print(f"L={L:2d}:  zeros Sigma^2={sigma2[i]:5.2f}   GUE={gue[i]:5.2f}   Poisson={poisson[i]:5.2f}")
