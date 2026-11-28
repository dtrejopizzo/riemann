> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the remaining results are being consolidated.

# P53: injectivity and determinant of the chain

Direct review, 28-11-2026: P53 491–641, 850–894, 1083–1415, 1510–1600, 6647–6695, 6955–7010, 7554–7587, 8193–8275, 8857–8905. The target statements `au:inj` and `au:factor` in P46 were compared. This note separates the algebra from the automorphic construction of the triangle. The closure of a conditional deduction is not extended to the inputs not reconstructed here.

## Verdict by obligation

| Obligation | Verdict | Precision |
|---|---|---|
| `pc:tri-inj`, 566–590 | **(a)** | T1–T3 suffice; σ≠0 is not presupposed. Injectivity then implies σ≠0 when V≠0. |
| `pc:tri-gram`, 592–639 | **(a)** | Complete formula, conjugation of σ and order of the S_i checked; commutativity is not required. |
| `pc:index`, 1346–1365 | **(a)** under the indicated definition of level | The parahoric/principal distinction is kept and c_Q and the exponent e_m are verified. |
| `pc:heckeclosure`, `pc:detcompare` | **(a)** under convergence and M⁺ | Closure in finite dimension and Newton; M⁺ must include non-split places. |
| Norm of a lift → cancellation of determinants, 1370–1413 | **(a) conditional** | The c_Q^m and the dimensions cancel exactly; the final power is −d_T and the power of the norm is half-integral. |
| `au:inj`, as a written automorphic proof | **Not certified; route affected by (b) in the exchange of 53** | The algebra does not remove the need for T1. The failure of the product of 53 affects the proof of the input T1. It is not a counterexample to injectivity. |
| `au:factor`, as a written automorphic proof | **Not certified; same affected route**, in addition to the precise inputs below | It requires T4 and M⁺, apart from T1–T3. Correcting the final determinant formula is not enough. |

## 1. Injectivity without dividing by the square constants

Let X_(i,n)=(w_(n−1)a_(i,n−1))⋯(w₀a_(i,0)). With T1 one obtains by induction

`X_(i+1,n) d_(i,0) a_(i,0) = τ_(i,n) d_(i,n) X_(i,n+1)`,

`τ_(i,n)=w_(n+1)/(w₀w₁) · ∏_(l<n)σ_(i,l)`.

For n=0 the factor is 1/w₀. The step uses w_n a_(i+1,n)d_(i,n)=σ_(i,n)w_(n+2)d_(i,n+1)a_(i,n+1), so that the added factor is σ_(i,n)w_(n+2)/w_(n+1), exactly the one required. All indices remain in i+n+2≤m.

If X_(i,n+1)j_i y=0, T3 provides y′ with j_(i+1)y′=d_(i,0)a_(i,0)j_i y. The preceding identity and the inductive injectivity give y′=0, hence y=0. **There is no division by τ.** If afterwards some σ were 0 and V≠0, the same identity one level higher contradicts the injectivity already established. Thus κ^sharp≠0 is not introduced as a circular hypothesis of exchange.

The preservation of j_(i+1)(A₀) in T3 is checked by means of the equivariance of the first lift under J_M: aρ(u⁻¹)=cρ(g)a, |c|=1, and d=a*. The factors c and bar c cancel in the pairing; this gives d a x fixed by J_M. The injectivity of a makes d a injective. This argument does not presuppose that every later lift is in the stable range of Rallis.

## 2. Gram form: constants and order of operators

The inner product of the text is conjugate-linear in the first variable. The law T4 and T2 produce

`<z,a_(i,n)X_(i,n)j_i y> = (∏_(l<n)κ_(i,l)) <d_(i,n)z,X_(i+1,n)j_(i+1)y>`.

On substituting dX=τ⁻¹Xda in the first variable, **barτ⁻¹** appears, not τ⁻¹. Hence β_(i,n)=1/barσ_(i,n). For x′ defined by j_(i+1)x′=d a j_i x, the first norm gives

`<x′,v>=(C_i/w₀)<x,S_i v>`.

There is no need to solve for x′ by means of S_i*, nor to commute S_i with the other operators. The recurrence preserves the order S_iS_(i+1)⋯S_(m−1). The constants satisfy

`K_(i,n+1)=(w₁w_n/w_(n+1)) C_i (∏_(l<n)κ_(i,l)β_(i,l)) K_(i+1,n)`.

Their telescoping product is w₀w₁^m/w_m. Each square i+n+2≤m contributes κβ exactly once; the bijection (i,n)↦(i+1,i+n+2) runs through exactly the pairs 1≤i′<j′≤m.

## 3. From the Gram form to Z(1)/Z(θ)

The first lift contributes C_i/#Mat_((r+t)×r)(R_θ) and S_i=Ral_(i+1)(θ^(i+1)). Its source normalisation is w₀=#GL_r(R_θ). The algebraic/Petersson comparison by Schur contributes [K_m:J_θ] and an archimedean constant independent of θ. At Q_θ the final level is the parahoric with blocks r,t,…,t, whose radical has dimension

`e_m=mrt+m(m−1)t²/2`.

It is incorrect to replace it by the principal congruence level of each stage; the text does not make that substitution. With g_N=#GL_N(F_q), the local factor of the index and of the weights of the triangle is

`g_(r+mt)/(g_r g_t^m q^e_m) · g_r g_(r+t)^m/g_(r+mt) · q^(−(r+t)rm)`

`=q^(−e_m) [q^(rt) ∏_(a=t+1)^(t+r)(1−q^(−a))]^m`.

It is exactly q^(−e_m)c_(Q,w)^m. The factors at the chosen places do not depend on the twist and go into C_M.

For an isolated lift the block datum has squared norm g_r q^(rt) and the target index is g_(r+t)/(g_r g_t q^(rt)); together with #Mat=q^((r+t)r) one obtains the SAME c_(Q,w), once only. The change of convention towards P54/P55 multiplies the target form by the unitary character χ∘det; it is an isometry for Gram, although it does change the Hecke roots. That isometry is not used to assert integrality without further argument.

The operator Ral is an absolutely convergent limit of elements of the Hecke algebra. On the joint image over two finite-dimensional spaces, the linear image of that algebra is closed; hence there is a single element h that realises the two actions. M⁺ applied to h^k, including k=0, gives equal dimension and equal power sums throughout; Newton gives equality of determinants. The algebra of **all** places outside M is required: equality at split places only is not enough for this step.

Thus, with d_j=d_T,

`Z(θ)=[Λ(θ)c_Q(θ)^m]^d_T ∏_j det Ral_j(θ^j)`,

`Z_j(θ^j)=[A_j c_Q(θ)]^d_T det Ral_j(θ^j)`.

Cancellation gives Z(θ)/∏Z_j(θ^j)=[Λ(θ)/∏A_j]^d_T. Both determinants are positive by injectivity. Hence the right-hand side coincides with the modulus raised to d_T; one does not infer from this that Λ itself is positive when d_T is even. Normalisation by θ=1 removes all the independent constants and produces

`Z(1)/Z(θ)=[(Nm Q_θ)^(e/2) ∏_(1≤i<j≤m)ρ_ij(θ)]^(−d_T) ∏_(j=1)^m Z_j(1)/Z_j(θ^j)`.

No ambiguous d_T-th root remains, nor a change of sign in e: e is defined by |Λ(θ)/Λ(1)|. The case d_T=0 is separated beforehand, in accordance with the empty determinant.

## 4. Ranks of the exchange and of the twists

For the square (i,n), W=G_(i,n+1)⊕G_(i+1,n+1) has N=2(r+(n+1)t), A of rank r+(n+2)t and A′ of rank r+nt. Hence e=t. The identity of sign numbers is verified entry by entry in the three regions a≤i, i<a≤i+n+1 and a≥i+n+2 of the stem formula. q≤2r and t=5r give 2q+2≤N; Δ=2r⁸ and the admissible sizes give N≤2(n+1)Δ. For the reversed square the targets have equal rank, e=0, and the same inequalities for N, q; only then is L_*(…,0)=1 used.

The character of the square is (ν_(n+1)θ^(n+1))⁻¹, of weight (n+1)Δ. Since i+n+2≤m, the exponent n+1 lies in 1,…,m−1. The powers θ^j preserve Q by the definition of m-fold twist, and the chosen tame parts have order >2m. The ratios ρ_ij have exactly t factors with z=1,…,t, exponent j−i≤m−1 and weight (j−i)Δ≤4b; by Δ≥t they are critical pairs. The exchange constant gives |c|²=C M^(ft²)(Nm Q)^t²∏|L|², whence |β|² is a norm power times ρ_ij², with constant independent of θ.

In T4, the printed assembly gives κ_(i,n)=c_n η κ_rev/(γ c_(n+1)). With M_n=r+nt and |η|=1, the norm contribution of the three constants is

`−M_nM_(n+1)+M_(n+1)M_(n+2)−t(t+2M_n)=t²`.

It is an integer; κ_rev has constant modulus because the reversed exchange has e=0. This control does not require κ to have modulus exactly 1: the definition only demands modulus 1 **up to powers of the norm**.

## 5. Inputs that this deduction does not prove

**Historical status of the first batch:** the later section 6 discharges H/Hc/F; the obligations closed there do not remain pending. Exchange is still affected.

The automorphic proof `pc:tri` refers to obligations distinct from the preceding algebra:

1. **T1:** `ptr:square` combines exchange with archimedean multiplicity one. Exchange is still affected by `pcu:product` (ERROR-53-CHARACTERS and MAP-53). Multiplicity one (H), `ptq:H` 7554, uses `ptq:howe` and the properties (a)–(d) of the projector `ptq:P`. The deduction of H was inspected, but the whole polynomial elimination that proves those properties is not reconstructed here. This is a concrete obligation, not covered by the correctness of the algebra of the triangle.
2. **T4:** `ptv:adjoint` 8193–8240 is reconstructed conditionally from RS, reversal and Fourier. RS 8857 applies another exchange, now with e=0, and demands multiplicity one with the groups interchanged (`ptw:Hc`, `ptw:revedge`). The final formula of powers does not prove those inputs, nor does it remedy exchange.
3. **First lift:** `pc:first` uses `pc:rallis`, the series near 1 and the archimedean positivity `ptv:arch` 8244. The substitutions of level, sharp datum and characters were checked. Positivity passes through `ptq:F` for the first pairs; no new proof of that theorem is given here. The SW01 reconstruction in THETA for the compact lift of P54 does not by itself authorise every non-compact case of this first row.
4. **M⁺:** it is imported from 51; its audit is MULTIPLICITIES. It is not obtained from mere equality of rank, nor from finitely isometric local forms.

There is no algebraic circle in proving injectivity first and deducing κ^sharp≠0 afterwards. Nor is there a circle in obtaining the factorisation from the determinants of isolated lifts, since their norms are proved beforehand by means of Rallis. No absence of cycles is asserted for all the transitive proofs of H/Hc/F that this note leaves individually identified.

## 6. Update: discharge of F, H and Hc

Lines 7094–7587 and 8347–8838 were read in full, as well as `ptr:Z` 7033–7083; the polarisations of 49:1711–1750 were collated again. **The pending items H/Hc/F of §5 are replaced by the following reconstruction**, under the inputs on discrete series and growth already identified in THETA/MULTIPLICITIES. The proof of RS remains conditional on the defective exchange; it is not declared proved by the closing of these other inputs.

### F: positive coefficients and non-vanishing of the first factor

**(a) for `ptq:coef`, `ptq:vac` and `ptq:F` under the indicated Weil action.** Heisenberg covariance, separated into linear and antilinear parts in w, gives the two ladder formulas with the correct factor η_i. The matrix C(u)=u_++⊕bar(u_--) is invertible for u∈U(η). When the polynomial is harmonic by columns, the terms of opposite sign disappear; inverting the block of C* gives the coefficient bar(A_ij). The Euler induction nP=Σz_j∂_jP preserves the harmonic conditions exactly and produces

`<Q,ω(u)P>=c_u<L_(C(u)⁻¹)Q,P>`.

The non-vanishing of c_u is not presupposed: if it were 0, all the coefficients between polynomials of sign + and sign − would vanish. The Heisenberg exponential series of the vacuum converge in norm because ||A^n1||≤M^n√(n!). Thus the coefficients also vanish between their translates in W_+ and W_−. The invertible block (u⁻¹)_-- implies W_++u⁻¹W_−=W; the irreducibility of Heisenberg forces ω(u)⁻¹1=0, a contradiction.

For positive w=expX, detw=1. With JwJ=w⁻¹ and the vacuum an eigenvector of J, c(exp(tX)) is real; continuity and non-vanishing make it positive. C(u) and A=C(u)⁻¹ are positive Hermitian. Writing A=BB* converts the coefficient into c_u||L_(B*)P||²>0. The norm is not merely non-negative: P≠0 and L_(B*) is invertible.

In `ptr:Z`, two compact averages by Schur give exactly d_Λ⁻¹, while the coefficient of the discrete series is expressed with positive denominator m_(−μ)(u⁻¹zu). The result is

`bar A(κz)=d_Λ⁻¹∫_K <Φ,σ(u⁻¹zu)Φ>/m_(−μ)(u⁻¹zu) du >0`.

The total integral is finite by e_λ∈L¹, and Z_∞=∏d_λ⁻¹<Φ,PΦ>>0. This step depends on the Flensted–Jensen formula in the normalisation audited in the spanning branch; the translation erratum of that proof requires its repair recorded there. It requires neither exchange nor `pcu:product` nor the global multiplicity theorem.

### H: projector and elimination of polynomials

**(a) for the deduction with the specified inputs on discrete series.** The integration by parts uses L¹ derivatives of e_λ and real conjugation of gl_n: bar(E_ba)=−E_ab for equal signs; hence P E_ba=0 and P E_aa=Λ_aP. The image of the projector belongs to the isotypic H_λ by the weight/Casimir rigidity; that input is reconstructed in THETA AR01–AR03 with Vogan–Zuckerman. Self-adjointness allows Pσ(y)Q to be killed when the K-type of Q is outside the positive cone; P need not be the projection onto the WHOLE isotypic.

The content of D4 that is used is that the other K-types differ from Λ by a sum of positive roots: the cone of the hypothesis `ptq:P(c)` includes all of them. The stronger version printed with non-compact roots only is not needed for this inference. The alternative primary source [Atiyah–Schmid, Theorem8.5, p.42](https://www.math.utah.edu/~ptrapa/math-library/schmid/atiyah-schmid.pdf), collated in THETA AR01, covers the content used.

For D5, [Harish-Chandra, *Discrete series for semisimple Lie groups II*, §8, Theorem1, p.18](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6013-11511_2006_Article_BF02392813.pdf) was downloaded and read. The original demands finiteness under the algebra generated by the centre of the enveloping algebra and the compact algebra; this holds for e_λ by infinitesimal character and K-finiteness. It gives f*α=f with α smooth of compact support. Applying it to f(g⁻¹), followed by inversion and unimodularity, gives β*f=f as used. Hence there exists β₀ that fixes PΦ under the opposite group. That smoothing is not deduced merely from approximating the identity.

In Howe, the complement N of G∩D_j is finite-dimensional. The compact operators and their adjoints preserve it; a highest vector of columns is chosen. The hypotheses (iv), (v) impose exactly the row weight and kill raising. The column Laplacians lower the degree by two and Fischer annihilates them: their multiplier adjoint lies in G. For the row ones, `ptq:tensor` is a finite induction on λ_b−λ_a; the terms of the commutator have strictly smaller difference. If the shifted weight falls outside the cone, Fischer applies; if it falls inside, λ_a>λ_b, and the polarisations of 49 with the sign of ξ remove one derivative from each term. One obtains a pre-joint harmonic, proportional to Φ by uniqueness, incompatible with N⊥G. Differentiating the smoothing function preserves compact support and gives stability under the opposite algebra, completing H. The equality is transported to F_s by Bochner convergence, not by a supposed pointwise continuity in the Hilbert space.

### Hc: unpaired columns and reversal

**(a) for Hc and the revedge deduction under the indicated inputs.** The inversion of rows/columns changes η into −η. The row B of unpaired columns is not ignored: w′_c=0, and polarisation with both signs eliminates all its variables. For the paired columns, w′_(c(r))=−w_r and ξ′_(c(r))=−ξ_r give the required sign. In the uniqueness by Taylor at x₀, each possible variable has a polarising field whose only non-zero coefficient at x₀ points to that variable; the cases diagonal, minor comparison and major comparison are exhaustive. Thus Hc does not invoke without justification the symmetry of a situation with a different number of rows and columns.

The reversal A_∞ is antilinear and antisymplectic. The uniqueness of the positive complex structure commuting with K×K′ is checked block by block: the real commutant of each block Hom(S_±,T_±) is C, and positivity selects a single sign. The result is φJ=−J′φ. The combinations ∂_y±i∂_(Jy) carry, through A_∞, creators to creators and annihilators to annihilators; hence vacuum→vacuum and degree≤d→degree≤d, and also conversely.

`ptw:W7` computes the character through the metaplectic cover: the antilinear conjugation changes d into bar d, and d⁻²=det(g)^(−N′)det(h)^N. The absence of any other continuous character of Mp follows from connectedness and a perfect Lie algebra. The global form of W7 already restricts the character to powers of υ; hence computing those exponents at infinity suffices, without introducing an arbitrary residual finite character. The flip law then cancels those exponents and gives λ_S=λ_T=1.

Applying A_∞ to P′ requires conjugating e_T and changing x↦x⁻¹; it gives exactly P^rev. Applying it to the smoothing Hc conjugates β_Q, so that α_Q=barβ_Q. The types of the reversed lifts are obtained by conjugating the kernel and the form: e_T→e_S and bar e_S→bar e_T, as demanded in RS. The deduction of RS still uses exchange with e=0, whose defect is not removed by this reconstruction.

**Remaining dependencies:** H/Hc/F is no longer pending for lack of a traversal of these proofs. What remains are their explicit inputs on models and discrete series, treated in the other branches, and the structural failure of exchange. No new circularity is introduced: F is proved before the positivity of the first lift; H/Hc use rigidity and smoothing, not injectivity of the chain nor its determinant.
