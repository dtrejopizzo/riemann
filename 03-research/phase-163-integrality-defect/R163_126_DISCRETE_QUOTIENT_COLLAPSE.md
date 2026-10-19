# R163_126 — Collapse of any discrete Dirichlet quotient with a first gap

**Status:** conditional reduction proved for ζ's effective exchange. Extends `R163_113`: it is not even necessary for the quotient's exponents to be `log n` or for its coefficients to be positive. **Does not close Row D**, because it has not been proved that the effective quotient has a discrete Dirichlet expansion.

## Theorem

Let `E` be the canonical product of **all** of ζ's effective exterior quartets (`R163_001`) and `F=ζ/E`. Suppose that for some `a>0`, `σ₀<∞`, with absolute convergence for `Re s>σ₀`,

```
F(s)=1+Σ_{j≥1} A_j exp(−λ_j s),     λ_j≥a,
Σ_j |A_j| exp(−σλ_j)<∞   (σ>σ₀).                 (1)
```

The `A_j` are not required to be real, integer or non-negative; nor is `λ_j=log n` required, nor that (1) comes from Beurling primes. Then `E≡1`: ζ has no exterior quartets.

The **first-gap** requirement `a>0` is essential. A series or measure with exponents accumulating at zero does not satisfy (1).

## Proof

1. Take `σ` large enough that the absolute norm of `F−1` in (1) is less than `1/2`. The convergent expansion of `log F` in powers of `F−1` is a Laplace series of a complex discrete measure supported on `[a,∞)`: each convolution product has support on `[ka,∞)`. The classical series `log ζ=Σ_{p,k≥1}p^{-ks}/k` converges absolutely for `Re s>1` and its measure is supported on `[log 2,∞)`. Hence

   ```
   log E(s)^{-1}=log F(s)−log ζ(s)                  (2)
   ```

   is the Laplace transform of a discrete measure of finite exponential variation, supported on `[c,∞)`, `c=min(a,log 2)>0`. The real-normalized branch on the right half-plane is chosen; `E(σ)→1` by `R163_118`.

2. `R163_001`'s current `q_E` is a distribution of exponential type, not just a local distribution. Indeed, on a unit interval around `U≥0`, the factor-by-factor formula

   ```
   q_j(u)=4e^{u/2}(cosh(δ_j u)−1)cos(γ_j u)/u
   ```

   and two integrations by parts give, for `φ∈C_c^∞((U,U+1))`, the explicit bound

   ```
   |⟨q_j,φ⟩| ≤ γ_j^{-2}||(a_j φ)''||_{L¹}
              ≤ C δ_j² γ_j^{-2}(1+U)^2 e^{U+1}||φ||_{C²},
   a_j(u)=4e^{u/2}(cosh(δ_j u)−1)/u.              (3a)
   ```

   The function `a_j` extends smoothly through `u=0` with value zero; a test touching `0` only adds the boundary term `a_j'(0)φ(0)/γ_j²`, of equal size. Since `Σ_jδ_j²/γ_j²<∞`, the sum defines a distribution of growth at most `e^U` times a polynomial. For `Re s>1`, its Laplace transform exists in the distributional sense; cutting at `u≤R` and the preceding bound allow passing to the limit. Frullani gives, per factor,

   ```
   L(q_j)(s)=log E_j(s)^{-1}.
   ```

   The sum on the right converges normally for `Re s>1` on compacts avoiding the zeros and poles (there are none there). So

   ```
   L(q_E)(s)=log E(s)^{-1}                         (3)
   ```

   on a right half-plane. This global verification is specific to the effective sum and does not follow merely from its convergence in `D'(0,∞)`.

3. By uniqueness of the Laplace transform for exponential-type distributions supported on `[0,∞)`, (2) and (3) identify `q_E` with the discrete measure in (2). In particular `q_E|(0,c)=0`. The no-gap theorem `R163_116` implies there is no exterior quartet. Hence `E=1`. □

## Scope and audit

- The deduction combines ζ's Euler product (whose current starts at `log2`) with the **hypothesis** of a first discrete gap for the quotient. The difference of the two currents inherits the gap. Positivity of `F` is not postulated. **It still does not use ζ's exact integrality `N_ζ=⌊x⌋` in a step that produces that hypothesis**; so it is a reduction, not the sought arithmetic mechanism.
- It is a strictly broader reduction than `R163_113`–`R163_114`'s **ordinary** Euler support: it allows arbitrary exponents and complex coefficients. It does not replace the arithmetic gate: (1) does not follow from `N_ζ(x)=⌊x⌋`, from `Λ*1=log`, from `(PC-ren)` or from Poisson–Tate.
- A candidate construction claiming `F=ζ/E` is a **discrete** Beurling zeta would already have finished the proof as soon as it justifies convergence on some right half-plane. The real difficulty is precisely producing (1). Quotients with a continuous current starting immediately after `u=0` evade the theorem and are what remains to be controlled.
- Epstein/Davenport–Heilbronn lack ζ's ordinary Euler product used in step (2). `R163_103`'s discrete systems keep infinitely many exterior zeros, but their spectral mass at fixed horizontal distance is of order `T log T`, not `o(T)`; so they do not satisfy the no-gap step `R163_116`. Beurling–DMV likewise does not automatically get that effective lemma. The reduction does not exclude those falsifiers nor authorize transferring (1) from them to ζ's case.

**Remaining gate:** prove, from exact arithmetic and `(PC-ren)`/Poisson–Tate, some property forcing (1) or directly a gap in `q_E`, without assuming a discrete representation of the quotient. This still has RH strength for the effective exchange.
