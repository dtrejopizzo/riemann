# Separating the cost of the gaps and an identity with weights only on primes

Use I=(X,Y], Y=X exp h, L=Y−X and the normalisation X⁻² of 231. One obtains an unconditional ceiling for the cubic part of the gaps and a second local evaluation, in which each prime is compared with its position predicted by the accumulated rank. This last evaluation gives the same subsequence criterion without computing a least-squares fit.

**Gaps.** Split the interval into the stretches without primes, including the fragments at the edges. Let l be their length, z their midpoint measured from X and S the local prime mass accumulated in their interior. Let D_mid be the minimum over A,C of X⁻²Σ l(S−A−Cz)². By 231 the exact objective function adds C²Σ l³/(12X²). The theorem of Peck and Maynard gives Σ_(p_n≤eX)(p_(n+1)−p_n)²≪_ε X^(5/4+ε). The fragments are contained in the gaps of that sum (the gap containing both endpoints is counted once). Therefore Σ l³≤(Σ l²)^(3/2)≪_ε X^(15/8+ε). The variance identity of the midpoints is Σ l(z−L/2)²=(L³−Σ l³)/12≥L³/24 for large X, since L=X^(1−o(1)). In the regression line of midpoints the slope is covariance divided by variance. Its numerator in unnormalised sums costs O(M L²), M=Σ_(X<p≤Y)log p, and M/L=O(log X) by counting integers. Evaluating the exact functional at this minimiser gives

    0 ≤ D(X,h)−D_mid(X,h) ≪_ε X^(−1/8+ε).

This controls entirely the variation term inside gaps, even when the slope is refitted. The accumulated error of the positions of the midpoints remains. [Second-moment theorem for gaps](https://arxiv.org/abs/1201.1787).

**Rank identity on the primes.** For an alternative that does not even use l as a weight, order p_i in I, w_i=log p_i and T_i=Σ_(j<i) w_j+w_i/2. Fix the line between the two endpoints of the local count, of slope c=M/L. Then, for M>0, with R(x)=Σ_(X<p≤x)log p−c(x−X),

    X⁻² ∫_X^Y R(x)² dx =
       1/(cX²) Σ_i w_i [T_i−c(p_i−X)]² + 1/(12cX²) Σ_i w_i³.

Indeed R starts and ends at zero. Between jumps d(R³)/dx=−3cR²; at each jump the difference of the two cubes is 3w_i[T_i−c(p_i−X)]²+w_i³/4. Summing gives the identity, even if Y is prime. The last summand is ≤L log²(Y)/(12X²) unconditionally. At the scale admitted by 231, M∼L by the quantitative PNT already used in 213, since h≥(log X)^(−o(1)) and the error O(X exp(−c'√log X)) is o(L).

**An obligation with neither fit nor exterior data.** It would suffice that the first normalised sum on the right-hand side be X^o(1) along a subsequence. The error of this line dominates the minimum of 231, and its second term always tends to zero. Conversely under RH the ordinary error θ(x)−x is O(√X log² X) on I by von Koch; on subtracting its linear interpolation between the edges the supremum costs at most twice as much. Hence the normalised integral costs O((L/X)log⁴ X) and the condition is also necessary. Equivalently, one can use the weighted mean of the square of the distance of each prime to the point X+T_i/c, with the factor c w_i/X² in the sum. The two discardable terms are proved; neither the gap theorem nor the cube identity bounds that accumulated deviation of the ranks.
