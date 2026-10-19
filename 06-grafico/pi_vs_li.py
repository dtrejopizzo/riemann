"""
pi(x) vs Li(x): the prime-counting function against its smooth approximation.

- pi(x)  = number of primes <= x  (step function, actual)
- x/ln x = first approximation (prime number theorem)
- Li(x)  = logarithmic integral, the BEST smooth approximation to pi(x)

The Riemann hypothesis is equivalent to the error |pi(x) - Li(x)| being
as small as possible: it grows like ~sqrt(x)*ln(x). The size of the error
is controlled by the real parts of the zeta zeros. If all zeros lie on
Re(s)=1/2, the error is bounded by sqrt(x) up to logarithms; if one were off
the line, the error would be larger.
"""
import math
import matplotlib.pyplot as plt

X_MAX = 100000
PASO = 200  # sampling step in x for the smooth curves

# --- pi(x) via the sieve of Eratosthenes ---
def criba(n):
    es = bytearray([1]) * (n + 1)
    es[0] = es[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if es[i]:
            es[i * i::i] = bytearray(len(es[i * i::i]))
    return es

es_primo = criba(X_MAX)

# cumulative pi(x)
pi = [0] * (X_MAX + 1)
c = 0
for x in range(X_MAX + 1):
    c += es_primo[x]
    pi[x] = c

# --- Li(x) = integral_2^x dt/ln(t)  (trapezoidal rule) ---
def Li(x):
    if x < 2:
        return 0.0
    n_pasos = 2000
    a, b = 2.0, float(x)
    h = (b - a) / n_pasos
    s = 0.5 * (1.0 / math.log(a) + 1.0 / math.log(b))
    for k in range(1, n_pasos):
        t = a + k * h
        s += 1.0 / math.log(t)
    return s * h

xs = list(range(2, X_MAX + 1, PASO))
pi_vals = [pi[x] for x in xs]
li_vals = [Li(x) for x in xs]
pnt_vals = [x / math.log(x) for x in xs]  # x/ln(x)

# --- Figure: two panels ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 11))

# Panel 1: the three curves
ax1.plot(xs, pi_vals, color="#dc2626", linewidth=2.2, label=r"$\pi(x)$  (actual primes)")
ax1.plot(xs, li_vals, color="#16a34a", linewidth=1.8, linestyle="--", label=r"$\mathrm{Li}(x)$  (best smooth approx.)")
ax1.plot(xs, pnt_vals, color="#2563eb", linewidth=1.8, linestyle=":", label=r"$x/\ln x$  (simple approx.)")
ax1.set_title(r"$\pi(x)$ vs its approximations, up to x = 100,000")
ax1.set_xlabel("x")
ax1.set_ylabel("number of primes <= x")
ax1.grid(True, alpha=0.3)
ax1.legend()

# Panel 2: the error pi(x) - Li(x) and the RH-type bound ~sqrt(x)*ln(x)
error = [pi[x] - Li(x) for x in xs]
cota_sup = [math.sqrt(x) * math.log(x) / (2 * math.pi) for x in xs]
cota_inf = [-c for c in cota_sup]

ax2.plot(xs, error, color="#7c3aed", linewidth=1.8, label=r"$\pi(x) - \mathrm{Li}(x)$  (actual error)")
ax2.plot(xs, cota_sup, color="#f59e0b", linewidth=1.5, linestyle="--",
         label=r"RH-type bound  $\pm\frac{\sqrt{x}\,\ln x}{2\pi}$")
ax2.plot(xs, cota_inf, color="#f59e0b", linewidth=1.5, linestyle="--")
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_title("The error stays TRAPPED inside a band ~sqrt(x): this is what the line 1/2 guarantees")
ax2.set_xlabel("x")
ax2.set_ylabel(r"$\pi(x) - \mathrm{Li}(x)$")
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.savefig("pi_vs_li.png", dpi=130)

# --- Report ---
print(f"pi(100000)      = {pi[X_MAX]}")
print(f"Li(100000)      = {Li(X_MAX):.1f}")
print(f"100000/ln       = {X_MAX/math.log(X_MAX):.1f}")
print(f"error pi - Li   = {pi[X_MAX]-Li(X_MAX):.1f}")
print(f"sqrt(x)         = {math.sqrt(X_MAX):.1f}")
