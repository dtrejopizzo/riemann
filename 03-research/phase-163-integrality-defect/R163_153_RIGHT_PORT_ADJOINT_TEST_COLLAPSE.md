# R163_153 — The right port's adjoint test is exactly Tate at every cutoff

## Verdict

The concrete candidate `H_{M,N,T}F=Π_TP_T(S_N^ren)^*g_{M,N}` from `R161_022 (5.1)` was audited under the hypothesis defining a **right port**: `supp g_{M,N}⊂[T,∞)`. The test not only lacks a new sign law (`R161_023`): it is **identically zero for every `N≥1`**. The claim refers to the finite operator `S_N^ren`; it does not automatically identify a meromorphic limiting adjoint outside its domain.

## Support and polarity lemma (proved)

Let `g∈L²(ℝ)` with `supp g⊂[T,∞)`, `P_T=1_{(-T,T)}`, and `Π_T` the orthogonal projection onto the primitive subspace, orthogonal to `e^{±t/2}` on `(-T,T)`. For every integer `N≥1`, with `S_N^ren=S_N−C_N(D)` as in `R161_003`, for almost every `−T<t<T`:

```
P_T(S_N)^*g(t)=0,                                             (1)
P_T(C_N(D))^*g(t)=e^(t/2)∫_T^∞ e^(−u/2)g(u)du,                 (2)
P_T(S_N^ren)^*g(t)=−e^(t/2)∫_T^∞e^(−u/2)g(u)du.                (3)
```

Consequently,

```
Π_TP_T(S_N^ren)^*g=0.                                        (4)
```

*Proof.* `S_N^*=Σ_{1≤n≤N}n^(−1/2)τ_{−log n}`. If `t<T`, then `t−log n<T`, so `g(t−log n)=0`: this gives (1). By definition,

```
(C_N(D))^*g(t)=∫_0^N x^(−1/2)g(t−log x)dx.
```

With `u=t−log x`, the integrand becomes `e^(t/2)e^(−u/2)g(u)du`. Since `N≥1` and `t<T`, the lower limit `u=t−log N` lies to the left of `T`; by `g`'s support, the integral runs exactly from `T` to `∞`. The moment converges by Cauchy–Schwarz, since `e^(−u/2)∈L²([T,∞))`. This proves (2)–(3). Its restriction to `(-T,T)` belongs to the Tate line `span{e^(t/2)}`, annihilated by `Π_T`, giving (4). ∎

## Consequence for the `L161.5` attempt

If the finite ports `g_{M,N}` of `R161_022` are truly right-supported, the proposed primitive conjugate test `H_{M,N,T}F` is zero **before** invoking radicality. So the equality `a_T(F,H_{M,N,T}F)=0` cannot transport the scattering square `X_T(F)`; it is not a non-trivial test awaiting estimation. If a finite precursor `g_{M,N}` does not have exact right support, any primitive contribution comes exclusively from that prehistory, which must be explicitly exhibited and controlled. Tacitly switching between these two port types would invalidate the inference.

This is consistent with `R161_023`: its tautological recombination had already ruled out closure via a direct pullback. The present lemma pins down the cause at the level of support and the polar subtraction. It holds for any unit-weight comb and any Euler system, including the falsifier `Z_K`; it uses neither `Λ*1=log`, first contact, nor the functional equation. **It does not close D.** The next candidate must insert the Poisson/Fourier orientation *before* the adjunction, or use a finite prehistory demonstrably non-Tate; repeating (4) cannot produce the gate.
