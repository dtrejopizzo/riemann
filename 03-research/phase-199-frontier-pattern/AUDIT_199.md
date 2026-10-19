# AUDIT_199 — review of MECH_001 and PATTERN_001 (phase 199)

Pen and paper, plus one arithmetic check (Rayleigh floor at μ = 10, 12, 15).
Sources checked:
- Mori VII (log 12, zenodo 23265728, scratchpad `zen/moriVII.txt`): §1.2, §3 (3.1)–(3.4), Prop 3.1, Lemma 3.2, Remark 2.3, §7.
- Mori VI (log 10, `zen/moriVI.txt`): Lemma 3.2 (L < 7/6) and §7.
- AUDIT_ZENODO_FRONTIER §0, B1, B8.
- Paper 47: def:W, prop:env, rem:moriceiling, subsec:shape-geom (thm:geo-tv).
- BARRIER_EST_001 Thm 4.
- ROUTES-TRIED-INDEX README (lines 50, 52, 447–450).

## Main finding (new): Lemma L′ as stated is FALSE (gauge falsifier)
MECH_001 Prop 3.1 shows that E f depends only on f|_{[1/λ,λ]}. Take any nonzero even f ∈ C_c^∞(−1/λ, 1/λ) with
f(0) = 0 and ∫f = 0. Then:
- E f = 0, because n e^x ≥ e^x ≥ 1/λ.
- W_T(E f) = 0.
- leak(f) > 0, because no nonzero compactly supported f is band-limited.

L′ would then give 0 ≥ κμ^{−A}·leak(f) > 0, a contradiction. **L′ is NO-GO as written (PROVED, elementary).** MECH_001
called the gauge "free" and then used it against itself.

**Repair, L′♯ (OPEN).** W_T(g) ≥ κμ^{−A}·ℓ(g), where ℓ(g) := inf{leak(f) : f even, C², supp ⊂ [−λ,λ],
f(0) = f̂(0) = 0, E f = g} is the gauge-minimized leakage. Prop 3.2 survives verbatim: its chain
leak(f) ≥ (1−λ₀)‖f‖² ≥ (1−λ₀)‖g‖²/(4μ) holds for **every** representative, so it also holds for the infimum.
- L′♯ ⇒ λ^W_T ≥ κμ^{−A−1}(1−λ₀(2πμ))/4 for every T: **CONDITIONAL on L′♯**, and the proof is correct.

## (a) S0–S7 against Mori — faithful, with minor omissions
Uniform-in-L statements are explicit in Mori VII:
- §1.2: "nothing there depends on L" (S0).
- §3 opening: "L > 0 is fixed … every constant written in terms of L, Ω, m, N" (S1, S4–S6).
- Remark 2.3 / Theorem N: "for every L" (S3).
- Lemma 3.2: general ρ, N, c = ΩL (S5).
- (3.3): cited to [14, (4.1)], "the proof uses only mI ⪯ M and n < m" (S6). This is uniform but **CITED by reference**;
  the proof is not in Mori VII.

Omissions to add to the table:
- Prop 3.1 requires c = ΩL > 2, C > 0 and Ω ≥ 15/4.
- Mori VI Lemma 3.2 is **only for L < 7/6**. The uniform version is Mori VII Theorem N.
- The "working precision ≈ 2N_cert bits" row is **ARGUED**, not derived.

Verdict: **CITED (uniform ∀L), faithful.**

## (b) Prop 1.1, superpolynomial cost — CORRECT, relative to the class
- **(ii) checked.** With v₀ = (2L)^{−1/2}1_I and C_p = Σ Λ(n)n^{−1/2}(S_{log n} + S_{−log n}) (Mori VII §3.1),
  ⟨v₀,C_p v₀⟩ = Σ_{n<μ} 2Λ(n)n^{−1/2}(1 − log n/log μ). Arithmetic:
  | μ | Rayleigh floor | Mori s | 𝒜_T |
  |---|---|---|---|
  | 10 | 2.367 | 3 | 7.08 |
  | 12 | 2.763 | 3.56 | 8.52 |
  | 15 | 3.312 | 4.09 | 9.94 |
- **(iii) checked.** The integral is 8√μ/log μ − 4 − 8/log μ. With the de la Vallée Poussin error,
  √μ·e^{−c√log μ} = o(√μ/log μ), so the o(1) is legitimate.
- **(iv)** S2 needs C > 0, that is log(Ω/2π) − 1/Ω > γ ≥ s ≥ ‖C_p‖. So Ω ≥ 2π·exp((8+o(1))√μ/log μ).
  **PROVED for the class "constant absorption γI + Prop 3.1 tail"**, which is the architecture of Mori VII §3. It is not
  a statement about every certificate. This is a refinement of prop:env, where 𝒜_T ~ 4√μ.
- **(v)** N ≥ (1+o(1))ΩL for r_N < 1: correct, since inf_ρ sinh(log ρ)/log ρ = 1. The Landau extension is ARGUED.
- **PATTERN_001 §2 "polynomial cost ~μ⁴" is wrong as an asymptotic for rigorous certificates of this class.** It is
  valid only for Galerkin evaluation of λ^W, which is NUMÉRICO and not certified.
- The μ = 16 feasibility estimate (N ≈ 2060) is unaffected, because the superpolynomial term is still modest there.
- Label for "~μ⁴": **retracted for certificates; NUMÉRICO for Galerkin only.**

## (c) Proofs
- **Prop 2.1: correct.** It is (3.2) of Mori VII plus the hypothesis K_κ.
  - Label: **CONDITIONAL on K_κ**, with CITED steps Prop 3.1 / Theorem N.
  - K_κ must quantify over admissible (Ω, δ, u₀, u₁): c > 2, C > 0, u_jE_j ≤ C.
  - The Cδ term is negligible (≈ e^{−2ΩL}).
- **Prop 3.1 (Möbius bijection): PROVED, checked line by line.**
  - Support: n u ≥ u ≥ 1/λ.
  - Inversion: Σ_{m|k} μ(m) = [k = 1].
  - Surjectivity: put H = 0 beyond λ. Then Σ_n f(nu) = Σ_k H(ku)Σ_{m|k} μ(m) = H(u).
  - Isometry: ‖g‖_{L²(dx)} = ‖H‖_{L²(du)}.
  - Bounds: ‖E‖, ‖E⁻¹‖ ≤ Σ_{m≤μ} m^{−1/2} < 2√μ.
  - C² regularity of E⁻¹g: terms switch on at u = λ/m, where g vanishes to second order at T. The gauge on
    (−1/λ, 1/λ) meets C² matching and the two linear constraints.
- **Prop 3.2: the algebra is correct.** The prolate constant is c = 2π·λ·λ = 2πμ, which matches Mori's c = ΩL with
  Ω = 2πλ and L = λ. The bound 1 − λ₀ ≥ d(c) gives the /16 form. The hypothesis must be L′♯, not L′.

## (d) F-DH — partly right; the conclusion overreaches
- That Mellin(E_b f) = F(s)f̃(s) vanishes at the zeros of F is true for **any** Dirichlet series. FE is not needed for
  that part.
- Poisson with Gauss sums for periodic b (mod 5) holds. However:
  - the dual window is rescaled by the conductor;
  - there is no pole term;
  - the archimedean kernel is K_{3/4}.

  So "DH passes the residual identity" holds only for a **conductor-rescaled, pole-free analogue** of the identity.
  ARGUED, and the rescaling must be written out.
- The inference "ζ-specific content must sit in exterior coercivity" is fine as ARGUED, given B8's caveat that the form
  is not W_T.
- **"Must use the Euler product" overreaches.** F-DH also lacks Λ_F ≥ 0 with prime-power support, the pole at s = 1,
  and conductor 1. Correct to: "a feature absent from F-DH (Euler product, or positivity and prime-power support of the
  comb, or the pole and conductor 1) must act in the coercivity." ARGUED.

## (e) Novelty and the barrier
- **Not a retry of C1/L81.** It asks for no sign from gluing. Accepted.
- **Not BARRIER_EST.** That file is a constraint, not a target.
- **L′♯ is a quantitative reformulation of D on summation-map images (REF-D: a valid target, not closed).**
- It belongs to the families "coercivity" (index l.50, walls W-*) and "Euler/Möbius algebra". Any proof of it built
  only from Möbius identities + Cauchy–Schwarz/Bochner falls under the N_018 meta-theorem. A way
  around this must be stated before launching.
- **Barrier: the MECH §4 claim is mislabelled.**
  - BARRIER_EST Thm 4 bounds the TV slack by **λ_A**, not by the doubly-exponential ceiling.
  - The ceiling κ₊μ^{9/2}e^{−4πμ} bounds **λ^W ≤ λ_A** (rem:moriceiling, CITED, PLAUSIBLE-UNVERIFIED, uses zero data).
  - To transfer it, one needs (i) a W-form analogue of Thm 4 and (ii) Mori's upper bound. (i) is ARGUED: the same
    δ_u perturbation argument applies to the complete form.
  - Label: **CONDITIONAL**, not PROVED.
- **Consistency of L′♯ with the ceiling.** At a bottom vector, ℓ(g★) ≥ (1−λ₀)‖g★‖²/(4μ) ~ μ^{−1/2}e^{−4πμ}, and
  W(g★) ≤ κ₊μ^{9/2}e^{−4πμ}. These are compatible for A ≥ 0. L′♯ is therefore **consistent** with the ceiling.
  Its RHS is itself doubly-exponentially small in T, so it does not contradict the barrier. It also cannot be proved
  from TV-robust premises.

## (f) κ-band ⇄ K_κ ⇄ L′♯
- **K_κ ⇒ κ-band (lower half):** PROVED.
- **L′♯ ⇒ weak κ-band:** PROVED. The bound has λ₀ in place of λ₄ and a μ^{−A−1} loss.
- **κ-band ⇒ L′♯:** the naive route gives only an e^{−4πμ} coefficient. MECH §5 labels "does not imply" as PROVED. It
  is only "not implied by this route": **OPEN** (ARGUED false).
- **K_κ ⇐ κ-band:** ARGUED false in general. ARGUED near-equivalent at the bottom.

## Label corrections
| item | MECH/PATTERN label | corrected |
|---|---|---|
| Lemma L′ | OPEN | **NO-GO as stated** (gauge falsifier). Repair L′♯ OPEN (REF-D) |
| Prop 3.2 | PROVED given L′ | PROVED given **L′♯** (vacuous under L′) |
| Prop 1.1 | PROVED | PROVED, **relative to the Mori VII §3 class** |
| PATTERN_001 §2 "~μ⁴" | NUMÉRICO law | retracted for certificates; Galerkin-only |
| §4 barrier "Λ-exact to doubly-exp tolerance" | PROVED | CONDITIONAL (W-analogue of Thm 4 + rem:moriceiling) |
| F-DH "Euler product must act" | ARGUED | ARGUED, weakened (Euler product / Λ ≥ 0 / pole); conductor-rescaled identity |
| §5 "κ-band ⇏ L′" | PROVED | OPEN |
| S6 (3.3) | CITED | CITED by reference ([14] (4.1)) |

**Verdict.** The scaling analysis (Prop 1.1) and the Möbius bijection (Prop 3.1) stand. Lemma L′ is false as stated.
The gauge-minimized repair L′♯ is the correct uniform target; it is OPEN and is a REF-D reformulation. No sign is
claimed. Row D OPEN.
