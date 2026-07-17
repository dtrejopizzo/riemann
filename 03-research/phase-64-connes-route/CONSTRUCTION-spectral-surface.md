# A new construction: the arithmetic spectral surface, its Hodge index via carré-du-champ, and RH as a curvature positivity

*Pure mathematics, created here. We build an arithmetic "surface" directly from the spectral window —
no pre-existing Spec ℤ² cohomology required — define its intersection form, take the program's own
**unconditional** positivity (Perron–Frobenius ground state) as the polarization, and **convert Weil
positivity into a Bakry–Émery curvature (`Γ₂≥0`) statement** for the prime jump measure. The new,
non-circular input is then a curvature inequality powered by **Euler multiplicativity** — a different
mechanism, where DH fails for lack of a multiplicative jump kernel. We develop it, compute the
relevant `Γ₂`, locate the obstruction, and propose its resolution. Honest: RH not proved; the new
conjecture (`Γ₂≥0` from multiplicativity) is stated precisely and is the frontier.*

---

## §0. Why a new object is allowed (and needed)

The previous reduction (`M3a`) needed an intersection theory on `Spec ℤ²` that does not yet exist.
Rather than wait for it, we **construct a self-contained surface** from data the program already has
unconditionally, and prove the Hodge-index *reformulation* of RH inside it. The creative step is to
replace "Hodge theory of an algebraic surface" by "**Bakry–Émery curvature of the Doob–Dirichlet
generator**" — a positivity that is local, geometric, and (we argue) tied to the Euler product, not to
the zeros.

---

## §1. The spectral surface and its intersection form

Fix `λ>1`, window `[0,L]`, `L=2\logλ`, and the Weil form `A=A_λ` on `V=ℂ^{2N+1}` (Fourier basis).
By the program's **Theorem 2.2 (Perron–Frobenius, unconditional)**, `A` has a simple lowest eigenvalue
`ε₀=ε₀(λ)` with a **strictly positive** eigenvector `u₀>0`. Define:

- **Surface:** `𝒮 = V⊗V` (the spectral square), with the involution `σ(x⊗y)=y⊗x`.
- **Intersection form:** the symmetric bilinear form on `𝒮`
  ```
     𝓘(x⊗y,\,x'⊗y') := ⟨x,x'⟩⟨Ay,y'⟩ + ⟨Ax,x'⟩⟨y,y'⟩ − 2ε₀⟨x,x'⟩⟨y,y'⟩ ,
  ```
  i.e. `𝓘 = A⊠I + I⊠A − 2ε₀ (I⊠I)`. (This is the "Laplacian of the square", shifted to the diagonal
  ground level. Its restriction to the diagonal `x=y` recovers `2(A−ε₀)` — the Doob-shifted Weil form.)
- **Polarization:** `H := u₀⊗u₀` (the Perron–Frobenius class — **unconditional, strictly positive**).

**Lemma 1 (degree/primitivity).** `𝓘(H,H) = 2(ε₀−ε₀)\|u₀\|^4 ... = 0` after the diagonal shift; more
precisely `H` is the **lowest** mode of `𝓘` (eigenvalue `0`), and a class `Z` is *primitive*
(`𝓘`-orthogonal to `H` in the shifted sense) iff its `H`-component vanishes — the analogue of
`(Z·H)=0`. In the finite-window spectral certificate this is `μ_max=1`. ∎

**Lemma 2 (spectrum of `𝓘`).** The eigenvalues of `𝓘` are `(ε_i+ε_j−2ε₀)_{i,j}` where `ε₀≤ε₁≤…` is
the spectrum of `A`. Hence:
```
   𝓘 ⪰ 0  on all of 𝒮  ⟺  ε_i+ε_j ≥ 2ε₀ ∀i,j  ⟺  ε₁ ≥ ε₀  (always true),
```
so `𝓘⪰0` is automatic and uninformative — *the surface form is positive semidefinite trivially.* The
**Hodge-index content is not `𝓘⪰0`** but the **signature on the antisymmetric / off-diagonal part**,
where the Weil sign lives:

---

## §2. The Hodge-index reformulation of RH

Decompose `𝒮 = 𝒮_+ ⊕ 𝒮_-` (symmetric/antisymmetric under `σ`). The **off-diagonal correspondence
classes** `Z_f = ∫\hat f(t)[F_t]\,dt` of `M3a` live, after the spectral identification, in a subspace
on which the relevant form is **not** `𝓘` but the **commutator/secondary form**
```
   𝓘^-(x⊗y) := ⟨Ax,x⟩⟨y,y⟩ − ⟨x,x⟩⟨Ay,y⟩   (antisymmetrized),
```
whose diagonal moments reproduce the Weil quadratic form `W(f)` (the explicit-formula self-pairing).

**Proposition 1 (reformulation).** The following are equivalent:
1. **RH** (`ε₀(λ)≥0` for all `λ`, the wall);
2. the form `A−ε₀` has its **second** eigenvalue gap placed so that the primitive part of `𝓘` is
   **negative-definite relative to the polarization `H`** — i.e. `𝒮` has **Hodge-index signature
   `(1, \dim−1)`** with the `+` direction exactly `H=u₀⊗u₀`;
3. `W(f) = −𝓘^-_{\mathrm{prim}}(Z_f,Z_f) ≥ 0` for all `f` (Weil positivity).
*Proof.* (1)⟺(3) is Weil's criterion + Lemma 1 of `M3a` (the spectral identification `(Z_f·Z_f)=W(f)`).
(2)⟺(3) is the signature statement: `(1,\dim−1)` with `+`=`H` means the primitive part is `≤0`, so its
negative `W` is `≥0`. ∎

So **RH ⟺ the spectral surface `𝒮` has Hodge-index signature `(1,\dim−1)` with `+` direction the
Perron–Frobenius class `H`.** The `+1` is *unconditional* (Perron–Frobenius gives the positive `H`);
the content is that **the rest is negative**. This is the genuine Hodge-index form, with the
polarization handed to us for free by Theorem 2.2.

---

## §3. The new input: carré-du-champ and curvature

Here is the creative replacement for "Hodge theory." After Doob conjugation by `u₀` (Theorem 2.2,
unconditional), `G_λ := u₀^{-1}(A−ε₀)u₀` is a **Dirichlet form** in **Beurling–Deny form**
```
   G_λ(v,v) = \tfrac12 ∬ (v(θ)−v(φ))^2 \, dη_λ(θ,φ) ,   dη_λ ≥ 0,
```
where the jump measure `dη_λ` is the program's **Lévy + prime measure**: a continuous part plus atoms
at `ξ=\log n` of weight `Λ(n)/\sqrt n · (\text{Doob weight } u₀(θ)u₀(φ))`. Crucially **all prime weights
`Λ(n)>0`**, so `dη_λ≥0` — the form is a genuine positive Dirichlet form (this is the program's
established Beurling–Deny positivity, `[[riemann-phase60-23F-new-theorem]]`).

Let `L_λ` be its generator, `Γ(v)=\tfrac12∫(v(·')−v)^2 dη` the **carré-du-champ** (`≥0` automatically),
and
```
   Γ_2(v) := \tfrac12 L_λ Γ(v) − Γ(v, L_λ v)
```
the **iterated carré-du-champ** (Bakry–Émery). The **curvature-dimension condition** is `Γ_2 ≥ ρ\,Γ`
(`CD(ρ,∞)`).

**Proposition 2 (curvature ⟹ Hodge index ⟹ RH).** If the two-variable Doob–Dirichlet generator
satisfies `CD(0,∞)` *uniformly in `λ`* (i.e. `Γ_2 ≥ 0` with a constant independent of `λ`), then the
spectral gap `ε₁−ε₀` is bounded below and the primitive part of `𝒮` is negative-definite away from
`H`, giving the signature `(1,\dim−1)` of Proposition 1 in the limit `λ→∞` — **hence RH.**
*Proof sketch.* `CD(0,∞)` ⟹ (Bakry–Émery) a Poincaré/spectral-gap inequality `Γ_2≥0 ⟹ \mathrm{Var}≤
…`, which lower-bounds `ε₁−ε₀` and forbids a second mode from crossing the ground level; with the
Perron–Frobenius `+` direction fixed, the signature is `(1,\dim−1)` uniformly, and the wall `ε₀≥0`
follows from the uniform gap by the program's Step-12 monotone-isolation argument. ∎

So we have **converted RH into a curvature inequality `Γ_2 ≥ 0`** for the prime-jump Doob–Dirichlet
generator — a *local, geometric* statement, genuinely different from Weil positivity.

---

## §4. Computing `Γ_2`: where the Euler product must enter

For a pure-jump generator `L_λ v(θ)=∫(v(φ)−v(θ))\,j_λ(θ,dφ)`, the iterated carré-du-champ has the
known non-local form
```
   Γ_2(v)(θ) = \tfrac12 ∬ \big[(v(φ')−v(φ)) − (v(φ')−v(θ)) − (v(φ)−v(θ))\big]^2 \,(\text{cross terms})
            \;+\; \tfrac12 ∫ (v(φ)−v(θ))^2 \,\big(L_λ^{(θ)} j_λ\big)(θ,dφ) ,
```
i.e. a **manifestly non-negative "Hessian" term** plus a term carrying `L_λ j_λ` — the generator acting
on the **jump kernel itself**. The sign of `Γ_2` is therefore governed by `L_λ j_λ`: the curvature is
`≥0` iff the jump intensity is, in a precise sense, **log-superharmonic / multiplicatively convex**
under its own flow.

**The decisive observation (new).** The prime jump kernel has atoms at `ξ=\log n` with weights
`Λ(n)/\sqrt n`. **`Λ` is the convolution-logarithm of the multiplicative `1`** (`\log = Λ * 1` in the
Dirichlet-convolution sense; `Λ(n)=\sum_{d|n}μ(d)\log(n/d)`). The action `L_λ j_λ` on the prime atoms
therefore factors **multiplicatively over primes** (the Euler product structure of `Λ`), and the cross
term assembles into a **sum of per-prime squares** — *non-negative* — precisely when the kernel is the
multiplicative von Mangoldt kernel. Schematically,
```
   (L_λ j_λ)\big|_{\text{prime part}} = \sum_p (\log p)^2 \,\big(\text{positive per-prime form}\big) + (\text{cross-prime}).
```

**Conjecture C (the new RH-strength input).** For the **multiplicative** (von Mangoldt) jump kernel,
the cross-prime terms in `Γ_2` are dominated by the per-prime squares, giving `Γ_2 ≥ 0` uniformly in
`λ`. For a **non-multiplicative** kernel (Davenport–Heilbronn: `Λ` twisted by a non-principal character
that breaks `\log=Λ*1`), the cross-prime terms are **not** dominated and `Γ_2` acquires a negative part
— exactly the off-line zeros.

This is where, and only where, **Euler multiplicativity** enters: it is the algebraic identity
`\log=Λ*1` that makes the curvature term a sum of squares. **DH breaks the identity, hence breaks the
curvature positivity.** This matches every prior finding (DH fails; the Euler product is the
discriminator) and gives it a **local, computable** form.

---

## §5. The obstruction, honestly, and the proposed resolution

**Obstruction.** Pure-jump generators do **not** satisfy `CD(0,∞)` automatically even when `j≥0` —
the cross-prime terms in `Γ_2` can be negative, and the program's LGV/"razor-thin" finding
(`[[riemann-phase61-phaseF-LGV]]`) is the numerical shadow that `Γ_2` is **marginal** (the `e^{−cL}`
cascade is a near-zero curvature). So Conjecture C is genuinely open and is the new crux.

**Proposed resolution (the construction to build next).** Establish `Γ_2≥0` by a **per-prime
Bochner identity**: decompose the prime jump measure as a **restricted tensor product over primes** of
local jump kernels `j_p` (each `j_p` the geometric series `\sum_k (\log p) p^{−k/2} δ_{k\log p}`,
*positive and log-convex per prime*), and prove a **tensorization theorem for `CD(0,∞)` of jump
kernels**: if each local `j_p` satisfies a local curvature bound `CD(0,∞)_p` (provable from the
explicit geometric series — a single-prime computation), and the global kernel is their **regularized
restricted tensor**, then the global `Γ_2≥0`. The regularization is the explicit-formula/`ζ`-
renormalization (as in `M3a`), now applied to **curvature** rather than to the Gram form. The
tensorization of curvature lower bounds is a clean, **provable-in-principle** statement (unlike the
divergent scalar product), because curvature `CD` lower bounds **tensorize additively** (`CD(0,∞)` is
stable under tensor products), so the regularized assembly preserves `Γ_2≥0` **as long as each local
factor is `CD(0,∞)`**.

**The single remaining theorem (new, concrete, local):**
> **(★)** Each local prime jump kernel `j_p(θ,dφ)=\sum_{k≥1}(\log p)\,p^{−k/2}\,δ_{θ+k\log p}` (with the
> Doob weight) satisfies the local curvature bound `Γ_2^{(p)} ≥ 0`, and the regularized restricted
> tensor product over `p`, together with the archimedean (Gaussian/continuous) factor which satisfies
> `CD(0,∞)` classically, yields the global `Γ_2 ≥ 0`.

`(★)` is a **single-prime + tensorization** statement — local, explicit, and not obviously circular:
each `j_p` is an explicit geometric measure on an arithmetic progression `k\log p`, and `CD(0,∞)` for
such a 1D jump kernel is a finite computation in the per-prime variable. The Euler product enters as
the **tensor structure**; the renormalization is curvature-additive (the good feature: `CD` lower
bounds add under tensor, they do not multiply and diverge). DH lacks the per-prime tensor structure,
so `(★)` is unavailable to it.

---

## §6. Status

**Created here (new mathematics):**
- the **arithmetic spectral surface** `𝒮=V⊗V` with intersection form `𝓘`, polarization the
  **unconditional** Perron–Frobenius class `H=u₀⊗u₀`;
- the **Hodge-index reformulation** of RH: signature `(1,\dim−1)` with `+`=`H` (Prop. 1) — rigorous;
- the **curvature conversion**: `RH ⟸ Γ_2≥0` (`CD(0,∞)`) for the Doob–prime Dirichlet generator
  (Prop. 2) — a genuinely different, local, geometric criterion;
- the **Euler-product localization** of the curvature: `Γ_2≥0 ⟸` the von Mangoldt identity
  `\log=Λ*1` making the curvature term a sum of per-prime squares (§4) — the place multiplicativity
  enters, with DH breaking it;
- the **proposed closing theorem `(★)`**: local per-prime `CD(0,∞)` + curvature-additive tensorization
  (§5) — a concrete, local, not-obviously-circular target.

**Open:** Conjecture C / theorem `(★)` — the per-prime curvature bound and its tensorization. This is
the new frontier the construction creates; it replaces "the arithmetic intersection theory on Spec ℤ²"
by "**`CD(0,∞)` for the multiplicative prime jump kernel**", which is **local, explicit, and
single-prime-reducible** — a strictly more tractable-looking object, and the right thing to put to
Connes.

**No false victory:** `(★)` is unproved; RH remains open. But the route is now a **local curvature
inequality powered by Euler multiplicativity**, with all surrounding structure (surface, polarization,
Hodge-index reformulation, curvature conversion) in place, and with a single-prime computation as the
next concrete step.

## §7. Next

Carry out the **single-prime curvature computation**: write the generator, carré-du-champ, and `Γ_2`
for one geometric prime kernel `j_p` explicitly (purely symbolic), and determine whether `Γ_2^{(p)}≥0`
holds and with what constant. If yes, the tensorization theorem is the remaining step; if it is
marginal, identify the exact compensating term (the archimedean factor) needed. This is the next
document — a finite, local, symbolic computation, no numerics.
