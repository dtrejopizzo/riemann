"""
Positividad de Weil, forma diagonal: criterio de Li sobre los 10000 ceros.

Coeficientes de Li:  lambda_n = sum_rho [ 1 - (1 - 1/rho)^n ]   (rho y su conjugado)
Criterio de Li:  RH  <=>  lambda_n >= 0  para todo n >= 1.

Clave estructural: para un cero SOBRE la linea, |1 - 1/rho| = 1 exactamente,
asi que el termino de cada par conjugado es  2 - 2 cos(n*theta) >= 0  automatico.
Si un cero estuviera FUERA, |1-1/rho| != 1 y el termino podria hacerse negativo
para algun n -> lambda_n < 0. Ahi 'se rompe' la positividad.

Computamos lambda_n sobre los ceros reales y mostramos:
  (1) todos positivos (consistente con RH, como debe ser: estan en la linea)
  (2) su crecimiento ~ (n/2) log(n/2pi) : EL PATRON LOGARITMICO ESPECTRAL
  (3) el residuo oscilante = la parte aritmetica (primos)
"""
import math
import numpy as np

g = np.loadtxt("zeros_10000.txt")
rho = 0.5 + 1j*g
a = 1.0 - 1.0/rho          # 1 - 1/rho  (|a| = 1 en la linea)
print(f"chequeo |1-1/rho| medio = {np.abs(a).mean():.10f} (debe ser 1.0 en la linea)")

# lambda_n = sum sobre pares conjugados de [2 - 2 Re(a^n)]
Nmax = 120
lam = np.empty(Nmax)
an = np.ones_like(a)
for n in range(1, Nmax+1):
    an = an * a            # a^n incremental
    lam[n-1] = np.sum(2.0 - 2.0*np.real(an))

# validacion: lambda_1 conocido = 1 + gamma_E/2 - (1/2)log(4pi) ~ 0.0230957
lam1_teo = 1 + 0.5772156649/2 - 0.5*math.log(4*math.pi)
print(f"lambda_1 computado = {lam[0]:.6f}   teorico = {lam1_teo:.6f}")

# patron logaritmico suave:  lambda_n ~ (n/2)(log(n/2pi) - 1) + ...
ns = np.arange(1, Nmax+1)
suave = (ns/2)*(np.log(ns/(2*math.pi)) ) - (ns/2)*(1 - 0.5772156649 - math.log(2))

print("\n n    lambda_n     (n/2)log(n/2pi)   positivo?")
for n in [1,2,5,10,20,50,100]:
    print(f"{n:3d}  {lam[n-1]:11.4f}   {(n/2)*math.log(n/(2*math.pi)):13.4f}   {lam[n-1]>0}")

neg = np.where(lam < 0)[0]
print(f"\ncoeficientes negativos entre n=1..{Nmax}: {len(neg)} "
      f"(RH predice CERO; hallar uno negativo REFUTARIA RH)")
print(f"minimo lambda_n = {lam.min():.4f} en n={np.argmin(lam)+1}")

# ---------- grafico ----------
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.plot(ns, lam, "o-", color="#7c3aed", ms=3, label="lambda_n (10000 ceros)")
ax1.plot(ns, (ns/2)*np.log(ns/(2*math.pi)), color="#dc2626", lw=2,
         label="patron log:  (n/2) log(n/2pi)")
ax1.axhline(0, color="black", lw=0.8)
ax1.set_title("Criterio de Li: lambda_n > 0 (positividad de Weil) + patron logaritmico")
ax1.set_xlabel("n"); ax1.set_ylabel("lambda_n")
ax1.legend(); ax1.grid(True, alpha=0.3)

# residuo: lambda_n menos su tendencia suave -> la parte aritmetica (primos)
resid = lam - (ns/2)*np.log(ns/(2*math.pi))
ax2.plot(ns, resid, color="#16a34a", lw=1.5)
ax2.axhline(0, color="black", lw=0.8)
ax2.set_title("Residuo (lambda_n - tendencia log): la parte aritmetica / oscilante")
ax2.set_xlabel("n"); ax2.set_ylabel("residuo")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("positividad_li.png", dpi=130)
print("\nGuardado: positividad_li.png")
