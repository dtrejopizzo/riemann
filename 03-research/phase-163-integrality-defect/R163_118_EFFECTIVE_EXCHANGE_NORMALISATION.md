# R163_118 — Real normalization and faithfulness of the test defect

**Status:** two consequences proved for ζ's effective exchange; the arithmetic vanishing law remains open. Does not close Row D.

## 1. The infinite product tends to one on the right real axis

Let `E=∏_jE_{δ_j,γ_j}` from `R163_001`, and `w=σ−1/2→+∞`. `R163_115`'s weighted bound says

```
S(T):=Σ_{0<γ_j≤T}δ_j²=o(T).                            (1)
```

For `w≥1`, the elementary factor satisfies the exact identity

```
E_{δ,γ}(1/2+w)−1
 = [2δ²(γ²−w²)+δ⁴]/(w²+γ²)².                     (2)
```

Since `0<δ<1/2`, one gets uniformly

```
|log E_{δ,γ}(1/2+w)| ≤ C δ²/(w²+γ²),              (3)
```

for instance with any sufficiently large absolute constant: (2)'s quotient has modulus at most `9/16<1` for `w≥1`, and `|log(1+x)|≤C|x|` on that interval. The factors are positive on the real axis, so the real logarithm is used.

Splitting (3)'s sum into `γ≤w` and `γ>w` gives

```
Σ_{γ≤w} δ²/(w²+γ²) ≤ S(w)/w²=o(1/w),
Σ_{γ>w} δ²/(w²+γ²) ≤ ∫_{(w,∞)} t^{-2}dS(t)=o(1/w).  (4)
```

For the last equality, integration by parts and `S(t)=o(t)` give `S(w)/w²+2∫_w^∞S(t)t^{-3}dt=o(1/w)` as an absolute bound. Consequently,

```
log E(1/2+w)=o(1/w),       E(1/2+w)=1+o(1/w).        (5)
```

This justifies the normalization that `R163_001` left pending on the **real axis**. Uniformity over a whole right half-plane, or an ordinary Dirichlet expansion, is not asserted: both would be stronger claims.

## 2. R163_001's test defect is faithful with no central term

Let `(φ_k)` be dense tests in `C_c^∞(0,∞)` and

```
D_test(E)=Σ_{k≥1}2^{-k}min(1,|⟨q_E,φ_k⟩|).
```

If `D_test(E)=0`, then `q_E=0` as a distribution on `(0,∞)`. In particular it vanishes on `(0,1/2)`. The variable-displacement no-gap theorem `R163_116` then implies there are no quartets, so `E=1`. The converse implication is immediate. Hence, **for the effective exchange**,

```
D_test(E)=0  ⇔  E=1.                                   (6)
```

There is no need to add `log E(1/2)` to the defect to obtain faithfulness, nor to justify a global Laplace transform from local distributional convergence. For increasing finite truncations of the effective product, `q_{E,J}→q_E` in `D'(0,∞)` by the sum `Σγ_j^{-2}<∞`; `D_test`'s lower semicontinuity with respect to this convergence follows by Fatou. This verifies the **detection** and **truncation-limit** properties of `R163_001`'s prototype.

## 3. What was not obtained

(6)'s faithfulness does not produce its vanishing. The O2601.1∞ proposal's arithmetic property 2 — deducing `D_test(E)=0` from the exact values `b(n)=1` and `Λ(p^k)=log p`, together with Poisson–Tate — remains unproved. Normalization (5) likewise does not imply that `ζ/E` has integer coefficients, a positive Beurling measure, or an ordinary Dirichlet series. `R163_117` shows, in fact, that its prime current cannot be positive if `E` is non-trivial.
