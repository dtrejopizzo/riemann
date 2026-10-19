# R163_154 — Two boundary waves of the renormalized Poisson defect

## Result

The defect `E_N^ren=S_N^ren Fcal−J S_N^ren` tends to zero on fixed data, as in `R161_003`. Its **first non-zero term**, however, has an exact operator form at scale `N^(−1/2)`. Writing `L=log N` and `τ_LF(t)=F(t+L)`, for `F∈S(ℝ)` we have

```
√N E_N^ren F
 = (1/2)[τ_L Fcal F−Jτ_L F]+O_{L²,F}(N^(−1)).       (1)
```

More precisely, the remainder satisfies an `H²→L²` **operator-norm bound** of `C N^(−1)`; by density, (1) holds for every `F∈H²`. The two waves in (1) escape in opposite directions. If `P_R=1_{(-R,R)}` with `R` fixed,

```
P_R τ_{−L}√N E_N^ren F → (1/2)P_R Fcal F,              (2)
P_R τ_L √N E_N^ren F →−(1/2)P_R JF                    (3)
```

strongly in `L²`. Moreover,

```
lim_{N→∞} N||E_N^ren F||²=(1/2)||F||².                (4)
```

So a **zero-order operator in a frame following the boundary** appears, even though the unscaled defect vanishes. This is a construction of the two additive channels; it is not yet the arithmetic scattering identity that would close D.

## Proof

For `s=1/2+iξ`, uniform Euler–Maclaurin on the critical line, keeping the half-step, gives

```
Z_N(s):=Σ_{n≤N}n^(−s)−N^(1−s)/(1−s)
      =ζ(s)+(1/2)N^(−s)+R_N(s),
|R_N(1/2+iξ)|≤C(1+|ξ|)² N^(−3/2).                (5)
```

A direct derivation uses the Euler–Maclaurin formula up to the second-derivative term: after the half-step, the derivative in `N` and the periodic remainder are bounded by `O((1+|s|)²N^(−Re s−1))`. The same bound holds at `1−s`. Multiplying (5) by `F`'s Fourier data and using that `Fcal` and `J` preserve the `H²` norm (their multipliers have modulus one), `E_N^ren F`'s remainder has norm `O(N^(−3/2)||F||_{H²})`.

ζ's functional equation exactly cancels the two `ζ` terms in `S_N^ren Fcal−J S_N^ren`; the two half-steps give (1). For (2), use `τ_{−L}Jτ_L=τ_{−2L}J`; for (3), use `τ_LJτ_L=J`. A translation moving away from a fixed interval converges to zero there in `L²`. Finally, `Fcal` and `J` are unitary, and the cross product of the two waves is a pairing with a translation of length `2L`, which tends weakly to zero in `L²`. Taking norms in (1) proves (4). ∎

## Moving-graph theorem for the truncated Weil operator

Let `A_M=M_Γ−L_M−L_M^*` be `R161_001`'s finite operator, with weight `Λ`, and `F∈C_c^∞(ℝ)` fixed. Chebyshev's bound `ψ(x)=Σ_{n≤x}Λ(n)=O(x)` and partial summation give

```
Σ_{n≤M}Λ(n)/√n=O(√M),
||A_MF||_{H²}≤C_F(1+√M).                                (5)
```

The Gamma summand has finite `H²` norm on `F` because its symbol grows logarithmically; translations preserve `H²`. Applying the above operator bound to the **moving vector** `A_MF` proves, uniformly if `M≤cN` for fixed `c`,

```
||√N E_N^ren A_MF
 −(1/2)[τ_{log N}Fcal A_MF−Jτ_{log N}A_MF]||_2
 ≤ C_F N^(−1)(1+√M)=O_{F,c}(N^(−1/2)).             (6)
```

The same statement holds for weights `a` with `Σ_{n≤M}|a(n)|/√n=O(√M)`, including `Z_K`. This **does** cover the moving graph of the truncated Weil operator that the fixed-data estimate did not cover. It does not claim (6)'s two leading terms converge individually: `||A_MF||` may grow, and the corrected product ports have a different topology.

## Test of the right-followed channel at a smooth contact

For `F∈C_c^∞((-T,T))` and `M_N≤cN`, (6)'s first term, followed toward the right boundary, vanishes on every fixed window:

```
P_T τ_{2log N} Fcal A_{M_N}F →0 in L².                 (7)
```

Indeed, `Fcal F(t)` and `Fcal(XF)(t)` decay faster than `e^(−Kt)` for every `K>0` as `t→+∞`: in ordinary coordinates they are Fourier transforms of smooth compactly supported functions evaluated at `e^t`. The Tate–Beckner identity `M_Γ=X+Fcal X Fcal` gives `Fcal M_ΓF=Fcal(XF)+X Fcal F`, with the same right tail. Also `Fcal τ_{±log n}F=τ_{∓log n}Fcal F`, and for `n≤cN` the arguments of `τ_{2log N}τ_{∓log n}Fcal F` in `(-T,T)` are at least `log N−O_{T,c}(1)`. The sum of coefficients is `O(√N)` by (5), absorbed by the super-exponential tail. This proves (7).

By (6) and `τ_{log N}Jτ_{log N}=J`, we get

```
P_T τ_{log N}√N E_N^ren A_{M_N}F
   =−(1/2)P_T J A_{M_N}F+o_{L²}(1).                  (8)
```

If, furthermore, `F` were a **smooth** first-contact vector and `M_N≥e^(2T)`, then `P_T A_{M_N}F=r` belongs to the two-dimensional Tate space. (8)'s limit is `−Jr/2`, and its primitive projection equals zero. So the rescaled right channel does not by itself produce the scattering square either. The left channel of (1) preserves `Fcal A_{M_N}F` and is not annihilated by this argument. The `C_c^∞` regularity of a real contact vector is not justified here; the test is conditional on it, not a closure of Gate 1.

## Scope audit and falsifiers

The formula resolves a subproblem noted in `R161_016 §3`: it exhibits a rescaling and boundary tracking turning `E_N^ren` into a non-zero map, and (6) justifies that expansion **also over `A_MF` with `M=O(N)`**. It **does not** resolve the physical scattering: (2) and (3) live in different spatial frames, and the operator exchanging the product ports or reversing the metric arrow has not been built. Control (6) likewise does not automatically extend to the ports `g_{M,N}` after multiplying by ζ or taking polar limits.

Expansion (1) only uses the integer comb and ζ's ordinary functional equation; it uses neither contact, `Λ*1=log`, nor the exact weight of a prime. So the leading operator is the same whether `A_M`'s weight is changed to `Z_K`'s or to any `a`, as long as `E_N^ren` stays ordinary. Epstein/Davenport–Heilbronn lack this same coupled Euler–Poisson operator; Beurling lacks (5)'s exact comb. The gate's proof must **couple waves (1) to `R163_152`'s Euler jumps and to Tate/exterior**, and obtain from that coupling a sign that fails for `Z_K`. That has not been proved; Row D remains open.
