# A prime band around the cube root

For each fixed δ>0 it suffices to control a family of centered integrals with v exclusively in [c X^(1/3), X^(1/3+δ)]. The lower cut has exact cancellation of the factorial kernel. The discrete average of 127 is replaced by continuous averages that jointly detect any pole. The internal arithmetic term still contains Möbius coefficients up to 4X^(2/3).

**Averages.** Take an integer r with (1+2r)δ>1/2 and for positive integer n use w_n(t)=(sin⁴ t/t³) sinc(t/n)^(2r), sinc(u)=sin(u)/u, on t>0. It is positive except for isolated zeros. Its odd extension to the line is entire, L¹ and of exponential type B_n=4+2r/n; by Paley–Wiener its Fourier transform is supported in [−B_n,B_n]. By the sine series of the periodic function {u}−1/2, using Abel summation and dominated convergence, ∫₀∞ w_n(t)({yt}−1/2)dt=0 for 2πy>B_n. The values at the jumps are irrelevant.

The moments G_n(s)=∫w_n(t)t^s dt converge, as n→∞, for each 0<Re s<2 to the corresponding moment of sin⁴t/t³. With α=2−s, the latter equals [4·2^α−4^α]π/[16Γ(1+α)sin(πα/2)] by the integral of (1−cos t)t^(−1−α). It does not vanish in that strip. Consequently each relevant zero survives for some fixed n, without requiring a given n to keep all of them.

**Factorial cost.** Set D=floor(X^(2/3)) and use the two correctors of 130. Write K(v)=Σ c_d ∫w_n(t)floor(Xt/(dv))dt, W(v)=∫_{v/X}∞ w_n(t)dt, with dE=dψ−b(v)dv of 129. For Y=X/d large one has

    ∫ w_n(t) [∫floor(Yt/v)dE(v)]dt = O_n,r(1/Y).

For t≥3/Y use the calibrated expansion of 129 (increase 3 by a constant if needed); ∫w_n(t)/t dt is finite. The small interval costs O(Y⁻²) by bounding the original factorial discrepancy for bounded Yt, since w_n(t)=O(t). Extending the sawtooth term with log(Yt) to that interval also costs O(Y⁻²) by the change u=Yt. The part with log Y disappears exactly by the Fourier support. For the part with log t integrate by parts against the bounded primitive, of size O(1/Y), of the periodic sawtooth. The derivative of w_n(t)log t is in L¹, and the boundary terms vanish. Thus ∫K dE=O(D² log(2D)/X)=o(√X) by the ℓ¹ bound of 130.

**Both endpoints.** For v≤cX^(1/3) choose c>0 so small that 2πX/(4Dv)>B_n (it can be chosen uniform in n). The mean of the floor is exactly X/(dv) times the moment ∫tw_n minus (1/2)∫w_n, that is, an affine function of 1/d. Both coefficient sums vanish, hence K(v)=0. W is bounded and its absolute cost up to that cut is O(X^(1/3)) by Chebyshev. Above X^(1/3+δ), inversion gives W_t=K_t for t≤X^δ/2 and X large, since Xt/v<D. For t>X^δ/2 the absolute cost over all v of W_t plus the floors with the absolute values of the coefficients is O(Xt log(2+Xt)log(2D)): use Chebyshev, the factorial identity and ∫_a∞floor(y/v)dv≪y log(2+y), with Σ|c_d|/d≪log(2D). Integrating w_n(t)≪_{n,r}t^(−3−2r) gives o(√X) by the choice of r. By Fubini

    ∫ w_n(t)[ψ(Xt)−Xt]dt = ∫_{cX^(1/3)<v≤X^(1/3+δ)} (W−K)dE + o(√X).

Changing from b to density one in the W term costs O(1).

**Pending criterion.** For each n it would suffice that the arithmetic right-hand side be bounded above by O_{n,ε}(X^(1/2+ε)) for all ε>0. Under RH this holds by PNT with root-log² error. Conversely apply Landau as in 127: truncating ψ(x)−x to x≥1 before averaging costs O(X⁻²) for large X; in 1<Re s<2 the two-sided Mellin transform in X of the truncated average is G_n(s) times the Mellin transform of that discrepancy. The part X<1 of the average is O_n(X²) by the decay of w_n and Chebyshev, so removing that part subtracts a function holomorphic in Re s<2. Every pole to the right of 1/2 survives for some n, and the transform is regular on the positive real axis of the strip. The one-sided bound excludes such a pole. That ceiling has not been proved.

**Cross-check.** R155_005/006 already use sinc⁴ and B-splines; 045 and 047 use Poisson in quadratures. The additional application is an exact affine identity for the mean of each floor over a whole interval, together with the Mellin transfer and the upper cut for the same averages. The weight differs from 127 and the criterion of this memo uses tolerance.
