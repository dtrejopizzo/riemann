# Semiprime band with superlogarithmic width

Quantitative refinement of 063, with the same average. Fix 0<a<1, b=a/(1+a), 0<κ<b. With L=√x, h=(log L)^κ, R=L exp(h), P=L/√R, Q=L²/p³, take P≤p≤2P and all primes √R≤q≤Q L^(1/4). The signed contribution of these slopes to H is o(L). R parametrises the resonance, it does not bound the product pq. The upper endpoint in q also changes with respect to 063.

On the circle, C(exp(it)) admits near each small nonzero real t a complex disc of radius ε|t| on which its absolute value is ≤exp(−c|t|^(−a)): choose ε so that a times the absolute value of the argument of 1−exp(it') is strictly less than π/2 with uniform margin. Cauchy and optimisation in |t| bound its derivative of order n by A^(n+1)(n!)^(1+1/a), also on the rest of the circle by analyticity. Integration by parts n times and the choice n≈δ j^b give |c_j|≤A exp(−c j^b). In 063 the sum for J(z) starts at j≥log₂(1/z)−O(1); thus J and its first logarithmic derivative are O(z² exp(−c|log z|^b)) at zero and rapidly decreasing at infinity.

In the formula of 060 for r=pq, T=L/√(pq), separate J(T)−J(T/p). The remainder costs O((T/q)²+(T/p²)²) by |J(v)|≪v² and two geometric series. Even summing over integers, the total cost is O(L exp(−h)+exp(2h)log L), using Σ_{q≥√R}q^(−3)≪1/R and Σ_{p≥P}p^(−5)≪P^(−4). T≥p/L^(1/8) and the number of pairs is polynomial, hence J(T) contributes o(L).

For the term J(√(Q/q)), on each dyadic interval q≈U the sup norm plus variation of the weight is O(min(1,Q/U)). Partial summation and quantitative PNT allow replacing the prime sum by the integral with density 1/log q with error O(Q log L exp(−c√log L)) per p. It is essential to use the weight on each interval.

Write 1/log q=∫₀^(1/4) q^(−s)ds+q^(−1/4)/log q. The remainder contributes O(Q R^(−1/8)) by integrability of |J(z)|z^(−3). For the first term put z=√(Q/q); completing the integral in z gives 2Q∫₀^(1/4) Q^(−s) M_J(2−2s)ds in the convention of 063. The tail z<L^(−1/8) costs O(Q exp(−c(log L)^b)), by the bound at zero and z^(2s)≤1. The tail z>√(Q/√R) costs O_N(Q exp(−Nh/2)) for any fixed N by rapid decay. In the complete integral M_G is bounded on [3/2,2] and C(2^(−2s))≤exp(−c s^(−a)); minimising s log Q+c s^(−a) gives O(Q exp(−c'(log Q)^b)). Summing over p one has ΣQ≪L exp(h) and log Q≈log L. All bounds are o(L) taking N>2. The four ordered slopes per pair only multiply the cost by a constant.

The signed sum of complete rows in q is controlled. The estimate does not decide the complement nor does it enlarge T.
