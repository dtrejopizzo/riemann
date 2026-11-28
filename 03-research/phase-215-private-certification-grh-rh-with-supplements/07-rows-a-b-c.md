# Papers 43 44 and 45 Weil framework

The radial identification of row C with the explicit formula has the correct signs and normalisation. The family of measures of row B satisfies its main laws of composition and contact. The declared main theorems of 43 were reconstructed in [HOCHSCHILD-43.md](deep-review/HOCHSCHILD-43.md) and [COMPLETION-FORM-43.md](deep-review/COMPLETION-FORM-43.md), with verdict **(a)** in their precise scopes. Neither bibliographic priority nor a geometric positivity that the manuscript does not assert is thereby certified. These conclusions do not validate the automorphic deduction of RH: paper 46 itself excludes 43–45 from that deduction.

## Paper 43

There is no single main theorem: the introduction contains `introA`, `introH`, `introB`, `introC` and `introD`, in addition to results on completion and determinant. The verdict for these main theorems is **(a)** after the two deep batches cited. The bibliographic priority of its additional constructions remains **(c)**; the explicit distribution and its symbols are classical.

| Statement | Verdict and scope |
|---|---|
| Decomposition `A_S^×=Γ_S×ker φ`, identification of `C_S` and homomorphic section | **(a)**, `thm:split`, line 777; normalising each finite valuation produces a unique representative, and the section preserves products. |
| Convolution of smeared objects | **(a)** for the formal identity given the definition; it does not prove a geometric theory of intersections over Spec Z. |
| Hochschild computation `thm:shadow`, line 2800 | **(a)** after deep audit: `prop:crossed`, excision, Künneth, local contractions and compatibility with the completed tensor products reconstructed; see HOCHSCHILD-43.md. |
| Formula for the symbol in the radial component | **(a)**: the finite geometric integrals and the digamma identity give the symbol used in 45. |
| Formula for all the components, non-degeneracy, signature and completion | **(a)**: the ramified/odd components, dual density, LF/strong dual topology and infinite-dimensional Gram construction reviewed. See COMPLETION-FORM-43.md. |
| Stabilisation on increasing S | **(a)**: `thm:chartcomp` and `thm:colimtrace`, 5242–5335, for the system of projections defined in the text. |
| Limits of rulings, determinant and Riemann–Roch pairing | **(a)**: explicit incompatible limits, Mertens computation, injection of the Banach completion and Log branch verified. The RR pairing is the defined pair of exponentials, not an index theorem. |

The initial pending item in `thm:shadow(a)`, lines 2841–2849, was discharged: the action is tempered with respect to the concrete rapid weights; the comparisons of resolutions are continuous and preserve labels. The Koszul contraction loses one weight, absorbed by the complete family of seminorms. Excision and Künneth are constructed with complements and finite filtrations by degree, and the contractions of shells have estimates uniform in the shell index. The ledger details the reconstructed proofs, without assuming nuclearity of the p-adic factors nor non-existent equivariant homotopies.
For the stabilisation a direct check can indeed be given. A new prime `ℓ` contributes

`(log ℓ) Σ(k≠0) ℓ^{−|k|/2} F(δ_S(ℓ^{−k}))`.

On the units, the regularised integrand is zero because the inflation is constant in the new coordinate. If `log ℓ` exceeds the radius of the support, each remaining term is zero. The limit is therefore an eventual stabilisation of values, not a spectral convergence of operators nor an unlimited interchange of series.

The relation with the literature must be formulated result by result. The Weil distribution and its reading as a trace are not new: [Connes](https://arxiv.org/abs/math/9811068) develops the geometric realisation of the explicit formula; [Meyer](https://arxiv.org/abs/math/0312305) computes homology of adelic crossed products, with objects that must be distinguished from the algebra and the twisted coefficients of this paper. The semilocal twisted computation proposed here is not automatically identified with Meyer's result, but its bibliographic priority has not been established either. **Novelty of the exact Hochschild package: (c)**. The text acknowledges the logical independence between its two constructions and that the link of coinvariants with the local density is not an identification with Hochschild homology (introduction, 140–151).

## Paper 44

For the two main theorems expressly formulated as `introA` and `introB`, the verdict is **(a)** under the hypotheses indicated; this verdict is not extended automatically to each secondary result of the paper.

The crucial definition is `Frob_n=μ_(c_n K_P(n))`, with `P(n)⊂S_f` and probability Haar measure. The representatives and supports are computed in 1153–1200. Since the convolution of two Haar measures of cosets in this abelian group is the Haar measure of the product coset, and `P(mn)=P(m)∪P(n)`, one obtains `Frob_m*Frob_n=Frob_mn`. The constant modulus `1/n` recovers n. The semigroup inverse keeps A and replaces r by `1/r`; the product with the adjoint is `μ_KA`, not always the unit. Thus no non-existent inverses are introduced.

The argument of non-existence of continuous interpolation (`rem:nointerp`, 1232–1260) is also correct. Projecting to a prime `p≠q` gives a point mass at `1/q` at time `log q`. The convolution roots and continuity force point masses for all times. A continuous homomorphism from the connected interval to the totally disconnected group `Z_p^×` is constant, and the law forces it to be 1, a contradiction.

For the contact (`thm:frobcontact`, 1441–1510), the support condition eliminates all the layers except `p^k` if `n=p^k`. The density on that layer is `p^{-k/2}` and its local volume is `log p`, giving exactly `Λ(n)n^{-1/2}h(1/n)`. For n with two prime factors no layer remains. At the real place, the finite coordinates of `j_infty(x)` are 1; hence the indicator requires `s^N | n−1` at each prime not in P(n). With Haar measure `dx/(2|x|)` and the positive real support, the change `x=e^{-t}` gives `1/(4sinh(t/2))`. This factor is compatible with the statement, without a lost factor 2.

The hypothesis `P(n)⊂S_f` is active throughout the section, from 1149; it is not missing in the theorem although reference is made to the definition. Nor can the contact of functions be replaced by `T(Frob_n)` as a value on a measure: the text itself explains the lack of a continuous weak extension. The Frobenius terminology is an analogy of composition, not a realisation of an endomorphism of a curve.

**Novelty:** the contact coefficients are those of Weil; they are not new. The coset laws are consequences of Haar measure and inverse semigroups. There may be a particular useful presentation of the semilocal semigroup and its obstructions, but priority of that formulation has not been proved. Compare with [Connes–Consani–Marcolli](https://arxiv.org/abs/math/0703392), where the action of idele classes is already connected with correspondences and positivity.

## Paper 45

**(a)** for the comparison theorem `thm:comparison` and the radial normalisation requested; **(a)** for `thm:sufficiency`, the primitive criterion used by 46. Not all the later results on radicals are certified by this conclusion.

The change of variable has an important convention: `Γ_h(w)=h(−log|w|_S)`, so that `λ_−(Γ_h)=Φ_h(1)` and `λ_+(Γ_h)=Φ_h(0)` (523–525). Inverting those labels is by itself harmless in the symmetric term, but they must be kept in the individual identities.

In `lem:radial-trace` (582–634), the real term is

`W_infty(Γ_h)=(γ+log(4π))h(0)+∫₀∞ [e^{−t/2}/(1−e^{−2t})][h(t)+h(−t)−2h(0)e^{−t/2}]dt`.

To check the constant, substituting `u=2t` in the symbol gives

`J(τ)=ψ(1/2)−Re ψ(1/4+iτ/2)`.

Since `ψ(1/2)=−γ−2log2`, the result is `logπ−Re ψ(1/4+iτ/2)`, exactly **−m(τ)** of paper 46. The kernel K of 45 is half the K of 46, since the former multiplies the sum `h(t)+h(−t)`; this is not a discrepancy of normalisation.

I reviewed the contour argument of `lem:contour` and `thm:EF` (772–981). The symmetry transforms the integral on the line −1 into the negative of that on the line 2, which is why `1/(πi)` appears, not `1/(2πi)`. On parametrising the critical line, the factor 1/2 of the gamma logarithmic derivative returns `1/(2π)` in the real integral. The Euler term contributes `−Λ(n)/sqrt(n)` for each `h(±log n)`. The heights chosen avoid the zeros and make the horizontal edges disappear. The compact support makes the prime sum finite.

On subtracting the terms, one obtains

`T_lim(Γ_h)=Φ_h(0)+Φ_h(1)−Σρ Φ_h(ρ)`.

The Mellin product for `F*G†` is `Φ_F(s) overline(Φ_G(1−bar s))`; thus the hermitian formula and the real formula that 46 imports also coincide. Adding `c h(0)` does alter the formula: the value c=0 depends on the normalisation previously chosen, it is not selected by an independent geometric principle.

**Novelty:** it is a verification of compatibility of normalisations and an exposition of the classical explicit formula; not a new explicit formula. The direct antecedents include [Connes–Consani, appendices B, C and E](https://arxiv.org/html/2006.13771), [Meyer, spectral interpretation](https://arxiv.org/abs/math/0412277) and [Burnol, local terms and conductor operator](https://arxiv.org/abs/math/9902080). The explicit construction of even and odd tests may have expository value, but the mechanism of interpolating zeros and damping the tail is correctly attributed to Yoshida/Connes–Consani.

## Junctions of rows A B C with the form of 46

| Junction | Check |
|---|---|
| 43 `thm:chartcomp`, `thm:colimtrace` → 45 `prop:colimit` | **(a)** in the radial case and under the support restrictions indicated. |
| 43 `lem:radialtrace` → 45 `lem:radial-trace` | **(a)**, inversion of the profile compensated by the symmetry of the sums and of the kernel. |
| 44 radial algebra → 45 convolution and moments | **(a)**, Haar measure of the compact group normalised to 1. |
| 45 `thm:EF`, `thm:comparison` → 46 `comparison`, `eq:W` | **(a)**, sign, `2π`, conjugation and polar term compatible. |
| 45 `thm:sufficiency` → 46 `thm:all-support` | **(a)**; each test constructed fits in some window, not necessarily one fixed in advance. |

There is no demonstrated junction between a geometric Hochschild positivity and the positivity of `W_T`: 43 does not assert such a result and 46 does not use it. That absence is not a logical error of the declared chain; it limits the interpretation of "carrying Weil's proof to Spec Z".
