# The exact off-diagonal cost, even with weight equal to the gcd

Let P_off(κ) be the sum with term-by-term absolute values of 326 over n≠d, multiplying each term by (n,d)^κ. For h=exp(−am), fixed a>0 and 0≤κ≤1 one has

    lim P_off(κ)^(1/(2m)) = 2 exp(−a/2)       if a≤2,
                           = a exp(1−a)      if a≥2.

In particular, for a≥log 4 the off-diagonal ceiling one is preserved unconditionally up to κ=1. For a<log 4 the excessive absolute rate persists even at κ=0.

**Ceiling.** In the block X≤n<2X of 331, for two distinct multiples of g one has g≤|n−d|≤C hX. Hence there are only blocks X≥1/(Ch). Majorize the weight by the sum of g^κ over the common divisors and apply the count by g of 331. The sum Σ_{g≤ChX}g^(κ−2) costs O(log(2X)) even at the endpoint κ=1. After AM–GM and symmetry the ceiling is a constant times

    h/(m!)² Σ_{X dyadic ≥1/(Ch)} (log(2X))^(2m+1)/X.

By the integral comparison of 331 this costs at most a constant times h/(m!)² times the integral of u^(2m+1)exp(−u) from am−O(1) to infinity. For a≤2 use the full integral (2m+1)!. For a>2 the logarithmic derivative of the integrand is (2m+1)/u−1 and on the whole stretch it is ≤−c_a for large m. The integral costs at most the initial value divided by c_a. Stirling gives the two indicated ceilings.

**Floor.** With t=max(2,a) take X=⌈exp(tm+√m)⌉ and H=⌊c₀hX⌋ as in 332. Both X and H grow even at t=a. The count of 332 gives ≫ XH coprime pairs with both factors squarefree and K≥1/2. All have gcd weight one. With l_m(n)≥(log X)^m/((m!)(3X)^(3/2)) in the block, the lower root is at least t exp(1−(a+t)/2), which coincides with both ceilings.

**Signed cancellation in the pending regime.** For 0≤κ<1, the improvement of 333 also admits the power q^κ off the diagonal:
    
    Σ_q q^κ |S_q| ≪_(a,b,A,κ) h binom(2m,m) m^(−A)

in the whole range of 333. Indeed, in the inversion of weights use |c_g|≤g^κτ(g). The tail of 331 costs in units of h binom(2m,m) at most O_κ(G^(κ−1)log(2G)); it is obtained by partial summation. Take G=m^B with B>(A+1)/(1−κ). In the short part at most G^(1+κ)(1+log G) units of the uniform error of 333 are summed; choose the saving exponent above A+B(1+κ)+2. This last argument does not give the endpoint κ=1. For a<log 4 converting the power saving into an exponential improvement is still missing.
