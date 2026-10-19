"""
Weil positivity, diagonal form: Li's criterion on the 10000 zeros.

Li coefficients:  lambda_n = sum_rho [ 1 - (1 - 1/rho)^n ]   (rho and its conjugate)
Li's criterion:  RH  <=>  lambda_n >= 0  for all n >= 1.

Structural point: for a zero ON the line, |1 - 1/rho| = 1 exactly,
so the term of each conjugate pair is  2 - 2 cos(n*theta) >= 0  automatically.
If a zero were OFF the line, |1-1/rho| != 1 and the term could become negative
for some n -> lambda_n < 0. That is where positivity 'breaks'.

lambda_n is computed over the actual zeros, showing:
  (1) all positive (consistent with RH, as it must be: they lie on the line)
  (2) growth ~ (n/2) log(n/2pi): THE SPECTRAL LOGARITHMIC PATTERN
  (3) the oscillating residual = the arithmetic part (primes)
"""
import math
import numpy as np

g = np.loadtxt("zeros_10000.txt")
rho = 0.5 + 1j*g
a = 1.0 - 1.0/rho          # 1 - 1/rho  (|a| = 1 on the line)
print(f"check: mean |1-1/rho| = {np.abs(a).mean():.10f} (must be 1.0 on the line)")

# lambda_n = sum over conjugate pairs of [2 - 2 Re(a^n)]
Nmax = 120
lam = np.empty(Nmax)
an = np.ones_like(a)
for n in range(1, Nmax+1):
    an = an * a            # a^n incremental
    lam[n-1] = np.sum(2.0 - 2.0*np.real(an))

# validation: known lambda_1 = 1 + gamma_E/2 - (1/2)log(4pi) ~ 0.0230957
lam1_teo = 1 + 0.5772156649/2 - 0.5*math.log(4*math.pi)
print(f"lambda_1 computed = {lam[0]:.6f}   theoretical = {lam1_teo:.6f}")

# smooth logarithmic pattern:  lambda_n ~ (n/2)(log(n/2pi) - 1) + ...
ns = np.arange(1, Nmax+1)
suave = (ns/2)*(np.log(ns/(2*math.pi)) ) - (ns/2)*(1 - 0.5772156649 - math.log(2))

print("\n n    lambda_n     (n/2)log(n/2pi)   positive?")
for n in [1,2,5,10,20,50,100]:
    print(f"{n:3d}  {lam[n-1]:11.4f}   {(n/2)*math.log(n/(2*math.pi)):13.4f}   {lam[n-1]>0}")

neg = np.where(lam < 0)[0]
print(f"\nnegative coefficients for n=1..{Nmax}: {len(neg)} "
      f"(RH predicts NONE; a negative one would REFUTE RH)")
print(f"minimum lambda_n = {lam.min():.4f} at n={np.argmin(lam)+1}")

# ---------- plot ----------
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.plot(ns, lam, "o-", color="#7c3aed", ms=3, label="lambda_n (10000 zeros)")
ax1.plot(ns, (ns/2)*np.log(ns/(2*math.pi)), color="#dc2626", lw=2,
         label="log pattern:  (n/2) log(n/2pi)")
ax1.axhline(0, color="black", lw=0.8)
ax1.set_title("Li criterion: lambda_n > 0 (Weil positivity) + logarithmic pattern")
ax1.set_xlabel("n"); ax1.set_ylabel("lambda_n")
ax1.legend(); ax1.grid(True, alpha=0.3)

# residual: lambda_n minus its smooth trend -> the arithmetic part (primes)
resid = lam - (ns/2)*np.log(ns/(2*math.pi))
ax2.plot(ns, resid, color="#16a34a", lw=1.5)
ax2.axhline(0, color="black", lw=0.8)
ax2.set_title("Residual (lambda_n - log trend): the arithmetic / oscillating part")
ax2.set_xlabel("n"); ax2.set_ylabel("residual")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("positividad_li.png", dpi=130)
print("\nSaved: positividad_li.png")
