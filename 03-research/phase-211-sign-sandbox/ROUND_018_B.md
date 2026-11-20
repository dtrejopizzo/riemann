# Round 18 B — Exact ledger of the survivor, tail Grams on the first rungs, and the collapsed-weight test c·log N

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_017_A: λ = e^T, N = λ², c = 2πN, ψ_k the k-th prolate of [−λ, λ]
(unit norm), E the summation map, f_* the survivor of span{ψ_0, …, ψ_8} cut by f(0), ℱf(0), A(Ef), B(Ef), Ψ_f the Poisson
tail of Ef on (−∞, −T), Ψ_* := Ψ_{f*}/‖Ef_*‖. Forms in the conventions of tools/galerkin_mp.py:
𝒜_∞(F, G) = C_0⟨F, G⟩ + ∫_0^∞(c_{FG}(0) − c^sym_{FG}(u))K(u)du, C_0 = ψ(¼) − log π, K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2));
𝒞(F, G) = Σ_{n≥2} 2Λ(n)n^{−1/2} c^sym_{FG}(log n); 𝒯(F, G) = A(F)B(G) + B(F)A(G). Complete tail form 𝒲̂ := 𝒜_∞ − 𝒞 + 𝒯,
so that a_T(Ef) = 𝒲̂[Ψ_f] for admissible f (ROUND_015_B Cor 1.2, ROUND_016_B ident.py; mollified limit for f(λ) ≠ 0).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Read: ROUND_017_A (Prop 1.1 Schur form, Prop 1.2 (d) second-level identity, §4.1 inequality (4.1) and its pieces (P), (R), (S),
§4.2 comb-genericity left OPEN for the rung piece, next step), ROUND_015_B (§1.2 domain caveat, §3.4 diagonal ledger robust
for c < 1), ROUND_015_A Thm 3.1 (collapse Λ ∗ 1 = log on tails), ROUND_016_B (dilation form, polar term), tools/README.md.
Index rows P211-15B, P211-17A (do-not-retry: the sign in the low-block ledger; "comb averages out along chirps"; arch/comb
split of the coupling vector; falsifiers on the vector). Ledger C33–C38.
What differs. 17A computed the coupling vector against the Galerkin complement (truncated survivor) and left two items
uncomputed: the exact ledger 𝒲̂[Ψ_*] and the tail Gram on the pair (Ψ_*, Ψ_g) for the rungs g, with the c·log N test on that
Gram. Both are done here, on the exact (untruncated) survivor and on E-images of an enlarged prolate span, with the weight
changed in the tail form only. No indexed route is retried: the object is the one 17A names as next, and the question
asked of it (is the rung inequality Λ-specific?) has not been answered in any memo of record.

## 1. Two bookkeeping facts (PROVED)

**Lemma 1.1 (collapsed weight = scaled comb on tails).** For tails Ψ_f, Ψ_g the collapsed form of ROUND_015_A Thm 3.1,
Σ_{N,N′}[𝒜_∞(F_N, F′_{N′}) − w_c(N, N′)⟨F_N, F′_{N′}⟩] + 𝒯, with w_c(N, N′) = c(log N + log N′), equals 𝒜_∞ − c𝒞 + 𝒯 on the
same pair. *Proof.* The collapse is linear in the prime weight: the comb with weight cΛ collapses to (cΛ ∗ 1)(N) = c log N.
∎ Hence "replace log N by c log N in the tail form only" is the form 𝒲̂^c := 𝒜_∞ − c𝒞 + 𝒯 on tails, with every other
ingredient (survivor, rungs, window norm, Tate term) frozen. This is not the window form a^c_T on Ef: by ROUND_017_A Prop 3.1
the two differ by the radical defect (1 − c)𝒞(Φ_f, ·), of size O(1) (not O(d)).

**Lemma 1.2 (the 2×2 form of (4.1) is a determinant).** For ρ := 𝒲̂[Ψ_*] > 0 and g admissible, (4.1) of 17A restricted to
G ∈ span{Ef_*, Eg} ⊖ Ef_* is equivalent to det[[𝒲̂(Ψ_*,Ψ_*), 𝒲̂(Ψ_*,Ψ_g)], [𝒲̂(Ψ_g,Ψ_*), 𝒲̂(Ψ_g,Ψ_g)]] ≥ 0.
*Proof.* With G = Eg − ⟨Eg, F⟩F (F = Ef_*/‖Ef_*‖): ρ a_T(G) − a_T(F, G)² = ρ a_T(Eg) − a_T(F, Eg)² (expand; the ⟨Eg, F⟩-terms
cancel), and a_T = 𝒲̂ on E-images of admissible data. ∎ The share of a rung in the Schur correction is
s_g := a_T(F, G)²/(a_T(G)ρ) = 1 − det/(ρ a_T(G)) for G ⊥ F normalised.

## 2. Tool and validation (NUMERICAL)

tools/rung_gram_prep.py (multiprecision, 60 digits): even prolates ψ_0 … ψ_20 (nP = 11) at c = 2πe^{2T}, the four exact
constraint rows (as schur_coupling_survivor.py), the survivor (5-dim null vector; smallest singular value 10⁻⁹⁹ / 4·10⁻⁸⁸
at T = 0.8 / 1), the 7-dim admissible null space in all 11, Frobenius edge series and Fourier scale (checked against the
Bessel series to 10⁻³²). tools/rung_gram_tail.py: Ψ_{ψ_k} for every k separately by the dual formula
Ψ(x) = e^{−x/2}Σ_m u(me^{−x}) (prolate ODE to ξ = 8πλ³, 14-order edge series and Bernoulli closed forms beyond, as
schur_coupling_tail.py), on a uniform midpoint grid of step h on (−T − L, −T); all bilinear forms are 11×11 Gram matrices:
𝒜_∞ by FFT cross-correlations and trapezoid in u with the closed-form tail ∫_L^∞K, 𝒞 over all prime powers n < e^L,
A and B with the closed-form sawtooth remainder of B beyond −T − L; window masses ⟨Eψ_i, Eψ_j⟩ by Gauss on the pieces
between T − log n. tools/rung_gram_schur.py: all linear algebra in 60-digit arithmetic on the Gram matrices (entries of
very different size: ‖Ψ_{ψ_0}‖² ≈ 10⁻³⁸, ‖Ψ_{ψ_20}‖² = O(10⁻²) at T = 1).

Validation.
- Ψ_* from the tail formula against the finite Poisson sum e^{x/2}Σ_n f_*(ne^x) in 70 digits at three depths: 7 digits
  (e.g. T = 1, x = −1.7: 5.32632084·10⁻¹³ vs 5.326316864·10⁻¹³).
- u from the ODE table against the edge series at the switch point: relative 2·10⁻⁶ (T = 1), 4·10⁻⁷ (T = 0.8).
- Grid convergence (T = 1, unit survivor):

| h, L | 𝒜_∞[Ψ_*] | 𝒞[Ψ_*] | 𝒯[Ψ_*] | ρ = 𝒲̂[Ψ_*] |
|---|---|---|---|---|
| 10⁻⁴, 8 | 2.7325·10⁻²³ | 5.524·10⁻²⁴ | −1.6·10⁻²⁷ | 2.1799·10⁻²³ |
| 10⁻⁴, 10 | 2.7338·10⁻²³ | 5.527·10⁻²⁴ | −1.2·10⁻²⁷ | 2.1810·10⁻²³ |
| 5·10⁻⁵, 8 | 2.7373·10⁻²³ | 5.706·10⁻²⁴ | +1.1·10⁻²⁷ | 2.1667·10⁻²³ |

  The archimedean part is stable to 0.2 %, the comb to 3 % (linear interpolation of c^sym at log n across the dense kinks
  of the sawtooth tail), ρ to 0.6 %; L is irrelevant. The Tate term is at the noise level (|A(Ψ_*)| ≤ 0.005‖Ψ_*‖, B unstable
  in sign under h): |𝒯| ≤ 10⁻⁴ρ.
- Galerkin cross-check on the 3-dim admissible space of span{ψ_0 … ψ_12} (generalised eigenvalues of a_T against the window
  norm, Galerkin on truncated sine expansions of the E-images from cache/eproj_*.pkl vs the tail form):

| T | Nb | Galerkin | tail form (exact) |
|---|---|---|---|
| 1.0 | 80 / 120 / 160 | 2.695 / 2.403 / 2.265 ·10⁻²³; 1.553 / 1.458 / 1.346 ·10⁻²⁰; 2.207 / 2.020 / 1.882 ·10⁻¹⁷ | 2.062·10⁻²³; 1.245·10⁻²⁰; 1.783·10⁻¹⁷ |
| 0.8 | 45 / 67 / 90 | 8.33 / 7.96 / 8.03 ·10⁻¹²; 1.706 / 1.592 / 1.610 ·10⁻⁹; 8.51 / 8.41 / 8.18 ·10⁻⁷ | 7.43·10⁻¹²; 1.474·10⁻⁹; 7.31·10⁻⁷ |

  At T = 1 the Galerkin values decrease monotonically in Nb toward the tail values (the slow sine convergence of the jumpy
  E-images noted in 17A §2.2); the window masses agree exactly (ratio λ, the known factor of the eproj vectors). The tail
  form is the more accurate representation; the residual 8–10 % is the Galerkin truncation excess.

## 3. Task (1): exact ledger, rung Grams, exact Schur balance (NUMERICAL; h = 5·10⁻⁵, L = 8; spread to h = 10⁻⁴ in brackets)

### 3.1 The exact ledger of the survivor
| T | ‖Ψ_*‖² | 𝒜_∞[Ψ_*] | 𝒞[Ψ_*] | 𝒯[Ψ_*] | ρ = 𝒲̂[Ψ_*] | ρ/λ_A^Gal | ρ_Gal/λ_A^Gal (17A) |
|---|---|---|---|---|---|---|---|
| 0.8 | 3.367·10⁻¹² | 1.0821·10⁻¹¹ | 2.595·10⁻¹² (2.538) | noise | 8.226·10⁻¹² (8.272) | 1.377 (1.385) | 1.578 |
| 1.0 | 7.536·10⁻²⁴ | 2.7373·10⁻²³ | 5.706·10⁻²⁴ (5.524) | noise | 2.167·10⁻²³ (2.180) | 1.345 (1.353) | 1.489 |
λ_A^Gal = 5.974·10⁻¹² (T = 0.8, Nb 90), 1.611·10⁻²³ (T = 1, Nb 160). In units of the tail mass: 𝒜_∞/‖Ψ_*‖² = 3.21 / 3.63,
𝒞/‖Ψ_*‖² = 0.77 / 0.76, ρ/‖Ψ_*‖² = 2.44 / 2.88 (T = 0.8 / 1). The exact ledger lies 13 % / 10 % below the truncated
Galerkin value of 17A (same direction as the Galerkin excess of §2) and above λ_A^Gal, as it must (Rayleigh).
Reading: on the survivor's tail the comb is a 24 % / 21 % correction to the archimedean energy; the Tate term vanishes to
the accuracy of the tool. The ledger is not a near-cancellation of comparable terms.

### 3.2 Rungs and their 2×2 tail Grams
Complement of F = Ef_*/‖Ef_*‖ in the admissible E-images of span{ψ_0 … ψ_20} (dimension 6), diagonalised by the tail form;
μ_g = a_T(G) (unit G ⊥ F), b_g = a_T(F, G), s_g = b_g²/(μ_gρ), "F-odd" = window mass of the ψ_{4j+2} components (≈ 1:
odd sector rung).

T = 1.0:
| rung | μ_g | b_g | s_g | det₂/(ρμ_g) | F-odd | 17A Galerkin complement |
|---|---|---|---|---|---|---|
| o₁ | 1.200·10⁻²⁰ | 5.48·10⁻²³ | 0.0115 | 0.9885 | 1.0 | 9.1·10⁻²¹ (odd) |
| **g₁** | 1.589·10⁻¹⁷ | −2.35·10⁻²¹ | 0.0161 | 0.9839 | 4·10⁻⁵ | 1.2·10⁻¹⁷ (ev) |
| o₂ | 4.817·10⁻¹⁵ | −1.87·10⁻²⁰ | 0.0034 | 0.9966 | 1.0 | — |
| **g₂** | 1.863·10⁻¹² | 8.96·10⁻¹⁹ | 0.0199 | 0.9801 | 1·10⁻⁴ | 1.3·10⁻¹² (ev) |
| o₃ | 2.755·10⁻¹⁰ | 1.59·10⁻¹⁸ | 0.0004 | 0.9996 | 1.0 | — |
| g₃ | 5.687·10⁻⁸ | 1.75·10⁻¹⁶ | 0.0248 | 0.9752 | 8·10⁻⁵ | 3.8·10⁻⁸ (ev) |

T = 0.8:
| rung | μ_g | b_g | s_g | det₂/(ρμ_g) | F-odd | 17A |
|---|---|---|---|---|---|---|
| o₁ | 1.351·10⁻⁹ | −7.80·10⁻¹² | 0.0055 | 0.9945 | 1.0 | |
| **g₁** | 7.060·10⁻⁷ | −6.68·10⁻¹⁰ | 0.0768 | 0.9232 | 7·10⁻⁵ | 6·10⁻⁷ (ev) |
| o₂ | 6.724·10⁻⁵ | 9.53·10⁻¹⁰ | 0.0016 | 0.9984 | 1.0 | |
| **g₂** | 4.227·10⁻³ | −2.77·10⁻⁸ | 0.0221 | 0.9779 | 3·10⁻⁴ | 3.3·10⁻³ (ev) |
| o₃ | 0.1205 | −4.7·10⁻⁹ | 0.0000 | 1.0000 | 1.0 | |
| g₃ | 1.053 | 1.30·10⁻⁷ | 0.0019 | 0.9981 | 0.02 | |

The even rungs g₁, g₂ are the directions 17A identified by eigenvalue scale (μ larger here by 1.2–1.5: the E-image
subspace is smaller than P_T). Entrywise split of the 2×2 Grams (T = 1):
| pair | 𝒜_∞ | 𝒞 | 𝒯 |
|---|---|---|---|
| (Ψ_*, Ψ_*) | 2.737·10⁻²³ | 5.71·10⁻²⁴ | ~10⁻²⁷ |
| (Ψ_*, Ψ_{g₁}) | (rung o₁: 1.56·10⁻²²; g₁: −4.7·10⁻²¹) | (o₁: 1.01·10⁻²²; g₁: −2.3·10⁻²¹) | ≤ 10⁻²⁴ |
| (Ψ_{g₁}, Ψ_{g₁}) | 1.78·10⁻¹⁷ | 1.87·10⁻¹⁸ | ~10⁻²² |
On the off-diagonal the comb is 50–65 % of the archimedean entry and has the same sign: it reduces the coupling.

### 3.3 Exact Schur balance on the E-images
| T | ρ | Σ_g s_g (all 6 rungs) | ρ − bᵀC⁻¹b = Ritz minimum on the 7-dim E-image space | λ_A^Gal | ratio |
|---|---|---|---|---|---|
| 0.8 | 8.226·10⁻¹² | 0.108 | 7.338·10⁻¹² | 5.974·10⁻¹² | 1.23 |
| 1.0 | 2.167·10⁻²³ | 0.076 | 2.002·10⁻²³ | 1.611·10⁻²³ | 1.24 |
(Secular check: Schur value and direct Ritz minimum agree to 2·10⁻⁵ relative.) Consistency with λ_A: both numbers are upper
bounds for λ_A(T); the E-image space of ψ_0 … ψ_20 recovers the even-rung coupling but not the whole correction. The
missing (1 − 1/1.24)·ρ_exact ≈ 0.19–0.26 ρ is carried by directions of P_T outside E(span{ψ_0 … ψ_20}); the odd E-images
(ℱ-odd prolates ψ_{4j+2}) carry only 0.6–1.5 % of ρ, so the parity defect (P) of 17A (0.13–0.16 ρ) does not live on E-images
of low ℱ-odd prolates. Even-rung share: 0.078 + 0.022 (T = 0.8), 0.016 + 0.020 + 0.025 (T = 1) — the rung piece (R) is
2–10 % of ρ on the exact survivor, the low end of the 0.05–0.24 range of 17A.

## 4. Task (2): the collapsed-weight test log N → c·log N in the tail form only (NUMERICAL, plus one PROVED reduction)

By Lemma 1.1 the test form is 𝒲̂^c = 𝒜_∞ − c𝒞 + 𝒯 on the frozen pair (Ψ_*, Ψ_g); det₂(c) is a quadratic polynomial in c
with leading coefficient det(𝒞-Gram on the pair). Normalised determinants det₂(c)/(ρ^c μ_g) (rungs frozen at c = 1), and
the full re-optimised Schur value on the 7-dim E-image space:

T = 1.0 (g₁: μ = 1.59·10⁻¹⁷, g₂: μ = 1.86·10⁻¹²)
| c | ρ^c/ρ | det₂(g₁) | det₂(g₂) | Schur value (re-optimised) |
|---|---|---|---|---|
| 0 | 1.263 | 1.069 | 1.091 | 2.228·10⁻²³ |
| 0.5 | 1.132 | 1.028 | 1.037 | 2.125·10⁻²³ |
| 0.9 | 1.026 | 0.9931 | 0.9919 | 2.029·10⁻²³ |
| 0.99 | 1.0026 | 0.9849 | 0.9813 | 2.0048·10⁻²³ |
| 1 | 1 | 0.9839 | 0.9801 | 2.0020·10⁻²³ |
| 1.01 | 0.9974 | 0.9830 | 0.9789 | 1.9993·10⁻²³ |
| 1.1 | 0.9737 | 0.9745 | 0.9682 | 1.9735·10⁻²³ |
| 2 | 0.7366 | 0.8776 | 0.8489 | 1.489·10⁻²³ |
Zeros of det₂(c): g₁ at c = 4.23 and 21.8, g₂ at c = 4.19 and 15.1 (h = 10⁻⁴: 4.38/22.0, 4.34/15.3); ρ^c = 0 at c = 4.80 (4.95).

T = 0.8 (g₁: μ = 7.06·10⁻⁷, g₂: μ = 4.23·10⁻³)
| c | ρ^c/ρ | det₂(g₁) | det₂(g₂) | Schur value |
|---|---|---|---|---|
| 0 | 1.315 | 0.9882 | 1.0429 | 8.147·10⁻¹² |
| 0.9 | 1.0315 | 0.9311 | 0.9852 | 7.444·10⁻¹² |
| 0.99 | 1.0032 | 0.9240 | 0.9787 | 7.349·10⁻¹² |
| 1 | 1 | 0.9232 | 0.9779 | 7.338·10⁻¹² |
| 1.01 | 0.9968 | 0.9224 | 0.9772 | 7.327·10⁻¹² |
| 1.1 | 0.9685 | 0.9149 | 0.9705 | 7.223·10⁻¹² |
| 2 | 0.6845 | 0.8120 | 0.8889 | 3.123·10⁻¹² |
Zeros of det₂(c): g₁ at 3.56 and 77.8, g₂ at 3.82 and 29.3 (h = 10⁻⁴: 3.65/79.8, 3.92/30.6); ρ^c = 0 at c = 4.17 (4.26).

Readings.
(i) At c = 1 ± 0.01 the normalised determinants move by 10⁻³; at c = 0.9 and 1.1 by < 10⁻². The 2×2 positivity, the
diagonal ledger and the whole Schur balance on the E-images survive every c in [0, 3.5] at both windows, including c = 0
(no comb at all). In each pair the comb Gram is positive definite (leading coefficient of det₂(c) positive: 5·10⁻⁴² /
9·10⁻³⁷ at T = 1), so det₂(c) > 0 on (−∞, c₋) with c₋ = 3.6–4.2: the only way to break the rung inequality in tail form is to
multiply the comb by about four.
(ii) The rung inequality is therefore comb-generic in the sense of rule 4 (a): it is not Λ-specific through Λ ∗ 1 = log,
and it is not a sign carrier. Task (3) (identity-plus-remainder for a Λ-specific rung inequality) does not arise.
(iii) Contrast with the window form (17A §3): there c = 1 + 5·10⁻²² (T = 1) already kills (★), first order, through the
radical defect X = 𝒞(Φ_{f*}, ·). On the same data the tail form tolerates |1 − c| ≈ 3. The whole c-sensitivity of (★) on
E-images sits in the identity a_T(Ef) = 𝒲̂[Ψ_f] (radicality of Φ_f for the true weight), none in the tail Gram.

**Remark 4.1 (bookkeeping of the robustness; definitions, NUMERICAL constants).** For a tail Ψ and a weight w ≥ 0 on prime
powers write 𝒜_∞[Ψ] = m_eff‖Ψ‖² and 𝒞_w[Ψ] = κ_w‖Ψ‖²; then 𝒲̂^w[Ψ] = (m_eff − κ_w)‖Ψ‖² + 𝒯[Ψ], and
|κ_w| ≤ Σ_n 2w(n)n^{−1/2}‖Ψ1_{(−∞,−T−log n)}‖/‖Ψ‖ (Cauchy–Schwarz on c^sym(log n); the shift by log n meets only the part of
the tail below −T − log n). No sign is claimed from this; it only names the two numbers that decide the test.
On the survivor m_eff = 3.21 / 3.63 and κ_Λ = 0.77 / 0.76 (T = 0.8 / 1): the tails are out-of-band chirps whose Fourier mass
sits where the archimedean symbol m(τ) = Re ψ(¼ + iτ/2) − log π is ≈ 3–4, while the comb sees only the overlap of the tail
with its own shifts by log n ≥ log 2, which lies in the deep, small part of the tail. Any weight with κ_w < m_eff keeps the
ledger positive; the rungs behave the same way. This is a frequency statement about the tails, blind to the arithmetic of w.

Falsifier test (rule 4) on the rung inequality in tail form: (a) cΛ — survives for c ∈ [0, 3.5] (computed); it therefore
fails rule 4 and is recorded as not a sign step. (b) a_P, (c) Beurling systems, (d) finite modifications were not run: (a)
already disqualifies the step. In each case the window form dies through the radical identity, as in 17A Prop 3.1.

## 5. Enlarged span through the transition (T = 0.8, ψ_0 … ψ_40, 2c/π = 19.7; NUMERICAL)
Same tools with nP = 21 (17-dim admissible E-image space; edge values φ_k(1) up to 6.3, Ψ_* identical to 7 digits):
- ρ unchanged (8.226·10⁻¹²); Schur share 0.132 (was 0.108 with ψ_0 … ψ_20); Ritz minimum 7.141·10⁻¹² against λ_A^Gal
  5.974·10⁻¹² (ratio 1.195). The new directions (ψ_22 … ψ_40, μ_g = 0.11 … 3.4) add 0.024 ρ in total, none more than 0.007 ρ.
- Rungs g₁, g₂ stable (μ = 6.89·10⁻⁷, 4.04·10⁻³; s = 0.075, 0.025). Collapsed-weight test: det₂(g₁) zeros at c = 3.67 and 145,
  det₂(g₂) zeros at c = −212 and 3.94 (comb Gram indefinite on this pair, still positive on [0, 3.9]); re-optimised Schur
  value 7.764·10⁻¹² at c = 0, 7.141·10⁻¹² at c = 1. Same verdict.
- The missing part of the correction, 1 − 1/1.195 ≈ 0.16 of ρ_exact, matches the odd-sector parity defect (P) of 17A
  (0.126 ρ_Gal at T = 0.8): it needs window directions whose preimages under E carry structure at y ≈ e^{−T} (frequency
  ≈ Nb·π/(2T)/y in y) far beyond the prolate scale; E-images of prolates through the transition do not reach it.
  (ARGUED from the numbers; the preimage statement uses only that f ↦ Ef on (−T, T) depends on f|[e^{−T}, λ] and is
  inverted there by Möbius summation.)

## Result
NO-GO (class: "the rung piece (R) of the Schur inequality as a sign carrier — 2×2 positivity of the complete tail Gram on
{Ψ_*, Ψ_g} with the collapsed weight log N"), plus PROVED bookkeeping and the exact ledger.
The rung inequality survives log N → c·log N for every c ∈ [0, 3.5] at T = 0.8 and 1.0 (with the comb removed entirely it
holds with a larger margin); its determinant first vanishes at c ≈ 3.6–4.2. It is comb-generic (rule 4 (a)), so it cannot carry
the sign; task (3) does not arise. The Λ-specific content of (★) on E-images is the identity a_T(Ef) = 𝒲̂[Ψ_f] itself: on
the same data the window form dies at |1 − c| ≈ 5·10⁻²² (17A) while the tail form tolerates |1 − c| ≈ 3.

### What was proved
- Lemma 1.1: the collapsed-weight change log N → c log N on tails is exactly the scaled comb 𝒜_∞ − c𝒞 + 𝒯 on tails, and
  differs from the window form a^c_T on Ef by the radical defect (1 − c)𝒞(Φ_f, ·).
- Lemma 1.2: (4.1) of 17A on span{Ef_*, Eg} ⟺ nonnegativity of the 2×2 complete tail Gram determinant; rung share formula.
NUMERICAL (tools validated to 7 digits on Ψ_*, grid-converged to 0.6 % on ρ and 3 % on the comb):
- exact ledger ρ = 𝒲̂[Ψ_*] = 8.23·10⁻¹² (T = 0.8), 2.17·10⁻²³ (T = 1); ρ/λ_A^Gal = 1.38 / 1.35 (17A truncated: 1.58 / 1.49);
  𝒜_∞ : 𝒞 : 𝒯 = 3.2 : 0.77 : 0 (T = 0.8), 3.6 : 0.76 : 0 (T = 1) in units of ‖Ψ_*‖²;
- rung Grams: even rungs μ = 7.1·10⁻⁷, 4.2·10⁻³ (T = 0.8), 1.59·10⁻¹⁷, 1.86·10⁻¹² (T = 1); shares 0.077, 0.022 / 0.016, 0.020;
  normalised determinants 0.92–0.98; odd E-image rungs ≤ 0.012;
- exact Schur balance on E-images: ρ − bᵀC⁻¹b = 7.34·10⁻¹² / 2.00·10⁻²³ (ψ_0 … ψ_20), 7.14·10⁻¹² (ψ_0 … ψ_40, T = 0.8), above
  λ_A^Gal by 1.20–1.24: consistent (both are upper bounds), the remainder being the parity piece outside the E-images of
  prolates;
- Galerkin on truncated E-images converges monotonically (T = 1) toward the tail-form values; excess 8–10 % at Nb = 160.

### What failed and why
- The hypothesis that the rung piece is Λ-specific through Λ ∗ 1 = log: the tail form on the survivor and its rungs is an
  archimedean energy of out-of-band chirps (m_eff ≈ 3.2–3.6) with a comb correction of ≈ 0.77 and a vanishing Tate term;
  scaling the comb by c changes the 2×2 determinants by O(|1 − c|·10⁻¹) and breaks them only near c ≈ 4.
- The 33–37 % Schur share of 17A is not reproduced on E-images of prolates: exact survivor 8–13 % (rungs ≈ 2–10 %), the
  remainder being the parity/stiff piece, which E-images of ψ_0 … ψ_40 do not reach.

### Next concrete step
The Λ-dependence of (★) on E-images is now located entirely in the identity a_T(Ef) = 𝒲̂[Ψ_f] (radicality of Φ_f) and in
the part of P_T not reached by E-images of prolates. Compute, at T = 0.8, the Schur coupling of the survivor to the window
directions of the parity piece (P) in their E-preimage form f = E⁻¹G (Möbius inversion on [e^{−T}, λ]), i.e. evaluate
𝒲̂ on the tails of those preimages, to decide whether (P) also has a comb-robust tail form (then the full low-block
balance is comb-blind in tail form, and every sign test must be put on the identity — the first-level radical lemma of
ROUND_001_B — rather than on any Gram), or whether (P) is the one piece where the tail form itself sees Λ.

## Index row and ledger line
Index (05-meta-and-planning/ROUTES-TRIED-INDEX/README.md): row P211-18B. Ledger (LEDGER.md): line C39.
Tools: tools/rung_gram_prep.py, tools/rung_gram_tail.py, tools/rung_gram_schur.py (caches cache/rung_*).
