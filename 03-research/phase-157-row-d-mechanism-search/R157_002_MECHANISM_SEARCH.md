# R157_002 — The mechanism search under the proved filters F1–F5

*Phase 157, round 1, task 2 of `R157_000_BLUEPRINT.md`. Pure mathematics; no computation was run.
No sign is claimed for ζ at any window. Row D has no label; nothing here changes a label. The form is stated each
time: **primitive** = `λ^A_T = λ_min(A_T|P_T)` (`RD_T`), **complete** = `λ^W_T` (Weil form `W_T` on `L²(I_T)`).
Papers and READMEs were not edited.*

Sources read for this memo: the blueprint (filters F1–F5); `ROW-D-REDUCED-STATEMENT.md` (§1–§6);
`PATH-TO-D.md` §2–§3; Paper 46 `main.tex` (statements of every label cited below); Paper 47 `main.md`
Thms 18.1, 18.16, 19.25, 27.3, Remarks 27.15–27.16, §28.2–28.4; phase-136 `NOTE_OFF_THE_PAGE_CANDIDATES.md`,
`MAP_1_WALLS_AND_MASTER_DOCS.md`, `MAP_5_LITERATURE_VS_CORPUS.md`; `ROW-D-CLOSURE-PLAN.md` §4, §7, §10;
`R151_005`, `R152_005`, `R155_038/043/046/060`, `R156_005`, `R154_013`, `R154_031` §3; abstracts of Papers 08, 11,
13, 14, 15, 18, 20, 25, 36, 37, 38, 39, 40, 41. Corpus grep: 60 keywords over `03-research/`, `04-papers/`,
`05-meta-and-planning/`, `00-references/` (counts in §1.1).

---

## §0 Verdict in one paragraph

I screened 55 candidate mechanisms: 30 from the corpus and 25 from the literature. **None survives as a
mechanism with a formulated statement.** One candidate is **formally not excluded**: (P152.2), a difference kernel
on the Berkovich line `A^{1,an}_Z`. It was recorded in phase 152 with a cheap decisive test that was never run, and
§5 restates that test as a one-round lemma adapted to F1–F5. Of the other 55 table rows (#26 is split into 26a/26b), 39 are
**excluded**, each by a named proved statement or by a named method constraint. A few of the 39 rest partly on an
argument rather than a labelled theorem (rows 18, 27, 28), and they are marked as such. 16 are **equivalent to
RH**, or to row D, with no content that bears on uniformity in `T`.
Two observations organise the whole search:

* **O1.** Uniformity in `T` *is* global Weil positivity (§1.2). So "a mechanism that supplies uniformity" means
  exactly "a proof of Weil's criterion".
* **O3.** Per window, the sign cannot be resolved by any input with an error term larger than the margin (§1.2).
  So estimate-type mechanisms are excluded from the per-window route and can act only through the global route
  (P47 W4), where the per-window structure plays no role.

**[amended per R157_004, A9/A10/A15]** The audit changes the verdict. Row 37 (Deninger) is **not excluded**: its F4
exclusion inverted P47 T1, which says "the proof must be uniform in the number field" (P47 §18.1). Rows 35 and 36
exclude only their `h⁰` and import readings. What they leave, together with row 37, is the unbuilt **MW-5 cluster**,
which no proved statement excludes. Five missed candidates were added as rows 56–60. Counts: **61 rows: EXCL 39,
EQUIV 20, SURV 1 (P152.2), NOT EXCLUDED 1 (row 37 = MW-5 cluster, unbuilt, no test).** O3 holds only as an upper
bound with factor `1/|c_{F*}(log n₀)|`, and it is vacuous for `T ≤ 1.51` (A2, A3).

---

## §1 Method, and four observations used throughout

### 1.1 Corpus grep (file counts, `.md/.tex/.txt`, `.bak` excluded)

Nyman 53 · Báez-Duarte 31 · de Bruijn/Newman 154 · Rodgers 51 · Lee–Yang 37 · Turán 86 · Jensen polynomial 28 ·
Griffin 35 · Keiper 50 · Hermite–Biehler 70 · Laguerre–Pólya 58 · Csordas 22 · Burnol 54 · Yoshida 60 ·
Bombieri–Lagarias 25 · Deninger 160 · scaling site 75 · arithmetic site 66 · Arakelov 175 · de Branges 282 ·
Suzuki 77 · screw function 28 · prolate 420 · semi-local 390 · Hilbert–Pólya 96 · GUE/random matrix 1396 ·
Selberg trace 7 · Pontryagin 199 · Kreĭn 388 · Pick 286 · F₁ 249 · Berry–Keating 18 · Bost–Connes 40 · Haran 379 ·
Borger 20 · Weng 1 · Kurasov 8 · Dyatlov/FUP 6 · Lindenstrauss/Furstenberg 5 · Berkovich/Poineau 17 ·
model-theor. 13 · Pila 39 · Beurling 202 · Voronin 40 · Selberg class 9 · Robin 51 (mostly Robin boundary roots,
not Robin's criterion) · Nicolas/colossally abundant **0** · Redheffer 33 · Mertens 110 · Levinson/Conrey 96 ·
Polymath 25 · Nevanlinna 135 · Stieltjes 358 · Beurling–Selberg/Vaaler (row-D arc) 5 · Conrey–Li 3 ·
o-minimal/Hrushovski **0** · Neshveyev **0** · "first crossing"/clopen (row-D arc) **0**.

### 1.2 Four observations (O1, O2 restate the record; O3, O4 are new here and marked for audit)

**O1 (uniformity = global positivity; `RESTATEMENT`).** By `lem:monoT`, `W_T` is the restriction of `W_{T'}` for
`T < T'`. Hence `∀T: λ^W_T ≥ 0` is Weil positivity on `C_c^∞(ℝ)`, and `∀T: RD_T` is the same statement by
`prop:uniform` and `cor:margin2`(iii). A mechanism "uniform in `T`" is therefore a proof of Weil's criterion, no
more and no less. What the per-window language adds is not an object but **filters** (F1–F5): it says which
proofs are impossible, not which proof to build.

**O2 (uniformity is RH-strength; `RESTATEMENT`).** If an input `H` is consistent with the existence of one off-line
zero, then `H` does not imply `∀T: λ^A_T ≥ 0`. Proof: in the proof of `cor:margin2`(iii), P45 Thm 10.4 turns an
off-line zero into a window `T₀` with `λ^A_{T₀} < 0`, and the same then holds for `λ^W_{T₀}`. Consequently every
quasi-RH mechanism fails F2 at the level of uniformity: zero-free strips, `β < ¼` resonance gaps, Λ_dBN ≤ t for
`t > 0`, `κ < ∞`, density-one statements.
**[amended per R157_004, A8]** Read literally, "H does not imply" is empty: if RH holds, every true H implies it
(P46 l.3416). O2 is a derivation schema in the sense of P47 Thm 18.1/Rem 18.1a. A derivation from H that is valid
in a structure satisfying H with an off-line zero is unsound. The unconditional content used below (in O4) is
P45 Thm 10.4.

**O3 (margin resolution; `COROLLARY` of the proof of `thm:finmod`(ii); PROVED per R157_004 §1.1 after A1–A5).** Fix `T` and
let `F*` be a real unit minimiser of `a_T` on `P_T`. It exists by the compactness in the proof of `thm:O`, or by
Bombieri Thm 3. Put `Φ* = Φ_{F*}` **[amended per R157_004, A1: read `c_{F*}` (autocorrelation) wherever `Φ*(log n)`
appears. P46's `Φ_F` (l.136) is the Mellin-type transform]**. Suppose some contact `n₀ ∈ N_T` has `Φ*(log n₀) ≠ 0`. Let `a = Λ + s·ε·1_{n=n₀}`
with `s = sgn Φ*(log n₀)`, and take `ε ≤ Λ(n₀)` when `s = −1`, so that `a ≥ 0` (and `a ≤ Λ` in that case). By
`prop:finite`(ii),

    λ_min(A_T(a)|P_T) ≤ a^{(v(a))}_T(F*) = λ^A_T − (2ε/√n₀)|Φ*(log n₀)| ,

and this is `< 0` as soon as `ε > √n₀ λ^A_T / (2|Φ*(log n₀)|)`. With `cor:margin1` (`λ^A_T ≤ 4·10⁹ T e^{−15.449T}`
for `T ≥ 1`) and `n₀ < e^{2T}`, a perturbation of the single weight `Λ(n₀)` by

    ε ≍ 2·10⁹ T e^{−14.449T} / |Φ*(log n₀)|      [amended per R157_004, A2: "≍" → "≤"; this is an upper bound on the threshold]

already destroys `RD_T`. **Reading.** Any per-window derivation of `RD_T` must use an input that is not invariant
under a change of one `Λ(n₀)` by that amount. Every estimate with an error term, every class property, and every
asymptotic fails this. This is F1 in quantitative form: `cor:void` takes `ε` large, O3 takes it
exponentially small. The same computation with `W_T(a)` gives the complete form. The degenerate case
`Φ*(log n) = 0 ∀ n ∈ N_T` is not excluded by this argument.
**[amended per R157_004, A2–A5]** (i) The threshold is `ε_* ≤ 2·10⁹Te^{−14.449T}/|c_{F*}(log n₀)|`. It is not `≍`.
With `|c| ≤ 1` the bound is `≥ 1` for `T ≤ 1.51`, so O3 is vacuous there. "Exponentially small" needs an unproved
lower bound on `max_n |c_{F*}(log n)|`. (ii) For `s = −1`, one needs `Λ(n₀) ≥ ε_*`. Non-prime-power contacts allow
only `s = +1`, and `C_BT` allows only `s = −1`. (iii) For the complete form, use the minimiser of `W_T` on `L²(I_T)`,
not `F*`. (iv) Degenerate case (R157_004 Lemma D, PROVED): if some minimiser has `c_{F*} ≡ 0` on `log N_T`, then
`v_T(Λ)` maximises `v ↦ λ_min(A^{(v)}_T|P_T)` over `ℝ^{N_T}`. This is OPEN, and not excluded. (v) "Every estimate …
fails this" should read "every input whose class is closed under a change of one weight by `ε_*`". For
`C_PNT`/`C_zeros`, `cor:void` already acts with no size restriction.

**O4 (clopen reformulation; `EQUIVALENT`, **to be audited**).** Window minima are continuous in `T`
(Bombieri 2000 Thm 5, as cited in P46 §1.2), and `λ^W_T > 0` for `T ≤ 0.8` (Zhu, `cor:KEP08`; cited, not
re-verified). Hence

    RH ⟺ Z_W := {T > 0 : λ^W_T = 0} = ∅ .

(⇒) is the Jensen argument in the proof of `cor:RH`. (⇐) If RH fails, O2 gives `λ^W_{T₀} < 0`, and the
intermediate value theorem gives `T_c ∈ Z_W`. At `T_c`, `W_{T_c} ⪰ 0` with a kernel vector `F*`. By the computation
in `thm:KEP2`, every `ν ∈ 𝔖(T_c)` satisfies `∫|F̂*|² dν = 0`, so it is carried by the real zero set of `F̂*`: this is
the **determinate** Kreĭn case, `thm:finDet`-like. This is a restatement: it turns "`≥ 0` for all `T`" into "never
exactly `0`", and it needs no margin (F2 holds). But `cor:convfail`(ii) produces comb data of the same structural
type that *are* degenerate (at `θ_* ∈ (0.8148, 1)`, `λ^W_T(a_{θ_*}) = 0` by continuity in `θ`). So
non-degeneracy is not structural. It carries no mechanism and is recorded as hygiene.
**[amended per R157_004, A6/A7]** (i) *Continuity* is proved in R157_004 Lemma C (dilation plus relative form bound)
and is also Bombieri 2000 Thm 5 (`λ^W = min(μ_+, μ_−)`). P46 itself claims no continuity (l.3103, l.2409), so this is
an import into the P46 frame. (ii) *Small-window positivity* needs no citation: R157_004 Lemma E gives
`λ^W_T ≥ C₀ + log coth(T/2) − 4 sinh T > 0` for `T ≤ 0.005`. (iii) *(⇒)* is already in P46 (`cor:RH` proof;
`thm:KEP3`(b) proof) and in Bombieri Thms 1 and 3, so O4 is a **RESTATEMENT**. (iv) *"Determinate" FAILS as stated.*
Proved: if `𝔖(T_c) ≠ ∅`, every solution is atomic and carried by `F̂*^{−1}(0) ∩ ℝ`. Unproved: solvability at `T_c`,
and uniqueness (`thm:finDet` is for finite zero sets). Also, if RH fails, `Z_W` is a nonempty compact interval.
(v) The `cor:convfail`(ii) crossing is in `θ` at fixed `T`, not in `T`.

---

## §2 The table

Verdict key: **EXCL** = excluded by the cited proved statement or method constraint (`arg.` = by a stated argument,
not a labelled theorem); **EQUIV** = a known equivalence of RH or of row D, no content toward uniformity;
**SURV** = no proved statement excludes it. "F-items" lists the failing filter items.

| # | candidate | F-items failed | proved obstruction (label) | corpus status | verdict |
|---|---|---|---|---|---|
| 1 | D-HS (fibrewise Hilbert–Samuel `h⁰` on the S-square) | F5 | P47 Thm 19.25, Cor 19.25b; three kills in R155_054 | LEAD_NOTE §1; R155_054; R155_060 §1 | EXCL |
| 2 | D-θ (Bost/van der Geer–Schoof theta `h⁰`) | F5 | Thm 19.25 (any `h⁰: D^W → ℝ_{≥0}`, real-valued allowed); Cor 19.25b | LEAD_NOTE §2; never run separately | EXCL |
| 3 | D-K / Kreĭn extension KEP(T) / definitizability | — (reformulation) | `thm:KEP3`(b): RH ⟺ KEP(T) indeterminate ∀T | Papers 08, 18; R155_040/043 (P5 closed) | EQUIV |
| 4 | Pontryagin finite defect `κ < ∞` (Paper 11) | F2 (O2), F3 | Paper 11 (no fixed prime head; infinite-dim near-null space); `thm:arena`; ES-18 | Paper 11; MAP_1 l.157 | EXCL |
| 5 | Connes scaling operator on a Pontryagin space (Paper 25) | — | conjectural identity `κ = ind₋(H_C)`, V.2 open; NG-C3 (eigenvectors not in L²) | Paper 25; MAP_1 l.43 | EQUIV |
| 6 | Paper 36 ARP-P Pick/Nevanlinna chain (terminates at Li) | F3 (termwise) | `cor:Li` (Li kernel not flat-top, not admissible); `rem:LiSC`; R155_038 "disjoint" | Paper 36; R155_034/038 | EQUIV |
| 7 | Li–Keiper, Bombieri–Lagarias complements, Paper 38 sliding windows | F3 (termwise) | `cor:Li`, `cor:nontermwise`, `rem:LiSC` | Papers 36–38; NG-A5 (MAP_1 l.29) | EQUIV |
| 8 | Positivity transfer from auxiliary nonnegative objects (16 attacks) | F3 | Paper 37 (sixteen witnesses); `lem:Rrig`; `thm:SC` | Paper 37 | EXCL |
| 9 | CCM/Suzuki cofinal finite semilocal operators (Papers 39–41) | F1, F3 | P41 P1 (radical saturation), P3 (counterfactual invariance); `thm:O` | Papers 39–41 | EXCL |
| 10 | Nodal criterion for `S_even` (P8) | F3 | `thm:arena`, `cor:arena`; R155_046 (closed as a route) | R155_044–046 | EXCL |
| 11 | Alignment-band arithmetic lower bound (P6) | — | R155_053 §7: closed as an equivalence; `prop:band`, `prop:negtrace` | R155_053/058/060 | EQUIV |
| 12 | Prolate concentration floor (archimedean Problem A) | F1, F4 | `prop:archneg`, `cor:Tarch`, `thm:index`: the archimedean form is indefinite on `P_T` from `0.60`; primes necessary | R155_046 §4, R155_047 | EXCL (as a uniformity mechanism) |
| 13 | Finite compressions, lattice classes, Galerkin, computer-assisted windows (P42, Zhu, Groskin) | F2, F3 | `thm:N`, `thm:Np`, `prop:TK`, `thm:arena`, `thm:finZ`, `thm:margin`; Zhu Conj. 12.1 | Papers 42, 47; P47 §28.4 | EXCL |
| 14 | Closed-form / exact dual certificate (identity) | F3 | `thm:O`, `lem:Onat` | P46 §3 | EXCL |
| 15 | Mass/radius rate lemmas; pointwise envelope | F3 | `thm:Vp`, `prop:env` (Zhu Thm 1.4 independently) | P46 §4–5 | EXCL |
| 16 | Upward induction / bootstrap / monotone spectral flow in `T` | F2 | `cor:mono`, `lem:monoT`, `rem:regimes` + `lem:cpos`; N5, D.53 | P46; R156_005 §2 | EXCL |
| 17 | Continuity / first-crossing (clopen) argument | — | O4 (§1.2) | never treated (grep 0) | EQUIV |
| 18 | Sub-comb, prime-by-prime, semilocal finite `S` (CC semi-local trace formula, CCM semilocal prolate) | F3 | `thm:SC`, `prop:finsupp`; for infinite-support finite-mass `S`, the proof of `prop:finsupp` (arg. → **PROVED**, R157_004 §2, A11) | P46 §8; CCM refs in 00-references | EXCL |
| 19 | Local–global: Hasse–Minkowski, per-place reflection positivity | F3 | NG-C1, MW-3, NG-E1 (MAP_1 l.41, 48, 59) **[A17: NG-E1 is l.48 (a computed refutation, `p ≤ 7`); MW-3 is l.57 ("absence of a known theorem"); l.59 is MW-5. The exclusion rests on `thm:SC`/`prop:finsupp`, and only for arguments that infer the sign from local or finite-`S` positivity]**; `thm:SC` | phases 6, 25–27 | EXCL |
| 20 | Classical prime-side theorems (PNT error terms, VK zero-free region, zero density, Levinson–Conrey, sieve bounds, level of distribution, bilinear estimates *as outputs*) | F1 | `thm:finmod`, `cor:void` (classes `C_PNT`, `C_zeros`, `C_BT`); O3 | P46 §10.4 | EXCL |
| 21 | de la Vallée Poussin numerator sign; Rankin amplification by nonnegative trigonometric polynomials | F1, F2 | R151_005 §2.2 (depth `1/log γ` capped by the archimedean sea) → zero-free region → `cor:void`; O2 | R151_005; phase 37 Doc 111 | EXCL |
| 22 | Deligne route over Z: tensor power, additive pencil, moments, single-fibre extraction | F5 | P47 T5 (Thm 27.3–27.4), T6 (R151_005), (P149) = k-tuples | phases 149–151 | EXCL |
| 23 | Laumon purity of `FT` over Z (one-round dictionary) | F5 | inherits the rationality wall; `thm:finZ`/`cor:infinite` (over `F_q` the zero set is finite) | phase 150; ROW-D-CLOSURE-PLAN §4 L1 | EXCL |
| 24 | Frame enlargements: Galois ring, Taylor–Wiles patching, mixed effectivity, additive square | F5 | P47 Thm 22.17, Lemma 24.1, Thm 24.10, Thms 25.6–25.7, 26.13, 26.17 (§28.4) | phases 147–149 | EXCL |
| 25 | Mayer transfer / Lewis–Zagier / Dolgopyat–FUP resonance gap (P152.1) | F2 (O2), arch gate | R152 Prop A.2 (`β = ¼` *is* RH), Prop A.4; fails gate g3 | R152_001/002/005 | EXCL below RH strength; EQUIV at it |
| 26a | Berkovich spectrum `M(Z)`, tree potential theory | F3 (per branch) | R152 Prop B.3 | R152_001/005 | EXCL |
| 26b | **Difference kernel on `A^{1,an}_Z` (P152.2)** | none proved | Prop B.3 is scoped to trees; no statement covers it | R152_005 §2; test never run (grep 153–156: 0; confirmed by R157_004 §3) | **SURV** (§5) |
| 27 | Measure rigidity of `×p` (Furstenberg–Rudolph–Lindenstrauss); Kronecker-flow discrepancy (GAP-157.A) | F1 | positions-only inputs: `cor:void` applied to `C_supp = {a ≥ 0: supp a ⊆ prime powers}` (closed under amplification at `n₀ = 2`); the Bost–Connes use (Neshveyev) sits on the β-axis (MW-2) | never analysed (R151_005 §2); GAP-157.A phase 49 | EXCL (as instantiated; arg. for Bost–Connes) |
| 28 | Model-theoretic methods (o-minimality, Pila–Wilkie, ACFA) | F1, F3 | arg.: Λ is not definable in any o-minimal expansion of ℝ; bounded-parameter families see finitely many `Λ(n)` → `prop:uniform`(b), `prop:finsupp`; ACFA needs Frobenius → P47 Thm 22.17 | never analysed (grep 0) | EXCL (arg.) |
| 29 | Auxiliary functions / Stepanov / Baker / transcendence | F1, F3 | Stepanov one-sided counts → `C_BT` (`cor:void`, `T > 0.749`); Baker/Pila → positions only (#27); the `F_q` closing step needs rationality → `thm:finZ` | NG-B7 (MAP_1 l.39); otherwise never analysed | EXCL |
| 30 | Arithmetic-not-metric bilinear cancellation (Friedlander–Iwaniec, Heath-Brown), O-150.2 | F1 per window | outputs are estimates → `cor:void`, O3; at RH strength → P47 Thm 27.10 (W4) | P47 Rem 27.15, §28.3 (42) | EXCL per window; EQUIV globally |
| 31 | Weil positivity / Bombieri variational theory itself | — | definition (MW-1) | P45, P46 | EQUIV |
| 32 | Hilbert–Pólya realisations (Berry–Keating, Connes adèle class, Bender–Brody–Müller, Sierra) | — | T6/O-151.4 (spectral positivity is a summand mechanism: restatement) **[A13: O-151.4 is an OPEN item (R151_005:19, 52), and T6 concerns moment families. The EQUIV verdict rests on "a realisation is a reformulation of RH", not on T6]**; NG-E5, NG-C3; AUDIT_A 161 | phases 14, 53, 67; MAP_1 l.52, 58 | EQUIV |
| 33 | Bost–Connes KMS, β = 1 transition | F2, MW-2 | AUDIT_A Thm 161.9 (partition function = ζ(β)); acts at `Re s ≥ 1` **[A16: MW-2 is a pattern, "not itself a single closed theorem" (MAP_1:56)]** | CORPUS_CHECK_ROW_D_PLAN §4 | EXCL |
| 34 | CC archimedean Weil positivity and prolate operators (CC 2021; CCM 2023; Connes–Moscovici UV prolate) | F1, F4 | `prop:archneg`, `cor:Tarch`, `thm:index`, `thm:J` (`n₋ ≈ 4.004T`); ES-22 | phases 137, 153; MAP_5 | EXCL (as a uniformity mechanism) |
| 35 | F₁ geometry: CC scaling/arithmetic site, Riemann–Roch on `Spec Z̄`, Haran plane, Borger λ-rings, Deninger rational Witt vectors; category changes (condensed, K-theory, motivic) proposed for `h⁰` growth | F5 | Thm 19.25/Cor 19.25b (category-independent: a statement about functions on the divisor domain); MW-5; NG-113-d3; NG-107; MAP_5 (log growth) **[A10: EXCL covers only the `h⁰`/Riemann–Roch-growth readings. A Hodge index on the square not routed through an `h⁰` on `D^W` is outside Thm 19.25 (MAP_1:59, "UNBUILT (not proved impossible)") → row 37 cluster]** | phases 107–118, 136–148 | EXCL (`h⁰` readings) |
| 36 | Arakelov intersection / Faltings–Hriljac arithmetic Hodge index | F5 | phase 15 M3/M10 (heights ≠ zeros); P122.007; Thm 19.25 **[A10: P122.007:3–8 excludes *importing* the existing theorems (hypothesis mismatch). Building an arithmetic square is the row 37 cluster]** | phase 15; LEAD_NOTE §0 | EXCL (import) |
| 37 | Deninger foliated dynamics, leafwise Hodge–Riemann **[A9/A10: row re-scoped to the MW-5 cluster: Deninger's cohomology, a CC Hodge index on the square of the scaling site, an arithmetic surface over `F₁`, i.e. the residuals of rows 35–36]** | ~~F4, F2~~ none proved | ~~T1 (field-uniform: must prove GRH for every K)~~ **T1 prescribes field uniformity (P47 §18.1 title, Rem 18.1a); it does not exclude it.** NG-62b is a finite-window diagnostic (`EQUIVALENT-TO-RH`, MAP_1:73), not a theorem about this cohomology | phases 42–43, 62; MAP_1 l.59, 73 | ~~EXCL~~ **NOT EXCLUDED (unbuilt; no object; no one-round test)** |
| 38 | Suzuki screw function; Weil Hilbert space ≅ `H(E_ξ)` | — | Suzuki Thms 1.2–1.7 (RH ⟺ screw ⟺ `Ψ ≥ 0` ⟺ `Ψ = O(1)`); KEP is its window form **[A12: Thm 1.4 (nondegeneracy) must be read in the primary text for its conditional status before any novelty claim for O4]** | R154_031 §3; P46 §1.2 | EQUIV |
| 39 | de Branges spaces / de Branges's positivity condition / Hermite–Biehler / Lagarias's de Branges space | — | HB ⟺ RH (ES-16, Paper 20); de Branges's sufficient condition refuted (Conrey–Li) | phase-16-surf-witness-variety/07 l.42, /08; Paper 20 | EQUIV |
| 40 | Laguerre–Pólya, Jensen polynomials (GORZ), Turán, Csordas–Norfolk–Varga, Csordas–Varga | F2 (finite order), F1 | P15 `thm:hr` + `cor:margin2`(iii): the limit form is degenerate, so no uniform HR **[A14: no uniform *gap* (`inf δ_m = 0`), i.e. `thm:margin` again; it does not forbid `δ_m ≥ 0`. Finite order is excluded by O2 (arg.)]**; P14 stability preservers are arithmetic-blind | Papers 14–15; phase 11 | EQUIV (full order) / EXCL (finite order) |
| 41 | de Bruijn–Newman `Λ ≤ 0` (Rodgers–Tao `Λ ≥ 0`, Polymath `Λ ≤ 0.22`) | F1, F2 | P13 Thm N5 (the flow is arithmetic-blind); O2 for `t > 0` | Paper 13; phases 33, 55, 70 | EQUIV |
| 42 | Lee–Yang, Newman, Kurasov–Sarnak crystalline measures | F1 | E70_1_RESULTS l.30–33 (Lee–Yang positivity = LP = RH; the forcing gives `Λ ≥ 0`, the wrong direction); P14 | phase 70; ROW-D-CLOSURE-PLAN §4 | EQUIV |
| 43 | Nyman–Beurling, Báez-Duarte, Burnol's lower bound | — | NG-A5, NG-B4, CIR-3; R155_038 (P4 closed) | phases 33–34 (docs 82, 83, 93); P36 l.9831 | EQUIV |
| 44 | Yoshida / Bombieri small windows; Burnol local analysis | F2, F4 | prime-free window only; `thm:SC` remark; `prop:arch`, `cor:Tarch` | P46 §1.2; P37 l.903 | EXCL beyond `½log2` |
| 45 | Random matrix / GUE / pair correlation / Katz–Sarnak | F1, F4, F3 | NG-B8; P13 (iii) (Λ is extremal, not an average); T1 (universality is field-uniform); `cor:infinite` | Paper 13; MAP_1 l.40 | EXCL |
| 46 | Selberg-trace analogues (modular-surface resonances `ρ/2`, Selberg 3/16, Ihara/Ramanujan graphs) | MW-2 | R152 Props A.1–A.2; ROW-D-CLOSURE-PLAN §4 (discarded: Kesten/Ramanujan, Maass–Selberg) **[A16: Prop A.1 is PROVED for Maass–Selberg; MW-2 is pattern-level; the graph and 3/16 discards are closure-plan judgements]** | phase 152; P36 l.641 | EXCL (listed instances) |
| 47 | Weil–Deligne over `F_q` (Castelnuovo, Bombieri–Stepanov, Deligne) transported to Z | F5 | Thm 19.25 + Thm 21.15 (the frame defect holds on a curve over `F_q`); T5/T6; `thm:finZ` (rationality = finite zero set = determinate); Thm 22.17 | phases 33 (doc 74), 145 | EXCL |
| 48 | Probabilistic models (random multiplicative functions, Cramér, multiplicative chaos) | F1, F4 | class-level models; N7; T1/T2 | phases 12–13, 19 | EXCL |
| 49 | Nicolas, Robin, Redheffer, Mertens, Riesz, Hardy–Littlewood, Speiser criteria | — | W4 (P47 Thm 27.10) for the partial-sum criteria; the others are classical equivalences | NG-A5 family; Nicolas/Robin never treated (grep 0) | EQUIV |
| 50 | Beurling–Selberg / Holt–Vaaler extremal functions; Cohn–Elkies LP; SDP for zero statistics | F3 (termwise) | `lem:Rrig`, `cor:nontermwise`; the literature instances assume RH (R154_013 Tab. 1(d)) | R153_016, R154_007/013 | EXCL |
| 51 | Sum-of-squares / Positivstellensatz for `W_T` with arithmetic squares | F3 | P41 P1 (no local edge square); `thm:O`; the zero-side SOS is the RH SOS (`cor:RH`) | Papers 37, 41 | EXCL / EQUIV |
| 52 | Voronin universality, Fourier interpolation, sum–product, prismatic, functoriality, quantum chaos | F1/F5 | closed in the record: ROW-D-CLOSURE-PLAN §10.2 (phases 15, 30, 35, 53, 67, 101, 102, 150) | analysed | EXCL |
| 53 | Weng zetas; Lagarias–Suzuki RH for Eisenstein-integral zetas | MW-2 (pattern-level, A16) | RH for these is proved from the location of ξ's zeros in the strip (a Hermite–Biehler comparison), not from the line; it says nothing about ξ (CAND-2) | ROW-D-CLOSURE-PLAN §7(e) | EXCL |
| 54 | Kreĭn extremal-extension conjecture | — | R155_040 §4(iii) `HEURISTIC`; `thm:KEP3` (any proof is RH-hard) | R155_040/043 | EQUIV |
| 55 | Selberg's `μ*log² ≥ 0`, Möbius inversion as a positive adjoint (identity-level positivity) | F3 | Paper 37 (both among the sixteen witnesses) | Paper 37 | EXCL |
| 56 | **[added per R157_004]** Zagier/Sarnak/Verjovsky horocycle equidistribution (RH ⟺ rate `O(y^{3/4−ε})`) | F1 per window, F2 below RH | an estimate → `cor:void`; weaker rates quasi-RH (O2); same family as #25 | not in the table before | EQUIV |
| 57 | **[added per R157_004]** Balazard–Saias–Yor integral (`≥ 0` always; RH ⟺ `= 0`) | — | classical equivalence; a one-sided no-margin identity, the rhyme of `cor:margin2`(iii) | not in the table before | EQUIV |
| 58 | **[added per R157_004]** Lax–Phillips / Pavlov–Faddeev scattering (zeros of `ζ(2s)` as resonances) | F2 (O2) | R152 Prop A.2 (`β = ¼` is RH); same object as #25 | naming gap only | EQUIV |
| 59 | **[added per R157_004]** Selberg-class axiomatics | — | no record falsifier lies in the class (DMV: no functional equation; `Ξ_a`: violates Ramanujan; Epstein, Davenport–Heilbronn: no Euler product); `ξ_K ∈ S` → T1 standard (GRH for all `K`); a hypothesis set, no mechanism | not in the table before | EQUIV (framework; not excluded) |
| 60 | **[added per R157_004]** Connes–Consani ζ-cycles / Sonin spaces (literature description not re-verified) | F3 per `L` | finite approximation: `thm:finZ`, `thm:arena`; the limit is #32 | not in the table before | EXCL (per `L`) / EQUIV (limit) |

Counts (26a and 26b counted separately; each row counted once under the verdict that governs it): **56 rows (55 candidates,
#26 split): EXCL 39, EQUIV 16, SURV 1.** **[amended per R157_004: 61 rows (56–60 added): EXCL 39 (row 37 removed, row
60 added), EQUIV 20 (rows 56–59 added), SURV 1 (26b), NOT EXCLUDED 1 (row 37, the MW-5 cluster). Rows 12, 45 and 48
cite T1 as if it excluded something. They keep their verdicts on their F1/F3 grounds. The blueprint's F4 wording
misreads T1, and this should be amended (R157_004 §2).]** The mixed rows are counted under the governing verdict: 25, 30 and 51
as EXCL, 40 as EQUIV. The four arguments that are not labelled theorems are in rows 18 (infinite-support extension),
27 (Bost–Connes part), 28 and O3; row 20's O3 citation is supplementary to `cor:void`.

---

## §3 Candidate paragraphs

### Family A — the corpus's own candidates (row-D arc and the earlier arcs)

**1. D-HS.** A fibrewise Connes–Consani `H⁰` on the S-square with Frobenius transport, meant to produce the
`m²` growth that clause (c) of P47 Thm 12.3 needs. It is an `h⁰` construction in the intersection frame and fails
**F5**. P47 Thm 19.25 (`PROVED`) says no `h⁰: D^W → ℝ_{≥0}` satisfies (a), (b′), (c) for ξ. Cor 19.25b extends
this to the small domains `C_c^∞ ⊕ ℝK` and `P_c^∞ ⊕ ℝK`. R155_054 killed D-HS by three independent routes
(R155_060 §1). Corpus: `NOTE_OFF_THE_PAGE_CANDIDATES.md` §1; R155_054/057. **EXCL.**

**2. D-θ.** A Bost-type `h⁰_θ(E) = log Σ e^{−π‖v‖²}`. It is real-valued, which the lead note said survives
R16. Thm 19.25 is stated for every `h⁰` into `ℝ_{≥0}` and for every constant `χ`. Integrality is never used, so
D-θ falls under it verbatim: **F5**. Its own kill test (a lattice rank linear in `m`) was never run, and it is now
unnecessary. Corpus: LEAD_NOTE §2 only. **EXCL.**

**3. D-K / Kreĭn / KEP.** The per-window Kreĭn extension problem for the explicit-formula datum `g`.
`thm:KEP3`(b): RH ⟺ KEP(T) is solvable for every `T` ⟺ it is indeterminate for every `T`. By (a), indeterminacy and
certificates coincide off `{λ^W = 0}`. The chain is one-directional: indeterminacy ⟹ `λ^W ≥ 0` (R156_005). Papers
08 and 18 give the global Kreĭn-space identity `𝒲 = E*JE`, with negative directions the off-line zeros, and Paper
08 (C) proves that the zero-side expression is the same functional as the arithmetic side. Translating to the
per-window form adds exactly `thm:KEP1–3`: a reformulation, not a step (P46 remark after `cor:KEP08`).
Corpus: R155_040, R155_043 ("P5 CLOSED as a route"). **EQUIV** (complete form).

**4. Pontryagin finite defect.** Track `κ = n₋`, the number of off-line zeros, and aim at `κ < ∞`, then at
`κ = 0`. The output `κ < ∞` is consistent with off-line zeros, so by **O2** it cannot give uniformity. Paper 11
closes both mechanisms for `κ < ∞`: the subordination cutoff scales as `e^{2d}/10`, and the near-null space of the
prime–archimedean pencil is infinite-dimensional (**F3**, finite rank; compare `thm:arena`). The step
`κ < ∞ ⟹ κ = 0` is Conjecture C_B (MAP_1 Table 2), open with no bridge. Corpus: Paper 11; ES-18 (MAP_1 l.157).
**EXCL.**

**5. Connes scaling operator on a Pontryagin space (Paper 25).** The bridge conjecture `κ(Q) = ind₋(H_C)`. The
bound `≤` is free (Kreĭn–Langer), and the reverse needs the characters `x^{b+iγ}` as generalised eigenvectors
(V.2 open). NG-C3: these are not in L². Even if it were proved, RH ⟺ `ind₋(H_C) = 0` is a restatement.
Corpus: Paper 25; MAP_1 l.43. **EQUIV.**

**6. Paper 36 ARP-P chain.** A fifteen-step Pick/Nevanlinna equivalence whose single open input (Step 5)
terminates at Li–Keiper positivity. The Li coefficients are `λ_n = Σ_ρ Φ_n(γ_ρ)` with `Φ_n = 1 − cos nθ ≥ 0`
termwise, so the Li route is termwise positivity. `cor:Li`: the Li kernel `w_n` is not flat-top, has decay exactly
`e^{−|u|/2}`, and `w_n` is not an admissible test function for the explicit formula, since the associated prime sum
diverges. `rem:LiSC`: the Li coordinates do not see collectivity (the weights `m^{−1}` are subcritical). R155_038:
the Li dictionary is "disjoint"; P4 closed. **F3** (termwise) as a per-window mechanism; **EQUIV** globally.

**7. Li–Keiper; Bombieri–Lagarias complements; Paper 38 sliding windows.** Li: RH ⟺ `λ_n ≥ 0 ∀n`.
Bombieri–Lagarias 1999 extend this to multisets and give the asymptotics `λ_n ∼ (n/2)log n` under RH (used in
`rem:LiSC`). Paper 38: RH ⟺ eventual nonnegativity of every sliding sum `Y_L(N)`. All are equivalences on the
zero side. The per-window translation is `cor:Li`: no flat-top weight realises them. **What the translation would
add:** nothing toward uniformity; it adds the negative dictionary already proved. **EQUIV.**

**8. Positivity transfer from auxiliary nonnegative objects.** Paper 37 records sixteen closed attacks, each with
an exact witness: order kernels, Gram and energy factorisations, zero-lobe Grams, Möbius inversion as a positive
adjoint, the Euler–Gamma Koszul complex, `μ*log^k ≥ 0`, Abel/Cesàro positivity, compound Poisson/PF₂, Bernstein
complete monotonicity, Stein–Mecke, Fejér–Carathéodory, sums of squares, Vinogradov–Korobov tails. The target is a
signed cancellation between two divergent blocks (P37 abstract). In the per-window language this is `lem:Rrig`
(no termwise sign), `thm:SC` (no sub-family) and `rem:PF2`. **F3.** **EXCL.**

**9. CCM/Suzuki cofinal finite operators (Papers 39–41).** The reduction of RH to "physical source surplus
`𝔤 > δ`" on a cofinal family of finite semilocal rows. Paper 41 catalogues 31 no-gos and proves three principles:
P1 radical saturation (no local edge square), P2 measure capacity, and P3 counterfactual invariance ("if a
proposed argument would remain valid verbatim in a system with an off-line zero, it is already refuted"). P3 is
**F1** in the P41 language. The finite rows fall under `thm:O` (no finite attainment) and `thm:arena`: **F3**.
**EXCL.**

**10. Nodal criterion P8.** Express the even Schur complement through the nodes of the archimedean eigenvectors
relative to `{log n}`. R155_046: the nodes decide the dominant signs; the arithmetic sits in the small entries the
nodes leave undecided. The arena has `≥ 12` modes at `log 2` and grows doubly exponentially (`cor:arena`), so no
fixed truncation decides it (`thm:arena`). **F3.** Per window only, never uniform. **EXCL.**

**11. P6, the alignment-band lower bound.** State what the primes must do on the band `[2πe^{2T}, 2πe^{A_T}]` at
the alignment arcs. R155_053 §7: closed as an equivalence. `prop:negtrace`: the negative part is trace class and
the band does not decide. **EQUIV.**

**12. Prolate concentration floor.** A lower bound on the spectral mass that a window-supported primitive `F`
must carry above `τ₀`: an archimedean Problem-A statement. It acts only on `A_∞|P_T`. `prop:archneg`/`cor:Tarch`/
`thm:index`: `A_∞|P_T` is indefinite from `0.58 ≤ T*_{∞,P} ≤ 0.60` on (primitive form), and the complete
archimedean form is negative from `0.4608`. So no archimedean statement gives the sign beyond `0.60`: **F1** (no
Λ) and **F4** (no property separating ξ from ξ_K; the Γ-data are shared by every field with the same signature).
It is useful per window as an ingredient. **EXCL** as a uniformity mechanism.

**13. Finite compressions and computer-assisted windows.** Galerkin compression (Paper 42, primitive, `T ≤ log 2`),
Zhu's certificate (complete, `T ≤ 0.8`, cited), Groskin's budget, and the lattice classes of Paper 46. Excluded by
`thm:N`/`thm:Np`/`prop:TK` (class ceilings), `thm:arena`, `thm:finZ` (**F3**), and `thm:margin` with Zhu's
Landau–Widom conjecture, under which the per-window effort grows at least like `e^{2T}` (**F2**). P47 §28.4
classes these as "measuring rather than moving the wall". **EXCL.**

**14. Exact dual certificate.** `thm:O`: no finite `ν` and no finite family of continuous multipliers attains the
dual value, even with `v = 0`. `lem:Onat` gives the same for the complete form. **F3** (identity). **EXCL.**

**15. Rate lemmas and envelopes.** `thm:Vp`: escaped mass trades against value at exactly `Θ(log R)`, so no
mass-based rate is uniform. `prop:env`: the pointwise threshold `2πe^{A_T}` is doubly exponential. **F3.** **EXCL.**

**16. Upward induction in `T`.** `cor:mono` and `lem:monoT`: `λ` is nonincreasing, so a certificate at `T`
constrains nothing at `T' > T`. `rem:regimes` with `lem:cpos`: a new contact enters at `T = ½log n` with a sign
not determined by anything prior. The monotone spectral flow and finite-rank compressions are closed (N5, D.53;
R156_005 §2). **F2.** **EXCL.**

**17. First crossing / clopen.** O4 (§1.2): RH ⟺ `λ^W_T ≠ 0` for every `T`, by continuity (Bombieri Thm 5) and O2.
At a crossing, the datum is determinate. It is not structural: the comb models of `cor:convfail`(ii) cross. It
needs no margin, but it needs the same `∀T`. Corpus: the set `{λ^W = 0}` appears in `thm:KEP3`(a) and at P46
l.3607, 3916, 4240 as the exceptional set; the clopen equivalence is not stated anywhere (grep 0). **What it would
add:** the exact locus where any proof must act (a determinate window). **EQUIV** (complete form).

**18. Sub-combs, prime-by-prime, finite semilocal `S`.** Connes's semi-local trace formula and the CCM semilocal
prolate operators use only the places in a finite `S`. `thm:SC`: any nonnegative sub-comb of mass
`A < −C₀ = 5.372` is negative on `P_T` for `T > T₀(A)`, which covers `S = {2}` (mass `2log2/(√2−1) ≈ 3.35`).
`prop:finsupp`: every finitely supported comb fails for large `T` (`limsup λ ≤ C₀ − A_S < 0`). For finite `S` with
all prime powers (infinite support, finite mass `A_S`), the proof of `prop:finsupp` goes through **(arg.)**. The
test functions `F_T = (−∂² + ¼)g(·/T)` concentrate at `τ = 0`, and the comb value there is `A_S` minus a tail that
tends to `0`. So `limsup ≤ C₀ − A_S < 0` **[amended per R157_004, A11: this is a proof. `σ_T` depends on `T`
through the contacts in `S`, but `|Σ_{S∩N_T}v_n cos(s log n/T) − A_S| → 0` pointwise with the bound `2A_S`, and
dominated convergence runs as in `prop:finsupp`: PROVED]**. If `S` grows to contain all primes `< e^{2T}`, the object is the full
comb and nothing is gained. **F3.** Corpus: P46 §8; `cor:SC1` (the "ten random primes"). **EXCL.**

**19. Local–global.** NG-C1 (the Weil form does not factor over places; there is no Hasse–Minkowski theorem in
infinite dimension, MW-3); NG-E1 (the per-place forms `G_p` are indefinite, computed); `thm:SC` (positivity is
collective). **F3.** **EXCL.**

**20. Classical prime-side theorems.** `thm:finmod` and `cor:void`. The classes `C_PNT(ε)` (any error term with
`inf ε > 0`, including RH-strength `x^{1/2+ε}` *as a class*), `C_zeros` (the same zeros and the same pole) and
`C_BT` (upper-bound sieves) are closed under deletion or amplification, so they decide no window beyond `½log2`
(primitive form; `cor:convfail`(iii) for the complete form). O3 sharpens this: any input with per-window error
`≳ e^{−14.4T}` at one contact is excluded **[amended per R157_004, A2–A5: read "any input whose class is closed
under one-weight changes of size `2·10⁹Te^{−14.449T}/|c_{F*}(log n₀)|`, for `T > 1.51`, when the minimiser does not
vanish at that contact". For the classes named here `cor:void` already suffices]**. Bilinear and level-of-distribution estimates are estimates, so they fall
here. **F1.** **EXCL.**

**21. dlVP / Rankin amplification.** The one numerator-sign mechanism over Z. Its depth `σ − 1 ≍ 1/log γ` is fixed
by the archimedean sea (R151_005 §2.2: penalty `(P(0) − a₀)(½)log γ`, Fejér `a₁ ≤ 2a₀`). The output is a zero-free
region, which is a class property: `cor:void` (**F1**) and O2 (**F2**). **EXCL.**

**22. The Deligne route over Z.** T5 (P47 Thm 27.3): no single-fibre extraction from any `L²` moment bound,
uniformly in `k`, in family size and in family type. T6 (R151_005): every family with nonnegative fibre summands is
the theorem itself at each `k`. (P149) is the k-tuple conjecture. **F5.** **EXCL.**

**23. Laumon over Z.** Phase 150: a one-round dictionary between the purity of `FT` and Gauss sums. Over `F_q` the
closing step uses constructibility, i.e. rationality, i.e. a finite zero set. Over Z, `thm:finZ` and
`cor:infinite` say the relevant zero set is intrinsically infinite, so the determinate/finite mechanism has no
analogue. **F5.** Corpus: R150_005; memory note "inherits the rationality wall". **EXCL.**

**24. Frame enlargements.** P47 §28.4, five independent closures: no ring of correspondences on `Spec Z`
(Thm 22.17); invisibility on the radial carrier (Lemma 24.1); action away from the zeros (Thm 24.10); vacuous or
infinite full-square constraints (Thms 25.6–25.7); the additive coinvariant block is zero-blind (Thms 26.13,
26.17). **F5.** **EXCL.**

**25. Mayer / Lewis–Zagier / Dolgopyat–FUP (P152.1).** RH ⟺ modular-surface resonances on `Re s = ¼`. R152 Prop
A.2: the Riemann–von Mangoldt density defeats any gap `β > ¼`, and `β = ¼` *is* RH. Prop A.4: the branch-sum
Dolgopyat route has abscissa `½` ("MW-2 in dynamical form"). (P152.1), a contraction on the disc space for the
continued Mayer operator, is stateable but has no method and fails the archimedean gate g3. Any strip narrower than
the full one is quasi-RH, excluded as a uniformity mechanism by **O2** (**F2**); the full strip is **EQUIV**.

**26a. `M(Z)` tree potential theory.** R152 Prop B.3 (`PROVED`, scoped to trees): a tree pairing is a function of
the meet, per branch, and blind to the cross-place coupling where the sign lives. This is the tree shadow of
`thm:SC` (**F3**). **EXCL.**

**26b. (P152.2) A difference kernel on the Berkovich line `A^{1,an}_Z`.** This is a group object with a genuine
archimedean fibre, so Prop B.3's hypothesis (a tree) fails, and the Weil kernel might be an *energy* there. If it
existed, it would be a global positivity. By **O1** it would be uniform in `T` automatically, which is why it is
the one candidate of the right shape. No proved statement excludes it. Risks, stated in advance:
* if the energy decomposes as a sum of local energies, NG-E1 (local forms are indefinite) and `thm:SC` kill it;
* if it is defined for every Beurling system, T3 kills it (conditional on H-DMV), and so does `thm:finmod`
  (Euler-factor modifications `ζ ↦ ζE`) **[amended per R157_004, A18/A19: T3 is `METHOD-CONSTRAINT` modulo the
  `CITED (secondary source)` import (H-DMV′) (R157_003 §3). It needs a bridge "`𝓔_𝒫 ⪰ 0 ⟹` (ZFS_δ) for `𝒫`",
  which is unavailable for the DMV system. The operative exclusion is `cor:void` + `thm:finmod`, read as a
  statement about derivations, not definitions (P47 Restatement 12.4a)]**;
* if it does not read phase, `Ξ_a` (P47 Thm 12.4) kills it.

Corpus: R152_005 §2 ("cheap decisive test: Beurling blindness"; recommended for one round). The test was never run:
grep over phases 153–156 finds no occurrence. **SURV** → §5.

**27. `×p` measure rigidity; Kronecker-flow discrepancy.** Rudolph–Johnson–Lindenstrauss rigidity, and the
discrepancy of `τ ↦ (τ log p)_p` (GAP-157.A). As inputs to the per-window sign, these are properties of the
*positions* `{log n}` or of the multiplicative structure of the index set. Amplification `Λ + c·1_{n=2}` preserves
both. So `cor:void`, applied to the class `C_supp = {a ≥ 0 : supp a ⊆ prime powers}` (contains Λ, closed under
amplification at `n₀ = 2`), excludes every derivation whose only prime input is of this type at `T > ½log2`
(primitive form): **F1**, proved. The only arithmetic instantiation of `×n` rigidity I know is Neshveyev's
ergodic proof of Bost–Connes KMS uniqueness for `β ≤ 1`. It acts on the real axis `s = β` (MW-2), not at the
zeros **(arg.)**. An entropy-weighted version (`h(×p) = log p = Λ(p)`) has no formulation. Note that for `p^k`
the natural entropy is `k log p ≠ Λ(p^k)`. Corpus: never analysed (R151_005 §2; ROW-D-CLOSURE-PLAN §10.2 item (3),
"0–1 hits"). **EXCL** (as instantiated).

**28. Model-theoretic methods.** o-minimal uniform finiteness and cell decomposition give uniformity over
*definable families with boundedly many parameters*. The sequence `Λ` is not definable in any o-minimal expansion
of `(ℝ, <, +, ·)`: it would define the primes, an infinite discrete subset of ℝ, and definable subsets of ℝ are
finite unions of points and intervals. So `Λ(n)` can enter only as parameters, boundedly many, and by
`prop:uniform`(b) and `prop:finsupp` no finite initial segment of Λ decides `∀T RD_T`. The cosine comb over all
`τ` is not o-minimally definable either (infinitely many sign changes). ACFA/Hrushovski needs a Frobenius (P47
Thm 22.17: none on `Spec Z`). Pila–Wilkie counts positions (#27). **F1/F3 (arg.).** Corpus: never analysed (grep
"o-minimal", "Hrushovski": 0). **EXCL (arg.).**

**29. Auxiliary functions / Stepanov / Baker.** Over `F_q`, Bombieri–Stepanov gives a one-sided point count for
every `F_{q^n}` and closes by rationality. Over Z the one-sided analogue is an upper bound on prime counts, i.e.
`C_BT`, closed under deletion, so `cor:void` excludes it for `T > T₀(0) = 0.749`. The closing step (rationality =
finitely many zeros) is excluded by `thm:finZ`/`cor:infinite`. Baker's bounds on `|Σ b_p log p|` and Pila–Wilkie
counts are positions-only (#27). NG-B7 (MAP_1 l.39) records a category mismatch for Baker on the ordinates. **F1,
F3.** **EXCL.**

**30. Arithmetic-not-metric bilinear cancellation (O-150.2).** P47 Rem 27.15 withdrew T4 because
Friedlander–Iwaniec and Heath-Brown get power-saving bilinear cancellation from the arithmetic of a ring, at no
oscillatory frequency. As an *input* to a per-window derivation, any such theorem is an estimate with an error
term, so `cor:void` (and quantitatively O3) excludes it: **F1**. As a *global* route it would have to prove
`ψ(x) − x ≪ x^{1/2+ε}`, which is equivalent to the zero bound (P47 Thm 27.10, W4). The identity-level use (the
exact Vaughan/Heath-Brown identity for `Λ = μ*log` at a load-bearing step) is what P47 T2 already demands (invoke
A7/A8) and has no formulation. P47 §28.3 (42) stays open as a question about fixed-frequency floors, not as a route
to uniformity. **EXCL** per window; **EQUIV** globally.

### Family B — the literature

**31. Weil positivity / Bombieri.** The definition of row D (MW-1; E1 of the reduced statement). **EQUIV.**

**32. Hilbert–Pólya realisations.** A self-adjoint `H` with spectrum `{γ}` gives RH. Positivity
`⟨Hf,f⟩ = Σλ_j|⟨f,e_j⟩|²` is a nonnegative-summand mechanism. By T6 and O-151.4 (R151_005 §1, auditor), a summand
mechanism restates the theorem at every order, and the numerator-sign axis is what distinguishes Deligne. Every
concrete realisation in the record either presupposes the zeros or re-encodes ζ: Bost–Connes partition function
(AUDIT_A 161.9), NG-E5 (OS reconstruction retracted), NG-C3 (distributional eigenvectors). A realisation built from
exact prime data would pass F1, but its positivity is the theorem. **EQUIV.**

**33. Bost–Connes.** The KMS phase transition at `β = 1` lives on the real axis at the pole (MW-2), and its
partition function is ζ(β) (AUDIT_A Thm 161.9; CORPUS_CHECK_ROW_D_PLAN §4). It says nothing at the zeros. **EXCL.**

**34. CC archimedean positivity; prolate operators.** CC 2021 prove positivity of `W_∞` on small intervals after a
finite-codimension restriction; CCM and Connes–Moscovici match the zeros numerically with prolate spectra. In row-D
terms this is the archimedean form. It is positive on `P_T` only below `T*_{∞,P} ∈ [0.58, 0.60]` (primitive form;
`cor:Tarch`, `thm:index`); its negative index grows like `4.004T` (`thm:J`); the complete archimedean form is
negative from `0.4608` (`prop:archneg`). ES-22: a gap does not identify the ground state. **F1, F4.** **EXCL** as a
uniformity mechanism.

**35. F₁ geometry and category changes.** CC's Riemann–Roch on `Spec Z̄` has integer dimensions with *logarithmic*
growth (MAP_5 §1). The square is unbuilt in the literature (MAP_5 §2). Haran's arithmetical plane has no `H⁰`.
Borger's λ-rings and Deninger's rational Witt vectors are ring-level (NG-107). The category changes named in AUDIT_A
§3 (condensed, K-theory, motivic, Berkovich-as-codomain) were proposed to give `h⁰` quadratic growth (NG-113-O1).
Thm 19.25 and Cor 19.25b are statements about *functions* `h⁰` on the divisor domain, independent of the category
that supplies them. The one escape is the bare set `𝒢_min`, where the hypothesis is satisfiable ⟺ RH (Rem 19.25c):
an equivalence, not a route. **F5.** **EXCL.** **[amended per R157_004, A10: "category-independent" holds for
functions `h⁰` on `D^W`. It does not cover a Hodge index proved on a square without such an `h⁰` (MW-5, MAP_1:59:
"UNBUILT (not proved impossible)"). That residual moves to #37.]**

**36. Arakelov / Faltings–Hriljac.** The arithmetic Hodge index theorem is a theorem on arithmetic surfaces, whose
heights are not zeros (phase 15 M3 attempts 5–6, M10). The import was rejected in P122.007. The "mechanism" reading
(Hilbert–Samuel growth) is D-HS (#1). **F5.** **EXCL.** **[amended per R157_004, A10: excluded as an import
(P122.007) and in its `h⁰` reading. Building an arithmetic square with a Hodge index is the MW-5 cluster (#37),
which is not excluded.]**

**37. Deninger's foliated dynamics.** A leafwise cohomology with a Hodge–Riemann polarisation would give global
positivity. It is uniform over number fields (it predicts GRH for all `K`), so by T1 it must prove GRH for every `K`.
Under the filter **F4** as written, it is excluded; T1 itself is a method constraint and does not say this is
impossible (P47 Rem 18.1a). On the finite Weil window, the quaternionic Hodge–Riemann polarisation found in the
corpus is gapless (NG-62b: the `V₊` spectrum decays like `e^{−cL}`, with ζ pinned at `μ_max = 1`), which is the
Deninger-side shadow of `thm:margin` (**F2**). **EXCL** (F4 method constraint; F2 by NG-62b, which is a structural
finding, not a theorem). **[amended per R157_004, A9: WITHDRAWN. P47 §18.1 is titled "T1: the proof must be uniform
in the number field", and Rem 18.1a says T1 "does not say that GRH is out of reach". A field-uniform programme is
what T1 prescribes. NG-62b concerns a finite-window model, not Deninger's unbuilt cohomology. Verdict: NOT
EXCLUDED (unbuilt). The row is re-scoped as the MW-5 cluster, which includes the residuals of #35 and #36.]**

**38. Suzuki.** `Ψ(t) = Σ_γ (1 − cos γt)/γ²`. Suzuki's results, as read in R154_031 §3:
* Thm 1.2: RH ⟺ `g = −Ψ` is a screw function.
* Thm 1.3: RH ⟺ `⟨·,·⟩_{G_g,a} ⪰ 0` for every `a`, and it is nondegenerate under RH.
* Thm 1.7: RH ⟺ `Ψ(t) ≥ 0` pointwise.
* Thm 1.6: RH ⟺ `Ψ = O(1)`.

The window form of the screw condition is KEP (#3). Thm 1.7 is notable: a per-`t` condition on one scalar, which is
`W` evaluated on the single tent test (Fejér kernel `(2 − 2cos γt)/γ² ≥ 0`). It is again a termwise-positive kernel
under RH, like Li. Its proof of `⇐` is a partial-sum bound for a polar sequence (W4). **What translation adds:**
row D can be tested on one vector per window without loss *globally*, but not per window (`λ^W_T ≥ 0` is stronger
at fixed `T` than the one-vector inequality). Nothing toward uniformity. **EQUIV.** **[amended per R157_004, A12: the
sentence "Its proof of `⇐` is a partial-sum bound for a polar sequence (W4)" is not supported by R154_031 or any
file found. Treat it as UNVERIFIED.]**

**39. de Branges / Hermite–Biehler.** RH ⟺ `E_ξ` Hermite–Biehler ⟺ `ξ'/ξ` Herglotz on `σ > ½` (Paper 20).
de Branges's sufficient positivity condition is refuted for ζ (Conrey–Li; phase-16-surf-witness-variety/07 l.42). Suzuki identifies the
Weil space with `H(E_ξ)` under RH. ES-16: the versions tried are circular. **EQUIV.**

**40. Laguerre–Pólya, Jensen, Turán (GORZ, Csordas–Varga).** Full order: `Ξ ∈ LP` ⟺ RH. Each finite order
(Turán, fixed-degree Jensen for `n ≥ N(d)` by GORZ, finite minors) is unconditional. Paper 15 (`thm:crit`,
`thm:hr`): eventual ⟹ uniform iff the threshold is bounded or the limit form is strictly definite. For row D the
limit is degenerate (`cor:margin2`(iii): `L^W = 0` under RH; `thm:margin`). So `thm:hr`(2) says uniform positivity
cannot come from a stability argument: **F2** **[amended per R157_004, A14: `thm:hr`(2) (P15 l.210–211) says only
that no uniform *gap* exists (`inf δ_m = 0`). It does not exclude `δ_m ≥ 0` for all `m`]**. Paper 14: the interlacing and stability-preserver machinery is
arithmetic-blind (**F1**). **What translation adds:** GORZ's "for each `d`, eventually in `n`" is the analogue of
"for each `T`, decidable" (`prop:decide`). Both are the same quantifier gap, and P15 already proves the bridge
fails exactly because the limit is degenerate. **EQUIV** (full order) / **EXCL** (finite order + stability).

**41. de Bruijn–Newman.** RH ⟺ `Λ_dBN ≤ 0`, and Rodgers–Tao prove `Λ_dBN ≥ 0`. The heat flow is arithmetic-blind
(P13 Thm N5: the Lyapunov identity holds for every conjugate-symmetric configuration): **F1**. Upper bounds
`Λ ≤ t, t > 0` (Polymath) are quasi-RH: **O2**. **What translation adds:** a structural rhyme, not a mechanism.
Rodgers–Tao "`Λ ≥ 0`: ζ is at most barely real-rooted" corresponds to `thm:margin`/`cor:margin2` (`λ^W_T → 0`: row D
has no margin). Both say ζ sits exactly at the boundary. The flow `H_t` has no Euler product, so its per-window forms
are not arithmetic and fail F1. **EQUIV.**

**42. Lee–Yang / Newman / Kurasov–Sarnak.** Phase 70 (E70_1_RESULTS l.30–33): "Lee–Yang positivity" for ξ is
LP = RH, and the heat-flow forcing gives `Λ ≥ 0`, the wrong direction. Crystalline measures from stable polynomials
(Kurasov–Sarnak) are Lee–Yang (ROW-D-CLOSURE-PLAN §7(f)). Stability preservers are blind (P14): **F1**. **EQUIV.**

**43. Nyman–Beurling / Báez-Duarte / Burnol.** RH ⟺ `d_N → 0` (Báez-Duarte). Burnol (2002) gives the unconditional
lower bound `d_N² ≳ C/log N`. **What translation adds:** the dilation cutoff `θ ≥ e^{−2T}` plays the role of the
window, and Burnol's bound is a second no-margin law next to `thm:margin`, with the opposite direction and a
polynomial-in-`T` rate against our exponential one. No dictionary to certificates exists (R155_038: "HEURISTIC; no
theorem; P4 CLOSED"). **EQUIV.**

**44. Yoshida / Bombieri small windows; Burnol local.** Positivity where the prime sum is empty (complete form,
`T ≤ ½log2`). Beyond that, primes cost first (`thm:SC` remark) and are then necessary (past `0.60`, `cor:Tarch`).
It is per window only: **F2, F4**. **EXCL** beyond `½log2`.

**45. Random matrices / GUE.** Pair correlation sees only on-line spacings and is conditional on RH (NG-B8).
Universality statements are averages, field-uniform (T1, **F4**), and invariant under counterfactual off-line
orbits (P41 P3, **F1**). Paper 13 (iii): `Λ_dBN` is an extremal quantity, not an average. The certificate must hold
pointwise in `τ` on the infinite zero set (`cor:infinite`, **F3**). "RH from unconditional GUE gap universality"
(Paper 13) restates the target. **EXCL.**

**46. Selberg-trace analogues.** For the modular surface the zeros of ζ are resonances (`ρ/2`), not spectrum.
Maass–Selberg reaches exactly the absolute-convergence region (R152 Prop A.1 = MW-2). Selberg 3/16 and Ramanujan
graphs control discrete or local spectra (ROW-D-CLOSURE-PLAN §4, discarded: "local Plancherel; tempered ≠ global
zeros"). **EXCL.**

**47. Weil–Deligne over `F_q` transported to Z.** Three reasons, each proved:
* the frame defect theorem holds even on a curve over `F_q`, where RH is a theorem (P47 Thm 21.15), so Weil's
  mechanism there is *not* the frame's `h⁰`, and the frame cannot import it;
* over `F_q`, uniformity over all extensions `F_{q^n}` comes from rationality (a finite zero set, the determinate
  case of `thm:finDet`), which over Z is `thm:finZ`/`cor:infinite`;
* Deligne's extraction is T5/T6, and there is no Frobenius ring (Thm 22.17).

**F5.** **EXCL.**

**48. Probabilistic models.** Random multiplicative functions, Cramér and multiplicative chaos are class-level
models (**F1**) without the Euler product and Γ structure demanded by T2 (**F4**); N7; phases 12–13 and 19.
**EXCL.**

**49. Nicolas, Robin, Redheffer, Mertens, Riesz, Hardy–Littlewood, Speiser.** Classical equivalences. The
partial-sum ones (Mertens `M(x) ≪ x^{1/2+ε}`, Riesz) are W4. Nicolas's criterion (`∏_{p≤x} p/(p−1) > e^γ log θ(x)`
for all `x`) is notable: it has exactly the shape of E4, a per-scale finite condition on exact primes whose
uniformity is RH. **What translation adds:** a second instance of the same shape, with the same `∀`-gap. Corpus:
never treated (grep "Nicolas", "colossally": 0). **EQUIV.**

**50. Extremal functions / LP / SDP.** Beurling–Selberg, Holt–Vaaler and Cohn–Elkies majorants are termwise-signed
kernels. `lem:Rrig`/`cor:nontermwise`: no flat-top weight has `ŵ ≥ 0` (**F3**). The literature instances optimise
zero statistics *under* RH (R154_013 Tab. 1(d)). Paper 46's LP is already the exact version (`thm:D1`, `thm:O`).
**EXCL.**

**51. Sum-of-squares with arithmetic squares.** P41 P1: no decomposition into nonnegative summands contains a local
edge square. `thm:O`: no finite attainment. The only known infinite SOS is the zero side `Σ_γ |F̂(γ)|²`, which is
the RH SOS (`cor:RH`). **EXCL / EQUIV.**

**52. Other analysed non-positivity mechanisms.** Voronin universality (35/102, "RUTA CERRADA"), Fourier
interpolation (35/101), sum–product (150), prismatic/arithmetic differential equations (15 M6: local Satake data,
wrong object), functoriality (30, T1), quantum chaos (53, 67): all analysed and closed (ROW-D-CLOSURE-PLAN §10.2).
**EXCL.**

**53. Weng / Lagarias–Suzuki.** RH is proved for certain Eisenstein-period zetas built from shifted ξ. The proofs
use a Hermite–Biehler comparison that needs ξ's zeros only in the strip, not on the line: MW-2, and nothing about
ξ follows. This description is from the literature, not re-verified here. **EXCL.**

**54. Kreĭn extremal extension.** R155_040 §4(iii) (`HEURISTIC`): `μ_ζ` as the extremal singular solution, with the
certificates interior. By `thm:KEP3` any proof is RH-hard. **EQUIV.**

**55. Identity-level positivity (Selberg `Λ₂ = μ*log² ≥ 0`, Möbius as a positive adjoint).** Among Paper 37's
sixteen closed attacks (P37 abstract). **F3.** **EXCL.**

---

## §4 The known equivalences, and what the per-window language adds

The equivalences met above: Weil (MW-1); Li–Keiper and Bombieri–Lagarias; Báez-Duarte/Nyman–Beurling;
`Λ_dBN ≤ 0`; `Ξ ∈ LP` (Pólya); Hermite–Biehler/Herglotz; Suzuki's screw and `Ψ ≥ 0`; Kreĭn indeterminacy
(`thm:KEP3`); Mertens/Riesz/Redheffer; Nicolas/Robin; the modular resonance gap `β = ¼`; the clopen O4. Translating
any of them into the per-window language produces one of three outcomes, and nothing else:

1. **A proved mismatch.** Li (`cor:Li`): the kernel is not flat-top and is not admissible. Nyman–Beurling
   (R155_038). This is useful hygiene: it closes the hope that the classical criterion is a certificate in disguise.
2. **An isomorphism of frames.** Kreĭn and Suzuki: KEP is the window form of the screw condition (`thm:KEP3`).
   Nicolas: the same E4 shape. The translation is exact and moves nothing.
3. **A rhyme between no-margin laws.** Rodgers–Tao `Λ ≥ 0`, Burnol `d_N² ≳ 1/log N`, NG-62b gaplessness,
   P15 `thm:hr`(2), all against `thm:margin`. These are the same phenomenon, that ζ sits on the boundary of the
   positive cone. P15 turns the rhyme into a theorem-level exclusion of every stability-type route (#40).

**What the translation would not add, in any case:** a mechanism. By O1 the per-window language contains no object
beyond Weil's form. Its content is the filters, and each filter is stronger than the classical wall it replaces:
* F1 (with O3) says per-window proofs cannot use estimates at all;
* F2 says no margin exists (`thm:margin`);
* F3 says no finite object suffices (`thm:finZ`, `thm:arena`, `thm:O`).

A classical criterion becomes a per-window mechanism only if its proof survives all three. None does: every proof
of every equivalence above passes through the global zero set.

---

## §5 The survivor, and a one-round test

### (P157.S1) = (P152.2): the Berkovich-line difference kernel

**Object.** On the Berkovich affine line `A^{1,an}_Z` over the Banach ring `(Z, |·|_∞)` (Poineau), a kernel
`k(x,y)` that depends on a difference `x − y` in the group structure of `A¹`. It should carry the lattice
`{k log p}` as the integer points of the `p`-adic branches (Dictionary B.1). It defines an energy
`𝓔(f) = ∬ k d μ_f d μ_f` for a measure `μ_f` attached to `f ∈ C_c^∞(ℝ)`.

**Why it is the only survivor.**
* It is not an `h⁰` (F5 passes).
* It is not a sub-comb or a tree (Prop B.3 does not apply; F3 passes if the coupling is not per place).
* If `𝓔 ⪰ 0` with `𝓔(f) = W(f⋆f̃)`, it is global, hence uniform in `T` by O1, with no margin (F2 passes).
* Whether it pins exact `Λ` (F1) and separates ξ from Beurling systems and from `ξ_K` (F4) is exactly what is
  unknown.

**Test lemma (one round, pure mathematics; the outcome decides the candidate).**

> **Lemma P157.S1.** Let `𝒫` range over (i) the rational primes, (ii) Beurling systems satisfying BE1–BE8,
> (iii) the Euler-factor modifications `ζ_a = ζE` of `thm:finmod`, and (iv) the prime ideals of a number field `K`.
> For the construction of (P152.2), decide:
> **(a) Definability.** Is `μ_f` and `𝓔` defined for `𝒫` in (ii) and (iii) by the same formulas as in (i)? If yes,
> and the identity `𝓔_𝒫(f) = W_𝒫(f⋆f̃)` holds, the candidate is **excluded** by T3 (conditional on H-DMV) and by
> `thm:finmod`/O3 (a modification at one contact changes `W_T` but not the definability).
> **[amended per R157_004, A19]** As stated, this is the non-sequitur that P47 Restatement 12.4a corrected: a
> uniform *definition* transfers a *proof*, not a *truth*. Valid form: if `𝓔 ⪰ 0` is *derived* from data and
> properties common to a class of weights that contains Λ, is closed under one-term amplification, and on which
> `𝓔_a = W_T(a)` holds, then the derivation is excluded by `cor:void` + `thm:finmod`(ii) (PROVED). T3 is
> supplementary. It is `METHOD-CONSTRAINT` modulo the `CITED (secondary source)` import (H-DMV′), and it applies
> only with a bridge "`𝓔_𝒫 ⪰ 0 ⟹` (ZFS_δ) for `𝒫`".
> **(b) Locality.** Does `𝓔` decompose as `Σ_v 𝓔_v` with each `𝓔_v` depending only on the `v`-adic branch and on
> `f`? If yes, it is **excluded** by NG-E1 (local forms indefinite) and by `thm:SC` (no proper sub-family carries
> the sign).
> **[amended per R157_004, A20: (b) is not an exclusion criterion. Weil's explicit formula is already `Σ_v W_v`,
> so (b) fires on every construction that satisfies the identity, and indefinite summands do not forbid a
> positive sum. Replace it with (b′): if the positivity of `𝓔` is *inferred* from positivity of the `𝓔_v`, or of
> `𝓔_∞ + Σ_{v∈S}𝓔_v` for a finite `S`, it is excluded by `prop:finsupp`/`thm:SC` (PROVED), with NG-E1 (computed)
> as corroboration. This is R152_002's gate (g3).]**
> **(c) Phase.** For `Ξ_a` (roots `p^{±a}`), is `𝓔` still defined and still `⪰ 0`? If yes, it is **excluded** by
> P47 Thm 12.4 (it would prove a false statement).
> **[amended per R157_004, A21: Thm 12.4 concerns `h⁰_a` in the intersection frame. The fact needed is that
> `Ξ_a`'s Weil-type form is negative on some primitive test: P47 Prop 12.4B + Hardy (X16). The criterion is the
> schema of Restatement 12.4a. It fires if `𝓔_Z ⪰ 0` and `𝓔_Z = W_Z` are both derived model-uniformly over a class
> containing `Ξ_a`. An unconditional `𝓔_{Ξ_a} ⪰ 0` shows only that the identity fails for `Ξ_a`.]**
> **[added per R157_004, A22] (d) Fields and Epstein.** If the positivity derivation uses only A1–A6, A2⁺ and `𝔇`,
> it is excluded by P47 Thm 18.16 (T2; falsifier `Ξ_Q`). If it is field-uniform over `M(O_K)`, T1 requires it to
> prove GRH for all `K`. That is a standard to meet, not an exclusion. This is R152_002's gate (g2).
> **Pass** ⟺ (a), (b), (c) all fail *and* one can state the load-bearing step where the additive group law on the
> archimedean fibre couples the branches **[amended per R157_004: read (a), (b′), (c), (d) all fail, the derivation
> invokes A3 and one of A7/A8/A9 (T2), and that step is stated]**. Only then is a positivity question `𝓔 ⪰ 0` worth posing, and it is RH
> (O1).

**Expected outcome (stated in advance, not claimed).** Clause (a) is the likely failure point. Poineau's
construction starts from the Banach ring `(Z, |·|_∞)` and its multiplicative seminorms, and a Beurling system has no
such ring. So the construction is *not* defined for (ii), which is a pass of (a). The question then moves to (b):
whether the energy on `A^{1,an}_Z` couples branches other than through the trivial-norm point. That is where it
should die or live. The round should end with a proved statement of (b) either way.
**[amended per R157_004, A23]** This expectation conflicts with the record: R152_002:232–233 estimates that (g1)
*fails*, and R152_001:407 says Dictionary B.1 "applies verbatim to a Beurling generalized-prime system". The test
must decide whether `μ_f` and `k` factor through the atom list `{(q, k log q)}` with its weights. If they do, the
geometry of `A^{1,an}_Z` is decorative and (a) fires via `cor:void`, whatever ring a Beurling system lacks.

No second survivor **[amended per R157_004: no second *formulated* survivor. The MW-5 cluster (#37) is not excluded,
but it has no object and no one-round test]**. The identity-level use of `Λ = μ*log` (#30) and an entropy-weighted `×p` construction (#27)
are *regions* not excluded by any proved statement, but they have no object and no statement. Proposing a test for
them would be inventing the candidate, which the record's rule ("check the corpus first; do not sell") forbids here.

---

## §6 Honest paragraph

The search was run as the filter prescribes and it is exhaustive for what the corpus and the standard literature
contain: 55 candidates, each checked against a proved statement. The result is almost entirely negative, and the
negative has a reason that is itself a small finding.

**Uniformity in `T` is not a property a mechanism can supply on the side.** By nestedness (O1) it is global Weil
positivity. So "a mechanism for uniformity" is "a proof of RH", and the per-window reduction, valuable as it is,
contributes filters, not a new object. The filters are strong. The margin-resolution corollary O3, to be audited,
makes F1 quantitative: at window `T ≥ 1`, changing a single `Λ(n₀)` by about `e^{−14T}` can already flip the
primitive sign **[amended per R157_004, A2/A3: by at most `2·10⁹Te^{−14.449T}/|c_{F*}(log n₀)|`, which is vacuous for
`T ≤ 1.51`, and only when the minimiser does not vanish at that contact]**. So no estimate of any kind acts per window. Estimates can only act globally, through the partial-sum
wall W4, where the per-window structure plays no role.

Every classical equivalence of RH either fails to translate (Li, Nyman–Beurling), translates isomorphically (Kreĭn,
Suzuki, Nicolas), or rhymes with our no-margin theorem (Rodgers–Tao, Burnol, Paper 15). None of them brings a
mechanism.

Exactly one candidate is not excluded by anything proved: the Berkovich-line difference kernel (P152.2).
**[amended per R157_004: two entries are not excluded. One is the formulated (P152.2). The other is the unbuilt MW-5
cluster (#37: Deninger; a CC or Arakelov square with a Hodge index not routed through `h⁰`), which has no object
and no test.]** It is
unbuilt, with a pre-registered test that was recommended in phase 152 and never run; §5 restates it so that one
round decides it. I would not call it promising, only not excluded, and "not excluded" was the bar.

If that round kills it, the honest conclusion is option (A) of the reduced statement. The map is complete, row D is
RH, and the programme has no mechanism to propose. The one change worth recording is that O3 and O4 (both
equivalences or constraints, neither a sign) could be added to Paper 46 after an audit.
**[amended per R157_004: O3 is cleared as an optional remark in the amended form of R157_004 §5(i). O4 is cleared
only as a one-sentence RESTATEMENT citing Bombieri 2000 Thms 1, 3, 5 (R157_004 §5(ii)). It is not new.]**
No sign is claimed or suggested for ζ at any window, in either form.
