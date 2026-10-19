# R158_003 — Audit of R158_001 (the MW-5 specification sheet), phase 158

Object: `R158_001_SPEC_SHEET.md`, checked against `R158_000_BLUEPRINT.md` and
against the labelled statements it cites, each opened at its label (process rule ). This audit touches no
paper, no README, and not `R158_002`. Amendments are applied in place to R158_001 as A1–A20, each marked "[amended per
R158_003]", with struck text kept. **No sign is claimed, asserted or suggested.** Row D: no label; the endpoint of
record is unchanged.

Sources opened this review (arXiv PDF → `pdftotext`, or the abstract page):
* math/0204110 (Deninger), full text: Thm 2.1, Cor 3.5 Rem 2–3, §4 (21).
* math/0204194 (Deninger, elliptic example), full text: the Hasse sentence, the `H`-action, the metric `g̃`, the
  measure `μ̃`.
* 1307.3851 (Leichtnam), full text: §2 eq. (6), axioms 5]–6], Comment 6, Comment 8, Prop 2, §4.4.
* math/9811068 (Connes, Selecta 1999), full text: introduction, the Jordan-form remark after Thm 1.
* 1405.4527 (CC, arithmetic site), full text and abstract.
* 1805.10501 (CC, RR strategy), full text: §1, §3.1.
* 1807.06400 v4 (Deninger), full text: §1.
* 0906.3146 (Borger), full text: introduction.
* 1507.05818 and 2402.06671: abstract only.

## §1 Verdict table

| # | item | verdict | fix |
|---|---|---|---|
| 1 | **Lemma T**, (⇒) | **CORRECT.** (D3) makes `U_t = e^{−t/2}φ^t` isometric, and it is a group, hence unitary. By Stone, `Θ − ½` is skew-adjoint, so every eigenvalue has real part `½`. (D2) identifies the eigenvalues with the zeros. This is word for word Leichtnam §2 eq. (6) ("This argument comes from an idea of Serre [Se60] and has been formalized in the foliation case in [De-Si02]"), and it is Deninger Thm 2.1 with `α = 1` | A1: statement re-phrased. The qualifier "if `H¹` may be defined from the zeros" belongs to (⇐) only; (⇒) holds for every realisation |
| 1′ | **Lemma T**, (⇐) | **CORRECT.** For `h ∈ C_c^∞`, `Φ_h` decays faster than any power, uniformly on the strip, and `N(Γ) ≪ Γ log Γ`, so `Σ m_ρ|Φ_h(ρ)| < ∞`. The operator is trace class and its Lidskii trace is the zero side of the unconditional explicit formula | none needed; conventions made explicit (A1) |
| 1″ | multiplicities | the sheet's "algebraic multiplicity" is harmless, because (D3) forces semisimplicity (algebraic = geometric). **New and relevant for R158_002:** Connes' realisation has Jordan blocks at multiple zeros, "compatible with the almost unitary condition … but not with skew symmetry" (math/9811068). Leichtnam's 6] uses generalised eigenspaces, which 5] reduces to eigenspaces | A1 |
| 1‴ | trace conventions | (⇒) uses no trace. Leichtnam's 6] allows a trace "in some generalized sense" (AKL); nothing in Lemma T depends on that choice | A1 |
| 1⁗ | novelty | **CLASSICAL, no novelty.** The (⇒) direction is Serre 1960 / Deninger–Singhof / Leichtnam §2 and Comment 6 ("the first six Assumptions imply the Riemann hypothesis"). The (⇐) direction is the trivial Hilbert–Pólya converse (Connes introduction; corpus R157_002 row 32, EQUIV). The corpus has neighbouring RH-equivalences too: phase 113 `(E°)` ⟺ RH (`113_10` Thms 4.2/4.3), and P46 Rem 19.25c(i) | A1 labels it `PROVED (elementary); content CLASSICAL`; the sheet never claimed novelty, and now says so |
| 1⁵ | Cor T′ | **CORRECT for real `F`**, and that is P47's convention (`prop:P`, `lem:roughEF`: the product formula is stated for real `F`). The statement said "`F ∈ L²(I_T)`". For complex `F` it holds with `Σ_ρΦ_{c_F}(ρ)`. `F(U)` is HS only when the zero sum converges, i.e. `lem:roughEF`(b) | A1′ |
| 2 | (P-HI) ↔ primitive form | **SIGNS CORRECT.** P46 (11.6), l.2136: `I_∞(F,F) = 2Φ_F(0)Φ_F(1) − Σ_ρΦ_F(ρ)Φ_F(1−ρ)` (real `F ∈ D^W`). P47 `eq:W` l.134–138 and `lem:roughEF`: `Φ_F(1) = A`, `Φ_F(0) = B` for real `F`. On primitive real tests `I_∞ = −𝔞_T`, so Hodge index `I_∞ ≤ 0` ⟺ `𝔞_T ≥ 0` (E2). Castelnuovo `I_∞ ≤ 2Φ(0)Φ(1)` ⟺ `W ≥ 0` (E1) | A2 records the check, the real-test proviso, and that the Castelnuovo inequality is E1 (RH), not a theorem |
| 2′ | (P-HS) ↔ complete form | **CORRECT** (Cor T′). The primitive form is its restriction; per window the converse needs `𝔊_T ≻ 0` (`thm:parityschur`(c), checked) | A1′ |
| 3 | constraints C1–C27 | 16 of 27 opened at their labels (§2). **Stronger than source:** C3, C4 (label), C12 ("its zeros lie on"), C17 (reading), C18 ("identity type"), C21 (contradicts `thm:D1`), C25 (Thm 21.17 only for `g = 1`; (4a)–(4c) RH-strength), C26 (Parseval qualifier). **Misattributed:** C5 (two statements merged), C6 (Assumption 7 vs §4.4). C9 was missing its direction and non-degeneracy provisos | A3–A13 |
| 4 | object test | 4 items rest **wholly** on proved constraints (OT-3, OT-8 core, OT-11, and OT-12 via OT-2). 5 mix PROVED necessity with a DESIGN or HEURISTIC part (OT-1, OT-2, OT-5′, OT-7, OT-9). OT-5 "expected A3" is **HEURISTIC**. OT-4, OT-6, OT-10 were **stronger than the record** as worded. OT-9 contains an **RH-strength** clause. Remark 3.1's "none RH-strength" was false for OT-9, and for OT-2 in Connes' case. The OT list omits P46 §28.4 clauses (2) and (3) | A14 (status table Rem 3.0 + pass-condition fixes), A15, A16 (new Rem 3.3) |
| 5 | 18-framework table | 8 arXiv sources checked (§4). **One first-failure claim is wrong:** Connes' adèle class space, where the sheet said "trace formula = explicit formula (CITED)". Connes proves the S-local trace formula; the **global** trace formula is equivalent to RH (introduction; §VIII Thm 5). First failure is OT-2, not OT-5′. The rest are confirmed. The abstract-only entries (Scaling Site, Leichtnam `p`-adic, AKL, Kopei 2011, 0709.2801) are correctly marked. Corpus claims (Doc 130, Doc 128:24/63/166, M8 F1/F5) are confirmed at file:line, with one caveat on Doc 130's "verbatim" lines | A17, A20 |
| 6 | the conclusion | **STATED TOO STRONGLY.** "No published framework" rests on 18 surveyed. "OT-9 ∧ OT-12 is the precise residual" contradicts §0 (OT-5′ is the whole content), and OT-9 applies only to an RR route. The conjunction is necessary on one route and nowhere shown sufficient. The residual is RH-strength and should be called so | A18 (restated, struck text kept) |

## §2 Constraints sampled at their labels (16 of 27)

| C | source opened | finding | amendment |
|---|---|---|---|
| C3 | P46 Thm 22.17 l.10082; Prop 22.5 l.9679 | 22.17 is about `Spec Z` as a scheme (terminal object, self-maps of the base). "Compatible with the explicit formula" is not in the source. "Frobenius cannot be an endomorphism of a one-variable object" is too wide: CC's arithmetic site, not a scheme, realises Frobenius correspondences | A3 |
| C4 | P46 Cor 22.9a l.9842 | labelled "PROVED given the cited obstruction" (P122.028), on the radial carrier | A4 |
| C5 | Deninger math/0204110 Thm 2.1, Cor 3.5 Rem 2–3 (text) | Rem 2 (α = 0; α ≠ 0 expected on generalized solenoids) and Rem 3 (finitely generated periods; fixed points needed) are separate statements | A5 |
| C6 | Leichtnam Prop 2, Comment 8, §4.4 (text) | Assumption 7] addresses the factor −2 at `t > 0`; the `t < 0` riddle is resolved formally in §4.4 by the covering `S_{Q[i]} → S_Q` (mild singularity at `x_∞`) | A6 |
| C8 | P47 `cor:void` l.3563, `thm:finmod` l.3452 | faithful (deletion `T > T_0(0)`; amplification `T > ½log 2`; `𝒞_BT` under deletion) | — |
| C9 | P47 `rem:resweights` l.3484 | the direction `s = sgn c_{F⋆}` and the admissibility `ε ≤ Λ(n₀)` for `s = −1` are missing; the non-degeneracy `c_{F⋆}(log n₀) ≠ 0` is OPEN; "Lemma D" = `lem:degen` | A7 |
| C12 | P46 Prop 12.4B l.2899, Thm 12.4 l.3006, Thm 18.14 l.5284, Restatement 12.4a, Rem 12.4a′ | "`Ξ_a` satisfies A1, A2, A2⁺, A4–A9": faithful. "Its zeros lie on `Re s = ½ ± a`" overstates Hardy: only infinitely many are located (the same slip is in P46 Prop 27.17 item 2; flagged §6) | A8 |
| C13 | P46 Thm 18.16 (T2) l.5327, Lemma 18.15 | faithful | — |
| C14 | P46 Rem 27.16 (T3), 27.16a, Prop 27.17 | faithful ("modulo (H-DMV)", CITED secondary) | — |
| C15 | P46 Thm 18.1 (T1), Rem 18.1a, Cor 18.17 | faithful. OT-10 derived from it was stronger (A14) | — |
| C17 | P46 Prop 28.4 l.12359; P47 `cor:Qp` l.3431, `thm:SC` l.2184, `prop:finsupp` l.3543 | numbers faithful (`Q_p(F_φ) = −v_p‖φ‖²`, `A < −C_0 = 5.3721…`, `T_0(0) = 0.74921`). But `cor:Qp` explicitly "gives no sign": a sum of indefinite local forms may be positive. C17/OT-6 must exclude *derivations* place by place, not sums | A9, A14 |
| C18 | P47 `thm:margin` l.3277, `cor:margin1`, `cor:margin2` l.3328 | numbers faithful (`4·10⁹ T e^{−15.449T}`, `T ≥ 1`). "Must be of identity type" is not implied (per-window bounds `c(T) → 0` are not excluded) | A10 |
| C20 | P47 `lem:Rrig` l.1374, `thm:Z` l.1234 | faithful; the HEURISTIC label on the reading is correct | — |
| C21 | P47 `thm:O` l.665, `thm:D1` l.601 | **wrong as written.** `thm:D1`: for `λ^P_T > 0`, `λ^A_T > 0` *is* provable by a finite certificate. `thm:O` excludes only an exact finite dual identity. "Not an identity" collides with C18's "identity type" | A11 |
| C22 | P47 `thm:parityschur`(c) l.3814, `cor:convfail` l.3996, `prop:polarcap` | faithful (`[0.4608, 0.58]`, `½log 3`, `θ ≤ 0.8148`; the `θ_* < 1` clause via Zhu, CITED) | — |
| C23 | P46 Thm 19.25 l.6406, Cor 19.25b l.6509 (localised form) | faithful, including hypotheses (X19), (E2), (E3d) | — |
| C24 | P46 Thm 21.15 l.9031, Rem 21.16a, Rem 21.23 (§21.7) | faithful ("the cone … is the whole gap"; missing: `Γ_{m+nπ}` and fibres) | — |
| C25 | P46 Prop 21.21 l.9277, §21.8 (P145′) l.9432, Thm 21.17 l.9081 | Thm 21.17 is PROVED for `g = 1` only. (4a) ends in bigness, which is RH by Prop 21.21, so the deliverable is RH-strength | A12 |
| C26 | P46 Thm 27.3 l.11579 | holds for Parseval-type `𝔅` (Def 27.2) with the stated family hypotheses | A13 |
| C27 | P46 Thms 27.10, 27.11, §28.4 l.12439 | faithful; the six clauses are summarised correctly | — (A16 adds them to the OT) |

Not re-opened: C1, C2, C7, C10, C11, C16, C19. They cite labels (`thm:finZ`, `thm:arena`, `prop:finite`, Prop 22.5,
`lem:monoT`) that I read for other rows; nothing contradicting them was seen. C7 and C2 (Suzuki/Selberg via MAP_5)
rest on corpus files not re-read here.

## §3 The object test

The status of each item is now a table inside R158_001 (Remark 3.0, A14). The points that change the reading:

* **OT-3** is implied by Lemma T. Its catalogue sweep is inspection.
* **OT-4.** The record constrains *derivations*, not definitions. Rem 12.4a′: "uniformity of a *definition* transfers
  a *proof*, never the *truth*". A substitute may break a line of the positivity proof rather than an axiom, and the
  pass condition is widened to allow that.
* **OT-5, the `Ξ_a` gate.** The necessity of a `Ξ_a`-failing step is PROVED; "that axiom is A3" is HEURISTIC.
  Audit point (ii) of R158_001 §5 asks what `Ξ_a` would need. Formally it needs two copies of a (D1)–(D3) system with
  flows twisted by `e^{±at}`. That system has `H⁰, H²` of rank 2 (`Θ ∈ {±a}`, `{1 ± a}`) and two conformal factors
  `e^{(1±2a)t}`, so it violates the rank-one clause of (D1) and the single-factor clause of (D3) together. Any object
  satisfying (D1) and (D3) passes the gate **automatically** (Lemma T(⇒) + Hardy). The gate therefore has content only
  for the *derivation* of (D3), which is OT-5′.
* **OT-6** as worded ("not a sum of local forms") is excluded by nothing: `cor:Qp` says the opposite. The item now
  reads "not *derived* as a sum of local positivities".
* **OT-9.** Its filter part is PROVED: outside Thm 19.25, Cor 19.25b and Thm 21.15; two variables on the radial
  carrier (Cor 22.9a, given P122.028); cone `⊋ 𝓔` in the model (Rem 21.16a). Its clause "(P145′)(4a)–(4c)
  constructed" is **RH-strength** (Prop 21.21). A corpus item not cited in R158_001 bears on it: phase 113 O2
  (NO-GO-LIST:490–517), infinite mutual intersection of the `δ_n` in the Schwartz-data class (A19).
* **OT-10.** T1 alone gives only a disjunction: either a named separating property, or field uniformity at GRH
  strength. The family requirement comes from §28.4(6) and F4 as amended (R157_000 l.10).
* **OT-12** is implied by OT-2 through C11. The concrete mechanism is Leichtnam's §4.4 singular covering; it is not an
  open riddle at the level of the axioms (A6).
* **Missing from the OT list:** P46 §28.4 clauses (2) (polar divisor fixed by local data) and (3) (zeros holomorphic to
  the left). Passing OT-1…OT-12 does not reopen row D (A16, Remark 3.3).

## §4 The frameworks table: sources checked

| framework | source | claim checked | result |
|---|---|---|---|
| CC arithmetic site | 1405.4527 (text + abstract) | "realize the Frobenius correspondences in the square … compute their composition"; "This translation would require … an adequate version of the Riemann-Roch theorem in characteristic 1" | **confirmed**; first failure OT-1 stands |
| CC scaling site | 1507.05818 (abstract) | "The Riemann-Roch formula holds and involves real valued dimensions and real degrees" | **confirmed at abstract level**; stays CITED (abstract) |
| CC RR strategy | 1805.10501 (text) | "a substantial difficulty. The problem, which is still open at this time, has to do with an appropriate definition of the sheaf cohomology (as idempotent monoid) H¹ … the presence of the null elements creates unwanted contributions"; "RH ⟺ s(f,f) ≤ 0 ∀f" (§3.1) | **confirmed**; OT-1 stands; the OT-9-at-risk reading is sound |
| Deninger surveys | math/0204110 (text) | Thm 2.1 (compact 3-manifold, Riemannian foliation, dense leaf; `Θ = 0`, `α`, `α/2 + S`); Cor 3.5 Rem 2–3; §4 (21) `χ_Ar = −log|d_K|` | **confirmed**; C5 re-split (A5) |
| Deninger `W_rat` | 1807.06400 v4 (text) | "There are no fixed points of the flow"; "a bit more involved"; "infinite dimensional whereas ideally … dimension 2 dim X0"; "the cohomological problem pointed out in [KS18] … persists" | **confirmed**; OT-1 first, OT-12 further |
| Deninger formalism (Leichtnam) | 1307.3851 (text + abstract) | "(whose existence is still unknown)"; axioms 5]–6]; Comment 6 ("might be too strong"; "the first six Assumptions imply the Riemann hypothesis"); Prop 2 | **confirmed**; C6 attribution corrected (A6) |
| Borger | 0906.3146 (text) | "a surface bearing some kind of intersection theory"; "says nothing about the archimedean place of Q, it is hard to imagine this succeeding without further ideas" | **confirmed** |
| AKL | 2402.06671 (abstract) | closed manifold, codimension 1, transversely oriented; simple closed orbits, transversely simple preserved leaves; two spaces of leafwise currents (conormal, dual-conormal); Lefschetz distribution; conjecture of Deninger | **confirmed at abstract level**. The exact verb ("solves"/"resolves") was not verified from a clean abstract string. Stays CITED (abstract) |
| Connes adèle class space | math/9811068 (text) | the sheet: "trace formula = explicit formula (Connes; CITED)" | **REFUTED as stated.** Introduction: "its equality with the geometric side, i.e. the global trace formula, is equivalent to the Riemann Hypothesis for all L-functions with Grössencharakter"; the S-local case is proved (§VII). First failure is **OT-2**. Tally: OT-2 in 7, OT-5′ in 1 (A17) |
| Deninger elliptic | math/0204194 (text) | Hasse input | **confirmed in substance**: "According to a theorem of Hasse … we have |ξ|² = q"; `H` acts by `(ξ^{−ν}z, ξ^{−ν}v̂, t + ν log q)`; `g̃ = e^t Re(ξη̄)` on tangent vectors and `μ̃` are `H`-invariant because `|ξ|² = q`. The sheet (and Doc 130) wrote the metric with the Frobenius `ξ` in place of tangent vectors (A20) |

Corpus claims at file:line:
* Doc 128:24: "no está construido … desconocida"; AKL; spectral rigidity 1712.04181. Confirmed.
* Doc 128:63: AKL abstract. Confirmed.
* Doc 128:166: Leichtnam "whose existence is still unknown". Confirmed.
* Doc 130: verdict "INDETERMINABLE con fuerte sesgo a CIRCULAR" at l.30 and l.223; ENUNCIADO-MÍNIMO-130 at §5.3,
  l.203; the Hasse sentence at l.82. Confirmed. **Caveat:** the further "verbatim" sentences at l.82 are a
  summariser's paraphrase and are not source text (checked against the PDF); the conclusion does not depend on them.
* M8 F1 (l.14, continuous spectrum), F5 (l.47–55, finite transverse measure and finite-dimensional basic cohomology
  fail). Confirmed.
* NO-GO-LIST:221–232 MW-5 ("real-valued, not even integral" at l.230). Confirmed.
* Grep counts: Kopei 0, Leichtnam 1 (Doc 128 only), ENUNCIADO-MÍNIMO-130 3, Borger 14. Confirmed. NG-107 is 5 outside
  phase 158, 6 with R158_000.

## §5 The conclusion

The original: "no published framework combines OT-9 with OT-12; that conjunction is the precise MW-5 residual;
OPEN". It is **not at the right strength**, for four reasons:
1. It is universal over the literature, but the survey is over 18 frameworks.
2. OT-9 is conditional ("if a Riemann–Roch/`h⁰` route is used"), so the conjunction is not the residual of the
   (P-HS)/Deninger route.
3. It contradicts §0 of the same sheet ("the whole content of MW-5 is OT-5′").
4. It is silent on strength: the residual, if met, proves RH.

A18 replaces it with a route-split statement. On the RR route, none of the 18 has OT-9 ∧ OT-12. On the conformal route,
none has OT-1 ∧ OT-5′ ∧ OT-12. The residual is OT-5′ on a carrier passing OT-1 and OT-2 (hence OT-12), plus OT-9 on the
RR route and the P46 §28.4 clauses. It is OPEN and RH-strength. With A18 the conclusion is stated at the right strength.

## §6 Flags (papers not edited)

1. **P46 Restatement 19.29(iv)** (l.6630ff.) reads "Theorem 19.6 gives (a) and (c) unconditionally … — the bound
   `I_∞(E,E) ≤ 2ab ≤ (deg E)²/2` is the surface inequality". Thm 19.6(ii) proves clause (c) only. The inequality
   `I_∞ ≤ 2ab` is E1, i.e. RH. The sentence should be read as a dictionary of *shapes*; as printed it can be misread
   as asserting the bound. Recommend a wording fix at the next P46 revision.
2. **P46 Prop 27.17 item 2**: "its zeros lying on `Re s = ½ ± a`". The correct statement is "infinitely many of its
   zeros" (Hardy); the same slip is fixed in R158_001 C12 (A8).
3. **Doc 130 l.82**: the extra "verbatim" lines attributed to math/0204194 are not source text. The corpus conclusion
   stands (A20).

## §7 Handover to R158_002 (not edited)

The following points from this audit bear directly on the adèle class foliation candidate:
* Connes' global trace formula on the adèle class space is itself RH-equivalent (A17).
* At multiple zeros Connes' `D` has Jordan blocks, which is incompatible with (D3) (A1).
* OT-5 is automatic under (D3). The content sits in how (D3) is derived.

## §8 Final checklist

| check | status |
|---|---|
| Lemma T both directions verified; multiplicities (algebraic = geometric under (D3); Leichtnam 6]; Connes Jordan blocks); trace conventions; classical attribution (Serre / Deninger Thm 2.1 / Leichtnam §2, Comment 6 / Hilbert–Pólya); no novelty claimed | **CLEARED** (A1, A1′) |
| (P-HI)/(P-HS) signs against P46 (11.6) l.2136 and P47 `eq:W` l.134, `lem:roughEF`; real-test proviso recorded | **CLEARED** (A2, A1′) |
| ≥ 12 constraints opened at their labels, including every one named in the brief; overstatements amended | **CLEARED** (16 opened; A3–A13) |
| OT-1…OT-12 each labelled implied / DESIGN / HEURISTIC / RH-strength; OT-3, OT-4, OT-5, OT-9, OT-12 specifically | **CLEARED** (A14, A15) |
| §28.4 reopening clauses linked to the OT; (2), (3) flagged missing | **CLEARED** (A16) |
| ≥ 8 framework first-failure claims checked against open sources; abstract-only entries kept CITED (abstract) | **CLEARED** (10 checked; one refuted and corrected, A17) |
| corpus claims at file:line (Doc 130, Doc 128, M8, NO-GO-LIST) | **CLEARED** (Doc 130 paraphrase caveat, A20) |
| corpus-first rule: omitted prior item found and added (phase 113 O1–O3, d3) | **CLEARED** (A19) |
| conclusion at the right strength | **CLEARED** after A18 |
| no sign claimed; no paper, README or R158_002 edited | **CLEARED** |

Verdict on R158_001: **ACCEPTED AS AMENDED.** It is a filter, not an object. Its organising lemma is classical. Its
residual is correctly OPEN and, after A18, correctly called RH-strength.
