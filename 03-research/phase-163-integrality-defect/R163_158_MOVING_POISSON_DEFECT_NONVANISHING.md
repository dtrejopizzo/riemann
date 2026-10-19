# R163_158 — The Poisson defect over the moving prime graph does not vanish

**Status:** theorem for smooth compactly supported sources. It rules out a concrete limiting hypothesis; it does **not** prove Gate 1's sign nor close D.

Let `F∈C_c^∞(ℝ)`, `F≠0`, `M_N=⌊αN⌋`, `α>0` fixed, and use `A_M` and `E_N^ren` from `R163_154`. With `R163_157`'s `U_α`, set

```
 B_α(F):=||U_αF||²
        =α/(2π)∫ |F̂(ξ)|²/(1/4+ξ²)dξ >0,            (1)
 C_α(F):=Re⟨U_α(Fcal F),V_α(JF)⟩.                  (2)
```

Then the limit of the **unscaled norm** of the defect over the moving prime vector exists:

```
 lim_{N→∞} ||E_N^ren A_{M_N}F||²
       =B_α(F)−C_α(F)/2,                           (3)
 (1/2)B_α(F) ≤ B_α(F)−C_α(F)/2 ≤ (3/2)B_α(F). (4)
```

In particular, the limit is strictly positive for `F≠0`. (1)'s first equality identifies the universal level with the Green energy of symbol `(1/4+ξ²)^{-1}`, already present in phase 114, multiplied by `α`.

## Proof

`R163_157`'s rescaled prime measure `μ_N` converges to `x^(−1/2)dx` and has uniformly small mass on `(0,δ]`. Applying the same `L²`-translation argument to the two orientations of

```
 L_M+L_M*=Σ_{n≤M}Λ(n)n^(−1/2)(τ_{log n}+τ_{−log n}),
```

gives

```
 lim_{N→∞} ||A_{M_N}F||²/N
    =||U_αF||²+||V_αF||²=2B_α(F).                (5)
```

Indeed, following the centers `±log N`, the two prime sums normalized by `√N` converge strongly to `U_αF` and `V_αF`; their cross products tend to zero by separation of the centers, after discarding the `O(√δ)` mass of primes `n<δN`. The term `M_ΓF` has fixed norm and vanishes after dividing by `√N`. `U_αF`'s and `V_αF`'s norms coincide because their multipliers have the same modulus `√α/(1/4+ξ²)^(1/2)`. This proves (5) and (1).

`R163_154 (6)`'s expansion gives

```
 √N E_N^ren A_{M_N}F
   =[τ_{log N}Fcal A_{M_N}F−Jτ_{log N}A_{M_N}F]/2+r_N,
 ||r_N||₂=O_F(N^(−1/2)).                          (6)
```

The two leading summands have norm `||A_{M_N}F||=O_F(√N)` and their cross product is `R163_157`'s `C_{N,α}(F)`. Squaring (6) and dividing by `N`, the remainder contributes `o(1)`; by (5) and `R163_157 (3)`, (3) follows.

Finally, `Fcal=U_∞(D)J` is unitary and its multiplier `u_∞` has modulus one. `U_α`'s and `V_α`'s multipliers have the same modulus, even in `ξ`; by Plancherel,

```
 ||U_α(Fcal F)||₂=||V_α(JF)||₂=||U_αF||₂.
```

Cauchy–Schwarz implies `|C_α(F)|≤B_α(F)`, giving (4). ∎

## Scope against the gate and falsifiers

The theorem holds equally for `R163_147`'s weight `a_K`: the extra measure from powers of 2, divided by `√N`, vanishes, and `R163_154`'s moving-graph bound keeps the same order. That model has a first contact. So neither (3)'s positivity nor the Green identity in (1) distinguish ζ from `Z_K`.

The precise conclusion is negative: `E_N^ren A_{αN}F` **cannot** be sent to zero in `L²` to close `(PC-ren)`; the moving graph keeps two waves with a fixed-size energy. This does not rule out cancellations with the product, Tate and exterior ports in a *different* identity. Nor does (3) extend to merely-`L²` contact vectors via `R163_156`, which gives distributional convergence with derivative loss, not norm control.
