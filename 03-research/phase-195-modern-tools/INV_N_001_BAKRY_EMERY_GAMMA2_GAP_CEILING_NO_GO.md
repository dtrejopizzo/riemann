# INV_N_001 — Bakry–Émery Γ₂ / CD(K,N) for the censored jump semigroup of 𝔞_T: exact calculus and a gap-ceiling NO-GO

Phase 195.
Survey candidate B2 (SURVEY_MODERN_UNTRIED). **No sign. No negative value for ζ.** Checked against P46 eq:symbol, eq:form,
𝒫_T (Tate moments A, B), and CA_I_001 §0 (Lévy–Khintchine form, CITED from phase 60).

## 0. Corpus / index check and new reason
- Index: `04_PHASES_100-189.md` G2D-R160_S2 §3.1 **phase-64 CURVATURE**: Γ₂ / CD(0,∞) for the *translation-invariant prime jump generator on ℝ*
  — DEAD (generic for every nonnegative weight). G2C R160_S3 T17 / R160_M10_R1: Doob-variance / CD(0,∞) corridor — REF-D. G2D phase-106:
  Beurling–Deny / positivity-preserving semigroups — DEAD. CA_I_001 Thm 2: Markov class NO-GO under O2. P33-11 entropy/Wasserstein: not used here.
- **New reason (written):** phase 64 worked on ℝ, where Γ₂ is a Schur square of the PD kernel B(ξ,η) and only K = 0 is
  possible. Here the object changes: the *censored* process on I_T = (−T,T) plus the exact *killing potential* W_T, with the two Tate
  constraints; K > 0 is not excluded a priori (finite window, boundary breaks translation invariance), and the question is quantitative
  (K vs. the potential), not qualitative. Result: the quantitative route is closed by a ceiling that does not need K at all (§3).

## 1. Exact decomposition of 𝔞_T into a censored Markov form plus a potential (PROVED)
With ν(u) = e^{−u/2}/(1−e^{−2u}) one has, from ψ(z) = −γ + ∫(e^{−x} − e^{−zx})/(1−e^{−x})dx (x = 2u),
m(τ) = m(0) + 2∫_0^∞(1 − cos τu)ν(u)du, m(0) = ψ(¼) − log π = −5.37218… (κ = 1 in CA_I_001). Using
(1/2π)∫2(1−cos τu)|F̂|² = ∫(F(t)−F(t+u))²dt and −v c_F(u) = ½v∫(F(t)−F(t+u))² − v‖F‖², with the one-sided jump measure
Π(du) = ν(u)du + ½Σ_{n∈𝒩_T} v_n δ_{log n}, and splitting ∫_ℝ dt into "both endpoints in I_T" / "one endpoint out":

  **𝔞_T(F) = E_T(F) + ∫_{I_T} W_T(s)F(s)² ds,**
  E_T(F) = ∫_0^∞Π(du)∫_{t,t+u∈I_T}(F(t)−F(t+u))²dt = ∫_{I_T}Γ(F)dx,
  **W_T(s) = m(0) − 𝒜_T + Π̄(T−s) + Π̄(T+s)**, Π̄(r) = Π([r,∞)), N(r) := ∫_r^∞ν = Σ_{k≥0} e^{−(2k+½)r}/(2k+½).

E_T is the Dirichlet form of the censored (reflected-jump) Markov process on I_T with symmetric kernel
J(x,dy) = 1_{I_T}(y)[ν(|y−x|)dy + ½Σ v_n(δ_{x+log n} + δ_{x−log n})(dy)], invariant measure Lebesgue on I_T. Atoms Λ ≥ 0 ⇒ J ≥ 0.

## 2. Γ and Γ₂ exactly (PROVED algebra; for ν first truncated at ε, finite total rate q(x) = J(x,I_T), then ε→0, ARGUED standard)
L f(x) = ∫J(x,dy)(f(y)−f(x)); Γ(f)(x) = ½∫J(x,dy)(f(y)−f(x))²;
  **Γ₂(f)(x) = ¼∬J(x,dy)J(y,dz)(f(z) − 2f(y) + f(x))² − ¼∫J(x,dy)(q(x)+q(y))(f(y)−f(x))² + ½(Lf(x))²**
(derivation: Γ₂ = ½LΓ − Γ(f,Lf); b² − 2ab = (b−a)² − a² with a = f(y)−f(x), b = f(z)−f(y)). Γ₂ is a quadratic form in J:
for J = J_ν + J_Λ, Γ₂ = Γ₂^{νν} + Γ₂^{ΛΛ} + Γ₂^{νΛ} + Γ₂^{Λν} with the mixed term Γ₂^{12} = ½L₁Γ^{(2)} − Γ^{(2)}(f, L₁f) (non-linear in Λ: clause 1
formally met). On ℝ (phase 64) the mixed term is a Schur product of PD kernels (≥ 0); on I_T the censoring makes q(x) position-dependent and
the mixed terms carry boundary terms of no fixed sign (ARGUED; not needed below).
Single atom at T = ½log3: 𝒩_T = {2}, u = log 2 ∈ (T, 2T); the atom graph is a perfect matching t ↔ t+u on I_T∖M plus the isolated middle
M = {|t| < u−T = 0.14384}; on each edge Γ₂^{ΛΛ} = 2wΓ^{Λ} (two-point space, w = ½v₂), on M Γ^{Λ} = 0.

## 3. Transfer and the ceiling (main result)
**Lemma 3.1 (Tate controls the mean; PROVED).** On 𝒫_T, ∫F = ⟨F, 1 − c·cosh(t/2)⟩ for every c, so (∫F)² ≤ δ_T²‖F‖² with
δ_T² = 2T − 16 sinh²(T/2)/(T + sinh T) = O(T⁵). At T = ½log3: δ_T²/2T = 1.246·10⁻⁴. Hence Var(F) ≥ (1 − δ_T²/2T)‖F‖² on 𝒫_T.

**Prop 3.2 (BE transfer; PROVED given CITED BE ⇒ Poincaré).** If Γ₂ ≥ KΓ (CD(K,∞)), then E_T(F) ≥ K·Var(F) (Bakry–Gentil–Ledoux,
Γ-calculus, CITED; for CD(K,N) the Lichnerowicz gap KN/(N−1) is still ≤ the gap g_T), so
  λ_A(T) ≥ K(1 − δ_T²/2T) + inf_{𝒫_T}⟨W_T F,F⟩/‖F‖²  (valid for every nonnegative comb: a sound partial bound).

**Theorem 3.3 (gap ceiling; PROVED structure + NUMÉRICO constants).** Every bound of the form "λ_A ≥ (lower bound on E_T/Var) + potential
term on 𝒫_T" is ≤ g_T + ess inf W_T, where g_T = spectral gap of E_T (K ≤ g_T for every CD(K,N)). Proof: inf over 𝒫_T of the
multiplication form equals ess inf W_T (bumps concentrating at the infimum point; a 3-dim span of disjoint bumps meets 𝒫_T, codim 2).
At T = ½log3:
  ess inf W_T = W_T(0.14384⁺) = −2.53448 (the atom contributes −½v₂ off M, 0 on M; W_T(0) = m(0) + 2N(T) = −2.08100),
  g_T ≤ E_T(t)/‖t‖² = 2.10838 (one test, f(t) = t, mean zero; Rayleigh–Ritz on Legendre P₁…P₆ gives g_T ≤ 1.94138),
  **⇒ g_T + ess inf W_T ≤ −0.426 < 0.**
So no Bakry–Émery / curvature–dimension argument (any K, any N, Tate constraints included) certifies λ_A(½log3) ≥ 0, a window where
positivity is PROVED (P46 Theorem C). **NO-GO** for the class 𝒦_BE = {deductions that use the censored Markov part only through a
curvature / Poincaré constant, plus W_T and Tate data}. Constants: mpmath quadrature at 30 digits (INV_N_001_be_check.py); the margin 0.43
is large relative to quadrature error; rigorous interval re-check OPEN (routine).

**Prop 3.4 (falsifier screen, PROVED).** Under O4 (cΛ) or O2 at n₀ = 2, at T = ½log3, any F supported in M has zero atom energy, so
g_T(J_c) ≤ g_M (ν-only Rayleigh quotient on M) uniformly in c, while ess inf W_T decreases by ½c v₂: the BE bound tends to −∞ as λ_A does.
The cheap screen therefore does not decide (the bound is sound for every comb); the qualitative property CD(K>0) for ζ and for O2/O4/O6/
Beurling: OPEN, and irrelevant after 3.3, since even K = g_T fails.

## 4. Residues
- Feynman–Kac / Schrödinger curvature (Γ₂ of L − W) = ground-state (Doob) transform by h₀: returns to CA_I_001 Prop 1.1 (Krein–Rutman lives
  below λ₀ < λ_A) and to the indexed Doob-variance corridor (R160_M10_R1, REF-D). Not retried.
- Position-dependent curvature K(x) with weighted Poincaré: the ceiling becomes inf over 𝒫_T of a weighted gap + W, again ≤ E_T(f)/‖f‖² +
  W-average for localized f; ARGUED same NO-GO (W has log edge singularity, the deficit is in the interior band |s| ∈ (0.144, 0.4)).
- Γ₂ formula of §2 with the mixed boundary terms is a usable PROVED tool (no sign).

## Verdict
Track N: **NO-GO (class 𝒦_BE)**. Reason: the Markov part E_T is too weak; the sign is decided by the killing potential W_T, whose infimum
(−2.53 at ½log3) exceeds the largest possible curvature (≤ g_T ≤ 1.94). Clause 1 (non-linear in Λ) is met formally but the transfer
step linearizes. No sign. Do not retry Γ₂/CD/log-Sobolev/Poincaré of the censored jump part of 𝔞_T without an input that couples E_T and W_T.
