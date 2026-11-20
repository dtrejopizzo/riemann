# A certified degree interval inside a criterion that detects all zeros

Fix c=1.25·10^(−25), W=cT and Y centred normal of variance W. For real polynomials normalized by E[P(Y/√W)²]=1, form the quadratic

    Q_T(P)=E[P(Y/√W)² U(T+Y)],    U(t)=exp(−t/2)L(exp t).

Without RH, uniformly over ALL polynomials of degree ≤floor(cT), one has Q_T(P)=1/ζ(1/2)+O(exp(−10^(−24)T)). In particular the whole matrix of this quadratic is negative definite for sufficiently large T, with uniform margin. In turn, the global sign is equivalent to the subexponential ceiling of the positive part of the largest quotient, for each fixed degree slope κ>0 (degree ≤κT). If there is an off-line zero, some fixed slope admits exponentially large positive quotients at every sufficiently large scale.

**Certified interval.** In the orthonormal probabilists' Hermite basis the derivative lowers the degree and has norm ≤√d in degree ≤d. Translating by complex h is exponentiating h∂, of norm ≤exp(|h|√d) from that space to itself. The multiplier on the contour of 145 is

    E[P(Y/√W)² e^{sY}]=exp(Ws²/2) E[P(Z+s√W)²],    Z standard normal.

The identity holds for real s by change of mean and then by entire continuation. The modulus bound for the integrand, without R(s), has rate per T at most σ+c(σ²−τ²)/2+2c|s| if d≤cT. On the right line σ=.54, above height 2.99·10¹² the rate is <−.01; the same on the horizontals of the rectangle of 145. On the left side σ=−1/4 it is <−.24, even maximizing in τ. At the included zeros σ=0 and |τ|>14, the rate is ≤c(−14²/2+28)=−70c. Surround each one by a small fixed disjoint circle where the rate stays <−2·10^(−24); this allows arbitrary multiplicities with constants independent of P,d,T. The real residue at zero is a=1/ζ(1/2) by normalization. The uniform estimate follows by the same finite contour. The height verification used is Z2 of P47.

**Why larger slopes matter.** Under RH, |U(t)|≪ε exp(εt) for t≥0 and U=0 for t<0. The above translation at s=ε gives |Q_T(P)|≪ε exp(T[ε+cε²/2+2ε√(cκ)]) when d≤κT. For each κ this gives upper exponential rate zero using log(1+|Q|).

If there is a pole z=b+iγ with b>0, modulate the Gaussian by exp(−iτY), with τ fixed close to γ. In the finite rectangle of 142 the multiplier is exp(Ts+W(s−iτ)²/2); centring the frequency gives a strictly positive maximum rate. Choose τ generic in the open set to have a unique maximum: for poles of equal ordinate the rate grows with b in the strip used, and for distinct ordinates there is only one tie per pair. The contours are chosen after τ, including the maximizers and at a distance from the poles. The left edge is negative and the right tails become negligible at a sufficiently large finite height. The leading coefficient for a multiple pole contains (1+c(z−iτ))^(m−1)≠0. Hence the modulus of E[U(T+Y)exp(−iτY)] exceeds exp(ηT) for some η>0 at every large T. Choose a phase depending on T and use that E U(T+Y)→a: the weight 1+cos(τY+phase)=2cos²((τY+phase)/2) gives a positive quadratic of exponential size.

Approximate that cosine by its Taylor expansion at y=0 up to d=floor(κT), keeping the phase in the coefficients. The real pointwise error is ≤(|τy|/2)^(d+1)/(d+1)!. For n=d+1, the L² norm of this error in the measure exp(y/2)φ_W(y)dy is ≤exp(W/16)[C|τ|(W+√(Wn))/n]^n by tilting the normal, the Gaussian moment bound and Stirling. The same without tilting. With κ large enough depending on τ,c the error is O(exp(−2T)) in both norms. By Cauchy–Schwarz and |U(T+y)|≤exp((T+y)/2), replacing the cosine by the polynomial costs o(1) in the quadratic, also taking into account that the norm of the cosine in the tilted measure is ≤exp(W/16). The ordinary Gaussian norm of the polynomial is bounded and it is nonzero by the positive signal. After normalizing a positive rate is kept. This proves the equivalence, without claiming that all degrees have negative sign under RH.

**Why approximating the short weight directly was not enough.** In L² of the standard normal, the square root of the ratio of the short and wide Gaussian densities is g(t)=q^(1/4)exp(−(q−1)t²/4), q=W/V, V=j log(j+2) of 144. Its coefficient of degree 2k is

    q^(1/4)((q+1)/2)^(−1/2) [−(q−1)/(q+1)]^k √((2k)!)/(2^k k!).

It is obtained by integrating the generating function exp(tz−z²/2). For d=O(T) the first omitted even coefficient has modulus ≥exp(−O(V+log T)); this is a lower bound for the L² error. It does not justify a precision exp(−δT) with fixed δ>0 to transfer the sign via the elementary bound on U. The fixed-frequency modulation is what makes the preceding proof work.

**Cross-check and scope.** 115/122 already detect poles by modulation or by growing spaces for the Weil form. 145 certified the constant (P=1) of the Liouville mean. Here the uniform bound on a linear interval of degrees for this arithmetic quadratic and detection by some larger slope if the sign fails are verified together. The pending part is a subexponential ceiling for all fixed slopes; certifying this interval does not prove it.
