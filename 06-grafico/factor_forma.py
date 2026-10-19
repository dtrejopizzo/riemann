"""
Spectral form factor K(tau): the central diagnostic of quantum chaos.

K(tau) = (1/N) | sum_j exp(i 2pi tau w_j) |^2   over the unfolded zeros w_j.

Signature of QUANTUM CHAOS (Bohigas-Giannoni-Schmit):
  - linear 'ramp' K(tau) ~ tau for tau < 1  (GUE correlations)
  - 'plateau' K(tau) ~ 1 for tau > 1        (rigidity, Heisenberg time)
At small tau the deviations are governed by the PRIMES (periodic
orbits, Berry's diagonal approximation).

If the zeros show ramp+plateau, they are a quantum-chaos spectrum:
eigenvalues of a self-adjoint operator of a chaotic classical system.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

g = np.loadtxt("zeros_10000.txt")
def N_smooth(t):
    x = t/(2*math.pi); return x*math.log(x) - x + 7/8
w = np.array([N_smooth(t) for t in g]); w = w[np.isfinite(w)]
N = len(w)

# raw K(tau)
taus = np.linspace(0.001, 2.5, 4000)
K = np.empty_like(taus)
for i, tau in enumerate(taus):
    K[i] = np.abs(np.sum(np.exp(1j*2*np.pi*tau*w)))**2 / N

# smoothing (moving average) to see ramp+plateau under the noise
def smooth(y, win):
    k = np.ones(win)/win
    return np.convolve(y, k, mode="same")
Ks = smooth(K, 80)

# theoretical GUE: K_connected(tau) = min(tau,1); K = min(tau,1) + delta part
gue = np.minimum(taus, 1.0)

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(taus, K, color="#c4b5fd", linewidth=0.5, alpha=0.6, label="raw K(tau) (10000 zeros)")
ax.plot(taus, Ks, color="#7c3aed", linewidth=2.2, label="smoothed K(tau)")
ax.plot(taus, gue, color="#dc2626", linewidth=2.2, linestyle="--",
        label="GUE: ramp min(tau,1) + plateau")
ax.axvline(1.0, color="#16a34a", linewidth=1.2, linestyle=":", label="tau=1 (Heisenberg time)")
ax.set_title("Form factor K(tau): RAMP + PLATEAU = quantum-chaos signature in the zeros")
ax.set_xlabel("tau  (time, in units of the Heisenberg time)")
ax.set_ylabel("K(tau)")
ax.set_ylim(0, 1.6)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right")

plt.tight_layout()
plt.savefig("factor_forma.png", dpi=130)
print("Saved: factor_forma.png")

# ramp diagnostic
for t in [0.25, 0.5, 0.75, 1.0, 1.5, 2.0]:
    i = np.argmin(np.abs(taus-t))
    print(f"  tau={t:.2f}:  K={Ks[i]:.3f}   GUE={gue[i]:.3f}")
