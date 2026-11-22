# Contraction in rectangles of verified height via explicit Taylor weights

Let G=3·10¹² be the verified height used by datum Z2 of paper 46. For each ε>0 with ε<1/2 there is a single construction of weights (independent of ε) with polylogarithmic band such that

    sup_(1/2+ε≤Re s≤1, |Im s|≤G−2) |H_X(s)| ≪_ε (log X)^(−c_ε),    c_ε>0.

The observation filter of 320 also preserves this bound. The constants may depend on G. No practical numerical threshold for X is provided. The argument uses the zero verification already available; it does not extend that verification nor the support window T. Unlike the supremum at all heights of 322, here the distance to the line 1/2 can be any fixed ε and the height is limited.

**Polynomial fixed without knowing the ordinates.** Put L=log X, m=⌊log L⌋, D=m, B=⌈exp(20m)⌉. With f=1/ζ expand f(s+1) towards s via the polynomial Σ_(j=0)^m (−1)^j f^(j)(s+1)/j!. Since Re(s+1)>1, the coefficient of n^(−s) in this expression is exactly

    μ(n) e^(−u) Σ_(j=0)^m u^j/j!,    u=log n.

For each s in the rectangle, the disc with center s+1 and radius 1+η, with 0<η<min(ε/2,1/4), lies to the right of 1/2 and at height less than G. By Z2 there are no zeros there; the pole at 1 is removable for f. The union of the discs is compact. By Cauchy the error when evaluating the expansion at s is O_ε((1+η)^(−m)), uniform. The same holds in a neighbourhood of the rectangle by reducing η. More generally this disc condition suffices, with no hypothesis at greater heights.

**Gap, support and harmonic mass.** Replace the weight by μ(n) for n≤m, and by zero for n>B. For the former, the Poisson tail of order greater than m with mean ≤log m is ≤(e log m/(m+1))^(m+1) by Chernoff, so the cost is superexponentially small in m. For the latter, the probability of order ≤m is ≤4^m exp(−3u/4) by Markov applied to 4^(−Y) for Y Poisson with mean u. The absolute tail on Re s≥1/2 is therefore O(4^m B^(−1/4)). Call A₀(s) the polynomial thus obtained; by the previous computation A₀(1) is exponentially small since f(1)=0. At index 2m add −2m A₀(1) to its coefficient. The new polynomial A satisfies A(1)=0 and the three modifications keep an error O_ε(exp(−c_ε m)) on the rectangle and in a fixed neighbourhood of the point 1. The Cauchy bound in that neighbourhood also controls the derivative of the error; hence ζ(s)A(s)−1 satisfies the same type of bound even near the removed pole in the product.

**Passage to the real dilations.** With a the coefficients of A, g=1*a, N=C₀ B L² and the cut ψ of 320, put H_X(s)=Σ_(D<n<2N) g(n)(1−ψ(n/N))n^(−s). There is a gap up to D, Σ|a(d)|=O(B) and Σa(d)/d=0. The estimates of 320 give the same one-sided criterion for the arithmetic balance: substitute B for 2D in the Poisson derivation of order ⌈L⌉, since B is polylogarithmic and N/B=C₀L². For the symbol, the centered sampling of ψ(v/N)v^(−s) in 321 gives 1+H_X=ζA+O_K(L^(−K)) on the rectangle: for fixed order j the remainder is ≪_(G,j) N^(1−σ)(B/N)^j, and j can be taken large enough since B≤2L²⁰. This concludes the bound. The positive observation factor in 322 has modulus ≤exp(1) on the whole region.

**Where the result stops being informative.** Under RH the same polynomial works on each interior compact rectangle of any fixed height by the disc proof. A fixed exterior zero ρ, if it existed above the verification, forces H_X(ρ)→−1 by Poisson, whatever the value of A(ρ). Hence control in all rectangles at any height is already equivalent to RH. The improvement is an effective localization of the approximation mechanism in height and the return to a polylogarithmic band; it is not a new zero-free region nor a uniform control when the height grows with X.
