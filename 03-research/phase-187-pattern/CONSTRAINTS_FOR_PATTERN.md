# CONSTRAINTS_FOR_PATTERN — corpus constraints on any pattern T ↦ λ_A(T) and on the per-window observables

Phase 187 (pattern over ~100 windows). Row D independent
objective; positivity assumed; honest labels. This document is independent of the dataset
(`DATA_100_WINDOWS.csv`, in progress, not touched): it collects EVERYTHING the corpus already imposes on a candidate
pattern, with a label and source per row, so that pattern extraction does not violate anything proved. Normalization: λ_A(T) = bottom of
𝔞_T on 𝒫_T (primitive form, Paper 46 def); λ_W = full form on L²(I_T); λ_P = class K′. Always
λ_W ≤ λ_P ≤ λ_A (Paper 46 thm:A, rem:Kprim). T* := 2πe^{2T}; N(T*) := #{γ ≤ T*} (Riemann–von Mangoldt, real zeros,
CITED); N_Sh := 2T·|{σ_T<0}|/π (Shannon number of the negative set of the symbol).

Main sources: `04-papers/46-row-d-dual-certificates/main.tex` (P46), `04-papers/48-row-d-route-map/main.tex` (P48),
`03-research/phase-165-critical-interlacing/R165_202_NODE_FLOW.md`, `03-research/phase-163-integrality-defect/R163_901_INTEGER_ZERO_CONFIGS.md`,
`03-research/phase-162-row-d-first-contact-closure/grid/R162_2300_MASTER_GRID.md` (grid), `03-research/phase-186-*/R186_{022,023,028,034,036,039,040,103,110,112}*.md`,
`03-research/phase-155-row-d-flat-kernel-criterion/R155_001_ROUND1.md`, `03-research/phase-183-*/R183_030_*.md`,
`00-references/arxiv-math-nt-2026-review/2608.24827v2.txt` (Zhu).

## 1. Quantitative constraints on T ↦ λ_A(T)

| # | Constraint (exact form) | Label | Source |
|---|---|---|---|
| 1.1 | **Monotonicity.** T ↦ λ_A(T), λ_P(T), λ_W(T) are non-increasing on (0,∞), including the thresholds T = ½log n where a contact enters (zero extension: 𝒫_T ⊂ 𝒫_{T′} isometrically with the same form values). Every pattern must be non-increasing; a fit with λ_A(T₂) > λ_A(T₁), T₂ > T₁, is excluded. | PROVED | P46 lem:monoT; R186_036 Lemma 1(d) (trivial transport λ_A(T) ≥ λ_A(T′)) |
| 1.2 | **Monotonicity with fixed contacts.** With 𝒩_T fixed, Λ_T non-decreasing and λ_P non-increasing. | PROVED | P46 cor:mono |
| 1.3 | **Continuity.** T ↦ λ_A(T) continuous on (0,∞); modulus of continuity of order C/log(1/h) (unitary rescaling F(t)=T^{−1/2}f(t/T); uses only lem:mbounds). No jumps at the thresholds ½log n: a piecewise pattern with a discontinuity is excluded; a "kink" (slope change) is admissible. | PROVED | P46 lem:contA; R165_202 §1.3; R162_407 §2 (rate) |
| 1.4 | **Explicit upper bound (decaying margin).** For T>0, k≥5, Y = Tγ₁/√2, ε_k(Y)<½: λ_W ≤ λ_P ≤ λ_A ≤ 𝓑(T,k) = 2·1.0012·T²(k/T)^{2k}[Σ_p(21)+e^TΣ_p(H_PT)] / ((14.13⁴T/64)(½−ε_k(Y))), p = 2k−8. Consequence: limsup λ_A ≤ 0. | PROVED | P46 thm:margin, eq:Bmargin, lem:zerosum, lem:testfam |
| 1.5 | **Closed form.** For T ≥ 1: λ_A(T) ≤ 4·10⁹·T·e^{−15.449T}. Every pattern must lie below this for T ≥ 1. | PROVED | P46 cor:margin1 eq:closedmargin |
| 1.6 | **Theorem M (b): double-exponential decay.** ∀ε>0 ∃T₀(ε): T ≥ T₀ ⇒ λ_A(T) ≤ exp(−e^{(2−ε)T}). Hence −log λ_A(T) ≥ e^{(2−ε)T} asymptotically: a pattern with −log λ_A polynomial or simple-exponential in T is excluded for large T. T₀(ε) is not explicit: do not use as a quantitative test in the dataset range without the constant. | PROVED in the record (not refereed) | P48 thm:M(b), App. index; grid §3 W2 |
| 1.7 | **Upper bound at small T.** λ_A ≤ C₀ + 𝖠 + φ((3π/2T)²): 1.291 at ½log3, 2.327 at log 2. | PROVED | P46 cor:mono |
| 1.8 | **Certified values (lower bounds).** λ_A(½log3) ≥ λ_P ≥ 8.8577·10⁻⁵ (dual certificate, interval arithmetic). λ_A(T) ≥ 2.5·10⁻¹² for 0 < T ≤ ½log5 (even sector ≥ 2.5e-12, odd ≥ 3.0e-10). λ_W(T) ≥ 10⁻¹⁸ for T ≤ ½log5 (even ≥ 1e-18, odd ≥ 1e-16). | PROVED (computer-verified, ball arithmetic) | P46 thm:C, thm:log5A, thm:log5W, App. encl/encllog5 |
| 1.9 | **Reference numerical values (variational upper bounds, Galerkin–Legendre).** λ_A(½log3) = 9.49·10⁻⁴ (P46: 9.45e-4); λ_A(½log5) = 3.86·10⁻¹² (1−β₁ = 1.73e-11); λ_A(0.62) ↔ 1−β₁ = 7.6e-5; log 2 ↔ 4.2e-7; 0.75 ↔ 3.5e-9; λ_A(0.9) ≈ 5.8·10⁻¹⁷ (1−β₁ = 1.71e-16, mpmath dps 40); λ_A(1.0) ≤ 4.2·10⁻²³ (Galerkin does not converge on the first two eigenvalues at T=1: upper bound ONLY). Note: 1−β₁ = λ_A/Pos(h*), not λ_A. | NUMERICAL | R186_039 §2.4; R186_040 §1.1, §5; R186_028 script |
| 1.10 | **Zhu bounds (full form, even tests).** λ_W(0.5) ≤ 1.05e-6, λ_W(0.8) ≤ 2.27e-17, …, λ_W(2.0) ≤ 3.19e-283 (Table 3, certified). λ_W ≥ 0 for T ≤ 0.8 (Zhu Thm 1.2, cor:KEP08). Ratio λ_A/λ_W at ½log5 ∈ [1.7e5, 3.9e6] = e^{12…15}: it is **not** subexponential against the total exponent (26–41). A pattern for λ_A does not transfer to λ_W (nor vice versa) without modeling the polar term. | CITED (Zhu) / NUMERICAL (ratio) | Zhu 2608.24827 Table 3, Thm 1.2; P46 cor:KEP08; R186_112 MAJOR-3; R186_028 Lemma 1.1 |
| 1.11 | **Fold at boundaries (exact form).** Under (REG) (c_{F_T} ∈ C¹ near the comb points), d/dT λ_A = −𝒱_T(F_T)/T with 𝒱_T(F) = (1/2π)∫τm′(τ)|F̂|² − Σ_{log n<2T} v_n log n·Re c_F′(log n) + 𝒯_T(F), 𝒯_T = −2T·Re[ȦB̄ + A·conj(Ḃ)]. At the activation instant log n = 2T the comb enters via c_F′(2T⁻) = −F(T)·conj(F(−T)) (F continuous up to ±T), which vanishes if F vanishes at the boundary. Monotonicity ⇒ 𝒱_T(F_T) ≥ 0 where λ′ exists. | PROVED under (REG); (REG) OPEN | R165_202 §1.4; R162_407 (3.1); R186_036 §4 Lemma 2 (CONDITIONAL) |
| 1.12 | **Sign of the fold by parity.** For even F: F(T)·conj(F(−T)) = |F(T)|² ≥ 0 ⇒ c_F′(2T⁻) ≤ 0; for odd F: = −|F(T)|² ⇒ c_F′(2T⁻) ≥ 0. Contribution to the fold at the activation of n: −v_n log n·Re c_F′(2T⁻) = +v_n log n|F(T)|² (even) / −v_n log n|F(T)|² (odd), with v_n > 0. The λ_A minimizer is even throughout the computed range (1.14), so the observable fold at each ½log n is that of the even sector. This is an algebraic consequence of 1.11; there is no separate theorem. | PROVED under (REG) (direct consequence) | R165_202 §1.4; R186_040 §1.2(a) (parity of the minimizer) |
| 1.13 | **Sectors.** λ_A = min_even λ_min(A_T\|𝒫_T^even); λ_W = min_even λ^W_{T,even}; the sum by parity is orthogonal for L², 𝔞_T and W_T. A pattern must admit two branches (even/odd) and λ_A is the minimum of both; branch crossings are admissible kinks. | PROVED | P46 thm:parityschur(o); R186_028 Lemma 1.1 |
| 1.14 | **Even minimizer; index one.** The λ_A minimizer is even in all computed windows (parity +1.000 at 0.45, ½log3, ½log5, 0.90). n₋(𝔞_T\|L²(I_T)) = 1 for 0.12 ≤ T ≤ ½log5, even negative direction, caused by the pole (not by the primes). | NUMERICAL (parity) / PROVED mod. CITED (index) | R186_103 table; R186_028 Thm 1.4, Thm 1.2 |
| 1.15 | **Finite negative band.** {σ_T<0} is a finite union of bounded intervals, the first one containing 0; τ_last ≤ τ^lo(𝖠) with τ^lo > 2πe^{𝖠}, 𝖠 = Σ_{𝒩_T}v_n ~ 4e^T. Neg_T is trace class; λ_A ≥ −tr Neg_T = −(2T/2π)∫σ₋. The band does **not** decide the sign (prop:negtrace(v)). | PROVED | P46 prop:band, prop:negtrace; R186_112 §2.3 |
| 1.16 | **No log-convexity.** Log-convexity of λ_A in T is a NO-GO (no theorem or evidence); do not impose or assume convexity of −log λ_A. | NO-GO (as a lemma) | R186_033; grid §8 entry 28 |

## 2. Constraints on the per-window observables

| # | Observable and constraint | Label | Source |
|---|---|---|---|
| 2.1 | **Count of nearly balanced directions** K_δ(T) := #{j : 1−β_j < δ} of the pencil Neg_T u = β Pos_T u on 𝒫_T. Robust datum: K_δ = N(T*) + c, c ∈ {−1,0,+1} for δ ∈ [10⁻⁴,10⁻²]; K_{e⁻¹} = N(T*) + 2…3. Table: T = 0.62, log2, 0.75, ½log5, 0.9, 1.0 → N(T*) = 2,3,3,4,6,8; K₃ = 1,2,3,4,6,9. "K₃ = N(T*) exactly" is an artifact of the 10⁻³ threshold. It **never** follows N_Sh or the #negative components (at T=1: 24 and 44 against 8–11). | NUMERICAL (robust to ±1) | R186_039 §2.4; R186_112 §3 (MAJOR-1); R186_040 §1.1 |
| 2.2 | **N_Sh vs N(T*).** N_Sh/N(T*) ∈ [1.6, 2.5] in the range; N_Sh ≈ 2N(T*)+O(1). N_Sh = 1.6, 2.0, 2.4, 4.6, 5.1, 6.6, 7.05 (up to ½log5), 13.94 (0.9), 24.08 (1.0). Head bound J(T) ≤ 2N_Sh + O(log N_Sh): ARGUED (Landau–Widom hypotheses not satisfied: α and the set depend on T). | NUMERICAL / ARGUED | R186_039 Lemma 2.1; R186_112 MAJOR-2, §3 |
| 2.3 | **Head vanishing at low zeros.** u₁ satisfies \|û₁(γ_k)\|² ≤ 10⁻²⁰…10⁻²³ at γ_k ≤ T* (½log5), ≤ 2e-25 at T=0.9; direction j interpolates worse than j−1 by ~10⁴ per step and stops interpolating at j = K_e+1. Exact identity: 1−β_j = Σ_ρ Φ_{u_j}(ρ)Φ_{u_j}(1−ρ)/Pos(u_j) (lem:roughEF). | NUMERICAL (identity PROVED) | R186_040 §0.1, §2.1, §2.3; P46 lem:roughEF |
| 2.4 | **Sign mass in (T*, ∞).** At ½log5: zeros ≤ T* contribute 10⁻⁶ of 𝔞_T(u₁); 91% of γ ∈ (T*, 319], 9% tail. Geometric side: 𝔞_[0,T*] = −3.613e-9, 𝔞_[T*,τ_last] = +3.615e-9, 𝔞_far = +1.52e-12 (cancellation to three digits; 𝔞_far = 40% of the total at ½log5, 15% at 0.9). What is called "mass in (T*,10T*)" in the objective is the band (T*, τ_last] with τ_last ≍ 2πe^{𝖠}; there is no "10T*" statement in the corpus. | NUMERICAL | R186_040 §0.2–0.3, §2.3 |
| 2.5 | **Ladder** −log(1−β_j) (deep steps): 5.38/5.78 (½log5), 5.78/6.45 (0.9), 6.05/6.97 (1.0); growing with T. Refuted as a law: π²/log N_Sh (5.05, 3.75, 3.10: opposite trend), 2π²/log N(T*) (14, 11, 9.5), Slepian one interval (fits the first step to 1–5%, fails the second). "Steps ≈ 14" (Zhu's 2π² constant) refuted for λ_A. No law proved or fitted. | NUMERICAL (no law) | R186_040 §3.2, §5; R186_039 §2.4 |
| 2.6 | **Alternating parity of the head.** u₁ even, u₂ odd, u₃ even, … in all windows (at T=1 the order of the first two, degenerate at 10⁻²², is swapped). Commutation with reflection t ↦ −t: PROVED; the strict alternation: NUMERICAL. | PROVED (commutation) / NUMERICAL (alternation) | R186_040 §1.2(a) |
| 2.7 | **Peak of the minimizer** h* (frequency of the maximum of \|ĥ*\|²): 10.20 (T=0.36), 8.22 (0.45), 7.53 (½log3), 6.90 (½log5), 6.68 (0.90), 6.30 (1.0); peak·T NOT constant: 3.67 → 6.30. For T ≥ 0.85 the peak moves ±0.3 (baseline noise; the "peak" is a plateau ±0.5). The archimedean mode h_a does follow ≈ 3.7/T. Distinct objects (s₀, h*, h_a) with overlap ≥ 0.95 only up to ½log3. | NUMERICAL (valid up to 0.8; ±0.3 beyond) | R186_023 table, §obs; R186_022; R186_103 §12, §36 |
| 2.8 | **Index and pole.** n₋(𝔞_T\|L²) = n₋(𝔞_T\|𝒬_ev) + [𝔤_ev<2] + n₋(𝔞_T\|𝒬_odd) + [𝔤_odd<−2]; in the certified range = 1. n₋(Γ\|𝒫_T) = 0,0,0,1,1,1,2 (no sign of D). n₋(𝔞_T\|𝒫_T) = 0 in all computed windows (consistent with thm:log5A). | PROVED / NUMERICAL | R186_028 Thm 1.2, 1.4, §4.1; R186_039 §0 |
| 2.9 | **TK ceiling (lattice class).** Every dual certificate in the lattice class L(T,2T/M,U) with value c satisfies c ≤ Q(τ₀,φ,β) = local average of σ_T+β₀ĝ₀+β₁ĝ₁ against every test kernel φ of order M: a class-dependent upper bound on what a certificate can achieve (not on λ_A). | PROVED | R155_001 Theorem TK; R155_006 §species |
| 2.10 | **Archimedean inertia.** On the primitives n₋(W_∞) becomes 1 at T₁ = 0.5967 and 2 at T₂ = 0.8039; the full archimedean form is negative from T = 0.4608; prime 3 is needed from 0.567. | NUMERICAL / PROVED (archneg) | R183_030 §4; P46 prop:archneg |
| 2.11 | **Contact alignment** (𝒩_T = {2,3}): every τ > τ_a = 23.34 with σ(τ)<0 satisfies \|k log3 − l log2\| < 0.4479 (0.639 < 2^l/3^k < 1.565). The distant negative components lie in Diophantine alignment arcs; do not extrapolate the negative band as "random." | PROVED | P46 prop:align |

## 3. Logical constraints on extrapolation

**3.1 Non-identifiability from a finite range (Thm F + Theorem 3). PROVED mod. CITED.**
*Theorem F* (R163_901): for every N₀ there exists f_t = ζ + t·g (g a quasicrystal of frequencies m/√M, m > R) with: a completed
functional equation of ζ, exact (Λ_t(s) = Λ_t(1−s), Λ_t + 1/s + 1/(1−s) entire of order 1), pole, real coefficients, atomic
prime side on a discrete semigroup, **W^{f_t}_T = W^ζ_T for T ≤ T₁ := ½log λ₁** (λ₁ = m₁/√M ∉ ℤ), and for large |t| a zero
off the line and a finite first contact T_c(f_t) ≤ ½log λ₁ + ε. *Theorem 3* (R186_036, PROVED mod. Thm F CITED):
(a) if J ⊂ (0,T₁) is bounded, no statement P about {λ_A(T′)}_{T′∈J} valid for ζ implies λ_A(T) ≥ 0 ∀T (f_t satisfies P
and has a witness); (b) if J is unbounded, P implies λ_A(T₀) ≥ 0 only through L := lim λ_A ≥ 0; (c) the qualitative
properties (monotonicity, continuity, Thm M) do not separate: M_m shares them with L^{M_m} < 0.
**Consequence for the pattern:** any rule T ↦ λ_A(T) fitted on windows T ≤ T_max coincides, as data, with that of
f_t (N₀ = e^{2T_max}); out of sample, f_t's law is λ_A^{f_t}(T) = λ_A^ζ(T) + θ|t|C(T) (R186_039 §3.1), of a sign decided
by the perturbation. Hence **no pattern extrapolated from finite-range data proves anything about the sign**; it can
only (i) describe, or (ii) propose a law that is later proved per window.

**3.2 What kind of pattern does escape: two-sided asymptotic laws (open box, R186_110 §4; R186_039 §1.2).** A
statement λ_A(T) = L(T)(1+o(1)) with explicit L > 0 (or λ_A ≥ L(T)(1−ε(T)), ε → 0) is strictly stronger than D, is not
refuted by f_t (J unbounded, and the perturbation of f_t changes the sign of the leading term beyond T₁), is not shared by M_m
(L^{M_m} < 0; Q_m ≍ −e^{2δT} from its contact, ARGUED), and no wall (W-lin, W-det, W-fam, BR) excludes it. Every admissible L
satisfies L(T) ≤ exp(−e^{(2−ε)T}) (1.6) and L(T) ≤ 4·10⁹Te^{−15.449T} at T ≥ 1 (1.5), is non-increasing (1.1) and continuous (1.3).
That "it is proved only by per-window certificates" is ARGUED, not a theorem (R186_110 §4.1). Declared writing defect:
W-fam is stated over statements but proved over proofs (R186_110 §4.4).

**3.3 M_m as a test of a candidate pattern (grid §4; R163_801 Thm 5; R186_036 Thm 3(c)).** M_m = ξ × rational factors of
m off-line quartets: it shares EF, the zero-side identity, the closed semi-bounded form, lem:contA, lem:monoT, Thm M,
first contact, witness, nodes, finZ; κ(M_m) = κ(ζ)+4m; L^{M_m} < 0. Its prime side is that of ζ plus a density
β_m(u) = Σ_{j≤m} 4cos(γ_ju)cosh(δ_ju)1_{|u|<2T} (non-atomic). **Rule:** if a candidate pattern/observable/law is also
satisfied by the family {λ_A^{M_m}(T)}, it says nothing about the sign for ζ (class blindness, W3/F3). Operative test: compute the
observable for M_m (m = 1, quartet at height γ₁ with small δ) on the same windows; if the pattern is reproduced, it is a
"class property," with no content for D. Likewise f_t for the prime side (3.1): the wall dichotomy requires that a
pattern with content not be shared by either of the two (grid §3 "Wall dichotomy," R166_190 §0).

**3.4 Walls bounding interpretation.** W2 (Theorem M: no margin/compactness/bootstrap > exp(−e^{2T}); average ⇏ per
window; T/log T ceiling per window), W-lin (linear certificates in a fixed basis do not decide new windows), W-det (no
determinant with leading term + O(1) multiplicative error decides the sign: D_B factors as λ_A·R), W-fam (3.1). A pattern
for λ_A extracted from data is, by construction, "leading term + O(1) relative error": it falls into W-det as soon as it is used
to decide the sign, not while it merely describes. Sources: grid §3; R186_034 Thm 3.1; R186_036; P48 thm:M.

## 4. Functional form of Zhu's Conjecture 12.1 and its free parameters

Text (CITED, 2608.24827v2 l. 1388–1392), for λ* = λ_W restricted to even tests, L = T: −ln λ*(L) = 2π²·N(T*)/ln N(T*)·(1+o(1)),
T* = 2πe^{2L}, N(T*) = e^{2L}(2L−1) + O(L). Remark 12.2: the data discriminate the *form* N/ln N; the constant 2π² "is read
off the plateau" (R₁ = −ln λ*/(2π²N/ln N) flat to 1.3%, 20.02–20.27 per zero) and **is not derived**. Thm 1.4 (barrier, unconditional):
every pointwise-envelope certificate requires T♯ > T₁(L) = 2πe^{𝖠_L}, 𝖠_L = (4+o(1))e^L; matrix size N ≍ L·T₁ doubly exponential;
sup of the comb = 𝖠_L exact (Lemma 3.2), a threshold that cannot be lowered within the class. Zhu §14.2: the asymptotic object is the smallest
singular value of PW_T's "low-zero sampling operator" at the zeros ≤ T*.
Free parameters of the family: (i) constant c in −ln λ = c·N(T*)/ln N(T*) (Zhu fixes c = 2π² by fitting); (ii) the form of the
denominator (ln N vs log N_Sh vs none); (iii) the o(1) term (no rate); (iv) which λ (λ_W vs λ_A: they differ by e^{12…15} at
½log5, MAJOR-3 of R186_112, so **the same c cannot serve both** unless the ratio is o(N/ln N), not proved);
(v) the cutoff T* (2πe^{2T} ↔ m(T*) = 2T, an intrinsic reading ARGUED in R186_040 §1.3). Status: CITED/NUMERICAL for λ_W (Zhu);
for λ_A it is CONDITIONAL[λ_A/λ_W subexponential in the exponent] and contradicted at ½log5 (R186_112). Local data: −ln λ_A(1.0)
≥ 51.5 against −ln λ_W(1.0) = 67 (Zhu).

## 5. "Patterned" observables already detected and their status

| Observable | Pattern | Status | Source |
|---|---|---|---|
| K_δ(T) (near-kernel of the pencil) | N(T*) + c, c ∈ {−1,0,1}; +1 per window | NUMERICAL (robust to ±1; 6 windows up to T=1, mp at 0.9/1.0) | R186_039 §2.4; R186_040 §1.1; R186_112 §3 |
| Parity of u_j | alternating even/odd | NUMERICAL (commutation PROVED) | R186_040 §1.2 |
| Ladder −log(1−β_j) | steps 5.4 → 7.0, increasing with T | NUMERICAL, no law (all candidates refuted) | R186_040 §3.2 |
| Vanishing at zeros ≤ T* | \|û_j(γ)\|² ≤ 10⁻⁶(1−β_j)Pos(u_j) | NUMERICAL (Lemma H′ OPEN formulated) | R186_040 §3.3 |
| Spectral mass of the head within {σ<0} | L_in ∈ [0.50, 0.75] (not exponentially concentrated) | NUMERICAL; "Slepian leak" NO-GO | R186_040 §0.4, §3.1 |
| Peak of h* | 10.2 → 6.3; peak·T 3.7 → 6.3 | NUMERICAL up to 0.8; ±0.3 beyond | R186_023; R186_103 |
| Peak of the archimedean mode h_a | ≈ 3.7/T up to T = 1.5 | NUMERICAL | R186_103 §36 |
| n₋(𝔞_T\|L²) | = 1, even, caused by the pole | PROVED mod. CITED (T ≤ ½log5) | R186_028 Thm 1.4 |
| n₋(Γ\|𝒫_T) | 0,0,0,1,1,1,2 (≈ 4T−2 on primitives in CC) | NUMERICAL | R186_028 §4.1; R183_026 |
| T* read in σ_T | m(T*) = 2T = rms of the comb; (1/2π)∫₀^{T*}m = leading term of N(T*) | ARGUED (elementary asymptotics) | R186_040 §1.3 |
| Cancellation of rank ≈ N_Sh of the negative set | 2.4/7.0 | NUMERICAL | R186_034 (grid §8 entry 28) |
| n₋(𝔞_T\|𝒫_T) ≤ 4/10 | bound by eigenvalues of Neg_T | PROVED (improves prop:NC) | R186_034 §3.3 |
| Cost of prime 2 in s₀ | maximum near T ≈ 0.45–0.50 | NUMERICAL (predictive conjecture withdrawn) | R186_022 |

## 6. Pattern validation protocol

1. **Prior admissibility (before fitting).** Every candidate law L(T) must be: non-increasing (1.1), continuous (1.3),
   ≤ 𝓑(T,k) with k chosen per window (1.4), ≤ 4·10⁹Te^{−15.449T} at T ≥ 1 (1.5), ≥ certified bounds where they exist (1.8:
   L(½log3) ≥ 8.86e-5 if it aims to be a lower bound; if it is a two-sided fit it must pass through [8.86e-5, 9.5e-4] at ½log3 and
   [2.5e-12, 3.9e-12] at ½log5). Report at which T the law violates thm:margin if it does. Do not impose convexity (1.16).
2. **Fit on a subset.** Fit only on windows with T ≤ T_fit (e.g., 60% of the range); fix the functional form
   before seeing the held-out ones; record the number of free parameters (see §4: c, denominator, o(1), T*, λ_A vs λ_W).
3. **Out-of-sample prediction.** Predict λ_A and K_δ, parity, peak on the held-out windows (T > T_fit); Zhu's
   criterion (Table 3, test 1.2 → 1.4–2.0 which rejected "one nat per zero"): a law that does not predict the exponent with relative error
   decreasing in T is not two-sided. Report relative error in −log λ_A, not in λ_A.
4. **Test against f_t (3.1).** For the fitted law with T_fit, construct N₀ = e^{2T_fit} and explicitly state: "f_t with
   this N₀ satisfies the same fit; the extrapolation is not a statement about ζ." If the law claims content, it must be
   two-sided (3.2) and validation is only by per-window certificate (1.8) or by a proved lemma (Lemma H′ OPEN).
5. **Test against M_m (3.3).** Recompute the §2 observables (K_δ, parity, peak, ladder) for M_m (m = 1, γ₁, small δ)
   in ≥ 5 windows with the same script (r034_det/r040_head). Any observable that M_m reproduces is labeled
   "class property" and enters no claim about the sign. Likewise with the f_t tail if implemented.
6. **Test against thm:margin and Thm M.** Evaluate 𝓑(T,k) (eq:Bmargin) in every window of the dataset and check λ_A^{num} ≤ 𝓑;
   check that −log L(T) grows at least as e^{(2−ε)T} for large T (1.6) or declare the law pre-asymptotic (R186_039
   §0.(b): no candidate law fits on [0.36, ½log5]).
7. **Precision.** 1−β_j < 10⁻⁹ is at the limit of Cholesky in double precision; for T ≥ 0.85 use mpmath (dps ≥ 40, M ≥ 56) or
   label it a variational upper bound (R186_040 §5; R186_034). The peak of h* has an intrinsic ±0.3–0.5 spread (2.7).
8. **Labels.** Every fit result is NUMERICAL; a proposed law is CONJECTURE/ARGUED; nothing in the dataset changes
   any symbol in the grid or touches the sign. Record results in grid §8 and in the crossword. No contact with the
   sign: D OPEN.
