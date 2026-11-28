> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the remaining results are being consolidated.

# P53: constant term, constancy and non-vanishing

Direct audit of `main.tex`, lines 4610–5465 and 5544–6368, 28-11-2026. The operations of those proofs were reconstructed. Explicit dependencies: Weil model W1–W5 of 49, convergence and moment norms, mixed model corrected on Schwartz according to COVOLUME. Exchange is not certified by assembly; the error `pcu:product` remains.

| Obligation | Verdict | Scope |
|---|---|---|
| `pct:plane`, 4850; proof 4897–5195 | **(a), under the inputs of the model and convergence indicated** | Zero term, unfolding, local factors, Mellin and the two ranges are reconstructed. It does not use `pcu:product`. |
| `pct:SA`, 5240–5300; `pcx:const`, 5302–5330 | **(a) under `pct:plane`** | Strong approximation eliminates radicals; the additional toral condition eliminates the obstruction of the determinant. Unrestricted strong approximation for U(Y) is not invoked. |
| `pct:coneimage`, 5395–5438; `P-plane`, 5441–5465 | **(a), with the mixed model in moment norms** | The section is chosen simultaneously for all the characters of weight μ; B(x)>0; it does not require dividing by an oscillating integral. |
| `pct:vandesc`, 5551–5575 | **(a) under the constant term** | The range d≥−k, k≤μ and the non-vanishing of L(d+1) are verified. |
| `pcn:negcoeff`, 5719; proof up to 6352 | **(a) for the argument reconstructed with the local laws indicated** | It does not depend on global unfolding nor on product. A distribution descends to the space of the orbit, then to a functional of the stabiliser which vanishes. |
| `pct:vantop` → `P-nonvan`, 5607–5652 | **(b) the written proof** | First defective use in this proof: 5632–5634, "by Lemma pcu:product". The period has the residual character already identified in ERROR-53-CHARACTERS. It is not proved here that the statement is false. |

## 1. Reconstruction of `pct:plane`

**Levi and range.** With d=r−N/2, the modulus of the radical of V′ contributes |a|^(r+1). The two sequences of zero terms contribute respectively |au|^(−N/2) and |au|^(−N/2−1), in addition to |u|^(r+1) and ν̃(au). The hypothesis u=1 or r=N is indispensable: only then are χ_(r+2) and χ_r at u identified with ν̃⁻¹ with the printed exponents. That restriction is maintained in const, plane and descent; the formula is not applied for arbitrary u in unequal rank.

**Terms of the expansion.** The mean over the centre of N_A eliminates Q(y)≠0. The term y=0 vanishes locally at any w∈S: the zero term requires xe_A=0, but the matrix formed by z·pr and x would be invertible and would have zero column e_A. Here S≠∅ is declared at 4618; it is not the defective empty case of `pcx:decay`. For ξe_X≠0, the remaining radical averages the translations of Hom(W,Ee_X); W2 identifies exactly L_t(ξ). The isotropic lines constitute P_X(E)\U(V′)(E), by Witt, and the parabolic integral gives the exponent d+1. The proof does not need to integrate the sum of absolute values of all the y for all h before the regrouping: the pointwise identity is used and then the absolute integrability of Φ_x′ on the parabolic quotient.

**Local factor.** Outside S, the primitivity of the lattice line and its dual produces the indicator of α integral. In S, after the unimodular change of frames, the matrix has blocks

`[z 0 0; y 0 p; q α_w s; 0 0 t]`.

Its determinant is ±α_w t det[z;y]. The variables p,q,s have volume 1; α_w,t must be units. The integral in t is a Gauss sum of modulus q_w^(−1/2) and support v_w(overline(α_barw))=−1. This gives λ_varpi for both orientations of the line, not an additional power of q depending on r. The characters of the changes of frame have modulus 1. K′_f fixes the datum because χ(det k) of the change of matrix cancels γ_W′(det k)=χ(det k)⁻¹.

**Mellin and endpoints.** For x>1, Tonelli and the local factors give the Euler product L^S(x,ν) and the archimedean integral cone_x. The archimedean convergence uses x>0 near 0 and a sufficiently high moment norm at infinity. Poisson provides

`|a| Σξ≠0 Λ_t(ξa)=Σξ≠0 Λ_f(ξ bar(a)⁻¹)`.

The terms ξ=0 are zero in both polarisations. The change a↦bar(a)⁻¹ preserves ν̃ and changes |a| into |a|⁻¹, so it gives the bound for the absolute value of the SUM of the t side at exponents 1−x. This suffices for the integrand of Z; it is not asserted that Poisson preserves the sum of absolute values. Interpolating between R and 1−R produces convergence for every real exponent and analyticity, with domination of the logarithmic derivatives. The case x=1 is obtained by continuity; absolute convergence of the Euler product is not used there.

With K₀=c⁻¹α₀, |c⁻¹|=Q and |g_S|=Q^(−1/2), the factor is ε_β |α₀|^x Q^(x−1/2)L^S(x,ν), with |ε_β| independent of ν. Thus the Q^(−1/2) is not missing. The factor |α₀|^x is absorbed in C only after fixing the spaces and, therefore, x=d+1 or −d. d integer is used: d<0 implies −d≥1.

## 2. Constancy and addition of a plane

In `pct:SA`, the strong approximation used is that of the additive group, not that of the torus U(1). Approximating c and the skew coordinate of β outside a non-empty finite set provides left invariance under N and N⁻, using rational invariance and right invariance in S. The explicit formula of three unipotents of `pct:qref` gives the Levi m(λ,ρ), where ρ is a quasi-reflection of Y₀. λ=(j barσ)⁻¹ and j barλ=−σ⁻¹ were verified. On cutting components to a finite set R the identity is preserved; generation by quasi-reflections allows all the rational elements of U(Y₀). Condition (iv) allows λ to be replaced by any toral parameter t. Then weak approximation by Cayley and the invariance under compact groups outside S eliminate the finite components; weak approximation at infinity concludes. Thus the obstruction of the determinant has not been discarded gratuitously.

In `pcx:const`, the right invariance under the full group in S is deduced from `linfactor`: at b=0 the two sections are ξ(det x)⁻¹. The action Sact(b) has η(det g)^0=1. Condition (iv) comes from `pct:plane` at r=N. This uses neither `P-plane`, `P-equal` nor `P-nonvan` and hence there is no cycle in this subchain.

The construction `coneimage` uses a local smooth section of the isotropic orbit, extended by exp(φX) inside a chart of the group. The mixed model produces prescribed slices in that chart. The equivariance of the zero term cancels ν̃_∞(a), leaving β(κ⁻¹ae_X)|a|^(N/2)≥0. The integral B(x) is positive because the integrand equals 1 at (1,1), and its support has |a_τ| in [2^(−1/2),2^(1/2)]; it is analytic for every real x. The resulting vector depends only on μ, not on the finite twist. On adding the plane, const is used to replace F(1) by its constant term and L^sharp(d+1)² is cancelled exactly against L_*(d+1)/L_*(d). This construction requires the topological repair on moments recorded in COVOLUME; it does not make the false phrase "Hilbert-bounded evaluation" correct.

## 3. `negcoeff`: reconstruction of the local vanishing

The hypotheses H1–H3 hold in the application: q′=b+q₀, p₀≥1 and N_τ=μ_τ+p₀−n/2=μ_τ+k≥1. The character of the slice is γ_Xυ⁻ᵇ=γ_W₀; not γ_X uncorrected. The compact law gives vacuum weight μ^flat−p₀ in a negative row. Hence a rotation of a negative line with eigenvalue barη multiplies the vacuum by η^(N_τ).

If the invertible index β is not negative definite, it has a positive direction. Witt moves that direction to a standard positive row. For each value z of the Fock variables there is a negative line perpendicular to the b columns of the frame and to the q₀ negative columns of z: in the b+q₀ negative rows the first b conditions have a dependency, because the frame contains a positive row. The rotation of that line fixes the frame. On the hyperplane imposed on z, the invariance of a polynomial P gives η^(N_τ)P(z+(η−1)z′)=P(z). Evaluating the polynomial identity at η=0 proves P(z)=0. η=0 is not taken as an element of the group; continuation of a polynomial identity valid on the circle is used. Averaging over the compact stabiliser and the density of polynomials in Schwartz eliminate every continuous invariant functional.

To pass from a functional of the large model to the fibre, the central character first forces each coordinate of Q(x)−β to be killed. Since β is invertible, dQ is surjective: ξ=(1/2)xβ⁻¹η produces dQ(ξ)=η. Hadamard then shows that ALL the functions vanishing on Q⁻¹(β) are killed, not only that the support of the distribution is there; that excludes normal derivatives. The space of the fibre is a homogeneous orbit with unimodular unitary stabiliser. The map

`F ↦ (gx₁ ↦ ∫_S ω^flat(gs)F(gs) ds)`

is surjective by a compact function with positive average. Left invariance converts the lifted distribution into Haar tensor ε; the twisted right invariance forces ε∘ω^flat(s)=ε. The preceding compact vanishing gives ε=0. Continuity is controlled with Schwartz seminorms, not with bounded evaluation in Hilbert.

Finally the global coefficient defines that continuous functional: the decay bound is uniform over the compact set of the centre and the moment norms dominate the integral. After absorbing p_∞ into the vector, translating the centre gives the character ψ_β with positive sign, and translating h gives U(T_τ) invariance. Hence `negcoeff` is proved without U1 nor integrability of a term on the quotient of the stabiliser. It does not use `pcu:product`.

## 4. Non-vanishing and the dependence that is not eliminated

`vandesc` extends analytically Z(x)=εP(x)L(x,ν̃)B(x)I. If d≥−k and k≤μ, then j=d+1>−k and j+μ_τ>0; the gamma functions of the functional equation are finite and non-zero. L(j)≠0 follows from non-vanishing at 1−j≥1 when j≤0. The descent of 2k+1 planes arrives exactly at (J,0), where the kernel is 1.

But to start that descent `vantop` is needed. Its case of non-negative indices uses the correct `negcoeff`; its case of index J_U applies `pcu:product` explicitly to the integral in l, lines 5632–5634. The correct formula introduces β(det l), so the hypothesis of vanishing of the period without that factor is not enough. The problem reappears even in this proof whose assumed period is zero: multiplying the integrand by a variable character does not preserve zero integral. **`P-nonvan` is not closed.** Concrete pending repair: identify and control that twisted period, or supply an alternative proof of non-vanishing; it is not enough to have closed plane/const/negcoeff.
