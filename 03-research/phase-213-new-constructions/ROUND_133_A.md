# Exact exponent of the local Mertens oscillation in each power band

For fixed h>0, B=Z^(1+h), let L(Z,B)=max_{Z≤u≤v≤B}|Σ_{u<d≤v}μ(d)|. Then, without assuming RH,

    lim_{Z→∞} log(1+L(Z,B))/log B = Θ = sup Reρ.

In particular, to close the sign it would suffice to exhibit an unbounded sequence of bands with some fixed h where L(Z,B)≤B^(1/2+o(1)). It suffices to control the variations of Mertens on those intervals, with an unknown starting level on each one. The identity does not ensure that such a sequence exists.

**The witness of 132 appears in every logarithmic neighborhood.** Keep a fixed weight w* of 132 chosen to detect a zero with real part arbitrarily close to Θ, and write G*(s)=∫t^s w*(t)dt. For X large, its average of ψ(Xt)−Xt is

    J(log X)=−Σ_ρ G*(ρ)X^ρ/ρ + O(1).

Indeed by smoothed Perron one integrates (−ζ'/ζ)(s)G*(s)X^s/s initially between real parts 1 and 2. The identity is also obtained by Mellin inversion of the tail weight W. Shift to Re s=−1/4: G* is holomorphic in the strip by the O(t) behavior at zero and the decay at infinity, and two logarithmic integrations by parts give O((1+|Im s|)^−2) uniformly on that closed strip. Use good heights of the explicit formula and the functional equation at the left edge. The residue at 1 and the term Xt vanish since G*(1)=0; the origin is regular in the integrand since G*(0)=0. One even obtains error O(X^(−1/4)). The multiplicity of each zero multiplies the corresponding residue. The series is absolutely convergent.

For every η<Θ close enough to Θ, each interval [(1−q)T,(1+q)T] with fixed small q>0 and T large contains t with |J(t)|≥exp((Θ−e)T), where e>0 can be fixed in advance by choosing η close enough to Θ and q small enough. To make this precise, apply the Gaussian lemma of 115 to z=ρ−1/2 if Θ>1/2. Choose a zero with Reρ>Θ−e/4, a weight detecting it and a rate d<Reρ−1/2 with d>Θ−1/2−e/2. Undoing the normalization loses at most qT/2 in the exponent. For Θ=1/2 the normalized series is an absolutely convergent trigonometric series with a nonzero coefficient. Its mean square over any interval of length tending to infinity converges, uniformly in the origin, to the sum of squares of its coefficients: truncate the series uniformly and integrate the finitely many cross terms. Hence on each interval the modulus is bounded below by a positive constant. This also covers Θ=1/2.

**Error margin.** In 131–132 one can choose r so large that the high tail costs O(X^(1/3)) for the chosen δ, using (1+2r)δ>2/3 with strict inequality to absorb logarithms. The lower endpoint costs O(X^(1/3)), and the factorial cost without correctors is O(D²/X)=O(X^(1/3)). Thus the total error stays below X^(2/5) eventually. This allows the product argument to be used also when Θ=1/2; a mere o(√X) would not suffice for that inference. First δ,r are chosen, then the zero and n.

**Placing the whole local sum inside the given band.** For a small τ>0 take T=(3/2)(1−τ)log B. Choose τ,q,δ small in that order with

    (1−τ)(1+q)<1,
    (1−τ)(1−q)(1−3δ/2)>1/(1+h).

Thus for every t of the interval, X=exp t has [κ X^(2/3−δ), floor(X^(2/3))] inside [Z,B] for B large, by strict margin. In the above witness apply 132 and P≪ε X^((1/3+δ)(Θ+ε)). One obtains

    log(1+L(Z,B)) ≥ T[Θ−e−(1+q)(1/3+δ)(Θ+ε)−o(1)].

The loss X^(2/5) is negligible for small enough parameters even at Θ=1/2. Dividing by log B and letting τ,q,δ,e,ε tend to zero respecting the margins proves liminf≥Θ. The limsup≤Θ is the classical Mertens bound used in 132. The conclusion concerns every large Z for each fixed precision, with constants that may depend on that precision.

**Antecedents and limit.** The detector in each neighborhood is 115; the local product bound comes from 132. The conclusion about Möbius increments in all bands uses both and the quantitative improvement of the error of 131 for the critical case. The coincidence in modulus of 132 alone does not give a contradiction: here it is explained why the Mertens excursions can be found in prescribed bands without information on the joint signs.
