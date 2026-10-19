"""
The Riemann zeros and the even numbers in the SAME complex plane.

- Even numbers (2,4,6,...): REAL -> they live on the horizontal axis (Im=0).
- Nontrivial zeta zeros: COMPLEX  rho = 1/2 +- i*gamma
  -> they live on the vertical line Re = 1/2 (the critical line).

Objects of different nature: one set on the real axis, the other on a
vertical line. This is why primes/evens do NOT 'fall' on the line 1/2:
they are real numbers; what falls there are the zeros.
"""
import mpmath as mp
import matplotlib.pyplot as plt

mp.mp.dps = 30

# --- First 20 nontrivial zeros: imaginary part gamma ---
gammas = [float(mp.zetazero(n).imag) for n in range(1, 21)]
print("First 20 gammas:")
for i, g in enumerate(gammas, 1):
    print(f"  zero {i}: 0.5 + i*{g:.4f}")

# each zero comes with its conjugate: 1/2 + i*gamma  y  1/2 - i*gamma
zeros_re = [0.5] * (2 * len(gammas))
zeros_im = gammas + [-g for g in gammas]

# --- First 20 even numbers on the real axis ---
pares = [2 * n for n in range(1, 21)]
pares_im = [0] * len(pares)

# --- Figure ---
fig, ax = plt.subplots(figsize=(13, 10))

# critical strip 0 <= Re <= 1
ax.axvspan(0, 1, color="#fde68a", alpha=0.25, label="critical strip  0 ≤ Re ≤ 1")
# critical line Re = 1/2
ax.axvline(0.5, color="#16a34a", linewidth=1.5, linestyle="--", label="critical line  Re = 1/2")
# axes
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="gray", linewidth=0.6)

# zeta zeros
ax.scatter(zeros_re, zeros_im, s=70, color="#dc2626", zorder=5,
           label="zeros of ζ(s)  =  1/2 ± i·γ")

# even numbers
ax.scatter(pares, pares_im, s=70, color="#2563eb", marker="s", zorder=5,
           label="even numbers (real, Im = 0)")

# labels for some zeros
for g in gammas[:6]:
    ax.annotate(f"γ={g:.2f}", xy=(0.5, g), xytext=(0.5 + 1.2, g),
                fontsize=8, color="#dc2626", va="center")

ax.set_xlim(-2, 42)
ax.set_ylim(-55, 55)
ax.set_xlabel("real part  (Re)")
ax.set_ylabel("imaginary part  (Im)")
ax.set_title("Riemann zeros vs even numbers in the complex plane\n"
             "(zeros on the vertical line 1/2; even numbers on the real axis)")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig("ceros_vs_pares_plano.png", dpi=130)
print("\nSaved: ceros_vs_pares_plano.png")
