# A fixed plateau profile would detect arbitrarily large widths

The conclusion strengthens the order of quantifiers of 029. The new step combines 028 with the central scalar identity of P46 prop:boundary. For each real, even, primitive, smooth, compactly supported F of mass one, it suffices to prove the line inequality of 029 for all D sufficiently large **depending on F**. It even suffices to prove liminf_{D→∞}(line−Φ)≥0 for each F. Both conditions are necessary and sufficient for the global sign.

**Central value.** Let C_F^×(D)=a(F,V_DF) for any real smooth primitive F, and L_F(z) its one-sided transform, initially for Re z>1/2. By 028 it continues along the real axis up to a neighbourhood of the origin. We show L_F(0)=0 for the true comb. The archimedean contribution to C_F^× is the inverse transform of m|F̂|², real, even and integrable in D by the separated kernel estimate of 028. By Fourier inversion its integral over the half-line equals m(0)M²/2, M=∫F.

For the comb part put l=log n and c=c_F even. The one-sided integral of c(l−D)+c(l+D), weighted with exp(−zD), equals

    exp(−zl)P(z) + ∫_{l}^∞ c(v)[exp(−z(v−l))−exp(z(v−l))]dv,
    P(z)=∫ c(v)exp(zv)dv.

The second term is entire and vanishes for l larger than the support diameter of F. Moreover it is zero at z=0 even for the low contacts. With the sign and coefficient of 028, the comb contribution to L_F(0) is thus −S(1/2)M², where S is the real continuation of ΣΛ(n)n^(−s) built in 028. P46 prop:boundary at its central value gives 2S(1/2)=m(0). It is a scalar identity: for Z=η/(1−2^(1−s)), η(1/2)>0 by the pairs of 028; the symmetry s↦1−s of π^(−s/2)Γ(s/2)Z(s) gives zero derivative at 1/2 and, by logarithmic differentiation at that point, the indicated equality. No information about non-real points is required.

**Residue.** Let E_F(D)=a(1_[−D/2,D/2]*F). The triangular kernel identity in 027 gives transform 2L_F(z)/z² in Re z>1/2. It continues locally along the positive real axis and has at most a simple pole at 0, with residue r(F)=2L'_F(0). For F=F₀+εK with support in a fixed compact set and both profiles primitive, r(F) is a quadratic polynomial in real ε. This follows by polarization: the quadratic identities of the transforms in the convergence zone persist under continuation and extraction of residues.

If the sign fails, take G odd smooth compactly supported primitive with q=a(G)<0 as in 028, and F₀=G'. Then E_{F₀}(D)=2q−2C_G^×(D), so its transform is 2q/z−2L_G(z). Hence r(F₀)=2q<0. For an even primitive smooth K of nonzero mass built in 029, choose **once** ε≠0 sufficiently small. The profile F₀+εK keeps r<0. Normalizing its mass to one multiplies the residue by a positive factor. F stays fixed in the rest of the proof.

**From the residue to real energy values.** One has liminf_{D→∞}E_F(D)≤r(F). Indeed, if eventually E_F≥h with h>r(F), the tail of E_F−h is nonnegative. Its transform has local continuation on the positive axis and residue r(F)−h<0 at 0; removing a compact interval only subtracts an entire function. By the Taylor argument with positive coefficients of 028, its Laplace integral converges at each positive real z: a strictly positive abscissa of convergence would contradict the regularity there. It then equals what the continuation gives, by uniqueness. The product of that integral by z is nonnegative for z>0 and its limit at 0 would be negative. This proves the liminf inequality without identifying in general the integral with its continuation at 0 nor claiming an ordinary limit in D.

For the fixed F above, S_D(F) of 029 tends to zero. Thus liminf(line−Φ)=liminf E_F≤r(F)<0 and there are violations with fixed margin at arbitrarily large widths for the same profile. In the direct sense, the global sign gives line−Φ=E_F+S_D(F)≥0 for each D larger than the diameter. The proof also shows that r(F)≥0 for every even primitive profile of mass one is an equivalent criterion: in the direct sense use liminf E_F≤r(F) and E_F≥0; the previous construction gives the converse. Nonnegativity of those residues remains open. PROVED after independent mathematical audit.

**Distinction of the altered weight.** When replacing Λ by cΛ with c constant, the central value of the transform of the crossing becomes (1−c)m(0)M²/2. For M≠0 and c≠1 a term (1−c)m(0)M²/z² appears in the transform of the energy. For the control c=1.1 its coefficient is positive. The simple residue then no longer decides the contradiction used here. This identifies an exact dependence on the arithmetic normalization; it does not exclude other weight modifications sharing the same central value.

## Negative control with any finite number of exact central derivatives

For each fixed integer m≥0 there exist nonnegative weights that differ from Λ on a finite set of prime powers, coincide with its continued series S and all its first m derivatives at 1/2, and give strictly negative energy to the certified test of BUILD084 (16)–(17). The modification depends on m. P46/P48 thm:finmod are direct antecedents; here a modification that exactly matches central derivatives must compensate the low changes before concluding. No additional Euler law tying together the weights of all powers of a prime is imposed.

First add 0.1Λ(n) for 2≤n≤257; this reproduces all the contacts of the test of BUILD084 and its proved negative energy for 1.1Λ. For j=1,...,m+1 take only primes p in [exp(jR),exp(jR+1)], with R large. Let B_j=Σ_p (log p)/√p over block j. By PNT for primes, B_j→∞. For k=0,...,m let V_kj be the mean of (log p/R)^k over the block with weights (log p)/(√p B_j). Since j≤log p/R≤j+1/R, V converges to the Vandermonde matrix (j^k), invertible. Solve exactly over the reals

    Σ_j V_kj u_j = − Σ_{2≤n≤257} 0.1Λ(n)n^(−1/2)(log n/R)^k.

The right-hand side is bounded with m fixed, so u_j=O_m(1). In block j add (u_j/B_j)log p to each weight. All remote relative modifications tend to zero and the weights remain nonnegative. No remote contact enters the support of the test. By construction, the difference of series is a Dirichlet polynomial with derivatives of order 0,...,m exactly zero at 1/2; it suffices to multiply equation k by (−R)^k. The control on the test of the original form with modified weights is proved.

In particular the central cancellation of 030 is preserved, while the sign fails for these weights. The identity distinguishes the uniform 1.1Λ control, but even all central data up to a prescribed finite order are compatible with a negative direction. This does not decide the sign of r(F) for Λ; nor is a single modification built that preserves derivatives of all orders. PROVED after independent mathematical audit.

## Identification of the residue with the kernel of D.52

We use g with the sign of (2.1) of 114_d_52_CONTINUOUS_SCREW_KERNEL_PRIMITIVE_BRIDGE, coinciding with (1.3) of Suzuki in the local copy of 2606.09096v3. For the real primitive profile F of 030, c=c_F and M=∫F, one obtains

    r(F)=2∫_ℝ c(v)g(v)dv + [ (1/2)Σ_{k≥0}(k+1/4)⁻² −16−2S'(1/2) ] M².

To verify it, differentiate at zero the entire term of each low contact of 030. Since P is even, the arithmetic part of r is

    −2M² S'(1/2) + 4 Σ_n Λ(n)/√n ∫_{log n}^∞ (v−log n)c(v)dv.

By support the sum is finite. It is exactly the contribution of the ramps of D.52 to the pairing 2∫cg, plus the central term written. For the archimedean side, the expansion of m in P46, thm:S(i), uses a=k+1/4 from k=0. The box computation of 027 applied to that symbol gives constant term

    −m(0)∫|v|c(v)dv + (1/2)Σ_{k≥0}a⁻²∫ exp(−2a|v|)c(v)dv

in the archimedean energy for large D, after removing m(0)M²D; the remainder decays exponentially. This constant is 2L'_arch(0) by the triangular Laplace identity. In 2∫cg the same terms come with −(M²/2)Σa⁻² by the Hurwitz–Lerch constant in (2.1). The polar term of g contributes 16M² since ∫exp(±v/2)c(v)dv=0 and ∫c=M². This fixes the full adjustment, even for nonzero mass. All the previous series of constant terms converge absolutely.

The antecedent D.52 (3.6) already identifies the form on antiderivatives in the zero-mass sector. The formula identifies in what sense 030 extends that same object to nonzero mass. Re-examining the sign of the pairing under the name of residue would repeat the kernel problem already recorded in D.134 without an additional inequality.
