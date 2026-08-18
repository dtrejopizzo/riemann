"""
La formula explicita de Riemann: los ceros RECONSTRUYEN a los primos.

Funcion escalon de Chebyshev  psi(x) = suma de ln(p) sobre potencias de primo p^k <= x.
Salta en 2, 3, 4=2^2, 5, 7, 8=2^3, 9=3^2, 11, ...  El salto es ln(p).

Formula explicita (Riemann - von Mangoldt):
    psi(x) = x - sum_rho x^rho/rho - ln(2pi) - (1/2)ln(1 - x^-2)

Usando N ceros rho = 1/2 +- i*gamma, la suma de ondas se acerca cada vez
mas a la escalera de los primos. Con pocos ceros: onda suave. Con muchos:
aparecen los escalones EXACTAMENTE en los primos.
"""
import math
import mpmath as mp
import matplotlib.pyplot as plt

mp.mp.dps = 30

X_MAX = 30.0
NPTS = 1200
xs = [1.5 + (X_MAX - 1.5) * k / NPTS for k in range(NPTS + 1)]

# --- escalera real psi(x) ---
def psi_real(x):
    total = 0.0
    p = 2
    # potencias de primos <= x
    for n in range(2, int(x) + 1):
        # es n una potencia de primo? hallar factor primo
        m = n
        f = 2
        primo = None
        while f * f <= m:
            if m % f == 0:
                primo = f
                while m % f == 0:
                    m //= f
                break
            f += 1
        if primo is None:
            primo = m  # n es primo
            m = 1
        if m == 1:  # n = primo^k  -> es potencia de primo
            total += math.log(primo)
    return total

psi_vals = [psi_real(x) for x in xs]

# --- aproximacion por N ceros ---
def psi_aprox(x, gammas):
    # x - sum_rho x^rho/rho - ln(2pi) - 0.5 ln(1 - x^-2)
    s = mp.mpf(x)
    for g in gammas:
        rho = mp.mpc(0.5, g)
        s -= (mp.power(x, rho) / rho)
        rho_c = mp.mpc(0.5, -g)
        s -= (mp.power(x, rho_c) / rho_c)
    s -= mp.log(2 * mp.pi)
    s -= 0.5 * mp.log(1 - mp.power(x, -2))
    return float(s.real)

# primeros ceros
NUM_CEROS = 50
gammas = [float(mp.zetazero(n).imag) for n in range(1, NUM_CEROS + 1)]

conjuntos = [
    (1,  "#93c5fd", "1 cero"),
    (10, "#3b82f6", "10 ceros"),
    (50, "#1e3a8a", "50 ceros"),
]

fig, ax = plt.subplots(figsize=(14, 8))

# escalera real
ax.plot(xs, psi_vals, color="#dc2626", linewidth=2.5, label=r"$\psi(x)$ real (escalera de los primos)", zorder=5)

# aproximaciones
for n, color, etiqueta in conjuntos:
    gs = gammas[:n]
    aprox = [psi_aprox(x, gs) for x in xs]
    ax.plot(xs, aprox, color=color, linewidth=1.4, label=f"reconstruccion con {etiqueta}")

# marcar los primos y potencias de primo con lineas verticales
saltos = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29]
for s in saltos:
    if s <= X_MAX:
        ax.axvline(s, color="gray", linewidth=0.6, linestyle=":", alpha=0.5)

ax.set_title("Formula explicita: sumando ondas (una por cada cero) aparecen los ESCALONES en los primos")
ax.set_xlabel("x")
ax.set_ylabel(r"$\psi(x)$")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("formula_explicita.png", dpi=130)
print("Guardado: formula_explicita.png")
print("Escalones en potencias de primo:", saltos)
