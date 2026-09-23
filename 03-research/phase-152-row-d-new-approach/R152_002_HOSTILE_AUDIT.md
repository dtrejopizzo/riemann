# R152.002 — Hostile audit, phase 152 round 0

*Auditor: Opus 5 (hostile), 2026-09-19. Target: `R152_001_FEASIBILITY.md` (457 lines) against
`R152_000_LEAD_BLUEPRINT.md`. Mandate: attempt to REVIVE both mechanisms and check the kill proofs.
**No sign is claimed. Row D keeps no label.** Nothing below is a zero-free region, a moment bound or a
cancellation estimate; the (P152.x) items are conditional statements with gates, not results.*

---

## §0 Verdicts

| item | builder's claim | audit verdict |
|---|---|---|
| Prop. A.2 (`R152_001`:115–124) | `~log T` density kills BD-type gap | **CORRECT BUT NON-BINDING.** The proposition is true as stated; it refutes only `β > ¼`, which is not the mechanism's target. **Death not established by this clause.** |
| Q1 hypothesis failures (`:126–140`) | FUP degenerates at `δ=1` | **SUSTAINED** as "no machinery", not as impossibility. |
| Q2 (`:146–168`) | none known | **SUSTAINED**, with the structural reason correctly identified (any such constraint *is* a zero-free region). |
| Q3 (`:170–194`) | "empty for `Re ρ`, circular" | **ASSERTED, NOT PROVED.** Item (ii) is `the builder finds no route`. **DEATH NOT ESTABLISHED** (undecided, not revived). |
| Prop. A.4 + Cor. A.5 (`:200–214`) | structural obstruction | **A.4 CORRECT; A.5 OVERREACHES.** Kills the *naive* Dolgopyat argument only. **DEATH NOT ESTABLISHED**; see (P152.1). |
| Mechanism A overall | DEAD for the sign | **DEATH NOT ESTABLISHED.** Correct verdict: *no known machinery, no proof of impossibility.* |
| "phase 16 already covers this" (`:40`, `:52`) | Route A = this picture | **PARTLY FALSE.** Different object; see §3. |
| Prop. B.2 (`:284–296`) | tree energy is `f`-independent | **TRUE BUT VACUOUS** (it computes the energy of one fixed measure; no one proposed that as the form). |
| Prop. B.3 (`:303–318`) | meet vs difference | **CORRECT FOR `M(Z)`, SCOPE-LIMITED.** Does not answer the blueprint's own Q5, which also names `A^{1,an}_Z`. **DEATH NOT ESTABLISHED** for Q5 as posed; see (P152.2). |
| Q6 "no Frobenius via Thm 22.17" (`:332–336`) | ring-level reason | **CATEGORY ERROR** at the stated level. Conclusion plausible, argument invalid; see (P152.3). |
| Mechanism B overall | DEAD as a route | **DEATH NOT ESTABLISHED** as stated; **sustained for the tree `M(Z)` alone.** |

No mechanism is REVIVED with a proof. Three (P152.x) are formulated below; none is a restatement of RH,
each is a statement about an object the corpus has never constructed.

---

## §1 Mechanism A

### 1.1 Prop. A.2 — the comparison is against a strawman

The proposition (`R152_001`:115–124) is arithmetically correct: Riemann–von Mangoldt gives `≍ log T`
resonances per unit window on `Re s = ¼`, so `{Re s > ½ − β}` with `β > ¼` contains infinitely many, and
Bourgain–Dyatlov's "finitely many exceptions" clause cannot absorb them. The auditor confirms both the
count and the exception clause: BD is `#{resonances in Re s > ½ − β} < ∞`, so infinitude is fatal to
`β > ¼`. **But no one wants `β > ¼`.** The gap in BD is measured from the unitary axis `½` for a surface
whose resonance line is *`Re s = δ`-governed*; the modular surface's Eisenstein resonance line is
`Re s = ¼`, at distance exactly `¼`. Therefore:

* `β > ¼`: false (Prop. A.2), and uninteresting.
* `β = ¼` with finitely many exceptions: **equivalent to "all but finitely many `ρ` on the critical
  line"**, i.e. the substance of RH.
* `β < ¼`: **strictly weaker than RH and not known** — it is a zero-free strip `Re ρ > 1 − 2β'`, hence
  a quasi-RH; anything with `β > 0` uniform already beats de la Vallée Poussin, whose depth is
  `O(1/\log γ)` and not uniform.

So Prop. A.2 does not fire the (Q1) clause of kill criterion A in the sense the criterion needs. What
*does* fire is the auditor's own restatement: **the BD threshold is placed at the boundary value, so the
mechanism is not over-asking; it is asking exactly for RH (at `β = ¼`) or for a quasi-RH (at `β < ¼`).**
That is a reason the mechanism cannot be *easy*; it is not a reason it is dead. The builder's §A.5 should
not have counted (Q1) as satisfied on the strength of A.2. The *other* Q1 content (the three hypothesis
failures, `:126–140`: `δ = 1` non-porosity, cusp vs funnel, `P(½) > 0`) is sustained and is the real
content: **no FUP-type theorem exists for cusped finite-area surfaces, and every known exponent `β(δ)`
degenerates as `δ ↑ 1`.** That is "no machinery", which is the honest verdict.

**Audit verdict A.2: CORRECT BUT NON-BINDING. Death not established by this clause.**

### 1.2 Prop. A.4 / Cor. A.5 — the abscissa is right, the impossibility claim is not

Prop. A.4 (`:200–212`) is correct and is the round's best piece: the branch series
`Σ_{n≥1}(n+z)^{−2s}h(1/(n+z))` converges on the disc iff `Re s > ½`, because `|T'|^{−1} ≍ n^{−2}`. The
identification with the Euler-product abscissa under `w = 2s` is correct and worth keeping.

Cor. A.5 (`:212–214`) then claims: on `Re s ∈ (¼,½)` "none of these objects exists", so "the UNI
hypothesis cannot even be stated". **This is too strong, in three places.**

1. **The operator exists.** Mayer and Lewis–Zagier continue `s ↦ L_s` meromorphically to all of `C` as a
   holomorphic family of **nuclear operators of order 0** on the disc Banach space `A_∞(D)`
   (`CERTIFIED`; the builder marks the same facts `CERTIFIED` at `:100–108`). Hence `L_s^n`, `Tr L_s^n`,
   `det(1 − L_s)` and the operator norms `‖L_{σ+it}^n‖` are all defined and holomorphic on
   `¼ < σ < ½`. A statement "`‖L_{σ+it}^n‖ ≤ C|t|^ε θ^n` uniformly on that strip" is **well-posed**.
   What fails is not well-posedness but the *proof technique*: no positive cone, no Ruelle–Perron–
   Frobenius leading eigenvalue, no `n`-cylinder decomposition of `L_s^n`.
2. **No theorem can establish the impossibility the corollary asserts.** If RH holds, then
   `det(1−L_s)det(1+L_s) = Z_{Selberg}(s)` has no Eisenstein zeros off `Re s = ¼`, and consequently
   *some* uniform bound of Dolgopyat shape holds on `¼ < σ < ½ − ε` for trivial reasons. So "no
   Dolgopyat-type estimate can hold there" is not a provable statement — it would disprove RH. The
   correct formulation is **"no known method produces one"**, which is a statement about the literature,
   not about the operator.
3. **UNI is a property of the map, not of the parameter.** Uniform non-integrability of the temporal
   distance function of the Gauss map is a statement about the continued-fraction map's periodic orbits
   and holds or fails independently of `s`. The obstruction is that the *conclusion* of Dolgopyat's
   argument is proved by dominating branch sums, and those diverge; it is not that the hypothesis is
   unstateable. The builder's own sentence "the failure is not a failure of the UNI hypothesis" is
   correct; the next clause ("cannot even be stated") contradicts it.

**Audit verdict A.4: PROOF CORRECT. Cor. A.5: DEATH NOT ESTABLISHED** — what is established is that the
*branch-sum* route is unavailable below `Re s = ½`, which the auditor accepts and which is a genuine and
new statement of this round.

**Is there a Dolgopyat/UNI formulation on the continued operator?** The auditor knows of none in the
literature and does not assert one exists. The only structure available on `¼ < σ < ½` that is not a
branch sum is the **Lewis–Zagier three-term functional equation**
`ψ(x) = ψ(x+1) + (x+1)^{−2s}ψ(x/(x+1))`, whose solutions (period functions) are in bijection with the
zeros of `det(1∓L_s)`; this equation is an identity, valid by continuation, with no convergence
condition. That is the only candidate substrate, and it yields:

> **(P152.1) — period-function cancellation.** Let `¼ < σ₀ < ½`. Does there exist a family of
> finite-rank operators `A_N(s)` on `A_∞(D)`, defined from the Lewis–Zagier three-term equation (not
> from the branch sum), with `det(1 − A_N(s)) → det(1 − L_s)` uniformly on compacts of
> `{σ₀ < Re s < ½}`, and constants `C, ε > 0, θ < 1` with `‖A_N(σ+it)^n‖ ≤ C|t|^ε θ^n` uniformly for
> `σ ∈ [σ₀,½)`, `|t| ≥ 1`?
>
> *Consequence if true:* `det(1 − L_s) ≠ 0` on `σ₀ < Re s < ½` for `|t|` large, i.e. a zero-free strip
> `Re ρ > 1 − 2σ₀` for `ζ` up to finitely many zeros; at `σ₀ = ¼`, RH.
>
> *Gates.* **(g1) `Ξ_a`:** no transfer operator of a finite-index continued-fraction system has `Ξ_a` as
> Fredholm determinant, so (P152.1) does not trivially generalize — but the gate is *unchecked*, because
> what would have to be exhibited is the class of maps whose Mayer determinant is `Ξ_a`; the auditor
> cannot exhibit it and does not claim the gate passes. **(g2) `Ξ_Q`:** Epstein-type combinations with
> off-line zeros must be shown not to arise as Mayer determinants of any such system; unchecked.
> **(g3) archimedean:** the `Γ`-factor must enter (P152.1); in Mayer's identity it enters through
> `Z_{Selberg}`, i.e. by hand, which is the corpus's standing objection to Hilbert–Pólya realizations.
>
> *Status:* **OPEN, UNBUILT, and failing gate (g3) as stated.** (P152.1) is recorded as the precise
> content of "mechanism A is not dead, only unarmed"; the auditor does **not** recommend building it.

### 1.3 Q3 — proved or asserted?

**Asserted.** `R152_001`:184–190, item (ii), reads in full: "*None.* … The builder finds no route from
(i) to `σ = ¼`". That is a search report, not a proof; it is correctly labelled `ARGUED` in the §6 table
(`:421`). Item (i) (non-`L²`, truncation-dependent normalization) is a genuine and correct obstruction:
the Maass–Selberg norm `T^{2σ−1}/(2σ−1)` depends on the unknown `σ`, so the non-concentration statement
is *conditionally* formulable only. Item (iii) (Luo–Sarnak circular) is `CERTIFIED` and the auditor
concurs in substance: Luo–Sarnak's QUE for `E(·,½+it)` is on the line and uses `ζ(1+2it)` lower bounds.

But "circular in its only proved instance" does not make the *statement* circular: Hecke recurrence
(`T_p E(·,s) = (p^{s−½}+p^{½−s})E(·,s)`) is an identity valid for all `s`, and the Bourgain–Lindenstrauss
entropy machine is an argument about measures, not about `L²` membership. The honest verdict is that the
analogue is **undecided**, not empty. The auditor's objection to reviving it is different from the
builder's and is decisive in practice: the Hecke eigenvalue `p^{σ−½+iτ} + p^{½−σ−iτ}` is, for `σ ≠ ½`,
**unbounded in `p`**, so the Hecke operators are not uniformly bounded on the relevant states and every
known entropy bound (which needs `|λ_p| ≤ 2p^{...}` uniformly, i.e. temperedness) loses its input exactly
when `σ ≠ ½` — the case one wants to exclude. This is an `Ξ_a`-shaped failure: the mechanism reads
**magnitude** and the off-line hypothesis is what destroys its hypothesis.

**Audit verdict Q3: DEATH NOT ESTABLISHED (the builder's clause is asserted); mechanism nonetheless not
revivable by the auditor, for the stated non-temperedness reason, which is recorded as new.**

---

## §3 The phase-16 "Route A already covers it" claim — PARTLY FALSE

Verified in `03-research/phase-16/`, docs 01–07.

* **Doc 01** (`01-pillar1-triage-three-routes.md`:26–45): Route A = `GL₂`/Eisenstein; establishes
  `φ(s) = ξ(2s−1)/ξ(2s)`, resonances at `s = ρ/2`, **verified numerically**; Pillar 1 **PARTIAL**.
  This is the same *dictionary* as `R152_001` (A.0.1). **Overlap confirmed here, and only here.**
* **Doc 05** (`05-resonance-pairing-definite-THEOREM.md`:11–33): the theorem is about the **Gram matrix**
  `K_{ρσ} = 1/(s_ρ + \overline{s_σ} − 1)` of resonance states, shown negative-definite for *every*
  configuration of zeros via `K_{ρσ} = −1/(w_ρ + \overline{w_σ})`, `w_ρ = ½ − s_ρ`, `Re w_ρ =
  (1−β_ρ)/2 > 0` — the Cauchy/Hardy reproducing kernel of the right half-plane. The proof is **correct**
  and its hypothesis is only `β_ρ < 1`. Its conclusion: no resonance/scattering **pairing** on the
  modular surface can equal the Weil form `Q`; `κ` is structurally absent (doc 05:39–45; doc 04
  `04-MSZ-pairing-hits-CAP.md`:1–7, 61–73).
* **Docs 02, 03, 06, 07**: Pillar-2 prototype, non-triviality of the residue weights, the hunt for an
  indefinite object, Pontryagin spaces. All of it is **positivity/signature** work.

**Therefore:** phase 16 proves that Route A cannot supply the *indefinite pairing*. Mechanism A of
phase 152 is **not a pairing mechanism** — it asks for a resonance-free strip by dynamical/microlocal
cancellation, with no bilinear form anywhere. The two are the same *surface* and the same *dictionary*
(`s = ρ/2`), and nothing more. `R152_001`:40 ("Not new: phase 16 is the corpus's Route A") and `:52`
("Phase 16 already contains Route A in full") are **overstated**: phase 16 contains Route A's Pillar 1
and Pillar 2, not its resonance-gap question, which is genuinely new to the corpus. This does not change
the verdict on mechanism A (the death is not established either way), but it is a mislabelling of the
corpus record and should be corrected in `R152_001` §1 and §7.

---

## §4 Mechanism B

### 4.1 Prop. B.2 — true and vacuous

`E(μ) = Σ_p (log p)³ Σ_{k,l} p^{−(k+l)/2}\min(k,l)` with the closed form `t²/((1−t)²(1−t²))`,
`t = p^{−1/2}`, and divergence `≍ Σ_p (log p)³/p`: the computation is **correct** (auditor re-derived it).
But it proves only that *one fixed measure* has a constant energy — which is true of any fixed measure
under any fixed pairing, and is not a refutation of anything anyone proposed. The mechanism would pair
`μ_f` against `μ_f` with `f`-dependent measures. Prop. B.2 should be demoted to a remark. It carries no
weight in kill criterion B.

### 4.2 Prop. B.3 — correct, and scope-limited

The proposition (`:303–318`) is **correct as stated and correctly proved**: a pairing
`⟨μ,ν⟩_κ = ∬ κ(x∧y)dμdν` is a function of the meet; on `M(Z)`, cross-prime meets are all the root, so
the pairing is constant `κ(0)` on every cross-prime pair, whereas `K(k\log p − l\log q)` varies. The
observation that tree metrics are of negative type, so every such energy is *unconditionally* positive
semidefinite on mass-zero measures (`:324–329`), is correct and is a second, independent reason: an
unconditionally nonnegative output cannot separate `ζ` from `Ξ_a`. Both points sustained.

**What it does not do.** It refutes the *tree* `M(Z)` only. The blueprint's Q5 (`R152_000`:67–72)
explicitly names two other objects, and `R152_001` answers for neither:

1. **`A^{1,an}_Z`, Poineau's Berkovich line over `Z`.** This is **not** a tree: it fibres over `M(Z)`
   with, over the archimedean point `|·|_∞^ε`, a fibre that is the ordinary complex line
   `C/{z ↦ \bar z}` (an archimedean, 2-real-dimensional fibre), and over each `p`-branch point a
   Berkovich `p`-adic line. **A translation structure exists**: `A^{1,an}_Z` is a group object
   (the additive group `G_a^{an}` over `Z`), so difference kernels `k(x − y)` are *defined* on each
   fibre, and the hypothesis of Prop. B.3 — that the pairing is a function of the meet — **fails**.
   Prop. B.3 therefore does not apply to the object the blueprint actually named.
2. **A global analytic space with a non-trivial archimedean fibre.** Same remark; the whole point of
   Lemanissier–Poineau is that the archimedean place is not collapsed to a branch.

This is the audit's main finding on B. The builder's conclusion may still be right — the auditor's own
expectation is that the difference structure on the archimedean fibre is just `C` with its usual
translation, so that "the Weil form is a difference kernel on the archimedean fibre" is the explicit
formula written twice — but that has not been checked, and the kill criterion was declared fired on a
proposition whose hypothesis the named object does not satisfy.

> **(P152.2) — archimedean-fibre pairing on `A^{1,an}_Z`.** Is there a linear map `f ↦ μ_f` from test
> functions to (signed) measures on `A^{1,an}_Z`, supported on the union of the integer points
> `\{(p, k\log p)\}` of the non-archimedean fibres and of the archimedean fibre, and a kernel `g` which
> is a **difference** kernel along the archimedean fibre and a **meet** kernel across branches, such
> that `W(f * \tilde f) = ∬ g\,dμ_f\,d\overline{μ_f}` and such that the Laplacian of `g` on
> `A^{1,an}_Z` (Thuillier / Chambert-Loir–Ducros, if it can be defined over `Z` at all) is a divisor
> supported on the integer points?
>
> *Consequence if true:* the Weil positivity `W(f*\tilde f) ≥ 0` would become a statement about the
> sign of a Laplacian energy on a space where the archimedean place is a fibre rather than a branch,
> i.e. the first object in the corpus where the cross-place coupling is not collapsed to a root.
>
> *Gates.* **(g1) `Ξ_a`:** the construction must use the weights `p^{−k/2}`, i.e. the unimodularity of
> the local roots, in an essential way; if `μ_f` is defined for any Beurling-type lattice of atoms, the
> gate fails and (P152.2) is dead on arrival — this is the same failure that killed the tree.
> **(g2) `Ξ_Q`:** must distinguish `ζ_Q(s)` for class number `≥ 2` (off-line zeros of Epstein
> combinations). **(g3) NG-E1/MW-3:** the corpus has proved the per-place forms indefinite and no
> Hasse–Minkowski assembly; (P152.2) must say what supplies the assembly, and "the space is connected"
> is not an answer.
>
> *Status:* **OPEN and heavily gated.** The auditor's estimate is that (g1) fails — the construction
> would be blind to the arithmetic weights — but this is an estimate, not a proof, and it is the one
> thing round 1 could cheaply settle: **write down `μ_f` for a Beurling system and see whether anything
> in the definition notices.** If nothing does, mechanism B is dead for the full Q5, not just for the
> tree, and the death is then final.

### 4.3 Q6 — "no Frobenius via Thm 22.17" is a CATEGORY ERROR

`R152_001`:332–336 argues: "none can come from the ring: `Hom(Spec Z, Spec Z) = {id}`, which is exactly
**Theorem 22.17** of Paper 46". Theorem 22.17 is a statement in the category of **schemes** (`Spec Z` is
terminal in `Sch`, so there are no non-trivial self-correspondences of rings). `M(Z)` and `A^{1,an}_Z`
are objects of a **different category** (Berkovich `Z`-analytic spaces), whose morphisms are not induced
by ring maps `Z → Z`. The counter-instance is in the builder's own text two lines later: the exponent
flow `|·|_v^ε ↦ |·|_v^{λε}` is a genuine, non-trivial continuous self-map of `M(Z)` for every `λ > 0`,
fixing the root, so `End(M(Z))` in the analytic category is **not** trivial. The builder calls it "a flow,
not an endomorphism of the base" and dismisses it — correctly in substance, since it is the corpus's own
scaling flow with the same content (rows A–C) — but the dismissal is the real argument and Thm 22.17 is
doing no work. Importing a scheme-theoretic terminality statement into the analytic category is invalid.

**The conclusion is probably right; the proof is not one.** What is actually needed:

> **(P152.3) — endomorphisms in the analytic category.** Classify the continuous self-maps of `M(Z)`
> (equivalently, the endomorphisms of `A^{1,an}_Z` over `M(Z)`) and show that every one of them acts on
> the `p`-branch by `ε ↦ λ_p ε` for scalars `λ_p > 0` and on the archimedean branch by `ε ↦ λ_∞ ε` —
> i.e. that the full endomorphism monoid is the scaling flow, with **no** map inducing `k ↦ k+1` on the
> integer points of a single branch while fixing the others.
>
> *Consequence if true:* "no Frobenius on Poineau's spaces" becomes a theorem in the right category, and
> the corpus can retire the Thm-22.17 import. *Consequence if false:* a self-map moving `k \log p` to
> `(k+1)\log p` is precisely a Frobenius on the Frobenius lattice, and Dictionary B.1 stops being a
> relabelling. The auditor believes the first alternative, on the ground that such a map would have to
> be a homeomorphism of the branch multiplying `u` by `(k+1)/k`, which is not a single affine map — but
> this is a sketch and not a proof.
>
> *Status:* **OPEN, cheap, and worth settling** — it is a finite question about a tree, not an analytic
> estimate, and it is the only way the corpus's repeated "no Frobenius over `Z`" claim becomes a theorem
> outside the scheme category. It claims no sign and is not a route to RH; it is hygiene.

Separately, the second and third bullets of `R152_001` §B.2 (`:337–349`) are honest: the `F₁`/`Λ`-ring
comparison is **not known to the builder** and nothing is asserted; no pairing on `M(Z) × M(Z)` is known.
The auditor confirms he knows of no such published pairing either and asserts nothing. Q6's negative half
("no square pairing known") is therefore an absence-of-literature claim, correctly labelled at `:427`.

---

## §5 Effect on the kill criteria

* **Kill criterion A** requires all four clauses. (Q2) fires. (Q1) fires only in its "no machinery"
  reading, not through Prop. A.2. (Q3) is asserted, not proved (though the auditor supplies an
  independent non-temperedness obstruction, §1.3). (Q4) fires for the branch-sum route only (Prop. A.4),
  not as the structural impossibility Cor. A.5 claims. **Criterion A is not met as written; the correct
  record is "no known machinery, on four independent counts, and (P152.1) is what would be needed".**
* **Kill criterion B** requires (Q5) refuted. (Q5) is refuted **for `M(Z)`** and is **unanswered for
  `A^{1,an}_Z`**, which the blueprint named. (Q6)'s Frobenius half rests on a category error.
  **Criterion B is not met as written; it is met for the tree.**

**Practical consequence: the verdicts in `R152_001` §0 should read "no route found; no impossibility
proved", and the two propositions that do survive as theorems — A.4 (abscissa `= ½`) and B.3 (meet vs
difference, for trees) — should be stated with their exact scope.** The auditor does **not** recommend
opening a round 1 on either mechanism, with the single exception of the cheap gate test in (P152.2)
(does `μ_f` notice a Beurling system?) and the hygiene question (P152.3), neither of which is a sign
mechanism and both of which are bounded work.

---

## §6 Labels

Nothing in this audit changes any label. **Row D keeps no label. No sign is claimed.** (P152.1),
(P152.2), (P152.3) are `OPEN`, `UNBUILT`, and are not results. Prop. A.4 `PROVED` (scope: the branch
series). Prop. B.3 `PROVED` (scope: pairings of the form `κ(x∧y)` on trees). Prop. A.2 `PROVED` (scope:
`β > ¼` only). Prop. B.2 `PROVED` and demoted to a remark. The Thm-22.17 import in §B.2 is `INVALID` as
an argument and must be removed or replaced by (P152.3). The claim that phase 16 covers the resonance-gap
picture is `OVERSTATED` and must be narrowed to the dictionary `s = ρ/2` and to Pillars 1–2.
