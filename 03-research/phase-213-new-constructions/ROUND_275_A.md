# One weight for the one-sided sign in the octave and the signed residue of the band

Let L=log 2, λ=1−10^(−6). In the logarithmic coordinate take the density (1−cos(2πv/L))/L on [0,L], contract it by the factor λ keeping integral one, and convolve it with the density of uniforms of 274 contracted to [0,(1−λ)L] and normalized to mass one. Call the resulting density f, w(y)=y^(−1/2)f(log y), h=∫w(y)dy. It is positive on (1,2), with logarithmic mass H(1/2)=1. The support is still [1,2]. Its Mellin transform does not vanish for Re s>1/2 by the product formulas of 257 and 274. The convolution preserves the Gevrey-order-two derivative bounds of the second factor with fixed, possibly large, constants. Thus 274 applies to w with its own constant C.

**One-sided budget.** On the critical line put t=γL/2. The modulus of the transform is ≤|F(λt)|, with F(t)=sin(t)/[t(1−t²/π²)], by the formula of 257 and because the other factor is the transform of a probability. For v≥4.7 one has |F'(v)|≤100/v³: write F=−π² sin(v)/[v³(1−π²/v²)] and differentiate, using 1−π²/v²>0.55. For all zeros under RH, λ|t|>4.7 by the first ordinate >14. By the mean value theorem the additional cost per zero is ≤100(1−λ)/(λ³t²). The trace of 248/257 gives Σγ^(−2)<0.048 under RH (multiply the bound 0.047 for Σ|ρ|^(−2) by 1+1/(4·14²)). With the bound 0.471 of 257 one gets Σ|H(ρ)|<0.472. The explicit formula for Λ gives a spectral error ≤0.472√x plus o(√x). The contribution of the squares of primes, by the prime number theorem with the fixed weight w(u²), is (√x/2)H(1/2)+o(√x). The other proper powers are nonnegative. Hence under RH

    liminf [xh−Σ_p log(p)w(p/x)]/√x ≥ 0.028.

Conversely, the eventual sign of the numerator implies RH by Landau's argument of 257 and the absence of zeros of H in the open half-plane. Here the margin is asymptotic under RH; the finite range of 257 has not been recomputed.

**Reduction to a one-sided scalar.** Take the concrete fit R of 274 for this weight, after the lower repair and the calibration, with U=⌊√N⌋, N=⌊2x⌋. Define

    E(x)=Σ_(U/(C log²(2N))<q≤U) Λ(q) R(q).

Then RH is equivalent to: for each ε>0 there exists C_ε with E(x)≥−C_ε x^(1/2+ε) for all sufficiently large x. One side suffices; exactness is not imposed at any additional atom.

Indeed, with J(x)=ΣΛ(m)w(m/x), the exact identity is J(x)+E(x)=Σ a_(n,k)log binom(n,k), because the target is zero on the band and is reproduced at the other atoms. Calibration and Stirling give J(x)−xh=−E(x)+O(√x log³(2x)). Under RH one has J(x)−xh=O_w(√x), which proves necessity. In the converse direction, the lower bound for E gives an upper bound for J(x)−xh at every exponent σ>1/2. If there were a zero ρ to the right, choose 1/2<σ<Re ρ. The eventually nonnegative function Kx^σ−(J(x)−xh) has a Mellin transform with a pole at ρ because H(ρ)≠0, but it is analytic at all real points greater than σ: the principal pole of ζ cancels at 1 and ζ has no real zeros there. This contradicts Landau's theorem on the abscissa of convergence of a Mellin transform of eventual sign. The one-sided bound for E remains open. This equivalence allows errors at different primes of the band to compensate completely.
