# A density ceiling for integers whose squarefree part is prime

Let S(x)=Σ_{p,n≥1} log p exp(−π(pn²/x)²), with p prime and n a positive integer. Each counted integer has a unique representation of the indicated form. With a=1/ζ(1/2) and c=ξ(1/2)>0, the global sign is equivalent to the eventual ceiling

    S(x) ≤ ζ(2)x/2 + ca √x log x + O(√x).

All weights are positive. The secondary coefficient is negative. The formula does not establish unconditionally that saving with respect to the main density.

**Passage to the positive weight.** Write Q(T)=exp(−T/2)S(exp T)/c. Its bilateral transform on Re z>1, z=1/2+s, equals
    G(z) D(z),   G(z)=π^(−z/2)Γ(z/2)ζ(2z)/(2c),   D(z)=Σ_p log p/p^z.
This follows from the Mellin integral of the Gaussian by absolute convergence. Since B(z)=(z−1)G(z), one has P=(d/dT−1/2)Q with P of 152. The transform of the derivative is also justified by differentiating the Gaussians and integrating by parts in the initial strip.

**Density term.** For y→∞ the prime number theorem gives Σ_p log p exp(−π(p/y)²)~y/2 by integration by parts, with bound O(y) for all y>0 by Chebyshev. Taking y=x/n² and summing, dominated convergence by 1/n² gives S(x)/x→ζ(2)/2. Thus L=ζ(2)/(2c) is the integration constant when solving the equation for Q. Under RH, 151 gives E(T)=O(1), so 152 gives P(T)=−aT/2+O(1). Integrating from T to infinity gives

    Q(T)−L exp(T/2)=−∫₀^∞ exp(−u/2)P(T+u)du=aT+O(1).

**Why the ceiling suffices without differentiating it.** On Re z>1/2, D(z)=−ζ'(z)/ζ(z)−Σ_{p,k≥2}(log p)p^(−kz), with the second series holomorphic by normal convergence. The pole at z=1 contributes L to the transform. At any zero ρ to the right of 1/2 there remains a pole with residue −mρ G(ρ)≠0. The part T<0 of the transform of Q is entire by Gaussian decay. For Q−L exp(T/2) on T≥0 the subtraction removes the pole at z=1. If the announced ceiling holds, aT+C−Q(T)+L exp(T/2) is eventually nonnegative. Its unilateral transform is regular on the real axis s>0, by the above and the absence of real zeros of ζ in (1/2,1). Landau excludes any singularity in Re s>0. This forces RH and, by the bridge, the sign of the paper. In fact any polynomial ceiling in T for the normalized remainder also suffices. The secondary term identifies the most precise asymptotics needed under RH.

**Arithmetic truncation without scale cost.** In S(x) all n>√x can be omitted without changing the criterion. By the Chebyshev majorant O(x/n²) above, their total positive contribution is O(√x). The antecedents 107 and 152 separated prime powers. Here integration removes the sign change of the weight and the counted variable is the product of a prime and a square. The density ceiling at scale √x remains open.
