# Splitting P3: alternative reconstruction and documentary scope

**Current status:** the mathematical verdict on P3 is **(a), reconstructed**, according to §§6–9. The provisional obligations described before those sections have been discharged by the explicit formula reproduced by Chan and its Gaussian comparison with Murase. No mathematical item remains pending because of the lack of access to Kudla's original; that limitation is documentary.

28-11-2026. P3 of 49:538–560 and conversion to left actions 49:576–587. **The full text of Kudla 1994 was not obtained:** Springer delivers only the access page. [Murase 2001, original text reproduced](https://scispace.com/pdf/on-metaplectic-representations-of-unitary-groups-i-splitting-uq1lp9d5j5.pdf) was read; the [publisher's DOI](https://doi.org/10.3792/pjaa.77.59) leads to ProjectEuclid, whose direct access was blocked. No visual collation with Kudla is claimed.

Murase §§1.2–1.8 defines, for A(w,w′)=Tr(w*Qw′), the operator M(g) by integration of ψ(A(w,gw)/2)ρ((1−g)w), with the self-dual measure for A(w,(g−1)w′). Its factor is λ_E(ψ)^(−ν_g)χ(Δ(Q(g−1))), ν_g=dim_E W/ker(g−1), χ|F×=ε. Theorem 1.8 makes their product a representation. Remark 1 includes the archimedean case; Remark 2 asserts coincidence with Kudla in the split model. The proof does not restrict the residual characteristic to be different from 2: Q₂ is included.

We do not use Remark 2 to guess the normalisation: the following computations fix the scalars. Murase's symbols are not automatically those of the manuscript; **his χ must be ξ⁻¹** in the dictionary of left actions of 49.

## 1. Common conventions

We write ψ=ψ_k and N(z)=bar(z)z. In a polarisation of the skew-hermitian space one chooses column coordinates w=(x,y) with

\[
A(w,w')=\operatorname{Tr}_{E/F}(x^*y'-y^*x'),\qquad Q=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]

In the original coordinates of 49 this corresponds to Q=−jH if H is the hermitian matrix: A(w,w′)=Tr(j⟨w′,w⟩)=Tr(−j⟨w,w′⟩). The change to hyperbolic coordinates removes j from Q; it does not change A. The Heisenberg operator is

\[
\rho(x,y)f(t)=\psi\bigl(\operatorname{Tr}(t^*y)+\tfrac12\operatorname{Tr}(x^*y)\bigr)f(t+x).
\]

Its multiplier is ψ(A/2), exactly P2. To read Kudla's form A/2 with the same operator one requires ψ_K(u)=ψ_k(2u). Then η(u)=ψ_K(u/2)=ψ_k(u). This conversion affects both the operator and its self-dual measure: one cannot change only the name of ψ.

Let λ=λ_E(ψ) be the Gaussian constant of the form N with the self-dual measure for ψ(Tr(bar u v)). We shall use

\[
\int_E\psi(aN(u))\,du=\lambda\,\epsilon(a)|a|_F^{-1},\qquad \lambda^2=\epsilon(-1),
\]

interpreting the integral as a stabilised/distributional Gaussian. By hermitian diagonalisation, with the self-dual measure of the pairing corresponding to B, the integral of ψ(u*Bu) is λ^sε(det B), s=rank B. This is the explicit normalisation that allows one to avoid an informal identification of Weil indices.

## 2. Unipotents

Let g_B=[[I,0],[B,I]], B*=B of rank s. Then Q(g_B−1) has a block B and a zero block; ν_g=s and ξ_g=det B modulo norms. In the quotient by the kernel, the integrand of M(g_B) applied to f(t) is

\[
\psi(u^*Bu-\operatorname{Tr}(t^*Bu))f(t)
=\psi((u-t)^*B(u-t)-t^*Bt)f(t).
\]

Hence M(g_B)=λ^sε(det B)T_B, where T_Bf(t)=ψ(−t*Bt)f(t). The splitting factor λ^(−s)χ(det B) cancels that constant exactly, since χ(det B)=ε(det B). Thus M_χ(g_B)=T_B. The computation holds for singular B on passing to the quotient and does not divide by 2 inside a lattice.

## 3. Levi and choice of the character

For m(a)=diag(a,(a*)⁻¹), suppose first that a−I is invertible. One has ν=2d and

\[
\Delta(Q(m(a)-1))\equiv(-1)^d\overline{\det a}^{-1}\pmod{N(E^\times)}.
\]

By χ(bar z⁻¹)=χ(z) and λ²=ε(−1), Murase's factor is χ(det a). In the integral M(m(a)), integrating in the variable y imposes the linear equation (I−a)u+(I−a⁻¹)t=0. The Jacobian |det(I−a)|_E⁻¹ cancels that factor in the self-dual measure, leaving

\[
M(m(a))f(t)=|\det a|_E^{-1/2}f(a^{-1}t).
\]

The identity extends by continuity from the open set where a−I is invertible. Therefore

\[
M_\chi(m(a))f(t)=\chi(\det a)|\det a|_E^{-1/2}f(a^{-1}t).
\]

In 49, the left action on Y is (a*)⁻¹, and its required factor is ξ(det(m(a)|Y))⁻¹=ξ(det a)⁻¹. **Choosing χ=ξ⁻¹ gives exactly that factor.** Both restrictions to F× remain ε. Taking χ=ξ without changing the conventions would give, in general, the wrong inverse character; Murase's assertion of coincidence must be read with this dictionary.

## 4. Weyl: computation of the factor 2

In a hyperbolic plane let τ=[[0,−1],[1,0]]. Then ν_τ=2 and det(Q(τ−1))=2. For w=(u,v), the product of the two phases of the integrand of M(τ) is

\[
\psi\bigl(2N(v)+\operatorname{Tr}(t^*(v-u))\bigr)f(t+u+v).
\]

Putting z=t+u+v, the exponent becomes 2N(v+t)−Tr(t*z). The self-dual measure of W for A(w,(τ−1)w′) is |2|_F times the product measure. Integrating over v gives λ ε(2)|2|_F⁻¹, so that

\[
M(\tau)=\lambda\epsilon(2)\mathcal F_-,\qquad
\mathcal F_-f(t)=\int_Ef(z)\psi(-\operatorname{Tr}(t^*z))\,dz.
\]

The splitting factor is λ⁻²χ(2)=λ⁻²ε(2), and hence

\[
M_\chi(\tau)=\lambda^{-1}\mathcal F_-.
\]

The factors |2| cancel **also in residual characteristic 2**. In j orthogonal planes the computation factorises and gives λ^(−j) times the partial Fourier transform. For F=R,E=C,ψ(t)=exp(−2πit), λ=−i, coinciding with the negative Gaussian scalar used in the archimedean computation of 49.

## 5. Bruhat formula and limit of the literal collation

The parabolic of Y and the partial Weyl elements generate the split U(W). The three preceding computations, together with Murase's theorem, construct a representation with the required phases on those generators. In the right decomposition p₁τ_jp₂, the compositions with the operators of the parabolic effect only linear changes of variables and quadratic multiplications: their Jacobians are positive. They introduce no additional Gaussian phase. The phase of the partial transform is λ^(−j), and the characters of the two parabolic factors multiply to give ξ(det(p₁p₂|Y)). One thus obtains the explicit supplement

\[
\omega(g)=\xi(x(g))\lambda_E(\psi_k)^{-j(g)}r_Y(g)
\]

read with the conversion of actions of 49. The measure of r_Y is fixed positive and unitary; no freedom of sign remains hidden in Haar.

**(a) reconstructed:** existence and normalisation of the split representation, actions of Levi/unipotent/Weyl, character, factor 2 and Gaussian phase, by means of the explicit formula with λ. **(c) documentary, still delimited:** it was not possible to verify on page 364 of Kudla that his exact symbol γ_F(η∘RV), with the original definition of RV and of "character of second degree", is literally λ_E(ψ_k), and not a notation for a scaled form whose conversion would have to be written out. Murase's Remark 2 supports the identification, but does not replace that collation of definitions. It is not claimed that Kudla's Theorem 3.1 was read.

For a reconstructed argument, P3 can be replaced by the preceding formula **with λ defined explicitly** and the computations of §§1–4; the uses of Levi, Fourier and the archimedean scalar are determined. To certify the citation of Kudla word for word, his original convention RV is missing. Nor should one conclude from these computations alone the whole compatibility of doubling (P4), global tensor/product and rationality of the theta: these are distinct obligations audited in the Weil branch, which must use this same normalisation consistently. This supplement is not a mere assertion that "some splitting exists".

## 6. Closure of the identification of RV by means of another primary source

**Updates the pending item of §5.** [Chan, *Period identities of CM forms on quaternion algebras*, §5.1, p. 10, Definition 5.1 and Theorem 5.2](https://web.math.princeton.edu/~charchan/CM.pdf), original research available on the author's page, was collated. Kudla's splitting is reproduced there with the same definition x(g)=det(p₁p₂|Y), j(g), restriction ξ|F×=ε^m and factor γ_F((ψ/2)∘RV). For E=F(√u), it defines the latter by

\[
(u,\det V)_F\,\gamma_F(-u,\psi/2)^m\gamma_F(-1,\psi/2)^{-m}.
\]

In our case m=1,detV=1,ψ_K/2=ψ_k. Let G_ψ(a) be the index of the Gaussian ψ(ax²). Whether γ_F(a,ψ) denotes G_ψ(a) or its normalised version G_ψ(a)/G_ψ(1), the quotient that appears is the same. The identity G_ψ(−1)=G_ψ(1)⁻¹ is obtained by conjugating the Gaussian. Therefore

\[
\gamma_F(\eta\circ RV)
=\frac{G_{\psi_k}(-u)}{G_{\psi_k}(-1)}
=G_{\psi_k}(1)G_{\psi_k}(-u)
=\gamma(\psi_k(x^2-u y^2))
=\lambda_E(\psi_k).
\]

The penultimate equality is multiplicativity of the Gaussian integral in orthogonal coordinates; x²−uy²=N_(E/F)(x+y√u). The self-dual measures transform with the corresponding positive Jacobian, without phase. One thus obtains the **exact** equality, not merely equality of moduli nor up to a possible quotient character. It holds over Q₂ as well: no identity uses that 2 is a unit. At the real place the computation gives −i for negative ψ_k, as was already checked.

**Updated verdict (a) for P3 in its mathematical normalisation**, with indirect collation of Kudla's published statement by means of Chan's precise reproduction and independent reconstruction of the generators by means of Murase. Only the documentary limitation of not having opened the original pages of Kudla 1994 remains; no undetermined mathematical constant is left by it.

## 7. Propagation: the representation is not being changed

The equality of §6 identifies the coefficient γ of P3 exactly with λ. The actions on the parabolic and on Weyl, which generate the split group, coincide; therefore no undetected local character remains. The splitting is not replaced by another that coincides only globally.

**Doubling and orthogonal sums (P4).** Murase's formula works without supposing W split. For W=W₁⊥W₂ and g=(g₁,g₂), the quotient W/ker(g−1) is the sum of the two quotients; the phase is a sum, the self-dual measure is a product, ν=ν₁+ν₂ and Δ=Δ₁Δ₂ modulo norms. On tensors of smooth vectors, Fubini for stabilised integrals (and distributional Gaussians at infinity) gives M(g)=M(g₁)⊗M(g₂); the splitting factors also multiply. In particular ω_(W⊕W⁻)(g,1)=ω_W(g)⊗1, with no scalar. Naturality under isometries follows by changing variables in that same integral and preserving Δ modulo norms. Since the split splitting already coincides with P3, its restriction to the double is exactly the definition D2 of the paper. Thus P4 and `pwf:sum` keep their operators, even in non-split spaces.

**Change of character, used in 54.** For R_g=Q(g−1), on the non-degenerate quotient one has R_g*=R_g g⁻¹. Hence Δ/overlineΔ=det g, since g acts as the identity on its kernel. Changing υ to υ·(μ∘bc) changes χ_Murase=υ⁻¹ to χ_Murase·(μ∘bc)⁻¹; the quotient of splittings is μ(det g)⁻¹. The universal sign in left actions is −1. The assertion holds in D2 as well and does not come from attributing an arbitrary sign to the change of character.

**Vacuum, finite phase and integrality.** Since the same local operators are identified on the whole of U(W), any computation of the scalar on a vacuum line and its evaluation at 0 uses the same operator, not merely a proportional one. For this reason the existing review of `vacfix` and of the phase supplement of 49 applies without adding a new root of unity. This observation does not claim to prove by itself each strong phase formula: the distinction of the report REVIEW-PHASE49-V2 between strong formula and sufficient consequences remains. The contribution here is to remove an ambiguity of splitting that could alter those consequences.

**Theta, Poisson, CM/CS constants.** The action of the Heisenberg group, the additive character, the self-dual measures and the archimedean Gaussian factor are preserved. The proof of rational invariance 49:872–914 uses the Levi action and the uniqueness of the theta functional, plus doubling; all of these remain the same. It does not need an informal compensation of phases over the places. Thus its identification with the rational Weil action used by Poisson/Siegel is preserved. In particular the theta functional, the Fock vacuum and the argument of the theta functions have not been rescaled, so that this explanatory replacement of γ by λ introduces no modification of CM periods, Chowla–Selberg constants, norms or local integrals. Their arithmetic verifications remain those of THETA; the present collation does not replace them, but it removes this possible change of normalisation.

**Final status of this obligation:** no discrepancy of characters, factor 2, Weil index or doubling scalar remains undetermined in the comparison P3/Murase. The exact identification allows the earlier computations of the Weil branch and the applications of 49–56 to be used with their original normalisations.

## 8. Unequivocal verdict and final collation with the phase supplement

**Mathematical verdict (a), reconstructed with the preceding explicit formulas. The pending access to the original of 1994 does not constitute a remaining mathematical obligation.** The alternative primary source fixes the formula, and the reconstruction by generators fixes the operator, its signs and constants.

REVIEW-PHASE49-V2 was reread in full. Its premises reduce to: character υ constructed with the declared infinity type and non-ramification; finiteness of ideal classes; Heisenberg and self-dual lattices; Rao operators and arithmetic changes of polarisation; exact P3 and doubling; character of the stabiliser on the vacuum line; split models above 2 and computation of the non-split unimodular vacuum in odd characteristic. The phase report already collates Rao and the vacuum computation in Pan; P3 and doubling, which remained (c) there, are discharged by §§1–7 of this note. No new global premise arises from that discharge.

The field A of the supplement is stable under conjugation, and σ commutes with it on A because each generator υ(a) has all its conjugates of modulus 1. The Gram identities are finite algebraic sums after supports and subgroups of constancy are fixed; σ is not applied to infinite integrals. The ℓ-integrality uses operators and inverses at p≠ℓ and the smooth character of finite image of the stabiliser at p=ℓ. The transition to rational representatives requires only integrality above ℓ by approximation, not a component exactly zero. Hence the closure of P3 allows the two sufficient properties of δ_g to be concluded without any loss and without invoking Short Forms, auxcore or GRH. The strong classification of the phase remains distinct and not necessary.

## 9. Limited cross-review of the correction ν^flat in 54

The definitions 54:2695 and 7584 were compared with the operative computation 2730–2736 and with REVIEW-54-THREE-EXCHANGES-V2. With the printed definition ν^flat=ν″υ^m/χ′, the equality α=χ′ν^flatυ^m=ν″υ^m is false: the left-hand side is ν″υ^(2m). It cannot be treated as a harmless constant factor.

The supplementary replacement ν^flat=ν″/χ′ makes the following simultaneously true: α=ν″υ^m; αβ⁻¹=υ^m with β=ν″; the weight of ν^flatυ^m equal to m−#ι; and

\[
j+(t+k-1)/2+m-3m-(7m+k)/2=j+(t-11m-1)/2=n'.
\]

Thus the L-factor of the third exchange is the declared one, not one shifted by m. The correction removes exactly the extra υ^m in the two definitions; it keeps that factor in the formulas of F_i. The quotient ν″/χ′ remains independent of the twist and without tame part. Therefore it changes neither conductors nor local integrality conditions. What is confirmed is the necessity and coherence of this correction with the exchange, not an independent closure of all the steps of global spanning of 54, which are reviewed in its other notes.
