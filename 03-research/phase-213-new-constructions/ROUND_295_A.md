# A cutoff near the square root balances the block without a large prime at square-root precision

For the coefficients b_t of 292 let S_t(x,y)=Σ_(n≤x; P⁺(n)≤y)b_t(n). For all sufficiently large x and each t∈[1,2] there exists a cutoff y=y(x,t) in [√(x/48),√(x/2)] such that

    |S_t(x,y)| ≪ √x/log x.

The constant is uniform. Hence the integrated one-sided criterion of 292 can be applied only to the integers having some prime >y(x,t). The cutoff depends on the frequency and can be taken as the first jump from negative to nonnegative. The partial sum of that complement remains open.

**Identity when moving the cutoff.** Fix z=2 or 48, y=√(x/z), L=log x. In the series of b_t remove each factor (1−u_p p^(−s))² for p>y, multiplying by its inverse. Up to x only the degree-one and degree-two terms in those primes are needed, since y³>x. The uncorrected term is the full partial sum, O_R(x/L^R) by 294. The correction from one prime is 2Σ_(m≤x/y)b_t(m)Σ_(y<p≤x/m)u_p. It is O_z(x/L³) by the moment computation of 294: here no coprimality between m and p is imposed, and log y/L stays bounded away from 0 and 1. The p² term costs O_z(√x), since its multiplier is 3u_p² and its cofactor m≤z.

For two distinct primes there remains 4Σ_(m≤z)b_t(m)Σ_(y<p<q; pq≤x/m)u_pu_q. Uniformly in t, the weighted prime mass over intervals in [y,zy] is replaced by du/log u with error O_(z,R)(√x/L^R), by the PNT in the two classes modulo 3 and partial summation. Apply it first to the vertical section and then to the horizontal one of the hyperbolic region; the weighted length function of the section is monotone and O_z(√x/L), so the errors are O_z(x/L³) taking R large. One can count ordered pairs, remove the diagonal at cost O_z(√x) and divide by two. For the two densities, 1/log p and 1/log q equal (2/L)(1+O_z(1/L)). The ordered area is y²(R log R−R+1) with R=z/m. One obtains

    S_t(x,√(x/z)) = (8x/L²) K_t(z) + O_z(x/L³),
    K_t(z)=Σ_(m≤z) (b_t(m)/m)[log(z/m)−1+m/z].

**Two certified signs.** K_t(2)=log 2−1/2>0. For z=48, the interval computation of verify_295.py encloses the same finite sum on 1024 closed cells covering [1,2]. It uses the exact local values 1,−2u_p,u_p²,0 and interval arithmetic with 35 digits. The run verifies K_t(48)<−1/25 on each cell. Hence the block passes from negative to positive between the indicated cutoffs, uniformly for all large x.

**Actual size of a jump.** On admitting p in that range one adds the terms with largest prime p. Those with exponent two cost O(1), since the cofactor is ≤48. For exponent one there remains b_t(p) times the sum of b_t(m) over m≤x/p with all primes <p. The full partial sum up to x/p is O(√x/log² x) by 294. To discount m with a prime q≥p, observe that m/q≤x/p²≤48, and for large x such a q is unique and simple. There are O(√x/log x) possible q by Chebyshev, and the cofactor contributes only an absolute constant. Thus the jump is O(√x/log x). Starting at the lower endpoint and choosing the first cutoff with nonnegative value proves the statement. The rule is measurable in t since it is a choice among a finite number of continuous inequalities. Both taking the positive part and integrating preserve the budget on removing this block. The result does not claim that the two blocks vanish at the same cutoff.
