# An energy of nearby pairs measures exactly the extreme abscissa of the zeros

Let Θ be the supremum of the real parts of the nontrivial zeros of ζ. Fix η real, smooth, nonnegative, with compact support in (0,1) and nonzero integral. Define K(v)=∫η(y)η(y+v)dy / ∫η² and h_m=exp(−√m). For m≥1 put l_m(n)= (log n)^m/(m! n^(3/2)) and

    E_m = Σ_(n,d≥1) μ(n)μ(d) l_m(n)l_m(d) K(log(n/d)/h_m).

Then E_m≥0, the sums are absolutely convergent at each order, and

    limsup_(m→∞) E_m^(1/(2m)) = 1/(3/2−Θ).

In particular RH is equivalent to E_m≤O_ε((1+ε)^(2m)) for every ε>0. There is no height parameter nor finite verification in the statement. The same result holds for any h_m→0 with log(1/h_m)=o(m). One can for example use exp(−m/log(m+2)).

**Positive representation.** Use the transform ∫η(y)exp(−iuy)dy and the probability with density W_m(t)=h_m |hatη(h_m t)|²/(2π∫η²). Fourier inversion gives exactly E_m=∫W_m(t)|A_m(t)|²dt, where A_m(t)=Σ μ(n)l_m(n)n^(−it). Up to the sign (−1)^m, A_m(t) is the Taylor coefficient of order m of 1/ζ at 3/2+it. Unlike the Bohr norm of 321, the average is taken at a height scale depending on m and keeps the nearby pairs, which carry the arithmetic cancellation.

**Ceiling determined by the abscissa.** Fix 0<r<3/2−Θ. On all discs with centers 3/2+it and radius r, the reciprocal is holomorphic and bounded by C_r(2+|t|)^(C_r). To make the uniformity explicit, take 0<δ<3/2−r−Θ. For large heights use log ζ on discs with center 3+iT, of radius 3−Θ−δ, inside the zero-free zone and away from the real pole. Its upper real part is O_δ(log(2+|T|)) by the classical polynomial growth of ζ in fixed strips; the value of the logarithm at the center is bounded by the Euler product. Borel–Carathéodory on an interior disc gives the same ceiling for the modulus of the logarithm, in particular at the required abscissae at height T. Bounded heights are handled by compactness of the reciprocal, regular at 1. Cauchy gives |A_m(t)|≤C_r(2+|t|)^(C_r)r^(−m). The fixed moments of W_m cost O_r(h_m^(−2C_r))=exp(o(m)), by the rapid decay of hatη. This proves the upper bound after letting r increase to 3/2−Θ.

**Why an isolated zero is detectable.** Suppose the limsup were less than the announced value. Choose radii 3/2−Θ<R<R' with the limsup less than 1/R'. There is a zero ρ at horizontal distance from the line of centers strictly less than R. By continuity, on a whole fixed interval of t around Im ρ, the distance |3/2+it−ρ| is less than R. On that bounded interval W_m(t)≥c h_m for all large m, because hatη(0)≠0. By Cauchy–Schwarz the local L¹ of |A_m| is ≤C h_m^(−1/2)√E_m. Hence Σ R^m ∫|A_m|dt<∞. By Tonelli the Taylor series converges absolutely at radius R for almost every t of the interval. This contradicts the pole of 1/ζ at ρ, regardless of its multiplicity. It was not assumed that Θ is attained.

**Where the missing estimate lives.** K is nonnegative, equals 1 at zero and vanishes for |v|≥1. The diagonal already costs O((m+1)^(−1/2)): dropping μ² it suffices to compare Σ (log n)^(2m)n^(−3) with the integral and a maximum by unimodality (an absolute constant times the maximum suffices). The integral divided by (m!)² is (2m)!/[2^(2m+1)(m!)²]; the maximum divided by (m!)² is O((2/3)^(2m)). Only Möbius products with 0<|log(n/d)|<h_m remain. A subexponential ceiling for that signed sum would close the sign. The reduction does not estimate that sum. The index records antecedents of Turán, moments and Gram forms; what is specific here is the quantitative identity for Θ with a relative support that narrows at subexponential speed in the order.
