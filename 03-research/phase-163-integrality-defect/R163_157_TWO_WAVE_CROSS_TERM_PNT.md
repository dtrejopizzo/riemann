# R163_157 — Cross term of the two waves: the leading order is universal

**Status:** limit of the moving cross product, for smooth compactly supported sources. It is a direct test of the possible orientation source in `R163_154`; the leading order **does not** distinguish ζ from the falsifier `Z_K` and does not close D.

Let `F∈C_c^∞(ℝ)` be primitive, `h=Fcal F`, `L=log N`, `M_N=⌊αN⌋` with `α>0` fixed, and

```
 A_M=M_Γ−Σ_{n≤M} Λ(n)n^(−1/2)(τ_{log n}+τ_{−log n}).
```

The real cross product of `R163_154`'s two leading waves is

```
 C_{N,α}(F):=Re⟨Fcal A_{M_N}F, τ_{−2L}J A_{M_N}F⟩.       (1)
```

Define two boundary convolutions (Bochner integrals in `L²`)

```
 U_αh(u)=∫_0^α x^(−1/2)h(u−log x)dx,
 V_αJF(u)=∫_0^α y^(−1/2)JF(u+log y)dy.               (2)
```

Then

```
 lim_{N→∞} C_{N,α}(F)/N
      =Re⟨U_αh,V_αJF⟩_{L²(du)}.                     (3)
```

The right side contains only the Poisson–Tate transform `Fcal`, the source `F`, and the continuous density `dx/√x`; it **does not** contain the exact integer lattice nor the individual jumps `Λ(p^j)`.

With the convention `\hat f(ξ)=∫f(u)e^(−iξu)du` and `Fcal=U_∞(D)J`, the same limit has the exact spectral formula

```
 Re⟨U_αh,V_αJF⟩
   =(1/2π)∫ |F̂(−ξ)|² Re{ α^(1−2iξ)u_∞(ξ)/(1/2−iξ)² }dξ. (3a)
```

Indeed, `U_α`'s and `V_α`'s multipliers are respectively `α^(1/2−iξ)/(1/2−iξ)` and `α^(1/2+iξ)/(1/2+iξ)`; the product of the first with the conjugate of the second gives (3a)'s factor. The formula shows that the macroscopic crossing is a **phase multiplier**, not a positive energy: the phase of the Gamma quotient `u_∞(ξ)` has derivative of size `log|ξ|` by Stirling, while the other factors only add a linear phase in `ξ` and a bounded phase. By continuity, the symbol's real part takes both signs at arbitrarily large heights. This asserts indefiniteness in `L²` with no restriction, **not** a sign for first-contact radical vectors.

## Proof

The rescaled prime measure

```
 μ_N=(1/√N)Σ_{n≤αN}Λ(n)n^(−1/2)δ_{n/N}
```

converges weakly on `(0,α]` to `x^(−1/2)dx` by `ψ(x)∼x`. Chebyshev's bound, via partial summation, gives uniformly

```
 μ_N((0,δ])≤C√δ,                                (4)
```

so the mass does not escape through `x=0`.

Write product (1) as a sum of the Gamma–Gamma, Gamma–prime, and prime–prime parts. The first two are `o(N)` by Cauchy–Schwarz: `||M_ΓF||₂<∞` and each prime sum's norm is `O_F(√N)`. In the prime–prime part, set `t=L+u`. Of the four sign combinations of the translations, only one can keep overlap when `m,n` are proportional to `N`:

```
 (Fcal τ_{log m}F)(L+u)=h(u−log(m/N)),
 (τ_{−2L}Jτ_{−log n}F)(L+u)=JF(u+log(n/N)).      (5)
```

Here `Fcal τ_a=τ_{−a}Fcal` and `Jτ_a=τ_{−a}J` were used. The other three combinations are separated by distances growing like `log N`: `JF` is compactly supported and `h` decays rapidly to the right. To justify discarding them without false uniformity for small `n`, first cut off `m,n≥δN`; the complementary contribution, divided by `N`, is bounded by `O_F(√δ)` via (4) and Cauchy–Schwarz/Minkowski. Then let `N→∞` and finally `δ↓0`.

Combination (5), divided by `N`, is exactly

```
 Re⟨∫ h(u−log x)dμ_N(x),
     ∫ JF(u+log y)dμ_N(y)⟩.
```

`L²`-continuity of translations, `μ_N`'s weak convergence on `[δ,α]`, and (4) make the two Bochner integrals converge to (2). This proves (3). ∎

## Adversarial check

Replace `Λ` with `R163_147`'s weight `a_K=Λ+K(log2)1_{n=2^j}`, with `K` fixed. The extra mass of the rescaled measure satisfies

```
 (1/√N)Σ_{2^j≤αN}K(log2)2^(−j/2)=O_K(N^(−1/2)),
```

so (3) is **identical** for ζ and `Z_K` with the same source `F`. In particular, it remains valid even if `F` is the smooth test driving `Z_K`'s form to negative values; it does not exclude its first contact. Any law aiming to close D from this term must use a **subprincipal remainder** after subtracting (3), and prove there a signed identity failing for `a_K`. The `N`-order of the crossing cannot be that law.
