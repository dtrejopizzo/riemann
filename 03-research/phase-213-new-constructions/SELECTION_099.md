# A fixed binomial splitting does not reproduce the logarithmic weight with positive dilations

For 0<y<1 put K_y(t)=floor(t)−floor(yt)−floor((1−y)t), which equals zero or one. Allow any fixed probability distribution of y on (0,1) and write K for the average. There is no positive measure ν on [1,∞) with ∫K(t/u)dν(u)=log t for all t≥1 (also impossible almost everywhere).

For real s>1, Tonelli and the integration of each floor give the transform of K with respect to dt/t^(s+1) as ζ(s)A(s)/s, with A(s)=1−E[y^s+(1−y)^s]. It is strictly positive. The representation would force

    ∫ u^(−s)dν(u)=1/[s ζ(s) A(s)].

A is holomorphic on Re s>0 by local domination. On the positive half-axis A vanishes only at 1 and there its derivative is the expectation of −y log y−(1−y)log(1−y), strictly positive. Its zero cancels the pole of ζ at 1. The right side is therefore regular on the whole positive real axis (ζ does not vanish on 0<s<1 either). By Landau for the transform of a positive measure in log u, the abscissa of convergence would have to be ≤0. The transform would be holomorphic on Re s>0, incompatible even with the first critical zero of ζ: the product sζ(s)A(s) vanishes there. The argument does not assume RH.

**Local failure in the symmetric splitting.** For y=1/2 the kernel jumps by (−1)^(n−1) at n. If G(t)=ν([1,t]), the inversion of the divisor convolution forces G(t)=Σ_{n≤t}b_n log(t/n), where b_n=μ(n)+2 b_(n/2) (last term only for even n), by the Dirichlet series of the jump (1−2·2^(−s))ζ(s). Thus tG'(t)=Σ_{n≤t}b_n. The cumulative values from n=1 to 13 are 1,2,1,3,2,1,0,4,4,3,2,0,−1. The required mass is negative on (13,14). The check uses only integers up to 13.

**Limit.** The exact representation with splitting distribution independent of the scale is discarded. A majorization with sufficiently small error or a distribution that changes with the dilation is not decided here. 098 gives a quantitative loss for floors without subtractions; this kernel admits one subtraction but keeps each count nonnegative.
