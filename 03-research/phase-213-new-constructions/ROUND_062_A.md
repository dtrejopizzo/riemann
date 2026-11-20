# Signed compensation in the semiprime band of 061

Let S(x), f, G and u* be those of 060–061; L=√x. For a fixed integer h≥0, apply h times the difference sending S(x) to 4S(x)−S(4x). Write S_h for the result. In the slopes G(Z) changes to G_h(Z)=(4−D₂)^h G(Z), with D₂G(Z)=G(2Z).

**Criterion preserved.** The global sign is equivalent to S_h(j⁴)≤C√x eventually, x=j⁴. If the sign holds each term is O_h(√x) in absolute value. Conversely S=o(x), since Q=o(x) by PNT and the compact correction of 060, and Σ_k Q(x/k⁴)/x tends to zero by domination by C/k⁴. The same holds for any fixed number of differences. The interpolation bridge of 060 also holds for its logarithmic translates. If 4H(x)−H(4x)≤M√x on the whole tail and H=o(x), iterating towards 4^n x gives H(x)≤M√x/(4−2). Repeating returns the upper bound of 060. h is chosen once and for all.

**Band including all second primes of the resonance.** For fixed B₀>2, put R=L(log L)^B₀, P=L/√R and Q_p=L²/p³. Consider the products of two primes in

    P≤p≤2P,      √R≤q≤C_h Q_p,

with fixed C_h>(2^h u*)². Each product counts four ordered slopes. Let W_h be the signed sum of all of them in S_h. One obtains

    |W_h| ≪_{h,B₀} R/(log L)^(h+2).

Thus, if h>B₀−2, **the whole band contributes o(L)** to the equivalent criterion. The interval in q is essential; trimming the two families of 061 separately does not justify this estimate.

Indeed T=L/√(pq) tends to infinity as a power of L throughout the band; q/T and p²/T tend uniformly to infinity. In the expansion by valuations only 1,p intervene, also after the h dilations. The slope equals G_h(T)−G_h(√(Q_p/q)); the first term costs less than any inverse power of L, even after summing. The function G_h is smooth, zero below a fixed threshold and decreases rapidly together with its derivatives at infinity (Poisson applied to the logarithmic derivatives of the integral-zero profile).

For the second term, quantitative PNT and partial summation replace the sum over q by the integral with density 1/log q at error O_N(Q_p/log^N L), uniform in p: the weight has bounded total variation, and q≥√R. After putting z=√(Q_p/q) the integral is

    2Q_p ∫_{1/√C_h}^{√(Q_p/√R)} G_h(z) z⁻³/(log Q_p−2log z) dz.

The Mellin transform of G_h, in the convention of 061, is (4−2^s)^h ζ(s)∫f(u)u^(s−1)du. Its derivatives of orders 0,...,h−1 at s=2 are zero. Expand the denominator up to those h terms: log Q_p and log q are comparable to log L on the whole interval, so the integrated remainder is O_h(1/log^(h+1)L) thanks to the finite absolute moment with |log z|^h. The lower endpoint lies below the support and the upper one is comparable to (log L)^(B₀/2); completing each moment to infinity costs an arbitrary inverse power of log L. For h=0 the direct bound by 1/log L suffices. The cost per p is O(Q_p/log^(h+1)L); by PNT Σ_{P≤p≤2P} Q_p≪ R/log L. The two sign families of 061 can also be constructed for each fixed G_h: it is nonzero by its Mellin transform and its moment at −2 is still zero.

**Sign in the original representative.** For h=0 there is moreover an asymptotic, including the four slopes,

    W₀ ∼ −3 M_G(2) R/[log P · log(L²/P³)],    M_G(2)=∫G(z)z⁻³dz>0.

The first term of the integral expansion equals 2Q_p M_G(2)/log Q_p. The sum of p⁻³ over [P,2P] is asymptotic to 3/(8P² log P), and log Q_p=log(L²/P³)+O(1). To check the sign, write I(z)=2^(z−1)V̂(z/2)η(z/2)² as in 057. One has M_G(2)=ζ(2) I(2)[I'(2)/I(2)−b₀]. The logarithmic derivative at s=1 of V̂ is at least 1−(16/255)log16: the averaging factor P of 047 contributes at least its mean 1/2 (the positive exponential tilt increases the mean), and the logarithmic derivative of the hat of 060 is 1/2−(16/255)log16. For η one obtains η'(1)/η(1)=γ_E−(log2)/2 from the expansion of ζ at 1; at 1/2 the functional equation gives γ_E/2+π/4+(log π)/2−(1/2+√2)log2. Therefore

    I'(2)/I(2)−b₀ ≥ 1/4+γ_E/2−π/4−(log π)/2+(√2−32/255)log2 > 0

(even using γ_E>0.57, π<22/7, log π<1.15, √2>1.41 and log2>0.69). The original band thus has a negative balance larger in absolute value than L; its sign favours an upper estimate, although it does not pay its cost in a two-sided estimate.

**Scope.** Differences of dilations and one-sided recovery already appear in 054. The specific operation is to impose vanishing moments at s=2 on the function of the two-prime resonance, and to verify square-root precision for the whole interval of q. For each B₀ a fixed order is used; no limit in h is taken. The other ranges of primes and the other factorisations remain without global estimate.
