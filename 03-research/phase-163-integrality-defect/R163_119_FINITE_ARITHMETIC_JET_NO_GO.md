# R163_119 — Every finite arithmetic jet can be exact and coexist with off-line zeros

**Status:** unconditional theorem from [Broucke, Theorem 6.3](https://journals.sns.it/index.php/annaliscienze/article/download/6843/2289/4170), plus an improvement **conditional on the review of `R163_103`**. A NO-GO for vanishing laws that use only a finite portion of the integer/Euler lattice. Does not close Row D.

## Finite-splice theorem

Let `B` be a **discrete** Beurling system with real primes `q>1`, integer multiplicities, `N_B(x)=ρx+O(x^θ)` for some `0<θ<1`, and a zero `β+iγ` of `ζ_B` with `β>max(θ,1/2)`. For every `X≥2` there exists a discrete system `B_X` such that:

1. Its prime and generalized-integer multisets **coincide exactly** with the ordinary ones on `[1,X]`; in particular `N_{B_X}(x)=⌊x⌋` for `1≤x≤X` and the weights `Λ_{B_X}(p^k)=log p` there.
2. `N_{B_X}(x)=ρ_Xx+O_X(x^θ)` with `ρ_X>0`.
3. On every region of `Re s>0` where `ζ_B` has meromorphic continuation, `ζ_{B_X}` has exactly the same zeros and poles, with multiplicities; in particular it keeps the zero `β+iγ` (which lies in the continuation region `Re s>θ` given by the counting error).

**Construction.** Remove every occurrence of generalized primes of `B` with value `q≤X`, and add one occurrence of each ordinary prime `p≤X`. Only finitely many occurrences are removed, by discreteness/local finiteness. Every remaining prime is `>X`, so no product containing them can be `≤X`. The products of the added primes give exactly the ordinary integers `≤X`, with multiplicity one. This proves 1, including the prime-power ledger.

For `Re s>1`, and by continuation wherever `ζ_B` is defined,

```
ζ_{B_X}(s)=ζ_B(s) C_X(s),
C_X(s)=∏_{q≤X}(1−q^{-s})^{m_B(q)}
           ∏_{p≤X}(1−p^{-s})^{-1}.                     (1)
```

For `Re s>0`, each factor `1−u^{-s}` is holomorphic and non-zero, and the finite product `C_X` and its inverse are holomorphic. So zeros and poles are preserved with multiplicities **wherever the base zeta is meromorphic**. The hypothesis `N_B(x)=ρx+O(x^θ)` gives meromorphic continuation at least to `Re s>θ`; the chosen zero must lie there, as happens in the instantiations below. This proves 3.

For 2, call `B^-` the system after removing the finitely many occurrences. The first product in (1) is a finite polynomial in `q^{-s}`; by finite convolution,

```
N_{B^-}(x)=ρ^-x+O_X(x^θ),
ρ^-=ρ∏_{q≤X}(1−q^{-1})^{m_B(q)}>0.                (2)
```

Adding the ordinary primes `p≤X`, let `\mathcal S_X` be the semigroup they generate, each integer counted once. Then

```
N_{B_X}(x)=Σ_{d∈\mathcal S_X,\ d≤x}N_{B^-}(x/d).
```

The sum of errors is `O_X(x^θ Σ_{d∈\mathcal S_X}d^{-θ})=O_X(x^θ)`, because there are only finitely many generators and `θ>0`. Extending the main sum from `d≤x` to all `d` costs at most

```
x Σ_{d∈\mathcal S_X,\ d>x}d^{-1}
 ≤ x^θ Σ_{d∈\mathcal S_X}d^{-θ}=O_X(x^θ).
```

So `ρ_X=ρ^-∏_{p≤X}(1−p^{-1})^{-1}>0`, proving 2. □

The requirement `θ>0` in this step is real: `Σ_{d∈\mathcal S_X}d^{-θ}` converges for `θ>0` and diverges for `θ=0`. So the splice preserves any positive error exponent, but it **does not** give a countermodel with bounded error `O(1)`; `R163_102`'s case `θ=0` remains intact.

## Instantiation and exact scope

- **Unconditional:** [Broucke, Theorem 6.3](https://journals.sns.it/index.php/annaliscienze/article/download/6843/2289/4170) builds discrete systems with `N_B(x)=Ax+O(x^θ)` and off-line zeros for every `1/2<θ<1`. Applying the splice theorem gives, for every `X`, a `B_X` with an exact ordinary jet up to `X` and those zeros. At `θ=1/2`, the source has an extra `log x` factor; it is not removed in this note.
- **If it survives the `R163_103` review:** the same splice works with its Witt-rounding systems for `1/3<θ<1/2`, preserving `O_ε(x^{θ+ε})` and the transported zeros. The splice is proved independently; the threshold improvement inherits `R163_103`'s status.
- **It is not a falsifier of a law that also uses ζ's exact functional equation:** `B_X` has no such known functional equation. The theorem says something more precise and limited: *no finite number of exact coefficients `b(n)=1`, exact Euler weights, or `Λ*1=log` identities up to a fixed cutoff distinguishes ζ by itself from discrete systems with off-line zeros*. A law closing D must use infinitely many coefficients in a genuinely global way and/or ζ's exact Poisson–Tate orientation, not a finite chamber disguised as a global identity.

## Relation to the `D_test` defect

The splice shows why `R163_001`'s arithmetic vanishing property cannot come from a finite check of the ledger. Even though `D_test` is faithful for ζ's **effective** exchange (`R163_118`), that faithfulness uses the geometry of its zeros and does not turn equality of the first `X` Euler data into the defect's vanishing. This is a design restriction, not a proof that property 2 is impossible.

In particular, as `X→∞`, `ζ_{B_X}`'s coefficients converge **coefficient by coefficient** to those of ζ, and each system keeps the chosen off-line zero. So the product topology of all finite jets does not control zero location to the left of absolute convergence. A semicontinuity of a defect under truncations of *the same effective exchange* (`R163_118`) is a different statement: it does not license passing from that arithmetic convergence of systems `B_X` to a theorem of RH or to a contradiction.
