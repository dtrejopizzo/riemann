# Along an unconditional subsequence the two infinite tails disappear

Let w be the fixed weight of 275, h=∫w and φ=w/h. There exist scales L→∞ with ΣΛ(n)φ(n/L)=L exactly. At x=2L², the criterion of 281 reduces to a FINITE sum over pairs of indices both in

    V/(C log²(2N)) ≤ d,e ≤ C V log²(2N),      V=x/U ≍ L.

The reduction costs O(log^C(2N)) per sample and preserves the square-root budget for the diagonal. In these coordinates the pairs with gcd≥V exp(−√log(2N)) can be paid for even by summing their moduli. The signed ceiling for the other pairs remains open.

**Existence of the scales.** For Jφ(L)=ΣΛ(n)φ(n/L), the Mellin transform of Jφ(L)−L on L≥1 is Hφ(s)(−ζ'/ζ)(s)−1/(s−1) in Re s>1. The principal part cancels at 1. The continued function has a pole at the first critical zero, where Hφ does not vanish by 276, and is analytic at every real point s≥1/2. By Landau neither it on the original domain of scales (the deficit) nor its opposite can have eventual sign: the real abscissa of convergence would have to be a real singularity ≥1/2. By continuity of the locally finite sum there are therefore arbitrarily large roots of the deficit. No hypothesis on the other zeros is required.

**Cancellation common to all samples.** For each sample y of 280 write H_d=(V/d)[α+β log(d/V)] for the affine tail of K_y(d) identified in 282, with |α|+|β|≪log²(2N). Extend H_d by that formula down to d=1. Put c₁=∫φ(u)log u du and a=α+β(log(L/V)+c₁). Define

    K'_y(d)=K_y(d)−H_d
        +(V/L) Σ_(l≥1) [a−β log l] φ(ld/L).

Since ∑μ(d)/d=0 and ∑μ(d)log(d)/d=−1, the subtracted part has Möbius sum −Vβ. By μ*1=δ and μ*log=Λ, the added part has sum −(V/L)β Jφ(L); the δ term is zero for L>1. Hence at each root the two operations compensate exactly, even with α and β different for each sample. Choosing x=2L² avoids any need to invert the step function U=⌊√N⌋: it suffices that V/L be bounded above and below.

**Localization and size.** Above max(4V,2x/Y,2L) the new coefficient is identically zero. For d<V, K_y(d)=0. In the compensation sums write log l=log(L/d)+log(ld/L). The integral terms in the periodizations of φ and φ log u give exactly H_d by the choice of a. The rest is

    O((V/d) log^C(2N) exp(−c√(L/d)))       (1≤d<V).

Both profiles are of Gevrey order two and the periodization of 274 applies; for L/d comparable to one the constant is adjusted. Thus the sum of moduli below V/(C₀ log²(2N)) is O(N^(−3)) choosing C₀ large. In the retained finite band all coefficients are O(log^C(2N)): this follows directly from the formula by counting the l≤2L/d and the bound of 281. Denote by K'' the coefficients after that lower cutoff. Then T(y)=Σ μ(d)K''_y(d)+O(log^C(2N)) simultaneously at all samples. The total quadratic variation of the coefficients (sum of squares over d and y) is O(V log^C(2N)).

**Remaining pairs.** In the finite upper square of side M≪V log²(2N), the number of pairs with gcd≥H is at most Σ_(g≥H)⌊M/g⌋²≪M²/H for H≥2. Thus that part is removed from the new Gram matrix by absolute summation at cost x^(1/2+o(1)) for H=V exp(−√log(2N)). By 280–281 a ceiling x^(1/2+o(1)) for the remaining signed sum along a subsequence of the roots L would suffice. Conversely RH would give it at all those roots. The auxiliary roots exist unconditionally; their existence does not prove control of the Möbius correlations.

**Cross-check.** 049 already isolated pairs of factors close to √x and their bilinear barrier. 281–282 kept two calibration tails up to infinity in the Gram matrix. What is obtained here is a common choice of scales and compensators that turns that specific matrix into a finite matrix without sacrificing the two calibrations or the sum-of-squares structure. Mere localization near √x already had an antecedent.
