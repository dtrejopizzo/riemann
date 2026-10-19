# R163_155 — Local limit of the left wave on the moving Weil graph

## Theorem

Let `F∈C_c^∞((-T,T))` with both Tate moments zero. Define, **without postulating a global infinite operator**, the local limit

```
H_F^left(t):=lim_{M→∞}(Fcal A_MF)(t),
A_M=M_Γ−L_M−L_M^*.                                      (1)
```

The limit exists in `C^k([-R,R])` for every finite `k,R`. More precisely, for every `k,R`,

```
||(Fcal A_MF)−H_F^left||_{C^k([-R,R])}=O_{F,k,R}(M^(−2)). (2)
```

If `M_N→∞` and `M_N≤cN` for fixed `c`, `R163_154`'s rescaled left wave has the strong local limit

```
P_R τ_{−log N}√N E_N^ren A_{M_N}F
   → (1/2)P_R H_F^left                       in L².     (3)
```

This is a local construction of the additive channel on the **moving prime vector**, not the product scattering equality. `R163_154 (8)`'s right wave collapses to Tate at a smooth contact; (3) identifies the channel that can preserve primitive information.

For each finite `M`, `A_M` commutes exactly with `Fcal`: both `m(D)` and `L_M+L_M^*` have even multipliers, and `Fcal=U_∞(D)J` reflects the Fourier variable. So one may also write `H_F^left=lim_M A_M(Fcal F)` **only in (1)'s local topology**. The global commutation is not preserved upon compressing the window; its exterior defect is `R161_059`'s cross block, not a vanishing law.

## Proof of local convergence

Write `h=Fcal F`. The relation `F(t)=e^(t/2)f(e^t)` with `f` even, smooth and compactly supported lets us write `h(t)=e^(t/2)f̂(e^t)` with Tate's fixed normalization. Since `f̂` is even and analytic near zero, and `∫e^(t/2)F(t)dt=0` is equivalent to `f̂(0)=0`, for every `k`,

```
|h^(k)(t)|≤C_{F,k}e^(5t/2)       (t→−∞),
|h^(k)(t)|≤C_{F,k,A}e^(−At)      (t→+∞, every A>0).     (4)
```

The logarithmic involution satisfies `Fcal τ_{±log n}=τ_{∓log n}Fcal`. So, on a fixed window, the tail of `Fcal(L_M+L_M^*)F` for `n>M` is bounded by

```
C_{F,k,R} Σ_{n>M}Λ(n)[n^(−3)+n^(−A−1/2)].             (5)
```

The first sum is `O(M^(−2))` by `ψ(x)=O(x)` and partial summation; the second is `O_A(M^(1/2−A))`, which for `A>5/2` is smaller. The term `Fcal M_ΓF` does not depend on `M`. This proves (1)–(2), also after differentiating `k` times. It is not claimed that `A_MF` converges globally in `L²`, nor that `H_F^left` is `Fcal` of an untyped global limit.

## Proof of boundary tracking

Applying `τ_{−log N}` to `R163_154 (6)` gives

```
τ_{−log N}√N E_N^ren A_{M_N}F
 = (1/2)Fcal A_{M_N}F
   −(1/2)τ_{−2log N}J A_{M_N}F+o_{L²}(1).            (6)
```

On a fixed interval, the second translation tends to zero. For the prime terms this is even exact when `N` is large: `F` is compactly supported and `log n≤log(cN)`, while the total displacement is `2log N`. The Gamma term `M_ΓF` is a fixed `L²` vector, so its translation vanishes locally. The first part converges by (2). This proves (3). ∎

## Arithmetic audit and gate

The same proof holds with `Z_K`'s weight `a_K`: only the local series defining `H_F^left` changes. So the existence of limit (3) is not a law ruling out falsifiers. For ζ, the expansion of `h(t−log n)`'s left tail has coefficients `Σ_nΛ(n)n^(−2m−1)=−ζ'(2m+1)/ζ(2m+1)`, connecting this channel to phase 161's Gamma-moment lattice, but those coefficients impose no inequality on a contact state.

The **unproved gate** is a signed relation identifying `H_F^left`'s primitive compression — together with the polar/Tate corrections and the full product port — with `R161_021`'s scattering square `X_T(F)`, or with a term annihilating it. Radicality alone does not make such an identification (`R161_023`). This note resolves the channel's local convergence, not its sign nor Row D.
