# Sign inversion of the sector with a single macroscopic prime

**Status: PROVED, with independent review of the frozen moments, the PNT substitution and the sign inversion.**

Let z=L², L=log x, E=∏_{p≤z}(1−1/p)^−1 and J=exp(1/8). For fixed 1/2<θ<1, the contribution V_θ to S of 368 from the integers with exactly one prime greater than x^θ satisfies

    V_θ ∼ +J x E/L².

The sign is opposite to that obtained in 379 for the threshold exp(L^a), fixed a<1. There is no uniformity when passing from one regime to the other. 302 treats another coefficient and grouping.

**Freezing the sieve.** Let f(u)=S^*(exp u;z) keeping z fixed at its value at x. One has |f(u)|+|f'(u)|≪exp u by the Gaussian count in bands, and both decay in a Gaussian way for u<−1 (in the sum n≥1). Up to O_θ(x exp(−c_θ L²)), V_θ=−Σ_{p>x^θ}f(L−log p). The duplications or multiples of p² in this expansion have n≥x^(2θ), with multiplicity O(log(2n)); they are absorbed by the Gaussian tail. Likewise p can be cut at x². The PNT replaces this sum by its integral with density dt/log t, with error O_θ(x L exp(−c_θ√L)): integration by parts, using |π(t)−li(t)|≪t exp(−c_θ√L), and the bound for f and f' just given. Completing the tail t>x² one obtains

    V_θ=−x ∫_{−∞}^((1−θ)L) exp(−u)f(u)/(L−u) du + o(x/L²).

**Two exact moments.** For u≥L^(1/10) one has |f(u)|≪exp(u−c u/log u) uniformly. It is the contour of 377 with scale exp u, height 2√u and shift c₀/log u: here log z=2log L≤20log u, so z^(c₀/log u) is bounded, log E_z(1−c₀/log u)≪log log z and the rest of its estimates apply unchanged. In particular the moments of orders zero and one above (1−θ)L can be completed with error superpolynomial in L. For frozen z, the bilateral transform ∫ exp(−su) f(u)du, first for real s>1, is exp((s−1/2)²/2)E_z(s)/ζ(s). Its value and its right derivative at 1 give

    ∫ exp(−u) f(u) du=0,     ∫ u exp(−u) f(u) du=−JE.

The passage to the limit is justified by the preceding bound and the negative tail. The identity 1/(L−u)=1/L+u/L²+u²/[L²(L−u)] has integrated remainder in absolute value O_θ(L^(3/10)/L³): use L−u≥θL, the elementary absolute bound up to u=L^(1/10) and the exponential afterwards. Thus the first term vanishes exactly and the second, together with the minus of the marked prime, gives the positive sign and the equivalent.

**Review record.** In the expansion by the marked prime, every repeated term or one with two possible marks has n≥x^(2θ), and the number of marks is bounded by O_θ(log(2n)); the Gaussian sum of that tail is O_θ(x exp(−c_θL²)). For the PNT one integrates the smooth function f(L−log t), not a sieve varying with t: z is frozen. The bounds t|f(L−log t)|≤Cx and |f'|≤C exp u give the cost xL exp(−c_θ sqrt L), including both ends of the interval[x^θ,x²].

The contour for u≥L^(1/10) is uniform: log z≤20log u implies p^(c₀/log u)≤exp(20c₀) for p≤z, and log log z≤log log u+O(1). Thus its finite factors are absorbed by the saving u/log u, with constants independent of L and u in that range. This bound and the negative Gaussian tail allow differentiating the transform at s=1 by dominated convergence. Since (1/ζ)'(1)=1, the first moment is −JE, not +JE. The remainder of the expansion of the denominator has absolute value O_θ(L^(−27/10)), and the truncated moments differ from the complete ones by less than any negative power of L. The minus of the marked prime therefore turns the negative first moment into +JxE/L². No uniformity is claimed when θ tends to1/2 or to1.

By 377, the integers without a prime greater than x^θ have balance ∼−JxE/L² (two or more are negligible here). The result identifies cancellation between two sectors at each large scale; the sign of the complete sum requires greater precision.
