# Sign of the quadrature error for the inner divisor sum

Fix 0<d≤1/4 as in 155. Let b(r)=Σ_{qn²=r}Λ(q) and u=π(r/x)². The inner sum in A_d(x) is Σ_{m≥1}m^(−d)exp(−u m²). After subtracting its integral over (0,∞) and the constant ζ(d), its remainder E_d(u) is strictly positive and satisfies

    E_d(u) ≍_d min(u,1)   (u>0).

Hence on any prefix 1≤r≤Y≤x, for Y sufficiently large,

    Σ_{r≤Y} b(r) E_d(π(r/x)²) ≍_d Y³/x².

This controls the prefix error up to Y=x^(5/6) at scale √x. It also shows that the same replacement by integral plus constant loses that scale when Y/x^(5/6) grows. These are bounds for the replacement error, not for the whole centred average.

**Elementary monotonicity.** Let G(v)=Σ_{n≥1}exp(−vn²)−√π/(2√v). By Poisson, G(v)=−1/2+√(π/v)Σ_{n≥1}exp(−π²n²/v). Each variable summand has positive derivative for v<2π². For v≥2π², use the original series: G'(v)=√π/(4v^(3/2))−Σ n²exp(−vn²)>0, because the sum is ≤7exp(−v) by n²≥1+(n−1) and Σ n²exp(−(n−1))<7. On that interval 7v^(3/2)exp(−v)<√π/4. Hence G increases strictly from −1/2 to zero, with bounded derivative near zero and O(v^(−3/2)) at infinity.

**Mixture.** Write h=d/2. The difference between sum and integral is
    J_d(u)=∫₀^∞ t^(h−1)G(u+t)dt / Γ(h).
The representation follows by applying the gamma integral separately to the sum and to the integral for u>0. At u=0 the integral with G converges at both ends. Its value is ζ(d): the Mellin transform of Σ exp(−tn²) is Γ(h)ζ(2h) for h>1/2; splitting at t=1 and subtracting √π/(2√t) continues the identity to 0<h<1/2 and gives precisely the integral with G. Thus E_d=J_d−J_d(0) is increasing and tends to −ζ(d)>0 by dominated convergence. At zero it has a finite strictly positive right derivative, since G'(t) is integrated with the same weight; for 0≤u≤1 a constant near zero and O(t^(−3/2)) in the tail dominate. This proves the global comparison.

**Arithmetic sum.** One has Σ_{r≤Y}b(r)∼ζ(2)Y by the prime number theorem on ψ(Y/n²) and domination by Chebyshev. Thus Σ_{r≤Y}r²b(r)≍Y³ (for the lower bound the last interval [Y/2,Y] suffices). On the prefix considered min(π(r/x)²,1) is comparable to (r/x)². Positivity prevents internal cancellation of the error.

**Antecedents and scope.** 046 located another quadrature via variation of the derivative; 129–134 treated factorial remainders. Here the positive mixture of Gaussians also determines the direction and the lower order of the specific error of 155. The continuous term and the constant correction must stay grouped with the remainder outside the prefix: summing them separately over the whole half-line would give divergences. The centred ceiling of 155 remains open.
