"""
Berry-Keating xp model: H = (xp + px)/2, discretised as a Hermitian matrix.

Question: does the 'regularisation' of this candidate Hamiltonian reproduce the
GUE statistics (repulsion + rigidity) measured on the zeros?

We build H = (X P + P X)/2 with P = -i d/dx (Hermitian) on a grid,
diagonalise, unfold empirically and compare the spacing distribution
with GUE, Poisson and the actual zeros.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

# ---------- build Hermitian xp ----------
Ngrid = 3000
a, b = 0.5, 60.0
x = np.linspace(a, b, Ngrid)
dx = x[1] - x[0]

# P = -i * D,  D antisymmetric (centred differences) -> P Hermitian
D = np.zeros((Ngrid, Ngrid))
idx = np.arange(Ngrid - 1)
D[idx, idx + 1] = 1.0 / (2 * dx)
D[idx + 1, idx] = -1.0 / (2 * dx)
P = -1j * D
X = np.diag(x)
H = 0.5 * (X @ P + P @ X)
H = 0.5 * (H + H.conj().T)  # enforce numerical Hermiticity

print("Diagonalising xp...")
E = np.linalg.eigvalsh(H)
E = np.sort(E.real)
# keep the bulk (drop contaminated edges)
E = E[E > 5]
E = E[E < E.max() * 0.6]
print(f"{len(E)} eigenvalues in the bulk")

# ---------- empirical unfolding (polynomial fit to the staircase) ----------
n = np.arange(len(E))
coef = np.polyfit(E, n, 8)
unf = np.polyval(coef, E)
sp_xp = np.diff(unf)
sp_xp = sp_xp[(sp_xp > 0) & (sp_xp < 6)]
sp_xp /= sp_xp.mean()

# ---------- actual zeros ----------
g = np.loadtxt("zeros_10000.txt")
def N_smooth(t):
    xx = t/(2*math.pi); return xx*math.log(xx) - xx + 7/8
wz = np.array([N_smooth(t) for t in g])
sp_z = np.diff(wz); sp_z = sp_z[np.isfinite(sp_z)]; sp_z /= sp_z.mean()

# ---------- curves ----------
s = np.linspace(0, 4, 400)
P_gue = (32/math.pi**2) * s**2 * np.exp(-4*s**2/math.pi)
P_poi = np.exp(-s)

fig, ax = plt.subplots(figsize=(13, 7))
ax.hist(sp_xp, bins=50, range=(0,4), density=True, color="#fbbf24",
        alpha=0.55, label=f"Berry-Keating xp spectrum ({len(sp_xp)} levels)")
ax.hist(sp_z, bins=50, range=(0,4), density=True, histtype="step",
        color="#2563eb", linewidth=2, label="Riemann zeros (10000)")
ax.plot(s, P_gue, color="#dc2626", linewidth=2.5, label="GUE (repulsion)")
ax.plot(s, P_poi, color="#6b7280", linewidth=2, linestyle="--", label="Poisson (integrable)")
ax.set_title("Berry-Keating xp vs zeros: reproduces the MEAN N(T) but NOT the GUE statistics")
ax.set_xlabel("normalised spacing s")
ax.set_ylabel("density P(s)")
ax.set_xlim(0, 4)
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig("berry_keating_xp.png", dpi=130)
print("Saved: berry_keating_xp.png")

# diagnostic: fraction of small spacings (repulsion?)
print(f"xp:    frac(s<0.3) = {np.mean(sp_xp<0.3):.3f}")
print(f"zeros: frac(s<0.3) = {np.mean(sp_z<0.3):.3f}")
print(f"(GUE ~0.01 with repulsion; Poisson ~0.26 without repulsion; "
      f"picket-fence ~0 but from crystalline rigidity, not repulsion)")
