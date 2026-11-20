# The average over modular directions satisfies the ceiling; parity obstructs transferring it to the original direction

Take q an odd prime and the primes q<p≤2q with weights w_p=log p, M=Σw_p. In the direction a∈{1,…,q−1} place the weight w_p at the coordinate y_p={a(p−q)/q} of the circle of length one. Set R_a(y)=Σ_(y_p≤y)w_p−My and

    V_a=(1/q)∫₀¹ |R_a(y)−∫₀¹ R_a|²dy.

At a=1 this is the endpoint-slope line of the interval [q,2q] with optimised intercept, in the normalisation of 231. Under RH it is O(log⁴ q) by von Koch. If RH fails, 231 gives liminf log(1+V₁)/log q≥2B since also fitting the slope only decreases the error. Therefore a subsequence of primes q with V₁=q^o(1) would suffice.

**Exact Fourier and the part already controlled.** Write S(m)=Σ w_p exp(2πim(p−q)/q). The periodic derivative of R_a is the comb of masses minus Mdy; its nonzero modes have coefficients of modulus |S(am)|. Parseval after removing the mean and grouping the integers congruent modulo q gives

    V_a=M²/(12q³)+(1/(4q³)) Σ_(m=1)^(q−1) |S(am)|² / sin²(πm/q).

One used Σ_(k≡m mod q)1/k²=(π/q)²csc²(πm/q), obtainable from the partial-fraction expansion of the cotangent. By discrete orthogonality Σ_(m=0)^(q−1)|S(am)|²=qΣ w_p² for any a≠0; the residues are distinct. The terms with min(m,q−m)≥√q contribute O(log q) UNIFORMLY IN a, since csc²(πm/q)≪q there and Σw_p²≪q log q by Chebyshev. The term of multiples of q is O(1/q). Consequently, in the true direction only the ceiling q^o(1) is needed for the block of frequencies 1≤m≤√q, with each |S(m)|² divided by qm² (absolute constants by symmetry and the sine).

**What cancellation is obtained for the primes without RH.** Average a over all nonzero residues. For each m≠0, am runs through exactly the same residues. Using Σ csc²(πm/q)=(q²−1)/3, one obtains

    mean_a V_a=M²/(12q³)+(q+1)(qΣw_p²−M²)/(12q³) ∼ (log q)/12.

Here M∼q and Σw_p²∼q log q by PNT. The trigonometric identity is obtained by taking the constant term in the differentiated cotangent summation formula near the origin. By Markov, for example, the fraction with V_a>exp(√log q) tends to zero. Weights are not permuted independently: the group of q−1 multipliers of the same set of primes suffices.

**An arithmetic obstacle to using the average.** If b is an even integer with 2≤b<q and a=b⁻¹ modulo q, the mode m=b/2 satisfies am≡2⁻¹ mod q. Since p and q are odd, p−q is even and the coefficient S(2⁻¹) is exactly Σw_p exp(πi(p−q)/q). The measure q⁻¹Σw_p δ_((p−q)/q) converges to Lebesgue on [0,1] by PNT, so |S(2⁻¹)|/q→|∫₀¹exp(πiy)dy|=2/π. By the exact formula,

    V_(b⁻¹) ≳ q/b²

with a constant uniform over all such b. For b=2 it is already of order at least q, although the average is logarithmic. Moreover, for any inverse b of a with 1≤b<q one has V₁≤b²V_a: in the term of |S(n)|² one uses |sin(πbn/q)|≤b|sin(πn/q)| and the constant contribution is the same. Thus a good multiplier with inverse b=q^o(1) would suffice, but for ALL even inverses of that size the parity bound blocks this transfer. The global average does not guarantee a good small odd inverse. The bound for the true direction is not proved.

**Antecedent.** 220 averaged excursions by varying the order of the detector, and 232 isolated a rank error. The present average is finite and exact at each q, and its obstruction comes from a frequency identified by parity in the authentic primes.
