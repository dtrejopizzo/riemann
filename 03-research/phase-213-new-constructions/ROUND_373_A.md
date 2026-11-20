# Width of the parity exceptions on the logarithmic scale

**Status: PROVED, with independent review of the cut cells, the case Θ=1 and the two integrated consequences.**

We use S(x) and Θ of 372. If Θ>1/2, for each η>0 and each sign e=±1 there exist arbitrarily large v and intervals I⊂[v−1,v+1] of length ≥exp(−ηv) where e S(exp w)>exp((Θ−η)v) on all of I. The cut is the exact w², even next to a jump.

**Proof.** Choose 0<δ<min(η/5,(Θ−1/2)/2). By 372 there are v→∞ with e S(exp v)>exp((Θ−δ)v). For a frozen cut z=v² and |w−v|≤1 we have

    |∂_w S^*(exp w;z)| ≪δ exp((Θ+δ)v).

If Θ<1, a fixed vertical Θ<σ<min(Θ+δ,1) is used as in 372. Differentiating only introduces s in the integral, absorbed by the Gaussian; the cost E_z(σ)=exp(o(v)) is uniform. If Θ=1 one can sum in modulus the derivative of the weight, bounding |g'| by a wider Gaussian with the same factor exp(u/2); the dyadic sum costs O(exp w). The derivative bound also holds if the set of primes corresponding to v² is kept on both sides of v.

The possible jumps are at the points √p, p prime; it suffices to use the finer partition by √n, n integer. The cell [√floor(v²),√(floor(v²)+1)) containing v has length asymptotic to 1/(2v). In at least one direction from v a distance ≥1/(5v) to its edge remains; if v is the left endpoint the right side is taken, since the cut includes the primes p≤v² and is constant to its right. On that side the set of removed primes coincides exactly with that of v. The closed interval of length exp(−3δv) fits strictly before the next edge for large v and the variation is Oδ(exp((Θ−2δ)v)), negligible relative to the initial value. The result follows by the choice of δ.

**Two consequences.** The integral of max(S(x),0) dx/x^(3/2) from e to infinity is finite if and only if RH. Under RH, 368 makes the integrand vanish eventually. If Θ>1/2, choose 2η<Θ−1/2 in the previous result: a single interval contributes at least exp((Θ−1/2−2η)v−1), without bound.

One can even ignore the amplitudes. Let B={x≥e:S(x)>0}. For any fixed ε>0, RH is equivalent to the finiteness of ∫_B x^(ε−1)dx. Under the alternative, choose η<ε and an interval of positive sign; its contribution is ≥exp((ε−η)v−ε). This does not imply divergence of the logarithmic measure ∫_B dx/x.

292 integrates a positive part in an auxiliary parameter. Here the length of intervals of a single variable with discontinuous cut is estimated and one can integrate only the indicator of the sign. An arithmetic estimate of that measure remains open. The independent review checked that the argument for Θ=1 uses only the absolute sum of |g'|, without needing a vertical to the right of Θ inside the strip. In the integrated consequences there is no need to select disjoint intervals: the mass of a single interval tends to infinity, which already contradicts the finiteness of the total integral. Under RH the integrals over the initial compact set are finite by uniform convergence of the Gaussian sum. Deduction dependent on 368 and 372.
