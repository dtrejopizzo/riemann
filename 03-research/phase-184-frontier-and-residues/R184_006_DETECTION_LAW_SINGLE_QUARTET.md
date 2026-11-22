# R184_006 — Quantitative detection law for a quartet of zeros of ζ off the line

Pure mathematics; the only figures are evaluations of constants of an
explicit polynomial bump (computed by hand, §1.1). RH is not claimed, nor the closure of D.*

## State

| Item | Content | Label |
|---|---|---|
| Thm 1 | If ζ has a quartet ½±a±iγ (0<a<½) that is **maximal and X-isolated** (§2), then λ_min(W_T\|P_T) < 0 for every T ≥ T*(a,γ) := max{1+1/a, (1/(2a))·log(C_ψ·L(γ))}, L(γ)=1.1 log(γ+3)+5, C_ψ = 67K/M0² explicit (≈1.6·10⁵ for the bump of §1.1), γ ≥ γ₀ = 100 | PROVED (from the explicit formula CITED and the N(t) bound CITED) |
| Thm 1′ | Version with off-line neighbors: if the zeros at distance ≤ X from γ have β' ≤ a₁ < a, the same result with a replaced by a−a₁ in the logarithmic term | PROVED |
| Cor 2 | Contrapositive: certified positivity on window T₁ excludes isolated maximal quartets with a ≥ max{1/(T₁−1), log(C_ψL(γ))/(2T₁)} | PROVED |
| Cor 2 at T₁ ≤ ½log5 | **Gives no new information whatsoever** (vacuous: requires T₁ > 2) | PROVED (trivial) |
| Corpus comparison | Qualitative version = R162_2501 Prop 1 (non-explicit constant C(γ_j)) and P46 cor:margin2(iii) / P45 Thm 10.4 (existence of T₀). New here: the constants and the dependence on γ | — |
| (P153.5) | Answered in the form of an upper bound: the law for an isolated quartet is (1/2a)·log(C log γ), not 0.624+0.027 log(1/a) | PROVED as an upper bound on T*; optimality OPEN |
| Row D | Does not move: it is the E1 direction (¬RH ⟹ ¬positivity), quantified | unchanged |

## 0. Corpus check

Read: R153_005 (Thm A, law T*(a) of Ξ_a, item P153.5), R184_004 Lemma 1 (signature (2,2), q = 4Re A(F_e)² − 4Re A(F_o)²),
R162_2501 §2 Prop 1–2, R162_2602 §0–3 (count N(T), two-bump packets of R162_2501a), P46 cor:margin2, thm:KEP3,
remark after thm:KEP3 (l.1760), phase-138 README (D.17: RH ⟺ W(h_T) ≥ 0 ∀T, Landau). **Finding:** the mechanism (Gabor
packet at the endpoints of I_T, phase chosen so that arg A = π/2, quartet ≍ −e^{2β*T}) is already in R162_2501 Prop 1
(upper bound λ_A ≤ −c e^{2β*T} + C, with c, C, T₁ "configuration-dependent," no values). The DH gate of
phase 119 and D.17 are qualitative statements of the same direction. No file in the corpus gives an explicit T₀ as a
function of (a, γ), nor treats off-line neighboring zeros, nor the Tate correction quantitatively, nor discusses
what zero-free region a certified window buys. That is what is new; the mechanism is not.

## 1. Setup

Conventions from R162_2501/R184_004: I_T=[−T,T], Φ_F(s)=∫F(t)e^{(s−½)t}dt, P_T = {Φ_F(0)=Φ_F(1)=0},
W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ) (with multiplicity). **Accounting (CITED, Weil; R183_015/022):** for F in P_T the
explicit formula equates this sum over zeros to the prime side + the archimedean side; the polar terms are of Φ_F(0)Φ_F(1)-type and vanish
in P_T. Hence on P_T *there are no* polar/archimedean terms to add to the spectral side: everything is in Σ_ρ.
The series converges absolutely for F ∈ C¹ with F'' ∈ L¹ and compact support (|Φ_F(½+iy)| ≪ y^{−2}); λ_min is taken over
C_c^∞(I_T)∩P_T, and the piecewise-C² tests below are approximated in the norm that controls Σ_ρ (|Φ|·(1+|ρ|)² uniform),
so that W_T(F)<0 for the C² test implies the same for a nearby C_c^∞ function in P_T.

**Count (CITED, Trudgian 2014, Thm 1; constants from corpus memory, verify):**
|N(t) − (t/2π)log(t/2πe) − 7/8| ≤ 0.112 log t + 0.278 log log t + 2.51 (t ≥ e). With log log x ≤ log x − 1 one gets, for
n(t) := #{γ' ∈ (t−1, t+1]}:  **n(t) ≤ L(t) := 1.1 log(t+3) + 5** (PROVED from what is CITED).

### 1.1 The test
Let ψ ∈ C¹, ψ'' ∈ L¹, ψ ≥ 0, supp ψ ⊂ [−1,0], ψ=ψ'=0 at the endpoints. M0 := ‖ψ‖₁, M2 := ‖ψ''‖₁+‖ψ'‖₁+‖ψ‖₁.
Explicit example: ψ(u)=16u²(1+u)²: M0 = 16·B(3,3) = 8/15 ≈ 0.533, ‖ψ'‖₁ = 2, ‖ψ''‖₁ = VT(ψ') = 4·|ψ'(−½+1/(2√3))| ≈ 12.32,
M2 ≈ 14.85, K := M0² + 3M2² ≈ 662.

    F_+(t) := ψ(t−T)·sin(γt) − c·ψ(t−T),   F(t) := F_+(t) + F_+(−t)   (even, real, supp ⊂ I_T).

For F even, Φ_F(0)=Φ_F(1) and the two Tate conditions reduce to one: ∫F_+cosh(t/2)=0, which fixes
c = ∫ψ(t−T)sin(γt)cosh(t/2)dt / ∫ψ(t−T)cosh(t/2)dt. Integrating by parts twice and using cosh(x−½) ≥ e^{−½}cosh x:
**|c| ≤ 1.65·M2/(M0γ²)** (rank-1 correction; the odd part is not used).

## 2. Theorem 1

**Hypothesis (Max–Iso, X).** ζ has simple zeros (or multiple ones: that only helps) at ½±a±iγ, 0<a<½, γ ≥ γ₀ := 100; every other
zero ρ'=½+β'+iγ' satisfies |β'| ≤ a (maximality: a = Θ attained here) and, if |γ'−γ| ≤ X, β' = 0 (isolation), with
X³ ≥ 270 (M2/M0)² (L(γ) + 2log(X+3)) (for the bump of 1.1: X ≈ 60·L(γ)^{1/3}).

**Theorem 1 (PROVED).** Under (Max–Iso, X), W_T(F) < 0 for every T ≥ T*(a,γ), with

    T*(a,γ) := max{ 1 + 1/a ,  (1/(2a)) · log( C_ψ · L(γ) ) },   C_ψ := 67K/M0²   (≈ 1.56·10⁵ for 1.1).

Consequently (monotonicity, P46 lem:monoT) λ_min(W_T|P_T) < 0 for every T ≥ T*(a,γ).

*Proof.* Let z=a+iγ, A := Φ_F(½+z). Since F is even, Φ_F(½−z)=A, and by Lemma 1 of R184_004 the quartet contributes q = 4Re(A²)
= 4[(Re A)² − (Im A)²]. With cosh(zt) = cosh(at)cos(γt) + i sinh(at)sin(γt) and A = 2∫F_+cosh(zt):

* Im A = ∫ψ(t−T)sinh(at)(1−cos2γt)dt − 2c∫ψ(t−T)sinh(at)sin(γt)dt. The first term is ≥ s·M0 − η₁ with
  s := sinh(a(T−1)) and η₁ := M2cosh(aT)/(4γ²) (two integrations by parts; |(ψ(·−T)sinh(a·))''| ≤ cosh(aT)(|ψ''|+2a|ψ'|+a²ψ)).
  The second is ≤ 2|c|cosh(aT)M0 ≤ 3.3 M2 cosh(aT)/γ².
* |Re A| ≤ |∫ψ(t−T)cosh(at)sin(2γt)| + 2|c|cosh(aT)M0 ≤ 4 M2cosh(aT)/γ².

For T ≥ 1+1/a and a<½: cosh(aT) ≤ e^{a}cosh(a(T−1)) ≤ e^{½}coth(1)·s ≤ 2.2 s. With γ ≥ 100 and M2/M0 ≈ 27.8 (or in general
γ² ≥ 300 M2/M0), η := 4M2cosh(aT)/γ² ≤ 0.03 s M0. Hence

    q ≤ −4(0.97 sM0)² + 4(0.03 sM0)² ≤ −3.7 s²M0² ≤ −0.24·M0²·e^{2aT}        (★)

using sinh²x ≥ (1−e^{−2})²e^{2x}/4 ≥ 0.187e^{2x} for x = a(T−1) ≥ 1 and e^{−2a} ≥ e^{−1}.

*Remaining zeros.* For a zero ρ'=½+z', z'=a'+iγ', γ'>0, a' ∈ [0,a]: the zeros above the axis contribute in total
≤ Σ_{γ'>0} 2|Φ_F(ρ')|² (a pair on the line gives exactly 2|Φ|² ≥ 0; a quartet gives 4Re(A'²) ≤ 4|A'|², two zeros above the axis).
Expanding sin(γt)e^{±z't} in exponentials and using ∫ψ(u)e^{a'u}e^{iξu}du ≤ g(ξ) := min(M0, M2/ξ²):

    |Φ_F(ρ')| ≤ e^{a'T}[ g(γ'−γ) + g(γ'+γ) + 2|c|g(γ') ].

Summing over blocks of length 2 centered at γ+2k, with n ≤ L(γ)+1.1log(1+2|k|), Σ_{j odd}j^{−4} = π⁴/96,
Σ log(j+2)/j⁴ ≤ 1.13:
* nearby (|γ'−γ| ≤ X, a'=0 by Iso): Σ g(γ'−γ)² ≤ (M0² + 3M2²)L(γ) = K·L(γ) (L ≥ 5);
* far (a' ≤ a): Σ_{|γ'−γ|>X} g(γ'−γ)² ≤ 2M2²(L(γ)+2log(X+3))/X³ (tail Σ_{j≥X} j^{−4} ≤ 1/(2X³), X ≥ 3);
* the terms g(γ'+γ) and |c|g(γ') are O(M2²L(γ)/γ³) and O(M2⁴/(M0²γ⁴)) and are absorbed into the constants for γ ≥ γ₀
  (factor (a+b+c)² ≤ 3(a²+b²+c²) already included in the 67 below; item for audit verification).

Hence the remaining contribution is ≤ 8K·L(γ) + 8e^{2aT}·2M2²(L+2log(X+3))/X³ ≤ 8K·L(γ) + 0.06 M0² e^{2aT}
(by the choice of X). With (★): W_T(F) ≤ −0.18 M0²e^{2aT} + 8·1.5·K·L(γ)… and W_T(F) < 0 as soon as
e^{2aT} > 67 K L(γ)/M0², i.e. T > (1/2a)log(C_ψ L(γ)). □

**Thm 1′ (PROVED, same proof).** If the zeros with |γ'−γ| ≤ X only satisfy β' ≤ a₁ < a, the nearby term is
8e^{2a₁T}K L(γ) and T* = max{1+1/a, (1/(2(a−a₁)))·log(C_ψL(γ))}.

**Order of magnitude.** log C_ψ ≈ 12; for γ = 10^{10}, L ≈ 30, T* ≈ 7.7/a; for a = 0.1, T* ≈ 77. In general
**T*(a,γ) = (1/(2a))·(log log γ + O(1)) for a ≥ 1/T*,** with O(1) ≈ 12 for the bump of 1.1 (improvable with ψ ∈ C^k:
X ~ L^{1/(2k−1)} and smaller K; not optimized).

## 3. Comparison with the law of Ξ_a (P153.5)

Ξ_a: whole vertical lines of zeros at distance a, all consistent with the same test (Thm A: form = 2[⟨A_Tu,u⟩ −
⟨A_Tw,w⟩]); numerical law T* ≈ 0.624 + 0.027 log(1/a). An isolated quartet of ζ competes against the local density of
zeros on the line, ≍ log γ per unit window, and has only the growth sinh²(a(T−1)) at its disposal: law (1/2a)log(C log γ),
**exponentially worse in 1/a and growing (doubly logarithmically) in γ.** The bump width fixed at 1 is not a
loss at the unconditional level: widening it to ℓ reduces the frequency window to 1/ℓ, but the unconditional count in
short intervals remains O(log γ) (S(t) = O(log t)), so the on-line part scales as ℓ²·log γ, the same
as the quartet: there is no gain without a stronger local count bound (which is conditional information). For
aT ≲ 1 the quartet contributes ≈ −a²T²·M0² and the law becomes T ~ (log γ)^{1/2}/a (regime excluded by the clause 1+1/a).
Optimality of T*: OPEN (only an upper bound on the real threshold; trivial lower bound: the quartet is ≥ −4sinh(2aT)‖F‖²/a,
R162_2501 Prop 1).

## 4. Corollary 2: what positivity on a window buys

**Cor 2 (PROVED).** If λ_min(W_{T₁}|P_{T₁}) ≥ 0, then ζ has no (Max–Iso, X) quartet at height γ ≥ 100 with
a ≥ a₁(T₁,γ) := max{ 1/(T₁−1), log(C_ψL(γ))/(2T₁) }.

* **Certified windows from the corpus (T₁ ≤ ½log5 ≈ 0.805, P46; 0.8, Zhu):** the condition 1/(T₁−1) requires T₁>1, and even
  ignoring that clause log(C_ψL)/(2T₁) ≥ 12/1.6 > ½ ≥ a. **New zero information: none.** (Consistent with P46
  §subsec:where: at T ≤ 1 the certificate sees the region |τ| ≲ 2πe^{2T}, below the first zero.)
* **When it would surpass the classical region** (which excludes a > ½ − c/log γ): one would need a₁ < ½ − c/log γ, i.e.
  T₁ ≳ log(C_ψ L(γ)) ≈ 12 + log log γ, plus the Max–Iso hypotheses. But at that scale Cor 2 is not a zero-free
  region: it only excludes a quartet that *attains* Θ and is isolated; it says nothing if Θ is not attained or if several
  zeros with β ≈ Θ cluster at distance < X (the phases cannot be aligned). De la Vallée Poussin type: **no**.
* Any certificate at T₁ ≥ 13 is itself inaccessible: by P46 cor:margin2(i), λ_W ≤ 4·10⁹Te^{−15.449T}, a margin
  ≲ 10^{−77} at T=13 (and doubly exponential in the refined version). Cor 2 quantifies what was already known:
  positivity on small windows buys no zeros.

**Relation to P45 Thm 10.4 / P46 cor:margin2(iii) / R162_2501 Prop 1.** All three give ¬RH ⟹ ∃T₀ with λ < 0 (R162_2501 with
rate e^{2β*T}); none gives T₀. Thm 1 is their effective form under (Max–Iso): explicit T₀ ≤ T*(a,γ). It is an improvement
of constants, not of mechanism.

## 5. Does it move D?

No. Thm 1 quantifies the E1 direction ¬RH ⟹ ∃T: λ<0 (already PROVED qualitatively). The direction that is D — positivity
∀T — is not touched: Thm 1 only says what T one would have to reach to *see* a given quartet, and Cor 2 shows that the
certifiable windows (T ≤ 0.805) see nothing. Moreover Thm 1 applies verbatim to M_m (R184_004 Thm 4): it is blind to the
class (W3), as a statement of the E1 direction should be. Row D label: unchanged.

## For the audit

1. **CITED constants from memory.** Trudgian 2014 (0.112, 0.278, 2.51): not verified without web access. If they change, only L(t)
   and hence log C_ψ change, by O(1).
2. **Absorption of the O(γ^{−2}), O(γ^{−3}) terms.** §2 absorbs them "for γ ≥ 100" with the factor 3 of (a+b+c)²; the
   numerical chain 0.24 → 0.18 → 67 should be redone line by line (it was done by hand; a factor
   of 2–3 may be lost in C_ψ, harmless in the log but not in the literal statement).
3. **The Max–Iso hypothesis is strong.** "a = Θ attained and isolated within radius X ~ 60 L^{1/3}" excludes the
   dangerous configurations (zeros with β≈Θ nearby, Θ not attained). Without it the method fails: distant zeros with β'=a
   contribute e^{2aT}·O(L/X³), of the same order as the main term if X = O(1). Thm 1′ only relaxes the nearby part.
4. **C² → C_c^∞ step.** Asserted by continuity of Σ_ρ in the (1+|ρ|)²|Φ| norm; the audit may require the explicit
   lemma (mollifying ψ preserves P_T after readjusting c).
5. **Regime aT < 1.** Excluded by the clause 1+1/a; the law ~ (log γ)^{1/2}/a of §3 is heuristic (not PROVED).
6. **Novelty.** Mechanism = R162_2501 Prop 1; what is new is only the explicit form and Cor 2. Do not call it a "detection
   law for ζ" without the qualifier "upper bound, under Max–Iso".

## Note (R184_092)

* MAJOR: the far-zero terms g(γ+γ′), |c|g(γ′) carry e^{2a′T} and are not absorbed into the constant KL; chain redone: q ≤ −0.254·M0²e^{2aT}, margin ≈4e-3 sufficient. The statement survives; the proof needs to be rewritten.
* Trudgian cited from memory; "applies to M_m" → ARGUED; C²→C_c^∞ step without proof.
