# Sign of the block with a prime above the square root and cancellation with the complement

For the self-convolution b_t of 292 define B_t(s)=Σ b_t(n)n^(−s) in Re s>1 and by continuation near 1. For fixed 1/2≤α<1, uniformly in 1≤t≤2, one obtains unconditionally

    Σ_(n≤x; P⁺(n)>x^α) b_t(n) = −2 B_t''(1) x/log³x + O_α(x/log⁴x),
    Σ_(n≤x; P⁺(n)≤x^α) b_t(n) = +2 B_t''(1) x/log³x + O_α(x/log⁴x),

with P⁺(1)=1 and min_t B_t''(1)>0. The main term does not depend on the cutoff α within this fixed range. The obstacle to the square-root ceiling is the difference between two large signed contributions, even after grouping each of them.

**Signed moments.** From 292,

    B_t(s)=G_t(s)² L(s−it,χ)L(s+it,χ)/ζ(s)².

The coefficients of G_t² converge absolutely with weight n^(−σ) for each σ>1/2 uniformly in t: the local factors of the squared correction are (1+(cos θ_p−1)z)²(1−χ(p)p^(it)z)(1−χ(p)p^(−it)z)/(1−z)², with z=p^(−s), except for the finite factor at 3, which is adjusted by the extension. The linear term cancels for p≠3 and the absolute local tail costs O_σ(p^(−2σ)). The series of B_t is therefore a convolution of that correction, two copies of μ and the sequences χ(n)n^(±it). For all R>0,

    Σ_(n≤z)b_t(n) ≪_R z/log^R(2z).

Indeed, μ satisfies the ceiling for every R by the quantitative PNT, and the two twisted periodic sequences have partial sums O(log(2z)) by parts. The hyperbola method with cutoff √z preserves the arbitrary logarithmic savings for their finite convolutions: each short sum of moduli with weight 1/n costs a fixed power of log z by divisor bounds. For the final correction split its convolution into d≤√z and d>√z; the absolute harmonic tail gains a power by convergence at σ=3/4 and the divisor bound for the other factor suffices. All these bounds are uniform in t.

By partial summation the moments Σ b_t(m)(log m)^j/m converge to (−1)^j B_t^(j)(1) with tail O_(j,R)(log(2M)^(−R)) beyond M. The first two moments are zero, and B_t''(1)=2G_t(1)² |L(1+it,χ)|²>0. The local factors at 1 are real positive for the squared correction; only that of p=2 could vanish, if u_2=2, which is excluded by 1≤t≤2. The tail converges uniformly and L has no zeros on Re s=1. By compactness the floor is uniform.

**Summing the large prime.** There is a unique prime p>x^α in the integers of the first block, always with exponent one. Write n=mp, m≤x^(1−α); then b_t(n)=−2b_t(m)u_p. On primes, the PNT with classical remainder, in the two classes modulo 3 and by parts against p^(it), gives Σ_(p≤z)u_p=li(z)+O_R(z/log^R(2z)) uniformly. On substituting this sum at the two endpoints of (x^α,x/m], the errors cost O_R(x/log^R x), reducing the exponent beforehand if necessary, since Σ_(m≤x)|b_t(m)|/m≪log^C(2x) by the local factors. The lower endpoint includes li(x^α)Σ_(m≤x^(1−α)) b_t(m), negligible to any logarithmic order for fixed α. What remains is −2Σ_m b_t(m)li(x/m).

**Computation of the first term.** Put L=log x, M=exp(√L). For M<m≤x^(1−α) the partial-sum bound and the derivative of li(x/m), of modulus x/(m² log(x/m)), give a cost O_R(x/L^R), choosing the initial saving high enough. For m≤M use the expansion of li:
    
    li(x/m)=(x/m) Σ_(k=1)^8 (k−1)!/(L−log m)^k + O(x/(m L⁹)).

The absolute harmonic sum of |b_t| up to M is O((log(2M))^4), by the local factor (1+2/p)². In each denominator expand in log(m)/L up to degree 16. The summed error is O(x/L⁴), since |log(m)/L|≤L^(−1/2). Replacing by the full moments costs O_R(x/L^R). Only the pair k=1, degree 2 contributes at order L^(−3); degrees 0 and 1 vanish exactly and the subsequent fixed moments are bounded. The resulting coefficient is B_t''(1). This proves the first asymptotic, and the bound for the full partial sum gives the second formula.

**Limit for the route.** Deleting the large-prime block because it is negative leaves a positive complement of order x/log³x. Integrating in frequency does not remove that term either, since the coefficient has a positive floor on all of [1,2]. At logarithmic precision one identifies explicitly what compensates; the bound at square-root precision for the balance remains open. Unlike 293, the mass of each parity is not estimated separately here: the arithmetic balance within each block is evaluated.
