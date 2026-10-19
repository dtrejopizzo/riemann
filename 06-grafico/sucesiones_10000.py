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

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.scatter(indices, pares, s=2, color="#2563eb")
ax1.set_title("First 10000 even numbers (2n)")
ax1.set_xlabel("n (position)")
ax1.set_ylabel("value")
ax1.grid(True, alpha=0.3)

ax2.scatter(indices, primos, s=2, color="#dc2626")
ax2.set_title("First 10000 primes")
ax2.set_xlabel("n (position)")
ax2.set_ylabel("value")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("sucesiones_10000.png", dpi=130)
print("Evens: first =", pares[0], " last =", pares[-1])
print("Primes: first =", primos[0], " last =", primos[-1])
