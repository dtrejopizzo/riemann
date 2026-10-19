# Phase 192 — Review summary

Reviews: EI_001_REVIEW.md, EI_002_REVIEW.md, EI_003_REVIEW.md.
 anywhere. Pen and paper; no numerics.
**No sign; no negative value of 𝔞_T for ζ; λ_A(T) unchanged at every T.**

## 1. Verdicts
| memo | identities | object vs the shape theorem | sign content |
|---|---|---|---|
| EI_001 (exterior field of h*) | Lemma 1, Thm 1 (2.1), Thm 2(i)–(iii), P1–P3: CONFIRMED PROVED (elementary; (2.1) = prop:wit-cheb split applied outside I_T). 2 minor FIXes (size factor e^{T}; residue constant ARGUED) | **EXCLUDED** — invariant under every O1–O15 (holds for any positive or signed comb, any kernel, ζ_K, random positions) | REF-D (C*_A = SPEC_A Lemma S) |
| EI_002 (Mellin / ℤ²-Poisson on s_w) | Thm 1, Thm 2 (split), Thm 3(i) bulk+edge, Thm 3(iii), Thm 4: CONFIRMED PROVED. **FIX**: Corollary "Fact N2 upgraded to PROVED" is false (the polar term M^{½−iγ}W(½−iγ) is of size M^{½} at low ordinates; no annihilation); Thm 3's Poisson framework needs the y ≥ 1 cut and boundary terms (kernel singular at the corner); Thm 5(d) is ARGUED, not PROVED | **EXCLUDED** — invariant under O1–O5, O7, O11, O15 (test lattice is the prover's choice; the (0,0) vanishing is Tate, not ℤ) | REF-D (T*₃(η) = (S), SPEC_B) |
| EI_003 (Z_X, Z_T, σ_T = 2Θ_X′; "symbol rigidity") | Thm 1 CONFIRMED PROVED (elementary). (2.1) identity CONFIRMED; its size claim "test ≈ cζ for |τ| ≤ M^{1−ε}" is **FALSE** (same polar term). **Thm 2 is a tautology**: "every expression for σ_T is affine in Λ" is eq:symbol/prop:finite(iv); 𝔖 is not a deduction class (no 𝖯, no falsifier, no lem:transfer instance); as a NO-GO it is ARGUED and aimed at the wrong clause | **EXCLUDED** — invariant under every O1–O15; borderline retry of N_BUILD_005 (partial Euler products) | none (no statement with a sign) |

## 2. Column moves requested in README — endorsed / rejected
| proposed move | decision | reason |
|---|---|---|
| "Λ enters non-linearly" → NO column on the symbol side, "PROVED impossible" (EI_003 Thm 2) | **REJECTED** | Category error. cor:shape(a) / prob:region(3) require the *deduction* to use Λ non-linearly ("a linear use is a measure identity on the window", lem:shape-lin); σ_T itself has been affine in Λ since eq:symbol. The three constructions use Λ linearly — a fact about them, predicted by cor:shape(a), not a NO-GO for the region |
| "Euler × FE × ℤ jointly as mechanism" → "jointly as factors" | **REJECTED as a region move** | prop:shape-inputs(iv) stands unchanged; the memos show their objects do not meet it. "Factors in one integrand" with no sign is identification (W-identification), which thm:shape(C) excludes |
| "ℤ-integrality as mechanism: YES" for EI_002/EI_003 | **REJECTED** | ℤ-Poisson/Mellin act on the test lattice (m,k) chosen by the prover; the second-order (0,0) vanishing uses only the two Tate conditions of F₀; all identities survive O6/O11 (Beurling) and O15 (random positions) applied to the comb |
| "doubly-exponential margin from the identity" → NO for all three | **REJECTED as a region move; ACCEPTED as a verdict on the objects** | lem:shape-margin(i) is a constraint on every proof; nothing in phase 192 shows an exact identity cannot carry it (the exact Schur reductions in prob:region's own "not excluded" list carry the whole margin). The three objects simply do not produce one |
| "names ζ vs ζ_K: YES" for EI_002/EI_003 | **REJECTED** | prob:region(10) requires the separating property at a load-bearing line; naming it without any sign-bearing use is not meeting the clause |
| Fact N2 (phase 190) NUMÉRICO → PROVED | **REJECTED** | False (EI_002 review §1). Stays NUMÉRICO. If the numerical observation is right, EI_002 Thm 2 reads it as W_M(½−iγ) ≈ 0 at the low ordinates for the minimizer's cutoff — zero-side, descriptive |
| Correction to SPEC_A §2(d) (polar partner of n_j is the opposite-collar Tate moment, not 2n_j^{−½}; archimedean coupling at lag 2T_j is K₁(2T_j) = O(e^{−5T_j})) | **ENDORSED (PROVED)** | re-derived: for primitive x and t on the collar, ∫2e^{−(t−s)/2}x = 2e^{−t/2}A(x) = 0 |
| Correction to SPEC_B §4 Line 2 (second-order vanishing of the continuous atom sum: PROVED in the bulk by both Tate conditions, explicit quadratic edge term, essential cut y ≥ 1) | **ENDORSED (PROVED), with the Poisson bookkeeping FIX** | re-derived (EI_002 review §1) |
| New index rows P192-EI1/EI2/EI3 | EI1, EI2: acceptable as "PROVED identity, no sign, REF-D content". **EI3 as "symbol rigidity NO-GO" must not be written**: record it as "σ_T = 2Θ_X′ phase identity (PROVED, elementary); no NO-GO" | |

## 3. Which SI-column properties move to the NO column as a result of phase 192
**None.** Every property of the admissible region (Problem (R)(1)–(10); SHAPE §3(e)1–10) stands as before. Phase 192 produced three exact identities that are invariant under all modifications of thm:shape(A) and therefore, by thm:shape(C), cannot be load-bearing in any valid proof; their sign content, where they have one, is SPEC_A's C*_A (= Lemma S) and SPEC_B's T*₃ (= (S)), both already REF-D in the index. The round confirms the two known channels for non-linearity (h*(Λ) via the resolvent; a test built from ζ's coefficients against an affine symbol) and adds no third; it does not prove that no third exists.

## 4. Errors to fix before any of this is cited
1. EI_002 Corollary of §3 and README/table line "Fact N2 → PROVED": withdraw.
2. EI_003 §2: "the test is c·ζ up to M^{−Aε} for |τ| ≤ M^{1−ε}" and "the tail is the only place the density differs from c²F̂₀²|ζ|²": false; the polar term M^{½−iτ}W(½−iτ) dominates at bounded height.
3. EI_003 Thm 2: relabel as a restatement of eq:symbol/prop:finite(iv); delete "PROVED NO-GO for non-linear in Λ"; delete the corresponding README column move.
4. EI_002 Thm 3: state the ℤ²-Poisson with the y ≥ 1 cut and its Euler–Maclaurin boundary terms (the kernel is (xy)^{−½}-singular at the origin; the cut produces 1/|ℓ₂| dual decay); "absolute convergence" and "support touches neither axis" are wrong.
5. EI_002 Thm 5(d): ARGUED.
6. EI_001 §4: size of ⟨G,p⟩ is ≍ e^{T}‖G‖‖h*‖_{L¹(left collar)}, not e^{−T/2}.

## 5. What survives for the record (PROVED, no sign)
- EI_001 (2.1): E = p − q − r with p the truncated density-1 field (opposite-collar Tate moment), q the Chebyshev fluctuation tested by H̃(e^t/u), r the exponent-5/2 archimedean tail; Ê holomorphic in |Im τ| < 5/2; SPEC_A §2(d) corrected.
- EI_002 Thm 2 (3.1) smoothed-Perron split of the family's test with exact contour remainder; Thm 3(i),(iii): exact second-order cancellation of the continuous atom sum on the family by the two Tate conditions, edge term and y = 1 boundary identified; Thm 4: ℤ²-self-duality of near-coincidences (= N_009 on ℤ²).
- EI_003 Thm 1: σ_T = 2Θ_X′, R_X(½+iτ) = Θ_X′ + iZ_T′/Z_T.
None of these is a route; all are coordinates.
