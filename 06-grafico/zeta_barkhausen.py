"""
Zeta as an oscillator waveform (Barkhausen reading).

Panel A: the Riemann-Siegel function Z(t).
    It is REAL on the critical line and |Z(t)| = |zeta(1/2 + it)|.
    It is literally the WAVEFORM of the oscillator: it crosses zero exactly
    at each zeta zero (gamma = 14.13, 21.02, 25.01, ...). The peaks between
    zeros are the "pattern of maxima".

Panel B: |zeta(sigma + it)| for sigma = 0.3, 0.5, 0.7.
    ONLY at sigma = 1/2 does the curve TOUCH zero (in this range).
    Off the line, |zeta| does not reach zero here -> no marginal oscillation.
    This is the Barkhausen condition: the modulus vanishes only on the edge 1/2.
"""
import mpmath as mp
import matplotlib.pyplot as plt

mp.mp.dps = 25  # precision

T_MAX = 50.0
N = 1500
ts = [T_MAX * k / N for k in range(1, N + 1)]

# --- Panel A: Riemann-Siegel Z(t) (actual waveform) ---
Z = [float(mp.siegelz(t)) for t in ts]

# first known nontrivial zeros (imaginary part gamma)
gammas = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
          37.586178, 40.918719, 43.327073, 48.005151, 49.773832]

# --- Panel B: |zeta(sigma + it)| on three vertical lines ---
sigmas = [(0.3, "#2563eb", "sigma = 0.3  (inside)"),
          (0.5, "#16a34a", "sigma = 0.5  (critical line)"),
          (0.7, "#dc2626", "sigma = 0.7  (outside)")]
abs_zeta = {}
for sig, _, _ in sigmas:
    abs_zeta[sig] = [float(abs(mp.zeta(mp.mpc(sig, t)))) for t in ts]

# --- Figure ---
fig, (axA, axB) = plt.subplots(2, 1, figsize=(14, 11))

# Panel A
axA.plot(ts, Z, color="#7c3aed", linewidth=1.4, label="Riemann-Siegel Z(t)")
axA.axhline(0, color="black", linewidth=0.8)
for g in gammas:
    if g <= T_MAX:
        axA.axvline(g, color="#f59e0b", linewidth=1.0, linestyle=":", alpha=0.8)
axA.plot([], [], color="#f59e0b", linestyle=":", label="zeta zeros (gamma)")
axA.set_title("Zeta as a waveform:  Z(t) crosses zero EXACTLY at each zeta zero")
axA.set_xlabel("t  (height on the critical line)")
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
axB.set_title("|zeta(sigma + it)|:  ONLY at sigma = 1/2 does the wave touch zero (Barkhausen condition)")
axB.set_xlabel("t")
axB.set_ylabel("|zeta(sigma + it)|")
axB.set_ylim(0, 3)
axB.grid(True, alpha=0.3)
axB.legend(loc="upper right")

plt.tight_layout()
plt.savefig("zeta_barkhausen.png", dpi=130)

# report: minima of |zeta| for each sigma
print("Minimum of |zeta| for 0 < t <= 50:")
for sig, _, _ in sigmas:
    m = min(abs_zeta[sig])
    print(f"  sigma={sig}:  min |zeta| = {m:.4f}")
