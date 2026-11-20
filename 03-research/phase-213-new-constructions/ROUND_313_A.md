# Negative sign with a growing gap and positive weights outside the gap

Fix 0<θ<1/2, A>0 and a non-exceptional frequency t of 312 in [1,2]. For each large x put L=log x and D=floor(exp(L^θ)). There exist explicit nonnegative weights v_x(n), frozen in the observation window, with v_x(1)=1 and v_x(n)=0 for 2≤n≤D. If U_x(X)=Σ_(n≤X)v_x(n)B_t(X/n), then for φ and δ=L^(−A) of 312,

    ∫ φ(u) U_x(x(1+δu)) du ≤ −c_t √x / L^(3/2).

Moreover |U_x(X)|≪_ε x^(1/2+ε) for x≤X≤2x. Unlike 312 the gap is allowed to grow, and the weights beyond it are modified. The inequality is for the full smoothed average.

**Positive filter.** Choose integers N₁,N₂ in (D,C_t D] whose phases exp(−it log N_j) are close, respectively, to exp(2πi/3) and exp(4πi/3). One can round up a real solution of each phase between 2D and 2D exp(2π/t), with angular error O_t(1/D). There are positive coefficients a,b, uniformly bounded (solving two real equations), with 1+a exp(−it log N₁)+b exp(−it log N₂)=0. Then

    P(s)=1+a√N₁ N₁^(−s)+b√N₂ N₂^(−s)

vanishes at both points 1/2±it. Take m=ceil(K log D/log L), K fixed and sufficiently large depending on θ. Define v_x by its series being equal to that of w_D of 310 multiplied by P^m. Convolution preserves positivity, the initial coefficient and the gap. For any σ>1/2 the norm of P^m on that line is (1+O_t(D^(1/2−σ)))^m=O_(t,σ)(1), so the pointwise bound follows from 310 and D=x^o(1).

**The real cut keeps its sign.** Separate the factor h_D P^m from the integrand of 312. At real s=1/2−v, 0≤v≤η=c/log D, the jump of the real branch factor contributes negative sign with the orientation of 312; the base analytic factor is positive and bounded below for large x, by continuity and the choice of t. Also Wδ is real positive, P≥1 and h_D>0. There is even a uniform floor h_D(s)≫√D/log D on that range. In the Bernoulli representation of 312, each prime D/2<p≤D intervenes only in the summand −X_p because no multiple of it other than p is ≤D. Those variables are independent of the rest; the expectation of the square dominates the sum of their variances. Each variance is ≫D^(−1/2) on the range and there are ≫D/log D primes. Integrating only 0<v<1/L on this negative cut gives a contribution of modulus ≫_t √x L^(−3/2), with the rest of the cut of the same sign.

**Control of both nonreal cuts.** By 310 on Re s=1/2 the absolute norm of h_D is O(D²), and its support is ≤D⁴. Moving v to the left loses at most D^(4v). By the vanishing of P and the inequality e^u−1≤u e^u, on each cut

    |P(1/2±it−v)| ≤ C_t v log(C_t D) exp(v log(C_t D)).

The remaining discontinuity costs O_t(v^(3/4)) by 312. Since (m+4)log(C_t D)=o(L), the additional exponential is absorbed by exp(−Lv/2). Integrating and using the factorial bound for Γ(m+7/4), both cuts together cost at most

    O_t(√x D² L^(−7/4) (C_t(m+2)log(C_tD)/L)^m).

The logarithm of the last parenthesized factor is ≤−(1−2θ+o(1))log L. Choosing K>4/(1−2θ) absorbs D² with margin. Thus the error is o(√x L^(−3/2)).

**Uniformity of the contour.** First bring the infinite contour to 1/2+1/L as in 312, now with finite polynomials for each x. Truncate at T=D. On that line the new factors cost O(D² C_t^m); the rest grows at most polynomially in L and the height. The decay (1+δ|Im s|)^(−N) of the kernel, with N fixed and sufficiently large, absorbs all of that in the tail. Use the zero-free region with edge 1/2−η. For 0≤v≤η, the polynomials cost at most D² C_t^m exp((m+4)v log(C_tD)), and this last exponential is again absorbed in x^(−v/2). The rest of the outer contour costs a fixed power of T and L, as in 312. On the left edge the gain exp(−ηL/2) dominates any fixed power of D because θ<1/2. On the horizontal edges, increasing N absorbs those powers of D. The whole outer contour is o(√x L^(−3/2)). This proves the inequality with the sign of the real cut.

The cancellation of the nonreal points is obtained through positive integer dilations larger than D, without reinserting scales neighboring the main sample. To deduce the global sign one would still need a lower bound for the balance of the other samples, and to pass from the local average to the pointwise one-sided bound required by 292.
