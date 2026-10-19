# TRACT_001 — Phase 204: are we dismissing, under «REF-D», reformulations more tractable than D?

All the reformulations in this memo are
reformulations **of D** (or of L′♯ in a window T) and are stated D-only.
ARGUED / OPEN / NO-GO. This memo **proves nothing new**: it classifies. Only this file was written; the proposed
index entry is in §7 for the coordinator to copy.

## Summary (≤300 words)

The index uses «REF-D» in ~350 places: 82 occurrences in `README.md`, 239 in `04_PHASES_100-189.md` (89 automatic
rows relabeled «REF-D; NOT closed»), 11 in `06_`, 9 in the certainty audit of
phase 193 (≈1/3 of ~105 dismissals from phases 190–193 are REF-D). The index's own header says REF-D **is not
closure**. The initial hypothesis is therefore plausible a priori: the index never records a «tractability»
column.

I reviewed 13 reformulations (R1–R12 of the target plus (L2) = S_{T,k} ⪰ 0). Result:
- **Dismissals backed by a theorem** (not just judgment): R4 (Horn A/B ⇒ (W⁰), Thm HA/HB PROVED), R5 (MW-5: the
  frame defect also holds over 𝔽_q, NO-GO for carriers that postulate positivity), R9 (additive +
  multiplicative gauge, Thm M.1–M.2), R11 (T201-a: explicit monotone falsifier), R12 (C-pos (i)–(iii) PROVED).
- **Dismissals by judgment, without tractability analysis, with an identifiable own path:**
  **R6 (2×2 polar capacity)**, **R10 (Lemma F, logarithmic moment inequality without Λ)** and **R13/(L2)
  (S_{T,k} ⪰ 0, finite Schur matrix)**. All three reduce D in T to a finite-dimensional object or to a
  functional inequality without explicit primes, where general theorems exist (Hadamard/Kato for the variation in T
  of capacity constants; three-lines/Hardy–Heisenberg type convexity; Sylvester/eigenvalue continuity with
  induction on T).
- R1/R2/R3/R7/R8 remain in the middle: they have classical structure (prolates, Kreĭn, Bochner, Γ-convergence) but
  the missing hypothesis is literally the data of ζ in the window; they do not gain tractability.

**Answer to the original question: PARTIAL.** There was no gross error: no dismissed tool «worked» in
the sense of closing D, and most REF-D entries come with a theorem showing that the reformulation inherits the same
bottleneck (Λ-linear, comb-generic, margin). But there WAS a **bounded method error**: three finite-dimensional or
Λ-free reformulations were filed under «it's REF-D» without asking whether the new structure admitted a general
theorem. Those three are valid targets and have a first concrete lemma (§6).

---

## 0. Count and reading of the index

| source | «REF-D» occurrences | note |
|---|---|---|
| `ROUTES-TRIED-INDEX/README.md` | 82 | includes l.110–112 (correction: REF-D ≠ dead) |
| `04_PHASES_100-189.md` | 239 | 89 automatic rows «DEAD [REF-D]» relabeled «NOT closed» |
| `06_OPEN_RESIDUES_DEAD_SUBROUTES.md` | 11 | l.4: «records where a sub-route ends; it does not close the residue» |
| `AUDIT_PHASE193_CERTAINTY.md` | 9 | ≈1/3 of ~105 dismissals from 190–193 are REF-D |
| `SURVEY_MODERN_UNTRIED`, `05b_`, `03_` | 4+2+1 | — |

Reading: the index formally distinguishes REF-D from NO-GO, but **in practice** the rounds of phase 193 and phase
200 used «REF-D» as sufficient reason to move to the next seed (e.g. README l.165, 174, 175, 212, 251,
255, 263; «REF-D as route» on front I). No entry records the question «is it more tractable?». The only
explicit exception is CPOS_CLASS_001 (iv): «what is not ruled out is that a stronger statement might be more
tractable», left as ARGUED with no follow-up. META_200_BARRIER_001 (Φ200, branch 2) formalizes the same pattern: every
stability λ_A(a) ≥ −CΔ(a) with Δ(Λ)=0 is equivalent to WP_T(Λ) plus a condition — i.e. it falls into branch 2 «by
construction»; Φ200 is ARGUED as a class. That is a theorem about *content*, not about *tractability*.

**Criterion of this memo.** A reformulation R is **more tractable** than D if there exists a class of general
theorems 𝒯 (not specific to row D) such that: (1) R is in the domain of 𝒯, and (2) the remaining hypotheses of 𝒯
are verifiable using information *different* from the sign value being sought. If the only remaining hypothesis is
«the window form is ≥ 0» rewritten, R is not more tractable (I call it a **transfer**).

---

## 1. Minimal notation (D-only)

- 𝔞_T = Weil form of window T on the declared carrier (Paper 47, def:W / eq:nuw); P_T the admissible core; λ_A(T)
  its normalized infimum. **D in T:** 𝔞_T ≥ 0 on P_T. **D:** D in T for every T.
- 𝒢̄_T: additive gauge (subspace that the radical of the full form contains, Guo L4.4 CITED). ℓ(g): gauge-minimized
  leak. N = N(T) the contact level.
- **L′♯** (prob:ext-L): ∃κ>0, A₀≥0, ∀T with N≥5, ∀g in the core: W_T(g) ≥ κN^{−A₀} ℓ(g). L′♯ ⇒ D (PROVED, trivial
  since ℓ ≥ 0); L′♯ is strictly a quantification of D.

---

## 2. The reformulations, one by one

Format: (a) statement; (b) direction and label; (c) relative strength; (d) tractability and general theorem; (e)
reason for dismissal; (f) risk of being harder than D.

### R1. exterior (★★) (prop:ext-consol)

(a) For every N ≥ 5 and every r = 𝓕f|_{(λ,∞)} with f admissible in T, with Ψ̌ = (Zr)(e^·)𝟙_{(T,∞)}:
(1/2π)∫ m|Ψ̂̌|² + 2A(Ψ̌)B(Ψ̌) − 2⟨Ψ̌,(Z_log r)(e^·)⟩ ≥ 2κN^{−A₀} dist²(r, 𝒢̄_T).
(b) (★★) ⟺ L′♯ (PROVED, prop:ext-consol). (c) Same as L′♯; strictly stronger than D (quantifies).
(d) Structure: quadratic form on the half-line (T,∞) with archimedean symbol m plus a Chebyshev term
∫t^{−½}C(log t)d(ψ_Λ − t) (variant (a) of the proposition). Candidate general theorems: Hardy-type/Wiener–Hopf
on the half-line; prolate basis (variant (b)) with D = diag(1−χ_k) and Landau–Widom for χ_k. Missing hypothesis: a
lower bound for the term d(ψ_Λ − t) tested against autocorrelations C of exterior tails — this is the Chebyshev
fluctuation **at the scale of the margin**, and phase 191 (`lem:shape-est`) shows that no prime estimate operates at
that scale (PROVED in part (i)). → **transfer**.
(e) Dismissal: «REF-D in block» (LEMMA_I3_001 verdict Q1: all the sign transfers to A_⊥⊥(1) = (★★)). Judgment, but
backed by lem:shape-est (theorem).
(f) High risk: it adds the factor N^{−A₀}·dist²; if λ_A decays faster than any power of N, (★★) is false while D is
true. That risk is quantified: thm:margin gives λ_A ≤ 4·10⁹ T e^{−15.449T} (PROVED), compatible with a power of
N = e^{cT} only if A₀ ≳ 15.4/c. Not an obstruction, but it constrains A₀.

### R2. Gauge-minimized L′♯

(a) As in §1. (b) L′♯ ⇒ D (PROVED); with leak(f) in place of ℓ it is FALSE (PROVED: φ ∈ 𝒢_T has Eφ=0, leak>0).
(c) Stronger than D. (d) General theorems: Gårding/Korn-type coercivity for forms with known kernel —
the model is «form ≥ c·dist² to the kernel» (Korn inequality, Poincaré with quotient). The useful structure would
be that 𝒢̄_T = the exact radical of a *neighboring* Λ-free form, and the difference is relatively compact: then the
Fredholm/Weyl theorem gives coercivity except on a finite space, which is handled by hand. Missing hypothesis: (i)
relative compactness of (𝔞_T − neighboring form) with respect to dist²(·,𝒢̄_T); (ii) that the exceptional finite space
has no negative direction — the second point **is D in finite dimension**: that is exactly R13. (e) Dismissal: not
dismissed; it is the current target (project-goal-lemma-L-sharp). (f) Moderate risk (see R1).

**Tractability remark.** The «Fredholm + finite» scheme is the only general theorem that reduces L′♯ to something
different: I note it as a bridge R2 → R13.

### R3. Kreĭn indeterminacy (phase 155 r5), rewritten D-only

(a) Let g_T be the distribution of the explicit formula restricted to [−2T,2T] (the window data of thm:Z). **R3:**
for every T, g_T is positive definite on [−2T,2T] **and** the Kreĭn extension problem for g_T is in the
indeterminate case (the Toeplitz forms of g_T have full rank at every scale; no finite linear recurrence propagates
it).
(b) R3 ⇒ D (PROVED: the first clause is D in T by thm:Z/def:PD). D ⇒ «g_T PD» trivially; D ⇒ indeterminacy is
OPEN (R155_031 P5 marks half of ζ as HEURISTIC; the citation of R155_014 Rem 2.5 unverified).
(c) Strictly stronger than D (adds indeterminacy). (d) General theorems: Kreĭn (1940) extension of
PD functions on an interval; indeterminacy criterion via de Branges spaces / logarithmic integral (Kreĭn,
Akhiezer); finZ (Paper 47 §7) is the degenerate determined case. **But Kreĭn theory presupposes the PD of the data
on the interval**; indeterminacy is a property *within* the PD cone. Missing hypothesis: the PD of g_T, which is D
in T. → **pure transfer** with respect to sign; the new part (indeterminacy) IS tractable with Kreĭn once PD is
given, but contributes no sign.
(e) Dismissal: phase 155 r5 («restatement»); phase 193 front D: «de Branges/Kreĭn dead». Judgment with the correct
reason: Kreĭn does not produce positivity, it consumes it.
(f) Risk: stronger than D; no gain. **Not recommended.**

### R4. Schur complement A_⊥⊥(1) / Horn A = (W⁰) / minimal operator (boundary triple)

(a) In the affine congruence L (LEMMA_I3_001, PROVED): A(c) = Lᵀ[(1−c)C ⊕ (A_⊥⊥(1) + (1−c)Q/C)]L; R4: A_⊥⊥(1) ⪰ 0.
Horn A: Hodge-transfer hypothesis with defect Δ; (W⁰): I_∞(G,G) ≤ 0 on real classes of degree 0. Boundary triple:
the minimal operator of W_λ is ≥ 0.
(b) A_⊥⊥(1) ⪰ 0 ⟺ D on the block (PROVED, «REF-D on block»); Horn A ⇒ (W⁰) in two lines (Thm HA, PROVED) and the
falsifiers fail Horn A only because they fail the target; Horn B ⇒ (W⁰) with any cone (Thm HB, PROVED); boundary
triple = polar capacity 𝔊_T (phase 193 front A, PROVED).
(c) Same as D (the block) / stronger (Horn). (d) Candidate general theorem for A_⊥⊥(1): **the O(1) gap in the block**
(LEMMA_I3_001: In(C_RR) = (2,0,dim𝒢−2), NUMERICAL, translation-invariant block PROVED) suggests that A_⊥⊥(1) is
a Toeplitz/convolution operator on the block, for which Szegő/Böttcher–Silbermann give the spectrum as the range of
the symbol. Missing hypothesis: that the symbol is ≥ 0 — the data again. → **transfer**, though *with* available
general spectral theory (see §5: it is the infinite-dimensional version of R13).
(e) Horn A/B: genuine NO-GO as a *transfer route* (theorem: trivial reformulation). A_⊥⊥(1): judgment «REF-D on
block».
(f) Low for A_⊥⊥(1) (it equals D); Horn: closed by theorem.

### R5. MW-5 / OT-5′

(a) There exists a polarized object over ℤ (extension of D^W) with ample class, quadratic h⁰, and trace property
whose Hodge-index inequality gives 𝔞_T ≥ 0. (b) MW-5 ⇒ D (CONDITIONAL on existence; Hodge-transfer cond. on h⁰,
phase 135). (c) Existential; if it exists, stronger. (d) General theorems: Hodge index, Riemann–Roch; but the
object does not exist. Phase 158 proved that the instance in the adèle class space is a restatement; HORN_B:
«(Big♯) OPEN without object». (e) **Genuine NO-GO as a class**: «every carrier postulates positivity; the frame
defect also holds over 𝔽_q» (04_ l.27, W10); scaling site R9-02 structural NO-GO. What's alive is *construction*,
not reformulation.
(f) Very high: inventing the object is harder than D in any finite window.

### R6. 2×2 polar capacity condition (per-window converse, phase 156)

(a) For each T: the content of D in T, modulo RD_T (the resolved part of the window), is the sign of two polar
capacity constants g_±(T) (prop:polarcap: 𝔊_T = S^{Sch}_T + J, a 2×2 matrix on the even/odd polar modes). R6: g_±(T)
≥ 0 for every T.
(b) D in T ⟺ RD_T ∧ (g_±(T) ≥ 0) (R156_001; P2.1 PASS/PROVED in R156_004). Converse: fails in comb models (phase
156: «fails in comb models») — i.e. the per-window *sufficiency* without RD_T fails, not the equivalence.
(c) Same as D (given RD_T). (d) **Here there is genuine structure:** g_±(T) are Schur complements of a form on a
codimension-2 space; as functions of T they are *scalars* with (i) continuity in T (lem:contA, PROVED for λ_A; the
same proof works for g_±), (ii) Hadamard/Kato variation formula: dg_±/dT = (boundary data at ±T)·|trace of the
extremal|², because changing T moves the domain boundary. General theorems: Hadamard (capacity variation with
domain), Kato–Rellich (analytic perturbation of isolated eigenvalues), continuation argument: if g_±(T₀) > 0
(known for T₀ ≤ ½log15, Mori boundary verified, NUMERICAL/CITED) and g_± cannot cross 0 without the extremal
satisfying an overdetermined boundary condition, continuation follows. Missing hypothesis: **a no-crossing lemma** —
that at a T* with g_±(T*) = 0 the Euler–Lagrange equation of the extremal plus the boundary condition are
incompatible. That incompatibility is not D: it is a rigidity property of a 1D boundary-value problem.
(e) Dismissal: «converse fails in comb models» + «2×2 = 𝔊_T = boundary triple = REF-D» (phase 193 front A).
**Judgment**: the comb-model falsifier kills *sufficiency without RD_T*, not the continuation route in T. Nobody
attacked the T-dynamics of g_±.
(f) Risk: no-crossing might require ζ information along the whole boundary (margin scale). Moderate; but the
question is 1D and therefore quickly falsifiable.

### R7. «ν̂ ≥ 0 on the admissible cone» (GG)

(a) The spectral measure ν of the window formula has transform ν̂ ≥ 0 tested on the admissible cone of flat-top
tests (thm:Z, GG in phase 199). (b) ⟺ D (thm:Z: the certificate is the explicit formula on flat-top tests; PROVED).
(c) Same. (d) Bochner–Schwartz requires ν̂ ≥ 0 on the *entire* cone of autoconvolutions; here the cone is
restricted, so the applicable general theorem is cone duality (Kreĭn–Milman / Hahn–Banach): ν ≥ 0 on the dual of
the cone. Missing hypothesis: describing the dual cone — phase 199 constraint 10 shows 2AB ≡ 0 on the FF.1/GG base.
→ **transfer**.
(e) Judgment «REF-D» (README l.212 convex decomposition «= D or certificate»; front L LP on the torus REF-D). (f)
Same as D; no gain.

### R8. Quantitative variational stability (SPEC_006 area 1 / Φ200 branch 2)

(a) λ_A(T; a) ≥ −C_T·Δ_T(a) for weights a near Λ, Δ_T(Λ) = 0. (b) Φ.1 (PROVED): every stability of this form is
equivalent to WP_T(Λ) (= D in T) plus Lipschitz; META_200 l.149. (c) Stronger than D. (d) General theorem:
Łojasiewicz (analytic gradient) — E9 «VIRGIN», 0 hits. But Łojasiewicz gives stability *around a known minimum*;
here the minimum's value is the unknown. → **transfer**. E9 notes that D2 and E1 are the same object.
(e) **NO-GO by theorem** (Φ.1 PROVED: branch 2), although Φ200 as a class is ARGUED. (f) High.

### R9. «Mass at the zeros» / additive + multiplicative gauges

(a) The value of W_T(g) on the core is invariant under every η ∈ 𝔐 (weights equal to 1 at the ordinates) and under
𝒢̄_T.
(b) Thm M.1, M.2 PROVED; «together they generate no new structure» PROVED (class theorem: the value does not
depend on η). (c) Not a reformulation of D: it is a *symmetry* of the form. (d) Symmetries give no sign; the
general theorem (averaging over the gauge group) returns the same form. (e) **Genuine NO-GO**. (f) n/a.

### R10. Lemma F (logarithmic moments without Λ, minimal-leak representative)

(a) F(ε) = ‖Z^{(ε)}r‖² (comb deformed n ↦ n^ε) on the minimal-leak representative f♯; Lemma F: F convex at ε=0.
Explicit form (F0_TEST_001 §5): 2‖Z_log r‖² + 2⟨Zr, Z_{log²}r⟩ ≥ 0 (M₁-convexity), integrated Δ_ε ≥ 0.
(b) Exact identity (A_MU_FACTORIZATION_001 (f), PROVED): the exterior prime term = F′(0). Lemma F ⇒ the exterior
part carrying the sign (CONDITIONAL on the splice with the interior; A_MU: «filter P10 holds halfway»). F0_TEST:
F″(0) ≥ c·ℓ* with c ≈ 2.1 (NUMERICAL) at the extremal: **Lemma F does not die at the extremal**.
(c) **Different from D in form**: it contains no Λ; it is an inequality on the family Z^{(ε)} of ε-deformed
Dirichlet operators. Its relation to D is CONDITIONAL. (d) **Genuine structure:** convexity in a deformation
parameter of an L² norm is a classical problem — Hadamard three-lines / Riesz–Thorin log-convexity
(CITED on the full line, A_MU), Hardy/Heisenberg inequalities for ⟨Zr, Z_{log²}r⟩ (the second derivative is a
«position²» type operator in log n), and complex interpolation of Stein for analytic families. Missing hypothesis:
on the half-line (not the full line) the FE symmetry that trivializes convexity does not exist (R-F2 PROVED:
«on the full line every transversal convexity vanishes by FE»); what's missing is a **three-lines theorem with
boundary** for the half-space of exterior tails. That is harmonic analysis, not arithmetic.
(e) Dismissal: SPEC_006 row R-F2 (PROVED) kills «Lemma F as sign» on the full line; F0_TEST revived it as an
OPEN moment inequality. In phase 201 it was abandoned due to a family change, not a NO-GO. **Judgment.**
(f) Risk: the inequality could be false for some admissible r far from the extremal (F0_TEST tested only the
extremal) — cheaply falsifiable numerically; or the interior/exterior splice could reintroduce Λ (A_MU (f): «Λ dies
in the formula, only in the descent»). Moderate.

### R11. T201-a / (H) from PROOF_H (minimizer virial)

(a) Excess inequality: there exists β_T: ℤ_{≥0}→ℝ_{≥0}, β_T(0)=0, such that the integer excess controls 𝔞_T; with
(T201-b) it gives L′♯ in T (SPEC_201_001 l.184–199). (b) T201-a ∧ T201-b ⇒ D in T (PROVED as a combination). (c)
Stronger. (d) General theorem: virial/Pohozaev — but front I phase 193: «virial holds for every comb, DH included»
(dead). (e) **Genuine NO-GO:** SPEC_201 l.286 gives an explicit falsifier for every monotone (T201-a); l.208: if one
only proves by summing entries with sign, it falls into branch 2. (f) n/a.

### R12. H(O_{g,ζ}) generic operator positivity (C-pos (iv))

(a) Uniform construction O_{g,a} over the degree-one theory 𝔗₁, with H(O) ⇒ P(O) ≥ 0 and 𝔞^a_T(g) ≥ Φ(P(O_{g,a})).
(b) (i)–(ii) PROVED (fails in F_DH, Epstein); (iii) PROVED if κ_T ≠ 0; (iv) ARGUED: verifying H for ζ uses a premise
outside 𝔗₁ and is at least as strong as D. (c) ≥ D. (d) **It is exactly the original question in theorem
form**: (iv) admits that «stronger» might be more tractable. But (iv) does not specify O; without O, there is no
general theorem. (e) Class theorem (i)–(iii); (iv) explicit and honest judgment. (f) Indeterminate without O.

### R13 (found in `06_` l.181). (L2): S_{T,k(T)} ⪰ 0

(a) For every T > ½log5, the finite Schur matrix S_{T,k(T)} (R186_025, Thm A/B + Cor (L1) PROVED) is positive
semidefinite. (b) λ_A(T) > 0 ⟺ S_{T,k} ≻ 0 (PROVED, R186_025/105). (c) Same as D in T. (d) **Genuine structure:**
finite dimension k(T), explicit entries, continuity in T. General theorems: Sylvester's criterion (principal
minors), Cauchy interlacing when passing from k to k+1, eigenvalue continuity (Weyl) + first-crossing argument: if
det S_{T,k} does not vanish on (T₀,T₁), the sign is preserved. Induction on contacts: k(T) jumps at new primes
(lem:contA: empty entry instant). Missing hypothesis: **non-vanishing of the determinant between contacts** and
**interlacing at the jump k → k+1**. Neither is D: the first is a fact about a real-analytic function of T on an
interval; the second is the Schur formula for a rank-one border.
(e) Dismissal: walls W-lin, W-det, W-fam, W-pat, W-loc, W-mom (phases 183–186): «every first-order discriminant is a
functional of h*, not σ» — which is a **theorem about which functionals don't work** (first-order), not a NO-GO
for the crossing argument. W-det kills «determinants» as a pointwise *sign* discriminant, not as a continuation
tool. **Partial judgment**.
(f) Risk: the no-crossing condition in T might require certified enclosures (numerics as mechanism) in each
interval; no uniformity in T guaranteed. Moderate-high.

---

## 3. Consolidated table

| R | direction | strength vs D | general theorem | missing hypothesis = D? | dismissal | type |
|---|---|---|---|---|---|---|
| R1 (★★) | ⟺ L′♯ PROVED | stronger | Wiener–Hopf, prolates | yes (Chebyshev at margin scale) | REF-D on block + lem:shape-est | judgment+theorem |
| R2 L′♯ | ⇒ D PROVED | stronger | Fredholm/Korn + finite | partial (→R13) | current target | — |
| R3 Kreĭn | ⇒ D; ⇐ OPEN | stronger | Kreĭn/de Branges | yes (PD of the data) | restatement | correct judgment |
| R4 Schur/Horn | ⟺ / ⇒ PROVED | same / stronger | Szegő-Toeplitz | yes (symbol ≥0) | Thm HA/HB | NO-GO (Horn); judgment (block) |
| R5 MW-5 | cond. | existential | Hodge index | nonexistent object | W10 | NO-GO as class |
| **R6 polar capac.** | ⟺ given RD_T | same | Hadamard/Kato + continuation | **no** (1D no-crossing) | «comb models» + =𝔊_T | **judgment** |
| R7 ν̂≥0 | ⟺ PROVED | same | cone duality | yes | REF-D | correct judgment |
| R8 stability | Φ.1 PROVED | stronger | Łojasiewicz | yes | branch 2 | NO-GO (PROVED piece) |
| R9 gauges | symmetry | n/a | averaging | n/a | Thm M.1–M.2 | NO-GO |
| **R10 Lemma F** | ⇒ exterior, CONDITIONAL | different, no Λ | three-lines with boundary, Stein, Hardy–Heisenberg | **no** | family change | **judgment** |
| R11 T201-a | ⇒ PROVED | stronger | virial | — | explicit falsifier | NO-GO |
| R12 C-pos(iv) | ARGUED | ≥ | none without O | — | (iv) ARGUED | honest open |
| **R13 (L2)** | ⟺ PROVED | same | Sylvester, Cauchy-interlacing, first crossing | **no** (det non-vanishing between contacts) | walls W-* (first order) | **partial judgment** |

---

## 4. Tractability ranking (not novelty)

Criterion: (1) dimension of the object; (2) is the missing hypothesis distinct from the sign?; (3) is there a
general theorem with verifiable hypotheses?; (4) cost to falsify.

1. **R13 (L2) S_{T,k} ⪰ 0** — finite, explicit, continuity PROVED, fully general matrix theorems.
2. **R6 polar capacity g_±(T)** — two scalars; Hadamard variation; no-crossing = 1D rigidity.
3. **R10 Lemma F** — no Λ; classical harmonic analysis; quickly falsifiable away from the extremal.
4. R2 L′♯ via Fredholm+finite (reduces to 1).
5. R4 block A_⊥⊥(1) as Toeplitz (infinite-dimensional version of 1/2).
6. R1 (★★).
7. R7, R3 (transfers; general theory consumes PD).
8. R8, R12 (stronger, without object or branch 2).
9. R5, R9, R11 (genuine NO-GO or existential).

Warning: 1 and 2 are related (g_± are the polar modes that survive in the finite Schur; R156 + R186). They might be
the same object in two coordinates; that **does not** lower their tractability, but it must be checked before
launching two builders (consistency check: does S_{T,k} contain 𝔊_T as a block?).

---

## 5. Why most of the REF-D entries were indeed transfers

The common pattern (R1, R3, R4, R7, R8): the reformulation leads to a general theory (Kreĭn, Bochner, Toeplitz,
Łojasiewicz, Wiener–Hopf) whose **input hypothesis** is the positivity of the window data. Those theories *consume*
positivity; they do not *produce* it. The corpus theorems proving this are: lem:shape-est (prime estimates do not
reach the margin scale), lem:shape-ident (identities valid for every comb carry no sign), Φ.1 (stability = branch
2), C-pos (i)–(iii), Thm HA/HB. In those cases the «REF-D» dismissal was a verbal shortcut for an existing theorem,
and the conclusion does not change.

What those theories do not cover is the **continuation in T** of a finite-dimensional object or a Λ-free
functional inequality: there, positivity at T₀ (known up to ½log15) is *starting data*, not hypothesis, and what is
missing is a no-crossing property. None of the corpus barriers (thm:shape, Φ200, C-pos, W-*) is a theorem about
continuation arguments: W-det/W-fam rule out pointwise first-order discriminants; thm:shape(A) rules out
deductions valid for the whole class 𝔗₁ — and a no-crossing argument **could** fail for DH/Epstein (which
cross at T ≥ 9/5, T ≥ 1.59), so it is not excluded by lem:transfer: it must use something that distinguishes ζ at
the crossing instant. That is a requirement, not an impossibility.

Honest nuance: lem:transfer implies that the no-crossing lemma **cannot** be uniform over 𝔗₁; it must fail where
F_DH crosses. So the first lemma of R6/R13 must contain a datum that F_DH lacks (e.g. the Euler product at the
rank-one border of the new contact, lem:contA). That is the admissibility condition that must be declared in the
next round.

---

## 6. The three reformulations dismissed only by judgment with their own path, and their first lemma

### 6.1 R13 — (L2) S_{T,k} ⪰ 0 by continuation in T

**Lemma T13.1 (first crossing between contacts; OPEN).** Let (T_j, T_{j+1}) be an interval with no new contacts (k
constant). Then det S_{T,k}, as a real-analytic function of T on (T_j,T_{j+1}), does not vanish; equivalently, the
eigenvector of eigenvalue 0 at a hypothetical crossing T* would satisfy a boundary condition at ±T* (derivative in
T via Hadamard: d/dT of the form = boundary trace) incompatible with the contact block Λ(n_j)δ − du (Prop Θ,
CA_R3_001, PROVED).
**Lemma T13.2 (jump k → k+1; OPEN).** At a contact T_j, S_{T_j,k+1} is obtained from S_{T_j,k} by a rank-one
border (empty entry, lem:contA); by Cauchy interlacing it suffices that the scalar Schur complement of the border
be ≥ 0. First case to do by hand: contact 5 → 7 (CA_R4_001 already reduces this step to a near-cancellation of four
shifted copies at 1.6·10⁻⁶ precision — here it reappears as the scalar complement).
Admissibility filter: T13.1 must fail for F_DH at T ≈ 9/5 (lem:transfer); the next round declares which feature of
Λ prevents it.

### 6.2 R6 — polar capacity g_±(T)

**Lemma T6.1 (Hadamard formula for g_±; probably PROVED with standard work).** dg_±/dT = −|∂_n u_±(T)|²
+ (explicit polar term), with u_± the extremal of the capacity. Theorems: Hadamard domain variation; Kato
for simple eigenvalues.
**Lemma T6.2 (no-crossing; OPEN).** If g_+(T*) = 0 then u_+ is simultaneously extremal of 𝔊_{T*} and an element of
the enlarged radical; show that this forces u_+ ∈ 𝒢̄_{T*}, a contradiction with the polar normalization. Risk: that
T6.2 is R4 (A_⊥⊥(1) ⪰ 0) in another coordinate; first check with LEMMA_I3_001 whether 𝔊_T is a block of A(1).

### 6.3 R10 — Lemma F on the half-line

**Lemma T10.1 (cheap falsification; NUMERICAL strictly necessary).** Evaluate 2‖Z_log r‖² + 2⟨Zr,Z_{log²}r⟩ on a
family of admissible r far from the extremal (prolate basis, first 12 modes — arena ≥ 12, phase 155 r6). If
negative: Lemma F dies as a uniform inequality and remains only at the extremal (close it).
**Lemma T10.2 (three lines with boundary; OPEN, pure analysis).** For r supported on (λ,∞), the function
ε ↦ log‖Z^{(ε)}r‖² is convex in a neighborhood of 0 whenever the boundary trace of r at λ satisfies a Hardy
condition (‖r(λ)‖ ≤ C ℓ(r)^{½}). Tool: Stein interpolation on the strip with the boundary λ treated as an error
term controlled by the leak; the constant c ≈ 2.1 from F0_TEST gives the budget.
Filter: Lemma F has no Λ; the splice with the interior (A_MU (f)) is where Λ enters and must be declared.

---

## 7. Answer to the original question: «did we grossly err, and did some dismissed tool actually work?»

**Partial. Not grossly; yes, a bounded method error.**

Argument for «not gross»: (1) of the 13 reformulations reviewed, 5 (R4-Horn, R5, R8, R9, R11) were closed
by a theorem or explicit falsifier, not by the label; (2) 4 others (R1, R3, R4-block, R7) are transfers: the
general theory that makes them «classical» requires as input the positivity of the data, and that is backed by
corpus theorems (lem:shape-est, lem:shape-ident, Φ.1, C-pos (i)–(iii)); (3) no dismissed tool closes D: there is no
reformulation in the corpus with an almost-complete proof that was abandoned.

Argument for «yes there was an error»: (1) the index never recorded tractability, and ≈350 REF-D entries were in
fact treated as closures, against its own header; (2) three reformulations (R13, R6, R10) have a missing hypothesis
*distinct from the sign* — a no-crossing in T of a finite object, or an interpolation inequality without Λ — and
were filed by judgment («REF-D», «comb models», family change), not by theorem; (3) no corpus barrier
(thm:shape, Φ200, C-pos, walls W-*) addresses **continuation arguments in T from the known boundary**
(½log15); lem:transfer only requires that the no-crossing step not be uniform over 𝔗₁, which is a design
condition.

What I am not claiming: that R13/R6/R10 are easier than D. I am claiming that they have a concrete first lemma
whose statement is not D, and that they were never attempted. Row D: OPEN. L′♯: OPEN.

**Proposal for the index (for the coordinator to copy):** «Phase 204 (TRACT_001): tractability review of 13
REF-D reformulations. 5 closed by theorem, 4 transfers (general theory consumes PD), 3 dismissed only by judgment
with their own path: (L2) S_{T,k} by first crossing/interlacing (T13.1–2), polar capacity g_± by Hadamard +
no-crossing (T6.1–2), Lemma F by three-lines with boundary (T10.1–2). New column recommended for the index: TRAT
(yes/transfer/no). No new NO-GO.»
