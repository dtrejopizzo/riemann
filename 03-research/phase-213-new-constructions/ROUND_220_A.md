# Unconditional balance and conditional frequency of sign excursions

Use the complex arithmetic sample C_k of 217. Fix a real angle φ, a threshold λ>0 and a progression k=qn+b, q a positive integer. In each block M<n≤M+H with H≤M, H/√M→∞, count separately

    P: Re(exp(−iφ) C_k)>λ,      D: Re(exp(−iφ) C_k)<−λ.

Unconditionally (#P−#D)/H→0. More precisely, under RH both fractions are eventually zero; if RH fails, each tends to 1/2. In particular it suffices to prove for ONE direction, ONE progression and ONE sequence of such blocks that the frequency of negative excursions has liminf below 1/2. No estimate on the size of the extreme values is needed. Proving only that positive and negative excesses balance does NOT discriminate the global sign: that balance holds in both cases.

**Proof.** Under RH, 217 gives C_k→0. Off RH, its complex equivalence and the phase of the beta factor give, modulo 2π,

    arg C_k=π + k log r₀ + Θ√k + o(1),      |C_k|→∞,

since w₀ has argument −Θ and K_(k²)(s_k) has phase o(1). In each progression this phase equidistributes on the circle, even if log r₀/(2π) is rational. To verify this on the indicated blocks, fix a nonzero integer harmonic m and set f(n)=m[(qn+b)log r₀+Θ√(qn+b)]. The increment Δf(n) is monotone and tends to mq log r₀. If the limit is not a multiple of 2π, Σ exp(if(n))=O_m(1) on the block. If it is a multiple of 2π, the distance of Δf to the multiple is comparable to 1/√M on the whole block by Θ>0, fixed q and H≤M. Then the sum is O_m(√M). The constants may depend on Θ,q,b,r₀. Both ceilings follow directly from summing by parts the identity exp(if(n))=(exp(if(n+1))−exp(if(n)))/(exp(iΔf(n))−1): the reciprocal has constant real part −1/2 and monotone imaginary part while the increments stay between consecutive multiples of 2π. Hence its variation is O(1) or O(√M), respectively. The phase o(1) in 217 alters the normalised average by o(1). Dividing by H and applying Weyl's criterion proves equidistribution.

The phase of C_k thus distributes half of the indices in each semicircle. To impose λ>0 and rotate by φ, first exclude a fixed neighbourhood of the two endpoints of the semicircle, use |C_k|→∞ uniformly in the tail, and let the size of the excluded neighbourhood tend to zero. This gives the stated limits. The dichotomy for natural density is also obtained via dyadic blocks, applying the same exponential-sum argument to [1,M] or adding the block limits.

**Arithmetic reading.** 207 obtained negative signs infinitely often for a rational rate depending on the hypothetical zero, via a rotation that could be periodic. Here the same prime sample, fixed in advance, is observed at each order, and an exact frequency of excursions above a fixed threshold in both directions is obtained. The curvature Θ√k that results from the weight of 217 eliminates possible resonance. The unconditional estimate of the difference of counts is a consequence of the spectral dichotomy; it is not evidence for either of its branches. A prime estimate distinguishing frequency zero from frequency one half remains pending.
