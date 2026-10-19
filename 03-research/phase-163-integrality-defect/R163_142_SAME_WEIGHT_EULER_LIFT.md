# R163_142 — Single-weight Euler lift: the selector measures exact integrality

**Status:** construction and algebraic equivalences proved. It couples the physical operator's weight with the inverse of its own Euler product, fixing `R163_132`'s decoupling. It does not supply `(PC-ren)`'s orientation nor close Row D.

## 1. Single-weight definition

Let `a(n)` be a real weight with `a(1)=0` and formal/Euler product

```
 Z_a(s)=exp(Σ_{n≥2}a(n)n^(−s)/log n)
       =Σ_{n≥1}b_a(n)n^(−s),  b_a(1)=1.        (1)
```

We assume `Z_a` and its inverse converge absolutely for `Re s>1`, as happens for ζ and the finitely-modified `κ` models. Let `μ_a` be the coefficients of `Z_a(s)^{-1}`, i.e. `μ_a*b_a=δ_1`. On window `I_T`, take the full operator `A_a=M−C_a` with **the same weight** `a`, and for `F` real, primitive and of parity `ε` define

```
 c_{A_a}(v)=⟨F,τ_v A_aF⟩,
 w_{a,F}(n)=n^(−1/2)c_{A_a}(log n),
 ĥ_{a,F}(k)=Σ_{j≥1}μ_a(j)w_{a,F}(|k|j)   (k≠0),
 ĥ_{a,F}(0)=0.                                  (2)
```

For ζ, `b_Λ(n)=1`, `μ_Λ=μ` and (2) is exactly `R163_127`. For any finite modification of ζ, `μ_a` has a series absolutely convergent for `Re s>1`; since `w_{a,F}(n)=O(n^(−3))` beyond the collar, (2) converges absolutely, defines a `C¹` function, and allows the following rearrangements.

## 2. Selector and equivalence with the exact ledger

Define `r_a=μ_a*1`. Then

```
 h_{a,F}(0)−∫h_{a,F}
   =2Σ_{k≥1}ĥ_{a,F}(k)
   =2Σ_{n≥1}r_a(n)w_{a,F}(n).                  (3)
```

The first equality is Fourier evaluation; for the second, regroup `n=kj` in the absolutely convergent sum. The arithmetic property turning (3) into the physical contact is **exactly**

```
 r_a=δ_1   ⇔   μ_a=μ   ⇔   b_a(n)≡1.        (4)
```

Indeed, `μ*1=δ_1` and the Dirichlet inverse is unique. If `r_a=δ_1`, then `μ_a=μ`, hence `b_a=1`; the converse implications are immediate. So, for ζ,

```
 h_{Λ,F}(0)−∫h_{Λ,F}
    =2w_{Λ,F}(1)=2⟨F,H_{T,Λ}F⟩.           (5)
```

At a first contact of ζ, (5) equals zero **without adjusting the test**. For a weight `a` with `b_a≠1`, the selector contains the explicit defect

```
 2Σ_{n≥2}r_a(n)w_{a,F}(n),                 (6)
```

in addition to the physical term `2w_{a,F}(1)`. We do not claim (6) is non-zero at every vector of a falsifier model; the exact claim is that the selector's universal reduction to the compressed energy holds if and only if the integer ledger is `b_a≡1`.

## 3. The Gamma tail keeps its own weight

`M`'s exterior expansion is the same and the comb `C_a` is finite on a window. For `k>e^{4T}`,

```
 ĥ_{a,F}(k)
   =−εΣ_{m≥1}K_m(F)² k^(−2m−1)
                      ·Σ_{j≥1}μ_a(j)j^(−2m−1)
   =−εΣ_{m≥1}[K_m(F)²/Z_a(2m+1)]k^(−2m−1).  (7)
```

If `Z_a(2m+1)>0` for `m≥1`, as for ζ and the `κ` models, the lift remains faithful: every `F≠0` has high coefficients of sign `−ε`. The tail now reads `Z_a` of the **same weight** that created the contact, not ζ inserted externally.

## 4. Computed κ falsifier

For `R162_103`'s `a_κ`, write `δ=κ−1`. Then

```
 Z_{a_κ}(s)=ζ(s)exp(δ[2^(−s)+3^(−s)+½·4^(−s)]),
 r_{a_κ}(s):=Σ_nr_{a_κ}(n)n^(−s)
       =exp(−δ[2^(−s)+3^(−s)+½·4^(−s)]).    (8)
```

The second equality uses `r_a=μ_a*1`, whose series is `Z_a^{-1}ζ`. For instance,

```
 r_{a_κ}(2)=−δ,
 r_{a_κ}(3)=−δ,
 r_{a_κ}(4)=(δ²−δ)/2.                         (9)
```

There are also coefficients on products of powers of 2 and 3. By (3), `H_{T,a_κ}`'s contact leaves a global residual sum of correlations `w_{a_κ,F}` over that support. This is the concrete failure of exact integrality that the two-ledger lift `R163_132` could not see. `R163_133` complementarily gives its Ward defect at the torsional atoms.

## 5. Scope

Identities (3)–(9) combine **in a single step** the physical operator, the Euler product and the ordinary integers' `b(n)≡1` condition. This gets past the two-ledger falsifier as a formulation problem. But for ζ two facts are still missing: an oriented comparison of `(PC-ren)`/Poisson–Tate with (7)'s exterior energy, and control of `R163_140`'s rational collars. The vanishing of the first order via (5) does not imply Jensen's entropic term has the opposite physical sign. Row D remains open.
