# Annex: phase 170, files R170_823 to R170_840

Record of the complete reading of the eighteen files R170_823–R170_840 of
`03-research/phase-170-global-prime-inequality/`. No construction is proposed. For each
memo: object, claims (declared label / what the text sustains), stopping point,
later memo that corrects or audits it, and cross-check with the non-excluded terrain T1–T4 of round 1.

Common notation of the stretch. N = ⌈e^{2T}⌉, M ≥ N. S_N = Σ_{n≤N} n^{-1/2} τ_{log n},
K_N = Σ_{n≤N} (log n) n^{-1/2} τ_{log n}, L_M = Σ_{d≤M} Λ(d) d^{-1/2} τ_{log d},
A_M = m(D) − (L_M + L_M^*), E_N = S_N 𝓕 − J S_N (Poisson defect), H_{M,N} = L_M S_N − K_N =
Σ_{k>N} h_{M,N}(k) k^{-1/2} τ_{log k} with h_{M,N}(k) = Σ_{dm=k, d≤M, m≤N} Λ(d). "PC" is the finite
Poisson–Chebyshev identity S_N A_M 𝓕 = {X,E_N} − L_M^* E_N − J H_{M,N} − H_{M,N} 𝓕.
Z = ker H_T is the radical of a hypothetical first contact; R_L the L Gamma moments
(a_m = 2m+½); D_{N,L} the Gamma–Euler contraction; D_Δ = R_L^*(I − D_{N,L}) R_L ⪰ (1−q_0) R_L^*R_L,
q_0 = log2/4 + 1/16.

The whole stretch works in the frame "first contact ⟹ finite radical ⟹ prove R_L F = 0", not on
an identity (G) a_T = ‖V_T F‖² + ρ_T of the type phase 212 looks for.

---

## R170_823 — Multiscale average of Poisson–Chebyshev

**Object.** Fixed weight w ∈ C_c^k((ρ_0,1)), ∫w = 1 (or profile w_h(ρ) = h^{-1}W((1−ρ)/h)), weak
average ⟨B⟩_w = ∫ w(ρ) B_ρ dρ of the PC conjugated by the dilation D_ρ:
S_ρ A_ρ U_ρ = {ρX, E_ρ} − L_ρ^* E_ρ − J H_ρ − H_ρ U_ρ, U_ρ = D_ρ^* 𝓕 D_ρ (5); its average (APC).
H_ρ = Σ_{N<j≤MN} h_{M,N}(j) j^{-1/2} τ_{log j/ρ} keeps the exact coefficients (6).
Operator T_{a,w} = ∫ w(ρ) τ_{a/ρ} dρ with multiplier q_{a,w}(ξ) = ∫ η(s) e^{-iaξs} ds,
η(s) = w(1/s)s^{-2} (9)–(10). Exact interface (24) between ∫w(Φ_ρ + 𝓔_ρ^int) and four lines: PC
ordered via χ^{(ρ)}, commutator [A_ρ,S_ρ], defect A_1 − A_ρ = m(D) − m(D/ρ) − (L_1+L_1^*) +
(L_ρ+L_ρ^*), and alignment error with the interior energy 𝓔_ρ^int = (1−ρ)^{-1} a_M(δ_ρ,δ_ρ) ≥ 0.

**Claims.**
- (11)–(12) T_{a,w}: L² → H^k bounded, a ≠ 0. Declared a proved fact; sustained (integration
  by parts in the multiplier, without boundary terms).
- (13)–(17) P_T T_{a,w} P_T Hilbert–Schmidt, with ‖κ‖₂² = |a|^{-1}∫ρ²|w|²; HS bound (17) for
  P_T⟨H_ρ⟩_w P_T. Sustained.
- (19) ‖T_{a,w} − τ_a‖ ≥ 1: subtracting against scale one is not small. Sustained (Riemann–Lebesgue).
- (24) exact interface; sustained as an identity (assumes the same pair of primitive correctors over
  the whole interval of scales).
- No compactness of the coupled collar ⟨H_ρ U_ρ⟩_w is proved, nor any sign. Declared OPEN.

**Stopping point.** No line of (24) has a sign; compactness is proved only for the
decoupled block; the constant is not uniform in T, N, M nor as h → 0. The domain of the dilation
generator 𝒜 = −½ − t∂_t is not proved for first-contact vectors (§6).

**Correction/audit.** R170_824 (three corrections of the first version: order S_ρA_ρ vs A_ρS_ρ,
support of the kernel at u = −a/ρ, withdrawal of the bounded-kernel claim for P_T H_ρ U_ρ P_T).
R170_825 closes the compactness of the coupled collar.

**Cross-check T1–T4.** T1: yes, partially — it is an average with weight w over the dilation, but it does not
produce squares or sign; only regularity/compactness. T2: no. T3: Λ∗1 = log only in the absence
of coefficients j ≤ N of H_ρ. T4: touches the tail Σ_{k>N} h(k) k^{-1/2} τ, but as an averaged
(compact) operator, not as a sum Σ h(k)|ℓ_k(F)|² with h ≥ 0.

## R170_824 — Audit of the multiscale piece

**Object.** Audit of R170_823.

**Claims.** Accepts: derivative gain of T_{a,w}, HS after compression, exact preservation
of h_{M,N}(k); ‖T_{a,w} − τ_a‖ ≥ 1; interface (24) with four blocks. Does not accept compactness or sign
for ∫w H_ρ U_ρ. Records and corrects three errors of the first version (double order, orientation of the
kernel, bounded kernel withdrawn). Labels consistent with the text.

**Stopping point.** No block of (24) has a sign; converting compactness into sign would require another
arithmetic input.

**Cross-check.** Same as R170_823; none of T1–T4 advances.

## R170_825 — Phase of the coupled averaged collar

**Object.** C_{a,w} = ∫ w(ρ) τ_{a/ρ} U_ρ dρ = q_{a,w}(D) J with
q_{a,w}(ξ) = ∫ η(s) e^{i[θ(sξ) − asξ]} ds, θ' = m (5)–(6). Phase derivative ξ[m(sξ) − a].

**Claims.**
- m even, strictly increasing on [0,∞) (Bernstein series of P47), m(0) = −5.372…; stationary
  point confined to ρ_0 r_a ≤ |ξ| ≤ r_a, r_a = m^{-1}(a) (9). Sustained.
- For the opposite orientation (m + a), roots only if 0 < a ≤ −m(0), i.e. k ≤ 215 for a = log k
  (10). Sustained.
- |q| ≤ A_w/|ξ| for |ξ| ≥ B_a = 2πe^{a+2}, A_w = ‖η'‖₁ + C_m‖η/s‖₁ (13)–(14); C_{a,w}: L² → H¹ (17);
  ‖P_T C_{a,w} P_T‖²_HS ≤ (T/π)(2B_a‖w‖₁² + 2A_w²/B_a) (18); bound (20) for the finite arithmetic
  block. Sustained (only one derivative; no more is claimed).
- Non-uniform bound: B_{log k} = 2πe²k gives growth k^{1/2}, which compensates k^{-1/2}.

**Stopping point.** HS ≠ sign; not uniform in cutoffs; does not control the other lines of (24).

**Correction/audit.** R170_826 accepts it.

**Cross-check.** T1: still a dilation average without a square. T4: the block Σ_{N<k≤MN}
h(k) k^{-1/2} C_{log k,w} is the T4 tail in operator form, without diagonal form |ℓ_k(F)|² or sign.
T2, T3: no.

## R170_826 — Audit of the coupled multiscale collar

**Object.** Audit of R170_825.

**Claims.** Accepts phase, sign of the derivative, location of the stationary point, bound
A_w/|ξ|, L² → H¹, local HS. Points out: constant growing with a = log k, not uniform; HS means
compactness, not sign; a self-adjoint compact operator has eigenvalues of both signs.

**Stopping point.** Asks to exploit the matrix on the radical together with Tate, Gamma and alignment (done in
R170_827).

**Cross-check.** None of T1–T4 advances.

## R170_827 — Multiscale matrix on the radical

**Object.** Basis F_1…F_d of Z (without separating parities), faithful Gram B_ij = ⟨R_L F_j, R_L F_i⟩ ≻ 0.
Form q_ms(F) = ∫ w(Φ_ρ + 𝓔_ρ^int); matrices K = P + E with E_ij = ∫ w/(1−ρ) a_M(δ_ρF_j, δ_ρF_i) ⪰ 0,
and Q = K (joint hermitization of the four lines, (10)–(11a)). Self-adjoint collar:
q_{a,w}(−ξ) = conj q_{a,w}(ξ) ⟹ C_{a,w} = C_{a,w}^* (18). Singular values
s_{r+1} ≤ ‖𝒞‖_HS/√(r+1) (21a). Spectral criterion: q_ms ≤ 0 on Z ⟺ λ_max(B^{-1/2}KB^{-1/2}) ≤ 0 (25).
Matrix closure map: P − (1−q_0)B ⪰ 0 and P + E ⪯ 0 together give a contradiction (28a)–(28b).

**Claims.** B ≻ 0, correct hermitization, self-adjointness of the collar, (21a), (25): sustained
(finite algebra and min–max). The two inequalities (28a): OPEN, declared not proved. Warns that
(27) (Gamma–Euler reserve) cannot be added to (8) without a joint identity.

**Stopping point.** Both inequalities of (28a) are missing; moreover the reduction does not use the dynamic
minimality of the first contact (it holds for any null mode of H_T ≥ 0).

**Correction/audit.** R170_828 (corrects double counting in the first version: the four-line residue
plus the interior energy again; what remains is Q = K = P + E).

**Cross-check.** T1–T4: no. It is a finite Rayleigh criterion on the radical, without a sign mechanism.

## R170_828 — Audit of the radical matrix

**Object.** Audit of R170_827.

**Claims.** Validates six points (B ≻ 0, hermitization, non-invariance of parity, self-adjointness,
singular value bound, normalization). Records the corrected double counting. Reaffirms that
D_Δ ⪰ (1−q_0)B does not prove that P dominates it; inserting it without a joint identity would be circular.

**Stopping point.** Not uniform in T; does not use minimality.

**Cross-check.** None of T1–T4.

## R170_829 — Gamma–Euler matrix bridge toward the multiscale flux

**Object.** Exterior flux as transport defect p(F) = Re e_F^{(1)}(z̄_F − g_F), with
z̄_F = ∫w S_ρU_ρ S_L F, g_F = S_L F, using e_F^{(1)}(g_F) = 0 (5). Reserve d(F) = ⟨R_LF,(I−D)R_LF⟩.
Functional Λz(F) = ⟨F, A_1 z⟩ − ⟨r_F, z⟩; lifting equation Herm[Λ Y_L] = D_Δ (12).
Exterior candidate ι_+c = 1_{(T,∞)} Σ b_m c_m e^{-a_m t}, Y_+ = ι_+(I−D)R_L (14). Exact residue
R_GE = P − D_Δ = Q − E − D_Δ = Q − E − B − ½Q^{(1)} (18), (25), (26).

**Claims.**
- Interior obstruction: if Yz is supported in the window, Λz = 0 by the weak equation (13); no
  interior synthesis (R_L^*CR_L, G_L, JG_LJ, S_L, adjoint of the collar) solves (11). Sustained.
- R_GE ⪰ 0 sufficient (not necessary) for P − (1−q_0)B ⪰ 0. Sustained; (32) is exactly equivalent to
  the sought bound (declared: not to assume it).
- The collar identity R_LB_N = D_{N,L}R_L − 𝓔_{N,L} does not transport R_L S_ρ U_ρ S_L F (§5).
- Sign of R_GE: OPEN.

**Stopping point.** No identity reduces R_GE to a positive form; minimality contributes no inequality
for the exterior test; Λι_+ is not computed.

**Correction/audit.** R170_830; R170_831 computes Λι_+ and detects the typing defect of the Tate
port.

**Cross-check.** T1–T4: no. (Mentions another statement at the end only as a disclaimer; uses an external
equivalence only in that disclaimer, without development.)

## R170_830 — Audit of the exterior Gamma–Euler bridge

**Object.** Audit of R170_829.

**Claims.** D_Δ = B + ½Q^{(1)} verified; D_Δ ≻ 0 on Z. Equation Herm(ΛY_L) = D_Δ
verified; exclusion of all interior candidates exact. Y_+ is in the logarithmic domain
despite the jump, but R_LB_N = D_NR_L − 𝓔 does not compute Λι_+ (m(D), jump and Tate are missing). Structural
contribution: the lifting must cross the boundary.

**Stopping point.** Asks for an exterior Green formula for the exponential tails.

**Cross-check.** None of T1–T4.

## R170_831 — Exterior Gamma–Euler formula and Tate typing defect

**Object.** Lemma 2.1: for z_a^+ = 1_{(T,∞)} e^{-as}, on I_T,
(A_1 z_a^+)(t) = −½ ∫_{T−t}^∞ K(u) e^{-a(t+u)} du − e^{-at} Σ_{d≤M, t>T−log d} Λ(d) d^{-a−1/2} (2.2),
with K(u) = 2Σ_j e^{-(2j+1/2)u}. Jump: m(D)z_a^+ ~ −(e^{-aT}/2) log(1/(T−t)) (3.1), not a delta.
Reflection g^-(t) = g^+(−t), with L_M^* instead of L_M (4.1). Lemma 5.1: r_F = α e^{-t/2} + β e^{t/2} on I_T
does not determine ⟨r_F, z⟩ for exterior z. Matrix equation after choosing port Θ_±:
Herm[(Γ_{+,M} − Θ_+)(I−D)R_L] = R_L^*(I−D)R_L (6.3).

**Claims (own ledger).** Domain of tails: PROVED (sustained). Right/left response:
PROVED (sustained; specialization of the kernel of R162_404 §4, declared not new). Logarithmic jump:
PROVED (sustained). Identification with truncated collars: PROVED. "Exterior Tate port determined
by the weak equation": FALSE (sustained by Lemma 5.1). Canonical choice Θ_±: OPEN. Equation (0.2):
OPEN.

**Stopping point.** Typing defect: the Tate term is not defined on exterior tails; choosing
Θ = 0 would impose a transmission law (pointed out as open in P122_029).

**Correction/audit.** R170_833 (validates); R170_834 refines.

**Cross-check.** T1–T4: no. Uses Λ(d) only linearly in the prime collar.

## R170_832 — Puzzle map v2

**Object.** Map of pieces R170_819–831 with cross-check against phases 121, 122, 124, 155, 162. Splits the
gap into G1 (canonical exterior Tate port), G2 (oriented lifting), G3 (arithmetic sign law
with Λ∗1 = log essential), G4 (minimality and uniformity). Table "what not to rebuild":
P121 (Tate localization), P122_028–029 (Green complex, transmission), P124_009 (leakage; finite
counterexample to Cauchy–Schwarz), P124_011 (Schur), R162_404, R162_301 (indefinite Euler/Hankel lifting),
R162_503 (sum–product), small exponential tails.

**Claims.** Inventory; no new theorems. §7 (later addition) corrects G1: the Hardy port
of the source is already canonical (R161_009, R161_015); what is missing is a source–port map, not another gauge;
what is gauge-independent lives only in Z_0 = {r_F = 0}.

**Stopping point.** G1–G4 open.

**Cross-check.** Does not touch T1–T4.

## R170_833 — Audit of the exterior formula

**Object.** Audit of R170_831.

**Claims.** Verifies domain, kernel, logarithmic jump, prime/reflection orientation. Declares that
the kernel formula is already in R162_404 §4 (not to present it as new). What is useful: the type check
(extension by zero vs by global characters give different ports). Θ_± parametrizes, does not construct.

**Stopping point.** Asks to derive Θ_± from a global identity or boundary quotient; requirements: hermitize to
D_Δ, use minimality, use Λ∗1 = log in the sign line, not transport to falsifiers.

**Cross-check.** None of T1–T4.

## R170_834 — Canonical Tate port: Hardy range, exterior ambiguity and exact quotient

**Object.** Two natural extensions: by global characters Θ^char (2.3)–(2.4) and Hardy boundary
form Θ^H(c)(F) = p_±(F) conj ℓ_±(z_c^±), with ℓ_+(z) = ∫_T^∞ z e^{-t/2} (2.5)–(2.7). Lines
κ_m^- = b_m e^{-(a_m+½)T}/(a_m+½), κ_m^+ = b_m e^{-(a_m−½)T}/(a_m−½), quotient κ^+/κ^- =
e^T (a_m+½)/(a_m−½) depending on m (2.9). Perturbation E_λ = E_0 + λH, H supported outside I_T,
compatible with reflection (3.1)–(3.4). Intrinsic quotient Z^*/Ran 𝒜^*, realization Z_0 = ker 𝒜 (4.2)–
(4.4). Residues ℛ_H = M_H − D_Δ (5.4), ℛ_char − ℛ_H of rank ≤ 4 (5.7), ℛ_0 = P_0(Herm[Γ_+C_+ +
Γ_−C_−] − D_Δ)P_0 (5.8).

**Claims (ledger).** Hardy port of the source: PROVED/CANONICAL (cited from R161). Θ^char ≠ Θ^H
for L ≥ 2: sustained. Uniqueness of Θ_± on Ran ι_±: FALSE (sustained). Two-sided cancellation of the
ambiguity: FALSE (sustained, (3.4) doubles it). Quotient by Ran 𝒜^*: PROVED. M_H and ℛ_H: COMPUTED
EXACTLY (as explicit definition; no numerical value). ℛ_H = 0 or signed: OPEN; ℛ_0 = 0: OPEN.
Equivalence with the inverse scattering of R161_018: NOT PROVED / formally false.

**Stopping point.** Without a quadratic source–port map, choosing between (2.3) and (2.7) imposes the
transmission law one wants to prove. The quotient Z_0 loses precisely the Tate directions.

**Correction/audit.** R170_836 (validates).

**Cross-check.** T1–T4: no.

## R170_835 — Quadratic source–innovation–port map and exact residue

**Object.** In a parity sector Z_ε: innovations 𝒥_+ = (I−D)^{1/2}R_L, 𝒥_- = (I−D)^{1/2}R_LJ,
½(𝒥_+^*𝒥_+ + 𝒥_-^*𝒥_-) = D_Δ (0.3). Finite PC carrier with centred innovations
𝓘_{M,N}F = (Δ^R_{N,T}ℓ_F, Δ^L_{N,T}ℓ_F) and Tate scalars a_∓(ℓ_F) (2.6)–(2.9). Weight-substitution
defect: δ_a(k) = Σ_{d|k} a(d) − log k; block (2.11) −J Σ_{k≤N} δ_a(k)k^{-1/2}τ_{log k} − (…)𝓕, zero
for a = Λ. Column map 𝒦_± = ι_±(I−D)^{1/2}; slope Gram with W_+ = 2(X−T):
G^col_mn = 2 b_m b_n e^{-(a_m+a_n)T}/(a_m+a_n)² (Cauchy square) (3.7). Residue ℛ_col = 𝒮_col − D_Δ =
Σ_σ 𝒥_σ^*[(I−D)^{1/2}G^col(I−D)^{1/2} − ½I]𝒥_σ (3.9). Canonical slope form
𝒮_can = 𝒢_+^*W_+𝒢_+ + 𝒢_-^*W_-𝒢_- ⪰ 0 (4.3). Decomposition 𝒮_can − D_Δ = ℛ_range + ℛ_col (5.1).
Specification of a mixed form 𝔅^ε_{M,N,L} (6.3) with two readings of common residue.

**Claims.**
- (0.3), (3.4), (3.7), (3.9), (3.12), (5.1): PROVED/EXPLICIT; sustained (algebra and an elementary
  integral).
- Proposition 4.1 (PROVED): there is no universal factorization 𝐆_+^prod(F) = 𝒦 R_L F with finite L
  on a carrier preserving the critical jet. The proof evaluates the product germ at a zero of an
  external function and uses independence of exponentials; that is, it uses a reduction to zeros (recorded
  neutrally, without development). What the text sustains: the independence-of-exponentials argument
  is correct under the premise that such an evaluation is a functional of the carrier.
- Factorization restricted to the radical (4.9): exists a posteriori via (𝒥_+|_{Z_ε})^{-1}; not uniform.
- (5.3) ⟨F,(𝒮_can + D_Δ)F⟩ = 0 would force F = 0: trivially sustained (sum of two forms ⪰ 0, one
  ≻ 0). Shows that the "inverse law" is already the closure.
- §7 falsifiers: the column Gram survives arbitrary positive weights (d_m^w), Λ1_{n≥5},
  Type I, positive eigenvectors ((7.2) Q_{N,L} < 0); only (2.11) distinguishes Λ.

**Stopping point.** The identity Λ∗1 = log enters only in the PC carrier (2.11), not in the column Gram;
hence any sign of the Gram passes the weight falsifiers. The mixed form (6.3) is missing: NOT BUILT.
Minimality absent; uniformity absent.

**Correction/audit.** R170_836 (validates; (6.3) is a specification, not a construction); R170_837
proves that the common-residue condition is the closure itself.

**Cross-check.** T3: yes — records the exact entry of Σ_{d|k}Λ(d) = log k as the vanishing of δ_Λ(k), and
that this vanishing gives no sign by itself. T4: partially — works with the mixed pairings of
PC (E_N, H_{M,N}) but directs them toward Hardy ports/Gamma columns, not toward Σ_{k>N} h(k)|ℓ_k(F)|².
T2: the Cauchy Gram G^col is an explicit Gram, but of Gamma exponentials, not of divisors. T1: no.

## R170_836 — Audit of the canonical port and of the quadratic map

**Object.** Audit of R170_834–835.

**Claims.** Validates: non-uniqueness of the Tate port; reduction to Z_0 correct but incomplete; column
Gram exact; finite-rank obstruction (excludes only universal finite factorization, not an
infinite map, a source-dependent one, or an identity only on the radical); the factorization via
inverse is legitimate but depends on the object to be excluded. Real entry of the arithmetic: only δ_a(k).
Five requirements for the next piece (written from PC, preserving terms, algebraic cancellation of
δ_Λ, same residue in both readings, one-sided variation in T).

**Cross-check.** T3: confirms the role recorded in R170_835. Otherwise no.

## R170_837 — Mixed PC form: maximal construction, exact incompatibility and two-window datum

**Object.** Z_N = S_N^ren, E_N = Z_N𝓕 − JZ_N, C_N = Z_N𝓕 + JZ_N, K_N = −[X,Z_N],
𝒥_N = K_N𝓕 − JK_N = Z_N𝓜𝓕 − {X,C_N}; renormalized hyperbola H̃_{M,N} = L_M Z_N − K_N.
Mixed form 𝔐_N^ε[T_L](F,G) = Herm⟨E_NF, 𝒥_N T_L G⟩ (0.4), T_L = S_L. Polarized Green
Herm⟨e_N(F), X c_N(G)⟩ = Herm(⟨a_N,Xa_N⟩ − ⟨d_N,Xd_N⟩) (3.1); decomposition by supports
𝔖^phys − 𝔖^wrong + TΦ_N + 𝔊_{0,N} (3.6); Hardy reading (3.8)–(3.9); Euler–hyperbola reading (4.3).
Theorem 5.1. Monitor 𝔄_a (6.9). Two-window datum
ℭ^ε_{M,N;T,δ}(F,F_δ) = ⟨1_{C_δ} 𝔓^ren 𝓕 F̃, F_δ|_{C_δ}⟩ (8.3), with collar identity
λ_δ⟨F_δ, E_TF⟩ = ⟨ξ_F^δ, F_δ|_{C_δ}⟩ (7.5).

**Claims (ledger).**
- Finite E_N–C_N polarization, orientation, sesquilinear Green, four blocks: PROVED (sustained;
  declared identical to R161_056–057, not new).
- Hardy leading term for T_L = S_L: crossed, FALSE as 𝒮_can (sustained).
- Expansion (4.3): PROVED; appearance of +D_Δ in it: FALSE (sustained: slot incompatibility).
- Theorem 5.1 (PROVED): if there exist 𝔅, ℜ with 𝔅 = D_Δ + ℜ and 𝔅 = −𝒮_can + ℜ, then Z_ε = 0. Sustained
  (subtraction and positivity). Consequence: the "common residue" is the complete closure, not bookkeeping.
- (6.7) PROVED: after the recombination K_N = L_M^a S_N − H^a_{M,N}, 𝔐 is independent of the weight a
  (weight-blind). Sustained.
- Monitor 𝔄_Λ = 0 exact; contributes no sign.
- §7: interior derivative with zero linear term (R162_101); right minimality does not fit in a form on
  Z_T × Z_T (7.6): FALSE/WRONGLY TYPED.
- (8.3) declared PROVED/EXACT and "first carrier using (6.5) and (7.5) at once". What the text
  sustains: (8.3) is only a rewriting of PC-ren on the regular core; the audit R170_838 withdraws
  the claim of containing signed minimality and of novelty.

**Stopping point.** Three incompatibilities (common residue, test slot, minimality). Sign of (8.3) and
transport to R_LF: OPEN.

**Correction/audit.** R170_838 (nine corrections; see (e)).

**Cross-check.** T4: yes, closely — it is the maximal attempt to convert mixed pairings of PC (E_N with
the jet of the sum) into a form with a positive leading term; it fails because the leading term is a
cross-correlation 𝔖^phys[I,S_L] and the rest (𝔖^wrong, Φ_N, 𝔊_0) has no sign; a sum
Σ_{k>N} h(k)|ℓ_k(F)|² never appears. T3: yes — records that Λ∗1 = log only annihilates the block k ≤ N before
recombining and that after recombining the form forgets the weight (6.7). T1, T2: no.

## R170_838 — Audit of the two-window PC–collar datum

**Object.** Audit of R170_837 §§7–8. Exact expansion
ℭ = λ_δ⟨F_δ,E_TF⟩ + ℛ^Tate + ℛ^Z, ℛ^Tate = ⟨r_F, F_δ|_{C_δ}⟩, ℛ^Z = ⟨1_{C_δ}(Z_N − I)A_ME_TF, F_δ|_{C_δ}⟩
(0.3)–(0.4); expansion of ℛ^Z in translations and polar continuum (4.6); residue ℛ^tot = ℛ^{>L} + ℛ^Tate +
ℛ^Z (6.3)–(6.4), with ξ_F^δ = −ℓ_L(R_LF) + ξ_F^{>L} (R162_406 Prop. 4.1).

**Claims (corrected ledger).**
- Collar identity between T and T+δ: PROVED; sign for every F of the radical: FALSE; sign only for the
  normalized limit G with fixed phase: PROVED.
- 𝒫^pol_{M,N} = 0 on the common core (PC for C^pol minus PC for C^pol): PROVED; it is not a new block.
- 1_{C_δ}A_ME_TF = r_F + ξ_F^δ in 𝒬'_log if M ≥ e^{2T'}: PROVED; passing Z_N through the restriction: FALSE.
- (8.3) = signed minimality pairing: FALSE. Stabilization in M: FALSE. Dependence on N:
  explicit.
- δ_Λ(k) = 0 requires M ≥ N (R170_837 only imposed M ≥ e^{2T'}); clean scale N ≥ e^{2T'}, M ≥ N.
- δ_Λ = 0 and λ_δ < 0 in the same scalar: FALSE.
- Novelty of (8.3): NO / repackaging of R162_405–406; transport of the sign to R_LF with these data:
  NO-GO (by R162_406–408).
- Extension of (8.3) to the real first-contact domain: NOT PROVED (requires Z_N^* preserving
  𝒬_log).

**Stopping point.** The total residue (6.4) has neither sign nor vanishing; even without residues, (6.2) is a
single scalar inequality against an unknown profile and does not force R_LF = 0.

**Cross-check.** T3: yes (the vanishing δ_Λ lives in the coefficients of the raw hyperbola, minimality in
another pairing; they do not meet in one scalar). T1, T2, T4: no.

## R170_839 — Puzzle map v3

**Object.** Updated inventory: A (13 proved pieces), B (12 refuted or exhausted connections), C
(8 missing pieces: bilateral collar law, domination of the tail, comb–Gamma conversion, control
of the profile of the larger window, non-perturbative use of minimality, separation of falsifiers,
uniformity in T, final vanishing), D (admissible piece: bilateral collar law with ℓ_L(R_LF) and
ξ_F^{>L} on different sides or scales, using the exact comb of ℤ).

**Claims.** Inventory; pieces A.1–A.13 cite their memos. B.4 repeats the obstruction of
R170_835 that relies on evaluation at zeros (uses an external reduction; recorded neutrally).

**Cross-check.** C.3 ("comb–Gamma conversion: identity converting the exact geometry of the integer
divisors into coefficients of the Gamma moments") is close to T2/T3 as a question, without construction.

## R170_840 — Bilateral collar law: normal form, no-go and minimal virial datum

**Object.** Explicit scales δ_gap(T) = ½ min{log(n_1/e^{2T}), log 2}, δ_j = 2^{-j}δ_gap,
N_j = M_j = ⌈e^{2T_j}⌉ (1.3)–(1.4); minimal L_T with R_L injective (1.5). Collar decomposition
ξ_{F,+}^δ = −γ_F − Π^δ_{Λ,T}F − r_F, γ_F = Σ_{m≥1} e^{-a_m t} μ_F(a_m),
Π^δ_{Λ,T}F(t) = Σ_{2≤d<e^{2T}} Λ(d)d^{-1/2} F(t − log d) + θ_T ε Λ(n_0) n_0^{-1/2} F(2T − t) (2.1)–(2.3);
tail without Tate ξ̂^{>L} (2.5); direct normal form λ_δ a_δ = −⟨ℓ_L^ε(R_LF), f⟩ + ⟨ξ̂^{>L}, f⟩ − ⟨r_F, f⟩
(0.3)/(2.8); PC normal form (0.1)/(4.5) with cancellation of the local Tate and nonlocal residue ℛ^Z (4.7).
Virial functional 𝒱_{Λ,T}(F) = (2π)^{-1}∫ τ m'(τ)|F̂|² − Σ_{n<e^{2T}} 2Λ(n)n^{-1/2} log n · c_F'(log n) +
2Re⟨F, t r_F'⟩ (8.1), with λ_A(T+δ) = −(δ/T)𝒱(G) + o(δ) (8.2) under (REG). Open datum VIR–EP (8.3).

**Claims (ledger).**
- Choices of scales: PROVED/EXPLICIT. L_T finite: PROVED / not uniform.
- Decomposition (2.6) and normal form (0.3): PROVED (exact reorganization of R162_406).
- Equality of the two local orientations by parity (3.2)–(3.3): PROVED; second independent inequality
  by antisymmetry: FALSE. Sustained.
- PC normal form (4.5), cancellation of the local Tate: PROVED (bookkeeping, without sign). Stabilization of
  ℛ^Z: FALSE.
- δ_Λ = 0 localized before recombining: PROVED; sign produced by that cancellation: FALSE; arithmetic
  scalar after recombining: FALSE.
- Tail universally o-small relative to the observed part (6.1): FALSE (by R162_408 Prop. 5.1;
  independence of jets and moments). Feshbach orients the sum, not the components (6.4)–(6.6).
- Theorem 6.1 (NO-GO, PROVED): every two-window scalar identity whose only argument from the
  larger window is F_δ, obtained by linear compositions of finite PC, compressed Chebyshev,
  reflection, restriction to collars, pairing with F_δ, weak equation and minimality identity,
  reduces to the normal form + invertible changes of basis + null monitor 𝒟_Λ^{≤N} = 0; none gives
  strict domination of tail/Tate/ℛ^Z by R_LF. What the text sustains: the proof is a case-by-case closure
  argument over the listed operations (the phrase "every identity" is sustained
  for that list; the step "§§6.1–6.4 prove that no sign follows" relies on the cited R162_406–408). It is
  a NO-GO of declared class, pointwise in T.
- Falsifiers: passes F1 (positive eigenvectors, (7.2)), positive weights, Davenport–Heilbronn.
- Proposition 8.1 (PROVED): VIR–EP ⟹ R_LG = 0. Sustained (0 ≤ 𝒱(G) ≤ 0 and lower bound by the
  reserve). VIR–LB (𝒱|_N ⪯ 0) and VIR–DET (𝒱(G) ≥ c_T D_Δ(G)): OPEN. (REG) and threshold trace: OPEN.

**Stopping point.** No-go for the current carrier; the minimal datum VIR–EP has exactly the strength of the
closure and must be proved with a coefficient operation on the finite hyperbola before recombining
into K_N.

**Cross-check.** T3: yes — records precisely that the divisor identity only annihilates one block and that,
after recombining, the form "forgets the arithmetic reason"; VIR–LB requires its use before recombination,
open. T4: partially — the "tail part k > N" appears in condition 3 of VIR–EP ("retain the
boundary contribution k > N"), without the form Σ h(k)|ℓ_k|². T1: the term (2π)^{-1}∫τ m'(τ)|F̂|² is the
dilation derivative of the multiplier (dilation weight), but without an arithmetic square. T2: no.

---

## (a) Reusable PROVED pieces

1. T_{a,w} = ∫w τ_{a/ρ}: L² → H^k; P_T T_{a,w} P_T HS with ‖κ‖₂² = |a|^{-1}∫ρ²|w|² — R170_823 §3 (11)–(17).
2. ‖T_{a,w} − τ_a‖ ≥ 1 — R170_823 §4 (19).
3. Exact multiscale interface with interior energy ⪰ 0 — R170_823 §5 (24) (audited in R170_824).
4. Coupled collar C_{a,w} = q_{a,w}(D)J; stationary region ρ_0 r_a ≤ |ξ| ≤ r_a; |q| ≤ A_w/|ξ| outside
   the band; L² → H¹; HS with explicit bound (18); for the orientation m + a, roots only if
   log k ≤ −m(0) (k ≤ 215) — R170_825 §§2–5.
5. Self-adjointness of the averaged collar with real weight; singular value bound
   s_{r+1} ≤ ‖·‖_HS/√(r+1) — R170_827 §4 (18), (21a).
6. Faithful Gram B ≻ 0 and finite spectral criterion λ_max(B^{-1/2}KB^{-1/2}) ≤ 0 — R170_827 §§1, 5.
7. Exclusion of every interior lifting of D_Δ (ΛY = 0 for tests in the window) — R170_829 §2 (13).
8. Identities R_GE = P − D_Δ = Q − E − B − ½Q^{(1)} — R170_829 (18), (25), (26).
9. Exterior response of A_1 on cut exponential tails, logarithmic jump, reflection —
   R170_831 Lemma 2.1, §§3–4 (specialization of R162_404 §4).
10. Non-determination of the exterior Tate port by the weak equation — R170_831 Lemma 5.1.
11. Θ^char ≠ Θ^H (quotient κ^+/κ^- depending on m); no two-sided cancellation; intrinsic quotient
    Z^*/Ran 𝒜^* — R170_834 §§2–4.
12. Cauchy column Gram G^col_mn = 2b_mb_n e^{-(a_m+a_n)T}/(a_m+a_n)² and residues ℛ_col, (5.1) —
    R170_835 §3, §5.
13. Weight-substitution defect δ_a(k) and block (2.11), zero exactly for Λ — R170_835 §2.2;
    R170_837 §6 (6.2)–(6.5).
14. Theorem 5.1 (common residue ⟹ Z_ε = 0) — R170_837 §5.
15. Weight-blindness after recombining K_N = L_M^aS_N − H^a_{M,N} (6.7) — R170_837 §6.
16. 𝒫^pol_{M,N} = 0 on the common core — R170_838 §2 (2.4).
17. Expansion ℭ = λ_δ⟨F_δ,E_TF⟩ + ℛ^Tate + ℛ^Z — R170_838 §4.
18. Equality of the two local orientations in a parity sector — R170_840 §3.
19. PC normal form with cancellation of the local Tate — R170_840 §4 (4.5).
20. Theorem 6.1 (class no-go) and Proposition 8.1 (VIR–EP ⟹ R_LG = 0) — R170_840 §§6.5, 8.

## (b) Closures (class and falsifier)

- Subtracting the multiscale average against scale one: norm ≥ 1, not a small remainder (R170_823 §4).
- Compactness / Hilbert–Schmidt as a source of sign: a self-adjoint compact operator has both signs; on the
  finite radical every matrix is compact (R170_826, R170_829 §6).
- Interior lifting of D_Δ (any synthesis with image in the window): impossible by the
  weak equation (R170_829 (13), R170_830).
- Choice of the exterior Tate port: not forced; two natural choices differ; two-sidedness
  doubles the ambiguity (R170_831 Lemma 5.1, R170_834 §§2–3).
- Universal factorization of the Hardy port through finite R_L: false (R170_835 Prop. 4.1; argument with
  evaluation at zeros, recorded neutrally).
- Sign deduced from the column Gram or from D_Δ: falsified by arbitrary positive weights, Λ1_{n≥5},
  Type I and positive eigenvectors (Q_{N,L} < 0) (R170_835 §7).
- Mixed form with +D_Δ, −𝒮_can and common residue as a formal consequence of PC: it is the closure itself
  (R170_837 Theorem 5.1); falsifier: models with nontrivial first contact.
- E_N–C_N polarization after recombining: weight-blind (R170_837 (6.7)).
- Right minimality inside a form on Z_T × Z_T: wrongly typed (R170_837 (7.6)).
- Two-window datum (8.3) as a signed carrier: false; repackaging of R162_405–406 (R170_838).
- Bilateral collar law with PC/Chebyshev/collar/Feshbach: class NO-GO (R170_840 Theorem 6.1);
  falsifiers F1 (positive eigenvector with descent), positive weights, Davenport–Heilbronn.

## (c) Explicitly open, with its exact obstacle

- Sign of the lines of (24) of R170_823 on F ∈ ker H_T without estimating each one in absolute value.
- The two matrix inequalities P − (1−q_0)B ⪰ 0 and P + E ⪯ 0 (R170_827 (28a)); equivalently
  R_GE ⪰ −[D_Δ − (1−q_0)B] (R170_829 (32)).
- Exterior Green formula and canonical port Θ_± derived from a global identity (R170_831, R170_833);
  Herm(ΛY) = D_Δ on all of Z; ℛ_0 = 0 on Z_0 (R170_834 (5.8)), which even if proved does not control the
  Tate directions.
- Construction of the factorization of the port on the radical from PC without inverting R_L|_Z
  (R170_835 §4.2).
- Finite mixed form 𝔅^ε_{M,N,L}: NOT BUILT; by R170_837 it is equivalent to the closure.
- Sign of (8.3) and transport to R_LF; control of the total residue ℛ^{>L} + ℛ^Tate + ℛ^Z (R170_838 (6.4)).
- Pieces C.1–C.8 of R170_839 (bilateral law, domination of the tail, comb–Gamma conversion, profile of
  F_δ, non-perturbative minimality, separation of falsifiers, uniformity, final vanishing).
- VIR–EP: (REG) and threshold trace; VIR–LB 𝒱_{Λ,T}|_{N_T^ε} ⪯ 0 proved on the hyperbola before the
  recombination using 𝒟_Λ^{≤N} = 0; VIR–DET 𝒱(G) ≥ c_T⟨R_LG,(I−D)R_LG⟩ controlling tail, Tate and ℛ^Z
  without an a posteriori inverse; quantifiers L_*, c_* computable and uniform on compacts
  (R170_840 §8). Uniformity obstacle: inf_T δ_gap(T) = 0 and there is no bound on L_T.

## (d) What in this stretch already walks T1–T4, with the recorded reason for failure

- **T1 (continuous squares with dilation weights).** R170_823–826 average over the dilation with
  weight w (including profile w_h) and obtain only smoothing and compactness; reason: the operation is linear in
  the operator and produces no square; HS gives no sign; constants not uniform in k, T, h. The
  virial term (2π)^{-1}∫τ m'(τ)|F̂|² of R170_840 (8.1) is a continuous square with a dilation
  weight, but the global sign of 𝒱 on the radical (VIR–LB) remains open. There is no attempt to put
  the arithmetic in the index of a continuous square.
- **T2 (divisor Gram [log gcd] = E diag(Λ) Eᵀ).** Does not appear. The only explicit Gram is the
  Cauchy Gram of Gamma exponentials (R170_835 (3.7)), weight-blind; reason for its failure: it survives every
  system of positive weights. R170_839 C.3 formulates a "comb–Gamma conversion" as an open question.
- **T3 (Σ_{d|n}Λ(d) = log n converted into a quadratic bound).** Walked directly in R170_835 §2.2,
  R170_837 §6, R170_838 §5, R170_840 §5: the identity exactly annihilates the block of coefficients
  k ≤ N of the hyperbola (𝒟_Λ^{≤N} = 0), but (i) a null monitor contributes no sign; (ii) on recombining
  K_N = L_M^aS_N − H^a the form becomes weight-independent again (R170_837 (6.7)); (iii) the vanishing
  lives in a scalar different from the one carrying the minimality sign (R170_838). What remains requested
  (VIR–LB) is to use it before the recombination as an inequality: open. No memo converts it into
  a quadratic bound.
- **T4 (mixed pairings of PC → Σ_{k>N} h(k)|ℓ_k(F)|², h ≥ 0).** Closest: R170_837 (mixed
  form E_N–𝒥_N, polarized Green (3.6)) and R170_823/825/827 (the tail H_{M,N} = Σ_{k>N} h(k)k^{-1/2}τ
  averaged and compact). Reason for failure: the leading term is a cross-correlation
  𝔖^phys[I,S_L], not a norm; the remainders 𝔖^wrong, TΦ_N, 𝔊_0 have no sign; the tail appears as an
  operator, never diagonalized into squares |ℓ_k(F)|²; moreover the required common residue is equivalent to the
  closure (Theorem 5.1). The exact conversion requested by T4 is not attempted in the stretch.

## (e) Inconsistencies or errors between memos

1. R170_823 first version: confused S_ρA_ρU_ρ with A_ρS_ρU_ρ, oriented the kernel wrongly (u = a/ρ instead
   of −a/ρ) and claimed a bounded kernel for P_TH_ρU_ρP_T; corrected according to R170_824.
2. R170_823 leaves the compactness of ⟨H_ρU_ρ⟩_w open; R170_825 proves it (not a contradiction, a
   later closure).
3. R170_827 first version: double counting (four-line residue + interior energy); corrected to
   Q = K = P + E (R170_828).
4. R170_830 says that Y_+ is in the logarithmic domain; R170_831 adds that this does not suffice because the
   Tate term is not typed for exterior tests.
5. R170_832 §§5–6 asked to "fix the exterior Tate port canonically"; its §7 (added) and R170_834
   correct this: the source port is already canonical, what is missing is a source–port map.
6. Status of the linear no-go of R161_018: R170_834 §1 says that R161_075 corrects its scope; R170_835 §1
   adds that R162_2302 restores it for the weak carrier. The two memos do not contradict each other but
   R170_834 omits the restoration.
7. R170_837 introduces 𝒫^pol_{M,N} as an additional polar block; R170_838 proves 𝒫^pol = 0 on the core.
8. R170_837 §7.2 claims that the pairing has the sign of λ_δ without restriction; R170_838 limits it to the
   normalized limit vector with fixed phase.
9. R170_837 §8 imposes only M ≥ e^{2T'} but uses δ_Λ(k) = 0, which requires M ≥ N (R170_838 §5).
10. R170_837 omits R162_406 in its non-duplication audit; its "new obligation" had already been decided
    negatively there (R170_838 §7.3). Also a notation collision Z_N (operator) / Z_T (radical).
11. R170_837 labels (8.3) "PROVED/EXACT" as a carrier containing minimality; R170_838 downgrades it to a
    rewriting valid only on the regular core, without a proved extension to the first-contact domain.
12. R170_827 warns against decomposing by parity because U_ρ does not preserve sectors; R170_835 and following
    work in Z_ε. Not an inconsistency (they no longer use U_ρ), but the change of frame is not flagged.
13. R170_840 uses the notation ξ̂^{>L} (without Tate), different from ξ^{>L} of R162_406/R170_838 (with −r_F); the
    memo declares this in (2.7), but ℛ^{>L} of R170_838 (6.2) and the tail of R170_840 (0.1) are not the same
    object.

## (f) Files read (complete reading with Read)

R170_823_MULTISCALE_AVERAGED_PC.md (424 lines) — complete.
R170_824_MULTISCALE_AUDIT.md (95) — complete.
R170_825_COUPLED_COLLAR_PHASE.md (276) — complete.
R170_826_COUPLED_COLLAR_AUDIT.md (95) — complete.
R170_827_RADICAL_MATRIX_CANCELLATION.md (430) — complete.
R170_828_RADICAL_MATRIX_AUDIT.md (77) — complete.
R170_829_GAMMA_EULER_MATRIX_BRIDGE.md (342) — complete.
R170_830_GAMMA_EULER_BRIDGE_AUDIT.md (95) — complete.
R170_831_EXTERIOR_GREEN_FORMULA.md (262) — complete.
R170_832_PUZZLE_MAP_V2.md (171) — complete.
R170_833_EXTERIOR_GREEN_AUDIT.md (88) — complete.
R170_834_CANONICAL_TATE_PORT.md (418) — complete.
R170_835_QUADRATIC_SOURCE_PORT.md (773) — complete.
R170_836_SOURCE_PORT_AUDIT.md (116) — complete.
R170_837_MIXED_PC_FORM.md (932) — complete, in two readings.
R170_838_TWO_WINDOW_AUDIT.md (669) — complete.
R170_839_PUZZLE_MAP_V3.md (133) — complete.
R170_840_BILATERAL_COLLAR_LAW.md (838) — complete, in two readings.
