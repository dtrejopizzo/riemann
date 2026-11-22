# Review 007: round 009_A (mollified prolate leakage bound) against ROUND_008_E, REVIEW_006, Paper 46 §sec:ext and prolate theory

Scope. ROUND_009_A read in full, checked line by line against ROUND_008_E (Theorem 3.1, Corollary 3.2, Proposition 3.3),
REVIEW_006 §1, Paper 46 §sec:ext (def:ext, lem:ext-mob, thm:ext-half) and the classical prolate facts (Slepian–Pollak
1961; Landau 1993). Verdicts: CONFIRMED / REFUTED / DOWNGRADE, with the label each claim keeps. The memo claims an upper
bound only; no sign statement is made and none is reviewed. No equivalence of (★) with another statement is used here.

## 1. Conventions and the classical input

(0.1) normalisation. With ∫_{−1}^{1}φ_k(t)e^{−icxt}dt = α_kφ_k(x) and ∫_{−1}^{1}φ_k² = 1, Plancherel gives
∫_ℝ|∫_{−1}^{1}φ e^{−icxt}dt|²dx = (2π/c)∫_{−1}^{1}φ², hence ∫_ℝφ_k² = (2π/c)|α_k|^{−2}; the classical relation between the
integral-operator eigenvalue and the concentration is χ_k = c|α_k|²/(2π). So |α_k|² = 2πχ_k/c is correct, and (F3)
∫_ℝφ_k² = 1/χ_k, m_k = (1 − χ_k)/(2χ_k), |α_k|²m_k = π(1 − χ_k)/c follow. CONFIRMED.

(0.2) sign convention. −((1 − t²)φ′)′ + c²t²φ = ϑφ, so ϑ_k are the min-max values of the Rayleigh quotient written in (F1);
the extension of φ_k to ℝ through (0.1) solves (0.2) on ℝ (the operator commutes with the finite Fourier transform;
CITED, Slepian–Pollak). CONFIRMED.

Landau. The cited statement (Landau, "On the density of phase-space expansions", IEEE Trans. Inf. Theory 39 (1993))
is λ_{⌊2c/π⌋−1}(c) ≥ ½ for the concentration eigenvalues of time-and-band limiting, indices from 0. Normalisation check:
time interval [−a, a] and band [−b, b] in the convention e^{−2πixξ} have time–bandwidth count (2a)(2b) = 4ab = 4N, and
2c/π = 2·2πN/π = 4N; the two counts agree, so χ_k(2πN) ≥ ½ for k ≤ 4N − 1. The memo needs k ≤ 8, i.e. N ≥ 9/4, so N ≥ 3
is inside the cited range. CONFIRMED (CITED). Monotonicity χ_0 > χ_1 > … is classical. CONFIRMED.

Double orthogonality (∫_{−1}^{1}φ_jφ_k = δ_{jk}, orthogonality on ℝ) CITED, correctly used in §3.3(a).

## 2. The construction of V_d (§1)

Parameters. θ = 1/(48π²), ε = θλ^{−3}, a = λ − ε, b = λ²/a: ab = N and c = 2πab = 2πN exactly; δ = ε/λ = θλ^{−4} = θ/N²,
and δ₀ = 1/(12c²) = 1/(48π²N²) = θ/N². So δ = δ₀ exactly. CONFIRMED.

Mollifier. ρ = (35/32)(1 − u²)³: ∫ρ = 1, even, ≥ 0; ρ, ρ′, ρ″ vanish at ±1 (ρ‴ jumps), so ρ ∈ C²(ℝ) and not C³.
CONFIRMED.

(i) V_d ⊂ 𝒞_T. Evenness: K_d consists of even indices, φ_k(·/a)1_{[−a,a]} even, ρ even. Support: [−a − ε, a + ε] =
[−λ, λ]. C²: f^{(j)} = g ∗ ρ_ε^{(j)} for j ≤ 2 with g bounded and ρ_ε^{(j)} continuous, so f ∈ C²(ℝ), in particular C² on
[−λ, λ] as def:ext requires. Edge: f^{(j)}(λ) = ∫g(λ − y)ρ_ε^{(j)}(y)dy; g(λ − y) ≠ 0 needs λ − y < a, i.e. y > ε, outside
supp ρ_ε; hence f(λ) = f′(λ) = 0 (also f″(λ) = 0). This is exactly 𝒞_T of ROUND_008_E §3 (even, C², support, f(λ) =
f′(λ) = 0). The two remaining admissibility conditions f(0) = ℱf(0) = 0 are not properties of V_d and are not claimed;
they are imposed by Proposition 3.3 as linear constraints. CONFIRMED.

(ii) Fourier side (1.2). x = at gives ℱg_a(ξ) = a∫_{−1}^{1}Σa_kφ_k(t)e^{−2πiaξt}dt; with cx′ = 2πaξ, x′ = 2πaξ/(2πab) = ξ/b,
so ℱg_a(ξ) = aΦ_a(ξ/b); ℱρ_ε(ξ) = ρ̂(εξ) (real, even). For ξ > λ, ξ/b > λ/b = a/λ = 1 − δ. α_k real for even k (φ_k even,
real). CONFIRMED.

(iii) Titchmarsh. For a ≠ 0, Σa_kφ_k is real-analytic and nonzero on [−1, 1], so it vanishes only at isolated points and
the closed convex hull of supp g_a is [−a, a]; Titchmarsh–Lions (convex hull of the support of a convolution of compactly
supported distributions is the sum of the hulls; CITED) gives hull supp f_a = [−λ, λ]. An even f_a vanishing on [1/λ, λ]
has support in [−1/λ, 1/λ] ⊊ [−λ, λ] (λ > 1). Contradiction. dim V_d = d by linear independence of the φ_k. CONFIRMED.

## 3. Lemmas of §2

(F1) 0 ≤ ϑ_k ≤ k(k + 1) + c². On span{P_0, …, P_k}, ∫(1 − t²)P_n′P_m′ = n(n + 1)δ_{nm}∫P_n², so the kinetic part is
≤ k(k + 1), the potential part ≤ c²; min-max gives the upper bound; ϑ_k ≥ 0 since both parts are ≥ 0. CONFIRMED.

(F2) ϑ_0 ≥ c/8 for c ≥ 6. s = (3/(8c))^{1/2} ≤ 1/4 for c ≥ 6. Pointwise: φ(t)² ≤ 2φ(t′)² + 2(∫_{−2s}^{2s}|φ′|)² ≤
2φ(t′)² + 8s∫φ′²; averaging over J (measure 2s) gives φ(t)² ≤ s^{−1}∫_Jφ² + 8s∫_{|τ|≤2s}φ′²; integrating over |t| ≤ s
(length 2s) and 1 − τ² ≥ 3/4 gives ∫_{|t|≤s}φ² ≤ 2∫_Jφ² + (64/3)s²A; ∫_{|t|≥s}φ² ≤ B/(c²s²); so
1 ≤ 3B/(c²s²) + (64/3)s²A = (8B + 8A)/c with s² = 3/(8c). Every constant checked. CONFIRMED (crude; ϑ_0 ~ c is true, c/8
is all that is used).

Lemma 2.1 (edge sliver). Integrating (0.2) from t to 1, (1 − t²)φ′(t) = ∫_t^1(ϑ − c²τ²)φ dτ (the boundary term at 1 is
zero because φ is entire). |ϑ − c²τ²| ≤ max(ϑ, c²(1 + δ₀)²) ≤ 3c² uses ϑ ≤ 72 + c² ≤ 3c² (c ≥ 6) and (1 + δ₀)² ≤ 3.
|t − 1|/|1 − t²| = 1/(1 + t) ≤ 1 for t ≥ 0. The self-improving bound M ≤ |φ(1)| + Qδ₀M with Qδ₀ = 3c²/(12c²) = 1/4 is
valid because M(t) is the maximum over the segment and the derivative bound at intermediate points uses a maximum over a
sub-segment, ≤ M(t). Consequences 4/3, 4c², 2/3 follow. CONFIRMED.

Lemma 2.2. m_k ≥ ∫_1^{1+δ₀}φ² ≥ (4/9)δ₀φ(1)² gives φ(1)² ≤ (9/4)(12c²)m_k = 27c²m_k. Sliver derivative mass:
δ₀·16c⁴φ(1)² ≤ (16/12)c²·27c²m_k = 36c⁴m_k. Exterior identity: multiplying ((x² − 1)φ′)′ = (ϑ − c²x²)φ by x^{−2}φ and
integrating by parts on [1, X] gives exactly D = ∫(c² − ϑx^{−2})φ² + 2∫(1 − x^{−2})x^{−1}φφ′ + boundary, with the boundary
term (1 − X^{−2})φ(X)φ′(X) → 0 (φ, φ′ = O(1/x) as Fourier transforms of C¹ functions on [−1, 1] with nonzero endpoint
values). Cauchy–Schwarz with weight (1 − x^{−2}) on φ′ and (1 − x^{−2})x^{−2} ≤ 1 on φ gives D ≤ c²m + 2√(Dm), hence
√D ≤ (1 + √(c² + 1))√m ≤ (c + 2)√m, and (c + 2)² ≤ 2c² for c ≥ 2 + 2√2. On x ≥ 1 + δ₀, 1 − x^{−2} ≥ δ₀ iff δ₀ + δ₀² ≤ 1.
D/δ₀ ≤ 2c²·12c²m = 24c⁴m. Total 60c⁴m_k. CONFIRMED.

Lemma 2.3 (Sonin). With p = 1 − t², q = ϑ − c²t², u = pφ′, u′ = −qφ: (u²/(pq))′ = −2φφ′ − u²(pq)′/(pq)², so
S′ = −u²(pq)′/(pq)² ≥ 0 on 0 ≤ t < t₁ since (pq)′ = −2tq − 2c²tp ≤ 0 there. q ≥ ϑ/2 on [0, t₁]; t₁ ≤ 1 needs ϑ ≤ 2c², true
for c ≥ 12 by (F1) (k(k + 1) ≤ 72 ≤ c²). ∫_0^1φ² = ½ and ∫_0^1(1 − t²)φ′² ≤ ϑ/2 by parity and the Rayleigh identity give
∫_0^{t₁}S ≤ 3/2. φ² ≤ S ≤ S(h) on [0, h] and S(h) ≤ (3/2)/(t₁ − h) ≤ 3/t₁ when h ≤ t₁/2; t₁ = √(ϑ/2)/c ≥ 1/(4√c) by (F2).
Result ∫_0^hφ² ≤ 12h√c. CONFIRMED (needs c ≥ 12 as in the standing assumption of §2, not the "c ≥ 6" of the statement;
DOWNGRADE of the hypothesis wording only: the lemma as written for 6 ≤ c < 12 is not proved by this argument, and it is
used only at c = 2πN ≥ 2π·1.6·10⁶).

## 4. Lemma 3.4′ (§3)

Mollifier constants. |y|^j|ρ̂^{(i)}(y)| ≤ (2π)^{i−j}‖∂^j(u^iρ)‖_{L¹} (j integrations by parts; boundary terms vanish because
u^iρ ∈ C²_c). L¹ norms recomputed by quadrature at 30 digits: ‖ρ′‖₁ = 2.1875 = 35/16; ‖ρ″‖₁ = 7.513188… = 84√5/25 (sign
changes at ±1/√5); ‖(uρ)″‖₁ = 5.044642… = 565/112 (sign changes at 0, ±0.65465). Hence M_{2,0} ≤ (35/(32π))² = 0.1212,
M_{4,0} ≤ (84√5/(100π²))² = 0.03622, M_{4,1} ≤ (565/(224π))² = 0.6446. Scaling s^jρ̂^{(i)}(εbs)² ≤ (εb)^{−j}M_{j,i}. All
CONFIRMED. ∫u²ρ = 1/9 (used as ≤ 1 in §3.3(a)).

§3.1 exterior integrals. Coefficient Cauchy–Schwarz Φ_a(t)² ≤ ‖a‖²Σ_k|α_k|²φ_k(t)² requires no orthogonality and costs
the factor d. |α_k|²φ_k(1)² ≤ (2πχ_k/c)·27c²(1 − χ_k)/(2χ_k) = 27πc(1 − χ_k) ≤ 27πcD_d (χ_k decreasing, k ≤ 2d − 2).
Sliver [1 − δ, 1] (δ = δ₀, so Lemma 2.1 applies on the whole sliver): (16/9)·27 = 48; 48πcdD·δ₀ = 4πdD/c; derivative
16c⁴·27πcdD·δ₀ = 36πc³dD. Exterior: Σ|α_k|²m_k ≤ πdD/c; Σ|α_k|²·60c⁴m_k ≤ 60πc³dD. I₀ ≤ 5πdD_d‖a‖²/c,
I₁ ≤ 96πc³dD_d‖a‖². CONFIRMED. The claim that the REVIEW_006 cross-term gap does not arise is correct: the numerator
bound is a pointwise bound on the whole span, and the denominator uses exact orthogonality of the un-mollified φ_k.

§3.2 numerator. ξ = bs, dξ = b ds: L₁² = a²b³∫s²ρ̂(εbs)²Φ_a² ≤ a²bε^{−2}M_{2,0}I₀. r′ = aερ̂′(εξ)Φ_a(ξ/b) +
(a/b)ρ̂(εξ)Φ_a′(ξ/b); (x + y)² ≤ 2x² + 2y²; the two pieces are ≤ 2a²bε^{−2}M_{4,1}I₀ and 2a²b^{−1}ε^{−4}M_{4,0}I₁. Evaluation:
a²bε^{−2}·5πdD/c = (5/2)aθ^{−2}N³dD (λ⁶ = N³); 2a²b^{−1}ε^{−4}·96πc³M_{4,0}dD = 1536π⁴a(a/b)θ^{−4}N⁹M_{4,0}dD with a/b < 1.
(3.1) CONFIRMED.

§3.3 denominator. (a) ‖f_a‖² ≥ ∫_{|ξ|≤b}a²Φ_a(ξ/b)²ρ̂(εξ)²dξ; cos x ≥ 1 − x²/2 gives ρ̂(y) ≥ 1 − 2π²y²/9 ≥ 1 − 2π²y², ≥ 0
for |y| ≤ εb = θ/(λa) ≤ 2θ/N; double orthogonality ∫_{−1}^{1}Φ_a² = Σa_k²|α_k|² = (2π/c)Σa_k²χ_k ≥ (π/c)‖a‖² by Landau
(CITED; for N ≥ N₀ any lower bound χ_8 ≥ ½ is trivial in practice, but the cited statement is what is used); a²b·π/c
= a/2. ‖f_a‖² ≥ 0.99·a‖a‖²/2. CONFIRMED. (b) Jensen f_a² ≤ g_a² ∗ ρ_ε, Fubini, ∫_{|x|<1/λ}f_a² ≤ a∫_{|t|<h}(Σa_kφ_k)²,
h = (1/λ + ε)/a. Cauchy–Schwarz on the coefficients and Lemma 2.3 (both halves of |t| < h) give a·d‖a‖²·24h√c, and
24·1.01·√(2π) = 60.8 ≤ 61. CONFIRMED with one numerical slip: "for N ≥ 400, h ≤ 1/(8√c)" is false at N = 400
(1.01/400 = 2.525·10⁻³ > 1/(8√(800π)) = 2.494·10⁻³); the correct threshold is N ≥ 410. Without consequence: the step is used
only at N ≥ N₀. (c) Evenness gives ‖f|_{[1/λ,λ]}‖² = ½(‖f‖² − ∫_{|x|<1/λ}f²). At N₀ = 1.6·10⁶, 61·5·N₀^{−1/2} = 0.241 ≤ 0.25,
and ½(0.495 − 0.25) = 0.1225 ≥ 1/9. (3.2) CONFIRMED.

§3.4 constants. θ^{−1} = 48π² = 473.74, θ^{−4} = 5.037·10¹⁰, 1536π⁴ = 1.4962·10⁵; 9d·1536π⁴θ^{−4}M_{4,0} = 1.231·10¹⁶ (d = 5),
7.39·10¹⁵ (d = 3); N³ term 9d(5/2)θ^{−2}(M_{2,0} + 2M_{4,1}) = 3.56·10⁷ (d = 5), negligible relative to the N⁹ term for
N ≥ N₀. C_5 = 1.3·10¹⁶, C_3 = 8·10¹⁵ (exponent 9) CONFIRMED for N ≥ N₀. Notational defect: the letter b denotes both the
band λ²/a and the exponent 9 (§3.4, §3.5, §4 Remark (ii)); this does not affect any inequality but should be fixed.

§3.5 compact range 3 ≤ N ≤ N₀. The question is whether "continuous positive quotient on a compact set" is a valid
existence proof. It is, provided the numerator is continuous in (N, a) — the only point not written out. Check: for k
fixed, ϑ_k(c) is a simple eigenvalue, so φ_k(·; c) (sign fixed by φ_k(1) > 0, say) and α_k(c) depend continuously
(indeed analytically) on c, uniformly for t ∈ [−1, 1]; through (0.1) φ_k(x; c) and φ_k′(x; c) are continuous in c uniformly
on compact x-sets and are O(1/x) uniformly for c in a compact set. The integrands of L₁², L₂² are ξ²|r|², ξ⁴|r′|² with
r = aρ̂(εξ)Φ_a(ξ/b); ρ ∈ C² with a jump of ρ‴ gives ρ̂(y), ρ̂′(y) = O(|y|^{−3}) and therefore an integrable majorant
O(ξ^{−4}) uniform on the compact parameter range; the lower limit λ moves continuously. Dominated convergence gives
continuity of the numerator; the denominator is continuous (all data continuous in N) and positive by §1(iii); D_d(N) is
continuous and positive. The sign ambiguity of φ_k is irrelevant because the supremum over a ∈ S^{d−1} is invariant
under a_k ↦ −a_k. So the existence statement is valid. CONFIRMED as PROVED (existence, non-explicit), with the
continuity of the numerator to be written out as above; it is an existence statement only and carries no quantitative
information below N₀. Note that the compact range also needs N ≥ 2 for Theorem 3.1 of ROUND_008_E (satisfied) and does
not use Lemmas 2.1–2.3 (whose c ≥ 12 hypothesis holds anyway for N ≥ 3).

Verdict on Lemma 3.4′: CONFIRMED, label PROVED (Landau, Titchmarsh, Slepian–Pollak identities CITED), explicit for
N ≥ 1.6·10⁶, existence for 3 ≤ N ≤ 1.6·10⁶.

## 5. Corollary 4.1 and the transfer through Proposition 3.3

Transfer. Proposition 3.3 of ROUND_008_E (CONFIRMED in REVIEW_006) needs only: V ⊂ 𝒞_T linear, dim V ≥ 5 (resp. ≥ 3),
and V ∩ {f|_{[1/λ,λ]} = 0} = {0}. All three hold for V_5 (resp. V_3) by §1(i), (iii). The four functionals f(0), ℱf(0),
A(Ef), B(Ef) are linear and finite on V_5 (A, B by (3.0) of ROUND_008_E, continuous in f|_{[1/λ,λ]}), so a nonzero common
kernel element f exists; it is even, supported in [−λ, λ], C², with f(0) = ℱf(0) = f(λ) = 0, i.e. admissible in the
sense of def:ext (Paper 46 l. 9867ff.), and f′(λ) = 0, i.e. in 𝒜⁺_T. Hence thm:ext-half is used inside its hypotheses, and
Corollary 3.2 applies (f|_{[1/λ,λ]} ≠ 0 by injectivity). The mollification changes nothing in the count: it is applied
before the constraints are imposed, it keeps the space linear of dimension d, and it is what makes the elements C² with
vanishing edge data (the raw prolate span is not in 𝒞_T). The quotient of the kernel element is bounded by the maximum
over V_5, which Lemma 3.4′ bounds. So the 4-constraint count transfers. CONFIRMED.

Theorem 3.1 inputs on V_d. r = O(ξ^{−2}) (f ∈ C², f, f′ vanish at ±λ), ξr ∈ L² and ξ²r′ ∈ L² ((xf)″ ∈ L² needs f′(λ) = 0,
which holds) — CONFIRMED; this is the point REVIEW_006 identified as the reason for 𝒜⁺_T.

λ_W. With Paper 46's definition of λ_W as an infimum over 𝒟_T (REVIEW_006), Ef ∈ 𝒟_T suffices; two constraints on V_3.
CONFIRMED.

Statement. λ_A(T) ≤ 4KC_5N⁹(1 − χ_8(2πN)), λ_W(T) ≤ 4KC_3N⁹(1 − χ_4(2πN)) for N ≥ N₀, and with a finite non-explicit
constant for 3 ≤ N ≤ N₀. CONFIRMED, label PROVED given thm:ext-half (itself given Guo2026 Lemmas 4.2–4.4, Thm 4.5).
Two precisions to the label and to the wording of the brief:
(a) K is the absolute constant of Theorem 3.1, not computed; so even for N ≥ N₀ the bound is explicit only up to K.
(b) The statement is in terms of the exact 1 − χ_k(2πN). The phrase "doubly exponential upper bound" (e^{−4πe^{2T}} up to
polynomial factors) requires an upper bound 1 − χ_k(c) ≤ C_k c^{k+1/2}e^{−2c}; the memo proves none and cites none
(it explicitly avoids the asymptotic). As written, "doubly exponential" is CITED only through the classical asymptotic of
1 − χ_k (Slepian/Fuchs/Widom), which gives the rate but no explicit constant; for an explicit doubly exponential bound a
non-asymptotic estimate (e.g. Bonami–Karoui type bounds) must be cited with its exact statement. DOWNGRADE of the
"doubly exponential" reading to CITED (rate) / OPEN (explicit constants); the inequality in terms of 1 − χ_k stays PROVED.
(c) Relation to the record: the λ_W inequality is now proved without zero data in the same shape as the CITED upper half
of Mori; for λ_A it improves the single-exponential cor:margin1 in rate (given thm:ext-half), with an exponent 9 that is
not sharp (measured κ₈ bounded).

Remark (i) of §4 (Corollary 3.5 of ROUND_008_E: first inequality and λ_W inequality CONDITIONAL → PROVED with exponent 9;
the comparison with 1 − χ_0 stays withdrawn): CONFIRMED. Note that the replacement is of the tapered space by the mollified
space, so what is proved is Corollary 3.5 for V_d, not Lemma 3.4 as stated (taper of width 1/λ); the memo says so in §6.
Lemma 3.4 (taper) remains ARGUED and is no longer needed.

## 6. §5 falsifier paragraph and §0 claims

§5. The Λ-dependence sits in Theorem 3.1 through thm:ext-half (Poisson summation, Λ ∗ 1 = log); identity (5.1) of
ROUND_008_E is tautological (REVIEW_006), so the statement that Corollary 4.1 does not transfer to w = cΛ is the trivial
bound λ_A(T; cΛ) ≤ (bound) + |1 − c|·max|Π_T|/‖·‖² — CONFIRMED as an upper bound, no information on sign. "Consistent with
the negative block bottoms on both sides of c = 1" must be read with REVIEW_006's DOWNGRADE (PROVED for c > 1, NUMERICAL
for c < 1). Beurling systems: no analogue of Theorem 3.1 — ARGUED.

§0. "The taper width 1/λ is λ² times too wide": the edge scale is aδ₀ ≈ λ·θ/N² = θλ^{−3}; ratio (1/λ)/(θλ^{−3}) = λ²/θ.
CONFIRMED up to the constant θ. "Fuchs ratio off by ≈ 7 at c = 6π for k = 8": consistent with REVIEW_006. "No asymptotic
is used in any proof": CONFIRMED (Landau's bound is non-asymptotic).

## 7. Summary of verdicts

CONFIRMED (PROVED): construction of V_d and V_d ⊂ 𝒞_T with all constraints (evenness, C², support [−λ, λ], f(λ) = f′(λ) = 0;
f(0), ℱf(0) imposed later by Proposition 3.3); (1.2); Titchmarsh step and injectivity; (F1), (F2), (F3); Lemmas 2.1, 2.2
with every constant; Lemma 2.3 for c ≥ 12; mollifier constants (L¹ norms recomputed); §3.1 I₀, I₁; (3.1); denominator
via double orthogonality and Landau (CITED, normalisation 2c/π = 4N checked); (3.2); C_5 = 1.3·10¹⁶, C_3 = 8·10¹⁵ for
N ≥ 1.6·10⁶; §3.5 existence on 3 ≤ N ≤ 1.6·10⁶ (continuity of the numerator to be written out, argument supplied in §4);
Corollary 4.1 given thm:ext-half, including the transfer of the four-constraint count to the mollified space.
DOWNGRADE: Lemma 2.3 hypothesis "c ≥ 6" → c ≥ 12 (as used); "N ≥ 400" in §3.3(b) → N ≥ 410 (no consequence); the reading
"unconditional doubly exponential" of Corollary 4.1 → the PROVED statement is in terms of the exact 1 − χ_k(2πN) with
non-computed K; the doubly exponential rate is CITED via the classical asymptotic, explicit constants OPEN.
REFUTED: none.
Editorial: the letter b is used both for the band and for the exponent 9.
No sign is claimed by the memo and none follows from it.
