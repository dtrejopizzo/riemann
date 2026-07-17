# The sign `ε₀≥0` as a Schrödinger bound-state problem: the pole as barrier, the curvature as well-control, and the Bargmann criterion

*Pure mathematics. We attack the one irreducible quantity — the sign `ε₀(λ)≥0` (Weil positivity) —
with a new tool: realize `ε₀(λ)` as the **ground-state energy of a Schrödinger operator** on the
window, in which the **pole of ζ acts as a repulsive barrier** and Theorem 2's curvature controls the
shape of the **prime well**. Positivity then becomes a **Bargmann-type bound-state criterion**, where
the pole's barrier is exactly what keeps the Bargmann integral below threshold — and which DH (being
entire, pole-free) lacks. We set it up rigorously, state the criterion, and isolate the one remaining
estimate. Honest: RH not proved; the uniform Bargmann bound is the crux.*

---

## §1. The Schrödinger realization of `ε₀`

After Doob conjugation by `u₀>0` and the 2.3.F reduction, the Weil form on the window `[0,L]` is, in
the geometric coordinate `θ=πy/L∈[0,π]`, a **Schrödinger operator with Dirichlet boundary conditions**:
```
   H_λ = −\frac{d^2}{dθ^2} + W_λ(θ)   on  L²([0,π]),  Dirichlet,   ε₀(λ) = \inf\mathrm{spec}\,H_λ,
```
where the kinetic part `−d²/dθ²` is the `(k+1)²` Dirichlet Laplacian (Theorem 2.3.F, with first
eigenvalue `1>0`), and the **effective potential** `W_λ` is the explicit-formula remainder
```
   W_λ(θ) = W_λ^{\mathrm{pole}}(θ) + W_λ^{\mathrm{arch}}(θ) − W_λ^{\mathrm{prime}}(θ),
```
the pole/archimedean parts smooth, the prime part carrying the von Mangoldt data (Doob-weighted).

**`ε₀≥0` ⟺ `H_λ⪰0` ⟺ `H_λ` has no eigenvalue below `0`** — a **bound-state absence** statement. The
kinetic gap (Dirichlet) already gives `−d²/dθ²≥1`; a negative eigenvalue can appear only if the well
`W_λ^{-}` (negative part of `W_λ`) is deep/wide enough to bind a state below `0` against this gap.

This is the *non-Doob-invariant* picture: `H_λ` includes the absolute shift `ε₀`, and `W_λ^{pole}`
sets the absolute scale — exactly the structure the curvature/de Branges apparatus was blind to.

---

## §2. The pole is a repulsive barrier (and DH has none)

The pole of `ζ` at `s=1` contributes to the explicit formula the term `+(\hat h(0)+\hat h(1))`, which
in the window realization is a **positive rank-one (or rank-two) form**: a strictly positive,
smooth, `λ`-stable bump
```
   W_λ^{\mathrm{pole}}(θ) = +\,p_λ(θ),   p_λ ≥ 0,   ∫_0^π p_λ\,dθ = π_{\mathrm{res}} > 0
```
(`π_{res}` the residue normalization). It **raises** the potential — a **repulsive barrier**. By
contrast the prime part is a **well** (it lowers the potential where primes cluster). The competition
`barrier − well` is the sign of `ε₀`.

**DH:** the Davenport–Heilbronn function is **entire** — `\hat h(0)+\hat h(1)` has **no pole residue**,
so `W^{\mathrm{pole}}_{\mathrm{DH}}=0`: **no barrier.** Its well is unopposed, binds a negative state,
`ε₀^{\mathrm{DH}}<0`. This is the cleanest possible statement of why the falsifier is non-positive:
*it lacks the repulsive barrier that the pole provides.* (Matches `[[riemann-phase61-euler-mechanism]]`:
positivity requires the pole; remove it and `μ₀` drops to `−10.7`.)

---

## §3. The Bargmann criterion (the tool)

**Theorem (Bargmann/Calogero–Cohn, classical).** For `H=−d²/dθ²+W` on `[0,π]` with Dirichlet
conditions, a sufficient condition for `H⪰0` (no negative eigenvalue) is
```
   \int_0^π \mathcal G(θ)\,W^{-}(θ)\,dθ \;\le\; 1 ,
```
where `W^-=\max(−W,0)` is the well depth and `\mathcal G(θ)=\frac{θ(π−θ)}{π}` is (a multiple of) the
Dirichlet Green's function weight; more sharply, `H⪰0` iff the Birman–Schwinger operator
`K_λ = \mathcal G^{1/2}\,W^{-}\,\mathcal G^{1/2}` (with `\mathcal G` the Dirichlet Green's function of
`−d²/dθ²`) has operator norm `\le 1`.

**Reformulation of RH (rigorous).**
```
   ε₀(λ)≥0  ⟺  \|K_λ\|\le 1,    K_λ = G_{\mathrm{Dir}}^{1/2}\,W_λ^{-}\,G_{\mathrm{Dir}}^{1/2}.
```
This is the same `\|K\|\le1`/`μ_max\le1` boundary we met in E96/E101 — now with the **explicit
positive kernel `G_{\mathrm{Dir}}`** (Connes' Hardy/positive reference, §3 of `M3-arithmetic-index`),
and the **well `W_λ^- =` (prime well `−` pole barrier)`^-`**. The pole barrier **subtracts from the
well before taking the negative part**, so it directly lowers `\|K_λ\|`.

---

## §4. Where the inputs combine

We now have all three program ingredients meeting in one inequality `\|K_λ\|\le1`:

1. **Kinetic gap (2.3.F):** `−d²/dθ²≥1` (Dirichlet) — the `G_{\mathrm{Dir}}` is bounded, `\|G\|=` the
   inverse gap, finite and `λ`-stable. *(Shape, unconditional.)*
2. **Curvature (Theorem 2, this arc):** the prime well `W^{\mathrm{prime}}` is the kernel of a
   `CD(0,∞)` Dirichlet generator — so it is **nonneg-curved**, hence cannot oscillate to arbitrarily
   deep narrow spikes: its Birman–Schwinger contribution is **controlled by `Γ` (the carré-du-champ)**,
   `\|G^{1/2}W^{\mathrm{prime}}G^{1/2}\| \le C·(\text{total mass of the jump measure})` with `C` from
   the curvature bound. *(Shape of the well, unconditional, from `Λ≥0`.)*
3. **Pole barrier (this document):** `W^{\mathrm{pole}}=+p_λ≥0` subtracts from the well, reducing
   `W^-` and hence `\|K_λ\|`. *(Scale/sign, the non-Doob-invariant input; DH lacks it.)*

**The remaining estimate (the crux), stated precisely:**
> **(♦)** `\big\|\,G_{\mathrm{Dir}}^{1/2}\,(W^{\mathrm{prime}}_λ − p_λ)^{-}\,G_{\mathrm{Dir}}^{1/2}\,\big\| \le 1`
> uniformly in `λ`, where `p_λ≥0` is the pole barrier (mass `π_{res}`), `W^{\mathrm{prime}}_λ` is the
> `CD(0,∞)` von Mangoldt well, and `G_{\mathrm{Dir}}` is the Dirichlet Green's function (gap `1`).

`(♦)` is `ε₀≥0` = RH. Its three inputs are now **separated and individually controlled**: the gap and
the well-shape are unconditional (2.3.F + Theorem 2), and the barrier is the pole. The estimate is a
**quantitative comparison** of the von Mangoldt Birman–Schwinger operator against the pole barrier in
the Dirichlet metric. **DH fails `(♦)`** because `p_λ=0` (no pole) leaves `\|G^{1/2}W^{prime-}G^{1/2}\|>1`.

---

## §5. Why this is genuinely a new handle (and the honest gap)

**New:** `ε₀≥0` is realized as **absence of a Schrödinger bound state**, with
- the **pole as an explicit repulsive barrier** (its absence in DH is the cleanest non-positivity
  proof),
- the **prime well curvature-controlled** by Theorem 2 (`CD(0,∞)` ⟹ the well's Birman–Schwinger norm
  is bounded by the jump mass, no pathological deep spikes),
- the **kinetic gap** from 2.3.F giving a finite, stable Green's function.

This converts the marginal `μ_max=1` into a **Birman–Schwinger norm bound `\|K_λ\|≤1`** with a *named
positive barrier* (`p_λ`) on the well — a concrete inequality with classical tools (Bargmann,
Birman–Schwinger, Lieb–Thirring) on the table, rather than an abstract positivity.

**Honest gap:** `(♦)` is still `ε₀≥0`, hence RH; it is marginal (`\|K_λ\|=1` at the edge, E96/E101). The
classical Bargmann bound `∫\mathcal G W^-≤1` is **sufficient but not tight** at marginality, so a naive
application will not close the razor's edge — one needs the **sharp Birman–Schwinger eigenvalue**, not
the trace bound. The crux is therefore: **show the top Birman–Schwinger eigenvalue of the
pole-barriered von Mangoldt well equals exactly `1` (not `>1`) uniformly in `λ`.** That equality is the
marginal Weil positivity; the pole forces it down to `1`, the curvature keeps it from exceeding `1`,
and proving the *exact* marginal value is the last step.

---

## §6. The proposed path to `(♦)`

A Lieb–Thirring / Birman–Schwinger **sum rule** seems the right vehicle: the number of negative
eigenvalues `N_-(H_λ)` of `H_λ=−d²/dθ²+W_λ` satisfies
```
   N_-(H_λ) ≤ \mathrm{Tr}\,(K_λ)\;=\;\int_0^π \mathcal G(θ)\,W_λ^{-}(θ)\,dθ ,
```
and `ε₀≥0 ⟺ N_-=0`. Propose to show `\mathrm{Tr}(K_λ)<1` **for the pole-barriered well**, using:
- **Theorem 2** to write `W^{\mathrm{prime}}` as a sum of per-prime positive pieces (the curvature
  decomposition `B=Σ_p c_p[\dots]`), giving `\mathrm{Tr}(K_λ^{\mathrm{prime}}) = Σ_p (\log p)·(\dots)`
  — a **prime sum with positive terms**, evaluable;
- the **pole barrier** `p_λ` to subtract a fixed positive mass `π_{res}·\mathcal G`-weighted, lowering
  the trace below `1`;
- **PNT** to evaluate the smooth part of the prime sum and the archimedean part.

The resulting inequality is `Σ_p(\text{prime trace}) − (\text{pole mass}) < 1`, a **concrete
prime-vs-pole trace comparison**, with the curvature guaranteeing the prime trace converges (no deep
spikes) and the pole supplying the subtraction. **This is the next computation**: assemble
`\mathrm{Tr}(K_λ)` from the per-prime curvature pieces and the pole, and test the `<1` comparison
analytically (PNT-level), with DH (no pole) giving `>1`.

**Status:** `(♦)`/the trace comparison is the single remaining inequality; all its ingredients (kinetic
gap, curvature decomposition, pole barrier, PNT) are in hand or classical. It is `ε₀≥0`, hence RH, and
marginal — but now in the form of a **Birman–Schwinger trace comparison with an explicit pole
subtraction**, the sharpest and most classical-tool-ready form the wall has taken. *Open; proposed.*

---

## §7. Correction and the sharp threshold-resonance statement

**Self-correction.** The trace bound `Tr(K_λ)<1` of §6 is **too strong and the wrong tool at
marginality.** Always `Tr(K_λ) ≥ \|K_λ\|`, and at the razor's edge `\|K_λ\|=1` (E96/E101) while
`Tr(K_λ)>1` (the Birman–Schwinger operator has *many* eigenvalues, the top one at `1` and a tail
below). So a Lieb–Thirring/trace inequality cannot detect the marginal case — it is lossy by exactly
the amount that matters. The correct object is the **top Birman–Schwinger eigenvalue**, via the
Birman–Schwinger *principle*, not its trace.

**Birman–Schwinger principle (sharp).** `H_λ=−d²/dθ²+W_λ` has a zero-energy eigenstate (`ε₀=0`) iff the
Birman–Schwinger operator `K_λ(0)=G_{\mathrm{Dir}}^{1/2}\,W_λ^{-}\,G_{\mathrm{Dir}}^{1/2}` has **`1` as
an eigenvalue**, with eigenvector the **zero-energy resonance**; `ε₀<0` iff `K_λ(0)` has an eigenvalue
`>1`. Hence
```
   ε₀(λ) ≥ 0  ⟺  \|K_λ(0)\| ≤ 1  ⟺  1 is the TOP eigenvalue of K_λ(0)  (no eigenvalue exceeds 1).
```

**The Perron–Frobenius ground state is the threshold resonance.** The unconditional `u₀>0`
(Theorem 2.2) is precisely the eigenvector of `K_λ(0)` at eigenvalue `1` (it minimizes the Weil
quotient; at the margin `ε₀=0` it is the zero-energy resonance). The pole barrier `p_λ` is what **pins
this eigenvalue at exactly `1`** (remove the pole — DH — and the top eigenvalue jumps above `1`,
binding a negative state). So:

> **(♦′) Sharp form.** `RH ⟺` the **positive** Perron–Frobenius resonance `u₀` is the **top**
> eigenvector of the pole-barriered von Mangoldt Birman–Schwinger operator `K_λ(0)` — i.e. **no other
> mode out-couples `u₀` to the well.** The pole fixes `λ_{\mathrm{top}}(u₀)=1`; Theorem 2's curvature
> (`CD(0,∞)`, the well is nonneg-curved, no deep narrow spikes) is exactly what **prevents a
> non-ground mode from exceeding `1`** by forbidding the localized deep wells that would bind an excited
> negative state.

**Why this is the right final form.** It is a **single, sharp, Perron–Frobenius statement**: a positive
function is the top eigenvector of a positive operator. For an operator with a **positivity-improving**
(Perron–Frobenius) structure, the top eigenvector is automatically the unique positive one — *which is
exactly `u₀`.* So the content reduces to: **is `K_λ(0)` positivity-improving?** If the pole-barriered
von Mangoldt Birman–Schwinger kernel `G^{1/2}(W^{prime}−p_λ)^- G^{1/2}` is a **positivity-improving
kernel** (positive matrix entries, irreducible), then by Perron–Frobenius its top eigenvector is the
positive `u₀`, its top eigenvalue is `1` (pinned by the pole), and **`ε₀≥0` follows — RH.**

**The last inequality, restated:**
> **(♦″)** The Dirichlet-Green-dressed, pole-barriered von Mangoldt well
> `\mathcal K_λ := G_{\mathrm{Dir}}^{1/2}\,(W^{\mathrm{prime}}_λ − p_λ)^{-}\,G_{\mathrm{Dir}}^{1/2}`
> is **positivity-improving with spectral radius `1`** uniformly in `λ`.

Positivity-improving (entrywise-positive kernel) is a **structural** property — checkable from the
sign of the kernel, not from the zeros — and is exactly the kind of statement the curvature/`Λ≥0`
positivity (Theorem 2) and the positive Green's function `G_{\mathrm{Dir}}≥0` should supply, **with the
pole subtraction `−p_λ` the only delicate point** (it could create negative kernel entries where the
barrier exceeds the well). DH: no `p_λ`, spectral radius `>1`.

**This is the genuine final target:** a **Perron–Frobenius/positivity-improving** statement for an
explicit kernel — structural, sign-based, curvature-supported, with the pole as the one subtraction.
It is `ε₀≥0` = RH, now in the most classical-operator-theoretic and least circular-looking form the
program has reached: *a positive kernel with a positive top eigenvector and a pole-pinned spectral
radius `1`.* The crux is whether the pole subtraction preserves positivity-improvement (the delicate
sign of `(W^{prime}−p_λ)^-` near the pole). *Open; proposed; the next computation is the sign analysis
of `(W^{prime}_λ − p_λ)` — does the barrier ever over-subtract?*
