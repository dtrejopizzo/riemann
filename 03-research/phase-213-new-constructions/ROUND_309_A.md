# A positive average of the full balance keeps the square-root ceiling after sieving the divisors

Let B_t(v)=Σ_(m≤v)b_t(m) be the full sum of 292. For any finite set P of primes, even chosen depending on x, put

    T_P(x,t)=Σ_(n≤x; p∤n for all p∈P) τ(n) B_t(x/n),

where τ counts divisors. For every σ∈(1/2,1) one has unconditionally

    |T_P(x,t)| ≤ C_σ x^σ ∏_(p∈P)(1+p^(−σ))²,

uniformly in 0≤t≤2, x≥2 and P. In particular, even after removing all divisors containing some prime ≤Y, with Y=(log x)^(2+o(1)), the integrated balance with these discrete weights satisfies O_ε(x^(1/2+ε)). The individual contribution B_t(x) is kept with coefficient one.

**First, the unsieved average.** Its coefficient series is D_t(s)ζ(s)²=G_t(s)² L(s−it,χ)L(s+it,χ) by 292. The coefficients of each L have partial sums O(log(2v)), uniform in the band, by partial summation of the nonprincipal character. Dirichlet's hyperbola method splits the product into two short sums of length √v and the intersection rectangle. Hence the partial sum of the coefficients of the product of the two L-functions is O(√v log(2v)+log²(2v)). Convolving with the coefficients of G_t² costs their absolute norm with weight n^(−σ), uniformly finite by 294. It follows that |T_∅(v,t)|≤C_σ v^σ for v≥1.

**Then, the admitted divisors.** The series of their weights is ζ(s)²∏_(p∈P)(1−p^(−s))². The finite polynomial multiplying the previous average has weighted absolute norm exactly ∏_(p∈P)(1+p^(−σ))², which gives the claimed ceiling by convolution. It is even possible to reduce the weight of each prime partially: replace the finite factor by (1−a_p p^(−s))², with 0≤a_p≤1. The final weights remain positive or zero since each local factor is obtained by squaring 1+(1−a_p)Σ_(e≥1)p^(−es). The same ceiling is obtained with a_p p^(−σ) in the product of norms. The constants do not depend on how many primes or which reduction levels were chosen.

**Scale of the sieve.** For P contained in [2,Y], the logarithm of the cost is O_σ(Y^(1−σ)/log(2Y)) by Chebyshev and partial summation. Given small ε>0 take σ=1/2+ε/2. If Y=(log x)^(2+o(1)), the logarithm of the cost is o(log x), so the ceiling is O_ε(x^(1/2+ε)). More generally, for Y=(log x)^A, A>0 fixed, one obtains O_(A,ε)(x^(max(1/2,1−1/A)+ε)). For A>2 the absolute norm itself with all primes removed has logarithm comparable to Y^(1−σ)/log Y, by the PNT, so this estimate by moduli does not reach the square root for σ sufficiently close to 1/2. This limits the argument used, not the actual cancellation of the polynomial.

**Difference from the goal.** T_P is a signed sum with nonnegative weights, not a sum of positive parts. For P=[2,Y]∩primes the identity leaves B_t(x) plus the dilations B_t(x/n) with all primes of n greater than Y. The proved ceiling already pays for the whole sum at square-root scale; a floor for those dilations is missing if one wants to extract the one-sided ceiling for B_t(x). The formal cancellation by ζ² appeared in 292 and 294. The statement here is a uniform estimate for the family of arithmetic averages after removing divisors.
