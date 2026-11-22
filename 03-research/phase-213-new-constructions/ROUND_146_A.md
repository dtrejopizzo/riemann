# A positive Liouville average with uniformly bounded variance

Let U(u)=e^(−u/2)L(e^u), extended by zero to u<0, and c=1.25·10^(−25). At each T=log x take the even density of mass one

    w_T(y)=Z_T^(−1) sinc(3y)^4 exp(−y²/(2cT)),     sinc(t)=sin(t)/t.

Its variance is ≤1/12 for all T and tends to 1/12 as T grows. Without assuming RH,

    ∫ w_T(y) U(T+y) dy = 1/ζ(1/2) + O(exp(−10^(−25) T)).

In particular the full average is negative for every sufficiently large scale. One can truncate to |y|≤3√c T and renormalize without changing the result. This gives a finite sum with positive weights over the Liouville terms. No numerical starting point of the asymptotic regime is given.

**Mass and dispersion.** Z_T tends by dominated convergence to ∫sinc(3y)^4dy>0. In the variable t, ∫sinc(t)^4dt=2π/3 by Parseval for the triangle function, while ∫t²sinc(t)^4dt=π/2, using sin⁴t=[4(1−cos2t)−(1−cos4t)]/8 and ∫(1−cos(kt))/t² dt=π|k|. Scaling by 3 gives variance 1/12. Multiplying by a decreasing function of y² and renormalizing can only reduce its mean (compare two independent copies); the symmetric truncation has the same property. Hence already before the limit at least 11/12 of the mass lies in |y|≤1.

**Spectral control of the average.** Write M_T(s)=∫w_T(y)e^(sy)dy. The Fourier transform of sinc(3y)^4, in angular frequency, is integrable and vanishes outside [−12,12] by convolution of four indicators. Integrating the Gaussian in the inverse representation, for large T one gets

    |M_T(σ+iτ)| ≪ √T exp((cT/2)(σ²−max(|τ|−12,0)²)).

Derivatives of any fixed order obey the same bound up to a polynomial factor in T for s in a fixed compact set, by differentiating the Gaussian exponential. M_T(0)=1 exactly.

As in 145, invert the transform R(s)=ζ(1+2s)/[(1/2+s)ζ(1/2+s)] against exp(Ts) M_T(s) on the line σ=.54, by Fourier and Fubini. Truncate at a pole-free height G between 2.99·10¹² and 3·10¹² and shift to −1/4. On the right tails and on the horizontal sides the frequency shift by 12 keeps an exponent smaller than −.01 before polynomial factors. The left edge costs O(exp(−.24T)). Every included zero is on the critical line by Z2 of paper 46 and has |γ|>14 by Z1. Its contribution is at most a fixed polynomial in T times exp(−cT(|γ|−12)²/2). The negative rate has magnitude larger than 2.5·10^(−25), so the finite sum fits in the stated error, with multiplicities allowed. The real pole contributes exactly 1/ζ(1/2).

For the physical truncation use |U(T+y)|≤exp((T+y)/2) and sinc⁴≤1. The cost outside |y|≤3√c T is ≪√T exp((1/2+c/8)T) times a normal tail whose argument is at least (3−√c/2)√T. It is O(exp(−3T)) for this c and large T. The mass removed on normalizing is likewise exponentially small.

**Scope.** 131 uses sinc⁴ to remove floor errors with an odd weight and an additive arithmetic scale. Here an even low-frequency density is applied to the logarithmic variable of the full Liouville average. The Gaussian controls the transform in the complex strip and makes the mean finite against the elementary growth of U. The bounded variance refers to the distribution of scales, not to a fixed logarithmic support; a tail out to distances proportional to T is kept in the finite version. This weight suppresses the signal not verified in the proof, so its negativity does not imply negativity for the purely Gaussian weight of 144.
