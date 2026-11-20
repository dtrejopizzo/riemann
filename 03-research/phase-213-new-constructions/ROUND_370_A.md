# Unconditional saddle up to cuts exp(C(log log x)²)

**Status: PROVED, with [independent review of the transfer and of the local stretch](AUDIT_370_PHASE.md).** There is a sufficiently large absolute constant C for which, with L=log x, uniformly in

    C(log L)² ≤ b=log z ≤ L^(3/4),

the fixed-width pulses of 367–368 satisfy S^*(x;z)<0 and Q^*(x;z)>0 for sufficiently large x. The weight is still g(v)=exp(v/2)φ₁(v). RH is not assumed.

**Cross-check and operation.** The immediate antecedent is 367, «Direction under RH» and «Control replacing diffusion»: there the saddle stays next to 1/2 and RH allows shifting the contour. Here the saddle is moved towards 1 as the cut increases, inside an unconditional zero-free region. The useful band of primes no longer has constant logarithmic width, but 1/(1−α). 369 preserves the sign via Dickman layers up to b≥L^(3/4); the present argument covers the adjacent range and does not use a signed substitution of all layers. It is a partial extension of the same observable, not a proof of its sign at z=L² nor of the full form. The internal cross-check is limited to 367–369 and to the record of those results in Part V of the index; no historical novelty is claimed.

## 1. Saddle and free region

Put F=1/ζ, E_z(s)=∏_{p≤z}(1−p^(−s))^(−1) and

    K(s)=Ls+(s−1/2)²/2+log E_z(s).

Let α be the unique real root of K'(α)=0 in (1/2,1), and d=1−α, ξ=bd, u=L/b. The classical PNT, by partial summation, gives uniformly

    ξ→∞,  e^ξ/ξ∼u,  ξ=log u+log log u+o(1),
    K''(α)∼Lb,   K'''(α+it)=O(Lb²)  for |t|≤1/b.

To obtain these estimates it suffices to integrate the first powers in log p: ∑ log p·p^(−α)∼e^(db)/d; the higher powers contribute O(1) to K' and O(1) to each fixed derivative. The main mass comes from log p=b−O(1/d), and 1/d=b/ξ=o(b). The exact equation and the strict positivity of K'' justify existence and uniqueness; at α=1 the sum is O(b)=o(L), and at α=1/2 it exceeds L. Moreover

    d=ξ/b ≤ O(1)/(C log L),   sqrt(b/L)→0.

Choosing C large ensures that the whole rectangle α≤Re s≤1+1/L, |Im s|≤2sqrt L lies in an interior version of the classical free region Re s≥1−c/log(3+|Im s|). F is regular at s=1. There F and F' have bound exp(O((log L)²)), by the usual bounds in the free region, or by Borel–Carathéodory and Cauchy using a margin ≍1/log L. Only the [classical free region and its PNT consequences](https://www.ford126.web.illinois.edu/wwwpapers/zeros.pdf) are used.

## 2. Phase loss without RH

In the band b−1/d≤log p≤b, the mass ∑p^(−α) is ≍L/b. After r=d(b−log p), its normalized measure is comparable to exp(−r)dr on [0,1]. The elementary inequality

    inf_θ ∫₀¹ exp(−r)[1−cos(θ−ωr)]dr ≳ min(ω²,1)

follows by comparison with the uniform measure: the infimum of its integral is exactly 1−|sinc(ω/2)|, which is ≳min(ω²,1). Applied with ω=t/d, it implies

    log E_z(α)−log|E_z(α+it)| ≳ (L/b) min((t/d)²,1).

The transfer to the primes is uniform for 1/b≤|t|≤2sqrt L and uses only integration by parts. Integrate θ(v)−v against v^(−α)(1−cos(t log v))/log v on [exp(b−1/d),exp b]. The classical PNT gives an absolute error

    O((e^(db)/(db)) exp(−c₁sqrt b)(1+|t|)).

The boundary terms satisfy the same bound. Here e^(db)/(db)≍L/b; choosing C large, the relative error is o(ξ^(−2)), smaller than the minimal relative loss on the stretch. Neither a theorem on primes in short intervals nor summing an oscillating partition is required.

For |t|≤1/b, the phases of these same primes have modulus ≤1, whence the more precise bound ≳Lb t². Consequently, on the whole stretch 1/b≤|t|≤2sqrt L the loss is at least

    c L/(bξ²) ≳ L^(1/4)/(log L)².

This term dominates (log L)² and hence the cost of the zeta factor and its derivatives.

## 3. Equivalents and signs

The local integral on |t|≤(log L)/sqrt(Lb) is Gaussian: the normalized cubic remainder is O((log L)³sqrt(b/L))=o(1). Between that scale and 1/b the loss Lb t² dominates. On this stretch the global ceiling for zeta is not used: since |t|/d≤1/ξ=o(1), one has |F(α+it)|=O(d), F'=O(1), |L_z|=O(L), |H|=O(1) and |B_z|=O(Ld). Thus the local tail is negligible without comparing unknown constants in exponents of size (log L)². The rest of the vertical segment is dominated by the previous phase estimate. When shifting the contour from c=1+1/L to α no zero is crossed. The horizontals at ±2sqrt L and the tails on c are negligible by exp(−2L), against exp(K(α))=exp(L−o(L)); moreover log E_z(α)=O(L/b)=o(L).

For the pulse without exterior prime the factor is F. Since α→1 from the left,

    F(α)∼−d,
    S^*(x;z) ∼ F(α) exp(K(α))/sqrt(2πK''(α)) <0.

The factor varies relatively by o(1) at the local scale, since d sqrt(Lb)=ξ sqrt(L/b)→∞. For Q^* the factor of 367 is B_z=F'−F(H+L_z), with H the sum of higher powers and L_z=∑_{p≤z}log p·p^(−s). The saddle equation gives L_z(α)=L+O(1), while H(α)=O(1), F'(α)=O(1) and Ld→∞. Thus

    B_z(α)∼−LF(α)∼Ld,
    Q^*(x;z) ∼ Ld exp(K(α))/sqrt(2πK''(α)) >0.

All estimates are uniform in the announced range. The linked independent review checks the phase loss, its transfer by the PNT and the local control of the two factors. There is no numerical computation nor extrapolation from samples; nor is an explicit first x provided.

**Scope and next frontier.** Together with 369 one obtains S^*<0 for exp(C(log log x)²)≤z≤sqrt x. The cut of 368 is z=(log x)², whose logarithm is 2log log x: it lies outside. There the saddle leaves the classical free region available at the necessary heights. Reopening requires controlling that displacement or replacing it by an arithmetic identity preserving the sign; reducing C without a new estimate does not resolve the difference of orders.
