# Uniform sampling of the odd parity of 088

For any step h>0, fix a≥1/2, 0<b<1/2 and γ=mπ/h>a+b with m natural. Consider the model of the finite spectral formula with z=±b±iγ (four choices), without attributing those points to ζ. It satisfies the symmetries and the summability used in the computation of 088. At T=nh the pair with positive real part contributes to J(T) exactly

    2 exp(2bT) ((a+b)²−γ²)/((a+b)²+γ²)².

The other pair costs O(exp(−2bT)). The normalized diagonal converges to a constant since b<a. Hence the normalized odd energy 2D_T−2C_T tends to +∞ on the grid. At T=nh+π/(2γ) the sign of the two phases changes and the same energy tends to −∞. Adding any family on the critical axis with finite sum of (1+γ²)⁻¹ alters J and the normalized diagonals by O(1) (for ordinates bounded away from zero). So including the already verified critical zeros does not repair the formal inference.

**Decision.** Discard the inference of continuous positivity from the odd parity observed on a fixed grid using only symmetries and summability. 088 uses a pole off the real axis in the continuous transform; at the samples its phase is one. This model does not provide zeros of ζ nor refute an arithmetic inequality on the windows nh. The Nyquist failure of phase 186 (R186_117) corresponds to the window symbol, while here the window itself is sampled.

**Audited refinement.** In fact the odd contribution of the quartet is strictly positive at ALL nh with n≥1. Put A=a+b, B=a−b, U=sinh(AT)/(A²+γ²), V=sinh(BT)/(B²+γ²). On the grid the two-sided transform of sinh(at) at z=b+iγ is, up to sign, AU−BV−iγ(U+V), by direct integration. By oddness and conjugation the sum of the quartet in Weil is −4 times the real part of the square of that transform. It is positive because |AU−BV|<γ(U+V). The statement refers to the individual odd parity.
