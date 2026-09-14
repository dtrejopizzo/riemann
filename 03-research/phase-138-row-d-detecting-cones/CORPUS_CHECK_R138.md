# CORPUS_CHECK_R138 — was any of this tried already?

Purpose: before building phase 138 (D.15–D.18), verify against 03-research/ (~137 phases),
04-papers/, 05-meta-and-planning/, and NO-GO-LIST.md which of the nine candidate ideas were
already attempted, with what verdict, so the phase does not re-derive or re-open closed routes.
Method: `grep -rn -i` with synonyms, then read the surrounding passage. Quotes below are verbatim
except where translated (Spanish originals marked).

---

## 1. Pólya's criterion / convex-decreasing test functions / triangle & box functions as Weil test functions

**Status: NEW at the level of "is C_Pó detecting" — but the criterion itself and the triangle-family
computation are already staged as the phase's own D.17, not found attempted in any earlier phase.**

- Pólya's criterion (even, `h(0)=1`, convex decreasing on `(0,∞)`, `h→0` ⟹ positive definite) appears
  in the corpus only inside the phase-138 blueprint itself:
  `03-research/phase-138-row-d-detecting-cones/R138_000_LEAD_BLUEPRINT.md:89-91`:
  > "**Pólya's criterion (CLASSICAL, Pólya 1949; Lukacs, *Characteristic functions*, Thm 4.3.1):** an
  > even real function `h` with `h(0) = 1`, convex and decreasing on `(0,∞)`, `h → 0` at `∞`, is positive
  > definite ... Define the **Pólya cone** `C_Pó` ..."
  No earlier phase (0–137) defines this cone or runs the triangle-function (`h_T=(1-|t|/T)_+`)
  computation; grep for "Polya cone", "convex decreasing", "triangle test function" outside
  phase-138 returns nothing relevant except the unrelated Laguerre–Pólya-class material (item 9
  below) and a generic mention in `03-research/phase-16/00-SURF-SPEC-SHEET.md` (survey list, not
  attempted).
- The blueprint pre-computes the outcome it expects (D.17.3): the sign on `C_Pó` reduces to the
  PNT error term (see item 2) — this is a *prediction*, not yet a recorded result, since no builder
  round exists in phase-138 yet (`ls 03-research/phase-138-row-d-detecting-cones/` shows only
  `R138_000_LEAD_BLUEPRINT.md`).

**Recommendation:** build. Nothing to reuse; this is the phase's own open task (D.17). Do not
duplicate — proceed straight to the D.17.2/D.17.3 computation the blueprint already lays out.

---

## 2. Chebyshev/Mertens bounds ⟹ unconditional Weil positivity; PNT error identified as the obstruction

**Status: TRIED–NO-GO (route no-go, general form), confirmed independently in at least two phases.**

- `03-research/phase-114-closing-the-four-rows/114_d_185_PNT_TATE_LOW_BLOCK_NOGO.md:1,58` (= identical
  file duplicated under phase-116's `previous-phase-114/`):
  > "# D.185 — PNT plus two Tate moments cannot close the low block ... Thus no theorem whose
  > arithmetic hypotheses are only a PNT remainder and two linear moments can prove the needed
  > low-block bound. ... This is a route no-go, not evidence that the actual `Λ` violates the
  > desired inequality." (lines 1, 46-58)
  Mechanism: even the RH-conditional bound `A(x)=O(√x log²x)` is too weak on the required band; the
  classical (unconditional) PNT error is *weaker still*, and an explicit signed perturbation is
  built that satisfies the PNT remainder and the moment constraints while still spiking — i.e. PNT +
  finitely many moments provably cannot certify the sign.
- `03-research/phase-72-feshbach-leakage-calculus/E72_49_BANDLIMITED_PNT_ENDPOINT_THEOREM.md:27,133-139`:
  > "This is a tiny bandwidth compared with the strength of the classical PNT error." ... "The
  > obstruction is the factor: [classical PNT error]."
- Phase-138's own blueprint already anticipates this exact obstruction for the Pólya cone
  specifically (D.17.3): "the remainder is `Σ_ρ Φ_h(ρ)` itself ... i.e. the PNT error term of size
  `e^{T/2−c√T}` which dominates every unconditional term."

**Recommendation:** do not reopen as a route to unconditional positivity via Chebyshev/Mertens-type
bounds alone; reuse `114_d_185`'s no-go mechanism (signed perturbation saturating PNT-remainder +
moment constraints while still spiking) as the ready-made falsifier for D.17.3 if the corpus wants a
rigorous "no structural cancellation" proof rather than an informal remainder identification.

---

## 3. Hodge index / Lorentzian signature / Khovanskii–Teissier / effective-nef cone / log-concavity

**Status: TRIED–PARTIAL (surveyed extensively 04-papers/00-references + phases 15, 107, 108, 113,
120, 122; genuine sign-definite Hodge index theorems exist only on *tropical/combinatorial* stand-ins,
never on the arithmetic object itself — this is the corpus's chief standing gap, not a no-go).**

- `03-research/phase-136-row-d-map/MAP_5_LITERATURE_VS_CORPUS.md:40-46,84-90` (produced specifically
  to answer exactly this question against the literature):
  > "The second hit is **Cartwright's *Combinatorial Tropical Surfaces*** (1506.02023): an
  > intersection pairing on Néron–Severi classes ... proved non-degenerate with **at most one
  > positive eigenvalue** — a literal Hodge index theorem ... This is not `Spec Z̄ × Spec Z̄`."
  > "The tropical Hodge index theorem (Cartwright 1506.02023) and tropical Hodge–Riemann relations
  > (2007.07826) are absent from the corpus's own literature engagement ... despite this being the
  > one source ... that proves a genuine, sign-definite 2-dimensional Hodge index theorem on a
  > combinatorial stand-in object. This is a real candidate the corpus's own map never entered."
- `03-research/phase-113-the-trace-on-schwartz-data/113_10_THE_DEGREE_MAP_AND_THE_EFFECTIVE_CONE.md`
  constructs the effective cone and degree map used verbatim by phase-138's own `Definition 0.1` /
  `E := {F ≥ 0}` (line 137 "## 2. The effective cone").
- `03-research/phase-107-arithmetic-lefschetz-reconstruction/107_241_HODGE_INDEX_FOR_THE_CORNER_PAIRING.md`
  and `107_229_NORM_ADAPTED_PRO_DIMENSION_ON_THE_TWO_RULINGS.md` attempt a Hodge index statement for
  a "corner pairing" on the two-rulings structure — same rulings language phase-138 D.15 reuses.
- NO-GO-LIST `[MW-5]` (line 214 area, "Connes–Consani arithmetic-site wall") records: "Phase 113
  proves the missing positive intersection form cannot be built inside the natural Schwartz-data
  class (O1–O3), and that the one remaining input is equivalent to RH exactly."

**Recommendation:** build, but reuse: MAP_5's tropical-Hodge-index citation (Cartwright /
Adiprasito–Huh–Katz) as the structural model for D.15.2's "Lorentzian criterion," and reuse 113_10's
effective-cone construction verbatim (phase-138 already does, per Definition 0.1 / D.15.2). Do not
re-litigate whether a *literal* arithmetic Hodge index theorem for `Spec Z̄ × Spec Z̄` already exists —
it does not (confirmed absent across every primary source in MAP_5); phase-138's `Q = I_∞` route
around this via the "detecting cone" reduction is a genuinely new angle, not a duplicate.

---

## 4. Sufficiency / detection theorem (Theorem F, Paper 45 Thm 10.4/11.3; Landau's lemma; finite-window
insufficiency)

**Status: TRIED–PROVED (Theorem F is a standing, cited theorem) + TRIED–NO-GO (finite windows don't
detect, Connes–Consani cluster).**

- `04-papers/45-row-c-explicit-formula/main.tex:200,1995` states Theorem F verbatim ("Theorem F
  (Theorem~\ref{thm:sufficiency}; sufficiency)" ... "\begin{theorem}[sufficiency; Theorem F]"),
  reused by phase-138's own blueprint line 25-26: "Theorem F (Paper 45 Thm 11.3): if `ξ(ρ_0) = 0`
  with `Re ρ_0 ≠ ½` there is a real primitive `F ∈ C_c^∞` with `I_∞(F,F) > 0`."
- The complementary no-go — that a *finite window* of test functions cannot detect an off-line zero
  — is exactly the Connes–Consani `2T ≤ log 2` result (see item 6) and is cited by phase-136's map
  as "cluster B ... no finite window detects" (`R138_000_LEAD_BLUEPRINT.md:39-40`, referencing the
  phase-136 map).

**Recommendation:** reuse Theorem F directly (already imported as RESTATEMENT/PROVED-IN-REPOSITORY in
the blueprint) — do not re-prove; the phase-138 task is precisely to find the *cone* under which
Theorem F's annihilator classes coincide with a structurally signed cone, which is open, not settled.

---

## 5. Translations / support growth (unbounded support needed to detect; `e^{a|u|}` growth at off-line
zeros; bounded-support detectors)

**Status: NEW. No occurrence anywhere outside phase-138.**

- `grep -rn "e^{a|u|}\|unbounded support.*detect\|bounded.support.*detect" 03-research` (excluding
  phase-138) returns **no hits**. The `e^{a|u|}` growth argument and the translation-closure question
  (D.16) are original to phase-138's blueprint (`R138_000_LEAD_BLUEPRINT.md:65-85`, D.16 items 1-2).

**Recommendation:** build. This is genuinely new ground; there is no risk of duplicating prior work,
but also no prior result to reuse — the phase must derive the translation/growth statement from
scratch, exactly as D.16 specifies.

---

## 6. Connes–Consani archimedean positivity, window `2T ≤ log 2`; attempts to extend beyond `log 2`

**Status: TRIED–PROVED (the `log 2` window itself, unconditional, interval-certified) and
TRIED–NO-GO / TRIED–PARTIAL for every attempt to extend past it.**

- The certified result: `03-research/phase-118-the-exact-threshold-inequality/W4_CERTIFIED_RANGE.md:333-336`
  ("## 5. Strongest unconditional, interval-certified theorem" / "`A_T >= 0` for all `0 < T <= log 2`.")
  backed by `04-papers/42-arithmetic-lefschetz-programme/main.tex` `thm:certifiedendpoints`.
- The next-threshold attempt, `T=(1/2)log 5`, was explicitly tried and retracted:
  `W4_CERTIFIED_RANGE.md:219-238`:
  > "**The very next threshold, `T = (1/2)log 5`, was already attempted — and explicitly
  > retracted** ... 'Neither inequality follows from the five-column calculation.' ...
  > `main.tex:6202` and the `row_d_log2/README.md` both state plainly: `T=(1/2)log5` is **not**
  > certified and no artifact claims it." This is recorded as "an incomplete proof," not a disproof.
- Structural diagnosis of *why* extension is hard, not impossible:
  `W4_CERTIFIED_RANGE.md:277-283`: "Does it have room to extend? Structurally yes — nothing in the
  technique is intrinsically capped at `log 2`. But each new threshold requires, from scratch: [new
  coercive complement bound; new near-null direction; fresh bespoke capacity argument]" — i.e. no
  mechanical extension, escalating bespoke work at every step, with float diagnostics (no certified
  contradiction) up to `T ≈ 2 log 2 ≈ 1.386` showing no sign violation.
- Literature side, MAP_5 (item 3 above) confirms Connes–Consani's own paper names the missing
  object ("an intersection theory of divisors on the square of the Scaling Site ... still in
  development") and that the archimedean obstruction is explicitly unresolved by the authors
  themselves (`MAP_5_LITERATURE_VS_CORPUS.md:16,26-38`).

**Recommendation:** do not reopen extending `T > log 2` as a research target inside phase 138 — reuse
the `log 2` certificate as a hard, already-proved data point (a genuine detecting-adjacent structural
cone bounded exactly at `log 2`), and reuse `W4`'s diagnosis of *why* extension needs a fresh bespoke
argument per threshold as evidence for D.16's claim that a *finite* window is never closed under the
needed operations without escalating cost.

---

## 7. Hilbert–Pólya (self-adjoint operator with spectrum the zeros)

**Status: TRIED–NO-GO, repeatedly, "wrong sign" — recorded as a Master Wall. Listing only to avoid
reopening, per the task's own instruction.**

- NO-GO-LIST `[MW-4]` (`NO-GO-LIST.md:214-219` area):
  > "**[MW-4] Hilbert–Pólya wall (wrong sign)** — Every unconditional tool on ζ gives a LOWER bound
  > on positivity. RH is an UPPER restriction (we need λ_min(Q) ≥ 0). ... Confirmed in 8 independent
  > paradigms: explicit-formula/Kreĭn, per-place, Carleson, pair correlation, Connes prolate, heat
  > flow, cohomological Hodge, hyperbolicity."
- NO-GO-LIST `[NG-E5]` (`NO-GO-LIST.md:173-176`):
  > "**[NG-E5] Hilbert–Pólya via OS reconstruction "for free"** — Attempted: from OS reflection
  > positivity + the reconstruction theorem, claim H ≥ 0 automatically. Why it fails: RETRACTED. The
  > two-point function is oscillatory, NOT OS-decreasing."
- Other named phase attempts: phase-16 (Pontryagin/OS), phase-6 (M-OS-1/2, retracted), phase-64
  ("Connes route"), phase-71 (CCM zeta spectral triples, partial reduction, not closed — MAP_3 line
  50), phase-106 (white-light GNS, "no-sign theorem," item 3 above).

**Recommendation:** do not reopen; Hilbert–Pólya-style self-adjoint reconstruction is a closed Master
Wall (MW-4) — any phase-138 cone construction must not covertly rely on "positivity gives a spectral
realization for free" (exactly NG-E5's error).

---

## 8. Radical of the polar/Tate block; primitive sector `P`; rulings `e_±`; hyperbolic plane
`[[0,1],[1,0]]`; `K^⊥`; degree-zero classes

**Status: TRIED–PARTIAL / building blocks already proved; phase-138 D.15 is a genuine restatement/
sharpening, not a duplicate.**

- The two-rulings / hyperbolic-plane structure and the radical are already built in phase 113:
  `03-research/phase-113-the-trace-on-schwartz-data/113_08_THE_TWO_RULINGS_AND_THE_INDEX_ENGINE.md:146`:
  > "rulings are the fibre classes, they are isotropic, they meet once, and their [pairing forms the
  > hyperbolic plane]" (index-engine construction reused verbatim by phase-138's `deg⁺`, `deg⁻`,
  > polar block `B_pol = [[0,1],[1,0]]`).
  `113_09_THE_RADICAL_IS_THE_XI_IDEAL.md` already identifies the radical `𝓝_∞` with the `ξ`-ideal
  (Frobenius translates of `ΠK`), which phase-138's blueprint cites directly (`𝓝_∞ ⊇ Λ_W`).
- Phase 107's `107_241_HODGE_INDEX_FOR_THE_CORNER_PAIRING.md` and `107_24_PAPER_C_PRIMITIVE_DEGREE_ZERO_REDUCTION.md`
  already attempt a primitive/degree-zero reduction with a corner-pairing Hodge index statement (same
  shape as D.15.1-2, on an earlier candidate object).
- `03-research/phase-15/M3-arithmetic-hodge-index.md`, `M2-ample-cone-edge-positivity.md` are the
  earliest (phase-15) attempts at exactly this ample-cone / Hodge-index characterization, superseded
  by the 107/113/135/137 machinery phase-138 now builds on.

**Recommendation:** reuse 113_08/113_09's radical-is-`ξ`-ideal and two-rulings/hyperbolic-plane
results directly as the starting data for D.15.1 (phase-138 already does this implicitly via its
`§0` restatement) rather than re-deriving them; D.15's novel content is the *Lorentzian criterion*
(D.15.2) connecting this to reverse Cauchy–Schwarz on the effective cone, which is not present in
107/113/15 verbatim and should be built.

---

## 9. Laguerre–Pólya class / Jensen polynomials / Turán inequalities / Li's criterion / Keiper

**Status: TRIED–EQUIVALENT-TO-RH (classical restatement, not a new route) — recorded in phase 28, and
independently flagged as RH-equivalent / insufficient at several later phases (101, 103, 104). Avoid
re-deriving the equivalence as if it were new; do not expect these criteria to give unconditional
progress.**

- `03-research/phase-28/07-lp-class-rh.md` (full document is the corpus's canonical treatment):
  > "**Consecuencia directa de la Proposición 2:** `RH ⟺ f(t) = ξ(1/2+it) ∈ LP`." and "*Observación
  > histórica.* Esta equivalencia es la reformulación de de Bruijn (1950)." Also: "**Proposición 3**
  > (el muro final) ... Eliminar la posibilidad de pares complejos ES probar RH" (the wall is exactly
  > RH again).
- `03-research/phase-101-covariant-bordered-current/E101_076_JET_WRONSKIAN_LITERATURE_AND_PARITY_GATE.md:15,317`:
  > "classical Laguerre--Polya or Jensen criteria, and therefore RH-equivalent" ... "The
  > Polya--Jensen criterion gives [restatement, not new leverage]."
- `03-research/phase-103-direct-a1-closure/103_29_THETA_MLR_LOG_CONCAVITY_AND_SQUARE_NO_GO.md`,
  `103_34_FIRST_JENSEN_MINOR_FOR_THETA.md`, `103_36_CUBIC_JENSEN_DISCRIMINANT_GATE.md`,
  `103_39_CUBIC_GATE_COVARIANCE_AND_STRONG_CURVATURE_NO_GO.md` — a sustained attempt (phase 103) to
  get unconditional progress from Jensen-polynomial/Turán-inequality machinery on the theta kernel;
  titles ending "_NO_GO" record the outcome directly.
- `03-research/phase-104-unconditional-a1-closure/104_83_XI_FOURIER_DEEP_GATE.md`,
  `104_86_BOSE_MELLIN_SINE_REFLECTION_GATE.md` continue the same theta/Jensen line without closing it.

**Recommendation:** do not reopen Laguerre–Pólya/Jensen/Turán/Li/Keiper as a route to an unconditional
sign; they are classical restatements of RH (phase 28) whose only unconditional descendant attempts
(phase 103/104, theta-kernel Jensen minors) are recorded no-gos. If phase 138's `t`-concavity /
curvature language (`𝒞(t) = (ξ'/ξ)'(1/2+it)`) resurfaces, cite phase-28 directly rather than
re-deriving the LP-class equivalence.

---

## Summary table

| # | Idea | Status | Key file(s) | Recommendation |
|---|---|---|---|---|
| 1 | Pólya criterion / convex-decreasing cone, triangle/box test fns | NEW (staged as own D.17) | `phase-138/R138_000_LEAD_BLUEPRINT.md:87-119` | build |
| 2 | Chebyshev/Mertens ⟹ unconditional Weil positivity; PNT error obstruction | TRIED–NO-GO | `phase-114/114_d_185_PNT_TATE_LOW_BLOCK_NOGO.md`; `phase-72/E72_49...md` | do not reopen as unconditional route; reuse no-go mechanism |
| 3 | Hodge index/Lorentzian/Khovanskii–Teissier/effective cone | TRIED–PARTIAL | `phase-136-row-d-map/MAP_5_LITERATURE_VS_CORPUS.md`; `phase-113/113_10...md`; `phase-107/107_241...md` | build; reuse effective-cone (113_10) and tropical-Hodge citation (MAP_5) |
| 4 | Sufficiency/detection theorem (Theorem F); finite-window insufficiency | TRIED–PROVED / TRIED–NO-GO | `04-papers/45.../main.tex:200,1995`; CC window (item 6) | reuse Theorem F, do not re-prove |
| 5 | Translation/support growth `e^{a\|u\|}` | NEW | none outside phase-138 | build from scratch |
| 6 | Connes–Consani window `2T ≤ log 2`; extension attempts | TRIED–PROVED (window) / TRIED–PARTIAL (extension) | `phase-118/W4_CERTIFIED_RANGE.md` | do not reopen extension; reuse certified `log 2` bound as data point |
| 7 | Hilbert–Pólya self-adjoint realization | TRIED–NO-GO (Master Wall) | `NO-GO-LIST.md` MW-4, NG-E5 | do not reopen |
| 8 | Radical/primitive sector, rulings, hyperbolic plane, K^⊥ | TRIED–PARTIAL (building blocks proved) | `phase-113/113_08...md`, `113_09...md`; `phase-107/107_241...md`, `107_24...md` | reuse 113_08/09 as D.15 starting data; build the Lorentzian criterion (new) |
| 9 | Laguerre–Pólya / Jensen / Turán / Li / Keiper | TRIED–EQUIVALENT-TO-RH / TRIED–NO-GO (unconditional descendants) | `phase-28/07-lp-class-rh.md`; `phase-103/103_29...md` etc. | do not reopen; cite phase-28 if curvature language recurs |
