# MECH_001 — from the structure of Mori's certificates to a statement for every T

Phase 199 memo, pen and paper. The only computation is trivial arithmetic: sums of Λ(n)/√n over n < μ,
exponentials, and the PATTERN_001 model numbers. No audit yet.
Notation: μ = e^{2T}, λ = √μ = e^T,
L = T, c = 2πμ (prolate bandwidth·time), I = [−T,T], and W_T is the complete form (Mori's Q, AUDIT_ZENODO §0).

## Corpus check
- **Index, read.** ROUTES-TRIED-INDEX README: "Frontera certificada", "Relevamiento " (C1), the six-clause
  specification, phases 194–198, BARRIER_EST_001, PATTERN_001. Also 05b L104–L108, L81 and 06 (Möbius transport N_006,
  L2_017). AUDIT_ZENODO_FRONTIER, PATTERN_001.
- **Sources, read.** Mori VIII (log 15, 23281236). Mori VII (log 12 + Theorem N, 23265728), downloaded to the
  scratchpad `zen/moriVII.txt`. Mori VI (log 10, 23238480), `zen/moriVI.txt`. Guo (23297284), §1. Paper 46 lem:monoT,
  prop:env, rem:moriceiling.
- **Why this is not a retry.**
  - §1–§2 are a scaling analysis, not a construction.
  - §3 (Lemma L′) is the precise form of the target that PATTERN_001 §3 left unstated ("inverse estimate for the
    residual identity"). It differs from C1/L81 for two reasons. (a) It asks for no sign from gluing. It asks for
    coercivity of W_T with respect to prolate leakage, a comparison with a known archimedean quantity. (b) The Möbius
    bijection (Prop 3.1) makes it a statement about **all** of L²(I), not only about prolate images.
  - §4 shows that the residual identity is FE-generic (F-DH passes it). This is new and narrows where the Euler product
    must act.
  - No new construction is launched here.

## 1. Mori's proof as a chain, and how each constant scales with μ

Mori VII §3 / VIII §2. Every analytic step is stated for general L.

| step | content | dependence on μ | label |
|---|---|---|---|
| S0 | explicit formula, C² core, parity split | none | CITED (Mori VI §2), classical |
| S1 | prime operator: ‖C_p‖ ≤ s by weighted Schur; m > 0, γ = s+m, M = γI − C_p, mI ⪯ M ⪯ (2s+m)I | s grows (see Prop 1.1) | Schur test classical; values certified |
| S2 | archimedean tail: a(t) − γ ≥ C = log(Ω/2π) − 1/Ω − γ > 0 for \|t\| ≥ Ω | **forces Ω > 2π e^{γ}** | CITED (Mori VII (3.1)) |
| S3 | out-of-band defect: I − B_band ⪰ d(c_Ω), c_Ω = ΩL, d = e^{−2(c+1)}/(4(c+1)(c+4)) (Theorem N) | valid ∀c; constant e^{−2ΩL} | CITED (Mori VII Thm N; proof read, no gap seen) |
| S4 | Prop 3.1 + (2.1): Q ≥ Cδ‖f‖² + ⟨f,(M+V)f⟩ | valid ∀L | CITED |
| S5 | Legendre projection with N modes: errors e, n, h ~ e^{c_Ω(ρ−ρ⁻¹)/2}ρ^{−N} | needs N ≳ c_Ω | CITED (Mori VII Lemma 3.2) |
| S6 | block elimination: G⁻¹ + J ⪰ αI + βD_M ⇒ M + V ⪰ 0 | valid ∀L | CITED |
| S7 | **finite check** (2.2): T = W(X)⁻¹ + J − αI − β(B − A²) ≻ 0 in Arb | one μ at a time | NUMÉRICO-certified per μ |

**Proposition 1.1 (cost floor of the bounded-comparison class).**
(i) ‖C_p‖ ≤ A_T := Σ_{n<μ} 2Λ(n)/√n. **PROVED**: each S_a is a partial isometry.
(ii) Any admissible s satisfies s ≥ ‖C_p‖ ≥ ⟨v₀,C_p v₀⟩ = Σ_{n<μ} 2Λ(n)n^{−1/2}(1 − log n/log μ), because
⟨1_I, S_a 1_I⟩ = 2L − |a|. **PROVED.** Check: at μ = 15 this gives 3.31, and γ − 3.31 = 1.3127 = A₀₀. This matches
the audit.
(iii) By the PNT, ⟨v₀,C_p v₀⟩ = (8 + o(1))√μ/log μ. Partial summation gives
2∫₁^μ t^{−1/2}(1 − log t/log μ)dt = 8√μ/log μ − 4 − 8/log μ. **PROVED** (PNT CITED).
(iv) S2 needs Ω > 2π e^{γ} ≥ 2π e^{⟨v₀,C_p v₀⟩}. So Ω_min ≥ 2π exp((8+o(1))√μ/log μ). **PROVED** for this class.
(v) S5 needs N ≥ (1+o(1))·ΩL for the projection bound to be below 1. This holds because min_ρ (ρ−ρ⁻¹)/(2log ρ) = 1
as ρ → 1. **PROVED for Lemma 3.2's bound.** That any Legendre/Galerkin compression of the band [−Ω,Ω] needs
N ≳ ΩL·2/π is **ARGUED** (Landau).

So the cost of the method is **superpolynomial in μ**: N ≥ exp((8+o(1))√μ/log μ). This is the prop:env phenomenon:
Ω plays the role of τ_env = 2π e^{𝒜_T}. Constant absorption γI of the prime operator works frequency by frequency, and
the prime symbol reaches its sup at arbitrarily high frequency.

**Correction to PATTERN_001 §2.** "Certificate cost per window polynomial, ~μ⁴" holds for Galerkin resolution only. For
the Liu–Mori certificate the cost is at least exp(c√μ/log μ) (Prop 1.1, PROVED). The ratio of 5 between N_cert and
N_Gal at μ = 15 is the first sign of this.

### Scaling table (orders of magnitude, by hand)
How to read the table:
- s ranges from the Rayleigh floor (Prop 1.1(ii)) to the trivial bound A_T. Mori's Schur values fall inside: 3 at
  μ = 10, 3.56 at 12, 4.09 at 15.
- Ω = 2π e^{s+½} at the two ends of the s range.
- N_cert ≈ 1.67·ΩL, the ratio Mori found necessary (VIII Rem 3.1).
- Margin = 4.6 × Fuchs (PATTERN_001 model, NUMÉRICO).
- Bits to see the margin = −log₂ of the margin ≈ 18.1μ.
- N_Gal = 2.3·T·2πμ.

| μ | T | #contacts | s: floor … A_T | Ω | N_cert | N_Gal | margin λ^W | margin bits | 1/δ bits ≈ 2.9ΩL |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0.80 | 3 | 1.06 … 2.94 | 30 … 2·10² | 40 … 3·10² | 58 | ~1e−17 | ~56 | 70 … 460 |
| 10 | 1.15 | 7 | 2.37 … 7.08 (Mori 3) | 1.1·10² … 1.2·10⁴ | 2·10² … 2·10⁴ (Mori 640) | 166 | ~1e−43 (Mori 8.4e−44) | ~143 | 370 … 4·10⁴ |
| 16 | 1.39 | 9 | 3.47 … 9.94 | 3·10² … 2·10⁵ (Mori-type ≈ 800) | 8·10² … 5·10⁵ (≈ 2000) | 320 | ~3e−75 | ~248 | ~3·10³ … 9·10⁵ |
| 100 | 2.30 | 35 | 10.4 … 33.8 | 3·10⁵ … 5·10¹⁵ | 10⁶ … 2·10¹⁶ | 3.3·10³ | ~1e−529 | ~1.76·10³ | 2·10⁶ … 3·10¹⁶ |
| 1000 | 3.45 | 193 | 30 … 121 | 10¹⁴ … 4·10⁵³ | 10¹⁵ … 10⁵⁴ | 5·10⁴ | ~1e−5437 | ~1.8·10⁴ | 10¹⁵ … 10⁵⁴ |

**How each step behaves.**
- **Uniform in μ (logic and constants explicit ∀L):** S0, S3, S4, S6, and the Schur test itself.
- **Grows polynomially:**
  - the margin bits (≈ 4πμ/ln 2: the "precision ~ 4πμ bits" law);
  - the Galerkin resolution N_Gal ~ μ log μ.
- **Grows superpolynomially:** Ω, N_cert and the working precision (≈ 2N_cert bits for the Legendre/inverse
  conditioning), through S1 + S2.
- **What fails as μ → ∞:** no step fails logically. S7 is a finite verification for one μ, and its size grows like
  exp(c√μ/log μ). The method therefore never produces a statement for all μ. At μ = 100 it is already out of reach,
  at N ≥ 10⁶ and ≥ 2·10⁶ bits.
- The 1/δ bits are a symbolic constant and cost nothing.

## 2. The one essential inequality and its replacement for all μ

The Schur bound 4.0915 ≤ 66/16, the tail inequality and the projection lemmas are auxiliary. All of them are uniform
analytic statements; for the Schur bound, the trivial bound A_T suffices at a higher Ω. The **only** non-uniform input is
S7, the positivity of the Schur complement (2.2). By S6 this is a sufficient finite test for

  **(B_μ)  M_Ω + V_Ω ⪰ 0 on L²(I)**, that is, positivity of the Weil form whose archimedean symbol is lowered to the
  constant γ = s+m above Ω, plus the rank-2 term U.

The certified finite margins (2.4e−70 and 3.95e−66 at μ = 15; 8.4e−44 at μ = 10) are of the same order as λ^W
(NUMÉRICO, consistent with the AUDIT B1(c) model). So (B_μ) holds with margin on the Fuchs scale wherever it has been
tested.

**Lemma K_κ (OPEN).** There is κ₋ > 0 such that for every μ ≥ 5, and for Ω = Ω(μ) any value with C(Ω) > 0:
M_Ω + V_Ω ⪰ κ₋(1 − λ₄(2πμ)) I on L²(I).

**Proposition 2.1 (PROVED, given the CITED steps S3–S4, which are uniform in L).** K_κ implies
λ^W_T ≥ Cδ + κ₋(1−λ₄(2πμ)) > 0 for every T.
*Proof.* (2.1) gives Q ≥ Cδ‖f‖² + ⟨f,(M+V)f⟩. □

K_κ is the literal "certificate made uniform". Its weakness is that it is phrased in Mori's auxiliary operators, and
these carry the superpolynomial Ω. The intrinsic version is Lemma L′ below. It contains no Ω, γ or N.

## 3. The intrinsic lemma: leakage coercivity

**Summation map.** E f(x) = e^{x/2} Σ_{n≥1} f(n e^x) for x ∈ I. Here f is even, supported in [−λ,λ], and
f̂(ξ) = ∫ f e^{−2πixξ}. The leakage is leak(f) = ∫_{|ξ|>λ} |f̂|².

**Proposition 3.1 (Möbius bijection, PROVED, elementary).** E f depends only on f|_{[1/λ,λ]}. The map
E : L²([1/λ,λ], du) → L²(I, dx) is a bijection, with inverse f(u) = Σ_{m ≤ λ/u} μ(m)(mu)^{−1/2} g(log(mu)), and
‖E‖, ‖E⁻¹‖ ≤ 2λ = 2√μ.
*Proof.*
- Put u = e^x and H(u) = u^{−1/2} g = Σ_{n ≤ λ/u} f(nu). Since nu ≥ u ≥ 1/λ, only f on [1/λ,λ] enters.
- Σ_m μ(m) H(mu) = Σ_k f(ku) Σ_{m|k} μ(m) = f(u).
- ‖g‖_{L²(dx)} = ‖H‖_{L²(du)}, and ‖H(m·)‖ = m^{−1/2}‖H‖. Also Σ_{m≤μ} m^{−1/2} ≤ 2√μ.
- The bound for E is the same computation. □

So f on (−1/λ, 1/λ) is a **free gauge**. Every g ∈ L²(I) is a summation-map image. The additive structure of ℕ enters
through Poisson (Guo); the multiplicative structure enters through E and μ(m) (semiring principle).

**Lemma L′ (leakage coercivity, OPEN).** There are κ > 0 and A ≥ 0 such that for every μ ≥ 5 and every even f ∈ C²,
supported in [−λ,λ], with f(0) = f̂(0) = 0:

  W_T(E f) ≥ κ μ^{−A} · leak(f).

**Proposition 3.2 (PROVED, given L′).** Then for every T:
λ^W_T ≥ κ μ^{−A−1}(1−λ₀(2πμ))/4 ≥ κ μ^{−A−1} e^{−2(2πμ+1)}/(16(2πμ+1)(2πμ+4)) > 0.
*Proof.*
- Given g in the C² core, choose any admissible representative f = E⁻¹g on [1/λ,λ]. Fill (−1/λ,1/λ) to meet the two
  linear constraints; this is possible because the gauge is infinite-dimensional.
- leak(f) ≥ (1−λ₀(c))‖f‖². This is the prolate concentration bound with time·band = λ·λ, so c = 2πμ (CITED: Slepian,
  Landau–Pollak; explicit via Thm N).
- ‖f‖² ≥ ‖f|_{[1/λ,λ]}‖² ≥ ‖g‖²/(4μ) by Prop 3.1. □

**Why L′ is plausible and Λ-shaped (ARGUED).**
- Guo's Theorem 4.5 states that W_T(E f) is a residual that depends only on the out-of-band part of f̂ and on f(λ).
  Guo §10 adds that Rayleigh quotients are quadratic in the leakage.
- L′ asks that this residual be **coercive** with respect to its own data. That is exactly the inverse (stability)
  estimate PATTERN_001 §3 asked for, now on all of L²(I) through Prop 3.1.
- The scale is right: leak ≥ (1−λ₀(c))‖f‖², with 1−λ₀ ~ c^{1/2}e^{−2c} = poly·e^{−4πμ}. This matches the observed
  bottom up to polynomial factors.

## 4. Falsifier test: where Λ is used

- **The reduction S0–S6 and Props 2.1/3.2 are comb-generic** (PROVED: only ‖C_a‖ and real weights are used). So
  K_κ(a) and L′(a) imply λ^W(a) > 0 for any comb a. Hence:
  - **cΛ (c>1), a₂, a₃, single deletions, zero comb:** λ^W < 0, certified at T = 1, ½log5, …, so K_κ(a) and L′(a)
    are false (PROVED, by CERT_FALSIFIERS_001 + Lemma M).
  - **Beurling:** false (NUMÉRICO λ ≈ −0.08; ARGUED).
  - **F-DH** (its own form, K_{3/4}, conductor 5): false at a = 9/5 (CITED Ziad, PLAUSIBLE-UNVERIFIED).
- **Which ingredient breaks?** For a comb a, W_T(a)(E f) = W_T(Λ)(E f) − 2Σ_{n<μ}(a(n)−Λ(n))n^{−1/2} Re c_{Ef}(log n).
  - For cΛ, a_P and Beurling, the extra term is O(1) on the near-kernel images. The **residual identity** (Poisson +
    explicit formula; the Mellin transform of E f is ζ(s)·f̃(s)) is what fails. For these three falsifiers the
    Λ-exact ingredient is the identity (ARGUED; PROVED form = PATTERN_001 §3).
  - **For F-DH the identity survives (ARGUED).** The Mellin transform of E_b f with b = DH coefficients is F(s)f̃(s).
    It vanishes at the zeros of F, and Poisson for periodic b holds with a Gauss sum. So "E_b f lies in the radical"
    holds for DH as well. Yet DH is negative at 9/5.
  - **Consequence (ARGUED, new):** the residual identity is FE-generic, not ζ-specific. The ζ-specific content of L′
    must sit in the **coercivity of the exterior residual form**, and it must use the Euler product.
  - BARRIER_EST_001 adds a constraint: the premises of that step cannot be TV-robust with slack above
    κ₊μ^{9/2}e^{−4πμ}. So the coercivity must be Λ-exact up to doubly-exponentially small tolerance (PROVED by Thm 4
    there, applied to the margin).

## 5. Relation to Conjecture κ-band (PATTERN_001 lower half: κ₋(1−λ₄(2πμ)) ≤ λ^W)

- **K_κ ⇒ κ-band lower half.** PROVED (Prop 2.1). The converse is ARGUED false in general: K_κ discards the tail
  surplus T_tail − Cδ − U ≥ 0. At the bottom the two are ARGUED near-equivalent, because Ω ≫ 2πμ and the
  near-kernel vectors carry negligible energy beyond Ω.
- **L′ ⇒ a weak κ-band** λ^W ≥ κμ^{−A−1}(1−λ₀). This is the same e^{−4πμ} scale, with a polynomial loss of
  (1−λ₀)/(1−λ₄) ~ c^{−4}. PROVED.
- **κ-band lower half does not imply L′.** It only gives W(Ef) ≥ κ₋(1−λ₄)‖E⁻¹‖⁻²·leak, a coefficient e^{−4πμ}, not
  μ^{−A}. PROVED.
- **So L′ is stronger in kind** (W controlled by leakage at polynomial loss) **and weaker in constant**. Both give
  λ^W > 0 for every T.

## 6. What is proved here
- **PROVED:**
  - Prop 1.1 (the cost floor of the Liu–Mori class is superpolynomial; this corrects PATTERN_001 §2);
  - Prop 2.1 and Prop 3.2 (reductions to K_κ and L′);
  - Prop 3.1 (the Möbius bijection of the summation map, with norms ≤ 2√μ);
  - the falsifier exclusions in §4 for the certified combs.
- **CITED, uniform in μ:** Theorem N, Prop 3.1/Lemma 3.2/(3.3) of Mori VII.
- **ARGUED:**
  - the residual identity is FE-generic (DH passes it), so the Euler product must act in the exterior coercivity;
  - near-equivalence of K_κ and κ-band at the bottom.
- **OPEN:** K_κ and L′.

**Verdict.** Mori's structure yields one uniform target: leakage coercivity L′ of the Weil form on summation-map
images, which by Prop 3.1 cover all of L²(I). Its ζ-specific ingredient is not the residual identity, which F-DH
passes, but the coercivity of the exterior form. Row D is OPEN. No sign is claimed.
