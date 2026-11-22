# PROOF_L_SHARP_R_001 — Strategy R: the σ-derivative identity for 𝔔 on the critical line

Phase 199, prover memo (pen and paper; no numerics needed). Target: Lemma L′♯ = (★★_u) (AUDIT_L_SHARP_2 §7). No analyticity of 1/ζ or
F/ζ off the line is used; every derivative below is a pointwise derivative *at* Re = ½, at points where ζ ≠ 0, and the
identities are stated in a ζ-weighted form that is continuous across on-line zeros.
Notation of memos F, P, Q.

**Outcome.** L′♯ NOT proved. (R.0) The premise "F_log = −∂_sF" is FALSE; the correct relation is
F_log = ∂_sF + F[ρ log X] (PROVED, with a one-line counterexample to the premise). (R.1) The correct σ-derivative identity
lives in a *second* complex variable — the exponent w of the partial sums ζ_X(w), with the Mellin variable s frozen:
  Θ_∞|F|² − 2Re(F̄F_log) = |ζ(½+iτ)|²·∂_u|Φ(s,w)/ζ(w)|² at w = 1−s,  u = Re w   (PROVED, exact, pointwise).
Hence 𝔔 = (1/2π)∫|ζ|²∂_u|Φ/ζ|²dτ + 2AB, and Q(F₀,F₀) = 0 becomes "Φ₀/ζ = R(s) does not depend on w" (one-line proof
of F Thm F.2(ii)). (R.2) Integrated without the 1/ζ: 𝔔 = (1/2π)∫Θ_∞|F|²dτ + N′(0) + 2AB with N(σ) ≥ 0 the Gram norm of
memo Q (moment form) — so (R.1) is a reformulation (REF-D level). (R.3) NO-GO for any pointwise sign/monotonicity: the
integrand is Θ_∞|R|² < 0 on |τ| < τ₀ for shallow data, where 𝔔 ≥ 0 is known (CITED Zhu). (R.4) Q(G,G) ⪯ 0 is not
proved; a stationary-phase reading (ARGUED) shows each harmonic k of the Euler–Maclaurin sawtooth enters with weight
2log k − log(τ/2π): negative exactly below the approximate-functional-equation symmetry point k < √(τ/2π), positive
above it. That is the precise inequality left.

## 0. Corpus / index check and the new reason
Index searched for σ-derivative / ∂_σ / AFE / Riemann–Siegel: NT_007–010 (σ-derivative of the height flow at σ = 1,
PARTIAL), INV_T_001 (∂_σ log|q| of a unimodular gauge in a Green identity, NO-GO 𝒦_T), L2_012 (|ζ|²-positivity, AFE as
class, NO-GO), INV_K_001 (AFE/Euler–Maclaurin = reformulation), INV_C_001 (Λ only via ∂_σ log of the density of h⁰).
**Why not a retry.** All of these differentiate in the Mellin variable of a window/gauge object. Here the derivative is in
the exponent w of the partial sums of the exterior form, with s frozen (two-variable Φ(s,w)); R.0 shows the Mellin-σ
derivative is the *wrong* one. Outcome is again a reformulation (R.2), recorded as such; no sign source is claimed.

## 1. R.0 — the premise F_log = −∂_sF is FALSE (PROVED)
Put Φ(s,w) := ∫_1^∞ρ(X)X^{−s}ζ_X(w)dX = Σ_n n^{−w}∫_n^∞ρX^{−s}dX (absolutely convergent for Re s = ½, Re w > −½, since
ρ = O(X^{−2})). Then F(s) = Φ(s,1−s), F_log(s) = −Φ_w(s,1−s) (= ∫ρX^{−s}Σ_{n≤X}n^{s−1}log n), and
  ∂_sF = Φ_s − Φ_w = −F[ρ log X] + F_log,  i.e.  **F_log = ∂_sF + F_L,  F_L := ∫ρ log X·X^{−s}ζ_X(1−s)dX.**
In the y = log(X/n) picture: −∂_s multiplies Ψ̌ by y = log(X/n) (the dilate *coordinate*), while F_log multiplies by
log n (the dilate *index*); they are complementary, log X = y + log n.
Counterexample to the premise: ρ supported in (1,2) ⇒ ζ_X ≡ 1, F = R, F_log = 0, −∂_sF = ∫ρ log X·X^{−s}dX ≢ 0. □
Consequence: the requested formula "Q(F,F) = (1/2π)∫|ζ|²∂_σ|F/ζ(s)|²dτ" is not an identity. (What is true in the Mellin
variable: Θ_∞|F|² − ∂_σ|F|² = −|ζ|²∂_σ|F/ζ(1−s)|², using ∂_σ log|ζ(1−s)|² = −2Re(ζ′/ζ)(s̄) = Θ_∞; but then the extra
term −2Re(F̄F_L) remains and nothing is gained.) **Convention check:** ∂_σ log|ζ(s)|² = 2Re(ζ′/ζ)(s) = −Θ_∞,
∂_σ log|ζ(1−s)|² = +Θ_∞, ∂_σ log|χ(1−s)|² = 2Θ_∞ on the line (χ(1−s) = ζ(1−s)/ζ(s)), all from F Thm F.1 (FE only).

## 2. R.1 — the correct identity: derivative in the partial-sum exponent (PROVED)
**Theorem R.1.** Fix s = ½+iτ with ζ(½+iτ) ≠ 0 and put h_τ(w) := Φ(s,w)/ζ(w), holomorphic in w near w₀ = 1−s = ½−iτ
(only local non-vanishing at the on-line point w₀ is used). Then
  Θ_∞(τ)|F(s)|² − 2Re(F̄F_log)(s) = |ζ(½+iτ)|²·∂_u|h_τ|²(w₀),  w = u+iv.
*Proof.* ∂_u|h|² = 2Re(h̄h′), h′ = Φ_w/ζ − Φζ′/ζ²; so |ζ(w₀)|²∂_u|h|² = 2Re(Φ̄Φ_w) − 2|Φ|²Re(ζ′/ζ)(w₀). Φ_w = −F_log,
and −2Re(ζ′/ζ)(1−s) = −2Re(ζ′/ζ)(s̄) = −2Re\overline{(ζ′/ζ)(s)} = Θ_∞ (F Thm F.1). |ζ(w₀)| = |ζ(½+iτ)|. □
The right side equals ∂_u|Φ|² + Θ_∞|Φ|² at w₀, which is continuous in τ across on-line zeros (no 1/ζ), so
  **𝔔 = (1/2π)∫_ℝ|ζ(½+iτ)|²∂_u|Φ(s,·)/ζ|²(1−s)dτ + 2AB**  (integrand defined a.e., integrable by F Thm F.1).
No interchange of ∂ and ∫ is needed in this form (the derivative is taken pointwise and the result is the integrand of
F.1). **Corollary R.1′ (PROVED).** For F₀ = ζ(1−s)R(s): Φ₀(s,w) = ζ(w)R(s), h ≡ R(s) constant in w ⇒ integrand ≡ 0:
F Thm F.2(ii) in one line; Q-null vectors = data whose partial-sum quotient is w-independent. Polarised:
Q(U,V) = (1/2π)∫|ζ|²Re[h̄_U∂_wh_V + h̄_V∂_wh_U]dτ (line part), so Q(F₀,V) = (1/2π)∫|ζ|²Re[R̄·∂_wh_V]dτ.
**cΛ / Beurling (PROVED).** With weight c on the prime part: Θ_∞|F|² − 2cRe(F̄F_log) = c|ζ|²∂_u|h|² + (1−c)Θ_∞|F|² —
exactly Q.2's Toeplitz symbol a_c; nothing new. ζ ↦ ζ^c is *not* the right deformation: Φ is built from a_n ≡ 1
partial sums and is unchanged; only the weight/denominator would change, which does not reproduce the cΛ form.
Beurling (no FE): Θ_∞ ≠ −2Re(ζ_P′/ζ_P)(1−s), defect (Θ_∞ + 2Re(ζ_P′/ζ_P)(s̄))|F|² added. The identity's only arithmetic
input is the FE (conductor 1), as in Q.4; non-decisive (N_018).

## 3. R.2 — removing the denominator: the identity is the moment form (PROVED)
Without dividing by ζ: (1/2π)∫∂_u|Φ(½+iτ,½+σ−iτ)|²dτ = N′(σ), N(σ) := (1/2π)∫|Φ(½+iτ,½+σ−iτ)|²dτ =
‖Σ_m m^{−1/2−σ}φ(·+log m)‖²_{L²(0,∞)} ≥ 0 (Plancherel; differentiation under ∫ justified for σ > −½ by dominated
convergence, Σ_n n^{−1/2−σ}log n·O(n^{−3/2})). Hence
  𝔔 = (1/2π)∫Θ_∞|F|²dτ + N′(0) + 2AB,
which is memo Q's Π = −N′(0) together with F.1. So R.1 is the moment form with the Θ_∞ term absorbed by dividing by ζ:
**reformulation, REF-D level.** Note the version "M(σ) := ∫|ζ(½+iτ)|²|Φ/ζ|²(½+σ−iτ)dτ, 𝔔 = M′(0) + 2AB" is NOT available:
M(σ) for σ ≠ 0 needs ζ ≠ 0 off the line (forbidden); only the pointwise form R.1 is used.

## 4. R.3 — no pointwise / monotonicity sign (NO-GO, PROVED)
Pointwise, |ζ|²∂_u|h|² = |F|²[Θ_∞ − 2Re(F_log/F)]. Take ρ ≠ 0 supported in (1,X₀], X₀ ≤ 2: F_log ≡ 0, F = R, integrand
Θ_∞|R|², negative on |τ| < τ₀ = 6.2898 (Θ_∞(0) = −5.37) wherever R ≠ 0 — while 𝔔 ≥ 0 there (F Prop F.5; CITED Zhu Thm
1.2 / Paper 46 thm:log5W). So any argument "∂_u|h|² ≥ 0 pointwise (or on a τ-set of full measure)" is impossible, even on
the data where positivity holds; the pole term 2AB and the τ-integration are indispensable. **NO-GO for the class
𝒦_R^{pt} = {pointwise u-monotonicity of |Φ/ζ| on the line, with or without the |ζ|² weight}.**
Deep subclass (supp ρ ⊂ (X₀,∞)): R.2 gives N′(0) = −Π ≈ −2Dρ₀² and 2AB ≈ +2Dρ₀² (F Prop F.4); the leading terms cancel and
the O(1) remainder is J Thm J.3's (2+γ−log 4π)B_φ²e^D (PROVED there). The identity reproduces J.3; it adds no
mechanism. Leading term in μ: none extracted (ARGUED: the μ-dependence is entirely in the data class, F.0).

## 5. R.4 — Q(G,G) ⪯ 0 in this language (OPEN; heuristic ARGUED)
G = F − F₀ ⇒ Φ_G(s,w) = Φ − ζ(w)R(s) = −∫ρX^{−s}T_X(w)dX, T_X := ζ − ζ_X (analytically continued tail; F Lemma 3.1:
T_X(w) = −X^{1−w}/(1−w) + {X}X^{−w} − w∫_X^∞{t}t^{−w−1}dt), and h_G = h − R. By R.1,
  Q(G,G) = (1/2π)∫[∂_u|Φ_G|² + Θ_∞|Φ_G|²](w = 1−s)dτ,
so "Q(G,G) ≤ 0" says: on the tail, the u-decay rate of |Φ_G|² beats Θ_∞. **Stationary phase (ARGUED).** The sawtooth
part −Σ_{k≠0}∫_X^∞e^{2πikt}t^{−w}dt at w = ½−iτ has stationary point t* = τ/(2πk) (needs t* > X), contributing
∝ t*^{−w}; its u-log-derivative is −2log t*, and Θ_∞(τ) = log(τ/2π) + O(τ^{−2}). Diagonal weight per harmonic:
  Θ_∞ − 2log t* = 2log k − log(τ/2π),
negative iff k < √(τ/2π), i.e. iff the dual length t* exceeds the AFE (Hardy–Littlewood) symmetry point √(τ/2π). So the
numerical finding P.4 is consistent with "most of the tail mass sits at dual lengths above √(τ/2π)", but harmonics with
√(τ/2π) < k < τ/(2πX) enter positively, and cross terms k ≠ k′ and the polar mode (X^{1−w}/(1−w), whose u-derivative
is (−log X + Re 1/(1−w))·|·|²) are not controlled. **Not proved; no inequality derivable from FE + partial-sum structure
alone was found.** The residual, in this language:
  **(★★_R)** (1/2π)∫|ζ|²∂_u|Φ_ρ/ζ|²(1−s)dτ + 2AB ≥ κμ^{−A}dist²(ρ,𝒢̄₁) on PW_μ,
equivalently −Q(G,G) + 2Q(F,G) + 2AB ≥ … (memo P), with −Q(G,G) read as the excess of tail u-decay over Θ_∞ at dual lengths
beyond the AFE point. Restatement of (★★_P)/(★★_Q), OPEN.

## 6. Labels
PROVED: R.0 (premise false; F_log = ∂_sF + F_L), R.1 and R.1′ (w-derivative identity, one-line Q(F₀,F₀) = 0), R.2 (moment
form, interchange justified), R.3 NO-GO 𝒦_R^{pt}, cΛ/Beurling bookkeeping. CITED: Zhu Thm 1.2 / Paper 46 thm:log5W
(shallow positivity), J Thm J.3. ARGUED: §5 stationary-phase weights 2log k − log(τ/2π). OPEN: (★★_R) = L′♯.
**Do not retry:** σ-derivative identities in the Mellin variable for 𝔔 (wrong derivative, R.0); pointwise monotonicity of
|Φ/ζ| or |F/ζ| on the line (R.3); "M(σ) = ∫|ζ|²|Φ/ζ|²(½+σ)" (needs off-line zero information). No sign claimed. Row D OPEN.
