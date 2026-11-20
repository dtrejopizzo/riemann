# A multiplicative countermodel preserves the signs and all polynomial savings

Fix any window 0<a<log 4 and any initial cut P₀. There is a real multiplicative function f that coincides with μ on n≤P₀, has exactly the same signs and zeros on all integers, and satisfies the every-power savings of round 329 with its own coefficients. However, for the energy defined as in 325 replacing μ by f,

    limsup E_(m,f)[exp(−am)]^(1/(2m)) > 1.

Hence one cannot climb from all the savings of fixed order to the exponential target by invoking only multiplicativity, the exact pattern of signs and zeros, or the data of an arbitrary initial table.

**Construction.** Choose 0<δ<min(1/4,exp(−a/2)−1/2). For some P≥P₀ put

    f(n)=μ(n) ∏_(p|n; p>P) (1−p^(−δ)).

At the primes the maximal perturbation is ≤P^(−δ) and its harmonic norm is ≤Σ_(n>P)n^(−1−δ), both arbitrarily small. Even outside the table the support and the parity that determines each sign are preserved. In every large block [Y,2Y], Σ|f(n)|≫Y on choosing P large enough: the loss relative to μ² is bounded by Σ_(p>P)p^(−δ)⌊2Y/p⌋, while there are asymptotically Y/ζ(2) squarefree integers.

**The exponentially growing defect.** For Re s>1 the series of f is ζ(s)^(−1) times the product of 1+p^(−δ)p^(−s)/(1−p^(−s)) over p>P. Extract ζ(s+δ) from the product. At s=β=1−δ there remains a locally holomorphic nonvanishing correction: the first-degree terms cancel for p>P, the errors cost O(p^(−2Re s−δ)+p^(−2Re s−2δ)), and the adjusted small factors are units at β. Since ζ(β) is finite and nonzero, the continued series has a simple pole at β. Repeat the Taylor radius proof of 326 for the centers 3/2+it on an interval around zero: the density of heights there is ≫exp(−am). Hence the rate is at least exp(−a/2)/(1/2+δ)>1, with no hypothesis on ζ. It is not claimed that the series of the true μ has that pole.

**Why the interval estimates survive.** Write f=μ*k, with k multiplicative nonnegative, k(p^e)=p^(−δ) for p>P and e≥1, and zero on powers of the other primes. The previous product gives Σ k(d)/d^(1−δ/2)<∞. In the central blocks [Y,2Y] of 329, for each fixed a' in (0,log 4], h=exp(−a'm)m^b and fixed b, take H=ceil(4hY). There H≥Y^0.22 for large m. After opening the convolution, for d≤Y^ν with fixed ν>0 small enough, the length H/d still exceeds (Y/d)^(1/6+ε) with fixed margin. The maximum of a sum of μ over subintervals of ((x−H)/d,x/d] has mean over x∈[Y,2Y] bounded by O_A((H/d)(log Y)^(−A)), by the scalar result cited in 329 and the trivial bound on the exceptional set. The constants are uniform in those d; the change of scale multiplies the length of the exceptional set by d. Summing with k(d)/H costs O_A((log Y)^(−A)).

For d>Y^ν use moduli and Fubini: the average over x of the number of multiples of d in (x−H,x] is ≤(H/Y)⌊2Y/d⌋≤2H/d. The normalized tail costs O(Y^(−νδ/2)). Thus the normalized maximum for f has L¹ mean with a saving of every power of log Y. Since |f|≤1, its second moment also has that saving. The partial summation and the gamma tails of 329 go through unchanged, giving

    E_(m,f)[h]=Δ_(m,f)+O_(A,a',b,δ,P)(h binom(2m,m)m^(−A))

for each fixed A. For a'<log 4 the absolute mass is still ≫ h4^m/m by the weighted occupation argument of 326 and Σ_[Y,2Y]|f(n)|≫Y; the diagonal costs O(m^(−1/2)). Hence also E_(m,f)/P_(m,f) decreases faster than each fixed inverse power. The interval input is the same scalar theorem already used. [Source, §1.1](https://arxiv.org/html/2411.05770v1)

**Consequence for the route.** This obstruction operates even if all the sign products of pairs are preserved. To exclude it one must use information on the exact function, for example that the Euler factor is exactly 1−p^(−s) at each prime and not only a harmonically small approximation to it. The countermodel does not prevent a specific estimate of those factors from closing the sign.

**Size of the defect in the inversion identity.** For the previous countermodel let D(n)=Σ_{d|n}f(d), β=1−δ. For μ this observable is exactly zero for n>1. Here D is multiplicative, with D(p^k)=p^(−δ) for p>P and k≥1, and D(p^k)=0 for p≤P. For each β/2<σ<β one gets

    Σ_{n≤X}D(n) = C_P X^β/β + O_(P,δ,σ)(X^σ),   C_P>0.

Indeed, the series of D is ζ(s+δ)U(s). With x=p^(−s), y=p^(−δ), the factor of U is 1−yx for p≤P and 1+(y−y²)x²/(1−x) for p>P. The coefficients u of U are absolutely summable with weight n^(−σ) since 2σ+δ>1. Convolve with n^(−δ) and use Σ_{k≤v}k^(−δ)=v^β/β+O_δ(1) for v≥1. Both the partial sum of |u| in the error and the tail when completing U(β) cost O(X^σ) after including their respective weights. Thus C_P=U(β). The small factors at β give exactly ∏_{p≤P}(1−1/p); the product of the large ones tends to one by absolute convergence. In particular C_P is asymptotic to e^(−γ)/log P as P→∞ at fixed δ by Mertens' product. The estimate in X is for fixed P.

This formula distinguishes the countermodel by an elementary divisor sum and measures how much a long initial table hides it. For μ the defect vanishes identically; an inequality exploiting that vanishing in the pair energy of 326 remains pending.
