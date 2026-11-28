# Equality of multiplicities: deep audit in progress

## Literal failure in `pm:siegel(c)` of paper 51

**Verdict (b) for the assertion of uniform convergence for all g.** The first incorrect assertion is at `main.tex:4453`; it is repeated in the last sentence of its proof, lines 4511–4512. This is not a counterexample to the multiplicity theorem.

The lemma asserts that, with x in a compact set, the series

`Σ_{γ∈G(F)} M_{B′}(g⁻¹γx)`

converges uniformly with respect to g on all of G(A_F). Take x=1 and choose the compact set Ω_f containing 1, as the statement allows. For any finite set J of indices, choose γ₀ outside J and put g=γ₀. The non-negative tail is then at least

`M_{B′}(g⁻¹γ₀)=M_{B′}(1)=1`.

By the uniform Cauchy criterion, the tails do not tend uniformly to zero. There exist infinitely many γ₀ in the isotropic case of this section, for example in a non-trivial rational unipotent subgroup.

The earlier estimate of the lemma, uniform in g for the **total sum**, does follow from the argument of disjoint sets. That estimate does not imply uniform convergence of the tails: as g varies, the large term can move to any index.

## Repair and scope

Replace the conclusion by uniform convergence when **both g and x range over compact sets**. In the proof by disjoint sets a fixed neighbourhood U can then be chosen. For g and x in compact sets, the sets g⁻¹γxU corresponding to γ outside a finite set escape uniformly from any compact set. Their sum is dominated by the integral of the integrable function M′ outside that compact set, which tends to zero. The discreteness of G(F) makes finite the set of γ that do not escape.

This suffices for local continuity of the sums of `pm:bound(a)` and of the function F of `pm:bound(c)`. The global bound in g of the total sum, which remains valid, provides the integrable majorant on convolving with e∈L¹ at 4587–4589. Hence those applications do not need the false assertion of global uniform convergence.

## Additional checks of this pass

- `pm:kernel(c)`: the Cartan density is bounded by exp(n(n−1)t₁); integrating the remaining parameters introduces only a polynomial factor. B′>n² suffices for integrability.
- `pm:kernel(a,b)`: the idempotence uses Schur orthogonality with the formal degree. The construction of α uses a finite space of K-types and the density of smoothed vectors, so that membership of the closure implies membership of the subspace. It does not require an inverse of an infinite operator.
- `pm:cusp`: once the Harish-Chandra projection and its finiteness over the centre are admitted, the constant integral satisfies an ODE with constant coefficients along A′. The decay in both directions excludes every non-zero exponential polynomial. The exponent B=5n³ satisfies the integrabilities and the margin B/2>2n² for n≥2.
- `pm:decay`: the oscillation argument uses the global bound of F, the vanishing of its constant term and the weighted supremum C*. The inequality C*≤max(C*/2,T(δ/ε₀)^j) gives the conclusion without requiring the supremum to be attained.

These verifications do not yet close `pm:main`: in this pass the comparison of elliptic classes, the elimination of the auxiliary place and the complete collation of the archimedean inputs are missing. They are recorded separately from the preceding repair.

## Second pass: comparison and elimination of the auxiliary

Lines 4640–5029 were reconstructed. The comparison and the elimination of the auxiliary are correct as a deduction from `pm:arch`, from the classical inputs of class field theory and Hermitian classification cited, and from (G). The preceding uniformity correction suffices for the uses of the kernel in this deduction.

1. **Polynomials with coprime factors (`pm:red`).** The Bézout projector varies continuously and provides local sections of the space of decompositions. The function Ψ on H×X has compact support: the diagonal components m lie in a compact set, and the inverse of z↦m₁⁻¹zm₂−z remains bounded there because the coprime characteristic polynomials were fixed. The integration over N annihilates Ψ by supercuspidality. It is not presupposed that the factors are locally irreducible. For proper powers, the reduction cannot have a simple zero: it is exactly the obstruction used by (Z).
2. **Rational classes (`pm:classes`).** The quotient c₁/c₂ is a norm at all finite places by local conjugation, and at the infinite ones by equality of signs. The Hasse norm theorem for the quadratic extension gives rational conjugation. To change signs, the product condition is (−1)^{f(q+q′)}=1; f even guarantees it. The kernel of the Artin symbol gives an x with those signs and xN(z)=1 at the finite places. Landherr identifies V_{cx} with V′. Thus one obtains the product of finite classes by **all** the admissible choices of signs, and not simply an injection.
3. **Roots off the circle (`pm:selberg`).** The eigenlines of modulus greater than one form a non-zero isotropic subspace. On the radical of the parabolic stabilising it, Ad(γ)−1 is invertible. The triangular change in the unipotent group reduces the orbital integral to the constant term of e, zero by `pm:cusp`. The absolute convergence comes from `pm:bound(b)` before the unfolding; the text treats expressly the vanishing factors of the absolute integral.
4. **Sign and measure (`pm:ell`).** The infinite torus has mass 1; hence the integral over G in `pm:arch(b)` agrees with the orbital integral over T\G. Each assignment of signs appears p!q! times in S_n, a factor that cancels. The final sign is (−1)^{pqf}=1. The adelic volume of the torus and the finite orbital integrals are identified by L, independently of V. The separate treatment of the vanishing compact character avoids cancelling a factor that could be zero.
5. **Linear algebra of the auxiliary (`pm:line`).** Even if A is not normal, each of its generalised eigenspaces is invariant under T and T*, because A commutes with both; hence it is a reducing subspace of T and the restriction of T* is indeed the adjoint. The positive powers of T determine its eigenvalues and multiplicities because T is invertible. The determinant of TT*=d(1+cε) recovers the rank of ε. The space corresponding to α=0 does not contribute to tr(Aε); there is no need to recover that block.
6. **Hecke computation (`pm:hecke`).** tJt⁻¹ imposes the row condition opposite to the column condition of J. There are two double cosets J\K/J. The value at 1, vol(J)q^{n−1}, and the total integral determine the second value vol(J)q^{n−2}(q−1). From this comes exactly TT*=q^{n−2}(1+(q^n−1)ε). The powers of JtJ kill the first line modulo the uniformiser and are invertible on the quotient; the zero of the reduced polynomial remains simple.
7. **Application of the auxiliary.** The place u is chosen outside the support and different from the supercuspidal place. The convolution powers preserve supercuspidality by Fubini. The equality of traces of A^lT^i allows `pm:line` to be applied and the projector of maximal level to be recovered, with the same factor vol(K) in both groups.
8. **Passage to the data.** A good family has at least one irreducible label, the one supplying the supercuspidal component. The proof of (G) reduces cuspidality to the absence of the simplex of degree r in products of characters of smaller ranks; it is correct if the Green identities expressly cited are admitted. I do not attribute here a check of Green's original facsimile. The equality of traces for the commutative algebra stable under adjoints determines the multiplicities by independence of characters. The extension to inert places of `pm:rem-full` uses the freedom of the function outside the supercuspidal place; it does not wrongly apply the identification with GL_n at an inert place.

**Delimited pending item:** close the archimedean input `pm:arch` (decay and orbital sum) with its dependencies on discrete series and check against the documents the classical formulations cited. Equality of multiplicities is not asserted for two arbitrary groups merely because they are isometric at finite places: the conditions on parameters, types and supercuspidal component are essential in the audited proof.

## Third pass: orbital integral and formal degree

The arguments from `pbr:basic` to `pbr:degree`, lines 5199–5833, were reconstructed. The internal deduction of the orbital integral and of the constant of the formal degree is correct **conditional on the discrete series inputs and on the coefficient formulas of paper 49 declared in R1–R4**. The audit of those inputs is shared with the theta and spanning reviews; it is not hidden under the expression "Harish-Chandra".

- The rearrangement inequality with gain is obtained by perturbing o by ±e_i; its integrality preserves the weak inversion of the order. The top-term lemma also controls permutations within each block: the strict inequality forces w=1 on computing the top coefficient. The separation between signs ensures that κ+ND preserves the order even when two weights of the same sign are close.
- In `pbr:int`, the identity of the positive minor converts the growth of g into separation of eigenvalues. The exponent pqM fits within the separation h₀ and the final majorant is integrable because 2M>n². This justifies a Bochner integral in C(K), not a formal exchange of distributions.
- In `pbr:laurent`, the coefficients against characters are integers by Schur orthogonality and finite expansion of the product of a character by the regularising polynomial. Bessel forces there to be only finitely many non-zero coefficients. The identification P=D^Mt is checked coefficient by coefficient; the relevant sums are finite even when t is an infinite formal series.
- In `pbr:flag`, the complex Jacobian b^{2ρ} becomes |b^{2ρ}|² as real Jacobian. The compatible measure is preserved on multiplying by i the coordinates between opposite signs. Thus j_H is the same for U(p,q) and U(n). The mass 1 of the torus allows the comparison without a hidden volume. The complement of the cell is null by real analyticity and not by an unjustified algebraic assertion about measure.
- In `pbr:Un` and `pbr:orbit`, the compact coefficient formula and two applications of Schur give the exact factor 1/dim(Vσ). The change (y,k)=(vu,u⁻¹) preserves product Haar. The normalisation d_Λ∫_K|m_Λ|²=1 eliminates the K-type factor. The application of Fubini is backed by `flagG`.
- In `pbr:gain`, inverting X when the order of the weights is inverted preserves the hypotheses. Jacobi and Fischer are applied only to positive matrices. The bound with an entry between blocks cancels the numerator of the error by means of `pbr:compact`. In `pbr:Ebound` the shift e is kept in the constant C_e; uniformity in e is not required.
- In `pbr:low`, an identity in one holomorphic variable is continued from an interior arc of the sector. After the radial limit, varying e∈Zⁿ separates the exponents of the same level by means of independence of characters. This avoids assuming that the term of lowest level is unique.
- The five final steps compare low-level coefficients, eliminate permutations between signs through the gain h₀ and recover all the coefficients by antisymmetry. The top coefficient imposes s₀=1. Hence `pbr:degree` gives exactly d=dim(Vσ)=∏_{i<j}(λ_i−λ_j)/(j−i), with compatible Haar, and σ_λ=(−1)^{pq}. This constant is not obtained by an asymptotic approximation.

The remaining obligation of this front is reduced to the inputs of paper 49 on the coefficient of the discrete series, its identification and the cone of K-types, plus the external collation of the classical inputs indicated. No additional failure was found in this internal reconstruction.
