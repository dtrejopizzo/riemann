# Phase 136 — the map of where not to go, what it proves, and the plan for row D

Author: session lead (Fable 5.1). Date: 2026-09-13. Inputs: MAP_1 (walls and master
documents), MAP_2 sectors (phases 0–60), MAP_3 sectors (61–110), MAP_4 (111–135 and
Papers 42–46), MAP_5 (literature vs corpus), LEAD_NOTE (off-the-page candidates), and
Connes–Consani 2006.13771 read from source. All sector reports were produced by
Sonnet-class agents with grep-verified quotes; the synthesis and the decisions are mine.

## 0. Thermometer

Row D is about 20% built as a *frame* and 0–5% as *difficulty*. The frame (Paper 46):
target proved equivalent to RH; Weil completion; canonical class `K`; radical; affine
duality; transfer theorem "`h⁰` with (a),(b′),(c) ⇒ RH"; falsifier theorem for `Ξ_a`.
The difficulty is one object: a dimension of sections `h⁰` on the square
`Spec Z̄ × Spec Z̄` with a Riemann–Roch inequality whose quadratic term is `I_∞(E,E)`.
Everything the corpus can currently define grows logarithmically or linearly where
`¼m²` is required.

## 1. The grid

Roughly 200 distinct mechanisms across 135 phases were classified. Counts (MAP_1 for
the master lists; sector maps for phases): PROVED-IMPOSSIBLE ≈ 47 + ~40 (almost all are
impossibilities of *specific* constructions, not of ideas); EQUIVALENT-TO-RH ≈ 21 + ~45;
ABANDONED ≈ 22 + ~25; NUMERICAL-ONLY ≈ 4 + ~10; PARTIAL-SUCCESS ≈ 25.

Clusters, by mechanism, and the single reason each cluster dies:

| cluster | representative attempts | why the whole cluster dies |
|---|---|---|
| A. Analytic reformulations of positivity | Krein index, Pick passivity, Nevanlinna/Hermite–Biehler, Cesàro/DBN flow, Hardy constants, AHM/Cauchy–Weil, Wiener–Hopf factor, Abel boundary, Li kernels, entropy extremality, Pontryagin C1–C7, Laplace pole, Herglotz on ξ'/ξ | each is RH restated; the explicit formula is a *bijection* between primes and zeros, so no side carries independent leverage (phase 34 Doc 90; phase 64 letter) |
| B. Finite-window / compression positivity | CCM ground state, GLT symbols, Galerkin, Toeplitz, quaternionic HR on `V₊`, finite Euler colligations `K_P ⪰ 0` | positivity is *free* at finite rank and *gapless* as rank grows (`e^{−cL}` cascade); "a spectral gap needs finitely many eigenvalues; ζ has infinite genus" (phase 63 E99). Galerkin values are variational upper bounds (phase 134) |
| C. Geometric/cohomological realizations | Deninger foliations, Kähler–Riemann polarization, Morishita space, KK canonical metric, homotopy inertia, quantum import, functor constructions | the object (Frobenius on a Weil cohomology of `Spec Z`) is not realized; every realized witness either has no complex structure or uses the Hasse analogue (`|ξ|²=q`) as input, i.e. RH (phase 43 Doc 130) |
| D. Magnitude / density / averaging methods | large sieve, pair correlation, zero-density, mollifier floors, Cesàro-in-λ, Farmer floor | **theorem of method obstruction** (phase 60): any bound using only `\|Λ(n)\|` cannot decide the sign, because Davenport–Heilbronn has the same magnitudes and the opposite sign; the sign lives in the *phase coherence* of `cos(t log n)`; off-line zeros give secular growth `λ^{2β−1}` no average removes |
| E. Direct constructions of a nonnegative invariant | Paper 46 §6 negatives; convex-set dimension; one-parameter lattice `Λ_W`; tropical toy square | model-free definitions transfer to `Ξ_a` (Restatement 12.4a); the one lattice tried has logarithmic growth (Thm 13.6); the tropical toy reproduces Hodge index on a finite sublattice but dimensions become real on continuous correspondences (phase 40–41) |

**What is genuinely proved positive, unconditionally** (the "unpainted-but-lit" squares):
1. Archimedean-only Weil positivity for `supp ⊂ [2^{−1/2}, 2^{1/2}]` (Connes–Consani; phase 118 `T ≤ log 2`; phase 5 Thm 6.11 citation).
2. Single-prime local purity: Axiom H holds for `F_{p,α}` **iff** `|α| = √p` (phase 44 Doc 131 Thm 6.7).
3. **Two-primes theorem** with incommensurable periods, extended to `n` primes: Weil positivity for the prime-only object **iff** bilateral purity (phase 45 Doc 135 Thms A, A′, B) — *without* archimedean/polar block.
4. Finite Euler colligations `K_P ⪰ 0` from `Λ ≥ 0` + local Tate passivity (phase 64).
5. `Γ₂ ≥ 0` curvature of the prime Dirichlet form, marginal (`ψ(0)=0`), no gap (phase 64).
6. Tropical toy `C_p × C_p`: exact Hodge index `(1,2)` on `⟨f₁,f₂,Δ⟩` (phase 41 Doc 125).
7. Möbius connection identity `V_Λ = Z^{−1}δZ` (non-circular construction of the prime current), with the dissipativity inequality open (phase 70).
8. Paper 46 Part II: transfer theorem, canonical class, radical, `Ξ_a` inconsistency.

## 2. What the map proves (a meta-theorem, stated once)

Every unconditional positivity in the corpus is either **prime-only** (and holds by purity
= unimodularity of local roots) or **archimedean-only** (and holds by Connes–Consani's
analysis of the small square `∆`). Every reformulation of the **coupled** statement —
archimedean/polar block *plus* infinitely many primes — is RH. Therefore:

> **The sign is the interaction term between the polar/archimedean block and the
> Frobenius lattice, and it is a phase-coherence phenomenon of unimodular local roots.**

Three independent formulations of the same fact exist in the corpus and were never
put side by side: phase 60's "phase not magnitude" obstruction theorem; Paper 46's
Restatement 12.4a ("no model-free derivation; the datum is `Frob_n ⋆ Frob_n^† = Δ^{(n)}`");
Connes–Consani's "the obstruction lives in the small square `∆`, moved into `Σ` to use its
infinite reservoir of positivity" (2006.13771, §1–2, §4). In Paper 46's language the three
coincide: `∆` is the polar packet `K`, `Σ` is the Frobenius lattice inside the radical, and
the trace-remainder `δ(ρ)` of CC (8) is the 2×2 Tate block `Σ(T)` of P124.013.

Consequence for any future `h⁰`: its definition must **couple** `K` to the Frobenius
lattice through an object that (i) is not model-uniform, (ii) grows quadratically, and
(iii) reads unimodularity. No object in the corpus does all three; several do two.

## 3. No-gos to reopen (they were wrong, over-generalized, or never audited)

| item | verdict | action |
|---|---|---|
| MW-5 / R16 "no quadratic Riemann–Roch over `Spec Z`" | over-generalized: answered only for CC's *curve* object; the square was never tested; Paper 46 Thm 12.3 needs only `h⁰ ≥ 0`, not integrality | **reopened** (this campaign) |
| P122.007 "arithmetic Hodge index not applicable" | correct as an *import* ban; never asked whether the Hilbert–Samuel **mechanism** (fibre rank × archimedean size) can be rebuilt on the `S`-square | reopened as D-HS (LEAD_NOTE §1) |
| Phase 65 `RH-PROOF.md` (Vitali/Montel strip-crossing capstone, self-styled "complete, RH-free chain") | **never audited**; uses the same strip-crossing extension that the same phase's D8.5b-i refutes for a parallel object; MAP_3 flags it as the strongest circularity concern in the corpus | **mandatory hostile audit** (a purported proof cannot sit unaudited in the repository) |
| GAP-135.B (semilocal object with `a ≥ 0` and polar block, "next document") | never written | reopened (S2 below) |
| ES-8 signed `ψ(x) − x` route | only the absolute-value route is closed | admissible, low priority |
| Phase 62/63 "gapless" verdicts | float64 noise floor, not theorems; the analytic statement "margin → 0" is heuristic | not reopened as a route (cluster B), but the analytic gaplessness theorem is a clean target for a later note |
| E67.8 "no state on the multiplicative semigroup algebra carries log-distance coherence" | explicitly left open, not proved | recorded; touches D-HS transport |

## 4. Squares not painted, ranked by decidability × relevance

**S1 — Item (23): growth of `h⁰_Z(mK)` on the full Frobenius lattice.** Remark 13.6b's
near-parallel generators are exactly the mechanism that could give super-logarithmic
growth (integer Dirichlet combinations `Σ c_n τ_{log n}(ΠK)` approximating smooth
functions — Nyman–Beurling territory). Decidable by pure analysis; either outcome is a
theorem; a quadratic outcome would make `h⁰_Z` an (a)+(b′) candidate with (c) as the
only open clause. Tools: Lemma 13.5b's Mellin positivity on the real axis, Beurling–
Malliavin-type density for the exponents `log n`, lattice-point counting in the convex
set `C_m`. Falsifier: run the same count for `Ξ_a` weights.

**S2 — GAP-135.B: semilocal Weil positivity with the polar block.** Extend Doc 135's
`n`-prime purity theorem to the object `S ∪ {∞}` with the polar packet `K` subtracted:
`W_S(F) := Σ_{v∈S} W_v(F⋆F^∨) − 2Φ_F(0)Φ_F(1)`. Determine exactly for which supports and
which `S` this is a theorem (Connes' semilocal trace formula gives positivity of the
*trace*; the polar term is what must be paid), and where the first failure happens as `S`
grows. This is the corpus's coupled statement at finite `S`; its `S`-dependence is the
quantitative shadow of the sign, and the only place where unimodularity and `K` meet in
a *provable* inequality.

**S3 — Connes–Consani's intersection theory on the square of the scaling site.** Read
[12],[16] of 2006.13771 and their later papers (2401.08401, 2602.15941) from source, and
write the dictionary with Papers 43–46: Schwartz kernel of scaling ↔ divisor of the
Frobenius correspondence; trace ↔ intersection with the diagonal; `∆`/`Σ` ↔ polar
packet / Frobenius lattice; trace-remainder ↔ Tate block. Aim: state the intersection
form on divisors of the square in the corpus's normalization and check whether `I_∞` is
it. Decidable (a comparison), and it either imports CC's `∆ → Σ` positivity mechanism into
row D or shows the exact term it cannot pay (the prime principal values).

**S4 — D-HS: `H⁰` on the `S`-square by fibre-wise CC cohomology and Frobenius transport**
(LEAD_NOTE §1, kill tests T1–T5). New; nothing like it in the corpus or the literature
(MAP_5: no source constructs sections on the square). It is the only candidate whose
*definition* contains unimodularity (isometric transport) and whose *shape* multiplies two
linear factors. High risk at T1 (definability); the risk is the research.

**S5 — Cartwright's tropical Hodge index and tropical Hodge theory** (MAP_5): the
phase-41 toy matched Hodge index exactly; the obstruction was infinite rank and real
dimensions. Check whether the chart squares `C_S × C_S` are "combinatorial tropical
surfaces" in Cartwright's sense; if so, a *chart-level* Hodge index exists — to be compared
with Paper 43 Thm 14.1 (no Hodge-index shape at charts for the *numerical* form). Medium.

**S6 — The factorization `𝒯 = A^*A` / Wiener–Hopf `D_Euler` / the norm `(H,π,Ω)`**: three
names for the same off-the-page object (phase 4 RH-ENDGAME, phase 70 E70.9, Paper 46
Thm 3.7). Never engaged. It is the target, not a route; recorded so it is not re-derived.

**S7 — Deninger without Hasse** (ENUNCIADO-MÍNIMO-130), Witt-profinite polarization,
Morishita's space: geometric, unrealized, highest cost. Not this campaign.

## 5. The decision: squares or outside the page?

The analytic page is fully painted: the map shows ~65 RH-equivalent reformulations and a
proved obstruction to every magnitude-only method. Further analytic squares cannot hold
the sign. The geometric page has one unrealized object (MW-5), named identically by
Connes, Deninger and this corpus; it is off the page and no ingredient for it exists.
The **arithmetic-counting page** — Riemann–Roch with a dimension of sections on the
*square* — is nearly blank: CC's curve theorem (2022), Paper 46 §13's one lattice, and
the phase-41 toy. All its ingredients exist (CC's `H⁰` via additive adeles; row B's
Frobenius correspondences and integral shadow; Paper 46's `K`, radical and transfer
theorem; CC's own "divisor of the Frobenius correspondence" dictionary). Nobody has
defined `H⁰` of a divisor on `Spec Z̄ × Spec Z̄`.

**Decision.** Row D continues on the arithmetic-counting page, off the painted region but
with existing ingredients: S1 → S2 → S3 → S4, each a decidable theorem-or-refutation,
with S5 as a side check. The genuinely new mathematics to create is S4; S1–S3 are the
measurements that tell us whether S4 can have quadratic growth and where the polar
block is paid. No campaign target is "prove the sign".

## 6. Phase 136 campaign design

Rules: builder + hostile auditor every round; lead as audit of record with independent
derivations written before reading; labels as in phases 131–135; numerics only as
identity checks with a fast mode; every theorem run against `Ξ_a` and Davenport–
Heilbronn; nothing defined through the zeros' location; a theorem valid for `Ξ_a`
carries no sign and says so.

Round 0 (lead): blueprint R136_000 with S1–S4 as theorems D.11–D.14 and the mandatory
hostile audit of phase 65 `RH-PROOF.md` as item D.0.
Round 1 (builder): D.0 audit report; D.11 (S1) full-lattice growth — theorem or refutation;
D.12 (S2) semilocal positivity with polar block — exact scope; D.13 (S3) dictionary.
Round 2 (hostile), round 3 (builder repairs), round 4 (hostile confirmation), lead decision.
Round 5+ (only if D.11 gives super-logarithmic growth or D.12 gives a positive scope
beyond `log 2`): D.14 (S4) definability T1 and growth T2.

Deliverable: Paper 46 Part III (§§17–20) or a new Paper 47 if S4 is definable; phase
README; PLAN paragraph; memory. Honest expected outcome: theorems that locate the
sign's cost quantitatively (S1, S2), a dictionary that makes CC's mechanism usable in the
corpus's normalization (S3), and a decision on S4's definability. Not a sign.
