# Mellin zeros of a possible negative extremizer

If Γ>0, the Mellin transform U(s)=∫₀¹ u(x)x^(s−1)dx of any extremizer of 034 has, in Re s>1/2, exactly one zero: s=1, of order one. This is the transform of the profile; the conclusion does not concern the zeros of ζ.

**Cross-check.** P47, proof of thm:nyq-cone, already reflects a zero to preserve the autocorrelation. The compactification of 033 uses the special factor s/(s−1). The reason for using the operation here is that the arithmetic energy and the norm that normalizes its defect are measured on two different lines. Preservation on one produces a strict improvement on the other.

**Admissible reflection.** Let g(t) be the derivative of u(exp(−t)) for t≥0, extended by zero to the rest of the line. Its squared L² norm equals I(u). Since u(1)=0, the primitive of g from zero is u(exp(−t)) and grows at most like √t ||g||₂. By integration by parts its Laplace transform satisfies G(s)=sU(s) in Re s>0. Let z be a zero of U with b=Re z>1/2. Define on the line

    h(t)=−∫ₜ^∞ exp(z(t−v))g(v)dv,     g₁=g+(2b−1)h.

The convolution kernel of h is in L¹. Moreover h(t)=−exp(zt)G(z)=0 for t≤0 and h′=zh+g. Hence h belongs to H¹ and g₁ is causal and belongs to L². Integrating g₁ from zero defines a profile u₁ in X according to the characterization of 034 (zero trace at x=1 and finite energy). Transforming the equation of h, its Laplace factor is 1/(s−z), with a removable singularity in the product with G. Consequently

    U₁(s)=U(s) (s−1+conj(z))/(s−z).

If z≠1, U₁(1)=0 is preserved. If z=1 it suffices that the original zero have order at least two. In both cases u₁ belongs to X₀.

**Two norms.** On Re s=1/2 the factor has modulus one, so the integrals B_L of 033 are identical and so are their limits B∞. On Re s=0, where Plancherel for g gives I, the square of its modulus at iτ is

    [(b−1)²+(τ−Im z)²]/[b²+(τ−Im z)²] < 1.

This boundary multiplier identity is also obtained by Fourier transforming h′=zh+g. Since g is not zero, I(u₁)<I(u). If B∞(u)=−Γ I(u)<0, the quotient of u₁ would be strictly below the minimum. Complex profiles in X₀ are allowed; the minimum of a real form does not change under complexification either. This excludes every proposed zero except the simple zero at 1, which is mandatory because of the mean.

**Consequence for real moments.** Orient the real unit extremizer as in 034. Then U(s)>0 for real s greater than 1 and U(s)<0 for 1/2<s<1. Indeed u(exp(−t))/t→1 as t↓0 and |u(exp(−t))|≤√t. Integrating against exp(−st) and separating a neighbourhood of zero and its exponential tail gives s²U(s)→1 as real s grows. Continuity and the simple zero at 1 give the indicated signs. These constraints describe a hypothetical extremizer; an arithmetic inequality that excludes it remains pending.

Proof of reflection and membership in X₀ independently reviewed. PROVED as a conditional implication.

## A uniform strip including the middle line

Let λ₊=sup B∞(f)/I(f) over nonzero X₀. It is finite by 033 and nonnegative by compactness in infinite dimension. Under the hypothesis Γ>0, every zero z of U in Re z>0, except the mandatory simple zero at 1, satisfies

    Re z ≤ λ₊/[2(λ₊+Γ)].

Thus the minimal distance from any optional zero of the right half-plane to the middle line, on its left, is Γ/[2(λ₊+Γ)]. It is a bound depending on the hypothetical defect, with no unconditional numerical margin.

**Proof.** Write b=Re z. Use the causal convolution h of the first part, which only requires b>0. Its primitive in the logarithmic variable defines v∈X and the Mellin transform of v is V(s)=U(s)/(s−z). If z≠1 the zero mean is preserved. The same happens at z=1 if the zero is multiple. The vector v is not zero. On the middle line U=(s−z)V and the hybrid multiplier is real. Hence the real part of its polarized form satisfies Re B_L(u,v)=(1/2−b) B_L(v). Pass to the limit by 032–033. On the line Re s=0 use the transforms of the derivatives in log, related by the same factor (equation h′=zh+g). Plancherel gives Re I(u,v)=−b I(v). The extremizer equation Au=−Γu implies exactly

    (1/2−b) B∞(v) = Γ b I(v).

For b=1/2 this is impossible. For b>1/2 the quotient of v would be strictly less than −Γ. For 0<b<1/2 the quotient is positive and at most λ₊, which gives the bound. The argument only divides by s−z removably in the profile, even if z lies on the line of integration. PROVED as a conditional implication, with independent audit.

The alternative decomposition of moduli of rational numerators into sums of squares was cross-checked with POWER_SCALAR_BRIDGE_017 and its audit. Since it returns to a sign problem in a family of numerators, it was discarded as a closing route for this round.

The closest antecedent found for testing the eigen-equation against a quotient is R160_X_C1 §5, Theorem G; its §6 studies exclusion of zeros of extremizers by Blaschke (audit R163_501 §§1–2). The difference here is the quantitative bound obtained by evaluating the same quotient on two different lines. It does not incorporate a new inequality for the von Mangoldt weights.

## Filters with a pole on the left: exact value of the minimax problem

Let a>0 be fixed. For u∈X₀ with Mellin transform U and real γ define vγ by Vγ(s)=U(s)/(s+a−iγ). In the variable of the logarithmic derivative this is convolution with exp((−a+iγ)t)1_{t≥0}, in L¹. Hence vγ belongs to X and preserves the zero mean. For u≠0 it is always nonzero. Write R=B∞/I, λ₋=inf R and k=a/(a+1/2). Then

    inf_{u≠0} sup_{γ∈ℝ} R(vγ) = k λ₋.

In particular, if there is a negative extremizer, *each centre* gives the same negative quotient kλ₋ when filtering that extremizer.

**Equation and average.** For Au=λu, the same two-line computation of the previous section gives (a+1/2)B∞(vγ)=λ a I(vγ) without assuming any zero of U. In general integration in γ gives

    ∫ I(vγ)dγ = (π/a) I(u),      ∫ B∞(vγ)dγ = [π/(a+1/2)] B∞(u).

The first equality follows by Plancherel and the integral of the Cauchy kernel. For the second fix the cut L and apply Fubini (the integral with |h_L| against |U|² on the middle line is finite). Pass to B∞ using the norm convergence of the forms and the first equality. The average of R(vγ) with weight I(vγ) thus equals kR(u); in particular the supremum is at least that value. The minimax equality is obtained by evaluating at a minimal eigenvector when it exists. If λ₋=0 is not an eigenvalue, compactness provides eigenvectors with eigenvalues tending to zero, and for each one the filtered quotient is constant in γ.

**Sign obligation.** For a fixed width a, it would suffice that for each u≠0 there be some centre γ with B∞(vγ)≥0. Indeed, a negative minimum would provide a strictly negative family at all centres. Conversely, global positivity implies that condition. The minimax identity quantifies the equivalence; it does not prove the existence of the favourable centre. In particular the compact model B(u)=−|U(1/2)|² has a negative minimum and satisfies the same identities (evaluating U(1/2) is continuous on X₀ and not identically zero there). The averaging formula in this model is checked directly at s=1/2. Positivity of the Cauchy kernel alone does not certify the original weights.

Cross-check: R160_X_C1 §5 and the filters of POWER_SIGNED_TRANSFER_014 and POWER_SCALAR_BRIDGE_017 anticipate the use of quotients. The minimax value in the norm of 033 is the specific claim here. Identity and limitations independently audited.

## What is lost by applying the filter twice

Let u be an eigenstate with eigenvalue λ and let v_j be the profile with Mellin transform U(s)/(s+a−iγ)^j for j=1,2. Put d=a+1/2, B_j=B∞(v_j), I_j=I(v_j). The exact identity holds

    B₂ = λ [ (a²/d²) I₂ − I₁/(4d³) ].

Indeed Re B∞(u,v₂)=2d²B₂−B₁: on the middle line the real part of the quadratic factor is 2d²−|s+a−iγ|². The equality passes from each finite cut by continuity. On the energy line one similarly obtains Re I(u,v₂)=2a²I₂−I₁. Use the eigen-equation and B₁=λ(a/d)I₁. Thus, for λ<0, the double filter produces positive energy exactly when I₁/I₂>4a²d. A positive energy obtained after two filters is therefore compatible with a negative minimum.

**Verification of that possibility in a real model.** In the same X₀, let e_y be the unit representative of evaluation of the Mellin transform at s_y=1/2+iy, with e_{−y} the conjugate of e_y, and P_y its rank-one orthogonal projection. Consider A₀=−P₀+(P₄+P_{−4})/8. It is compact, real, and each evaluation form scales by r under S_r. To compute the normalized products, in logarithmic-derivative coordinates evaluation at s is the integral of g against exp(−st)/s and the zero mean removes the direction exp(−t). The projected Gram of two evaluations s,w is, up to conjugation convention,

    [(s−1)(conj(w)−1)]/[s conj(w)(s+1)(conj(w)+1)(s+conj(w))].

After normalizing, |〈e₀,e_{±4}〉|²=1/17. The test e₀ gives energy −1+1/68<0 and the negative part has rank one, so the minimum is simple and admits a real eigenvector u. Let −l be its eigenvalue (0<l≤1), α its normalized evaluation at 0 and b the vector of normalized evaluations at ±4; |b₊|=|b₋|. Evaluating the eigen-equation at those two frequencies gives (l Id+G/8)b=αc, with G the Gram of e₄,e_{−4} and ||c||²=2/17. Since ||G||≤2 one deduces |b₊|²/8≥2|α|²/(25·17). Here α≠0 by the negative energy.

Take a=1/2 and γ=4. The double filter multiplies the negative term by 1/289 and leaves the positive term at +4 intact. Since 2/(25·17)>1/289, the energy of the double filter is strictly positive, while that of the first is strictly negative by the eigenstate identity. The two-line identities are exact also in this three-evaluation model. The countermodel preserves real symmetry and scaling. It does not use the von Mangoldt weights; it distinguishes the global criterion with one filter from an invalid extrapolation to two. 

Antecedent for the caution about iteration: POWER_PRIME_TRANSFER_014 §4 observes that applying the first filter changes the input datum. The identity of the second filter and the exact bounds of the symmetric model received independent mathematical review.

## What a large frequency centre really detects

Fix a>0 and suppose g(t)=(d/dt)u(exp(−t))∈H¹(0,∞). Write c=g(0), the trace from the right. With the first filter above one has, as |γ|→∞,

    γ² B∞(vγ) → B∞(u),        γ² I(vγ) → I(u)+|c|²/(2a).

This regularity is not presupposed for an extremizer of 034. It does include all smooth compactly supported tests in (0,1), which are dense after imposing the zero mean.

**Proof.** If G(it) is the Fourier transform of g extended by zero, the error in the logarithmic derivative of (−iγ)vγ−u has transform −(a+it)G(it)/(a+i(t−γ)). Split g=c exp(−at)+g₀ on the half-line. The first term produces exactly −c exp((−a+iγ)t)1_{t≥0} in the derivative of the error. The second satisfies g₀(0)=0, so its extension by zero is in H¹ of the whole line. Its numerator is in L² and the denominator has modulus ≥a and grows pointwise. By dominated convergence its contribution tends strongly to zero. The exponential term converges weakly to zero by Riemann–Lebesgue and has squared norm |c|²/(2a). This proves the second limit and the weak convergence of (−iγ)vγ to u in X₀. Compactness of the full form of 034 gives the first limit, including all arithmetic weights.

**Scope for the sign.** If a negative test exists, by continuity and density there is a smooth compactly supported negative one. For that test and any fixed width, all centres of sufficiently large modulus have strictly negative filtered energy. Hence, proving that for every smooth negative test there is a favourable centre would require controlling centres in a bounded interval that may depend on the profile. The limit does not predict a sign change in that interval. With c=0 one even recovers the quotient R(u) by sending the centre to infinity. PROVED after independent review.
