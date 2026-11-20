# A macroscopic cutoff leaves the large-prime block bounded by a constant

Let R_t(x,y) be the sum of b_t(n) over n≤x with a prime >y. For sufficiently large x and 0≤t≤1 one can choose y in [x/4,x/2] with |R_t(x,y)|≤C absolute. Only sums over primes and the coefficients b_t(1), b_t(2), b_t(3) are needed to choose the cutoff. By 292, the global sign is equivalent to an integrated square-root ceiling with loss for the positive part of the remaining block in that fixed band. Here the error from removing the large block is O(1). The remaining block still contains almost all of the arithmetic difficulty.

**Computation at t=0.** Let π_i be the count of primes congruent to 2 modulo 3. Over the whole indicated interval, on factoring n=pm with p>y one has m<4, p is unique and b₀(3)=0. Hence

    R₀(x,y)=−4[π_i(x)−4π_i(x/2)+3π_i(y)].

The bracketed expression at y=x/4 is asymptotic to −x/(8 log x) and at y=x/2 to x/(4 log x), by the PNT in progressions. Choosing π_i(y) as the integer nearest to (4π_i(x/2)−π_i(x))/3 in fact gives |R₀|≤4, by integrality of the numerator. A prime attaining that value satisfies

    y = x/3 + x log(4/3)/(3 log x) + O(x/log²x).

To check this use π_i(cx)=li(cx)/2+O(x/log⁴x) uniformly in 1/4≤c≤1/2. After extracting x/(2 log x), the combination of the three li in the formula for R has main term −1+3c and next term [1−2(1+log 2)+3c(1−log c)]/log x. The first forces c=1/3+O(1/log x); substituting into the second gives log(3/4)/log x. Rounding the count by one unit is absorbed.

**Persistence in a fixed band.** For c=1/4 or 1/2, the PNT in progressions and partial summation for u_p=1−χ(p)cos(t log p) give, uniformly in 0≤t≤1,

    R_t(x,cx)=−2x/log x · Σ_(m≤3) b_t(m)(1/m−c)₊ + O(x/log²x).

At t=0 the profile equals −1/4 and 1/2 respectively. On all of [0,1] the second profile is 1/2, and the first is 3/4+b_t(2)/4+b_t(3)/12≤1/4−cos(log 2)/2<0. Thus the signs persist with margin over that whole band. At each jump when admitting p into the smooth block, the change in R has modulus ≤4Σ_(m≤3)|b_t(m)|≤36. The endpoints of opposite sign guarantee a value of modulus ≤18, choosing the endpoint closest to zero of the first jump that crosses it. The choice is measurable by finitely many comparisons. The one-sided argument of 292 works in the interior of any fixed interval of positive length, since the weight detecting a pole can also be localized there. By the 1-Lipschitz property of the positive part, removing the block R modifies the average by O(1).

**Scope.** Round 302 computes a large mass for a cutoff at the square root, and 295 balances the smooth block via another cutoff near the square root. Here the complement itself is balanced with jumps of constant size, thanks to the fact that the cofactors can only be 1, 2 and 3. Estimating the sum over the integers with all their primes below this cutoff is still pending.
