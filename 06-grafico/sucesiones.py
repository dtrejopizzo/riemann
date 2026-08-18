import matplotlib.pyplot as plt

# --- Primeros 500 pares (2n) ---
pares = [2 * n for n in range(1, 501)]

# --- Primeros 500 primos (criba simple) ---
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

primos = primeros_primos(500)

indices = list(range(1, 501))

# --- Gráfico ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.scatter(indices, pares, s=10, color="#2563eb")
ax1.set_title("Primeros 500 números pares (2n)")
ax1.set_xlabel("n (posición)")
ax1.set_ylabel("valor")
ax1.grid(True, alpha=0.3)

ax2.scatter(indices, primos, s=10, color="#dc2626")
ax2.set_title("Primeros 500 números primos")
ax2.set_xlabel("n (posición)")
ax2.set_ylabel("valor")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("sucesiones.png", dpi=130)
print("Pares: primero =", pares[0], " ultimo =", pares[-1])
print("Primos: primero =", primos[0], " ultimo =", primos[-1])
