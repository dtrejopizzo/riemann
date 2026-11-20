# Exact law of the floor with a derivative penalty that may tend to zero

For fixed s>0 add to W_T the energy ε_T ∫ |ξ|^(2s)|F̂(ξ)|² dξ/(2π) of the extension by zero, taking smooth compactly supported unit tests and the infimum (also in the primitive space). Let M_(W,s,ε) and M_(A,s,ε) be the negative parts of those infima. For any 0<ε_T≤1 such that log(1+log(1/ε_T))=o(T),

    lim log(1+M_(W,s,ε)(T))/(2T) = lim log(1+M_(A,s,ε)(T))/(2T) = Δ.

No additional local density condition is imposed on the zeros. For example ε_T=exp(−exp(√T)) is allowed. Eventual non-negativity of any of these penalized forms is equivalent to the global sign of the original form, since RH gives positivity and Δ>0 gives growth of both negative parts.

**Ceiling.** The classical count per unit interval gives D₂(y)≪log(2+|y|). The strip and multiplication part of 117 for κ=1, before imposing the archimedean budget, gives for any unit test −W_T(F)≤B_T ∫log(2+|ξ|)|F̂|² dξ/(2π), B_T=C(1+T)^6 exp(2ΔT), C≥1. After subtracting the penalty, it suffices to maximize over r≥0 the function B_T log(2+r)−ε_T r^(2s). For r≥1 use log(2+r)≤log 3+log r and maximize in r^(2s) explicitly; for r≤1 log 3 suffices. The result is at most C_s B_T[1+log(B_T/ε_T)]. Its upper exponent is Δ by the hypothesis on ε_T.

**Floor.** For each η<Δ choose an intermediate exponent η'<Δ larger than η. The primitive witnesses of 115 are built by adding two translates of the same smooth profile Pg fixed for η'. Their L² norm is fixed when the supports are disjoint, and their homogeneous H^s seminorm is at most twice that of the profile by translation invariance. The additional cost after normalization is O_(s,g)(1), independently of T. In each large window the depth ≥exp(2ηT) for η≥0 is preserved. The full form includes the same witnesses. When Δ=0, RH gives that the negative parts are zero.

**Necessary condition for a larger rate in the original form.** By Jensen, on any unit test of finite quadratic seminorm H_s, ∫log(2+|ξ|)|F̂|² dξ/(2π)≤C_s[1+log(1+H_s)]. If −W_T(F)≥exp(2(Δ+η)T) with η>0, necessarily log(1+H_s)≳_s exp(2ηT)/(1+T)^6 along that sequence. The local regularity in T of 077 for s<1/2 does not provide a bound of this size as T grows. The theorem closes the rate of the penalized problem; removing ε_T at fixed T by density does not authorize exchanging that limit with T→∞ nor does it give the upper bound without penalty.
