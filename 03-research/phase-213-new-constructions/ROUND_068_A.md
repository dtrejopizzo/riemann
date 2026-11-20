# One copy of each reduced product admits a lower bound at the root scale

Let S_λ be the sum of 060 multiplying the total of each reduced product r by λ^ω(r), including the diagonal r=1. The original number of slopes is 2^ω(r) and all give the same total for fixed r. For λ=1/2 exactly one copy of each product remains. For every ε>0,
    
    |S_{1/2}(x)| ≪_ε x^(1/3+ε)     (x≥1).

All orders are included and there is no cutoff on the product. The criterion of 060 corresponds to λ=1. The change of multiplicity is essential: for each 1/2<λ<1 and each θ<1, limsup S_λ(j⁴)/(j⁴)^θ=+∞.

**One copy.** For Re s>1 the transform in x with weight x^(−s)dx/x is
    
    2 M_G(2s) ∏_p (1−2λ p^(−s)/(1+p^(−2s))).

It is obtained by absolutely summing the formula of 067 over all d: the majorant product converges there. At λ=1/2 the local factor with u=p^(−s) is (1+u³)/[(1+u)(1+u²)]. Therefore the product is ζ(3s)ζ(4s)/[ζ(6s)ζ(s)]. Now use the specific profile of 059 and 062:
    
    M_G(2s)=ζ(2s)[I'(2s)−b₀ I(2s)],
    I(v)=2^(v−1) V̂(v/2) η(v/2)²,     I'(1)=b₀ I(1).

The bracket contains at least one factor η(s), also after differentiating. Dividing it by ζ(s) leaves an entire function, using η(s)/ζ(s)=1−2^(1−s). Moreover the bracket vanishes at s=1/2 by the centring and ζ(1/2) is finite and nonzero there (alternating series for η). The pole of ζ(2s) is thus eliminated. The complete transform is holomorphic on Re s>1/3: there 1/ζ(6s) has an absolutely convergent series. In each interior compact vertical strip it decreases faster than any power in height. Indeed V is smooth with compact support away from zero, its transforms V̂ and V̂' have that decay, and the zeta, eta factors and their derivatives have at most polynomial growth in those strips, away from the removed poles. Invert Mellin first on Re s>1 (inversion of the smooth profile and absolutely convergent sum), then shift to any line 1/3+ε. The stated bound results.

**Intermediate multiplicities.** For s=1+t, small t>0, divide the general product by ζ(s)^(−2λ). The quotient B_λ is holomorphic and positive at 1: the factors after removing the power of (1−p^(−s)) are 1+O(p^(−2 Re s)) uniformly near 1, using the real branch on the axis and the normally convergent product. Thus the transform is t^(2λ) times an analytic function with value 2M_G(2)B_λ(1)>0 at zero (062). If 1<2λ<2, its second derivative tends to +∞. An eventual upper bound S_λ(x)≤C x^θ, θ<1, would give a uniform upper bound for that derivative by integrating against (log x)² x^(−s)dx/x. The sum vanishes near zero. On the mesh of fourth powers the interpolation of 067 applies: the logarithmic derivative of S_λ is O_δ(x^(1+δ)), since the Euler majorant for the differentiated profile converges at 1+δ even summing over all orders. The one-sided claim is proved.

**Scope.** Counting at growing depth already appears in 043 and is not used here. The computation comes from the product of 067; the gain comes from the cyclotomic factorisation with multiplicity one and from the cancellation of a factor η before shifting the contour. One copy per product can be removed at cost o(√x) in the original representative; the rest carries multiplicities 2^ω(r)−1. The bound for it and the window T remain open. The failure for every strictly intermediate multiplicity prevents a passage by continuity of the same upper bounds between both extremes.

More precisely, if F is the transform of the one-copy case, the same shift to σ∈(1/6,1/4) gives S_{1/2}(x)=Res_{s=1/3}F(s) x^(1/3)+Res_{s=1/4}F(s) x^(1/4)+O_σ(x^σ). On Re s>1/6 the only possible remaining singularities are those two simple poles, coming from ζ(3s) and ζ(4s); a residue may vanish. Their signs need not be known.
