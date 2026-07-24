"""
Medir la 'intensidad' de cada rebote (pico en u=log p^k) de la senal de ceros
y ver que ley de decaimiento sigue.  h(u) = (1/N) sum_k cos(gamma_k u).
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

# prime powers y sus logs
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
        pp.append((math.log(n), n))  # n = potencia de primo

# altura del pico local cerca de cada log(p^k)
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

# ajuste: altura ~ C * n^{-alpha}  <=>  log altura = log C - alpha*u
mask = alturas > 0
A = np.polyfit(us_pp[mask], np.log(alturas[mask]), 1)
alpha = -A[0]
print(f"Ley de decaimiento medida: altura ~ n^(-{alpha:.3f})  (e^(-{alpha:.3f} u))")
print(f"  1/2 seria x^-0.5 (linea critica);  medido alpha = {alpha:.3f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.stem(us_pp, alturas, basefmt=" ", linefmt="#7c3aed", markerfmt="o")
uu = np.linspace(us_pp.min(), us_pp.max(), 200)
ax1.plot(uu, np.exp(A[1])*np.exp(-alpha*uu), color="#dc2626", linewidth=2,
         label=f"ajuste  ~ e^(-{alpha:.2f} u) = n^(-{alpha:.2f})")
ax1.plot(uu, np.exp(A[1])*np.exp(-0.5*uu), color="#16a34a", linewidth=2,
         linestyle="--", label="ley 1/2  (n^-0.5, linea critica)")
ax1.set_title("Intensidad de cada rebote (pico en log p) vs. altura u")
ax1.set_xlabel("u = log(x)"); ax1.set_ylabel("altura del pico")
ax1.legend(); ax1.grid(True, alpha=0.3)

# escala log para ver la recta
ax2.scatter(us_pp[mask], np.log(alturas[mask]), s=20, color="#7c3aed", label="rebotes (datos)")
ax2.plot(uu, A[1]-alpha*uu, color="#dc2626", linewidth=2, label=f"pendiente -{alpha:.3f}")
ax2.plot(uu, A[1]-0.5*uu, color="#16a34a", linewidth=2, linestyle="--", label="pendiente -0.5")
ax2.set_title("Mismo dato en escala log: la pendiente ES el exponente de decaimiento")
ax2.set_xlabel("u = log(x)"); ax2.set_ylabel("log(altura)")
ax2.legend(); ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("rebotes.png", dpi=130)
print("Guardado: rebotes.png")
