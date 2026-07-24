"""
pi(x) vs Li(x): la funcion que cuenta primos frente a su aproximacion suave.

- pi(x)  = cantidad de primos <= x  (funcion escalon, real)
- x/ln x = primera aproximacion (teorema de los numeros primos)
- Li(x)  = integral logaritmica, la MEJOR aproximacion suave a pi(x)

La Hipotesis de Riemann equivale a decir que el error |pi(x) - Li(x)|
es lo mas chico posible: crece como ~sqrt(x)*ln(x). Ese tamanio del error
esta controlado por la parte real de los ceros de zeta. Si todos los ceros
caen en Re(s)=1/2, el error queda acotado por sqrt(x); si alguno se saliera,
el error seria mayor.
"""
import math
import matplotlib.pyplot as plt

X_MAX = 100000
PASO = 200  # muestreamos x para las curvas suaves

# --- pi(x) via criba de Eratostenes ---
def criba(n):
    es = bytearray([1]) * (n + 1)
    es[0] = es[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if es[i]:
            es[i * i::i] = bytearray(len(es[i * i::i]))
    return es

es_primo = criba(X_MAX)

# pi(x) acumulado
pi = [0] * (X_MAX + 1)
c = 0
for x in range(X_MAX + 1):
    c += es_primo[x]
    pi[x] = c

# --- Li(x) = integral_2^x dt/ln(t)  (regla del trapecio) ---
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

# --- Figura: dos paneles ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 11))

# Panel 1: las tres curvas
ax1.plot(xs, pi_vals, color="#dc2626", linewidth=2.2, label=r"$\pi(x)$  (primos reales)")
ax1.plot(xs, li_vals, color="#16a34a", linewidth=1.8, linestyle="--", label=r"$\mathrm{Li}(x)$  (mejor aprox. suave)")
ax1.plot(xs, pnt_vals, color="#2563eb", linewidth=1.8, linestyle=":", label=r"$x/\ln x$  (aprox. simple)")
ax1.set_title(r"$\pi(x)$ vs sus aproximaciones  —  hasta x = 100.000")
ax1.set_xlabel("x")
ax1.set_ylabel("cantidad de primos <= x")
ax1.grid(True, alpha=0.3)
ax1.legend()

# Panel 2: el error pi(x) - Li(x) y la cota RH  ~sqrt(x)*ln(x)
error = [pi[x] - Li(x) for x in xs]
cota_sup = [math.sqrt(x) * math.log(x) / (2 * math.pi) for x in xs]
cota_inf = [-c for c in cota_sup]

ax2.plot(xs, error, color="#7c3aed", linewidth=1.8, label=r"$\pi(x) - \mathrm{Li}(x)$  (error real)")
ax2.plot(xs, cota_sup, color="#f59e0b", linewidth=1.5, linestyle="--",
         label=r"cota tipo RH  $\pm\frac{\sqrt{x}\,\ln x}{2\pi}$")
ax2.plot(xs, cota_inf, color="#f59e0b", linewidth=1.5, linestyle="--")
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_title("El error queda ATRAPADO dentro de una banda ~sqrt(x) — eso es lo que garantiza la recta 1/2")
ax2.set_xlabel("x")
ax2.set_ylabel(r"$\pi(x) - \mathrm{Li}(x)$")
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.savefig("pi_vs_li.png", dpi=130)

# --- Reporte ---
print(f"pi(100000)      = {pi[X_MAX]}")
print(f"Li(100000)      = {Li(X_MAX):.1f}")
print(f"100000/ln       = {X_MAX/math.log(X_MAX):.1f}")
print(f"error pi - Li   = {pi[X_MAX]-Li(X_MAX):.1f}")
print(f"sqrt(x)         = {math.sqrt(X_MAX):.1f}")
