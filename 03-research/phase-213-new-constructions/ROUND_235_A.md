# Only the first η log q modes of the original order detect the complete exponent

For q prime, S_q(m)=Σ_(q<p≤2q)(log p) exp(2πim(p−q)/q). For EACH fixed η>0,

    lim_(q→∞) log(1+q^(−1/2) max_(1≤m≤η log q)|S_q(m)|)/log q = B,

where B=sup |Re ρ−1/2|. Any large integer q can be taken in this statement. If B>0, in every sufficiently high dyadic interval there is among those modes one with modulus ≥q^(1/2+B−o(1)). Therefore it would suffice to control simultaneously only O(log q) sums over the primes in their true order along a subsequence. The proof does not require that the rest of the modes have little energy; it extracts a sufficient signal entirely within the short band.

**Auxiliary ceiling.** Set β*=1/2+B. For each ξ>0 one has |θ(x)−x|≪_ξ x^(β*+ξ), even if the supremum is not attained. Indeed, at a half-integer Y with truncation height T of order Y, the truncated von Mangoldt explicit formula gives ψ(Y)=Y−Σ_(|γ|≤T)Y^ρ/ρ+O(log²(2Y)) (a good height in [Y,2Y] can be chosen). In the version with error depending on the distance to a prime power, the distance to every integer is ≥1/2, so the extra term is O(log Y). Z3 gives Σ1/|ρ|≪log²(2Y). Passing to the general point costs O(log Y), and the powers ≥2 cost O(√Y log² Y). By parts against exp(2πim(x−q)/q), the integral of the continuum is zero for nonzero integer m and

    |S_q(m)| ≪_ξ (1+|m|)q^(β*+ξ).

This gives the required ceiling and the case B=0 with the added 1.

**Fixed filter and adjustable regularisation.** If B>0 fix a right zero ρ₀=β₀+iγ₀ and 1/2<σ<β₀. Use the factors of 230 to obtain a complex MEASURE μ of finite variation, mass one and support in [0,1/10]. Its bilateral transform at w annihilates all nonzero ρ−ρ₀ with Re ρ≥σ and also 1−ρ₀, by adding a finite factor. Do not yet use the last smooth convolution of 230. Fix ℓ=1/10. In the physical variable x, let b_n be the density of the point 1.3 plus the sum of n independent uniforms on [−ℓ/(2n),ℓ/(2n)]. It lies in [1.25,1.35] and its Fourier transform in cycles satisfies

    |b̂_n(ξ)|≤min(1,n/(πℓ|ξ|))^n.

Set Z_n=∫ x^(ρ₀−1)b_n(x)dx→1.3^(ρ₀−1)≠0 by concentration (variance ℓ²/(12n)). Regularise in the logarithmic variable with f_n=μ*[exp(ρ₀v)b_n(exp v)/Z_n]. This function has integral one and preserves all annihilations. Its derivatives up to order two have L¹ norms polynomial in n: when differentiating the convolution of boxes one can differentiate two factors as differences of measures of variation 2n/ℓ, and the other boxes have mass one. Changing variable on a compact and multiplying by the exponential preserves the ceiling.

The test for the primes is W_n(y)=(1+y)^(−ρ₀) f_n(log(1+y)) with y=(p−q)/q. It is supported in a compact interior to (0,1) because 1.35 exp(1/10)<2. Its mean over [0,1] is zero by the target 1−ρ₀. It can be written as an integral, against μ(dw)/Z_n, of exp(−ρ₀w)b_n((1+y)exp(−w)). After translating and rescaling, this gives for the coefficients of the periodic extension

    |Ŵ_n(m)| ≤ C min(1,n/(πℓ|m|))^n,   ||W_n||∞≤Cn.

The constants may depend on the zero and on σ, but stay fixed as q grows.

**Signal in the test.** The explicit formula of 230, derived as a distribution in log x, gives for the atoms dψ the main term dx and the terms −exp(ρ log x)dlog x with multiplicities. Integrate the test W_n((x−q)/q). The continuum disappears exactly. The term of ρ₀ is −mult(ρ₀)q^ρ₀ by mass one and the remaining ones with β≥σ vanish. The remainder is O(q^σ poly(n)): use two derivatives in the transform of f_n and counting by unit intervals; the trivial zeros add up to O(poly(n)) on this translated compact. On keeping only primes the error is O(n√q log² q). Therefore for n comparable to log q,

    Σ_(q<p≤2q) log p W_n((p−q)/q) = −mult(ρ₀)q^ρ₀ + o(q^β₀).

**Truncation in frequency.** Take K=floor(η log q), n=floor(πℓK/4). For |m|>K the coefficient bound is ≤C(K/(4|m|))^n. Multiply by the auxiliary ceiling for S_q(m) and sum: the tail costs O_ξ(q^(β*+ξ) K² 4^(−n)). There is an absolute constant c>0 such that it is O_ξ(q^(β*+ξ−cη)) for large q. The zero ρ₀ can be chosen as close to β* as desired: choosing β*−β₀<cη/3 and ξ<cη/3 makes this tail o(q^β₀). On the kept modes the sum of moduli of coefficients costs O(K) and the zero mode vanishes. By the formula above the maximum of |S_q(m)| for 1≤m≤K is ≳q^β₀/K, using S_q(−m)=conjugate(S_q(m)). Taking β₀ to β* proves the lower bound for EVERY large q, without interchanging the limit in q with a moving choice of zero.

**Scope.** 233 paid by orthogonality for all modes above √q. Here it is proved that a hypothetical failure must already be seen in the first η log q, with the original form of the sums. It is a reduction of where to look for a bound, not an estimate of cancellation of those sums. The number of modes still grows; the claim is not deduced for a fixed list.
