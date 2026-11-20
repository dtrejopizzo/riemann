# The upper prime band above any fixed power less than one suffices

For fixed 0<a<1, let y=x^a and
     
    E_a(x)=Σ_{y<p≤x} log p log(x/p) − [x−y−y log(x/y)].

The global sign is equivalent to E_a(x)≤0 eventually, even for a arbitrarily close to one but fixed. Under RH E_a(x)≤−(1.953−o(1))√x. For a≥1/2 the sets of multiples ≤x of the distinct admitted primes are disjoint. This localizes the criterion without an auxiliary condition on the removed sum.

**Cut at the root.** For F(x)=S(x)−x one has exactly F(x)−E_a(x)=F(y)+(1−a)log x [θ(y)−y]. If a=1/2, the classical quantitative PNT θ(y)−y=O(y/log³y) and its integral give F(x)−E_a(x)=o(√x) unconditionally. Under RH the classical bound θ(y)−y=O(√y log²(2y)) and 092 give the same o(√x) for each a<1. Thus 092 proves the direct implication with margin.

**Converse for a>1/2.** The unconditional estimate of the previous cut does not reach here. Set Θ=sup Reρ and P(s)=Σ_p(log p)p^(−s). In Re s>1/2, P is meromorphic since it differs from −ζ'/ζ by a holomorphic series (the powers of order ≥2). In Mellin over x≥1, F and θ−id have transforms P(s)/s²−1/(s−1) and P(s)/s−1/(s−1) respectively. Both are regular at s=1 by the unit residue of P. The scale x^a replaces s by s/a with factor 1/a, and log x gives the negative derivative. Hence the transform of E_a is regular on the real half-axis s>1/2; the contributions of the centered prefix are holomorphic in Re s>max(1/2,aΘ). If Θ>1/2 there is a zero with Reρ>max(1/2,aΘ) by definition of supremum. There the pole of P(s)/s² survives, even if Θ is not attained. An eventual upper bound E_a≤0 contradicts Landau for −E_a, since it would force holomorphy in Re s>1/2. This converse also works for a≤1/2 and for a ceiling O(√x) through the same argument.

**Comparison.** In 075–076 the weight U(x/p) brings its own root-order oscillation, and the fixed block can retain the criterion. Here the weight is log(x/p), the center is the elementary integral over the band, and the cut moves with x according to a prescribed law. The argument does not allow a to tend to one with x nor does it prove the arithmetic inequality in any of these bands.
