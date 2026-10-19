# R163_150 — Corner anomaly at `(PC-ren)`'s two cutoffs

## Theorem: the moving limit is path-dependent

Let `μ_{M,N}` be the **renormalized** ratio measure of `S_N^ren L_M^*` given in `R163_148` (it includes the continuous subtraction `C_N L_M^*`). Fix `α>1` and `φ∈C_c^∞(ℝ)`. Then

```
lim_{N→∞} ⟨μ_{⌊αN⌋,N}−μ_{N,N},φ⟩
  = (1/2)∫_1^α y^(−1/2) φ(−log y)dy.                 (1)
```

If `φ≥0` and is positive at some point of `(-log α,0)`, the limit is strictly positive. So **the distributional limit of the renormalized product, if it exists along both paths, cannot be the same** for `M=N` and `M=⌊αN⌋`. The ordinary polar subtraction of `R161_003` does not remove this corner anomaly.

### Proof

The difference between the two cutoffs only involves `N<n≤⌊αN⌋`. By `R163_148 (1)`, its pairing with `φ` is

```
Σ_{N<n≤⌊αN⌋} Λ(n)/√n [Σ_{k≤N} f_n(k)−∫_0^N f_n(x)dx],
f_n(x)=x^(−1/2)φ(log(x/n)).                           (2)
```

If `supp φ⊂[-R,R]`, for `N<n≤αN` the function `f_n` vanishes when `x<N e^(−R)` and satisfies, uniformly in that range, `f_n^(j)(x)=O_{φ,R,α}(N^(−1/2−j))` for `j=0,1,2` wherever it does not vanish. The Euler–Maclaurin formula with second-derivative remainder gives

```
Σ_{k≤N}f_n(k)−∫_0^N f_n(x)dx
 = 1/2 f_n(N)+O_{φ,R,α}(N^(−3/2))
 = φ(log(N/n))/(2√N)+O(N^(−3/2)).                    (3)
```

Since `Σ_{n≤αN}Λ(n)=O_α(N)`, (3)'s error, after summing the weights `Λ(n)/√n`, is `O_{φ,α}(N^(−1))`. The leading term is

```
(1/(2N)) Σ_{N<n≤αN} Λ(n)(n/N)^(−1/2)φ(−log(n/N)).     (4)
```

The prime number theorem, in its weak-convergence form `N^(−1)Σ_nΛ(n)δ_{n/N}→dy` on compact positive intervals, turns (4) into (1)'s right side. ∎

**Physical corollary.** If `F∈C_c^∞(ℝ)` is non-zero and `c_F(v)=⟨F,τ_vF⟩`, then for `α>1` sufficiently close to 1,

```
Re lim_{N→∞}⟨μ_{⌊αN⌋,N}−μ_{N,N},c_F⟩>0.          (5)
```

Indeed, `Re c_F(0)=||F||²>0` and `c_F` is continuous, so the real part of (1)'s integrand is positive for `1≤y≤α` when `α` is close to 1. This still holds if `F` satisfies the two primitive Tate moments: those moments do not make `c_F(0)` equal to zero. The corollary concerns **only** the term `S_N^ren L_M^*`, not `(PC-ren)`'s full sum.

## Interpretation and falsifiers

The anomaly is the **Euler–Maclaurin half-step at the integer endpoint `k=N`**, transported by the primes `n≈N`; it is not the isolated diagonal atom `k=n`. This distinction matters: (1) is obtained after jointly summing the integer comb and its continuous counterterm, keeping every nearby collision. Evaluating each of `R163_149`'s rational fibres before summing does not legitimately reproduce (1).

For `R163_147`'s falsifier `Z_K`, replacing `Λ` with `a_K=Λ+K log2·1_{n=2^j}` leaves **the same limit**: in `(N,αN]` there are only `O_α(1)` powers of 2, and their contribution to (4) is `O_{K,α}(N^(−1))`. More generally, every finite perturbation of prime weights leaves the main anomaly intact. So (1) uncovers a physical boundary term that must be preserved, but it cannot by itself impose ζ's exact law nor the Weil sign.

## Precise requirement for the gate

A candidate for `(PC-ren)`'s finite limit that identifies `S_N^ren A_MF` with `R161_021`'s scattering defect must specify the relation between `M` and `N`, or exhibit in **the other pieces of `(PC-ren)`** a counterterm opposite to (1). Otherwise its value changes when passing from `M=N` to `M=αN`, while the final physical defect does not depend on cutoffs. The cancellation must happen before compressing and must survive Tate/exterior; only afterward can one look for the sign distinguishing ζ from `Z_K`. That cancellation and the sign remain **open**. Row D is not closed.
