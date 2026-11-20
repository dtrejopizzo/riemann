# Compensation between bands in two families of odd products

Keep the band, the centers and 0<δ<1/4 of 345, before the truncation. Among the contributions in modulus of the band at odd products, the fraction corresponding to products with some prime square divisor tends, uniformly in the center, to

    1 − ∏_{p>2} (1−1/(p+1)²) > 0.

The other rows cancel **exactly** the whole coefficient of the band at each of those products. Moreover, on odd squarefree products, other rows cancel surplus multiplicities of total mass ≫hX. They are two disjoint compensations of order hX; both are internal to the same product n once the bands are gathered.

**Identity.** In the full observable C_h, an odd n only comes from the pulse S_h(x), so its coefficient is μ(n). According to 345, the band contributes λ(n)a_Y(n). If n is not squarefree, the complement has coefficient −λ(n)a_Y(n). If n is squarefree and a_Y(n)≥1, it has coefficient −λ(n)(a_Y(n)−1). These identities on the complement precede the truncation by Poisson; that truncation is only controlled in signed value.

**Fraction in the first family.** The mass counts pairs d,m odd squarefree with weight W_x(dm); their product is squarefree exactly when (d,m)=1. Fixing d, by 341 and partial summation the sum over odd squarefree m coprime to d equals

    c₂ ∏_{p|d} p/(p+1) · (hx/d) ∫η(v)e^(−hv)dv + O(τ(2d)√Y)

for odd squarefree d, where c₂ is the density of odd squarefree integers. Without the coprimality restriction the product is omitted. The total errors are O(Y^(3/2+o(1)))=o(hX). The quotient of the main terms is the mean of the product over odd squarefree d in [0.6Y,0.7Y], with weight 1/d. In this population, for each finite set of odd primes the events p|d have independent joint densities with parameters 1/(p+1), by the Chinese remainder theorem and the square sieve. The weight 1/d preserves the densities by partial summation. Replacing the product by the one truncated at p≤P costs in the mean O(Σ_{p>P}p^(−2)): by 1−∏(1−u_p)≤Σu_p and the count of multiples of p up to Y. Thus the quotient for squarefree products tends to the announced product and the complement gives the fraction of the statement.

**Squarefree products with two representations.** Take d=17v in [0.605Y,0.615Y] and m=19w. Require v,w to be odd squarefree, coprime to each other and to 17·19. Then n=17·19·v·w is squarefree and also admits the divisor 19v in the band because 19d/17∈[0.6Y,0.7Y]. These two divisors are distinct. There are ≫hX such pairs counting the weight: apply the previous computation to v and w with the pulse argument 323vw and also excluding the two fixed primes. The lengths of the variables change by constants, the product of densities stays positive and the error is again O(Y^(3/2+o(1))). For each n with a=a_Y(n)≥2 the surplus multiplicity a−1 is at least a/2, sufficient even when there are more than two divisors in the band.

**Scope.** 345 showed that grouping only the selected rows by product did not reduce the odd mass. Here a part that does disappear when combined with the other rows is measured. The surviving coefficient for each odd squarefree product is still μ(n); the identities do not give an estimate of its local sum. The positivity window does not change.
