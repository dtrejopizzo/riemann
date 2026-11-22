# R183.031 — Gap requirement and prolate spectrum: theorem, source, and NO-GO

Input: R183.021, 022, 024, 026, 027, 028. Sources: Connes–Moscovici,
PNAS 119 (2022) e2123174119 (local PDF, 7 pp.); CCM 2310.18423v2 (local tex); Paper 46
(thm:Z, thm:finZ). Numerics: a single sanity check (scratchpad, §3.3). Neither RH nor the
closure of D is claimed.

## 0. Verdict

* **Theorem 1 (PROVED, except for two CITED inputs).** Let E_{S(T)} = P_T + R_T, with P_T ≥ 0 a
  multiplier of density ρ_T and n₋(R_T | prim) ≤ N₀ for every T. Then, on every compact
  K ⊂ ℝ at positive distance from the real ordinates of zeros, ρ_T → 0 in Landau measure:
  |{s ∈ K : ρ_T(s) > τ}| ≤ πN₀'/T + o(1) for every τ > 0, with N₀' = N₀ + 2·#(zeros off the
  line). This holds in particular on the gap (−γ₁, γ₁). The version under RH is clean (N₀' = N₀).
  Without RH one uses that the hypothesis itself forces a finite number of zeros off the
  line (CITED Weil/Yoshida), whose contribution has finite rank. Consequence: ρ_T ds can only
  accumulate mass near the ordinates of the zeros. **P_T has to know the zeros at
  every height**, not only in the low gap.
* **Connes–Moscovici 2022 (CITED, with pages).** What is proved is a Weyl law, not a
  localization. The operator is W_λ = −∂(λ²−x²)∂ + (2πλ)²x² on L²(ℝ). Its self-adjoint extension is
  the unique one commuting with the Fourier transform. What "matches" the zeros is the
  counting function of the negative spectrum, and only to order O(log E). That counting function is the
  principal term θ(E)/π of Riemann–von Mangoldt, which is **archimedean**. That the individual
  eigenvalues resemble the zeros is **only numerical** (Figs. 1–2). The semilocal analogue
  W_{λ,S} is formal in CCM. Primes appear nowhere.
* **NO-GO of the prolate route (PROVED, structural).** By R183.021 Thm 3.1, a positive part
  only enters through its diagonal density in the scaling variable s. Every Landau–Widom or
  Bonami–Karoui-type estimate is modulation-invariant, because it depends only on
  |I|·|J|. Hence it cannot distinguish the gap (−γ₁, γ₁) from a band of equal length containing
  zeros. The only source datum distinguishing bands is the prime part of m_{S(T)}. Its smoothing at
  window resolution is, by the explicit formula (Paper 46 thm:Z), exactly the sum over
  zeros. Proving the gap property for an admissible P_T is equivalent to proving one-sided
  inequalities for Σ_γ ŵ(τ−γ). That is Theorem Z's certificate, which is ⟺ RH.
  **The gap property is not separable from D.**
* **P_C (R183.021 §4).** Its density is (m_S − C)_+. With C fixed, Theorem 1 excludes it whenever
  m_{S(T)} > C + τ on a nonzero fraction of the gap. This is CONDITIONAL on a fixed-interval
  mean-value statement, (MV_J), which is unproved. Numerically it holds massively: the fraction is ≈ ½ and
  grows with T. Hence (L-C) ∀T forces C_T → ∞.
  **(L-C) ∀T is a reformulation of D** (confirmed; §3).

## 1. The requirement as a theorem

### 1.1 Setup

* I_T = (−T, T), and h ∈ C_c^∞(I_T) primitive (ĥ(±i/2) = 0, as in R183.022 §3).
* S(T) ⊇ {p < e^{2T}}. Thus E_{S(T)}(h) = W(h), the full Weil form, because c_h = h * h̃
  vanishes for |x| ≥ 2T.
* Explicit formula (CITED Weil 1952; normalization verified in R183.027 §2):

      E_S(h) = Σ_ρ ĥ(γ_ρ) · conj ĥ(conj γ_ρ),    ρ = ½ + iγ_ρ.        (1.1)

* P_T(h) = (1/2π) ∫ ρ_T(s) |ĥ(s)|² ds, with ρ_T ≥ 0 locally integrable (R183.021 Thm 3.1).
* n₋(Q) is the maximal dimension of a subspace of C_c^∞(I_T) ∩ prim where Q < 0.
* **Metric.** n₋ is an algebraic invariant of the form on the vector space, so it is
  the same in the ξ metric and in L². The metric only changes the closure. If n₋ is requested on the
  closure in the ξ metric, the index is the supremum over dense finite subspaces, and coincides
  by continuity of the form in that metric. The quantitative statement below uses L² only
  to normalize the packets; the conclusion about n₋ does not depend on the metric.

### 1.2 Reduction of off-line zeros

**Lemma 1.1.** Suppose n₋(R_T) ≤ N₀ for every T. Then:

(a) **(PROVED.)** n₋(W | prim ∩ C_c^∞(I_T)) ≤ N₀ for every T. One has W = P_T + R_T with
P_T ≥ 0, and the windows I_T are nested.

(b) **(CITED: Weil 1952; Yoshida 1992, "finite index ⟺ finitely many off-line zeros".)** By
(a), there are only finitely many zeros off the line, in number k ≤ N₀ except for multiplicity. The
exact statement must be verified in the source; the local corpus only cites Yoshida for the positivity
on T ≤ ½log2.

(c) **(PROVED.)** Write (1.1) as Z_on + Q_off, where Z_on(h) = Σ_{γ∈ℝ} |ĥ(γ)|² ≥ 0 and
Q_off is the sum over the k non-real zeros. Q_off is a sum of products of two linear
functionals, so it has rank ≤ 2k. Hence n₋(Z_on − P_T) ≤ n₋(R_T) + 2k ≤ N₀' := N₀ + 2k.

Under RH, k = 0 and (b) is unnecessary. This is the honest form of R183.027's caveat: the
factor e^{T|Im γ|} that invalidated R183.022 Thm 3.3 only affects Q_off, and here Q_off is absorbed as
finite rank **instead of** being bounded.

### 1.3 Theorem 1

**Theorem 1.** Under Lemma 1.1's hypothesis, let K ⊂ ℝ be a compact set with
d := dist(K, {γ ∈ ℝ : ζ(½+iγ) = 0}) > 0. Let A ⊂ K be a finite union of intervals and τ > 0. If
ρ_T ≥ τ on almost all of A, then

    (T/π)·|A| ≤ N₀' + o_{τ,d,K}(T)      (T → ∞).

Hence |{s ∈ K : ρ_T(s) ≥ τ}| → 0 for every τ > 0, in the sense of unions of intervals,
with rate π N₀'/T + o(1).

Since (−γ₁, γ₁) contains no ordinates of zeros, neither real (CITED, classical computation)
nor non-real, this gives in particular the quantitative version of R183.026 §4 and R183.027's requirement:
**(T/π)·|J| · 1{inf_J ρ_T ≥ τ} ≤ N₀' + o(T).**

*Proof (PROVED).*

1. **Packets.** Fix L > 0 large and a window w ∈ C_c^∞(−L/2, L/2), L²-normalized,
   with |ŵ(u)| ≤ C_K L^{1/2} (1 + L|u|)^{−K}. Take an orthonormal Wilson/Gabor basis
   (Daubechies–Jaffard–Journé), localized in time within I_T at scale L and in frequency at
   scale 1/L. Let V be the subspace generated by the atoms whose frequency center lies in
   A' := {s ∈ A : dist(s, ∂A) ≥ L^{−1/2}}. Then

       dim V = M = (2T/2π)·|A|·(1 − O(L^{−1/2}/|A|) − O(L/T)).

   Pass to V ∩ prim, which has codimension ≤ 2. Wilson atoms have slightly larger support
   than L; they are truncated to I_T with dimension error O(L/T).
2. **Bound on P.** For h ∈ V, ĥ's mass outside A is ≤ δ_L‖h‖², with δ_L → 0 as L → ∞,
   by ŵ's decay and the L^{−1/2} distance to the boundary. Hence
   P_T(h) ≥ τ(1 − δ_L)‖h‖².
3. **Trace bound on Z_on.** Z_on|_V is ≥ 0 and

       tr(Z_on|_V) = Σ_{atoms} Σ_γ |ĥ_atom(γ)|² ≤ M · ε(L, d),
       ε(L, d) = C_K L Σ_{γ real} (1 + L·dist(γ, A'))^{−2K}.

   By the zero density (log γ / 2π) and dist ≥ d, ε(L, d) → 0 as L → ∞, with d and K fixed.
   The number of eigenvalues of Z_on|_V exceeding τ/2 is ≤ 2Mε/τ.
4. **Conclusion.** On a subspace of V of dimension ≥ M(1 − 2ε/τ) − 2 one has
   Z_on − P_T ≤ (τ/2 − τ(1−δ_L))‖h‖² < 0. Choose L with 2ε/τ + δ_L small, then let T → ∞.
   By Lemma 1.1(c), M(1 − o(1)) ≤ N₀'. ∎

**Corollary 1.2 (PROVED, under the same hypothesis).** Suppose further that the masses
∫_K ρ_T ds are bounded in T. Then every vague limit of ρ_T ds is supported on the closed
set of real ordinates of zeros. This is "P_T knows the zeros" as a statement.
Remark: the gaps between consecutive zeros at height t have length ≍ 2π/log t > 0, so
**every gap** is an admissible K.

**What survives without RH or (b).** Theorem 1 with a single packet of support L is unconditional.
E_S is translation invariant, so e^{−iγt_j} and its conjugate cancel in
ĥ(γ)·conj ĥ(conj γ), and the growth factor is e^{L|Im γ|/2} with L fixed. What does **not**
survive is the count with many packets: the cross terms between packets separated by
|t_j − t_k| ~ T carry e^{|Im γ||t_j−t_k|}. Without Lemma 1.1(b), controlling them is information about
the zeros.

## 2. Connes–Moscovici 2022: what exactly is there (CITED)

Source: `00-references/prolate-and-zeta-cycles/connes-moscovici-2022-the-uv-prolate-spectrum-matches-the-zeros-of-zeta.pdf`,
PNAS 119(22) e2123174119, 7 pp.

1. **Operator** (p. 1, eq. [1]): (W_λ ξ)(x) = −∂_x((λ²−x²)∂_x ξ) + (2πλ)² x² ξ, defined on S(ℝ)
   as W_min.
2. **Extension** (p. 2–3, Thm 1.6):
   * W_sa is the **unique** self-adjoint extension of W_min commuting with the Fourier
     transform e_ℝ, with Sturm–Liouville-type boundary conditions at ±λ.
   * Its spectrum is discrete, simple on the negative part, and unbounded in both directions.
3. **Sonin** (p. 3–4, Cor. 2.2):
   * Eigenfunctions of negative eigenvalue lie in the Sonin space.
   * Sonin = orthogonal complement of the classical prolates on [−λ, λ] and their transforms.
   * It is explicitly **not** claimed that the entire restriction to Sonin is negative: "supported by
     numerical evidence … only finitely many exceptions".
4. **What "matches" means** (p. 4, Prop. 3.2; p. 5, Thm 5.1):
   * Prop. 3.2 is a **semiclassical approximation** (phase-space area), not a counting theorem for
     W_sa. It gives 2σ(E, λ) with σ ≈ (E/2π)(log(E/2π) − 1) + log 4 − 2 log λ + λ² + o(1).
   * Thm 5.1 (λ = √2) is a theorem for the Dirac root 2D̸: N(E) ≈ (E/2π)(log(E/2π) − 1)
     − (log E)/2π + O(1). The "delicate" part is described as a refinement of the
     semiclassical computation; its proof is not given in full in the text.
   * The match with the zeros is thus that of the principal term of Riemann–von
     Mangoldt, θ(E)/π, to precision O(log E).
   * The eigenvalue-by-eigenvalue comparison is **numerical** (p. 5–6, Figs. 1–2, "one can use the
     computer").
   * Positives (p. 6, §6.B): the eigenvalues χ(2n) of the classical prolates, plus at most
     finitely many others; that there are no others is a **conjecture**.
5. **Reading (PROVED, elementary).** The principal term θ(E)/π is the integral of the
   archimedean density 2θ'(s)/2π = m(s)/2π of R183.021 §3.0. CM's result is then: **the Weyl
   law of the prolate operator reproduces the archimedean density m**, the same one that is > 0 on
   (6.3, γ₁) and that Theorem 1 forces to vanish. CM contains no primes, hence no
   S(E), nor any information distinguishing (−γ₁, γ₁) from another band except through m.

## 3. The prolate candidate and the constructive question

### 3.1 Density of the prolate positive parts (PROVED)

**Archimedean case, S = {∞}.**
* W_sa's positive spectral projection is 1 − Π_Son, except for §2.3's finite ambiguity.
* By R183.021 Thm 3.1, its contribution is the diagonal density of U(1 − Π_Son)U^*.
* Π_Son's is ρ_∞, with 2πρ_∞ = m + ε̂ (CC (83), R183.018 Prop. 3.1).
* Both are independent of T and > 0 on (s_m, γ₁) ⊃ (6.3, 14.13) (R183.026 §1).
* By Theorem 1, **none** serves as P_T for large T. This includes the fractions η·Son,
  already refuted in R183.027.

**Semilocal case.**
* W_{λ,S} = (H+½)² + λ²N_S is formal (CCM, text before Rem. care; R183.021 §1).
* There is neither self-adjointness nor a spectrum. Its "positive part" is not defined in the source.
* If defined via functional calculus, its density is the diagonal of a spectral projection in
  the scaling variable. By the reproducing property on the window (U L²(I_T) = PW_T, with
  constant diagonal T/π), one has 0 ≤ ρ ≤ T/π.

### 3.2 The theorem that would be missing, and why it is not enough

The suggested statement is: "W_{λ,S(T)} on the window has no eigenvalue (on √ scale) in
(−γ₁, γ₁) for large T." There are two objections.

**(i) Wrong object (PROVED).** W's eigenvalues live in the prolate variable, and
Theorem 1 restricts the scaling density ρ_T. To translate one into the other, one also needs:

**(M2) Uniform spectral localization.** Each eigenfunction of W_{λ,S(T)} with eigenvalue −μ would
have to have scaling spectral measure concentrated at ±√μ + O(1/L), uniformly in T.

All semiclassical theory gives is a WKB analogy in the ultraviolet: eigenfunctions
behave like x^{−½±is} as x → ∞. It gives nothing at low frequency, exactly the regime
of the gap.

**(ii) Invariance of the tools (PROVED).** Landau–Widom (plateau/drop), Landau–Pollak–
Slepian, and Bonami–Karoui count eigenvalues of time–frequency concentration as a function of
|I|·|J| and of log(·). They are invariant under modulation h ↦ e^{iat}h, which shifts J to J + a.
* Any eigenvalue bound for a prolate operator built only with those tools
  holds equally on J = (−γ₁, γ₁) and on a band J + a of equal length containing zeros.
* On J + a, Theorem 1 does not require ρ_T → 0. The bound therefore cannot be the one giving
  the gap, unless ρ_T → 0 everywhere. That makes P_T trivial and leaves R_T = E_S − o(1),
  i.e. D.
* The only source ingredient breaking modulation invariance is the prime part Σ_p σ_p(s log p) of
  m_S.

**Proposition 3.1 (NO-GO, PROVED given Paper 46's thm:Z [CITED]).** Let P_T ≥ 0 be a multiplier
built from source data. Suppose its positivity is proved from the source and that
Theorem 1's gap property is deduced from a bound on the density of the form

    ρ_T(s) ≤ (m_{S(T)} ∗ ŵ_T)(s) + o(1)  on K,                     (3.1)

where ŵ_T is a kernel ≥ 0 with w_T supported on (−2T, 2T) and w_T(0) = 1 (the only way
to compare ρ_T with the zero density at window resolution). Then:
* By thm:Z(ii), the right side of (3.1) is f_{w_T}(s) = Σ_γ ŵ_T(s − γ) plus polar terms.
* That it be small on K is a statement of absence of zeros at resolution ~1/T near K.
* That the certificate be ≥ 0 on all of ℝ for every T is thm:Z ⟺ RH.

Conversely, no bound on ρ_T not going through m_S's prime part distinguishes K from K + a.

**Conclusion of §3.2.** Proving the gap property for an admissible P_T, from source data,
is proving one-sided inequalities on the smoothed sum over zeros. This is **localizing
zeros** in Paper 46's sense. **NO-GO** for the prolate route as an independent mechanism.

### 3.3 P_C = T_{I_T}((m_S − C)_+) and lemma (L-C)

* P_C's density is (m_{S(T)} − C)_+/2π, pointwise. The compression sees the whole symbol:
  the positive part is not linear, so window smoothing does not neutralize it.
* **Proposition 3.2 (PROVED).** If (L-C) holds ∀T with fixed C, Theorem 1 gives
  |{s ∈ K : m_{S(T)}(s) > C + τ}| → 0 on every admissible K, in particular on the gap.
* **(MV_J), OPEN.** liminf_T |{s ∈ J : m_{S(T)}(s) > C}| > 0 for every C, with J = (−γ₁, γ₁).
  * Montgomery–Vaughan does not help on a fixed interval: the Dirichlet polynomial has length
    e^{2T} ≫ |J|^{−1}.
  * Under (MV_J), (L-C) ∀T forces C_T → ∞.
* **Numerical sanity check** (scratchpad; m_S = 2θ' − 2Σ_{n≤N} Λ(n)n^{−½}cos(s log n), with s ∈ [−13, 13]):

      N = 10³ (T≈3.5):  rms 22,   fraction{m_S > 10} = 0.15
      N = 10⁴ (T≈4.6):  rms 69,   fraction = 0.39
      N = 10⁵ (T≈5.8):  rms 217,  fraction = 0.47
      N = 10⁶ (T≈6.9):  rms 686,  fraction = 0.49

  The rms grows like ≈ √N = e^{T}. (MV_J) holds massively, and C_T would have to grow
  like e^{T}, not like T. Not certified.
* **(L-C) ∀T ⟺ D?** Yes, and it is a reformulation.
  * (⇐) R183.021 Thm 4.3 (E1, PROVED, verified in R183.027).
  * (⇒) C_T is free as a function of T, so (L-C) only requires T_{I_T}(min(m_S, C_T))
    ≥ −(bounded) on ker ℓ. By Thm 4.3 this is equivalent to E_S ≥ γ on K, i.e. to D_T.
  * Theorem 1 adds that fixed C is impossible, CONDITIONAL (MV_J).
* **Relation to Paper 46.**
  * The TK ceiling and thm:finZ say the same thing on the zero side: no finite set of
    zeros carries a flat certificate.
  * Here: no density with fixed Landau mass outside the zeros is admissible.
  * Both are the same rigidity: any certificate working ∀T is infinite at the zeros
    (finZ) and concentrated on the zeros (Thm 1).

## 4. Classification and the only missing theorem

| positive part | density on the gap | does it satisfy the requirement? | status |
|---|---|---|---|
| archimedean Sonin Son (CC) | ρ_∞ > 0 fixed on (6.3, γ₁) | NO | PROVED (Thm 1 + 026) |
| η·Son, fixed η | ηρ_∞ | NO (η_1(T) → 1) | PROVED with Lemma 1.1(b) CITED; previously CONDITIONAL(RH) in 027 |
| semilocal Son_S (CCM) | ρ_S = ρ_∞ + bounded prime correction (sandwich 021 Prop 3.3) | NO, unless the correction cancels ρ_∞ on the gap for every S(T) (that would be (3.1)) | CONDITIONAL (E′); not defined for S ⊋ {∞} as a positive form |
| P_C, fixed C | (m_S − C)_+ with fraction ≈ ½ on the gap | NO | CONDITIONAL (MV_J); massive numerical evidence |
| P_{C_T}, free C_T → ∞ | → 0 | trivially yes | ⟺ D (reformulation) |
| prolate positive part (W_sa or W_{λ,S}) | archimedean: = density of 1−Π_Son > 0; semilocal: undefined | NO (arch.); semilocal with no object | PROVED (arch.) / OPEN with no object |

**The only theorem that would turn Connes's route into a mechanism (OPEN).** Build, using only
source data S(T) (semilocal prolate/Sonin, primes < e^{2T}), a form P_T ≥ 0 whose positivity is
proved from the source and whose density satisfies

    ρ_T ≤ f_{w_T} + o(1)        (concentration at resolution 1/T on the zeros),

together with n₋(E_S − P_T) ≤ N₀. By Prop. 3.1 and thm:Z, this contains Theorem Z's
one-sided certificate for every T, which is ⟺ RH. No weaker version suffices: the
Theorem 1 is necessary and Prop. 3.1 shows that the only source of symmetry breaking is the
explicit formula itself. **Connes's route carried to every T is a reformulation of D, not a
mechanism.** No result of CM 2022 nor CCM 2024 provides that theorem: CM only gives the
archimedean Weyl law, CCM only the Sonin-space isomorphism.

## Status

```text
Lemma 1.1(a),(c) (reduction to finite rank)                           PROVED
Lemma 1.1(b) (finite index ⟹ finitely many off-line zeros)            CITED (Weil/Yoshida; verify statement)
Theorem 1 (gap requirement, Landau count, every gap)                   PROVED given 1.1(b); clean under RH
  version without 1.1(b): one packet yes, counting no                  PROVED / OPEN
Corollary 1.2 (vague limits supported on the zeros)                    PROVED (same hypothesis)
CM 2022: uniqueness of W_sa, Sonin, Weyl law O(log E)                  CITED (semiclassical Prop 3.2; Thm 5.1)
CM 2022: eigenvalue-by-eigenvalue match                                 NUMERICAL in the source
CM's Weyl law = archimedean density m                                  PROVED (elementary)
Archimedean/prolate positive parts fail the requirement                PROVED
NO-GO modulation-invariant tools                                        PROVED
Prop 3.1 (gap from source ⟹ thm:Z certificate)                         PROVED given thm:Z (CITED)
P_C with fixed C excluded                                               CONDITIONAL (MV_J); numerical: C_T ~ e^{T}
(L-C) ∀T ⟺ D                                                            PROVED (reformulation)
Connes's mechanism at every T                                           NO-GO as an independent mechanism
Row D                                                                    OPEN
```

## Review points

1. **Lemma 1.1(b).** It is the only unverified input. It must be checked in Yoshida 1992 or Weil
   that "n₋(W) < ∞ on primitive C_c^∞ ⟹ #zeros off the line < ∞", with this file's support
   normalization. If it fails, Theorem 1 remains CONDITIONAL(RH), as in R183.027.
2. **Proof step 1.** Review the truncation of the Wilson basis to I_T. The basis is not of
   exact compact support, and the dimension bound M carries O(L/T) errors. A safer
   alternative is the prolate functions of (I_T, A) with eigenvalue > ½ (Landau 1967,
   unions of intervals). Step 3's trace bound works the same way.
3. **Prop. 3.1.** Hypothesis (3.1) defines what "proving the gap from the source" means. An
   adversary could propose a P_T whose gap is proved another way. §3.2(ii)'s modulation-
   invariance argument covers prolate tools, but is not a theorem
   about every possible proof. It is a method NO-GO, not a statement NO-GO.
4. **(M2).** W_sa's spectral theory might give localization in s in the ultraviolet. Even
   so it would not touch the low gap.
5. **Numerics.** The grid s ∈ [−13, 13] with step 0.01 does not well resolve oscillations of
   frequency log N ≈ 14. The fractions are indicative, and the rms ≈ √N law seems dominated by
   the coherent peak near s = 0. Before using it, redo it excluding |s| < 1.

## Note (R183_032)

* The final statement "⟺ RH" is downgraded to "⟹ finite index (finitely many
  zeros off the line)". Under RH it holds trivially with P_T = 0.
  Prop 3.1 only gives f_w ≥ −o(1) on compacts away from zeros, not the
  global certificate of thm:Z.
* NO-GO of modulation invariance: HEURISTIC, not a theorem.
* Lemma 1.1(b) (finite index ⟹ finitely many zeros off the line): cited
  with no verified statement; Thm 1 without RH, Cor 1.2, and the η·Son row remain
  CONDITIONAL(1.1(b)).
