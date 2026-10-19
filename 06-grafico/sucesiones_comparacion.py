import math
import matplotlib.pyplot as plt

CANTIDAD = 10000

# --- First 10000 even numbers (2n) ---
pares = [2 * n for n in range(1, CANTIDAD + 1)]

# --- First 10000 primes (simple sieve) ---
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

# --- Prime number theorem curve: p_n ~ n*ln(n) ---
teorica = [n * math.log(n) for n in indices]

# --- Improved approximation: p_n ~ n*(ln(n) + ln(ln(n))) ---
# (ln(ln(n)) is undefined at n=1; the formula starts at n=2)
mejorada = [None]  # placeholder for n=1
mejorada += [n * (math.log(n) + math.log(math.log(n))) for n in indices[1:]]

# --- Single plot, same axes ---
plt.figure(figsize=(12, 8))

plt.plot(indices, pares, color="#2563eb", linewidth=2, label="Evens (2n)")
plt.scatter(indices, primos, s=3, color="#dc2626", label="Primes (n-th prime)")
plt.plot(indices, teorica, color="#16a34a", linewidth=2, linestyle="--",
         label="Approximation  n·ln(n)")
plt.plot(indices[1:], mejorada[1:], color="#9333ea", linewidth=2, linestyle=":",
         label="Improved approximation  n·(ln n + ln ln n)")

plt.title("Evens vs primes on the same axes: first 10000 terms")
plt.xlabel("n (position)")
plt.ylabel("value")
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig("sucesiones_comparacion.png", dpi=130)
print("Even 10000 =", pares[-1])
print("Prime 10000 =", primos[-1])
print("n*ln(n) at 10000 =", round(teorica[-1]))
print("n*(ln n + ln ln n) at 10000 =", round(mejorada[-1]))
