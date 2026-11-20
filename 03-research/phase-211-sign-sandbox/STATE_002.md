# State of phase 211 after rounds 5–20

Sources: STATE_001.md (rounds 1–3), ROUND_005_A … ROUND_020_A, REVIEW_004 … REVIEW_009, TOOL_001_GALERKIN_MP.md,
LEDGER.md. Labels of rounds 5–13 are the review verdicts (REVIEW_004–009: CONFIRMED read as PROVED, DOWNGRADE read as the
label given). Rounds 14–24 are reviewed in REVIEW_010; §2–§3 carry its verdicts (§1 still shows the pre-review wording
where it says "unreviewed"; REVIEW_010 governs). Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN /
NO-GO / NUMERICAL. The target is treated as a statement about one quadratic form; no equivalence of it with any
statement outside STATEMENT_001 is used.

Notation (STATEMENT_001, Paper 47): a_T = Arch − Π on P_T (Tate moments A = B = 0), λ_A(T) = inf a_T on the unit
sphere of P_T, N = e^{2T}, λ = e^T, v_n = 2Λ(n)/√n, m(τ) = Re ψ(¼ + iτ/2) − log π. Exterior coordinates (P47 §sec:ext):
Ef = Φ_f − Ψ_f, tail form 𝒲̂ = 𝒜_∞ + 𝒯 − 𝒞 on Poisson tails Ψ ∈ V_T with archimedean part 𝒜_∞, Tate part 𝒯,
comb part 𝒞; 𝒜𝒫 := 𝒜_∞ + 𝒯; R_T the gauge radicals; ℓ_g the gauge-quotient leakage.

---------------------------------------------------------------------------------------------------------------------
## 1. The target and the exact reformulations obtained in rounds 5–20

(★) λ_A(T) ≥ 0 for every T > 0. Known: PROVED (certified) for T ≤ ½log5; CITED for T ≤ ½log15 through
λ_W ≤ λ_A and the complete-form certificate (λ_A ≥ λ_W ≥ 2^{−2904}, analytic lemmas of the source not audited;
REVIEW_005); OPEN beyond.

| # | Reformulation | Label | File |
|---|---|---|---|
| R1 | Comb-response object E_T = N′ ⊕ P_𝒞Π(𝒩_η + 𝒯): negative Nyquist block plus comb responses, identified with the Λ-twisted Dirichlet polynomials on the mesh (Prop 2, 2′); Tate gauge; exact reduction of (★) to E_T with archimedean-only block coupling (Thm 2) | PROVED (REVIEW_005; mesh-square identity is a truncated convolution for N ≥ e^{2T}) | ROUND_005_C |
| R2 | Sign budget a_T = σ_T‖F‖² + κ(F) − ℛ(F) on P_T, σ_T = C₀ + 4 + Σ_j 2e^{−(4j+1)T}/(2j+½); σ_T‖F‖² + κ = 𝔞^♯ (P47 prop:sharp), ℛ = Π + 𝔢 (lem:polarelim); σ_T > 0 only for T < 0.0520; sign lemma ⟺ Π ≤ Arch on E_T | PROVED (|σ_T| → −σ_T correction, REVIEW_004) | ROUND_005_C, ROUND_007_B |
| R3 | (L2′) extended to the two-parameter (shift, gauge) family: (★) ⟺ S ⪰ 0 on the non-positive Nyquist block N′, complement coercive | PROVED (STATE_001 P15; gauge extension ROUND_005_C Lemma 1, CONDITIONAL until the gauge is chosen off a countable set, REVIEW_004) | ROUND_001_C, ROUND_005_C |
| R4 | Band reduction (packet form): (HR)(a) on the high block ⟹ pointwise P^ρ_T(τ₀) ≤ m(τ₀) − κ + o(1) for all profiles; all-profile form ⟺ λ_max(A_τ) ≤ m(τ) − κ; band-restricted packet identity Q_T(β cos τx) = ½‖β‖²[μ_η + D + X − R] with A_τ^{(η)} the compression to K = ⌊2Tητ/π⌋ envelope modes | necessity PROVED, equivalence not proved (REVIEW_009); band identity PROVED (unreviewed) | ROUND_011_A, ROUND_012_A, ROUND_016_A |
| R5 | Closed matrix-free form 2T𝔈 = CS − ESCE + ESHE + HS + Dd of A_τ^{(η)}: the comb acts on the band only through two Dirichlet-polynomial vectors s_k, d_k at frequencies τ ± a_k | PROVED (unreviewed) | ROUND_017_B Prop 1.1 |
| R6 | Weyl counts: two-sided count of the near-null cluster of a_T (Thm 3.1); λ_max(Π_T)/A_T ∈ [¼, ½]; joint-symbol cluster size exp(2e^T(1+o(1))) | PROVED (REVIEW_005/006) | ROUND_005_E, ROUND_006_A, ROUND_006_C |
| R7 | Margin law: exterior upper bound W_T(Ef) ≤ Kλ^{−2}(L₁² + L₂²) on 𝒜⁺_T; index count: λ_A is bounded by the worst weighted leakage over any 5-dimensional edge-regular even space (four constraints f(0), ℱf(0), A(Ef), B(Ef)), λ_W over any 3-dimensional one | PROVED given thm:ext-half (REVIEW_006) | ROUND_008_E Thm 3.1, Cor 3.2, Prop 3.3 |
| R8 | Prolate index-8 law: with mollified self-dual prolate blocks V_d, quotient ≤ C_dN⁹(1 − χ_{2d−2}); λ_A ≤ 4KC_5N⁹(1 − χ_8), λ_W ≤ 4KC_3N⁹(1 − χ_4) | PROVED given thm:ext-half (REVIEW_007; hypothesis c ≥ 12, N ≥ 410) | ROUND_009_A Lemma 3.4′ |
| R9 | Fourier-class selection rule: P_{−ε}Π_TEf = ½RΠ_TE(ℱf − εf); diagonal Fourier defect on prolates; cross term a_T(w_+, w_−) ≡ 0 by parity; diagonal = 𝒲[Ψ_{f_+}] − a_T(w_+); floor index 8 in class +1 | PROVED (identities); stiff-elimination bound (2.1) CONDITIONAL on κ(K), κ_C, ‖Gram‖ (REVIEW_008) | ROUND_009_B |
| R10 | Half-line / radical identity: W_T(Ef) = 𝒲̂[Ψ_f] on admissible data, 𝒲̂ constant on gauge fibres (Λ ∗ 1 = log via Poisson summation); second-level form b(Eg) = 𝒲(Ψ_f, Ψ_g) | PROVED (ROUND_001_B Thm 1.1, Cor 1.2, zero-free; ROUND_017_A second level unreviewed). It is the only Λ-specific input of every route below | ROUND_001_B, ROUND_015_B, ROUND_017_A |
| R11 | Tail form: high block M ⪰ 0 on 𝒜 ⟺ 𝒢 ⪰ 0 on S𝒜 (exact transfer b = Sa; 𝒢 defined only on S{f(λ) = 0}); M = S𝒢S on admissible prolate data; entrywise 𝒢^ρ on mollified data, SMS − 𝒢^ρ rank ≤ 8; comb on Poisson tails = 2⟨𝒯_{log}u, 𝒯u⟩; dilation form F_N = N^{−1/2}τ_{log N}F₁ (T-free) | PROVED (012B reviewed; 014A, 015A, 016B unreviewed) | ROUND_012_B, ROUND_014_A, ROUND_015_A, ROUND_016_B |
| R12 | Tail reduction: E(admissible) ⊇ C_c^∞(I_T) ∩ P_T, hence (★) ⟺ (ii) 𝒲̂ ≥ 0 on core E-images (= eq:ext-starstar with κ = 0) | PROVED (unreviewed) | ROUND_019_B Prop 1.1, Cor 1.2 |
| R13 | Comb-null formulation: (★) ⟺ 𝒜𝒫[Ψ] ≥ 0 for every Ψ ∈ V_T with 𝒞[Ψ] = 0 (weight-scaling invariant; its equivalence with (★) uses R10) | PROVED (unreviewed) | ROUND_020_A Cor 1.4 |
| R14 | Split (A) + (B_δ, s): (A) = R10; (B_δ, s) = 𝒲̂ ≥ δ|𝒞| on a Λ-free section s; (A) + (B) ⟹ (★) | PROVED implication; (B) OPEN (unreviewed) | ROUND_020_A §3 |
| R15 | Neumann/Schur form: a_CE = Arch_CE − Π_CE P_V; finite sufficient inequality 𝒫_K(v) ⪰ 0 at fixed T, N | PROVED CONDITIONAL on (H₋); "only if" of Cor 3 DOWNGRADED (REVIEW_005) | ROUND_008_D |
| R16 | Survivor's Schur functional: b = ∫⟨Ψ_*, G(·+u)⟩dν, ν = ½K du + Σ Λ(n)n^{−1/2}δ_{log n}; b_Tate ≡ 0 on P_T | PROVED (unreviewed) | ROUND_017_A |

---------------------------------------------------------------------------------------------------------------------
## 2. PROVED pieces (review verdicts applied)

| # | Statement | File | Label after review |
|---|---|---|---|
| Q1 | Certified falsifiers (arb ball arithmetic): a_3 and the Beurling system 3 → 3.2 give λ < 0 at ½log5 + 10⁻⁴ (hence all larger T); 1.1Λ gives λ < 0 at T = 1; witnesses in tools/falsifier_cert.py | ROUND_007_C | PROVED (REVIEW_005); makes the identity-mechanism NO-GO of ROUND_005_C fully PROVED |
| Q2 | Explicit doubly-exponential upper bound λ_A(T) ≤ 3.2·10²³ N^{33/2} e^{−2πN}, N = e^{2T}, N ≥ 1.6·10⁶ (finite constant below) | ROUND_009_A (l. 244) | PROVED given thm:ext-half (REVIEW_007) |
| Q3 | First-cell certificate: (1/2π)∫m|F̂|² ≥ 0.069611‖F‖² on ∫F e^{−y/2} = 0, length log 2, T-free; four transported constraints μ₄(0.8) ≥ 0.52763, μ₄(1.0) ≥ 0.54941 | ROUND_017_C | PROVED, arb-certified (REVIEW_010; cert_f0.py re-run reproduces the ball); κ_T ≥ (λ/2)μ₄ in ℓ_g CONDITIONAL; weight-blind |
| Q4 | Three-cell certificate: complete form ≥ 0.70·ℓ_g on transported constraints at T = 0.8, 1.0; transfer Lemma 1.1 (δ* = 0.075); piecewise compression with exact 𝔇₃ | ROUND_018_A Thm 3.4 | PROVED, arb (REVIEW_010; cert3.py re-run at T = 0.8 reproduces); ℓ_g is half of Paper 47's ℓ; a coercivity piece: survives a_3 (certified ≥ 0.60·ℓ_g) and every change beyond m = 2 for systems whose integers agree with ℕ below N (ROUND_019_A §5, corrected) |
| Q5 | Selection rule (R9) | ROUND_009_B | PROVED with REVIEW_008 parity correction; Λ-free, not a sign step |
| Q6 | Sandwich λ_W ≤ λ_A ≤ λ_{W,2}; lower half ⟺ (N1′) μ₁ ≥ L + Tate bound | ROUND_007_D | PROVED (REVIEW_005); floor transfer to ½log15 is a restatement of CITED input |
| Q7 | −log λ_A(T) ≤ 4πe^{2T} − 9T + O(1) under the κ-band hypothesis; no law −log λ_A = c₁e^{2T} + O(T) with c₁ > 4π on an unbounded range | ROUND_007_D Prop 4.4 | CONDITIONAL (REVIEW_005) |
| Q8 | Virial bracket for the one-sided variation of λ_A in T; edge-budget bracket (Prop 3); discrete Grönwall (Prop 4) | ROUND_008_C | Thm 1 CONDITIONAL on restriction property; "iff" at contact thresholds DOWNGRADED (REVIEW_006) |
| Q9 | Exterior bound and index count (R7); mollified prolate leakage (R8) | ROUND_008_E, ROUND_009_A | PROVED given thm:ext-half |
| Q10 | Symbol form (3.1), L² Markov; lem:ext-hf void on polynomial-index data; prolate cross-overlaps ≡ 0 | ROUND_010_A | PROVED (REVIEW_008/009) |
| Q11 | Emptiness of {P^ρ_T ≥ ϑm} above Ω_B, log Ω_B = (64/(eϑ²))Te^{2T}(1+o(1)); sup_{[N²,2N²]} P^ρ_T ≥ c₁T | ROUND_011_A | PROVED; value DOWNGRADED (superseded by the trivial bound, REVIEW_009) |
| Q12 | Packet bound (1.2) on [Ω_lo, ∞) for all profiles at T ≤ log 2, for cos² at T ≤ 2.64 (interval-certified); all-profile ⟺ λ_max(A_τ) ≤ m − κ | ROUND_012_A | PROVED (REVIEW_009) |
| Q13 | Type I sums above the plunge are pure dual; exact self-duality P^ρ_T = 𝒜_w + R_w | ROUND_013_A | Lemma 1.1 CITED (Poisson/B-process); identity PROVED, reformulation of (U) (REVIEW_009) |
| Q14 | Class = exact sign on out-of-band data; H₊–H₋ coupling = −tail Gram | ROUND_012_B | PROVED (REVIEW_009) |
| Q15 | Matrix-free closed form of A_τ^{(η)} (R5) | ROUND_017_B | PROVED (REVIEW_010, recomputed) |
| Q16 | Qualitative band constraint vacuous on R-cell data: 𝔅_R ∩ V_R dense in V_R, inf Q_R/ℓ_g unchanged | ROUND_019_A Prop 1.1 | PROVED (REVIEW_010) |
| Q17 | Gauge radicals Φ_φ with B = 0 and 𝒜𝒫 of both signs (→ −11.457‖η‖², → +1.114‖η‖²); inf of 𝒲̂^c over each gauge fibre is −∞ for every c ≠ 1 | ROUND_019_B Thm 2.1, Cor 2.2 | PROVED, zero-free (REVIEW_010) |
| Q18 | Fibre lemmas and representative margins: every fibre meets {𝒞 = 0}; best-representative c-margin is ℝ or ∅ by the sign of 𝒲̂; S-lemma multiplier forced to 1 | ROUND_020_A Lemmas 1.1–1.2, Thm 1.3, Thm 1.5 | PROVED (REVIEW_010; Thm 1.5 on finite-dimensional sections, ARGUED in general) |
| Q19 | Structure of the Krylov/word families: every homogeneous word family is cΛ-invariant as a set; Lanczos blind to the cluster at rate O(λ₂ − λ₁) | ROUND_005_A, ROUND_006_B | PROVED (sign claim of 005_A Prop 3.4 ARGUED; halo kernel −½K) |
| Q20 | Exact ledger of the survivor, rung tail Grams (Lemmas 1.1–1.2) | ROUND_018_B | PROVED for f(λ) = 0 data; survivor (f(λ) ≠ 0) ARGUED via mollified limit (REVIEW_010) |
| Q21 | Exact transfer M ⪰ 0 on 𝒜 ⟺ 𝒢 ⪰ 0 on S𝒜 (tail form defined on S{f(λ) = 0}); Toeplitz/banded sweep lemma | ROUND_014_A Thm 1.1, Thm 3.1 | PROVED (REVIEW_010) with 𝒢 built from the complete form of Paper 47 def:ext (polar term 2AB) |
| Q22 | Mollified entrywise tail Gram, SMS − 𝒢^ρ rank ≤ 8; comb on Poisson tails = 2⟨𝒯_log u, 𝒯u⟩; exact chirp ledger; Montgomery–Vaughan control of non-resonant chirp pairs in the dilation model | ROUND_015_A Lemma 1.0, Prop 1.1, Thm 3.1, Cor 3.2, Thm 3.3 | PROVED (REVIEW_010; complete-form reading; Cor 3.2 needs absolute convergence of the archimedean double series; Cor 3.4 = one model value) |
| Q23 | Exact packet identity Q_T(β cos τx) = ½[m‖β‖² − ⟨A_τβ, β⟩ + D + X − R]; leakage of V_η; band-restricted reduction (HB_η) | ROUND_016_A Thm 1.1, Lemma 1.2, Props 1.4–1.5, Thm 1.6 | PROVED (REVIEW_010; X-constant 5.72 → 5.73 for τ ≥ 10; P_T transfer ARGUED) |
| Q24 | Dilation form F_N = N^{−1/2}τ_{log N}F₁; first Poisson cell is comb-free | ROUND_016_B Lemmas 2.1–2.2 | PROVED (REVIEW_010) |
| Q25 | Schur form of λ_A at the survivor; coupling vector b = ∫h_G dν, b_Tate ≡ 0; second-level identity on E-images; parity identity; falsifier entry through the radical defect X | ROUND_017_A Props 1.1–1.3, 3.1, (4.1) | PROVED for f(λ) = 0 data (REVIEW_010); survivor and Prop 1.3 norm ARGUED |
| Q26 | Truncated Dirichlet homomorphism Φ_R (any multiplicative system); P_w𝔇_R = [M_x, 𝔇_R] iff w ≡ 1; Q_R^{(c)} = Q₀ − c𝒦_R; window sandwich; first variations in generators and exponent; operator Selberg identity [M, P] = 𝔇⁻¹[M,[M,𝔇]] − P²; dilation picture; edge bounds | ROUND_021_A §3.1, Prop 3.2, Lemma 3.3; ROUND_022_A Lemma 3.1, Prop 3.2; ROUND_023_A Lemma 2.1, Props 2.2–2.3, Lemma 4.1 | PROVED (REVIEW_010); 21A two-sided shrinking: one direction PROVED, c₋ side NUMERICAL; 22A Prop 3.3 structural statement true with corrected proof; 23A Prop 2.4 must include the polar functionals |
| Q27 | Entrance law: c_F(2T − δ) = δF(T⁻)F̄(−T⁺) + O(δ^{3/2}) in H¹; a newly entered contact contributes −2hv_nF(T⁻)² on real even states | ROUND_024_A Lemmas 4.1–4.2, Prop 4.3, Cor 4.4 | PROVED (REVIEW_010); Cor 4.4(ii) CONDITIONAL on (R_edge); weight-generic, not a sign step |

---------------------------------------------------------------------------------------------------------------------
## 3. NO-GO results (class and status)

| # | Class | Reason | File | Status |
|---|---|---|---|---|
| N1 | Comb-Krylov families at bounded degree j | cluster not captured; mechanism PROVED | ROUND_005_A/B | NO-GO (PROVED mechanism + NUMERICAL) |
| N2 | Floor-only Schur certificates on enlargements of the block by comb responses | c_need 2.5–8.9 against λ_min(C) ≈ 1.3 | ROUND_005_C | NO-GO (NUMERICAL instances, PROVED logic) |
| N3 | Identity-based sign mechanisms on E_T (Selberg, local Euler factors, Lévy kernel) | defeated by the certified falsifiers Q1 | ROUND_005_C, ROUND_007_C | NO-GO PROVED |
| N4 | Ground-state transform / weighted Poincaré, class 𝒦_gap | tautological once the slack is named; lands on polar capacity | ROUND_005_D | NO-GO ARGUED (REVIEW_005) |
| N5 | Homogeneous word families in {M, Π_P} | cΛ-invariant as sets ⇒ pencil | ROUND_006_B | NO-GO PROVED |
| N6 | Weyl caps from Arch − θ; single-exponential λ_A laws | λ_max(Π_T)/A_T ≥ ¼ | ROUND_006_A, ROUND_007_D | NO-GO PROVED / NUMERICAL |
| N7 | Crossing-window / per-minimiser budget statements; sub-part/dominant-part arguments on the response cubic | bookkeeping-dependent; degree parts ±1.4·10⁻³ cancel to 3·10⁻¹² | ROUND_007_B | NO-GO (PROVED bookkeeping; NUMERICAL cancellation) |
| N8 | Finite-degree Neumann class | degree ∝ log 1/λ_A | ROUND_008_D | NO-GO (NUMERICAL) |
| N9 | Grönwall-in-T route, class 𝒦_H | restatement | ROUND_008_C Prop 5 | NO-GO |
| N10 | PEψ₀ alone as test vector | index count | ROUND_008_E | NO-GO |
| N11 | Comb-mass-only class 𝒦_S below e^{S−C} | plunge not the only remainder | ROUND_010_A Prop 3.3 | NO-GO PROVED (reading DOWNGRADED) |
| N12 | Measure bound + Logvinenko–Sereda/Kovrijkine; moment class below log τ ≈ 8T² | collapses to the pointwise bound | ROUND_011_A | NO-GO (Prop 2.2 PROVED; moment limit ARGUED) |
| N13 | Two-block and three-block (class-split) Schur assembly of the high block | θ_K → 0, θ₃ < 0 at resolved points | ROUND_011_B, ROUND_012_B | NO-GO NUMERICAL |
| N14 | Fixed-profile trivial bound, short packets, MV + Sobolev for (U) | — | ROUND_012_A | NO-GO |
| N15 | Vaughan/Heath-Brown + B-process class 𝒱 | exact reassembly reproduces (U) | ROUND_013_A | NO-GO |
| N16 | Index-axis symbol + band/Toeplitz error for the high block in D-units | D-bottom → 0 with K; band non-decaying | ROUND_014_A | NO-GO NUMERICAL (REVIEW_010: class correct; does not cover ℓ_g-normalised sweeps) |
| N17 | No R-uniform constant for the R-cell complete form against ℓ_g on idealised data; band constraint (qualitative) vacuous | κ_R ≈ 0.81/0.75/0.68 (R = 2–4), collapse at R ≥ 5 | ROUND_018_A, ROUND_019_A | NO-GO (Prop 1.1 PROVED; collapse NUMERICAL; REVIEW_010) |
| N18 | Rung piece of the Schur inequality as sign carrier (tail form, c·log N) | survives c ∈ [0, 3.5]: comb-generic | ROUND_018_B | NO-GO NUMERICAL, falsifier (a) only (REVIEW_010) |
| N19 | Comb-robust / weighted "archimedean coercivity beats the overlapping comb" bounds for (ii) on the full class of admissible tails | Q17: 𝒲̂^c unbounded below on every fibre for c ≠ 1 | ROUND_019_B Cor 2.3 | NO-GO PROVED, zero-free (REVIEW_010) |
| N20 | Existential gauge-fixed representative with comb margin | Q18: margin ℝ or ∅ by the sign of 𝒲̂ | ROUND_020_A Thm 1.3 | NO-GO PROVED (REVIEW_010) |
| N21 | Canonical Λ-free sections with uniform δ (ℓ-section, f2, tail-L²) | δ → 0.0035 / 0.24 / 0.37 as resolution grows | ROUND_020_A §2 | PIVOT, NUMERICAL (REVIEW_010) |
| N22 | Positivity windows in the comb weight on idealised R-cell data (uniform, per prime, per atom) | J_R → {1} is the collapse λ₀(R) → 0 read in c; c-dependence is c·𝒦_R with 𝒦_R Λ-free; mechanism survives Beurling systems | ROUND_021_A | NO-GO (REVIEW_010; c₋ side of the shrinking NUMERICAL) |
| N23 | R-cell sign as a monoid invariant / additive characterisation of ℕ on the exponent ray ℕ^{1+t} | ℕ at the minimum-margin end of its segment; both edges from generic cluster collapse | ROUND_022_A, ROUND_023_A | NO-GO NUMERICAL + ARGUED reading (REVIEW_010) |
| N24 | Finitely many strict Chebyshev floor relations at the sharp truncation | open in c around Λ on bounded ranges | ROUND_024_A Prop 2.1 | NO-GO CONDITIONAL on the NUMERICAL width of J_T (REVIEW_010) |
| N25 | Positivity propagated through contact entrances along N | entrance term −2hv_nF(T⁻)² on even states, weight-generic; reduces to the rate bound (EB_C) | ROUND_024_A §4 | NO-GO PROVED for the sign of the entrance term (REVIEW_010) |
| N26 | Prolate extremality on the index-8 constrained subspace | retry of L′/L′♯; gauge directions kill it | ROUND_024_A Design C | NO-GO ARGUED (REVIEW_010) |

---------------------------------------------------------------------------------------------------------------------
## 4. NUMERICAL facts

λ_A table (Galerkin, multiprecision; upper bounds for λ_A up to matrix error; bottom vector even at every T; sources
TOOL_001 §2–3, ROUND_007_D §1, ROUND_016_A):

| T | λ_A (Galerkin) | N, digits | precision note |
|---|---|---|---|
| ½log3 | 1.008·10⁻³ | 80, 40 | above certified lower bound 8.86·10⁻⁵ |
| log 2 | 1.1137·10⁻⁷ | 80, 40 | reproduces P47 App. C |
| ½log5 + 10⁻³ | 3.088·10⁻¹² | 80, 40 | — |
| 0.9 | 6.03·10⁻¹⁷ | 80, 40 | earlier double value 4.5·10⁻¹⁵ was round-off |
| 1.0 | 1.74·10⁻²³ | 120, 40 | ≈ 10 % between N = 90 and 120 |
| 1.05 | 2.24·10⁻²⁷ | 150, 60 | — |
| 1.1 | 1.077·10⁻³¹ | 180, 60 | 6 % |
| 1.15 | 2.48·10⁻³⁶ | 150, 60 | — |
| 1.2 | 1.025·10⁻⁴¹ | 180, 80 | 19 % |
| 1.25 | 1.49·10⁻⁴⁷ | 150, 80 | — |
| 1.3 | 4.03·10⁻⁵⁴ | 180, 80 | 14 % |
| 1.35 | 2.61·10⁻⁶¹ | 150, 80 | — |
| 1.4 | ≤ 1.83·10⁻⁶⁹ | 180, 80 | not converged; one-sided (true value smaller); 40 digits gave −5·10⁻⁶⁰ below floor |
| 1.5 | ≤ 5.1·10⁻⁸³, positive | — | unconverged; unresolved at dps 30 (ROUND_015_C, ROUND_016_A) |

- Odd sector 10²–3·10³ times higher than the even bottom; near-null cluster (< 10⁻⁶) 7, 14, 20–25 at T = 1.0, 1.2, 1.4;
  cluster m_{10⁻³} ≈ 0.15e^{4T}, capture dimension ≈ 2.3 × cluster (ROUND_005_E).
- Decay law: −ln λ_A ≈ c₁e^{2T} + c₂T + c₃, rate 2, c₁ = 12.99 → 12.71 → 12.59 as the fit range grows, approaching
  4π = 12.566 from above; single-exponential fits fail out of sample (ROUND_007_D). Θ_T = max_c λ_A(T; cΛ) is attained at
  c* = 1 to 10⁻³⁰ for T ≥ 1.2 (TOOL_001 §4).
- κ₈ law: λ_A ≈ κ₈(1 − χ_8(2πN)), κ₈ ≈ 0.7–3.5, minimiser in a three-dimensional prolate block to 10⁻⁴; λ_W follows
  index 4 (ROUND_008_E; REVIEW_006); λ_j^ev ≈ κ_j(1 − χ_{4j+8}) (ROUND_009_B).
- Packet margins (all-profile band, η = ⅛): min μ = 0.888 (T = 1) … 0.256614 (T = 2.5, full range [1.1, 3]·2πN),
  0.114017 (T = 3, full range, polished), 0.134339 (T = 3.25, partial range [1.1, 1.6]·2πN); direct W_T on the extremal
  packet at T = 3 equals 0.11402 with D + X − R = −2·10⁻⁶ (packet identity exact to 10⁻⁶); extremal envelopes even,
  91–98 % on one half-sine mode. cΛ budget crosses zero at c* ≈ 1.07 (T = 2), ≤ 1.022 (T = 3). Margins positive on every
  covered range; minima stay in [1.1, 1.6]·2πN (ROUND_011_C, ROUND_016_A, ROUND_017_B).
- T = 1.5 operator anomaly, resolved: the unrestricted all-profile operator has λ_max(A_τ) > m(τ) (−0.511 at Nb = 1000,
  all T ∈ [1.40, 1.60], −1.71 at T = 2; the T ≥ 2 positives of ROUND_013_B were truncation), but its maximiser oscillates
  at frequency τ and is not a packet; the direct W_T on the projected test function is +0.79 (T = 1.5), +1.05 (T = 2), and
  the band-restricted margins are positive (+0.46–0.72). The failure is a property of the unrestricted operator, not of
  a_T (ROUND_015_C, ROUND_016_A).
- Three-cell form: true weight c₂ = 1 sits 0.8–1.6 % below the positivity threshold c₂* ≈ 1.016 (T = 0.8), 1.008
  (T = 1.0); at R = 4 the form is negative for c = 0.9 and for c = 1.1 in every band class up to θ = 0.9: the first two-sided
  falsifier failure recorded (ROUND_019_A §5).
- Survivor ledger: ρ = 8.23·10⁻¹² / 2.17·10⁻²³, 𝒜_∞ : 𝒞 : 𝒯 ≈ 3.4 : 0.77 : 0; arch and comb shares of bᵀC⁻¹b cancel
  from ±10¹⁶ (T = 0.8), ±10³⁸ (T = 1) (ROUND_017_A, ROUND_018_B).
- Schur coupling on E_T: sign resolved at Neumann degree K* ≈ 25–30 (T = 1.0), 105–125 (T = 1.2) (ROUND_008_D).
- High block: α_HI ≈ 3·4N/K, no K-uniform constant; gauge-quotient bottom drifts with K; drift = first chirp B₁₁
  (archimedean, comb weight 0) (ROUND_011_B, ROUND_015_A, ROUND_016_B).

---------------------------------------------------------------------------------------------------------------------
## 5. Map of the obstacle

Every route of rounds 5–20 ends in one of two places.

(a) A comb-generic statement. Coercivity pieces that survive one of the falsifiers (cΛ for c on one side of 1, a_P,
finite changes of v_n, Beurling systems): the first-cell and three-cell certificates (Q3, Q4: fixed-R statements survive
every change beyond the R-th cell), the selection rule (Q5), the packet margins (survive c < 1, fail c ≈ 1.02–1.07),
the ledger 𝔴_N ≥ 2T (ROUND_015_B), the rung inequalities (N18), the Λ-free sections (R14(B)). By rule 4 none of them is
a sign step; each is a piece that a proof would have to combine with a Λ-specific input. The falsifiers (a)–(d) remain
open against each such piece only in the sense that none of them distinguishes Λ.

(b) A restatement whose Λ-specific content is exactly the radical identity (R10). The tail reduction (R12), the comb-null
formulation (R13), the gauge-fixed representative (N20), the Schur functional of the survivor (R16) and the tail form
(R11) are all (★) rewritten through R10; the multiplier is pinned at c = 1 by the two-signed gauge radicals (Q17, Q18),
so no inequality with a comb margin can hold on the full class (N19). The only input that separates Λ from cΛ, a_P and
Beurling systems is R10 (Poisson summation, Λ ∗ 1 = log), and every route so far uses it as an identity, never as an
inequality.

Remaining open targets, in order:
1. (B_δ, s) on a Λ-free section with uniform δ (ROUND_020_A): fit δ(w) of the tail-L² section at w = 0.025, 0.018
   (R = 2, 3, T = 0.8); if δ(w) → 0, record the closure of the gauge-fixed tail-form line; if it stabilises, formulate (B)
   on the limit section with a weighted (H¹-type) tail norm. OPEN.
2. R-uniformity of the R-cell complete form with the quantitative band family (ratio β/ℓ_g of band defect to gauge
   leakage, ROUND_019_A §3–4): the sign, if this route carries one, lives only in R-uniformity, and the four-cell two-sided
   falsifier failure (c = 0.9 and 1.1) is the first place where the form is Λ-selective. OPEN.
3. Uniform-in-T proof of the band-restricted packet bound (HB_η) with a sharp cross-term lemma; full-range scan at
   T ≥ 3.25 (only [1.1, 1.6]·2πN covered at 3.25; ROUND_017_B). OPEN; comb-generic for c < 1, so a piece only.
4. Gauge-fixed (ii_s): (ii) with a fixed gauge, after N19 (ROUND_019_B). OPEN.
5. (H₋) for the Neumann expansion and (EB_C) edge budget ≤ 8πe^{2T}hλ_A (ROUND_008_C/D). OPEN.
6. prob:ext-L lower half (intermediate prolate range 10 ≲ k ≲ 4N) and (HR) in full ℓ_g normalisation (ROUND_008_E,
   ROUND_016_B). OPEN.

Results of ROUND_017_B and ROUND_019_A, present in the folder, are included above (R5, Q15, Q16, N17, packet margins to
T = 3.25, three- and four-cell falsifier thresholds).

---------------------------------------------------------------------------------------------------------------------
## 6. Corrections to Paper 47 (to be applied only when the paper is closed)

Items 1–7 of STATE_001 §4 stand. Added in rounds 5–20:
8. Open-problem sentence (main.tex L.10771–10772, "beyond ½log5 no lower bound better than the trivial … is known"):
   reconcile with L.3589 (λ_W ≤ λ_A next to the cited certificate); the cited complete-form certificate gives λ_A
   floors up to ½log15 (CITED; analytic lemmas of the source not audited) (REVIEW_005).
9. cor:margin1 (λ_A ≤ 4·10⁹ T e^{−15.449T}): add the doubly-exponential bound λ_A ≤ 3.2·10²³ N^{33/2}e^{−2πN} (Q2), given
   thm:ext-half, as an improvement in rate (REVIEW_007); cor:margin1 has no content for T ≤ 1.4 (TOOL_001).
10. lem:mbounds(i), (iii): cite these from P47 rather than re-deriving them in the packet memos; for signed profiles ρ
   the lower bound on Σ^ρ_T must use Σ^{|ρ|} (REVIEW_009).
11. Remark after prob:ext-L: (HR)(a) is prob:ext-L restricted to the high block; the reduction to a pointwise packet
   bound is necessary only (REVIEW_009 Prop 1.2 downgrade). Under the half-line identity, (ii) with κ = 0 on admissible
   tails is (★) itself (ROUND_019_B; unreviewed); state that prob:ext-L is the strictly stronger margin version.
12. thm:ext-half / §ext-constraints: record that for every c ≠ 1 the form 𝒲̂^c is unbounded below on every gauge fibre
   (Q17, unreviewed), which upgrades item 4 of STATE_001 §4 from ARGUED to PROVED once reviewed.
13. σ_T sign (P47 prop:sharp bookkeeping): σ_T < 0 only for T > 0.0520 (REVIEW_004).

---------------------------------------------------------------------------------------------------------------------
## 7. Verdict

The state of (★) is unchanged: PROVED for T ≤ ½log5, CITED for T ≤ ½log15, OPEN beyond. Rounds 5–20 produced exact
reformulations, coercivity pieces, certified falsifiers and an explicit upper bound, and located the Λ-specific content
of every route in the radical identity R10. No sign step has been obtained. Rounds 14–20 await review.
