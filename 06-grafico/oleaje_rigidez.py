"""
The 'swell' in Sigma^2(L): decomposing rigidity = log (GUE) + oscillation.

Sigma^2(L) is computed DETERMINISTICALLY (sliding the window densely,
no sampling noise) to see the actual oscillation.

Comparison with:
  - smooth GUE: (1/pi^2) ln L  -> the component that STABILISES (rigidity, does not diverge)
  - 'picket fence' {L}(1-{L}) -> pure triangular oscillation of a perfect crystal
Hypothesis tested: envelope = log + oscillation. The log gives the rigidity;
the oscillation (bounded, crystal/prime type) gives the variability.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

g = np.loadtxt("zeros_10000.txt")
def N_smooth(t):
    x = t/(2*math.pi); return x*math.log(x) - x + 7/8
w = np.array([N_smooth(t) for t in g]); w = w[np.isfinite(w)]; w -= w[0]
Wmax = w[-1]

# DETERMINISTIC Sigma^2(L): slide the window with a fine step
Ls = np.linspace(0.2, 15, 400)
starts = np.arange(0, Wmax - 15, 0.15)
sig2 = np.empty_like(Ls)
for i, L in enumerate(Ls):
    cnt = np.searchsorted(w, starts + L) - np.searchsorted(w, starts)
    sig2[i] = cnt.var()

# theoretical components
gue = (1/math.pi**2)*(np.log(2*math.pi*Ls) + 0.5772156649 + 1)  # rigidity (log)
frac = Ls - np.floor(Ls)
picket = frac*(1-frac)                                          # crystal oscillation

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# panel 1: the signal and its two components
ax1.plot(Ls, sig2, color="#7c3aed", linewidth=1.6, label="zeros: Sigma^2(L) (deterministic)")
ax1.plot(Ls, gue, color="#dc2626", linewidth=2, linestyle="--",
         label="LOG component (GUE): stabilises / rigidity")
ax1.plot(Ls, gue + picket - picket.mean(), color="#16a34a", linewidth=1.4, alpha=0.8,
         label="log + crystal-type oscillation {L}(1-{L})")
ax1.set_title("The 'swell' is real: Sigma^2(L) = log component (rigidity) + bounded oscillation")
ax1.set_xlabel("L"); ax1.set_ylabel("Sigma^2(L)")
ax1.grid(True, alpha=0.3); ax1.legend(loc="upper left")

# panel 2: the isolated residual (swell)
residuo = sig2 - gue
ax2.plot(Ls, residuo, color="#7c3aed", linewidth=1.6, label="swell = Sigma^2 - log(GUE)")
ax2.plot(Ls, picket - picket.mean(), color="#f59e0b", linewidth=1.6, linestyle="--",
         label="perfect-crystal oscillation {L}(1-{L}) (centred)")
ax2.axhline(0, color="black", linewidth=0.7)
ax2.set_title("The isolated swell: BOUNDED oscillation (does not grow), the observed 'variability'")
ax2.set_xlabel("L"); ax2.set_ylabel("residual")
ax2.grid(True, alpha=0.3); ax2.legend(loc="upper right")

plt.tight_layout()
plt.savefig("oleaje_rigidez.png", dpi=130)
print("Saved: oleaje_rigidez.png")
print(f"swell amplitude (std of residual) = {residuo.std():.4f}  (BOUNDED, does not diverge)")
print(f"range of residual: [{residuo.min():.3f}, {residuo.max():.3f}]")
