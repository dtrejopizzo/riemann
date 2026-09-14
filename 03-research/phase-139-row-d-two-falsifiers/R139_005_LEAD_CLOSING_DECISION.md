# R139.005 — Lead closing decision, phase 139 (the two falsifiers and the method theorem)

*Lead of record: Fable 5.1. Date 2026-09-13. Inputs: R139_000, CORPUS_CHECK_ROW_D_PLAN, R139_001 (rounds
1–2 in place), R139_002 (hostile audit, 16 findings), R139_003 (ledger), R139_004 (confirmation: CONFIRMED
with residue H17–H21, applied by the lead in place). Lead's own checks: D.19.5's Landau argument with real
zeros present; the Stirling exponent `πd/4` and the contour-shift existence proof of `K_K`; the
Prop. 12.6 reading (P46-5 correctly withdrawn).*

## 1. Results of record

| item | statement | label |
|---|---|---|
| D.19.2 | Epstein canonical class `K_Q(t) = ¼e^{t/2}Σ'(y_v²−2y_v)e^{−y_v}`, even, arbitrary exponential decay, `Φ_{K_Q} = Ξ_Q = ½s(s−1)Λ_Q`, polar set `{0,1}` equimodular | PROVED |
| D.19.4a | `Λ_{x²+ky²}` has real zeros in `(0,1)` for all large `k` (with `h(−4k) > 1`); hence `K_Q > 0` is **false** (blueprint refuted) and Prop. 12.6's "`Z > 0` on `R`" fails for Epstein | PROVED |
| D.19.5 | **Hodge index fails for `Ξ_Q`** (principal form, `h > 1`) on the effective cone, via Landau + Davenport–Heilbronn zeros right of `Re s = 1`; Voronin's zeros would not suffice | PROVED |
| D.19.5b | the witness cannot lie in the translation cone `Λ_Q^+` (Lorentzian by equimodularity) | PROVED |
| D.19.7 | **T2** (METHOD-CONSTRAINT with axiom list A1–A9 and Transfer Lemma D.19.7c): no derivation of Hodge index for `ξ` from A1–A6 + A2⁺ alone; any proof must use A3 (equimodularity, pinned by `Ξ_a`) **and** at least one of A7/A8/A9 (zero strip = polar strip / Euler product / real positivity, pinned by `Ξ_Q`) **and** be field-uniform (T1) | METHOD-CONSTRAINT; falsifier half PROVED |
| D.19.7d | escaping Epstein through A9 for `ξ_K` ⟺ no real zero of `ζ_K` in `(0,1)` ⟺ no Siegel zero — not field-uniform | PROVED |
| D.20.1 | field-uniform frame for every number field, with `K_K` constructed by contour shift (no theta, no units) and `deg_K`, `I_∞^{(K)}(K_K,K_K) = r²/2` | PROVED |
| D.20.2 | base change: `I_∞^{(L)}(N^*F,N^*F) = I_∞^{(K)}(F,F) + Σ_{[χ]} I_∞^{([χ])}(F,F)` over conjugate packets; extra terms primitive | PROVED (abelian), PROVED-CONDITIONAL on Artin holomorphy (general) |
| D.21 | consolidated ledger of Weil's proof vs rows A–C; **W2 (Riemann–Roch on the square) ABSENT**, everything else PRESENT or PRESENT-CONDITIONAL | PROVED-IN-REPOSITORY + new ledger |
| (P139) | see §2 | OPEN (the construction problem) |

Withdrawn/downgraded during the phase: P46-5 (Prop. 12.6 conflation) — a misreading, now editorial;
Thm D.20.2 general case — conditional; D.19.3–D.19.6 restricted to principal forms (O-10 for general `Q`).

## 2. The construction problem (P139), final form

Let `𝒵` be the class of `Z` satisfying A1, A2, A2⁺, A4, A5, A6 (contains `ξ`, every `ξ_K`, every `Ξ_a`,
and `Ξ_Q` for principal `Q` with `h > 1`). Construct a rule `Z ↦ h⁰_Z` defined on `𝒵` such that for
every number field `K` the member `h⁰_{ξ_K}` satisfies (a) `h⁰ ≥ 0`, (b′) `h⁰(E) > 0 ⟹ ∃E' ≥ 0,
E' ≢ 0, E − E' ∈ 𝓝_∞^{(K)}`, (c) `h⁰(E) + h⁰(K_K − E) ≥ ½I_∞^{(K)}(E,E) − ½I_∞^{(K)}(E,K_K) + χ_K`,
with the naming clause (N): the proof must name the line using A3 and the line using A7/A8/A9.
Growth forced by (c): `h⁰_K(mK_K) ≥ (r²/4)m² + O(m)`; for `Q`, `¼m²`. Acceptance tests: (AT-1) the rule
at `Ξ_Q` must fail at a named line (for a row-B construction: `Frob_m ⋆ Frob_n = Frob_{mn}`); (AT-2)
at `Ξ_a` at a use of A3; (AT-3) no line distinguishes `Q` from `K`. Clause (N) is an audit protocol on
proofs, carried by the hostile auditor, so that the object itself stays purely mathematical.

## 3. What the phase teaches

The sign requires simultaneously the polar block's equimodularity and the Euler product, and must be
proved for all number fields at once. The row-B structure that Epstein lacks is precisely the
inverse-semigroup law `Frob_m ⋆ Frob_n = Frob_{mn}` (multiplicativity of coefficients fails for `r_Q(n)`
because of the class group). This localizes the Euler-product step of `(P139)` inside row B, which is
where phase 140 builds.

## 4. Decision

Phase 139 closed; no label change for row D. Paper-facing list (P46-6, P46-7, P46-8, P46-9, P42-1,
doc-80 numbering) recorded for Part III. Open items O-1…O-12 carried; O-9 (`Sh_Z` for a general number
field) is the first task of phase 140.
