# Kernel-free diagnosis: the ordinary error on each power band

Let E(x)=ψ(x)−x+1 for x≥1 and B=sup_ρ |Re ρ−1/2|. For each fixed 0<α<1 one has the ordinary limit

    lim_(X→∞) log(1+∫_(X^α)^X E(x)² dx/x²)/log X = 2B.

In particular a ceiling X^o(1) for that mean along a sequence X→∞, for a single fixed α, would suffice. The statement holds even if there is no extreme zero. Replacing E by ψ−x preserves the limit by the triangle inequality in L²(dx/x²), since the difference has bounded norm. It is a consequence about means of the classical error, not a new arithmetic bound for B.

**Removing the weighted accumulation of 228.** Write t=log x, T=2N, g=g_N, F(t)=exp(−t/2)P_N(exp t), Y(t)=exp(−t/2)g(t)E(exp t). On [0,T], integration by parts against dE gives

    F(t)=Y(t)+∫₀ᵗ exp(−(t−s)/2) (s/(2N))Y(s)ds.

Conversely, integrate g⁻¹ against dP_N and multiply by exp(−t/2)g(t): Y=F minus the same operator applied to F, with the additional factor g(t)/g(s)≤1. There is no initial term because E(1)=0. Since s/(2N)≤1, both L² norms on [0,T] bound each other with factor 3 by Young. In the tail of 228, ∫_X^∞P_N(r)²dr/r²=F(T)² with X=exp(T). At the endpoint Y(T)=O(1/√N) by Chebyshev; the convolution added in F(T) costs O(||Y||₂) by Cauchy–Schwarz. Moreover ∫dν_N(x)/x=∫P_N(r)dr/r², whose square is dominated by ∫P_N(r)²dr/r². On a fixed interval near and to the right of 1 where E(x)=1−x, one sees ||Y||₂²≳1/N. Thus V_N of 228 is comparable, with absolute constants, to ||Y||₂². On extending the integral of |Y|² without cut up to t=∞, Chebyshev gives O(1/N) for the tail by t−t²/(2N)≤−(t−2N) if t≥2N. Consequently, setting dμ(t)=exp(−t)E(exp t)²dt,

    W(N)=∫₀^∞ exp(−t²/(2N)) dμ(t),       log W(N)/N→2B².

The removed factor 4πN is only polynomial. By monotonicity of W, the limit extends from integers to positive real N.

**At which scale the energy concentrates.** If B>0, for each 0<ε<2B, the fraction of W(N) in |t/N−2B|≥ε decays exponentially. For t≥(2B+ε)N compare with W((1+h)N): the logarithm of the ratio with W(N), divided by N, has limsup at most

    2B² h − h(2B+ε)²/[2(1+h)] < 0

if h>0 is sufficiently small. For t≤(2B−ε)N compare with W((1−h)N); the corresponding ceiling is −2B²h+h(2B−ε)²/[2(1−h)]<0. Only positivity of μ and the ordinary limit of 228 are used.

**Removing the Gaussian.** Set L=log X. If B>0, with N=L/(2B) one has μ([0,L])≤exp(L²/(2N))W(N), of upper rate 2B per unit of L. If B=0 take N=cL and let c→∞ to obtain upper rate zero. The 1 in the statement gives the floor in this last case.

For the floor when B>0 fix α<λ<1 and take N=λL/(2B). Choose ε sufficiently small so that [(2B−ε)N,(2B+ε)N] lies inside [αL,L]. That interval receives (1−o(1))W(N) with the Gaussian. On removing it, its unweighted mass is at least exp((2B−ε)²N/2)(1−o(1))W(N). Hence the lower limit per unit of L is ≥λ[2B²+(2B−ε)²/2]/(2B). Letting ε↓0 and then λ↑1 concludes for ALL large X, without selecting favourable heights.

**Consequence for the search.** If B>0, for each α and each η>0, on every sufficiently high band [X^α,X] there is a point x with |E(x)|/√x≥X^(B−η), since the length of the band in t is only (1−α)log X. The same is not claimed for bands [X,2X]. The invertible transfer shows that separating the accumulation of 228 from its Gaussian does not provide an additional inequality. The new step relative to 219 (uniform pointwise control on all cells) is that here ONE subsequence of quadratic means on power bands suffices. That ceiling is not established for any subsequence, nor is priority claimed relative to the Tauberian literature.
