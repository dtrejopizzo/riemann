# AUDIT_003 — Independent review of ANTICORRELATION_003

2026-10-18. Independent check. Pure mathematics; additional check of four rational inequalities with exact Fraction, without numerical evaluation of theta.

**Verdict: PROVED, auxiliary strict-sign theorem. Not a closure of O1 nor a Q_T link.**

## 1. Global concavity of theta minus one

The formula D²logτ=(πy)²V−πyM is correct and the termwise derivatives are locally valid on y>0 by convergence of all derived series.

For y≥1/2, V≤E((n²−1)²), and the denominator of the distribution divided by the weight n=1 is ≥1. Each y exp(−πy(n²−1)) decreases on that interval. The inequalities n²−1≥3(n−1) and n⁴≤16^(n−1), n≥2, produce the announced geometric series. q<1/4 implies 16q³<1/4 and sum <1/3; the result πyV<π/6<1≤M is correct and strict.

For y≤1/2, Poisson gives A=1−√y+ε and τ=y^(−1/2)A with A>0. I checked by expanding AA''−(A')² the numerator of D²logA: the six terms and all their signs are correct. ε₂=2Σ[(πn²/y)²−πn²/y]exp(−πn²/y)>0. The bound by 2π²y^(−2)Σn⁴exp(−πn²/y) is valid.

The functions y^(−j)exp(−πn²/y) are increasing on the indicated interval for j=0,1,5/2. The geometric ratios and the factor 8√2π² for ε₂/r are correct. Verified exactly via rational fractions:

- Σ_{k=0}^{20}(157/25)^k/k! >525.
- With q=1/525, 2q/(1−q³)<1/250.
- With π replaced by 22/7, 4πq/(1−4q³)<1/40.
- With √2 replaced by 99/70 and π by 22/7, 8√2π²q/(1−16q³)<11/50.

Thus the numerator is strictly less than −103r/25000. The proof covers both intervals including the junction point. **Theorem 1 approved.**

## 2. Anticorrelation and matrices

The double integral of the strictly negative second derivative proves the four-value inequality without approximations. For coprime d,e, lcm=de and one obtains strictly negative covariance for ALL y>0. This goes beyond an asymptotic sign and is not the generic PSD of a covariance.

For pairwise coprime integers, positive definiteness of V_y is proved by evaluating a constant relation at N=1 and N=d_i, all events of positive probability. The construction B=sI−V_y with s≥λ_max gives nonnegative entries and spectrum in [0,s−λ_min]; the Neumann series converges and its first two terms prove strict positivity of every entry of the inverse. m=1 handled correctly.

**Necessary editorial precision in §5:** state explicitly that the entrywise positive inverse refers to a family of PAIRWISE coprime indices. Having some coprime pair is not enough; nor is a claim of strict definiteness valid if repeated indices are admitted. Within the family of §3, all conclusions of §5 are proved: positive integration preserves strict definiteness and cross sign; the inverse argument applies again.

## 3. Prime valuations

The indicator series of p^j sum to v_p and are dominated in L² by log|N|/log p. The double sum of covariances converges absolutely: the sum of joint probabilities is E(v_pv_q)<∞ and the sum of products of means is E(v_p)E(v_q)<∞. Each summand for p≠q is strictly negative. The result is therefore strictly negative.

When summing over primes with weights log p, the bound by E(log²|N|)+(Elog|N|)² justifies the absolute interchange. The diagonal sum is finite by Σ_p(log p)²v_p²≤log²|N|. The variance identity, its exact difference and the strict inequality (4) are proved. The pair (2,3) ensures strictness.

## 4. Scope and novelty

The theorem provides an auxiliary arithmetic sign, built on a discrete Gaussian law whose Poisson formula effectively enters the proof. The sign was not obtained by writing a norm or by assuming the sign of Q_T. The note does not claim bibliographic priority; absence of a hit in the index is not proof of global novelty.

The result may still be inherited under arithmetic changes; it does not by itself satisfy the Euler specificity required of the complete object. Nor does it identify Mellin height, node weight, polar domain or domination of the gamma deficit. The final caveats are correct and must remain. Do not attribute to the matrix structure of this covariance a structure of the Weil matrix without proving the map.

**Final result:** strict auxiliary positive verified; the link with the node remains OPEN. A mathematical milestone distinct from and smaller than building the requested O1 kernel was achieved, and must be communicated with that distinction.
