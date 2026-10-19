"""
The spectrum of 10000 Riemann zeros: looking for order in the chaos.

Three views:

  (A) The raw zeros and the TRIVIAL envelope N(T) ~ (T/2pi)log(T/2pi).
      The mean spacing shrinks like 2pi/log(T). This must be REMOVED.

  (B) UNFOLDING: each zero is normalised by its expected position N(gamma),
      so that the mean spacing becomes 1. The histogram of the normalised
      spacings s is compared with:
        - GUE (Hermitian random matrices): level REPULSION,
          P(s) -> 0 as s -> 0. This is the actual pattern (Montgomery-Odlyzko).
        - Poisson (random points): P(s) = e^{-s}, no repulsion.
      If the zeros follow GUE, the 'chaos' is really a diffuse crystal:
      the zeros AVOID each other, like eigenvalues of a self-adjoint operator.

  (C) Transform of the zero process: the oscillating part has peaks at
      t = log(p^k), the LOGARITHMS of the prime powers. Exact dual of the
      plot 'primos_predicen_ceros': the zeros also 'know' the primes.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

# ---------- load zeros ----------
gammas = np.loadtxt("zeros_10000.txt")
N = len(gammas)
print(f"{N} zeros loaded. gamma_1={gammas[0]:.4f}, gamma_N={gammas[-1]:.4f}")

# ---------- (A) trivial envelope: theoretical N(T) ----------
def N_teorico(t):
    x = t / (2 * math.pi)
    return x * math.log(x) - x + 7.0 / 8.0

# ---------- (B) unfolding ----------
# each zero gamma_k is mapped to its expected count, so the mean spacing -> 1
unfolded = np.array([N_teorico(g) for g in gammas])
spacings = np.diff(unfolded)
spacings = spacings[np.isfinite(spacings)]
print(f"normalised spacing: mean={spacings.mean():.4f} (should be ~1), "
      f"std={spacings.std():.4f}")

# theoretical curves
s = np.linspace(0, 4, 400)
# GUE (Wigner surmise for beta=2)
P_gue = (32 / math.pi**2) * s**2 * np.exp(-4 * s**2 / math.pi)
# Poisson
P_poisson = np.exp(-s)

# ---------- (C) transform: zeros -> primes ----------
# sum over zeros of cos(u * gamma), which resonates at u = log(n)
us = np.linspace(0.5, 3.6, 3000)   # u = log(x); log 2=0.69, log3=1.10, ...
# only the first ~2000 zeros (moderate height) are used, for sharpness
G = gammas[:2000]
spec = np.array([np.abs(np.sum(np.exp(-1j * u * G))) for u in us])

# expected peak positions: log of prime powers
primos = [2, 3, 5, 7, 11, 13]
picos_u = []
for p in primos:
    k = 1
    while p**k <= 40:
        picos_u.append((math.log(p**k), p, k))
        k += 1

# ---------- figure ----------
fig = plt.figure(figsize=(15, 12))

# (A)
axA = fig.add_subplot(3, 1, 1)
Ts = np.linspace(gammas[0], gammas[-1], 500)
axA.plot(gammas, np.arange(1, N + 1), color="#dc2626", linewidth=1.5,
         label="actual zero count")
axA.plot(Ts, [N_teorico(t) for t in Ts], color="#16a34a", linewidth=1.5,
         linestyle="--", label="theoretical envelope N(T)=(T/2pi)log(T/2pi)")
axA.set_title(f"(A) The {N} raw zeros follow the trivial envelope N(T), which must be removed")
axA.set_xlabel("gamma (height of the zero)")
axA.set_ylabel("zero index")
axA.grid(True, alpha=0.3)
axA.legend(loc="upper left")

# (B)
axB = fig.add_subplot(3, 1, 2)
axB.hist(spacings, bins=60, range=(0, 4), density=True, color="#93c5fd",
         edgecolor="#2563eb", alpha=0.8, label="Riemann zeros (10000)")
axB.plot(s, P_gue, color="#dc2626", linewidth=2.5, label="GUE (random matrices): REPULSION")
axB.plot(s, P_poisson, color="#6b7280", linewidth=2, linestyle="--", label="Poisson (random): no repulsion")
axB.set_title("(B) ORDER IN THE CHAOS: the spacings follow GUE, not Poisson. The zeros REPEL.")
axB.set_xlabel("normalised spacing s (mean = 1)")
axB.set_ylabel("density P(s)")
axB.set_xlim(0, 4)
axB.grid(True, alpha=0.3)
axB.legend(loc="upper right")

# (C)
axC = fig.add_subplot(3, 1, 3)
axC.plot(us, spec, color="#7c3aed", linewidth=1.2, label="| sum_zeros exp(-i u gamma) |")
for (u, p, k) in picos_u:
    if us[0] <= u <= us[-1]:
        axC.axvline(u, color="#f59e0b", linewidth=1.2, linestyle=":", alpha=0.9)
        lbl = f"log {p}" if k == 1 else f"log {p}^{k}"
        axC.annotate(lbl, xy=(u, spec.max()*0.9), rotation=90,
                     fontsize=8, color="#b45309", va="top", ha="right")
axC.set_title("(C) The transform of the zeros peaks at log(p^k): the zeros 'know' the primes")
axC.set_xlabel("u = log(x)")
axC.set_ylabel("magnitude")
axC.grid(True, alpha=0.3)
axC.legend(loc="upper right")

plt.tight_layout()
plt.savefig("espectro_ceros.png", dpi=130)
print("Saved: espectro_ceros.png")

# statistical report
from math import sqrt
# fraction of small spacings (repulsion): GUE predicts very few < 0.3
frac_chicos = np.mean(spacings < 0.3)
print(f"Fraction of spacings < 0.3: {frac_chicos:.4f} "
      f"(Poisson would give ~{1-math.exp(-0.3):.3f}, GUE much less -> repulsion)")
