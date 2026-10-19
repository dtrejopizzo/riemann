# R167_102 — A2: direct attack on (WS). Dualisation, mean values, sieve blindness, and the uncertainty principle of the witness weight

**Status:** phase 167 round 1. Pure mathematics, no numerics. Inputs: R167_000 (problem (WS)),
R166_802 Thms 3–4, R164_601 Props 1.1–1.3, R150_000 §"Parseval-type" (T5, the sterility lemma).
**Verdict in one line:** (WS) with η < ½ cannot come from any of the zero-free tools. Positive-type averaging is Parseval,
so it gives nothing. Mean values (Montgomery–Vaughan) give η = ½ for *every* admissible witness weight, and a wider weight makes things
worse, not better. Every upper-bound sieve is blind to a cos-modulated subsequence of Λ (exponent ½, Thm B). A pointwise power
saving uniform in X is a zero-free statement (Thm C). The only input that is not blind is a combinatorial identity
(Vaughan/Heath-Brown). After Perron, that input becomes the zero-density machinery (Thm D, ARGUED). The stop is exact: §7.

## 0. Status table

| # | Statement | Label |
|---|---|---|
| L0 | Exact dualisation: 𝒮 = e^{iγu₀}(2π)^{-1}∫ Ŵ(τ) P_c(γ+τ) dτ with Ŵ = G²K ≥ 0. The positivity holds only for the **centred** sum P_c. The raw P(ξ) carries the phase e^{−iτu₀}, which oscillates at the resolution scale | PROVED |
| L0′ | The truncation to [log X, log X+2Δ] destroys Ŵ ≥ 0 when supp W ⊄ the window (supp W = [−2T−Δ, 2T+Δ] has length 4T+2Δ > 2Δ). Below, the natural range is used: n ∈ [e^{u₀−L}, e^{u₀+L}] with L = 2T+Δ | PROVED |
| L1 | Hermitian identity: ∫Ŵ|P_c|² = 2π Σ_{m,n} a_m ā_n W(log m/n) (a_n = Λ(n)n^{−1/2+iγ}). This is Parseval on the weight. Averaging over τ with Ŵ adds no information beyond the values of W | PROVED |
| Prop 1 | Bernstein floor: Ŵ ≥ 0 of type L ⇒ Ξ(Ŵ) := ‖Ŵ‖₁ / sup Ŵ ≥ 1/L | PROVED |
| Thm A | Mean-value bound and its exact exponent: \|𝒮\| ≤ C·sup Ŵ·(Ξ(Ξ+Y)·Σ\|a_n\|²)^{1/2}. With the quartet normalisation (sup Ŵ ≍ Ŵ(t_q)), η < ½ needs Ξ < X^{2η−1}, which contradicts Prop 1. So η_MV = ½ for **every** witness weight, and widening the weight increases the bound | PROVED (MV mean value cited) |
| Cor A′ | R167_000's step (3) is correct up to constants. The weight's width is ≍ 1/L and the resolution is 1/(2L), so the ratio is a constant. R167_000's "oversampling by X^ε" escape is wrong in direction: oversampling helps only relative to ‖Ŵ‖₁, never relative to Ŵ(t_q) | PROVED |
| Thm B | Sieve blindness: any argument whose arithmetic inputs are (i) Λ ≥ 0, (ii) support in prime powers, (iii) any family of upper bounds Σ Λ(n)φ(n) ≤ U_φ (φ ≥ 0) (Brun–Titchmarsh, Selberg, large-sieve counts, Bombieri–Vinogradov-type upper bounds), proves no \|𝒮\| ≤ c·X^{1/2}·(main mass) with a small constant c, and in particular no η < ½ | PROVED |
| Thm C | Pointwise/uniform: \|𝒮(u₀)\| ≤ C e^{ηu₀}·N(W) for all u₀ ≥ u₁, with a fixed shape W, ⇒ no zero ρ with Re ρ > ½+η and Ŵ(τ_ρ) ≠ 0. For the witness Ŵ(τ_q) = G(t_q)²K(t_q) ≠ 0, so this is the circularity of R166_802 Thm 3, localised | PROVED (Landau argument) |
| Thm D | Identities (Vaughan/Heath-Brown) are the only non-monotone input. With the multiplicative twist the Type II sums factor, (mn)^{iξ} = m^{iξ}n^{iξ}. After Perron the coupling mn ∈ I becomes a t-integral of products of Dirichlet polynomials, which is exactly the zero-density / large-values machinery. Pointwise savings from it are exp(−c(log X)^{3/5−ε})-type (Vinogradov–Korobov), never a power | ARGUED (+ PROVED-CITED known bounds) |
| Thm E | Finite range: for fixed (X, Δ, γ, W), 𝒮 is one number. "Exponent η" has content only for a family. A single instance equals pole − zero sum (R166_802 Thm 2), so proving it without zeros means evaluating it | PROVED (logic + explicit formula) |
| Verdict | (WS) is unattainable from mean values (½), sieves (½), positive-type averaging (Parseval, = L1) and uniform pointwise bounds (circular). The exact stop is §7 | PROVED for the four listed classes; ARGUED for "any zero-free method" |

## 1. Setup and the exact dualisation (L0, L0′)

Write u₀ for the centre and W(v) := w(u₀+v), so Ŵ(τ) = ∫W(v)e^{−iτv}dv = G(τ)²K(τ) ≥ 0 (R164_601 Prop 1.1–1.3). G has type T
and K has type ≤ Δ, so Ŵ has type L := 2T+Δ and supp W ⊂ [−L, L]. Put a_n := Λ(n) n^{−1/2+iγ} and define the **centred** twisted sum
P_c(ξ) := Σ_n Λ(n) n^{−1/2} e^{iξ(log n − u₀)}, summed over e^{u₀−L} ≤ n ≤ e^{u₀+L}. |P_c(ξ)| = |P(ξ)|.

**L0. PROVED.** By Fourier inversion, W(v) = (2π)^{−1}∫Ŵ(τ)e^{iτv}dτ. Then
𝒮 = Σ a_n W(log n−u₀) = (2π)^{−1}∫Ŵ(τ) Σ_n Λ(n)n^{−1/2} n^{iγ} e^{iτ(log n−u₀)} dτ = e^{iγu₀}(2π)^{−1}∫ Ŵ(τ) P_c(γ+τ)dτ.
(Ŵ is a nonnegative entire function of type L. It is integrable because W is continuous with compact support and Ŵ ≥ 0, so
‖Ŵ‖₁ = 2πW(0).) ∎
Remark. With the uncentred P(ξ) = Σ a-type n^{−1/2+iξ}, the integrand is Ŵ(τ)e^{−iτu₀}P(γ+τ). The phase e^{−iτu₀} oscillates at scale
1/u₀ ≈ 1/(2T), which is the same as the resolution. The statement "𝒮 is a positive average of P" is therefore true only for P_c. R167_000's
formula is correct once P is replaced by P_c.

**L0′. PROVED.** If the sum is truncated to [log X, log X+2Δ] while supp W = [−L, L] is longer, then the truncated weight
W·1_window has transform Ŵ * (Dirichlet kernel of half-width Δ)/2π. That transform takes negative values (the sinc kernel does, and Ŵ is not
constant). So positivity holds only on the natural range n ∈ [e^{u₀−L}, e^{u₀+L}]. Throughout, X := e^{u₀−L} and Y := e^{u₀+L}, so
log(Y/X) = 2L. With this convention the problem's "2Δ" becomes 2L, and the conclusions below do not depend on the choice.

## 2. Averaging over τ is Parseval (L1); the R150 sterility check

**L1. PROVED.** ∫Ŵ(τ)|P_c(γ+τ)|²dτ = Σ_{m,n} a_m ā_n ∫Ŵ(τ)e^{iτ log(m/n)}dτ = 2π Σ_{m,n} a_m ā_n W(log(m/n)).
The Hermitian form is ≥ 0 because W is positive-definite (Bochner, Ŵ ≥ 0). Its size is controlled only by the values of W at the
differences log(m/n) ∈ [−2L, 2L]. ∎

*Compliance with R150_000 §Parseval-type.* L1 is a Parseval identity on the **weight**. It is not evaluated at the pole: the
frequency is γ+τ with γ > 3·10¹², far from τ = 0. By T5 (R150), such an identity extracts at best the trivial bound unless the
family |ℱ| (here the τ-window, of measure Ξ) exceeds the length (here Y). §3 shows this is exactly what happens. The sterility lemma
applies with |ℱ| = Ξ ≤ O(1) ≪ L₀ = Y.

## 3. The width of the witness weight against the resolution (Prop 1, Thm A, Cor A′)

**Prop 1 (Bernstein floor). PROVED.** Let M := sup Ŵ = Ŵ(τ*). Ŵ is entire of type L and bounded on ℝ, so Bernstein gives |Ŵ′| ≤ LM on ℝ.
Hence Ŵ ≥ M/2 on [τ*−1/(2L), τ*+1/(2L)], and ‖Ŵ‖₁ ≥ M/(2L). So Ξ := ‖Ŵ‖₁/M ≥ 1/(2L). ∎
In the other direction, Ξ can be large: K ≥ 0 of type Δ can be flat over a long τ-range. Prop 1 is the only constraint from the
type.

**Resolution.** P_c is the Fourier transform of an atomic measure on an interval of length 2L in v = log n − u₀. Its correlation
length in ξ is π/L. R167_000's 1/(2T+2Δ) is this up to π. Width and resolution are both ≍ 1/L. So Ξ(Ŵ)/(π/L) ≥ 1/(2π), and for a
weight localised near t_q at scale 1/Δ ≲ 1/L·(L/Δ), the ratio is O(L/Δ), a **constant** as X varies. R167_000's step 3 is confirmed.

**Thm A (mean-value exponent). PROVED, using the Montgomery–Vaughan mean value theorem (PROVED-CITED: MV, J. London Math. Soc. 1974,
Cor. 3): for every t₁ and every Ξ₀ > 0, ∫_{t₁}^{t₁+Ξ₀}|Σ_n b_n n^{it}|²dt = Σ_n |b_n|²(Ξ₀ + O(n)).**
Cover ℝ by unit cells I_j and put M_j := sup_{I_j}Ŵ. By Cauchy–Schwarz and L0,
|𝒮| ≤ (2π)^{−1}‖Ŵ‖₁^{1/2}(∫Ŵ|P_c|²)^{1/2} ≤ (2π)^{−1}‖Ŵ‖₁^{1/2}(Σ_j M_j·(1+O(Y))·Σ|a_n|²)^{1/2}.
By Plancherel–Pólya for a nonnegative function of type L, Σ_j M_j ≤ C(1+L)‖Ŵ‖₁. Grouping the cells into blocks of length Ξ gives
|𝒮| ≤ C·M·(Ξ(Ξ+Y)·Σ|a_n|²)^{1/2}, with Σ|a_n|² = Σ Λ(n)²/n ≍ L·log Y.  (A)
Compare with the quartet normalisation M ≍ Ŵ(t_q). The witness requires the quartet to dominate, which forces Ŵ(t_q) ≥ c·sup Ŵ, as
K is localised at t_q. η < ½ would require Ξ(Ξ+Y) ≤ X^{2η}/(L log Y), so Ξ ≤ X^{2η}/Y = X^{2η−1}e^{−2L} < 1/(2L) for X large, against
Prop 1. Hence (A) gives η = ½ and no better for every admissible weight. The right side of (A) increases with Ξ. ∎

**Cor A′ (correction of R167_000's escape). PROVED.** The proposed escape was "make G²K wider than the resolution by X^ε". Relative to
‖Ŵ‖₁, widening does help: for Ξ ≥ Y^{1+ε}, W has width < 1/Y in v, at most O(1) terms survive, and |𝒮| ≲ ‖Ŵ‖₁·X^{−1/2}log X. But the
witness needs |𝒮| ≤ X^{η}Ŵ(t_q) ≤ X^{η}M = X^{η}‖Ŵ‖₁/Ξ. Combined with the true size |𝒮| ≍ ‖Ŵ‖₁·(one term), this requires
Ξ ≲ X^{η+1/2}/log X, and in that regime W spans ≍ X/Ξ terms. Run (A) uniformly: the bound relative to M is √(Ξ(Ξ+Y)) ≥ √(ΞY), which
increases with Ξ. **Uncertainty principle of the witness:** quartet dominance (Ŵ(t_q) ≳ ‖Ŵ‖₁/Ξ with Ξ small) and mean-value smallness
(Ξ ≳ Y) are incompatible for every η < 1. The precise inequality is Ξ·Y ≤ X^{2η}·O(1) together with Ξ ≥ 1/(2L), which forces η ≥ ½. ∎

## 4. Sieve blindness (Thm B)

**Thm B. PROVED.** Let 𝔄 be any set of statements about a sequence b: ℕ → [0, ∞) of the following forms:
(i) b ≥ 0; (ii) supp b ⊂ prime powers; (iii) Σ_n b(n)φ(n) ≤ U_φ for a family of φ ≥ 0, true for b = Λ.
Define b_θ(n) := Λ(n)·½(1 + cos(γ log n + φ_n + θ)), where φ_n := arg W(log n − u₀). Then 0 ≤ b_θ ≤ Λ, so b_θ satisfies all of 𝔄.
Expanding the cosine,
𝒮[b_θ] = ½𝒮[Λ] + ¼e^{−iθ}·A + ¼e^{iθ}·B, with A := Σ_n Λ(n)n^{−1/2}|W(log n − u₀)| ≥ 0 and B a fixed complex number.
A is the absolute mass ≍ X^{1/2}·‖W‖_{L¹}-type, using the prime number theorem in the window, so A ≫ X^{1/2}·‖W‖₁/L.
The function θ ↦ 𝒮[b_θ] has the form c₀ + ¼(e^{−iθ}A + e^{iθ}B). Its values at θ and θ+π differ by ½(e^{−iθ}A + e^{iθ}B), and
max_θ |e^{−iθ}A + e^{iθ}B| ≥ A. So for some θ, |𝒮[b_θ]| ≥ A/8 ≫ X^{1/2}‖W‖₁/L.
Any conclusion |𝒮[b]| ≤ C X^{η}‖w‖_⋆ derived from 𝔄 holds for b_θ, so it is impossible for η < ½ and X large. (For ‖·‖_⋆ ≍ ‖W‖₁ or
≍ sup Ŵ, using ‖W‖₁ ≥ |∫W| = Ŵ(0).) ∎
*Atomicity check (R167_000 test M_m / f_t).* b_θ is atomic and supported on the prime powers of ℕ, so Thm B is stronger than the M_m
test. Blindness already holds inside the integers. Integrality and atomicity are kept by b_θ; what b_θ breaks is the **identities**
(Λ = μ*log, Selberg). So the place where "Λ itself" must enter is an identity, not a support or sign condition. This answers A3's
localisation question for the sieve class.

## 5. Pointwise bounds uniform in the scale are zero-free statements (Thm C)

**Thm C. PROVED (Landau).** Fix the shape W, with Ŵ ≥ 0 of type L, and let u₀ vary. Suppose |𝒮(u₀)| ≤ C e^{ηu₀} for u₀ ≥ u₁. For
Re s > η, ∫ e^{−su₀}𝒮(u₀)du₀ converges and is analytic. Compute it termwise for Re s > ½:
∫W(log n − u₀)e^{−su₀}du₀ = n^{−s}Ŵ(is), so the transform equals −(ζ′/ζ)(s+½−iγ)·Ŵ(is) + (entire).
The right side is meromorphic. A zero ρ = β+iγ′ gives a pole at s_ρ = ρ − ½ + iγ unless Ŵ(i s_ρ) = 0. By analytic continuation the
left side is analytic in Re s > η. Hence every zero with β > ½+η has Ŵ(i s_ρ) = 0. ∎
For the witness quartet, Ŵ(i s_ρ) = G(t_q)²K(t_q) ≠ 0 by construction (that is the quartet term). So the uniform (WS) is the statement
"no zero at the witness", which is R166_802 Thm 3 localised to one frequency.

## 6. Identities: the only non-blind input, and where they lead (Thm D)

**Thm D. ARGUED, with the cited bounds PROVED-CITED.** Vaughan's identity (U = V = X^{1/3}) splits P_c(ξ) into:
- **Type I:** Σ_{d≤D} μ(d) d^{−1/2+iξ} Σ_{m∈[X/d, Y/d]} (log m) m^{−1/2+iξ}. The inner sums are short partial sums of ζ at height
ξ ≈ γ. If X ≪ γ (which R165_101 forces: T ≤ T_L(γ*)+0.226), the inner sums are dominated by the van der Corput B-process (stationary
phase at m ≈ ξ/2π, which lies **outside** [X/d, Y/d]). Then |inner| ≪ (X/d)^{1/2}·(d/X)·γ^{0}… In other words, Type I is small with a
power saving, by the first-derivative test (Kusmin–Landau), because f′(m) = ξ/(2πm) is large and monotone. PROVED-CITED (Kusmin–Landau);
gain X^{−1/2}·(X/γ)-type when ‖f′‖ stays away from ℤ.
  *Caveat.* f′ = ξ/(2πm) runs over many integers as m ranges over [X/d, Y/d] when γ/X ≫ e^{2L}. The B-process is then needed and returns
  ζ-type sums of length ξ/(2πm). There is no power saving uniformly, only the convexity/subconvexity exponent of ζ(½+iγ), which is known
  without zeros (PROVED-CITED: Bourgain 13/84). **This is a genuine zero-free power saving, but in γ, not in X.**
- **Type II:** Σ_{m~M} Σ_{n~N} α_m β_n (mn)^{−1/2+iξ}·1_{mn∈I}. The twist factors. Cauchy–Schwarz plus the MV mean value give
(M+N)^{1/2}-type bounds after the coupling 1_{mn∈I} is removed by Perron, ∫ A(½+i(ξ+t))B(½+i(ξ+t))·Î(t)dt. A pointwise bound at the
single ξ needs the **large values** of Dirichlet polynomials A, B near height ξ. That is the zero-density input (Huxley/Montgomery large
values). These give density theorems, i.e. "few zeros", not "no zero at ξ". In Type II there is no analogue of the Vinogradov
bilinear cancellation, because Vinogradov's gain uses e(αmn) ≠ e(αm)e(αn). PROVED for the factorisation; ARGUED for "no power saving
pointwise".
- **Known unconditional pointwise outcome:** Σ_{n≤N}Λ(n)n^{it} = N^{1+it}/(1+it) + O(N exp(−c(log N)^{3/5}(log log N)^{−1/5})) for
log t ≪ (log N)^{3/2}-type ranges (PROVED-CITED: from the Vinogradov–Korobov region). In our normalisation this is X^{1/2−o(1)}, so
η = ½.

*Remark on Type I (new, PROVED, but only a partial gain).* When X ≤ γ^{1−ε}, the Type I pieces with d ≤ D and the B-process length
ξ/(2π·X/d) ≤ γ… give contributions bounded by the ζ subconvex exponent in γ. In the witness scale (X fixed, γ > 3·10¹² huge) this is a
**negative power of γ**, not of X. It can matter only if (WS) is normalised by γ. R167_000 measures η in X, and in X Type I is not the
bottleneck: Type II is. Recorded for A1: if A1's requirement can be stated with γ-dependence, check the γ-side.

## 7. Finite range (Thm E) and the exact stop

**Thm E. PROVED.** For fixed (u₀, L, γ, W), 𝒮 is one complex number. Every inequality |𝒮| ≤ B is either true or false, and an
"exponent" is defined only through a family. In the family u₀ → ∞ with fixed shape, the bounds achievable without zeros are:
(a) mean values: η = ½ for the witness weights (Thm A). The value 0 is reachable only for weights with Ξ ≥ Y^{1+ε}, measured against
‖Ŵ‖₁, and those weights are not witness weights (Cor A′);
(b) monotone sieve inputs: η = ½, sharp (Thm B);
(c) the witness's own weight: width/resolution = O(1), so the constant-factor loss is the whole effect (Cor A′);
(d) uniform pointwise η < ½: equivalent to the absence of the witness zero (Thm C).
For a single fixed scale, the explicit formula gives 𝒮 = pole − Σ_ρ Ŵ(i s_ρ)e^{s_ρ u₀} (R166_802 Thm 2). A zero-free proof of
|𝒮| ≤ X^{η}Ŵ(t_q) would therefore have to show that the zero sum is smaller than the quartet term, which is the D statement itself.

**Exact stop.** Any route to (WS) below ½ must use an identity for Λ (Thm B), applied at one frequency in the X-aspect. After the
factorisation of the twist, this reduces to bounding the large values of Dirichlet polynomials at one height (Thm D). That is the
Montgomery large-values problem at a point. Its uniform version is Thm C, which is circular. It is the R150 Corollary (P149) again: an
M₂-type bound with |ℱ| < L is needed, here with |ℱ| = Ξ = O(1) and L = Y. Missing object: **a non-Parseval, non-monotone, single-height
bound for Type II Dirichlet-polynomial products of length X**. No such object exists in the literature (ARGUED).

## 8. Ledger

- New and PROVED here: L0 (centring phase), L0′ (truncation breaks positivity), Prop 1, Thm A with the exponent computation, Cor A′
(R167_000's oversampling escape points the wrong way: uncertainty Ξ·Y ≤ X^{2η} against Ξ ≥ 1/(2L)), Thm B (cos-modulated b_θ: sieve
blindness inside the integers, which localises A3: identities, not atomicity), Thm C (localised Landau), Thm E.
- PROVED-CITED: Montgomery–Vaughan mean value; Bernstein; Plancherel–Pólya; Kusmin–Landau; Vinogradov–Korobov; Bourgain subconvexity.
- ARGUED: Thm D's "no pointwise power saving in X from identities"; the final "no zero-free method" verdict.
- OPEN: a single-height large-values bound for Type II products. The γ-aspect Type I gain (§6 remark) goes to A1.
- Corpus consistency: agrees with R166_802 Thms 3–4 (½ from sieves, circular uniform bounds) and R150 T5 (Parseval sterility, with
|ℱ| = Ξ ≪ Y). Nothing here is claimed as progress on D.
