# A complete cone in the scalar table and 10¹⁵ entire rows

In POWER_SCALAR_BRIDGE_017 fix u=63/2 and F(s)=s^k/(s+u)^(N+k), N≥1, k≥0 integers. For the complete form W it is proved:

1. W(f)>0 for ALL N if k≤10¹⁹N.
2. W(f)>0 for ALL k if N≤10¹⁵.

There is no limit on the total degree N+k in the first statement. The second conclusion completes rows of the sufficient table of 017; it does not claim positivity of every numerator of the same degree.

**Cost of the tail without a degree estimate.** Use the spectral identity of 201, valid for each F of finite degree. Write G=3·10¹². At the two points s=±δ+iγ of each term, |δ|≤1/2 and |s+u|²−|s|²=u²+2u Re s≥u(u−1)>0. Thus |F(s)|≤|γ|^(−N) independently of k. For N≥2 the absolute sum of the whole tail |γ|>G is <10¹⁷ G^(−2N). Indeed on the dyadic bands B<|γ|≤2B with B=2^jG, Z3 by subtraction of endpoints gives fewer than 2B log(2B) zeros counting both signs (the main derivative is ≤log(2B)/(2π) and both endpoint errors are ≤log(2B)). Paying B^(−2N) and summing, the factor after extracting G^(−2N) is ≤2G Σ_{j≥0}2^(−3j)log(2^(j+1)G)<10¹⁷.

**One verified square pays all that cost.** By Z3 there is at least one ordinate t₀∈[G/2,0.51G]: the main increment is ≥0.01G·log(G/(4π))/(2π), and the loss in the two errors is ≤2 log G. By Z2 its contribution is |F(it₀)|², and all others up to G are nonnegative. Exactly

    |F(it₀)|²=t₀^(−2N)(1+u²/t₀²)^(−N−k)
            ≥G^(−2N) exp[2N log(1/0.51)−4u²(N+k)/G²].

If k≤10¹⁹N, the exponent is >1.3N, by the declared values of u and G. For N≥100 one has exp(1.3N)>10¹⁷. The resulting inequality is strict for the complete form. No specific zero beyond Z2 is located, nor is the individual sign of the tail assumed.

**Splicing.** For 2≤N<100 and k<10000N², the denominator degree N+k is <10⁸; by 204 the complete block is positive. For k≥10000N² and N≥2, POWER_QUADRATIC_EXPLICIT_017 directly proves the sign of the atom (summarized in POWER_STATE_018). N=1 is already covered for all k by POWER. This completes the first statement. When N≤10¹⁵ one has 10000N²≤10¹⁹N, and the two cones cover all integers k. The improvement does not come from extrapolating consecutive rows.

**Remaining region.** To close the bridge by these two cones it would suffice to prove the sign for N>10¹⁵ and 10¹⁹N<k<10000N². Other results of the corpus already cover part of that region, for example POWER_SUBQUADRATIC_COROLLARY_048 in its asymptotic range. The constants of the new cone are deliberately conservative. The absolute tail bound alone stops being informative when the damping of (1+u²/t₀²)^(−k) beats the advantage (G/t₀)^(2N). No uniform relative floor as the indices grow is deduced.
