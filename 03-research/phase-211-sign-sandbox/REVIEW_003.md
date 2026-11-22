# Review 003 — ROUND_002_D, ROUND_002_E, ROUND_002_A, ROUND_002_B, ROUND_003_B

Reference objects: STATEMENT_001.md and Paper 46 (04-papers/46-row-d-dual-certificates/main.tex). The statement (★) is
treated only through the definitions of STATEMENT_001 and its internal rewritings (§5 there); no equivalence with any other
statement is used. Verdicts: CONFIRMED (key step named) / REFUTED / DOWNGRADE. Line numbers refer to the memo under review.

## 1. ROUND_002_D — Theorem 1, Corollaries 2–3

Real or complex. P_T is the complex space {F ∈ L²(I_T; ℂ) : A(F) = B(F) = 0} (STATEMENT_001 l.9–15: conj F, complex
autocorrelation; A, B are ℂ-linear). D_T (l.3) is a complex subspace. Arch is Hermitian; Π(F) = Σ v_n Re c_F(log n) =
Σ v_n Re⟨F(·)…⟩ is the quadratic form of the self-adjoint operator ½Σ v_n(S_{log n} + S_{log n}*), S_u the translation, hence
Hermitian. So the restriction to a 2-dimensional complex V is a pair of 2×2 Hermitian matrices and Toeplitz–Hausdorff
applies (l.144–148). The objection "joint range of two real forms on ℝ² is not convex" does not apply. Remark: even if one
insisted on real F, the conclusion would survive by applying Brickman's theorem (image of the unit sphere of ℝ^n, n ≥ 3, under
two real quadratic forms is convex) to a 3-dimensional real span containing F_1, F_2 (P_T is infinite dimensional); the memo
should cite this as the real-case alternative, but nothing is lost.

(i) Convexity. CONFIRMED. Key step: reduction to span(F_1, F_2) and Toeplitz–Hausdorff on ℂ²; only finiteness of Arch on D_T used.
(ii) Π takes both signs. CONFIRMED. Key steps checked: ε < log(3/2) excludes the lag log 3; ε < 2T − log 2 puts J and J + log 2
in I_T; A(G(· − log 2)) = √2·A(G), B(G(· − log 2)) = B(G)/√2; c_{F_θ}(log 2) = e^{iθ}‖G‖² with the convention
c_F(u) = ∫F(t) conj F(t − u) dt (the memo's "e^{∓iθ}" hedge at l.156 is harmless: only cos θ enters).
(iii) Finiteness, concavity, attainment, max_c Φ_T = Θ_T. CONFIRMED. Key steps: Φ_T ≥ λ_arch − |c|π_T needs λ_arch(T) > −∞,
true since m is bounded below (Paper 46 lem:mbounds); Φ_T → −∞ at ±∞ from (ii); a finite concave function on ℝ tending to
−∞ at both ends attains its maximum. The separation argument (l.164–168) is correct: β = 0 forces αp ≥ γ ≥ 0 on W_T,
contradicting (ii); β > 0 gives Φ_T(−α/β) ≥ θ. Θ_T < ∞ is correctly obtained from convexity (segment meets p = 0).
(iv) J_T closed bounded interval; non-empty iff Θ_T ≥ 0. CONFIRMED (superlevel set of a continuous concave function tending to
−∞; non-emptiness uses that the max is attained, so Θ_T = 0 gives J_T = {c*_T} ≠ ∅).
(v) Scaling identities and the empty comb. CONFIRMED (immediate).

Corollary 2. CONFIRMED, with the input λ_arch(T) < 0 for T ≥ 0.60 CITED from Paper 46 (not re-proved in the memo; label
should read PROVED given the CITED input). "Θ_T = λ_A(T) iff 1 is a maximiser" is correct.
Corollary 3(a),(b). CONFIRMED (key step: inf(X − Y) ≥ inf X − sup|Y|). The remark that π_T grows makes (b) useless as a route
is accurate.
Paragraph l.189–193 ("Π(F*) = 0 iff c*_T = 1"). DOWNGRADE. The direction Π(F*) = 0 ⟹ 1 is a maximiser is correct (0 is a
supergradient). The converse "c*_T = 1 ⟹ Π(F*) = 0 for some minimiser" requires that the superdifferential at c = 1 be the
convex hull of {−Π(F) : F minimiser}, i.e. Danskin's theorem, valid when the bottom is an isolated eigenvalue of finite
multiplicity; it is false for a fixed computed minimiser when the bottom is degenerate. ROUND_002_E §2 (l.46–51) already
corrects this; the corrected statement (0 ∈ range of Π on the bottom eigenspace) is CONDITIONAL on the isolated-eigenvalue
property, which is CITED (compact-resolvent part) rather than proved here.
The "Why not in the index" (l.56–60) is accurate: the dual (joint-range) statement does give a lower-bound formula. But
Theorem 1(iv) shows that (I.a) is exactly the residue "∃c with λ_A(T; cΛ) ≥ 0" already recorded (D_∃c); the novelty is a
formula for that residue, not a new residue. Correctly stated at l.65 and l.213.
No NO-GO is declared in this memo. Falsifier test: (a) carried out (Theorem 1(v)); (b) carried out only for P > e^{2T}
(depends on the CITED sign of λ_arch); (b) for P ≤ e^{2T}, (c), (d) not carried out (OPEN, correctly labelled).

## 2. ROUND_002_E — Lemmas 1–3, Corollary 4, the correction, and the Galerkin method

Lemma 1. CONFIRMED. Key step: with x_0 the smallest position carrying weight, ε below x_0 and below the gap to the other
positions, c_{F_θ} meets the positions only at x_0 (l.21–25). Note the translate must satisfy J + x_0 ⊂ I_T, which needs
x_0 + ε < 2T: stated.
Lemma 2. CONFIRMED. Key steps: Ψ_T is an infimum of affine functions of w, 1-Lipschitz in ‖·‖_1 because |Re c_F(x)| ≤ ‖F‖²;
boundedness of 𝒦_T by a finite cover of the unit sphere of 𝒲 with test vectors F having Π_w(F) ≥ δ > 0 (Lemma 1 plus
continuity in w). 𝒦_T may be empty (it does not contain 0 when λ_arch(T) < 0); the statement holds with that reading. The
identity Θ_T(w) = max_c Ψ_T(cw) requires Theorem 1 of ROUND_002_D for a general w; its proof uses only (ii) for w, which Lemma 1
supplies. Correct.
Lemma 3. CONFIRMED. Key step: Θ_T(w′) = max_c Ψ_T(cw′) ≥ Ψ_T(c*w′) ≥ Ψ_T(c*w) − |c*|‖w − w′‖_1. (Holds also for w′ = 0.)
Corollary 4. First sentence CONFIRMED (strict inequality keeps Θ_T(w′) > 0). The clause "then Θ_T(Λ) ≥ λ_A(T) ≥ 0 forces
λ_A(T) = Θ_T(Λ) = 0 under (★)" (l.42) is CONDITIONAL on (★) and must be labelled so; it is not PROVED. Scope: "finite
modification" here means a change of weights at fixed positions (or adding a position with small weight); a Beurling shift of
positions (comb (f)) is not covered by the ℓ¹ Lipschitz bound, since moving a position is not a small ℓ¹ change of w.
Correction to Corollary 3 (l.46–51). DOWNGRADE to CONDITIONAL: correct for finite-dimensional pencils (Danskin, CITED); on S_T
it holds when the bottom of Arch − Π on P_T is an isolated eigenvalue of finite multiplicity, which the memo assumes and does
not prove. In the Galerkin model it is exact.

Galerkin methodology (l.60–66). The claim "Θ^{(N)} ≥ Θ_T, so a negative Θ^{(N)} proves Θ_T < 0" is TRUE but the justification
written is incomplete, and the direction of the inequality is the delicate point.
- Weak duality on V gives only max_μ λ_min((Arch − μΠ)|_V) ≤ Θ_V := inf{Arch(F) : F ∈ V, ‖F‖ = 1, Π(F) = 0}. Combined with
  Θ_T ≤ Θ_V (V ⊂ S_T) this yields no comparison between the computed quantity and Θ_T: a negative max_μ λ_min would bound Θ_V
  from below, which is useless.
- What is needed is strong duality on V: max_μ λ_min(Arch − μΠ)|_V = Θ_V. On the complexification V_ℂ this is exactly
  ROUND_002_D Theorem 1(iii) applied in finite dimension (Toeplitz–Hausdorff, CITED), provided Π is indefinite on V_ℂ (if Π is
  semidefinite on V the maximum becomes a supremum approached as μ → ∓∞ and the identity still holds). The sine basis is
  real and the matrices are real symmetric; λ_min is the same over ℝ^N and ℂ^N, and Θ over V_ℂ is ≤ Θ over V_ℝ. The chain
  Θ_T ≤ Θ_{V_ℂ} = max_μ λ_min holds. On the real span the S-lemma also holds for dim ≥ 3 (Brickman), so either route works.
  The memo must state this step; as written (l.64) it reads as if inclusion alone sufficed.
- The computed number is λ_min at the numerically found μ̂, which is ≤ the true max. A negative computed value therefore does
  NOT by itself show max_μ λ_min < 0: a rigorous upper bound needs either a certified maximisation (concavity in μ makes
  Brent reliable, but a certificate is a supergradient sign change bracket) or, better, a primal witness: an explicit
  F ∈ V_ℂ with Π(F) = 0 and Arch(F) < 0. Recommended: report the witness eigenvector pair and its exact Π-null combination.
- Tate constraints: imposed as the null space of a 2 × N matrix computed by 800-point Gauss–Legendre (l.61–62); A(φ_k),
  B(φ_k) have closed forms. The constraints are therefore exact to quadrature precision, not exactly; the trial space lies at
  distance O(10⁻¹⁵) from P_T. On a finite span this perturbs Θ^{(N)} by an amount controlled by ‖Arch|_V‖·10⁻¹⁵, negligible
  against the reported margins, but "exactly" (l.61) should read "to quadrature precision".
- Monotonicity check passed: every table row is non-increasing in N (nested sine spaces, nested null spaces), e.g. T₁ (e)
  +0.0020 → −0.0024 → −0.00486, log 2 (d, η = −0.5) +0.0074 → −0.0102 → −0.0186.
Verdict on l.115–116: DOWNGRADE "rigorous up to rounding" to NUMERICAL (non-certified upper bounds). The sign pattern is
credible (margins 0.005–0.42 vs quadrature 10⁻⁹), except the two smallest entries (T₁ (e) −0.00486, unstable at N = 20) which
need a primal witness before being quoted.

NO-GO / PIVOT. No NO-GO declared; the PIVOT (l.131–134) is correctly argued from Lemma 3 and Corollary 4 (PROVED parts) plus
NUMERICAL tables. Falsifier test: carried out numerically for (b) deletion, (c) deletion, (d) both signs, (e) swap, (f) Beurling
shift, at three windows; status NUMERICAL as above.

## 3. ROUND_002_A — Lemma P, Theorem F, Propositions S, L, M, Corollaries F1, M1–M3

Lemma P (l.46–50). CONFIRMED. Key step: Σ = ⟨x, u + v⟩ ≤ ‖u + v‖ and |⟨Px, Qx⟩| = |⟨Px, PQ·Qx⟩| ≤ ‖PQ‖‖u‖‖v‖ ≤ ½‖PQ‖Σ, so
Σ² ≤ (1 + ‖PQ‖)Σ. Sharpness remark correct.
Theorem F (l.52–70). CONFIRMED, conditional on the input from ROUND_001_C (coordinates c_j, H real unitary, ‖c‖ = ‖F‖,
2a_T = Σ s_{2j}|c_j|² + Σ s_{2l+1}|(Hc)_l|² absolutely convergent on 𝒟_T), which is cited, not re-proved. Key steps checked:
layer cake s = ∫_0^∞ 1[s > t]dt with Tonelli (all terms ≥ 0 on 𝒩_η^⊥); integrand = 2‖c‖² − ‖P′_t c‖² − ‖H*Q′_tHc‖²;
‖P′_t H*Q′_t H‖ = ‖Q′_t H P′_t‖ = ‖G_t‖ with (H)_{lj} = h_{l−j}; ν_t ≤ 2 since ‖G_t‖ ≤ 1. Monotonicity of ν_t (growing index
sets, growing submatrix norm) gives the partition bound. c_floor ≥ c_*: integrand 2 below min(s^e_+, s^o_+), ≥ 1 up to the
max: ½(2·min + (max − min)) = ½(s^e_+ + s^o_+). "Strict gain" (l.56) should read "gain ≥"; it is strict only if ‖G_t‖ < 1 on a
set of positive measure above the max. Finiteness of c_floor is automatic (a_T(F) < ∞ on 𝒟_T).
Corollary F1. CONFIRMED: |h_{l−j}| = 2/(π|2(l−j)+1|) = 2/(π|k_o − k_e|), Schur test.
Proposition S (l.99–105). CONFIRMED, conditional on ROUND_001_C Theorem 1 (P_T ∩ 𝒟_T = N′ ⊕ 𝒞 and the Schur reduction).
Key step: a_T(x + y) ≥ a_T(x) − 2‖b‖‖y‖ + c‖y‖² ≥ a_T(x) − ‖b‖²/c, minimised in ‖y‖.
Proposition L (l.107–114). CONFIRMED. (i) c ↦ c⁻¹ decreasing; (ii) S(x) = a_T(x) − ⟨b, A_𝒞𝒞⁻¹b⟩ and
⟨b, A_𝒞𝒞⁻¹b⟩ ≤ C⁻¹‖b‖². Requires b = P_𝒞Ax ∈ L², i.e. x in the form domain with Ax in the dual: holds for x ∈ N′ (finite
span of mode vectors) as in ROUND_001_C.
NO-GO (class: floor-only Schur inequalities). Status NUMERICAL, not PROVED: the class bound (Proposition L) is PROVED but the
failure is shown at two windows only by a truncated model (l.117–122). Direction check: the compression's λ_min(A_𝒞𝒞) is an
upper estimate of the true λ_min, and truncating the coupling B lowers BBᵀ and hence lowers c_need; so true c_need ≥ 2.10 >
1.11 ≥ true λ_min at ½log5 + 10⁻⁴. Both truncation errors go in the direction favourable to the NO-GO: the numerical NO-GO is
robust. Falsifier test for the class: correctly declared not applicable (§5, l.168–173): the class contains no sign step.
Proposition M (l.131–136). CONFIRMED, with the notation remark that s_T here includes r_T(τ) = ∫_{2T}^∞ cos(τu)K(u)du
(ROUND_001_C l.6), which differs from STATEMENT_001 l.13; |r_T| ≤ ε_T. Key step: cos(πk x_n) = 1 − 2 sin²(πk log n/4T) and
4‖y‖² ≤ sin²(πy) ≤ π²‖y‖².
Corollary M1. CONFIRMED (uses −r_T ≤ ε_T and r_T ≤ ε_T in the two directions; lem:mbounds CITED).
Corollary M2. CONFIRMED (the term k log n log n′/4T cancels). The two numerical examples at l.149–150 are WRONG in value or
sign: at T = ½log5 + 10⁻⁴, k = 158 gives q_2 = 34, q_3 = 54 and log(3^34/2^54) = −0.0771 (memo: −0.15); k = 144 gives
q_2 = 31, q_3 = 49 and log(3^31/2^49) = +0.0928 (memo: e^{−0.09}). The identity and the bound |δ_3| log 2 + |δ_2| log 3 = 0.077
are consistent with the corrected values; nothing else depends on them.
Corollary M3. Correctly labelled mixed (PROVED part from F + M; quantitative separation ARGUED). Fine.
Section 1 corrections (l.25–37) are NUMERICAL and not re-checked here.

## 4. ROUND_002_B — Lemma 1.1, Proposition 1.2, Theorems 2.1, 2.2, Proposition 2.3, Theorem 3.1

Conventions against Paper 46. def:ext (main.tex l.9867–9902) defines 𝒲[Ψ] = (1/2π)∫m|Ψ̂|² − Σ_{n≥2} v_n c_Ψ(log n)
+ 2A(Ψ)B(Ψ), v_n = 2Λ(n)/√n, over all n. The memo's 𝒫_w = Σ_q 2w(q)q^{−1/2}⟨Ψ̌, Ψ̌(· + log q)⟩ (l.69) equals Σ_q v^w_q c_Ψ̌(log q)
by translation invariance, so it matches def:ext. The phrase "comb 2w(q)q^{−1/2} at ±log q" (l.9) is ambiguous: with weight
2w(q)q^{−1/2} at both ±log q the comb would be doubled; Paper 46 lem:ext-cell(ii) (l.10276) writes w(q)q^{−1/2}(δ_{log q} +
δ_{−log q}). The formula actually used (l.69) is the correct one; fix the wording at l.9. Consistency check: on a single cell
[J, J+1] the memo's 𝒟_w gives 2‖ϱ‖²Σ_{n≤J}W(n)/n, exactly lem:ext-cell(ii).

Lemma 1.1. CONFIRMED. Key step: for y > 0, Ψ̌(y + log q) = Σ_l l^{−1/2}u_{lq}(y), then n = lq and Σ_{q|n, q≥2} w(q) = W(n)
(W(1) = 0). Affinity in W: the form is linear in w by definition and w ↦ W = w∗1 is a linear bijection, so "affine in W" is
immediate; the emphatic reading at l.18–19 ("no non-linearity in w can occur in any expansion") is a tautology of the
definition, not a finding. Convergence: from ϱ = O(X^{−2}), ‖u_m‖² = ∫_{t>m}|ϱ|² = O(m^{−3}), so the pair terms are
O((mn)^{−2}W(n)) — better than the stated (mn)^{−1} (l.77). The claim "W(n) ≪ n^ε under the hypothesis" (l.77–78) does not
follow from convergence of Σ w(n)n^{−σ}, σ > 1 (that gives w(n) ≪ n^{1+ε}); but the absolute convergence needed,
Σ W(n)n^{−2} < ∞, does follow (Σ W(n)n^{−s} = ζ(s)Σ w(n)n^{−s}, s = 2). Minor; conclusion stands.
Proposition 1.2. (a) CONFIRMED: ‖u_m‖² = ∫_{t>m}|ϱ|², so the diagonal is 2∫|ϱ|²H₁^w; H₁^w ≥ 0, linear in w. (b) CONFIRMED.
Key step: with α ⊂ (s₀, s₀+ε) ⊂ (1, 2) and β ⊂ (ns₀, n(s₀+ε)), α/m′ ⊂ (0,1) for m′ ≥ 2 so α only enters u_1, the β-dilates are
mutually disjoint, and the only overlap is u_1 (α part) with u_n (β part); ℬ_n[α ± β] = ±2∫α(s)β(ns)ds·(Jacobian). (c)
CONFIRMED in the form: 𝔔^w − 𝔔^{w′} = 𝒟_{w′−w} + 𝒪_{w′−w}, so a failure of monotonicity on given data is a failure of
𝒪_{w′−w} ≥ −𝒟_{w′−w} there (the memo's "failure of 𝒪_w to be semidefinite" should be stated for the difference weight).
Theorem 2.1. CONFIRMED. Key step: Gram matrix of ϱ_{4j}/√d_{4j} in L²((1,∞), 4H₁^w dt); normalisation checked (b_j scaling).
Theorem 2.2. ARGUED as labelled. The algebra (iv)–(v) and the formula for 𝐆(n) are CONFIRMED: diagonal (4/π)arcsin(1/n),
off-diagonal −sin(4d·arcsec n)/(πd), 𝐆(n) ⪰ 0 as a Gram matrix on (arcsec n, π/2). The gap (ii) is real, and the validation
§4(ii) is poor: (4,12) gives 0.006 against 0.227, (0,4) 0.609 against 0.492 (l.248–249). This is not "good for low orders"
for (0,4); the limit formula is not validated.
Proposition 2.3. ARGUED as labelled (remainder in thm:ext-layer(iv) open; thm:ext-multi does not cover prolate tails, as the
memo says, cf. main.tex l.10411–10446 which requires a fixed cut X and amplitudes vanishing at integers).
§2.4 and "𝐓₀ ⪰ I". The matrix statement 𝐓₀ − I = Toeplitz[(2/π)(H∘sec − 1)] ⪰ 0 is CONFIRMED ((2/π)∫_0^{π/2}cos 4dθ dθ = δ_{d0},
H ≥ 1). Its identification as the leading form log N·𝐓₀ of 𝒩^w is ARGUED (depends on the operator form of lem:ext-osc for
truncated dilates). The "Correction to K3" is therefore ARGUED, not PROVED; consistent with Paper 46 thm:ext-multi, which
gives only the lower bound log 2N.
Theorem 3.1. (a) CONFIRMED but it is a decomposition, not a monotonicity statement. (b) The monotonicity of Q₁ in w: DOWNGRADE
to CONDITIONAL on Theorem 2.2, Proposition 2.3 and the §2.4 expansion (all ARGUED); the memo conditions only on 2.3 (l.183,
l.275). At each finite N the coherent part is monotone (PROVED by Theorem 2.1); the passage to "Q₁" needs the expansion.
(c) CONFIRMED given (b): |κ_d(n)| ≤ 4 arcsin(1/n)/π ≤ 2/n via |sin(4d(π/2 − α))| = |sin 4dα| ≤ 4dα.

NO-GO (class: comb-monotone, bounded-linear dependence of the exterior form on the bulk prolate sector). DOWNGRADE to ARGUED
NO-GO. (1) It rests on Theorem 2.2, Proposition 2.3 and §2.4, all ARGUED; 𝐄 is not computed. (2) It is an asymptotic
statement as N = e^{2T} → ∞ at fixed K: at a fixed window the terms o(1) and N^{−1/2}log N are not small, so the NO-GO says
nothing about any fixed T. (3) The c > 1 clause of 3.2(a) (l.196–197) uses boundedness of 𝐄, not shown. Falsifier test:
carried out by argument only (no numerics on the full sector form, l.253); §4(i) checks only the PSD ordering of 𝐃^w_∞.
The conclusion of §3.3 (sign step on the sector is comb-generic at orders log N and 1; Λ-specificity sits in localisation) is
ARGUED, and is a reasonable reading.

## 5. ROUND_003_B — Propositions 1, 5, Lemma 2, Theorems 3–4

Proposition 1 (l.22–24). CONFIRMED. Key step: 𝕂_t ⪰ 0 because δ(m,k) = Σ_p |v_p(m) − v_p(k)| log p is an ℓ¹ distance on
exponent vectors, hence conditionally negative definite, and Schoenberg gives e^{−tδ} ⪰ 0; Schur product. The equivalence
with 𝔸_M ⪰ 0 is trivial in the (⇐) direction (𝕏 = 0), as the memo says.
Lemma 2 (l.27–29). CONFIRMED. Key step: 𝔸_{mm} = β = 𝕏_{mm} + ℝ_{mm} with ℝ_{mm} ≥ 0 gives 0 ≤ 𝕏_{mm} ≤ β, then
|𝕏_{mk}| ≤ β and multiply by 𝕂_{mk}. The reading l.30–33 is correct in substance; note that "near-coincident pairs have δ
large" holds because for a non-divisor pair m/k = m′/k′ in lowest terms with m′, k′ ≥ 2, so lcm/gcd = m′k′ ≥ 6.
β > 0 (l.5): uses λ_A(T_0) > 0 strictly (CITED); the numerics give β > 0 directly. Fine.
Theorem 3 (l.37–41). CONFIRMED. Key step: the 2×2 minor on {k, k+1}: 𝕏_{kk} = β − r_k, 𝕏_{k,k+1} = B(log(1+1/k))(k(k+1))^t,
det ≤ β² − (β²/4)(k(k+1))^{2t} ≤ β² − (β²/4)k^{4t} < 0 for large k; if r_k > β the diagonal is already negative. Continuity of B
at 0 is correct (finitely many comb terms near d = 0; archimedean part continuous). Numerics: profile T_0 = 0.15 (a = 0.075),
not the a = 0.15 profile of STATEMENT_001 §3; this is declared (l.3, l.49) but β = 1.5905 is in a different normalisation from
STATEMENT_001's B(0) = 0.01492; the memo says so (l.44). Validation only.
Theorem 4 (l.46–50). CONFIRMED in its key step (a real symmetric PSD matrix with zero diagonal vanishes; the diagonal of
Near^{comb} is zero because c_0(± log n) = 0 for log n ≥ log 2 > 2T_0). Gap: "Near^{comb}_M ≠ 0 as soon as M ≥ 4" requires
the entry (4,1), which collects c_0(log 3 − log 4)v_3 and c_0(log 5 − log 4)v_5 (both lags inside (−2T_0, 2T_0) = (−0.3, 0.3))
plus possibly others, to be non-zero; c_0 is the autocorrelation of F_0 = (¼ − ∂²)G_0 and is not sign-definite, so a
cancellation is not excluded by the memo. The NO-GO only needs Near^{comb}_M ≠ 0 for some M, which holds because the lags
log(m/k) are dense and c_0 is a non-zero continuous function on (−2T_0, 2T_0) (choose a lag hitting a single n where
c_0 ≠ 0). DOWNGRADE "M ≥ 4" to "some M" unless the (4,1) entry is computed.
Remark l.52–54: the Schur-test bound Σ_k(gcd(m,k)²/(mk))^t ≤ σ_{−t}(m)ζ(t) ≤ ζ(t)² (t > 1) is CONFIRMED (write k = gk′,
m = gm′, coprime m′, k′); the surrounding "(★) restricted to near pairs plus a bounded perturbation" is ARGUED.
Proposition 5 (l.58–64). CONFIRMED. Key steps: 𝕂_{t+s} = 𝕂_t ∘ 𝕂_s and Schur give an up-set; closedness of the PSD cone gives
[t*_M, ∞); t → ∞ gives βI since δ ≥ log 2 off the diagonal; 𝕂_0 = J gives t*_M = 0 ⟺ 𝔸_M ⪰ 0. "(★) ⟺ t*_M = 0 ∀M" goes
through prop:AM, an internal rewriting permitted by STATEMENT_001 §5 (requires 2T_0 < log 2, satisfied).

NO-GO. Declared class (l.76–77): "Schur factorisations 𝔸_M = 𝕏 ∘ 𝕂_t + ℝ and the dual suppression". DOWNGRADE the scope: by
Proposition 1 the class contains 𝕏 = 0, ℝ = 𝔸_M, which succeeds exactly when 𝔸_M ⪰ 0; the class as stated cannot be NO-GO.
What is PROVED is: NO-GO for the diagonal-remainder prescription (Theorem 3), NO-GO for the Div/Near prescription (Theorem 4,
with the "some M" correction), the restatement (Propositions 1, 5), and the structural constraint of Lemma 2. Falsifier test
(§5): carried out by argument, correctly; the negative statements are comb-uniform, which is the right conclusion.

## 6. Summary

| memo | item | verdict |
|---|---|---|
| 002_D | Thm 1 (i)–(v), Cor 2, Cor 3(a)(b) | CONFIRMED (complex space; Toeplitz–Hausdorff applies; Brickman covers the real case) |
| 002_D | "Π(F*) = 0 iff c* = 1" (l.189–193) | DOWNGRADE to CONDITIONAL (isolated bottom), superseded by 002_E |
| 002_E | Lemmas 1–3, Cor 4 first part | CONFIRMED |
| 002_E | Cor 4 "λ_A = Θ = 0" clause | DOWNGRADE to CONDITIONAL on (★) |
| 002_E | Galerkin "rigorous up to rounding" | DOWNGRADE to NUMERICAL; direction correct only via strong duality on V_ℂ (to be stated); needs certified max or primal Π-null witness; Tate constraints to quadrature precision |
| 002_A | Lemma P, Thm F, F1, S, L, M, M1, M2 | CONFIRMED (F, S, L conditional on ROUND_001_C inputs); M2 examples numerically wrong |
| 002_A | NO-GO floor-only Schur | NUMERICAL NO-GO, robust in direction |
| 002_B | Lemma 1.1, Prop 1.2, Thm 2.1, 𝐓₀ ⪰ I, Thm 3.1(c) | CONFIRMED (wording fix l.9; convergence remark) |
| 002_B | Thm 3.1(b), NO-GO | DOWNGRADE: CONDITIONAL on 2.2, 2.3, §2.4; NO-GO ARGUED and asymptotic in N only |
| 003_B | Props 1, 5, Lemma 2, Thm 3 | CONFIRMED |
| 003_B | Thm 4 | CONFIRMED with "M ≥ 4" → "some M" |
| 003_B | class NO-GO | DOWNGRADE scope to the two prescriptions |

NO-GO list. (1) 002_A floor-only Schur inequalities (I_c): NUMERICAL, falsifier test not applicable (no sign content).
(2) 002_B comb-monotone exterior sector: ARGUED, asymptotic; falsifier test by argument only. (3) 003_B diagonal-remainder
and Div/Near Schur prescriptions: PROVED; falsifier test by argument (comb-uniform). (4) 003_B dual suppression 𝔸_M ∘ 𝕂_t as
a transfer mechanism: PROVED (restatement); falsifier test by argument. 002_D, 002_E declare no NO-GO (002_E: PIVOT).
