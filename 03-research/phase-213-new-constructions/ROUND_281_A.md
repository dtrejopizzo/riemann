# The diagonal of the samples, including both calibrations, already costs a square root

For the points y of 280 there are explicit real coefficients K_y(d), independent of μ, such that with V=x/U and P=log(2N),

    T(y)=Σ_(d≥V) μ(d) K_y(d) + O(P⁶),       Σ_d |K_y(d)|² ≪ U P⁶.

The series are taken in increasing order of d. This includes the two mass and balance corrections, even though their original definition in 273 used all d from 1. Since there are O(P² log P) points, the diagonal of the full sum of squares is unconditionally O(U P⁹). What remains is a condition on correlations between distinct integers, with a kernel that is an explicit Gram matrix.

**Corrections.** Keep the discrete matrix of 273 divided by U, centering the second row by 1+log U, and denote its inverse by M, of norm O(1). For S₀(t)=χ(t/U)Σ μ(d)w(dt/x), the two discrete terms to be subtracted from the targets (0,xh) can be replaced by ∫S₀(t)dt and ∫S₀(t)log(t/U)dt with error O(U P²). Indeed Var(S₀)≪x/U, by summing variations; for the second coordinate one uses the exact integral of log(t/U) over (j−1,j], which equals the centered discrete difference. On the relevant cells the logarithm is O(P). Including the division by U, the error in the amplitudes is O(P²).

In the order of summation by d, the UNCUT integrals of each copy w(dt/x), against 1 and log(t/U), weighted by μ(d), sum respectively to 0 and xh. Indeed each copy gives xh/d in the first, and in the second (x/d)∫w(u)log(xu/(dU))du. One uses Σμ(d)/d=0 and Σμ(d)log(d)/d=−1, obtained from the prime number theorem with classical remainder, partial summation and the value and derivative of 1/ζ at 1. This computation integrates each copy before summing; it does not interchange a global integral with a non-absolutely convergent series.

Thus the amplitude vector is Σ μ(d) v_d + O(P²), where v_d is M applied to

    (V/d) ∫ w(u) [1−χ(Vu/d)] (1,log(Vu/d)) du.

It is zero for d<V. For d≥V its norm is O((V/d)(1+log(d/V))); hence Σ||v_d||²≪V by comparison with the scaled integral. It is essential to remove the known full moment before estimating: the weights x/(Ud) without that cancellation would start at d=1.

**Coefficients per sample.** Put Φ(y)=(Σ_l φ_i(ly/U))_(i=1,2). By 279 the full inversion sums to zero on the band. Hence

    K_y(d)= Φ(y)·v_d − Σ_(l≤U/y) [1−χ(ly/U)] w(dly/x).

The second summand only uses V≤d≤2x/Y and has size O(P²); ||Φ(y)||≪P². There are O(U P²) integers in the interval and V≍U. This gives the announced quadratic bound and an evaluation error O(P⁴), absorbed into the statement.

**What estimate would suffice.** For the prefixed set of samples define G(d,e)=Σ_y K_y(d)K_y(e). For each x sum first over d,e≤L and let L→∞. The rectangular truncation converges to the square of each convergent series, and the diagonal converges absolutely. Thus

    Σ_y |Σ_d μ(d)K_y(d)|²
      = Σ_d μ(d)²G(d,d) + lim_(L→∞) Σ_(d≠e≤L) μ(d)μ(e)G(d,e),

where in the last sum both indices are ≤L. The first term is O(U P⁹). Together with 280, RH is equivalent to the off-diagonal term being ≤x_j^(1/2+o(1)) along some subsequence x_j→∞. Indeed the sum of squares controls the maximum, and under RH the maximum satisfies the quarter-power ceiling, even at every scale. The O(P⁶) errors per sample affect none of the exponents. The kernel is positive semidefinite at each truncation by construction; positivity only gives a floor for the off-diagonal sum, whereas closure requires a ceiling. Unlike the bilinear form of 049, here the kernel comes from squares over a prefixed set of samples and the calibration contributions are controlled in the same diagonal. The ceiling for the distinct pairs remains open.
