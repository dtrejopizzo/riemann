# R163_139 — Physical balance of the Selberg jet: Tate + exterior + positive Gamma tail

**Status:** exact compression identity and sign separation of the tail for `R163_135`'s second jet. It does not control the signed collar and does not close Row D.

## 1. The jet on a kernel vector is purely a boundary term

Let `P` be the orthogonal projection of `L²(ℝ)` onto the zero-extension of the primitive space on `I_T`; `Q=1−P`. Let `A=M−C_Λ` be `R163_127`'s full operator and `0≠F∈ker(PAP)`, of parity `ε`. Then `PAF=0`, i.e. `AF=QAF`. For `N<∞`, set

```
 S_{W,N}F=Σ_{2≤n≤N}W(n)n^(−1/2)τ_{log n}F,
 W=Λ·log+Λ*Λ.                                  (1)
```

With the convention `τ_vF(x)=F(x−v)`, `R163_127`'s correlation satisfies `⟨AF,τ_vF⟩=c_A(v)`. Hence,

```
 Σ_{2≤n≤N}W(n)w_A(n)
    =⟨AF,S_{W,N}F⟩
    =⟨QAF,Q S_{W,N}F⟩.                         (2)
```

Decomposing `Q` into `I_T`'s exterior complement and the two-dimensional Tate space inside `I_T`, we get the literal balance

```
 Σ_{2≤n≤N}W(n)w_A(n)
   =⟨1_{I_T}AF, Π_Tate(1_{I_T}S_{W,N}F)⟩
    +⟨1_{I_T^c}AF,1_{I_T^c}S_{W,N}F⟩.       (3)
```

No interior primitive term was omitted: it vanishes exactly by `PAPF=0`. As `N→∞`, the **scalar side** of (2) converges absolutely by `w_A(n)=O(n^(−3))` and `W(n)≪d(n)(log n)²`; `L²` convergence of `S_{W,N}F` is not claimed. This distinction avoids `R161_068`'s illegitimate pullback.

## 2. The Gamma–Selberg tail has a fixed sign

Fix an integer `N₀>e^(4T)`. For `n>N₀`, `R163_127`'s exterior formula gives

```
 w_A(n)=−ε Σ_{m≥1}K_m(F)² n^(−2m−1).
```

Since `W(n)≥0` and does not vanish at the primes, the tail sum

```
 E_{W,N₀}(F):=Σ_{m≥1}K_m(F)²
                 Σ_{n>N₀}W(n)n^(−2m−1)>0       (F≠0)  (4)
```

converges absolutely. The strict positivity uses completeness of the Gamma moments and the existence of primes greater than `N₀`. Inserting this tail into `R163_135 (3)` gives the identity **with the whole collar kept**:

```
 B_F''(0)
   =−ε Σ_{2≤n≤N₀}W(n)w_A(n)+E_{W,N₀}(F).    (5)
```

So the sum×product square produces a positive exterior energy in the same jet as contact. The only possible compensation lies in the finite collar `n≤N₀`, but each `w_A(n)` includes `AF` and has no known sign. Equation (3) shows that compensation is a Tate/exterior pairing, not a forgotten primitive form.

## 3. What is missing

To exclude a non-zero contact, (5) is **not enough**: we have no bound from `(PC-ren)` forcing `B_F''(0)≤0`, nor one bounding the collar by less than `E_{W,N₀}(F)`. Either of those statements, with every polar and exterior term, would carry Gate 1's strength and must be proved independently. Positivity `W≥0` gives no sign to the collar because the correlation is crossed with `AF`.

The `κ` falsifier preserves (2)–(5) if the ordinary weight `W` is kept in the test while the physical operator uses `a_κ`; its non-trivial radical shows that no conclusion can come solely from the compression's geometry and `W≥0`. A valid formula from `(PC-ren)` would have to use the **same** weight on both sides and reproduce `R163_133`'s Ward defect as the model varies. Balance (3) specifies where the Tate collars and the exterior must enter that formula.
