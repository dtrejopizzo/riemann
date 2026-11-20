# The two signs of the band balance with a quantified relative error

For the concrete combination of 275–276 let A(x)=Σ_(Y<q≤U)Λ(q)|R(q)| and E(x) the same sum with R(q). Unconditionally, with Ω(U)=(log U/log log U)^(1/3), there exists c>0 such that for all sufficiently large x

    |E(x)| ≪ exp(−c Ω(U)) A(x).

The result also holds when both sums are restricted to primes. In particular the positive and negative masses (both taken in magnitude) are each (1/2+o(1))A(x), although the absolute mass exceeds the floor of 276. The bound concerns a relative error.

**The signed integral already meets the budget.** With I=∫S, the value at s=1 of the transform of T(y)−(I/y)1_(0,U)(y) is ∫S(t)log t dt+(γ_E−log U)I, by the constant term of ζ(s)∫S(t)t^(s−1)dt−I U^(s−1)/(s−1). As in 276, the part y<Y of the regularized integral and all terms with I between Y and U are O(N^(−2)), and above U one integrates the target weight with result xh. Moreover, the moment adjustment of 273 gives xh=Σ S(j)∫_(j−1)^j(1+log t)dt. Replacing S(j) by S(t) costs O(log(2N) Var(S))=O(U log³(2N)): the variation is applied on each interval, and the support of S begins at U/4. The integral also includes the last cell with endpoint ⌈2x⌉, with zero sample if it exceeds N. Consequently

    |∫_Y^U T(y)dy| ≪ U log³(2N).

**From the integral to the arithmetic mass with relative error.** Use the cells of 276, of length h between U^(7/10) and 2U^(7/10). Let ν be the measure ΣΛ(q)δ_q or only its prime part. On each prefix (a,a+v] of each cell, the discrepancy |ν((a,a+v])−v| is O(h exp(−cΩ(U))) uniformly. For primes one applies 238 above a^(5/8), and below O((U^(5/8)+1)log U) serves. For the proper powers, for each exponent j≥2 two consecutive j-th powers in the band are separated by ≫√Y, by the mean value theorem. There are O(log U) exponents and the weights are ≤log U, so it suffices to add O((1+h/√Y)log²U).

On each cell take the Taylor polynomial P of T of order two at the left endpoint. For F=P and for F=|P|, by parts the error in passing from dy to ν is bounded by the prefix discrepancy times |F(a+h)|+Var(F). The latter quantity is ≪h^(−1)∫|P|: rescale to the unit interval and use equivalence of norms on the space of polynomials of degree ≤2, and Var(|P|)≤Var(P). This gives a cost O(exp(−cΩ(U))∫|P|) per cell. Replacing P by T, both in the integral and in the arithmetic sum, costs in total O(U^(11/10)log¹¹(2N)), by the third-derivative bound of 276 and ν(cell)≪h. Also ||T|−|P||≤|T−P|.

By 276, L₁=∫_Y^U |T| ≫ U^(3/2)/log(2N). The Taylor cost and the size of the signed integral are O(exp(−cΩ(U)) L₁), decreasing c if necessary. Thus the absolute arithmetic mass is L₁(1+O(exp(−cΩ(U)))) and the signed one has modulus O(exp(−cΩ(U)) L₁). On the band R(q)=T(q), which concludes the proof.

**Missing scale.** The equivalence of 275 requires E(x)≥−C_ε x^(1/2+ε) for each ε>0. The relative saving proved here is subpolynomial, while A(x)≥c N^(3/4)/log(2N). To obtain the conclusion from a two-sided relative bound one would need at least a power saving at that scale. A one-sided absolute bound can still exploit additional information about which of the two masses dominates.
