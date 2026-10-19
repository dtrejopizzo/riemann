# R183.026 — Szegő falsifier: the archimedean band and lemma L2

Primary source: CC 2006.13771, (75)–(77), (82)–(89), Lemma 5.4,
(99)–(104), Prop 5.5, §6 (text in `phase-137-.../cc_2006.13771_text.txt`). Normalizations from
R183_018 §3, R183_022 (m(s)), R183_024 §2.5, §3.4, §4.

## 0. Verdict

1. **The statement's paradox is resolved against the reading "ε is positive definite".**
   ε is **not** a sum of autocorrelations ⟨ξ,ϑ(ρ^{-1})ξ⟩. It is a **cross coefficient**
   between ξ_n (supported on [−1,1]) and ζ_n (supported on |x| ≥ 1). Its transform ε̂ **changes
   sign**: ε̂ > 0 in the band |s| < s_m and ε̂ < 0 at high frequency. So neither (i) nor
   "−E negative semidefinite of infinite rank" holds. (PROVED, §1–§2.)
2. **The archimedean remainder lies below W_∞:** R_∞ := −E = W_∞ − Son ≤ W_∞ on every
   test (CC Thm 4.7). Hence n₋(R_∞|I_T) ≥ n₋(W_∞|I_T) on primitives. W_∞ has symbol
   m(s)/2π < 0 for |s| < s_m ≈ 6.290. (PROVED.)
3. **CC's single-direction structure dies by itself, with no primes.** Numerically (Rayleigh–Ritz,
   §4): n₋(W_∞ on primitives of [−T,T]) is 0 for T ≤ T₁ ≈ 0.5963, ≥ 1 for T > T₁, and ≥ 2 for
   T > T₂ ≈ 0.8033. From T₂ on, CC's operator K_{I_T} (104) has **at least two
   eigenvalues > 1**. Asymptotically n₋ ≈ 4.004·T − 2. (Numerical, not certified; the reduction
   is PROVED. The asymptotics is CONDITIONAL on Landau–Widom.)
4. **L2:** the archimedean band **cannot be compensated with fixed S**. For S = {2} and S = {2,3}
   the semilocal correction **worsens** the band: θ'_S(0) = −8.72 and −11.72, and the measure of
   {θ'_S < 0} goes from 12.58 to 28.14 and to 47.11. **But this does not refute C_T**, because C_T uses
   S = S(T), which grows. For S(T), the lower bound reduces to n₋(W|I_T), which is 0 under RH. The
   falsifier of R183_024 §3.4 is only valid for fixed S. For C_T, the question shifts to the
   density of Son_{S(T)} in the zero gap (−γ₁, γ₁). (OPEN, §5.)

## 1. The exact form of ε (from the source)

CC (84), for ρ ≥ 1: ε(ρ) = Σ_n λ(n)(1−λ(n)²)^{-1/2} ⟨ξ_n | ϑ(ρ^{-1}) ζ_n⟩. Here
ξ_n = P_1φ_n/‖·‖ is supported on |x| ≤ 1, and ζ_n = ψ_n/‖ψ_n‖ with ψ_n = P F ξ_n
supported on |x| ≥ 1 (Prop 4.5). With ζ_n = λ(n)(1−λ²)^{-1/2} ξ_n^{an} on [1,∞) (text
preceding (99)) one obtains Lemma 5.4's form:

    ε(ρ) = Σ λ²/(1−λ²) · ρ^{1/2} ∫_{ρ^{-1}}^{1} ξ_n^{an}(x) ξ_n^{an}(ρx) dx,   ρ ≥ 1.

**Remark 1.1 (PROVED).** The integrand is ξ_n(x)·ζ_n(ρx). The first factor lives only
on [0,1] and the second only on [1,∞). That is,
ε(ρ) = Σ c_n ⟨1_{[0,1]}ξ^{an}, ϑ(ρ^{-1}) 1_{[1,∞)}ξ^{an}⟩. It is a **cross** coefficient
between two orthogonal vectors, not ⟨v,ϑ v⟩. Bochner does not apply. By (82), the branch
ρ < 1 of the same coefficient is **identically 0**. The even function ε(ρ^{-1}) = ε(ρ)
is thus the **symmetrization** of the cross coefficient, not a matrix coefficient of
ϑ. Equivalently, by (89):

    ε = δ − Σ λ(n)² ⟨ζ_n | ϑ(·) ζ_n⟩ ,

a difference between δ and a positive-definite function. There lies the error in the
hypothesis "σ_ε ≤ 0 everywhere": the expansion mixes the branches.

## 2. The sign of ε̂ (PROVED)

Convention: E(h) = ∫ c_h(x) ε(e^{|x|}) dx = (1/2π)∫ |ĥ(s)|² ε̂(s) ds, with
ε̂(s) = ∫ ε(e^{|x|}) e^{−isx} dx (as a tempered distribution; ε is continuous and
bounded by R183_020).

**Prop 2.1 (lower bound in the band).** For all s, ε̂(s) ≥ −m(s)/2π in the sense of
distributions, with m(s) = Re ψ(¼ + is/2) − log π. In particular, ε̂ ≥ −m/2π > 0 for
|s| < s_m.

*Proof.* CC (83) gives Son(f) := Tr(ϑ(f)S) = W_∞(f) + E(f) for every f ∈ C_c^∞(R_+^*). For
f = h*h^* one has Son(f) = ‖Sϑ(h)‖²_{HS} ≥ 0 (Thm 4.7). The form W_∞ has symbol m/2π, the
archimedean term of the explicit formula (R183_022 §1). Thus σ_Son := m/2π + ε̂ is a
positive distribution on |ĥ|², and by Bochner–Schwartz it is a positive measure. ∎

**Prop 2.2 (high frequency; PROVED given H_dec).** ε(e^{|x|}) = φ(|x|) with
φ'(0^+) = ε'(1^+) ≈ 22.9965 (Lemma 5.4). If φ, φ', φ'' ∈ L¹(0,∞) (hypothesis H_dec), two
integrations by parts give ε̂(s) = −2ε'(1^+)/s² + o(s^{−2}) < 0 for large |s|. This is
consistent with (102): (s²+¼)ε̂ → −2ε'(1^+), i.e. K_I's symbol k̂ tends to 0 (K compact).

*H_dec (sketch, CONDITIONAL on uniformity in n).*
ξ_n^{an}(y) = λ^{-1}∫_{-1}^1 ξ_n(t)e^{−2πiyt}dt, with ξ_n(±1) ≠ 0, equals
A_n sin(2πy)/(πy) + O(y^{−2}). Substituting u = ρx:
ρ^{1/2}∫_{1/ρ}^1 ξ_n(x)ξ_n^{an}(ρx)dx = ρ^{−1/2}∫_1^ρ ξ_n(u/ρ)ξ_n^{an}(u)du = O(ρ^{−1/2}).
Thus ε(e^{x}) = O(e^{−x/2}). The sum over n converges by (100) and by the decay of
λ(n)²/(1−λ²).

**Conclusion 2.3.** The remainder's symbol r_∞ = −ε̂ is < 0 for |s| < s_m and > 0 at high
frequency. R183_024 §3.4's datum "r_∞ < 0 on a set of positive measure" is **PROVED without
the hypothesis ε ∈ L¹**.

## 3. Correct reading of CC's structure and correction of R183_018/019/024

* CC (102)–(104): E(Q(g*g^*)) = ⟨g, N_I g⟩ with N_I = −2ε'(1^+)(Id − K_I). In frequency,
  (s²+¼)ε̂(s) = 2ε'(1^+)(k̂(s) − 1). Hence **k̂ > 1 ⟺ ε̂ > 0**. CC's "single negative
  direction" is exactly #{λ_j(K_I) > 1} = 1 for |I| = log 2. It is an index **in L²(I) of g**
  (the "ξ metric"). With ĥ = (½ − is)ĝ, that metric is ‖h‖²_ξ = (1/2π)∫|ĥ|²/(s²+¼):
  **H^{−1} type in h**. It is not equivalent to Son, which is of type ∫|ĥ|² log|s|, nor to L²(h).
* **Correction (PROVED).** R183_024 §2.5 (N_T) requires R' ≥ −b|v⟩⟨v| + c(I − |v⟩⟨v|) **in X**
  (X = Son + L²) with c > 0. This is **false for every T**. The kernel −ε(e^{|x−y|}) is bounded
  on I_T × I_T (R183_020), so R' is Hilbert–Schmidt on L²(I_T). For h_k ⇀ 0 with ‖h_k‖_{L²} = 1
  one has R'(h_k) → 0, while ‖h_k‖_X ≥ 1 and ⟨v,h_k⟩ → 0. The correct formulation is in the
  ξ metric: R' ≥ −b|v⟩⟨v| + c(I − |v⟩⟨v|) in ‖·‖_ξ, which is CC with c = 2ε'(1^+)(1 − λ₂). The
  phrase "equivalent for the index" in R183_024 is correct only for n₋, not for c > 0. R183_018 §6
  uses X and must be changed likewise. R183_019 §2, which uses the ξ metric, is fine.
* With this reading, CC's statement is: "E∘Q ≤ 2ε'(1^+)‖·‖²_ξ except for one direction." It is a
  bound relative to the ξ metric, not "E ≤ Son".

## 4. The archimedean falsifier (no primes)

**Theorem 4.1 (reduction; PROVED).** For every T > 0, on primitive tests
h ∈ C_c^∞(I_T) with ĥ(±i/2) = 0:

    R_∞ = W_∞ − Son ≤ W_∞,   hence   #{λ_j(K_{I_T}) > 1} = n₋(R_∞|I_T) ≥ n₋(W_∞|I_T).

(n₋ does not depend on the metric, because g ↦ h is a support-preserving bijection, CC Prop 3.3.)
Here K_{I_T} is (104) with integration over |v| ≤ 2T.

**Computation 4.2 (numerical, not certified).** Rayleigh–Ritz of (1/2π)∫|ĥ|²m is performed on
h_j = (1 − (x/T)²)P_j(x/T), j < N (N = 30–70), restricted to the codimension-2 subspace
∫h e^{±x/2} = 0. Gauss–Legendre is used with 2000–3000 nodes and s ∈ [0, 600–1500] with step 0.02. The
tail s > 600 is positive and of order s^{−4}log s, hence negligible. Rayleigh–Ritz gives upper
bounds on the eigenvalues, so the counts are **lower bounds** on n₋.

| T | 0.3466 (=½log2) | 0.5 | 0.75 | 1.0 | 1.5 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|---|---|
| n₋(W_∞), primitives | 0 | 0 | 1 | 2 | 4 | 6 | 10 | 14 | 18 |
| λ_min | +0.549 | +0.179 | −0.235 | −0.535 | −0.99 | −1.36 | −2.09 | −2.80 | −3.42 |

The thresholds (bisection) are **T₁ ≈ 0.5963** (|I| ≈ 1.193) and **T₂ ≈ 0.8033** (|I| ≈ 1.607,
e^{|I|} ≈ 4.99). There are three internal controls:
- At ½log 2, n₋ = 0 is obtained, agreeing with CC's main theorem (W_∞ ≥ 0 there).
- Without the two primitive conditions, the count is n₋ + 2, because the two pole
  directions are negative.
- T₁ ≈ 0.596 coincides with phase 155's archimedean threshold ≈ 0.596 (round 3). It is an
  independent cross-check.

The observed slope is 4.0, equal to 2s_m/π = 4.0042 (Landau–Widom: (2T/2π)·|{m<0}|).

**Corollary 4.3.** For T > T₂ ≈ 0.80, K_{I_T} has ≥ 2 eigenvalues > 1. Asymptotically the number
is ≳ (2s_m/π)T − 2 (CONDITIONAL: Landau–Widom for a continuous symbol, bounded below and
growing logarithmically; the table confirms it). **CC's rank-one mechanism does not extend
beyond |I| ≈ 1.61 using only archimedean data.** It is the reverse of the theorem: positivity in
larger windows has to come from the primes. The initial prediction ("≈4T, equal to 1 at
T ≈ 0.25") is the asymptotics. The real count has an offset of −2 due to the primitive conditions
and the transition region, so the first T with 2 forced directions is ≈ 0.80, not 0.5.

## 5. L2 and the C_T conjecture

**Prop 5.1 (fixed S; PROVED the reduction, CONDITIONAL the asymptotics).** Let S be finite and
fixed, and let E_S be the semilocal Weil form, with symbol θ'_S/2π (R183_016). Then Son_S ≥ 0 gives
n₋(E_S − Son_S | I_T) ≥ n₋(E_S | I_T) ~ (T/π)|{θ'_S < 0}|. This does not use I_S. The computations
(script in the scratchpad, grid step 10^{−4} on [0,400]) are:

| S | θ'_S(0) | \|{θ'_S<0}\| | last negative s | slope /π |
|---|---|---|---|---|
| ∞ | −5.372 | 12.58 | 6.29 | 4.00 |
| {2} | −8.719 | 28.14 | 172.3 | 8.96 |
| {2,3} | −11.720 | 47.11 | 372.0 | 15.00 |

The prime correction is −2Σ log p Σ_k p^{−k/2}cos(ks log p). Its maximum negative value is at s = 0
and is periodic, so it **enlarges** the negative set, which extends out to where
m(s) < 2Σ log p/(√p − 1). **It does not compensate the band: it worsens it.** Thus R183_024 §3.4 is PROVED
for fixed S (lower bound; asymptotics CONDITIONAL). Moreover it is no longer necessary to assume
|δε_S| is small.

**Prop 5.2 (S = S(T): the falsifier does not reach; PROVED).** If S = S(T) ⊇ {p < e^{2T}}, then
E_{S(T)}|I_T is the true Weil form W|I_T, and under RH n₋(W|I_T) = 0 on primitives. Prop 5.1's
bound reduces to 0. **The archimedean band alone does not refute C_T.** What is refuted is
(a) the rank-one archimedean mechanism beyond T₂ and (b) any version of
C_T with fixed S.

**Reformulation (OPEN).** With S(T), N_T requires n₋(W − Son_{S(T)} | I_T) ≤ 1. Under RH, W has
"symbol" Σ_γ δ_γ, which is null in the gap (−γ₁, γ₁), γ₁ ≈ 14.13. The following is proposed
(CONDITIONAL, with a sketch proof via prolate concentration and R183_022's Thm 3.3): if there exist
η > 0, an interval J ⋐ (−γ₁, γ₁), and T₀ such that the density σ_{Son_{S(T)}} ≥ η on J for
T ≥ T₀, then n₋ ≳ (T/π)|J| and N_T fails. Hence **N_T forces the density of the semilocal
Sonin space to tend to 0 in the zero gap**. It is a concrete, checkable prediction from source
data (CCM). That is now where L2's content lies.

## Status

| Statement | Label |
|---|---|
| ε is the symmetrization of a cross coefficient ξ_n/ζ_n, not positive definite (Rem 1.1) | PROVED (from CC (82),(84),(89)) |
| ε̂ ≥ −m/2π; ε̂ > 0 for \|s\|<s_m (Prop 2.1) | PROVED (CC Thm 4.7, Bochner) |
| ε̂ ~ −2ε'(1^+)/s² < 0 at high frequency | PROVED given H_dec; H_dec CONDITIONAL (uniformity in n) |
| k̂>1 ⟺ ε̂>0; CC's index lives in the ξ metric (H^{−1} type in h) | PROVED |
| N_T "with c>0 in X" is false ∀T; R183_018 §6 and R183_024 §2.5 must be corrected to the ξ metric | PROVED |
| #{λ(K_{I_T})>1} ≥ n₋(W_∞\|I_T) (Thm 4.1) | PROVED |
| T₁≈0.5963, T₂≈0.8033; n₋ ≈ 4T−2 | numerical, not certified |
| Asymptotics (2s_m/π)T | CONDITIONAL (Landau–Widom, CITED) |
| Fixed S: the prime correction worsens the band; n₋ ≳ (T/π)\|{θ'_S<0}\| | PROVED (reduction) / CONDITIONAL (asymptotics) |
| The band refutes C_T with S(T) | NO-GO for the falsifier (does not reach) |
| N_T ⟹ density of Son_{S(T)} → 0 in (−γ₁,γ₁) | CONDITIONAL / OPEN |

Nothing here proves RH nor closes D. The purely archimedean rank-one CC route is bounded to
|I| ≲ 1.61.

## Review points

1. **Normalization of W_∞.** The symbol m(s)/2π of the explicit formula with
   ĥ(s) = ∫h e^{isx} is used. If CC (53) differs by a positive constant, only scales change, not
   n₋. An additional term f(1)·const would shift T₁ and T₂. The control at ½log 2 (n₋ = 0) and
   the agreement with phase 155's 0.596 rule this out in practice, but it should be checked
   against CC (53) literally.
2. **Positivity of Son.** Prop 2.1 uses Tr(ϑ(h*h^*)S) = ‖Sϑ(h)‖²_{HS}, finite. CC Thm 4.7 states
   this for every f ∈ C_c^∞, with no support restriction. It should be checked that (83) was not
   proved only for supp f ⊂ [½, 2].
3. **K_{I_T} for |I| > log 2.** CC (104) is derived only for |I| ≤ log 2. The extension (kernel on
   |v| ≤ 2T) is the natural compression, but (102) changes if f does not vanish outside
   [−log2, log2]. Thm 4.1 is stated for R_∞ = −E in h, which does not depend on this. The
   translation to "eigenvalues of K" is what needs review.
4. **Numerics.** Rayleigh–Ritz has no interval arithmetic. The lower bounds on n₋ depend on the
   quadrature (x·s ≤ 3000 rad with 2000–3000 nodes) and on the cutoff in s. Before labeling PROVED,
   a certificate (explicit basis and bounded quadrature error) would be needed.
5. **Prop 5.2** assumes RH only to show that the falsifier does not reach. Nothing is claimed in
   the opposite direction.
