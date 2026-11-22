# Strict positivity of the full form up to T=21/10

For 0<T≤21/10 and every f in the domain of the full form of paper 46,
    W_T(f) ≥ exp(−32000000001)||f||₂².
Use Z1–Z3 as in 175, in particular the already verified height G=3·10¹². Both parities and the two polar moments are kept. RH is not postulated. We give the parameters and the scalar certificate to avoid extrapolating the asymptotic law of 177.

**The compressed comb.** Prove only the endpoint T=21/10. Use U=log 9, R=1500000, k=16, even m=1200000000, H=240000000000 and N=10¹⁰. With u=1−sinc^(2k)(τ/H), g defined by ĝ=u^(m/2)f̂ is supported in [−2.18,2.18] inside [−U,U]. In the Schur quotient of 081/177 put x=exp(t); by symmetry 1≤x≤9 suffices. The normalized row is
    [xL(9x)+ψ(9x)+L(9/x)+xψ(9/x)]/(1+x).
Between jump points it is a monotone or constant linear fractional function. At the point itself the inclusive convention in the two sums gives a majorant of both limits, by positivity of the summands. The set of points to be checked is {1,9} and q/9,9/q inside [1,9] for all prime powers q≤81. The attached proof enumerates the primes by integer division, the powers by multiplication and the endpoints as exact fractions. At each endpoint the interval evaluation gives <12. By Schur, ||Π_U||≤12. Thus m_arch−12≥1/3 outside [−R,R] by the explicit lower bound of the paper for the digamma; on the whole line the bracket is ≥−18.

**Floor for the filter.** In the leakage proof of 175 take Ω=2R and n=63000000=10ΩT, keeping the coefficient 256^n for the interpolation. The remainder √(Ω/π)(3eΩT/n)^n is <1/(4√T), and 256^(−2n)/64≥η=exp(−230TR). The projection argument gives this same lower bound for the fraction of Fourier mass of f outside [−2R,2R]. With a=kR²/(3H²), u≤a on |τ|≤R and u≥2a for |τ|≥2R by the inequalities of 175 for k=16. In the archimedean term minus the comb reserve half of the bracket on |τ|>G/2. The remaining part integrated against u^m|f̂|²/(2π) gives at least
    a^m(2^mη/6−18)||f||² > 3a^m ||f||²,
since m log2−230TR>10. One has a^m>exp(−32000000000).

**Pole.** A(g) and B(g) are those of f multiplied by u(i/2)^(m/2). For v=1/(2H), sinh(v)/v≤exp(v²) by the series, so |u(i/2)|≤exp(2kv²)−1≤4kv²=k/H²<a/2. By Cauchy–Schwarz 2|A(f)B(f)|≤4exp(T)||f||². Hence the polar cost is less than a^m||f||².

**Tail.** For the projected extension μ of 172 use χ as in 175, changing the indicator to [−7,7]. It is one at least up to |t|=5.5>2U, so W_T(f)=W_U(g)+∫(1−u^m)|f̂|²dμ as in 177. The prefactor for the correction of a zero before (1+|s|)^(−2)min(1,N/|s|)^N is ≤2·14·exp(8.5/2)·25/(2π)<10⁵. The ceilings 10⁹log(3+|τ|) remain valid and, for |τ|≤G/2, the additional factor 100^(−N), which now leaves |C|<exp(−32000000002). On |τ|>G/2 the masked correcting density has modulus <1/1000 by (1−u^m)≤m(H/|τ|)^(2k); the same majorant for the mask is <1/2. The bracket reserve is at least (1/6)(1/2)/(2π)=1/(24π) per unit of |f̂|²dτ. It absorbs the whole high correction. The retained atoms of μ have nonnegative weight. At low frequencies the cost in units of ||f||² is ≤2π exp(−32000000002)<a^m. Adding the floor and the polar bound proves, with margin to spare, the announced inequality. Density of the smooth core and inclusion of supports give the complete result.

**Reproduction and scope.** Run python3 verify_178.py with python-flint; it uses Arb balls at 192 bits. The functional inequalities come from the arguments of 172–177, not from sampling the form. The asymptotic norm of 177 is preceded by 081; here the exact row is used and not the asymptotic approximation. The previously certified window in this phase was 6/5 in 175. No uniform margin for all windows is known.
