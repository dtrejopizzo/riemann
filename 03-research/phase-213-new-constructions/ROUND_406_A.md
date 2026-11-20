# A positive average suppresses all residues in an explicit window

**Status: PROVED, with independent review of the theta normalization, the window and the conclusion at frozen cut.**

Freeze z=L², x=exp L, and set S_z(u)=S^*(exp u;z). Let Φ be the bilateral theta kernel of ξ, normalized by ∫Φ(v)exp((s−1/2)v)dv=ξ(s). Then, unconditionally, with B=(log L)/2,

    ∫_{−B}^B Φ(v)exp(−v/2) S_z(L+v) dv ∼ −ξ(1/2) T₀(x).

In particular in each interval [x/√log x,x√log x] there is a scale t with S^*(t;z)≤−c T₀(x)L^(−1/4), with c absolute and positive. The cut in that conclusion is the z of the center. 365 annihilated finite systems of frequencies with discrete measures depending on the system. Here the classical kernel is fixed, the arithmetic integrand is the pulse of 368 and both the window and the floor are quantified. No novelty is attributed to the theta representation of ξ.

**Kernel and sign.** For v≥0 use Φ(v)=Σ_n (4π² n⁴ exp(9v/2)−6π n² exp(5v/2))exp(−πn² exp(2v)), n≥1; extend by parity. All its terms are positive on v≥0. Theta inversion gives the same bilateral series (for v<0 understood by summing before integrating). The term-by-term Mellin integral on Re s>1 is justified in that band for the two separate sums by the convergence of ζ(Re s); the change r=πn²exp(2v) gives ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2. The kernel has tail O(exp(5|v|−πexp(2|v|))). The expression for ξ extends by analyticity.

**Complete average.** In the initial Gaussian inversion on 1+1/L one can integrate in v by absolute convergence. The remaining factor after averaging is F(s)ξ(s)=s(s−1)π^(−s/2)Γ(s/2)/2, regular on the whole band α≤Re s≤1+1/L and negative at s=1/2. Now the whole contour is moved to α without residues. The gamma factor by Stirling has at most polynomial growth in that band, and is regular near the saddle. The local domination and the phase loss of 367, together with the Gaussian tail, give the equivalent exp(K(α))ξ(1/2)/(ζ(1/2)√(2πK''(α)))=−ξ(1/2)T₀. Thus the residues of higher order are also annihilated, by exact cancellation before shifting the contour.

**Effective window.** Uniformly in z, |S_z(L+v)|≪x exp v by the dyadic count in the Gaussian. After normalizing by exp(−v/2), the cost of |v|>B is ≤x exp(−πL+O(log L)), negligible relative to T₀. On [−B,B] the positive measure Φ(v)dv has mass ≤ξ(1/2). Some v satisfies exp(−v/2)S_z(L+v)≤−(1−o(1))T₀ and exp(v/2)≥L^(−1/4), which gives the floor. The average loses sensitivity to the zeros precisely because the multiplier vanishes at all of them. Recovering the sign at the center, or with a moving cut equal to that of each scale, remains open.

**Review record.** Set θ(t)=1+2Σ_{n≥1}exp(−πn²t). The series of the kernel is2t^(9/4)θ''(t)+3t^(5/4)θ'(t), t=exp(2v); differentiating θ(t)=t^(−1/2)θ(1/t) shows that this expression is invariant under t↦1/t, justifying the even extension and the same series for negative v. With r=πn²exp(2v), its bilateral Mellin transform for Re s>1 is exactly π^(−s/2)ζ(s)[2Γ(s/2+2)−3Γ(s/2+1)]=ξ(s). No factor2 is missing: the positive integral over v≥0 would be half the bilateral one when using cosh. In particular ∫Φ=ξ(1/2)>0.

The remaining multiplier Fξ is regular on the whole shifted strip and negative at the saddle; its gamma factor introduces no poles there. The cancellation of the zeros is carried out analytically before moving the contour, including multiple orders. On the tail |v|>B, exp(2B)=L and the absolute cost is x exp(−πL+O(log L)), using the uniform ceilingCe^(L+v); no square-root ceiling forS is used. Finally dividing the negative average by the positive mass of the window and using exp(v/2)≥L^(−1/4) gives the pointwise claim with the same frozenz, without replacing it by(log t)².
