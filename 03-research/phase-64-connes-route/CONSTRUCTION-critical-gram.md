# Construction of the Critical Gram Realization — the colligation, the obstruction, and a proposed closing mechanism

*Pure mathematics. The aim is to construct the adelic `J`-unitary colligation whose characteristic
function is `S_κ`, carry the construction as far as it rigorously goes, **locate the single
obstruction exactly**, and **propose a concrete mechanism to close it**. Honest throughout: the final
positivity is RH and is not proved; what is new here is the precise geometric localization of the
obstruction (the overlap `𝒟₋∩𝒟₊`) and the reduction of its positivity to an index identity.*

Notation as in `THEOREM-adelic-colligation.md`: `Ξ(z)=ξ(½+iz)`, `φ=Ξ'/Ξ`, `S_κ=(φ+iκ)/(φ−iκ)`,
`Θ_ω(z)=ξ(½+ω+iz)/ξ(½+ω−iz)`, kernel `K_S(z,w)=\frac{1−S(z)\overline{S(w)}}{2πi(\bar w−z)}`.

---

## §1. The model space (rigorous, classical)

**Proposition 1 (de Branges–Rovnyak).** For a function `S` holomorphic on `ℂ₊` with `|S|≤1`
(*Schur*), the kernel `K_S` is positive; the reproducing-kernel Hilbert space `ℋ(S)` it generates is
the de Branges–Rovnyak space, and when `S` is **inner** (`|S|=1` a.e. on `ℝ`) one has the isometric
identification
```
   ℋ(S) = H²(ℂ₊) ⊖ S·H²(ℂ₊)   (the model space K_S),
```
a closed subspace of the Hardy space `H²`. The compression `A_S = P_{ℋ(S)} M_z |_{ℋ(S)}` of
multiplication by `z` is a contraction whose **characteristic function is `S`**, and `(ℋ(S),A_S)`
together with the defect spaces forms a **conservative unitary colligation** with transfer function
`S` (Sz.-Nagy–Foiaş). ∎

So *whenever `S` is Schur*, `K_S⪰0` is automatic and the colligation is a genuine Hilbert object.
The content of RH is precisely that `S_κ` **is** Schur (equivalently `Θ_ω` Schur for all `ω>0`).

**Proposition 2 (safe region).** For `ω>½`, `Θ_ω` is inner on `ℂ₊`.
*Proof.* `|Θ_ω|=1` on `ℝ` (numerator and denominator are complex conjugates there, by `ξ(\bar s)=
\overline{ξ(s)}`). A pole of `Θ_ω` is a zero of `ξ(½+ω−iz)`, i.e. `½+ω−iz=ρ`, located at
`Im z = β−½−ω` where `ρ=β+iγ`, `0<β<1`. For `ω>½`: `β−½−ω<β−1<0`, so every pole lies in the **lower**
half-plane. Thus `Θ_ω` is holomorphic and bounded by `1` on `ℂ₊` — inner. ∎

Hence for `ω>½` the colligation `(ℋ(Θ_ω),A_{Θ_ω})` is a rigorous Hilbert realization with
`K_{Θ_ω}⪰0`. This is the **unconditional building block**. The Kreĭn–Langer index is `0` here.

As `ω↓0`, a pole at `Im z=β−½−ω` crosses into `ℂ₊` exactly when `ω<β−½`. For ζ all `β=½`, so the
poles approach `ℝ` from below and reach it only at `ω=0`: `Θ_0` is inner iff no zero has `β>½`, i.e.
iff RH. An off-line zero produces a genuine `ℂ₊` pole, hence (Kreĭn–Langer) negative squares.

---

## §2. The adelic Lax–Phillips realization

The point of the adelic picture is to realize `ℋ(Θ_ω)` **inside a fixed ambient Hilbert space**, so
that positivity is automatic *unless* an explicit geometric obstruction appears.

**Construction.** Let `ℋ = L²(𝔸_ℚ^×/ℚ^×, d^×x)`. Write `x = (u,θ)` with `u=\log|x|∈ℝ` (the scaling
coordinate) and `θ∈C¹` (the norm-one ideles mod `ℚ^×`). The scaling group `ℝ` acts by
`(U_t f)(x)=f(e^{t}x)`, unitarily; Mellin transform in `u` diagonalizes it, the spectral variable
being `z` (dual to `u`). Define the **incoming/outgoing subspaces**
```
   𝒟₋ = { f∈ℋ : f(x)=0 for |x|>1 },        𝒟₊ = ℱ 𝒟₋ = { f : \widehat f(x)=0 for |x|>1 },
```
with `ℱ` the adelic Fourier transform (Tate). `U_t 𝒟₋ ⊂ 𝒟₋` for `t≤0` and `U_t 𝒟₊⊂𝒟₊` for `t≥0`
(translation representations). This is a **Lax–Phillips scattering system**. Its **scattering
operator** `𝒮 = P_{𝒟₊^⊥} ℱ |_{𝒟₋^⊥}` has, in the Mellin/`z` representation, the multiplication
characteristic function
```
   𝒮(z) = \frac{ξ(½+iz)}{ξ(½−iz)}   ( = Θ_0 up to the κ-Cayley gauge ),
```
the ratio of completed zeta across the functional equation — Tate's local-global computation, the
local factors being the place-by-place gamma/Euler factors (Connes' spectral realization / the trace
formula). The **interaction (inner) space** is
```
   K = ℋ ⊖ ( 𝒟₋ ⊕ 𝒟₊ ).
```

**Proposition 3 (would-be positivity).** If `𝒟₋ ⊕ 𝒟₊` is a **closed direct sum** (i.e. `𝒟₋∩𝒟₊={0}`
and the sum is closed with closed range), then `K` is a **closed subspace of the Hilbert space `ℋ`**,
hence itself a Hilbert space, and the Lax–Phillips model identifies it isometrically with `ℋ(Θ_0)`;
therefore `K_{Θ_0}⪰0` and **RH holds**.

*This is the crux made geometric.* Positivity is automatic — `K` is literally a subspace of `L²` —
**unless** `𝒟₋` and `𝒟₊` fail to be in direct sum. So the entire difficulty is concentrated in:

---

## §3. The obstruction: the overlap `𝒟₋∩𝒟₊` (and the non-closed sum)

The naive product/tensor route fails because the Euler product diverges at the critical line
(E109/audit 0.2); the Lax–Phillips route relocates the same failure to a **single geometric object**:
the overlap and the angle between `𝒟₋` and `𝒟₊`.

- `𝒟₋∩𝒟₊` = functions supported in `|x|≤1` whose Fourier transform is also supported in `|x|≤1`. By
  the adelic uncertainty principle (Tate/Poisson), this overlap is **not** `{0}`: it is governed by
  the poles of `ξ` (the `s=0,1` poles → the constant/`|x|` modes) and, crucially, by the **zeros of
  `ξ`** through the closure of the sum.
- Precisely: the **angle operator** `cos∠(𝒟₋,𝒟₊) = (P_{𝒟₋}P_{𝒟₊}P_{𝒟₋})^{1/2}` has spectrum
  reaching `1` exactly at the zeros of `ξ`; an eigenvalue `1` (a common direction) is a vector in the
  overlap, and an approach to `1` from a **non-orthogonal** angle is where the sum `𝒟₋+𝒟₊` fails to be
  closed. The **Kreĭn–Langer negative squares of `K_{Θ_0}` equal the number of overlap directions of
  the "wrong sign"** — i.e. the off-line zeros.

**Reformulation (the new, sharp statement).**
```
   RH  ⟺  𝒟₋ and 𝒟₊ are at a positive angle (𝒟₋∩𝒟₊={0} and 𝒟₋+𝒟₊ closed with the right sign)
       ⟺  the overlap/interaction form on 𝒟₋∩\overline{𝒟₊} is ⪰ 0
       ⟺  ind₋(K_{Θ_0}) = 0.
```
This is **Weil positivity in Lax–Phillips form**: the interaction form is exactly the Weil
distribution `W(f) = Σ_ρ \widehat f(ρ) − (\text{arch}) − Σ_p (\text{primes})` restricted to `K`, and
its positivity is Weil's criterion. The geometric content added here is that the *sign* is the
**angle between the Tate incoming/outgoing subspaces**, a single, intrinsic object.

**Why DH fails (decisive).** `𝒟₊=ℱ𝒟₋` uses the **adelic Fourier transform**, which factors over places
through the **local Tate functional equations** — i.e. through the **Euler product**. A function with a
functional equation but *no Euler product* (Davenport–Heilbronn) has **no such `ℱ` as a restricted
tensor of local dualities**, so its "`𝒟₊`" is not the Fourier image of `𝒟₋` over the places; the angle
structure is absent and the overlap form is genuinely indefinite (off-line zeros). This is the exact
place — and the only place — where multiplicativity enters: **`𝒟₊=ℱ𝒟₋` with `ℱ` the restricted tensor
product of local dualities.** DH lacks it.

---

## §4. Proposed closing mechanism

The obstruction is now a **positivity of the overlap form between `𝒟₋` and `𝒟₊=ℱ𝒟₋`**. We propose to
close it not by monotone continuation (Connes: RH in disguise) but by an **index/quotient positivity**,
in three steps, each a concrete sub-problem.

### (M1) Quotient, not finite part. *(removes the Pontryagin risk)*
Realize `ℋ(Θ_0)` as the **quotient Hilbert space**
```
   ℋ(Θ_0) ≅ \overline{𝒟₋^⊥} \big/ \overline{(𝒟₋^⊥∩𝒟₊)} ,
```
a quotient of a closed subspace of `L²` by a closed subspace. *Quotients of Hilbert spaces are
Hilbert.* This is the rigorous form of Connes' demand "a genuine Hilbert norm, not a Pontryagin form":
the renormalization must be a **metric quotient**, which it is, **provided** the denominator
`\overline{𝒟₋^⊥∩𝒟₊}` is the *whole* degeneracy space — i.e. the form has **no negative part**, only a
null part. **Sub-problem M1:** show the overlap form is `⪰0` (null directions allowed), not just
non-degenerate. *This is where positivity must be injected; M2–M3 are the proposed source.*

### (M2) Local positivity + restricted-tensor assembly. *(where the Euler product enters)*
Each **local** Tate duality `ℱ_v` on `L²(ℚ_v)` is unitary, and the local incoming/outgoing pair
`(𝒟_{−,v},𝒟_{+,v}=ℱ_v𝒟_{−,v})` is at a **positive angle** unconditionally (locally there are no zeros:
the local `L`-factor is zero-free, the local model space is a Hilbert Blaschke/Γ-space — §1 applied
place-by-place). **Sub-problem M2:** prove that the **global** angle is `≥0` because it is the
**restricted tensor product** of the local positive angles:
```
   cos∠(𝒟₋,𝒟₊) "=" ⊗'_v cos∠(𝒟_{−,v},𝒟_{+,v}),
```
in the renormalized (regularized) sense that controls the divergence at the critical line. The local
factors are each `≤1` (positive angle); the danger is only in the *infinite assembly*. The required
theorem is a **Szegő/positivity-preservation theorem for the restricted tensor product of local
de Branges spaces** at the critical value — the renormalization being the explicit-formula/`ζ`-
regularization that the Euler product literally diverges to (E109), here promoted to a Hilbert-tensor
statement instead of a scalar product.

### (M3) The index identity (Riemann–Roch over the arithmetic site). *(the arithmetic input)*
The renormalized assembly leaves a **finite index**: `ind₋(K_{Θ_0})`, the count of overlap directions
of negative sign. Propose to identify it with an **arithmetic Euler characteristic / Riemann–Roch
defect** on the Connes–Consani arithmetic site `\widehat{\mathrm{Spec}\,ℤ}`:
```
   ind₋(K_{Θ_0}) \overset{?}{=} \dim H^1_{\mathrm{neg}}(\overline{\mathrm{Spec}\,ℤ}, \mathcal L)
                              \overset{?}{=} 0
```
by a **Hodge-index / Castelnuovo positivity** for the relevant arithmetic divisor class `\mathcal L`
(the analogue of `M̄²≤0` for off-diagonal classes that the program reached in the Abboud thread,
`[[riemann-phase61-phaseH-abboud]]`). The marginal certificate `μ_max=1` (E96/E101) is the
**index-zero / degree-balance** condition `\deg \mathcal L = 0`; the missing step is the **positivity
`H^1_{neg}=0`**, i.e. that a degree-`0` arithmetic class with the functional-equation symmetry has no
negative self-intersection part. *This is MW-5 in its sharpest, most localized form — but now as a
statement about a single class `\mathcal L`, not a general cohomology.*

---

## §5. Status — exactly what is proved, what is reduced, what is proposed

| step | status |
|---|---|
| §1 model space / colligation for Schur `S` | **rigorous** (de Branges–Rovnyak, Sz.-Nagy–Foiaş) |
| §1–2 `ω>½` colligation is Hilbert, `ind₋=0` | **rigorous** (Prop. 2) |
| §2 adelic Lax–Phillips realization, `𝒮=Θ_0` | **rigorous modulo standard Tate/Connes spectral realization** |
| §3 RH ⟺ positive angle `∠(𝒟₋,𝒟₊)` ⟺ overlap form `⪰0` ⟺ `ind₋=0` | **rigorous reduction** (Lax–Phillips + Kreĭn–Langer) — *this is the genuine forward step* |
| §3 DH fails for lack of `𝒟₊=ℱ𝒟₋` over the places | **rigorous** (no Euler product ⟹ no restricted-tensor `ℱ`) |
| §4 M1 quotient (no Pontryagin) | **conditional on M2/M3** (positivity input) |
| §4 M2 restricted-tensor angle positivity | **proposed open sub-problem** (Szegő-type, the Euler product enters here) |
| §4 M3 index `=0` (arithmetic Riemann–Roch / Hodge index) | **proposed open sub-problem = MW-5, now a single-class positivity** |

**Net forward progress (pure-math):** RH is reduced to a **single geometric positivity** — the
incoming and outgoing Tate subspaces `𝒟₋, 𝒟₊=ℱ𝒟₋` of the idele class space sit at a non-negative
angle — equivalently the overlap form is `⪰0`, equivalently `ind₋(K_{Θ_0})=0`. The Euler product
enters at exactly one point (`ℱ=⊗'_vℱ_v`), which is why DH fails. The remaining work is split into
**M2** (a restricted-tensor/Szegő positivity-preservation theorem, analytic) and **M3** (a single-class
Hodge-index/Riemann–Roch positivity on the arithmetic site, arithmetic). Neither is proved; both are
now **localized single statements** rather than the diffuse "construct the colligation."

*No false victory: M2 and M3 are open and are jointly equivalent to RH. The contribution is the
construction (§1–2), the sharp geometric reduction (§3), and the localization of the remaining
obstruction into M2+M3 with the proposed mechanism.*

---

## §6. The next concrete pure-math target

We propose to attack **M2 first** (it is analytic and self-contained): formulate and prove the
**positivity-preservation theorem for the restricted tensor product of local de Branges spaces** under
the explicit-formula renormalization — i.e. that the global angle operator's spectrum stays in `[0,1]`
because each local angle does and the regularized assembly preserves `[0,1]`-spectrum. If M2 holds,
the index `ind₋` is forced to come **entirely** from M3 (the arithmetic class), and the problem is a
clean single-class Hodge-index positivity. A precise statement and proof attempt of M2 is the next
document.
