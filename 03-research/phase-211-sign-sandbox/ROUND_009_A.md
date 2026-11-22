# Round 009 A — The tapered prolate leakage bound: proof of Lemma 3.4 of ROUND_008_E (in a mollified form)

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). This memo proves an UPPER bound only; no sign is claimed anywhere.
Notation of ROUND_008_E and Paper 46 §sec:ext: λ = e^T, N = λ², c = 2πN, ℱf(ξ) = ∫f(x)e^{−2πixξ}dx; P_T, a_T, W_T, λ_A,
λ_W, E (summation map), 𝒞_T, 𝒜⁺_T, L₁, L₂ as in ROUND_008_E §3. Prolates: for a parameter c > 0, φ_k = φ_k(·; c) is the
k-th prolate spheroidal wave function, real, of parity (−1)^k, normalised by ∫_{−1}^{1}φ_k² = 1, with
    ∫_{−1}^{1} φ_k(t) e^{−icxt} dt = α_k φ_k(x)   (x ∈ ℝ),    |α_k|² = 2πχ_k/c,                                   (0.1)
χ_k = χ_k(c) ∈ (0, 1) the concentrations (eigenvalues of time-and-band limiting), 1 > χ_0 > χ_1 > …, and φ_k solves
    ((1 − t²)φ′)′ + (ϑ_k − c²t²)φ = 0   on ℝ,                                                                        (0.2)
with ϑ_0 < ϑ_1 < … the Sturm–Liouville eigenvalues (written ϑ_k to avoid a clash with the concentrations). Labels:
PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check

Searched: ROUND_008_E (Lemma 3.4, Cor. 3.5 and the "Argument and what is missing" paragraph), ROUTES-TRIED-INDEX README
row P211-8E and table rows C21, 05b row L106 (prolate clusters), Paper 46 §sec:ext (def:ext, lem:ext-mob, thm:ext-half,
prop:ext-consol(b), the closing list "Scale"), cor:margin1, lem:contA; tools/prolate_*.py.
What is on record. Lemma 3.4 was ARGUED with a taper η_λ of width 1/λ and left open: uniform edge bounds for φ_j^{(i)} on
[1 − 1/N, 1], the out-of-band tail of the tapered product, the denominator near u = 0. Nothing in the index proves a
weighted out-of-band bound for an explicit admissible prolate family. The upper bound with doubly exponential rate for
λ_W is CITED in the record (Mori, with zero data); for λ_A only cor:margin1 (single-exponential, 4·10⁹Te^{−15.449T}).
What differs here. (i) The taper is replaced by a dilation plus a convolution: the prolates are taken on the slightly
shorter interval [−a, a], a = λ − ε, with the band enlarged to b = λ²/a so that the prolate parameter stays exactly
c = 2πab = 2πN (no loss of the defect 1 − χ_k(c) by a shift of c), and then mollified at scale ε = θλ^{−3}, matched to
the edge scale 1/c² of the prolates in the normalised variable (the taper width 1/λ of ROUND_008_E is λ² times too wide;
this is the reason the taper argument could not close: on a layer of width 1/λ the prolate grows like e^{√(πc/2)} into
the band, a super-polynomial factor). (ii) All prolate input is reduced to two ODE facts proved here from (0.2) (a
Liouville-type monotone energy on t > 1 and a Grönwall bound on a sliver t ∈ [1 − 1/(2c²), 1]), plus the classical
identities (0.1). No asymptotic formula for 1 − χ_k is used anywhere in a proof (the Fuchs/Slepian asymptotic is off by
a factor ≈ 7 for the ratio (1 − χ_8)/(1 − χ_0) at c = 6π; the statements below are in terms of the exact 1 − χ_k(c)).
(iii) The test space is not a span of tapered prolates with cross terms to control: the numerator is bounded for the
whole span at once by a pointwise bound on ℱu and Cauchy–Schwarz on the coefficients (no orthogonality needed), and
the denominator uses only the exact orthogonality of the φ_k on [−1, 1] (double orthogonality on the band). No
equivalence of (★) with another statement is used; no zero data are used.


## 1. The test family

Fix d ∈ {3, 5}, K_d := {0, 2, …, 2d − 2}, and put
    θ := 1/(48π²),   ε := θλ^{−3},   a := λ − ε,   b := λ²/a,   δ := ε/λ = θ/N²,   so ab = N, c = 2πab = 2πN,     (1.1)
and δ = δ₀ := 1/(12c²) exactly. Mollifier: ρ(u) := (35/32)(1 − u²)³ on [−1, 1], 0 outside; ρ ≥ 0, even, ∫ρ = 1,
ρ ∈ C²(ℝ) (triple zero at ±1), ρ_ε(u) := ε^{−1}ρ(u/ε). For a = (a_k)_{k∈K_d} ∈ ℝ^d put
    g_a(x) := Σ_k a_k φ_k(x/a) 1_{[−a,a]}(x),     f_a := g_a ∗ ρ_ε,     V_d := {f_a : a ∈ ℝ^d}.
(i) V_d ⊂ 𝒞_T (PROVED). f_a is even (g_a and ρ even); supp f_a ⊂ [−a − ε, a + ε] = [−λ, λ]; f_a^{(j)} = g_a ∗ ρ_ε^{(j)},
j ≤ 2, continuous; f_a^{(j)}(λ) = ∫ g_a(λ − y)ρ_ε^{(j)}(y)dy = 0 for j = 0, 1 because g_a(λ − y) ≠ 0 forces y ≥ ε.
(ii) Fourier side (PROVED from (0.1)): substituting x = at, ℱg_a(ξ) = a∫_{−1}^{1}Σa_kφ_k(t)e^{−2πiaξt}dt and 2πaξ = c·(ξ/b), so
    ℱf_a(ξ) = a ρ̂(εξ) Φ_a(ξ/b),    Φ_a := Σ_k a_k α_k φ_k,    ρ̂(y) = ∫ρ(u)cos(2πuy)du.                              (1.2)
(For k even α_k is real.) Hence for f = f_a, r(ξ) = aρ̂(εξ)Φ_a(ξ/b) on ξ > λ, and ξ/b > λ/b = a/λ = 1 − δ.
(iii) dim V_d = d and V_d ∩ {f : f|_{[1/λ,λ]} = 0} = {0} (PROVED, with Titchmarsh's convolution theorem, CITED). If
a ≠ 0, Σa_kφ_k is a nonzero real-analytic function on [−1, 1], so the convex hull of supp g_a is [−a, a]; by Titchmarsh
the convex hull of supp(g_a ∗ ρ_ε) is [−a, a] + [−ε, ε] = [−λ, λ]. An even f_a vanishing on [1/λ, λ] would be supported in
[−1/λ, 1/λ]; contradiction. In particular a ↦ f_a is injective.

## 2. Prolate input: four elementary bounds

Throughout k ≤ 8 and c ≥ 12 (N ≥ 2). Facts used: (0.1), (0.2) on ℝ for the extension defined by (0.1) (CITED,
Slepian–Pollak 1961), double orthogonality (CITED, ibid.), χ_k decreasing in k, and
(F1) 0 ≤ ϑ_k ≤ k(k + 1) + c² (PROVED: ϑ_k is the k-th min-max value of R(φ) = ∫_{−1}^{1}[(1 − t²)φ′² + c²t²φ²]/∫φ²; on the
span of the Legendre polynomials P_0, …, P_k the first part of R is ≤ k(k + 1) and the second ≤ c²).
(F2) ϑ_k ≥ ϑ_0 ≥ c/8 for c ≥ 6 (PROVED). Let ‖φ‖ = 1, A := ∫(1 − t²)φ′², B := c²∫t²φ², s := (3/(8c))^{1/2} ≤ 1/4. For
|t| ≤ s and any t′ in J := {s ≤ |t′| ≤ 2s}, |φ(t)| ≤ |φ(t′)| + ∫_{−2s}^{2s}|φ′|; squaring, averaging over t′ ∈ J and using
Cauchy–Schwarz, φ(t)² ≤ s^{−1}∫_Jφ² + 8s∫_{|τ|≤2s}φ′². Integrating over |t| ≤ s and using 1 − τ² ≥ 3/4 on |τ| ≤ 2s ≤ ½:
∫_{|t|≤s}φ² ≤ 2∫_Jφ² + (64/3)s²A. Together with ∫_{|t|≥s}φ² ≤ B/(c²s²): 1 ≤ 3B/(c²s²) + (64/3)s²A = (8B + 8A)/c.
(F3) Mass identity (PROVED from (0.1) and Plancherel): ∫_ℝ φ_k² = (2π/c)|α_k|^{−2} = 1/χ_k, so, by parity,
    m_k := ∫_1^∞ φ_k² = (1 − χ_k)/(2χ_k),     |α_k|² m_k = π(1 − χ_k)/c.                                             (2.1)

**Lemma 2.1 (edge sliver; PROVED).** Put Q := 3c² and δ₀ = 1/(12c²) (so Qδ₀ = ¼). Then
    |φ_k(t)| ≤ (4/3)|φ_k(1)|,  |φ_k′(t)| ≤ 4c²|φ_k(1)|   on [1 − δ₀, 1 + δ₀];    |φ_k(t)| ≥ (2/3)|φ_k(1)|  on [1, 1 + δ₀].
*Proof.* Integrating (0.2) from 1 (where (1 − t²)φ′ = 0): (1 − t²)φ′(t) = ∫_t^1(ϑ − c²τ²)φ(τ)dτ. On |τ − 1| ≤ δ₀,
|ϑ − c²τ²| ≤ max(ϑ, c²(1 + δ₀)²) ≤ Q by (F1) (k(k + 1) ≤ 72 ≤ 2c²). Since |t − 1|/|1 − t²| = 1/(1 + t) ≤ 1, |φ′(t)| ≤ QM(t),
M(t) := max of |φ| between t and 1. Then M(t) ≤ |φ(1)| + Qδ₀M(t), so M ≤ (4/3)|φ(1)|, |φ′| ≤ (4/3)Q|φ(1)| = 4c²|φ(1)|, and
for t ∈ [1, 1 + δ₀], |φ(t)| ≥ |φ(1)| − δ₀Q(4/3)|φ(1)| = (2/3)|φ(1)|. ∎

**Lemma 2.2 (edge value and exterior derivative mass; PROVED).**
    φ_k(1)² ≤ 27c² m_k,        ∫_1^∞ φ_k′² ≤ 60c⁴ m_k.
*Proof.* First: m_k ≥ ∫_1^{1+δ₀}φ_k² ≥ (4/9)δ₀φ_k(1)² by Lemma 2.1. Second: on [1, 1 + δ₀], Lemma 2.1 gives
∫φ′² ≤ δ₀·16c⁴φ(1)² ≤ 36c⁴m_k. On [1, X], multiply ((x² − 1)φ′)′ = (ϑ − c²x²)φ by x^{−2}φ and integrate by parts; the
boundary term (1 − X^{−2})φ(X)φ′(X) → 0 as X → ∞ because φ = O(1/x) and φ′ = O(1/x) (both are finite Fourier transforms
of C¹ functions on [−1, 1], by (0.1) and its derivative). With D := ∫_1^∞(1 − x^{−2})φ′²:
    D = ∫_1^∞(c² − ϑx^{−2})φ² + 2∫_1^∞(1 − x^{−2})x^{−1}φφ′ ≤ c²m_k + 2√D√m_k
(ϑ ≥ 0, Cauchy–Schwarz, (1 − x^{−2})x^{−2} ≤ 1). Hence (√D − √m_k)² ≤ (c² + 1)m_k, D ≤ (c + 2)²m_k ≤ 2c²m_k (c ≥ 5).
On x ≥ 1 + δ₀, 1 − x^{−2} ≥ δ₀ (as δ₀² + δ₀ ≤ 1), so ∫_{1+δ₀}^∞φ′² ≤ D/δ₀ ≤ 24c⁴m_k. Sum: 60c⁴m_k. ∎

**Lemma 2.3 (mass near the origin; PROVED).** For c ≥ 6 and 0 < h ≤ 1/(8√c): ∫_0^h φ_k² ≤ 12h√c.
*Proof.* Sonin function S := φ² + (1 − t²)φ′²/(ϑ − c²t²) on 0 ≤ t < t₁ := √(ϑ/2)/c. With p = 1 − t², q = ϑ − c²t²,
S = φ² + (pφ′)²/(pq) and (pφ′)′ = −qφ give S′ = −(pφ′)²(pq)′/(pq)² ≥ 0, since (pq)′ = −2tq − 2c²tp ≤ 0. So S is
nondecreasing on [0, t₁). On [0, t₁], q ≥ ϑ/2, hence ∫_0^{t₁}S ≤ ½ + (2/ϑ)∫_0^1(1 − t²)φ′² ≤ ½ + (2/ϑ)(ϑ/2) = 3/2 (parity:
∫_0^1(1 − t²)φ′² ≤ ϑ/2 by the Rayleigh identity). By (F2), t₁ ≥ 1/(4√c) ≥ 2h; thus ∫_0^hφ² ≤ hS(h) ≤ h·(3/2)/(t₁ − h) ≤
3h/t₁ ≤ 12h√c. ∎

Lemma 2.1–2.2 close the "uniform edge bounds" item of ROUND_008_E: the edge region of the prolate in the normalised
variable has width 1/c² and is controlled by one Grönwall step; the edge value is controlled by the exact exterior mass
(2.1) (no use of the Slepian edge identity or of any asymptotic).

## 3. Proof of Lemma 3.4 (mollified form)

**Lemma 3.4′ (weighted leakage of the mollified self-dual prolate block; PROVED, with Landau's plunge bound CITED).**
Let d ∈ {3, 5}, D_d := 1 − χ_{2d−2}(2πN), and N ≥ N₀ := 1.6·10⁶. For every 0 ≠ f ∈ V_d,
    (L₁(f)² + L₂(f)²)/‖f|_{[1/λ,λ]}‖² ≤ C_d N⁹ D_d,        C_5 = 1.3·10¹⁶,  C_3 = 8·10¹⁵.
For 3 ≤ N ≤ N₀ the same holds with b = 9 and some finite constant C_d(N₀) (PROVED as an existence statement, §3.5).

Write ‖a‖² = Σa_k². Constants of ρ (PROVED: |y^jρ̂^{(i)}(y)| ≤ (2π)^{i−j}‖∂^j(u^iρ)‖_{L¹}, exact L¹ norms
‖ρ′‖₁ = 35/16, ‖ρ″‖₁ = 84√5/25, ‖(uρ)″‖₁ = 565/112): M_{j,i} := sup_y |y|^j|ρ̂^{(i)}(y)|² satisfy M_{2,0} ≤ 0.1213,
M_{4,0} ≤ 0.0363, M_{4,1} ≤ 0.645. For every s > 0, j ≥ 0: s^j|ρ̂^{(i)}(εbs)|² ≤ (εb)^{−j}M_{j,i}.

**3.1 Exterior integrals of Φ_a (PROVED).** Let I₀ := ∫_{1−δ}^∞ Φ_a², I₁ := ∫_{1−δ}^∞ Φ_a′². By Cauchy–Schwarz on the
coefficients (no orthogonality used), Lemma 2.1–2.2 and (2.1), with |α_k|²φ_k(1)² ≤ (2πχ_k/c)·27c²(1 − χ_k)/(2χ_k) =
27πc(1 − χ_k) ≤ 27πcD_d:
  sliver [1 − δ, 1]: Φ_a² ≤ (16/9)‖a‖²Σ|α_k|²φ_k(1)² ≤ 48πc d D_d‖a‖², Φ_a′² ≤ 16c⁴·27πc d D_d‖a‖²; times δ = 1/(12c²);
  exterior (1, ∞): ∫Φ_a² ≤ ‖a‖²Σ|α_k|²m_k ≤ πdD_d‖a‖²/c, ∫Φ_a′² ≤ ‖a‖²Σ|α_k|²·60c⁴m_k ≤ 60πc³dD_d‖a‖².
Hence I₀ ≤ 5πdD_d‖a‖²/c and I₁ ≤ 96πc³dD_d‖a‖². (The cross-term gap of REVIEW_006 does not arise: the coefficient
Cauchy–Schwarz costs the factor d and nothing else.)

**3.2 Numerator (PROVED).** From (1.2), with ξ = bs:
L₁² = a²b³∫_{1−δ}^∞ s²ρ̂(εbs)²Φ_a² ≤ a²bε^{−2}M_{2,0}I₀;
r′(ξ) = aερ̂′(εξ)Φ_a(ξ/b) + (a/b)ρ̂(εξ)Φ_a′(ξ/b), so L₂² ≤ 2a²bε^{−2}M_{4,1}I₀ + 2a²b^{−1}ε^{−4}M_{4,0}I₁.
Using ab = N, a/b ≤ 1, c = 2πN, ε^{−1} = θ^{−1}λ³: a²bε^{−2}·5πdD_d/c = a·(ab)·θ^{−2}λ⁶·5πdD_d/(2πN) = (5/2)a θ^{−2}N³dD_d,
and 2a²b^{−1}ε^{−4}M_{4,0}·96πc³dD_d = 192π·a·(a/b)·θ^{−4}λ¹²·8π³N³·M_{4,0}dD_d ≤ 1536π⁴ a θ^{−4}N⁹M_{4,0}dD_d. Hence
    L₁² + L₂² ≤ a·dD_d‖a‖²[(5/2)θ^{−2}N³(M_{2,0} + 2M_{4,1}) + 1536π⁴θ^{−4}N⁹M_{4,0}].                             (3.1)

**3.3 Denominator (PROVED; uses χ_{2d−2}(2πN) ≥ ½, CITED: Landau 1993, χ_k(c) ≥ ½ for k ≤ ⌊2c/π⌋ − 1 = 4N − 1).**
(a) Whole line: ‖f_a‖² = ∫|ℱg_a|²ρ̂(εξ)² ≥ (1 − 2π²(εb)²)²a²b∫_{−1}^{1}Φ_a², because ρ̂(y) ≥ 1 − 2π²y²∫u²ρ ≥ 1 − 2π²y² ≥ 0 on
|y| ≤ εb. Double orthogonality on [−1, 1]: ∫_{−1}^1Φ_a² = Σa_k²|α_k|² = (2π/c)Σa_k²χ_k ≥ (π/c)‖a‖². With εb ≤ 2θ/N
(tiny): ‖f_a‖² ≥ 0.99·a‖a‖²/2.
(b) Near the origin: by Jensen (ρ_ε a probability density) f_a² ≤ g_a² ∗ ρ_ε, so ∫_{|x|<1/λ}f_a² ≤ ∫_{|x|<1/λ+ε}g_a² =
a∫_{|t|<h}(Σa_kφ_k)², h := (1/λ + ε)/a ≤ 1.01/N. For N ≥ 400, h ≤ 1/(8√c), and Lemma 2.3 with Cauchy–Schwarz gives
≤ a·d‖a‖²·24h√c ≤ 61·a d N^{−1/2}‖a‖².
(c) f_a even: ‖f_a|_{[1/λ,λ]}‖² = ½(‖f_a‖² − ∫_{|x|<1/λ}f_a²). For N ≥ N₀, 61dN^{−1/2} ≤ 0.25, so ‖f_a|‖² ≥ ½(0.495 − 0.25)a‖a‖², hence
    ‖f_a|_{[1/λ,λ]}‖² ≥ a‖a‖²/9.                                                                                    (3.2)

**3.4 Conclusion for N ≥ N₀.** Dividing (3.1) by (3.2): the quotient is ≤ 9dD_d[(5/2)θ^{−2}N³(M_{2,0} + 2M_{4,1})
+ 1536π⁴θ^{−4}N⁹M_{4,0}]. Numerically (exact arithmetic of the displayed constants, θ^{−1} = 48π²): the N⁹ coefficient is
1.229·10¹⁶ (d = 5), 7.37·10¹⁵ (d = 3); the N³ coefficient is 3.6·10⁷ (d = 5), ≤ 10⁻²⁰ of the first after N³ ≤ N⁹N₀^{−6}.
This gives C_5 = 1.3·10¹⁶, C_3 = 8·10¹⁵, b = 9. ∎

**3.5 The range 3 ≤ N ≤ N₀ (PROVED, existence only).** On the compact set [3, N₀] × S^{d−1}, the numerator and denominator
of the quotient are continuous in (N, a) (prolates depend continuously on c; CITED, Slepian–Pollak; all other data in
(1.1) are continuous in N), the denominator is positive by §1(iii), and D_d(N) > 0 is continuous. Hence
sup quotient/(N⁹D_d) < ∞ on that range. No explicit value is claimed; the explicit constants need N ≥ N₀ only because
Lemma 2.3 is a crude N^{−1/2} bound (a sup-norm bound of order c^{1/4} for low prolates would lower N₀ to O(1)).

## 4. Consequence: the unconditional (given thm:ext-half) upper bounds

**Corollary 4.1 (PROVED, given thm:ext-half; no sign).** With K the constant of ROUND_008_E Theorem 3.1,
    λ_A(T) ≤ 4K·C_5·N⁹(1 − χ_8(2πN)),        λ_W(T) ≤ 4K·C_3·N⁹(1 − χ_4(2πN))
for N = e^{2T} ≥ N₀ with the explicit C_d of Lemma 3.4′, and with some finite constant for 3 ≤ N ≤ N₀.
*Proof.* Proposition 3.3 of ROUND_008_E with V = V_5 (resp. V_3): V ⊂ 𝒞_T and V ∩ {f|_{[1/λ,λ]} = 0} = {0} by §1, dim V = d;
bound the max quotient by Lemma 3.4′. ∎
Remarks. (i) This replaces Corollary 3.5 of ROUND_008_E (which was CONDITIONAL): its first inequality is now PROVED with
b = 9; the second inequality there (comparison with 1 − χ_0) used the Fuchs ratio and is NOT reproved here — REVIEW_006
showed the asymptotic ratio is off by ≈ 7 at c = 6π; any comparison with 1 − χ_0 must use exact or certified values of
1 − χ_k (tools/prolate_defect_k.py), not the asymptotic. (ii) b = 9 is far above the measured exponent of the
sharp law (λ_A ≈ κ₈(1 − χ_8), κ₈ bounded, ROUND_008_E §1); the loss comes from cutting the weight ξ⁴ of L₂ at the
mollifier scale 1/ε = λ³/θ (factor ε^{−4} = θ^{−4}N⁶) and from the c³ of Lemma 2.2. Decay of the exterior prolate tail
(φ_k′ ~ φ_k(1)/x oscillating) is what forces a cut; b is not optimised. (iii) The λ_W statement inherits the "core vs
form-domain closure" remark of Proposition 3.3(ii). (iv) The taper of ROUND_008_E is abandoned: the taper-derivative cost
gap of REVIEW_006 is avoided because the mollifier acts multiplicatively on the Fourier side ((1.2)) and its scale ε is
matched to the edge scale δ₀ = 1/(12c²) of Lemma 2.1 through δ = ε/λ = δ₀.

## 5. Falsifier test (BRIEF rule 4)

Lemma 3.4′ and Lemmas 2.1–2.3 are archimedean statements about prolates and a mollifier; they contain no weight and
survive all four falsifiers, as they must (they are not sign steps). The Λ-dependence of Corollary 4.1 sits entirely in
Theorem 3.1 of ROUND_008_E via thm:ext-half. For w = cΛ, by (5.1) of ROUND_008_E, W^{cΛ}_T(Ef) = 𝒲[Ψ_f] + (1 − c)Π_T(Ef);
on V_5 the first term is ≤ 4KC_5N⁹(1 − χ_8)‖Ef‖²-small while the second is O(|1 − c|)·‖Ef‖² with no small factor, so
Corollary 4.1 does NOT transfer to cΛ: the best one gets is λ_A(T; cΛ) ≤ 4KC_5N⁹(1 − χ_8) + |1 − c|·max_{V_5}|Π_T|/‖·‖²,
consistent with the negative block bottoms on both sides of c = 1 recorded in ROUND_008_E §5. (b) a_P and (d) finite
modifications: same mechanism with 𝒫_{Λ−w}, O(1). (c) Beurling systems: no Poisson summation, no thm:ext-half, no
analogue of Theorem 3.1. No sign is claimed.

## 6. Corrections to the record

- ROUND_008_E Lemma 3.4 (ARGUED, taper of width 1/λ) is superseded by Lemma 3.4′ (mollified, PROVED for N ≥ N₀, existence
  for 3 ≤ N ≤ N₀). The taper version is not proved and is not needed.
- ROUND_008_E Corollary 3.5, first inequality for λ_A and the λ_W inequality: CONDITIONAL → PROVED (given thm:ext-half),
  b = 9. The comparison with 1 − χ_0 via the Fuchs ratio stays withdrawn (REVIEW_006).

## Result

PROVED piece (upper bound only; no sign).

### What was proved
- Lemmas 2.1–2.3 (PROVED, elementary from (0.1)–(0.2)): edge sliver bounds on [1 − 1/(12c²), 1 + 1/(12c²)];
  φ_k(1)² ≤ 27c²m_k and ∫_1^∞φ_k′² ≤ 60c⁴m_k with the exact exterior mass m_k = (1 − χ_k)/(2χ_k); ϑ_k ∈ [c/8, k(k+1) + c²];
  Sonin bound ∫_0^hφ_k² ≤ 12h√c.
- Lemma 3.4′ (PROVED; Landau's plunge bound and Titchmarsh CITED): for the mollified self-dual prolate block V_d
  (prolates on [−a, a], band b = λ²/a so c = 2πN exactly, mollifier scale ε = λ^{−3}/(48π²)), the weighted leakage quotient
  is ≤ C_dN⁹(1 − χ_{2d−2}(2πN)), C_5 = 1.3·10¹⁶, C_3 = 8·10¹⁵, for N ≥ 1.6·10⁶; finite constant for 3 ≤ N ≤ 1.6·10⁶.
- Corollary 4.1 (PROVED given thm:ext-half): λ_A(T) ≤ 4KC_5N⁹(1 − χ_8(2πN)), λ_W(T) ≤ 4KC_3N⁹(1 − χ_4(2πN)).

### What failed and why
- No explicit constant for 3 ≤ N < 1.6·10⁶: Lemma 2.3 (mass near 0) gives only N^{−1/2}·61d decay; an O(c^{1/4}) sup bound
  for φ_k, k ≤ 8, would remove N₀ but was not proved here (not CITED: no verified source at hand).
- Exponent b = 9 is not sharp (mollifier cut of the ξ⁴ weight); the measured law has b ≈ 0 relative to 1 − χ_8.
- Comparison 1 − χ_8 vs 1 − χ_0 not reproved (needs certified values, not the Fuchs asymptotic).

### Next concrete step
Lower N₀ and b: (1) prove sup_{[−1,1]}|φ_k| ≤ C(k)c^{1/4} from the Sonin function S and (F2) (S(0) bounds the interior
maxima; the turning region needs an Airy-scale estimate); (2) replace the cut s⁴ρ̂² ≤ (εb)^{−4}M by the exact 1/s decay of
Φ_a′ (integration by parts in (0.1), boundary term ∝ φ_k(1)), which gains (εb)^{−1} per derivative and should give b ≤ 6.

## §7 Explicit doubly exponential bound

This section makes Corollary 4.1 fully explicit for N ≥ N₀ = 1.6·10⁶: an explicit value of K and a cited
non-asymptotic upper bound for 1 − χ_k(c). No sign is claimed.

**7.1 The cited bound (CITED).** Bonami, Jaming and Karoui, "Non-asymptotic behaviour of the spectrum of the sinc kernel
operator and related applications" (arXiv:1804.01257; J. Math. Phys. 2021), Theorem 3.2 (numbering of the arXiv version):
for every real c > 0 and every integer n with 0 ≤ n ≤ c/2.7,
    λ_n(c) ≥ 1 − (7/√c)·(2c)^n e^{−c}/n!.                                                                          (7.1)
Normalisation check. There λ_n(c) is the (n+1)-th eigenvalue of Q_c f(x) = ∫_{−1}^{1} sin(c(x − y))/(π(x − y)) f(y)dy on
L²(−1, 1), equivalently (their (2.4)) λ_n(c) = ‖𝓕^{−1}[1_{(−1,1)}f]‖²_{L²(−c,c)}/(2π‖f‖²) with the e^{ixt} transform; the
eigenfunctions are the prolates ψ_{n,c} of the operator ((1 − t²)φ′)′ − c²t²φ (their (2.2)–(2.3), eigenvalue bounds identical
to (F1)). This is exactly the concentration χ_n(c) of (0.1)–(2.1): |α_n|² = 2πλ_n/c is the classical relation for the
finite Fourier transform ∫_{−1}^{1}φ_n(t)e^{−icxt}dt with the same c, and indexing starts at n = 0 in both. With c = 2πN,
the hypothesis n ≤ c/2.7 holds for n = 8 when N ≥ 4 and for n = 4 when N ≥ 2, in particular for all N ≥ N₀. Note that (7.1)
has the rate e^{−c}, not the asymptotic rate e^{−2c} of 1 − λ_n(c) ~ 4√π c^{n+1/2}e^{−2c}/n! (their (2.9)); only the
non-asymptotic e^{−c} is used below. Hence, for N ≥ 4, with c = 2πN,
    1 − χ_8(c) ≤ B_8(c) := (7·2⁸/8!)c^{15/2}e^{−c} = (2/45)c^{15/2}e^{−c},
    1 − χ_4(c) ≤ B_4(c) := (7·2⁴/4!)c^{7/2}e^{−c} = (14/3)c^{7/2}e^{−c}.                                          (7.2)

**7.2 The constant K of ROUND_008_E Theorem 3.1 (PROVED).** Only the upper bound m(τ) ≤ log(2 + |τ|) + C_∞ is used,
m(τ) = Re ψ(¼ + iτ/2) − log π.
(i) C_∞ = 1.13 is admissible. From ψ(z) = −γ + Σ_{n≥0}(1/(n + 1) − 1/(n + z)), Re ψ(x + iy) = ψ(x) + S,
S = Σ_{n≥0} y²/((n + x)((n + x)² + y²)). Take x = ¼, Y = |y|. If Y ≥ 1: terms with n + x ≤ Y are ≤ 1/(n + x), summing to
≤ 4 + Σ_{1≤n≤Y}1/n ≤ 5 + log Y; terms with n + x > Y are ≤ Y²(n + x)^{−3}, summing to ≤ Y²(Y^{−3} + ½Y^{−2}) ≤ 1.5; so
S ≤ 6.5 + log Y. If Y < 1: the n = 0 term is ≤ 1/x = 4 and Σ_{n≥1}(n + ¼)^{−3} ≤ 1.2, so S ≤ 5.2. In both cases
S ≤ 6.5 + log(2 + Y). With Y = |τ|/2 ≤ |τ| and ψ(¼) = −γ − π/2 − 3log 2 = −4.2275, log π = 1.1447:
m(τ) ≤ log(2 + |τ|) + 6.5 − 4.2275 − 1.1447 ≤ log(2 + |τ|) + 1.13.
(ii) Archimedean term, step (c) of Theorem 3.1 with constants. With Ψ = Ψ₁ + Je, |Ψ̂|² ≤ 2|Ψ̂₁|² + 2J²|ê|², log(2 + |τ|) ≤ 1 + τ²
and Plancherel (factor 1/2π): (1/2π)∫log(2 + |τ|)|Ψ̂|² ≤ 2(‖Ψ₁‖² + ‖Ψ₁′‖²) + (J²/π)L, L := ∫_ℝ log(2 + |τ|)(1 + τ²)^{−1}dτ.
Since log(2 + |τ|) ≤ log 2 + log(1 + |τ|) and ∫_0^∞ log(1 + t)(1 + t²)^{−1}dt = (π/4)log 2 + G (G Catalan's constant,
classical), L ≤ π log 2 + (π/2)log 2 + 2G ≤ 5.10, L/π ≤ 1.63. With ‖e‖² = ‖e′‖² = ½,
‖Ψ₁‖² + ‖Ψ₁′‖² ≤ 2(‖Ψ‖² + ‖Ψ̌′‖²) + 2J², and J² ≤ 2‖Ψ‖‖Ψ̌′‖ ≤ ‖Ψ‖² + ‖Ψ̌′‖²; hence the archimedean term is
≤ (4 + 4 + 1.63)(‖Ψ‖² + ‖Ψ̌′‖²) + C_∞‖Ψ‖² ≤ 10.76‖Ψ‖² + 9.63‖Ψ̌′‖².
Inserting ‖Ψ‖ ≤ ζ₃L₁/λ and ‖Ψ̌′‖² ≤ ζ₃²(L₁/2 + L₂)²/λ² ≤ ζ₃²(L₁²/2 + 2L₂²)/λ²: archimedean ≤ ζ₃²λ^{−2}(15.58L₁² + 19.26L₂²).
(iii) Comb (d): ≤ 2(−ζ′/ζ)(3/2)ζ₃²L₁²λ^{−2} = 3.011ζ₃²L₁²λ^{−2} ((−ζ′/ζ)(3/2) = 1.50524). Rank two (e): ≤ 2ζ₃²L₁²λ^{−2}.
(iv) Sum: W_T(Ef) ≤ ζ₃²λ^{−2}(20.6L₁² + 19.3L₂²) ≤ 20.6ζ₃²λ^{−2}(L₁² + L₂²). With ζ₃² = ζ(3/2)² = 6.8245:
    K = 141 is admissible in Theorem 3.1 of ROUND_008_E.
(The digits ψ(¼), ζ(3/2), (−ζ′/ζ)(3/2), G are classical values; only upper roundings are used.)

**Corollary 7.1 (explicit doubly exponential upper bounds; PROVED given thm:ext-half and (7.1) CITED; no sign).**
For every T with N = e^{2T} ≥ 1.6·10⁶, with c = 2πN,
    λ_A(T) ≤ 4·141·C_5·N⁹·B_8(2πN) = 564·1.3·10¹⁶·(2/45)(2π)^{15/2} N^{33/2} e^{−2πN} ≤ 3.2·10²³ N^{33/2} e^{−2πe^{2T}},
    λ_W(T) ≤ 4·141·C_3·N⁹·B_4(2πN) = 564·8·10¹⁵·(14/3)(2π)^{7/2} N^{25/2} e^{−2πN} ≤ 1.4·10²² N^{25/2} e^{−2πe^{2T}}.
*Proof.* Corollary 4.1 with K = 141 (§7.2) and (7.2). ∎
Remarks. (i) The rate is e^{−2πe^{2T}}, i.e. half the exponent of the asymptotic rate e^{−4πN}; the factor two is lost
only because the cited non-asymptotic bound (7.1) has e^{−c}; the asymptotic e^{−2c} is not used. (ii) For 3 ≤ N < N₀ the
bound remains existence-only (§3.5), because of C_d, not of K or (7.1). (iii) This supersedes the DOWNGRADE "explicit
constants OPEN" of the doubly exponential reading: the doubly exponential bound is now PROVED with explicit constants
for N ≥ N₀, given thm:ext-half and the cited Theorem 3.2.
