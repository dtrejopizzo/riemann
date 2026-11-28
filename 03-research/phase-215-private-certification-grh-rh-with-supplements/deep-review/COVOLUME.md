> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the remaining results are being consolidated.

# Paper 53: exchange and determinant, deep audit in progress

**Finding that affects the exchange route:** [incompatibility of characters in `pcu:product`](ERROR-53-CHARACTERS.md). The direct computation gives a factor depending on the variable that is integrated in `pcu:period`. This obligation must be resolved before certifying the exchange and the covolume chain by this proof. The conditional checks of the following sections remain local.

## `pcx:decay`: necessary non-empty hypothesis

**(b) for the literal statement allowing P=∅.** The convergence subsection introduces a set P of primes with P∩bar(P)=∅, without requiring it to be non-empty. In `pcx:decay(a)` the surjectivity condition "at each place of P" is then vacuous. The first invalid inference of the proof is the application of `pcx:meanzero` in the paragraph asserting that the pairing is non-zero at some place because x is surjective at P. That place cannot be chosen if P=∅.

Counterexample to the literal scope: take S₁=0, S₂ a hyperbolic plane, P=∅, trivial characters and the vector 1 in the Fock representation of Hom(0,S₂)=0. The manuscript explicitly uses the zero space and normalises its theta functional as 1 in `pcx:twice`. The kernel is therefore 1. At the cusp of the unitary group of the plane, the height ht(h) is unbounded: for infinite h that scales a rational isotropic vector by t and its dual by t⁻¹, with fixed finite part, an integral multiple of the former has length O(t⁻¹) in Λ_h. For N₀>0, the asserted inequality would require ht(h)^N₀≤C‖1‖_M, which is impossible.

**Correction:** add P≠∅ to `pcx:decay` and keep it in `pcx:conv` when it is formulated outside the exchange context. In `pcx:X` one already requires m≠(1), so that S has at least one place. It is not a counterexample to the exchange nor to the global conclusion. This condition must be checked in every other application of the lemma.

## Assembly of the exchange: reconstruction

Lines 1730–2260 and the convergence argument up to `pcx:conv` were read and reconstructed, with the preceding correction and conditionally on the intermediate propositions indicated below.

- The transposition of indices between the two splitting conventions is exact by definition. On passing from α=1, α′=γ to αα′=γ, both sides are multiplied by α(det g)⁻¹; c does not change.
- The determinant identity of the standard data gives Φ(k^[a])=χ(det k)Ψ(k_[b]) with the correct sign. The supports are identified by extending a primitive family to a basis over each DVR. For moduli with powers, lifting an invertible matrix from the reduction preserves invertibility: a squarefree modulus is not needed.
- The change U→U⁻ in `P-matches` transforms q_U into b−q_U, exactly the sign condition of `P-std`. The adjoint introduces d of constant modulus; C is transformed into C/d₀².
- In `pcx:twice`, the two applications with triples (J,J,0) and (J,0,J) give ξ=c₁c₂ by Fubini over the compact quotient. The positive volumes vol₀ and vol_J cancel. Since L_*(k)L_*(-k)=1, the square of the equal-rank ratio is independent of the character. There is no division by a ratio that could be zero.
- `P-equal` first chooses a non-zero vector for one character; `twice` turns it into the **same vector** that works for all. The ratio is non-negative by definition, so that equality of squares implies equality. Adding planes and transporting spaces with equal signs preserves the independence of the character, provided `P-plane` and `P-signs` are supplied.
- In the final assembly, C₁|c|²=L_*C₀, with C₀≠0 and L_*>0, forces C₁≠0 and c≠0. The positivity of C=C₀/C₁ results from this identity, not from an assumption on the initial sign of C₁. The case without characters is handled by vacuity.

The non-vanishing of L_* uses the Euler product for z>1 and the classical non-vanishing theorem on Re(s)=1 for the non-trivial unitary character. The positive weight excludes the trivial character; removing factors in S does not introduce zeros at s=1. This is a classical analytic input, not a new proof of non-vanishing within the audit.

## Convergence: mechanism checked

`pcx:reduce` normalises the idelic parameters by means of ideal classes and units before estimating infinite norms. The rational isotropic vector e₁ provides the comparison between the largest parameter of the cusp and the inverse of the first minimum. The compact set of the finite part allows a uniform integer denominator.

`pcx:thetagrowth` uses sums over translates of a lattice with exponent 2s>dim_R X: the supremum over the translate is finite. After reduction, the finite datum runs through a finite set up to unitary phases. The resulting bound depends on the heights and not on the Heisenberg translation.

In `pcx:diffgain`, the induction is carried out on translated vacua and their polynomial derivatives; each difference gains a power of the size of the translation. The mean-zero hypothesis is applied to each vector, avoiding the assumption of a contraction of operator norm. The superposition of the vacuum extends the bound to vectors with finite moments.

`pcx:mean` uses a compact fundamental domain of E\A_E and an integer that fixes the finite datum. The adelic translations over the isotropic subspace become small real translations, without a cocycle on that subspace. The norm of the mean functional is controlled by the same norm uniform under translations. In `pcx:meanzero`, a finite partition of the support allows a non-trivial local character to be chosen on each piece.

Finally a short isotropic vector d and a short basis of the source give rank-one maps dλ of size δ≪ht(g)^n/ht(h). With P≠∅ and local surjectivity the mean vanishes. Choosing l=N₀+A gives ht(h)^{A−l}=ht(h)^{-N₀}. The injective case interchanges source and target. This justifies the absolute convergence of the exchange integrals for data of full rank and non-trivial modulus.

## Next obligations

`pcx:X` is not certified. The initial list of pending items is updated by the batches below: `P-match` was reconstructed; `P-slice` has an explicit repair of topology; the algebra of the descent was checked conditionally on its constant-term formula. `P-top` meets the concrete failure of `pcu:product`, documented separately. Still without a complete independent closure in this ledger are `P-flip`, `P-nonvan`, `P-plane` and `P-signs`, including their constants and ranges. The preceding assembly shows what they are needed for and does not replace their proofs.

## Second batch: `P-match` checked

Lines 2680–2910 were reconstructed, conditionally on the local Weil model of 49 and on the convergence already reviewed for non-empty S.

The partition Surjᵃ=⊔r Prᵃ is correct: rOᵃ is precisely the image of the matrix over Oᴺ, so that the coset rGL_a(O) is unique. The integral defining the section has compact support in GL_a(F), because the support of Φ is compact inside the open set of surjective matrices; compactness in the ambient space allowing degeneration of rank is not used.

In `linfactor`, the invariance of Λ allows a finite number of translates over GL_a(O) to be averaged, reducing Φ to 1_Prᵃ S_Φ. The linear extension to all functions serves only to define T outside the image of the pairs: on each pair used the function is again the required locally constant section. No continuity of that extension is needed, nor is anything integrated with respect to it.

`generate` uses the idempotent e=x₀s and d=varpi^{-c}(1−e)+e to concentrate a standard datum near a primitive orbit. The periodicity at scale varpi^c and the right equivariance of Ψ give the pointwise identity of the text. The average over GL_N(O) is a finite sum by uniform smoothness of the action on the function of compact support. The factor I(x₀)>0 because p(dx₀)=1; there is no division by an oscillating integral that could vanish, since |p| is averaged.

In `Sact`, the factor on the large side is υ_w(det g)^{r−N}|det g|^{(r−N)/2}=η(det g)^{-b}. On the small side, the model at the conjugate place contributes υ_w^b|det g|^{-b/2}, and the twist υ^b contributes υ_w^{-2b}; the same factor is obtained. Thus the stability of the kernel of the difference D is preserved and the standard identity is extended to all matched data. This closes `P-match`, but not the remaining exchange propositions listed above.

## Third batch: topology error in the pointwise restrictions

**(b) for the assertion that sl(x):F′→F is bounded as an operator between Hilbert spaces.** It is declared at lines 4409–4410, before `pcu:eq-mixed`, and is used in `pcu:slicedecay` and in the last part of (M1). The proof of `pcu:mixedmodel` also invokes that boundedness when speaking of uniqueness.

`pcu:mixedmodel` itself identifies F′, up to a norm constant, with L²(V_ℓ;F), and sl(x) with evaluation at x. For dim_R V_ℓ=d>0, take a smooth function of compact support φ with φ(0)=1, a Schwartz vector v₀≠0 of F and

`G_ε(x)=φ(x/ε)v₀`.

Its L² norm is ε^{d/2}‖φ‖₂‖v₀‖→0; its value at 0 is always v₀. The Bargmann inverse of G_ε is a Schwartz vector, so that it has all the finite moments required. Hence evaluation is not bounded even on that subspace equipped with the Hilbert norm. It is not enough to say that the vectors used are smooth.

### Repair with the moment norms

The assertion needed is continuity of sl(x) **from the space of vectors with a suitable moment norm**, not from the whole of F′ with the Hilbert norm. It can be reconstructed without assuming the false assertion:

1. First define the restriction on translated vacua by the explicit formula of the mixed model: sl(x)ρ(y)e is a phase times exp(−|x+Ay|²)ρ(Wy)e. This formula is obtained directly from the Bargmann inverse.
2. For a vector with finite moments, define sl(x)v by the integral of that formula against v(y). The inequality of `slicedecay`, proved first on a translated vacuum, gives an integrable majorant and produces

   `(1+|x|)^M ‖sl(x)v‖_N ≤ C‖v‖_{N+M}`.

3. The map M to the mixed model is indeed bounded in the Hilbert norm. Hence M can pass inside the coherent superposition in L². The result coincides almost everywhere with the preceding pointwise integral, which is continuous in x by dominated convergence. This identifies the canonical restriction without using bounded evaluation on L².
4. In (M1), the integral that constructs Λ converges in **all** the moment norms, according to its integration-by-parts computation. Using the preceding bound with M=N=0 allows sl(x) to pass inside that integral. Fourier inversion then gives exactly the prescribed sections. The incorrect inference "it converges in the Hilbert space, therefore evaluation passes through" is not needed.

Thus the conclusion of (M1) and `P-slice` is preserved after correcting the topology and the order of construction. The repair employs the same estimates as the manuscript, but it has to be written out: the literal text does contain a false assertion. The case d=0 does not present this problem; the steps with hyperbolic planes do have d>0 when the other dimension is positive.

The normalisation of `P-slice` is correct under this repair: κ=(c_D∫τ)⁻¹, with τ≥0 non-zero, and the change of polarisation converts the integral of the sections into the value at zero in the opposite polarisation. Applying the argument with the two polarisations interchanged gives the prescribed value in the required orientation.

## Junction 53 → 55: integral Gram matrix

Lines 9770–9804 of 53 were collated with 6221–6268 of 55 (`pax:gram`, `pax:pairing`). The scale of the form is consistent: W_λ(Z)=Σ_μ^# is identified with m(C_μ∩T_μ(Z)), and the form is the restriction of the tensor form of orthonormal basis, in accordance with 49 §5.2.6. The identity ⟨m(u),b_U⟩=(u,e_U) converts the duality with all the products of minors into integrality of all the tensor coordinates. Using the standard products suffices because they constitute a basis of Σ_μ.

Hence the e_T are integral tensors and their Gram matrix has integer entries. The identity G_λ=H_μF_μ⁻¹ does not introduce a change of norm: it expresses that same form in the dual basis, whereas H_μ⁻¹F_μ is the matrix in the basis of products of minors. The application in 55 cancels the conjugate gauges by means of the algebraic invariance identity and, at free level, the stabiliser weightings are 1. This junction is checked from the tensor model and the duality identity of 49; it does not depend on the defective exchange `pcu:product`.

## Descent: check of exponents, conditional on `pct:plane`

The deduction of `pct:descent` at 5512–5530 preserves the function ℓ and changes the exponent from d+1 to d. One divides by κ_ν, non-zero by the classical non-vanishing of L at the points used. For d≥0, L_*(d+1)/L^sharp(d+1)²=L_*(d); for d<0, putting d=−(z+1) gives L_*(−z)/L^sharp(z+1)²=L_*(−z−1). The identity also holds on crossing from d=−1 to 0. The factor Q has successive exponents (d+1)²−d²=2d+1, exactly that of L^sharp(d+1)² in the positive case.

This checks the algebra of the descent provided the constant-term formula `pct:plane` and the small term `pct:small` are supplied. It does not by itself certify those two lemmas, nor does it repair the failure of the product of characters used in the construction of the large triple.

## Laws of the mixed model: `pcu:laws`

Lines 3766–3838 were reviewed. The Levi contributes α(q/\bar q)⁻¹ υ(q)^a |q|^{a/2}, in accordance with (W2). The factor υ(h)⁻ᵇ of the target model transforms βυᵇ into β; no residual character in h remains. The action of the radical is obtained from the Heisenberg formula with phase ψ(−j tr(z x*J_Vx)/2), first for the centre and then with z₂=−c*Jc/2. Evaluation at x=0 fixes the normalisation scalar. This bookkeeping of characters is correct and does not reproduce the error of `pcu:product`. For the pointwise restrictions the topology repair described above remains necessary.

## Conjugation of norms: `pcj:CL`

The complete proof, lines 15456–16070, was read. Its reconstruction is conditional on the exact CM reciprocity of 49 and on the non-vanishing of the lift of 54, Proposition 3.4. It does not use the defective identity `pcu:product` within this section. The check of the order of dependencies must be kept: the non-vanishing used to construct ρ_σ has to be available without invoking CL.

**Check of the order completed together with the theta review:** for z≥2, which is exactly the range of CL, Proposition 3.4 of 54 obtains the non-vanishing by means of Siegel–Weil of 53, the datum `clean` and the local Euler factors. It does not use CL. The non-zero constant of `clean` and the positivity of the Euler product give a non-zero norm. There is no circle in this particular import. The branch z=1, which does employ exchange, does not intervene in CL.

The semilinear map Λ is defined on rational translates of the vacuum by means of jets. The injectivity of the Taylor expansion proves independence of the relations. The passage from rational points to adelic ones uses eventual equality by local constancy, not continuity of an arbitrary automorphism of C. The identity of additive characters is obtained first on rationals and extended by density and local constancy. The smooth irreducibility of Heisenberg gives surjectivity.

After writing B=ua, with u of norm one and a a unit, the normalisation Λ′=ω(u)⁻¹Λ transforms the vacuum into a non-zero multiple of the vacuum. The vectors S_k are orthogonal sums of translates, with |δ_k|²=1/I_k. From this come the multiplier m_σ(k)=σ(δ_k)/δ_k and the identity m_σ(k)·conj(m_{cσc}(k))=1. For the datum at the chosen places, a_w=1 allows Λ′ to be identified with conjugation of the values of the function; the 0–1 indicator functions remain fixed.

The lift is a finite sum of jets with common volume w₀, independent of the character ν. The finite-part character σ∘ν_f is extended with the permuted weight: it is unitary because the adelic quotient of the torus is compact. The comparison of a non-zero jet under a rational translation shows that ρ_σ is trivial on U(1)(E⁺). It is also trivial on K¹, so that it has finite order. The correction ν^σ=ν^(σ)ρ_σ⁻¹ preserves weight and ramification; there is no need to prove ρ_σ=1.

The coordinate formula contains C_{σ,p}, whose modulus does not depend on p: |t_σ|=|s₀|, |σ(π_M)|²=M, and all the remaining character factors have modulus one. To conjugate the norm one has to use σ′=cσc, as the text does, instead of supposing that σ commutes with conjugation on the whole of C. The permutations of the CM embeddings coincide for σ and σ′; the tensor multiplicities n_β and the stabiliser weights r_h are rational. The identity of the multipliers removes their dependence on h. The result is the positive factor a_σ(z), independent of ν, which cancels on comparing a principal pair and a flat one of the same z. This is exactly the scope required by the application in 54; it does not assert individual rationality of each norm.

## Adjoint and change of space: localised conditional closure

Lines 2912–3025 were reviewed. In `P-flip`, the determinant of the action on Hom(U,W) is det(g)^b det(h)⁻ᴺ. The law (W6) therefore carries the characters (γ,γ) to (γ⁻¹υᵇ,γ⁻¹υᴺ) in the reversed pair. Since γ=ν⁻¹υᴺᐟ², the target character turns out to be νυᴺᐟ²; removing γ⁻¹ from the source character contributes γ(det g), with the correct sign. The defect of the product of characters is not repeated.

The central adjustment u of the lattices is eliminated by translation in the integrated variable, at the cost of only a character value of modulus one. The transposition introduces −X; the right invariance of the matched datum converts that sign into another character value of modulus one. The remaining constant c_θ depends on the identification of models and on the spaces, not on ν. Convergence uses injective support and the non-empty set of places already provided for in this application. Thus `P-flip` is reconstructed under (W6), the dictionary of lattices and convergence, without requiring the defective exchange.

In `pcx:move`, the rational transport of the spaces and the adelised changes of frames transform the data by ω(k,k′). The quotient of twists is α(det k)β(det k′)⁻¹. Translating h to hk′ preserves Haar measure; its modulus is one. The argument of `P-signs` is then valid **conditionally on `pcx:const`**: evaluation at k is replaced by evaluation at 1 because that function would be constant. The proof of `pcx:const` refers to the constant term of the plane; this reading does not turn it into an obligation already closed. The dependence is delimited, instead of `P-signs` being certified in isolation.

## Constant term and non-vanishing: later specialised review

The complete reconstruction of 4610–5465 and 5544–6368 is in [MAP-53](MAP-53.md). `pct:plane`, `pcx:const`, `pct:coneimage`, `P-plane` and `pct:vandesc` are closed conditionally, under the Weil model and the repair of the mixed model in moment norms. The restriction u=1 or r=N is respected. This closes the const premise of the preceding `P-signs` argument; it uses neither exchange nor `pcu:product`.

`pcn:negcoeff` was also reconstructed, with descent of the distribution to the fibre and vanishing by compact rotations; it does not use global unfolding. **`P-nonvan` is still not proved by the written route:** its input `pct:vantop`, case (a), uses `pcu:product` again at 5632–5634. The supposed vanishing of the period without twist does not imply that of the period with β(det l). This is an identified defective dependence, not a mere lack of reading nor a counterexample to the statement.

## Algebra of the chain and determinants

[CHAIN-53](CHAIN-53.md) reconstructs `pc:tri-inj`, `pc:tri-gram`, the level indices, the comparison of determinants by M⁺ and the cancellation that gives `au:factor`. It preserves the order of operators without assuming commutativity, the conjugation of σ, the factor c_Q and the final power −d_T. It verifies the ranks of the exchange of excess t and of the reversed one of excess 0, and the conversion of constants into powers of the norm. These are conditional closures: the proof of the squares still receives the defective exchange. The note also identifies individually the archimedean obligations H/Hc/F not replaced by that algebraic check.

**Update on H/Hc/F:** CHAIN-53 §6 reconstructs the three archimedean obligations that the first batch left open, including the unpaired columns in Hc and the primary source of the Harish-Chandra smoothing. This does not close RS or T1, because both still use exchange.
