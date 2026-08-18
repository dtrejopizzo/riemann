import math
import matplotlib.pyplot as plt

CANTIDAD = 10000

# --- Primeros 10000 pares (2n) ---
pares = [2 * n for n in range(1, CANTIDAD + 1)]

# --- Primeros 10000 primos (criba simple) ---
def primeros_primos(cantidad):
    primos = []
    candidato = 2
    while len(primos) < cantidad:
        es_primo = True
        for p in primos:
            if p * p > candidato:
                break
            if candidato % p == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(candidato)
        candidato += 1
    return primos

primos = primeros_primos(CANTIDAD)

indices = list(range(1, CANTIDAD + 1))

# --- Curva teorica del teorema de los numeros primos: p_n ~ n*ln(n) ---
teorica = [n * math.log(n) for n in indices]

# --- Aproximacion mejorada: p_n ~ n*(ln(n) + ln(ln(n))) ---
# (n=1 no tiene ln(ln(n)); empezamos la formula desde n=2)
mejorada = [None]  # placeholder para n=1
mejorada += [n * (math.log(n) + math.log(math.log(n))) for n in indices[1:]]

# --- Grafico unico, mismos ejes ---
plt.figure(figsize=(12, 8))

plt.plot(indices, pares, color="#2563eb", linewidth=2, label="Pares (2n)")
plt.scatter(indices, primos, s=3, color="#dc2626", label="Primos (n-ésimo primo)")
plt.plot(indices, teorica, color="#16a34a", linewidth=2, linestyle="--",
         label="Aproximación  n·ln(n)")
plt.plot(indices[1:], mejorada[1:], color="#9333ea", linewidth=2, linestyle=":",
         label="Aproximación mejorada  n·(ln n + ln ln n)")

plt.title("Pares vs Primos en el mismo plano (mismos ejes) — primeros 10000 términos")
plt.xlabel("n (posición)")
plt.ylabel("valor")
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig("sucesiones_comparacion.png", dpi=130)
print("Par 10000 =", pares[-1])
print("Primo 10000 =", primos[-1])
print("n*ln(n) en 10000 =", round(teorica[-1]))
print("n*(ln n + ln ln n) en 10000 =", round(mejorada[-1]))
