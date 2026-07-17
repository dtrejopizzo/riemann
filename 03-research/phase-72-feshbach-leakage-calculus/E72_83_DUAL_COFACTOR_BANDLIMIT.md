# E72.83 -- Dual cofactor bandlimit

**Date:** 2026-07-09.
**Role:** identify the first positive compactness mechanism after the dual cofactor transport
identity.

**Correction:** E72.84 replaces the fixed-index version below by the invariant physical-height
version. The observation in this note remains useful as finite-window evidence, but the theorem to
prove is `(PDCT)`, not fixed `|n|` tightness.

## 0. Input

The current minimal theorem is E72.81:

```text
i C_{g,k}(tau_j)
-(exp(i tau_jL)-1)L^(-1)C_{g,1}(tau_j)M_k(tau_j) -> 0,
```

where:

```text
g_{x,s}=B_xC_E^(-1)B_x^*r_s^even.
```

E72.82 showed that the mesh factor alone does not annihilate the residual. The full profile of
`g_{x,s}` matters.

## 1. Bandlimit observation

Although `g_{x,s}` is not close to the plane `span{1,k_x}`, it is numerically tight in frequency for
fixed `s`. Define:

```text
T_M(g):=sum_{|n|>M}|g_n|^2 / sum_n |g_n|^2.
```

The observed data for `s=10+0.2i`:

```text
lambda   N     E(|n|<=2)  E(|n|<=4)  E(|n|<=8)  E(|n|<=16)
12      28       0.005      0.011      0.969      0.999
16      34       0.008      0.016      0.133      0.998
20      40       0.020      0.033      0.123      0.990
24      48       0.005      0.010      0.037      0.996
```

So `g` is not a low-rank vector, but it is concentrated in a finite band in this window. E72.84 shows
that the stable meaning of this concentration is physical height `|d_n|`, not fixed index `|n|`.

## 2. The lemma to prove

The first compactness statement considered here was:

```text
Dual cofactor tightness (DCTight):
For every compact s-window K in the admissible strip,

lim_{M->infty} limsup_{x->infty} sup_{s in K}
  sum_{|n|>M}|g_{x,s,n}|^2 / ||g_{x,s}||^2 = 0.                 (DCTight)
```

E72.84 corrects this to the physical-height version:

```text
lim_{H->infty} limsup_{x->infty} sup_{s in K}
  sum_{|d_n|>H}|g_{x,s,n}|^2 / ||g_{x,s}||^2 = 0.              (PDCT)
```

This is not RH in disguise: it is a resolvent/tightness statement for the shorted even cofactor vector.
It depends on the pole-relative compressed complement and on the Cauchy decay of `r_s^even`.

## 3. Why it matters

If `(DCTight)` holds, then root transport reduces to finite frequency:

```text
C_{g,f}(tau)
 = C_{Pi_Mg,f}(tau) + small_M(x,tau,s),
```

for `f=k_x,1`. Therefore E72.81 becomes a finite-mode transport identity:

```text
i C_{Pi_Mg,k}(tau_j)
-(exp(i tau_jL)-1)L^(-1)C_{Pi_Mg,1}(tau_j)M_k(tau_j)
 -> 0,
```

followed by `M->infty`.

This is the first place after E72.81 where the infinite profile of the shorted inverse is replaced by
a compact finite object without assuming vector convergence `k_x -> xi_x`.

## 4. Proof route for DCTight

Since:

```text
C_E y_{x,s}=B_x^*r_s^even,
```

it is enough to prove a tail coercivity estimate for `C_E`:

```text
||Pi_{>M}B_xy|| <= eps_M ||B_xy|| + A_M ||B_x^*r_s^even||_{tail},
eps_M -> 0.
```

The right-hand source has Cauchy decay:

```text
r_s^even(n)=s/(s^2-d_n^2)=O(d_n^-2).
```

So the missing estimate is purely operator-theoretic:

```text
the inverse of the pole-relative even complement does not move fixed-strip Cauchy data
to arbitrarily high Fourier modes.
```

This is weaker than the global strong-resolvent estimates that failed earlier.

## 5. Status

```text
observed: dual cofactor vectors are band-tight in the finite harness;
corrected: the invariant target is physical-height tightness `(PDCT)` from E72.84;
then: reduce root transport to finite-mode transport.
```
