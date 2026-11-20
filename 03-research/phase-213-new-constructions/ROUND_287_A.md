# For ordinary Möbius increments it suffices to control one direction

Let C(X)→∞ as slowly as desired, with log C(X)=o(log X), and let

    D₊(X)=max_(X≤u≤v≤XC(X)) [M(v)−M(u)],
    D₋(X)=max_(X≤u≤v≤XC(X)) [M(u)−M(v)].

For each of the two directions separately,

    lim log(1+D_±(X)²/X)/log X = 2Θ−1.

In particular it suffices to find arbitrarily distant bands in which the excess of squarefree integers with an even number of prime factors over those with an odd number does not exceed X^(1/2+o(1)) on any subinterval. One may also choose the opposite excess from the start. Here the initial endpoint of the subinterval is allowed to vary. The cost compared to 285 is using a multiplicatively wider band.

**Compensation occurs with both signs.** Fix an exterior zero ρ₀ and 1/2<σ₁<σ₂<β₀. From the complex test of 285 with h=1, choosing the polynomial factor that leaves the target pole simple, one obtains a fixed smooth weight W, compactly supported in [1,e], with |Σ μ(n)W(n/Z)|≫Z^β₀ for all large Z. Integrating by parts with the step function M gives ∫₀¹|M(Z exp v)|dv≫Z^β₀, since the derivative of the weight in the logarithmic coordinate is bounded and the boundary terms disappear.

Separately, build the two-point probability of 284 for each zero with Re ρ≥σ₁, repeating the factors according to multiplicity. The sum of their widths H is finite by the density of 230. Convolve with the uniform distribution on [0,H+4] and then with a Gevrey-two density of mass one on [0,1]. The resulting density k is nonnegative, with fixed support [0,2H+5], and equals 1/(H+4) on [H+1,H+2]. Its positive transform P(s)=∫k(v)exp(sv)dv cancels with multiplicity all poles of 1/ζ in Re s≥σ₁ and has vertical decay exp(−c√|Im s|) on fixed strips.

On the line 2 smoothed Perron inversion gives for ∫k(v) M(X exp v)dv the integrand X^s P(s)/(sζ(s)). This is justified by first integrating the step smoothed by k, or by absolutely convergent Mellin inversion after smoothing. Move to the path between σ₁ and σ₂ of 285. No effective pole is crossed and the Gevrey factor dominates the growth of the reciprocal on the path. Thus the signed average is O(X^σ₂). Its average in absolute value is ≫X^β₀ by the plateau of k and the lower integral of the previous paragraph. Since k is a probability, each of the two masses ∫k max(±M,0) is ≫X^β₀. Consequently in EACH sufficiently distant [X,BX], B=exp(2H+5) fixed for this zero, there are values of M greater than c X^β₀ and less than −c X^β₀.

**Temporal orientation.** Apply the result on [X,BX] and [BX,B²X]. A negative value in the first band and a positive one in the second produce a positive increment of size ≫X^β₀. Choosing the signs the other way round gives a negative increment. For each fixed zero, C(X) eventually exceeds B². Take the lower limit and then the supremum over the exterior zeros. The ceiling follows from M(y)≪_θ y^θ for Θ<θ<1, or from trivial counting if Θ=1. At Θ=1/2 the positive normalization suffices, as in 285.

**Implication for the sign proof.** The asymmetry is usable: an upper bound for the sums of μ from left to right that holds on all subintervals of a chosen band suffices. Controlling from a maximum selected a posteriori without varying the start would not suffice. In the real multiplicative falsifier of 286, the defect f*1 is in fact nonnegative: its local factors are powers of a series with coefficients 1,2,2,… at altered primes, and the identity elsewhere. Its signed average therefore offers no additional cancellation to repair the inversion. Localization in both directions for the true μ uses that 1/ζ has no real poles to the right of 1/2; the artificial real pole of 286 blocks this argument for f. The existence of bands with a one-sided square-root ceiling remains open.
