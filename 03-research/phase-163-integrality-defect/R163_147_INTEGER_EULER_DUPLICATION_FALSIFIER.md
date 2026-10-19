# R163_147 — Integer-coefficient Euler falsifier and first contact

**Status:** explicit construction proved. It refutes any step using only positive Euler + integer multiplicities (without requiring `b(n)≡1` and the Poisson–Tate orientation). It does not assert RH nor close Row D.

## Theorem

There exists an integer `K≥1` such that

```
 Z_K(s)=ζ(s)(1−2^(−s))^(−K)                 (1)
```

has an Euler product with non-negative prime weights and **positive integer** Dirichlet coefficients, while its compressed primitive form with the same Gamma factor as ζ has a non-zero first contact at some window

```
 ½log2<T_*^K<½log3.                         (2)
```

The system does not satisfy ζ's functional equation: that is exactly the extra hypothesis a closure of D must use.

## Integer coefficients and port defect

(1)'s extra factor amounts to adding `K` copies of the prime 2. Its log-derivative weight is

```
 a_K(n)=Λ(n)+K(log2)·1_{n=2^r, r≥1}.      (3)
```

If `v_2(n)=j`, the generalized integer coefficient is

```
 b_K(n)=Σ_{r=0}^j binom(K+r−1,r)
       =binom(K+j,j)∈ℕ_{≥1}.                  (4)
```

It is not `1` if `2|n`. `Z_K`'s residue at `s=1` is `ρ_K=2^K`, so `R163_143`'s ports have, at each Gamma point, the exact discrepancy

```
 Res_{s=−2m}(B_K^Eul−B_K^lat)
  =(2^K−1)K_m(F)²/Z_K(2m+1).               (5)
```

It is positive when `K_m(F)≠0`; at a non-zero contact vector this occurs for some `m` by Gamma completeness.

## First contact without numerology

Let `ℓ=log2` and fix `T₀` strictly between `ℓ/2` and `(log3)/2`. Choose a non-zero smooth even function `φ`, supported on `(-δ,δ)`, with `δ>0` small enough that the following three supports are disjoint and lie within `I_{T₀}`. Define

```
 F(t)=φ(t−ℓ/2)+φ(t+ℓ/2)
      −2cosh(ℓ/4)φ(t).                         (6)
```

The function is even. By translation and parity,

```
 ∫F(t)e^{t/2}dt=∫F(t)e^{−t/2}dt=0,
 c_F(ℓ)=∫F(t)F(t+ℓ)dt=||φ||²₂>0.           (7)
```

The second equality uses that, if `δ` is small enough, the only overlap at distance `ℓ` is between the two exterior copies of `φ`; the central bump does not contribute. So `F` is an admissible primitive test.

Since `2T₀<log3`, the **only** visible prime contact on that window is `n=2`. (1)'s primitive form evaluated at `F` is

```
 ⟨F,H_{T₀,K}F⟩
   =⟨F,M F⟩−2(K+1)(log2)/√2 ·||φ||²₂.    (8)
```

The first term is finite and independent of `K`; so (8) is negative for all sufficiently large integers `K`. For `T≤ℓ/2`, there is no contact from any prime, so the form coincides with ζ's and is strictly positive on those small windows (unconditional range already proved in the corpus). Continuity of the minimal primitive eigenvalue in `T`, proved in `R162_001` and valid for these finite weights on each window, guarantees a first `T_*^K∈(ℓ/2,T₀)` with a non-trivial kernel. This proves (2). □

## Adversarial test for any closure

This model keeps **integer support, positive integer multiplicities, a genuine Euler product, weights `a_K≥0`, and ζ's Gamma part**, yet has a first contact. So none of those data separately — nor their conjunction without a functional equation and without `b(n)≡1` — can force the Gamma vanishing on the kernel. In particular, `R163_144`'s tilt positivity and `b_K`'s integrality do not orient the compression.

The two-port proposal passes this test at the object level: (5) detects `b_K≠1` exactly at the Gamma poles. Turning it into a closure for ζ still needs a physical Poisson–Tate identity that uses both **the reflection valid for ζ** and **the coincidence `b_Λ≡1`**, and that is not valid for (1). That was not built here.
