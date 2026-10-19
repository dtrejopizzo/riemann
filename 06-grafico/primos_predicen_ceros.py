"""
The hidden pattern of the primes lives in the frequency domain.

Take ONLY the primes (via the von Mangoldt function Lambda(n), equal to
ln(p) on prime powers p^k and 0 elsewhere) and form the spectral sum

    F(t) = | sum_{n<=N} Lambda(n) * n^{-1/2} * n^{-i t} |

This sum is part of -zeta'/zeta(1/2 + i t), which has POLES at the zeta
zeros. Hence F(t) develops PEAKS exactly at t = gamma
(the heights of the Riemann zeros): 14.13, 21.02, 25.01, ...

Conclusion: the primes, viewed in frequency, 'draw' the zeta zeros.
That is the pattern. It is not a formula for the next prime: it is a DUALITY
between the primes (real axis) and the zeros (frequencies).
"""
import math
import mpmath as mp
import matplotlib.pyplot as plt

# --- von Mangoldt Lambda(n) for n <= N ---
N = 100000
def lambda_vonmangoldt(N):
    lam = [0.0] * (N + 1)
    es = bytearray([1]) * (N + 1)
    es[0] = es[1] = 0
    for i in range(2, N + 1):
        if es[i]:  # i is prime
            lp = math.log(i)
            pk = i
            while pk <= N:
                lam[pk] = lp
                # mark multiples as composite
                pk_next = pk * i
                pk = pk_next
            for j in range(i * i, N + 1, i):
                es[j] = 0
    return lam

print("Computing Lambda(n)...")
lam = lambda_vonmangoldt(N)
# list of (n, Lambda(n)) with Lambda != 0
terminos = [(n, lam[n]) for n in range(2, N + 1) if lam[n] > 0]
print(f"  {len(terminos)} prime powers <= {N}")

# --- spectral sum F(t) ---
T_MIN = 8.0   # start after the pole at t=0 to see the peaks
T_MAX = 60.0
NPTS = 2200
ts = [T_MIN + (T_MAX - T_MIN) * k / NPTS for k in range(NPTS + 1)]

def F(t):
    re = 0.0
    im = 0.0
    for n, L in terminos:
        w = L / math.sqrt(n)          # Lambda(n) * n^{-1/2}
        ang = -t * math.log(n)        # n^{-i t} = e^{-i t ln n}
        re += w * math.cos(ang)
        im += w * math.sin(ang)
    return math.hypot(re, im)

print("Evaluating the spectral sum F(t)...")
F_vals = [F(t) for t in ts]

# --- actual zeta zeros for comparison ---
gammas = [float(mp.zetazero(n).imag) for n in range(1, 16)]
gammas = [g for g in gammas if g <= T_MAX]

# --- plot ---
fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(ts, F_vals, color="#7c3aed", linewidth=1.3,
        label="F(t) = | sum of Lambda(n)*n^(-1/2-it) |  (built ONLY from primes)")
for i, g in enumerate(gammas):
    ax.axvline(g, color="#dc2626", linewidth=1.2, linestyle="--", alpha=0.8,
               label="zeta zeros (gamma)" if i == 0 else None)

ax.set_title("The primes 'draw' the zeros: F(t), built ONLY from primes, peaks at each gamma")
ax.set_xlabel("t  (frequency = height on the critical line)")
ax.set_ylabel("F(t)")
ax.set_xlim(T_MIN, T_MAX)
ax.set_ylim(0, 40)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig("primos_predicen_ceros.png", dpi=130)
print("Saved: primos_predicen_ceros.png")

# report: value of F at each gamma vs between gammas
print("\nF(t) at the zeros (should be large):")
for g in gammas[:8]:
    print(f"  gamma={g:6.3f}:  F={F(g):8.2f}")
