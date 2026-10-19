# R163_156 — Boundary wave over primitive L² sources: exact scope

**Status:** distributional extension of `R163_154`–`155` to the domain of possible first-contact vectors. It is **not** a sign identity nor a closure of D.

Let `F∈L²(ℝ)` with support in `[-T,T]` (values up to the endpoints are allowed, in the essential-support sense) and Tate moments

```
 ∫e^(t/2)F(t)dt=∫e^(−t/2)F(t)dt=0.
```

Set `A_M=M_Γ−L_M−L_M*` and `E_N^ren=S_N^ren Fcal−J S_N^ren`, with phase 161's conventions. `M_Γ` has symbol `m(ξ)=O(log(2+|ξ|))`; so, for every `ε>0`, `A_MF∈H^(−ε)` and

```
 ||A_MF||_{H^(−ε)} ≤ C_{F,ε}(1+√M).                 (1)
```

`R163_154 (5)`'s uniform Euler–Maclaurin bound, read as a multiplier bound, gives

```
 ||√N E_N^ren G
    −(τ_{log N}Fcal G−Jτ_{log N}G)/2||_{H^(−2−ε)}
       ≤ C_ε N^(−1)||G||_{H^(−ε)}.                  (2)
```

In particular, if `M_N→∞` and `M_N≤cN`, (2)'s remainder for `G=A_{M_N}F` is `O_{F,c,ε}(N^(−1/2))`. The loss of two derivatives cannot be removed by this argument.

## Limit of the left wave

The limit

```
 H_F^left := lim_{M→∞} Fcal A_MF                       (3)
```

exists in `D'(ℝ)`, and the tail, paired with each `φ∈C_c^∞`, is `O_{F,φ}(M^(−2))`. To prove it, we use `Fcal`'s self-adjointness and translation reflection. If `h_φ=Fcal φ`, then `h_φ(t)=e^(t/2)\widehat{f_φ}(e^t)`; to the left,

```
 h_φ(t)=c_0(φ)e^(t/2)+O_φ(e^(5t/2)),
```

and to the right it decays faster than any exponential. Pairing `Fcal τ_{log n}F` with `φ`, the leading left term is

```
 c_0(φ)n^(−1/2)∫e^(t/2)F(t)dt=0.
```

The remainder, multiplied by `(L_M+L_M*)`'s coefficient `Λ(n)/√n`, is `O_{F,φ,T}(Λ(n)n^(−3))`. The opposite translation uses the right tail and is even smaller. `Σ_{n>M}Λ(n)n^(−3)=O(M^(−2))` by `ψ(x)=O(x)`. (3)'s Gamma term is a fixed distribution. The bound only uses `|t|≤T` in the pairings, not that the support be separated from `±T`; so it covers sources touching the window's edge. This proves (3) without assuming `F` or `A_MF` are smooth.

Let `L=log N`. From (2) we obtain, in `H^(−2−ε)` and then locally in distributions,

```
 τ_{−L}√N E_N^ren A_{M_N}F
  = (Fcal A_{M_N}F−τ_{−2L}J A_{M_N}F)/2+o(1).      (4)
```

The second term tends to zero in `D'`: every prime translation has support outside any fixed compact set, uniformly for `n≤cN`; the translation of the fixed distribution `JM_ΓF∈H^(−ε)` tends weakly to zero when paired with a translated test (Riemann–Lebesgue after weighted Cauchy–Schwarz in Fourier). Consequently,

```
 τ_{−log N}√N E_N^ren A_{M_N}F
        → H_F^left/2          in D'(ℝ).             (5)
```

## Adversarial test and limit of the result

The proof of (1)–(5) uses neither `Λ*1=log`, the multiplicity coincidence `b(n)=1`, nor the first-contact state. It also works for `R163_147`'s weight `a_K`, because its absolute weighted sum up to `M` is still `O_K(√M)` and its tail `Σ a_K(n)n^(−3)` converges. That model **does have first contact**. So (5), even on a real contact vector, cannot be the arithmetic implication annihilating the Gamma moments nor the scattering square. Its precise usefulness is removing the smoothness hypothesis from the boundary computation; any later use claiming a sign must introduce an additional identity that fails for `a_K` while preserving the physical compression.
