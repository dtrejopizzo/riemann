# A band of squared-logarithm ratio for the calibrated binomial fit

There exists a fixed weight w≥0 with support [1,2] for which the calibrated criterion of 262 remains equivalent to the global sign. With N=⌊2x⌋ and U=⌊√N⌋, there is an unconditional fit of exact mass and variation O(√N log²(2N)) that satisfies all equations except, possibly, those of the atoms

    U/(C log²(2N)) < q ≤ U

for some absolute constant C. Above U the equality holds even at every integer. The smoothing of 047 is reused here; the additional conclusion concerns the exact fit on prime powers of 271–273.

**Weight and criterion.** Let L=log 2 and f the density of the convolution of the uniforms on [0,L/(j(j+1))], j≥1. Put w(y)=y^(−1/2)f(log y) for y>0. Its Mellin transform H(s) is the product of the factors (exp(l_j z)−1)/(l_j z), with z=s−1/2. It is nonzero for Re z>0, by normal convergence of the deviations from one and the absence of vanishing factors there. The argument of 262 applies with h=H(1). A calibrated fit of cost x^(1/2+o(1)) implies, by Stirling and Mellin, absence of zeros to the right of 1/2. Conversely, under RH the inversion of 261 costs x^(1/2+o(1)) by partial summation with Mertens and the smooth derivative of the weight. The calibration defect is corrected with the relation of 262 because the explicit formula for the smooth weight gives ΣΛ(m)w(m/x)−xh=O_w(√x) under RH (rapid decay of H in the strip). The calibrated-fit criterion is used; the numerical margin of the cosine weight of 257 is not transferred.

**Control of derivatives of all orders.** Differentiating the first k uniforms once, each derivative has measure norm 2/l_j. The next uniform has density bounded by 1/l_(k+1), and the tail has mass one. Hence ||f^(k)||∞≤C₀^(k+1)(k!)², absorbing polynomial factors into C₀. The same bound holds for w: on [1,2] the Taylor coefficients of log(y+t)−log y in t are ≤1 in modulus. In the composition formula up to order k, the degree-j power of the increment contributes in degree k at most binom(k−1,j−1). Multiplying by f^(j)/j! and by k! gives the stated bound, also after multiplying by y^(−1/2). All endpoints are flat. The two correctors φ_i of 273 are obtained by rescaling f, and the cutoff χ by integrating another rescaled copy. All satisfy bounds of the same type.

**Quadrature.** Use S of 273 with w and these correctors. The argument of the discrete moments gives |A|+|B|≪(x/U)log²(2N). For all k≥0,

    ||S^(k)||₁ ≤ x log²(2N) C₁^(k+1)(k!)² U^(−k).

Indeed, in each term χ(t/U)w(dt/x) only d≤4x/U are involved, with integration interval of length ≤2x/d. In the Leibniz rule, the differentiation scales are ≤4/U and binom(k,i)(i!)²((k−i)!)²≤(k!)². Summing x/d and adding the correctors proves the bound. For the initial cost the variation estimate O((x/U)log²(2N)) of 273 is retained.

Integrating k times by parts and choosing k proportional to √(U|ξ|) with a sufficiently small constant, one obtains |Ŝ(ξ)|≪x log²(2N) exp(−c√(U|ξ|)). For 1≤m≤U the sum over frequencies l/m with l≠0 satisfies the same exponential bound with smaller c: for A=√(U/m)≥1 one has Σ_(l≥1)exp(−c A√l)≪exp(−cA/2). The exact sum at m=1 is zero, so the integral of S is also bounded by O(x log²(2N) exp(−c'√U)). By periodization,

    |R(m)| ≪ (x/m) log²(2N) exp(−c'√(U/m)).

For m≤U/(C log²(2N)) take C sufficiently large: the error is O(N^(−3)) per modulus. Since the target there is zero, the exact chain repair of 271 and the fixed recalibration cost o(1), without altering m>U. The variation of the repair in the indicated band remains open; that both ends are N^(1/2+o(1)) does not bound its cost. The improved threshold concerns this fixed smooth weight, not the original cosine.
