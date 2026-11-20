# Phase 212 — Building the object that carries the sign

Working memos in this folder are written in Spanish.

## Aim

Target (★): λ_A(T) ≥ 0 for every T > 0, with the definitions of
`../phase-211-sign-sandbox/STATEMENT_001.md` (window form a_T on the primitive subspace P_T).
The problem is treated purely as the sign of an explicit quadratic form; no equivalence with any other
statement is used, named or reasoned from. Pure mathematics; computations only to validate concrete
points. No paper is modified until the sign is proved.

Phase 211 is kept as a record. This phase does not continue its towers: it starts from what was PROVED
there and in Papers 47–48 about the shape the object must have, and builds only candidates that pass the
filter of `RULES_AVOID.md`. The object sought is specified in `OBJECT_SPEC.md`: in one line, a family of
exact Gram realisations a_T(F) = ‖V_T F‖²_{ℋ_T} + (manifestly ≥ 0 remainder) on P_T, with V_T built
non-linearly from the exact values Λ(n), n < e^{2T}, whose identity breaks (not merely "loses margin")
under every falsifier.

## What is established and fixes the design

1. **Zero slack.** λ_A(T) ≤ 4·10⁹ T e^{−15.449T} for T ≥ 1 (P47 cor:margin1); the window of positive
   weights closes on c = 1 from both sides (211 LEDGER C43). The sign step cannot be an estimate with
   remainder (P47 thm:shape (B′)); it must be an exact identity "form = manifestly non-negative expression".
2. **Not generic.** An identity valid for every weight vector carries no sign (P47 lem:shape-ident). The
   sign-step identity must fail for cΛ (c ≠ 1), a_P, finite deletion and amplification, and the models of
   the battery (`RULES_AVOID.md` §E).
3. **Conjunction without a common falsifier.** Euler product over ℕ (E), functional equation with
   Γ(s/2) at conductor 1 (F) and integrality (I) used together have no common falsifier
   (P47 rem:conjunctions). What was never built is a **non-linear** sign step in which all three enter
   together. The elementary exact separator is Σ_{d|n} a(d) = log n (P48, scope note after req:spec): it
   identifies Λ, but turning identification into a quadratic bound is OPEN.
4. **The sign lives in the cross terms.** Every line of phase 211 stopped at a joint remainder without
   sign. The existing positive pieces are correct and do not suffice separately.
5. **Grid row 6 used only linearly.** The exact values of Λ (Λ ∗ 1 = log as an identity) never entered a
   sign step non-linearly (P48 §Coordinates).

Available PROVED pieces (not re-derived here): exact reductions (L2) P47 thm:coer-schur, (S) P47 prop:AM,
one profile P47 thm:oneprofile, Nyquist mesh P47 thm:nyq, power ladder 211 POWER_BRIDGE_002 §6, thermal
polynomial kernel 211 GRAM_SLICES §§19.8, 19.10, integer blocks ⟺ real nodes 211 GRAM_SLICES §18; partial
positivities (prop:nearfree; resonant sum of squares with uniform margin, 211 GRAM_SLICES §17; reciprocal
endpoint C_0 of all orders; all-order Gram of the hyperbolic model, 211 HYPERBOLIC §§4–5; certified plane
{E₁,E₂}, 211 GRAM_SLICES §19.9; certified range T ≤ ½log5); identities with the three inputs (finite
Poisson–Chebyshev identity P47 thm:PCfinite and contraction prop:GEgap; theta operator realisation 211
HYPERBOLIC §12.6, without metric).

## Status

- **(★) is OPEN. No construction meeting `OBJECT_SPEC.md` has been obtained.**
- `LEDGER.md` records rounds 1–18 candidate by candidate: closed with NO-GO with class (L-comp, K3),
  accepted without a new mechanism (K1, K2, K4, K1′, K2′, K5), or no candidate passing the selection gate
  (rounds 3–5 and 7–18); round 6 (per-prime window split) is NUMERICAL, reaching the ceiling up to
  T ≈ 0.69 and failing from 0.70.
- Later rounds (`ROUND_019_*` … `ROUND_095_*`) and constructions `BUILD_079`–`BUILD_084` carry their own
  status lines: the builds have sign OPEN (079–083: formulas reviewed, global sign not established);
  `ROUND_095_A/B` are PROVED results about an auxiliary form (negative sign of the cyclotomic finite part;
  no self-energy constant repairs it) and do not decide the sign of the full form.
- Every attempt is registered in `05-meta-and-planning/ROUTES-MASTER-INDEX.md` (Part III.0 and Part V).

Labels used: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL (NUMÉRICO).

## Method

- **Selection gate before building.** Each candidate states the four points of the novelty filter
  (closest antecedent with file/section; the genuinely new object or claim; why the change avoids the
  concrete difficulty of the antecedent; which identity or inequality connects it with global positivity of
  the full form). An independent review checks the difference against the index, the grid, the crossword,
  Paper 48 and `RULES_AVOID.md` before any derivation.
- If no candidate passes, this is recorded and the search continues; novelty is not manufactured.

## Contents

**Core documents**
- `OBJECT_SPEC.md` — Phase 212 — Specification of the object to be built
- `RULES_AVOID.md` — Phase 212 — What is not done
  ground.
- `BRIEF_CONSTRUCTOR.md` — Brief for every memo of phase 212
- `LEDGER.md` — Candidate ledger (one line each; updated every round)
- `NEAR_DOSSIER.md` — Dossier on the near-coincidence term (Near_M)
- `TRIAGE_D_1.md` … `TRIAGE_D_5.md` — triage of row-D ideas recorded but never carried through.

**Series**
- `ROUND_nnn_X.md` — designs and constructions, rounds 001–095 (full list below).
- `REVIEW_*.md` — independent reviews of the rounds.
- `BUILD_079_*` … `BUILD_084_*` — explicit constructions with their data folders.
- `ANNEX_*.md` — complete readings of the index, of phases 114, 161, 170, 193 and 211, comparisons and
  literature.

**Data and scripts**
- `build_079_data/` — scripts (Arb certification, residual and source evaluations) and data for BUILD_079.
- `build_084_data/` — certification scripts and JSON certificates for BUILD_084.
- `free_weight_scripts/` — scripts and outputs for rounds 017–033 (free-weight / window-split numerics);
  subfolders `hp_out/`, `out_032A/`, `out_033/` hold outputs.
- `verify_window_split.py`, `verify_window_split_canonical.py` — numerical checks of the per-prime window
  split (rounds 6 and 17).

## Suggested reading order

1. This README, `OBJECT_SPEC.md`, `RULES_AVOID.md`, `BRIEF_CONSTRUCTOR.md`.
2. `LEDGER.md` for rounds 1–18.
3. `NEAR_DOSSIER.md` and the `TRIAGE_D_*` files.
4. The `BUILD_*` memos and the latest rounds (`ROUND_09*`).
5. `ANNEX_*` files as reference when a round cites them.

## Running the scripts

Python 3 with `numpy`, `scipy`, `mpmath` and `python-flint` (Arb). Scripts import sibling modules, so run
them from their own folder, e.g. `cd build_084_data && python3 certify_three_cells.py`. They are
validation tools for specific memos; a numerical output is not a proof.

## Full index of rounds, reviews, annexes and triage files

- `ROUND_001_A.md` — Round 1, memo A — Candidate K1: Gram realization from the exact separator with Poisson and the archimedean factor
- `ROUND_001_B.md` — Round 1 B — Candidate K2: Schur pivots along a multiplicative nesting of the integers (selection memo)
- `ROUND_001_C.md` — Round 1 — Candidate K3: enlarged system of squares for the non-resonant crossings
- `ROUND_001_D.md` — Round 1, candidate K4 — non-linear multiscale inequality with Λ beyond the window
- `ROUND_001_L.md` — ROUND_001_L — Rigidity of Carathéodory-type comparators on the power ladder
- `ROUND_002_A.md` — Round 2, candidate A — The exterior tail of the hyperbola as a sum of squares: selection memo
- `ROUND_002_B.md` — Round 2 B — The incidence factorization [log gcd] = E diag(Λ) Eᵀ acting on F (selection memo)
- `ROUND_002_C.md` — Round 002 C — The two-prime-base channel: selection memo
- `ROUND_003_1.md` — Round 3, option 1 — Families of functionals that see the window and are not the theta modal one (selection memo)
- `ROUND_003_2.md` — Round 3, option 2 — Functionals and factors that depend on Λ (selection memo)
- `ROUND_003_3.md` — Round 3, option 3 — the parity sector: products mn via the reflection J
- `ROUND_003_4.md` — ROUND_003_4 — Selection: boundary coordinate and null anchor with boundary inside (G)
- `ROUND_003_5.md` — Round 3, option 5 — the virial pair: selection
- `ROUND_003_6.md` — Round 3, option 6 — Joint conversion of the finite Poisson–Chebyshev identity without recombining (selection memo)
- `ROUND_003_7.md` — Round 3, option 7 — The formulation (S): divisor incidence on 𝔸_M (selection memo)
- `ROUND_003_8.md` — Round 3, option 8 — the object quadratic in the weight and the Riccati-type factorization
- `ROUND_003_9.md` — ROUND_003_9 — Selection: non-local metric of the theta realization
- `ROUND_004_A.md` — Round 4, candidate A — The SP-161 / L161.1 target with signed weights and sieve weights (selection memo)
- `ROUND_004_B.md` — Round 4, zone 1 — Quadratic divisor defect entering additively (selection memo)
- `ROUND_004_C.md` — Round 4, zone 3: the remainder R(F) of the truncated Möbius test (selection memo)
- `ROUND_004_D.md` — Round 4, zone D — Factorization of 𝔸_M with support on the near-coincidences m ≈ kn (selection memo)
- `ROUND_004_E.md` — ROUND_004_E — Selection: indefinite forms (Kreĭn/Pontryagin) with a non-radical neutral vector
- `ROUND_005_G1.md` — Round 5, seed G1: object of degree ≥ 3 whose Hessian is the form
- `ROUND_005_G2.md` — Round 5, seed G2 — closure under products of Euler factors applied to the signature
- `ROUND_005_G3.md` — Round 5, seed G3 — a measure built from the form whose closure gives the sign
- `ROUND_005_G4.md` — Round 5, seed G4: induction that lengthens the window with the divisor identity in the step
- `ROUND_005_G5.md` — Round 5, memo G5: free invention from A1–A6 (backward deduction of object types)
- `ROUND_006_WINDOW_SPLIT_NUMERIC.md` — Round 6 — Window-dependent local distribution at T = 0.5925 (NUMERICAL)
- `ROUND_007_A.md` — Round 7, memo A: the square of the deficit, the ground-state representation of the contacts, and the optimality conditions of the split
- `ROUND_007_B.md` — Round 7, B — stage predicate for induction over primes
- `ROUND_007_C.md` — Round 7, item C — nonlinear relation in the weight between convolution and window
- `ROUND_008_A.md` — Round 8, item A — the boundary concomitant that would convert the product channel into the ratio channel
- `ROUND_009_G1.md` — Round 9, item G1 — object with inverted roles: arithmetic as the source of the sign
- `ROUND_009_G2.md` — Round 9, G2: recursion with a history-dependent stage datum
- `ROUND_009_G3.md` — Round 9, item G3 — where the map has no marks
- `ROUND_010_A.md` — Round 10, A: additive covariance as the mechanism of the sign
- `ROUND_011_A.md` — Round 11, A: the open residues of (PC) and the one-sided lattice discrepancy
- `ROUND_012_A.md` — Round 12, A: the residue L161.4 and its passage to all of P_T
- `ROUND_013_A.md` — Round 13 A — Small-scale reverse engineering: the window ½log 4 < T < ½log 5
- `ROUND_013_B.md` — Round 13, memo B: the weight as the equality case of a positivity (Gram, Schur, completed square)
- `ROUND_013_C.md` — Round 13, C — map of combination operations between signed objects and objects that see the weight
- `ROUND_014_A.md` — Round 14, A — linearizing the ratio channel: independence of the primes, polarization and transport from the product channel
- `ROUND_014_B.md` — Round 14, memo B: Schur–Schoenberg positivity on the Euler product as an independent source of a non-Gram block
- `ROUND_014_C.md` — Round 14, memo C: transition between windows that is not the inclusion
- `ROUND_015_A.md` — Round 15, memo A — Non-affine delay transport: cross-check and closure by repetition
- `ROUND_015_B.md` — Round 15, memo B: coupling distinct primes in the block split, and GCD matrices as coupling
- `ROUND_015_C.md` — Round 15, memo C — Convex functional with Hessian a_T (O14) and nonlinear odd pairing in A_M (O-odd)
- `ROUND_015_D.md` — Round 15 — D. Threshold of the DIR split, transfer vector and count of missing squares
- `ROUND_016_A.md` — Round 16, memo A — Curvature (Γ₂, Bakry–Émery, Lichnerowicz) as source of the sign
- `ROUND_016_B.md` — Round 16, memo B — KMS states on algebras where the sum and the product of ℕ act together
- `ROUND_016_C.md` — Round 16, memo C: reflection positivity, correlation inequalities and Gaussian domination as source of the sign
- `ROUND_017_A.md` — Round 17, memo A: the log 2 wall, the DIR split wall and the split of the atoms
- `ROUND_018_A.md` — Round 18, memo A: ground-state representation with sign-changing `φ` for the local split at `T ∈ (0.60, 0.69)`
- `ROUND_019_A.md` — Round 19, memo A — Scale control: is the margin `e^{−2πe^{2T}}` the lattice tail beyond `N = e^{2T}`?
- `ROUND_020_A.md` — Round 20, note A — negative index of the archimedean form on P_T for all T
- `ROUND_020_B.md` — Round 20, memo B — The radical identity of `M` as a single linear relation between the symbol and the weights
- `ROUND_021_A.md` — Round 21, memo A — The near-radical family `{Π_T(M∗φ)}`: count and structural statement
- `ROUND_022_A.md` — Round 22, memo A — «Undoing the sum»: a single object?, and the Möbius congruence on 𝔸_M
- `ROUND_022_B.md` — Round 22, memo B — the «soft» reformulation with a strong norm
- `ROUND_022_C.md` — Round 22, memo C — «First contact» standpoint: inventory of the null vector and cross-check of two ideas
- `ROUND_023_A.md` — Round 23, memo A: reflection positivity through log m = log(kn)
- `ROUND_023_B.md` — ROUND_023_B — Gate: (PC) compressed before pairing and orientation of the terminal jump
- `ROUND_023_C.md` — Round 23, memo C — Interior block I^λ with sieve weights and lemma 𝒩_k(ν): selection gate
- `ROUND_023_D.md` — Round 23, memo D — an exact identity for the per-atom cancellation for general vectors?
- `ROUND_024_A.md` — Round 24, memo A — Leading term of the truncation defect: ROUND_019_A §§2–4 versus ROUND_021_A §3
- `ROUND_024_B.md` — Round 24, memo B — Near-null block of 211 = near-radical family `{Π_T(M∗φ)}`?
- `ROUND_024_C.md` — ROUND 024 C — The three cheap checks left by the row D triage
- `ROUND_024_D.md` — ROUND_024_D — Gate: object of degree ≥ 2 with the Möbius of the system μ_a and the boundary leak
- `ROUND_025_A.md` — ROUND_025_A — Cross-check of antecedents: "existence + rigidity" scheme (WF)/(R)/(E) against Paper 47 and phases 153–160, 197
- `ROUND_025_B.md` — Round 25, memo B — Logical attack on the "existence + rigidity" scheme (R)/(E)/(WF)
- `ROUND_026_A.md` — ROUND_026_A — Computation of the concave value V*_T against λ_A(T)
- `ROUND_026_B.md` — Round 026 B — (PBP_T) as an exact extremal problem; Kreĭn and density argument; four-point gate
- `ROUND_027_A.md` — Round 027-A — Adversarial numerical verification of the damped weight `v_n cos(ω log n)`
- `ROUND_027_B.md` — ROUND_027_B — Adversarial cross-check of antecedents: damped weight v_n·cos(ω log n) and closure via closed K_T
- `ROUND_027_C.md` — Round 27, memo C — Structure of the damped form `a^{(ω)}_T`
- `ROUND_028_A.md` — Round 28, memo A — Extremal state of the nonnegative free-weight problem
- `ROUND_029_A.md` — Round 029-A — Damped weight `w_n = v_n cos(kπ log n/(4T))` with an hp finite-element basis
- `ROUND_030_A.md` — Round 030-A — Rigidity of the weight without temperedness: the gap on Z, formulated and attacked
- `ROUND_030_B.md` — Round 030 B — Divisor chains, low-frequency spectral mass and primitivity in (PBP_T)
- `ROUND_031_A.md` — Round 031 A — Cross-check of antecedents: inequality for entire functions with zeros at ±i/2 for (PBP_T)
- `ROUND_031_B.md` — Round 031 B — Primitivity as a quantitative bound and generation of the negative block by translations in log ℕ
- `ROUND_032_A.md` — Round 032-A — Is the existence of weights with margin a property of the integers? (NUMERICAL)
- `ROUND_032_B.md` — ROUND 032 B — Selection gate: (PBP_T) as a problem of representing measures of the origin on the infinite polydisc
- `ROUND_095_A.md` — Prime dilations: negative sign of the cyclotomic finite part
- `ROUND_095_B.md` — No self-energy constant repairs the cyclotomic finite part
- `REVIEW_001_ABD.md` — Review of the selection memos ROUND_001_A, ROUND_001_B and ROUND_001_D
- `REVIEW_001_LC.md` — REVIEW_001_LC — Critical review of ROUND_001_L and ROUND_001_C
- `REVIEW_002_A.md` — REVIEW_002_A — Critical review of ROUND_002_A (exterior tail of the hyperbola as a sum of squares)
- `REVIEW_002_BC.md` — REVIEW_002_BC — Critical review of ROUND_002_B and ROUND_002_C
- `REVIEW_003.md` — Review of round 3 (selection over nine non-excluded zones)
- `REVIEW_004.md` — Review of round 4 (meta SP-161 with signed weights and four non-excluded zones)
- `REVIEW_005.md` — Review of round 5 (generative: write an object from the specification A1–A6)
- `REVIEW_006.md` — Review of the selection gate after round 6 (rule-based splitting: distance bands and per-prime potentials)
- `REVIEW_007.md` — Review of round 7 (`ROUND_007_A.md`, `ROUND_007_B.md`, `ROUND_007_C.md`)
- `REVIEW_009.md` — Review of round 9 (`ROUND_009_G1.md`, `ROUND_009_G2.md`, `ROUND_009_G3.md`)
- `REVIEW_022_027.md` — Independent review of ROUND_022_A, 024_A, 024_B, 025_B and 027_C
- `REVIEW_030_031.md` — Independent review of ROUND_030_A, ROUND_030_B and ROUND_031_B
- `ANNEX_114_D163_D135.md` — Annex — The objects D.163 and D.134/D.135 of phase 114: statements, status and relation to phase 212
- `ANNEX_161_FILES_1.md` — Annex: file-by-file reading of phase 161, part 1 (README and R161_000 to R161_027)
- `ANNEX_161_FILES_2.md` — Annex: file-by-file reading of phase 161, part R161_028 – R161_055
- `ANNEX_161_FILES_3.md` — Annex: file-by-file reading of phase 161, part 3 (R161_056 to R161_099)
- `ANNEX_170_FILES_1.md` — Annex 170 — files, stretch 1 (R170_000 to R170_822)
- `ANNEX_170_FILES_2.md` — Annex: phase 170, files R170_823 to R170_840
- `ANNEX_170_FILES_3.md` — Annex 170 — stretch 3: files R170_841 to R170_862
- `ANNEX_170_FILES_4.md` — Annex 170 — stretch 4: files R170_863 to R170_900
- `ANNEX_211_FILES_1.md` — Annex 211 — Files AUDIT_001 … POWER_DEFICIT_LIMIT_013 (61 files)
- `ANNEX_211_FILES_2.md` — Annex 211 — Files, second batch (POWER_DESCENT_016 … POWER_INVERSE_INTERIOR_022)
- `ANNEX_211_FILES_3.md` — Annex 211 — third portion of files (POWER_INVERSE_INTERIOR_AUDIT_022 … POWER_RECURRENCE_BOUNDARY_036)
- `ANNEX_211_FILES_4.md` — Annex 211 — Files POWER_REDUCTION_AUDIT_044 … POWER_THETA_DENSITY_ORIGIN_087 (106 files)
- `ANNEX_211_FILES_5.md` — Annex 211, block 5 — complete reading of `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md` … `ROUND_001_A.md`
- `ANNEX_211_FILES_6.md` — Annex 211 — files ROUND_001_B to ROUND_007_B (complete reading)
- `ANNEX_211_FILES_7.md` — Annex 211 — files ROUND_007_C to ROUND_016_A (complete reading)
- `ANNEX_211_FILES_8.md` — Phase 212 — Complete reading annex: files of phase 211, block 8
- `ANNEX_211_GLOBAL_REVIEW.md` — Annex — Complete reading of `phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`
- `ANNEX_211_GRAM_HYPERBOLIC.md` — Annex 211 — Translation Gram kernel, hyperbolic model and audit
- `ANNEX_COTEJO_LORENTZ_1.md` — Annex — Targeted cross-check: Hodge, Lorentz, Alexandrov–Fenchel, log-concavity
- `ANNEX_COTEJO_LORENTZ_2.md` — Cross-check annex — Lorentz-type signature and mechanisms with closure rules (part 2: stability, Lee–Yang, Laguerre–Pólya, total positivity, closure under product or convolution, flows)
- `ANNEX_COTEJO_NULLDIR.md` — Cross-check annex — near-null directions of a_T on P_T and window in c
- `ANNEX_INDEX_04.md` — Phase 212 — Annex to the consolidated file: route index, phases 100–189 (file 04)
- `ANNEX_INDEX_README.md` — Annex to RULES_AVOID — routes index, README lines 366–2396
- `ANNEX_LITERATURE_CONCENTRATION.md` — Annex — literature: concentration-type positivity mechanisms
- `ANNEX_MARGIN_CONFLICT.md` — Annex: the conflict over the margin of λ_A(T)
- `ANNEX_PHASE_193_LABELS.md` — Annex — Relabelling of the candidates of phase 193
- `ANNEX_PHASE_193_PRIMARY.md` — Annex — Complete primary reading of phase 193 and contrast with ANNEX_PHASE_193_LABELS.md
- `ANNEX_SONIN_READING.md` — Annex — Primary-source reading of the semilocal Sonin chain
- `TRIAGE_D_1.md` — Triage D-1: row D ideas recorded and never carried through (list 1, items 1–41)
- `TRIAGE_D_2.md` — Triage D-2: row D ideas written and never executed (items 42–82)
- `TRIAGE_D_3.md` — Triage D, list 3: row D ideas recorded and not carried through (items 83–123)
- `TRIAGE_D_4.md` — Triage D — list 4 (items 124–164, phases 170–211)
- `TRIAGE_D_5.md` — Triage D, list 5 (items 165–201)
