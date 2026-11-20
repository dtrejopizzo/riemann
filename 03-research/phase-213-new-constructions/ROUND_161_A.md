# Two contributions of determined sign in the band of 160

With K,B,P,W,d=1/4 of 160, the part of the non-prime powers in the filtered sum equals, unconditionally,

    Σ_{p,k≥2} (log p) K(x/p^k)
       = [B(1/2)/2]√x + [B(1/3)/3]x^(1/3) + o(x^(1/3)).

Both coefficients are strictly negative. The same expansion holds on restricting to the band q>x/(K₀ log⁶x) of 160, since its o(1) error was proved in total modulus. Unlike estimating the squares by the prime number theorem, here the precision of the square-root term suffices to distinguish the cubic term.

**Complete even part.** On Re s>1 the Mellin transform of the sum over p and even k is B(s)(−ζ'/ζ)(2s)=−P(s)W(s)ζ(s+d)ζ'(2s). Hence at each zero of ζ(2s) the singularity is already removed. At 1/2 only a simple pole remains (the double pole of ζ' meets the zero of P), with residue B(1/2)/2. No poles remain at 0 or at 1−d. In any fixed vertical strip the derivatives of zeta have polynomial growth by Cauchy and the functional equation, while PW decreases faster than any power in height. Shifting to Re s=−N for fixed N gives the square-root main term with error O_N(x^(−N)), without hypotheses on the zeros. The sign follows from B(1/2)=P'(1/2)W(1/2)ζ(1/2+d)/2, with P'(1/2)>0 and ζ(3/4)<0.

**Odd part.** Let X=x^(1/3). By the prime number theorem the measure X^(−1)Σ log p δ_(p/X) converges to Lebesgue on compact intervals of (0,∞). The profile t↦K(t^(−3)) is continuous, has a finite upper end of support by 160 and extends by zero at the origin. Chebyshev controls the small end uniformly. Thus the coefficient of X is ∫K(t^(−3))dt=B(1/3)/3 by Mellin; the transform of K converges for all s by the two ends of 160. At s=1/3 the polynomial P is negative, W is positive and both real zeta factors are negative, so B(1/3)<0. For k≥5 only p^k≤exp(A)x count and K is uniformly bounded. The exponent 5 costs O(x^(1/5)) by Chebyshev; the sum of odd k≥7 costs O(x^(1/7)log x), there being O(log x) exponents. This proves the expansion.

**What remains for the sign.** In the original ceiling of order √x of 160 it suffices to work with the simple primes, whose excesses still have no proved bound at that scale. 107 and 152–154 already separated powers and 154 gave the pointwise identity of the squares. The precision O_N(x^(−N)) for the even part in this filter allows the sign of the next correction to be declared without presupposing a rate for the error in the prime number theorem. The expansion does not prove the sign of the sum over primes.
