# R163_127 — Cross-energy torsion lift: contact selector and exterior faithfulness

**Status:** two new properties proved (the `λ=0` selector and faithfulness on the radical), plus a strict-sign entropic identity. **Does not close Row D:** the opposite geometric sign still needs to be derived from `(PC-ren)`/Poisson–Tate. Fixes `R163_107`'s concrete obstacle without claiming the whole route is closed.

## 1. Construction prescribed before contact

In `R162_1201`'s notation, let `A=M−C` be the Weil operator **complete on the line**, before compressing to `I_T=(-T,T)`, and let `F` be real, of parity `ε∈{+1,−1}`, supported on `I_T`, and primitive. One may first take `F` smooth; for a contact eigenvector, its `H^s` regularity, `s>1/4`, proved in phase 161, is used, which ensures `AF∈L²` because `M`'s multiplier grows only logarithmically. Outside `I_T`, `AF` is a smooth function. Define the cross correlation

```
c_A(v):=∫_ℝ F(t)(AF)(t+v)dt.
w_A(n):=n^(−1/2)c_A(log n),       n≥1.              (1)
```

Since `A` is real, even, self-adjoint and translation-invariant on the full line, `c_A(v)` is real and even. In particular

```
w_A(1)=c_A(0)=⟨F,AF⟩=⟨F,H_TF⟩,                 (2)
```

because `F` is primitive and `H_T=P_TA_TP_T`. If `H_TF=λF`, then `w_A(1)=λ||F||²`. At the first contact window, where `H_T≥0`, the equality `w_A(1)=0` is equivalent to `F∈ker H_T` by the spectral square root. **The vanishing of the first order selects the radical**; it does not hold for positive eigenvectors. Unlike `R163_107`, the `n=1` coefficient was not removed, nor was a harmonic added by hand.

## 2. The exterior tail is a faithful Gamma square

Let `a_m=2m+1/2` (`m≥1`) and `K_m(F)=∫_{I_T}F(t)e^(−a_m t)dt`. By `R162_1201`, for `x>3T` the comb `CF(x)` has already vanished and primitivity removes `m=0`, so

```
(AF)(x)=−Σ_{m≥1} x_m(F)e^(−a_m x),
x_m(F)=∫_{I_T}F(t)e^(a_m t)dt=εK_m(F).          (3)
```

Hence, for `v>4T`, every argument `t+v` in (1) lands in `x>3T` and

```
c_A(v)=−ε Σ_{m≥1} K_m(F)² e^(−a_m v),
w_A(n)=−ε Σ_{m≥1} K_m(F)² n^(−2m−1)
                                      (log n>4T).  (4)
```

The series is absolutely convergent: `|K_m(F)|²≤2T e^(2a_mT)||F||²`, while `e^(2T−v)<1`. If `F≠0`, some `K_m(F)≠0` by the Müntz completeness used in `R162_1201`/paper 47. In (4) every summand has the same sign; hence `c_A(v)≠0` for **every** `v>4T` and `w_A(n)≠0` for every sufficiently large integer. Also `w_A(n)=O_{F,T}(n^(−3))`.

The Möbius inversion of §3 even preserves this sign at **every high mode**. If `k>e^(4T)`, then `kj>e^(4T)` for every `j≥1`; inserting (4) into (5) and using the absolutely convergent series `Σ_{j≥1}μ(j)j^(−s)=1/ζ(s)` (`s>1`) gives

```
ĥ_A(k)=−ε Σ_{m≥1} [K_m(F)²/ζ(2m+1)] k^(−2m−1),
                                           k>e^(4T). (4a)
```

Every coefficient on the right has the same sign. For instance, for any integer `k₀>e^(4T)`, `||h_A||²_{L²(𝕋)}≥2|ĥ_A(k₀)|²>0` if `F≠0`. This formula uses **ordinary** Euler inversion and literally does not exist for a non-integer Beurling lattice.

## 3. Möbius lift, convergence and selector

Define a real even function on `𝕋=ℝ/ℤ` by

```
ĥ_A(k)=Σ_{j≥1} μ(j) w_A(|k|j)   (k≠0),
ĥ_A(0)=0.                                      (5)
```

The tail `O(n^(−3))` gives `Σ_n d(n)|w_A(n)|<∞`, so the sums and the Möbius rearrangement are absolute. Moreover `ĥ_A(k)=O_{F,T}(|k|^(−3))` for large `|k|`. So `h_A∈C¹(𝕋)` and belongs to the log-weighted Wiener algebra; `e^{h_A}` belongs to the same algebra, so `R163_106`'s cocycle extends from smooth tests by absolute convergence.

Inversion over multiples and evaluation at the point `0` give, exactly,

```
w_A(k)=Σ_{j≥1} ĥ_A(kj),
h_A(0)−∫_𝕋h_A=2Σ_{k≥1}ĥ_A(k)=2w_A(1)
                              =2⟨F,H_TF⟩.       (6)
```

Since `ĥ_A(0)=0`, a contact `F∈ker H_T` in fact satisfies `∫h_A=h_A(0)=0`. If, moreover, `h_A` were constant, all its non-zero coefficients would be zero; by inversion, (6) would give `w_A(n)=0` for every `n`, against the strict tail (4). So **`F≠0` on the radical produces a non-constant `h_A` with vanishing first order**. This is exactly the combination that `R163_107`'s canonical lift failed to achieve.

There is also an exact Euler ledger, useful for localizing the geometric work. The identity `μ*log=Λ` and the `O(n^(−3))` decay allow rearranging

```
⟨Φ_Λ,h_A⟩
 =2Σ_{n≥2}Λ(n)n^(−1/2)c_A(log n)
 =2Σ_{2≤n≤e^(4T)}Λ(n)w_A(n)
  −2εΣ_{m≥1}K_m(F)²
       Σ_{n>e^(4T)}Λ(n)n^(−2m−1).                    (6a)
```

The second line separates a finite arithmetic collar from a Gamma–Euler tail of sign known by parity. It does **not** claim the collar has the necessary sign or size; the contact equation only gives (6), not an inequality for (6a).

## 4. Exact arithmetic consequence and remaining gate

For each ordinary prime `p`, `R163_106`'s exact cocycle `Φ_Λ` gives

```
⟨Φ_Λ,e^{h_A(p·)}−e^{h_A}⟩
  =(log p)[e^{h_A(0)}−∫_𝕋e^{h_A}].              (7)
```

At a contact `H_TF=0`, (7)'s right side is simply `(log p)[1−∫e^{h_A}]`. Strict Jensen and §3's faithfulness give

```
⟨Φ_Λ,e^{h_A(p·)}−e^{h_A}⟩
 ≤−(log p)e^(min h_A)/2 ·∫_𝕋|h_A−∫h_A|² <0
                                           (F≠0). (8)
```

To close D, one would need to deduce **independently**, from `(PC-ren)` with Poisson–Tate orientation, polar collars and physical compression, that the same left side of (8) is `≥0` (or that its corrections have a bound unable to absorb the margin). **That comparison was not obtained.** The `≥0` inequality for this `h_A` would be of RH strength and must not be assumed. What is new here is that the test is canonically defined by the cross energy, selects `λ=0` by (6), and remains faithful thanks to (4); the orientation gate was not resolved.

## 5. Adversarial tests

- **Positive eigenvector:** if `H_TF=λF`, `λ>0`, (6) equals `2λ||F||²>0`, so Jensen does not deliver (8). It passes the first-contact test F1 that `R163_107` failed.
- **Deletion and modified weights:** (1)–(6) are operator-theoretic and can be repeated for other combs. At a contact of theirs, a faithful lift and a vanishing linear term likewise appear; so any `≥0` geometric comparison would have to use `Λ`'s exact cocycle and fail for those modifications. No such separation is claimed here.
- **Earlier Gamma–Euler detector:** pairing `Φ_Λ` linearly with `h_A` brings back the sums `−ζ'(2m+1)/ζ(2m+1)` from `R161_068` and the extra factor `A` in the observed vector. Formula (4a) avoids cancellation at high modes, but it does **not** remove `R161_068 §4`'s pullback obstacle: radicality alone does not cancel the Gamma–Euler energy. This comparison prevents presenting (4a) as the missing geometric sign.
- **Non-integer Beurling:** the torsional construction (5) uses indices `k,j∈ℕ` and ordinary Möbius; it does not literally transport to non-integer generalized indices. This is a real difference, but still not a sign proof.
- **`M_m`, Epstein/DH:** the entropic sign alone does not exclude them; the pending geometric comparison must localize its failure there. In particular, simply using the functional equation or squaring `(PC-ren)` would reproduce the falsifiers.

**Round result:** `R163_107` ruled out the autocorrelation lift because its first order was `2||F||²`. The crossed lift replaces that quantity with `2⟨F,H_TF⟩`, which vanishes selectively at contact, while keeping a strict Gamma tail. This is a concrete mathematical candidate for the arithmetic gate; Row D remains open until the opposite geometric sign is built.
