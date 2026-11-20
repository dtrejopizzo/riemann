# The masses of the true primes between fourth powers keep the rate

For the block of 121 replace f(v)=c_F(log v)/√v by f(m⁴) on each cell [m⁴,(m+1)⁴), both in the prime sum and in the integral. The rate Δ of the positive excess is preserved for the spaces of 122. Hence the prime mass weighted by log p in each cell suffices (for the two edges its intersection with the block is used). Unlike 123 this uses the explicit formula for the primes. The model of 124 explains why positivity and masses, without the arithmetic relation with the zeros, did not give the same comparison. The sign still requires proving the subexponential ceiling of the rounded matrix.

**Local estimate.** Let Θ=1/2+Δ. On a band [R,2R] intersected with the block, set q(v)=f(v)−f(m⁴) inside and zero outside. With F unit and ||F'||≤B we have |q|≤A=C(1+B)R^(−3/4), J=ceil(C R^(1/4)) jumps including endpoints, piecewise derivative in y=log(v/R) bounded by C A J. This follows from |c'|≤B. The total variation is O(AJ). We claim

    |∫ q(v)(dψ(v)−dv)| ≪ (1+log R)^C R^Θ A √J + O(AJ(1+log R)^C).

Use the explicit formula for ψ truncated at height H comparable to R², with uniform error O(log^C R) on [R,2R]. This is the classical version with the term for proximity to the nearest prime power bounded by O(log R) (for the other integers one sums the harmonic series); one can take a good height in [R²,2R²]. Changing the half-jump convention costs O(log R). Integrating by parts against q, the remainder costs O(AJ log^C R); this includes edge assignments, since each jump of ψ is ≤log(2R). The smooth part of the truncated formula gives integrals R^ρ M(ρ), where

    M(s)=∫ q(R exp y)exp(sy)dy.

**Sum up to H.** For −1≤σ≤2, w(y)=q(R exp y)exp(σy) has support of bounded length, amplitude O(A) and the same piecewise derivative bound. Hence for 0<h≤1,
    
    ||w(·+h)−w||₂² ≪ A² min(1,Jh).

On the set crossing jumps use its length O(Jh); outside use the derivative and, for Jh≤1, (Jh)²≤Jh. At heights L≤|t|≤2L, L≥2, Plancherel with h=1/L gives ∫|M(σ+it)|²dt ≪ A² min(1,J/L), since |exp(ith)−1| is bounded away from zero. This also holds on the band widened by distance 1/4, changing the constant. By subharmonicity of |M|² on discs of radius 1/4 around each zero and local multiplicity O(log(2L)), the sum of |M(ρ)|² over the band is ≪ log(2L) A² min(1,J/L). Cauchy–Schwarz with O(L log(2L)) zeros gives a sum of moduli ≪ A log(2L)√J. Summing the bands up to H gives the local claim. The factor R^ρ was pulled out before sampling, which allows using R^Θ without widening the exponent.

**Application.** Changing from ψ to primes costs O(A√R log² R) from the proper powers. The arithmetic comparison of quadratic forms per band is thus O((1+B) log^C(2R) (1+R^(Δ−1/8))). Summing dyadically up to X gives in norm O((1+B)log^(C+1)(2X)(1+X^(Δ−1/8))). The factor 1+B is subpolynomial in X for the spaces of 122. If Δ>0, the rate of the error is strictly below Δ; if Δ=0, the error is subexponential in T. The variational inequality for the largest eigenvalue and 121–122 prove the announced preservation without assuming RH. The dependence of the intermediate bound on Θ is not a numerical estimate of its value.

**Antecedents and scope.** 121 already uses the explicit formula to discard small primes; 123 interpolates with two moments; 124 keeps masses of a general measure. Here the saving 1/8 comes from summing the transforms of the discontinuous error over the zeros using the number of jumps and Plancherel. No estimate of the sign of the remaining part has been obtained.
