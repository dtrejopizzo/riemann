# Review 010: rounds 014_A through 024_A against their proofs and against Paper 46

Scope. ROUND_014_A, ROUND_015_A, ROUND_015_B, ROUND_015_C, ROUND_016_A, ROUND_016_B, ROUND_017_A, ROUND_017_B, ROUND_017_C,
ROUND_018_A, ROUND_018_B, ROUND_019_A, ROUND_019_B, ROUND_020_A, ROUND_021_A, ROUND_022_A, ROUND_023_A, ROUND_024_A. Every claim
labelled PROVED is checked against its written proof and against Paper 46 (04-papers/46-row-d-dual-certificates/main.tex:
def:W and eq:nuw L.1225–1235, form-core argument L.1825–1838, prop:arch L.2323–2345, def:ext L.9867–9897, lem:ext-mob,
thm:ext-half L.9913–9936, prop:ext-gauge, prob:ext-L, prop:ext-consol L.9972–10000). Verdicts: CONFIRMED / REFUTED /
DOWNGRADE. Line numbers are memo line numbers. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.
Two certificates were re-run: tools/first_cell/cert_f0.py 100 112 and tools/multi_cell/cert3.py 100 70 0.8 20 0.70; both
reproduce the recorded balls (§9, §10). The restatements of λ_A(T) ≥ 0 that appear in the memos (Schur forms, fibre forms,
comb-null forms) are judged only as rewritings of the same quadratic form of STATEMENT_001; none is used here as a
reduction to any other statement.

## 0. A definitional point that affects rounds 14–16

Paper 46 def:ext defines the complete form on the line with the polar term: 𝒲[Ψ] = (1/2π)∫m|Ψ̂|² − Σ_{n≥2}v_n c_Ψ(log n) +
2A(Ψ)B(Ψ), and thm:ext-half states W_T(Ef) = 𝒲[Ψ_f] for that form. ROUND_001_B (Thm 1.1, the bilinear 𝒲 with A(F)B(G) +
B(F)A(G)) agrees. ROUND_015_A (L.7–9) defines 𝒲 without the polar term, and ROUND_014_A uses 12B Thm 1.1 with the tail form
written as 𝒲 = 𝒜_∞ − comb. With the 15A definition, the identities "M[a] = 𝒢[Sa]" (14A Thm 1.1, 15A Prop 1.1(iii)) and
"𝒲[𝒯u] is the high-block value" are off by 2A(𝒯u)B(𝒯u). ROUND_016_B Lemma 2.3 (L.104–110) identifies the omission, measures
the polar part as ≤ 10⁻⁶ on the 15A bottom vectors, and exhibits an admissible probe where it is O(1) (A = 0.061,
B = 0.479). Ruling: every 14A/15A statement in which 𝒢 or 𝒲 is identified with W_T(Ef) is CONFIRMED only when 𝒲 is read as
the complete form of def:ext; with the 15A definition it is false in general. The numbers of 14A/15A stand (polar part
measured negligible on those vectors).

A second normalisation point. Paper 46 sets ℓ(g) = 2 dist²_{L²(λ,∞)}(r_f, Ḡ_T) (prop:ext-gauge). Rounds 16B–19A use ℓ_g :=
dist² on (λ, ∞) (one half of Paper 46's ℓ); 18A Thm 4.1(ii) (L.197) writes ℓ_g^S = 2ℓ_g, which is consistent with Paper 46.
Any transfer of a constant κ from these rounds to prob:ext-L must divide by 2.

## 1. ROUND_014_A

**§1.0 domain (L.22–30).** CONFIRMED. One integration by parts gives ℱ(ψ1_{[−λ,λ]})(ξ) = ψ(λ)sin(2πλξ)/(πξ) + O(ξ⁻²); the
domain 𝒟 = S{f(λ) = 0} follows. This settles the REVIEW_009 objection to 12B Thm 1.1 correctly.

**Theorem 1.1 (L.32–41).** CONFIRMED, with the reading of §0 (𝒢 built from the complete form). The transfer M[a] = 𝒢[Sa] on
𝒜 is the polarised half-line identity applied to f = Σa_kψ_k with f(λ) = 0, never entrywise; S is an involution of 𝒜 onto
𝒜^S; (ii) and (iii) hold because D is diagonal and ℓ_g[a] = aᵀ(D − DJH⁻¹JᵀD)a, so ℓ_g^S = Sℓ_gS (the sentence on H at
L.38 is superfluous: H does not depend on a at all).

**Proposition 1.2 (L.43–50).** CONFIRMED in form; sizes NUMERICAL.

**Corollary 1.3 (L.52–55).** CONFIRMED (κ ≥ 0, ℓ_g ≤ D since DJH⁻¹JᵀD ⪰ 0 for H ≻ 0).

**Theorem 3.1 (L.106–116).** CONFIRMED (Parseval for the finite Toeplitz section; Gershgorin for the band; operator bound
for the rest). Notational slip: P_X must be the projection onto D^{1/2}X, the space in which b lives, not onto X.

**Proposition 3.2, NO-GO (L.118–133).** CONFIRMED as NUMERICAL NO-GO; class correctly stated: index-axis symbol plus band or
Toeplitz error in D-normalisation. The class does not cover ℓ_g-normalised sweeps (the memo says so at L.126). The chirp
explanation (L.128–133) is ARGUED, as labelled.

## 2. ROUND_015_A

**Lemma 1.0 (L.33–38).** CONFIRMED. rank [[0, X], [Xᵀ, Y]] ≤ 2r; R(Pv, Pv′) = 0 for any projector with range U.

**Proposition 1.1 (L.40–56).** CONFIRMED with the reading of §0. ρ̂(y) = O(|y|⁻⁴) (ρ ∈ C² with a jump of ρ‴), φ̃_k = O(1/ξ), so
ũ_k = O(ξ⁻⁵) and ‖F_N‖² = N⁻¹∫_{Nλ}^∞ũ² = O(N⁻¹⁰); f_k ∈ C² with f_k(λ) = f_k′(λ) = 0 (convolution of a bounded function by a
C² compactly supported mollifier); rank ≤ 8 from Lemma 1.0 with codimension 4.

**§1.1 "by (iv) the compressed matrix is the tail Gram itself, not a proxy" (L.63–66).** DOWNGRADE to ARGUED. (iv) is a
statement about the mollified family M^ρ; the identification of the raw SMS with M^ρ at the Galerkin resolution is the
estimate of L.59–62, which is ARGUED (labelled so in the section heading but not in this sentence).

**Theorem 3.1 (L.128–153).** CONFIRMED. For x < −T and m ≥ 2, τ_{log m}F_n = m^{1/2}F_{nm} on the half-line (the indicator
1_{x−log m<−T} is automatic); Σ_{m|N}Λ(m) = log N; the rearrangement is justified by Σ log N‖F_N‖ < ∞. This is Paper 46
thm:ext-half (last display) and phase 199 E.2 written for 𝒯; it is used, not new. With 15A's 𝒲 the displayed formula
𝒲[𝒯u] = 𝒜_∞[𝒯u] − 2⟨𝒯_log u, 𝒯u⟩ lacks + 2A(𝒯u)B(𝒯u) (§0).

**Remark (L.154–156).** DOWNGRADE in wording. Σ log N/N = ∞ is the divergence of the norm majorant Σ log N‖F_N‖, which
shows that the absolute-convergence hypothesis fails; it does not by itself show that the comb series diverges. "Exactly
the obstruction" → "the absolute-convergence hypothesis fails".

**Corollary 3.2 (L.158–168).** CONFIRMED under one added hypothesis: the double series Σ_{N,N′}𝒜_∞(F_N, F_{N′}) must converge
absolutely, e.g. Σ_N 𝒜_|m|[F_N]^{1/2} < ∞ with 𝒜_|m| the form of |m|. It holds on the mollified data of Prop 1.1 (each
F_N has a single jump of size e^{T/2}|ũ(Nλ)| = O(N⁻⁵)). The stationary-phase localisation of ν_N stays ARGUED.

**Theorem 3.3 (L.170–186).** CONFIRMED. Integration by parts against w ∈ W^{1,1}; Montgomery–Vaughan (J. London Math. Soc.
(2) 8 (1974) 73–82, constant 3π/2) with δ_N ≥ log(1 + 1/N) ≥ 1/(N + 1); the bilinear version through the normality of the
skew-symmetric δ^{1/2}Kδ^{1/2} (norm = numerical radius); constants (3/2)‖w₁′‖₁A₀ and 3‖w₀′‖₁(A₀A₂)^{1/2} recomputed.

**Corollary 3.4 (L.195–203).** CONFIRMED as arithmetic (Σ1/N = log X + γ + O(1/X), Σ log N/N = ½log²X + γ₁ + O(log X/X),
γ₁ = −0.0728). DOWNGRADE of the word "coercive" (L.199): with a_N ≡ 1 the model is a single datum, so (C) gives positivity
of one model value, not coercivity of a block; ε₀ is unspecified.

**§3.5, §4.** ARGUED and NUMERICAL as labelled. §4 falsifier analysis: correct reading (the high-block criterion survives
c < 1, a_P and small finite modifications, so it is not a sign step).

## 3. ROUND_015_B

**§1.1 (L.38–48).** CONFIRMED (assembled from ROUND_001_B, 15A Thm 3.1).

**§1.2 "low-block matrix, PROVED given (S), (T)" (L.50–67).** DOWNGRADE to ARGUED for the survivor. The hypothesis of the
half-line identity is f(λ) = 0 (def:ext); the five-prolate survivor has f_*(λ) ≠ 0 (L.60–62), and by 14A §1.0 the entries
𝒢_{jk} = 𝒲(𝒯u_j, 𝒯u_k) are not defined on raw prolates. Formula (1.2) is PROVED only on the f(λ) = 0 subspace of V_low,
which contains no admissible survivor (L.65–66). The memo states the caveat; the section label must follow it.

**Identity (3.1) (L.125–136).** CONFIRMED as an identity for admissible f with f(λ) = 0. The size statement "up to O(d)" is
ARGUED (𝒲 is not bounded by ‖Ψ‖²; it needs the m-weighted norm of Ψ_f). The recorded numerical instance (five-prolate Ritz
vector) has f(λ) ≠ 0 and is an instance of the mollified limit, ARGUED.

**Lemma 3.1 (L.142–146).** CONFIRMED. ω²/√(ω² − 1) ≥ ω; F(n+1) − F(n) = H_n log(1 + 1/n) − log(n+1)/(n+1) ≥ (H_n − log(n+1))/(n+1)
≥ 0; on (1, 2), min ω²/√(ω² − 1) = 2 at ω = √2.

**§3.4 "PROVED algebra" (L.156–163).** DOWNGRADE to ARGUED. The algebra 𝔴_N^c = 𝔴_N − 2(c − 1)H₁ and ∫H₁dm < ∞ is correct, but
the conclusion "the leading low-block term stays positive" rests on the leading form (1.3), which is ARGUED.

**§4.1 (L.179–183).** CONFIRMED (a^{cΛ}_T = a_T + (1 − c)Π_T on P_T).

**§4.3 (L.200–206).** CONFIRMED as statements about where the falsifiers enter; sizes ARGUED.

**§2.2 harmonic constant (L.108–121).** ARGUED as labelled; the sawtooth identity Σ_n sin(2πnλw)/(πnw) = (½ − {λw})/w and
−ζ′(2)/ζ(2) = 0.5700 are correct, so 2T + 0.430 is the right constant for the model.

## 4. ROUND_015_C

No PROVED claim (L.87–89). The Rayleigh–Ritz direction (Galerkin top eigenvalue is a lower bound for λ_max, so the true
margin is ≤ −0.511) is correct. The finding is consistent with REVIEW_009: the all-profile operator inequality is a
condition on A_τ, not on W_T, and its maximisers are not packets. No conflict with Q12 (certified for T ≤ log 2 and for
the fixed cos² profile only).

## 5. ROUND_016_A

**Theorem 1.1 (L.25–37).** CONFIRMED. f̂ = ½(β̂(· − τ) + β̂(· + τ)); the two square terms give ½∫M_τ|β̂|² by evenness of m;
the cross term gives ½X_τ; c_f(u) = ½cos(τu)c_β(u) + ½∫ββ(· + u)cos(τ(2x + u)); ⟨A_τβ, β⟩ = Σv_n cos(τℓ_n)c_β(ℓ_n).

**Lemma 1.2 (L.43–52).** CONFIRMED. (a) closed form of ê_k checked (sin 2a_kT = 0, cos 2a_kT = (−1)^k); (b) a/(ξ² − a²) is
increasing in a < |ξ| and |K_η| ≤ 2Tητ/π; (c) the integral gives (8/3π²)(η/θ)³(1 − η²/θ²)⁻²; L₁(⅛) = 5.45·10⁻⁴ recomputed.

**Lemma 1.3 (L.54–59).** (i) CONFIRMED (d/dt Re ψ(¼ + it/2) = −½Im ψ′ > 0; m(0) = ψ(¼) − log π = −5.37218). (ii)–(iii) CITED +
NUMERICAL as labelled.

**Proposition 1.4 (L.61–68).** CONFIRMED (log(1 − s) ≥ −s/(1 − s); |r| ≤ 1/(20t²) on both arguments; (1/2π)∫ξ²|β̂|² = ‖β′‖² ≤
η²τ²‖β‖² since β vanishes at ±T; outside the band M_τ ≥ ½(m(τ) + m(0)) by monotonicity).

**Proposition 1.5 (L.70–78).** R-bound CONFIRMED (every ξ has |ξ| ≥ τ or |2τ + ξ| ≥ τ; Cauchy–Schwarz on each region with the
factor above τ). X-bound: DOWNGRADE of the constant. The step ∫_τ^∞(c + log ζ)²ζ⁻⁴dζ ≤ (c + log τ + ⅓)²/(3τ³) (L.77) is false:
the exact value is (1/(3τ³))[(A + ⅓)² + 1/9], A = c + log τ. Also the 1/τ added at L.76 is unnecessary (log(1 + ζ − τ) ≤ log ζ
for τ ≥ 1). Corrected statement: |X_τ(β)| ≤ √(2L₁)(5.73 + log τ)‖β‖² for τ ≥ 10 (the printed 5.72 holds for τ ≥ 14).
No downstream consequence: Theorem 1.6's E is not used to certify anything (L.97–98).

**Theorem 1.6 (L.80–88).** CONFIRMED with the corrected constant in E. It is a sufficient condition for positivity of Q_T on
band-limited packets; the falsifier note's phrase "(HB_η) is a necessary condition" (L.203) is a reading through the upper
bound of the same theorem and holds only up to E; DOWNGRADE that phrase to "necessary up to the error E".

**P_T transfer bound (L.89–92).** The bound on |⟨f, e^{±x/2}⟩| is stated as PROVED but only sketched ("same Cauchy–Schwarz"):
with the complex argument s = −(½ ± iτ) in Lemma 1.2(a) the denominator becomes |a_k² + s²|, whose lower bound
τ²(1 − η² − 1/(4τ²)) and the e^{T/2} boundary factor are plausible but not written out. DOWNGRADE to ARGUED until derived.
The inequality transfer Q_T → W_T is ARGUED, as labelled.

§2–§3: NUMERICAL as labelled. The λ_A(1.5) runs give an upper bound only, as the memo says (L.186–195).

## 6. ROUND_016_B

**Lemma 2.1 (L.86–95).** CONFIRMED. F₁(x − log N) = N^{1/2}F_N(x) for x < −T; ‖F₁‖² = ∫_λ^∞|u|². "T-free" holds for 𝒜_∞,
the comb and the product A·B (translation multiplies A by e^{T/2}, B by e^{−T/2}); the constraint functionals carry T.

**Lemma 2.2 (L.97–102).** CONFIRMED (supports; the comb shift log 2 meets the cell in one point). Here 𝒲 is 15A's polar-free
form; the complete form adds 2A(F₁)B(F₁) (Lemma 2.3).

**Lemma 2.3 (L.104–110).** CITED + NUMERICAL as labelled; agrees with Paper 46 def:ext and thm:ext-half. This lemma is the
correction recorded in §0.

**Remark 2.4 (L.112–116).** CONFIRMED for the isolated exponential piece J·1_{x<−T}e^{β(x+T)}; the cross terms between that piece
and the continuous part are not covered, so "the jump part of 𝒜_∞" is a heuristic split (ARGUED), as the memo half-says.

§3–§4: NUMERICAL and ARGUED as labelled. The (HR_g) statement (L.194) is OPEN.

## 7. ROUND_017_A

**Proposition 1.1, Schur form (L.30–35).** CONFIRMED (standard; at λ = 0 a singular C is handled by sup = +∞ on its kernel
unless b vanishes there).

**Proposition 1.2 (L.37–58).** CONFIRMED for admissible f with f(λ) = 0: with Ψ and G disjointly supported, only ⟨Ψ, G(· + u)⟩
survives, b = −𝒲(Ψ, G) = ∫h_G dν with ν = ½K du + ΣΛ(n)n^{−1/2}δ_{log n}; on E-images the second-level identity (1.3) follows
from the radical lemma (ROUND_001_B Thm 1.1 with G = Φ_g, Ψ_g). ARGUED for the survivor (mollified limit), as stated.

**Proposition 1.3 (L.60–65).** CONFIRMED as an identity: Φ_f(−t) = Φ_{ℱf}(t) by Poisson summation (f even, f(0) = ℱf(0) = 0),
and ℱ(ψ_k1) = √χ_kφ_k for k ≡ 0 (mod 4). Two corrections. (i) For the survivor (f_*(λ) ≠ 0) Poisson summation holds with
midpoint values at the jumps and conditionally convergent dual sums; the identity is ARGUED there. (ii) "Its norm is O(√d_8)"
(L.63) is ARGUED: it needs a bound for E on functions supported on (λ, ∞), which lem:ext-mob does not give.

**Proposition 3.1 (L.130–139).** CONFIRMED. 𝒲^c = 𝒲 + (1 − c)𝒞; 𝒲(Φ, G) = 0 and Tate(Φ, G) = 0 for G ∈ P_T; 𝒞(Ef, G) = Π_T(Ef, G)
for window functions; 𝒜_∞(Φ, G) = 𝒞(Φ, G) by radicality.

**Schur form (4.1) (L.167–184).** CONFIRMED as a rewriting of Prop 1.1 with b from Prop 1.2, PROVED for admissible data with
f(λ) = 0, ARGUED for the survivor (as labelled). The (R) reading at L.174–176 uses span{Ef_*, Eg} without orthogonalising Eg
against F; the determinant form of 18B Lemma 1.2 makes this harmless.

## 8. ROUND_017_B

**Proposition 1.1 (L.16–31).** CONFIRMED. Recomputed: (1/T)∫_0^{2T−ℓ}sin(a_jy)sin(a_k(y + ℓ))dy gives
(σ_k − ε_jε_kσ_j)/(a_j − a_k) for j ≠ k, (2T − ℓ)cos(a_kℓ) for j = k, and (σ_k + ε_jε_kσ_j)/(a_j + a_k), using
sin(pπ − y) = −(−1)^p sin y; summing c_n gives CS − ESCE + ESHE + HS + Dd. Sh(−ℓ) = Sh(ℓ)* gives A = ½(𝔈 + 𝔈ᵀ).
§2–§3 NUMERICAL (no certificate), as stated (L.159–160).

## 9. ROUND_017_C

**§1.1 (L.22–27).** CONFIRMED; C₀ + ∫_{log 2}^∞K = −5.37218 + 1.76275 + 1.23096 = −2.3785 recomputed.

**Lemmas 2.1–2.4 (L.45–73).** CONFIRMED. 2.2: min(m, M) = M − h with 0 ≤ h ≤ M − C₀. 2.3(ii): Taylor remainder bound
L^{1/2}(|τ|L/2)^n/n! integrated over |τ| < τ* and over y gives the Hilbert–Schmidt bound as printed. 2.4: the cross terms
⟨Gp, r⟩ = ⟨(1 − P)Gp, r⟩ ≤ εab and ⟨Gr, r⟩ ≤ εb²; ‖p_W‖ ≤ ηb from Wᵀp = −(⟨r, (1 − P)w_i⟩); γ ≥ 0 because G ⪰ 0 (needed for
γ‖p₁‖² ≤ γa²).

**Certification protocol (L.75–84).** CONFIRMED in design. The Bernstein-ellipse radius uses analyticity of m in |Im τ| ≤ 3/8
(poles of ψ(¼ + iτ/2) at |Im τ| ≥ ½) and the bound |τ² + 1/4| ≥ 7/64 there.

**Theorem 3.1 (L.88–97).** CONFIRMED and re-run: python3 cert_f0.py 100 112 returns PD = True, γ = 2.6976772206,
ε = 2.61·10⁻⁸, η = 3.29·10⁻²⁶⁸, μ₀ ∈ [0.06961173221 ± 4.38·10⁻¹²] (CERTIFIED), identical to the memo.

**Corollary 3.2 (L.98–99).** CONFIRMED. On {B(F) = ∫Fe^{−x/2} = 0} the polar term vanishes. Note: prop:arch of Paper 46 writes
𝒜_∞ = C₀‖F‖² + Lev without the polar term and (iii) calls "complete form" W_T on windows with empty contact set; the memo's
"complete form = 2AB + 𝒜_∞" is def:ext's reading. Either reading gives the corollary on {B = 0}.

**Theorem 3.3 (L.101–108).** CONFIRMED as computer-assisted for the stated T (not re-run; the cert_multi.py outputs
out_multi_08.txt, out_multi_10.txt on disk read CERTIFIED with balls [0.5276311697 ± 4.42·10⁻¹¹] and [0.5494172344 ±
3.66·10⁻¹¹], matching the memo). It is a statement about the transported
constraints only (the transport is the ARGUED idealisation of 16B §3.1), as the memo states.

**§4(i) (L.116–122).** CONDITIONAL as labelled (transport, and the factor λ is the NUMERICAL normalisation of 16B §1.2).

## 10. ROUND_018_A

**Lemma 1.1 (L.65–80).** CONFIRMED (triangle inequality for the seminorm (𝒬 + β)^{1/2}; β = 2.3784 rigorous). q_W and δ* are
NUMERICAL.

**Proposition 3.1 (L.134–138).** CONFIRMED (on length log 2 no comb shift acts; B(𝔇₂F) = B(F) is the transported f(0)).

**Lemma 3.2 (L.140–150).** CONFIRMED. I₀ and I₂ both have length log(3/2), so S maps the Legendre basis index by index; only
m = 2 acts on length log 3; ‖𝔇₃‖² = 2, σ_min² = ½ (eigenvalues 2, ½ of [[3/2, 2^{−1/2}], [2^{−1/2}, 1]]).

**Lemma 3.3 (L.152–170).** CONFIRMED. Every term recomputed: 𝔇₃p ∈ ran P, 𝔇₃r ⊥ ran P, Π commutes with P, |Π[H]| ≤ v‖H‖² (in
fact ≤ (v/2)‖H‖²), polar expansion with δ_α, δ_β, gauge term with ‖X‖‖C_g‖δ_g, constraint split p = p₁ + p_W; collecting gives
γa² − 2X_c ab + Y_c b², nonnegative iff X_c² ≤ γY_c.

**Theorem 3.4 (L.172–188).** CONFIRMED and re-run at T = 0.8: python3 cert3.py 100 70 0.8 20 0.70 returns γ = 3.75658·10⁻⁴,
X_c = 4.44·10⁻³, Y_c = 0.19352, CERTIFIED = True, identical to the memo. T = 1.0 not re-run (out3_10_k07.txt on disk).
The D-unit figures 0.779 / 0.951 are 0.35λ, consistent with ℓ_g^S = 2ℓ_g (§0).

**Theorem 4.1 (L.191–204).** (i) CONFIRMED (= Prop 3.1 + Thm 3.4 on the idealised class). (ii) CONDITIONAL as labelled.
(iii) NUMERICAL NO-GO, class correctly stated (idealised R-cell class with transported constraints, R-uniform κ).

**§5 falsifier remark (L.206–216).** NUMERICAL; the reading "not weight-blind for c > 1" is correct and is later explained by
21A Prop 3.2 (the c-dependence is c·𝒦_R with 𝒦_R Λ-free).

## 11. ROUND_018_B

**Lemma 1.1 (L.25–30).** CONFIRMED (the collapse is linear in the weight).

**Lemma 1.2 (L.32–36).** CONFIRMED. With G = Eg − tF, ρa_T(G) − a_T(F, G)² = ρa_T(Eg) − a_T(F, Eg)² identically in t; a_T = 𝒲̂ on
E-images of admissible data with f(λ) = 0 (survivor: mollified limit, ARGUED).

**Remark 4.1 (L.180–187).** CONFIRMED (|⟨Ψ, Ψ(· + u)⟩| ≤ ‖Ψ‖‖Ψ1_{(−∞,−T−u)}‖).

**NO-GO (L.207–212).** CONFIRMED as NUMERICAL NO-GO; class correct: the rung piece of the Schur inequality in tail form with
collapsed weight c·log N, rung data frozen, tested for falsifier (a) only. It does not cover the window form (which dies at
|1 − c| ≈ 10⁻²², 17A), and 19B later shows the c-robustness is a property of the representative.

## 12. ROUND_019_A

**Proposition 1.1 (L.22–41).** CONFIRMED. The annihilator argument is correct: ℓ(ℱf) = ∫fΦ with Φ entire, Φ(x) + Φ(−x) = 0 on
[−λ, λ] hence everywhere, and every h ∈ C^∞(J̄_R) is the restriction of ℱ of an even Schwartz function. Form-norm density
follows from H¹ ⊂ H^s (s < ½) and density of C^∞ in the form domain (the core argument of Paper 46 L.1832–1837); the
constraint correction by d_i is valid. NO-GO for the qualitative band constraint: PROVED, class correct.

**Lemma 2.1 (L.60–64).** CONFIRMED. The gloss "the band information actual R-cell data carry is exactly" (L.63) overstates:
the lemma is an upper bound. Read "at most".

**Theorem 4.1 (L.139–152).** CONDITIONAL as labelled; the derivation from Lemma 2.1 and (H_band), (H_lim) is correct.

**§5.1 (L.167–178).** DOWNGRADE of item (c). The transported A and B weights use the summation map over all n with
ne^{−T} < λ, i.e. integers up to N = e^{2T} (≈ 4.95 at T = 0.8, 7.39 at T = 1.0), not only {1, 2}. A Beurling system leaves
Theorem 3.4 of 18A word for word unchanged only if its integers agree with ℕ below N (or if the constraint weights are frozen
at their ℕ values). Items (b), (d) CONFIRMED (v_n does not enter the weights). 22A §2.3 later measures that swapping the
summation set changes nothing at the sign level, which supports the frozen-weight reading NUMERICALLY.

**§5.2 certificates (L.180–193).** CONFIRMED as computer-assisted (outputs on disk; not re-run).

## 13. ROUND_019_B

**Proposition 1.1 (L.31–37).** CONFIRMED (Möbius inversion Σ_nΣ_{d}μ(d)g(dnu) = g(u); the free values on (0, 1/λ) are fixed by
one bump for ∫f = 0; the difference of two preimages is in 𝒢_T). It is lem:ext-mob of Paper 46.

**Corollary 1.2 (L.39–54).** CONFIRMED as a rewriting of λ_A(T) ≥ 0 through the core of Paper 46 L.1832 and the half-line
identity; the comparison with prob:ext-L (κ = 0 versus κ > 0) is correct.

**Theorem 2.1 (L.63–82).** CONFIRMED. Φ_φ = Σn^{−1/2}h(· + log n), Φ̃_φ = ζ·Mφ, B(Φ_φ) = ζ(0)Mφ(0) = 0 after the correction,
|ĥ_R|² = R|η̂(R·)|² of mass 2π‖η‖²; limits m(0)ζ(½)²‖η‖² = −11.457‖η‖² and m(10)|ζ(½ + 10i)|²‖η‖² > 0. The bumps χ_r, χ_l must
sit inside (−∞, −T) in the u-variable, which holds for R > 1. Zero-free.

**Corollary 2.2 (L.84–89).** CONFIRMED (Ψ_{f+tφ} = Ψ_f + tΦ_φ; 𝒲̂^c = 𝒲̂ + (1 − c)𝒞; 𝒞 = 𝒜𝒫 on Φ_φ by radicality, Paper 46
prop:ext-gauge).

**Corollary 2.3 (L.91–97).** CONFIRMED as NO-GO, class correct (inequalities 𝒜𝒫 − c𝒞 ≥ 0 on the full class of admissible tails,
c ≠ 1). DOWNGRADE of one phrase: "c = 1 is the only weight at which it is semi-bounded at all" (L.93) asserts semi-boundedness
at c = 1, which is the target itself; read "the only weight at which it can be semi-bounded".

**(ii_s) and observations (α), (β) (L.103–114).** OPEN and ARGUED as labelled.

## 14. ROUND_020_A

**Lemma 1.1 (L.22–23).** CONFIRMED.

**Lemma 1.2 (L.25–29).** CONFIRMED (𝒞 → +∞ along Ψ + tΦ₊ and → −∞ along Ψ + tΦ₋ for fixed large R in Thm 2.1; intermediate
values on the plane).

**Theorem 1.3 (L.31–38).** CONFIRMED (𝒲̂^c[Ψ′] = w + (1 − c)𝒞[Ψ′]; 𝒞 takes every real value on the fibre).

**Corollary 1.4 (L.40–45).** CONFIRMED as a rewriting on V_T (each fibre meets {𝒞 = 0}, where 𝒜𝒫 = 𝒲̂ = w). Its link to
λ_A(T) ≥ 0 passes through 19B Cor 1.2 and the radical identity, as the memo says.

**Theorem 1.5 (L.47–54).** CONFIRMED on finite-dimensional S containing Φ₊, Φ₋ (equality-constrained S-lemma with an indefinite
constraint form, CITED; then μ ≥ 1 from Φ₋ and μ ≤ 1 from Φ₊). The infinite-dimensional version stays ARGUED.

**§3 (L.101–119).** (A) + (B_δ, s) ⟹ λ_A(T) ≥ 0: CONFIRMED. The "not weaker than prob:ext-L" reading is ARGUED.

## 15. ROUND_021_A

**Lemma 1.1 (L.24–27).** CONFIRMED (infimum of affine functions is concave and upper semicontinuous).

**§2.1 (L.42–46).** CONFIRMED (nested trial spaces; outer bounds).

**§3.1 (L.92–100).** CONFIRMED (τ_aτ_b = τ_{a+b} by convexity of I; linear independence via a bump at the left end;
[M_x, τ_a] = aτ_a).

**Proposition 3.2 (L.102–115).** CONFIRMED (homomorphism + injectivity on n < R + Λ ∗ 1 = log; Π_w[H] = 2⟨H, P_wH⟩ for real H).

**Lemma 3.3 (L.117–127).** The three inequalities are CONFIRMED. DOWNGRADE of the "In particular" sentence (L.120–121): with
only bounded Rayleigh quotient for the vector v with 𝒦[v] < 0, the bound 1 − c₋ ≤ Q^{(1)}[v]/|𝒦[v]| stays bounded and does not
force c₋ → 1. Lemma 3.3 gives J_R ⊇ [1 − λ₀/‖𝒦‖, 1 + λ₀/‖𝒦‖] and c₊ − 1 ≤ λ₀/K₀; two-sided shrinking needs vectors v with
Q^{(1)}[v]/|𝒦[v]| → 0, which is NUMERICAL here (§2.2). Accordingly §3.4 "the two-sided shrinking is the same fact as
λ₀ → 0" (L.130–131) is PROVED in one direction (two-sided shrinking ⟹ λ₀ → 0 when ‖𝒦‖ is bounded) and for the c₊ side
(when K₀ stays bounded below); the c₋ side is NUMERICAL.

**§3.4(ii)(c) (L.144–150).** CONFIRMED structurally (Lemma 3.1 of 22A); numerical part ARGUED, then measured in 22A.

**NO-GO (L.161–164).** CONFIRMED, class correct (positivity windows in the comb weight on idealised R-cell data). Its content is
the 18A collapse read in c.

## 16. ROUND_022_A

**Lemma 3.1 (L.95–100).** CONFIRMED (no integrality used). Injectivity for a general discrete set needs distinct log-positions
(true for a set).

**Proposition 3.2 (L.102–118).** CONFIRMED. For a free system k_i(x) = (E_i ∗ 1_𝒩)(x), so ∂_{η_i}𝔇 = −G_i𝔇(½ + ∂);
Λ_𝒩 = Ση_iE_i; Ση_ik_i = log; Ση_i²E_i^{(1)} = Λ_𝒩·log. Hellmann–Feynman CITED.

**Proposition 3.3, structural part (L.120–125).** The isomorphism ℕ^{1+t} ≅ ℕ with Λ scaled by 1 + t: CONFIRMED. "ℕ is the only
member closed under addition (2^{1+t} = 1 + 1 forces t = 0)": the statement is true, the proof is REFUTED as written —
1 + 1 = 2 only has to equal some n^{1+t}, and 4^{1/2} = 2 lies in ℕ^{1/2}. Correct proof: additive closure with 1 gives
ℕ ⊆ ℕ^{1+t}, so #{x ≤ X} ≥ X against ≍ X^{1/(1+t)}, hence t ≤ 0; for t < 0, 2^{1+t} + 2^{1+t} = m^{1+t} forces 1 + t = 1/j
(j ≥ 1 integer), and then 1 + 2^{1/j} = m^{1/j} forces (1 + 2^{1/j})^j ∈ ℤ, false for j ≥ 2. So t = 0. Sign part NUMERICAL.

## 17. ROUND_023_A

**Lemma 2.1 (L.27–33).** CONFIRMED (Φ(μ) = 𝔇⁻¹; [M, 𝔇⁻¹] = −𝔇⁻¹[M, 𝔇]𝔇⁻¹; P = Φ(μ ∗ log) = 𝔇⁻¹[M, 𝔇]; the identity is
Λ·log + Λ ∗ Λ = μ ∗ log², Selberg).

**Proposition 2.2 (L.35–47).** CONFIRMED. The pieces δ_lam, δ_sig, δ_pos add up to ∂_t𝔇 = −[M, 𝔇](½ + ∂) and
∂_tP = P − [M, P](½ + ∂); δ_lamλ_k = −𝒦_R[u_k]. The displayed δ_•Q (L.42) is correct only with P replaced by its symmetric
part P^{sym} in the term −4⟨δ𝔇F, P𝔇F⟩, as the parenthesis at L.43–44 says; write it that way.

**Proposition 2.3 (L.49–58).** CONFIRMED ((U_sτ_{sa}G)(y) = 1_{I/s}(y)(U_sG)(y − a); cell condition n < R^{1/s}).

**§2.4 (L.60–63).** CONFIRMED: δ_lamλ_k = −(Q₀[u_k] − λ_k); its sign on u₀ is conditional on Q₀[u₀] > λ₀ (measured).

**Proposition 2.4 (L.65–78).** DOWNGRADE (incomplete list of transported data). The polar term 2A(𝔇F)B(𝔇F) is part of Q and its
functionals A, B are not dilation-covariant; under U_s they are transported like 𝒜 and C. The virial identity is correct
once the polar functionals are included in the transported data (an extra δ_{AB} term, or 𝒜 read as 𝒜 + 2AB). Prop 2.3(iii)
has the same omission.

**Lemma 4.1 (L.139–147).** CONFIRMED. Caveat: for a non-affine family the positive set need not be an interval; "left edge"
must mean the nearest failure point to the left of 0.

**2×2 coupling formula (L.157–161).** CONFIRMED (det of diag(λ + τa) − τ²c²).

**§5 (L.183–210).** ARGUED as labelled; the logical point (iii) (a slope sign at t = 0 says nothing about λ₀(0) ≥ 0) is
correct.

## 18. ROUND_024_A

**Proposition 2.1 (L.84–95).** The lemma is CONFIRMED (finitely many distinct affine inequalities on y ≤ Y, each strict for Λ,
remain valid for cΛ with |c − 1| ≤ δ(𝒮, Y) > 0). The NO-GO drawn from it is DOWNGRADED to NO-GO CONDITIONAL. (i) The sentence
"λ_A(T; cΛ) < 0 for every c ≠ 1 as soon as λ_A(T; Λ) is at its interval endpoint" (L.92) is incorrect as a general claim:
c ↦ λ_A(T; cΛ) is concave and continuous, so when λ_A(T) > 0 the window J_T is a neighbourhood of 1. (ii) The argument bites
only if δ(𝒮, Y) exceeds the true half-width of J_T; the latter is measured at ≈ 10⁻¹⁶ (c < 1) and ≈ 5·10⁻²² (c > 1) at T = 1
(17A, NUMERICAL), not certified; the certified falsifier is c = 1.1 (Q1). So the class statement is CONDITIONAL on the
NUMERICAL window width; δ(𝒮, Y) is not computed.

**Lemma 4.1 (L.123–126).** CONFIRMED.

**Lemma 4.2 (L.128–133).** CONFIRMED (substitution t = T − s; the H¹ remainder constants hold, ∫_0^δ(δ − s)^{1/2} ≤ δ^{3/2} and the
product term ≤ δ²‖F′‖²).

**Proposition 4.3 (L.135–142).** CONFIRMED with the quantitative reading: for fixed T the "o(h)" is the H¹ remainder of Lemma 4.2
with δ = 2h; for a single F the limit h → 0 has no meaning because P_T moves with T. The sign statement on real even
(resp. odd) states is correct.

**Corollary 4.4 (L.144–155).** (i) CONFIRMED. (ii) CONDITIONAL on (R_edge), as labelled.

**Class statement (L.157–169).** CONFIRMED as NO-GO, class correct: propagation of positivity through contact entrances along N.
The monotonicity of λ_A in T between contacts (P_T ⊂ P_{T′}, extension by zero) is PROVED and recorded (prop:arch(i) has the
archimedean analogue). The entrance law is weight-generic, hence not a sign step.

**Design C (L.97–109).** ARGUED, correctly identified as a retry of L′/L′♯; not pursued.

## 19. NO-GO register (class and correctness)

1. Index-axis symbol + band/Toeplitz error for the high block in D-units (14A Prop 3.2): NUMERICAL NO-GO, class correct;
   does not cover ℓ_g-normalised sweeps.
2. "Long-range band = finite-rank radical correction" (15A §1.3): NUMERICAL falsification of a hypothesis, not a class.
3. Comb averaged along chirps (15A §3.6): CONFIRMED correction (the comb collapses to resonant weights log N; mean values act
   only on the non-resonant remainder).
4. D-unit floor of the high block (16B §4(i)): ARGUED with NUMERICAL witnesses; the metric is ℓ_g.
5. Idealised R-cell class with transported constraints, R-uniform κ in ℓ_g (18A Thm 4.1(iii)): NUMERICAL NO-GO, class correct.
6. Rung piece of the Schur inequality as sign carrier, tail form with c·log N (18B): NUMERICAL NO-GO for falsifier (a), class
   correct.
7. Qualitative band constraint on R-cell data (19A Prop 1.1): PROVED NO-GO, class correct.
8. Absolute band-defect bounds on R-cell data (19A §3): NUMERICAL.
9. Comb-robust / weighted bounds 𝒜𝒫 − c𝒞 ≥ 0 on the full class of admissible tails, c ≠ 1 (19B Cor 2.3): PROVED NO-GO, class
   correct, zero-free.
10. Existential gauge-fixed representative with a comb margin (20A Thm 1.3): PROVED NO-GO, class correct.
11. Canonical Λ-free sections with uniform δ (20A §2): NUMERICAL PIVOT, not a closed class.
12. Positivity windows in the comb weight on idealised R-cell data (21A): NO-GO, class correct; the c₋ side of the shrinking
    is NUMERICAL (§15).
13. R-cell sign as a monoid invariant / additive characterisation on the exponent ray (22A, 23A): NUMERICAL; the reading
    "addition singles out ℕ" is ARGUED closed (23A §5).
14. Finitely many strict Chebyshev floor relations (24A Prop 2.1): NO-GO CONDITIONAL on the NUMERICAL width of J_T.
15. Positivity propagated through contact entrances along N (24A §4): PROVED NO-GO for the sign of the entrance term, class
    correct; the remaining rate bound is the recorded open (EB_C).
16. Prolate extremality on the index-8 subspace (24A Design C): retry of L′/L′♯, ARGUED.

## 20. Summary of verdicts

- REFUTED: the written proof of "ℕ is the only additively closed ℕ^{1+t}" (22A Prop 3.3; statement true, corrected proof in
  §16); the integral bound at 16A L.77 (constant 5.72 → 5.73 for τ ≥ 10).
- DOWNGRADE: 15A §1.1 "not a proxy" → ARGUED; 15A Remark (domain) wording; 15A Cor 3.4 "coercive" → positivity of one model
  value; 15B §1.2 → ARGUED for the survivor; 15B (3.1) size → ARGUED; 15B §3.4 → ARGUED; 16A Prop 1.5 X-constant; 16A P_T
  transfer bound → ARGUED; 16A "(HB_η) necessary" → up to E; 16B Remark 2.4 split → ARGUED; 17A Prop 1.3 norm O(√d_8) and the
  survivor case → ARGUED; 19A Lemma 2.1 gloss; 19A §5.1(c) → integers below N must agree; 19B Cor 2.3 phrase; 21A Lemma 3.3
  "in particular" and §3.4 two-sided equivalence → one direction PROVED, c₋ side NUMERICAL; 23A Prop 2.4 and Prop 2.3(iii)
  → add the polar functionals; 24A Prop 2.1 NO-GO → CONDITIONAL.
- Definitional: 14A/15A identifications of 𝒢, 𝒲[𝒯u] with W_T(Ef) hold only with the complete form of def:ext (polar term),
  supplied by 16B Lemma 2.3.
- CONFIRMED: everything else labelled PROVED in the listed memos, including the two re-run certificates (17C Thm 3.1, 18A
  Thm 3.4 at T = 0.8).
- No step in rounds 14–24 is a sign step; every PROVED piece is either an identity, a coercivity piece that survives some
  falsifier, or a NO-GO. Row D OPEN.
