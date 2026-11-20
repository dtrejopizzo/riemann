# Transferring the verified tail to a bound in L² norm

For fixed T and positive integer A there is C(T,A), independent of the height G, such that if all zeros up to G≥2 are on the critical line, then

    W_T(f) ≥ −C(T,A) G^(−A) ||f||₂².

It holds for the whole form by closure from the smooth core of paper 47. Compared with 172 the derivative norm of f is removed. The idea is to combine two exact extensions on a slightly larger window. One controls the low frequencies via the verified zeros and the other has positive density at high frequencies via the archimedean term.

**Two extensions.** Take the enlarged interval |u|<2T+1. On it use the atomic variant of 172, μ=Σδ_γ+C(τ)dτ, where for each n
    |C(τ)|≤C(T,n) Σ_{|γ|>G} (1+|τ−γ|)^(−n).
On |τ|≤G/2 this costs O_(T,n)(G^(1−n)log(2G)); on the whole line it costs O_T(log(2+|τ|)) by the unit count. The second extension is ν=b(τ)dτ, using a smooth compact weight equal to one on the enlarged interval in the formula fw of the paper. In the normalization of measures the density fw is divided by 2π. By the archimedean formula of §7, b(τ)=m(τ)/(2π)+O_T(1): the difference with the pure multiplier is supported away from the singularity in the integration variable, the prime term is a finite sum and the polar term is bounded. Thus b⁻ is bounded and supported in |τ|≤R(T) because m(τ) grows like log|τ|. No positivity inside that compact set is assumed.

**Mixture preserving the data.** Write sinc t=sin(t)/t and put H=√G,
    φ(τ)=1−[1−sinc(τ/H)^(2k)]^m,    λ=φ μ+(1−φ)ν.
Here k,m are fixed positive integers. One has 0≤φ≤1 and its transform is supported in [−2km/H,2km/H] by the support of the transform of sinc. For H>2km, the transform of φ(μ−ν) vanishes on |u|<2T, since that of μ−ν vanishes on the enlarged interval. Convolution of a compactly supported distribution with a tempered one is used. Hence λ reproduces the form exactly on the requested window. The atoms in λ are positive.

**Bounding the negative density.** On |τ|≤G/2 the term φC inherits the preceding tail bound. The other term can be negative only up to R(T); there 1−φ=O_(k,m,T)(G^(−m)) by the quadratic expansion of sinc at zero. On |τ|>G/2, for G>2R(T), b is positive and φ≤m |sinc(τ/H)|^(2k)≤m G^k |τ|^(−2k). Thus the negative contribution costs O_(T,k,m)(G^(−k)log(2G)). Taking n=A+3 and k=m=A+1 gives λ≥−C(T,A)G^(−A)dτ as measures. For G below the fixed thresholds it suffices to enlarge the constant using the lower bound for b directly. Plancherel, with its normalization factor absorbed in C, proves the claim.

**Scope.** For the height already verified in the paper one obtains a ceiling on the size of any negative eigenvalue in that window in the original norm. The constant depends on the order A and on T, including R(T); it was not evaluated for any new window. One cannot fix the constant and send A to infinity. The gluing with loss of support refers to spectral measures for the SAME local datum; the attempts at gluing blocks of forms, such as D.74–D.79, do not provide that prior equality. Exact positivity would still require a positive margin that pays for the error, or an exact elimination of the negative part.
