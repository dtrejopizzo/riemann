# POWER SCALE AUDIT 029

Status: ROW_PATTERN029, BOUNDARY_WEDGE029 and SCALE_BRIDGE_LIMIT029 APPROVED. Papers untouched.

## 1. Region k≥1, u²≥256N — APPROVED

Reviewed `POWER_ROW_PATTERN_029.md` and `tools/power_row_pattern_029_verify.py`; independent run PASS. The Euler formula with periodic B2 gives an error after logz−1/(2z) of modulus≤1/(4t²). Applied at5/4+it and translated to1/4+it, it produces exactly9/(8t²). The beta integral has the declared logarithmic and inverse moments; the inverse is finite from k1. The monotonicities of the bound in k and ψ(N−1/2)≤logN give ARCH>.9 for all N≥2,k≥1,u²≥256N.

Cauchy–Schwarz with both weights has the factor e^−ηt and the two correct opposite norms. WRN admits negative η. The quotients of B_l and of the binomial coefficient differ by (N−1)l≥0; the sum of series and the algebraic simplification produce CENTERED with cost[(u²−η²)/(u²−4η²)]^(N−1/2). eta4 and u²≥256N make that cost less than exp(3/14)<14/11, uniformly in N. The comb bound<.16 includes the whole real sum ofΛ.

The beta polar, Jensen for the gamma ratio, Bernoulli and the quotient2N/(4u²−1)≤4/2047 control all adverse polars by.001; the even ones are favourable. Thus W/norm²>739/1000>.7 is an inequality of the full REAL form on the whole region. GAIN is correct but is not used as an automatic sign.

The distinction from JOINT_SCALE016 is keeping N/u² bounded and cancelling the linear cost of weights through both signs. It does not contradict the obstacle at fixed u, growing N/u². k0 is not covered because of a divergent inverse moment.

## 2. Limit of the bridge of growing rates — APPROVED

Reviewed `POWER_SCALE_BRIDGE_LIMIT_029.md`. The spectral density is normalized. Its maximum atτ²/u²=k/N decreases with k: the convex midpoint comparison gives ψ′(x)≤1/(x−1/2), whose integral provides the declared strictly negative logarithmic derivative. The limit k0 and Jensen for the gamma ratio give HEIGHT<sqrtN/(u sqrtπ).

Hence every normalized positive mixture of the domain u≥C√N has height≤1/(C√π). On I=[−C/8,C/8] its mass is<1/4. A fixed target atom u0 with2M−3>256u0²/C² has mass>3/4 on I by Chebyshev. The L1 distance is therefore>.5. The argument uses an interval, not a pointwise value; it also excludes non-normalized cones whose mass tends to1.

This is an obstruction to automatically replacing the positive cone of the bridge017 by this restricted region. It does not exclude other bridges, identities with additional structure or direct controls. The new region certifies neither window T nor global sign.


## 3. Region including k0, u≥64√N — APPROVED

Reviewed `POWER_BOUNDARY_WEDGE_029.md` and `tools/power_boundary_wedge_029_verify.py`; independent run PASS. The coefficient comparison uses exactly(N−1)(l−1)≥0 and also holds for N1. The WRN expansion requires a>0 andη²/a²<1, valid for both signs of the weight whenη<u/2. The bilateral product and eta15 give cost≤exp(675/4096)<6/5 uniformly; the bound of the whole comb<1/5000 keeps realΛ.

The global lower bound ofψ translated from5/4 has the exact reciprocal1/(τ²+1/4). The k0 density has maximum Gamma(N)/[u√π Gamma(N−1/2)]; Jensen and the integral of the reciprocal2π produce Erecip<4√N/u. The beta logarithmic moment, ψ(1/2)>−2 andψ(N−1/2)≤logN give Elog|τ|>log(u/√N)−1, also for N1. The elementary endpoints of log(32/π) and the certified constants leave ARCH>.45. The monotonicity of ARCH in k extends that bound without a singular inverse moment.

The base polar satisfies the uniform Bernoulli bound p0<1/4. Since a≥4095N, p1<1/(4·8190); the quotient of magnitudes decreases with k and its endpoint N1 is also less than1. All adverse polars are controlled by.001, keeping the positive even ones. Thus W/norm²>.45−.0002−.001>.4 for ALL N≥1,k≥0,u≥64√N. It is a sign of the full real form, not an extrapolation of the constants for small N.

## 4. Scope closure

The region k≥1 has margin>.7 under u²≥256N; the region with edge k0 has margin>.4 under u²≥4096N. These are theorems uniform in all orders, not certificate campaigns. At rate31.5 the first only covers N≤3, already known, and the second adds no orders; it does not change the rest of the fixed table. The obstruction of the density cone prevents automatically transferring the positive bridge017 to these regions, without excluding other mechanisms. There is no new window T nor global sign of Paper47. Second independent reviews of the three memos agree.
