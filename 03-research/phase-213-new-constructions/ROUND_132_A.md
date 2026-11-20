# A failure requires simultaneous excursions of θ and of Mertens

Write Θ=sup Reρ and M₀(z)=Σ_{d≤z}μ(d). If Θ>1/2, there exist sequences v_j,d_j→∞ such that

    log d_j / log v_j → 2,
    log |θ(v_j)−v_j| / log v_j → Θ,
    log |M₀(d_j)| / log d_j → Θ.

The maxima may occur at different points of the two bands. The relation is logarithmic; neither d_j/v_j²→1 nor a relation between signs is claimed. A size bound is obtained for the remainder in terms of the product of two local discrepancies of the true arithmetic data.

**Removing the correctors.** In 131 take r≥2 and replace w_n by w*=(T₂−I)(T₂−2I)w_n, where T₂w(t)=w(t/2)/2. The average is signed. Its moment of order s is multiplied by (2^s−1)(2^s−2); it keeps the nontrivial poles detected by w_n since 0<Reρ<1. Its moments of orders 0 and 1 vanish. It keeps oddness and Fourier support in [−B_n,B_n]. Consequently F(y)=∫w*(t)floor(yt)dt is exactly zero for y>B_n/(2π). Moreover F, yF' and (y∂_y)²F are bounded. For bounded y use F(y)=Σ_{k≥1}W(k/y), with W(s)=∫_s^∞ w*(t)dt; the two derivatives are absolutely summable by the decay of w* and of its first derivative. For large y the function is zero.

In the formula of 131 one now takes K(v)=Σ_{d≤D}μ(d)F(X/(dv)), without correctors, D=floor(X^(2/3)). The factorial estimate follows by linearity of the three dilations or by the same Stirling proof. The two endpoints are kept: F gives the lower cut, inversion in d and the absolute decay of w* give the upper one. Writing Y=X^(1/3), U=Y X^δ, the average of ψ(Xt)−Xt equals ∫_(cY,U](W(v/X)−K(v))dE+o(√X), where c>0 is fixed and small enough. The constants may depend on the fixed weights. In this band K(v) only uses d≥l=κX/U, with κ>0 fixed and small enough.

**Two-sided size bound.** Let A=1+sup_{l≤u≤z≤D}|Σ_{u<d≤z}μ(d)| and P=1+sup_{cY≤v≤U}|ψ(v)−v|. One can reduce κ so that the possible terms of the left endpoint are included. By Abel in d, |K|+|vK'|≪ A(1+log X), using the two logarithmic derivatives above to integrate the variation of each weight. W and its logarithmic derivative are bounded. On the band b=1 for X large. An integration by parts against d(ψ(v)−v), including the boundary terms, gives

    |∫_(cY,U](W(v/X)−K(v))dE| ≪ A P (1+log X)².

**Obtaining simultaneity.** Unconditionally |ψ(t)−t|+|M₀(t)|≪ε t^(Θ+ε). For Θ=1 Chebyshev and the trivial count suffice. For Θ<1, the first bound is the explicit formula of 121. For the second, in each half-plane Re s≥Θ+η and at large heights one has 1/ζ(s)≪ε,η |Im s|^ε. Indeed on discs centered at 2+it contained with margin in the zero-free region, Borel–Carathéodory gives |log ζ|≪log |t| by the polynomial growth of ζ. On a smaller disc inside Re s>1 one has O(1) by the series. Three circles gives at each intermediate radius O((log |t|)^a) with a<1. Truncated Perron at half-integers at height x² and a shift to Θ+η give the announced bound by choosing η and the height exponent small enough.

For small δ,ε>0 choose a zero with real part >Θ−ε/2 and then a fixed n detecting it, by 131. The signed average deviates in modulus by more than X^(Θ−ε) at arbitrarily large scales: an eventual ceiling of that order would give absolute convergence of its Mellin transform to the right of Θ−ε and contradict that pole. Take ε<Θ−1/2 to discard the o(√X) error. At those scales A P ≫ X^(Θ−ε)/log²X. By the general ceilings above A≪X^((2/3)(Θ+ε)) and P≪X^((1/3+δ)(Θ+ε)). Hence A≥X^((2/3)Θ−O(ε+δ)) and P≥X^((1/3)Θ−O(ε+δ)) at the same scales. A large local Möbius sum implies that at least one of its endpoints has large |M₀|. For δ,ε small enough, the proper-power term O(U^(1/2)log² U) is negligible at the peak of ψ, so that of θ is obtained. Letting δ,ε→0 and taking X arbitrarily large at each step, the two chosen points satisfy log v/log X→1/3 and log d/log X→2/3 and the two rates of the statement.

**Scope.** The general bounds for the two factors allow exactly the exponent Θ as the bands are narrowed; a joint improvement is missing. 130 already cancelled two moments in the coefficients; here they are cancelled in the average and the dependence on the global harmonic moment of μ disappears. 131 already detected poles in the prime band. The additional claim concerns the two arithmetic sums and the relation between the scales of their excursions, not only the support of a kernel.
