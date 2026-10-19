# R163_122 — Audit: normality of the explicit completion is equivalent to RH

**Status:** equivalence proved under `R163_121`'s construction. Does not close Row D. It bounds the new object's value: building it is easy; controlling its family uniformly to the right of `1/2` is exactly of RH strength.

## 1. Exact Euler comparison

For `Re s>1`, `R163_121`'s definitions give

```
log Z_X(s)−log ζ(s)
 = ∫_X^∞ t^{-s}dt/log t
   −Σ_{p>X}Σ_{k≥1}p^{-ks}/k.                         (1)
```

The `k≥2` term converges absolutely and tends to zero uniformly on compacts of `Re s>1/2` as `X` grows. The `k=1` term is the difference between the continuous tail `Li` and the prime tail; its continuation toward `Re s>1/2` requires controlling the discrepancy `π−Li`. By integration by parts, if one knew the RH-strength bound

```
π(t)−Li(t)=O_ε(t^{1/2+ε}) for every ε>0,           (2)
```

the `k=1` difference in (1) would extend holomorphically to `Re s>1/2` and tend to zero uniformly on compacts there. So RH implies `Z_X→ζ` locally uniformly on `Re s>1/2` away from the pole at `s=1`.

The converse direction does not require (2). Each `Z_X` is holomorphic and **non-zero** on `Ω={Re s>1/2}\{1}` by `R163_121`, and `Z_X→ζ` on the open set `Re s>1` by absolute convergence of the tails in (1). If the family `{Z_X}` were locally bounded on `Ω`, Vitali's theorem would make it converge locally uniformly to ζ on all of `Ω`. Hurwitz would then say ζ has no zeros on `Ω`; by its functional equation, RH would follow.

This gives the precise equivalence

```
RH  ⇔  {Z_X}_{X≥2} locally bounded on Re s>1/2, s≠1. (3)
```

In the `RH⇒` direction, the classical prime estimate that RH implies is used; in the other, Vitali and Hurwitz. Boundedness is understood as `X→∞`; values of `X` in a compact interval form a locally bounded family by the explicit formula.

## 2. Consequence for the `(UC_θ)` gate

`R163_121`'s uniform integer bound `(UC_θ)` implies the local boundedness of (3) via `R163_120 (5)`, so it is at least as strong as RH. The converse `RH⇒(UC_θ)` has **not** been proved for this family; `(UC_θ)` should not be called an equivalence without that proof.

In the first band `X<x<2X`, `R163_121 (12)` already reduces `(UC_θ)` to controlling increments of `π−Li` at square-root scale. Equivalence (3) shows the same wall on the holomorphic side. Presenting `Z_X`'s normality as though the positivity of its tail supplied it would be circular: every `Z_X` system is zero-free, but **a family of zero-free functions can converge, outside the domain of normality, to a function with zeros**.

## 3. Falsifiers and route decision

- `R163_119`'s splice keeps an exterior zero and, by `R163_120`, pays growing constants; it does not contradict (3).
- The Epstein and Davenport–Heilbronn functions lack ζ's exact ordinary Euler product; Beurling–DMV lacks the global integer lattice. The `Z_X` construction uses ζ's prefix, but only splices it with a continuous tail: precisely for that reason, convergence on `Re s>1` does not force normality on `Re s>1/2`.
- **Decision:** do not claim that `R163_121` has weakened the problem. Its contribution is an explicit object and a falsifiable quantitative specification. To move D, a new estimate of the arithmetic tails proving (3) without presupposing (2) beforehand would be needed, or else this object should be abandoned in favor of a discontinuous property of the full lattice.
