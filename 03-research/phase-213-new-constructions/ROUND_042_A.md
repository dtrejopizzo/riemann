# An explicit minorant with a single sieve corrector

In the problem of 041 the optimal value can be attained asymptotically, with additive error o(1), without choosing coefficients by chains of powers of large primes. The variable data used are only divisibility by small primes, a finite Euler product and the weight w(t)=min(t,t⁻²).

For x sufficiently large take Y=x^(3/4)/(log x)^(1/8). Call free the integers with no prime divisor ≤Y; 1 is included in this class. Write

    Z=Σ_{m free}m⁻²=ζ(2)∏_{p≤Y}(1−p⁻²),       c=1−1/Z.

Define b₁=0, and for free n>1 take b_n=w(n/x)−c(x/n)². For the other integers take b_n=0. These coefficients are nonnegative for large x. Indeed, 0≤c≤Σ_{p>Y}p⁻²=O(1/(Y log Y)) by the Euler product and Chebyshev. On the branch n≥x the remaining factor is 1/Z>0. On the branch n<x it suffices that n³≥cx³, which already holds at n=Y for large x because x³/(Y⁴ log Y)→0.

**Exact row identity.** For every integer d>1 that is not free, D_d=Σ_{m≥1}b_{dm}=0. If d>1 is free, the only admissible terms are those with m free. For m>1 one has dm>Y²>x, so all strict multiples use the same quadratic branch. Consequently

    D_d=w(d/x)+(x/d)²[(Z−1)−cZ]=w(d/x).

This verifies even the composite rows outside the support of Λ. In particular the minorant only loses the rows of prime powers with base p≤Y. The argument only uses the Euler product at 2, where it is absolutely convergent.

**Precision with infinite support.** By the divisor identity and Tonelli, the value V=x^(−1/2)Σ b_n log n is the full weight of the rows p^k with p>Y. The discarded weight of the primes p≤Y is O(Y²/x^(3/2))=O((log x)^(−1/4)). The weight of all squares tends to 2/3 by 039, and the squares with p>Y have weight O(x^(3/2)/Y³)=o(1) by partial summation. The total for exponents ≥3 is o(1). In sum, Q(x)−V(x)=2/3+o(1), the same asymptotic loss as at the optimum of 041.

**Precision with finite support.** Truncate b_n to n≤N∼λ x^(3/2), with λ>0 fixed. By positivity all constraints are kept. The removed value is exactly

    x^(3/2) Z⁻¹ Σ_{n>N, n free} log(n)/n².

The primes of the tail contribute 1/λ+o(1) by the prime number theorem and Z→1. To bound the free composites, write B=Σ_{p>Y}p⁻² and A=Σ_{p>Y}log(p)/p². Majorizing each product of k prime factors by the count that uses all its orderings gives, when summing log n over its k factors, a total ≤Σ_{k≥2}k A B^(k−1)=O(AB). One has A=O(1/Y), B=O(1/(Y log Y)). Even before imposing n>N, the normalized contribution of these composites is O(x^(3/2)/(Y² log Y))=o(1). Thus the truncated explicit weights leave loss 2/3+1/λ+o(1), and their value differs by o(1) from the exact maximum of 041. Computing b_n does not require classifying any integer greater than Y as prime or composite.

**Scope.** The explicit dependence on the capacities of the large primes has been removed from the *choice* of the minorant. Its value is a sum over integers passing the sieve, and where Y<n≤x those integers are precisely primes. Proving a lower bound (3/2)√x−O(1) for the sum remains the sign obligation. The row identity and the o(1) error do not by themselves give such an estimate.

Cross-check and review: R166_601_ROUGH_ZETA_JOIN §§1–3 already records the Euler product of sieved integers and their count by inclusion–exclusion. The contribution of this round is the positive corrector at this scale and the comparison of its value with the optimum. The identity, the eventual nonnegativity and both asymptotic losses received independent audit.

## Can the value be estimated by an average of translations of the sieve?

Fix N∼λx^(3/2) and Y as above. Put P=∏_{p≤Y}p, ρ=φ(P)/P, and f(n)=log(n)[w(n/x)−c(x/n)²] for Y<n≤N, zero outside. For a residue h uniform modulo P consider

    V_h=x^(−1/2) Σ_n f(n) 1_{(n+h,P)=1}.

V₀ is precisely the value of the truncated minorant of this round. The other translations serve only as comparison; they are not presumed to be admissible minorants. One has

    V₀=(3/2+o(1))√x,     mean_h V_h=(2 exp(−γ_E)+o(1))√x,
    var_h V_h=O(log x).

Hence, for each fixed C, the proportion of residues with V_h≥(3/2)√x−C is O((log x)/x). The same conclusion holds with threshold V₀−C. The estimate for phase zero uses here only the main term, not the O(1) error being sought.

**Mean.** The exact mean is ρx^(−1/2)Σ f(n). The unsieved mass is (3/2+o(1))x log x, by Riemann sums of w, whose integral is 3/2. For passing to the infinite interval, the sum over n>Mx is O(x(log x+log M+1)/M) for M≥1, by integral comparison; the piece n≤Y=o(x) contributes O(Y²log x/x). The corrector costs O(cx²(log Y+1)/Y)=o(x log x). Mertens gives ρ log x→(4/3)exp(−γ_E). For V₀, the prime number theorem in Q and the bounded loss of 042 give the indicated main term. The difference between both coefficients is strictly positive.

**Variance.** The ℓ¹ norm of f is O(x log x) and its total variation, including both endpoints, is O(log x). On the lower branch n log(n)/x grows up to log x and the term c x² log(n)/n² decreases from O(log x), by the choice of Y. On the upper branch (1−c)x² log(n)/n² decreases. By summation by parts the discrete transform of f at a frequency t has modulus O(log x) min(x,1/dist(t,ℤ)). For a reduced frequency r/d with d|P, the modulus of the normalized Fourier coefficient of the coprimality indicator is ρ/φ(d): by the Chinese remainder theorem each prime dividing the conductor changes its local factor by the ratio 1/(p−1). Parseval omitting the zero frequency gives

    var_h V_h ≪ (ρ² log²x/x) Σ_{d|P,d>1} φ(d)^(−2)
                     Σ_{r=1}^{d−1} min(x,d/min(r,d−r))².

The inner sum is O(dx): if d≤x it suffices to sum the inverse squares, and if d>x split at r=d/x using the symmetry. The resulting product ∏_{p≤Y}(1+p/(p−1)²) is O(ρ⁻¹), by factor-by-factor comparison with (1−1/p)⁻¹ and convergence of Σp⁻². This gives the variance bound. The estimate of the proportion follows from Chebyshev and the separation of order √x.

**Decision.** R166_601 already distinguishes between periodic density and the count of free integers when log x/log Y stays bounded. This computation quantifies the failure for the weighted target of 042, even when allowing translations: the average loses in the main term and the values of the size sought are exceptional relative to that mean. For phase zero the inequality with additive error O(1) remains open. The variance is a bound for the ensemble of translations, not for the error of phase zero.

**How many moduli can be averaged at sign precision.** There is a partial version that does preserve the value up to O(1). Choose any subset B of the primes in (Y/2,Y]. Keep h≡0 in all sieve moduli outside B and average h freely in those of B. By the Chinese theorem, the conditional mean is

    ρ_B [V₀+o(1)],        ρ_B=∏_{p∈B}(1−1/p),

with error uniform in the choice of B. Indeed the factor ρ_B comes out exactly when averaging the local indicators. When removing the constraints of B from the original count, the new integers of the support Y<n≤N are composite (they contain a prime of B less than n) and all their factors are greater than Y/2. Hence n>(Y/2)²>x for large x. Their additional contribution is nonnegative and at most O(x^(3/2)/(Y² log Y))=o(1), using the same count by ordered products of the first part with cut Y/2. This proves the uniformity.

Consequently the difference between V₀ and the conditional mean is (1−ρ_B)V₀+o(1). Since V₀∼(3/2)√x and the primes of B are comparable to Y, preserving the value at distance O(1) is exactly equivalent to |B|=O(Y/√x). To see both directions, use 1−exp(−Σ_{p∈B}1/p)≤1−ρ_B≤Σ_{p∈B}1/p. With |B|=o(Y/√x) the error tends to zero. By contrast, averaging the whole band costs asymptotically (3/2)√x log(2)/log Y, since Σ_{Y/2<p≤Y}1/p∼log(2)/log Y by the prime number theorem. It is a precise tolerance for this operation; it does not provide the lower bound of the value being averaged.
