# Round 12 B — Three-block class-split assembly of the high prolate block; the class structure of the coupling

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_009_B / ROUND_011_B: λ = e^T, N = λ², c = 2πN, ψ_k the k-th
prolate of [−λ, λ] (unit L² norm on the interval), χ_k its concentration, d_k = 1 − χ_k, ε_k = i^k (even k), E the
summation map, Φ_f, Ψ_f = Φ_f1_{(−∞,−T)} as in ROUND_001_B, 𝒲 the full-line Weil form, ℓ_g the gauge-minimised leakage
(tools/prolate_gauge_adm.py). Blocks: LM = even k ≤ 4N; H₊ = k > 4N, k ≡ 0 (4); H₋ = k > 4N, k ≡ 2 (4); each block is
admissible on its own (the five linear conditions f(λ) = f(0) = ∫f = A(Ef) = B(Ef) = 0 imposed inside the block).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Index rows read: P211-9B (selection rule, Thms 1.1/1.2/1.5), P211-10A, P211-11A, P211-11B (two-block LM/HI Schur NO-GO:
do not retry the two-block assembly with block-diagonal ℓ_g normalisation), P211-11C; REVIEW_008 §4 (cross term
= −𝒲(Ψ_{f+}, w_−), a_T(w_+, w_−) ≡ 0 by parity); phase 199 PROOF_L_SHARP_A_001 Thm 1.1 (W_T(Ef) = 𝒲 on the aliasing tail,
the tail built from the out-of-band part of ℱf) and ROUND_001_B Thm 1.1 / Cor 1.2 (𝒲(Φ_f, ·) = 0 on Φ_{f′}, Ψ_{f′}).
What differs. (i) The assembly splits the high block by ℱ-class: three diagonal blocks and three couplings instead of
one HI block; this is the step named in 11B and is not on record. (ii) The exterior-tail identity is used in its
bilinear form together with the whole-line Slepian eigen-equation, which turns the prolate class into an exact sign on
the tail data (Theorem 1.1 below). The recorded tail identity (199 A_001) is scalar and class-blind; the selection rule
of 9B is about window parity and is void for d_k ≈ 1. Neither identifies the high cross-class coupling. No sign is
claimed from the class structure (9B §3: it is Λ-free), so no recorded NO-GO is retried.

## 1. The class structure of the form on admissible prolate data (pure mathematics)

### 1.0 Two inputs
(S) CITED (Slepian–Pollak 1961, the finite Fourier eigen-equation holds for every real argument). With c = 2πλ², each
ψ_k extends to an entire function φ_k on ℝ, band-limited to [−λ, λ], equal to ψ_k on [−λ, λ], and
    ℱ(ψ_k1_{[−λ,λ]})(ξ) = ε_k √χ_k φ_k(ξ)      for every ξ ∈ ℝ  (not only on the band).
Consequences (PROVED from (S) and Plancherel): ‖φ_k‖²_{L²(ℝ)} = 1/χ_k (since ‖ℱψ_k‖ = 1); the out-of-band data
u_k := √χ_k φ_k 1_{|ξ|>λ} satisfy ⟨u_j, u_k⟩ = δ_{jk} d_k (double orthogonality: ⟨φ_j, φ_k⟩_ℝ = δ_{jk}/χ_k and ⟨φ_j, φ_k⟩_band
= δ_{jk}). This is Theorem 1.2 of ROUND_009_B extended off the band, with the class sign factored out.
(T) PROVED in ROUND_001_B (Thm 1.1, Cor 1.2) and recorded in 199 A_001: for f, g admissible at T, 𝒲(Φ_f, Φ_g) =
𝒲(Φ_f, Ψ_g) = 0, Ef = Φ_f − Ψ_f, and Φ_f(x) = e^{−x/2}Σ_{k≥1}ℱf(ke^{−x}) (Poisson; the two boundary terms vanish because
f(0) = ℱf(0) = 0).

### Theorem 1.1 (sign conjugation of the high block; PROVED given (S), (T))
Let 𝒯h(x) := 1_{(−∞,−T)}(x)·e^{−x/2}Σ_{n≥1}h(ne^{−x}) (tail map, defined for even h = O(ξ^{−2})). For admissible
f = Σ a_kψ_k, g = Σ b_kψ_k (finite sums of even prolates, any classes),
    W_T(Ef, Eg) = Σ_{j,k} a_j b_k ε_j ε_k 𝒢_{jk},       𝒢_{jk} := 𝒲(𝒯u_j, 𝒯u_k).
So on any admissible coefficient subspace (basis Z), M = Zᵀ S 𝒢 S Z with S = diag(ε_k): the numerator of the
gauge quotient is the class-sign conjugate of a class-blind Gram matrix 𝒢 of exterior tails of the out-of-band data.
*Proof.* W_T(Ef, Eg) = 𝒲(Ef, Eg) (both supported in Ī_T, comb terms with log n ≥ 2T vanish) = 𝒲(Φ_f − Ψ_f, Φ_g − Ψ_g)
= 𝒲(Ψ_f, Ψ_g) by (T) three times. For x < −T and k ≥ 1, ke^{−x} > λ, so Ψ_f = 𝒯(ℱf) only samples ℱf off the band, where
ℱf = Σ a_kε_k√χ_kφ_k = Σ a_kε_ku_k by (S); 𝒯 is linear and the sums are finite. Bilinearity of 𝒲. ∎

### Corollary 1.2 (exact identification of the H₊–H₋ coupling; PROVED)
With Z₊, Z₋ admissible bases of H₊, H₋: M_{++} = Z₊ᵀ𝒢_{++}Z₊, M_{−−} = Z₋ᵀ𝒢_{−−}Z₋, M_{+−} = −Z₊ᵀ𝒢_{+−}Z₋. In every
normalisation that is invariant under coefficient sign changes (D = diag d_k; the operator norm), ‖M_{+−}‖ = ‖Z₊ᵀ𝒢_{+−}Z₋‖.
Hence the ℱ-class gives the high-class coupling an exact sign and no small factor: the coupling of the two high classes
is minus the tail-Gram coupling of the interleaved indices k ≡ 0 and k ≡ 2 (mod 4).
Reading against the selection rule. Theorem 1.1 of 9B (P_{−ε}Π_TEf = ½RΠ_TE(ℱf − εf)) is the same Poisson identity seen in
the window; its smallness factor is the Fourier defect ‖ℱf − εf‖² = Σ2(1 − εε_k√χ_k)a_k² (9B Thm 1.2), which for k > 4N
(χ_k → 0) equals 2Σa_k² — no selection. Corollary 1.2 is the exact statement of what replaces it above the plunge: the
class survives only as the sign ε_k on the out-of-band data u_k, and the summation map sends class −1 data to the
negatives of what it sends the same out-of-band profile in class +1. So the expectation that "the summation map sends class
−1 data to near-orthogonal images" is FALSE in general: the images of ψ_k, ψ_{k+2} (opposite classes) have exterior tails
−𝒯u_{k+2}, +𝒯u_k, and their overlap is the tail overlap 𝒢_{k,k+2}, not a defect product. (NO-GO for any proof of
smallness of the high cross-class coupling from the selection rule or from ℱ-class symmetry; reason: Corollary 1.2.)

### Corollary 1.3 (what the class mixing does; PROVED)
For a₊ supported on H₊ and a₋ on H₋ (S = +1 on H₊, S = −1 on H₋), Theorem 1.1 gives exactly
    M(a₊ + a₋) = 𝒢[a₊ − a₋],
i.e. M on the joint span is 𝒢 evaluated at the coefficient vector with the class −1 part negated. The leakage D = Σd_ka_k²
is invariant under that negation; the gauge correction (overlaps J_{k·} = ⟨ψ_k, gauge⟩) and the admissibility conditions
∫f = Σ a_kε_k√χ_kφ_k(0) are not. Therefore the decrease of α_HI(K) relative to the flat per-class values is the Rayleigh
quotient of the class-blind tail Gram 𝒢 on alternating-sign vectors over interleaved indices, i.e. the near-cancellation
𝒯u_k − 𝒯u_{k+2} of neighbouring exterior tails. This is the precise form of "the decrease comes from mixing the two classes".

### Proposition 1.4 (low–high coupling; PROVED shape, constants CONDITIONAL)
For f_L admissible in LM and f admissible in H₋ (or H₊): M(f_L, f) = ±𝒲(Ψ_{f_L}, Ψ_f) with Ψ_{f_L} = Σ_{k≤4N} a_kε_k𝒯u_k.
For two functions Ψ, Ψ′ supported in (−∞, −T] with |Ψ(y)| ≤ C_Ψe^{3(y+T)/2}, the Lévy form and the comb give
    |𝒲(Ψ, Ψ′)| ≤ (|C₀| + 0.7)‖Ψ‖‖Ψ′‖ + ¾‖Ψ‖_∞‖Ψ′‖_∞ + 2(−ζ′/ζ)(3/2)·(C_Ψ‖Ψ′‖ + C_{Ψ′}‖Ψ‖)
(archimedean part as in 9B Lemma 1.6(a) with the local term C₀⟨Ψ, Ψ′⟩ now present; comb: the shift by log n moves
mass of size ≤ C·n^{−3/2}·… onto the other function, and Σ_nΛ(n)n^{−1/2}·n^{−1} = (−ζ′/ζ)(3/2) — the factor 2 covers both
shifts; ARGUED in the constant, PROVED in shape). With Lemma 1.3 of 9B (s = 1) applied to the out-of-band data,
‖Ψ_{f_L}‖ ≤ ζ(2)^{1/2}λ‖ξ·Σa_kε_ku_k‖, so the low factor is a weighted out-of-band norm of the low datum, ≍ its leakage
up to poly(N) on mollified data (ROUND_009_A, CONDITIONAL). The high factor has no small parameter (d_k ≈ 1). In
ℓ_g-normalised units the low–high coupling is therefore bounded by poly(N)·O(1) — a finite bound, but not a bound below
κ_LMα_±, which is what a Schur assembly needs. The sign-conjugation makes the L–H₊ and L–H₋ couplings the same tail
pairings with opposite signs on the high side; they are NOT separated in size by the class (NUMERICAL §2 confirms:
G_{L+} ≈ G_{L−}).

## 2. The three-block assembly (NUMERICAL)

Tool: tools/prolate_gauge_3blk.py (same objects, caches and switches as prolate_gauge_adm.py; working digits 30;
LAMA = 5.8443·10⁻¹² (T = 0.8), 1.47·10⁻²³ (T = 1.0); MIN = 12 gauge functions). Each block admissible on its own.
Columns: α_± = gen-min of (M, ℓ_g) on H_±; α_HI = the jointly admissible HI of 11B (for comparison); G_{L±}, G_{+−} =
operator norms of the couplings in block-diagonal ℓ_g normalisation; Dcross = the same norm for the ℓ_g cross blocks;
θ₃ = λ_min [[κ_LM, −G_{L+}, −G_{L−}], [−G_{L+}, α₊, −G_{+−}], [−G_{L−}, −G_{+−}, α₋]] (the three-block Schur bound);
θ₂ = the two-block bound of 11B; "true" = gen-min of (M, ℓ_g) on LM ⊕ H₊ ⊕ H₋; Ritz = inf W/‖Ef‖² ÷ λ_A on that span.
Points within 10% of the resolution cap k_* ≈ 0.32–0.35·Nb are marked *.

### 2.1 T = 0.8 (4N = 19.8, κ_LM = 2.12)
| Nb | top (K/4N) | dim₊/dim₋ | α₊ | α₋ | α_HI | G_{L+} | G_{L−} | G_{+−} | Dcross₊₋ | θ₃ | θ₂ | true | Ritz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 250 | 48 (2.4) | 3/2 | 2.04 | 2.25 | 1.22 | 0.34 | 0.38 | 1.15 | 0.005 | 0.79 | 0.71 | 1.41 | 1.46 |
| 300 | 52 (2.6) | 4/3 | 2.05 | 2.16 | 1.11 | 0.64 | 0.40 | 1.40 | 0.013 | 0.39 | 0.52 | 1.27 | 1.44 |
| 250 | 60 (3.0) | 6/5 | 2.02 | 2.13 | 1.05 | 0.84 | 0.87 | 1.81 | 0.036 | −0.33 | 0.42 | 1.13 | 1.39 |
| 300 | 62 (3.1) | 6/6 | 2.02 | 2.13 | 1.02 | 0.85 | 0.87 | 1.82 | 0.045 | −0.34 | 0.40 | 1.12 | 1.38 |
| 250 | 72 (3.6) | 9/8 | 1.99 | 2.13 | 0.86 | 0.88 | 0.88 | 2.22 | 0.16 | −0.70 | 0.24 | 1.11 | 1.36 |
| 300 | 72 (3.6) | 9/8 | 1.97 | 2.13 | 0.87 | 0.91 | 0.88 | 1.86 | 0.11 | −0.43 | 0.26 | 1.11 | 1.35 |
| 250 | 80* (4.0) | 11/10 | 1.92 | 2.04 | 0.81 | 0.98 | 0.89 | 2.82 | 0.36 | −1.34 | 0.11 | 1.10 | 1.35 |
| 300 | 80 (4.0) | 11/10 | 1.94 | 2.10 | 0.84 | 0.94 | 0.88 | 3.28 | 0.36 | −1.70 | 0.15 | 1.00 | 1.34 |
| 300 | 88* (4.4) | 13/12 | 1.93 | 2.06 | 0.80 | 0.99 | 0.88 | 4.70 | 0.80 | −3.04 | 0.006 | 0.98 | 1.34 |
| 300 | 92* (4.6) | 14/13 | 1.90 | 1.98 | 0.79 | 1.02 | 0.92 | 4.82 | 0.80 | −3.23 | −0.010 | 0.97 | 1.33 |

### 2.2 T = 1.0 (4N = 29.6, κ_LM = 3.12), Nb = 370
| top (K/4N) | dim₊/dim₋ | α₊ | α₋ | α_HI | G_{L+} | G_{L−} | G_{+−} | Dcross₊₋ | θ₃ | θ₂ | true | Ritz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 56 (1.9) | 2/2 | 2.96 | 2.94 | 1.82 | 0.58 | 0.77 | 0.89 | 0.0003 | 1.49 | 1.11 | 2.38 | 1.52 |
| 64 (2.2) | 4/4 | 2.95 | 2.92 | 1.52 | 1.02 | 0.84 | 1.80 | 0.0009 | 0.49 | 0.73 | 1.96 | 1.51 |
| 72 (2.4) | 6/6 | 2.95 | 2.91 | 1.33 | 1.11 | 0.86 | 2.59 | 0.010 | −0.24 | 0.39 | 1.61 | 1.49 |
| 80 (2.7) | 8/8 | 2.94 | 2.91 | 1.20 | 1.15 | 1.42 | 2.87 | 0.026 | −0.79 | 0.21 | 1.55 | 1.48 |
| 88 (3.0) | 10/10 | 2.94 | 2.91 | 1.09 | 1.49 | 1.47 | 3.05 | 0.052 | −1.15 | 0.10 | 1.48 | 1.46 |
| 96 (3.2) | 12/12 | 2.92 | 2.89 | 1.01 | 1.49 | 1.49 | 3.21 | 0.077 | −1.30 | 0.035 | 1.45 | 1.44 |
| 100* (3.4) | 13/13 | 2.91 | 2.83 | 0.98 | 1.50 | 1.49 | 3.44 | 0.091 | −1.53 | 0.003 | 1.43 | 1.42 |

### 2.3 Readings
(i) Each high class on its own is K-uniformly coercive on the resolved range: α₊ ≈ 1.9–2.05 and α₋ ≈ 2.0–2.25 at T = 0.8,
α₊ ≈ 2.91–2.96 and α₋ ≈ 2.83–2.94 at T = 1.0, drifting by ≤ 7% across K/4N = 1.9–4.6. New: class −1 alone is as flat as
class +1 (11B had measured class +1 only).
(ii) The coupling that grows is G_{+−}, the coupling between the two high classes: 1.15 → 2.8 (T = 0.8, Nb = 250, resolved)
and 0.89 → 3.44 (T = 1.0), roughly linear in the number of interleaved pairs, and it exceeds √(α₊α₋) at K ≈ 3.6·4N
(T = 0.8) and K ≈ 2.4·4N (T = 1.0). The low–high couplings saturate: G_{L±} ≈ 0.9–1.0 (T = 0.8), ≈ 1.5 (T = 1.0), with
G_{L+} ≈ G_{L−} (Proposition 1.4: same tail pairings, opposite signs).
(iii) θ₃ < θ₂ beyond K ≈ 2.5·4N at both T, and θ₃ turns negative at K ≈ 3·4N (T = 0.8) and ≈ 2.4·4N (T = 1.0): the
class-split three-block Schur assembly is WORSE than the two-block one. NO-GO for K-uniform θ₃.
(iv) The form itself stays positive on the same span: true gen-min 0.97–1.41 (T = 0.8), 1.43–2.38 (T = 1.0); Ritz bottom
1.33–1.52 λ_A. As in 11B, the failure is of the decoupling inequality, now localised in one coupling, not of the sign.
(v) The ℓ_g cross block between H₊ and H₋ becomes O(1) near the cap (0.36–0.80 at T = 0.8, k ≥ 80): at those points the
block-diagonal normalisation is itself unreliable; the resolved points (Dcross ≤ 0.16) already show θ₃ < 0.

### 2.4 Control: split the high block by index range instead of class (SPLIT=range; H_a = lower half, H_b = upper half)
| T | top | α_a | α_b | G_{La} | G_{Lb} | G_{ab} | θ₃(range) | θ₃(class) | true |
|---|---|---|---|---|---|---|---|---|---|
| 0.8 (Nb 250) | 60 | 1.54 | 1.96 | 0.64 | 0.86 | 0.21 | 0.72 | −0.33 | 1.39 |
| 0.8 | 72 | 1.34 | 1.74 | 0.78 | 0.91 | 0.45 | 0.29 | −0.70 | 1.14 |
| 0.8 | 80* | 1.22 | 1.63 | 0.84 | 0.91 | 0.61 | 0.057 | −1.34 | 1.02 |
| 1.0 (Nb 370) | 64 | 2.42 | 2.45 | 0.86 | 1.11 | 0.13 | 1.26 | 0.49 | 2.37 |
| 1.0 | 80 | 2.06 | 2.00 | 1.14 | 1.52 | 0.20 | 0.47 | −0.79 | 1.88 |
| 1.0 | 96 | 1.71 | 2.37 | 1.33 | 1.58 | 0.82 | −0.10 | −1.30 | 1.58 |
| 1.0 | 100* | 1.52 | 2.21 | 1.38 | 1.59 | 0.88 | −0.32 | −1.53 | 1.39 |
Reading. Cutting by index range keeps the inter-block coupling 4–15 times smaller than cutting by class (G_{ab} 0.13–0.88
vs G_{+−} 1.8–3.4), consistent with Corollary 1.3: the strong bonds of the tail Gram join neighbouring indices, which the
class cut severs and the range cut mostly keeps inside blocks. The price is that each range block contains both classes
and its own bottom decreases (1.54 → 1.22; 2.42 → 1.52). The range split also turns negative (T = 1.0, K ≈ 3.2·4N).
Neither three-block cut is K-uniform.

## 3. Falsifier test
Theorem 1.1 and Corollaries 1.2–1.3 are identities, not sign steps. Their inputs behave differently: (S) is weight-free;
(T) uses the radical relation 𝒲(Φ_f, ·) = 0, which is specific to Λ (ROUND_001_B §3). For a weight w,
W^w_T(Ef, Eg) = 𝒲^w(Ψ_f, Ψ_g) + 𝒫_{Λ−w}(Ef, Eg) − 𝒫_{Λ−w}(Ψ_f, Ψ_g) (polarised ROUND_001_B Cor), and the middle term has
no S-conjugation structure: Theorem 1.1 fails as stated for (a) cΛ, (b) a_P, (d) finite modifications (nonzero 𝒫_{Λ−w}),
and for (c) Beurling systems with the plain map E (radical relation lost; with the system's own map the analogue of (T)
holds but Poisson (1.0) and hence (S)-transport are additive-specific to ℕ). The identity therefore uses Λ, but it carries
no sign and is not used as a sign step.
NUMERICAL (T = 0.8, Nb = 250): under 1.01Λ the high blocks are unchanged to 3 digits (α₊ 2.006/1.906 vs 2.024/1.921, G_{+−}
1.80/2.81 vs 1.81/2.82 at top 60/80); under a_3 both high classes stiffen (α₊ 3.11/2.65, α₋ 3.20/2.85) and G_{+−} grows
too (2.46/3.60); both are rejected only in LM (κ_LM = −2.2·10⁸ and −1.9·10⁷; Ritz −1.2·10⁹ and −8.6·10¹⁰ in units of λ_A).
The high range does not distinguish Λ from its falsifiers; any sign step must live in LM or in its coupling.

## 4. Reduction status
θ₃ is not K-uniform, so no reduction of (★) to the low block plus three inequalities is written. The obstruction is one
named coupling: H₊–H₋, which by Corollary 1.2 is exactly −𝒲(𝒯u_j, 𝒯u_k) between interleaved indices j ≡ 0, k ≡ 2 (mod 4)
above the plunge; it grows roughly linearly in the number of interleaved pairs and exceeds √(α₊α₋) at K ≈ 3.6·4N
(T = 0.8) and 2.4·4N (T = 1.0). The per-class bottoms (flat) and the low–high couplings (saturating at 0.9–1.5) are not the
problem.
Consequence for any assembly (PROVED by Theorem 1.1 and Cor 1.3): since M = S𝒢S and D is S-invariant, the class is a sign
gauge of the problem above the plunge; a block decomposition of the high range should be made in the class-blind variable
b = Sa and cut where 𝒢 is weak, along the index (frequency) axis, not along the class. The ℓ_g gauge correction and the
integral constraint are the only non-S-invariant pieces.

## Result
NO-GO (class: three-block LM/H₊/H₋ Schur assembly with block-diagonal ℓ_g normalisation, NUMERICAL) for a K-uniform θ₃;
it is worse than the two-block assembly. PROVED piece: Theorem 1.1 (sign conjugation M = S𝒢S of the form on admissible
prolate data; the ℱ-class acts as an exact sign on out-of-band data), Corollary 1.2 (exact identification of the high
cross-class coupling, no small factor: NO-GO for smallness from the selection rule) and Corollary 1.3.

### What was proved
- Theorem 1.1, Corollaries 1.2, 1.3: PROVED given the CITED whole-line Slepian eigen-equation and ROUND_001_B Thm 1.1.
- Proposition 1.4: the low–high coupling is a tail pairing bounded by a weighted out-of-band norm of the low datum times an
  O(1) high factor (shape PROVED; constants ARGUED; leakage comparison CONDITIONAL on ROUND_009_A); not below κ_LMα_±.
- NUMERICAL: α₊, α₋ each flat (≈ 2.0/2.1 at T = 0.8, ≈ 2.9/2.9 at T = 1.0); G_{+−} grows 0.9 → 3.4; G_{L±} saturate;
  θ₃ < 0 from K ≈ 3·4N (T = 0.8) / 2.4·4N (T = 1.0) while the true infimum stays 1.0–1.4 and the Ritz bottom 1.33–1.52 λ_A.

### What failed and why
- K-uniform θ₃: G_{+−}² > α₊α₋ beyond K ≈ 3.6·4N / 2.4·4N. Reason (Cor 1.2–1.3): the class cut severs the
  nearest-neighbour bonds of the class-blind tail Gram 𝒢.
- Smallness of the H₊–H₋ coupling from the selection rule: impossible (Cor 1.2; the Fourier defect equals 2‖a‖² above
  the plunge).
- Range-split control: coupling 4–15× smaller, but block bottoms decrease; negative at T = 1.0, K ≈ 3.2·4N.

### Next concrete step
Work in the class-blind variable b = Sa with the tail Gram 𝒢: measure its band structure in ℓ_g-normalised units (is
𝒢 − κℓ_g diagonally dominant along k, neighbour bonds ≤ ½ diagonal?) and replace block Schur by a banded sweep along the
index axis; in parallel express 𝒢_{jk} through the packet symbol of ROUND_011_A/011_C (the 𝒯u_k are packets above the
plunge), so that the neighbour bond becomes the packet overlap governed by m − P^ρ_T.

## Reproducibility
KLIST=<tops> LAMA=<λ_A> FASTMUL=1 [SPLIT=range] [PROFILE=1] python3 tools/prolate_gauge_3blk.py T Nb 30 KMAX 12 [w].
Runs: (0.8, 250, 100; tops 48–80), (0.8, 300, 120; 52–92), (1.0, 370, 148; 56–100), SPLIT=range (0.8, 250; 60–80) and
(1.0, 370; 64–100), falsifiers w ∈ {1.01, a3} at (0.8, 250; 60, 80). Each run ≤ 900 s, one core.
PROFILE (T = 0.8, Nb = 250): the top singular pair of the normalised H₊–H₋ coupling is spread over the high range with
weight on neighbouring index pairs (top 80: k = 56–76 in H₊ against 58–74 in H₋); singular values 2.82, 1.86, 1.62, 1.42:
several O(1) directions, not one rogue mode.
