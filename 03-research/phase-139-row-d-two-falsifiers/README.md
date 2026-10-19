# Phase 139 — Row D: the two falsifiers and the method theorem

Row D of the ABCD closure plan (the sign / Hodge-index statement). This phase pins the two factors of
the phase-136 meta-theorem "sign = polar block × Frobenius lattice" with one falsifier each, and
states the construction problem that remains.

| File | What it is | Status |
|---|---|---|
| `R139_000_BLUEPRINT.md` | Blueprint: the three falsifier tests, D.19–D.21, the binding corpus consequences | input |
| `R139_001_ROUND1.md` | **Report**: D.19 complete with **T2**; D.20 items 1–3; D.21 the consolidated ledger and **`(P139)`**; corpus check per idea; FATAL screen; paper-facing list; open list; label. **Round-2 repairs applied in place**, each marked by a bracketed `[…, round 2, finding H·]` note | delivered, repaired |
| `R139_002_AUDIT.md` | Audit of round 1: 16 findings (7 MAJOR), no FATAL, verdict NOT CONFIRMED AS DELIVERED | delivered |
| `R139_003_ROUND2.md` | **Round 2**: the repair ledger — 16/16 findings addressed (11 repaired, 2 withdrawn, 3 sharpened), plus one further defect found while repairing H7 | delivered |
| `R139_005_CLOSING_DECISION.md` | Closing decision | pending |

Reference plans (outside this directory):
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-COMPLETION-PLAN.md` §1 and
`05-meta-and-planning/ABCD-CLOSURE-PLAN/CORPUS_CHECK_ROW_D_PLAN.md` (binding).

## Contents of `R139_001` at a glance

| § | Result | Label |
|---|---|---|
| D.19.2 | the Epstein canonical class `K_Q(t) = ¼e^{t/2}Σ'_v(y_v²−2y_v)e^{−y_v}`, `y_v = (2π/√D)e^tQ(v)`: even, super-exponential decay, `Φ_{K_Q} = Ξ_Q := ½s(s−1)Λ_Q`, polar set `{0,1}` **equimodular**, `deg K_Q = ½` | `PROVED` |
| D.19.2 | `K_Q > 0` (blueprint's expectation) | **`REFUTED`** |
| D.19.3 | the Weil class, `I_∞^{(Q)}`, the splitting `D^W = Λ_Q ⊥ P^W_Q`, the Lorentzian normalization | `PROVED` |
| D.19.3b | `Ξ_Q` lies **outside** Paper 46 Prop. 12.6's class (it fails four of its hypotheses), so Thm 11.14, the ample cone and Thm 12.3 are not available for it; D.19.3(ii) is a new proposition with its own hypotheses | `PROVED`; the round-1 erratum claim against Prop. 12.6 is **withdrawn** (P46-5 → `EDITORIAL`) |
| D.19.4a | `Λ_{x²+ky²}` **has** real zeros in `(0,1)` for `k` large | `PROVED` |
| D.19.4b | all real zeros lie in `(0,1)`, so `θ_R < ½` | `PROVED` |
| D.19.5 | **Hodge index fails for `Ξ_Q`** for principal `Q` with `h(−D) > 1`, with an effective, even, smooth, compactly supported witness (Landau criterion + Davenport–Heilbronn) | `PROVED` |
| D.19.5b | the witness cannot come from the translation cone (equimodularity makes it Lorentzian) | `PROVED` |
| D.19.6 | `c_Q(n) ≥ 0` is **false**; the density axiom fails; `θ_Z > θ_P` | `PROVED` |
| D.19.7 | **T2**: no derivation of Hodge index for `ξ` from A1–A6 + A2⁺ alone (`Ξ_Q` satisfies all of these, A3 included) | **`METHOD-CONSTRAINT`** |
| D.19.7d | a derivation escaping `Ξ_Q` via A9 (`Z > 0` on `R`) is not field-uniform unless it disposes of Landau–Siegel zeros | `PROVED` |
| D.20.1 | the field-uniform frame for every number field; what changes (archimedean sum, discriminant term, regulator) | `RESTATEMENT` + `PROVED` |
| D.20.1(iii) | existence of `K_K` with `Φ_{K_K} = ξ_K` and decay `e^{−A|t|}` for every `A`, by **contour shift** — no theta function, no fundamental domain for the units | `PROVED` |
| D.20.2 | additivity of the primitive zero form under base change, over **conjugate packets** `Λ(\cdot,χ)Λ(\cdot,\barχ)`; all Artin factors are primitive | `PROVED` for `L/K` abelian; `PROVED-CONDITIONAL` on Artin holomorphy in general |
| D.20.3 | Epstein = the same Hecke L-functions read as a **sum**; `ζ_K` reads them as a **product**; `Z ↦ Ŵ^{(Z)}` is multiplicative-to-additive | `PROVED` |
| D.21.2 | the consolidated line-by-line ledger W1–W8 of Weil's second proof, labelled PRESENT / PRESENT-CONDITIONAL / ABSENT | new (entries cited) |
| D.21.3 | **Euler-product step = W4** (the Frobenius correspondence and its composition law); **field-uniform step = W2 + W5** (Riemann–Roch and Hodge index on the square) | `PROVED` |
| D.21.4 | **`(P139)`** — construct a rule `Z ↦ h⁰_Z` *defined* for every `Z` satisfying A1, A2, A2⁺, A4, A5, A6 (A3 excluded, so that `Ξ_a ∈ 𝒵`; fix after R139_004 H17), satisfying (a),(b′),(c) for `Z = ξ_K`, with growth `\tfrac{r²}4m² + O(m)` (`¼m²` for `K = Q`) and the **naming clause (N)**; acceptance tests (AT-1) Epstein, (AT-2) `Ξ_a`, (AT-3) `ζ_K` non-distinction | `OPEN` |

## The axiom table (D.19.7a), in one line each

A1 analytic frame · A2 canonical class · A2⁺ polar positivity · A3 **equimodular polar block** ·
A4 non-negative Dirichlet coefficients · A5 explicit formula · A6 splitting + Lorentzian normalization ·
A7 **zero strip = polar strip** · A8 **Euler product with non-negative atoms** · A9 `Z > 0` on `R`.

`ξ`: all. `Ξ_a`: all but **A3**. `Ξ_Q` (**principal** `Q`, `h > 1`): A1–A6, A2⁺, but **not A7, A8,
A9** — all three provably. `ξ_K`: all but A9, which is open for real quadratic `K`. Hodge index fails
for `Ξ_a` and for `Ξ_Q`.

## Scripts

**None.** The one place the blueprint allowed a numerical certificate — whether `Λ_Q` has a real zero
in `(0,1)` — is settled by proof in both directions (Theorem D.19.4a, Lemma D.19.4b).

## Label

**Row D: no label change.** FATAL screen clean (§6 of `R139_001`), re-run after the round-2 repairs
(`R139_003` §5). Two items were relabelled **downward** in round 2 (P46-5 `MAJOR erratum → EDITORIAL`;
Theorem D.20.2 `PROVED → PROVED` abelian / `PROVED-CONDITIONAL` general) and one restricted in scope
(D.19.3–D.19.6 to principal `Q`). Nothing was relabelled upward.
