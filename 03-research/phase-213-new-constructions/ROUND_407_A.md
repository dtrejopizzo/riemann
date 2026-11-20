# Removing a critical pair from the average while keeping positive weights

**Status: PROVED, with independent review of the parity, the differential equation and the variance.**

Fix γ>0 with ξ(1/2+iγ)=0 verified, and use the normalization Φ of 406. The multiplier

    U(s)=ξ(s)/(1+(s−1/2)²/γ²)

is the centered bilateral transform of a strictly positive even kernel Φ_γ. It has the same mass as Φ and its normalized variance is exactly smaller by 2/γ². The negative average of 406, including the truncation stated there, persists with Φ_γ. The result uses a single pair, without presupposing the location of the others.

**Real construction.** For v≥0 take Φ_γ(v)=γ∫₀^∞ Φ(v+t)sin(γt)dt and extend by parity. We use the classical strict monotonicity of Φ on the positive half-line; it also follows from the convexity of Φ(√t) and its zero limit. [Csordas, Convexity and the Riemann zeta-function](https://web.math.pmf.unizg.hr/glasnik/33.1/33105.pdf). Pairing two consecutive half-periods of the sine gives a positive integral by the difference Φ(v+t)−Φ(v+t+π/γ). The derivative at zero equals −γ²∫₀^∞Φ(t)cos(γt)dt=0 by the verified zero. Thus the even extension is C² and differentiating the integral one obtains Φ_γ''+γ²Φ_γ=γ²Φ on the whole line. By the doubly exponential tail, integration by parts proves the identity of transforms, even at the points removable by continuation. At s=1/2 the quotient preserves the mass. Its second derivative divided by that mass subtracts 2/γ² from the second moment, which coincides with the variance by parity.

**Application to the pulse.** After multiplying by F=1/ζ, the quotient remaining in the integral of 406 is s(s−1)π^(−s/2)Γ(s/2)/(2(1+(s−1/2)²/γ²)). Its two possible poles are on Re s=1/2, strictly to the left of α. On α≤Re s≤1+1/L the inverse of the denominator costs O_γ(b) by the distance α−1/2≍1/b to the two poles, and at large heights it decays. At the real saddle the new relative factor tends to one. This preserves the equivalent −ξ(1/2)T₀ without RH, with the same domination of 367. The truncation cost remains negligible by Φ_γ(v)≤γ∫₀^∞Φ(|v|+t)dt and the bound of 406. The quantified reduction is in variance, not in the guaranteed length of the window of 406.

**Review record.** [Theorem2.1(v) of Csordas](https://hrcak.srce.hr/en/file/12426) states the strict monotonicity directly; its normalization is related to that of406 by Φ(v)=2Φ_Csordas(v/2), so the sign is preserved. The critical vanishing gives ∫₀∞Φ(t)cos(γt)dt=ξ(1/2+iγ)/2=0 and hence Φ_γ'(0)=0. The equation Φ_γ''=γ²(Φ−Φ_γ) makes the second derivatives of the even extension coincide; by regularity of the equation it is even smooth. Integrating twice by parts with the centered exponentw=s−1/2 produces(w²+γ²)U=γ²ξ, confirming the plus sign of the denominator. Atw=0 the second derivative subtracts exactly2ξ(1/2)/γ², that is2/γ² from the normalized variance.

The product F·U may keep simple poles at1/2±iγ, although the division is removable inU. Both lie strictly to the left ofα; they are not crossed when coming down from1+1/L. In that strip the inverse of the denominator is O_γ(b) and only produces a polynomial factor absorbable by the phase loss. The tail ofΦ_γ and its first derivatives allows the same truncation as406, at frozen cut.

**Obligation for iterating.** The positivity of Φ_γ is proved. To apply the same half-period argument again to another zero one would need to justify, for example, that Φ_γ is still decreasing on the whole half-line. The previous formula does not establish it. [408](ROUND_408_A.md) settles that obligation for a selection of sufficiently high zeros, without proving concentration. Nor is the negativity of the average converted into pointwise negativity.
