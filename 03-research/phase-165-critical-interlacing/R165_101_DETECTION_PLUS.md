# R165_101 — (Det+): an explicit detection time for an off-line zero

* Task A1 of phase 165 (R165_000 §1, (Det+)). Pure mathematics, no numerics. No other file was edited.
No label of record moves.*

**Labels.** PROVED = full proof here. PROVED-CITED = reference given. ARGUED = argument given, one named step not
proved. OPEN.

## Status table

| # | statement | label |
|---|---|---|
| Thm Det+ | ¬RH at ρ* ⟹ λ^W_T < 0 for all T ≥ τ(ρ*), with τ explicit in X* = πe^{2τ} (eq. (4)) | **PROVED** (inputs: (1.1) PROVED-CITED; Euler product, Stirling product, Σ Re 1/ρ, all PROVED-CITED, classical) |
| Cor Det+.1 | τ ≤ T_L(γ*) + ½log(π/2) + (2/πγ*)·[Σ″ log⁺(1/\|ρ*−ρ\|) + C k log γ* + log(1/δ*)] | **PROVED-CITED** (Titchmarsh Thm 9.6(A); C absolute but not computed) |
| Cor Det+.2 | if all other zeros are at distance ≥ η from ρ*: τ = T_L(γ*) + ½log(π/2) + O(k log γ*(1 + log⁺1/δ* + log⁺1/η)/γ*) | **PROVED-CITED** (same, plus N(t+1)−N(t) ≪ log t) |
| Rem D.1 | the construction cannot give τ < T_L(γ*) + ½log(π/2) − o(1) | ARGUED (Cauchy upper bound for ξ^{(k)}; constants not written) |
| Rem D.2 | the polynomial design F̂ = P·S of R165_000 loses a constant factor in the type (edge growth 2^n of P) | ARGUED; superseded by the ξ-division design |
| Obstruction O.1 | a τ depending on (γ*, δ*) **only** needs a lower bound for the reduced derivative \|a*\| (eq. (2)); none is known unconditionally (other off-line zeros may cluster at ρ*) | PROVED as a statement of what the proof uses; the missing bound is OPEN (standard open problem: no unconditional lower bound for \|ζ^{(k)}(ρ)\|) |
| Falsifiers | Det+ holds verbatim, with its own Landau window, for every function with FE, Euler-product-type bound on σ ≥ 2 and zero-side identity (f_t, f_χ, M_m variants) | ARGUED (expected; excludes nothing) |

**Answer to the task in one line.** (Det+) is PROVED with the sharp Landau form
τ = T_L(γ*) + ½log(π/2) + (lower order), ½log(π/2) = 0.2258, **no factor 2**; the only non-(γ*,δ*) input is the
reduced leading coefficient a* of ξ at the quartet, which enters as log log, i.e. only through
(1/πγ*)·log(1/|a*| e^{−πγ*/4}).

---

## 0. Setup (from R163_401 §1)

F ∈ L²(−T,T), F̂(z) = ∫F(t)e^{izt}dt, F̂^#(z) = conj F̂(z̄). For F ∈ 𝒟_T (Lemma 3.0 domain),

  W_T(F) = Σ_ρ (F̂F̂^#)(t_ρ),  t_ρ = γ − iδ for ρ = ½+δ+iγ,        (1.1, PROVED-CITED: Paper 46 lem:roughEF + R163_401 Lemma 3.0)

with multiplicity, absolutely convergent. If F is real and even, F̂ is even and real on ℝ, F̂^# = F̂, and the summand is
F̂(t_ρ)². W_T(F) does not depend on T as long as supp F ⊂ [−T,T]; hence λ^W_T is nonincreasing (also R163_401 2.2).

Ξ(z) := ξ(½+iz), ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s). Ξ is entire, even, real on ℝ, and its zeros are exactly the t_ρ.

**Hypothesis.** ρ* = ½+δ*+iγ* is a zero of ζ of multiplicity k ≥ 1 with δ* > 0. By Platt–Trudgian (PROVED-CITED,
R163_401 §4.2) γ* > H = 3·10¹², and 0 < δ* < ½. Put t* = γ* − iδ*. The quartet {ρ*, 1−ρ̄*, ρ̄*, 1−ρ*} corresponds to
{t*, t̄*, −t*, −t̄*}, each of multiplicity k.

## 1. The design: divide ξ by its quartet

Instead of a local polynomial P (R165_000), use the global function whose zeros are *all* zeros of ζ and remove only the
quartet:

  Q(z) := (z² − t*²)(z² − t̄*²),  h(z) := Ξ(z) R(z) / Q(z)^k,  R(z) := z² − c, c ∈ ℝ.

- h is entire (Q^k divides Ξ), even, real on ℝ (Q and R are even and real on ℝ).
- h(t_ρ) = 0 for every zero ρ outside the quartet q*. So all on-line zeros, near and far, and all *other* off-line
  quartets are annihilated exactly; the only non-zero values are at the quartet.
- Reduced coefficient. Write Q(z) = (z−t*)q₁(z), q₁(t*) = (2t*)(t*−t̄*)(t*+t̄*) = 2t*·(−2iδ*)·2γ*. Then

  a* := lim_{z→t*} Ξ(z)/Q(z)^k = Ξ^{(k)}(t*) / (k! q₁(t*)^k) ≠ 0,  |a*| = |ξ^{(k)}(ρ*)| / (k!(8|t*|γ*δ*)^k).   (2)

The price: h is not of exponential type. Its inverse transform H(u) = (1/2π)∫h(x)e^{−iux}dx is supported on all of ℝ
but decays like exp(−πe^{2|u|}) (the Riemann–Pólya kernel Φ). Truncation to [−T,T] costs exp(−πe^{2T}); the quartet value
is of size e^{−πγ*/4}. Balancing gives e^{2T} ≈ γ*/4, i.e. T ≈ T_L(γ*) + ½log(π/2). This is where the Landau window
comes from: the local exponential type of ξ at height γ is θ′(γ) = T_L(γ) + O(γ^{−2}).

## 2. Theorem Det+ — PROVED

**Theorem Det+.** Let ρ* be as above, a* as in (2), and put

  B* := log(1/|a*|) + log( 3350(1+γ*²) / (γ*δ*) ),  B′ := max(B*, 30),  X* := B′ + 6 log(2B′ + 6),
  τ(ρ*) := ½ log(X*/π).                                                                                     (4)

Then for every T ≥ τ(ρ*) there is a real even F ∈ L²(−T,T) ∩ 𝒟_T, given explicitly in Step 1, with
W_T(F) ≤ −1.8k|h(t*)|² < 0. Hence λ^W_T < 0 for all T ≥ τ(ρ*).

**Proof.**

*Step 0 (phase; Lemma 3.1/3.3 light cone).* Let φ₀ = arg a* mod π. R(t*) = (γ*² − δ*² − c) − 2iγ*δ*. As c runs over ℝ,
θ := arg R(t*) runs over (−π,0); with Y₀ = 2γ*δ*, c = γ*² − δ*² + Y₀ cot θ. The arc θ ∈ [−5π/6, −π/6] (length 2π/3) and
the arc {θ : θ + φ₀ ∈ [π/3, 2π/3] mod π} (length π/3) are closed arcs on ℝ/πℤ of total length π, so they meet. Fix such
θ and c. Then, with A := h(t*) = a*R(t*):
- |arg A − π/2| ≤ π/6 mod π, so Re A² = |A|² cos(2 arg A) ≤ −|A|²/2;
- |R(t*)| = Y₀/|sin θ| ≥ 2γ*δ*, so |A| ≥ 2γ*δ*|a*|;
- |cot θ| ≤ √3, so |c| ≤ γ*² + √3γ* ≤ 2γ*².

*Step 1 (the test function).* h decays faster than any power of |x| in every horizontal strip (Stirling and the
polynomial bound for ζ in vertical strips; PROVED-CITED, Titchmarsh §4.12, §5.1), and it is entire. Contour shift (Step
3) shows |H(u)| ≤ C_Y e^{−Y|u|} for every Y, so H is real, even, smooth, and h(z) = ∫_ℝ H(u)e^{izu}du for all z ∈ ℂ (both
sides entire, equal on ℝ). Put

  F := H·1_{[−T,T]},  E(z) := ∫_{|u|>T} H(u)e^{izu}du,  F̂ = h − E.

F is real and even. F ∈ 𝒟_T: h ∈ 𝒟 by its decay, and one integration by parts gives |E(x)| ≪ 1/(1+|x|) on ℝ.

*Step 2 (zero side).* By (1.1) and Step 1, h(t_ρ) = 0 off the quartet, and E is real-even (E(t̄) = conj E(t), E(−t) = E(t)):

  W_T(F) = 4k Re(A − E(t*))² + Σ′_ρ E(t_ρ)²,

Σ′ over zeros not in q*. For |Im t| ≤ ½, E(t) = 2∫_T^∞ H(u)cos(tu)du; integrating by parts, with |sin tu| ≤ e^{u/2},

  |t|·|E(t)| ≤ 2M_T,  M_T := |H(T)|e^{T/2} + ∫_T^∞ |H′(u)|e^{u/2}du.

*Summation over zeros (PROVED from a PROVED-CITED identity).* Σ_ρ Re(1/ρ) = 1 + γ_E/2 − ½log 4π (Davenport ch. 12,
unconditional). Pairing ρ with 1−ρ̄: β/(β²+γ²) + (1−β)/((1−β)²+γ²) ≥ 1/(1+γ²). Hence
Σ_ρ 1/(1+γ_ρ²) ≤ 2 + γ_E − log 4π < 0.04620, and since |γ_ρ| ≥ 14.13, Σ_ρ 1/|t_ρ|² ≤ 1.0051·0.04620. So

  |Σ′| ≤ 4M_T²·0.0465 ≤ 0.19 M_T²,  |E(t*)| ≤ 2M_T/γ* ≤ 10^{−12}M_T.

With Re A² ≤ −|A|²/2:

  W_T(F) ≤ −2k|A|² + 8k|A||E(t*)| + 4k|E(t*)|² + 0.19M_T².

If M_T ≤ |A|, then W_T(F) ≤ (−2 + 10^{−11} + 0.19)k|A|² ≤ −1.8k|A|².

*Step 3 (tail of H).* For u > 0 shift to Im x = −Y (Y ≥ 3/2; h is entire and decays in the strip):
|H(u)|, |H′(u)| ≤ e^{−uY}J(Y), J(Y) := (1/2π)∫(1+|x|+Y)|h(x−iY)|dx. So
M_T ≤ J(Y)e^{−T(Y−½)}(1 + 1/(Y−½)) ≤ 2J(Y)e^{−T(Y−½)}.

Write σ = Y+½ ≥ 2, s = σ + ix, a = σ/2, b = x/2, A₀ = a+6, B = |b|. Then h(x−iY) = ξ(s)R(x−iY)/Q(x−iY)^k, and:
- |Q(x−iY)| ≥ (Y−½)⁴ ≥ 1 (each of ±t*, ±t̄* has |Im| ≤ ½).
- |ζ(s)| ≤ ζ(2) < 1.645.
- |Γ(a+ib)|² = Γ(a)² Π_{n≥0}(1 + b²/(a+n)²)^{−1} (Weierstrass product; PROVED-CITED). Keeping n = 0..6:
  |Γ(a+ib)| ≤ Γ(a) min(1, (A₀/B)⁷) ≤ Γ(a)(2A₀/(A₀+B))⁷.
- (1+|x|+Y)|s||s−1||R| ≤ 2(A₀+B)·4(A₀+B)²·4(A₀+B)²(1+γ*²) = 32(A₀+B)⁵(1+γ*²) (using |c| ≤ 2γ*²).

So the integrand is ≤ ½·1.645·32·128·(1+γ*²)π^{−a}Γ(a)A₀⁷/(A₀+B)², and ∫dx/(A₀+|x|/2)² = 4/A₀:

  J(Y) ≤ 2145(1+γ*²)(a+6)⁶ π^{−a}Γ(a) ≤ 5860(1+γ*²)(a+6)⁶ a^{−½}(a/(πe))^a,

by Stirling Γ(a) ≤ √(2π)a^{a−½}e^{−a}e^{1/(12a)} (a ≥ 1). Choose a = πe^{2T} (so Y = 2a−½ ≥ 5.7): the exponent
a log(a/π) − a − 2Ta + T equals −a + T, and a^{−½}e^{T} = π^{−½}. With X := πe^{2T}:

  M_T ≤ 6700 (1+γ*²)(X+6)⁶ e^{−X}.                                                                       (3)

*Step 4 (threshold).* By (3) and |A| ≥ 2γ*δ*|a*|, M_T ≤ |A| holds if X − 6log(X+6) ≥ B*. The left side is increasing in
X ≥ 0. At X = X*: X* ≤ 2B′ because 6log(2B′+6) ≤ B′ for B′ ≥ 30; hence X* − 6log(X*+6) ≥ B′ + 6log(2B′+6) − 6log(2B′+6)
= B′ ≥ B*. So every T ≥ τ = ½log(X*/π) works. ∎

*Remark (what is used).* Only (1.1), the functional-equation shape of ξ, and |ζ| ≤ ζ(2) on σ ≥ 2. Neither N(t), the
Backlund bound, Σδ² = o(T), nor zero-density estimates are needed: the other quartets and the far on-line zeros are
annihilated exactly, not estimated. This makes the R165_000 bookkeeping (far sum, other quartets, Phragmén–Lindelöf)
unnecessary.

## 3. Size of τ — Corollaries

**Upper bound for log 1/|a*| (PROVED-CITED).**
- Leibniz: ξ^{(k)}(ρ*) = ½ρ*(ρ*−1)π^{−ρ*/2}Γ(ρ*/2)ζ^{(k)}(ρ*).
- Stirling: |Γ((β+iγ)/2)| = √(2π)(γ/2)^{(β−1)/2}e^{−πγ/4}(1+O(1/γ)).
- Titchmarsh Thm 9.6(A): ζ′/ζ(s) = Σ_{|γ−t|≤1} 1/(s−ρ) + O(log t), integrated horizontally from 2+iγ* and taken to the
  limit at ρ*, gives log|ζ^{(k)}(ρ*)/k!| = Σ_{ρ≠ρ*, |γ−γ*|≤1} log|ρ*−ρ| + O(log γ*).
- The reflection 1−ρ̄* (distance 2δ*, multiplicity k) contributes k log 2δ*, which cancels the δ*^k of (2).

Hence, with Σ″ the sum over zeros with |γ−γ*| ≤ 1 other than ρ*, 1−ρ̄*:

  log(1/|a*|) = πγ*/4 + Σ″ log(1/|ρ*−ρ|) + O(k log γ*).

**Cor Det+.1.** τ(ρ*) ≤ T_L(γ*) + ½log(π/2) + (2/(πγ*))·[Σ″ log⁺(1/|ρ*−ρ|) + log(1/δ*) + C k log γ*]. This uses
½log(X*/π) = ½log(γ*/4) + ½log(1 + (4/πγ*)(X* − πγ*/4)) and ½log(1+x) ≤ x/2, and C is absolute.

**Cor Det+.2.** Suppose ρ* is η-isolated: every zero other than ρ*, 1−ρ̄* is at distance ≥ η. On-line zeros are
automatically at distance ≥ δ*. Since N(γ*+1) − N(γ*−1) ≪ log γ* (PROVED-CITED, Backlund/Titchmarsh 9.2),

  τ(ρ*) = T_L(γ*) + ½log(π/2) + O( k log γ* · (1 + log⁺(1/δ*) + log⁺(1/η)) / γ* ).

For γ* > 3·10¹² the error is < 10^{−9} unless δ* or η is smaller than exp(−10^{10}).

**Rem D.1 (sharpness of the design; ARGUED).** Cauchy's estimate on a circle of radius ~1/log γ* gives
log(1/|a*|) ≥ πγ*/4 − O(k log γ*), so this F never detects before T_L + ½log(π/2) − o(1). Whether *some* F detects
earlier is (Det−) (A2's task), not this memo's.

**Obstruction O.1 (the δ*-only form).** The task asked for τ = T_L + C + f(δ*). The proof gives this exactly when the
cluster sum Σ″ is O(log γ*·log 1/δ*), for example under η-isolation with η ≥ δ*. Unconditionally, other off-line zeros
may lie arbitrarily close to ρ*. Then |a*| has no lower bound in terms of (γ*, δ*), and none is known for |ζ^{(k)}(ρ)|. The
dependence is still very weak (log log): τ grows by ½log 2 only when Σ″ ≳ πγ*/4. Two outs:
- Choose ρ* to be the zero in its cluster that minimises τ. Det+ holds for **every** off-line zero, so
  T_c ≤ min_ρ τ(ρ).
- Divide out the whole cluster and fix the phases by a real even interpolating R. This reintroduces the same
  divided-difference sizes, so it does not remove O.1 (ARGUED).

**Rem D.2 (why the polynomial design loses a factor; ARGUED).** If P has n ≈ (L/π)Δ roots of density L/2π on
[γ*−Δ, γ*+Δ], then |P| at the window edge exceeds |P(γ*)| by about 2^n. The potential of the uniform measure differs
by 2ρΔ log 2 between centre and edge. S must recover this inside the window, and a sinc^k majorant then needs type
≳ 2n/Δ, a constant multiple of T_L. The global ξ has no window edges: its zeros continue at the right density for
ever. This is the "factor 2" hinted at in R165_000 §1, and the ξ-division removes it.

## 4. Falsifier logic

The proof uses only:
- (1.1);
- that the completed function is entire, even and real, with Gamma factor Γ_ℝ;
- |L| ≤ L(2) on σ ≥ 2.

For f_t and M_m the same proof runs verbatim (the window becomes ½log(γ/2π) again; for f_t, |f_t| on σ ≥ 2 replaces
ζ(2)). For f_χ (conductor 7) the same proof gives T ≈ ½log(7γ/2π)+O(1), its own Landau window. So (Det+) excludes
nothing, as R165_000 §4 expects. Its content is the **location** of T_c under ¬RH:
T_c ≤ T_L(γ*) + 0.226 + o(1) (when δ* and the cluster are not superexponentially small).

**Contrapositive (PROVED, from Det+).** Suppose λ^W_{T₀} ≥ 0. Then every off-line zero has τ(ρ) > T₀, i.e.
γ/4 + (1/π)[Σ″log(1/|ρ−ρ′|) + log(1/δ) + Ck log γ] > e^{2T₀}. In words: positivity of W at T₀ forces RH up to height
≈ 4e^{2T₀}, up to clustering. The novelty of this form against Yoshida/Bombieri has not been checked; it is not to be
claimed as new before a literature check.

## 5. Cells

- **7A (D.16-γ, cone cut by the zero data).** Det+ is the first PROVED statement of the form "the zero data cut the cone
  at a known T": the explicit vector F = (ΞR/Q^k)^∨·1_{[−T,T]} lies in the negative cone of W_T for T ≥ τ. It is built
  from ζ's own zero set: all zeros except one quartet are annihilated. Status: PROVED (upper half of the detection
  theorem).
- **7D.** T_c ∈ (0.8047, τ(ρ_min)]. Upper end ≈ T_L(γ_min) + 0.226. This bounds where (★_cell)/(EC) of R165_000 §2 must be
  studied: the critical interlacing window is at most 0.226 + o(1) above Landau.
- **Implication for §2 (EC).** At T ≥ τ the witness F of Det+ is not real-rooted near γ*. Its zeros there are the zeros
  of ξ, so at the quartet it is complex-rooted. So Det+ says nothing about the real-rooted first-contact witness; it only
  bounds T_c.

## 6. Ledger

| item | label |
|---|---|
| Thm Det+ (explicit τ, eq. (4)) | PROVED |
| bound (3) on the truncation tail | PROVED |
| Σ_ρ 1/(1+γ²) < 0.0462 (from Σ Re 1/ρ) | PROVED (from PROVED-CITED identity) |
| Cor Det+.1, Det+.2 | PROVED-CITED (Titchmarsh 9.6(A), 9.2; Stirling) |
| T_c ≤ T_L(γ*) + ½log(π/2) + o(1) (generic δ*, cluster) | PROVED-CITED |
| Rem D.1 (design cannot beat T_L + 0.226) | ARGUED |
| Rem D.2 (polynomial design loses a constant factor) | ARGUED |
| O.1: (γ*, δ*)-only τ needs a lower bound on \|ζ^{(k)}(ρ*)\| | OPEN (known open problem) |
| Novelty of the contrapositive | not checked |
| Row D | OPEN (unchanged) |
