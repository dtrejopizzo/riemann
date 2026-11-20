# A horizontal band that no simple contour of absolute values can go around

**Status: PROVED, with independent review of all abscissae, the reflection and the geometric cost of curves.**

Let D,z,y,L be as in 388, b=log y∼L/2 and h=log L. For every t∈[0.95π/b,1.05π/b] and every real abscissa σ one has uniformly

    |x^s exp((s−1/2)²/2) D(s)| ≥ x exp(−O(h^12)),   s=σ+it.

Hence every piecewise rectifiable path going from below to above that band pays ≥x exp(−O(h^12))/b in the integral of the modulus. The vertical 1 gives a cost ≤x^(1+o(1)) for the complete contour. The optimum in exponent is still one even allowing curves and negative abscissae.

**Strip near one.** For σ≥1 one uses |D|≥∏(1−1/p)≫1/b. If 0≤1−σ=w/b with w≤10log h, then σ≥1/2 eventually and log|D|≥−2Σ p^(−σ)≥−O(h^11), since p^(−σ)≤e^w/p and Σ_{p≤y}1/p=O(h). Moreover σL≥L−O(log h). The Gaussian factor in absolute value is always ≥exp(−t²/2).

**Abscissae 1/8≤σ<1 with w>10log h.** All factors with log p≥3b/4 have cos(t log p)≤−c. The part b−b/(2w)≤log p≤b contributes to log|D| at least c exp(w)/w. Indeed the weight of each dyadic interval of primes there is ≫exp(w)/b by PNT and p^(1−σ)≥exp(w−1/2). If b/(2w)<2 log 2 use the final subband of logarithmic width 1/2, which fits since w≤7b/8, and apply the PNT with fixed ratio. This argument gives ≫(1+b/w)exp(w)/b in both cases. The remaining negative cost is ≤C exp(3w/4) h, by Mertens and p^(−σ)≤z^(−1/8)=o(1) to estimate the logarithm. The quotient by exp(w)/w is O(hw exp(−w/4))=o(1) uniformly for w>10log h. The floor log|D|≫exp(w)/w absorbs the loss (1−σ)L=O(w).

**Abscissae between zero and 1/8.** Even when p^(−σ) is close to one, for p<y^(3/4) the modulus |1−p^(−σ)exp(−it log p)| is ≥c/b: minimizing over the positive real radius gives the sine of the angle up to π/2 and one from there on in the arc considered; t log p≫1/b. The negative cost is O(y^(3/4)log b). The primes in [y/2,y] contribute ≫y^(7/8)/b, since log|1−p^(−s)|≫p^(−σ) on that arc; all the others in the upper strip add non-negative terms. The floor exceeds L.

**Negative abscissae.** The exact identity |D(−u+it)|=exp(uΣ_{z<p≤y}log p)|D(u+it)| for u≥0 shows that the modulus of the integrand at −u divided by that at +u is exp(u(Σlog p−2L+1)). The final 1 comes from the Gaussian. It is ≥1 for large x by the PNT. Finally the length of the portion of the curve in the band is at least its height, even with backtracking, whence the claim.

**Review record.** For σ≥1 the factor-by-factor inequality |1−p^(−σ−it)|≥1−1/p also covers σ without an upper ceiling. On the intermediate range w>10log h, the ratio O(hw exp(−w/4)) is maximized at the lower endpoint for large h and tends to0; moreover exp(w)/w≫w, uniformly, so the floor absorbs (1−σ)L even when σ is far from1. The final band of width1/2 fits because b/(2w)≥4/7 for σ≥1/8. For0≤σ≤1/8, minimizing the modulus over any positive radius gives at least sin(t log p) if the angle is below π/2 and at least1 when it exceeds it. On the lower arc the angle is separated from0 by c/b, and on the upper one all logarithms of moduli are non-negative. Thus the cost O(y^(3/4)log b) and the floor y^(7/8)/b are uniform also at σ=0.

The reflection identity uses |D(u−it)|=|D(u+it)| and the quotient of the Gaussian factors is exactly exp(u); hence the term+1 and the uniform comparison for all u≥0. Finally, for a continuous piecewise rectifiable curve crossing both boundaries, ∫_band|ds|≥∫_band|dt|≥0.1π/b, even with backtracking. Multiplying by the pointwise floor gives the claimed cost and its exponent1, since h^12=o(L). It is not assumed that the curve is a graph in t nor that its abscissae are bounded.

Scope: the lower bound applies to the intact integrand and to the integral of its modulus. It does not apply if contributions are first combined with their phases or a term whose integral is known is subtracted.
