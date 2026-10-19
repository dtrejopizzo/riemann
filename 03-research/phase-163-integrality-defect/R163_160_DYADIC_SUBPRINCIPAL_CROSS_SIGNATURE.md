# R163_160 — Dyadic subprincipal signature of the Euler–Poisson crossing

**Status:** exact comparative limit for smooth primitive sources. It detects the falsifier `Z_K` where `R163_157`'s macroscopic term does not see it. It does **not** prove a first-contact inequality nor close D.

Let `F∈C_c^∞([-T,T])` be primitive, `k_F(v)=⟨Fcal F,τ_v JF⟩`, and `C_N^a(F)=C_{N,N}^a(F)` from `R163_159`. Take the weight `a_K=Λ+η_K`, `η_K(2^j)=K log2` for `j≥1`, and zero at every other integer. Fix `0≤θ<1` and `N_j=⌊2^(j+θ)⌋`. For `0<y≤1` define

```
 I_F(y)=∫_0^1 x^(−1/2) k_F(log(xy))dx.           (1)
```

Then the difference **without dividing by `N_j`** has the limit

```
 lim_{j→∞}[C_{N_j}^{a_K}(F)−C_{N_j}^{Λ}(F)]
   =2K(log2) Re Σ_{r=0}^∞ y_r^(−1/2) I_F(y_r),
                    y_r=2^(−θ−r).                  (2)
```

The series converges absolutely. The right side's function depends on `log_2 N`'s fractional position and may have a discontinuity when the next power of 2 is born. In particular, **modifying a single prime leaves an order-one signature** after cancelling ζ's common background, even though its contribution divided by `N` is zero.

## Proof

By `R163_159 (2)`, the `o(1)` error holds for both `Λ` and `a_K`. Subtracting, `R163_159 (4)`'s exact weight identity splits off a mixed part `2Λ *_N η_K` and a part `η_K *_N η_K`.

In the mixed part, fix `n=2^(j-r)≤N_j`, `r≥0`, and set `y_{j,r}=n/N_j→y_r`. `R163_157`'s weighted prime measure, now with `m/N_j=x`, and the prime number theorem give

```
 Σ_{m≤N_j} Λ(m)m^(−1/2)
       k_F(log(mn/N_j²))
    =√N_j I_F(y_{j,r})+o_F(√N_j)                (3)
```

for each fixed `r`. Multiplying by `η_K(n)/√n=K(log2)/(√N_j√y_{j,r})` produces the term `K(log2)y_r^(−1/2)I_F(y_r)`; the symmetry `m↔n` gives (2)'s factor of 2.

To justify the step from finite sum to infinite series, note that `k_F(v)` decays faster than `e^{A v}` for every `A>0` as `v→−∞`, by `Fcal F`'s right tail and `JF`'s compact support. So, uniformly for `0<y≤1`,

```
 |I_F(y)|≤C_{F,A}y^A.                           (4)
```

Chebyshev's bound `Σ_{m≤N}Λ(m)/√m=O(√N)` and (4) give a majorant `C_{F,A}y_{j,r}^{A−1/2}` for each normalized mixed summand. Choosing `A>1/2` makes the geometric tail in `r` summable, uniformly in `j`.

The `η_K *_N η_K` part is `o(1)`: writing both indices as powers `2^(j-r),2^(j-s)`, each pair with fixed `r,s` has weight `O_K(N_j^(−1))`; for large `r+s`, (4) gives a uniform geometric bound. The same splitting argument over `r+s≤R` and `r+s>R` proves vanishing, letting `j→∞` first and then `R→∞`. This proves (2). ∎

## Physical scope

The jump between `θ→1−` and `θ=0` is the newly born term `2K(log2)Re I_F(1)` when it is non-zero; its sign depends on the test. A perturbation of `Λ` at only **finitely many indices** leaves no such signature: its factors `n/N→0` and (4) annihilate its contribution. The `Z_K` model does modify every power of 2 and so survives that erasure.

Limit (2) compares two different operators on **the same fixed source**. One cannot simply insert a contact vector of ζ or of `Z_K`, nor infer that (2)'s value has the opposite sign on those radicals. Closing D would still require identifying, from `(PC-ren)` with the integer comb, Tate and exterior, an equality law making ζ's arithmetic signature incompatible with a non-zero contact. The mere existence of (2) is not that law.
