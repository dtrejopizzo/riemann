# The phase of the deterministic cut when moving the scale: both signs in each block

**Status: PROVED, with independent review of the moving phase law and of the jumps at both edges.**

Fix real κ. Let C_κ(x) be the finite pulse without fractional weight with z=L², b=log z, Y=(4+κ/b)z. For each large L₀, b₀=2log L₀ and 0≤u≤3b₀, the unconditional equivalent of 398 takes the form

    C_κ(exp(L₀+u))/A_osc(L₀+u)
      = cos(Ψ₀+πu/b₀)+o(1)

uniformly in u. Here Ψ₀ is the initial phase of 398 and A_osc=2exp(Re G(s_*))/√(2π|G''(s_*)|)>0 is its local amplitude. In particular in EACH block of scales [X,X(log X)^6] there are positive and negative values of absolute value at least (1−o(1)) times the corresponding amplitude. In this block x is varied and the cut rule is kept; in 398 x was kept fixed and the cut was varied.

**Motion between jumps.** Use the branch of G of 398 and the simple upper saddle. With the set of primes fixed, differentiating G(s_*) with respect to L gives exactly s_* since G'=0. Hence dΨ/dL=Im s_*=π/b+O(1/b²) uniformly. In the block b=b₀+O(b₀/L₀), and the integrated error is o(1).

**Jumps of the phase.** Each prime admitted by Y or removed by z produces a change O(1/(L₀ b₀)) in Ψ. To justify it interpolate its weight in [0,1] with L frozen. The derivative is the imaginary part of −p^(−s_*)/(1−λp^(−s_*)). At either of the two edges log p=b+O(1), p^(−Re s_*)≍1/L and |Im s_* log p−π|=O(1/b). The local construction of 398 holds during the interpolation also at the lower edge: a single factor of weight O(1/L) is modified and the inner blocks, the limiting mean and the derivative bounds remain intact. At the junction the branch is recovered by the same convergent series; a simultaneous jump is split into the two steps. This controls the unwrapped real phase.

The functions z(L),Y(L) are eventually increasing, with derivatives O(L₀) in the block. Each sweeps an interval of length O(L₀ b₀). The total number of primes there is o(L₀ b₀) unconditionally and without short PNT: for each fixed primorial P the number of integers coprime to P in any interval of length H is ≤H φ(P)/P+O(P); add the prime divisors of P and then let P grow. Thus the sum of all jumps in absolute value is o(1), uniformly in blocks and subblocks. Together with the derivative the proposed phase law follows. The uniform additive error in the cosine comes from 398. An angular interval of length 3π contains both a maximum and a minimum; evaluating at the corresponding u of the linear phase gives both excursions even when the pulse has discontinuities.

**Review record.** Between jumps G depends explicitly onL only through Ls, so the total derivative of its critical value is exactly s_*; the motion of b introduces no additional term. At the lower edge a factor is removed and at the upper one a factor is added: the orientations can be treated separately and the absolute phase cost is O(1/(L₀b₀)) at both, when interpolating the factor. If they occur simultaneously two steps are performed and the series branches return to the canonical product. The modifications of one factor do not affect the inner blocks nor the uniform construction of398.

For each fixed primorialP, the number of primes in any of the swept intervals is≤C L₀b₀φ(P)/P+O(P)+ω(P). Dividing by L₀b₀, letting L₀→∞ and then P→∞ proves the uniform o(L₀b₀), without lettingP grow before the limit nor using a PNT for intervals of square-root length. The absolute sum of jumps is therefore o(1). The integral of the error O(b^(−2)) along3b₀ is O(1/b₀), and replacing b by b₀ costs o(1). This controls the unwrapped phase also at the discontinuity points. Evaluating at the points where the linear phase equals0 orπ modulo2π uses the uniform additive error of the cosine and does not require the pulse to be continuous asx varies.

**Obstruction.** No choice of constant κ in this family produces an eventual negative sign of the finite product. If RH holds, the complete pulse S is indeed eventually negative by 368, so a deterministic cut of this form cannot reproduce it at all scales. This concerns the sign or exact equality: the finite pulse itself always admits a ceiling of exponent 1/2+o(1) by 393, and a bound on the error made when substituting S remains pending.
