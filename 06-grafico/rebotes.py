"""
Measure the 'intensity' of each bounce (peak at u=log p^k) of the zero signal
and find its decay law.  h(u) = (1/N) sum_k cos(gamma_k u).
"""
import math
import numpy as np
import matplotlib.pyplot as plt

gammas = np.loadtxt("zeros_10000.txt")
N = len(gammas)

fs = 8000.0
U_MAX = 6.0
u = np.arange(0, U_MAX, 1.0/fs)
h = np.zeros_like(u)
for g in gammas:
    h += np.cos(g * u)
h /= N

# prime powers and their logs
def es_primo(n):
    if n < 2: return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0: return False
    return True
pp = []
for n in range(2, int(math.e**U_MAX)):
    m, f, p = n, 2, None
    while f*f <= m:
        if m % f == 0:
            p = f
            while m % f == 0: m//=f
            break
        f += 1
    if p is None: p, m = n, 1
    if m == 1:
        pp.append((math.log(n), n))  # n = prime power

# local peak height near each log(p^k)
alturas, us_pp, ns = [], [], []
for (lu, n) in pp:
    idx = int(lu*fs)
    w = 40
    seg = np.abs(h[max(0,idx-w):idx+w])
    if len(seg):
        alturas.append(seg.max())
        us_pp.append(lu)
        ns.append(n)
alturas = np.array(alturas); us_pp = np.array(us_pp); ns = np.array(ns, float)

# fit: height ~ C * n^{-alpha}  <=>  log height = log C - alpha*u
mask = alturas > 0
A = np.polyfit(us_pp[mask], np.log(alturas[mask]), 1)
alpha = -A[0]
print(f"Measured decay law: height ~ n^(-{alpha:.3f})  (e^(-{alpha:.3f} u))")
print(f"  1/2 would be x^-0.5 (critical line);  measured alpha = {alpha:.3f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.stem(us_pp, alturas, basefmt=" ", linefmt="#7c3aed", markerfmt="o")
uu = np.linspace(us_pp.min(), us_pp.max(), 200)
ax1.plot(uu, np.exp(A[1])*np.exp(-alpha*uu), color="#dc2626", linewidth=2,
         label=f"fit  ~ e^(-{alpha:.2f} u) = n^(-{alpha:.2f})")
ax1.plot(uu, np.exp(A[1])*np.exp(-0.5*uu), color="#16a34a", linewidth=2,
         linestyle="--", label="law 1/2  (n^-0.5, critical line)")
ax1.set_title("Intensity of each bounce (peak at log p) vs. height u")
ax1.set_xlabel("u = log(x)"); ax1.set_ylabel("peak height")
ax1.legend(); ax1.grid(True, alpha=0.3)

# log scale to see the line
ax2.scatter(us_pp[mask], np.log(alturas[mask]), s=20, color="#7c3aed", label="bounces (data)")
ax2.plot(uu, A[1]-alpha*uu, color="#dc2626", linewidth=2, label=f"slope -{alpha:.3f}")
ax2.plot(uu, A[1]-0.5*uu, color="#16a34a", linewidth=2, linestyle="--", label="slope -0.5")
ax2.set_title("Same data on a log scale: the slope IS the decay exponent")
ax2.set_xlabel("u = log(x)"); ax2.set_ylabel("log(height)")
ax2.legend(); ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("rebotes.png", dpi=130)
print("Saved: rebotes.png")
