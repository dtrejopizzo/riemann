# Phase 188 — Closing D: the (L2) and (N) tracks, combs and one profile

Two pen-and-paper tracks toward the open items (L2) and (N) of Paper 46. The phase proves the polar
elimination lemma and the polar-free form (lem:polarelim, prop:sharp), the exact (E_γ) threshold
(prop:Egamma-exact), positive combs and the atomic positive comb (thm:kappa, thm:atomic), the integer
density ceiling (thm:ceiling), lag-localized primitive tests (lem:transl, thm:band), the random-comb
bound (thm:poisson), the one-profile criterion (thm:oneprofile) and the absence of an arithmetic square
decomposition for T ≥ ½log3 (thm:sos). These are integrated into Paper 46 (see `INTEGRATION_188.md`);
the sign itself is not obtained and row D remains OPEN. The synthesis is `SYNTHESIS_188.md`.


## (L2) track (pen and paper, no numerics)

| file | content | label |
|---|---|---|
| L2_BUILD_001 | edge-mass lemma ∫_J|F|² ≤ 5N(F)/log(1/δ); m ≥ log(2+|τ|) − κ; contact-entry theorem λ_A(T') ≥ (1−ε)λ⁰ − ε(κ+A⁰), ε = 5v_n/log(1/δ) | PROVED (weak; inside fixed-frame norm class + finmod — a gluing tool only) |
| L2_BUILD_002 | s_{T,k}(e) = min_{v∈V_k} 𝔞_T(e+v); nesting E_k ⊂ E_{2k}; S_{T,k} = Schur complement of S_{T,2k} with W-block ⪰ c(T,k); n_− independent of k; c(T,k/2) > 0 ⟺ S_{T,k}|_{E_k⊖E_{k/2}} ≻ 0 | PROVED (routine, structural) |

No sign certified; no negative value. Next: L2_BUILD_003 (OPEN) — one-step coercivity transfer
c(T,k/2) ≥ Φ(c(T,k), S_{T,k}|_{W'}) built from minimizer geometry of adjacent half-blocks (not
operator norms, not determinants), iterated k_0(T) → 1. Link to (N): none used; the prime data
enter only through Φ, where a signed twisted-Chebyshev bound from N_BUILD would be the input.

### (L2) continuation — 003–005
| file | content | label |
|---|---|---|
| L2_BUILD_003 | one-step transfer Φ(c_k, λ_min S|_{W'}): falsifier 2×2 ⇒ Φ ≤ 0 | NO-GO (class 𝒞_scal, PROVED); sign transfer tautological (PROVED) |
| L2_BUILD_004 | IMS localization; primes are pure coupling for supports < log 2; leading logs cancel exactly (critical) | IMS identity CITED; §2 PROVED; NO-GO for IMS+Schur-test chain |
| L2_BUILD_005 | signed lag-coupling: 𝔞_T = Σ local − truncated Toeplitz form of the positive measure 𝒦 = K + Σ v_n δ_{±log n}; (L2-H) reformulation, link to (N) | rewriting PROVED; (L2-H) OPEN |
Next: L2_BUILD_006 — prime-free (L2-H₀) on P_T with explicit slack δ₀, then (N)-type bound Σ v_n Re𝓕(log n) ≤ δ₀. No sign contact.

### (L2) continuation — expansions of 003–005, and 006–007
003–005 now have full proofs and whole-corpus checks. Repeats found: the 004 identity is the nonlocal
IMS identity of phase 106 (106_47/106_59); the 005 reformulation (L2-H) is P121's "sign the IMS cross
term", rejected there absent an Euler-specific cut identity. New and PROVED: 003 NO-GO for a scalar Φ
(2×2 falsifier); 004 §2 primes are pure coupling for supports shorter than log 2; 004 §3 two-sided O(1)
criticality; 004 §4 a Tate-free localization certifies nothing for T > (8+π²/12)/(2|C_0|) < 0.822
(test function 1_{I_T}, pen and paper).

| file | content | label |
|---|---|---|
| L2_BUILD_006 | best prime-free slack δ₀*(T) = λ_{∞,P}(T); negative on all of T > ½log5 and → C_0; (L2) ⟺ (N_loc): Σ v_n Re𝓕(log n) ≤ 𝔞_∞(F) on P_T; no F-uniform version (it would need δ ≥ A_T); comparison with §open (N) | identification PROVED; sign CITED (known since phase 155); NO-GO for the slack split |
| L2_BUILD_007 | finite negative index of 𝔞_∞ on P_T; necessary test 𝒯_0: Σ v_n Re𝓕_{φ₀}(log n) ≤ μ₀(T) < 0; Schur reduction onto H_η (variant of thm:wh-schur) | PROVED (low novelty); dimension count ARGUED |

No sign certified; no negative value of 𝔞_T. Next: an arithmetic (not archimedean) input for (N_loc) on the
finite space H_η. It must use the actual values of Λ (cor:void) and signed exponent-½ cancellation
(rem:wit-cheb).

## (N) track (pen and paper, no numerics)

| file | content | label |
|---|---|---|
| N_BUILD_001 | polar elimination & ψ(5/4) symbol m^♯ (corpus-known, R186_033/114_d_133); **exact (E_γ) ⟺ limsup 𝓕_T(F_T)/‖F_T‖² ≤ m^♯(γ)** (removes ±4 slack of rem:wit-cheb); explicit mesh Tate identities Σ(−1)^k a_k/(T²+π²k²) = 0 and its derivative; (L2)-frame slack λ^♯ ↓ C₀+4; no F-uniform fluctuation bound | PROVED / NO-GO (F) |
| N_BUILD_002 | polar term = Dirichlet resolvent R of ¼−∂² on P_T: 𝔞_T = ⟨(A_∞+R)F,F⟩ − 𝓕_T; Schur onto finite H^♯_η (η > A_T+4); signed demand on the negative part ≤ 1.372 uniformly in T; segmentwise Λ re-summation tautological; per-prime Euler bounds NO-GO | PROVED / NO-GO |

No sign contact; no negative value certified. Next: (N^♯_fin) on the negative eigenvectors of (A_∞+R)|P_T with an
arithmetic correlated inequality (sieve majorants on lag sets / anti-periodic reflection n ↔ e^{2T}/n).

### (L2) — 008–009: the test 𝒯₀
| file | content | label |
|---|---|---|
| L2_BUILD_008 | P_T = (¼−∂²)H²_0(I_T) (Tate ⇔ clamped ends); ground state of 𝔞_∞/𝔞^♯ on P_T is a low-frequency clamped bending mode (μ₀ ≤ C₀ + O(T⁻²)), not an x^{-1/2} edge object; 𝒯₀ ⇔ 𝔞_T(φ₀) ≥ 0; 𝓕_F = (¼−∂²)²(G⋆G̃), and (¼−∂²)e^{u/2} = 0 kills the PNT main term; asymptotic 𝒯₀ = (E_0) | parametrization PROVED (corpus-known); bound PROVED; (E_0) link CONDITIONAL on concentration of the exact minimizer |
| L2_BUILD_009 | 𝒯₀(T) ⇔ Σ 2Λ(n)n^{-1/2}h_T(log n) ≤ μ₀(T) < 0 with h_T = (¼−∂²)²(G₀⋆G̃₀); PNT errors and finite zero data give no sign (cor:void, thm:finZ); open core (Ω₀) | reduction PROVED; (Ω₀) OPEN |
No sign certified; no negative value of 𝔞_T.
| N_BUILD_003 | route (a) lag-restricted sieve: **Thm 1 (tail deletion, PROVED): Λ·1_{n<n₀} fails WP_T for T large, any n₀** — sharpens cor:void (keeps all small Λ(n)); Thm 2: two-sided precision must be < λ_A/|κ_T| | NO-GO (new barrier W-tail) |
| N_BUILD_004 | route (b) reflection = alternating sampled comb, no sector localization (ARGUED on P_T); contact windows couple only powers of the entering prime; route (c) Selberg symmetry in cor:void class | NO-GO / OPEN residual |

### (L2) — 010: the ζ′/ζ(½) lead
L2_BUILD_010: 2Re(−ζ′/ζ)(½+iτ) = m(τ) − 2ΣRe 1/(½+iτ−ρ); the zero sum vanishes at τ=0 for ANY zero
configuration, so −2ζ′/ζ(½) = C₀ (corpus-known, phase-159 G2_B1_R1). For 𝒯₀ the "regularized centre value" is
the archimedean term itself: both sides agree to all τ-local orders; 𝒯₀ ⇔ Z_T(φ₀) = Σ_ρ ĥ_T(γ_ρ) ≥ 0 (explicit
formula, CITED). Zero-free-region control cannot fix the sign (cor:void C_zeros, CITED; exponents ARGUED).
Lead closed NEGATIVE. No sign contact.
| N_BUILD_005 | truncated causal algebra 𝔄_T: exact finite Euler product, comb = −∂_s log Z_{½}; **Euler-product structure is preserved by partial products and powers ⇒ NO-GO** (extends W-tail); both modifications destroy exactly 1*a = log (coefficients 1); surviving object (Ω_EM): Euler–Maclaurin split Z = M + B in 𝔄_T | PROVED / NO-GO / OPEN |

### (L2) — 011: the input map
L2_BUILD_011: 23 properties of Λ classified. KILLED: PNT, zero data, Beurling, tail, rescaling, sieves,
Euler product alone (NEW explicit falsifier a_P = Λ·1_{p≥P}: Euler over ℕ, positive local factors, same zeros
and pole, fails WP_T for 0.60 ≤ T ≤ ½log P), FE without Euler (Epstein/DH), window-linear data (M_m, f_t),
Selberg degree ≤ 2 inequalities, inertia. SURVIVES: identification sets (Λ*1 = log over ℕ; ℕ-frequencies + FE
q = 1; Selberg degree 1 real) and the exact window vector per T. UNKNOWN: Euler+FE at q > 1; étale.
Minimal combination: Euler over ℕ × FE (q = 1), used non-linearly. No sign contact.
| N_BUILD_006 | sawtooth modes: integer-comb discrepancy vs c_F is O(1+‖F′‖²) uniformly in T (k^{−2} modes, no stationary phase); exact transfer comb = 2⟨L, f^μ⟩ (Möbius-transported test); termwise cost T e^{T} ⇒ the sign lives entirely in Z^{−1} (Ω_μ). Large overlap with phase 170 EM port (R184_002) | PROVED (low novelty) / NO-GO termwise and NO-GO weighted-contraction (M^{−1} = 2δ₀ − 2e^{−u/2}du explicit) / OPEN (Ω_μ) |
| N_BUILD_007 | correction M^{−1} = δ₀ − e^{−u/2}du (006 addendum fixed; Neumann series converges unweighted, costs e^{T} in TV); dual-cone order 𝒦_T^* on 𝔄_T; shifts never preserve it; ρ = M^{−1}*B = −e^{−u/2} on (0,log2) with atom 2^{−½} at log 2 is order-indefinite ⇒ no monotone iteration; Odlyzko–te Riele consistency | PROVED / NO-GO; next: archimedean-relative order |

### (L2) — 012: Euler × FE
L2_BUILD_012: candidate (ii) |ζ|²-type positivity NO-GO (holds for every f; transfer to a_P, Epstein); AFE/RS as a
class identity NO-GO (Epstein has its own AFE); specialized to coefficients 1 it is Poisson = the E–M split Z = M + B
in 𝔄_T (track N's (Ω_EM)). New PROVED: −∂_s log M_{½} = (e^{u/2} − e^{−3u/2})du; on P_T 𝔞_T = ∫m^♭|F̂|² − 2⟨R_B,c_F⟩ with
m^♭ = m + 1/(¼+τ²) + 3/(9/4+τ²), m^♭(0) = C₀+16/3 ≈ −0.039 — choice-dependent repackaging (spurious zero of 𝓛M at −3/2),
no slack. Discrimination vs a_P and Epstein PROVED. Missing: a non-linear INEQUALITY (Euler cone positivity). No sign contact.
| N_BUILD_008 | archimedean-relative order: any KLMN bound |𝔮| ≤ θ𝔞^♯_+ + C gives bottom ≤ (1−θ)λ^♯ − … < 0 once λ^♯ < 0; on ρ it does not propagate (shifts leave the cone) and summing returns the comb with T-growing constant ⇒ excluded class (W-lin/thm:margin). Survivors: exact (N^♯) and (Ω_μ); next: Euler-factor SOS certificate in 𝔄_T, test at ½log3 | NO-GO / OPEN |

### (L2) — 013–014
| file | content | label |
|---|---|---|
| L2_BUILD_013 | conventions reconciled with N_BUILD_007 (M=½δ₀+… ⇒ −∂log M=e^{u/2}−e^{−3u/2}; M=δ₀+… ⇒ e^{u/2}−e^{−u/2}); Prop 0: archimedean "slack" is not invariant (any positive-definite kernel can be moved) — retracts reading m^♭(0)≈−0.039 as slack; Euler cone killed three ways (contains a_P; exp(tδ_{log2}) ∉ 𝒦_T^* via N_BUILD_007; exp-pairings blind to the linear comb) | PROVED; NO-GO |
| L2_BUILD_014 | NEW object: Euler–Poisson cube t ∈ [0,∞)^{π(N)}, Z(t)=Π(δ₀−t_p p^{−½}δ_{log p})^{−1}; λ concave in w=(t_p^k); Poisson locus = {1} (FE+ℤ singles ζ); interaction (Möbius) expansion; non-monotone in each prime; passes all discrimination tests by identification | definitions/axioms PROVED; quantitative statement (Q) OPEN |
No sign contact.
| N_BUILD_009 | NEW OBJECT: Poisson–Euler map Φ(λ) = −∂_s log(M + 𝒞^*(Z[λ] − M)); axioms (E) Euler/positivity/ℕ, (P) Poisson self-duality q = 1; Λ fixed point (PROVED), unique (CONDITIONAL on Hamburger growth hyp.); passes all L2_011 falsifiers; window question (Ω_Φ): window negativity ≤ 𝒦_T(λ − Φ(λ)). Note: 005 §1 overlaps R162_903 Thm 3.2 | NEW object / OPEN |
| N_BUILD_010 | linearization of Φ at Λ: c_*(T,2) ≥ λ_A/√2; residual of Λ+cδ_{log2} is c·ρ₂ ≠ 0 (even-integer comb vs its Poisson dual on ½ℤ); consistency at first order but any perturbative 𝒦_T makes (Ω_Φ) at Λ ≡ WP_T (NO-GO perturbative); residual non-local (Poisson mixes scales); characterization = Hamburger (not new); next: global continuation λ_t | PROVED / NO-GO / OPEN |

### (L2) — 015: prime interactions
L2_BUILD_015: the window form has NO prime–prime terms (log of Euler product is additive; Λ(p^a q^b)=0) — PROVED; all
interaction of λ comes from the infimum; infinitesimal 2-prime interaction = −2⟨Rg_p,g_q⟩ (Gram entry, indefinite sign,
Kato CITED); exact I_{2,3} not pen-computable (OPEN). (Q) at Hamming neighbours is ill-posed (neighbours can be negative via
prop:wit-sens; corrections non-canonical by 013 Prop 0) — NO-GO for that formalization. Cube ∩ Fix Φ = {Λ}: same
identification object as N_BUILD_009; gives stability at ζ, not positivity of ζ. Next: a transport inequality in T. No sign contact.

### (L2) — 016: Frobenius doubling in T
L2_BUILD_016: exact identity 𝔞_{kT}(U_kF) = [∫m(σ/k)|F̂|² − Σ 2Λ(m)m^{−k/2}Re c_F(log m)] − [non-k-th powers at lags log n/k]
(PROVED). The "copy" lives on Re s = k/2 (weights m^{−k/2}, not m^{−1/2}), the archimedean symbol is lowered (m(σ/k)), Tate
conditions are not transported, and the copy carries O(T) of the ≍ e^{kT} prime mass. Shell statement ≈ target at kT:
NO-GO as a reduction. No sign contact.
| N_BUILD_011 | EXISTENCE: Pos convex; Pos + e^{u/2}-densities ⊂ Pos; mass ≥ c₀T² necessary; **Thm 1: ρ_κ = 2κe^{u/2}du ∈ Pos ⟺ κ ≥ κ* = sup(−m)(¼+τ²) (≥ |C₀|/4 = 1.343); Cor 2: continuous Beurling systems ψ_B = κ(x−x₀)_+ (κ > κ*, x₀ ≈ 1) have b_T ≥ η > 0 for ALL T — first proved members of Pos**; Λ's main term (κ = 1) is not enough; segment (1−t)ρ_κ + tΛ with first-contact t*(T) > 0; atomic existence = discrepancy problem (A), OPEN | PROVED / OPEN |

### (L2) — 017: Möbius–log splitting certificates
L2_BUILD_017: conjugated dilation dead (e^{βu}c_F not an autocorrelation / not positive-definite; Tate points move). NEW dual
object: certificate (θ,W), W ≻ 0 on L²(ℝ), with 𝔞_∞ ≥ θ⟨WU_μF,U_μF⟩ + θ^{−1}⟨W^{−1}U_logF,U_logF⟩ on P_T, where Λ = μ*log in shift
operators (𝔞_T = 𝔞_∞ − 2Re⟨U_μF,U_logF⟩). Sufficiency PROVED; pointwise tightness PROVED; certificate set convex (operator
convexity, CITED); immune to 013 Prop 0. ADDENDUM: class EMPTY for T ≥ 0.60 (RHS ≥ 0 forces λ_{∞,P} ≥ 0, false by cor:Tarch) — NO-GO PROVED; explicit 2×2-type counterexample to necessity. Lesson: need a LOWER bound (anti-alignment of U_μF and U_logF on 𝒩_T), not a modulus bound. No sign contact.
- N_BUILD_011_REVIEW.md: review of N_BUILD_011 — sign of polar term CONFIRMED; Thm 1 CONFIRMED; Cor 2 FIX (4κ(√x₀−1), not 2κ); Prop 3 CONFIRMED with minor FIX; novelty and barriers CONFIRMED; no downgrade.
| N_BUILD_012 | segment λ_t: t*(T) nonincreasing, b_T concave in t; **trichotomy: target ⟺ t_∞ = 1; "t_∞ > 0" (fixed fraction of ℤ-fluctuation harmless) is strictly weaker = (Ω_{t₀}): sup (𝓕−𝔞^♯)₊/G_κ < ∞**; Euler–Lagrange and transversal crossing at t*; NO-GO: 006 decomposition cannot give uniform t₀ (H¹ vs log-energy mismatch, ζ(½+iτ) Ω-results CITED, non-additivity); next: (E_γ, C) | PROVED / NO-GO / OPEN |
| N_BUILD_013 | (E_γ,C): packet limit of 𝓕_T is the boundary value Re(−2ζ′/ζ − 2/(s−1))(½+iγ) = m^♯(γ) — **exactly critical at every γ** (extends L2_010's centre); summability at one γ is a half-plane statement (Hardy–Riesz, CITED), divergence is exponential ⇒ (E_γ,C) ⟺ (E_γ) (CONDITIONAL on CITED/ARGUED inputs); classical one-sided results do not give it; (Ω_{t₀}) can only differ from (N) on families with non-convergent spectral measures | PROVED / CONDITIONAL / NO-GO |

### (L2) — 018: Problem (A) — atomic positive comb EXISTS
L2_BUILD_018: exact trapezoid error for e^{wu}: ε_h = 2κ(e^{wb}−e^{wa})[(h/2)coth(hw/2) − 1/w], with |ε| ≤ 2κ(e^{b/2}+e^{a/2})(4+h²/24)
and |ε| ≤ (2/9)κ(e^{b/2}+e^{a/2})h²|w| for |w| ≤ π/h (PROVED). Theorem A (one window) and Theorem B (ALL windows): a multiscale
lattice comb ν = Σ_j trapezoid(h_j on [2j,2j+2]) with κ > κ*, h_j ≈ exp(−30κe^{j+1}), has 𝔞^ν_T ≥ (η_κ/4)‖F‖² on P_T for every T
(PROVED, pointwise symbol). First atomic comb in Pos; not Beurling-integral (weights arbitrary positive reals), not about ζ.
Arithmetic content of D in this frame: ζ has κ = 1 < κ* and integer resolution, so its positivity cannot be quadrature; it must be
P_T-correlation (anti-alignment on 𝒩_T). Open: Beurling realizability, generic positions, minimal resolution. No sign contact for ζ.
| N_BUILD_014 | two copies of a fixed primitive profile at distance d: 𝔞_T = 2𝔞(F₀) − Ξ(d) + O(e^{−d/2}), PNT main term killed exactly by Tate; **Thm A (PROVED, prime-side): limsup_d Ξ_{F₀}(d) = +∞ for some profile ⇒ t_∞ = 0; Cor: t_∞ > 0 ⇒ scale-local one-sided bound (Ξ)**; multi-copy lattices → packets (ARGUED); full {0,1} dichotomy NOT proved | PROVED / OPEN |
- L2_BUILD_018_REVIEW: Lemma 1 / Thm A / Thm B CONFIRMED (PROVED); FIX: atom at u=0 outside (0,2T) (harmless), partial-block error ≤0.18η not η/16 (absorbed); 'ℤ-primes lack' (b)–(c) DOWNGRADE to HEURISTIC; novelty confirmed.

### (L2) — 019: Q3, necessary resolution
L2_BUILD_019: Fejér mean square ∫W_Ω(Re S)² ≥ ½ΩΣν_j² with no separation hypothesis (PROVED); mean-square → positive sup loses e^T,
giving only the weak necessary resolution δ ≲ 4Te^{−T}log(·)/κ (PROVED) — Q3 (doubly exponential necessity) OPEN; resonance identity
isolates additive triples u_k ≈ u_l ± u_j (multiplicative relations of integers) as the place ℤ would enter (OPEN). Corrected reading:
ζ's pointwise positivity fails first by DENSITY (κ = 1 < κ*, low band), not resolution; at Ω ≈ e^{2T} the comb's RMS ≈ 2T equals
m ≈ 2T: critical, matching N_BUILD_013. Correlation in P_T must act on the fixed low band and at the critical level up to e^{2T}. No sign contact.
| N_BUILD_015 | (Ξ) for a fixed profile: ∫Ξe^{−sd} = −2(ζ′/ζ)(s+½)C(s), C = L(s)L(−s) with double zeros at ±½; **Theorem L (unconditional, Landau CITED): limsup_d Ξ ≥ 0, liminf ≤ 0 for every profile** (uses ζ ≠ 0 on (0,1)); no contact with the sign; Λ ≥ 0 gives nothing (Tate removes the mass); cor:void does not obstruct tail statements; VK bound only | PROVED / NO-GO |

### (L2) — 020: resonances of the integer comb
L2_BUILD_020: at resolution Ω ≥ N³ integer near-triples are exact (|x| ≥ 1/(2N) otherwise; PROVED); exact triples in supp Λ are only
prime-power ladders p^a·p^b = p^{a+b}, total weight C_ex ≤ 8Σ(log p)³/(p−1)² < ∞. Natural resonance: ℤ vs generic differ by O(1).
Integer resonator (multiplicative r on squarefree P-numbers): sup_{|τ|≤Ω} Re S ≳ √(log Ω) (main term PROVED, errors ARGUED; classical
order) ≪ g_1 ≈ log Ω. Verdict: ℤ's comb is additively generic up to prime-power ladders — no structural resonance advantage or
disadvantage; multiplicativity can only act via P_T-correlation. No sign contact.
| N_BUILD_015 / SYNTHESIS_188 | consolidation of both tracks: results table, new barriers, positive structure (Pos ≠ ∅, κ*), frontier; grid log 45 and crossword addendum appended | record |

### (L2) — 021: random combs and the integer ceiling
L2_BUILD_021: Poisson density-matched comb: exact Campbell mean (m^♯-form) and variance 4∫u(Re c_F)²du (PROVED); at φ₀ the variance is
16T²I, CLT ⇒ P(𝔞^ν(φ₀) ≥ 0) → ½: 𝒯₀ alone is a coin flip, ζ not exceptional there (PROVED). Joint positivity on the clamped span
≈ exp(−cT²) (ARGUED, Dean–Majumdar analogy). Prop 4 (from phase-159 Theorem D + N_011): combs on log ℕ that are ∀T-positive have
residue ≤ 1 < κ* — positivity on log ℕ is never density-driven; ζ sits at the ceiling. Consistency: N_011/018 (κ > 1) are not on
log ℕ — no contradiction; integer test-function structure is destructive for density. No sign contact.
| N_BUILD_016 | anti-alignment: (b) −∂_s log U_s is the commuting multiplier −(ζ′/ζ)_N — no monotonicity/convexity in s (two-bump tests) NO-GO; (a) **exact Gram identity: comb = −‖F‖²∂_s log‖U_sF‖² (ℤ-additive centre, Λ-blind) + 2Re⟨a⊥,c⊥⟩ (Möbius⊥ × log⊥ interaction)** using μ*1 = δ; Cauchy–Schwarz loses ≍T (ARGUED); target = anti-alignment of a⊥, c⊥ | PROVED / NO-GO / OPEN |
| N_BUILD_017 | centre 𝒞(F) = ‖F‖²(4T − ⟨1/(¼+τ²)⟩_{|F̂|²/(¼+τ²)}) + O(Te^{−T}) — **positive, size 4T (wrong sign)**: the main term N^{1−s}/(1−s) of ζ_N survives in the quadratic Gram norm though Tate kills it in the comb; interaction must be ≈ −4T; no slack (NO-GO); repair by subtracting the main multiplier makes (G1) inexact (smoothed Mertens) | PROVED (uniformity ARGUED) / NO-GO |
| L2_BUILD_021 review | §4 Prop 4 CONFIRMED (cond. on Q′): same form as P46 𝔞_T on P_T; log ℕ support built into Thm D, load-bearing via resolution (gap 1/M ⇒ arch gain log M ≈ density gain); κ>1 combs (ρ_κ, 018 lattice h≪e^{−e^T}) escape, no contradiction; "only via P_T-correlation" → HEURISTIC; Thm D, N_011, 018 all correct | PROVED / HEURISTIC |

### (L2) — 022: large deviations; ζ's clamped-span matrix
L2_BUILD_022: exact exponential moments via the Poisson Laplace functional (PROVED); NO-GO: single-functional Chernoff + nets give only
P(M ⪰ 0) ≤ ½ + o(1) on the clamped span (PROVED) — decay needs independence; independence route via lag-disjoint tests gives exp(−cK),
K ≍ T, but construction of lag-disjoint P_T tests is OPEN (Tate correction spreads lags). exp(−cT²) remains ARGUED. ζ's matrix: X_ζ =
Z − M₀ with Z the zero-sum Gram (identity); on-line zeros give O(T^{−4}) per entry, so in the verified range ζ's low-mode fluctuation is
O(1) vs Poisson's ≍ T: "super-regular", ≈ exp(−cT log T) outlier (ARGUED). No sign contact.
| N_BUILD_018 | linear-centre split = N_006 §2 rewritten ((Ω_μ); Prop 1 PROVED); **meta-theorem: shift-multiplier calculus = 𝔄_T-linear identities + Bochner/C–S** ⇒ NO-GO for further operator splits in C–S form; survivor: SOS certificates; next object: divisor-lattice SOS (arithmetic squares A^*A with atoms at log of rationals), first test at ½log3 | PROVED / NO-GO / OPEN |

### (L2) — 023: lag-localized primitive tests
L2_BUILD_023: Lemma L — translates of F₀ = (¼−∂²)G₀ are primitive, c_F lives on the difference set ± 2T₀, central window atom-free if
2T₀ < log 2, polar density cancels EXACTLY in every window (no Tate correction needed; 022's obstacle removed). Lemma C — archimedean
cross term O(e^{−5d/2}) (k = 0 term cancels), polar kernel cross term 0. Theorem T — two-sided (Ξ): target ⇒ |Ξ_{F₀}(d)| ≤ 2a₀ + O(e^{−5d/2})
at every scale (sharpens N_014 Cor A′). Theorem P — random Poisson combs (any κ): P(λ_A(T) ≥ 0) ≤ exp(−T log T/(4T₀)(1+o(1))),
rate → 1/(2 log 2) (PROVED, Esseen CITED). No sign contact.
| N_BUILD_019 | SOS vs dual class: SOS with free p.d. part = Paper 46 dual class (D) (Prop 1, PROVED; lossless by thm:D1, no new content); **pure-arithmetic SOS (atoms only from squares of Dirichlet polynomials) is EMPTY for every T ≥ ½log3** (needs m ≥ A_T and λ_{∞,P} ≥ m; by hand λ_{∞,P}(½log3) ≤ 0.33 < 0.980 ≤ A_T) — divisor-lattice SOS DEAD | PROVED / NO-GO |
| L2_BUILD_023_REVIEW | Review of 023: L, C, T, P CONFIRMED; FIX Lemma C denominator (1−e^{−2(d−2T₀)}); T novelty DOWNGRADE (implicit in N_014 §3); P FIX: rate exp(−cT log T) for every c>0 (T₀↓0), 1/(2log2) is the worst constant | CONFIRMED / FIX |

### (L2) — 024: single-profile Bochner reformulation
L2_BUILD_024: Theorem T is sharp only CONDITIONALLY (identity: B(d) = Σ|F̂₀(γ)|²cos γd; sup attained under Kronecker independence of ordinates).
Theorem S: for ONE explicit profile F₀ = (¼−∂²)(g*g̃*g*g̃), g = e^{bt}1_{[0,a]} (F̂₀ = (τ²+¼)|ĝ|⁴ > 0 on ℝ), target ∀T ⟺ B_{F₀}(d) := 𝔞(F₀, τ_dF₀)
is positive definite on ℝ. (⟹) PROVED; (⟸) PROVED modulo Lemma I (distribution identification, ARGUED). Multi-copy spans = finite sections;
Theorem T = 2×2 case. A reformulation (cf. KEP), window-free; no sign gained. No sign contact.
| N_BUILD_020 | Poisson-dual exterior = integer-log positions (FE self-dual at s=½): prescribed coefficients = prime part of thm:Z flat-top class (corpus); **Thm 2: exterior certificates supported beyond large U have negative value (via W-tail)**; free-coefficient ceiling = constrained window forms (Prop 3); dual-class route exhausted in all known exterior choices | PROVED / NO-GO / ARGUED |
| SYNTHESIS_188 update 2 | rows 38–48 (N_016–020, L2_020–024, reviews of 021/023), §5 «Primal and dual sides reduced to D», grid log 46, crossword update 2 | record |

### (L2) — 025: Lemma I, Theorem S closed; σ-family
L2_BUILD_025: Lemma I written in full (approximation of ψ = |Ĝ|²/F̂₀² by compactly supported lag tests; prime sum dominated since the profile
is analytic beyond the polar line, b > ½). **Theorem S PROVED**: λ_A ≥ 0 ∀T ⟺ B_{F₀} positive definite, for the explicit profile
F₀ = (¼−∂²)(g*g̃*g*g̃), g = e^{bt}1_{[0,a]}, b > ½. Honest: a reformulation; new only "one fixed profile, no T" (cf. Weil positivity, KEP).
Proposition H (PROVED, Hadamard/Euler/FE CITED): D_σ = 2Re ξ′/ξ(σ+iτ) ≥ 0 for σ > 1, giving an explicit autocorrelation B^{(σ)} = h_σ⋆h̃_σ built
from Γ and an absolutely convergent Λ-series; uses Euler × FE jointly; does not apply to a_P, Epstein, Beurling. Stops at σ = ½ (the B pairing is
analytic continuation, not a boundary value): explicit h at σ = ½ OPEN. No sign contact.

### (L2) — 026: FE reflection of the σ-family
L2_BUILD_026: Prop H of 025 is classical (CITED-known). FE + reality ⇒ D_{1−σ} = −D_σ exactly: symmetrization is identically 0 — NO-GO (PROVED);
at σ = ½ the boundary density vanishes pointwise off on-line zeros — pointwise form of the exact criticality (010, N_013). Window-level comb family
B^{comb}_σ: continuous through ½, PD for σ > 1, and PD on any σ_j ↓ ½ ⇒ target (limit lemma, PROVED). Intermediate σ: deformed problems (damped comb,
non-vanishing polar term p_σ < 0 at 0); controlling them via residues = zero location (cor:void) — not built; density margin O(σ − ½) (ARGUED). No sign contact.
- L2_BUILD_024_025_REVIEW.md: Theorem S PROVED with FIXes (|b| > ½; even cut-off; density via H ∈ H²₀ — dilation of G breaks Tate); Prop H CONFIRMED, content classical (Lagarias-type Re ξ′/ξ > 0 on Re s > 1); σ>1→½ transport must clear cor:void C_zeros clause.

### (L2) — 027: conjugation test
L2_BUILD_027: deformed window problem at σ with its own primitive class P^σ_T (Tate exponents ±(1−σ), codim 2 by lem:polar). Exponential conjugation
cannot match Tate points (only at σ = ½) (PROVED). Dilation r = 1−2η matches them but sends the comb to positions n^{1−2η} (non-integer, Beurling-type):
P(½+η) is conjugate to a ½-problem for a different comb — NOT a reformulation of D (PROVED). Window family has no known endpoint (at σ > 1 the form is
∫(D_σ − p_σ)|F̂|², p_σ > 0 not annihilated) — OPEN. Cleanest interpolation with a known endpoint: P_prof(σ) = "B^comb_σ PD" (σ > 1 known, ½ ⟺ D, limit
lemma); missing a comb-level propagation (M) — zero-location proofs excluded (cor:void). No sign contact.

### (L2) — 028: integer-lattice matrices
L2_BUILD_028: A_M = [B_{F₀}(log(m/k))]_{m,k≤M} ⪰ 0 ∀M ⟺ D (PROVED: log-ratios approximate any configuration, B continuous). Structure: Arch − Div − Near,
Div = Dirichlet-convolution by v_n (Redheffer-type), diagonalized on the Bohr torus 𝕋^∞; NO-GO: multiplicativity does not diagonalize A_M (archimedean
convolution in the real lag log r, unbounded on ℓ²(ℚ_{>0}); near-coincidences) (PROVED). Theorem D's test at the ceiling: Q(M) = (γ + C_χ + log(1/θ))log M
+ o(log M) (Mertens CITED, archimedean ARGUED): log²M cancels exactly at r = 1; next order positive only through resolution θ — no certificate. No sign contact.

### (L2) — 029: separated multiplicative sets
L2_BUILD_029: on S = {Π p_i^{k_i}} with profile width < e^{−2L}/2, Near vanishes and A|_S = a₀I − (Kronecker sum of one-prime Toeplitz D_i) + O(e^{−5 log2/2})
(PROVED); local symbol δ_p(θ) = 2log p Re[x/(1−x)], x = p^{−½}e^{iθ}, range [−2log p/(√p+1), 2log p/(√p−1)] (exact; min = phase-146 threshold). λ_min ≈ a₀ −
Σ 2log p_i/(√p_i−1). Separation forces a₀ ≳ 2L, so ζ (and a_P) pass trivially, for local reasons; only gross amplification fails. No certificate: the sign of D must
involve near-coincidences (Near). No sign contact.

### (L2) — 030: Near as shifted convolution
L2_BUILD_030: s^TA_Ms = s^TW_ms − s^TW_1Vs = (1/2π)∫F̂₀²|P_s|²[m − Re V(τ)] (V Dirichlet convolution by v_n; Dirichlet polynomials multiply) (PROVED). Splitting by
h = m − kn: Div = h = 0, Near = |h| ≲ 2T₀m (≤ c when 2T₀ = c/M): boundedly many shifted convolutions Σ_{m−kn=h}s_ms_kΛ(n)/√n weighted by c₀(h/m). W_1 PSD, W_m and
W_1V indefinite; Near has no sign of its own (finite-resolution remainder of |P_s|²V). Ramanujan expansion: Q = m^♯-form − Chebyshev fluctuation (q=1) − Σ_{p^b}
additive-character components (exact in analytic pairing; discrete interpolation ARGUED). Arithmetic of Σ_{m−kn=h}Λ(n) left to (N). No sign contact.
| N_BUILD_021 | Near_M = s^T[Ξ_{F₀}(log(m/k)) − exact]s (local fluctuation at every scale × test-vector correlation); **Thm 2: every progression/short-interval class (BV, BDH, Siegel–Walfisz, Titchmarsh divisor, Brun–Titchmarsh) is closed under finite modification ⇒ KILLED by cor:void**; Prop 3: χ-twisted vectors give a hybrid (ζ-Arch − L(s,χ)-Div − ζ-Near with non-multiplicative phases), not L(s,χ)'s window form — conductor>1 family not an exact input via A_M | PROVED / NO-GO |

### (L2) — 031: residue-balanced subspace
L2_BUILD_031: constraint families (R_Q) rough support and (B_Q) residue-balanced blocks (kill small-prime Div / small-modulus components). Theorem E (PROVED):
positivity of A_M on either family for all M ⟺ D (approximation of configurations by rough integers / balanced blocks + continuity of B + Theorem S).
So "q=1 Chebyshev fluctuation ≤ m^♯-form on the balanced subspace" is EQUIVALENT to D, not weaker; at fixed M only a finite section. m^♯-form ≥ (C₀+4)s^TW_1s, not
positive — anti-alignment still needed. finmod/W-tail transfer through the equivalence: no escape. No sign contact.
| N_BUILD_022 | exact matrix identity ZΔ = [L,Z] ⇔ Δ = Z⁻¹LZ − L (1*Λ = log; = R162_903 B2.1, corpus-known); Δ + L similar to diag(log m) (spectrum log m, tr Δ = 0) — no sign; X_M not reached: Near = discretization defect of the Möbius-transport convolution, vanishes only on Near-free supports (trivial by L2_029) ⇒ NO-GO; Bohr symbol = Theorem S | PROVED / NO-GO |
