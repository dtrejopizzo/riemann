# R183.021 — The semilocal Sonin space as a positive part: what it gives and what it does not

Input: R183.015, 017–020. Neither RH nor the closure of D is claimed.

## 0. Verdict

* CCM (2310.18423v2) prove **no** trace formula, positivity, nor comparison
  with Weil's form for S ⊋ {∞}. They only prove that the semilocal Sonin
  space is, as a Hilbert space, the archimedean one transported by θ_S
  (Thm 4.12 / isosonin), with a different inner product. `CITED`.
* **Structure theorem (PROVED).** Every trace-type positive part
  Tr(ϑ(g)Pϑ(g)^*) on L²(X_S)^{K_S}, with P ≥ 0, is a multiplier form
  ∫ρ_P|ĥ|² ds/2π, where ρ_P ≥ 0 is P's diagonal density in the
  spectral variable s of the scaling. Hence R' = E_S − P is the
  compression to I_T of a convolution with symbol φ = m_S − ρ_P. The
  semilocal Sonin space only enters through its diagonal density ρ_S.
* **Index criterion (PROVED).** (a) If φ ≥ c > 0 outside a compact set,
  then n₋(R') < ∞. (b) If φ = ψ + r, with ψ Bohr almost periodic and
  r → 0 at ∞, then on R183.018 Thm 5.1's bump pairs
  R'(x)/‖x‖² → M(ψ) + M(ψ·cos(s log p)). If that number is < 0, n₋ = ∞.
* **CCM's semilocal Sonin: NO-GO `CONDITIONAL`** on the Christoffel
  lemma (CF-S): ρ_S(s) − ρ_∞(s) → 0 on average. Under (CF-S), R' has on
  the family of pairs at distance log 2 the same limit −log 2/√2 < 0 as
  R183.018, and n₋ = ∞. Unconditionally only the sandwich bound (§3.3) is
  proved, which does not decide the sign.
* **A candidate that does absorb the primes (PROVED, but E1).**
  P_C := T_{I_T}((m_S − C)_+) ≥ 0. The remainder R'_C = T_{I_T}(min(m_S,C))
  is bounded on L²(I_T), equal to C·Id − (trace class ≥ 0), and has
  finite n₋. It is **positive** on the family of pairs (limit C > 0).
  Moreover: E_S ≥ γ on K ⟺ ∀γ'<γ ∃C: R'_C ≥ γ' on K. By Paper 47 Thm C
  (½log3), this gives n₋(R'_C|primitives) = 0 for some C in the first new
  window, but only **starting from** already-proved positivity. It is not
  a new proof.
* Missing lemma, self-contained: (L-C) in §5.

## 1. CCM source (CITED, local tex `00-references/papers-ref-2/arXiv-2310.18423v2/mainc2m24fine.tex`)

§5 (l.692–1072) and the introduction were read. The published PDF
(`Zeta-zeros-and-prolateproofs-final-2024.pdf`) has the same content.
CM 2022 (UV prolate) is purely archimedean and does not mention the
semilocal case.

* X_S = A_S/Γ, with Γ = Q_S^*. w_S: L²(X_S) → L²(C_S) is unitary and
  C_S/K_S ≅ R_+^*.
* η_S(f) is the class of 1_{R_S}⊗f. One has
  F_μ w_S η_S f = ∏_{p∈S} L_p(½−is)·F_μ w_∞ f (Prop. groundstate (i)), and
  F_S η_S = η_S F (iii).
* The semilocal part of the Hermite oscillator is N_S, obtained by
  orthogonalizing η_S(x^{2n}e^{−πx²}) (Thm hermsemiloc). The prolate
  candidate **W_{λ,S} = (H+½)² + λ²N_S** is only formal: neither
  self-adjointness nor the spectrum is proved (text before Rem. care).
* Local Sonin: Def. soninp. For Q_p, the Z_p^*-invariant part of Son_1 is
  C·σ_p, with σ_p = ε_0 − p^{-1}ε_1 and F σ_p = σ_p (Prop. soninppp).
* Semilocal Sonin (Def. soninsemiloc):
  Son_λ(X_S) = {f ∈ L²(X_S)^{K_S} : f = 0 = F_S f at |x|_S < λ}.
* θ_S(f) is the class of σ_S⊗f. One has
  **F_μ w_S θ_S f = ∏_{p∈S∖∞}(1 − p^{−½−is})·F_μ w_∞ f** (Prop. sonintensor),
  and ⟨θ_S f|η_S g⟩ = ⟨f|g⟩ (groundstatedual (iii)).
* **Thm isosonin:** θ_S: Son_λ(R) → Son_λ(X_S) is a Hilbertian
  isomorphism: bounded with bounded inverse, **not** unitary. Prop. propbb:
  the inner product on B_λ is that of L²(ds/|E_S(s)|²).
* On Weil positivity, CCM only say (introduction, l.198) that they
  "expect" to compare the trace of the semilocal prolate with Weil's
  functional. There is no statement about tests supported on
  (q^{-1/2}, q^{1/2}). The only proved positivity remains CC's
  (2006.13771) with S = {∞}. **No CCM result can be cited as a step
  towards (L-Son).**

## 2. Crossing with the corpus

* Grid R162_2300, row 2A (l.115): "semilocal Sonin trace: favorable
  sign, no exact identity." The identity was given by R183.018 §3. Here
  it is shown that CCM's semilocal version only changes the diagonal
  density (§3).
* Grid l.114: "CC's global semilocal (phase-5/B2), not run." Not
  repeated here.
* R162_2602 Thm 4 (PROVED): CC's semilocal support is the same
  truncated S, with no independent positivity and blind to deletion. Thm 3
  (PROVED, E1): "A_T|P_T = compression of S_+ ≥ 0 plus rank ≤ 2 ⟺ λ_A ≥ 0".
  **This file's §4 is a variant of Thm 3**, with remainder
  C·Id − compact instead of rank ≤ 2, and with translation-invariant P.
  It shares its E1 status.
* R161_014 Thm 2.1: Sonin–Gamma coercivity for product ports.
  It is a different object and is not used.
* Paper 47 Thm C: λ_min(A_{½log3}|P_T) ≥ 8.8577·10⁻⁵, machine-verified.
  `CITED`. For the full form on (½log2, 0.8], Zhu 2026 Thm 1.2:
  `CITED`, not re-verified (PATH-TO-D l.52).

## 3. Every trace-type positive part is a multiplier

### 3.0 The semilocal symbol (PROVED, from R183.015/018)

Take h ∈ C_c^∞(I_T), ĥ(s) = ∫h e^{−ist}dt and m(s) = h_+(s) = 2θ'(s)
(R183.018 §1). Since Re c_h(x) = (1/2π)∫|ĥ|²cos(sx)ds,

    E_S(h) = (1/2π) ∫ m_S(s)|ĥ(s)|² ds,
    m_S(s) := 2θ'(s) − Σ_{p∈S} σ_p(s log p),
    σ_p(s log p) = −2 Re (L_p'/L_p)(½+is),   L_p(z) = (1−p^{−z})^{−1}.

Hence m_S(s) = 2 d/ds arg[Γ_R(½+is)·∏_p L_p(½+is)]: it is twice the
phase derivative of the function E_S(s) = ∏_{v∈S}L_v(½+is), i.e. CCM's
dual weight (ess), (msdual). This is the exact link between the energy
and CCM's object. The series over all k is legitimate: c_h vanishes for
|x| ≥ 2T. Also m_S is continuous, real, and even, and m_S(s) → +∞ like
log|s| (θ' ~ ½log(|s|/2π), σ_p bounded).

**Remark 3.0 (PROVED).** If E_S(s) were a Hermite–Biehler function, the
de Branges space H(E_S) would have diagonal kernel
φ'_{E}(s)|E|²/π with φ'_E = m_S/2 > 0. But m_S < 0 in a neighborhood of
s = 0: 2θ'(0) = −log π + ψ(¼) < 0, and σ_p(0) > 0. Hence E_S is not
Hermite–Biehler on the line, and **no** nonnegative diagonal density ρ
coincides with m_S. The positive part necessarily differs from m_S on
{m_S < 0}, a low-frequency compact set (R183.016).

### 3.1 Structure theorem (PROVED)

Let P ≥ 0 be bounded on L²(X_S)^{K_S} such that ϑ(g)Pϑ(g)^* is trace
class for g ∈ C_c^∞(R_+^*). Let U_S = F_μ w_S, unitary on
L²(R, ds/2π), carrying ϑ(g) to multiplication by ĝ (CCM Prop.
httransfoS). Define

    μ_P(B) := Tr(P^{1/2} U_S^* 1_B U_S P^{1/2}),   B ⊂ R Borel.

μ_P is a positive, locally finite measure, and
Tr(ϑ(g)Pϑ(g)^*) = Tr(P^{1/2}U_S^*|ĝ|²U_S P^{1/2}) = ∫|ĝ|² dμ_P.
In the h variable (dictionary R183.018 §1, |ĝ|² = |ĥ|² on the critical
line) one obtains

    P(h) = ∫|ĥ(s)|² dμ_P(s),    R'(h) := E_S(h) − P(h) = ∫|ĥ|² (m_S ds/2π − dμ_P).

*Proof.* It follows from cyclicity of the trace plus the fact that
B ↦ Tr(A^*1_B A) is σ-additive for Hilbert–Schmidt A on compact sets
(normal monotone convergence). ∎

**Consequence.** In R' only P's **diagonal density** in the scaling
spectral variable matters. Neither the geometry of X_S, nor the phases of
the Sonin vectors, nor the prolate operator appear except through ρ_P.
R' is the compression to I_T of a convolution (truncated Wiener–Hopf
operator) with symbol φ_P := m_S − 2πρ_P. This holds for the semilocal
Sonin projection, for the positive part of W_{λ,S}, and for any other
trace-type operator.

### 3.2 Negative index criterion (PROVED)

**Lemma 3.2.** Let φ be R''s symbol (locally continuous function,
bounded below on compacts).

(a) If φ ≥ c > 0 outside a compact set K₀, then

    R' ≥ c·Id − T_{I_T}((c−φ)_+),

where T_{I_T}((c−φ)_+) is positive, trace class, with continuous kernel
(2π)^{−1}((c−φ)_+)^∨(x−y). Consequently n₋(R') < ∞ and R' is bounded
below. R' is bounded on L²(I_T) if and only if φ is bounded.

(b) (**Pair family.**) Let φ = ψ + r, with ψ(s) = Σ_λ a_λ cos(λs),
Σ|a_λ| < ∞, and r(s) → 0 as |s| → ∞. Let a = log p < 2T and x the
combination of bump pairs from R183.018 Thm 5.1, with
h_j = β_w(·−t_j) + β_w(·−t_j−a). Then

    R'(x)/‖x‖² → M(ψ) + ½ a_a(ψ) = a_0 + ½a_a      (w → 0),

where a_a is the coefficient of cos(as). If that number is < 0, then
n₋(R'|primitives ∩ ker ℓ) = ∞.

*Proof.* (a) Write φ = c + (φ−c)_+ − (c−φ)_+. The last summand is
supported on K₀ and bounded, hence integrable. Compressing a positive
integrable multiplier to a bounded interval has a continuous kernel of
positive type, and by Mercer it is trace class. Thus c − (trace) has
finite n₋.

(b) Use |x̂_j|² = |β̂_w|²(2 + 2cos(as)) and
∫e^{iλs}|β̂_w|² ds = 2π c_{β_w}(λ), which is **exactly 0** for
|λ| > 2w. This suffices for each λ ≠ 0 in ψ's spectrum, except λ = ±a,
for small w. The series tail is controlled by Σ|a_λ| < ∞, with o(1)
uniform loss; the frequencies λ ≤ 2w form an empty set in the limit if
ψ's spectrum is separated from 0. Cross correlations between pairs vanish
by the choice of t_j (R183.018). For the term r: |β̂_w(s)|² = (s²+¼)²w²|ĉ₀(ws)|²,
whose normalized mass escapes to |s| ~ 1/w, so ∫r|x̂|² = o(‖x‖²). The
infinite dimension and the passage to ker ℓ ∩ primitives proceed as in
R183.018 (dimension argument and loss of finite codimension). ∎

**Control (PROVED).** For P = Son, CC (S = {∞}): 2πρ_∞ = m + ε̂, so
φ = −ε̂ − σ_2(s log 2). The part −ε only acts on [−2T,2T] and is
bounded, so it contributes O(w) (R183.018). With a_0 = 0 and
a_{log 2} = −2 log 2·2^{−1/2}, the limit is −log 2/√2 ≈ −0.490. It
coincides exactly with R183.018 Thm 5.1 (−√2 log 2·‖β‖²Σ|c|² divided by
‖x‖² = 2‖β‖²Σ|c|²). The lemma reproduces the known NO-GO.

**Reading.** By (a)–(b), a trace-type positive part gives finite n₋
if and only if (modulo boundary cases) its symbol **contains the prime
oscillation** at high frequency: 2πρ_P(s) = m_S(s) − c(s), with c ≥ c₀ > 0
at infinity. It is not enough for c to be almost periodic without
positive mean. Absorbing the primes means exactly this.

### 3.3 CCM's semilocal Sonin space

In the U_S image, the semilocal Sonin space is V_S = D·V_∞, with
D(s) = ∏_{p∈S∖∞}(1 − p^{−½−is}) and V_∞ = U_∞(Son_λ(R)), by CCM (ms1). Let
Π_S be the orthogonal projection of L²(X_S)^{K_S} onto Son_λ(X_S), and
ρ_S its diagonal density. ϑ commutes with θ_S, because the scaling acts
only on the archimedean variable.

**Prop. 3.3 (sandwich; PROVED).** The elements of V_∞ are continuous in s
with continuous pointwise evaluation (de Branges, CCM propbb). By the
extremal characterization of the diagonal kernel,

    ρ_S(s) = sup_{F∈V_∞} |D(s)|²|F(s)|² / ∫|D|²|F|² ,

and hence

    |D(s)|²/C_D · ρ_∞(s) ≤ ρ_S(s) ≤ |D(s)|²/c_D · ρ_∞(s),
    c_D = ∏(1−p^{−½})²,   C_D = ∏(1+p^{−½})².

For S = {∞,2}: |D|² = 3/2 − √2 cos(s log 2) ∈ [0.0858, 2.914].

The sandwich **does not decide**: it leaves a possible oscillation of
amplitude ~ρ_∞ ~ log|s|, much larger than the prime amplitude, which is
O(1).

**Lemma (CF-S), OPEN.** As |s| → ∞, ρ_S(s) − ρ_∞(s) → 0. The weak
liminf form (ρ_S − ρ_∞) ≥ 0 on average over fixed-length windows
suffices.

*Heuristic* (not a proof). It is the Christoffel asymptotics with a
continuous, fixed weight |D|², in a space whose local density ν(s) ~
log|s|/π grows. One expects λ_w ≈ λ/w(s) with relative error O(ν^{−2}),
hence absolute error O(1/log|s|). The direct proof with the test
function F = K_∞(·,s) only gives error O(1): sinc²-type tails have
infinite second moment. A better localized test function within V_∞
is needed. That is the open technical point.

**Theorem 3.4 (NO-GO for CCM's semilocal Sonin; CONDITIONAL on
(CF-S)).** Let S = {∞,2} (or any S ∋ 2) and T > ½log 2. If (CF-S)
holds, then

    R'_{S,T} := E_S − Tr(ϑ(g)Π_Sϑ(g)^*)

satisfies, on the family of pairs at distance log 2,
R'(x)/‖x‖² → −log 2/√2 < 0, and n₋(R'|primitives ∩ ker ℓ) = ∞.

*Proof.* Under (CF-S), φ_S = φ_∞ + o(1). Apply Lemma 3.2(b) with the
same ψ as in the control. ∎

Why it cannot help, even without (CF-S): θ_S multiplies by D, which is
the causal operator h ↦ h − p^{−½}h(·−log p) in the t variable. It
changes the Sonin space's **metric**, but the space remains archimedean
(Thm isosonin). For its diagonal density to acquire the oscillation
−σ_p(s log p) with the exact coefficient, the projection would need to
"know" the explicit formula's term. Nothing in CCM's construction forces
this, and the Christoffel heuristic says it does not occur. The positive
part of W_{λ,S} is not rigorously defined in CCM (only formal), so it
cannot be evaluated: OPEN and lacking an object.

## 4. A positive part that does absorb the primes: the truncated symbol

### 4.1 Definition and properties (PROVED)

Let C > 0 and g_C := (C − m_S)_+. This function is continuous and
compactly supported, because m_S → +∞. Define

    P_C(h) := (1/2π)∫(m_S − C)_+ |ĥ|² ≥ 0,
    R'_C(h) := (1/2π)∫ min(m_S, C) |ĥ|² = C‖h‖² − ⟨T_{I_T}(g_C)h, h⟩.

Then E_S = P_C + R'_C, and R'_C is **bounded** on L²(I_T) with
‖R'_C‖ ≤ max(C, ‖g_C‖_∞ − C). It equals C·Id minus a positive trace-class
operator. Hence n₋(R'_C) = #{λ_j(T_{I_T}(g_C)) > C} < ∞.

P_C is trace type in §3.1's sense, with ρ = (m_S − C)_+/2π. For large
|s|, it equals exactly m_S − C, with the prime oscillation
−Σσ_p(s log p) inside: it **absorbs the primes**, as desired.

### 4.2 The NO-GO family is positive here (PROVED)

On R183.018's pairs, R'_C(x)/‖x‖² → C > 0 as w → 0. Indeed, |x̂|²'s mass
escapes to the region {m_S ≥ C}, where min(m_S,C) = C. The reason is that
the oscillation −σ_2(s log 2), which the family detects with coefficient
−log 2/√2, is now inside P_C and not in the remainder. Seen from R', the
bump pairs are high-frequency vectors, and there R' is the scalar C.

### 4.3 Window-equivalence with D (PROVED; E1)

Let K ⊂ L²(I_T) be a closed subspace defined by finitely many continuous
functionals, e.g. primitives ∩ ker ℓ, with
ℓ(h) = ∫h. E_S(h) ∈ (−∞, +∞] is defined by the integral, because m_S is
bounded below.

**Theorem 4.3.** Let γ ∈ R.
(i) If R'_C ≥ γ on K for some C, then E_S ≥ γ on K.
(ii) If E_S ≥ γ on K, then for every γ' < γ there is C with R'_C ≥ γ'
on K.

*Proof.* (i): P_C ≥ 0.

(ii): let q_C := R'_C − γ, increasing in C. Suppose there exist η > 0
and, for every C, unit vectors h_C ∈ K with q_C(h_C) ≤ −η. A
subsequence converges weakly to h ∈ K with ‖h‖ ≤ 1. For fixed C₀ ≤ C,
q_{C₀}(h_C) ≤ −η, and q_{C₀} = (C₀−γ) − ⟨T_{C₀}·,·⟩ with T_{C₀}
compact. Passing to the limit:

    (C₀−γ) − ⟨T_{C₀}h, h⟩ ≤ −η.

If h = 0, this fails for C₀ > γ. So h ≠ 0. For C₀ ≥ γ and ‖h‖ ≤ 1,
q_{C₀}(h) ≤ (C₀−γ) − ⟨T_{C₀}h,h⟩ ≤ −η. By monotone convergence,
E_S(h) − γ‖h‖² = sup_{C₀} q_{C₀}(h) ≤ −η < 0, contradicting the
hypothesis. ∎

This is exactly R162_2602 Thm 3's type: the positive part P_C is
"E_S at high frequency", and its positivity is trivial because the cut
was made by hand. That cut adds no content. **E1.**

### 4.4 First new window (PROVED from CITED; no new content)

Let S = {∞,2}. For T ∈ (½log 2, ½log 3] the only prime with log p < 2T
is p = 2. Paper 47 Thm C gives λ_min(A_{½log3}|P_T) ≥ 8.8577·10⁻⁵
(`CITED`, machine-certified). By extension by zero (R162_2602 Thm 6(a))
the same bound holds for every T ≤ ½log 3. By Thm 4.3(ii), for each such
T there is C(T) with

    R'_{C(T)} ≥ 4·10⁻⁵ on P_T   (in A_T's normalization),

and hence n₋(R'_C|P_T) = 0. In particular the bound "at most one
negative direction, aligned with ∫h" holds trivially, with δ > 0 in
R183.017's sense.

This is `PROVED` modulo the A_T ↔ E_S dictionary (§Review, point 2). It
is not a new positivity proof: it is **deduced** from Thm C. C(T) is not
explicit.

## 5. The missing lemma (self-contained)

**Lemma (L-C), OPEN.** Let S = {∞} ∪ {p < e^{2T}},
m_S(s) = 2θ'(s) − Σ_{p∈S} σ_p(s log p) and K_T = {h ∈ L²(−T,T) :
∫h e^{±t/2} = 0, ∫h = 0}. There exist C > 0 and γ > 0, **given
explicitly and proved without using Weil positivity**, such that

    sup_{h∈K_T, ‖h‖=1} (1/2π)∫_R (C − m_S(s))_+ |ĥ(s)|² ds ≤ C − γ.

Equivalently: the time–frequency concentration operator (Landau–
Pollak–Slepian type) with time window I_T and spectral weight
(C − m_S)_+, compressed to K_T, has norm ≤ C − γ.

* By Thm 4.3, (L-C) for every T ⟺ E_S ≥ γ_T > 0 on K_T for every T
  (D by windows, with a gap). That is, (L-C) for every T is D.
* For T ≤ ½log 3 (S = {∞,2}) it is true, by §4.4, but only via
  certificate.
* (L-C)'s new content is the shape of the problem: T_{I_T}(g_C) is
  positive, trace class, with ≈ (2T)(2s_C)/2π significant eigenvalues
  (s_C = sup{s : m_S(s) < C}). It is a finite-effective-dimension prolate
  problem, with a semilocal spectral weight. **Here the prolate operator
  naturally reappears.** If CCM's W_{λ,S}, or an analogue, commuted with
  T_{I_T}(g_C) (a semilocal "Slepian miracle"), (L-C) would reduce to
  counting eigenvalues of a differential operator. For a non-polynomial
  weight this is OPEN and probably false.
* (L-C) must use that S contains every p < e^{2T}. Deleting a
  prime changes m_S, and R162_2602 Thm 4(b)'s deletion falsifier
  applies to any proof not using this.

## Status

```text
CCM 2310.18423: semilocal Sonin ≅ archimedean via θ_S (not unitary);
  semilocal prolate W_{λ,S} only formal; no semilocal positivity           CITED
m_S = 2·(phase of E_S=∏_{v∈S}L_v(½+is))'; E_S not Hermite–Biehler          PROVED
Thm 3.1: every trace-type positive part = multiplier ρ_P ≥ 0               PROVED
Lemma 3.2(a) finite n₋ if φ ≥ c>0 at ∞; (b) exact limit on pairs           PROVED
Control: (b) reproduces −log2/√2 of R183.018 Thm 5.1                        PROVED
Prop 3.3 sandwich ρ_S ∈ [|D|²/C_D, |D|²/c_D]·ρ_∞                           PROVED
Lemma (CF-S) ρ_S − ρ_∞ → 0                                                   OPEN (Christoffel heuristic)
Thm 3.4 CCM semilocal Sonin: n₋(R') = ∞ for T>½log2, S∋2                   NO-GO CONDITIONAL on (CF-S)
P_C = T((m_S−C)_+): absorbs primes, R'_C bounded, finite n₋                 PROVED
R'_C on the pair family → C > 0 (does not die)                              PROVED
Thm 4.3: E_S ≥ γ on K ⟺ (∀γ'<γ ∃C) R'_C ≥ γ'                                PROVED, E1 (R162_2602 Thm 3 type)
S={∞,2}, T ≤ ½log3: n₋(R'_C|P_T)=0 for some C                               PROVED from Paper 47 Thm C (CITED); not new
Explicit lemma (L-C) without Weil positivity                                 OPEN (for every T ⟺ D)
RH / row D                                                                   OPEN
```

## Review points

1. **Theorem 3.1 and the dictionary.** The identification |ĝ(s)|² = |ĥ(s)|²
   in the scaling spectral variable of L²(X_S)^{K_S} uses CC's conjugation
   Δ^{1/2} and the unitarity of CCM's U_S. If there were a shift
   s ↦ s ± i/2, μ_P would no longer be the density compared with m_S. This
   must be checked against CCM (essl0)–(ms0) and R183.018 §1.
2. **§4.4.** It assumes that Paper 47's A_T is R183.015's E_S restricted
   to P_T up to a positive factor, and that the polar terms vanish on
   primitives. A normalization discrepancy only changes the constant
   γ, not the sign, but it must be checked against Paper 47's def:W (rule).
   The monotonicity in T via extension by zero is R162_2602 Thm 6(a).
3. **Thm 3.4 depends on (CF-S), which is unproved.** The direct proof
   with K_∞(·,s) gives error O(1), of the same order as the prime
   amplitude. Hence, strictly, the NO-GO for CCM's semilocal Sonin is
   CONDITIONAL. It cannot be excluded that ρ_S has a Bohr component at
   frequency log 2 of the right sign. If it did, with coefficient
   ≥ +log 2·2^{−1/2}, the candidate would not die on this family. This
   would be decided by a numerical computation of ρ_S for S = {∞,2} at
   |s| ∈ [50,500], but this has not been done (rule: numerics only if
   strictly necessary).
