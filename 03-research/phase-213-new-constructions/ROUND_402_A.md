# Search window in number of primes around a computable amplitude

**Status: PROVED, with independent review of the constants, the normalization and the first hit.**

Let α,K be those of 368 at the cut z=L², b=log z and T₀=exp(K(α))/(|ζ(1/2)|√(2πK''(α))). This positive number uses ζ at a real point and the product up to z, without knowing S. Enumerate in increasing order the terminal primes of the strip κ₀−1≤b(Y/z−4)≤κ₀+1 of 398; traverse each prime with the weight λ from 0 to 1 and use as coordinate r the number of accumulated weight steps (each prime has length one). Define

    A₀(r)=2 exp(Re G(s_*))/√(2π Lb).

There is a unique r₀ with A₀(r₀)=T₀. Under RH, if r_* is the coordinate of the first weight reproducing S, then for each fixed ε>0, eventually,

    r₀−ε L ≤ r_* ≤ r₀+[8/(2−log 4)+ε] Lb.

This bounds part of the adaptation in number of primes; the width is not converted into length using an average of prime gaps.

**Calibration without consulting S.** The comparisons of 394–395 with T₀ are unconditional: RH was only used to replace T₀ by |S|. The correction to the logarithm of the signed amplitude costs O(L/b³) by 398. At each end of the strip, log(A₀/T₀) has opposite sign and absolute value ≍L/b² (taking the nearest interior prime does not alter the result, by the PNT with remainder as in 398, or start with the set of primes already present at the real endpoint). In the strip the exact derivative of G(s_*) with respect to λ is −p^(−s_*)/(1−λp^(−s_*)); its real part satisfies

    ∂_r log A₀=(1+o(1))/(4L),

because Re s_*=1/2+(log 2+o(1))/b and p/z→4. Its imaginary part, by 398, is

    ∂_r Im G(s_*)=−[π(2−log 4)+o(1)]/(4Lb).

Both estimates are uniform and join when passing to the next prime. The first ensures uniqueness of r₀ and leaves ≫L²/b² steps between r₀ and each end. The prefactor of 398 differs from A₀ by 1+o(1): G''(s_*)/(Lb)→1 by the positive saddle equation, log p=b+O(1) and 398.

**Scope of the first hit.** Under RH, |S|/T₀→1. For every r≤r₀−εL in the strip, the continuous envelope A₀(r)≤T₀ exp(−ε/4+o(1)) does not reach |S| even with the uniform error of 398. Before the strip the exclusion is that of 394, valid for all weights. For the other direction start at r₀+L√b: the envelope already exceeds T₀ by a factor tending to infinity. A complete turn of phase needs (8/(2−log 4)+o(1))Lb steps. Along the way phases of both signs of the cosine with modulus one are attained, by continuity, counting an additional o(Lb) if needed. There the finite balances enclose S; by interpolation it is attained in the announced interval. The roundings of one prime are O(1).

**Review record.** In the terminal factor p^(−s_*)=−a exp(−iδ), with a=(1+o(1))/(4L) and δ=[π(2−log4)+o(1)]/b. The real part of a exp(−iδ)/(1+λa exp(−iδ)) is a(1+o(1)); its imaginary part is−a sinδ/(|1+λa exp(−iδ)|²). Thus one obtains the two rates with factor1/4 and, for a turn of2π, exactly8Lb/(2−log4). The junctions are continuous and the rates uniform, including the weights0 and1. The positive equation and log p/b→1 give G''(s_*)/(Lb)→1; hence A₀ and the complex amplitude of398 differ only by1+o(1), without losing a factor2 or a root of2π.

The margins r₀−r_initial and r_final−r₀ are≳L²/b², which dominate bothLsqrt b andLb. Hence the phase turn used for the ceiling fits in the strip. Before r₀−εL the monotonicity ofA₀ is used to reduce the estimate to an interval of lengthεL; no non-uniform relative error is accumulated over the whole list. The exclusion of394 before the strip holds for any weight, and underRH |S|/T₀→1. This localizes the global first hit and not only one of the hits of the block. The claims about r₀, its margins and the rates are unconditional; both excluding earlier values by comparison withT₀ and asserting that the extremes encloseS in this window useRH.

The construction of r₀ and the amplification of both signs are unconditional. The localization of r_* uses RH. The pending problem is to compare the complete balance with the range of values of these products without using the equivalent for S of 368.
