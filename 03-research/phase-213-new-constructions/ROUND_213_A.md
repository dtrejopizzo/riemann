# Centring changes the stability of the critical cut

At fixed rate u≥3 use v*, a*, l and c_N from 212, α=a*−1/2. Set L=Nv*−κ√N. For sufficiently small positive κ, the centred short sum

    S_N(L)=Σ_{p≤exp L} (log p)c_N(log p;u)/√p − ∫₀ᴸ exp(t/2)c_N(t;u)dt

reproduces the infinite prime sum with error o(1). At this same scale the cut error of the uncentred sum has magnitude at least C exp(ακ√N)/√N for one of two bounded shifts in L for each large N. Both results allow fixed u outside the verified band. The first also preserves the rational-rate criteria of 208–209.

**Error after centring.** The quantitative PNT used in R161_078 gives |θ(x)−x|≤Cx exp(−c√log x) for some c>0 (passing from ψ to θ costs O(√x log² x) counting powers). Integration by parts on (exp L,∞) against d(θ−x) and the envelope of 212 for c_N and its derivative give, including the endpoint,

    |centred tail| ≤ C_u N^(−1/2) exp(Nl(a*)−αL−c√L).

Indeed, in the integral exp(−c√t) is dominated by exp(−c√L) and exp(−αt) is integrated. It suffices to choose 0<κ<c√v*/α. The estimate remains valid with any bounded shift. The complete continuous integral is H(i/2)^N−∫₀^∞ exp(−t/2)c_N(t;u)dt by symmetry and the inversion of 208. The first term decays and the second is O_u(1/√N) by 211. This proves the comparison with the uncentred infinite prime sum.

**Uncentred error at the same endpoint.** In the formula of 212 use a=a*, t=Nv*−κ√N+d. The phase exp(iNθ+ix_a(d−κ√N)) is preserved, and the coefficient K is multiplied by exp(−κ²/(2Q)), Q=−h''(x_a+ia), with positive real part. Indeed, on rescaling the peak by w=√N(x−x_a), the factor exp(−iκw) remains inside the Gaussian; its integral gives exactly that nonzero multiplier. The same domination as in 212 justifies the limit for each fixed d. Integrating in d=c₀+r, r≥0, with majorant C exp(−αr), the denominator α−ix_a of the continuous tail is recovered and the centring above allows dx to be replaced by dθ. The shifts c₀=0,π/(2x_a) again give phases in quadrature, and the unnormalised exponent is ακ√N−αc₀. Hence the announced floor for the maximum of the two tails. This floor by itself does not exceed root rate one.

**The exceptional slope of 212 also fails for stability under shifts.** For a=1/2 and v=l'(1/2) the domination on a half-line is lost. Compare instead TWO consecutive increments of the initial cut, on the logarithm intervals [Nv+jD,Nv+(j+1)D], j=0,1, with D=π/(2x_a); use the left-open convention. PNT by parts on these intervals of fixed length gives error o(exp(Nl(a))/√N) with the envelope of 212. The profile there, after multiplying by exp(t/2), has common coefficient K exp(iNθ) and phases exp(ix_a d). The integrals of these phases over the two intervals differ by the factor i, and the first equals (i−1)/(ix_a)≠0. Therefore one of the increments, and with it at least one of the THREE initial cuts, has modulus ≥C exp(Nl(1/2))/√N. This completes the obstruction under shifts for all interior slopes of 212, without determining which of the three endpoints wins for each N.

**Scope.** Centring already appears in 208 and the quantitative PNT in phase 161. The simultaneous comparison of a stable centred cut and an unstable uncentred cut uses the new boundary scale of 212. The proved saving in log X is sublinear; the estimate does not dominate the centred sum that remains below the cut. It does not provide a new window T.
