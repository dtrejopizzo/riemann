"""
El patron oculto de los primos vive en el dominio de la frecuencia.

Tomamos SOLO los primos (via la funcion de von Mangoldt Lambda(n), que vale
ln(p) en potencias de primo p^k y 0 en el resto) y formamos la suma espectral

    F(t) = | sum_{n<=N} Lambda(n) * n^{-1/2} * n^{-i t} |

Esta suma es la parte de -zeta'/zeta(1/2 + i t), que tiene POLOS en los ceros
de zeta. Por eso F(t) desarrolla PICOS exactamente en t = gamma
(las alturas de los ceros de Riemann): 14.13, 21.02, 25.01, ...

Conclusion: los primos, mirados en frecuencia, 'dibujan' los ceros de zeta.
Ese es el patron. No es una formula del proximo primo: es una DUALIDAD entre
los primos (eje real) y los ceros (frecuencias).
"""
import math
import mpmath as mp
import matplotlib.pyplot as plt

# --- von Mangoldt Lambda(n) para n <= N ---
N = 100000
def lambda_vonmangoldt(N):
    lam = [0.0] * (N + 1)
    es = bytearray([1]) * (N + 1)
    es[0] = es[1] = 0
    for i in range(2, N + 1):
        if es[i]:  # i es primo
            lp = math.log(i)
            pk = i
            while pk <= N:
                lam[pk] = lp
                # marcar multiplos como no primos
                pk_next = pk * i
                pk = pk_next
            for j in range(i * i, N + 1, i):
                es[j] = 0
    return lam

print("Calculando Lambda(n)...")
lam = lambda_vonmangoldt(N)
# lista de (n, Lambda(n)) con Lambda != 0
terminos = [(n, lam[n]) for n in range(2, N + 1) if lam[n] > 0]
print(f"  {len(terminos)} potencias de primo <= {N}")

# --- suma espectral F(t) ---
T_MIN = 8.0   # arrancamos despues del polo en t=0 para ver los picos
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

print("Evaluando la suma espectral F(t)...")
F_vals = [F(t) for t in ts]

# --- ceros reales de zeta para comparar ---
gammas = [float(mp.zetazero(n).imag) for n in range(1, 16)]
gammas = [g for g in gammas if g <= T_MAX]

# --- grafico ---
fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(ts, F_vals, color="#7c3aed", linewidth=1.3,
        label="F(t) = | suma de Lambda(n)*n^(-1/2-it) |  (hecha SOLO con primos)")
for i, g in enumerate(gammas):
    ax.axvline(g, color="#dc2626", linewidth=1.2, linestyle="--", alpha=0.8,
               label="ceros de zeta (gamma)" if i == 0 else None)

ax.set_title("Los primos 'dibujan' los ceros: F(t) hecha SOLO con primos tiene picos en cada gamma")
ax.set_xlabel("t  (frecuencia = altura sobre la recta critica)")
ax.set_ylabel("F(t)")
ax.set_xlim(T_MIN, T_MAX)
ax.set_ylim(0, 40)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig("primos_predicen_ceros.png", dpi=130)
print("Guardado: primos_predicen_ceros.png")

# reporte: valor de F en cada gamma vs entre gammas
print("\nF(t) en los ceros (deberia ser alto):")
for g in gammas[:8]:
    print(f"  gamma={g:6.3f}:  F={F(g):8.2f}")
