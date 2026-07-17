# Phase 64 — Connes' route: L1 is an RH criterion; realize regularized positivity

**Status:** open · started 2026-06-27 · route proposed by A. Connes in response to the
[2.3.F briefing](../phase-63-lefschetz-realization/BRIEFING-2.3.F-for-Connes.md).

> **Paper:** the publishable consolidation of this phase is **P50** (`04-papers/P50-colligation-route/main.tex`).
> All development notes below live here in the research phase, not in the papers folder.

## ⇒ [THE-TARGET.md](THE-TARGET.md) — the single theorem that is RH, the exact obstruction, the new object to build

**Target (= RH):** realize Ξ as the structure function of a **positive** canonical system ⟺ the negative Kreĭn–Langer index `κ` is **continuous** through the rank-one pole renormalization of the positive von Mangoldt system (finite systems have `κ=0` ⟹ `κ(Ξ)=0` ⟹ RH). **Obstruction:** the only bridge `D_P→Ξ` is the **signature-blind scalar determinant**; `κ` lives in the operator and can only jump through the **single rank-one, definite-signed pole divergence**. **New object to create:** an **index-preserving regularized determinant `D̃`** (axioms A1 recover finite `E_P`/`κ=0`; A2 `κ`-continuous through the rank-one renormalization; A3 limit `=Ξ`) — equivalently a topology on generalized-Nevanlinna `N_κ` in which `N_0` is closed *and* the arithmetic renormalization converges. Lever the program uniquely supplies: the divergence is **rank-one + definite-sign (ζ's pole) + arithmetically explicit**, not generic. Everything feeding it is proved; the one missing piece is **A2 (signature-continuity through the pole)**.

## Theory development (pure-math, no numerics) — the `𝖳𝖶^can_ℤ` construction

The handoff/construction notes, in logical order:
- [THEOREM-adelic-colligation.md](THEOREM-adelic-colligation.md) — the de Branges equivalences + the target theorem
- [TASK-A-CLOSURE.md](TASK-A-CLOSURE.md) — `L1 ⟹ RH` proved (Paley–Wiener lemma unconditional)
- [CURVATURE-computation.md](CURVATURE-computation.md) — `Γ₂≥0` (`CD(0,∞)`) for ζ's prime kernel (new theorem)
- [POLE-DEFECT-estimate.md](POLE-DEFECT-estimate.md) — the wall as a Schrödinger bound state; pole = barrier
- [CONSTRUCTION-critical-gram.md](CONSTRUCTION-critical-gram.md), [M3-arithmetic-index.md](M3-arithmetic-index.md), [M3a-realization.md](M3a-realization.md), [CONSTRUCTION-spectral-surface.md](CONSTRUCTION-spectral-surface.md) — the reduction to a single-class arithmetic Hodge index
- [CONSTRUCTION-local-Tate-colligation-p-adic.md](CONSTRUCTION-local-Tate-colligation-p-adic.md) — **SUPERSEDED** (scalar Euler-factor cell invalid; erratum)
- [CONSTRUCTION-TW-canonical-system.md](CONSTRUCTION-TW-canonical-system.md) — **corrected** object: positive Hamiltonian canonical system, `K_P=∫Y^*dℋY⪰0`; the rank-one escape theorem
- [CANONICAL-FOUNDATION.md](CANONICAL-FOUNDATION.md) — **rigorous foundation**: the canonical Gram identity proved (Lagrange identity); positive Binet archimedean cell; the `D_P→Ξ` determinant identification. Construction now rigorous up to the single wall
- [FACE-C-compactness.md](FACE-C-compactness.md) — **face (C) partial**: escape = a Carleson-measure condition on the von Mangoldt measure; **smooth (PNT) part bounded unconditionally**; the wall = the ½-Carleson norm of the fluctuation = short-interval prime variance at the √n scale (RH-strength, center-of-strip; Goldston–Montgomery ↔ pair correlation)
- [FACE-C-positivity-vs-size.md](FACE-C-positivity-vs-size.md) — **does free positivity bound the wall?** No, with a sharp reason. Lever 1 (Cauchy–Schwarz): positivity collapses the all-intervals Carleson condition to a **single primitive-diagonal sup** `sup_{P,u} e^{−u/2}𝔡_P(u)<∞`. Lever 2: positivity gives a **one-sided lower bound** (off-line pairs can't cancel — the detector). But the diagonal sup **is** the same center-of-strip second moment = pair correlation (proved). **Positivity is orthogonal to size** — sign vs magnitude; the sharpest statement of why every positivity route in the program lands here
- [FACE-C-spectral-shift-monotonicity.md](FACE-C-spectral-shift-monotonicity.md) — **the spectral-shift thread, computed (honest NEGATIVE).** Phase derivative computed explicitly: `πξ_K'(λ)=Σ_n Λ(n)n^{−1/2}cos(λ log n)` = the explicit-formula prime sum; `φ_Ξ'=θ'(λ)+`(that sum), `θ'=½log(λ/2π)>0`. **Sign-chase caught**: the quick "Re ζ'/ζ off-line is negative ⟹ inequality automatic" is a sign-direction ERROR (off-line zeros enter φ' as negative **Poisson dips** of depth `1/(β−½)`, threatening monotonicity). **Verdict: orthogonality theorem at FIRST order** — positivity gives `ξ_K≥0` (0th order) free, RH needs `ξ_K'≥−θ'/π` (1st order); no free sign→derivative passage, and archimedean budget is only **logarithmic** vs off-line dips `1/ε`. Arithmetic rigidity fixes the exact oscillation SHAPE but not its negative envelope. **Thread reduces to the wall.** Yield = sharp pointwise equivalent: **RH ⟺ `½log(λ/2π)+Σ Λ(n)n^{−1/2}cos(λ log n) ≥ 0` pointwise**. Next honest direction (NOT positivity): Diophantine/discrepancy control of the cosine sum over frequencies `{log n}`
- [AUDIT-structure-function-death.md](AUDIT-structure-function-death.md) — **self-audit (2026-06-29): did the phase-monotonicity proof die? NO.** The stated cause of death (`det Y≡1 ⟹ E_P≠D_P ⟹ E_P→E_∞≠Ξ`) was an **invalid non-sequitur, withdrawn** (`det Y≡1` is the Wronskian, says nothing about `E_P` vs `D_P`; never computed; contradicts **Hurwitz** — HB IS preserved under locally-uniform limits). Correct status: the proof is a **valid reduction**, `[E_P HB] + [E_P→Ξ locally uniformly] ⟹ RH`; the open input is **Hurwitz-safe convergence** `E_P→Ξ` (only the *renormalized* determinant is known to →Ξ, and ren-lim isn't locally-uniform). Lesson: a reduction-to-RH-strength is not a dead proof; don't bury a reduction with a hand-waved decoupling
- [FACE-C-structure-function-fork.md](FACE-C-structure-function-fork.md) — **the structure-function fork** *(§2/§3 CORRECTED per the audit above)* (det Y≡1, zeros migrate not condense). Sharp tool = **phase monotonicity** (E HB ⟺ phase φ non-decreasing; RH ⟺ φ_Ξ'≥0; archimedean θ'>0 monotone unconditional, prime S'(t) spikes negative). **Would-be proof caught**: finite φ_P monotone (de Branges) + "pointwise limit of monotone is monotone" ⟹ RH — false at ONE step, `E_P→Ξ` is FALSE (it's the determinant `D_P→Ξ`; `det Y≡1` ⟹ `E_P→E_∞≠Ξ`, limits DECOUPLE). **Floor theorem**: RH = "one canonical system is BOTH positive(HB) AND Ξ-realizing"; every program decomposition supplies one complementary half (positive-not-Ξ: vM/Weil/CD/Gram; or Ξ-not-positive: determinant/Krein-Langer); the join is RH BY DEFINITION (de Branges) — proves *why* every road ends at RH. **Live lead (not yet circular): Kreĭn spectral shift `arg D_P=πξ_K`, positivity ⟹ ξ_K≥0 free; RH needs ξ_K MONOTONE; open = does arithmetic rigidity of vM atoms upgrade sign→monotonicity ξ_K'≥0**
- [FACE-C-rigidity-attack.md](FACE-C-rigidity-attack.md) — **rigidity attack on the isometry equivalent** (non-positivity tool, per directive "attack the equivalence directly"). de Branges structure theorem IS real (positive **structure** Hamiltonian ⟹ Hermite–Biehler ⟹ RH; escapes positivity-orthogonality). Audit: two Hamiltonians — `H_vM≥0` free vs `H_dB≥0`=RH — bridged only by the **signature-blind** scalar determinant `D_P→Ξ`, which can't transport positivity (signature κ = #off-line zeros lives in the operator, not in det). False victory caught: finite truncations ARE HB but their zeros aren't the ζ-zeros (those emerge only in the renormalized limit, which isn't trace-normalizable — the divergence is the rank-one pole). **Yield = sharpest equivalent yet (Thm): RH ⟺ Hermite–Biehler survives the rank-one renormalization ⟺ rank-one escape** (HB-survival wall = rank-one wall, same wall). Turns "decomposition=RH" into a **stability** question. Next probe (pre-audited, untested): pole-sign interlacing + finite HB, avoiding a new zero-sum bound
- [FACE-C-simple-crossings-audit.md](FACE-C-simple-crossings-audit.md) — **attack+audit of the simple crossings.** Four natural "hidden in plain sight" proofs of the one-point wall — (I) averaging/flatness, (II) positive sandwich, (III) Schur/Bernstein from the ODE, (V) phase-interference — each pushed to its limit and audited dead at a **named** step; all four steps are the **same scalar** `λ^{2β−1}` (off-line window amplitude). Structural theorem: the wall has a **free lower fence and an RH-strength upper fence**, asymmetry forced by the **minus sign on primes** in the Weil explicit formula. New clean equivalent extracted from (V): **RH = the functional-equation reflection `s↔1−s` acts as an ISOMETRY of the primitive canonical kernel** (off-line zero = reflection is a contraction/expansion, mismatched amplitudes `λ^{±(2β−1)}`)
- [CONSTRUCTION-critical-finite-part.md](CONSTRUCTION-critical-finite-part.md) — positivity is free (Stage 4)
- [CONSTRUCTION-boundedness.md](CONSTRUCTION-boundedness.md) — the wall = rank-one escape, center-of-strip
- Correspondence: [REPORT-BACK-to-Connes.md](REPORT-BACK-to-Connes.md), [REPORT-2-to-Connes.md](REPORT-2-to-Connes.md), [LETTER-to-Connes.md](LETTER-to-Connes.md), [LETTER-from-Connes.md](LETTER-from-Connes.md)

## The reclassification

Connes' diagnosis: **L1 (`sup_λ ‖A^osc_λ‖ < ∞`) is not a technical lemma below RH — it is an RH
criterion in finite-window/Jacobi clothing.** A new route must not bound `A^osc` coefficientwise; it
must either (1) prove the precise equivalence `L1 ⟹ RH`, or (2) replace finite-window
gap/coercivity by a **regularized infinite-dimensional positivity** (relative determinant /
de Branges canonical system / adelic scattering colligation).

This explains every Phase 60–63 failure at once: the obstruction is a **pole of `ℒF_a(w)` with
positive real part** at `w = 2ρ−1` for each off-line zero `ρ`. Cesàro cannot remove a pole in
`Re w > 0`; zero-density controls `γ` not `β`; the gaplessness is the `L²`-norm being wrong, not an
accident.

## The four tasks (Connes)

| task | statement | type | status |
|------|-----------|------|--------|
| **A** | Laplace-pole theorem: `F_a(t)=O(1) ⟹ ℒF_a` holo in `Re w>0`; off-line `ρ` ⟹ pole at `2ρ−1`. Prove detector-nonvanishing `∀ρ (β>½) ∃a∈𝒥: C_a(ρ)≠0` ⟹ **L1 ⟹ RH**. | analytic + numeric check | — |
| **B** | Replace gap by **relative determinant** `𝒟_λ(z)=det₂((I−zK_λ)(I−zK_λ⁰)⁻¹)`, `K_λ=L_arch^{−½}L_prime L_arch^{−½}`; finite part at `z=1`. ζ bounded, DH drifts `λ^{2β−1}`. | numeric | — |
| **C** | **Herglotz/de Branges**: Weyl `m_λ`, Schur `S_λ`, canonical Hamiltonian `H≥0`. | numeric + theory | **first pass** ([E102](E102_debranges.py), [RESULTS](RESULTS.md)): finite structure holds for BOTH ζ&DH (auto for self-adjoint Jacobi) → no discrimination; ζ marginally degenerate at boundary; **real content = Euler-product/adelic colligation (theory)** |
| **D** | **Parity no-go**: scaling-compatible 1st-order op has odd symbol ⟹ anticommutes with `J`; `J`-linear ⟹ even ⟹ sees only `γ²`. | lemma | **PROVEN** ([RESULTS](RESULTS.md)) |

## Connes round 3 — Kreĭn–Langer negative-square index (E108): the sharp, robust RH index

Connes' reply to report 2 sharpened the index: **not** `μ_max=1` (boundary) but the **Kreĭn–Langer
negative-square count** `ind₋(K_{S_κ}) = #{UHP poles} = #{off-line zeros}`, with **RH ⟺ ind₋=0**.
Verified exactly ([E108](E108_krein_langer.py), [E108_RESULTS](E108_RESULTS.md)): ζ has **`ind₋=0`**;
`k` planted off-line zeros give **`ind₋=2k`** (k=1,2,3 all match). An **exact integer count** — robust,
unlike the marginal `μ_max`/Pick min-eig. Plus Connes' two audits applied: non-strict HB (RH doesn't
need simple zeros); the Euler product is a **boundary/strip** object (`Im z<ω−½`), passivity on `ℂ_+`
is by analytic continuation + zero-free placement (E105 corrected). Target = **Critical Gram
Realization**: `K_{S_κ}=⟨k_w,k_z⟩` for adelic Hilbert vectors (the renormalized ω↓0 limit a genuine
Hilbert, not Pontryagin, norm).

## Task A closure + finite-prime test (Connes round 3 follow-up)

- [TASK-A-CLOSURE.md](TASK-A-CLOSURE.md) — **`L1 ⟺ RH` proved (RH-neutral)**: the Laplace-pole theorem
  with **Lemma 1 (Paley–Wiener nonvanishing) proved unconditionally** (`ê_n(ρ)≠0` for off-line ρ);
  two standard inputs flagged (converse convergence; Lemma 2 cyclicity, needed only for the Jacobi
  phrasing — the forward proof uses raw entries and bypasses it). So 2.3.F ⟸ L1 ⟺ RH: 2.3.F is
  genuinely RH-equivalent, no hidden easier route. DH unbounded by Lemma 1.
- [E109](E109_finite_prime_colligation.py) ([results](E109_RESULTS.md)) — **finite-prime scalar route
  fails at ω=0**: in-strip (ω=1) the truncation converges and is passive; at ω=0 the scalar Euler
  product **diverges** (error→9.8e8). Confirms Connes: the scalar finite-prime criterion is void at
  the critical value; the **matrix colligation + renormalization is essential** (the open Gram step).

## Pure-math construction (no numerics) — the colligation, reduced to one arithmetic obstruction

- [CONSTRUCTION-critical-gram.md](CONSTRUCTION-critical-gram.md) — §1 de Branges–Rovnyak model space
  (rigorous); §2 `ω>½` colligation is Hilbert (Prop. 2, rigorous) + adelic Lax–Phillips realization;
  **§3 (rigorous reduction): RH ⟺ positive angle between the Tate subspaces `𝒟₋, 𝒟₊=ℱ𝒟₋` ⟺ overlap
  form ⪰0 ⟺ `ind₋=0`.** DH fails for lack of `ℱ=⊗'_vℱ_v`.
- [M3-arithmetic-index.md](M3-arithmetic-index.md) — corrects M2 (global norm couples places; angle =
  Hankel operator); shows the analytic side is **RH-equivalent** (not an independent input) ⟹ the
  non-circular input must be **arithmetic**; reduces it to a single-class Hodge index with
  **Abboud's unconditional `(D·D)≤0`** and degree-balance `(D·H)=0 ⟺ μ_max=1`.
- [M3a-realization.md](M3a-realization.md) — the correspondence realization `Z_f=∫\hat f(t)[F_t]dt−c_f[Δ]`;
  **formal self-intersection identity `(Z_f·Z_f)=W(f)`** via the trace formula; RH follows from
  realization + Abboud + sign. **Irreducible gap (§4):** the arithmetic intersection theory on the
  Connes–Consani arithmetic-site square `\widehat{Spec ℤ}^2` with the Hodge-index sign — MW-5 localized
  to one construction, the active Connes–Consani frontier (open, not fabricable).

**Honest endpoint:** `RH ⟸ [model/Lax–Phillips/Kreĭn–Langer + Abboud + μ_max=1 : rigorous, assembled]
⟸ §4 (one arithmetic intersection pairing with Hodge-index positivity, OPEN).** RH not proved.

## The RH-strength theorem + second report

- [THEOREM-adelic-colligation.md](THEOREM-adelic-colligation.md) — precise statement of the crux:
  Theorem 1 (equivalences RH ⟺ `K_κ⪰0` ⟺ `Θ_ω` passive ⟺ `m` Herglotz ⟺ `R≥0`, de Branges);
  Theorem 2 (unconditional `ω>½` Tate colligation, matrix level); **Theorem 3 = RH** (interior
  passivity (P) continued to `ω=0` = critical de Branges kernel positive). Boundary unitarity (U,
  functional equation) is in hand; (P) is open and must be powered by the Euler product.
- [REPORT-2-to-Connes.md](REPORT-2-to-Connes.md) — second report: route validated end-to-end,
  the regularized-continuation finding (`R≈6.1e-8>0` for ζ), the matrix-colligation refinement, and
  four questions on the mechanism for (P) / where the Euler product must enter.

## Connes round 2 — shifted scattering / Pick matrix (E104): CONFIRMED, sharp

Per Connes' second reply (§7), the decisive test is the **shifted scattering family**
`Θ_ω(z)=ξ(½+ω+iz)/ξ(½+ω−iz)` via the **Pick matrix** (interior passivity — *sees poles*, stronger
than edge contractivity). Result ([E104](E104_pick_scattering.py), [E104_RESULTS](E104_RESULTS.md)):
- **ζ: Pick-PSD for all ω from 1.0 → 0.01** (marginal at ω→0) — passivity survives the continuation
  to the critical value ⟹ RH-consistent.
- **off-line zero at β: passivity fails exactly at `ω* = β−½`** — confirmed for β=0.65/0.75/0.80/0.90
  (thresholds 0.15/0.25/0.30/0.40, all exact). The Pick matrix directly detects the off-line pole.

This is the strongest, most quantitatively faithful realization of the route: `Θ_ω` is
**unconditionally** Schur for ω>½ (Euler-product safe region), and **RH = passivity survives ω↓0.**

**Canonical de Branges kernel (E106, Connes §1):** `K_κ` for `E_κ=Ξ'−iκΞ` is **genuinely PSD for ζ**
(dps=40, rel margin +3.4e-14), fails for off-line zeros — `RH ⟺ E_κ` Hermite–Biehler `⟺ K_κ⪰0`,
validated on the true ζ.

**ω↓0 continuation margin (E107):** the *absolute* margin →0 as ω→0, but the **relative
(regularized) margin `r=min/max eig` converges to a positive constant `R≈6.1e-8` for ζ** — the
regularized positivity **survives the continuation to ω=0**. Off-line zeros flip the sign **exactly
at ω=β−½** (confirmed down to β=0.55, with local sampling near the pole). Proving `R>0` for all
configurations = RH.

**Audited (2026-06-28, [AUDIT.md](AUDIT.md)):** all results re-checked; one precision correction
(E104 float64 was noise; dps≥30 confirms genuine PSD). Every ζ-positive is a *marginal* detector
(stated as such); falsifier integrity intact (ω=β−½, `λ^{2β−1}`).

**Tate factorization (E105):** for ω>½, `Θ_ω = Θ_∞·∏_p Θ_p` (Euler product, confirmed), and the
**assembled product is passive** (Pick-PSD). Refinement: the scalar local factors are unimodular on
ℝ but **not individually inner** — passivity is **collective / a J-unitary matrix-colligation
property** (each local Tate piece = a passive delay matrix, delay `log p`). The construction must use
the local **transfer matrices**, not scalar factors. RH-strength step unchanged: continue the passive
adelic *matrix* colligation to ω↓0.

## Status: Connes' reclassification validated; 3 of 4 tasks confirmed/proven

L1 **is** an RH criterion (A); finite-window positivity = **edge-contractivity** (ζ `μ_max=1`, no
past-edge mass — B; canonical Hamiltonian marginal at the boundary — C); DH violates with the
predicted `λ^{2β−1}` drift + complex modes. No 1st-order J-linear zero operator (D). **The crossing
is now precisely: construct the Euler-product/adelic unitary colligation whose Schur function `S_λ`
is contractive by Hilbert-space geometry** — a theory construction (Connes–Consani / adelic
scattering) that numerics can scaffold and falsify-test (DH must lack it) but not carry out. No proof
of RH. See [RESULTS.md](RESULTS.md).

## Guardrails

dps ≥ 40; **DH falsador mandatory** — it is the diagnostic that any soft (functional-equation +
symmetry) argument fails; a real proof must use Euler-product/adelic positivity that DH lacks.
No false victory. Reuse phase-61 engine; the E3 CCM operator (phase-60) for the `H_x`/zero spectrum.

## Order of attack

D (clean, nearly proven) → A detector-nonvanishing (numeric, via DH growth → `2β−1`) →
B relative determinant (the central new positivity object) → C de Branges (deepest).
