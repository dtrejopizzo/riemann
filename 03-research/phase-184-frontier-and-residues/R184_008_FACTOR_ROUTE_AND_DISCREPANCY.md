# R184_008 — Factor route (O184.001b) and rounding discrepancy (O184.001a)

Inputs: R184_001 (Prop 2.1, 2.2, O184.001a–c), R164_201 (Theorem L, §1, §3, §3.5,
Lemma D), R163_803 (eq. 2.2–2.3, Φ), R171_FINAL (BFdisc), `00-references/beurling-dmv/` (zbMATH, 2012.06220, 2211.08716).
RH is not claimed, nor the closure of D.

## State

| # | Statement | Label |
|---|---|---|
| 1 | Lemma AC: a generalized Euler product with multiplicities ≥ 0 and prime abscissa θ_Q has no zeros in Re s > θ_Q | PROVED (§1) |
| 2 | Theorem F (multiplicative rigidity): if B is exact (N_B = c_B x + O(x^θ), ζ_B(σ) ≠ 0 on (θ,1)) and P = B ⊔ Q with Q of multiplicities ≥ 0 and N_P = cx + O(x^θ), θ < 1, then Q has abscissa ≤ θ and the zeros of ζ_P in Re s > θ are exactly those of ζ_B | PROVED (§2) |
| 3 | Corollary: O184.001b ("multiplying ℕ by a factor") | **NO-GO** (PROVED), for every θ < 1, not only θ < 1/3 |
| 4 | Division variant P = B ∖ Q: every zero of ζ_P outside those of ζ_B in Re s>θ forces a REAL zero of ζ_P at σ_Q = abscissa of Q | PROVED (§2.3); the variant is not closed: OPEN |
| 5 | Overview: BFdisc (θ ∈ (1/3,1/2)) refutes rigidity; DMV / Broucke–Debruyne–Vindas: N = kx + O(x^{1/2+ε}) with zeros arbitrarily close to Re s = 1; θ < 1/3: nothing known | CITED / OPEN |
| 6 | The "Spencer discrepancy" framing for O184.001a is incorrect: the obstruction is blind to sign (integrality |ε_p| ≥ ‖p^a‖), not probabilistic | PROVED (observation, §3.1) |
| 7 | Sharp lower bound sup_X|T₁(X)| ≫ X^{(1−2a)/2} for every rounding | **OPEN** (not proved; L* remains ARGUED) |
| 8 | Linear model: rms_{[Y,2Y]} T₁ ≫ Y^{η(1−2a)/2−ε}, η = a/((1+a)(3−a)), for every integer rounding | PROVED in the model (§3.2; audit pass pending); does not qualitatively improve on Theorem L's range |
| 9 | Row D movement | none |

## 1. Lemma AC (absolute convergence)

Let Q be a system of generalized primes 1 < q₁ ≤ q₂ ≤ … with multiplicities m_q ≥ 0 (integer or real), Π_Q(x) = Σ_{q≤x} m_q,
and θ_Q = inf{σ : Σ_q m_q q^{−σ} < ∞}.

> **Lemma AC.** For Re s > θ_Q, ζ_Q(s) = ∏_q (1 − q^{−s})^{−m_q} converges absolutely and ζ_Q(s) ≠ 0.
> Moreover θ_Q is also the abscissa of convergence of Σ_n a_n n^{−s} = ζ_Q(s) (coefficients a_n ≥ 0), i.e.
> N_Q(x) = O(x^{θ_Q+ε}) and not O(x^{θ_Q−ε}) (if θ_Q > 0).

*Proof.* For σ = Re s > θ_Q, log ζ_Q(s) = Σ_q m_q Σ_{k≥1} q^{−ks}/k; |·| ≤ Σ_q m_q Σ_k q^{−kσ}/k ≤ Σ_q m_q q^{−σ}·(1−q₁^{−σ})^{−1} < ∞.
So log ζ_Q is an absolutely convergent, holomorphic series, and ζ_Q = exp(log ζ_Q) ≠ 0. Abscissas: for real σ > 0,
Σ_q m_q q^{−σ} ≤ log ζ_Q(σ) ≤ C_σ Σ_q m_q q^{−σ} (both series with terms ≥ 0), and ζ_Q(σ) = Σ a_n n^{−σ}; hence
the two series converge or diverge together for real σ, and since coefficients are ≥ 0 the abscissa of convergence coincides with that
of absolute convergence. The relation to N_Q is standard partial summation. ∎

Direct consequence: N_Q = O(x^{θ}) with θ < 1/2 ⟹ ζ_Q has no zeros in Re s > θ ⊇ {Re s > 1/2}.

## 2. Theorem F: a multiplicative factor never contributes zeros to the right of θ

**Hypothesis.** B a discrete (or continuous) system with N_B(x) = c_B x + O(x^θ), θ < 1, c_B > 0, and ζ_B(σ) ≠ 0 for σ ∈ (θ, 1)
real. (For B = ℕ: ζ(σ) < 0 on (0,1), classical PROVED.) Q with multiplicities ≥ 0, P = B ⊔ Q (multiplicities add),
so that N_P = N_B ∗ N_Q (multiplicative convolution) and ζ_P = ζ_B ζ_Q.

> **Theorem F.** If N_P(x) = c x + O(x^θ), then θ_Q ≤ θ. Consequently ζ_Q has no zeros in Re s > θ (Lemma AC)
> and {zeros of ζ_P in Re s > θ} = {zeros of ζ_B in Re s > θ}, with multiplicities.

*Proof.* (i) N_P = cx + O(x^θ) ⟹ ζ_P(s) − cs/(s−1) = s∫_1^∞(N_P − cx)x^{−s−1}dx + const is holomorphic in Re s > θ;
so ζ_P is meromorphic in Re s > θ with a single simple pole at s = 1. The same for ζ_B. (ii) Since N_P ≥ N_Q·N_B(1)… more
simply N_Q ≤ N_P pointwise (the Q-integers are P-integers), θ_Q ≤ 1. (iii) Suppose θ_Q > θ. By the
Landau theorem (generalized Dirichlet series with coefficients ≥ 0; CITED, classical), ζ_Q has a singularity at the
real point σ_Q := θ_Q ∈ (θ, 1]. But in a neighborhood of σ_Q, ζ_Q = ζ_P/ζ_B: if σ_Q < 1, ζ_P and ζ_B are holomorphic there
and ζ_B(σ_Q) ≠ 0 by hypothesis, so ζ_Q is holomorphic at σ_Q; if σ_Q = 1, ζ_P/ζ_B has a removable singularity at 1
(both simple poles, residues c, c_B > 0) and is holomorphic there. Contradiction. Hence θ_Q ≤ θ. (iv) Lemma AC. ∎

**2.1 Corollary (O184.001b, NO-GO).** With B = ℕ (θ_B = 0): no system P = ℕ ⊔ Q with N_P = cx + O(x^θ), θ < 1,
has zeros of ζ_P in Re s > θ that are not zeros of ζ. In particular, for θ < 1/2, the zeros of ζ_P in Re s > 1/2 are
exactly those of ζ: the factor route produces a counterexample to rigidity only if ζ already has zeros off the line.
The argument covers the "dense Q" case of the objective (Π_Q ≫ x^{1/2}) without estimating cancellations: cancellation between
ℕ's error and Q's error is impossible because the Landau pole of ζ_Q at the real σ_Q would have to be cancelled by a real zero
of ζ_B on (θ,1), which does not exist. This is the "pole at β" argument of the objective, made rigorous and without assuming N_Q ~ x^β.

**2.2 Scope.** Theorem F uses neither integrality nor θ < 1/3: it is a positivity obstruction (Landau). It holds equally for
B = any exact system of R163_102 (N = ρx + O(1)) and for B = systems of R166_701 (θ = 0), as long as ζ_B has
no real zeros on (θ,1). If B had a real zero β₀ ∈ (θ,1), Q could have abscissa β₀ and contribute zeros in
Re s ∈ (θ, β₀]; but then B itself already refutes rigidity (β₀ > 1/2) or is useless (β₀ ≤ 1/2). There is no gain.

**2.3 Division variant.** P = B ∖ Q (multiplicities m_B − m_Q ≥ 0), ζ_P = ζ_B/ζ_Q. The new zeros of ζ_P in
Re s > θ are poles of ζ_Q. Landau applied to ζ_Q = ζ_B/ζ_P: if θ_Q > θ, σ_Q is a singularity, and since ζ_B is holomorphic
and nonzero at σ_Q ∈ (θ,1) (or with a simple pole at 1 that is compensated), necessarily **ζ_P(σ_Q) = 0 (real zero)**. That ζ_P(σ) → −∞ to the
left of 1 does not forbid it. Thus: the division variant requires a real zero of ζ_P in (θ,1); it is not refuted here.
It is essentially the general problem (any P ⊂ primes of ℕ is of this form). **OPEN**, no new reduction.

## 3. O184.001a: can a rounding cancel T₁?

Notation of R164_201 §1: a = θ/(1−θ) ∈ (0,1/2), X = x^{1−θ}, T₁(X) = Σ_{p≤X} ε_p p^{−a} Φ(X/p), Φ = −ψ + O(·^{−1})
(R163_803 eq. 2.2), ε_p ∈ ℤ − p^a, |ε_p| ≤ C.

**3.1 The Spencer framing does not apply (PROVED, observation).** The objective proposed: "Spencer does not beat √, so
cancellation by independent signs is NO-GO." Two corrections:
- The linear discrepancy of interval-type families is O(1) (carry rounding: Σ_{p≤y}ε_p p^{−a} ∈ [−1,1]). R164_201 §1
  already records this: the carry controls p > X/J. Hence there is no "à la Spencer" lower bound valid over the whole range.
- In 𝒦_θ, |ε_p| ≥ ‖p^a‖ by integrality (Lemma W(i)). The correct lower bound is blind to sign: Bessel against the
  nearly orthogonal tests ψ(X/q) (Franel identity). This is exactly the mechanism of Theorem L. No correlation
  among the ε_p can help in the modulus range where Bessel applies; the problem is **the range of q**, not the signs.

**3.2 Proposition M (linear model, PROVED in the model).** Let Y be large, Q = Y^{η−ε}, η = a/((1+a)(3−a)). For every
choice ε_p ∈ ℤ − p^a, |ε_p| ≤ C,
  (1/Y)∫_Y^{2Y}|T₁(X)|²dX ≫ Σ_{q≤Q, ‖q^a‖≥1/4} q^{−2a} ≫ Q^{1−2a}/log Q.

*Proof (full scheme of constants).* φ_q(X) := ψ(X/q). For q ≤ Q:
(a) Franel in a finite window: ∫_Y^{2Y}φ_pφ_q = Y/(12pq) + O(pq) (p ≠ q primes), Y/12 + O(q) (p = q).
(b) Split T₁ = T_≤ + T_> with cutoff P₁ = q^{(1+a)/a}Y^{ε}. For p ≤ P₁: ⟨T_≤, −φ_q⟩ = (Y/12)ε_q q^{−a} + O(Y/q)
    + O(q P₁^{2−a}); the O(Y/q) term uses Σ_p|ε_p|p^{−1−a} < ∞.
(c) For p > P₁: g = T_> has sup|g| ≪ Y^{1−a} and total variation on [Y,2Y] ≪ Y Σ_{p>P₁}p^{−1−a} + Y^{1−a} ≪ Y P₁^{−a} + Y^{1−a};
    integrating against φ_q (zero mean over each period q): |⟨g,φ_q⟩| ≪ q(Y P₁^{−a} + Y^{1−a}).
(d) The errors are o(Y q^{−a}) if q^{1+a} ≪ Y^{a−ε}, q^{1+a}P₁^{−a} ≪ Y^{−ε} (choice of P₁), and q P₁^{2−a} ≪ Y^{1−ε}q^{−a},
    i.e. q^{(1+a)(2−a)/a+1+a} ≪ Y^{1−ε}; the minimum of the exponents gives η. The Φ + ψ = O(p/X) term contributes ≪ Q^{2−a}/Y.
(e) Gram of {φ_q}_{q≤Q}: maximum eigenvalue ≤ Y/12 + O(Y Σ1/q²) + O(Q³) ≤ Y/4 (Q³ = o(Y)). Bessel:
    ‖T₁‖² ≥ (4/Y)Σ_q|⟨T₁,φ_q⟩|² ≫ Y Σ_q ε_q²q^{−2a}, and |ε_q| ≥ ‖q^a‖ ≥ 1/4 for a positive proportion of q
    (Lemma W, equidistribution of q^a mod 1: CITED from memory, already FLAGGED in R164_201). ∎

In exponents of x: the error of T₁ is ≫ x^{θ + δ_M}, δ_M = η(1−θ)(1/2 − a)·(1−ε). This is of the same type as Theorem L
(κ = a/(5/2+a)); the model avoids the equidistribution of h_n mod p but ignores the interaction with the rest of E, so
it **does not replace** Theorem L for the system. L* is not promoted to PROVED.

**3.3 Where the real gap lies.** For the sharp bound X^{(1−2a)/2}, tests up to q ≈ Y^{1−ε} are needed. For q ≫ Y^{1/2}
the functions ψ(X/q) have ≲ Y/q periods in [Y,2Y] and cease to be nearly orthogonal (error O(pq) ≥ Y); moreover for
q ≫ Y^{η} the carry partially controls T₁ (§3.1). Neither Bessel nor Spencer resolve this range. What would be needed
is one of two things:
- (L*-yes) a large sieve over moduli q ∈ (Y^η, Y^{1−ε}) for the family {ψ(·/q)} with weights ε_q q^{−a} — an energy
  lower bound for "Franel sums" over a long range; or
- (O184.001a-yes) a structured rounding that, in that range, makes Σ_q ε_q q^{−a}ψ(X/q) = o(X^{(1−2a)/2}) uniformly,
  i.e. the vector (ε_q q^{−a})_{q∈(Y^η,Y]} is nearly orthogonal to all the sawtooths ψ(X/q), X ∈ [Y,2Y]. With ≍ Y/log Y
  integer degrees of freedom and ≍ Y constraints of size ≲ 1, a dimension count does not exclude it.
Both remain **OPEN**. O184.001a remains the only live construction below 1/3; O184.001b is closed.

## 4. What is known about rigidity (CITED)
- Beurling 1937: N = cx + O(x/log^γ x), γ > 3/2 ⟹ PNT. Gives no zero-free region in a strip.
- Diamond–Montgomery–Vorhauer (2006) and its generalization (Broucke–Debruyne–Vindas, `00-references/beurling-dmv/2012.06220`,
  `2211.08716`; zbMATH summary in `zbMATH-records.txt`): systems with N = kx + O(x^{1/2}exp(c(log x)^{2/3}))
  and ζ_P with infinitely many zeros on σ = 1 − 1/log t. So rigidity fails for every θ > 1/2 (CITED).
- BFdisc (R163_803/R163_891, R171_FINAL): fails on θ ∈ (1/3, 1/2) with zeros in Re s > 1/2 (PROVED on record).
- θ = 0 with ζ_P = ζ is RH; θ < 1/3 in general: **OPEN**. Theorem F shows that any construction must have
  Π_P − Π_target with genuine cancellation, not factorizable as a product by a system of multiplicities ≥ 0.

## For the audit
1. Theorem F (iii): verify Landau for generalized Dirichlet series (frequencies log n_k of a Beurling system,
   coefficients ≥ 0) and the case σ_Q = 1 (removability of ζ_P/ζ_B at 1 requires only simple poles, residues > 0).
2. Theorem F (i): that N_P = cx + O(x^θ) implies meromorphic continuation to Re s > θ — immediate from the Mellin integral.
3. Hypothesis ζ_B(σ) ≠ 0 on (θ,1): classical for B = ℕ; must be checked case by case for other B.
4. Negative multiplicities of Q ("virtual" Q) fall outside Theorem F: then there is no Landau. This is variant 2.3 / the general case.
5. Prop. M: check the choice of P₁ and the exponent η in (d); the use of equidistribution of q^a mod 1 inherits the FLAG from R164_201.
6. §3.1 does not prove L* false: only that the Spencer-type argument proposed in the objective is not the correct one.

## Note (R184_092)

* Prop M: the correct η is a/(2(1+a)); Gram as rank one + O(Q³); exclude small q. Lemma AC: the abscissa fails if Q is finite (θ_Q=−∞ vs 0). Theorem F verified, including σ_Q=1.
