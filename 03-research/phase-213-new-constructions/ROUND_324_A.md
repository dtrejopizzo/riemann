# Localization up to the critical line without assuming simple zeros

Put m=⌊log log X⌋. On the closed rectangle K given by 1/2≤Re s≤1, |Im s|≤G−2 with G of 323, there is a modification of its weights with the following result. Let Z be the finite set of critical zeros up to height G−1 in modulus. For every integer k≥1,

    |H_X(s)| ≤ C_(k,G)(1+m dist(s,Z))^(−k) + O_G(exp(−c_G m)),   s∈K.

The weights are the same for all k. In particular the modulus is <1/2 outside discs of radius C_G/m around the zeros, for X sufficiently large, even on the critical line. The constants are not computed. At the zeros themselves the multiplier tends to −1. This describes where the contraction of the symbol is lost in the verified zone, without extending that zone.

**Changing the Taylor order.** Choose w smooth nonnegative with integral one and compact support in (1,2). Average the Taylor polynomials of 323 of integer degrees j with weights w(j/m)/Σ_j w(j/m). Keep μ(n) for n≤m and erase n>B=ceil(exp(40m)). The Poisson bounds of 323 remain uniform for m≤j≤2m: for example the support tail is O(4^(2m)B^(−1/4)). Correct the mass at 2m as in 323, which costs exponentially little because in a neighbourhood of 1 the Taylor series converges geometrically. The short symbol with N=C₀ B(log X)² approximates this polynomial multiplied by ζ, minus one, with error exponential in m (Poisson of fixed, sufficiently high order, B=O((log X)^40)). In a neighbourhood of 1 the cancellation of the pole is used as in 323. Consequently the arithmetic criterion of 320 with polylogarithmic band remains applicable.

**Separating the singularities.** Away from fixed neighbourhoods of the zeros, the discs centered at s+1 of radius 1 contain no zero: they lie to the right of 1/2, with possible tangency only at s if Re s=1/2. By compactness the radius can be increased slightly, always within the verified height. Near each zero ρ∈Z touching the zone under consideration, write f=1/ζ as its principal part plus a regular part. The latter admits the same increase of radius, after reducing the neighbourhood, since in the disc of center 1+ρ and radius 1 the only zero was ρ. The regular Taylor error is exponential, uniformly in the degree j≥m. The finiteness of Z allows gathering the constants.

**What the averaging of orders contributes.** Write δ=s−ρ and r the multiplicity. For (s−ρ)^(−1) the exact remainder of the degree-j expansion from s+1 is δ^(−1)(1+δ)^(−j−1). For a pole of order l≤r apply (−∂δ)^(l−1)/(l−1)! to that remainder; differentiation commutes with truncation since the translation has fixed length. On multiplying by ζ(s), each term is a bounded analytic unit times a constant, times δ^(r−l+a), times a polynomial in j of degree a, and times (1+δ)^(−j−1−a), with 0≤a≤l−1. This description includes the coefficients of the principal part.

With v=(1+δ)^(−1) one has |v|≤1 and |1−v| comparable to |δ| in the right neighbourhood. For a fixed polynomial P_a of degree a, the normalized sum of w(j/m)P_a(j)v^j costs O_(a,b)(m^a(1+m|δ|)^(−b)) for every fixed b. The trivial bound handles m|δ|≤1. Elsewhere multiply by (1−v)^b and shift indices; the absolute sum of the finite differences of order b of the normalized coefficients is O(m^(a−b)), by smoothness and interior support of w. Taking b≥k+r absorbs the powers of m|δ|. This proves the ceiling also in the limit δ=0 by continuity.

**Checkable profile.** For fixed z with Re z≥0 and ρ in the rectangle, evaluating at s=ρ+z/m one obtains

    H_X(ρ+z/m) → −∫₁² w(u) exp(−uz) Σ_(a=0)^(r−1) (uz)^a/a! du.

In the differentiated formula only the pole of order r survives. Its coefficient cancels the leading factor of ζ; the coefficient of the distributed derivative gives 1/a! and the polynomial in j is monic of degree a before that factor. Passing from j/m to the integral is a Riemann sum. The minus sign comes from H≈ζ T−1. At z=0 the limit is −1, which prevents a uniform contraction within distances o(1/m). Neither the proof nor the profile presupposes simplicity. No new zero ordinates nor a sign inequality above the verified height have been obtained.
