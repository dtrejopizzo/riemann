# Removing the small prime powers with both their inner sums complete

Fix d=1/4, W of 159 and P(s)=s(s−1)(s−1+d)(s−1/2). Define w_* by applying P(−t d/dt) to the profile w of 159. It has compact support in [exp(−A),exp(A)] and may change sign. For y>0 put
    K(y)=Σ_{m,n≥1} m^(−d) w_*(mn²/y).
The condition Σ_q Λ(q)K(x/q)≤O(√x) eventually is equivalent to the sign. In that condition all q≤x/(K₀(log x)^6) can be deleted, with total absolute error o(1) for K₀ sufficiently large. The discard includes the main terms and the constant of both sums, without any cancellation estimate in Λ.

**Discard.** By Mellin, K is the inverse of B(s)=P(s)W(s)ζ(s+d)ζ(2s). B is entire: the only possible poles are at 0, 1−d and 1/2. On Re s=−L with L=N+1/4, N≥2, and s=−L+it,
    |P(s)W(s)| ≤ exp(C L−c√|t|)(1+L+|t|)^3.
Indeed each factor of the product of uniforms before the divisor s costs ≤exp(L/j²)min(1,j²/|s|) by the formula with sinh and the integral representation. Each j≤√|t|/2 gives a saving ≥4 in the denominator of the majorant. On the same line the functional equations give
    |ζ(s+d)ζ(2s)| ≤ C^(L+1)(1+L+|t|)^(3L+C).
To see this, in each equation use Stirling in the right half-plane for Γ(1−z) and |sin(πz/2)|≤exp(π|Im z|/2). The difference between these angular exponents costs O(1+|Re z|), by v arctan(u/v)≤u; the factor ζ(1−z) is absolutely bounded. Shift the contour for fixed L (the decay in t beats every power). The integral in modulus is ≤y^(−L) C^(L+1)(1+L)^(6L+C'): split |t|≤L and the rest, and use the gamma moment of exp(−c√|t|). Choosing L of order ε y^(1/6) with ε small gives |K(y)|≤C exp(−c' y^(1/6)) for y≥1. The Chebyshev bound Σ_{q≤x}Λ(q)=O(x) proves the discard. At the opposite end K(y)=0 for y<exp(−A), so the remaining sum is finite.

**Detection.** The transform of the original sum is B(s)(−ζ'/ζ)(s). P(1)=0 removes the main pole of the logarithmic derivative; the other real poles were already removed from B. Under RH one can shift to Re s=1/4, summing critical residues of total size O(√x) by the vertical decay and the zero count. If there are zeros to the right, choose the rightmost at a given height. There ζ(s+d), ζ(2s), W(s) and P(s) are nonzero, so a simple pole remains. Landau as in 155 excludes such a pole if the unilateral ceiling is proved. The argument operates on the filtered weight directly, without differentiating an inequality.

**Cross-check.** 047 already localized criteria using Gevrey averages and Landau. Here the specific double fibre mn² of 155 is estimated; the difference with 159 is that in the removed piece no main term weighted by Λ remains. What survives is another centred inequality over prime powers in a multiplicative band. Narrowing that band further without controlling its sign would repeat the localization strategy of the corpus. No new window is obtained.
