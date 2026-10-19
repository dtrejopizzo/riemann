# R184_013 — The full system with dither: the composites are the exponential, and the exponential sees all frequencies

Pure mathematics, no numerics.
Inputs: R184_010 (Theorem D, O184.010a), R184_001 §1 (Prop 2.2: Perron), R163_803/R163_891 (BFdisc), R171_FINAL §3 (dictionary s ↦ w).
RH is not asserted, nor the closure of row D.

## State

| # | Statement | Label |
|---|---|---|
| 1 | Exact identity: log R(s) is **linear** in ε (ζ_𝒫 = ζ_target·R, log R = Σ_j j^{−1} Σ_p ε_p v_p^{−js}). The composite
    terms γ_{p₁}⋯γ_{p_k} are exactly the coefficients of exp(log R) | PROVED (§1) |
| 2 | With the dither of R184_010 (at every Witt level): a.s. log R(σ+it) = O(√log(2+\|t\|)) uniformly for Re s ≥ (1−θ)/2 + δ. Hence N_𝒫(x) = cx + O(x^{(1−θ)/2+ε}), and the zeros in Re s > (1−θ)/2 are those of the target, at Re s = (1+θ)/2 | PROVED (§2). **Not new**: it is the (1−θ)/2 exponent of L* |
| 3 | For (1−θ)/3 < Re s < (1−θ)/2 the variance of the twisted linear series is V(σ,t) ≍ \|t\|^{1−2σ_u}/log\|t\| (σ_u = Re s/(1−θ)): the dither cancellation **is lost** at frequencies \|t\| ≥ p | PROVED (§3, upper and lower bound of the variance) |
| 4 | Consequence: the exponential method (Perron on ζ_target·e^{L}) does not go below (1−θ)/2 | PROVED (§3) |
| 5 | Ω for the dither: with probability ≥ c > 0, N_𝒫(x) − cx ≠ O(x^{σ}) for every σ < (1−θ)/2 | ARGUED (§4; steps listed, two CITED) |
| 6 | O184.010a: does the dither diffuse the composites? | **NO** (resolved negatively modulo #5): the exponent of the full system with dither is (1−θ)/2, not (1+θ)/4 |
| 7 | "Theorem BFdisc′" (error < x^{1/3} with θ < 1/3 and zeros off the line) | **NOT obtained**. The 1/3 frontier is intact |
| 8 | L\*\_comp for every rounding ⇐ lower bound of the Montgomery–Vaughan mean value for L plus a fourth moment | OPEN; reduced to one estimate (§5) |
| 9 | Row D | unchanged |

## 1. The exact expansion

Dictionary (R171 (3.1), R184_010 §1): a = θ/(1−θ), v_{p,k} = p^{k/(1−θ)}, u := s/(1−θ), w := u − a = (s−θ)/(1−θ).
Target: c_{p,1} = p^a, and the c_{p,k}, k ≥ 2 of BFdisc, with ζ_target(s) = ∏_{p,k}(1 − v_{p,k}^{−s})^{−c_{p,k}} =
ζ(w)·(holomorphic factor of polynomial growth in the band considered, R163_891). Its nontrivial zeros lie at
Re s = θ + (1−θ)/2 = (1+θ)/2. With b_{p,k} = c_{p,k} + ε_{p,k}:

  ζ_𝒫(s) = ζ_target(s)·R(s),  log R(s) = Σ_{k≥1} Σ_{j≥1} j^{−1} Σ_p ε_{p,k} p^{−jku}.   (1.1)

(1.1) is an equality of formal Dirichlet series and holds wherever it converges. **It is linear in ε.** The "composite
terms" γ_{p₁}⋯γ_{p_k} of R184_010 §5 are the coefficients of exp(log R): they need not be canceled separately. But the price
is that N_𝒫 − cx = O(x^σ) requires polynomial growth of **e^{Re log R}** on Re s = σ. That is, it requires
sup_{|t|≤T} Re log R(σ+it) ≤ C log T, and it is not enough for log R to merely converge (Prop 2.2 of R184_001 and §3.3 below).
Integrality and sign: b = ⌊z + U + ½⌋ ≥ 0 integer (Lemma D1(iii)), c_{p,k} ≥ 0 (c^+ of BFdisc). The generalized integers
have nonnegative integer multiplicities because the monoid is free. OK.

## 2. Upper bound (PROVED)

Level k = 1, term j: L_j(u) := Σ_p ε_p p^{−ju}. By Lemma D1, ε_{p_k}p_k^{−a} = S_k − S_{k−1} and S_k = ν_k p_k^{−a}. Abel summation gives

  L_j(u) = Σ_k ν_k c_k^{(j)}(u) + (boundary → 0),  c_k^{(j)}(u) := p_k^{−a}(p_k^{a−ju} − p_{k+1}^{a−ju}).   (2.1)

Write u = σ_u + iτ, with τ = t/(1−θ). There are two bounds: |c_k^{(j)}| ≤ 2 p_k^{−jσ_u}, and
|c_k^{(j)}| ≪ (1+j|τ|) g_k p_k^{−jσ_u−1}, where g_k = p_{k+1} − p_k.

**Lemma 2.1.** For σ_u > 1/2 (j = 1) the series (2.1) is a martingale with Σ_k |c_k^{(1)}|² ≤ 4Σ_p p^{−2σ_u} < ∞,
uniformly in τ. Azuma over a τ-grid of step T^{−2} on [−T,T], with Lipschitz continuity in τ (|∂_τ c_k| ≪
p_k^{−σ_u} log p_k, summable in the deterministic tail p > T⁴ by the second bound), plus Borel–Cantelli over T = 2^m, give
a.s. sup_{|τ|≤T}|L_1(σ_u+iτ)| ≪ √log T, uniformly in σ_u ≥ ½ + δ. For j ≥ 2 and σ_u > 1/2 the series converges
absolutely (|ε| ≤ 3). The levels k ≥ 2 are equally good or better. ∎

Hence, on Re s ≥ (1−θ)/2 + δ: |R| = exp(O(√log|t|)) and |R|^{−1} as well. ζ_𝒫 has there exactly the zeros of
ζ_target, at Re s = (1+θ)/2 > 1/2, with polynomial growth. Perron (R184_001 Prop 2.2) gives

  **N_𝒫(x) = cx + O(x^{(1−θ)/2+ε})** a.s.   (2.2)

This is the exponent of L*, which for θ < 1/3 is > 1/3. Theorem D (linear, (1+θ)/4) is **not** inherited.

## 3. Why the dither does not diffuse the composites (PROVED)

**Proposition 3.1 (variance at frequency τ).** Let 1/3 < σ_u < 1/2 and j = 1. With V(σ_u,τ) := Σ_k |c_k^{(1)}(σ_u+iτ)|²:

  V(σ_u,τ) ≍ |τ|^{1−2σ_u}/log|τ|  (|τ| → ∞).

*Proof.* Write c_k = p_k^{−u}(1 − (p_{k+1}/p_k)^{a−u}) and φ_k := τ log(p_{k+1}/p_k) ≍ |τ|g_k/p_k.
- *Upper bound.* For p_k > |τ|log²|τ| we have |c_k| ≪ |τ|g_k p_k^{−σ_u−1}, and the tail sums to
  ≪ τ² Σ g_k² p^{−2σ_u−2} ≪ |τ|^{1−2σ_u}·(log)^{O(1)}. The log powers are removed using Σ_{p≤y} g_p² ≪ y log y
  (CITED: Heath-Brown / Selberg, unconditionally, in averaged form). For p_k ≤ |τ|log²|τ|, |c_k|² ≤ 4p_k^{−2σ_u} and the sum is
  ≍ (|τ|)^{1−2σ_u}/log|τ| by the PNT.
- *Lower bound.* For p_k ∈ [|τ|/4, |τ|/2], φ_k ≍ g_k ≥ 2 in modulus. Then |1 − (p_{k+1}/p_k)^{a−u}| =
  |1 − ρ_k e^{−iφ_k}|, with ρ_k = 1 + O(g_k/p_k). This is ≫ |sin(φ_k)| + o(1), and ‖φ_k/π‖ does not concentrate at 0 over
  a positive proportion of these k: φ_k = τ log(1+g_k/p_k) varies continuously with τ, so this holds for τ outside
  a set of arbitrarily small logarithmic density, which suffices for §4. Thus V ≫ Σ_{p∼|τ|} p^{−2σ_u}. ∎

**Interpretation.** Theorem D works because the test p ↦ Φ(X/p) is **smooth** at the scale of the gaps for p > √X.
The dither is blue noise: it kills the low frequencies in p. The exponential e^{L} contains all the tests p ↦ p^{−iτ} with
|τ| ≤ T ≈ x^{1−σ}, and for p ≤ |τ| those tests oscillate at the scale of the gaps. In the language of R184_010 §5, the
composites m = p₁⋯p_k with small factors **are** the high frequencies of log R. The heuristic X^{(k/(k+1))(1−2a)}
of R184_010 §5 matches: with σ_u ↔ the exponent, the mass |τ|^{1−2σ_u} over |τ| ≤ x^{1−σ} reproduces, in the limit,
X^{(1−2a)/2}.

**Corollary 3.2 (the method does not go below (1−θ)/2, PROVED).** For σ_s ∈ ((1−θ)/3, (1−θ)/2), Re L_1(σ+it) is a
martingale sum with variance V ≍ |t|^{δ}/log|t|, where δ = 1 − 2σ_u > 0. By Proposition 3.1 and the martingale central limit
theorem, Re L_1 is not O(log|t|) in probability. No Perron argument based on |R| ≤ |t|^C works.
**Caution (correction of the target):** the bound "L(σ+it) = O(log|t|) for σ > σ_L + δ" is only true with
σ_L = (1−θ)/2. The "linear" σ_L coming from Theorem D (convergence of L at a fixed point, up to σ_u > −1/2) is irrelevant
for uniform growth in t.

## 4. Ω for the dither (ARGUED)

Suppose N_𝒫 − cx = O(x^{σ'}) with σ' < σ < (1−θ)/2. Then ζ_𝒫(s) − c s/(s−1) = s∫E x^{−s−1}dx is holomorphic and
O(|s|) on Re s = σ (rigorous implication). Steps toward the contradiction, with u = σ/(1−θ) ∈ (1/3, 1/2):
(a) log R = L₁ + L₂ + A, where A converges absolutely (j ≥ 3, k ≥ 3, plus L₂ at level 2). L₂ has variance
    ≪ |t|^{1−4σ_u}, of lower order than that of L₁. [PROVED, same as Prop 3.1]
(b) E(Re L₁)=0, E(Re L₁)² ≍ V and E(Re L₁)⁴ ≪ V² (Burkholder–Rosenthal, bounded increments). Then
    E(Re L₁)⁺ = ½E|Re L₁| ≫ √V, and Paley–Zygmund gives P(Re L₁(σ+it) ≥ c√V) ≥ c₀ for each t. By Fubini, with
    probability ≥ c₀/2 the set A_T = {t ∈ [T,2T] : Re L₁ ≥ cT^{δ/2}} has measure ≥ c₀T/2. [PROVED up to
    constants]
(c) For the target: meas{t ∈ [T,2T] : log|ζ(w)| < −T^{δ/4}} ≪ T^{1−δ/4}, with Re w fixed ≠ 1/2. This follows from
    ∫_T^{2T}|log|ζ(σ_w+it)||dt ≪ T (CITED: Littlewood/Selberg; for Re w < 1/2 via the functional equation).
(d) Intersect the sets: |ζ_𝒫(σ+it)| ≥ exp(cT^{δ/2} − T^{δ/4} − O(1)), not O(|t|). This must be done "infinitely
    many times T = 2^m with probability ≥ c₀/2" (reverse Fatou). The event is not a tail event (U₁ affects all the b's), so
    only positive probability is obtained, not a.s.
Gaps in rigor: the control of L₂ and of A in the lower bound of (d), and Prop 3.1 outside an exceptional set in
τ. Label: **ARGUED**.

## 5. Every rounding: reduction of L\*\_comp (OPEN)

For any rounding in 𝒦_θ(C), by (1.1) and §4 it suffices to have the following:
(M2) ∫_T^{2T}|L₁(σ+it)|² dt ≫ T^{2−2σ_u−o(1)}. By the Montgomery–Vaughan mean value theorem, the block p ≤ T
     contributes T Σ_{p≤T}|ε_p|²p^{−2σ_u}(1+O(p/T)) ≥ T Σ‖p^a‖²p^{−2σ_u}, which is ≫ T^{2−2σ_u−o(1)} if ‖p^a‖ is not
     typically small. This depends on the equidistribution of p^a mod 1: FLAG CITED from memory, R184_010 #8.
     **Missing** is the interaction with the block p > T (analogous to step (c) of Prop M).
(M4) a fourth moment ≪ (M2)², which gives Re L₁ ⁺ large on a set of positive measure (∫ Re L₁ dt = O(1) because there is no p⁰ term).
**The only missing estimate** is (M2) with the tail p > T, without sign information on ε_p (which is precisely what
cannot be used, Corollary 2 of R184_010) **unless** the tail p > T is smooth in p at the scale of the gaps, where the blue
noise does kill it. That is why the dither is not a counterexample to (M2), and (M2) is plausible for every rounding.

## 6. Consequence for row D (honest)

It is a **class** statement (5G/O2601.1). The PROVED result (2.2) re-obtains that there exist discrete systems with
N = cx + O(x^{(1−θ)/2+ε}) and zeros at (1+θ)/2. No property "N = cx + O(x^{θ″})" with θ″ > (1−θ)/2 implies RH for
the class. θ″ < 1/3 is **not** obtained. It does not touch ζ. Row D does not move.

## For the audit

1. Is (1.1) correct with non-integer multiplicities in ζ_target? log(1−v^{−s})^{−c} = cΣv^{−js}/j: it is linear in c, so
   the quotient is exact.
2. Prop 3.1, lower bound: check that ‖φ_k/π‖ does not concentrate at 0 for p_k ∼ |τ|. There is a risk with resonant
   gaps (g_k ≡ multiples of π/(τ/p)). The way out is to average over τ, which is what §4 needs.
3. Could the dither be chosen so as to also kill the high frequencies ("multiscale" dither: impose bounded partial
   sums of ε_p p^{−a−iτ} for all τ ≤ T at once)? There is a single integer variable per prime and ≍ T constraints per
   block of primes p ∼ P ≤ T: the dimension count (R184_008 §3.3) says no. This is exactly
   (M2). This is the point where a counterexample would reopen O184.001a.
4. §4(d) only gives positive probability. Is that enough? For the verdict "the dither does not give BFdisc′", yes: a
   rounding with positive probability of failing is not an a.s. construction; moreover (2.2) is the best the method proves.
5. Check the dictionary: Re u = 1/2 ⇔ Re s = (1−θ)/2, and (1−θ)/2 > 1/3 ⇔ θ < 1/3.
