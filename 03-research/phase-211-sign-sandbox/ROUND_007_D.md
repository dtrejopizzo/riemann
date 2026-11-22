# Round 7 D: the lower half of a two-sided law for λ_A(T)

Object: λ_A(T) = inf{a_T(F) : F ∈ P_T, ‖F‖ = 1} (STATEMENT_001). Target (★): λ_A(T) ≥ 0 for every T. This memo asks
what a law λ_A(T) = L(T)(1 + o(1)), L > 0 explicit, looks like on the resolved range, what its lower half
λ_A(T) ≥ L(T)(1 − o(1)) would need from the structure found in rounds 5–6, and whether the law distinguishes the true
comb from the falsifiers cΛ and a_3. Notation: λ_W(T) is the bottom of the complete form W_T on L²(I_T); λ_A^par,
λ_W^par the parity bottoms; 𝔤_par, h_par the polar capacity and its vector (Paper 46 thm:parityschur).

## 0. Corpus check

Searched: ROUTES-TRIED-INDEX (README, 04, 05b, 06) for "asymptotic law", "two-sided", "bilateral", "margin",
"15.449", "bar-fam", "frontier", "PATTERN", "W-pat"; phase 187 (PATTERN_REPORT, DATA_100_WINDOWS.csv); phase 199
(PATTERN_001_FRONTIERS, MECH_001_MORI_STRUCTURE_ALL_T); Paper 46 subsec:margin, rem:bar-fam, rem:moriceiling, the
open-problem list, thm:parityschur; ROUND_005_C/D/E, ROUND_006_A/B of this phase.

Recorded and not retried:
- R6 / R186-bilateral (06_OPEN_RESIDUES): lower half of the bilateral law, OPEN; dead sub-routes: Landau–Widom main term
  (NO-GO), L_Sh, the phase-187 pattern fit −ln λ_A ≈ 13.0e^{2T} − 24.6T − 18.7 (W-pat, NUMERICAL; P46 cor:pattern: a
  quartet model M₁ matches every observable and is negative), bounded-range families (W-fam, P46 thm:famblind).
- Phase 187 already fitted ten law families to 46 windows T ≤ 1.075 in 128-bit arithmetic (PATTERN_REPORT §1).
  Those values are reused here as data; the fit is not redone as a route.
- Phase 199 PATTERN_001 fitted λ_W (Mori's tables) to κμ^{9/2}e^{−4πμ}, μ = e^{2T}, with a contact sawtooth in κ.
- [margin] (06): the doubly exponential ceiling for λ_W must not be transferred to λ_A as a ceiling (λ_W ≤ λ_A has the
  wrong direction). It does transfer as a FLOOR; §4 uses only that direction.

What differs here, and why it avoids the recorded failures. (i) New data: λ_A at T = 1.1–1.4 in 40-digit arithmetic
(tools/galerkin_mp.py), beyond phase 187's converged range, and λ_A for the falsifiers cΛ (c = 0.9, 0.95, 1.05, 1.1) and
a_3 on the same grid, which phase 187 did not compute. (ii) The question is not "which law interpolates" (W-pat already
says no interpolation decides the sign) but the falsifier content: does a fitted law for Λ carry a sign change that
the falsifiers show and Λ does not, and at what scale. (iii) The structural part (§4) is a pair of exact inequalities
between λ_A and λ_W (min–max and the bordered secular equation), which turns the cited certified λ_W floors into
λ_A floors; this direction was not used in the record (the record only discusses, and forbids, the opposite one).
No equivalence of (★) with another statement is used anywhere below.

## 1. The resolved values of λ_A(T)

All values below are NUMERICAL unless marked. Galerkin values are upper bounds for the true infimum (up to the
quadrature error of the archimedean entries), never inputs to a proof.

(a) Certified lower bounds (PROVED in Paper 46, interval arithmetic; or CITED).
| window | bound | source | label |
|---|---|---|---|
| T = ½log3 | λ_A ≥ λ_P ≥ 8.8577·10⁻⁵ | P46 thm:C | PROVED (computer-assisted) |
| T ≤ ½log5 | λ_A ≥ 2.5·10⁻¹², λ_W ≥ 10⁻¹⁸ | P46 thm:log5A, thm:log5W | PROVED (computer-assisted) |
| T ≤ 17/16 | λ_W ≥ 2^{−49162} | Liu Thm B | CITED |
| T ≤ ½log12 | λ_W ≥ 2^{−1518} ≈ 10^{−457.0} | Mori VII | CITED (not audited) |
| T ≤ ½log15 | λ_W ≥ 2^{−2904} ≈ 10^{−874.2} | Mori VIII | CITED (computational part reproduced, AUDIT_ZENODO_FRONTIER) |
The λ_W rows are on the same normalisation as here (W_T = 𝔞_T + 2Re AB̄ on L²(I_T), AUDIT_ZENODO_FRONTIER §0). By
Proposition 4.1 below (λ_A ≥ λ_W, PROVED) and monotonicity in T (P46 lem:monoT), they are floors for λ_A:
λ_A(T) ≥ 2^{−1518} for T ≤ ½log12 and λ_A(T) ≥ 2^{−2904} for T ≤ ½log15 (CITED inputs, PROVED transfer). This corrects
the sentence of P46's open-problem list "beyond ½log5 no lower bound better than C₀ − A is known" to "no lower bound
proved within the paper": cited complete-form certificates give floors up to ½log15.

(b) Converged values, 128-bit arithmetic, T ≤ 1.075 (phase 187 DATA_100_WINDOWS.csv, 46 windows, relative error
≲ 1–3 %; reused as data). Selected rows: λ_A = 9.46·10⁻⁴ (½log3), 9.86·10⁻⁸ (log 2), 3.18·10⁻¹² (½log5),
4.66·10⁻¹⁷ (0.9), 1.05·10⁻²¹ (½log7), 1.35·10⁻²⁶ (½log8), 1.88·10⁻²⁹ (1.075).

(c) This phase, 40–80 digits (tools/galerkin_mp.py, Dirichlet sines, N modes). Cross-check against (b): at log 2,
1.114·10⁻⁷ (N = 80) vs 9.86·10⁻⁸; at 0.9, 6.03·10⁻¹⁷ (N = 80) vs 4.66·10⁻¹⁷. So the sine basis at N = 80 is 13–30 %
above the converged value at T ≤ 0.9, and the gap widens with T. Values at T ≥ 1 (both parities, bottom = even sector
at every T):

| T | N | λ_A^ev | λ_A^odd | N-stability |
|---|---|---|---|---|
| 1.0 | 90 / 120 | 1.96·10⁻²³ / 1.74·10⁻²³ | 1.03·10⁻²⁰ | ≈ 10 % between 90 and 120 |
| 1.05 | 150 | 2.24·10⁻²⁷ | 1.64·10⁻²⁴ | (phase 187 converged value at 1.0497: 1.96·10⁻²⁷) |
| 1.1 | 150 / 180 | 1.145·10⁻³¹ / 1.077·10⁻³¹ | 9.60·10⁻²⁹ | 6 % |
| 1.15 | 150 | 2.48·10⁻³⁶ | 2.68·10⁻³³ | — |
| 1.2 | 120 / 180 | 1.26·10⁻⁴¹ / 1.025·10⁻⁴¹ | 1.41·10⁻³⁸ | 19 % |
| 1.25 | 150 | 1.49·10⁻⁴⁷ | 2.74·10⁻⁴⁴ | — |
| 1.3 | 150 / 180 | 4.70·10⁻⁵⁴ / 4.03·10⁻⁵⁴ | 8.85·10⁻⁵¹ | 14 % |
| 1.35 | 150 | 2.61·10⁻⁶¹ | 7.04·10⁻⁵⁸ | — |
| 1.4 | 120 / 180 | 5.7·10⁻⁶⁵ / 1.83·10⁻⁶⁹ | 6.25·10⁻⁶⁶ | NOT converged at 120 (4.5 digits); at 180 unknown, take as upper bound |
(dps 60 for T ≤ 1.15, 80 for T ≥ 1.2.) At T ≥ 1.1 the N-dependence is 0.03–0.08 digits per 30 modes except at 1.4; for
the fits below the error in −log₁₀λ_A is ≤ 0.1 digit for T ≤ 1.35 and unknown (but one-sided: the true value is
smaller) at 1.4. The even sector is the bottom at every window; λ_A^odd/λ_A^ev grows from 10² (log 2) to 3·10³ (1.4).

## 2. Fits (NUMERICAL)

Data: the 35 converged phase-187 windows with ½log3 ≤ T ≤ 1.075, plus the seven 40–80-digit values T = 1.1, …, 1.4
(largest N). y := −ln λ_A. Residuals in decimal digits.

| family | fit range | parameters | rms in fit | residuals at T = 1.1, 1.15, …, 1.4 (out of sample when fit ≤ 1.08) |
|---|---|---|---|---|
| single: L = cT^a e^{−bT} (y = bT − a ln T + k) | ≤ 1.08 | b = 320, a = 166 | 0.25 | +0.9, +1.8, +3.3, +5.2, +7.6, +10.6, +14.4 |
| single | ≤ 1.41 | b = 485, a = 295 | 1.26 | systematic (−1.7 … +4.0) |
| double: y = c₁e^{2T} + c₂T + c₃ | ≤ 1.08 | c₁ = 12.99, c₂ = −24.8, c₃ = −18.5 | 0.04 | −0.04, −0.21, −0.21, −0.38, −0.50, −0.76, −0.89 |
| double | ≤ 1.25 | 12.71, −22.0, −19.4 | 0.05 | (in fit to 1.25) …, −0.27, −0.27 |
| double | ≤ 1.41 | 12.59, −20.6, −19.8 | 0.055 | +0.08, −0.03, +0.07, +0.01, +0.02, −0.09, −0.04 |
| free rate: y = a e^{βT} + d | ≤ 1.08 | a = 5.99, β = 2.44 | 0.055 | −0.1 … −3.6 |
| free rate | ≤ 1.41 | a = 7.72, β = 2.25 | 0.12 | ±0.2 |
Leave-one-out on the ≤ 1.08 range: c₁ ∈ [12.93, 13.04]; single-exponential b ∈ [315, 327]; free β ∈ [2.42, 2.46].

Reading (NUMERICAL).
(i) The singly exponential family is excluded: a law cT^a e^{−bT} fitted on T ≤ 1.08 misses λ_A(1.4) by 14 orders of
magnitude, and needs a ≈ 166–295, i.e. it is not a law but a local Taylor fit of a convex y.
(ii) The doubly exponential family with rate 2 is the only one that is stable: the extrapolation error from ≤ 1.08 to
1.4 is 0.9 digit out of 69, and over the whole range the residuals are within ±0.1 digit (the Galerkin error). The
leading constant drifts downward as the range grows: 12.99 → 12.71 → 12.59, against 4π = 12.566. A free rate drifts
the same way (β = 2.44 → 2.25), so rate 2 is consistent and the constant is approaching 4π from above; the data do not
fix it to better than ≈ 3 %.
(iii) Ratio to cor:margin1. The local slope dy/dT is 45 at ½log3, 106 at ½log5, 150 at ½log7, 190 at 1.06, 300 at
1.25 and 376 at 1.375 (from the 1.35–1.4 pair), so the effective b/15.449 is 2.9, 6.9, 9.7, 12.3, 19.5, 24.3 and grows
without bound in the doubly exponential model (b_eff = 2c₁e^{2T} + c₂). At T = 1.4, λ_A ≈ 10^{−68.7} against the proved
ceiling 4·10⁹·1.4·e^{−21.6} ≈ 2.3·10⁰: cor:margin1 is uninformative on the whole resolved range, as P46 already says.
The exponent 15.449 = 42/e is a property of the test family of lem:testfam (cutoff 21 just below γ₂, optimisation of
k in (k/21T)^{2k}); it removes one point and decays only singly exponentially, so it cannot be the rate.
(iv) Contacts. Over the contacts ½log3, log 2 (= ½log4), ½log5, ½log7, ½log8 the residuals of the double fit are
+0.08, −0.03, +0.02, +0.03, −0.00 digits: no jump at the resolution 0.03 digit. Segment-by-segment fits of
y = c₁e^{2T} + c₃ between consecutive contacts give c₁ = 9.17, 10.27, 10.93, 11.32, 11.19: a slowly increasing
effective constant, without a discontinuity. Monotonicity forbids upward jumps in λ_A; a downward jump at a contact
would be a kink (λ_A is continuous, P46 lem:contA). The data show no visible kink: the law is a law "across contacts",
not piecewise between them. (By contrast the κ in Mori's λ_W table drops by 8–15 % at each contact, PATTERN_001; for
λ_A the corresponding jump is below 0.03 digit ≈ 7 %, so the same effect is not excluded at that size.)

## 3. The structure of the bottom (NUMERICAL, 40 digits, even sector unless stated)

μ_k: unconstrained eigenvalues of a_T on L²_ev(I_T); τ_k/‖χ‖ the normalised Tate moments; λ_W^par the bottom of
W_T on the sector; 𝔤/‖h‖² the capacity ratio of thm:parityschur(a4).

| T | μ₀ | μ₁ | λ_A^ev | μ₁ − λ_A^ev (rel.) | τ₀/‖χ‖ | τ₁/‖χ‖ | λ_W^ev | 𝔤/‖h‖² − λ_W^ev (rel.) | λ_A/λ_W |
|---|---|---|---|---|---|---|---|---|---|
| log 2 | −2.823 | 1.114·10⁻⁷ | 1.114·10⁻⁷ | < 10⁻⁵ | 0.9975 | 3.4·10⁻⁸ | 8.23·10⁻¹³ | 3·10⁻⁶ | 1.35·10⁵ |
| 0.9 | −3.803 | 6.03·10⁻¹⁷ | 6.03·10⁻¹⁷ | < 10⁻⁵ | 0.9991 | 1.5·10⁻¹⁷ | 5.15·10⁻²³ | 3·10⁻⁷ | 1.17·10⁶ |
| 1.0 | −4.284 | 1.96·10⁻²³ | 1.96·10⁻²³ | < 10⁻⁵ | 0.9986 | 4.7·10⁻²⁴ | 7.89·10⁻³⁰ | 1.4·10⁻⁷ | 2.49·10⁶ |
| 1.2 | −5.348 | 2.61·10⁻⁴¹ | 2.61·10⁻⁴¹ | < 10⁻⁵ | 0.9989 | 5.5·10⁻⁴² | 3.05·10⁻⁴⁸ | 4·10⁻⁸ | 8.57·10⁶ |
(N = 80, 80, 90, 90.) Observations.
(a) n₋ = 1 and λ_A^ev = μ₁ to five or more digits: the first excited unconstrained eigenvector is Tate-null to the
order of its own eigenvalue (τ₁/‖χ‖ ≈ 0.2–0.3·μ₁), so by ROUND_005_D (3.1) μ₁ − λ_A = τ₁²/D = O(μ₁²) and the
constraint is invisible at the scale of λ_A. The whole size of λ_A is the size of μ₁, the second eigenvalue of the
unconstrained window form on the even sector. The next ones, μ₂, μ₃, are the cluster (ROUND_005_E), separated from μ₁
by factors 10⁴–10⁷ (μ₂/μ₁ = 2·10⁴, 2·10⁵, 7·10⁵, 4·10⁶).
(b) λ_W^ev = 𝔤/‖h‖² to 7–8 digits (thm:parityschur(a4) is sharp here), and λ_A/λ_W ≈ 10⁵–10⁷, growing slowly
(ln ratio = 11.8, 14.0, 14.7, 16.0).
(c) The odd sector repeats the pattern one level higher: λ_A^odd = μ₀^odd ≥ 0 (n₋ = 0 there), with τ₀^odd ≈ 7μ₀^odd.

## 4. Pure mathematics: λ_A against the complete form, and what a lower half needs

Setting: fix T and a parity; write 𝒟 = 𝒟_T^par, ℓ = ℓ_par, ε = ε_par, 𝒬 = 𝒬_T^par = ker ℓ ∩ 𝒟 (P46 thm:parityschur).
On 𝒟, W_T = 𝔞_T + 2ε ℓ(·)² (thm:parityschur(o), CITED).

**Proposition 4.1 (two-sided sandwich; PROVED).** For each parity,
    λ_W^par ≤ λ_A^par ≤ λ_{W,2}^par,
where λ_{W,2}^par is the second min–max value of W_T on 𝒟. Consequently λ_W ≤ λ_A (this half is P46 thm:A with
rem:Kprim, CITED) and λ_A ≤ min_par λ_{W,2}^par.
*Proof.* On 𝒬, ℓ = 0, so W_T = 𝔞_T there and λ_A^par = inf_{𝒬} W_T/‖·‖² ≥ inf_{𝒟} W_T/‖·‖² = λ_W^par. For the upper
bound, let S ⊂ 𝒟 be any two-dimensional subspace; ℓ|_S has a nonzero kernel vector F ∈ S ∩ 𝒬, and
W_T(F) = 𝔞_T(F) ≥ λ_A^par‖F‖², so sup_S W_T/‖·‖² ≥ λ_A^par; take the infimum over S. ∎

**Proposition 4.2 (the capacity correction; PROVED, and the requested inequality REFUTED in general).** Assume the
sector is non-degenerate (thm:parityschur(a)) with 𝔤 = 𝔤_par, h = h_par, and let P be the L²-orthogonal projection
onto the closure of 𝒬, A_𝒬 the operator of 𝔞_T|𝒬. For μ < λ_A^par put R(μ) := ⟨Ph, (A_𝒬 − μ)^{−1}Ph⟩ ≥ 0 and
    φ(μ) := 𝔤 − μ‖h‖² − μ² R(μ).
(i) If λ_W^par < λ_A^par, then λ_W^par is the smallest zero of φ on (−∞, λ_A^par), and
    λ_W^par − 𝔤/‖h‖² = −(λ_W^par)² R(λ_W^par)/‖h‖² ≤ 0.                                                     (4.1)
(ii) The inequality "λ_A^par ≥ λ_W^par − 𝔤/‖h‖²" therefore holds trivially whenever λ_A^par ≥ 0 (right side ≤ 0)
and whenever 𝔤 ≥ 0 (it is weaker than Prop. 4.1). It is FALSE in general: in the two-dimensional bordered model
𝒟 = ℝ², ℓ(F) = F₂, 𝔞 = diag(α, w) with α = −1, w = −5, one has 𝒬 = ℝe₁, λ_A = −1, h = e₂, 𝔤 = −5, λ_W = −5, and
λ_W − 𝔤/‖h‖² = 0 > λ_A.
*Proof.* (i) Write F = G + xh, G ∈ 𝒬 (thm:parityschur(a1)); then W_T(F) = 𝔞_T(G) + 𝔤x². A constrained critical point
of W_T − μ‖·‖² with μ < λ_A^par satisfies, testing with δG ∈ 𝒬, (A_𝒬 − μ)G = μxPh, and, testing with δx,
𝔤x − μ(⟨G, h⟩ + x‖h‖²) = 0. Since ⟨G, h⟩ = ⟨G, Ph⟩ = μx R(μ), and x ≠ 0 (else G is an eigenvector of A_𝒬 with
eigenvalue μ < λ_A^par), φ(μ) = 0. Conversely a zero of φ below λ_A^par gives an eigenvector. The bottom of W_T on 𝒟,
if below λ_A^par, is attained (compact resolvent, thm:parityschur proof) and is the smallest such zero. At μ = λ_W^par,
𝔤 = μ‖h‖² + μ²R(μ); divide by ‖h‖². (ii) The model is checked directly. ∎

Reading. The polar capacity enters λ_W, not λ_A: the passage from W_T to 𝔞_T|P_T can only RAISE the bottom, and by the
exact amount encoded in (4.1). So "λ_A ≥ λ_W − capacity" is never a better tool than λ_A ≥ λ_W, and Prop. 4.1 is the
correct statement of the transfer.

**Corollary 4.3 (floors for λ_A from complete-form certificates; PROVED transfer of CITED inputs).** λ_A(T) ≥ 2^{−1518}
for T ≤ ½log12 and λ_A(T) ≥ 2^{−2904} for T ≤ ½log15. *Proof.* Prop. 4.1, monotonicity (lem:monoT), and the cited
certified values of §1(a). ∎ These floors are 400–800 decimal orders below the Galerkin values (λ_A(1.2) ≲ 10⁻⁴¹):
the certificates bound λ_W at the out-of-band constant, not at the size of λ_A.

**Proposition 4.4 (a law for λ_W transfers only as a floor, and caps the λ_A fit; CONDITIONAL).** Suppose the lower half
of the κ-band (phase 199 PATTERN_001 §4, OPEN): λ_W(T) ≥ κ₋(1 − λ₄(2πμ)), μ = e^{2T}, with Fuchs' asymptotics
1 − λ₄(c) ≍ c^{9/2}e^{−2c} (CITED). Then −log λ_A(T) ≤ 4πe^{2T} − 9T + O(1). In particular no law
−log λ_A = c₁e^{2T} + O(T) with c₁ > 4π can hold on an unbounded range. *Proof.* Prop. 4.1 and the hypothesis. ∎
Consequence for §2 (NUMERICAL comparison, CONDITIONAL reading). The fitted c₁ = 12.59 (whole range) is 0.2 % above
4π = 12.566. The κ-model of λ_W (κ ≈ 4.6, Mori V Table 1; Fuchs constant) predicts −ln λ_W − (−ln λ_A) = 14.4 at
T = 1 when combined with the double fit, against the measured 14.7 (§3); it stays between 14 and 28 up to T ≈ 3 and
the two curves cross only at T ≈ 3.8, beyond the data. So within the resolved range the λ_A law and the λ_W law have the
same leading term 4πe^{2T} and differ by a factor e^{14…16} ≈ 10⁶–10⁷ that grows like ≈ 6T; if the κ-band lower half holds,
the leading constant of the λ_A law is ≤ 4π, and the fitted 12.59 is that constant within its error.

### 4.5 What the lower half λ_A ≥ L(T)(1 − o(1)) needs, in this phase's structure

Work in the even sector (the bottom sector at every resolved T, §1(c)). Let μ₀ < μ₁ ≤ … be the unconstrained
eigenvalues of 𝔞_T on L²_ev(I_T), e_k their eigenvectors, τ_k = ⟨e_k, χ_ev⟩. ROUND_005_D Theorem 3.1 (PROVED) with n₋ = 1
gives λ_A^ev as the unique root in (μ₀, μ₁) of 𝒲(z) = Σ_k τ_k²/(μ_k − z). Since 𝒲 is increasing there:

**Lemma 4.6 (exact form of the lower half; PROVED).** For 0 < L < μ₁ (n₋ = 1, τ₁ ≠ 0):
    λ_A^ev ≥ L  ⟺  τ₀²/(|μ₀| + L) ≥ Σ_{k≥1} τ_k²/(μ_k − L).                                                       (4.2)
In particular, a necessary condition is μ₁ > L, and with the near-null cluster 𝒦 = {k ≥ 1 : μ_k ≤ δ} (size m_δ,
ROUND_005_E: m_δ ≈ 0.15e^{4T} on T ≤ 1.2, NUMERICAL; m_δ ≤ N_Arch(δ + A_T), PROVED there) the right side splits as
    Σ_{k∈𝒦} τ_k²/(μ_k − L) + Σ_{k∉𝒦} τ_k²/(μ_k − L) ≤ Σ_{k∈𝒦} τ_k²/(μ_k − L) + (‖χ_ev‖² − τ₀²)/(δ − L).
*Proof.* 𝒲(L) ≤ 0 ⟺ λ_A^ev ≥ L by monotonicity of 𝒲 on (μ₀, μ₁); split the sum. ∎

So a lower half with explicit L requires three inputs, each with an explicit size:
(N1) a spectral floor μ₁(T) ≥ (1 + η)L(T) for the first excited unconstrained eigenvalue;
(N2) Tate-nullness of the cluster at the scale of L: Σ_{k∈𝒦} τ_k²/(μ_k − L) ≤ (1 − η′)τ₀²/(|μ₀| + L) − (bulk term). With
     ROUND_005_D's observation τ_k/τ₀ = O(μ_k) on the cluster (NUMERICAL), each cluster term is O(μ_k²/(μ_k − L)), so
     (N2) is a statement that the cluster eigenvalues above L are not too close to L relative to their Tate moments;
(N3) the bulk term (‖χ‖² − τ₀²)/(δ − L) ≤ τ₀²/(2|μ₀|): this is the two-level condition of ROUND_005_D Cor. 3.3 and
     holds with room when δ is of order one (ROUND_005_D §5: cos²∠(h_T, χ_ev) ≥ 0.994, NUMERICAL).
Sign budget (ROUND_005_C Prop. 3, PROVED): on the minimiser, ℛ(F*) = κ(F*) − |σ_T| − λ_A, so (4.2) is equivalently the
statement that the fluctuation functional ℛ stays below κ − |σ_T| by at least L on every unit F ∈ P_T. The lower half is
thus a quantitative version of (★) whose margin is L(T) ≈ exp(−13e^{2T}): it is (★) plus an explicit gap, and none of
(N1)–(N3) is weaker than (★) at that scale. The exact Schur reductions (ROUND_005_C Theorem 2) carry the same margin
(P46 lem:shape-est(ii)) and add nothing.

**Corollary 4.7 (the lower half is a statement about one unconstrained eigenvalue; PROVED reduction).** In the even
sector with n₋ = 1, τ₁ ≠ 0, ROUND_005_D Cor. 3.2 gives λ_A^ev = μ₁ − τ₁²/D(λ_A^ev), D(z) = τ₀²/(|μ₀| + z) −
Σ_{k≥2}τ_k²/(μ_k − z) > 0. Hence, for any L > 0 and η ∈ (0, 1),
    [ μ₁ ≥ L  and  τ₁² ≤ η L·D(L) ]  ⟹  λ_A^ev ≥ (1 − η)L,
and conversely λ_A^ev ≥ L ⟹ μ₁ ≥ L (interlacing). *Proof.* If λ_A^ev < (1 − η)L ≤ μ₁ then, D being decreasing on
(μ₀, μ₁) (D′ = −τ₀²/(|μ₀|+z)² − Σ_{k≥2}τ_k²/(μ_k − z)² < 0), D(λ_A) ≥ D(L) fails to be the right comparison; argue instead
with 𝒲: 𝒲((1 − η)L) = −τ₀²/(|μ₀| + (1−η)L) + τ₁²/(μ₁ − (1−η)L) + Σ_{k≥2}τ_k²/(μ_k − (1−η)L) ≤ −D((1−η)L) + τ₁²/(ηL)
≤ −D(L) + τ₁²/(ηL) ≤ 0, using D((1−η)L) ≥ D(L) (D decreasing) and μ₁ − (1−η)L ≥ ηL; 𝒲 ≤ 0 at (1−η)L means the root
λ_A^ev lies to the right. ∎
With the §3 data (τ₁²/D ≈ 10⁻² μ₁² ≪ ημ₁), the second condition holds with enormous room at every resolved window
(NUMERICAL). So the lower half of the law reduces, up to a correction quadratic in L, to
    (N1′)  μ₁(T) ≥ L(T),  μ₁ = the second eigenvalue of the unconstrained window form 𝔞_T on L²_ev(I_T),
together with the bound τ₁² ≤ ηL·D(L) on the Tate moment of its eigenvector. (N1′) is again a statement with the size of
(★) and a margin exp(−4πe^{2T}): the reduction removes the Tate constraint, not the difficulty. It is the cleanest form of
the lower half found here.

## 5. The law on the resolved range, and the contacts ½log7, ½log8, ½log9 (NUMERICAL)

Candidate law (fitted, not proved): −ln λ_A(T) = c₁e^{2T} + c₂T + c₃ with c₁ ∈ [12.59, 12.99], rate 2 (§2(ii)); the
constant drifts towards 4π = 12.566 as the range grows. Equivalently L(T) ≈ e^{−c₃}e^{−c₂T}exp(−c₁e^{2T}), i.e. the
"c·exp(−b e^{aT})" family with a = 2, b ≈ 4π, and a polynomial prefactor in μ = e^{2T} (−c₂T = −(c₂/2) ln μ, c₂/2 ≈
10–12, against Mori's μ^{9/2} for λ_W; the gap of the prefactors is the slowly growing ratio λ_A/λ_W of §3(b)).
Stability: the rate-2 double family is the only one whose extrapolation from T ≤ 1.08 to 1.4 stays within one digit;
the singly exponential family misses by 14 digits (§2(i)).
Contacts. ½log7 (0.973) and ½log8 (1.040): residuals +0.03 and −0.00 digit, segment constants continuous (§2(iv)).
½log9 (1.0986): the nearest resolved windows are 1.075 (phase 187), 1.1 and 1.05 (this phase, sine basis); the whole-
range residual at 1.1 is +0.08 digit, inside the Galerkin error (≤ 0.1 digit). So a jump at ½log9 is not resolved; any
kink there is below ≈ 25 % in λ_A. The response cubic of ROUND_007_B gives ½log5/7/8/9 as entry thresholds of new comb
responses; on λ_A they leave no visible trace at 0.03–0.1 digit. Reading: the bottom μ₁ is a smooth function of T at
the resolution available, and the comb enters λ_A only through the continuous drift of c₁.

## 6. Falsifiers: the fitted law for cΛ and a_3 (NUMERICAL, N = 60, 25 digits, 19 windows T ∈ [0.3, 1.2])

Bottom eigenvalue λ^ev / λ^odd of the constrained form with weights cΛ (c = 0.9, 0.95, 1.05, 1.1) and a_3 (prime 2
deleted), same sine basis. (For Λ at N = 60 the values are upper bounds only, e.g. 5·10⁻³⁷ at 1.2 against 10⁻⁴¹; for
the falsifiers the values are O(10⁻²) and the basis error is negligible at that scale; the signs at 1.0 for 1.1Λ and
at ½log5+10⁻⁴ for a_3 are certified in ROUND_007_C.)

| T | Λ | 0.9Λ | 0.95Λ | 1.05Λ | 1.1Λ | a_3 |
|---|---|---|---|---|---|---|
| 0.45 | 7.1·10⁻² | +9.4·10⁻² | +8.2·10⁻² | +5.9·10⁻² | +4.7·10⁻² | +0.29 |
| 0.5 | 1.3·10⁻² | +3.2·10⁻² | +2.3·10⁻² | +3.8·10⁻³ | −5.7·10⁻³ | +0.18 |
| 0.545 | 1.2·10⁻³ | +1.6·10⁻² | +8.7·10⁻³ | −6.5·10⁻³ | −1.4·10⁻² | +0.096 |
| 0.6 | 7.7·10⁻⁵ | +9.8·10⁻³ | +5.5·10⁻³ | −6.9·10⁻³ | −1.6·10⁻² | −0.14 |
| 0.65 | 2.7·10⁻⁶ | −2.4·10⁻⁴ | +1.4·10⁻³ | −1.4·10⁻² | −4.1·10⁻² | −0.35 |
| 0.69 | 1.5·10⁻⁷ | −9.3·10⁻³ | −4.1·10⁻³ | −2.6·10⁻² | −5.4·10⁻² | −0.43 |
| 0.8 | 6.2·10⁻¹² | −2.6·10⁻² | −1.3·10⁻² | −4.5·10⁻² | −9.4·10⁻² | −0.51 |
| 1.0 | 2.5·10⁻²³ | −5.0·10⁻² | −2.5·10⁻² | −7.0·10⁻² | −0.14 | −0.54 |
| 1.2 | (≤5·10⁻³⁷) | −7.1·10⁻² | −3.5·10⁻² | −9.6·10⁻² | −0.20 | −0.54 |

Sign changes (even sector, linear interpolation): 1.1Λ at T ≈ 0.48; 1.05Λ at ≈ 0.52; a_3 at ≈ 0.57 (just above the
contact ½log3 = 0.549 of the first surviving prime); 0.9Λ at ≈ 0.65; 0.95Λ at ≈ 0.67. The odd sector changes sign later
(0.9Λ near 0.85, a_3 near 0.7) or not at all for c < 1 on T ≤ 0.8.
Fitted laws past the crossing: λ(T; cΛ) ≈ −|1 − c|·g_±(T), with g₋(T) (c < 1) ≈ 0.50 at T = 1 and 0.71 at 1.2 (both
c = 0.9 and 0.95 give the same g₋ to 2 %), and g₊ (c > 1) ≈ 1.4 at 1.0 and 1.9 at 1.2 (same 2–5 % agreement); a_3
saturates at ≈ −0.54. The falsifier bottoms are linear in the defect |1 − c| (first order in the weight perturbation)
and grow at most linearly in T; none has a doubly exponential size.
Discrimination. A law of the form L(T) = exp(−c₁e^{2T} + …) > 0 separates Λ from every falsifier only through its
sign, not through its shape: the falsifiers do not follow a positive law that later crosses zero at a doubly
exponentially small level; they leave the positive regime at T ≈ 0.5–0.67 at size O(10⁻²) and then sit at
−|1−c|·g(T). Hence (NUMERICAL) any lower-half statement λ_A ≥ L(1 − o(1)) must use the weights exactly: by Lemma 4.6 /
Cor. 4.7 its content is μ₁(T) ≥ L(T) with L ≈ exp(−4πe^{2T}), and at c = 1 ± 10^{−k} the falsifier bottom is
≈ −10^{−k}g(T), which crosses below L(T) at every T where L(T) < 10^{−k}g(T). Every argument for (N1′) must therefore be
sensitive to a relative weight perturbation of size L(T) — the "margin" of [margin] (06) in its λ_A form. This is the
falsifier test of BRIEF rule 4 applied to the law itself: (a) cΛ, (b) a_3 fail as required; (c) Beurling 3→3.2 and
(d) finite modifications enter at first order in the same way (ROUND_007_C certifies the first).

## Result

PROVED piece + PIVOT. The lower half of the two-sided law is reduced, exactly, to one unconstrained eigenvalue.

### What was proved
- Prop. 4.1 (sandwich λ_W^par ≤ λ_A^par ≤ λ_{W,2}^par, PROVED) and the transfer of cited λ_W certificates to λ_A floors:
  λ_A ≥ 2^{−1518} on T ≤ ½log12 and ≥ 2^{−2904} on T ≤ ½log15 (CITED inputs, PROVED transfer).
- Lemma 4.6 (exact form of the lower half through the secular function, PROVED) and Corollary 4.7: with n₋ = 1,
  λ_A^ev ≥ (1 − η)L follows from μ₁ ≥ L and τ₁² ≤ ηL·D(L) (PROVED reduction); conversely λ_A ≥ L forces μ₁ ≥ L.

### What failed and why
- Singly exponential laws cT^a e^{−bT}: NO-GO as laws (NUMERICAL; 14-digit miss at 1.4, a ≈ 166–295).
- Rate-2 doubly exponential law −ln λ_A = c₁e^{2T} + c₂T + c₃, c₁ → 4π from above: stable to ±0.1 digit on
  [½log3, 1.4] (NUMERICAL); no contact jump at ½log7, ½log8 above 0.03 digit, ½log9 unresolved below 0.1 digit.
- The lower half itself is not weaker than (★): (N1′) carries margin exp(−4πe^{2T}) and the falsifiers show it must
  be sensitive to weight perturbations of that relative size. No mechanism in the phase's structure (near-null
  cluster, Tate-nullness, sign budget, polar capacity / parity Schur, transfer from λ_W) supplies a positive floor
  for μ₁: λ_W transfers only floors that are themselves doubly exponentially weaker (λ_A/λ_W ≈ 10⁵–10⁷, growing).
- Falsifiers: cΛ and a_3 cross zero at T ≈ 0.48–0.67 at size O(10⁻²) and then sit at −|1−c|g(T); the law
  discriminates only by sign (NUMERICAL).

### Next concrete step
Attack (N1′) directly: a lower bound for the second even eigenvalue μ₁(T) of the unconstrained window form 𝔞_T,
with first-order weight sensitivity (Hellmann–Feynman: dμ₁/dc = Π_T(e₁) at c = 1) computed and bounded, since the
falsifier slopes g_± are exactly −Π_T(e₁)-type quantities; the sign of Π_T(e₁) − Arch(e₁) on the eigenvector e₁ is the
first test any such bound must pass.
