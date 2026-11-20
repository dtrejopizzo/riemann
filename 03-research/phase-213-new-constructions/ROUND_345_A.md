# What balance the first rows surviving the inversion have

Let Y=√X, h=X^(−δ), fixed 0<δ<1/4. In A_h of 338–344 select rows with 3Y/5≤d≤7Y/10 and centers 17X/10≤x≤19X/10. In this band of **complete rows**, before the truncation of small products, their contribution to A_h is exactly

    Σ_n λ(n) a_Y(n) W_x(n),
    a_Y(n)=Σ_{d|n, 3Y/5≤d≤7Y/10} μ²(d)μ²(n/d),

where λ(n)=(−1)^Ω(n). In C_h take the corresponding band at each scale. Then, even grouping both scales by the same argument n of the pulse, the sum of moduli of the terms with odd n is ≍ hX, uniformly in these centers. This exceeds the pointwise budget √(hX) by a power. What is measured is the cost by moduli of this exact representation of the band, not its signed balance.

**Computation.** Only m with xe^(−h)/d<m≤x/d reach the first pulse, hence 2Y<m≤4Y for large X. In the divisor sum of m cut at D=2Y exactly the divisor m is missing; every proper divisor is ≤m/2. The inner coefficient is −μ(m). In the second pulse one has 1<m≤x/(2d)<2Y: the row is zero by complete inversion. The exterior sign of 338 cancels the previous minus sign. At fixed product n=dm one has μ(d)μ(m)=λ(n)μ²(d)μ²(m), without requiring d and m to be coprime. Hence at the first scale all nonzero representations of n have identical sign.

The second scale has support at arguments 4dm of the original pulse. More precisely, the joint coefficient is λ(n)a_Y(n)−2·1_{4|n}λ(n/4)a_(Y/2)(n/4), interpreting the second summand only when applicable. For odd n the coefficient of the first scale remains intact.

**Uniform size.** Since η≥0 has positive integral, there is a fixed interior interval where η≥c>0. For each odd squarefree d in the band, that interval selects m in an interval of length comparable to hY inside [2Y,4Y]. The count of odd squarefree integers up to z is c₁z+O(√z) for c₁>0, by the expansion of μ² in odd square divisors and counting odd multiples. Since hY/√Y=X^(1/4−δ)→∞, there are ≫hY choices, uniformly in d and x. There are ≫Y choices of d, giving the floor ≫hX. The ceiling O(hX) comes from counting all pairs without parity or square restrictions. Grouping by product preserves the mass in modulus at the odd arguments.

**Use and scope.** By Poisson in 338 one can restore the truncation of small products with error O_B(X^(−B)) in the signed value of the band; this does not claim proximity of its coefficients in total variation. In contrast with the zero-balance rows of 344, here the remaining observable is identified as a local Liouville sum weighted by an explicit count of balanced divisors. To lower its cost one must use cancellation between distinct n or with other bands. No floor for the full signed sum is deduced.
