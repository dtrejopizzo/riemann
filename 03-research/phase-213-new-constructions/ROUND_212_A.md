# Stability threshold of the prime cut at linear scale

In 208 the height-1 contour gives the cut log X=2N log M₁. In 211 the boundary obstruction at scale √N was subexponential, invisible in the N-th root of 210. Here, even at the verified rates 3≤u≤4, certain cuts produce a spurious EXPONENTIAL growth in N. The stability threshold against bounded shifts of the endpoint is identified. The following claims are at fixed rate u.

Write l(a)=log M_a(u), v(a)=l'(a), F(a)=l(a)−(a−1/2)v(a). There is a unique a* in (1/2,1) with F(a*)=0. Indeed l is strictly convex and its series in a² has positive coefficients in all positive degrees: l'(a)=(1/√(1−4a²/u²)−1)/a. Thus F(1/2)>0, F(1)<0 (each monomial a^(2k) contributes at 1 with factor 1−k), and F'=(1/2−a)l''. Set v*=v(a*). It is the minimum of l(a)/(a−1/2) over 1/2<a≤1 and is strictly less than 2 log M₁. For any u≥3 the cut Nv*+O_u(1) preserves the whole infinite prime sum with error O_u(1/√N); for larger slopes the error is exponentially small. This improves the fixed-rate cut of the criterion of 208–209.

**Profile at the boundary.** For 0<a≤1 let x_a>0 be the positive maximum point of |H(x+ia)| given by 208. The two maxima ±x_a are strictly quadratic: the maximum in q of the rational fraction of 208 has negative second derivative and dq/dx=2x_a≠0. Write h=log H locally at x_a+ia. By Cauchy–Riemann and the maximum-point equation, h'=−i v(a); Re h''<0. For each fixed real d, inversion on the contour and expansion in (x−x_a)√N give

    √N exp(−Nl(a)+a(Nv+d)) c_N(Nv+d;u)
        = Re[K exp(iNθ+ix_a d)] + o(1),
    K=√(2/π)/√(−h''),   θ=arg H(x_a+ia)+x_a v.

The root with positive real part is taken. In each neighbourhood a Gaussian dominates after rescaling and the linear terms of order √N cancel. The other peak contributes the conjugate by symmetry; the complement is exponentially smaller by integrability and separation of both maxima. The same absolute contour bound with factor 1+|x+ia| gives, for N≥3 and t≥0,

    |c_N(t;u)|+|c'_N(t;u)| ≤ C_(a,u) exp(Nl(a)−at)/√N.

In particular Chebyshev and partial summation in the tail with a=a*>1/2 prove the cut claim above.

**The endpoint generates a prime signal.** Fix L=Nv(a)+c with c constant. For a<1/2 take B the prime sum up to exp L; for a>1/2 take B the strictly later tail. Substitute dθₚ(x) by dx (θₚ is the Chebyshev function) in the weight x^(−1/2)c_N(log x;u). After multiplying by √N exp(−Nl(a)−(1/2−a)L), the boundary error is o(1) by PNT and the contour bound. The integral of the error by parts is dominated in r=|log x−L| by C exp(−|a−1/2|r)|θₚ(x)/x−1|, with x≥1; it converges to zero by domination. For dx use the profile above with d=c±r and the same majorant without the PNT error. The result is

    √N exp(−Nl(a)−(1/2−a)L) B
      = Re[K exp(iNθ+ix_a c) J]+o(1),

with J=1/(1/2−a+ix_a) for the initial sum and J=1/(a−1/2−ix_a) for the tail. KJ≠0. Between the two endpoints c=0 and c=π/(2x_a), at least one gives, for each sufficiently large N, a modulus ≥C exp(NF(a))/√N, by the two phases in quadrature.

**Consequence and caveat.** In 3≤u≤4 the complete sum is o(1) by 209 and its tail proof. Hence, for each slope v in (0,v*) except v(1/2), at least one of those two initial cuts has modulus exponential in N, with exponent F(a)>0, where v=l'(a). For a>1/2 the tail is subtracted from the total. Therefore no slope strictly below v* guarantees stability for ALL cuts of slope at most v* lying above it: there are always intermediate slopes that fail. For the exact slope v(1/2) the domination argument loses the decay in r and does not decide. Nor is a lower bound deduced for each individual phase. The spurious growth already appears with the verified local zeros; it cannot be used as an indicator of failure of the sign. The upper estimate of the complete sum remains open.
