# Only centers with local mass balance need a reciprocal bound

Use r=exp(11/25), w,V and E of 109. For a prime q call L,R the sums of log p over (q/r,q) and (q,rq), respectively, and l,s the sums of (log p)/p over the same intervals. Let d=log q. The global sign is equivalent to this implication for every sufficiently large prime q:

    If −d ≤ R−rL ≤ rd, then r(s+d/q)−l ≤ 2√r V(1).

The filter only uses Chebyshev masses on the two intervals, with tolerance of order log q against masses of order q. The ceiling uses only their reciprocal moments. No density of centers passing the filter is claimed.

**Computation.** Set G(x)=E(x)/x. On each piece E(x)=Ax+B one has G'(x)=−B/x². At q the intercepts before and after are, by the branches of 109,

    B_−=(rL−R−d)/(2√r),     B_+=(rL−R+rd)/(2√r).

The endpoints q/r,rq are not primes since r is transcendental. A local maximum requires B_−≤0≤B_+, precisely the filter. The slope of E before q is A_−=[r(s+d/q)−l]/(2√r)−V(1). At a filtered center one has

    A_−−(r+1)d/(2√r q) ≤ G(q)=A_−+B_−/q ≤ A_−.

Under RH, 109 gives G(q)≤−c/√q eventually, so A_−≤0 at all filtered centers.

**Converse.** If RH fails, the poles of V P of 109 and Landau applied to either sign exclude both possibilities E≥0 eventually or E≤0 eventually. Hence there exist, arbitrarily late, three points with signs −,+,− in that order. G has the same signs. On the closed interval between the negative points choose the right endpoint of the set of maxima of G; the value is positive. The branches are finitely many on that compact set and monotone or constant for G. On leaving the maximal plateau the sign of the derivative passes from non-negative to negative (including a plateau of length zero). This is only possible at a downward slope jump of E, since the jump of G' is that of E' divided by x. By 109 that point is a prime. There the filter holds and A_−≥G(q)>0, a contradiction.

**Relation with the antecedents.** In 094 the crossing depends on the mass from the origin; in 109 all prime centers are checked. Here the center and both comparisons only require neighbors within the same fixed band. What remains is to control the correlation between the mass balance and the reciprocal balance at the selected centers.
