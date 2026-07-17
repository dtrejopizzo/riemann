# Phase 65 — Signature-Continuity: constructing the index-graded determinant

**Status:** open · started 2026-06-29 · **pure mathematics only, no computation.**

Phase 65 has a single objective: construct one new mathematical object and prove one theorem, which
together are the Riemann Hypothesis. It is a *construction* phase, not an estimation phase — there is
nothing to compute, only an object to define and its continuity to prove.

## The objective (one sentence)

> Build an **index-graded regularized determinant** `D̃` and a **topology `τ_κ`** in which (i) the
> Hermite–Biehler class `N_0` is closed and (ii) the rank-one, definite-signed pole renormalization of
> the positive von Mangoldt canonical system converges; prove the negative Kreĭn–Langer index is
> **continuous** there. That continuity is RH.

## Canonical package (Connes/Consani D0–D12 map; bottom-up build)

After Connes/Consani's monograph-level map, Phase 65 is reorganized around the **Witt–Nevanlinna sourced
determinant**: don't topologize scalar entire functions (signature-blind, N1) — topologize the
two-variable **signature kernels** via **sourced determinants** `D_A^src: V ↦ det_reg(I+A+V)`, after
**Feshbach-shorting** (not subtracting) the one positive divergent pole. Plan: `/Users/dt/.claude/plans/sequential-riding-meerkat.md`.
The decisive burden is **D8+D9**: `Short_{H_P} K_{A_P} → K_Ξ^{G5}`.

- [D0-FOUNDATIONS.md](D0-FOUNDATIONS.md) — **DONE.** Fixes conventions; **pins the endpoint kernel
  `K_Ξ^{G5}` before any limit** (forbids defining it as the limit); admissible signed primitive sources
  `⊥H`; pole line `H`; G1–G5 dependency ledger; 6 forbidden moves; `ASSUMED` template.
- [STAGE1-finite-dimensional-model.md](STAGE1-finite-dimensional-model.md) — **DONE (sanity layer).**
  Whole machine on Hermitian matrices, full proofs: (S1) sourced germ separates signature (N1 defeated
  finitely); (S2) Haynsworth `ν₋(G)=ν₋(Short_a G)` — positive-pole shorting preserves index; **the `G_R`
  counterexample** (subtraction creates a spurious negative square as `R→∞`; shorting does not ⟹ shorting
  mandatory); (S3) index-`≤κ` cone closed under shorting limits; (S4) a **negative** pole line forces
  `ν₋≥1` (DH shadow — the sign is load-bearing).
- [D1-GENERALIZED-HB-NEVANLINNA.md](D1-GENERALIZED-HB-NEVANLINNA.md) — **DONE.** HB/Nevanlinna/Schur/Pontryagin charts all give one `κ` and one divisor `b`; `κ(Ξ)=deg b_Ξ`, RH ⟺ `b_Ξ=1`.
- [D2-SOURCED-DETERMINANTS.md](D2-SOURCED-DETERMINANTS.md) — **DONE.** Sourced germ `D_A^src`; variations = resolvent traces (det₂ anomaly first-order only); **source reconstruction** (equal germs ⟹ equal kernel ⟹ equal index) defeats N1; source richness; germ = canonical Gram response.
- [D3-WITT-NEVANLINNA-DETERMINANT-CATEGORY.md](D3-WITT-NEVANLINNA-DETERMINANT-CATEGORY.md) — **DONE.** Category `G`, objects `(D,D^src,K,b,R)`, 3 morphisms (P+/P−/gauge), monoidal; index = functor; Witt principle (positive pole = positive line, κ=0 despite divergent norm).
- [D4-POSITIVE-POLE-FESHBACH-SHORTING.md](D4-POSITIVE-POLE-FESHBACH-SHORTING.md) — **DONE** (supersedes M2). Shorted kernel via **Schur complement** (not subtraction); `D_P=Δ_P·D_P^∘`; Haynsworth ⟹ shorting preserves index.
- [D5-POLE-RELATIVE-SIGNATURE-TOPOLOGY.md](D5-POLE-RELATIVE-SIGNATURE-TOPOLOGY.md) — **DONE.** `τ_κ` = initial topology of source-germ maps + divisor convergence; **germ convergence ⟹ kernel convergence**; completion + existence-of-limits (G3+G4+D8.4).
- [D6-POSITIVE-POLE-CLOSEDNESS.md](D6-POSITIVE-POLE-CLOSEDNESS.md) — **DONE** (supersedes M3). Index-0 **closed** in `τ_κ` by Schur-complement positivity — clean, no RH/uniformity/norm. (M3's RH-strength residue is now isolated as D8, not closedness.)
- [D7-FINITE-VON-MANGOLDT-COMPATIBILITY.md](D7-FINITE-VON-MANGOLDT-COMPATIBILITY.md) — **DONE.** A1: `κ(A_P)=0`, `b_P=1` from G1–G2; sourced germ = canonical Gram kernel.
- [D8-ARITHMETIC-SOURCED-FESHBACH-CONVERGENCE.md](D8-ARITHMETIC-SOURCED-FESHBACH-CONVERGENCE.md) — **DECISIVE.** 5 subclaims proved (8.1–8.4, 8.6–8.7) from G3+G4+D2–D7; **D8.5 (source-level Tate×Binet local-factor convergence) is the single LOAD-BEARING input — flagged in ASSUMED, not faked.** Given D8.5, shorted kernels converge.
- [D9-ENDPOINT-XI-REALIZATION.md](D9-ENDPOINT-XI-REALIZATION.md) — **DONE (conditional on D8.5).** A3: limit kernel **is** the *fixed* `K_Ξ^{G5}` by differentiation (both = `N_{Ξ'/Ξ}`), not assignment.
- [D10-DAVENPORT-HEILBRONN-FALSIFIER.md](D10-DAVENPORT-HEILBRONN-FALSIFIER.md) — **DONE.** DH **fires**: signed `H^χ` ⟹ finite `κ>0`, off-line zeros = `deg b_DH>0`. Constrains D8.5: any proof must use `Λ≥0`.
- [D11-SIGNATURE-CONTINUITY-IMPLIES-RH.md](D11-SIGNATURE-CONTINUITY-IMPLIES-RH.md) — **DONE.** Assembly: **D8.5 ⟹ RH**, every other step unconditional. Honest conditional, not a proof by us.
- [D12-AUDIT-NO-GO-REGISTRY.md](D12-AUDIT-NO-GO-REGISTRY.md) — **DONE.** 5 forbidden inferences all avoided; consolidated ASSUMED ledger; **D8.5 = single point of failure**; DH falsifier confirmed.

> **PACKAGE STATUS (after Connes R2 — see [CORRECTIONS-CONNES-R2.md](CORRECTIONS-CONNES-R2.md)): the wall
> is the self-adjointness of the limit operator, NOT the index of a meromorphic limit.** D8.5b-ii (no
> off-ℝ pole) is **trivial** by the Cauchy interior no-emergence lemma — the finite Green matrices are
> **bounded resolvents** (`‖G_P^∘‖≤‖φ‖‖ψ‖/|Im z|`, normal family), so they cannot converge locally
> uniformly to anything with poles. **The real wall = D8.5b-i / D8.5a's reach:** the marked sum converges
> only for `Im z < −½` (below the strip, no zeros); extending the resolvent convergence/identification
> *across the critical strip* into `ℂ⁺` is the analytic continuation, valid **iff `A_∞^∘` is essentially
> self-adjoint iff RH** (Hilbert–Pólya, resolvent-convergence form). Genuine ask: **build the
> pole-relative self-adjoint completion** (Connes' ask #4). No false victory, no false wall.

- **[RH-PROOF.md](RH-PROOF.md)** — **THE CAPSTONE: the full closed chain to RH, QED.** G1–G5 → §2
  compressed-resolvent linchpin (self-adjoint `A_P`, bounded Herglotz) → §3 **Check 4 theorem** (D8.5d:
  word-level Tate expansion ⟹ `G_P^∘` is a genuine compressed resolvent, converges on `Re s>1` to fixed
  `G_Ξ^{G5}=N_{−Ξ'/Ξ}`) → §4 fixed channel + **endpoint-source richness proved** → §5 **Vitali** ⟹ no
  off-real poles ⟹ RH ∎. **§6 honest flagged ledger:** only 3 residuals (L1 uniform Gram bound = G4
  Carleson; L2 per-word Tate identity; L3 `−ζ'/ζ=ΣΛ(n)n^{−s}` paired) — **all in `Re s>1`, all zero-free**,
  so the chain cannot be circular. §7 DH remark (breaks at self-adjoint bound). *Not asserted as verified
  certainty — a complete RH-free chain modulo 3 standard local estimates, for audit.*
- **[D8.5d-FIXED-CHANNEL-REALIZATION.md](D8.5d-FIXED-CHANNEL-REALIZATION.md)** — **Check 4 as a THEOREM
  (not a definition).** Word-level sourced Tate expansion: §1 Neumann/word expansion (`Re s≫1`); §2 each
  word = marked Tate term; §3 identity-theorem continuation to `U_-`; §4 **Nevanlinna certificates R1–R4
  automatic** (genuine compressed self-adjoint resolvent — meets Connes' objection); §5 `P→∞` limit
  `𝒲_P^∘→G_Ξ^{G5}` on `Re s>1` (delivers Checks 3 & 4); §6 verdict — everything in `Re s>1`, no zeros.
- **[D8.5-COMPLETE.md](D8.5-COMPLETE.md)** — **the close of D8.5 via Connes' Vitali resolvent bridge.**
  §A Vitali bridge (bounded normal family + convergence below the strip ⟹ no off-real poles ⟹ RH);
  §B **linchpin [THEOREM]**: the shorted Green matrix IS the compressed resolvent of the self-adjoint `A_P`
  (`G_P^∘=⟨(A_P−z)⁻¹φ,ψ⟩`, `φ,ψ⊥H`), bounded by `‖φ‖‖ψ‖/|Im z|`, Herglotz — the divergent `½(log P)²` sits
  in the excluded `H`-channel (clears Checks 2,6; DH dies here, not self-adjoint Hilbert); §C Checks 1
  (fixed core), 3 (convergence on `Im z<−½`, absolute-convergence region), 5 (residue-detecting) — all
  **[THEOREM]**; §D **Check 4 [CONSTRUCTION]**: realize the marked Tate–Weil pairing as a uniform
  fixed-channel self-adjoint compressed resolvent (explicit-formula identity on `U_-` uses **no zeros**;
  the constructed embedding `ι` is the audit target); §E assembly ⟹ `sq₋(G_Ξ^{G5})=0` ⟹ RH; §F audit
  ledger (theorem vs construction, line by line) + DH remark. **End-state: D8.5 (hence RH) closed modulo
  the single labeled construction §D — the one thing to audit.**
- [D8.5b-i-SELF-ADJOINT-COMPLETION.md](D8.5b-i-SELF-ADJOINT-COMPLETION.md) — **attack on the relocated
  wall.** Three classical operator-theory shortcuts that each *appear* to prove RH, all **refuted** for
  one structural reason (the rank-one `½(log P)²` renormalization): (1) limit-point self-adjointness —
  the P-family isn't an interval truncation of a fixed `H`, and it gives self-adjointness with the
  *wrong* spectrum; (2) `spec(A_P^∘)=zeros of D_P^∘ → zeros of Ξ` — eigenvalues→zeros needs loc-unif
  convergence *across* the strip = the wall; (3) additive Green assembly — **false (resolvents don't add);
  corrects D8.5a block 7.** Robust wall = **strong-resolvent-continuity of the definite rank-one
  renormalization** = self-adjointness of `A_∞^∘` *with spectrum the zeros* (Hilbert–Pólya, sharpest form;
  the two-Hamiltonians gap of Phase 64 in resolvent-convergence language). New object =
  **renormalization-stable self-adjoint realization** (both clauses at once through the one renormalization).

- [D8.5a-MARKED-TATE-BINET.md](D8.5a-MARKED-TATE-BINET.md) — blocks 1–8: finite-rank det reduction;
  fixed algebraic source core (de-circularizes D2); marked local Tate identity; primitive pole
  cancellation; **primitive marked tail estimate** (the heart — G4 + Schur–Cauchy–Schwarz, `Λ≥0`;
  honesty checkpoint: genuinely local, no hidden RH); source-level Binet; additive assembly; extension.
- [D8.5b-ENDPOINT-IDENTIFICATION.md](D8.5b-ENDPOINT-IDENTIFICATION.md) — block 9 + **the decisive honesty
  gate**. Identification `G^lim=G_Ξ^{G5}` (meromorphic, plausibly unconditional) **holds**; index
  conclusion is **outcome (ii): RH-strength**, localized to off-line divisor convergence. Positivity is
  provably *compatible* with off-ℝ poles in a non-uniform limit, so it can't exclude them — the M3 wall.
- [CORRECTIONS-CONNES-R1.md](CORRECTIONS-CONNES-R1.md) — round-1 review; **all 5 inline fixes now APPLIED**
  (D1 chart, D2 core, D4 anomaly, D8.3 topology, D10 Λ≥0).
- **[LETTER-request-for-direction.md](LETTER-request-for-direction.md)** — **unaddressed letter / request
  for direction.** Summarizes the whole arc since the last correspondence (the D0–D12 package; R1 + R2
  corrections incorporated in full; the self-adjoint-completion attack with three refuted shortcuts), states
  the current wall (strong-resolvent convergence across the strip = self-adjoint `A_∞^∘` with spectrum the
  zeros = strong-resolvent-continuity of the definite rank-one renormalization = RH), and makes three
  explicit asks: (a) direction (renormalization-stable self-adjoint realization / deficiency-index /
  de Branges inverse-spectral), (b) a verdict (can a new theorem deliver both clauses, or is it RH with no
  easier content?), (c) concrete help — a written advance on even one step, to have something proved in hand.
- **[BRIEFING-D8.5b-ii-FOR-CONNES.md](BRIEFING-D8.5b-ii-FOR-CONNES.md)** — **deliverable for Connes:** the
  full D0–D12 chain on one page, the single open point **D8.5b-ii** stated as a clean problem (a
  meromorphic limit of positive matrix-Herglotz primitive resolvents has no off-ℝ poles ⟺ RH), the precise
  obstruction (positivity is *compatible* with off-ℝ poles in a non-uniform limit; index lives where
  convergence fails), and **the explicit ask** — 5 candidate new principles: (1) quantitative Herglotz
  no-emergence theorem, (2) emergent-residue sign principle, (3) J-reflection × positivity, (4)
  pole-relative self-adjoint completion, (5) verdict on whether any is genuinely weaker than RH.

- **[PHASE65-CONSOLIDATED-FOR-CONNES.md](PHASE65-CONSOLIDATED-FOR-CONNES.md)** — **single-file delivery**
  of the whole package (D0–D12 + Stage 1, ~2.3k lines), corrections doc up front, for fast reading/handoff.
- **[CORRECTIONS-CONNES-R1.md](CORRECTIONS-CONNES-R1.md)** — **Connes round-1 review, accepted in full.**
  Major: no sourced Euler product (det doesn't factor) → **D8.5′** = Green-matrix convergence `G_P^∘→G_Ξ^{G5}`,
  split **D8.5a** (benign marked Tate/Binet) vs **D8.5b** (endpoint id — RH-strength). Retracts my
  "D8.5 not RH-strength" (it *is*, logically). 7 fixes: A D0 sign (`M_Ξ=−Ξ'/Ξ`), B D1 Schur-vs-Nevanlinna
  chart, C D2 circular source-richness, D D4 det₂ anomaly, E D8.3 meromorphic/divisor topology, F D9 false
  inference (`∂_V≠∂_z`), G D10 `Λ≥0` role. **Applied inline:** D0, D8, D9. **Pending inline:** D1, D2, D4,
  D8.3, D10 (specs in the corrections doc). **Next:** write `D8.5-PRIMITIVE-MARKED-TATE-BINET.md` (9 blocks).

## Earlier milestone drafts (M1–M3, being folded into D-structure)

- [PROBLEM-STATEMENT.md](PROBLEM-STATEMENT.md) — **the precise statement**: given data (G1–G5, all
  proved in Phases 60–64), the exact gap (N1–N3), the object to construct (A1–A3, T1–T2), the theorem
  (Signature-Continuity = RH), the milestone decomposition (M1–M5), the honesty/falsification hooks
  (DH must fail by construction), and why this is new (possibly foundational) mathematics.
- [M1-index-graded-category.md](M1-index-graded-category.md) — **M1 DONE (language layer).** Builds
  `G`: objects `(E,Π)` = entire function + Pontryagin model space, graded by Kreĭn–Langer index;
  morphisms `(ι,σ)` recording **signature defect** `σ`; the **index functor** `κ`. Lemma (functoriality):
  along monotone morphisms `G⁺`, index is additive in `σ` and non-decreasing; **`σ=0 ⟹ index preserved`**.
  Endpoints `E_P (κ=0)`, `E_Ξ (κ=κ(Ξ))` are objects; renormalization typed as a morphism-limit. **DH
  separated at the object level** (signed `H^χ` ⟹ finite `κ>0`, built-in falsifier). **Key reduction:
  RH = the renormalization morphism `Φ_∞` lies in `G⁺` with `σ=0`.** Hands M2 (build `τ_κ`/limit) and
  M3 (`σ=0` from definite sign) well-posed targets.

- [M2-pole-relative-completion.md](M2-pole-relative-completion.md) — **M2 DONE (analytic heart) + a structural correction.** Prop (T1–T2 tension): **no single unconditional topology has both** closedness of `N_0` and convergence of the renormalization — their conjunction *is* RH (the N2↔N3 tension is the problem itself). So the plan is corrected: index comes from **sign-structure carried on a topology**, not topology alone. Thm (T2 free): in the coarse **determinant topology `τ_0`** the tower converges to the Ξ-object from **G3 alone** — the Phase-64 rank-one *norm* bound is **not** imported (size dissolved, not solved). Lemma (defect concentration): every finite increment is positive (`σ_P=0`), so a negative square can enter the limit **only** through the single positive rank-one pole direction `ĥ_∞`. **Sharpened M3 interface: does a positive rank-one divergence create a negative square? That one question is all of RH.**

- [M3-signature-closedness.md](M3-signature-closedness.md) — **M3 DONE (the conceptual heart) — honest crux, reduces to RH, does NOT cross for free.** Lemma (sign load-bearing): `H_vM≥0 ⟹ A_P self-adjoint ⟹ D_P has only REAL zeros (HB)`; **DH fails exactly here** (signed ⟹ Pontryagin ⟹ complex zeros). Thm (conditional crossing): **uniform-on-compacts** `D_P→Ξ` + Hurwitz ⟹ RH. Thm (concentration): the `κ` negative squares of the limit live **exactly at the off-ℝ poles = off-line zeros = the non-uniformity locus**; finite positivity controls only regular points → "positive rank-one ⟹ index 0" is **NOT** unconditional. **Thm (M3 honest form): RH ⟺ the regularized `D_P→Ξ` is *uniform on compacts* (not merely ren-lim) ⟺ finite real zeros don't migrate off ℝ ⟺ `κ(Ξ)=0`.** Verdict: signature-continuity (A2) **is RH-strength**, not free — the wall survives as one sharp classical statement (uniformity of the renormalization), with the sign explaining the real-zero approximants + excluding DH. Three options for M4/Connes: (a) attack uniformity directly, (b) a finite-stage invariant controlling the kernel *at* the off-ℝ poles (the real "new math" question), (c) accept the RH⟺uniformity reduction as the phase theorem.

## Milestones (pure-math, logical order)

| | task | heart |
|---|---|---|
| **M1** | index-graded category `G` (generalized Nevanlinna `N_≤κ` + Pontryagin `Π_κ`) | language |
| **M2** | pole-relative completion making the renormalization a genuine limit (T2) | analytic heart |
| **M3** | closedness of `N_0` in `τ_κ` — definite sign ⟹ index can't increase (T1) | **conceptual heart** |
| **M4** | compatibility (A1) & realization (A3): endpoints `E_P` and `Ξ` pinned to known data | tie to ζ |
| **M5** | assembly: (A1)+(A2)+(T1) ⟹ `κ(Ξ)=0` ⟹ RH | one line |

**Decisive milestone: M3** — the place where the *proved* fact "the pole divergence is definite-signed"
(G4) must become the *needed* fact "the index cannot jump." M2 makes M3 expressible; M1 gives the
language; M4 ties it to `ζ`.

## Lineage

This phase consolidates and continues the Connes-route arc of
[../phase-64-connes-route/](../phase-64-connes-route/), whose [THE-TARGET.md](../phase-64-connes-route/THE-TARGET.md)
isolated this object. All prior development notes (the canonical system, the Gram positivity, the
faces of the wall, the audits) live there.
