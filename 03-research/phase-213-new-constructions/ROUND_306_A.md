# The sign at fixed logarithmic cutoffs detects any exterior zero

For fixed t∈[1,2], k>4 and large x, define y=x/(log x)^k. One has the equivalence

    RH ⇔ for each t∈[1,2] and each k>4 one eventually has R_t(x,y)<0.

It suffices to require it along the sequence k=4+1/n. No uniformity of the threshold in t or in n is required. If there is an exterior zero, then for almost every t and every k sufficiently close to 4 from above there are arbitrarily large x with R_t(x,y)>0. This converse adds the direction missing in the falsifier of 305. The unconditional eventual estimate at these cutoffs remains open.

**Direction under RH.** The exact transport of 305 holds over the whole band and 292 gives |B_t(v)|≪_σ v^σ for σ>1/2 (here B_t is the partial sum). The change from √x to y costs O_σ(x(log x)^(−1−k(1−σ))). Choose σ with k(1−σ)>2. At √x the asymptotic of 294 is −2D_t''(1)x/log³x, with D_t''(1)>0, where D_t is the Dirichlet series of b_t. Hence that asymptotic is preserved.

**Expansion on the moving scale.** Write z=(log x)^k, L=z^(1/k), F(z)=−L R_t(x,x/z)/(2x) for sufficiently large z, extended by zero from 1 up to that threshold. Summing the large prime first, the PNT in the two classes, with remainder of arbitrary logarithmic power and |t|≤2, replaces the two endpoints by li(x/m)−li(x/z) for each m≤z, with the factor −2 from the definition of R. The norm Σ_(m≤z)|b_t(m)|/m is O(log^4(2z)); log(x/z) is comparable to L. For each fixed integer M one obtains

    F(z)=Σ_(0≤j<M) z^(−j/k) H_j(z) + O_(M,k)(z^(−M/k)(1+log z)^(M+5)),
    H_j(z)=Σ_(m≤z) b_t(m)[P_j(log m)/m−P_j(log z)/z],
    P_j(u)=Σ_(r=0)^j (j!/r!) u^r.

Indeed expand L li(x/m)/x in 1/L uniformly for log m≤log z, and similarly at the endpoint z. The polynomial satisfies P_j−P_j'=u^j. In particular H₀ is the profile J of the respective frequency. The expansion is of the signed function, before taking signs.

**Mellin and detection.** With transform ∫₁^∞ f(z) z^(−1−s) dz one has exactly

    Mellin(H_j)(s) = (−∂_s)^j [D_t(1+s)/(1+s)] / s.

Indeed H_j(1)=0, its derivative between integers is B_t(z)(log z)^j/z² and it is continuous at each integer. Integrate by parts, initially in Re s>0. Thus each correction shifts its singularities to the left by j/k. The above expansion continues the Mellin transform of F meromorphically to Re s>max(−M/k,−1/2); the compact modification only adds an entire function. At the real points s>−2/k it is regular: D_t is regular on the real axis of that region and its double zero at 1 makes the denominators s+j/k removable for j=0,1. For j≥2 those points are already outside the interval.

Given an exterior zero ρ of ζ, choose t such that D_t has a pole at ρ; by 292 this holds for almost every t. Choose k>4 with Re ρ−1>−2/k and M>k/2. Among the points ρ+j/k, j a nonnegative integer, that are poles of D_t, take the rightmost one, w (the series is holomorphic to the right of 1). At s=w−1, not real, the Mellin transform of H₀ has a pole. All corrections are regular there by the choice of w. Consequently F has a Mellin transform with a nonreal singularity to the right of −2/k, despite being regular at all real points of that range. If F were eventually of fixed sign, Landau, applied after discarding a compact set, would force the Mellin transform to converge and be holomorphic on that whole half-plane. The contradiction proves both oscillations. Even subtracting from F a constant times z^(−2/k) preserves the argument, since the added real pole lies on the boundary. This avoids confusing a tiny crossing of H₀ with the effective sign change in the arithmetic partial sum.

**Row zero.** The same argument at t=0 uses the order-four zero of D₀ at 1 and the negative term of order x/L⁵ of 302. It detects each effective pole w of D₀ with Re w>1−4/k for k>8; a zero shared and cancelled with L may be invisible in that row. The band [1,2] in the main statement avoids that caveat.
