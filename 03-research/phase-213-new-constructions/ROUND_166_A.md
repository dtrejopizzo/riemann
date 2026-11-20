# A criterion on a family of blocks of zero density in the logarithmic variable

Let S be the sum over simple primes of 162. Define
    F(z)=(2π)^(−1/2) ∫_ℝ exp(−(z−v)²/2) S(exp v) dv.
For t_j=j log(j+1), the global sign is equivalent to the existence of C such that, eventually,
    ∫_{t_j}^{t_j+1} |F(u)|² du ≤ C exp(t_j).
Only one inequality per block of length one is imposed, leaving gaps of order log t_j. The union of the blocks has zero density in logarithmic time. The statement refers to the fixed Gaussian average of the prime sum; each evaluation integrates values at neighbouring scales.

**Why it serves for the sign.** S(exp v) is zero for sufficiently negative v and O(exp v) on the whole line by Chebyshev, the support at one end and the boundedness of K. Hence F is entire and |F(a+ib)|≤C exp(a+b²/2). Towards a→−∞ on the real axis it decays like a Gaussian by the end of the support. On Re s>1 its bilateral Laplace transform is exp(s²/2) B(s) Σ_p (log p)p^(−s) by Fubini. The Gaussian keeps the poles to the right of 1/2 detected by 162. Under RH, S(exp v)=O(exp(v/2)) by 160–161, so F satisfies the ceiling on all blocks. For the converse it will suffice to prove |F(t)|≤exp(t/2+o(t)) for all t→∞. Then the transform is holomorphic on Re s>1/2 and the same contradiction via the extreme zero of 162 applies.

**Interpolation covering the gaps.** Take T=t_j≤t<t_{j+1}, so that t−T=O(log T). By the quadratic ceiling, on a set of length ≥1/2 in [T,T+1] one has |F|≤C' exp(T/2). Choose there n=ceil(4T/log T) points with separation ≥1/(8n) by greedy selection: each choice removes length at most 1/(4n). For the ordered nodes a_i, the product of distances of the i-th to the rest is bounded below by (8n)^(1−n)(i−1)!(n−i)!. Evaluating the Lagrange interpolant at t, the sum of the moduli of its coefficients is therefore ≤(C log T)^n, using the binomial sum of the inverse factorials. This costs exp(o(T)).

For the error, use the Cauchy integral of the interpolation remainder over |z−T|=√T. There |F(z)|≤C exp(3T/2+√T), while the quotient ∏|t−a_i|/|z−a_i| is bounded by (C log T/(√T−1))^n. The length of the contour divided by the distance to t is O(1). The remainder is ≤exp(−T/2+o(T)). This gives the desired bound on all the gaps. The proof does not presuppose separation or multiplicity bounds for the zeros.

**Cross-check and boundary.** The index discards thickness arguments for coercivity in P211-11A and D.132. Here the blocks do not even have positive density; what is recovered is only a growth exponent, and losing exp(o(t)) is allowed. The Gaussian provides explicit complex growth and the interpolation is performed on the prime sum, not on the test data of the paper. 145–149 already used Gaussians for the Liouville sum. The specific contribution is the sufficiency of these sparse blocks for the fixed average of the prime sum of 162. The bound on the selected blocks remains open. This does not authorize replacing F by S without proving another estimate.
