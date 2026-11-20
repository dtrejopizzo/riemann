# AUDIT_004 — Control of the denormalised coprime Mellin

2026-10-18. Independent review of the insight and of the final memo CONSTRUCTOR_004.

**Final verdict: PROVED for the declared signs, identities and integrabilities. Link with Q_T and full specificity OPEN.**

## 1. Exact asymptotics

Let d,e≥2 be fixed coprime, l=de, c=y^(−1/2), r=√y and A=(d−1)(e−1)/(de)>0. Poisson implies

    τ(k²y)=c/k−1+O_k(c exp(−π/(k²y)))

for each fixed k. Substituting into B_y=τ(l²y)−τ(d²y)τ(e²y)/τ(y), and using τ(y)~c,

    B_y(d,e)=−A c/(c−1)+O_{d,e}(c exp(−π/(l²y)))
             =−A/(1−√y)+exponential error with factor c.

The computation of the numerator is exact for the error-free terms:

    (c/(de)−1)(c−1)−(c/d−1)(c/e−1)=−A c.

Hence B_y→−A and

    C_y(d,e)=−A√y/(1−√y)²+O_{d,e}(exp(−π/(l²y)))
             ~−A√y.

This refines the O(√y) of CONSTRUCTOR_002 and shows the automatic cancellation of the coprime coefficient G₀. **PROVED.**

## 2. Direct Mellin

By ANTICORRELATION_003, B_y=τ(y)C_y is strictly negative for all y>0 on those indices. It is bounded at zero and decreases exponentially at infinity. Hence

    J_α(d,e)=∫_0^∞ y^(α−1)B_y(d,e)dy

converges absolutely for Re α>0, defines a holomorphic function there and satisfies J_α<0 for real α>0. In particular α=1/4 is directly admissible. No coprime counterterm is subtracted because G₀(d,e)=0. **PROVED.**

For pairs with gcd(d,e)>1,

    B_y=y^(−1/2)G₀−A/(1−√y)+exponential error,
    G₀=(gcd(d,e)−1)/(de)>0.

The integral without subtraction converges near zero only for Re α>1/2. Do not extend the direct result to the diagonal or to powers of the same prime. Its regularised continuation remains R_α of CONSTRUCTOR_002 and its sign is not proved here.

## 3. Language and scope

B removes the outer normaliser of the covariance, but keeps the quotient τ(d²y)τ(e²y)/τ(y). It is not a denominator-free theta kernel. Its first term has classical Mellin Γ(α)ζ(2α)l^(−2α) for Re α>1/2; the second is nonlinear. At α=1/4 the DIFFERENCE integrates directly for coprime pairs, while separating both terms requires their continuations.

"Partial critical Mellin sign" is admissible only if it means this parameter α=1/4 and the distinction with the effective node weight is kept. It does not prove n^(−1/2) homogeneity of the whole kernel, nor cancel diagonal, gamma or polar of Q_T. Nor does it prove a quadratic inequality for arbitrary coefficients from negative entries: the products conjugate(a_d)a_e may change sign.

**Auxiliary positive:** −J_α(d,e)>0 for coprime pairs and real α>0, with exact cancellation of the divergence term. **Link with Q_T: OPEN.**

## 4. Revised extension to complete valuations of two primes

**PROVED for fixed primes p≠q.** It is not limited to one power of each prime.

For c=y^(−1/2)≥2, the integral comparison of the decreasing Gaussian and Poisson give c−1≤τ(y)≤c. More generally, δ_k=τ(k²y)−c/k belongs to [−1,0]. The algebraic identity

    B_y(d,e)=δ_de+
      [cδ_1/(de)−cδ_e/d−cδ_d/e−δ_dδ_e]/(c+δ_1)

holds for coprime indices. Hence

    |B_y(d,e)|≤1+[c(1/de+1/d+1/e)+1]/(c−1)≤9/2<5.

Moreover −B_y≤τ(d²y)τ(e²y)/τ(y)≤2c/(de). Hence

    0<−τ(y)Cov_y(v_p,v_q)
       =Σ_{j,k≥1}(−B_y(p^j,q^k))
       ≤Σ_{j,k≥1}min(5,2c p^(−j)q^(−k))
       =O_{p,q}(log² c).

For the last bound, cut at J=ceil(log_p c), K=ceil(log_q c). The rectangle contributes ≤5JK. Each tail is bounded geometrically by O_{p,q}(cp^(−J))+O_{p,q}(cq^(−K))=O_{p,q}(1). Since c≥2, the constant term is absorbed by log²c.

For y≥1, S_p(y)=Σ_j τ(p^(2j)y)=O_p(exp(−πp²y)); this is obtained by summing the Gaussian weights of the multiples of the powers of p, or by first dominating each theta sum and then the geometric tail in j. Since τ(y)≥2exp(−πy),

    0<−τ(y)Cov_y(v_p,v_q)
       ≤S_p(y)S_q(y)/τ(y)
       =O_{p,q}(exp(−π(p²+q²−1)y)).

The inequality used preserves the sign because all cross B are negative. These bounds justify the transform

    L_α(p,q)=−∫_0^∞ y^(α−1)τ(y)Cov_y(v_p,v_q)dy>0

for real α>0, absolutely convergent and holomorphic for Re α>0. At α=1/4 it requires no subtraction. Tonelli for the positive integrand allows summing ALL powers and writing L_α=Σ_{j,k}(−J_α(p^j,q^k)).

It has not been summed over ALL primes with weights Λ, nor has the diagonal p=q been controlled. The constant of the bound depends on p,q and does not imply sufficient uniformity for that sum. The extension produces a strict Mellin sign of interaction between two complete prime factors, not the sign of an arbitrary form of the node.

## 5. Final review of the memo CONSTRUCTOR_004

All sections reviewed, including the extension to powers and the mixture at σ>1. **Approved** with the deletion precision noted and corrected in the memo.

- **Lemma 1 and Theorem 2:** asymptotics, convergence and sign coincide with §§1–2 of this audit.
- **Theorem 3:** for a fixed sum, strict concavity increases the product of τ as both logarithmic arguments approach each other. (3,10) is more balanced than (2,15), which proves A(3,10)>A(2,15). It is non-dependence on the product in the indicated domain of coprime integers. It is not by itself a statement about the restriction to prime powers, nor about operators in heights.
- **Mellin formula §4:** the change z=k²y gives the exact factor k^(−2α). The regularisation of τ has residue 1 at α=1/2 and coincides with 2π^(−α)Γ(α)ζ(2α). The counterterms of the two parts are equal for l=de; subtracting them yields A=J−Z(de)^(−2α), correct sign and factor 2. At α=1/4 exactly 1/√(de) appears in that term, while the full kernel keeps the non-homogeneous quotient.
- **Mixture §7:** for α>1/2, τ(y)y^(α−1)/Z_α is a probability and the marginal on nonzero integers is |n|^(−2α)/(2ζ(2α)). The prime valuations are independent geometric under that marginal by absolutely convergent factorisation. Total covariance proves the exact cancellation of the two cross terms. Each q_y(d) is strictly decreasing because f'(x+2log d)−f'(x)<0; their sums r_p are too. The double integral of differences is strictly positive. All second moments are finite for σ=2α>1; the quadratic variance identity and the factor p^(−σ)/(1−p^(−σ))² are correct. A PSD identity is not continued below σ=1.
- **Lemma 4:** the new bound 3/2 improves the 5 of this audit and is correct: −B≤c²/[de(c−1)]−c/de+1=1+c/[de(c−1)]≤3/2. It does not require the lower bound c/de−1 to be positive. The minimum with 2c/(de) remains valid.
- **Theorem 5 and formula by powers:** cuts J,K and tails are those of §4. Tonelli produces the positive sum of A. For J, the entrywise identity J=A+Z(de)^(−2α), the finite positive sum of A and the two geometric series guarantee absolute convergence. The explicit term is exactly Z_α/[(p^(2α)−1)(q^(2α)−1)] with minus sign in A. At α=1/4 the denominators √p−1 and √q−1 appear; convergence over all primes is not inferred from this.

**Precision on deletion.** Removing indices from the fixed kernel preserves its already proved signs. Changing the Gaussian law by removing multiples of a prime is another operation: the anticorrelation sign of that modified law is not proved here. The memo and the synthesis must keep that difference; do not present inheritance as a theorem for the altered measure.

**SYNTHESIS, second round: approved.** It communicates an auxiliary result signed at all scales and in Mellin α=1/4 without coprime subtraction. It keeps diagonal, same prime, polar, effective domain and Q_T link as pending. Entrywise positivity of A is not PSD nor does it by itself pay any mode of the node. With these limits, everything labelled PROVED is supported by the reviewed proofs.
