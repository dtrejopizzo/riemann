# TRACT_D_README_001 — Phase 204, part D: tractability of ALL «REF-D / branch 2 / reformulation» entries in the index README

Every reformulation is stated D-only (window form 𝔞_T ≥ 0 on P_T, or λ_A(T) ≥ 0, or L′♯). This memo
**classifies; it proves nothing new.** Only this file was written. The 13 reformulations R1–R13 from `TRACT_001.md` are not
re-analyzed: their verdict is cited.

## Summary (≤300 words)

`grep -i "REF-D|branch 2|reformulat|restatement|equivalent to D"` on `ROUTES-TRIED-INDEX/README.md` currently gives **101 lines**
(103 occurrences of «REF-D»; it was 82 when TRACT_001 was written). After removing the header, meta-lines, and the two from
phase 204 itself, **90 route entries** remain. They are unified into **17 groups** (G1–G17): most are the same reformulation
under a different name (dual certificate ≡ ν̂ ≥ 0 ≡ LP ≡ Herglotz ≡ HKS ≡ Gram appears **15 times**; (★★)/𝒲_ext
**13 times**; «zero side» **9 times**).

TRAT verdicts: **NO** (closed by theorem/falsifier) 31 entries; **TRANSFER** (general theory consumes the data's
positivity) 46; **YES** 13 entries, falling into **only three groups**: G10 = exact induction by contacts L*_j / B8 / (L2)
(= R13, with the new fact that the index already marked it ADMISSIBLE OPEN), G4 = polar capacity 𝔊_T = D_pol − M(0) (= R6, now
with the explicit Kreĭn–Weyl tool from OO_001), and G14 = spectral flow/Maslov (l.209), which **is not a separate route but
the general theorem (Robbin–Salamon crossing forms) that R6/R13 were missing**. R10 (Lemma F) drops from YES to «weak
conditional YES»: the audit at l.523 shows that convexity is not automatic and that the positive F₀ test at r* is REF-D.

Stronger than D with their own path: only two — **L′♯ via Fredholm + finite block** (reduces to G10) and the
**quantitative no-crossing version** (det S_{T,k} ≥ c(T) > 0 between contacts), which is stronger than D and is exactly what
Kato + crossing forms can give. Ranking: G10 > G4 (+G14 as tool) > G16 (Lemma F) > rest.

Honest count: of the 90, **38 were dismissed only by judgment** («= D», «REF-D», «restatement») without a theorem or
falsifier written in the entry; of those 38, **31 are correct transfers** (the judgment was replaceable by lem:shape-est,
lem:shape-ident, thm:Z/thm:O, C-pos, or Φ.1) and **7 are the YES entries** of G4/G10/G14/G16.

---

## 0. Method and criterion (summary of TRACT_001 §0)

- **TRAT = YES:** there exists a class of general theorems 𝒯, not specific to row D, within whose domain the reformulation
  falls, and the remaining hypothesis of 𝒯 is **different from the sign value being sought** (e.g. a no-crossing property, a
  boundary-value rigidity, an interpolation inequality without Λ).
- **TRANSFER:** the general theory exists but its input hypothesis is the positivity of the window data rewritten (Bochner,
  Kreĭn, LP duality, Gårding, Toeplitz/Szegő, Łojasiewicz, Beurling–Deny Dirichlet forms, etc.).
- **NO:** closed by a class theorem or an explicit falsifier (not by judgment).
- **Original dismissal:** J = judgment («REF-D», «= D», «restatement») without a theorem in the entry itself; T = theorem or
  falsifier written in the entry; M = meta-line (not a route).
- Inherited admissibility filter (TRACT_001 §5, lem:transfer, thm:noimport from sec:spec): any YES must **fail for
  F_DH** (T ≥ 9/5) and for Epstein (T ≥ 1.59); its first lemma must declare which feature of Λ it uses. A continuation
  argument in T can satisfy this, because F_DH does cross.

## 1. Inventory of lines

101 grep lines: 22 (header), 110–112 and 331 (meta: «REF-D ≠ closure»), 592–593 (phase 204) → **8 non-routes**. That leaves
**93 lines, 90 entries** (l.110–112 are a single entry; 520 duplicates 519; 559 audits 558 — counted separately because the
index lists them separately, but they are unified in the group).

## 2. Groups (unification of duplicates)

| G | unified reformulation (D-only) | README entries | = TRACT_001 |
|---|---|---|---|
| G1 | **dual certificate / ν̂ ≥ 0 on the admissible cone / LP / Herglotz / Gram** (thm:Z, thm:O, def:PD) | 212, 255, 284, 306, 357, 387, 389, 394, 400, 407, 453, 469, 546(Gram), 505, 524(B) | R7 |
| G2 | **(★★) / 𝒲_ext on Z-images / Sonin ring / moment 𝔔** | 452, 458, 463, 466, 468, 486, 516, 519, 520, 560, 581, 582, 588 | R1 |
| G3 | **gauge-minimized L′♯** | 450 | R2 |
| G4 | **2×2 polar capacity 𝔊_T = D_pol − M(0) / boundary triple / KVB / Kreĭn** | 507, 560(Kreĭn), 209(boundary triples in the same item) | R3+R6 |
| G5 | **block Schur A_⊥⊥(1) / inertia C_RR / N3 / V6** | 536(N3, I.1), 538, 553(V6) | R4 |
| G6 | **Hodge / Horn A / Horn B / (Big♯) / (Eff_Δ) / Restatement 19.29** | 555, 556, 557 | R4-Horn, R5 |
| G7 | **«the mass is at the zeros» / zero side / Stokes** | 408, 521(a),(d), 544, 550(S3), 567, 469(BRS), 344? (no: G9) | R9 partial |
| G8 | **Arch ≥ Near / near-coincidences (S) / T*₃(η) / site independence / A_M(Λ)** | 55, 135, 175, 296, 390, 391, 393, 415 | — (new) |
| G9 | **minimizer exterior field C*_A / Lemma S / central cell {|Z_T|<1}** | 165, 174, 263, 344, 377 | — (new) |
| G10 | **exact induction by contacts using only identities L*_j(θ) / B8 / (L2) S_{T,k} ⪰ 0** | 142, 347, 367, 380 (+06_ l.181) | R13 |
| G11 | **concavity in c / infimum λ_A / Danskin / Guerra / D_∃c / Markov 𝖯⋆** | 277, 294, 350(+353), 434, 536(N1), 589 | — (new) |
| G12 | **REF-D⁺: quantitative λ_A(T) > 0 (quantitative Hamburger, FE defect, tangent cone)** | 422, 429 | R8 partial |
| G13 | **(Π_L): Green energy 𝓓(Φ) − 𝓓(ρ_SΦ) ≥ 0** | 399, 404, 405, 406 | — (new) |
| G14 | **integer invariant / spectral flow / Maslov / Floer / Bridgeland / nonnegative rank** | 209, 251, 571, 572, 573, 574 | — (new) |
| G15 | **sign-free arithmetic identities** (AFE, q≥2 divisor-gauge residue, Eichler–Selberg, 𝔞^{Euler}, V3-GC, Rankin, DH-Q2, P7, S1 of 𝔇) | 392, 396, 398, 514, 539, 540, 553(V3), 554, 558, 559 | R9/R12 partial |
| G16 | **Lemma F (convexity in ε of the n^ε-deformed comb on f♯)** | 521(f), 523 | R10 |
| G17 | **class theorems that *produce* the «branch 2» label** (Thm 3(iii), Φ200, M200, C-pos, Ξ1/Ξ2, cumulants, Gårding) | 403, 421, 528, 545, 546, 547, 577, 578 | R8, R12 |

## 3. Full table (one row per entry)

Columns: **l.** = README line; **dir.** = direction proved (⟺, ⇒D, ⇐D); **F** = strength vs D (= equal, > stronger,
< weaker, ≠ not a reformulation of D); **TRAT**; **desc.** = reason for the original dismissal (J/T/M).

| l. | G | route | D-only statement (one line) | dir. | F | TRAT | desc. |
|---|---|---|---|---|---|---|---|
| 22 | — | header | defines the REF-D label | — | — | — | M |
| 55 | G8 | lattice matrices A_M, L2_028–031 | A_M(Λ) ⪰ 0 ∀M on the full lattice at fixed T₀ | ⟺ D at T₀ (T₀ ≤ 0.3, already PROVED by Thm A) | = | NO (empty: D at T₀ ≤ log 2 is proved) | J |
| 110–112 | — | 10/15 correction | «REF-D is not closure» | — | — | — | M |
| 135 | G8 | phase 190: Q_M(w) on s_w | volume (defects N=2,3,4 vs Arch) + boundary at scale M | ⟺ D at T₀ | = | TRANSFER (boundary = Λ estimate at margin scale; lem:shape-est(i)) | J |
| 142 | G10 | SPEC_A, B8, L* | exact contact step T_j → T_{j+1} | ⟺ | = | **YES** (see G10) | J («exact reformulation») |
| 165 | G9 | EI_003 symbol rigidity | the nonlinearity in Λ enters only through h*(Λ) | — | = | TRANSFER (Theorem X: functional of h*) | T (Thm 2 withdrawn to tautology, l.~180) |
| 174 | G9 | EI_001 exterior field | C*_A = Lemma S ≥ 0 | ⟺ in the window | = | TRANSFER | J |
| 175 | G8 | EI_002 family s_w | T*₃(η) = (S) ≥ 0 | ⟺ | = | TRANSFER | J |
| 209 | G14 / G4 | front A: Maslov / spectral flow; boundary triples | «the integer index is constant in T» | ⟺ (constancy = positivity) | = | **YES as a tool** (crossing forms) | J |
| 212 | G1 | front B: convex decomposition; gap Γ | λ_A ≥ 0 as a convex combination / Γ ≥ 0 | ⟺ | = | TRANSFER (= certificate; density ceiling) | J |
| 251 | G14 | front F: Floer, Bridgeland | Floer homology = λ_A; support = 𝔞_T ≻ 0 | ⟺ | = | TRANSFER | J |
| 255 | G1 | G0 squares = Gram | 𝔞_T = Σ|L_j|² | ⟺ | = | TRANSFER (thm:sos: pure arithmetic of squares is empty) | T |
| 263 | G9 | front G consequence | nonlinearity only via the minimizer | — | — | TRANSFER | J |
| 277 | G11 | Cor 6 Markov/(S⁺) | separation of ζ by {(S⁺), pole, FE, Markov ∀T} | ⇒ separation, not an inequality | ≠ | NO (gives no inequality; Cor 6 PROVED) | T |
| 284 | G1 | Brascamp–Lieb | BL with constant = 𝔞_T | ⟺ or generic | = | TRANSFER | J |
| 294 | G11 | Guerra/ASS | concave interpolation | upper bound only | — | NO (concavity ⇒ upper bounds; INVENT Thm 2.3) | T |
| 296 | G8 | site independence | 𝖡 PSD on sites with ratios → 1; on primes: Arch ≥ Near | ⟺ PROVED | = | TRANSFER (Schoenberg/Bochner consumes PD) | J («reformulation») |
| 306 | G1 | prime-site LP on the torus | LP dual attained | ⟺ PROVED | = | TRANSFER (LP duality) | J |
| 331 | — | audit 193 | «~1/3 of dismissals are REF-D» | — | — | — | M |
| 344 | G9 | D8 W(α) / central cell | ζ-specific entry on {|Z_T|<1} | ⟺ | = | NO for W(α) (interpolation NO-GO PROVED); cell: TRANSFER | T + J |
| 347 | G10 | reworked SPEC_A | exact induction using only identities | ⟺ | = | **YES** — index: «OPEN and ADMISSIBLE» | J |
| 350 | G11 | 𝖯⋆ Markov | J_T ≥ 0 (jump measure) | ⟺ PROVED | = | TRANSFER (Beurling–Deny consumes) | T (identification PROVED) |
| 357 | G1 | Viazovska V1 | discrete primal attained | ⟺ | = | TRANSFER | J |
| 367 | G10 | step lemma L*_j(θ) | contact step with Chebyshev identity | ⟺ | = | **YES** | J («ADMISSIBLE, OPEN, REF-D») |
| 377 | G9 | CA_R3 exterior field | C*_A via transcendental evaluation | ⟺ | = | TRANSFER except via G10 | J |
| 380 | G10 | round R audit | «ADMISSIBLE» not endorsed: REF-D | ⟺ | = | **YES** (same object as 367) | J |
| 387 | G1 | INV_A Θ | Herglotz/thm:Z | ⟺ | = | TRANSFER | J |
| 389 | G1 | INV_B linear variance | = G0 | ⟺ | = | TRANSFER | J |
| 390 | G8 | INV_C off-diagonal h⁰ | Arch − Near limit ≥ 0 | ⟺ (Thm 4 PROVED: limit only) | = | TRANSFER | T (Thm 4) |
| 391 | G8 | INV_D Weil character | renormalized defect − comb ≥ 0 | ⟺ | = | TRANSFER (‖ω_+‖²_HS ≥ 0 blind to the comb) | J |
| 392 | G15 | INV_E Eichler–Selberg | sign via σ^{*−1} | — | ≠ | NO (Hölder–Ostrowski PROVED; comb-generic B″) | T |
| 393 | G8 | INV_G min term | positive part = Near | ⟺ | = | NO (𝓒_G class Beurling-generic PROVED) | T |
| 394 | G1 | INV_F Pick on σ>1 | transport = thm:Z | ⟺ | = | NO (F2 PROVED, cones on log ζ) | T |
| 396 | G15 | INV_H q≥2 residue | sign of s_φ at small τ | ⟸ (pointwise) | > | NO (K2 PROVED: inf s_φ = −∞ ∀ finite gauge) | T |
| 398 | G15 | INV_K AFE | AFE/Euler–Maclaurin | ⟺ | = | TRANSFER | J |
| 399 | G13 | INV_L (Π_L) | Green energy with ℤ handle ≥ 0 | ⟺ | = | TRANSFER | J |
| 400 | G1 | INV_O HKS | HKS functionals = dual certificates | ⟺ | = | TRANSFER (O2 PROVED) | T |
| 403 | G17 | INV_M Gårding | unique cone = PSD | ⟺ | = | NO (M1 PROVED: not real-stable) | T |
| 404 | G13 | INV_P (Π_L) | same as 399 | ⟺ | = | NO for subharmonicity/Jensen (P4: wrong direction); TRANSFER for (Π_L) | T |
| 405 | G13 | INV_Q | positivity Q2+L3 = (Π_L) | ⟺ | = | NO (𝒦_mix, Q3 additive over places) | T |
| 406 | G13 | INV_R Green energy without log | 𝓓(Φ) − 𝓓(ρ_SΦ) ≥ 0 | ⟺ (R1 PROVED) | = | TRANSFER (weight factors through ∏γ_v, O_6-stable) | T |
| 407 | G1 | INV_T unimodular gauge | expansive q ⇒ certificate | ⇒ | > | NO for contractive (T3 PROVED); TRANSFER for expansive | T |
| 408 | G7 | INV_S Stokes | sector sign = zero side | ⟺ | = | TRANSFER | J |
| 415 | G8 | INV_V (G2) | 𝔄ff_T ≥ Re⟨Vf,f⟩_Ш − 2A_∞ | ⟺ (tautological) | = | TRANSFER (audit: «no side carries sign») | J |
| 421 | G17 | BARRIER_001 Thm 3(iii) | classification: generic / certificate / REF-D | — | — | — (class theorem) | T |
| 422 | G12 | BARRIER_D1 quant. Hamburger | sup_{S_ε}⟨a−Λ,w_T⟩ ⇒ quantitative λ_A > 0 | ⇒ | > | TRANSFER (REF-D⁺) | T (Thm 4) |
| 429 | G12 | BARRIER_X tangent cone | WP_T of deleted finite combs | ⟺ | > | TRANSFER | T (X2 Kronecker parity) |
| 434 | G11 | BB_001 | Π monotone in c; λ_A concave | upper bounds only | — | NO (BB3/INVENT Thm 2.3) | T |
| 450 | G3 | MECH_001 L′♯ | L′♯ | ⇒ D PROVED | > | cites R2 (YES via G10) | — |
| 452 | G2 | PROOF_A | 𝒲_ext[Zr] ≥ c·dist² | ⟺ L′♯ | > | TRANSFER (R1) | T (Bochner/C–S NO-GO) |
| 453 | G1/G2 | PROOF_D Sonin | Son ≥ 0 + remainder (Cor 2.2, ε_c) | ⟺ | = | TRANSFER | T («Son+bound» NO-GO) |
| 458 | G2 | PROOF_H | (H) virial to precision 1/c | ⇒ L′♯ | > | TRANSFER (needs the minimizer) | J (audit: «reformulation») |
| 463 | G2 | PROOF_R | 𝔔 = ∫Θ_∞|F|²/2π + N′(0) + 2AB ≥ 0 | ⟺ | = | TRANSFER (R.3: pointwise monotonicity NO-GO) | T |
| 466 | G2 | PROOF_U | inequality in the Sonin ring | ⟺ (★★) | > | TRANSFER | J |
| 468 | G2 | PROOF_V | ∫e^{−t/2}(ǧ∗Ψ̌)dR_Λ ≥ … | ⟺ | = | TRANSFER; sectors NO-GO | T |
| 469 | G7 | PROOF_W BRS/Gram | pair form − Gram = off-line pairs | ⟺ | = | TRANSFER | J |
| 486 | G2 | TEST_2X2 | exterior bracket | ⟺ W(g*) > 0 | = | TRANSFER | J |
| 505 | G1 | PROOF_MM | Gram in Mellin; passivity | ⟺ | = | NO (passivity/small-gain NO-GO: margin = W_T) | T |
| 507 | G4 | PROOF_OO KVB | S ≥ 0 in the triple with M(0) = −S^Sch | ⟺ | = | TRANSFER for KVB; **YES** for the T-dynamics of 𝔊_T (G4) | T (as KVB) |
| 514 | G15 | AUDIT_SPEC_001 P7 | P7 = target | ⟺ | = | NO (it is the literal target) | J |
| 516 | G2 | Q1 SQ / Q2 ladder | yᵀ𝔅y = 𝒲[g] | ⟺ | = | NO (tautology; ladder ≡ W_T) | T |
| 519 | G3 | C1(ii) | L′♯ on subspace ∋ extremal | ⇒ | > | TRANSFER | J |
| 520 | G3/G5 | C1_DUPLICATION | κ_new sandwiched ⇒ L′♯ at level μ | ⟺ | > | TRANSFER | T (Prop C1.1) |
| 521 | G7/G16 | A_MU (a),(d),(f) | mass at zeros; ℰ ≥ 0; semi-annular derivative | ⟺ | = | (a),(d) TRANSFER; (f) → G16 | J (a,d) |
| 523 | G16 | AUDIT_AMU | Lemma F not automatic; positive F₀ = REF-D | — | ≠ | **weak conditional YES** | T (Theorem D = chain rule) |
| 524 | G1 | PI_MU B | Jordan/B+c, B_edge | ⟺ | = | TRANSFER | J |
| 528 | G17 | M200 | class 𝒦_200 → generic/cert./REF-D | — | — | — | T |
| 536 | G11/G5 | SPEC_004 N1, N3, I.1 | infimum; block inertia; Schur of C_RR | ⟺ | = | N1 NO (concavity); N3/I.1 TRANSFER (= R4) | T/J |
| 538 | G5 | LEMMA_I3 | A_⊥⊥(1) ⪰ 0 in block | ⟺ | = | TRANSFER (R4); O(1) gap NUMERICAL | J |
| 539 | G15 | Q2 DH/Bateman–Grosswald | reformulation of a result about DH, not about D | — | ≠ | NO (not a reformulation of D) | T |
| 540 | G15 | SPEC_005 | 𝔞^{Euler} ≥ 0 | ⟺ | = | TRANSFER | J |
| 544 | G7 | cumulants | zero side = rewriting of the comb | ⟺ | = | NO (Lemma 13.1 PROVED: indefinite form) | T |
| 545 | G17 | Φ200 / Φ.13 | branch 2; ultraproduct = REF-D | — | — | NO (Φ.13 PROVED) | T |
| 546 | G17 | Ξ1 von Neumann | τ(PEP) = Gram | ⟺ | = | NO (hyperfinite blind, PROVED) | T |
| 547 | G17 | Ξ2 Loeb | st λ_A* = λ_A | ⟺ | = | NO (Łoś, PROVED) | T |
| 550 | G7 | DH_TRANSFER S3 | zeros → REF-D | ⟺ | = | TRANSFER | T (channel (i) PROVED) |
| 553 | G15/G5 | SPEC_008 V3, V6 | V3-GC ≡ 𝔞^ζ ≥ 0; V6 = N3 | ⟺ | = | NO (large sieve: upper bound only) / TRANSFER | T |
| 554 | G15 | Rankin f×f̄ | 𝔞^{f×f̄} − 𝔞^{sym²f} ≥ 0 | ⟺ (Φ.12) | = | TRANSFER | T (Prop 19.2) |
| 555 | G6 | Restatement 19.29; H3 Horn A | D^W rules out linear systems | — | = | NO (Thm 19.25, 21.15) | T |
| 556 | G6 | Horn A | (W⁰) + (Eff_Δ) | ⟺ | ≥ | NO (Thm HA) | T |
| 557 | G6 | Horn B / (Big♯) | (W⁰) ∧ (Eff_𝓔′) | ⟺ | ≥ | NO (Thm HB) | T |
| 558 | G15 | 𝔇 construction, S1 | conditions defined with the form | ⟺ | = | NO (Thm 3 PROVED) | T |
| 559 | G15 | AUDIT_DCONS | Thm 3′: seeing the test ⇒ REF-D | — | = | NO (Thm 3′ ARGUED; δ ≡ 0 PROVED) | T |
| 560 | G2/G4 | oscillations; Kreĭn | log N cancels on both sides | ⟺ | = | TRANSFER | J |
| 567 | G7 | multiplicative gauge | mass at zeros read twice | ⟺ | = | NO (M.1–M.2, R9) | T |
| 571 | G14 | FAMILIES_A V1 | integer pairing; branch-2 risk | ? | ? | TRANSFER (risk declared) | J |
| 572 | G14 | FAMILIES_B V1 | nonnegative rank; branch-2 risk | ? | ? | NO (see 574) | J |
| 573 | G14 | SPEC_201 B-V1 | LP slack; branch-2 risk | ? | ? | NO (see 574) | J |
| 574 | G14 | AUDIT_201 B-V1 | T201-a + T201-b = L′♯ | ⟺ | > | NO (monotone falsifier, R11) | T |
| 577 | G17 | FAMILIES_C C-pos | intrinsic positivity with Λ in hypothesis = branch 2 | — | — | NO (C-pos identity PROVED) | T |
| 578 | G17 | CPOS_CLASS | thm:noimport (iv) | — | ≥ | cites R12 | T (i–iii) |
| 581 | G2 | BUILD_R1 X1 | partition of (★★) by q-classes | ⟺ | > | TRANSFER | J («restatement») |
| 582 | G2 | AUDIT_202 X1 | X1 = partition of (★★) | ⟺ | > | TRANSFER | J |
| 588 | G2/G10 | INVENT W^(N) | ladder W^(N) ≥ 0 by contacts | ⇐ W* ≥ 0 if c_{g*} > 0 | = | TRANSFER (becomes YES only if rewritten as G10) | J |
| 589 | G11 | AUDIT_203 III | residues ≥ 0 ⇐ W* ≥ 0 | ⟸ | = | TRANSFER | J |
| 592–593 | — | phase 204 | this work | — | — | — | M |

(Lines 353 —D_∃c— and 06_ l.181 —(L2)— do not contain the keywords but are part of the same item as 350 and of group
G10; they are treated in §4.)

## 4. Reading by groups

**G1 (15 entries) — dual certificate.** All TRANSFER or NO. The general theory is cone duality (Hahn–Banach, LP,
Bochner–Schwartz, Herglotz, Gram/SOS sums); its input hypothesis is that the functional be ≥ 0 on the cone, which is D by
thm:Z/thm:O. The judgments in this group are replaceable by those theorems from the paper. No YES.

**G2 (13) — (★★).** TRANSFER (TRACT_001 R1): the missing hypothesis is the Chebyshev fluctuation at the margin scale,
beyond the reach of every estimate (lem:shape-est(i) PROVED). The partitions (X1, Sonin ring, sectors, 𝔔, virial (H))
reorder the same term. No autonomous YES.

**G3 (3) — L′♯.** R2: YES only via «Fredholm/Weyl + finite block», which leads into G10.

**G4 (3) — polar capacity 𝔊_T.** R6 was YES. **New in this review:** OO_001 (l.507) PROVED identifies 𝔊_T = D_pol − M(0)
with M the Weyl function of a boundary triple with Γ₀ = Tate functionals. OO_001's dismissal is correct *for KVB*
(Kreĭn–Vishik–Birman requires S ≥ 0 = D: transfer). But the T-dynamics of a 2×2 Weyl function have general theorems that do
not require S ≥ 0: (i) M(z) is Nevanlinna in the spectral parameter (Kreĭn–Langer, CITED), (ii) the variation in T is a
perturbation of the triple's boundary, with a Hadamard formula for M. The missing hypothesis remains **1D no-crossing**
(Lemma T6.2), not the sign. Kept as YES.

**G5 (4) — block Schur.** TRANSFER (R4). The O(1)=3.77 NUMERICAL gap of A_⊥⊥(1) and the identical spectrum for μ=5,10,15
suggest a Toeplitz symbol; Szegő consumes the symbol's sign.

**G6 (3) — Hodge/Horn.** NO (Thm HA, HB, 19.25, 21.15).

**G7 (9) — zero side.** TRANSFER or NO: every general theory about the zero measure (de Branges, Carleson, Fejér–Riesz,
Stokes) receives the data in the form of positivity of a spectral measure; the NOs are proved (M.1–M.2, Lemma 13.1).

**G8 (8) — Arch ≥ Near / (S).** TRANSFER. The cleanest form is l.296 (PROVED): on prime sites Div ≡ 0 and D in T reduces to
**Arch ≥ Near** over tests at primes. Candidate general theorem: Schoenberg (PD on ℝ via functions on sites). Missing
hypothesis: the inequality itself. It is the live residue (S) from the README §Residues; no own path identified. l.55/135
(A_M at T₀ ≤ 0.3) are empty as input: D in those windows is already Theorem A.

**G9 (5) — C*_A / Lemma S.** TRANSFER: it is a functional of h* (Theorem X, phases 183–186). Only exit: rewrite as a
contact step (G10).

**G10 (4 + 06_ l.181) — exact induction by contacts.** **YES.** This is the main finding: the index itself (l.347) left it
«OPEN and ADMISSIBLE in (γ)/A15» with a single gap (θ) («where log ℕ enters ‖ℓ_e‖_{𝔄_j^{−1}}, e.g. the coincidence of the
contact block v_{n_j} against 2n_j^{−½} in the 2T_j phase shift»), and the audit at l.380 only removed the ADMISSIBLE
label for «REF-D». It is R13 in another coordinate: (L2) S_{T,k} ⪰ 0 with continuation in T. The original SPEC_A dismissal
(l.142) died by (γ) using the doubly exponential scale, **which the correction at l.~186 declared overstated** (what is
PROVED is thm:margin, simple exponential). l.345–346 reworked SPEC_A with the proved margin and clause (γ) failed again
*for the version with estimates* (ARGUED), not for the version using only identities. General theorems: Sylvester, Cauchy
interlacing for rank-one borders (lem:contA: the entry instant is empty), eigenvalue continuity (Weyl/Kato), and —from
G14— crossing forms.

**G11 (6 + D_∃c) — concavity in c.** NO as a lower-bound route (INVENT Thm 2.3 PROVED: concavity only gives upper
bounds). **D_∃c** (l.353): ∀T ∃c>0 with λ_A(T;cΛ) ≥ 0, equivalent to a common c*; **weaker than D**. AUDIT_203 (l.589):
c ↦ λ_A(T;cΛ) rises from negative, has a maximum, and equals ≈ 0 at c=1; (1+ε)Λ is negative at ½log15 for ε > 8e−69.
Hence the maximum lies at c* < 1 with a larger margin than at c=1, but no concavity argument carries c* to c=1 (a point
with c > 1, which is negative, would be needed). TRANSFER, weaker, no input toward D.

**G12 (2) — REF-D⁺.** Stronger than D (quantitative positivity in a ball of weights); TRANSFER: the quantifier is the
margin itself.

**G13 (4) — Green energy.** NO/TRANSFER: P4 PROVED gives the wrong orientation for subharmonicity/Jensen/Carleson; T3
PROVED for the contractive gauge.

**G14 (6) — integer invariants.** The «nonnegative rank» variants died by falsifier (l.574, R11). **But l.209
«Maslov: constancy = positivity, REF-D» contains a general tool that was misclassified:** the spectral flow along
T ↦ 𝔞_T (or T ↦ S_{T,k}) is computed by **crossing forms** (Robbin–Salamon 1993/1995, CITED): at a regular crossing T*,
the jump in the Morse index is the signature of the crossing form Γ(T*) = (d/dT)𝔞_T restricted to ker 𝔞_{T*}. The
statement «constancy of the index» is indeed D (transfer), but **computing the crossing form** is a new object: it is a
form on the (typically one-dimensional) kernel given by boundary data at ±T* (Hadamard). This is exactly the general
theorem that T13.1 and T6.2 need. Classified as **YES as a tool**, not as a separate route.

**G15 (10) — arithmetic identities.** NO or TRANSFER; l.539 is not a reformulation of D (false positive of the grep).

**G16 (2) — Lemma F.** TRACT_001 gave it YES. The audit at l.523 (not cited in TRACT_001) establishes: Theorem D is the
chain rule on Z_log (a rewriting of (★★)); the n^ε deformation = moving the line to σ = ½+ε (rule «do not retry
σ-derivatives in Mellin», l.463); «convexity is not automatic (requires ⟨h_m,h_n⟩ ≥ 0)»; A_ε does not vanish on 𝒢̄_T
(ARGUED) and therefore does not descend to the quotient 𝒬_μ; positive F₀ test at r* ⇒ REF-D. **Corrected verdict:
weak conditional YES.** Only the harmonic-analysis question of T10.2 (three lines with boundary) survives, *after*
projecting to the quotient; without that projection the lemma is not well defined. Before any new attempt: resolve
whether A_ε can be corrected by a gauge term (Π_μ, l.524).

**G17 (8) — class theorems.** These are not routes: they are the theorems that **produce** the label. Their relevant
content here: Φ200 and M200 are ARGUED as a class (missing exhaustiveness and a composition rule); none addresses
**continuation arguments in T from the certified boundary** (½log15). C-pos (iv) is ARGUED and explicitly admits that
«stronger might be more tractable».

## 5. Requested answers

### (1) Full list of TRAT = YES, first lemma, and what input it would produce

| # | group (entries) | concrete first lemma | input toward D if proved |
|---|---|---|---|
| S1 | **G10** (142, 347, 367, 380; 06_ l.181; = R13) | **Lemma G10.1 (rank-one border at the contact, OPEN):** at T_j, with k → k+1, S_{T_j,k+1} = [[S_{T_j,k}, b],[bᵀ, β]] with b, β explicit by lem:contA (empty entry); prove that the scalar complement β − bᵀS^{−1}b ≥ 0 reduces to the near-cancellation of the contact block v_{n_j} against 2n_j^{−½} in the 2T_j phase shift (the gap (θ) at l.348). First case by hand: 5 → 7 (CA_R4_001). **Lemma G10.2 (between contacts):** det S_{T,k} ≠ 0 on (T_j, T_{j+1}) via G14. | Closes the **«contact step»** piece of (★★) in the finite block: with G10.1 + G10.2 for every j, D is obtained for every T by induction from ½log15. Relative to sec:spec: it is an object that uses exact Λ(n_j) at the rank-one border, hence it is **not** comb-generic (clause 1) and is not an estimate (lem:shape-est); the step must fail for F_DH at T≈9/5 (filter of thm:noimport (i)). Clause (5) (coupling Λ to the FE by a route other than ζ(½+iτ)) would be satisfied *if* the scalar complement uses the FE in the 2T_j phase shift — that is what (θ) must specify. |
| S2 | **G4** (507, 560, 209-boundary; = R6) | **Lemma G4.1 (Hadamard formula for the Weyl function, probably PROVED with standard work):** d/dT M_T(0) = −Γ₁-trace of the extremal squared + explicit polar term; consequence: dg_±/dT. **Lemma G4.2 (no-crossing, OPEN):** g_+(T*) = 0 forces u_+ ∈ 𝒢̄_{T*}, a contradiction with the polar normalization. | Closes the **2×2 polar block** of the window: D in T ⟺ RD_T ∧ g_± ≥ 0 (R156, PROVED). Produces the «polar» half of (★★) (the term 2A(Ψ̌)B(Ψ̌)) with sign; does not touch the rest of RD_T. Check first whether 𝔊_T is a block of S_{T,k} (if so, S2 ⊂ S1). |
| S3 | **G14** (209; tool) | **Lemma G14.1 (crossing form, PROVED in general by Robbin–Salamon, CITED; its computation here OPEN):** for the analytic family T ↦ S_{T,k} between contacts, at a crossing T* the crossing form is Γ(v) = ⟨v, ∂_T S_{T*,k} v⟩, v ∈ ker; compute ∂_T S by Hadamard as boundary data at ±T*. **Lemma G14.2 (OPEN):** Γ is positive definite at every crossing (eigenvalues only cross upward) or the kernel is never nontrivial. | It is the general tool for G10.2 and G4.2. It closes nothing by itself; it converts «no-crossing» into the sign of a finite-dimensional form on the kernel. Risk: lem:monoT gives λ_A nonincreasing in T, so the global monotonicity runs the wrong way; the crossing form must win by the boundary term, not by monotonicity of the carrier. |
| S4 | **G16** (521(f), 523; = corrected R10) | **Lemma G16.0 (prerequisite, OPEN):** there exists a gauge correction A_ε ↦ A_ε − Π_μ-term such that A_ε vanishes on 𝒢̄_T and F(ε) descends to 𝒬_μ. Only afterward: T10.1 (cheap falsification, NUMERICAL strictly necessary) and T10.2 (three lines with boundary). | If G16.0 + T10.2: the **exterior part carrying the sign** of (★★) (the prime term = F′(0), A_MU (f)), CONDITIONAL on the interior/exterior splice. Weak: the audit left the splice as the place where Λ returns. |

There are no other YES entries. In particular G8 (Arch ≥ Near / (S)), although it is the index's declared live residue,
has **no** general theorem with a hypothesis distinct from the identified sign, in any of its 8 entries.

### (2) Stronger than D and still with their own path

1. **L′♯ (G3) via Fredholm + finite block.** General theorem: if 𝔞_T − 𝔟_T is compact relative to dist²(·,𝒢̄_T) for a
   neighboring Λ-free form 𝔟_T with exact radical 𝒢̄_T (Π.0′ PROVED: the gauge annihilator is two Fourier intervals,
   without ℕ), Weyl gives coercivity except on a finite space; that finite space is S1. Missing non-sign hypothesis:
   relative compactness. It is stronger than D (quantified with κN^{−A₀}) and its bottleneck is constrained by thm:margin
   (A₀ ≳ 15.4/c).
2. **Quantitative no-crossing** (strong variant of S1/S3): det S_{T,k} ≥ c(T) > 0 or min spec ≥ c(T) between contacts,
   with c(T) explicit. It is stronger than D in T and is what Kato + crossing form naturally deliver (a lower bound of
   |Γ| on the kernel gives a lower bound on the distance to the crossing). Missing hypothesis: definiteness of Γ — not
   the sign of 𝔞_T but the sign of its **derivative in T on the kernel**, which is boundary data.
3. **R3 (Kreĭn indeterminacy)** has its own theory for the new half, but that theory *presupposes* the PD of the data:
   it does not count.
4. **G12 (REF-D⁺)**, (★★) (G2), virial (H) (l.458): stronger, with no own path (transfer).

Direct answer: **yes, there are statements stronger than D with their own path — exactly two (L′♯ by Fredholm+finite
and the quantitative no-crossing) — and both lead to the same finite object G10/(L2).** None of the «big» stronger
statements (★★, REF-D⁺, Kreĭn, Horn) has a general theorem whose hypothesis is not the sign.

### (3) Ranking by tractability

1. **G10 / (L2) / L*_j** — finite, explicit, continuity PROVED, the index already marked it ADMISSIBLE OPEN; single gap (θ).
2. **G14 as a tool for G10** (crossing forms: general theorem CITED; what's missing is a computation).
3. **G4 polar capacity** — 2×2, Kreĭn–Langer Hadamard/Weyl; possibly a block of 1 (check first).
4. **G3 L′♯ by Fredholm + finite** — reduces to 1 once a relative compactness is proved.
5. **G16 Lemma F** — conditional on the descent to the quotient (G16.0); cheaply falsifiable.
6. G8 (S)/Arch ≥ Near, G5 block Schur — transfers with structure (Toeplitz/Schoenberg) but hypothesis = sign.
7. G2, G1, G7, G9, G12, G13 — transfers.
8. G6, G11, G15, G17 and the NOs of G14 — closed by theorem or falsifier.

### (4) Honest count

Out of **90 route entries** (101 lines − 8 non-routes, unifying 110–112):

| | entries |
|---|---|
| dismissal by **theorem/falsifier** written in the entry (T) | 45 |
| dismissal **by judgment only** (J) | **38** |
| mixed (T+J) or citing an already-reviewed R | 7 |
| — of the J entries: correct transfers (judgment replaceable by an existing theorem) | 31 |
| — of the J entries: **YES** (G10: 142, 347, 367, 380; G14: 209; G4: 560-Kreĭn by reference; G16: 521(f)) | 7 |
| TRAT = NO | 31 |
| TRAT = TRANSFER | 46 |
| TRAT = YES (includes conditional YES and tool) | 13 |

(The YES entries add up to 13 because 507, 450, 523, 588-rewritten, 536-N3-via-R13, and 06_ l.181 count as derived
YES entries even though their dismissal was T or a citation.)

Reading: **42%** (38/90) of the README's REF-D entries were filed by judgment. In 82% of those judgments (31/38) the
verdict was correct and is replaceable by a corpus theorem (thm:Z/thm:O, lem:shape-est, lem:shape-ident, Φ.1, C-pos,
INVENT Thm 2.3). The method error is concentrated in **seven entries, three objects**: exact induction by contacts
(G10, which the index itself left ADMISSIBLE and then retracted over the word «REF-D»), polar capacity in T (G4), and
spectral flow (G14, which is the tool both were missing).

## 6. Risks and filters for the next round (mandatory)

- **Index rule:** G10 appears in the index (l.142, 345–349, 367, 380) and R13 in 06_ l.181. The new reason written to
  retry is: (a) the death by (γ) used the doubly exponential scale withdrawn in the 10/15 correction; (b) the class of
  methods changes — from «estimate of the step» to «continuation by crossing forms (Robbin–Salamon) + rank-one border
  (Cauchy)», which no barrier (thm:shape, Φ200, M200, C-pos, W-*) covers, because all of them concern uniform deductions
  or pointwise first-order discriminants, not continuation arguments from a certified boundary.
- **lem:transfer:** the no-crossing step must fail for F_DH (T≈9/5) and Epstein (T≥1.59). The next round declares which
  feature of Λ(n_j) prevents it (candidate: the coincidence of the contact block in the 2T_j phase shift, gap (θ)).
- **lem:monoT:** λ_A nonincreasing in T; the crossing form cannot win by monotonicity of the carrier; it must win by the
  boundary data.
- **Uniformity in T:** nothing guarantees that no-crossing can be proved without certified enclosures interval by
  interval; if so, the route gives D only up to a finite T, not D. This is not a NO-GO; it is the main risk.
- **G16:** do not launch without G16.0 (descent to the quotient).

## 7. Proposed index entry (for the coordinator to copy; this memo does not edit the README)

- **TRACT_D_README_001 (phase 204, part D):** full sweep of the 101 REF-D/branch-2/reformulation lines in the README
  (90 entries, 17 groups). TRAT: NO 31, TRANSFER 46, YES 13 in three objects: G10 exact induction by contacts / (L2)
  (l.142, 347, 367, 380 — ADMISSIBLE OPEN retracted only over the label), G4 polar capacity 𝔊_T = D_pol − M(0) in T, G14
  crossing forms (Robbin–Salamon) as a tool for both; G16 Lemma F downgraded to weak conditional YES by AUDIT_200_AMU
  (l.523). 38/90 dismissals by judgment, 31 of them correct transfers. Stronger than D with their own path: L′♯ by
  Fredholm + finite block and quantitative no-crossing; both reduce to G10. Row D OPEN.
