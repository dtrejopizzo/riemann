# What the derivatives of the integrated deficit detect

**Status: PROVED, with independent review of the Laplace inversion, the oscillatory coefficient and the gamma limit.**

For the D of 412 let F(s)=D(√s)/√s. If the critical line has been verified up to height H≥2, then for all s>0

    (−1)^n F^(n)(s) ≥ 0 if (n+1) 2 arctan(1/(2H)) ≤ π/2.

With H=3·10¹² this includes all integer orders from 0 to 4.7·10¹². If there is an exterior zero, the inequality fails at some positive s for each sufficiently large n.

**Proof.** For each upper zero, counted with multiplicity, set d=|Re ρ−1/2|. Integrating twice the identity of 414 one obtains F(s)=4Σ∫₀ᵈ(d−u) Re[1/(s+(γ+iu)²)]du. The argument of the denominator is at most 2 arctan(u/γ); differentiating n times, its reciprocal is raised to n+1 and multiplied by (−1)^n n!. The local convergence of the differentiated series follows from Σγ⁻²<∞.

The inverse Laplace density is

    K(t)=4Σ∫₀ᵈ(d−u) exp(−(γ²−u²)t) cos(2γut)du.

It is continuous for t>0 by local uniform convergence. The integral of the series of absolute values is finite by Σ d²/(γ²−1/4)<∞, justifying the interchange of integrals. If there is an exterior zero, take the minimum A of γ²−d² among them. Finitely many zeros attain it and there is a positive jump to the remaining ones, by local finiteness. Their remaining contribution is O(exp(−(A+ε)t)) for t≥1, summing first at t=1.

For each minimizer substitute v=t(d−u). After multiplying by t² exp(At), its contribution is
4 Re[exp(−2iγdt)/(2d−2iγ)²]+o(1), by dominated convergence with majorant 4v exp(−dv). At fixed A, the frequency 2γd determines γ and d because (γ+id)²=A+2iγd. The multiplicities add up. The resulting trigonometric polynomial has mean zero and positive mean square. Since it is bounded, the lower mean of its absolute value is positive; both sign parts therefore have positive lower mean. Thus K takes strict values of both signs at arbitrarily late times.

Fix t₀ with K(t₀)<0. The derivative of order n with alternating sign, at s=(n+1)/t₀, has the sign of the integral of K against the gamma density proportional to tⁿ exp(−st). These densities have mean t₀ and variance t₀²/(n+1). Outside any fixed neighborhood of t₀ their supremum tends to zero by unimodality and Stirling; there the L¹ norm of K suffices. By continuity the integral converges to K(t₀).

**Review record.** The identity of412 gives J_R''(u)/R=4Re[1/(R²+(γ+iu)²)], confirming the factor4 inF and inK. The argument of the denominator at s>0 does not exceed2arctan(u/γ); hence the condition on n+1, and not on n, guarantees the sign. TheL¹ norm ofK is finite by the majorant2Σd²/(γ²−1/4), while its continuity is only needed for t>0; K is not presupposed bounded at0.

At the minimum A, the change v=t(d−u) gives exactly t²exp(At)K_ρ(t)=4Re[exp(−2iγdt)∫₀^(td) v exp(−2dv+v²/t+2iγv)dv]. Domination byv exp(−dv) leads to1/(2d−2iγ)², with the announced sign and coefficient. The reflected zeros with the sameγ and|δ| add their multiplicities; they do not cancel this frequency. Different minimizers with the sameA have different2γd except for that duplication, since the square root ofA+2iγd fixesγ,d>0. The positive mean square and zero mean give positive and negative values bounded away from0 for the polynomial at arbitrarily late times, sufficient to absorb the remaindero(1) and the later exponents.

Normalizing tⁿexp(−s_nt), s_n=(n+1)/t₀, gives the gamma density of shape n+1, mean t₀ and variance t₀²/(n+1). By Stirling its supremum outside a fixed neighborhood of t₀ tends to0; multiplying it by theL¹ norm ofK controls even the zone near0. In the neighborhood continuity is used. Thus the gamma average converges toK(t₀)<0 for all sufficiently large n, and not only along a subsequence. This proves exactly the eventual failure of each high order if there is an exterior zero, without contradicting the finite range guaranteed byH.

**Scope.** Phase 101 already records abstract criteria of complete monotonicity. Here the oscillatory term that prevents extrapolating the finite orders for the specific deficit of 412 is identified. Complete monotonicity of F is equivalent to RH, since under RH F is identically zero. An independent bound on the contribution of the ordinates remains open. Positivity of all iterated dyadic differences does not follow from 414.
