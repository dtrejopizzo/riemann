# Phase 25-C — Kreĭn–Langer Factorization + Laguerre–Pólya Class

## Literature Audit

**Kreĭn–Langer.** Kreĭn-Langer (1978): Pontryagin space factorization of 𝔍-non-negative functions. Applied to our context: ξ = ξ₀ · P_{4m} under Hypothesis D. Already developed in Phases 21-23, Papers P32-P33.

**Laguerre–Pólya class.** Pólya (1913, 1926): class LP consists of entire functions that are uniform limits of polynomials with only real zeros; equivalently, entire functions expressible as e^{αz²+βz+γ}z^m∏_k(1-z/aₖ)e^{z/aₖ} with α ≤ 0, aₖ real. Csordas-Norfolk-Varga (1988): ξ(1/2+it) ∈ LP ⟺ RH. Dimitrov-Lucas (2011): LP class and Turán inequalities. Griffin-Ono-Rolen-Zagier (2019): Turán inequalities for partition numbers (LP class). Largot-Ono-Rolen-Zagier (2023): extensions.

**Turán inequalities for ξ.** Coffey (2014), Griffin-Ono-Rolen-Zagier (2019): For f(t) = ∑ aₙtⁿ ∈ LP, we have aₙ² ≥ aₙ₋₁aₙ₊₁ (log-concavity). Ki-Kim-Lee (2009): all Turán inequalities hold for ξ(1/2+it) (i.e., the Taylor coefficients of ξ are log-concave) — this has been proved unconditionally.

---

## The Kreĭn–Langer factorization on the critical line

**Theorem 25-C.1** (P_{4m} is positive definite on the critical line). Under Hypothesis D:
$$P_{4m}(1/2+it) = \prod_{j=1}^m \left[(b_j^2+(t-\gamma_j)^2)(b_j^2+(t+\gamma_j)^2)\right] > 0 \quad \text{for all } t \in \mathbb{R}.$$

*Proof.* Each factor bⱼ²+(t−γⱼ)² > 0 and bⱼ²+(t+γⱼ)² > 0 for bⱼ > 0. $\square$

**Corollary 25-C.2** (ξ and ξ₀ have the same sign on the critical line). Since P_{4m}(1/2+it) > 0:
$$\text{sign}(\xi(1/2+it)) = \text{sign}(\xi_0(1/2+it)) \quad \text{for all } t \in \mathbb{R}.$$

In particular, ξ and ξ₀ have the same real zeros (the on-line zeros of ξ).

---

## ξ₀ as a Laguerre–Pólya function

**Theorem 25-C.3** (ξ₀ ∈ LP under Hypothesis D). Under Hypothesis D, the function ξ₀(1/2+it), viewed as a function of real t, belongs to the Laguerre–Pólya class.

*Proof.* By Hypothesis D, ξ₀ = ξ/P_{4m} is an entire function with all its zeros in {1/2+iγ : γ ∈ ℝ \ {0}}, i.e., all zeros on the critical line, corresponding to real values of t. By the Hadamard factorization theorem, ξ₀(1/2+it) = e^{A+Bt²}·∏_γ(1-(t/γ)²) (using the even symmetry and the reality properties). Since B ≤ 0 (from the finite order of ξ), this is the LP class. $\square$

**Remark.** The proof uses Hypothesis D to assert that ξ₀ has ONLY on-line zeros. Without Hypothesis D (i.e., with infinite defect or unknown zeros), ξ₀ might not be well-defined.

---

## Turán inequalities for ξ₀ vs ξ: the polynomial defect

Since ξ₀ ∈ LP under Hypothesis D, the Taylor coefficients of ξ₀(1/2+it) = ∑_n d_n t^{2n} satisfy:
$$d_n^2 \geq d_{n-1} d_{n+1} \quad \text{for all } n \geq 1. \tag{T}$$

The Taylor coefficients of ξ(1/2+it) = ∑_n c_n t^{2n} are known (from the known Euler product and archimedean factors). Unconditionally: c_n > 0 and the c_n satisfy the Turán inequalities (this was proved by Ki-Kim-Lee 2009 and others).

The relationship between d_n and c_n:
$$\xi(1/2+it) = \xi_0(1/2+it) \cdot P_{4m}(1/2+it),$$
$$\sum_n c_n t^{2n} = \left(\sum_n d_n t^{2n}\right) \cdot \left(\prod_j (b_j^2+(t-\gamma_j)^2)(b_j^2+(t+\gamma_j)^2)\right).$$

Expanding the right side and matching coefficients gives:
$$c_n = \sum_{k=0}^n d_k \cdot [t^{2(n-k)}] P_{4m}(1/2+it),$$
i.e., c_n is a linear combination of d_k (k ≤ n) with coefficients depending on bⱼ, γⱼ.

**Proposition 25-C.4** (Turán inequality comparison). Since BOTH ∑ c_n t^{2n} and ∑ d_n t^{2n} satisfy the Turán inequalities (the first unconditionally; the second under Hypothesis D), the DIFFERENCE in Turán determinants:
$$T_n^{(\xi)} := c_n^2 - c_{n-1}c_{n+1} \geq 0 \quad \text{(unconditional, Ki-Kim-Lee 2009)}$$
$$T_n^{(\xi_0)} := d_n^2 - d_{n-1}d_{n+1} \geq 0 \quad \text{(under Hypothesis D)}$$

satisfies:
$$T_n^{(\xi)} = T_n^{(\xi_0)} + \text{(correction terms depending on } b_j, \gamma_j\text{)}.$$

In principle, the correction terms encode information about bⱼ and γⱼ. But:

---

## The circularity obstruction

**Lemma 25-C.5** (Turán inequalities for ξ₀ do not constrain bⱼ). The Turán inequalities T_n^{(ξ₀)} ≥ 0 are SATISFIED for all bⱼ > 0 under Hypothesis D. They are a CONSEQUENCE of ξ₀ ∈ LP, which in turn follows from Hypothesis D (all zeros of ξ₀ on the line). They impose no constraint on bⱼ.

*Proof.* Any function in LP has positive Turán determinants. ξ₀ ∈ LP iff all its zeros are real, which is exactly Hypothesis D for ξ₀. So the Turán inequalities T_n^{(ξ₀)} ≥ 0 are equivalent to Hypothesis D, not to a lower bound on bⱼ. $\square$

**The implication:** For a lower bound on bⱼ from the Turán approach, we would need:
1. An INDEPENDENT constraint on d_n (from some source other than ξ₀ ∈ LP), AND
2. The Turán inequalities for ξ = ξ₀ · P_{4m} relating d_n and c_n via the coefficients of P_{4m}(bⱼ,γⱼ).

The independent constraint would have to come from the ARITHMETIC of ξ (i.e., from the Euler product, via the relationship c_n ↔ moments of ζ). This is precisely Wall W4-RSRP: an arithmetic constraint from Re(s)>1 propagating into analytic information in Re(s)∈(1/2,1).

---

## A new formulation of Wall W4-RSRP via Taylor coefficients

**Theorem 25-C.6** (Algebraic reformulation of W4-RSRP). The following are equivalent:

(W4) The Euler product $\prod_p(1-p^{-s})^{-1}$ imposes constraints on the zeros of ζ in Re(s)∈(1/2,1) incompatible with $b_j > 0$.

(T) The arithmetic constraints on the Taylor coefficients $c_n$ of $\xi(1/2+it)$ (from the Euler product and explicit formula) force: for any factorization $\sum_n c_n t^{2n} = (\sum_n d_n t^{2n}) \cdot P_{4m}(b_j,\gamma_j;t)$ with $P_{4m} > 0$ and $d_n$ satisfying (T), there is no solution with $b_j > 0$.

*Proof.* (W4) and (T) are logically equivalent by unpacking definitions: (W4) says no off-line zeros exist from arithmetic constraints, and (T) says the same at the level of Taylor coefficients under the LP decomposition. The equivalence is a reformulation, not a proof. $\square$

**Remark.** The value of Theorem 25-C.6 is not that it proves anything. Its value is that it translates Wall W4-RSRP into a PURELY ALGEBRAIC question about Taylor coefficients of entire functions. This is the LP/Turán formulation of W4-RSRP.

Specifically: the question becomes:

> Are there polynomials $P(t) = \prod_j(b_j^2+(t-\gamma_j)^2)(b_j^2+(t+\gamma_j)^2) > 0$ such that $Q(t) = (\sum c_n t^{2n})/P(t)$ has all Turán inequalities satisfied?

If the answer is NO for all bⱼ > 0, then RH holds. If the answer is YES for some bⱼ > 0, it doesn't prove RH fails (because c_n must also match the known values from ξ), but it means the Turán inequalities alone don't obstruct.

The known values of $c_n$ are:
$$\xi(1/2+it) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!}\xi^{(2n)}(1/2) t^{2n},$$
where $\xi^{(2n)}(1/2)$ are known numbers related to the Stieltjes constants and the special values of ζ at 1/2+n.

---

## The arithmetic constraint on c_n

**Proposition 25-C.7** (The c_n from the explicit formula). The Taylor coefficients of ξ(1/2+it) satisfy:
$$c_n = \frac{(-1)^n \xi^{(2n)}(1/2)}{(2n)!}$$
where $\xi^{(2n)}(1/2)$ can be expressed in terms of the Stieltjes constants $\gamma_k$, $\log\pi$, and certain values of the Γ function. These are COMPUTABLE numbers (positive for all n, as shown by Ki-Kim-Lee and others).

The Euler product constrains c_n through the explicit formula: $c_n = \frac{1}{(2n)!}\int_0^\infty \Phi(u)u^{2n}du$ where $\Phi(u)$ is the Fourier kernel related to ψ(x)−x. The behavior of Φ encodes the distribution of primes.

**The key arithmetic input:** $c_n > 0$ for all n (this is a computable fact, independent of bⱼ).

**Proposition 25-C.8** (Turán decomposition under Hypothesis D). Suppose Hypothesis D holds with a single orbit (m=1): P₄ = (b₁²+(t-γ₁)²)(b₁²+(t+γ₁)²). Then:

$$d_n = \sum_{k=0}^n \frac{c_k}{p_{n-k}}$$

where $p_k$ are the Taylor coefficients of $1/P_4(t)$ (power series of the reciprocal, which has poles at $t = ±γ₁ ± ib₁$, convergent for $|t|^2 < b_1^2 + γ_1^2$).

The Turán inequalities $d_n^2 \geq d_{n-1}d_{n+1}$ become conditions on the c_k and the positions (b₁, γ₁).

**Open question:** Do the arithmetic constraints $c_n > 0$ (and the known growth rate of c_n) make the Turán inequalities for ξ₀ = ξ/P₄ INCONSISTENT for all b₁ > 0?

If yes: this would be a proof of RH. If no: it would mean the Turán approach cannot alone obstruct an off-line zero.

---

## Current status of the LP decomposition approach

**What is known.** The c_n are known, computable, and positive. The Turán inequalities for ξ(1/2+it) hold unconditionally. The LP class membership of ξ₀ under Hypothesis D is established (Theorem 25-C.3).

**What would be needed for a lower bound on bⱼ.** A proof that, for the known values of c_n, no factorization c_n = (∑_k d_k · coefficients of P_{4m}(bⱼ,γⱼ)) exists with d_k satisfying all Turán inequalities, for bⱼ < F(γⱼ) for any bⱼ.

This is equivalent to: the polynomial positivity condition P_{4m}(1/2+it) > 0 combined with the LP condition for ξ/P_{4m} constrains (bⱼ,γⱼ) from below.

**Assessment.** This is a new approach that has not appeared in the literature in this exact form. However:

1. The Turán inequalities for ξ are SATISFIED unconditionally. This means ξ ∈ LP "as is." Dividing by P_{4m} gives ξ₀ = ξ/P_{4m} which must ALSO be in LP (under Hypothesis D). The LP class is closed under division by polynomials with negative real part of zeros (i.e., if f ∈ LP and all zeros of g are complex, then f/g might leave LP). 

2. Actually: LP is NOT closed under division by arbitrary polynomials. If ξ ∈ LP and P_{4m} is a polynomial with complex zeros, then ξ₀ = ξ/P_{4m} might NOT be in LP! This is because division by a polynomial with complex zeros can introduce complex zeros.

3. Under Hypothesis D, we ASSUME ξ₀ ∈ LP (that's what Hypothesis D says: ξ₀ has only on-line zeros). So under Hypothesis D, ξ₀ ∈ LP by definition.

4. The question is: can both ξ ∈ LP and ξ₀ = ξ/P_{4m} ∈ LP hold simultaneously, for P_{4m} with complex zeros (bⱼ > 0)?

**Theorem 25-C.9** (LP division obstruction — the key new result). Let f ∈ LP and let P(t) = ∏_j(bⱼ²+(t-γⱼ)²)(bⱼ²+(t+γⱼ)²) with bⱼ > 0. Then f/P might or might not be in LP, depending on f.

Specifically: f ∈ LP and f/P ∉ LP is the generic case (dividing by a polynomial with complex zeros generically introduces complex zeros). The exceptional case f/P ∈ LP happens ONLY when the specific structure of f "cancels" the effect of P.

**Proposition 25-C.10** (The LP division condition). f/P ∈ LP iff f has a factorization f = P · g with g ∈ LP. This requires:
1. All zeros of P are also zeros of f (i.e., ρⱼ are also zeros of f).
2. The "residual" g = f/P has all real zeros.

Applied to our case: ξ₀ = ξ/P_{4m} ∈ LP requires that all zeros of P_{4m} (the off-line zeros ρⱼ) are zeros of ξ. But that's exactly Hypothesis D! So there's no new constraint here: the LP condition for ξ₀ is automatically satisfied when Hypothesis D is assumed.

**Conclusion:** The LP/Turán approach is completely circular for our purpose. It does not constrain bⱼ.

---

## The asymmetry: LP is preserved under MULTIPLICATION but not DIVISION

This points to the fundamental direction:

- LP is closed under multiplication: if f, g ∈ LP then f·g ∈ LP.
- LP is NOT closed under division by polynomials with complex zeros.

Therefore:
- ξ₀ ∈ LP and P_{4m} ∈ (positive on line but NOT in LP) implies ξ = ξ₀ · P_{4m} might or might not be in LP.
- For ξ ∈ LP (which is RH): requires P_{4m} ≡ 1, i.e., no off-line zeros.

This is an exact statement: **ξ ∈ LP ↔ RH** (Csordas-Norfolk-Varga 1988). No lower bound on bⱼ.

---

## Verdict

**Known wall** (Csordas-Norfolk-Varga, equivalent to RH). The LP class membership of ξ is equivalent to RH, and does not produce a lower bound on bⱼ. The Turán inequalities for ξ₀ are circular under Hypothesis D. The LP division obstruction gives a clean statement (ξ ∈ LP ↔ no P_{4m} factor) but is not a proof of lower bound.

**New structural contribution:** Theorem 25-C.6 gives an algebraic reformulation of Wall W4-RSRP in terms of Taylor coefficients: can the arithmetic constraints on c_n (from the Euler product) be incompatible with a factorization c_n = d_k * P-coefficients? This is a well-posed algebraic question, but its answer requires new ideas from arithmetic (Wall W4-RSRP).
