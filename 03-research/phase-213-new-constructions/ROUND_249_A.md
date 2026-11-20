# How much future the barycentre admits using only the primes already known

For each prime p, form D(x)=x²C(x) from 247. If D(p)>0, call H(p) the positive root of

    D(p)+hD'_+(p)−θ(p)h²=0.

Set H(p)=0 if D(p)≤0. This length is computed with the three prime moments up to p. For 0≤h<min(H(p),p), the barycentre at p+h remains strictly positive even if any subset of the primes in (p,p+h] is removed. Indeed the quadratic expression is exactly what the primes up to p contribute, and each new prime r contributes (p+h−r)(3r−p−h)log r≥0. If the next prime is at distance less than H(p), the margin at p suffices to cross that gap.

Let Θ=sup Re ρ. One has

    limsup_(p prime→∞) log(1+H(p))/log p = (1+Θ)/2.

In particular, WITHOUT assuming RH there are arbitrarily large primes from which the sign is guaranteed on the whole stretch 0≤h≤0.41 p^(3/4), even discarding all new primes. To prove RH it would suffice to prove the arithmetic ceiling H(p)≤p^(3/4+o(1)) for all large primes. The direction of the ceiling matters: excessively long radii would also reveal a failure of the global sign.

**Computation of the radius.** On a stretch without entries D'_+(x)=4Σ_(r≤x) r log r−2xθ(x). Under RH the estimate of 235 and partial summation give D'_+(x)=O(x^(3/2)log²x); the continuous term cancels. By 247, 4/15−0.094+o(1)≤C(x)/√x≤4/15+0.094+o(1). Dividing the root formula by x^(3/4), using θ(x)∼x, gives

    H(x)/x^(3/4)=sqrt(C(x)/√x)+o(1).

Here the same definition is extended to real starting points. In particular 0.41<H(p)/p^(3/4)<0.61 for every sufficiently large prime under RH. Without hypothesis, for each ε>0, the bound of 235 for θ(x)−x gives D'_+=O_ε(x^(1+Θ+ε)) and C(x)=O_ε(x^(Θ+ε)) by partial summation with k from 247, whose integral is zero. The quadratic formula gives H≪|D'_+|/θ+√(max(D,0)/θ), of exponent at most (1+Θ)/2 in the upper limit, since Θ≤1.

**Lower radii when there are zeros to the right.** For each 1/2<d<Θ the continuous function C(x)/x^d is unbounded in both directions arbitrarily far out. In the case of an eventual ceiling or floor apply Landau to A x^d±C(x), eventually nonnegative: its transform has a nonreal pole to the right of d and no real pole there by 247. Between negative and positive excursions choose local maxima x→∞ with C(x)≥x^d. A prime cannot be such a maximum: the derivative of C(x)/x^d has there a strictly upward jump due to the entering prime. Hence D'(x)=(2+d)D(x)/x>0 at those maxima.

For 0≤h≤L=x^((1+d)/2)/2, the primes up to x contribute at least D(x)−θ(x)L²>0, since D(x)≥x^(2+d) and θ(x)≤2x. The first prime p>x is at distance O(x^(5/8)) by the short-interval theorem used in 238. Consequently p−x=o(L). Now freezing the primes at p preserves the margin up to x+L: the newly incorporated prime only contributes nonnegative amounts on that stretch. Thus H(p)≥L−(p−x) for those primes, which give lower exponent (1+d)/2. Letting d↑Θ and combining with the RH case gives the identity.

**Scope.** An unconditional sequence of positive blocks and an upper criterion on their robustness are obtained. Positivity of exceptional blocks does not give a perpetual induction from prime to prime. It remains to prove that the three partial moments do not produce radii of exponent greater than 3/4.
