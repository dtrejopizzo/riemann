# A centred, finite prime sum that preserves the growth of the diagonal

Fix u≥3 and put H(z)=4u²z²/(u²+z²)², c_N(t)=(2π)⁻¹∫ H(τ)^N exp(iτt)dτ. Define

    M_a(u)=2/(1+√(1−4a²/u²)),   X_N=M_1(u)^(2N),
    P_N(u)=Σ_{2≤n≤X_N} [Λ(n)−1] n^(−1/2)c_N(log n).

Uniformly in N≥2 for each fixed u, b_N(u)=−2P_N(u)+O_u(1), with b_N from 207. Consequently the global sign is equivalent to having, for every rational rate u≥3, limsup_N |P_N(u)|^(1/N)≤1. Equivalently one may ask that P_N(u) be bounded in N for each of those rates: under RH it is, by 207 and the identity above. This prime cancellation has not been proved for every rate.

**What is discarded with bounded error.** On the line 0≤H≤1 and the normalized Fourier density of the atom of 207 is H^N. The archimedean term costs O_u(1) by integrability of |m|H. The polar product is obtained by evaluating the rational density at τ=i/2 (with factor 2 from the polar) and is bounded by 2|H(i/2)|^N=O_u(1). What remains is −2Σ Λ(n)n⁻¹ᐟ²c_N(log n) by the complete prime formula. On |Im z|=a≤1, writing q=(Re z)²+a²,

    |H(z)|=4u²q/[(u²+q)²−4u²a²].

The maximum is at q=√(u⁴−4u²a²), admissible for u≥3, and equals M_a(u). The contour can be shifted to Im z=1 for t≥0 without crossing poles; the sides vanish by rational decay. Thus |c_N(t)|≤C_u M_1(u)^(N−1)exp(−t), since |H(·+i)| is integrable. By Chebyshev and partial summation, Σ_{n>X}(Λ(n)+1)n^(−3/2)≪ X^(−1/2) for X≥1. At X=X_N this leaves an O_u(1) error, even with no slack in the exponent. For large u, log X_N/N=2/u²+O(u⁻⁴).

**Centring the arithmetic.** On the line |c_N|+|c_N'|≤C_u uniformly for N≥2 by integrability of (1+|τ|)H². If g(x)=x^(−1/2)c_N(log x), the error between Σ_{n≥1}g(n) and ∫₁^∞ g(x)dx is ≤∫₁^∞|g'(x)|dx=O_u(1). The integral is ∫₀^∞ exp(t/2)c_N(t)dt. By parity and the bilateral transform at i/2 it equals H(i/2)^N−∫₀^∞ exp(−t/2)c_N(t)dt, also O_u(1). The bilateral equality is legitimate by the preceding decay in t, for each N. Omitting n=1 costs O_u(1). Therefore removing the term 1 from Λ preserves b_N up to bounded error.

**What an exceedance measures.** Let R(u) be the maximum of 207 and Q(u)=max(1,limsup |P_N(u)|^(1/N)). By the additive error Q=max(1,R). The largest horizontal displacement is recovered exactly, taking suprema even when there is no extreme zero:

    sup_ρ |Re ρ−1/2| = sup_{u≥3} u √(Q(u)−1)/Q(u).

Indeed |h_u(ρ−1/2)|=|H(γ+iδ)|≤M_|δ|(u), and M_a is inverted by a=u√(M_a−1)/M_a, increasing as a function of M_a on [1,2). For each given zero choose u²=2δ²+√(4δ⁴+|ρ−1/2|⁴), which is ≥9 by the first height of Z1. At that rate q=|ρ−1/2|² coincides with the preceding maximizer and its term attains M_|δ|(u). Both inequalities are obtained, also under RH taking Q=1. The formula does not allow replacing the maximum with one: the bounded errors can dominate decaying moments.

**Scope relative to earlier work.** 017 and 044 already provide the atoms and their rational densities; 207 gives the spectral growth law. 208 specifies the finite cut at bounded additive cost, the subtraction of the background 1 and the exact displacement that measures the growth rate. The cut of 014 §7 for arbitrary numerators is governed by the scale of the complete block and does not use this balanced density. Here the sum is still signed and its boundedness at every rate remains OPEN.

In particular P_N(u)=O_u(1) for each 3≤u≤G−1 by the verified sector of 207. The independent review checked the optimization over the contour and the cost of the tail via Chebyshev.
