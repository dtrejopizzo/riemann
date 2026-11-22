# Boundary condition of a negative extremizer

In the normalization of 033, if Γ>0 there exists an extremizer u with I(u)=1, and **every** extremizer satisfies

    liminf_{r↑1} (1−r)⁻¹∫ᵣ¹ x|u′(x)|² dx ≥ 1.

The constant is independent of the size of the defect. It is a conditional result on the optimal profile. Antecedents: variational monotonicity in BUILD083 and boundary arguments of 212-36; P46 mentions virial bounds. Here the exact scaling law in the degenerate norm of 033 is used.

**Compactness.** Represent B∞ by a self-adjoint operator A on the energy space X₀ of 033. For fixed L the Galerkin proof of 033 bounds uniformly on the ball the quadratic difference between B_L and its finite compression by 6c_L/M. For self-adjoint operators that bound controls the norm of the difference operator. Hence each B_L represents a compact operator. The cut-difference estimate of 032, transferred to X₀ in 033, gives norm convergence to A. If Γ>0, −Γ is a minimal eigenvalue and is attained by a unit vector.

**Exact compression.** Let Y_r be the image of the energy isometry u(x)↦u(x/r) extended by zero for x>r. The zero moment is preserved. Under U one obtains a translation by log r with amplitude √r; hence B_L and then B∞ are multiplied by r. The infimum of the Rayleigh quotient on Y_r is −rΓ. These closed subspaces grow and their union is dense by the smooth compactly supported zero-mean approximants of 033.

**Cost of the outer layer.** For a normalized extremizer, let P be the energy projection onto Y_r. Put m_r=∫₀ʳu−ru(r)=∫ᵣ¹xu′, by the zero moment and the trace at 1. On (0,r) one has Pu=u−u(r)−2m_r(r−x)/r² and outside it is zero. Indeed it has zero mean and zero trace at r; the residue is orthogonal to Y_r by integration by parts. Membership of the candidate in Y_r is obtained by rescaling and the characterization by finite energy and zero trace at r (in the logarithmic variable, first truncate the derivative in the tail, continue by a constant and cut that constant over an interval of growing length). Writing d²=I(u−Pu) and E_r=∫ᵣ¹x|u′|², one gets

    d²=E_r+2|m_r|²/r²,       E_r≤d²≤E_r/r².

The last bound uses Cauchy–Schwarz against x dx. One has d>0 by comparison of minima and d→0 by density. The unit residue e=(u−Pu)/d converges weakly to zero by orthogonality to the growing subspaces. By compactness B∞(e)=o(1). Writing R for the Rayleigh quotient, the equation Au=−Γu gives, when Pu≠0,

    (1−r)Γ ≤ R(Pu)+Γ = d²(Γ+B∞(e))/(1−d²).

The announced liminf follows. A contradiction would require another property of the arithmetic operator preventing such energy at the boundary. Smoothness alone admits nonzero slope at 1. PROVED (conditional implication), independent mathematical audit.

## Exact boundary law and simplicity of the minimum

Assume Γ>0. Then the smallest eigenvalue of the full form in the norm of 033 is simple. The real unit extremizer can be oriented so that u(x)/(1−x)→1 as x↑1. The claim refers to the normalized problem on X₀.

**Difference of dilations.** Write S_r for the previous isometry and w=S_ru−u. By the eigen-equation, the form B∞+ΓI annihilates the crossings with u. Evaluating it on S_ru one obtains exactly

    B∞(w)+ΓI(w)=Γ(1−r).

In particular I(w)≥Γ(1−r)/(||A||+Γ). The vector w/√I(w) converges weakly to zero: against each smooth compactly supported test φ of zero mean, the energy product with w is the integral of y u′(y) against the conjugate of rφ′(ry)−φ′(y), of order Oφ(1−r) by Cauchy–Schwarz. Pass by density. Compactness of A gives B∞(w)=o(I(w)); hence I(w)/(1−r)→1. On (r,1) the contribution to I(w) equals E_r. The lower bound of the previous section forces E_r/(1−r)→1 and the contribution of the interval (0,r) is o(1−r).

**The mean slope determines the eigenspace.** Let h=−log r and g(t) the derivative of u(exp(−t)) with respect to t. One has h⁻¹∫₀ʰ|g|²→1. The previous interior contribution is equivalent to D(h)=∫₀^∞|g(t+h)−g(t)|²dt=o(h). The variance of g with measure dt/h on [0,h] is

    (2h²)⁻¹ ∫₀ʰ∫₀ʰ |g(s)−g(t)|² ds dt ≤ h⁻²∫₀ʰ D(s)ds = o(1).

Hence |ℓ_h(u)|²→I(u) for every vector of the eigenspace by homogeneity, with ℓ_h(u)=u(exp(−h))/h. For two orthonormal vectors, polarizing would require ℓ_h(u)conj(ℓ_h(v))→0, although both moduli tend to one. This proves simplicity. The form is real by the symmetry of the symbol, so a real extremizer can be chosen. Its quotient ℓ_h is continuous for h>0 and its modulus tends to one; the sign is constant near zero. Choosing the orientation and using h/(1−exp(−h))→1 proves the slope law. It does not require continuity of u′ up to the boundary.

The result uses the structure of compression and compactness; by itself it admits a simple negative minimum. PROVED (conditional implication), independent audit.

Scope control: the model form −||u||₂² on X₀ is compact in I by 033, satisfies the same scaling and has strictly positive defect. The slope law and simplicity also hold for it. Hence a sign argument needs an additional property specific to the arithmetic form. The simple archimedean background of P46 corresponds to another operator.

## What the arithmetic contacts detect in a possible extremizer

For n≥2 let C_n be the operator on X₀ representing the form (2/n) Re ∫conj(u(y))u(y/n)dy. It is bounded by the inclusion in L² and Cauchy–Schwarz. For distinct integers n and real coefficients a_n of finite support, every combination C=Σa_n C_n with some a_n≠0 is injective. This holds without hypothesis on Γ. Injectivity concerns the action of the operator; a single quadratic value may be zero.

Indeed, its logarithmic symbol is q(t)=2Σa_n cos(t log n)/√n. If Cu=0, test the polarized form against S_ru for all 0<r≤1. Up to a factor √r, one obtains the Fourier transform of the real integrable function q(t)|widehat(Uu)(t)|² on a half-axis. By Hermitian symmetry it vanishes on the other, and injectivity of Fourier implies q|widehat(Uu)|²=0 almost everywhere. The distinct frequencies make q an analytic function not identically zero (independence of the exponentials). Its zeros are discrete, hence u=0.

**Consequence for the sign when varying weights.** If Γ>0, take the isolated simple minimum λ=−Γ and a unit extremizer u. Perturb the form as A+εC. The sign chosen for C only fixes the orientation of ε. In any nonzero direction in which λ′(0)=〈u,Cu〉 is zero, one has strictly

    λ″(0)=−2〈Cu,(A−λ)⁻¹ on u⊥ applied to Cu〉 < 0.

Indeed the isolated simple minimum admits a twice differentiable branch for bounded perturbations. Differentiating the eigen-equation with the derivative of the vector in u⊥ one obtains u′=−(A−λ)⁻¹Cu on that subspace when λ′=0. Differentiating λ′ gives the formula. The reduced inverse is positive and Cu≠0. Hence in every finite family of weights the Hessian is negative definite on the kernel of the first variation. That kernel need not have codimension exactly one.

P46 rem:resweights and lem:degen already study sensitivity to weights; here flat directions up to second order are excluded on the carrier of 033. Only injectivity is unconditional. The curvature computation already presupposes a negative minimum and does not decide the sign for the fixed von Mangoldt weights. PROVED after independent audit.
