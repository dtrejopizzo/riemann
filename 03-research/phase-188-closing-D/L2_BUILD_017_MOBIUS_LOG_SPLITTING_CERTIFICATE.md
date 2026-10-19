# L2_BUILD_017 — Conjugated dilation (dead) and a new dual object: Möbius–log splitting certificates

## Corpus check
Conjugated dilation: L2_BUILD_016, lem:contA. Operator form 𝔞_T(F) = 𝔞_∞(F) − 2Re⟨U_μF, U_logF⟩: N_BUILD_002 §1 / N_BUILD_005 §1
(identity Λ = μ*log in shift operators). Paper 47 §3 (primal/dual, measure certificates, non-attainment), §Z (flat-top
certificates = explicit formula), W-lin (fixed-frame linear certificates, R186_026/031), thm:posext / lem:half. grep
"splitting certificate / W^{-1} / AM-GM operator / factorization certificate / U_μ": only G1_B3_R1 (unrelated U_μ dilation
group). No memo uses an operator-valued certificate on the Möbius side. §2–§4 are new.

## 1. Conjugated dilation — dead (PROVED)
To restore the n^{−½} weights after U_k (016) one must multiply the lag variable by e^{(k−1)u/2}, i.e. replace c_F(u) by
e^{(k−1)u/2}c_F(u). (i) This is not the autocorrelation of any function in general: c_{e^{βt}F}(u) = e^{−βu}∫e^{2βt}F(t)F̄(t−u)dt
≠ e^{βu}c_F(u); and e^{β|u|}c_F(u) need not be positive-definite (its transform is |F̂|² convolved with the non-positive
kernel of e^{β|u|}, which is not a positive measure), so positivity of the cone of autocorrelations is not preserved.
(ii) Multiplying F by e^{αt} moves the Tate points ±i/2 to ±i/2 + iα: P_T is not mapped to P_{kT}. Dead.

## 2. The object (definitions)
Shift operators on L²(ℝ), (τ_aF)(t) = F(t − a). For N = e^{2T}:
  U_μ := Σ_{d<N} μ(d)d^{−½} τ_{log d},  U_log := Σ_{m<N} (log m) m^{−½} τ_{−log m}   (finite sums, bounded).
**Lemma 1 (PROVED).** For F ∈ L²(I_T): 2Re⟨U_μF, U_logF⟩ = Σ_{n<N} v_n Re c_F(log n). Hence 𝔞_T(F) = 𝔞_∞(F) − 2Re⟨U_μF, U_logF⟩.
*Proof.* ⟨τ_{log d}F, τ_{−log m}F⟩ = ∫F(t − log d)F̄(t + log m)dt = conj c_F(log dm) (substitute s = t + log m). Sum:
Σ_{d,m} μ(d)(log m)(dm)^{−½}conj c_F(log dm) = Σ_n (μ*log)(n)n^{−½}conj c_F(log n) (terms with dm ≥ N vanish since
c_F = 0 on [2T,∞), and d, m ≤ dm), and μ*log = Λ. Take 2Re. ∎
**Definition (Möbius–log splitting certificate).** A pair (θ, W) with θ > 0 and W a bounded positive invertible operator on
L²(ℝ) is a certificate at T if, for all F ∈ P_T ∩ D_T,
  (C_T)  𝔞_∞(F) ≥ θ⟨W U_μF, U_μF⟩ + θ^{−1}⟨W^{−1}U_logF, U_logF⟩.
(θ can be absorbed in W; kept for readability.) The certificate lives on the Möbius side: W is a metric in which the
Möbius-transported vector U_μF is measured, its inverse metric measures the logarithm side.

## 3. Basic properties (PROVED unless marked)
(P1) Sufficiency: (C_T) ⟹ λ_A(T) ≥ 0. *Proof.* 2|Re⟨a,b⟩| = 2|Re⟨W^{½}a, W^{−½}b⟩| ≤ ⟨Wa,a⟩ + ⟨W^{−1}b,b⟩ (θ = 1 after scaling),
so 𝔞_T(F) = 𝔞_∞(F) − 2Re⟨U_μF,U_logF⟩ ≥ 0. ∎ Strict version gives λ_A > 0.
(P2) Pointwise tightness: for fixed F with Re⟨U_μF, U_logF⟩ > 0 there is W ≻ 0 with equality in the AM–GM step: choose W with
W(U_μF) = U_logF (possible iff ⟨U_μF, U_logF⟩ > 0, e.g. a rank-two perturbation of the identity on span{U_μF, U_logF}).
So the only loss is the uniformity of W over F.
(P3) Scaling invariance: (W, θ) ↦ (cW, θ/c) leaves (C_T) invariant; the certificate class is a convex cone in the
parametrization (W, W^{−1}) ↦ … only after the substitution S = θW: the map S ↦ ⟨SU_μF,U_μF⟩ + ⟨S^{−1}U_logF,U_logF⟩ is convex in S
(operator convexity of S ↦ S^{−1}, CITED), so the set of certificates {S ≻ 0 : (C_T) holds} is convex. Finding one is a convex
(semidefinite) feasibility problem.
(P4) Prop 0 robustness (013): the certificate does not use a split of 𝔞_∞; it uses 𝔞_∞ whole. Moving a positive-definite kernel k
between 𝔞_∞ and the comb changes U_log/U_μ (the comb is no longer μ*log), so the object is tied to the exact factorization
Λ = μ*log: not subject to the redistribution of 013 Prop 0.
(P5) Necessity: OPEN. Precisely: in finite dimensions, given A ⪰ 0 and X, Y with A − X*Y − Y*X ⪰ 0, does there exist S ≻ 0 with
A ⪰ X*SX + Y*S^{−1}Y? (Here A = 𝔞_∞|P_T, X = U_μ, Y = U_log compressed.) For scalar X, Y (1-dimensional range) yes
(S = |y|/|x|); for general X, Y I have neither proof nor counterexample. If necessity holds, (L2) at T ⟺ existence of a
Möbius-side metric S — a genuinely new dual formulation.

## 4. Test against the input map (011)
- Epstein/DH: no factorization Λ_E = μ_E * log over ℕ with Euler structure (coefficients of −E′/E not of the form μ*log with
  μ multiplicative): U_μ is not defined in the same way; the object does not apply. ✓
- a_P: Λ_P = μ_P * log_P with μ_P = μ·1_{P-rough}, log_P = log·1_{P-rough}: the object IS defined for a_P, and a_P fails
  WP_T (0.60 ≤ T ≤ ½log P), so for a_P no certificate exists there (P1 contrapositive). Discrimination happens in the
  certificate, which must depend on the coefficient-1 structure of U_log (all n, not only P-rough). ✓ (as a requirement)
- Beurling: shifts by log of non-integers; U_μ, U_log defined on a different lattice; same remark as a_P.
- M_m: no μ*log factorization (form object only). ✓
- Linear in window data? (C_T) is quadratic in the operators U_μ, U_log and involves S^{−1}: non-linear in Λ's factors. ✓
- Barriers: not a fixed-frame norm bound (S is optimized, operator-valued: escapes W-lin/thm:posext as stated, which fix the
  frame); not a determinant/moment (W-det, W-mom); uses the full symbol (not W-loc). If (P5) fails, the certificate class may
  be strictly smaller than positivity — then it would be a new barrier-type class; this must be settled before use.

## 5. Review
- Lemma 1 is the corpus operator identity (N_BUILD_002/005), restated with explicit shifts: PROVED, not new.
- (P1) trivial (AM–GM with a metric). (P2) correct. (P3) operator convexity of the inverse is standard (CITED) — so the
  feasibility problem is convex; convexity is a real structural gain over the non-convex search for a minimizer.
- (P4) correct but should not be oversold: other factorizations Λ = α*β (e.g. α = Λ, β = δ₁) give other splittings;
  Λ = μ*log is singled out only by the requirement to use ℤ-integrality (log of all integers).
- (P5) is the crux — settled NEGATIVELY in §6 (addendum). Warning: the classical analogue (a matrix A ⪰ X*Y + Y*X ⟹ factorization) can fail when X*Y is not
  "aligned" — I suspect necessity fails in general and holds only up to a constant; then (C_T) would be a lossy class like W-lin.
  Next: settle (P5) for 2×2 blocks with 2-dimensional ranges by hand.
- No sign certified; no negative value of 𝔞_T.

## 6. Addendum (same day): the certificate class is EMPTY for T ≥ 0.60 — NO-GO (PROVED)
The right side of (C_T) is a sum of two nonnegative terms, so (C_T) forces 𝔞_∞(F) ≥ 0 on P_T, i.e. λ_{∞,P}(T) ≥ 0. By cor:Tarch
(CITED) λ_{∞,P}(T) < 0 for T ≥ 0.60, hence no certificate exists at any window of the (L2) range T > ½log5. ∎
This settles (P5) negatively in the strongest way, and an explicit finite-dimensional counterexample shows the same mechanism
abstractly: X = I, Y = J (J = J* , J² = I, J ≠ ±I, P := (I+J)/2), A = 2P: then A − X*Y − Y*X = 2P − 2J = 2(I−P) ⪰ 0, but for v with
Jv = −v, ⟨(S + JS^{−1}J)v,v⟩ = ⟨Sv,v⟩ + ⟨S^{−1}v,v⟩ ≥ 2 > 0 = ⟨Av,v⟩ for every S ≻ 0. (Same with A = 2P + εI, ε < 2.)
Reason: AM–GM bounds |cross term| from above; past 0.60 the sign needs the prime cross term to be POSITIVE energy
(−2Re⟨U_μF,U_logF⟩ > 0 on the archimedean-negative cone, 006/007), which no upper bound of its modulus can supply. Keeping
the square, 𝔞_T = 𝔞_∞ − ⟨SU_μF,U_μF⟩ − ⟨S^{−1}U_logF,U_logF⟩ + ‖S^{½}U_μF − S^{−½}U_logF‖², is a tautology for every S.
Verdict: the splitting certificate is dead. Lesson recorded for the next object: any certificate must produce a LOWER bound
of the signed cross term −2Re⟨U_μF, U_logF⟩ on the archimedean-negative cone 𝒩_T, i.e. an alignment statement
(U_μF and U_logF point in opposite directions there), not a modulus bound.
