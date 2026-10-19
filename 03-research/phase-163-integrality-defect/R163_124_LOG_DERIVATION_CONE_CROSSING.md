# R163_124 — The log multiplier crosses the cone of squares

**Status:** exact algebraic identity and circularity audit. Does not close Row D. It localizes, in a small equation, where the Euler/Poisson–Tate orientation would have to act to turn a square's positivity into a sign excluding quartets.

## 1. Factorization of the sign-changing test

Let `b=1/2`, `T_b(u)=(b−|u|)_+`. Its transform is

```
\widehat{T_b}(γ)=2(1−cos(bγ))/γ²≥0.
```

By the product theorem for positive-definite functions, `K₂=T_b²` and `K₃=T_b³` are also positive-definite. Moreover, the **pairings with `r` are positive**, despite the variable factor `B_δ`: on `0<u<b`, writing `v=b−u` and using `B≥1`, `B'≤u/6`, `B''≥0` from `R163_117`, the functions `g_k(u)=v^kB_δ(u)` (`k=2,3`) satisfy

```
g₂'(u)=−2vB+v²B'<0,      g₂''(u)=2B−4vB'+v²B''>0,
g₃'(u)=−3v²B+v³B'<0,     g₃''(u)=6vB−6v²B'+v³B''>0.
```

The inequalities are uniform for `b=1/2`, since `v,u≤1/2` and the negative terms are smaller than `1/6` of the dominant term. The representation of a convex, decreasing even function as a positive mixture of triangles (used in `R163_116`) gives `\widehat{K_kB_δ}(γ)>0` for every `γ`. Consequently `M₂,M₃>0` if quartets exist. Nevertheless, `R163_117`'s negative test is exactly

```
H_b(u)=|u|K₂(u)=bK₂(u)−K₃(u).                       (1)
```

So the multiplier `|u|` — the logarithm of the multiplicative quotient in the positive orientation — turns a positive-definite test into the **difference** of two positive-definite tests. R163_117 proves, for the effective stripped current `r`:

```
M₃−bM₂ = −⟨r,H_b⟩ = D_->0
if quartets exist,
M_k:=⟨r,K_k⟩.                                      (2)
```

The defect satisfies `0.099 log E(1/2)≤D_-≤log E(1/2)`. So requiring `M₃≤bM₂` for the **effective** current is equivalent to `E=1`, and is not a weak intermediate step. The value of (1) is not to resolve that inequality, but to pin down the single place where a new mechanism would have to reverse the sign's orientation.

## 2. The same `u` is exactly the Euler derivation

Work in the variable `u=log x` with additive convolution. For the ordinary zeta,

```
ν_N=Σ_{n≥1}δ_{log n},
ν_Π=Σ_{p,k≥1}(1/k)δ_{k log p},
ν_Ψ:=uν_Π=Σ_{n≥1}Λ(n)δ_{log n}.
```

The identity `ζ=exp_*(ν_Π)` and the Leibniz rule `u(α*β)=(uα)*β+α*(uβ)` give exactly

```
uν_N=ν_Ψ*ν_N,                                      (3)
```

which is `Λ*1=log` coefficient by coefficient. The coincidence between the multiplier `u` in (1) and the Euler derivation in (3) is literal, not metaphorical.

For the hypothetical quotient `Z₀=ζ/E`, the prime current would be `ν_Π+q_E` and the integer current `ν_N*exp_*(q_E)`, where the exponential requires the topology/convergence not yet built for the infinite exchange. In finite truncations, the derived identity would be

```
uν_{N₀}=(ν_Ψ+u q_E)*ν_{N₀}.                         (4)
```

Formula (4) is a **signed equality**. Neither (3) nor the positivity of `ν_N` says that `u q_E` or `ν_{N₀}` are positive; `R163_117` proves the first claim is false if quartets exist. So applying the Euler derivation and then squaring does not deliver `M₃≤bM₂`: it either returns to an equivalence or loses the orientation, exactly as `R162_903` and paper 48's wall F2 warn.

## 3. Unresolved construction target

A closure via this route would have to produce, from `(PC-ren)` with its polar/Tate terms and the Poisson–Fourier orientation, a **signed** identity comparing the two positive-definite channels `K₃` and `bK₂`, whose residual term is computed with the exact derivation (3). That identity must fail for finite modifications of `Λ`, for Epstein/DH without Euler, and for Beurling with a non-integer lattice. **It has not been built.** The final inequality on `M₃−bM₂` is RH-equivalent and must not be assumed as a premise.
