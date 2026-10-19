# 06 — Open residues of row D: dead sub-routes and admissible directions


REF-D = "the sub-route ends in an internal reformulation of D". It records where a sub-route ends; it does not close the residue.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / FALSIFIED / NUMÉRICO.
Sources: README "Residuos vivos"; 01–05; SYNTHESIS_188 (Updates 1–3); NT_SYNTHESIS; adversarial reviews 188 (N_011, L2_018, L2_021, L2_023,
L2_024_025) and 189 (NT_001_004, NT_005_007, NT_008_010, NT_011_014); Paper 47 §sec:open; master grid R162_2300 (live cells = rows tagged
OPEN-RESIDUE in 04_, 93 rows).
Abbreviations: P47 = 04-papers/47-row-d-dual-certificates/main.tex; 188/ = 03-research/phase-188-closing-D/; 189/ = 03-research/phase-189-new-theory/;
186/ = 03-research/phase-186-toolbox/.

**Barriers that every residue must escape.** Each admissible direction below lists the ones it must escape.
- **[void]** cor:void / thm:finmod (P47): classes closed under finite deletion Λ1_{n≥N} or one-term amplification Λ+c1_{n=n₀}.
- **[tail]** W-tail (N_003; P47 cor:wtail): any comb with a = Λ on n<n₀ and 0 ≤ a ≤ Λ.
- **[sens]** prop:wit-sens: bounded functionals of the weights (a 1e-5 perturbation flips the sign).
- **[F]** F-uniform falsifiers: M_m quartets, f_t, Λ̃, DH/Epstein, ζ̃ = ζ·R (NT_011), a_P, Poisson combs.
- **[T1/T2]** field-uniformity (ζ_K, S₃) and A1–A6 (Epstein).
- **[lin/det/fam/pat/loc/mom/coh]** W-walls (R186; P47 §barriers).
- **[margin]** P47 cor:margin1: λ_A ≤ 4·10⁹ T exp(−15.449T), T≥1 (PROVED). The doubly exponential estimate cited in P47 rem:moriceiling concerns λ_W, is recorded there as unverified, and must not be transferred to λ_A (λ_W≤λ_A has the wrong direction for that transfer). See AUDIT_207_001 and P47 thm:margin with its proof.
- **[opcalc]** prop:opcalc / N_018 meta: linear identities + Bochner/C–S only.
- **[zeros]** zero-information class C_zeros: zero-free regions, density, finite zero sets (thm:finZ).
- **[crit]** exact criticality: centre, packets, mean square (L2_010, N_013, L2_019).
- **[sym]** FE antisymmetry D_{1−σ} = −D_σ (L2_026).

---

## R1. (N) / (N_loc): correlation inequality on P_T
**Statement.** For every T and every F ∈ P_T: Σ_n v_n Re c_F(log n) ≤ 𝔞_∞(F), with v_n = 2Λ(n)n^{−1/2}. Polar-free form: 𝓕_T(F) ≤ 𝔞^♯(F), where
λ^♯(T) ↓ C₀+4 (N_001, P47 prop:sharp). Nyquist form: the coherence 𝒞_T(ω_k) is signed against the samples |F̂(ω_k)|², ω_k = πk/2T (P47 (N)).
(L2) ⟺ (N_loc) (L2_006).
**Status.** OPEN. Main frontier (SYNTHESIS_188 §4.1).
**Dead sub-routes.**
| sub-route | outcome | ref |
|---|---|---|
| absolute ψ(y)−y bounds, any exponent θ>½; large sieve / mean square | NO-GO (insufficient) | P47 rem:wit-cheb, prop:wit-sens |
| bounded functional of the weights v | NO-GO | prop:wit-sens |
| pointwise symbol positivity (κ=1<κ*) | NO-GO | L2_019 §4; P47 thm:nolocal (W-loc) |
| F-uniform prime-free slack δ₀* | NO-GO (δ₀*<0 for T>½log5) | L2_006 |
| sieve majorants, upper bounds, lag-restricted, exact small values | NO-GO | N_003 W-tail; R167_102 W-sieve |
| per-segment Λ re-summation; per-prime Euler bounds | NO-GO (tautological) | N_002 |
| Euler-product structure in 𝔄_T (partial products, real powers) | NO-GO | N_005; L2_011 row 8 |
| Möbius transport / integer-comb discrepancy | NO-GO (termwise cost Te^T) | N_006 |
| resolvent cone order; KLMN relative order | NO-GO | N_007 (prop:cone), N_008 (prop:relative) |
| Euler cone exp(ν), ν≥0 | NO-GO (3 ways; contains a_P) | L2_013 |
| Möbius–log splitting certificate | NO-GO (class empty for T≥0.60) | L2_017 |
| three-vector Gram, linear-centre split, shift-multiplier calculus | NO-GO (C–S loses; centre +4T‖F‖²) | N_016–018 |
| SOS: pure arithmetic / free p.d. part | NO-GO for T≥½log3 / REF-D (class (D)) | N_019; P47 thm:sos |
| exterior certificates (lattice, flat-top, far exterior, free log-coefficients) | PARTIAL / REF-D (thm:Z) | N_020; P47 rem:farext, thm:posext |
| reflection = alternating comb, Selberg symmetry | NO-GO (ARGUED) | N_004 |
| Frobenius doubling induction in T | NO-GO (Tate not transported) | L2_016 |
| IMS localization, Tate-free localization | NO-GO for T>0.822 | L2_004 |
| scalar one-step transfer Φ | NO-GO (2×2 falsifier) | L2_003 |
| determinants, moments, norms, Schur 4×4 | NO-GO | W-det, W-mom, R186_024, adversarial 104 |
| integer-density / Poisson-random comparison | NO-GO (r ≤ 1 < κ*; P(λ_A≥0) ≤ e^{−cTlogT}) | P47 thm:ceiling, thm:poisson |
**Admissible directions.**
- (a) Anti-alignment inequality between U_μF and U_logF on 𝒩_T, quantified against the deficit symbol (κ*−1)/(¼+τ²) (L2_017 lesson; N_011).
  Must escape: [void], [tail], [opcalc] (the inequality must be genuinely non-linear in Λ, not identity + C–S), [loc], [F].
- (b) Signed exponent-½ cancellation of the twisted sum at ≈e^{2T} Nyquist frequencies, jointly correlated with the samples of F.
  Must escape: [sens], [zeros], [crit].
- Reduced forms that are smaller but still open: R2 (Ω₀) (one test function) and R5 (E_γ) (one frequency).

## R2. (Ω₀): clamped ground-state test
**Statement.** For every T > ½log5: Σ_n 2Λ(n)n^{−½}h_T(log n) < 0, where h_T is the clamped bending ground mode of P_T = (¼−∂²)H²₀
(ĥ_T ≥ 0, double zeros at ±i/2) (L2_008–009).
**Status.** OPEN. Necessary for (L2) at each T, not sufficient (L2_007 §3; rem:bar-loc). The reduction 𝒯₀ ⟺ (Ω₀) is PROVED.
**Dead sub-routes.** PNT-type error terms (cor:void, L2_009 §1(i)); finitely many zeros (§1(ii), thm:finZ); local symbol argument (W-loc);
Tate-free localization (L2_004).
**Admissible directions.** One explicit Weil sum per window, using an individual property of Λ that finite modifications preserving PNT lack.
Must escape: [void], [tail], [zeros]. Nothing has been tried beyond the class statements above.

## R3. (Ω_{t₀}): fixed fraction / t_∞ > 0
**Statement.** sup_{T,F}(𝓕_T − 𝔞^♯)₊/G_κ < ∞. Equivalently, along λ_t = (1−t)ρ_κ + tΛ with κ > κ*, t_∞ := lim t*(T) > 0 (N_012).
The target is t_∞ = 1 (REF-D). t_∞ > 0 is implied by the target (D ⇒ (Ω_{t₀}), PROVED); whether it is strictly weaker is OPEN (K12_DAMPED_001 Lemma 2.1: (Ω_{t₀}) is invariant under finite comb modifications, so it does not imply D; the dichotomy t_∞ ∈ {0,1} is ARGUED — AUDIT_204_TRACT_E_001).
**Status.** OPEN.
**Dead sub-routes.**
| sub-route | outcome | ref |
|---|---|---|
| decomposition giving t₀ | NO-GO | N_012 |
| concentrating packets (E_γ,C) | collapse to (E_γ) (CONDITIONAL) | N_013 |
| translation / modulation two-copy and multi-copy families | not separable from D (ARGUED); multi-copy → packets | N_014 |
| Ξ unbounded above ⇒ t_∞=0 | PROVED, wrong direction (Thm A) | N_014 |
| Λ ≥ 0 / fixed profile oscillation | NO-GO (Thm L: limsup Ξ ≥ 0 ≥ liminf) | N_015 |
**Admissible directions.** Families with non-convergent spectral measures that are neither packets nor translation/modulation families
(SYNTHESIS_188 §4.2). Proving "(Ξ) for all F₀ ⇒ t_∞ > 0" is OPEN (N_014 §4). Must escape: [crit], [fam] (bilateral laws are not excluded).

## R4. (Ω_Φ): global fixed-point residual
**Statement.** Find a functional inequality controlling the window negativity of a comb λ by its Poisson–Euler residual r(λ) = λ − Φ(λ). Λ is a
fixed point of Φ (N_009; uniqueness CONDITIONAL on Hamburger).
**Status.** OPEN. No quantitative candidate.
**Dead sub-routes.** Perturbative or Lipschitz 𝒦_T linearized at Λ is tautological at Λ (λ_A ≥ λ_A) (N_010 §3, NO-GO).
**Admissible directions.** Only a non-perturbative, non-local 𝒦_T. Must escape: [F] (falsifiers have r ≠ 0, which is consistent, so the
inequality must be uniform over them), [void], [margin].

## R5. (E_γ): twisted Chebyshev inequality at one frequency
**Statement.** limsup_T 𝓕_T(F_T)/‖F_T‖² ≤ m^♯(γ) for the concentrating packets at γ. Here m^♯ = Re ψ(5/4+iγ/2) − log π
(exact form, N_001; P47 prop:Egamma-exact). D ⇒ (E_γ) is PROVED (R186_050; P47 prop:wit-Egamma).
**Status.** OPEN. The packet limit equals m^♯(γ) exactly, so the inequality is critical at every γ (N_013).
**Dead sub-routes.** Weakening by a constant (E_γ,C) collapses to (E_γ) (N_013, CONDITIONAL); large sieve and VK are insufficient (R186_051);
centre γ=0 is exactly critical (L2_010); no F-uniform bound (N_001).
**Admissible directions.** An exponent-½ signed twisted ψ bound at frequency γ. Must escape: [zeros], [crit], [void]. R186_050 §4.3 and N_013
Prop 3.3 read (E_γ) as a zero-side statement, so a prime-side proof must avoid zero-location input.

## R6. Lower half of the bilateral law
**Statement.** λ_A(T) ≥ L(T)(1−o(1)) with explicit L > 0 (Zhu Conj 12.1, primitive normalization; R186_039 BL). By P47 thm:wit-Tc(iv),
λ_A ≥ −ε(T) with ε → 0 already gives the target. In the stated asymptotic lower bound, any admissible L(T) must satisfy L(T) ≤ (1+o(1))4·10⁹ T exp(−15.449T) by P47 cor:margin1. The cited, unverified doubly exponential ceiling for λ_W is not a proved ceiling for λ_A.
**Status.** OPEN. Not excluded by W-fam (P47 rem:bar-fam). Beyond ½log5 no lower bound better than C₀ − A is known.
**Dead sub-routes.** Landau–Widom main term (predicts β_max > 1: NO-GO, R186_039 §2.3); L_Sh = exp(−cN_Sh log N_Sh) is not bilateral (ARGUED);
pattern fit 13.0e^{2T} (W-pat, NUMÉRICO); f_t and M_m share the law up to a perturbation (R186_039 §3); bounded-range families (W-fam).
**Admissible directions.** An asymptotic in which the sign enters through the lower half, uniformly in T. Must escape: [fam], [pat], [det],
[margin] (the proved exponential ceiling for λ_A), [F] (M_m, f_t).

## R7. O166.802.1: non-linear multiscale inequalities on Λ
**Statement.** Extend the circularity theorem of R166_802 (an inequality on Λ that excludes the witness at γ_q must be an O-bound of exact strength)
from single tests and power families (PROVED) to arbitrary non-linear, non-power B. Minimal form: TB-3, a degree-2 window × tail bilinear
Σ_{n≤X<m≤Y}ΛΛ(nm)^{−½+iγ}… (R186_000).
**Status.** OPEN. ARGUED in general. It is the only cell that no PROVED method theorem covers (R186_000 l.356; R184 README).
**Dead sub-routes.** TB-3 closed negative for every degree (R186_005 Thm TB3-neg: generalized Selberg holds ∀b, Λ*Λ ≥ 0 is trivial, b_θ satisfies
it). Finite-dimensional / bounded-type-cone exclusion is circular (R185_001/003). Unbounded-type tests are circular (R185_008). Single tests and
power families are circular (R166_802 PROVED).
**Admissible directions.** "Partial completeness beyond X" (R186_005 survivor; no candidate). Leaves ρ1‴ and ρ2 of R185_005B (R13). Must escape:
[void], W-sieve, F-b_θ.

## R8. The §28.4 object (Paper 46)
**Statement.** An adelic-square object 𝒪 satisfying six clauses: square, local polar divisor, holomorphic zero part, … (P46 §28.4). It is the only
path that reopens Paper 46.
**Status.** OPEN (object unbuilt).
**Dead sub-routes.** Five frame enlargements (P46 Thms 22.17, 24.1, 24.10, 25.6–7, 26.13/17); the h⁰-carrier MW-5/OT-5′ (W10; R142 Thm 19.25;
158–160); Schwartz–Bruhat adelic / Jacobi theta with T_{p²} / Weil–Connes trichotomy (R173_FINAL: all three families NO-GO, but no non-existence
theorem); AKL, Deninger, Borger/Witt, CC third coordinate (R175_FINAL: six clauses NO-GO for those families); function-field transport
(rationality wall W8, F-F_q); Deligne/Laumon (T4/T5).
**Admissible directions.** OT-5′ (global object, R173_OT5); TC-174 (Morita equivalence to the Tate–Meyer module); R175 statements A/B; MW-5
cluster (Deninger foliated, CC square not via h⁰, F₁ surface); laminated carrier with Álvarez López–Kordyukov polarization (R158_001). Must escape:
W10 (the carrier must not postulate positivity), [T1] (must name the property separating it from ζ_K), frame defect (it holds over F_q too).

## R9. Problem (S): near-coincidence part of [Ξ(log(m/k))]
**Statement.** Fixed profile F₀ with 2T₀ < log 2. Show Arch_M − Div_M − Near_M ⪰ 0 for every M (P47 (S); ⟺ target by prop:AM + thm:oneprofile).
For m > k, Div + Near = ½Ξ_{F₀}(log(m/k)). Near is the contribution of m ≈ kn with m ≠ kn.
**Status.** OPEN.
**Dead sub-routes.**
| sub-route | outcome | ref |
|---|---|---|
| Near-free tests (separated multiplicative sets) | positive for local reasons; no global input | L2_029; P47 prop:nearfree |
| multiplicativity diagonalizes A_M | NO-GO (real lag log r) | L2_028 §2 |
| exact matrix identity from 1*Λ = log beyond divisors | NO-GO (Near is a discretization defect) | N_022 §3 |
| 2×2 sections | each one is the band |X(d)| ≤ 2a₀; necessary only | L2_023 Thm T |
| progression statistics (BV, BDH, Siegel–Walfisz, Titchmarsh divisor, Brun–Titchmarsh) as class input | NO-GO | N_021 Thm 2; P47 prop:prog |
| conductor q>1 family via twisted vectors | hybrid form, not L(s,χ)'s window form | N_021 Prop 3 |
| residue-balanced subspaces (R_Q), (B_Q) | ⟺ D, not weaker (Thm E); no escape from finmod | L2_031 |
| Near as a separate signed operator | NO-GO: it is the finite-resolution remainder of |P_s|²V | L2_030 §2 |
| Gram of translates in {log n} alone | NO-GO | R186_001 |
| integer near-triples resonator | exact at Ω ≥ N³; natural resonance O(1) | L2_020 |
**Admissible directions.** Joint control of Near with Arch on vectors that see near-coincidences: the q=1 Chebyshev fluctuation plus the
additive-character components c_{p^b}(j) (L2_030 §3), at resolution ≈ e^{2T}. Must escape: [void] (Theorem E transfers every falsifier), W-sieve,
[opcalc]. Conductor > 1 routes other than the two excluded ones are not excluded (N_021 §3).

## R10. The NT door: inequality at σ = 1
**Statement.** An inequality at σ = 1 (or uniformly on (1,1+ε)) of the height flow (NT_001) that uses the multiplicativity of ζ on the line. It must
be false for ζ̃ = ζ·R and for Epstein/DH series, and it must not be a zero-free statement (NT_011_014_REVIEW).
**Status.** OPEN. No candidate input identified.
**Dead sub-routes.**
| sub-route | outcome | ref |
|---|---|---|
| Target E as stated (σ-transport from >1 through the FE-odd factor) | EXCLUDED: ζ′/ζ(w) is absolute only for σ>3/2; (1,3/2] = part (b); odd factor void; no conjugacy | NT_011_014 review; L2_026/027 |
| pointwise (𝒱) / bounds on ℓ″ via FE + line identities + mean values | NO-GO (ζ̃ model; zero geometry) | NT_011; NT_008_010 review |
| part (b), off-curve continuity 1<σ≤3/2 | ⟺ zero-free half-plane (forward PROVED, converse ARGUED) ⇒ NO-GO (ARGUED) | NT_013/014 |
| absolute methods with sub-power PNT errors | excluded | NT_013 |
| centre / Euler-direction families | cheap or exactly critical | NT_003 Thm 3.6, NT_004 |
| FE symmetrization of the spectral family | void (antisymmetric) | L2_026 |
| conjugation of the deformed problem at ½+η | not conjugate; no propagation (M) | L2_027 |
| weak (𝒱) at width √(T₀log) | PROVED but archimedean dominance; no sign content | NT_012 |
| truncations / finite modifications at σ↓1 | fail D(σ) (symbol pole) | NT_006 Cor 6.5 |
**Admissible directions.** Name a property of the Euler product on Re s = 1 that ζ̃, DH and Epstein lack, then use it at σ = 1 directly.
Must escape: [zeros], [sym], [F] (ζ̃, DH), [crit] (σ = 1 is the fixed line).

---

## Other open items

| ID | precise statement | status | dead sub-routes (ref) | admissible directions / barriers |
|---|---|---|---|---|
| **(L2)** | S_{T,k(T)} ⪰ 0 ∀T>½log5 (finite Schur matrix, R186_025; P47 (L2)) | OPEN; ⟺ target at T | norms, determinants, moments, local symbol (W-*), Lemma H (ARGUED), front T₁/(B_T) false, β₀=2, PNT cone, 4×4 Schur, Schur tower n₋ k-independent (L2_002), scalar transfer (L2_003), Γ-moment annihilation = REF-D (prob:annihilate) | first case T=½log5+ε; via (Ω₀), (N_loc); escape [margin], W-lin, W-det |
| **Theorem S / Lemma I** | target ⟺ B_{F₀}(d) p.d. on ℝ | PROVED (|b|>½, with 2 FIXes) (024_025 review) | — | open variant: explicit factorization B = h⋆h̃ at σ=½ without zero input (L2_025 §3; Prop H gives it only for σ>1); escape [zeros], [sym] |
| **(Ξ) fixed profile** | limsup_d Ξ_{F₀}(d) ≤ 2𝔞(F₀) | OPEN; refinement stopped (N_015) | Λ≥0, Thm L | needs Near (R9) |
| **Thm T converse** | does the two-sided band \|X(d)\| ≤ 2a₀ ∀d suffice? | not sufficient by itself: each 2×2 is necessary only (L2_023; P47 (S)) | 2×2 / translation families (N_014 ARGUED) | needs multi-scale joint matrix = R9 |
| **thm:X converse** | new primes cancelling σ_{T₀} on U_{T₀} ⇒ positivity | NO-GO (M₁ satisfies X and is negative) | — | dead |
| **(A)/Q1 Beurling realizability** | Beurling system (positive prime measure, powers) with comb in Pos | OPEN | integer density r>1 impossible (thm:ceiling); log ℕ combs with residue r>1 ∉ Pos | continuous Beurling ∈ Pos (N_011 Cor 2); atomic needs κ>κ* without ℕ-integrality |
| **Q2** | same with ℚ-independent positions | OPEN ("likely YES", not proved) (L2_018 §open) | — | Kronecker resonances at τ ≳ e^{cN} |
| **Q3** | is doubly exponential resolution necessary for atomic positivity? | OPEN (L2_019: weak resolution bound only) | Fejér mean square = critical | sharpening blocked at integer-log resolution 2Te^{−2T} |
| **thm:sos gap** | arithmetic SOS on ½log2 < T < ½log3 | OPEN (P47 secondary 8) | T≥½log3 NO-GO (N_019) | first window with a contact |
| **N_020 Thm 2** | far-exterior support ⇒ negative value | OPEN (dilated W-tail tests have pairing ≈4sinhT‖G‖², not o(1)) | "routine correction" failed (Update 3) | only weak duality (rem:farext) PROVED |
| **Problem A** | explicit deficit D(T,d,U): best lattice certificate ≥ λ_P − D | OPEN (only ceilings, cor:Rrate O(1/log M)) | radius-only deficit excluded (thm:Vp); thm:AL retracted → AL′ | Fourier tail bound of primal minimizer |
| **Problem B** | prime-built flat-top w_T depending only on outer primes | OPEN-RESIDUE; REF-D | 159 G1_B6, G2_B9, R160_S4 | — |
| **polar capacity >½log5** | certified window with 𝔊_T ≻ 0, contact 5 present | OPEN (existence by continuity, ε tiny) | thm:nyq-schur certifies up to ½log5 | certified computation (NUMÉRICO allowed) |
| **λ_P = λ_W?** | optimal multipliers → β=(2,0) | OPEN; parity bottoms never examined | fails if λ_W<λ_A | — |
| **R154_030** | two-prime window 0.58, hybrid N≥6 | off-machine package never run | thm:N′ class (M≤24) | NUMÉRICO only |
| **C_B** | m<∞ off-line quartets ⇒ m=0 | OPEN as a statement (O2601.1) | first-contact machinery (R162_2501, DEAD W2/F3), inertia chain = ζ chain (R184_004, DEAD F3:M_m), Hamburger in atomic class (no class content), Kreĭn–Langer bridge missing (P34-5) | needs an individual Euler-product property; escape [F] M_m |
| **Diana L8** | unconditional bound on the off-line quadruple count | OPEN, "unreachable with catalogued tools" (P37-3; G7D) | zero-density (binary 0 or T^θ) | same requirement as C_B |
| **W₂ two-variable form** | diagonal two-variable Weil kernel W₂ | OPEN (P36-4) | pair-correlation / parity wall; excluded in BR(M2) subject to ρ1‴ (R185_005B) | via ρ1‴ |
| **ρ1‴ / ρ2 / (iii-a)** | BR leaves: (M2) with infinite 𝔉, 𝓡 unbounded below, non-closed; discrete witness set vs W₂; gluing to ℕ≤X | OPEN; narrow; ρ1‴ is still a zero statement (R185_003 Thm 6∞); ρ2 lies outside 𝔐 | R185_005B tree | — |
| **θ ≤ 1/3** | discrete Beurling system N=ρx+O(x^θ), θ<1/3, with an off-line zero (Goal A) | OPEN (R164_503) | rounding/Perron W-dither, re-rounding Thm L (R164_201), prime-side DMV/Zhang capped at ½ (ARGUED), exact integrality ⇒ θ≥½, smearing ⇒ branch points; θ∈(1/3,½) killed by P_171 | O164.503a–d; class problem outside the BR tree |
| **LP-112** | sequential self-approximation ⇒ m∈{0,∞} | DEAD as a route (G8E: adapted Hadamard countermodel; renamed dichotomy); statement OPEN | Prop 2.6 density zero only | — |
| **GAP-157.A** | non-local Tauberian with LI input (Beurling–Malliavin on p^{iτ}) | OPEN-RESIDUE (condition C1 neither known nor excluded) | 2 of 3 diophantine routes killed (P50-1); frequency-local Tauberians = REF-D | escape W3′, [F] |
| **MW-3** | ∞-dim Hasse–Minkowski | OPEN gap (no theorem either way) | Q does not factor over primes (Wall A) | condensed-math variant untried |
| **Lemma 108** | κ_W(Q₂) ≤ C n_W | lemma OPEN, route DEAD | sup κ_W restates the target at k=2 | not REF-D; never attacked (G8C) |
| **O-151.4** | summand-vs-numerator axis as sign mechanism | OPEN-RESIDUE, never developed | — | — |
| **(M) propagation** | P_prof(σ) ⇒ P_prof(σ′), σ′<σ, at comb level | OPEN (L2_027) | conjugation (NO-GO) | must not be σ-transport through residues at zeros ([zeros]) |
| **row 18 of input map** | Euler + FE at conductor q>1 as falsifier source | UNKNOWN; two exact entries into A_M excluded (N_021 Prop 3) | twisted vectors, progressions | other routes not excluded |
| **R178_O** | arithmetic restriction excluding anticorrelation ρ_− | OPEN-RESIDUE | — | — |
| **R172_CAND** | liminf_N liminf_M 𝔑_rem ≥ 0 at first contact | OPEN-RESIDUE | — | — |
| **(★_loc)** | small-y local criterion (R168_103) | OPEN | Lemma 2 PROVED | — |
| **Lewis–Zagier route** | period functions / Mayer transfer operator for ζ as sign carrier (phase-152 R152_001 lists it OPEN, never tried) | OPEN (never attempted) | FUP and Berkovich–Poineau DEAD (same memo); Dolgopyat–Mayer branch series abscissa ½ | must escape [F] (DH has no transfer operator → good), [zeros], W-identification |
| **boundary triples for W_λ** | self-adjoint boundary triple realisation of the window form (phase-60 §4.B) | DEAD (04_ R162_2702b, G8D-160 C2; README l.207); stale note corrected; NO-GO retry (phase-199 PROOF_L_SHARP_OO_001: Tate triple = polar capacity; no edge trace; KVB hypothesis = λ_A ≥ 0, REF-D) | — | must escape W-det, inertia-nogo (n₋=∞ for T>½log2) |

## Grid live cells not listed above (OPEN-RESIDUE; never built or unaudited)
For full rows see `04_PHASES_100-189.md`, lines given in parentheses.
- **Unaudited theorems (159):** G2_B8 Lee–Yang (414) and Thm L″ (427); Thm U (428); R5 theorems B5/B6/B7/B10 (429); G1_B1_R5 DK_α (433);
  G1_B7 Prop BL (434).
- **Never constructed:** 108_99 scaling (279); 113_12 χ(D)=D²/2 (285, REF-D); P121 Kreĭn flux (317); P122 E_(∞,T) (320, 711); Cartwright tropical
  Hodge (340); D.16-γ (348); P152.1 Dolgopyat (369); KEP Nevanlinna (394, 640); o-minimal / Pila–Wilkie (399); global square K*QK−Q (443, REF-D);
  RD_{T′} (487); 𝔊_T in T (488); entangled OS model (494); I6 sub-resolution (503); GAP-141.G1 (503); unread web hit (513); rem:Dgrade (523);
  (H_L) (531); Z_{N,ε} (543); joint cross-prime constraint (544, zero side); Hecke-type coupled square (545); Meyer S+D (547); Thm A cross-term
  T-uniform (556); absorbing-channel twist (566); a4/b4/R16 (576); Sh_ℤ lattice (577); O-D4.2 (591); Λ=μ*log identity regions (592);
  V_T faces (594); v_T(Λ) maximizer (596); rigid-perturbation cone (600); LP-152 Gaussian correlation (601); prop:M family (602);
  multi-generator rigidity (603); O-D4.3 ζ_K transposition (606); Mertens hyperbolic ruling (608); corrected-mass Tate boundary (609);
  Hyp (H) (614, zero geometry); Cayley signed index (632); KEP(T_c) determinacy (637); H1_alg density (647); pollution-free Galerkin (651);
  R160_M11 (659); D1/D3/D5 (676, 691); D₀ self-pairing (701); 122.A (707); non-invertible correspondences (712); O-148.2 (719); Doc 125 semilocal
  (720); MW-5 cluster (730–731); Sonin (4.2) range lemma (739); R161_073–074 moment inverse (757); (E_θ) one-frequency BV (968); NGF non-local
  source (1000); R183_033 semilocal residues (1011); R184_014 L*_comp (1024); parity Schur (1034).
- All of these cells must escape at least [void] and [F]. The function-field/Hodge cells must also escape W10 and [T1].
