# R135.007 — Closing decision, phase 135 (row D, first construction campaign)

Rounds: report ×3 (R135_001, R135_004, R135_006), audit ×2 (R135_002, R135_005), audit round 1 R135_003 (§0 written before reading round 1; §4 cross-check).

## 1. Grep verification of round 3

| item | result |
|---|---|
| N1 | (11.17) reads `C_F ≤ |Φ_F(0)| + |Φ_F(1)| + Σ_ρ|Φ_F(1−ρ)|`; no `½` factor survives ✓ |
| N2 | Thm 13.5(iii) proves (b′) unconditionally for `h⁰_Z`; "(b′) off" occurs nowhere ✓ |
| N3 | Prop 12.6: "Not claimed for `Ξ_a`: Theorem 11.12" ✓ |
| N4 | §10 label section carries the schema-honest wording; "must use the Euler product" survives only inside withdrawal brackets (lines 1470, 1842, 3045, 3716) ✓ |
| N5 | Prop 12.4B re-read on `|Im z| ≤ ½+a`; `D ↦ D+4` re-derived ✓ |
| N6 | Remark 13.6b labelled `HEURISTIC`, `O(log q/q)` ✓ |
| N7/M11 | §1.13 amended again (line 185) ✓ |
| N8/M15 | `log #∅ := 0` stated as convention; import line of Thm 12.3 without (X15) ✓ |
| sign sweep | `I_∞(F,F) ≤ 0` occurs twice, both inside the conditional Theorem 12.3 (hypothesis/conclusion) ✓ |
| label | §10 "None." unchanged ✓ |
| scripts | `polya_class.py --check` exit 0; `canonical_pairings.py`, `h0_candidate.py` `--check` exit 0 (report, audit `--fast` re-run); the blueprint's independent `lead_polya_check.py` exit 0 ✓ |

## 2. Decision

    ROW D: NO LABEL. Phase 135 is closed. Paper 46 Part II (§§11–16) is accepted
           as a REDUCTION with no sign, fit per R135_005 after the round-3 erratum.

What is now proved in the repository (labels as recorded in Paper 46):

1. **The Weil completion `D^W`** (Def 11.1): `C²`, decay `e^{−(1+ε)|t|}`; the explicit formula and the comparison identity (9.9) extend to it with absolutely convergent zero sum (Thms 11.3, 11.5; `I_∞` by polarization, Lemma 11.4a). Not the colimit of Paper 43 (Thm 14.3).
2. **The canonical class** `K` = Pólya's kernel, `Φ_K = ξ`, `K > 0` (elementary), `M(K) = (½,½)`, `I_∞(F,K) = ½ deg F` for every `F ∈ D^W`, `I_∞(K,K) = ½`; `2K` is a degree form and an ample class inside `D^W` (Thms 11.7, 11.8, 11.14(iii)). The blueprint's `A = e_+ + e_-` is not a class; `2K` replaces it.
3. **The perp and the radical**: `(P^W)^⊥ = {Φ_G|_{Z(ξ)} = 0}` (order-one vanishing; equality with `ξ·entire` iff all zeros simple, `OPEN`, not asserted); `𝓝_∞ = P^W ∩ (P^W)^⊥ ≠ 0`, and `ΠK⋆D^W ⊊ 𝓝_∞` (Prop 11.11a); `𝓝_∞ ∩ C_c^∞ = 0` by counting distinct zeros against exponential type, with Conrey's `≥ 2/5` simple zeros as import (X18) (Thm 11.12) — the colimit statement Paper 45 Remark 12.4 declined to make. Separation Lemma 11.9 (Laplace transform + residue, multiplicity-honest, no RH).
4. **The affine duality** `σ_K(E) = K − E` satisfies (R5) of Def 6.8; the missing object was a class, not an involution (Thms 12.2, 12.2a). §9.1 item 3a closed.
5. **The Hodge-index transfer theorem** (Thm 12.3, `PROVED` conditional): any `h⁰ : D^W → R_{≥0}` with (a) nonnegativity, (b′) positivity ⇒ effective nonzero modulo `𝓝_∞`, (c) the RR inequality `h⁰(E)+h⁰(K−E) ≥ ½I_∞(E,E) − ½I_∞(E,K) + χ` (no sign condition on `χ`) yields `I_∞(F,F) ≤ 0` on primitive `C_c^∞` classes, hence RH via Paper 45 Thm 10.4. Its bound on the ample cone (Thm 11.14) uses only `0 < Re ρ < 1` and absolute convergence — Chebyshev-trivial.
6. **The falsifier theorem** (Thm 12.4 with Lemma 12.4A, Prop 12.4B, Prop 12.6): for `Ξ_a` the same three axioms are inconsistent (rank-4 primitive sector, `Ξ_a > 0` on `R` replacing (E2)'s last clause, Hardy's theorem). The "Euler-product locus" is a **schema about derivations** (Restatement 12.4a): no model-free derivation of (a),(b′),(c) exists; nothing is asserted about functions.
7. **Two natural `h⁰` constructions examined** (§13): the convex-set candidate carries structure (Thm 13.2) but no route; the integral candidate `h⁰_Z` on prime-power translates of `ΠK` satisfies (a) and (b′) (Thm 13.5, round 3) and fails (c) on every finite truncation (Lemmas 13.5a–b, Thm 13.6); on the full lattice `OPEN` (item 23).
8. **Three genera recorded, unreconciled** (Finding 13.8): CC `1 − log 2`, row D reading `3/2`, row B `∞`.

What is not proved: any sign; the existence of `h⁰`; the full-lattice growth bound; simplicity of zeros (never attempted).

## 3. Refutations of record

The blueprint's eight claims refuted or repaired (decay class; perp = `ξ·entire`; independence argument; `𝓝_∞ = ΠK⋆D^W`; "new proof of Thm 12.2"; `A = e_+ + e_-`; "shape lives in the colimit"; `2(2g−2)`), plus the round-1 Chebyshev route for `ω_∞`.

## 4. Next

The problem is now one function. Recommended start for phase 136 (heuristic Remark 14.5a): sections indexed by **pairs** — `Frob_m ⋆ Frob_n^†`, the bigrading `(n^{½}, n^{−½})` — so that `h⁰(nF)` can grow quadratically, with the discriminating datum `Frob_n ⋆ Frob_n^† = Δ^{(n)}` (unimodularity) entering the definition; and settle item (23) (full-lattice growth of `h⁰_Z(mK)`) by pure argument, since a positive answer there would make `h⁰_Z` an (a)+(b′) candidate with an open (c). Pure mathematics first; computation only for identity checks.
