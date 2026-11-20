# Exact cost of separating the primes after the Mellin oscillation

For N=k² write the sample D_k=B_N(k) of 215 as a sum over primes, first carrying out ALL of the oscillatory integral in u. Let V_N(t) be the sum of the moduli of those contributions to B_N(t). For every real sequence t=o(N),

    lim V_N(t)^(1/N)=M_(1/2)(3)=2/(1+√(8/9))>1.

Therefore, at t=k and N=k², the procedure of bounding after integrating in the rate pays exp(c k²+o(k²)), although the complete sample is bounded by exp(O(k)) by 215. The comparison holds unconditionally and proves that the oscillation in u by itself leaves a loss of exponential-quadratic order in k. Unlike 211 (squares of individual terms before the integral), here the absolute norm of the already integrated coefficients is evaluated.

**Coefficient of a prime.** Denote m(a)=log M_a(3), a=1/2, v=m'(a), x=x_a(3)>0 and use K,θ from 212 at rate 3. For L=log p define

    I_N(L;t)=∫_[3,N] 1_{L≤2N log M₁(u)} u^(−5/2+it)c_N(L;u)du.
    V_N(t)=Σ_p (log p) exp(−L/2)|I_N(L;t)|.

For the upper bound shift the contour to height a: ∫|H_u(τ+ia)|dτ≤Cu by scaling and a/u≤1/6. Thus |c_N(L;u)|≤Cu exp(Nm(a)−L/2) by 208 and monotonicity in u. Since L≤2N log M₁(3) and Σ_(p≤X)(log p)/p≪1+log X by Chebyshev, V_N≤C(1+N)exp(Nm(a)).

**Profile of the integrated coefficient.** For L=Nv+d and d in a fixed compact, the rate u=3 lies strictly inside the cut in the inequality for L: v<v*<2log M₁(3) by 212. Change to u=3+r/N and use c_N(L;u)=(u/3)c_N(uL/3;3). On each bounded interval of r, the new argument is Nv+d+rv/3+o(1). The profile of 212, uniform in compact shifts by Gaussian domination, gives

    N^(3/2) exp(−Nm(a)+aL) 3^(−it) I_N(L;t)
        = 3^(−5/2) Re[K exp(iNθ+ixd) · 3/(v(a−ix))] + o(1).

Indeed (u/3)^(it)→1 locally because t=o(N). After normalisation, the fixed-rate envelope of 212 and the scaling above dominate the integrand by C exp(−arL/(3N)), integrable uniformly for large N. The indicator converges to one for each fixed r. Integrating the complex exponential of the profile produces the factor 3/(v(a−ix)). The error is uniform in compact d by the same argument. Although the original coefficient is complex, only its constant phase 3^(it) survives at this scale.

**Arithmetic floor.** On 0≤d≤2π/x, the modulus of the main profile exceeds a positive constant on some interval of fixed length independent of N: one can choose a subinterval around an interior maximum of the modulus, which has period π/x. On that interval, for large N, |I_N|≥c N^(−3/2)exp(Nm(a)−aL). The prime number theorem gives Σ (log p)/p≥c' on that interval of logarithms, uniformly even if it moves with N inside the compact. Indeed the multiplicative endpoints have fixed ratio >1 and θ(X)/X→1 uniformly for X≥exp(Nv). Since a=1/2, these terms of V_N add up to at least c''N^(−3/2)exp(Nm(a)). The exact rate follows.

**Which part of the integral needs cancellation.** There is a complement that does admit a sufficient absolute bound at the scale of 215. Restricting the integral to u≥U_N, 3≤U_N≤N, the same upper proof gives V_N^(high)≤C(1+N)exp(N log M_(1/2)(U_N)). If N=k² and U_N/√k→∞, then log(1+V_N^(high))=o(k) because log M_(1/2)(U_N)=O(U_N^(−2)). Thus one can, for example, remove u≥√k log(2k) before posing the prime estimate of D_k. One can also remove a fixed compact [3,U] with U<G−1 using the uniform control of 209–210 at verified rates (in that band |h_u|≤1 by 207 and Z2 with the unit margin). The growth that remains to be controlled lies at the intermediate rates. The artificial lower endpoint 3 produces the total-variation floor above; the same argument with a larger fixed endpoint has constants depending on that endpoint. The subexponential ceiling for the signed sum over those rates has not been obtained.
