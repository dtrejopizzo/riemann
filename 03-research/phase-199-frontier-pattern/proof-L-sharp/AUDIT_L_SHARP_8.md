# AUDIT_L_SHARP_8 — audit of PROOF_L_SHARP_X_001 (Theorem B), BRIDGE_001 (Lemma B.0, planks) and PRECHECK_T1_001

Phase 199,
Checked against E_001 (Thm E.1/E.2, Cor E.3), J_001 (Prop J.1), F_001 (Prop F.0, F.5),
AUDIT_L_SHARP_7 (constraint 19), Paper 47 eq:Aform. Scratch checks (sympy/numpy, not stored) are NUMÉRICO and only check
the algebra.

**Verdict in one line.** Theorem B (single-cell form) **stands as PROVED** after two constant repairs: K₂ is undercounted, and
the gap g ≥ 2δ/N is used but only g ≥ δ/N is written. Neither repair changes the O(ν₀⁻¹) order or the polylog-in-N
dependence. Lemma B.0 and Lemma X.4 are PROVED. Cor X.7(ii) is PROVED. Cor X.7(i) is correct only as a statement about the
high-frequency single-cell cone. The BRIDGE claim "for c < 1 the chain does not fail in any plank" is downgraded to ARGUED,
with a caveat. PRECHECK_T1 is a sound NUMÉRICO non-falsification; its zero test validates conventions but not the
polylog-tail path. Constraint 20 is added. Row D OPEN.

## 1. Lemma X.1 (disjoint dilates) — PROVED, with a constant note
- In y-variables, J_m and J_n are disjoint iff (N+1−δ)/n < (N+δ)/m, i.e. m(N+1−δ) < n(N+δ).
  - For n = m+1 this reads m(1−2δ) < N+δ. That holds for every m ≤ N−1 and every δ ∈ (0,½).
  - So the dilates are disjoint for all N ≥ 1. N ≥ 2 is needed only so that cross classes exist and so that the worst
    case m = N−1 is defined.
- (In t-language: n·[N+δ, N+1−δ] for different n never collides with the cell [N+δ, N+1−δ] at the same dilation index.
  The right object is J_n = log([N+δ,N+1−δ]/n), not the multiplied intervals. Those intervals overlap for large n, but
  that is irrelevant because n ≥ N+1 lands at y < 0, where Ψ̌ := 0.)
- Exact gap for k = 1 at m = N−1: the difference N(N+δ) − (N−1)(N+1−δ) = 2δN + 1 − δ ✓.
  - Using log(1+x) ≥ x/(1+x) gives g ≥ (2δN+1−δ)/(N(N+δ)) ≥ 2δ/N ⟺ 1−δ ≥ 2δ², which is true for δ < ¼.
  - So **g_{m,m+1} ≥ 2δ/N is true**. The memo writes only δ/N, but E_cross uses 2δ/N. Repair: add the one-line
    inequality above. (Scratch check: min gap/(2δ/N) ≥ 1.016 over N ≤ 100, δ ≤ 0.24.)
- k ≥ 2: g ≥ (k−1+2δ)/N ≥ k/(2N) ✓.

## 2. Lemma X.2 (exact decomposition) — PROVED
- Ψ̌ = Σ_{n≤N} n^{−½}u_n follows from Ψ̌(y) = e^{y/2}Σρ(ne^y) ✓.
- Diagonal weight (n^{−½})² = 1/n, giving H_N; translation invariance of Θ_∞(D) ✓.
- Off-diagonal: the polarised Lévy form on disjoint supports gives −∫∫u_m ū_n ν, and the b_∞ term vanishes ✓.
  - Killing term: 𝒜 is the full-line form of the zero-extended Ψ̌ (E §1).
  - Lemma X.1(i) puts every dilate strictly inside (0,∞), so no truncation is lost ✓.
- Pole:
  - A = Σ n^{−½}·n^{½}∫u e^{−x/2} = N∫ρ dt/t ✓;
  - B = Σ n^{−1}∫u e^{x/2} = H_N∫ρ dt ✓;
  - ‖u‖²_{dx} = ‖ρ‖²_{dt} ✓.
- Hermitian extension: 2Re(AB̄) = 2(A_R B_R + A_I B_I) ✓.
- H₁(N) = Σ_{n≤N} log n / n ✓. It agrees with E.2's collapse Σ(mn)^{−½}log(mn)I(m,n) at I = δ_{mn}‖u‖²: 2Σ_n (log n)/n ✓.

## 3. Lemma X.3 (comb on single-cell data) — PROVED
- ⟨Ψ̌, S_{−log q}Ψ̌⟩ = Σ_{lq≤N}(lq·l)^{−½}‖u‖² = q^{−½}H(N/q)‖u‖² ✓.
- Weight c_q = w(q)q^{−½} gives −2Σ_q w(q)q^{−1}H(N/q)‖u‖² = −2‖u‖²Σ_{n≤N}(w∗1)(n)/n ✓ (Dirichlet hyperbola).
- For w = Λ, Λ∗1 = log gives −2H₁(N)‖ρ‖² ✓.
- The factor 2 matches Paper 47's comb (both signs ±log q) and PRECHECK's zero test ✓.
- **Phase-independent, exactly as stated.** This is precisely why single-cell data carry no cross-class information
  (constraint 20).

## 4. Lemma X.4 / Lemma B.0 (F(N)) — PROVED
- Exact values: F(1) = 0; F(2) = ½log 2 = 0.34657; F(3) = (11/6)log 3 − log 2 − (2/3)log 3 = (7/6)log 3 − log 2 = 0.58857.
- Increment: F(N+1) − F(N) = H_N log(1+1/N) − log(N+1)/(N+1) ✓ (algebra rechecked). It is ≥ 0 because H_N ≥ log(N+1)
  and log(1+1/N) ≥ 1/(N+1) ✓. Hence F ≥ 0 for all N ≥ 1 ✓ (BRIDGE B.0 and X.4 use the same F).
- Upper bound:
  - H_N ≤ log N + γ + 1/(2N) ✓;
  - H₁(N) − ½log²N ≥ γ₁. This holds at N = 1 (0) and N = 2 (0.106), and decreases from N = 3 (0.109) to γ₁ = −0.0728 ✓.
  - Hence F ≤ γ log N + (log N)/(2N) − 2γ₁ < γ log N + 1 ✓.
  - Scratch check: max_{N ≤ 10⁶}(F − γ log N) = 0.1456, attained at the right end, increasing toward −2γ₁ = 0.1456 ✓.
- B.0(i):
  - on (1,2): (ω²−2)² ≥ 0 ✓;
  - on ω ≥ 2: 𝔴 ≥ H log μ + F(N) + H log(ω/N) ≥ (3/2)log μ ≥ log 2μ for μ ≥ 4 ✓.
- **B.0 PROVED.**

## 5. Lemma X.5a and Theorem X.5 — PROVED after one constant repair
- **Non-stationary bound (a): K₂ is undercounted.**
  - With g = Φ′−τ: L²A = A″/g² − 3A′Φ″/g³ − AΦ‴/g³ + 3AΦ″²/g⁴ (sympy-verified).
  - With g ≥ Ω/2+σ and g ≥ Φ′/2 (both correct for τ ≤ Ω/2 ≤ Φ′/2), the right comparison is
    g^{−j} ≤ (2/Φ′)^{j−2}(Ω/2+σ)^{−2}. The memo's "2^{j−1}Φ′^{−(j−1)}(Ω/2+σ)^{−1}" gives only one power, which is a typo
    for the claim.
  - **Corrected K₂ := ‖A″‖₁ + 6‖A′Φ″/Φ′‖₁ + 2‖AΦ‴/Φ′‖₁ + 12‖AΦ″²/Φ′²‖₁** (memo: 4, 2, 8).
  - Also: K₂ is ν-independent for the semiclassical family (every term is scale-free). The memo's "K₂/ν ν-independent"
    is wrong but harmless, since the true statement is stronger.
- **(b) split:**
  - C_Θ = 0.18727 (recomputed, NUMÉRICO) ✓;
  - ∫(Ω/2+σ)^{−4} = 8/(3Ω³), so the stated K₂²(7+2log(1+Ω))/(2Ω³) majorises ✓.
- **(c) resolvent comparison:**
  - log X − log Y = ∫(X+s)^{−1}(X−Y)(Y+s)^{−1}ds ✓;
  - (D̃−M)v_s = −iA_s′e^{iΦ} + (Ω/2−D)_+v_s ✓ (D = −i∂, D̃ = D + (Ω/2−D)_+);
  - ‖A_s′‖ ≤ K₀/(Ω+s) ✓;
  - ∫ds/((Ω/2+s)(Ω+s)) = 2log2/Ω ✓;
  - second piece: ∫σ(Ω/2+σ)^{−3}dσ = 1/Ω, so the memo's bound is conservative by a factor 2 ✓.
  - The oscillatory log-symbol argument is correct. Negative τ are handled by the σ ≥ Ω/2 tail ✓.
- **Cross classes:**
  - The kernel is −ν(y−y′) and purely archimedean ✓. One integration by parts in y against e^{iΦ(y+ℓ_m)} is correct
    (one-sided oscillation suffices).
  - Kernel bounds ν ≤ 1/s, |ν′| ≤ 3/s² ✓ (NUMÉRICO sup sν = 0.75).
  - The pair sums are right given g ≥ 2δ/N (§1). Without the §1 repair, replace 1/(2δ) by 1/δ and 3/(4δ²) by 3/δ².
- **Pole:** O(H_N/(Nν₀)²) ✓.
- **Constants.** K₀, K₁, K₂ are explicit.
  - For a(t) = b(t−N): K₀ ≍ N‖b′‖, K₁ ≲ N^{−½}K₀, K₂ ≍ N^{3/2}.
  - The terms K₁K₂/Ω² and K₂²/Ω³ are then O(ν₀^{−2}) and O(ν₀^{−3}) uniformly in N.
  - E = O(H_N log N/ν₀) — **polylog in N: confirmed**.
- **Status:** Theorem X.5 PROVED (constants corrected as above).

## 6. Corollaries X.6, X.7 — PROVED, scope sharpened
- **X.6.** w ≥ H_N log(ν₀/2π) + F(N) + H_N log(1+δ/N) ✓.
- **X.7(ii).** ν₀ = 2πN^{(c−1)/2}. Then
  w^c = (c−1)/2·H_N log N + F(N) + H_N log(t/N) − 2(c−1)H₁(N) = −((c−1)/2)log²N + O(log N) ✓.
  - E ≤ C log²N·N^{−(c−1)/2} → 0 ✓.
  - **PROVED.** By F.5 this is also an explicit negative direction of the cΛ window form at T₀ = ½log(N+1), for every
    c > 1 and N ≥ N₀(c) — a proved version of the 1.15Λ/2Λ NUMÉRICO falsifiers (AA_001), on dilate-disjoint chirps.
- **X.7(i) and the 0.85Λ falsifier — no contradiction; different data class.**
  - By F.5, single-cell data are window data at T₀ = ½log(N+1), and T₀ ≥ 1 for N ≥ 7. AA_001 (phase 198) shows the
    0.85Λ window form negative at T ≥ 1 in the odd sector (NUMÉRICO). Under the BRIDGE §7 convention (archimedean and pole
    unchanged), that is a negative direction of 𝔔^{0.85} on shallow data.
  - Cor X.7(i) asserts positivity **only** on the cone {single cell, chirp, φ′ ≥ ν₀ ≥ ν_*(a,φ,N,δ)}.
  - The 0.85Λ negative directions are low-frequency window vectors near the archimedean floor (multi-cell, non-chirp after
    F.5 inversion). Theorem B is silent on them.
  - Corrected wording: "c ≤ 1: the high-frequency single-cell cone stays positive (larger weight)". The memo's "positivity
    persists" must not be read as positivity of 𝔔^c.
- **Consequence for BRIDGE §7 (CORRECTION).**
  - "For c < 1 the chain does not fail in any plank; it fails at I1" is not supported. 𝔔^{c} with c < 1 is already
    indefinite on shallow (non-PW) data, CONDITIONAL on the AA_001 normalisation equalling the §7 convention.
  - So pointwise positivity of the weight does not certify any plank for c < 1. Where c < 1 fails on PW tails
    (I1, P1-bulk or P3b) is OPEN.
  - Downgrade: ARGUED → OPEN.

## 7. PRECHECK_T1_001 (spot-check of wext.py, radical_test.py)
- **Conventions (wext.py):**
  - Θ_∞ = Re ψ(¼+iτ/2) − log π ✓;
  - 𝔔 = arch − 2P + 2AB, with P = ⟨φ,φ_log⟩ and log n weights only (a_n ≡ 1) ✓;
  - killing term included via the FFT of the zero-extended φ ✓.
  - These match E.3 and X.2.
- **Zero test (radical_test.py).** The pure-gauge datum has c = 2π (low frequency) and b ≡ 0, so the closed-form
  Li₁/Li₂/L_s tail path used for every prolate chirp is **not exercised**. The datum is also truncated at t ≤ 3000, with
  the j_j(2πt) ~ 1/t tail dropped.
  - The sum −1.4·10⁻⁸ (3·10⁻⁵ of the pieces) validates Θ_∞, the factor 2 and 2AB.
  - It does not validate the high-frequency tail summation. That path is covered only by the brute-force check
    (10⁻⁴, ψ₄, μ = 10).
  - Label: validation PARTIAL (NUMÉRICO).
- **Π negligibility (≤ 2·10⁻⁹).** This is expected: the gauge basis j_j(2πt), j ≤ 80, is low-Mellin, and the chirps sit at
  frequency c = 2πμ. Stable in J ✓. It does not test gauge-like data (constraint 19a, still binding there).
- **ψ₄ ratios 0.97–0.98 · ½D₄.** The offset is flat: Δκ ≈ 0.05–0.09 absolute while ½D₄ grows like log μ. That is the
  signature of an **O(1) correction to a log μ leading term**, not of a c^{−½}log c remainder.
  - "M3 confirmed at leading order" is fair only in the log μ sense.
  - The next-order term of M3 is unmodelled. "Route lives" is a fair reading of a non-falsification, and nothing more.
- **Edge −51 %.** It is the difference between the window value (MORI15, certified) and the pipeline's 𝒲_ext[Zr_{f*}].
  Its accuracy is that of the pipeline (≈ 10⁻³ relative after V-extrapolation). It agrees with AUDIT_7 §4.4's lower end ✓.
- **Labels:** all NUMÉRICO. No sign.

## 8. Label corrections
| item | memo | audit |
|---|---|---|
| Lemma X.1 | PROVED | PROVED (add g_{m,m+1} ≥ 2δ/N line) |
| Lemma X.2, X.3, X.4 | PROVED | PROVED |
| Lemma X.5a | PROVED | PROVED with corrected K₂ (6, 2, 12) |
| Theorem X.5 | PROVED | PROVED (constants per §5) |
| Rem X.5b | PROVED, constants not tracked | ARGUED (not checked in detail) |
| Cor X.6, X.7(ii), X.7(iii), X.8 | PROVED | PROVED |
| Cor X.7(i) "positivity persists" | PROVED | PROVED only on the high-frequency single-cell cone |
| BRIDGE Lemma B.0 | PROVED | PROVED |
| BRIDGE §7 "c < 1 survives every plank, dies at I1" | ARGUED | OPEN (𝔔^{c<1} indefinite on shallow data, CONDITIONAL on normalisation) |
| PRECHECK zero test | pipeline validation | PARTIAL (tail path untested by it) |
| PRECHECK "M3 leading order" | NUMÉRICO | NUMÉRICO, log-leading only; O(1) offset unexplained |

## 9. Constraint 20
**20 (single-cell data).** Data with supp ρ ⊂ [N+δ, N+1−δ] have pairwise disjoint dilates (X.1). For them the comb is the
phase-blind scalar −2Σ(w∗1)(n)/n·‖ρ‖² (X.3), and the cross classes are smooth archimedean kernels (no resonances).
Consequences:
- they **do not test cross-class interference, resonances (1,n), constraint 7, the edge P3b, or the gauge**;
- positivity on them is a high-frequency-cone statement, which is compatible with indefiniteness of 𝔔^c (c < 1) elsewhere;
- Λ-selection read from them is selection in the uniformity in N only (X.7(iii)).

**Do not retry:**
- single-cell evaluations as evidence for P2 or for c < 1 survival;
- the gauge zero test as validation of the high-frequency tail summation.

L′♯ OPEN. Row D OPEN.
