# R137.007 — Closing decision, phase 137 (row D, canonical coupling)

rounds 1–3), R137_002/004/006 (audit, confirmation, final). Independent checks: mpmath recomputation
of `ΠK` near `0.235` (root `u_0 = 0.238624`), numerical check of the termwise inequality `f_n'' ≥ f_n/4`
for `x ≥ 5.1` and of the cubic `8x³−56x²+82x−18` at `5.0`/`5.1`; reading of D.0 §§1.3–1.5, D.11
§§2.0–2.4, Proposition 1.1 of round 3.*

## 1. Verdicts of record

| item | verdict | label of the main statement |
|---|---|---|
| D.0 — phase-65 `RH-PROOF.md` | **REFUTED as a proof of RH**; correct as a *reduction* of RH to the `P`-uniformity of a renormalized family | `REFUTED` (proof) / `PROVED` (fork, Prop. 1.1 of R137_005) |
| D.11 — growth of `h⁰_Z(mK)` | lower bound `≫ (log m)^{3/2}/log log m` on the full lattice; feasibility threshold `e^{πq²} ≤ m ≲ e^{5.1q²}` per generator, both directions; conditional upper bound via Montgomery–Vaughan needing a zero-free region (X19); item (23) reduced one-sidedly to the largest index `Q(m)`; requirement (c) forces `Q(m) ≫ m√log m` | `PROVED` (bounds), `OPEN` (23), (23a), (23b), (23c) |
| D.12 — semilocal positivity | blueprint sign corrected (`W_S` was minus the Weil quantity); for `S={∞}` the `S`-dependence is vacuous inside the CC window; first unpaid term at `2T = log 2` is `2(log 2)2^{−1/2}(F⋆F^∨)(log 2)`; Doc-135 purity route NOT APPLICABLE | `PROVED` (scope), `OPEN` D.12-α, β, γ |
| D.13 — dictionary with CC | one exact identity (`Q = Π`); CC's vanishing condition on `f = F⋆F^∨` is `Φ_F(0)Φ_F(1) = 0`, weaker than primitivity, equal to it on even `F`; the rest analogy | `PROVED` (exact rows), `ANALOGY` (others) |
| D.14 — conditional | **not opened**; gate re-worded to `h⁰_Z(mK) = Ω(m^{2−ε})`, preceded by (23c) finiteness | — |
| Part III of Paper 47 | **not appended** (draft R137_001b kept as draft) | — |

## 2. What the phase established that was not known before

1. **The fork (Prop. 1.1, R137_005).** In the phase-65 chain the uniform Montel bound is available for the
   sourced channel matrix `G_P^∘` (R3 point 4 does deliver L1 for it, and shorting preserves a source norm
   because a Schur complement of a PSD form is `⪯` the block), while the identification of the limit is
   available only for the renormalized trace `M_P`, whose Nevanlinna mass is the divergent eigenvalue count.
   No object carries both premises. This is D8.5b-i §5's "each candidate gets one clause, never both" one
   level up. **No-go recorded** in `NO-GO-LIST.md`.
2. **The falsifier gap.** The class with G4's shape (Euler product with positive atoms, one simple pole,
   functional equation) is large — every Dedekind zeta `ζ_K` — but contains no member with proven off-line
   zeros. So `Ξ_a` (four polar points) cannot adjudicate any argument that uses rank-one polar divergence,
   and a sound argument of that shape would prove GRH for all number fields. This is a permanent constraint
   on the corpus's faithfulness test and is recorded as such. (R137_006 N9; R137_007 corrected the earlier
   "no falsifier exists" wording in `RH-PROOF.md`, `NO-GO-LIST.md`, README.)
3. **Sections of the arithmetic curve exist and are counted.** `H⁰_Z(mK) ≠ 0` from `m ≈ 4.5·10⁶`
   (certified), a single generator at `q` is feasible iff `m ≍ e^{cq²}` with `π ≤ c ≤ 5.1`, and the full
   Frobenius lattice gives `(log m)^{3/2}` growth against an `m²` requirement. The obstruction to (c) is
   quantitative: feasible corrections would have to live at prime powers `≳ m√log m`.
4. **The method for an upper bound is forced onto `Re s = 1`** (degree ceiling `Φ_E(σ) ≤ m` holds only on
   `[0,1]`, where `ξ` may vanish), so any quantitative bound imports a zero-free region. Recorded as (X19).
5. **Paper 47 corrections**: §14.5 item (23) "equivalently" is wrong (uniform `ρ_Q` alone does not suffice;
   `Q(m) = o(m√log m)` alone does); Remark 13.6a's heuristic is a theorem in both directions. To be entered
   in Paper 47 with the next Part III pass.

## 3. Decision

Phase 137 is **closed without a label change for row D** (still no sign, no `h⁰`). The arithmetic-counting
page (S1) is exhausted for now: growth is super-logarithmic but the (c)-requirement is quadratic and the
mechanism is structurally far from it. The semilocal page (S2) has a sharp open acceptance test (D.12-α).
The direction for the next phase — one question, the intrinsic distinction of the primitive radial
sector from the indefinite directions, with structure prior to the zeros and without attacking the sign
through the explicit formula — is adopted as phase 138 (`R138_000_BLUEPRINT.md`).

## 4. Record repairs made during this phase (outside row D)

* Paper 43 md: Theorem 8A.12 (clause A.2) written in for the first time; continuity of the crossed-product
  splitting (Thm 7.1(a)) marked CONDITIONAL (not proved in P123.121/123).
* Paper 44 md: off-diagonal Gram constant corrected (index set `S_f∖(P(m)∩P(n))`); `Prim_n` structure
  proved by induction (§12 "Corrections of record").
* LaTeX Papers 43 (58 pp.), 44 (47 pp.), 45 (31 pp.) accepted after two audit rounds each.
