# R186.010 — Proof of (TC_S): ϑ(g)Q₁Q₂ is Hilbert–Schmidt

Model and notation of R186.009 (L²(ℝ₊,du), P = 1_{(0,λ]}, F_S = F_∞U, U = e^{iφ(D)}, Q₁ = 1−P, Q₂ = 1−F_SPF_S).
## Status

| # | Statement | Label |
|---|---|---|
| R | F_∞ = I·m_∞(D), I the unitary inversion ξ(u) ↦ u⁻¹ξ(1/u), m_∞ a unimodular multiplier (local Tate factor) | PROVED (structure) + CITED (explicit form of m_∞) |
| S | For g ∈ C_c^∞(ℝ*₊) (or 𝒮(ℝ*₊)): ĝ·m_∞·U ∈ 𝒮(ℝ) | PROVED, using CC Prop. 1.5(iv) (ĝ m_∞ ∈ 𝒮) CITED |
| K | **Exact formula**: ϑ(g)Q₁Q₂ = I·[C_g + 1_{t<−a} K_g(D) 1_{t>a}]·M(D)^* I, with a = log λ, M = m_∞U, K_g = (g̃^∧)·M ∈ 𝒮, C_g = [ĝ̃(D), 1_{t<−a}] M(D)1_{t>a} | PROVED |
| **TC_S** | ϑ(g)Q₁Q₂ is Hilbert–Schmidt, with ‖·‖²_HS ≤ 2∫|k_g(x)|²|x|dx + 2∫|𝒦_g(x)|²(−2a−x)_+dx < ∞ | **PROVED** (CITED only CC Prop. 1.5(iv)) |
| TC′ | ϑ(f)Q₁Q₂Q₁ is trace class for f ∈ C_c^∞(ℝ*₊); Son_S(g) < ∞ and d_S(g*g^*) < ∞ | PROVED (Dixmier–Malliavin CITED to pass from f = g₁*g₂ to general f) |
| H_g | The reduction of R186.009 §4 to "H_g(μ) = o(μ)" is **unnecessary**: it was a loss from the triangle inequality over translates; the multiplier U is absorbed into the symbol | PROVED (remark) |
| (84)_S | Son_S = W_∞ − (prime comb of 2) + ∫f(ρ⁻¹)ε'_S d*ρ | CONDITIONAL **only** on (CV_S) (previously: TC_S and CV_S) |
| CV_S / B | Convergence/boundedness of ε_S = Σλ_n(1−λ_n²)^{−1/2}⟨ξ_n|ϑ(ρ⁻¹)ζ_n⟩ | OPEN (next memo) |

**Verdict.** (TC_S) is PROVED. The argument does not go through the archimedean bound H_g(μ) = o(μ): after conjugating by the inversion I, Q₁Q₂ is exactly "half-line · unimodular multiplier · complementary half-line" with symbol M = m_∞U, and U, being a geometrically convergent Fourier series, only multiplies the Schwartz symbol ĝ m_∞ by a C^∞ function with all derivatives bounded. The semilocal case is literally the archimedean one with a different Schwartz symbol.

## 1. Logarithmic variable and the inversion (R: PROVED)

W: L²(ℝ₊,du) → L²(ℝ,dt), (Wξ)(t) = e^{t/2}ξ(e^t), unitary. Then Wϑ(ρ)W⁻¹ = T_{log ρ} (translation), ϑ(g) = ∫g(ρ)ϑ(ρ)d*ρ ↦ convolution by k_g(x) := g(e^x) ∈ C_c^∞(ℝ), i.e. ϑ(g) = ĝ(D) with ĝ ∈ 𝒮 (Paley–Wiener). P ↦ 1_{t≤a}, a = log λ. The inversion I, (Iξ)(u) = u⁻¹ξ(1/u), is unitary, I² = 1, and W I W⁻¹ is the reflection t ↦ −t; hence Iϑ(ρ)I = ϑ(ρ⁻¹), I1_{t≤b}I = 1_{t≥−b}, Iĝ(D)I = ĝ̃(D) with g̃(ρ) = g(ρ⁻¹).
Since F_∞ϑ(ρ)F_∞ = ϑ(ρ⁻¹) (R186.009 L0), IF_∞ commutes with all translations; it is unitary, hence IF_∞ = m_∞(D) with |m_∞| = 1 (the commutant of the translations = multipliers). Thus F_∞ = I m_∞(D), and m_∞ is the Tate gamma quotient on the critical line (CITED; CC §1, Prop. 1.5). With Thm C (R186.008): F_S = F_∞U = I M(D), M := m_∞U, |M| = 1.

## 2. Exact formula for Q₁Q₂ (K: PROVED)

Q₂ = 1 − F_SPF_S. Since F_S = IM(D) is an involution (L0): F_S = F_S^* = M(D)^*I, hence F_SPF_S = I M 1_{t≤a} M^* I and, by unitarity of M(D), 1 − M1_{t≤a}M^* = M 1_{t>a} M^*:
 Q₂ = I M(D) 1_{t>a} M(D)^* I.
Q₁ = 1_{t>a} = I 1_{t<−a} I. Hence
 **Q₁Q₂ = I · 1_{t<−a} M(D) 1_{t>a} M(D)^* · I.** (2.1)
(Case S = ∅, U = 1: this is the archimedean structure of CC (43); the two half-lines (−∞,−a) and (a,∞) are separated if λ > 1 and overlap in (a,−a) if λ < 1.)

## 3. Symbol lemma (S: PROVED)

(i) U ∈ C_b^∞(ℝ): by R186.008 §4, U(s) = Σ_n u_n e^{inc s}, c = log 2, with u_1 = −q, u_n = q^{−n}(1−q²) (n ≤ 0), q = 2^{−1/2}, u_n = 0 if n ≥ 2. Σ_n |n|^j|u_n| < ∞ ∀j, hence ‖U^{(j)}‖_∞ ≤ c^jΣ|n|^j|u_n| < ∞. (Equivalently U(s) = (1−q e^{ics})^{-1}·(…), a quotient of two absolutely convergent series with no zeros, R186.094.) For a general finite S the product of the factors p ∈ S has the same property.
(ii) For h ∈ 𝒮(ℝ*₊): ĥ m_∞ ∈ 𝒮(ℝ) — CC Prop. 1.5(iv) (proof of that proposition, via Stirling for the derivatives of m_∞, polynomial growth). CITED.
(iii) 𝒮·C_b^∞ ⊂ 𝒮 (Leibniz). Hence 𝒦_g := ĝ̃ m_∞ U ∈ 𝒮 and its kernel K_g := 𝓕⁻¹𝒦_g ∈ 𝒮(ℝ). ∎

## 4. Proof of (TC_S) (PROVED)

From (2.1) and Iϑ(g) = ϑ(g̃)I... (more precisely ϑ(g)I = Iϑ(g̃)):
 ϑ(g)Q₁Q₂ = I · ĝ̃(D) 1_{t<−a} M(D) 1_{t>a} · M(D)^* I.
I, M(D)^* are unitary: it suffices that X := ĝ̃(D)1_{t<−a}M(D)1_{t>a} be HS. We write
 X = [ĝ̃(D), 1_{t<−a}] M(D)1_{t>a} + 1_{t<−a} 𝒦_g(D) 1_{t>a}.
(a) Commutator. ĝ̃(D) is convolution by k(x) := k_{g̃}(x) = g(e^{−x}) ∈ C_c^∞. Kernel of [ĝ̃(D),1_{t<b}]: k(t−t')(1_{t'<b} − 1_{t<b}). Changing to x = t−t':
 ‖[ĝ̃(D),1_{t<b}]‖²_HS = ∫|k(x)|²·|{t: exactly one of t, t−x is below b}|dx = ∫|k(x)|²|x|dx < ∞,
independent of b. With a bounded factor (‖M(D)1_{t>a}‖ ≤ 1) it follows HS.
(b) Hankel/Wiener–Hopf block. Kernel K_g(t−t')1_{t<−a}1_{t'>a}:
 ‖1_{t<−a}𝒦_g(D)1_{t>a}‖²_HS = ∫|K_g(x)|²·|{t' > a: t'+x < −a}|dx = ∫|K_g(x)|²(−2a−x)_+dx,
finite because K_g ∈ 𝒮 (it suffices that |K_g(x)| ≲ (1+|x|)^{−1−ε}). This holds for every a ∈ ℝ: if λ > 1 (a > 0) it decays as the tail of K_g beyond 2a; if λ < 1 it contains the overlap block, of size ≲ (1+2|a|)‖K_g‖²₂. No Peller criterion is needed.
Hence ‖ϑ(g)Q₁Q₂‖²_HS ≤ 2∫|k(x)|²|x|dx + 2∫|K_g(x)|²(−2a−x)_+dx < ∞. ∎

Remark on H_g. R186.009 §4 expanded UPU^* = Σu_nū_mP_{a−nc}T_{(n−m)c} and bounded term by term: in that way each translate costs ~μ and q^{|n|} = λ/μ compensates it with no margin. The proof here does not expand U: it leaves it in the symbol, where it only costs bounded derivatives. The "boundary" of R186.009 was an artifact of the triangle inequality, not an obstruction.

## 5. Consequences (TC′: PROVED)

(i) ‖ϑ(g)Q₁Q₂‖²_HS = Tr(ϑ(g)Q₁Q₂Q₁ϑ(g)^*) = Son_S(g) + d_S(g*g^*) (R186.009 §3–4), both ≥ 0: hence **Son_S(g) < ∞ and d_S(g*g^*) < ∞**. (Compatible with Prop. d: d_S is a finite distribution on smooth tests but not L^∞_loc.)
(ii) For f = g₁*g₂: ϑ(f)Q₁Q₂Q₁ = (ϑ(g₁)Q₁Q₂)(Q₂Q₁ϑ(g₂)) + ϑ(g₁)[ϑ(g₂), Q₁Q₂Q₁]. The first term is HS·HS (Q₂Q₁ϑ(g₂) = (ϑ(g₂^*)Q₁Q₂)^*). By (2.1), Q₁Q₂Q₁ = I1_{t<−a}M1_{t>a}M^*1_{t<−a}I and the commutator of ĝ₂̃(D) with each half-line is trace class (CC Lemma D.1, CITED: quantized differential of a Schwartz symbol), while it commutes with M(D), M(D)^*. Hence ϑ(f)Q₁Q₂Q₁ is trace class; Dixmier–Malliavin (CITED) gives all f ∈ C_c^∞(ℝ*₊).
(iii) The justification of CC (85)–(90) (exchange of trace/spectral decomposition) carries over: (84)_S remains CONDITIONAL **only** on (CV_S), i.e. convergence of the series ε_S and its meaning as a function (not merely as a distribution). Δ and C of R186.009 are upgraded to PROVED without the TC_S hypothesis.
(iv) What does **not** follow: boundedness of ε_S (B of R186.009). The weights λ_n/√(1−λ_n²) ≍ n^{−1/2} and the boundary mass c_n(ρ) remain the open question; this is the next memo.

## Audit notes

1. §1: verify F_∞ = Im_∞(D) with the normalizations of R186.007 (kernel 2cos 2πux on L²(ℝ₊)); the argument only uses F_∞ϑF_∞ = ϑ(·⁻¹) and unitarity.
2. §2: F_S = M^*I uses F_S self-adjoint (L0). Check 1 − M1_{t≤a}M^* = M1_{t>a}M^* (M(D) unitary).
3. §3(ii) is the only nontrivial external input: CC Prop. 1.5(iv), ĥ u_∞ ∈ 𝒮. Check that their u_∞ is our m_∞ (or its conjugate; irrelevant).
4. §3(i): for S with several primes, U is a finite product of factors of the type of R186.008; C_b^∞ is an algebra.
5. §4(b): the formula (−2a−x)_+ is exact; the sign of a does not matter for finiteness.
6. §5(ii): CC's Lemma D.1 is stated on L²(Ĉ) with the half-line [0,∞); translation to cutoff b is unitary conjugation.
7. No claim is made about the sign, nor about (CV_S), nor about (M).

## For Paper 46

Replace, in the remark proposed by R186.009, "the finiteness of Son_S and the boundedness of ε'_S remain open (TC_S), (CV_S)" with: "Son_S(g) is finite and ϑ(f)Q₁Q₂Q₁ is trace class for f ∈ C_c^∞: after the inversion, Q₁Q₂ is half-line·M(D)·half-line with M = m_∞e^{iφ_S}, and ĝm_∞e^{iφ_S} ∈ 𝒮 (lemma: CC Prop. 1.5(iv) plus e^{iφ_S} ∈ C_b^∞). Formula (84)_S holds modulo the convergence (CV_S) of ε'_S, which remains open." Labels: TC_S PROVED; (84)_S CONDITIONAL on CV_S; boundedness OPEN. No equivalence with RH.

## Note (R186_096)

* ACCEPTED. CC 1.5(iv) is superfluous (m_∞ ∈ 𝒪_M by Stirling). (84)_S remains CONDITIONAL on Δ (R186_095 M2).
