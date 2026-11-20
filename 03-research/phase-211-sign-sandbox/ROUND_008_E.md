# Round 008 E — The margin law of λ_A against the prolate defect 1 − χ_0(2πN)

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Object: λ_A(T) = inf{a_T(F) : F ∈ P_T, ‖F‖ = 1}, with
P_T = {F ∈ L²(I_T) : A(F) = B(F) = 0}, A(F) = ⟨F, e^{t/2}⟩, B(F) = ⟨F, e^{−t/2}⟩, and a_T = W_T on P_T. Notation of
Paper 47 §sec:ext: λ = e^T, N = λ² = e^{2T}, c = 2πN (time·band of [−λ, λ] × [−λ, λ] in the convention
ℱf(ξ) = ∫f(x)e^{−2πixξ}dx), χ_k(c) the prolate concentrations, ψ_k the prolate functions of [−λ, λ], E the summation
map Ef(x) = e^{x/2}Σ_{n≥1} f(ne^x) on I_T. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check

Searched: Paper 47 §sec:ext (def:ext, lem:ext-mob, thm:ext-half, prop:ext-gauge, lem:ext-ellbound, prob:ext-L,
prop:ext-consol, prop:ext-univ, thm:ext-margin, prop:ext-base, lem:ext-hf, the closing list "Scale"); phase 199
(PATTERN_001_FRONTIERS §2–3, MECH_001_MORI_STRUCTURE_ALL_T, AUDIT_199 (a)–(f), proof-L-sharp/TEST_CG_001); ROUTES-TRIED
-INDEX README rows P211-B, P211-2B, P211-7D, 05b row L106 (prolate clusters), AUDIT_ZENODO_FRONTIER B3; ROUND_001_B
Propositions 1.3–1.5, ROUND_002_B (Q₁ on the prolate sector), ROUND_007_D (data, law, Lemma 4.6, Cor. 4.7).

What is known about the margin law (before this memo).
- For the complete form λ_W (not λ_A): the model λ_W ≈ κ(μ)(1 − χ_4(2πμ)) ≈ κ·const·μ^{9/2}e^{−4πμ}, μ = N, κ ∈ [4.1, 5.4]
  on 7 ≤ μ ≤ 20 with a contact sawtooth (PATTERN_001 §2, NUMERICAL from Mori V Table 1); the upper half is CITED (Mori,
  test vectors = summation-map images of smoothed prolates, upper bound with zero data); the lower half is the
  conjecture κ-band (OPEN). AUDIT_199: L′ (with leak(f)) is NO-GO, the repair L′♯ = prob:ext-L (gauge-minimised ℓ) is
  OPEN; L′♯ ⇒ the weak band λ_W ≥ (κ/4)N^{−A_0−1}(1 − χ_0) (= thm:ext-margin, CONDITIONAL); consistency with the ceiling
  checked for A_0 ≥ 0. "Index 4" of χ_4 is read in PATTERN_001 as "four prolate directions absorbed"; no derivation of
  that index is recorded.
- For λ_A: ROUND_007_D fitted −ln λ_A = c₁e^{2T} + c₂T + c₃ with c₁ → 4π from above (NUMERICAL, W-pat class); it noted
  that the prefactor μ^{−c₂/2} ≈ μ^{10} differs from μ^{9/2}, without explanation. Lemma 4.6 / Cor. 4.7 (PROVED) reduce
  the lower half to μ₁(T) ≥ L(T).
- P211-2B: no sign statement on the prolate sector at orders log N and 1 (do not retry). P47 "Scale": the upper side
  is linear in the leakage on prolate blocks (Guo Thm 1.6, CLAIMED); a lower bound must be quadratic against the
  distance to the gauge.

What differs here. (i) The comparison is made for λ_A (the Tate-constrained form), against 1 − χ_0 itself, on all
resolved windows, with the polynomial exponent fitted at the fixed rate 4π; the record fitted c₁ free or treated λ_W.
(ii) The test-function side is computed: the summation-map images of prolates, their angle to the Galerkin minimiser,
and their Rayleigh quotients on P_T, which the record never computed for λ_A. (iii) An index count (how many prolate
directions the constraints of P_T and of admissibility absorb) is derived and tested; it predicts the polynomial
exponent. No equivalence of (★) with another statement is used; no zero data are used.

## 1. R(T) = λ_A/(1 − χ_0(2πN)) on the resolved windows (NUMERICAL)

### 1.1 The defect 1 − χ_k(c), computed exactly (not from the asymptotic)
1 − χ_k(c) is computed from Slepian's derivative identity ∂_c log χ_k = 2ψ_k(1)²/c (ψ_k unit in L²(−1, 1)), integrated
from c to ∞ by 20-node Gauss–Laguerre after s = c + x/2, with ψ_k(1;s) from the tridiagonal Legendre matrix of the
prolate operator, inverse iteration in c/2.3 + 40 digits (script in §6). Check: 1 − χ_0(2) = 0.11944 (Slepian's table
χ_0(2) = 0.88056); ratio to the asymptotic 4√π c^{1/2}e^{−2c} equal to 0.900, 0.954, 0.978, 0.989 at c = 5, 10, 20, 40,
i.e. 1 − 0.44/c, the known first correction −7/(16c). At the windows used here c = 2πN ∈ [18.8, 103]; the asymptotic is
1–2.5 % off, the exact value is used.

### 1.2 Data
44 windows: 35 converged 128-bit values of phase 187 (DATA_100_WINDOWS.csv, ½log3 ≤ T ≤ 1.075, relative error ≲ 1–3 %)
and 9 sine-Galerkin values of ROUND_007_D §1(c) at T = 1.0, …, 1.4 (largest N; upper bounds, 6–19 % high where tested).
Correction to the brief of this round: the value 5.7·10⁻⁶⁵ at T = 1.4 is the unconverged N = 120 value; the N = 180
value is 1.83·10⁻⁶⁹ (also an upper bound). Using 5.7·10⁻⁶⁵ puts T = 1.4 off every law by 4.5 digits; 1.83·10⁻⁶⁹ is used.

| T | N | λ_A | 1 − χ_0(2πN) | R = λ_A/(1−χ_0) | κ₈ = λ_A/(1−χ_8) |
|---|---|---|---|---|---|
| ½log3 | 3.00 | 9.46·10⁻⁴ | 1.27·10⁻¹⁵ | 7.4·10¹¹ | 0.74 |
| 0.61 | 3.39 | 3.55·10⁻⁵ | 1.05·10⁻¹⁷ | 3.4·10¹² | 0.96 |
| log 2 | 4.00 | 9.86·10⁻⁸ | 5.16·10⁻²¹ | 1.9·10¹³ | 1.05 |
| 0.76 | 4.57 | 3.29·10⁻¹⁰ | 4.17·10⁻²⁴ | 7.9·10¹³ | 1.22 |
| ½log5 | 5.00 | 3.18·10⁻¹² | 2.02·10⁻²⁶ | 1.6·10¹⁴ | 1.07 |
| 0.85 | 5.47 | 1.97·10⁻¹⁴ | 5.49·10⁻²⁹ | 3.6·10¹⁴ | 1.07 |
| 0.90 | 6.05 | 4.66·10⁻¹⁷ | 4.16·10⁻³² | 1.1·10¹⁵ | 1.36 |
| ½log7 | 7.00 | 1.05·10⁻²¹ | 2.92·10⁻³⁷ | 3.6·10¹⁵ | 1.21 |
| ½log8 | 8.00 | 1.35·10⁻²⁶ | 1.09·10⁻⁴² | 1.2·10¹⁶ | 1.31 |
| 1.075 | 8.59 | 1.88·10⁻²⁹ | 7.26·10⁻⁴⁶ | 2.6·10¹⁶ | 1.49 |
| 1.1 | 9.03 | 1.08·10⁻³¹ | 2.95·10⁻⁴⁸ | 3.6·10¹⁶ | 1.37 |
| 1.2 | 11.0 | 1.03·10⁻⁴¹ | 4.07·10⁻⁵⁹ | 2.5·10¹⁷ | 1.73 |
| 1.3 | 13.5 | 4.03·10⁻⁵⁴ | 2.16·10⁻⁷² | 1.9·10¹⁸ | 2.39 |
| 1.35 | 14.9 | 2.61·10⁻⁶¹ | 4.24·10⁻⁸⁰ | 6.2·10¹⁸ | 3.42 |
| 1.4 | 16.4 | 1.83·10⁻⁶⁹ | 1.29·10⁻⁸⁸ | 1.4·10¹⁹ | 3.45 |

### 1.3 Fit R = C·N^a (least squares in ln R)
| range | n | ln C | a | rms(ln R) |
|---|---|---|---|---|
| all, ½log3 ≤ T ≤ 1.4 | 44 | 17.15 | 9.62 | 0.13 |
| T ≤ 1.075 (128-bit only) | 37 | 17.11 | 9.65 | 0.13 |
| 0.8 ≤ T ≤ 1.4 | 30 | 17.36 | 9.51 | 0.10 |
| 1.0 ≤ T ≤ 1.4 | 16 | 16.89 | 9.71 | 0.10 |
Local exponents over consecutive blocks of four windows: 11.5, 10.5, 9.7, 10.0, 10.2, 7.7, 13.0, 6.0, 10.4, 9.6, 9.9 (the
scatter 6–13 between T = 0.9 and 1.08 is the contact region ½log7, ½log8 plus the 1–3 % data error over short ΔlnN).
So, NUMERICALLY, with the rate fixed at the prolate rate,
    λ_A(T) ≈ e^{17.1} N^{9.6} (1 − χ_0(2πN)) ≈ 1.0·10^{8}·N^{10.1}·e^{−4πN}       (½log3 ≤ T ≤ 1.4, rms 0.13 in ln),
stable in a to ±0.1 under change of range. This is the law of ROUND_007_D §5 rewritten: c₁ fitted free (12.59) absorbs
part of the polynomial; with c₁ = 4π fixed the polynomial exponent is ≈ 10, not the μ^{9/2} of λ_W.

### 1.4 Comparison with phase 199, and the index count
Phase 199 (PATTERN_001 §2): λ_W ≈ κ₄(1 − χ_4(2πμ)), κ₄ ∈ [4.1, 5.4] on 7 ≤ μ ≤ 20, so λ_W/(1 − χ_0) ≈ κ₄·(1−χ_4)/(1−χ_0)
≈ κ₄·(8⁴/4!)c⁴ ∝ N⁴. For λ_A the same comparison with higher prolate indices (exact 1 − χ_k):
- κ₆ := λ_A/(1 − χ_6) grows from 126 to 3.8·10⁴ (∝ N^{5.0}): index 6 is too low.
- κ₈ := λ_A/(1 − χ_8) ∈ [0.74, 1.62] on all 37 converged windows T ≤ 1.075 (mean 1.17), and 1.4–3.5 on the sine-Galerkin
  windows 1.1–1.4 (upper bounds). Fit κ₈ ∝ N^{0.6} (T ≤ 1.075), N^{0.9} (whole range); no contact jump above the data
  error. Index 8 is the right one; index 10 would make κ decay like N^{−1.4}.
Reading (NUMERICAL): λ_W ≈ κ₄(1 − χ_4), λ_A ≈ κ₈(1 − χ_8), κ₄ ≈ 4–5, κ₈ ≈ 1–3. The index of λ_W is 4 = 2·2 and that of
λ_A is 8 = 2·4: in the even sector (the bottom sector of both forms) the even prolates ψ_0, ψ_2, ψ_4, … are the
low-leakage directions, and each scalar linear constraint absorbs one of them. λ_W carries the two admissibility
constraints f(0) = ℱf(0) = 0 of the summation map (def:ext); λ_A carries those two plus the two Tate constraints A = B = 0
of P_T. Section 3 turns this count into a theorem for the upper half and Section 2 checks it on the test functions.

## 2. The test functions Eψ_k against the minimiser (NUMERICAL)

Setting. ψ_k = k-th prolate of [−λ, λ] at c = 2πN (ψ_k(u) = φ_k(u/λ), φ_k from the Legendre matrix in c/2.3 + 60
digits), restricted to [−λ, λ]; g_k := Eψ_k on I_T, integrated against the Dirichlet sines in multiprecision (composite
Gauss–Legendre of 40 nodes on panels ≤ 0.04 between the breakpoints T − log n, n ≤ N). The sine expansion captures
98.6–99.9 % of ‖g_k‖² (the rest is the endpoint value g_k(−T) ≠ 0 of a non-admissible ψ_k). u = Galerkin minimiser of
a_T on P_T (even sector, tools/galerkin_mp.py); P = orthogonal projector on P_T. All Ritz values below are Rayleigh
quotients of explicit vectors of the sine space intersected with P_T, hence upper bounds for the Galerkin λ_A.

### 2.1 The single test function Eψ_0
| T | N | λ_A^ev (Galerkin) | W_T(Eψ_0)/‖Eψ_0‖² | a_T(PEψ_0)/‖PEψ_0‖² | ‖PEψ_0‖/‖Eψ_0‖ | ∠(u, Eψ_0) | ∠(u, PEψ_0) |
|---|---|---|---|---|---|---|---|
| 0.8 | 90 | 5.97·10⁻¹² | 0.166 | 0.256 | 0.29 | 1.44 rad | 1.09 rad |
| 1.0 | 160 | 1.61·10⁻²³ | 0.137 | 0.167 | 0.30 | 1.47 rad | 1.23 rad |
| 1.2 | 180 | 1.03·10⁻⁴¹ | 0.116 | 0.159 | 0.30 | 1.49 rad | 1.31 rad |
So Eψ_0 is not a test function for the margin law: its quotient is O(1) (10⁻¹), not O(1 − χ_0), its projection to P_T
keeps only 30 % of its norm, and the angle to the minimiser is 63–75° and grows with T. Reason (ARGUED, matches the
data): ψ_0 is not admissible (ψ_0(0) ≠ 0, ℱψ_0(0) ≠ 0), so the summation-map identity of thm:ext-half does not apply;
Poisson gives Eψ_0 = (exterior part) + ½ℱψ_0(0)e^{−x/2} − ½ψ_0(0)e^{x/2}, and the orthogonal projection P removes the
span of e^{±x/2} in L²(I_T), which is not the same correction as removing those two terms, so the O(1) remainder of
the Tate terms survives. Eψ_0 is also not parity-adapted: its even part carries 50.3–50.8 % of its norm.

### 2.2 Ritz on P_T ∩ span{Eψ_0, Eψ_2, …, Eψ_{2m}}
| T | m (top index 2m) | dim | bottom | bottom/λ_A | ∠(u, span) | ∠(u, bottom vector) |
|---|---|---|---|---|---|---|
| 0.8 | 1 (ψ_2) | 2 | 0.108 | 1.8·10¹⁰ | 1.09 | 1.57 |
| 0.8 | 2 (ψ_4) | 3 | 3.6·10⁻⁴ | 6.1·10⁷ | 0.26 | 0.36 |
| 0.8 | 3 (ψ_6) | 4 | 3.6·10⁻⁴ | 6.1·10⁷ | 0.26 | 0.36 |
| 0.8 | 4 (ψ_8) | 5 | 9.24·10⁻¹² | 1.55 | 2.9·10⁻⁴ | 1.4·10⁻³ |
| 0.8 | 6 (ψ_12) | 7 | 7.95·10⁻¹² | 1.33 | 1.6·10⁻⁶ | 4.8·10⁻⁴ |
| 1.0 | 2 (ψ_4) | 3 | 1.1·10⁻⁴ | 7.0·10¹⁸ | 0.39 | 0.49 |
| 1.0 | 3 (ψ_6) | 4 | 1.1·10⁻⁴ | 7.0·10¹⁸ | 0.39 | 0.49 |
| 1.0 | 4 (ψ_8) | 5 | 2.40·10⁻²³ | 1.49 | 1.2·10⁻⁴ | 3.3·10⁻⁴ |
| 1.0 | 6 (ψ_12) | 7 | 2.26·10⁻²³ | 1.41 | 2.5·10⁻⁷ | 1.3·10⁻³ |
| 1.2 | 2 (ψ_4) | 3 | 5.9·10⁻⁵ | 5.7·10³⁶ | 0.48 | 0.58 |
| 1.2 | 3 (ψ_6) | 4 | 5.9·10⁻⁵ | 5.7·10³⁶ | 0.48 | 0.58 |
| 1.2 | 4 (ψ_8) | 5 | 1.73·10⁻⁴¹ | 1.69 | 1.1·10⁻⁴ | 2.3·10⁻⁴ |
| 1.2 | 6 (ψ_12) | 7 | 1.50·10⁻⁴¹ | 1.47 | 3.1·10⁻⁸ | 3.7·10⁻⁴ |
Readings (NUMERICAL).
(i) The minimiser of a_T on P_T lies, to angle 1–3·10⁻⁴ at every tested T, in the 3-dimensional space
P_T ∩ span{Eψ_0, …, Eψ_8}, and to angle 3·10⁻⁸–2·10⁻⁶ in P_T ∩ span{Eψ_0, …, Eψ_12}. The Ritz value on the five-prolate
block is 1.5–1.7 × λ_A, with the same doubly exponential size (10⁻¹², 10⁻²³, 10⁻⁴¹). This is a closed-form description of
the bottom of the form, from Λ-free archimedean data (prolates) plus one Λ-dependent map (E).
(ii) The drop happens exactly when ψ_8 enters, by 8, 19 and 36 orders of magnitude. Adding ψ_2 or ψ_6 changes nothing
(the Ritz values with top index 4 and 6 agree to all printed digits, and Eψ_2, Eψ_6 are orthogonal to u to 10⁻⁴):
the even sector of I_T sees only the prolates ψ_0, ψ_4, ψ_8, …, i.e. those with ℱ-eigenvalue +1 (ℱ(ψ_k1) = i^k√χ_k ψ_k
on the band, and Poisson summation intertwines t ↦ −t on I_T with f ↦ ℱf).
(iii) Index count in the even sector: three ℱ-even prolates ψ_0, ψ_4, ψ_8, two scalar constraints (the symmetric
admissibility condition f(0) + ℱf(0) = 0 and the even Tate condition A + B = 0), one survivor, whose leakage is
dominated by its ψ_8 component: λ_A ≈ κ₈(1 − χ_8). For λ_W only the admissibility constraint is present: two prolates
ψ_0, ψ_4, one survivor, λ_W ≈ κ₄(1 − χ_4), Mori's μ^{9/2}. Odd sector: ψ_2, ψ_6, ψ_10 with the antisymmetric conditions,
predicted λ_A^odd ≈ κ₁₀(1 − χ_10). Check (Galerkin λ_A^odd): κ₁₀^odd = λ_A^odd/(1 − χ_10) = 0.57, 0.79, 0.71, 0.87, 1.24 at
T = 0.8, 1.0, 1.1, 1.2, 1.3, against κ₈^ev = 1.22, 1.50, 1.37, 1.73, 2.39. The parity ratio λ_A^odd/λ_A^ev (180 → 2200)
is (κ₁₀/κ₈)·(1 − χ_10)/(1 − χ_8) with κ₁₀/κ₈ ≈ 0.5 throughout.
(iv) The gap λ_A/λ_W ≈ e^{14.7} at T = 1 measured in ROUND_007_D §3 is predicted by (κ₈/κ₄)(1 − χ_8)/(1 − χ_4) =
(1.5/4.6)·7.1·10⁶ = 2.3·10⁶ = e^{14.6}. The unexplained "μ^{10} against μ^{9/2}" of ROUND_007_D §5 is the index shift 4 → 8:
(1 − χ_8)/(1 − χ_4) ≍ c⁴.

## 3. The upper half: an exterior bound and the index count

Notation. 𝒞_T := {f : ℝ → ℝ even, C², supp f ⊂ [−λ, λ], f(λ) = f′(λ) = 0}; 𝒜⁺_T := {f ∈ 𝒞_T : f(0) = ℱf(0) = 0}
(admissible in the sense of def:ext, with the extra edge condition f′(λ) = 0). For f ∈ 𝒞_T put r := ℱf|_{(λ,∞)} and
    L₁(f)² := ∫_λ^∞ ξ²|r(ξ)|² dξ,    L₂(f)² := ∫_λ^∞ ξ⁴|r′(ξ)|² dξ
(the out-of-band energies of f′ and of (xf)″ up to 2π factors; finite since f ∈ C², f, f′ vanish at ±λ, so
r(ξ) = O(ξ^{−2}), r′(ξ) = O(ξ^{−2}) and ξ²r, ξ²r′ ∈ L² by Plancherel on f′ and (xf)″). The functionals A(F) = ⟨F, e^{t/2}⟩,
B(F) = ⟨F, e^{−t/2}⟩ on I_T are those of P_T (verified against the closed forms in tools/galerkin_mp.py: ⟨e_k, e^{t/2}⟩ =
T^{−1/2}e^{−T/2}a_k(1 − (−1)^k e^T)/(¼ + a_k²)). For g = Ef they read
    A(Ef) = Σ_{n<N} n^{−1}∫_{n/λ}^{λ} f(v)dv,    B(Ef) = Σ_{n<N} ∫_{n/λ}^{λ} f(v) dv/v,                              (3.0)
continuous linear functionals of f|_{[1/λ,λ]} (substitute v = ne^x).

**Theorem 3.1 (exterior upper bound; PROVED, given thm:ext-half).** There is an absolute constant K such that for every
T with N ≥ 2 and every f ∈ 𝒜⁺_T,
    W_T(Ef) ≤ K λ^{−2}(L₁(f)² + L₂(f)²).

*Proof.* By thm:ext-half, W_T(Ef) = 𝒲[Ψ], Ψ := Ψ̌_f 1_{(T,∞)}, Ψ̌(y) = e^{y/2}ρ(e^y), ρ(w) := Σ_{n≥1} r(nw) (w > λ;
absolutely convergent since r = O(ξ^{−2})). We bound the three terms of 𝒲 from above. Write ζ₃ := ζ(3/2).
(a) Tails. For X > 0, ‖r‖_{L²(X,∞)} ≤ X^{−1}‖ξr‖_{L²(X,∞)}. Since ‖r(n·)‖_{L²(W,∞)} = n^{−1/2}‖r‖_{L²(nW,∞)}, for W ≥ λ:
‖ρ‖_{L²(W,∞)} ≤ Σ_n n^{−1/2}(nW)^{−1}L₁ = ζ₃L₁/W. With w = e^y, ‖Ψ̌‖²_{L²(Y,∞)} = ∫_{e^Y}^∞|ρ(w)|²dw; hence
‖Ψ‖ ≤ ζ₃L₁/λ and ‖Ψ̌‖_{L²(T+u,∞)} ≤ ζ₃L₁e^{−u}/λ for u ≥ 0.
(b) Derivative. Ψ̌′(y) = ½Ψ̌(y) + e^{3y/2}ρ′(e^y), ρ′(w) = Σ_n n r′(nw), and ∫_λ^∞ w²|r′(nw)|²dw = n^{−3}∫_{nλ}^∞ξ²|r′|² ≤
n^{−3}(nλ)^{−2}L₂². So ‖e^{3y/2}ρ′(e^y)‖_{L²(T,∞)} = ‖wρ′(w)‖_{L²(λ,∞)} ≤ Σ_n n·n^{−5/2}λ^{−1}L₂ = ζ₃L₂/λ and
‖Ψ̌′‖_{L²(T,∞)} ≤ ζ₃(L₁/2 + L₂)/λ.
(c) Archimedean term. m(τ) ≤ log(2+|τ|) + C_∞ (C_∞ as in lem:ext-hf). Put J := Ψ̌(T⁺), e(y) := e^{−(y−T)}1_{y>T},
Ψ₁ := Ψ − Je. Ψ₁ is continuous, vanishes for y ≤ T, and lies in H¹(ℝ) with ‖Ψ₁‖ ≤ ‖Ψ‖ + |J|, ‖Ψ₁′‖ ≤ ‖Ψ̌′‖ + |J|.
Using |a+b|² ≤ 2|a|² + 2|b|², log(2+|τ|) ≤ 1 + τ², |ê(τ)|² = 1/(1+τ²) and Plancherel,
(1/2π)∫log(2+|τ|)|Ψ̂|² ≤ (|J|²/π)∫_ℝ log(2+|τ|)(1+τ²)^{−1}dτ + 2(‖Ψ₁‖² + ‖Ψ₁′‖²). The trace inequality
|J|² = −∫_T^∞(Ψ̌²)′ ≤ 2‖Ψ̌‖‖Ψ̌′‖ then bounds the archimedean term by K₁(‖Ψ‖² + ‖Ψ̌′‖²) + C_∞‖Ψ‖², K₁ absolute.
(d) Comb. |c_Ψ(u)| ≤ ‖Ψ‖‖Ψ̌‖_{L²(T+u,∞)} ≤ ζ₃²L₁²e^{−u}λ^{−2}, so |Σ_{n≥2}v_n c_Ψ(log n)| ≤ ζ₃²L₁²λ^{−2}Σ_n v_n n^{−1} =
2ζ₃²(−ζ′/ζ)(3/2) L₁²λ^{−2}.
(e) Rank-two term. ∫_T^∞Ψ̌(y)e^{y/2}dy = ∫_λ^∞ρ(w)dw and ∫_T^∞Ψ̌(y)e^{−y/2}dy = ∫_λ^∞ρ(w)w^{−1}dw; by Cauchy–Schwarz
∫_X^∞|r| ≤ X^{−1/2}L₁, so |∫_λ^∞ρ| ≤ Σ_n n^{−1}(nλ)^{−1/2}L₁ = ζ₃λ^{−1/2}L₁ and |∫_λ^∞ρ/w| ≤ ζ₃λ^{−3/2}L₁. Whatever the
orientation convention for A, B on the line (reflection swaps them and 𝒲 is reflection invariant), 2|A(Ψ)B(Ψ)| ≤
2ζ₃²L₁²λ^{−2}.
Adding (a)–(e): 𝒲[Ψ] ≤ Kλ^{−2}(L₁² + L₂²). ∎

**Corollary 3.2 (upper bound for λ_A from constrained exterior data; PROVED).** For every f ∈ 𝒜⁺_T with A(Ef) = B(Ef) = 0
and f|_{[1/λ,λ]} ≠ 0,
    λ_A(T) ≤ 4K (L₁(f)² + L₂(f)²)/‖f|_{[1/λ,λ]}‖².
*Proof.* Ef ∈ L²(I_T) is continuous and piecewise C² (at the breakpoints T − log n the term f(ne^x) leaves the support
with f(λ) = f′(λ) = 0), so Ef is in the form domain; A(Ef) = B(Ef) = 0 puts it in P_T, where a_T = W_T. lem:ext-mob gives
‖Ef‖ ≥ ‖f|_{[1/λ,λ]}‖/(2√N); combine with Theorem 3.1 and λ^{−2}·4N = 4. ∎

**Proposition 3.3 (index count; PROVED).** Let V ⊂ 𝒞_T be a linear space with V ∩ {f : f|_{[1/λ,λ]} = 0} = {0}.
(i) If dim V ≥ 5, then
    λ_A(T) ≤ 4K · max_{0≠f∈V} (L₁(f)² + L₂(f)²)/‖f|_{[1/λ,λ]}‖².
(ii) If dim V ≥ 3, the same bound holds for λ_W(T) := inf{W_T(g)/‖g‖² : g in the core}.
*Proof.* (i) The four functionals f(0), ℱf(0), A(Ef), B(Ef) are linear on V (the last two by (3.0)); their common
kernel in V has dimension ≥ 1; any nonzero f in it lies in 𝒜⁺_T with A(Ef) = B(Ef) = 0; apply Corollary 3.2 and bound
the quotient by its maximum over V. (ii) Same with the two functionals f(0), ℱf(0); then Ef is in the core
(lem:ext-mob: f ∈ C², f(λ) = 0, and Ef vanishes to second order at T; at −T, Ef(−T) = e^{−T/2}Σ_n f(n/λ) is the
Poisson tail, which is the only point where the core condition is not exact; replace "core" by the form-domain closure,
where W_T is continuous) and the quotient bound follows from Theorem 3.1 and lem:ext-mob as in Corollary 3.2. ∎

The count "5 for λ_A, 3 for λ_W" is the whole content of the indices 8 and 4: with V = span of edge-tapered even
prolates ψ_0, ψ_2, …, ψ_{2(d−1)} (dim d), the maximum in Proposition 3.3 is controlled by the largest leakage in V,
1 − χ_{2d−2}: d = 5 gives χ_8, d = 3 gives χ_4. (With the parity refinement of §2.2(iii) the same indices come from
{ψ_0, ψ_4, ψ_8} with two constraints, resp. {ψ_0, ψ_4} with one.)

**Lemma 3.4 (weighted prolate leakage on a tapered block; ARGUED, not proved).** Let η_λ be an even C² taper equal to 1
on [−λ + 1/λ, λ − 1/λ], vanishing with its first derivative at ±λ, with |η_λ^{(j)}| ≤ C_jλ^j, and V_d = span{η_λψ_0, …,
η_λψ_{2d−2}}. Then for d ≤ 5 and N ≥ 3
    max_{0≠f∈V_d} (L₁(f)² + L₂(f)²)/‖f|_{[1/λ,λ]}‖² ≤ C N^{b}(1 − χ_{2d−2}(2πN))
with absolute C, b.
Argument and what is missing. (1) Double orthogonality (CITED, Slepian–Pollak): the ψ_j1_{[−λ,λ]} are orthogonal on ℝ and
their transforms are orthogonal on the band, hence also off the band, so leak(Σa_jψ_j1) = Σ a_j²(1 − χ_j) exactly; the
maximum of the plain leakage over span{ψ_0, …, ψ_{2d−2}} is 1 − χ_{2d−2}. (2) The weights ξ², ξ⁴ in L₁, L₂ are
harmless only if the out-of-band mass sits at ξ = O(λ·poly(c)); for the untapered ψ_j1 it does not: the edge jump
ψ_j(λ) gives a 1/ξ tail and L₁ = ∞. The taper removes the jump; its cost is controlled by the edge values and
derivatives of ψ_j on [λ − 1/λ, λ], which by Slepian's identity ψ_j(λ)² ∝ c ∂_c log χ_j ≍ c(1 − χ_j) (CITED identity,
used in §1.1; asymptotic CITED) are of size poly(c)·(1 − χ_j)^{1/2}. (3) The denominator: prolates are bounded by
poly(c)·‖·‖ in sup norm, so ∫_{|u|<1/λ}|f|² = o(‖f‖²). A complete proof needs uniform (in j ≤ 8, c ≥ 6π) bounds for
φ_j^{(i)}(x), i ≤ 3, on 1 − 1/N ≤ x ≤ 1 relative to φ_j(1), and the out-of-band tail of the tapered product; this is
classical-looking archimedean analysis with no arithmetic in it, and it is not done here.

**Corollary 3.5 (the upper half of the margin law; CONDITIONAL on Lemma 3.4).**
    λ_A(T) ≤ C N^{b}(1 − χ_8(2πN)) ≤ C′N^{b+8}(1 − χ_0(2πN)),      λ_W(T) ≤ C N^{b}(1 − χ_4(2πN)),
using (1 − χ_k)/(1 − χ_0) ≍ (8^k/k!)c^k (Slepian–Fuchs, CITED; computed in §1.4). The λ_W statement is the shape of Mori's
cited upper bound, here with no zero data; the λ_A statement is new and matches the measured index (§1.4, §2.2).

What was asked and what happened. The upper half "with Eψ_0 projected to P_T as test function" is NO-GO (NUMERICAL,
§2.1: quotient 0.12–0.26, independent of the scale (1 − χ_0)); ARGUED reason in §2.1. The single prolate cannot satisfy
four constraints; the right test space is five-dimensional, and the minimiser itself lies in it to angle 10⁻⁴.
Theorem 3.1 and Proposition 3.3 are the PROVED part; the remaining input (Lemma 3.4) is archimedean only.

## 4. The lower half

**Conjecture 4.1 (margin law for λ_A; OPEN).** There are constants κ₋ > 0 and a ∈ ℝ such that for every T with N ≥ 3
    λ_A(T) ≥ κ₋ N^{a}(1 − χ_0(2πN)).
Sharp-index form (OPEN): λ_A(T) ≥ κ₋(1 − χ_8(2πN)), with the data giving κ₈ ∈ [0.74, 3.5] on ½log3 ≤ T ≤ 1.4 (§1.4), i.e.
the first form with a ≈ 9.6 (§1.3). Both forms contain (★) for every T; neither is weaker than (★) at any window, since
the margin is positive.

**Proposition 4.2 (the lower half from the leakage lemma; PROVED transfer, CONDITIONAL on prob:ext-L).** If (eq:ext-L)
holds with (κ, A_0), then λ_A(T) ≥ (κ/4)N^{−A_0−1}(1 − χ_0(2πN)) for every T with N ≥ 5, i.e. Conjecture 4.1 with
a = −A_0 − 1.
*Proof.* thm:ext-margin gives W_T(g) ≥ (κ/4)N^{−A_0−1}(1 − χ_0)‖g‖² on the core and, by density, on 𝒟_T; P_T ⊂ 𝒟_T and
a_T = W_T on P_T. ∎
So the exponent gap between what prob:ext-L delivers (a = −A_0 − 1 ≤ −1) and the measured a ≈ 9.6 is a polynomial factor
N^{10.6 + A_0}: the leakage lemma, if true, gives the right exponential rate e^{−4πN} with polynomial slack. Its weak
point is the leakage bound ℓ(g) ≥ (1 − χ_0)‖g‖²/(4N), which uses only the first prolate.

**Lemma 4.3 (index improvement of the leakage floor; PROVED, elementary).** Let H be a Hilbert space with orthonormal
system (ψ_j) and a positive diagonal form D = Σ d_j|⟨·, ψ_j⟩|² + (≥ d_q on the orthogonal complement), d_0 ≤ d_1 ≤ ….
Let C : H → ℂ^q be bounded with C restricted to H_< := span{ψ_0, …, ψ_{q−1}} invertible. Then for f ∈ ker C,
    D(f) ≥ d_q ‖f‖² / (1 + ‖(C|_{H_<})^{−1}‖²‖C‖²).
*Proof.* f = f_< + f_≥, C f_< = −C f_≥, so ‖f_<‖ ≤ ‖(C|_{H_<})^{−1}‖‖C‖‖f_≥‖ and D(f) ≥ d_q‖f_≥‖² ≥ d_q‖f‖²/(1 + …). ∎
Application (CONDITIONAL on a conditioning bound, OPEN). For g ∈ P_T the representatives f of g (lem:ext-mob) satisfy
ℱf(0) = 0, A(Ef) = 0, B(Ef) = 0, three L²-continuous constraints ((3.0); A, B depend on f|_{[1/λ,λ]} only and the gauge
𝒢_T does not move them). The fourth, f(0) = 0, is not L²-closed and is lost in the infimum over representatives (the
gauge-minimised leakage is an L² infimum). With D = leak (diagonal in the prolates by double orthogonality, d_j = 1 −
χ_j(2πN)) and q = 3 on the even prolates ψ_0, ψ_2, ψ_4, Lemma 4.3 gives
    ℓ(g) ≥ (1 − χ_6(2πN))‖g‖² / (4N(1 + κ_C(T)²)),
with κ_C(T) the conditioning of the 3×3 constraint matrix on span{ψ_0, ψ_2, ψ_4}. If κ_C(T) grows at most polynomially
in N (an archimedean-plus-summation-map statement with no sign in it; OPEN), prob:ext-L yields λ_A ≥ κ′N^{−A_0−1−b}(1 −
χ_6). This is two prolate indices short of the sharp form (index 8): the gauge costs exactly the f(0) constraint, i.e.
(1 − χ_8)/(1 − χ_6) ≍ c² (polynomial).

Why prolate structure might give the lower half (ARGUED; the reading of §2). prop:ext-consol(b) writes (eq:ext-L) in
the prolate basis as aᵀ𝔐a ≥ κN^{−A_0} inf_b (a+b)ᵀD(a+b), D = diag(1 − χ_k). §2.2 shows that the bottom of a_T on P_T
lives, to angle 10⁻⁴, in the 3-dimensional block P_T ∩ span{Eψ_0, …, Eψ_8}, and on that block the form is ≈ κ₈ × leakage
with κ₈ ≈ 1–3: so on the low block, (eq:ext-L) holds numerically with A_0 = 0 and κ ≈ 1. What is missing is the rest of
the space: (α) the intermediate prolate range 10 ≲ k ≲ 4N, where 1 − χ_k climbs from 10⁻³⁰ to O(1) and lem:ext-hf
(high-frequency coercivity) says nothing because its cutoff Ω_* is superpolynomial; (β) the coupling between the low
block and that range, which must be shown to be smaller than the geometric mean of the two diagonal scales. Two
prolate facts point in the right direction: the leakage is exactly diagonal (no cross terms between prolates), and the
summation map transports parity to the ℱ-eigenvalue (§2.2(ii)), so the coupling splits into two independent sectors
with interleaved indices (0, 4, 8, … | 2, 6, 10, …). Neither fact controls the off-diagonal entries of 𝔐 itself; that
control is prob:ext-L and it is not supplied here.

## 5. Falsifiers: the defect 𝒫_{Λ−w} destroys the law

For a weight w (comb (log n, w_n)), ROUND_001_B Proposition 1.3 (PROVED): W^w_T(Ef) − 𝒲^w[Ψ_f] = 𝒫_{Λ−w}[Ef] −
𝒫_{Λ−w}[Ψ_f], with 𝒲^w = 𝒲 + 𝒫_{Λ−w}; hence, with thm:ext-half,
    W^w_T(Ef) = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ef]                                                                                  (5.1)
(PROVED: the two 𝒫_{Λ−w}[Ψ_f] terms cancel). The first term is the Λ-exterior form, bounded by Theorem 3.1 by
Kλ^{−2}(L₁² + L₂²), i.e. ≍ (1 − χ_8) on the five-prolate block; the second is the comb defect on the window, of size
‖Λ−w‖·‖Ef‖² with no small factor.

**Proposition 5.1 (the law has zero robustness; PROVED).** Let F★ be a unit vector of P_T with a_T(F★) ≤ λ_A(T) + ε. For
every weight w, λ_A(T; w) ≤ λ_A(T) + ε + 𝒫_{Λ−w}[F★], and λ_A(T; w) ≥ λ_A(T) − ‖𝒫_{Λ−w}|_{P_T}‖. In particular, if
𝒫_{Λ−w}[F★] < −λ_A(T) − ε then λ_A(T; w) < 0, and for w = cΛ the law survives only for |1 − c|·|Π_T(F★)| ≤ λ_A(T) + ε.
*Proof.* a^w_T = a_T + 𝒫_{Λ−w} on P_T; evaluate at F★ and take the infimum. For w = cΛ, 𝒫_{Λ−w} = (1 − c)Π_T. ∎

Numerical size (NUMERICAL, the five-prolate block of §2.2, sine basis): on the Ritz bottom vector F_b of
P_T ∩ span{Eψ_0, …, Eψ_8}, Π_T(F_b) = Arch(F_b) = 0.0331 (T = 1) and 0.0152 (T = 1.2), equal to 10⁻²² resp. 10⁻⁴⁰
relative: the block vector is a near-exact balance of two O(10⁻²) quantities. Bottom of a^{cΛ}_T on the same 3-dimensional
block:
| c | 0.9 | 0.99 | 0.9999 | 1 | 1.0001 | 1.01 | 1.1 |
|---|---|---|---|---|---|---|---|
| T = 1.0 | −4.3·10⁻² | −3.9·10⁻³ | +1.1·10⁻⁶ | 2.4·10⁻²³ | −5.3·10⁻⁶ | −2.6·10⁻³ | −2.8·10⁻² |
| T = 1.2 | −5.8·10⁻² | −5.5·10⁻³ | −5.0·10⁻⁶ | 1.7·10⁻⁴¹ | −6.0·10⁻⁶ | −2.0·10⁻³ | −2.1·10⁻² |
The block bottom leaves the doubly exponential scale at first order in |1 − c| and is negative on both sides of c = 1
(the block contains directions where Π_T − Arch has either sign at O(10⁻²)), as the full-space values of ROUND_007_D §6
(−|1 − c|g(T)). So the margin law, with its prefactor κ₈(1 − χ_8), is a property of the exact comb only.

Falsifier test (BRIEF rule 4) for the pieces of this memo.
- Theorem 3.1 / Corollary 3.2 / Proposition 3.3 are upper bounds, not sign steps. For w ≠ Λ they fail as statements
  about W^w (by (5.1) the right side acquires 𝒫_{Λ−w}[Ef], O(‖Λ − w‖), so no doubly exponential upper bound follows):
  (a) cΛ: the extra term is (1 − c)Π_T(Ef); (b) a_P: 𝒫_{Λ1_{p<P}}[Ef], O(1); (c) Beurling systems: the summation map
  and thm:ext-half need Poisson summation over ℤ and Λ∗1 = log on ℕ (rem:ext-killing(ii)); for generalized integers there
  is no Poisson formula, so Theorem 3.1 has no analogue; (d) finite modification: 𝒫_{Λ−w} is a finite comb, O(1) on the
  block. The upper half is Λ-specific, as it must be (the falsifiers have negative bottoms, so any small positive upper
  bound would be true for them, but the doubly exponential smallness of the block value is not).
- Proposition 4.2 inherits prob:ext-L, which is recorded as having to fail for cΛ, c > 1 (P47 closing list
  "Ingredients"); Lemma 4.3 and its application are Λ-free and carry no sign (the conditioning κ_C(T) involves Λ only
  through E, which is Λ-free; A, B are archimedean). No sign step is claimed in this memo.

## 6. Reproducibility

tools/prolate_defect.py (prolates by inverse iteration on the Legendre tridiagonal; 1 − χ_0(c) by the Slepian
derivative identity), tools/prolate_defect_k.py (1 − χ_k), tools/prolate_eproj.py T N dps (sine coefficients of
Eψ_0, …, Eψ_12; output tools/cache/eproj_T*_N*.pkl; run from tools/), tools/prolate_anal.py T N dps (§2 tables),
tools/prolate_fals.py T N dps (§5 table). Galerkin matrices from the cache of tools/galerkin_mp.py (T = 0.8: N = 90,
40 digits; T = 1.0: N = 160, 40 digits; T = 1.2: N = 180, 80 digits).

## Result

PROVED piece + PIVOT. The margin law of λ_A is identified numerically as λ_A ≈ κ₈(1 − χ_8(2πN)) (index 8, against index 4
for λ_W), the bottom of the form is located in a three-dimensional prolate block, and the upper half is reduced, by a
proved exterior bound and a proved index count, to an archimedean prolate estimate.

### What was proved
- Theorem 3.1 (PROVED, given thm:ext-half): W_T(Ef) ≤ Kλ^{−2}(L₁² + L₂²) for f ∈ 𝒜⁺_T, with the weighted out-of-band
  energies L₁, L₂ and an absolute K.
- Corollary 3.2 and Proposition 3.3 (PROVED): λ_A is bounded by the worst weighted leakage over any 5-dimensional
  space of edge-regular even functions, λ_W over any 3-dimensional one (four, resp. two, linear constraints:
  f(0), ℱf(0), A(Ef), B(Ef)).
- Proposition 4.2 (PROVED transfer, CONDITIONAL on prob:ext-L): λ_A ≥ (κ/4)N^{−A_0−1}(1 − χ_0).
- Lemma 4.3 (PROVED, elementary): leakage floor on a constrained space is d_q/(1 + κ_C²); applied to P_T it gives index 6
  (the gauge removes the f(0) constraint), conditional on polynomial conditioning κ_C(T) (OPEN).
- Proposition 5.1 and identity (5.1) (PROVED): W^w_T(Ef) = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ef]; the law survives a weight change only
  below |1 − c||Π_T(F★)| ≤ λ_A.
- NUMERICAL: R = λ_A/(1 − χ_0) = e^{17.1±0.3}N^{9.6±0.1} on 44 windows ½log3 ≤ T ≤ 1.4 (rms 0.13 in ln R); κ₈ =
  λ_A/(1 − χ_8) ∈ [0.74, 1.62] on the 37 converged windows, ≤ 3.5 to T = 1.4; κ₁₀^odd ≈ 0.6–1.2; the minimiser lies in
  P_T ∩ span{Eψ_0, …, Eψ_8} to angle ≈ 10⁻⁴ (Ritz value 1.5–1.7 λ_A) and in P_T ∩ span{Eψ_0, …, Eψ_12} to angle 10⁻⁶–10⁻⁸
  at T = 0.8, 1.0, 1.2; only the ℱ-even prolates ψ_0, ψ_4, ψ_8 enter the even sector; the λ_A/λ_W gap e^{14.7} at T = 1
  is the index shift (prediction e^{14.6}).

### What failed and why
- The upper half with the single test function PEψ_0: NO-GO (NUMERICAL): quotient 0.12–0.26, angle to the minimiser
  63–75°. ψ_0 is not admissible and P_T removes the Tate exponentials orthogonally, not the Poisson terms; one prolate
  cannot meet four constraints.
- Lemma 3.4 (weighted leakage of tapered prolates ≤ CN^b(1 − χ_{2d−2})) is ARGUED, not proved; Corollary 3.5 (upper half
  with index 8) is therefore CONDITIONAL.
- The lower half: nothing beyond prob:ext-L; the index improvement stops at 6 because the gauge kills f(0) = 0, and
  the intermediate prolate range 10 ≲ k ≲ 4N is untouched by every available coercivity statement.
- The law has zero robustness under cΛ, a_P, finite modifications (first-order departure, both signs, on the block);
  any lower-half argument must see the weights at relative precision 1 − χ_8.

### Next concrete step
Prove Lemma 3.4 (pure prolate analysis: uniform edge bounds for φ_j^{(i)}, j ≤ 8, i ≤ 3, at x ∈ [1 − 1/N, 1]) to make
the index-8 upper half unconditional; in parallel, test prob:ext-L in its prolate form prop:ext-consol(b) on the two
sectors separately, with the low block {ψ_0, ψ_4, ψ_8} (even) / {ψ_2, ψ_6, ψ_10} (odd) Schur-eliminated and the
coupling to k ∈ [10, 4N] measured against √(d_k d_8), at T = 0.8–1.2 from the cached Galerkin data.
