"""
Why 'proving that ON-LINE zeros contribute positively' does NOT prove RH.

Contribution of a zero to lambda_n (with its images under the functional equation).
An off-line zero comes in a quadruple: beta+i*g, beta-i*g, (1-beta)+i*g, (1-beta)-i*g.

  - beta = 0.5 (ON-LINE):  contribution ALWAYS >= 0  (trivial, |1-1/rho|=1)
  - beta = 0.7 (OFF-LINE): contribution becomes NEGATIVE for some n
    -> THAT is the term that would break Li positivity.

Moral: positivity of the ON-LINE terms is automatic and carries no information.
The content is in excluding the OFF-LINE terms, which an argument about on-line zeros does not touch.
"""
import numpy as np

g = 14.134725   # sample height (1st zero)

def contrib(beta, g, nmax=200):
    # quadruple of zeros: beta±ig y (1-beta)±ig
    betas = sorted(set([beta, 1-beta]))
    rhos = []
    for b in betas:
        rhos += [complex(b, g), complex(b, -g)]
    rhos = np.array(rhos)
    a = 1 - 1/rhos
    out = np.empty(nmax)
    an = np.ones_like(a)
    for n in range(1, nmax+1):
        an = an * a
        out[n-1] = np.sum(1 - an).real
    return out

on  = contrib(0.5, g)   # on the line
off = contrib(0.7, g)   # off the line

print("beta=0.5 (ON-LINE):")
print(f"   minimum contribution over n=1..200 = {on.min():.4f}  (at n={on.argmin()+1})")
print(f"   -> always >= 0 ? {np.all(on >= -1e-9)}")
print()
print("beta=0.7 (OFF-LINE):")
print(f"   minimum contribution over n=1..200 = {off.min():.4f}  (at n={off.argmin()+1})")
print(f"   -> becomes NEGATIVE ? {np.any(off < 0)}")
print()
print("KEY: ON-LINE positivity is automatic (proves nothing).")
print("The only dangerous term is the OFF-LINE one.")
print("Excluding THAT term for every possible zero is the open problem.")

import matplotlib.pyplot as plt
ns = np.arange(1, 201)
fig, ax = plt.subplots(figsize=(13,6))
ax.plot(ns, on, color="#16a34a", lw=2, label="ON-LINE zero (beta=0.5): always >= 0")
ax.plot(ns, off, color="#dc2626", lw=2, label="OFF-LINE zero (beta=0.7): becomes NEGATIVE")
ax.axhline(0, color="black", lw=0.8)
ax.set_title("An off-line zero is the only thing that can break Li positivity")
ax.set_xlabel("n"); ax.set_ylabel("contribution to lambda_n")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig("porque_offline.png", dpi=130)
print("\nSaved: porque_offline.png")
