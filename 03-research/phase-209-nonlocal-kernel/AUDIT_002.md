# AUDIT_002 — Punctured covariance and Mellin

2026-10-18. Independent review of CONSTRUCTOR_002 §§0–6. Row D independent.

**Verdict: lemmas 1–5 PROVED within their scope; Q_T link OPEN.** The memo itself correctly declares that it did not reach the README milestone.

## 1. Probability and divisor identity

The normalisation τ=θ−1 is positive and the divisibility probabilities are τ(d²y)/τ(y). X_d X_e=X_lcm. PSD and its extension by positive integration are generic and the memo does not present them as specificity. Poisson for τ and for the quotients is exact, keeping the origin term and the fractional scales.

The truncated sum of Λ(d)1_{d|N} is dominated by log|N| and converges to it pointwise; the quadratic moment is finite under the Gaussian. L² convergence justifies the variance identity as a joint limit, without improperly interchanging a signed double series.

## 2. Mellin

At zero, τ(y)=y^(−1/2)−1+exponential error after Poisson, so q_y(d)=1/d+O_d(√y). The expansion of C_y is G₀+O(√y) and G₀=(gcd−1)/(de). At infinity the ratios decrease exponentially because the smallest nonzero integer of the denominator has |N|=1. This proves entrywise absolute convergence of I_α for α>0 and PSD on finite sequences.

The separate transform of τ(l² y) for α>1/2 is 2π^(−α)Γ(α)ζ(2α)l^(−2α), with correct factor 2. The remainder with denominator τ converges separately there. Multiplication by τ recovers the Mellin homogeneity of one term at the cost of losing it in the quotient: one cannot conclude a critical-weight law merely by choosing α=1/4.

## 3. Renormalisation

B_y=y^(−1/2)G₀+O(1) near zero and decays exponentially at infinity. Subtracting y^(−1/2)G₀ on the whole half-line gives convergence for 0<Re α<1/2. Splitting at 1, the subtraction of the tail produces G₀/(α−1/2), correct sign, and −4G₀ at α=1/4. The split expression continues meromorphically from Re α>1/2 to Re α>0 with a possible pole at 1/2.

The identity R_α=I_α+H_α is exact. H_α converges: cancellation of the y^(−1/2) term at zero and integrable power at infinity. No positivity of H or R is derived from that of I. The memo explicitly keeps this unknown.

## 4. Origin and limit of the sign

The decomposition by the event N=0 is exact:

    C⁰=(1−p₀)C×+p₀(1−p₀)u_y u_y*, u_y(d)=1−r_d.

It is not legitimate to identify that scale-dependent direction with cosh(x/2) without a map of tests. For coprime d,e>1, the negative asymptotics of C× follows because ((de)²−1)−(d²+e²−2)>0. There is no contradiction with PSD: a PSD matrix may have negative cross entries.

The strict association of the full theta, reviewed separately in POSITIVE_ASSOCIATION_002, has an effective source in Poisson, but removing the origin already changes its cross sign even without deleting a prime. This prevents presenting deletion specificity as sufficient proof of a new sign for the polar orthogonal.

## 5. Gates

The family C_y is not a universal function of de, by the counterexample of limits (2,6) and (3,4). This does not prove an equivalent property for I_α at a fixed α, and the memo distinguishes this. Nor does it yet produce a height kernel or prove exit from the effective algebra in the domain of Q_T.

There is no translation to BR, def:PD certificate or pointwise identity of thm:sos. The positive covariance lemmas do not reopen Gram as a route to the node: the specific link is the pending work. The option a_d=Λ(d)d^(−1/2)F(log d) is quadratic in evaluations of F, but does not reproduce the autocorrelation dependence without additional proof. The degree-four warning when using autocorrelations as coefficients is correct.

Result: coherent explicit construction and a localised denormalisation remainder; no useful arithmetic positive proved for Q_T. A possible strict cross sign of the punctured covariance remains under examination; it would be a lemma distinct from its generic PSD and will require a separate audit.
