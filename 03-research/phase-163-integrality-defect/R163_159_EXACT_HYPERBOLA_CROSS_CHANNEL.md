# R163_159 — The wave crossing keeps the `Λ*Λ` hyperbola before averaging

**Status:** arithmetic asymptotic formula with an error tending to zero for smooth primitive sources. It is a candidate **object**, not an inequality nor a closure of D.

`R161_034` already identified the product and ratio channels in the coherent Gram. What is specific to this note is the selection, by the **moving cutoffs**, of the channel `mn≈N²`, its truncated-hyperbola coefficient, and `o(1)` control of the other channels on smooth primitive data. It is not claimed that this formula by itself introduces the integer comb with exactly `1` coefficients.

Let `F∈C_c^∞([-T,T])` with both Tate moments zero, `h=Fcal F`, `L=log N`, `M=⌊αN⌋` (`α>0` fixed), and

```
 k_F(v):=⟨h,τ_v JF⟩,
 C_{N,M}(F):=Re⟨Fcal A_MF,τ_{−2L}J A_MF⟩.
```

With `a=Λ` or any weight `a` with `Σ_{n≤x}|a(n)|/√n=O_a(√x)` and the same Gamma part, define the **truncated hyperbola** coefficient

```
 (a *_M a)(k):=Σ_{mn=k,,m,n≤M}a(m)a(n).             (1)
```

Then, for `a=Λ` and also for `R163_147`'s falsifier `a_K`,

```
 C_{N,M}^{a}(F)
   =Re Σ_{k≤M²} (a *_M a)(k) k^(−1/2)
                    k_F(log(k/N²)) + o_{F,a,α}(1).    (2)
```

The formula retains the individual arithmetic collisions that `R163_157` averages away. For `k≤M`, the cutoff removes no divisors and `(Λ *_M Λ)(k)=(Λ*Λ)(k)`; for `k` near `N²`, the **simultaneous** condition `m,n≤M` is essential and cannot be replaced by the full convolution.

## Proof and orientation

Write `B_M^a=Σ_{n≤M}a(n)n^(−1/2)(τ_{log n}+τ_{−log n})`, so `A_M^a=M_Γ−B_M^a`. In the prime–prime product of `C_{N,M}^a`, the rules

```
 Fcal τ_v=τ_{−v}Fcal,
 Jτ_v=τ_{−v}J
```

give four arguments of `k_F`:

```
 log(mn/N²),
 log(m/(nN²)),
 log(n/(mN²)),
 −log(mnN²).                                      (3)
```

The first, coming from `Fcal τ_{log m}` against `Jτ_{−log n}`, is (2)'s summand. In the other three, the argument is `≤−log N+O_α(1)` for `m,n≤αN` and `m,n≥2`. Since `JF` has compact support and `h(t)` decays faster than any exponential as `t→+∞`, `k_F(v)=O_{F,A}(e^{A v})` as `v→−∞`, for every `A>0`. The absolute sum of coefficients of the three discarded channels is `O_a(N)`, and their contribution is `o(1)`.

What remains are the terms containing `M_Γ`. For smooth `F`, `Fcal M_ΓF=Fcal(XF)+Xh` has a super-exponential right tail. Outside `supp F`, `R161_026 (1.1)`'s Gamma Lévy kernel has tail `e^{−|t|/2}+O(e^{−5|t|/2})`; the first term vanishes in `M_ΓF` on both sides by the Tate moments. Consequently `M_ΓF(t)=O_F(e^{−5|t|/2})` as `|t|→∞`, apart from local terms supported on `[-T,T]`. Shifting the second port by `2L`, each Gamma–prime pairing is `O_{F,a,α}(√N·N^{−5/2})` plus a super-exponential tail; Gamma–Gamma is smaller. All are `o(1)`. Grouping (3)'s first channel by `k=mn` proves (2). ∎

## Arithmetic specificity test and logical limit

For `a_K=Λ+η_K`, with `η_K(2^j)=K log2` and zero outside those powers,

```
 (a_K *_M a_K)−(Λ *_M Λ)
    =2(Λ *_M η_K)+(η_K *_M η_K).                 (4)
```

So the **finite object** (2) detects a single-prime modification and keeps every crossing. Its limit divided by `N` does not detect it, per `R163_157`. The identity `Λ*1=log` enters when comparing (2) with the full second jet

```
 W=Λ·log+Λ*Λ,
 Σ_n W(n)n^(−s)=ζ''(s)/ζ(s),                      (5)
```

but (5) does not license replacing the truncated hyperbola of (1) with `Λ*Λ` near `N²`: the boundary term is precisely where `(PC-ren)`'s information may reside.

The scale of the omitted piece is visible even without the kernel `k_F`. For `M=N`, the truncated square has weighted mass

```
 Σ_{m,n≤N}Λ(m)Λ(n)/√(mn)
   =[Σ_{n≤N}Λ(n)/√n]²=4N+o(N),                 (6)
```

while the second jet's diagonal term over the range `k≤N²` weighs

```
 Σ_{k≤N²}Λ(k)log k/√k ∼4N log N.               (7)
```

Both estimates follow from the prime number theorem via partial summation. The **full** convolution `Λ*Λ` on `k≤N²` also contains the two wings `m≤N<n≤N²/m` and `n≤N<m≤N²/n`, absent from (2). The exact decomposition of the region `mn≤N²` is the square plus those two wings. So (5)'s `Λ·log` cannot be informally added to the wave crossing: it is of order `N log N` in the test-free sum, against (6)'s order `N`. A legitimate completion needs the wing terms and `(PC-ren)`'s polar counterterms **before** asserting a cancellation or a sign. This scale contrast assigns no sign to the sum with `k_F` nor proves the wings have one.

Nothing in (2)–(5) imposes a sign on `F` in the radical. In particular, (2) also holds for `Z_K`, which does have a first contact, and so is **not** the law closing D. The step that would need to be proved — without assuming it — is an oriented physical comparison between this arithmetic hyperbola, the `Λ·log` term, the **exact integer comb**, the polar/Tate part, and the scattering square at the contact state. Extending a single cutoff from `N` to `N²` to recover a wing reactivates a ratio channel and a Gamma term: it does not license transferring (2)'s `o(1)` error into that regime.
