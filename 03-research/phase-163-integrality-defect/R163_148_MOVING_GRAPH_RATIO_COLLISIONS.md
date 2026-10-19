# R163_148 — Ratio collisions in the moving limit of `(PC-ren)`

## Scope

This note reopens `R161_075`'s domain problem at a strictly finite level. It does not build the physical limit nor prove the Weil sign. It identifies exactly the part that a passage to the limit cannot discard merely because the truncated prime vector converges locally.

We use the conventions of `R161_001` and `R161_003`: `τ_vF(t)=F(t+v)`, `S_N=Σ_{k≤N}k^{-1/2}τ_{log k}`, `L_M^*=Σ_{n≤M}Λ(n)n^{-1/2}τ_{-log n}` and `S_N^ren=S_N-C_N(D)`, with `C_N(D)=∫_0^N x^{-1/2}τ_{log x}dx`.

## Theorem 1 — Exact ratio kernel

For all finite `M,N`, `S_N^ren L_M^*` is convolution by the signed measure

```
μ_{M,N}=Σ_{k≤N,n≤M} Λ(n)/√(kn) δ_{log(k/n)}
       − e^{v/2} Σ_{n≤M: n e^v≤N} Λ(n) dv.                 (1)
```

Its atomic mass at `v=0` is exactly

```
μ_{M,N}({0})=Σ_{n≤min(M,N)} Λ(n)/n.                      (2)
```

(1)'s polar counterterm is absolutely continuous and, hence, does not cancel that atom **as a measure at a finite cutoff**. Nor does (2) license separating the atom after the limit: the other ratios `k/n` accumulate at zero and may compensate it when tested against smooth functions.

*Proof.* The product of the two translation sums gives (1)'s first term. In the second, for each `n`, substituting `x=n e^v` into `Λ(n)n^{-1/2}x^{-1/2}dx` produces `Λ(n)e^{v/2}dv` and the condition `ne^v≤N`. The only way `log(k/n)=0` is `k=n`; its coefficient is `Λ(n)/n`. The integral part has no atoms. ∎

The formula holds literally with any prime weight `a(n)` in place of `Λ(n)`, with `a(n)` replacing `Λ(n)` in both terms. So the isolated diagonal atom **does not** by itself distinguish ζ from `R163_147`'s `κ` models; the identity `Λ*1=log` must enter an additional comparison.

## Theorem 2 — Local stabilization and loss of uniformity

If `F` is supported on `[-T,T]` and `R>0`, the restrictions of `L_MF` and `L_M^*F` to `[-R,R]` stabilize for `M>e^{R+T}`. The same holds for `A_MF=(M_Γ-L_M-L_M^*)F`, because the Gamma summand does not depend on `M`.

However, this local stabilization does **not** allow replacing `A_MF` with a local limit before applying `S_N^ren`: for `k=n` arbitrarily large, the product `S_N L_M^*F` contains the term `(Λ(n)/n)F(t)` in the original window. This is collision (2), returned from the `log n` endpoints via the integer comb.

*Proof.* For `|t|≤R`, `F(t±log n)` vanishes if `log n>R+T`; this gives the first claim. In the product, `τ_{log n}τ_{-log n}=I`, giving the second. ∎

## Corollary — The dilation commutator loses the diagonal

Since `[X,τ_v]=-vτ_v`, the discrete part of `[X,S_NL_M^*]` has coefficient `−log(k/n)Λ(n)/√(kn)`. So the commutator annihilates **every** collision `k=n`. The diagonal contribution cannot be recovered solely from a limit of commutators or from a derivative in the scale variable. One must also keep the zero-order term and the polar subtraction, with their Tate/exterior crossings, before passing to the limit.

This does not claim the diagonal has a final sign: the off-diagonal collisions, the continuous counterterm and the other pieces of `(PC-ren)` may compensate it. The result only fixes a faithfulness condition for any candidate for gate 1.

## Operational consequence for the closure

The limit missing in `R161_021` must simultaneously control the ratio measure (1) in a distributional topology strong enough for the physical compression, and the divisor identity `Λ*1=log` in the product channel. Taking the local limit `A_MF` first, or keeping only the commutator `[X,·]`, discards finite data that reappear after Poisson. Nor does the isolated diagonal mass suffice, since it is common to Euler falsifiers and does not control the sign. The step of pairing this collision ledger with the Gamma port and proving its vanishing at first contact remains **open**; Row D is not closed.
