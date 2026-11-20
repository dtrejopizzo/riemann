# A Möbius band of ratio tending to one suffices to detect an exterior zero

Let t=log X, 0<h=h(X)≤1 with log(1/h)=o(log t). Put

    D(X,h)=max_(X≤u≤X exp(h)) |Σ_(X<n≤u) μ(n)|.

Then lim log(1+D(X,h)²/X)/log X=2Θ−1. A subsequence on which D(X,h)≤X^(1/2+o(1)) suffices to close the sign. For example one can take h=exp(−√log log X). In 133 the Mertens band was [X,X^(1+δ)]; in 231 this range of lengths was reached for primes. For Möbius one must isolate poles of the reciprocal, with their multiplicities and without assuming bounds on 1/ζ' at its zeros.

**Upper bound.** If Θ<1, use M(v)≪_θ v^θ for each Θ<θ<1. If Θ=1 the number of summands suffices. At Θ=1/2 the normalized expression has limit zero. In that case the argument does not claim a floor of size √X for D in each window.

**Filter for the reciprocal.** Fix ρ₀ with β₀>1/2, of multiplicity m, and choose 1/2<σ₁<σ₂<β₀. Build as in 230–231 a complex measure supported in [0,2h/3], of mass one and with vanishing moments at e^((ρ−ρ₀)v) for the other zeros with Re ρ≥σ₁. Repeat the factor of each zero as many times as its multiplicity, which gives zeros of the required order in the entire transform. Ingham's estimate counts multiplicities. For |γ|>G use the positive factors of 230; a sufficiently large height G≪(1+1/h)^C leaves a sum of lengths <h/3. For the finite list, of size O(G log(2G)), use the short-step factors of 231: the support costs ≤h/3 and the total variation is exp(o(t)), because G=t^o(1). The target is normalized to one.

Convolve with a smooth Gevrey-two density of mass one on [0,h/3], using a rescaling of 274. Call the resulting density f and F(s)=∫f(v)e^((s−ρ₀)v)dv. Finally use

    Φ(s)=(s−ρ₀)^(m−1) F(s).

This reduces the target pole to a simple one, with fixed residue m!/ζ^(m)(ρ₀) in Φ/ζ. Multiplication by that polynomial is realized by derivatives of fixed order of f with appropriate sign, without enlarging the support. Thus Φ is the Mellin transform of a smooth weight W on [1,exp h]; ||W||∞+Var(W)≤exp(o(t)). On every fixed real strip around [σ₁,2] one has

    |Φ(s)| ≤ exp(o(t)) (1+|s|)^(m−1) exp(−c√(h |Im s|)).

Here the Gevrey convolution factor is separated when estimating the transform; multiplying it by e^((Re s−ρ₀)v) only changes the constants on a fixed strip. The losses from the fixed derivatives on rescaling are powers of 1/h=t^o(1).

**Contour shift.** For Σ μ(n)W(n/X) start from the line 2 with integrand X^s Φ(s)/ζ(s). Shift to a piecewise path in the strip [σ₁,σ₂]. In each horizontal band of height comparable to one there are O(log(2+|Im s|)) ordinates of zeros in its neighborhood of fixed size. Horizontal edges can be chosen within intervals of length 1/4 around integer heights, separated from all those ordinates by ≫1/log(2+|Im s|). Between two consecutive edges choose the vertical coordinate in [σ₁,σ₂] separated on the same scale from the real parts of all nearby zeros. Join the pieces along the chosen edges. At bounded height, edges without zeros are chosen by discreteness.

On those pieces and on the horizontal closures up to 2, |1/ζ(s)|≤exp(C log²(3+|Im s|)). Indeed, the local formula for ζ'/ζ as a sum of 1/(s−ρ) over |γ−Im s|≤1 with error O(log(3+|Im s|)), integrated in the real part from 2, gives the logarithm of the modulus as a sum of log-distances with error O(log(3+|Im s|)). One can pass to the limit from neighboring heights if the horizontal line of integration passes through a zero. At the points of the path all distances are ≫1/log(3+|Im s|). This estimate is used only for large heights.

The cost of integrating it against the Gevrey decay is exp(o(t)) uniformly in the allowed h. To see this put b=log(3+1/h) and divide the heights into dyadic blocks; with z=h|Im s| the log² part is O(b²+log²(3+z)), and exp(−c√z) dominates all factors in z. The remaining cost is exp(O(b²)) times a power of 1/h, admissible. The horizontal closures vanish at infinity for each X. All poles crossed except the target are removable by the filter; their individual residues need not be summed. This gives

    Σ μ(n)W(n/X) = X^ρ₀ m!/ζ^(m)(ρ₀) + O(X^σ₂ exp(o(t))).

By partial summation over the support its modulus is ≤D(X,h) exp(o(t)). It follows that liminf log(1+D²/X)/log X≥2β₀−1. Taking the supremum over the exterior zeros finishes the proof.

**Arithmetic obligation.** The criterion only requires controlling the ordinary partial sums within a band and needs neither the value of M(X), the Gram matrix nor an auxiliary crossing. It does not prove the existence of bands with a square-root ceiling. The new step compared to 231 is the control of the reciprocal along the path and the normalization of the multiple pole with cost uniform in the width.
