> **V2 update:** any reference in this note to the former global character failure of 53 is withdrawn. The current verdict and the new inventory of repairs are in the V2 final report. This note preserves the thematic programme, not an external endorsement.

# Mathematical connections and research programme

The central pattern proposed by the series is to convert **divisibility of theta coefficients into a one-sided inequality on primes**, by comparing short forms, spanning of almost all of a space, and a lower limit for its covolume. It is a concrete connection and one capable of producing independent problems. In this review it was not proved that this connection closes the proof of GRH, nor that it constitutes a new field by itself.

The difficulty of RH does not logically force its solution to invent a new branch. A new and valid combination of known tools could also solve it. The productive question is what exact bridge the work contributes, which of its pieces are proved, and which results survive if the conclusion about RH is withdrawn.

Internal sources: P57 `main.tex`, particularly lines 100–120, 485–640 and 833–843; collation with the statements of P46 and the specific review of P51/52. The references to "the proposal" describe the argument of the manuscript, not a theorem certified by this report.

## The proposed mechanism

The first conceptual chain is

\[
\text{Frobenius on CM and local divisibility}
\longrightarrow\text{integral and small theta coefficients}
\longrightarrow\text{lattices of automorphic forms}.
\]

The second chain attempts to compare those lattices in two ways:

\[
\begin{array}{c}
\text{seesaw and bounds for all the conjugates}\to\text{upper bound for volumes},\\
\text{L-values, congruences, twists and product formula}\to\text{lower bound}.
\end{array}
\]

The second moment of the Poincaré map must guarantee that the first way reaches a proportion `1−O(b^{-2})` of the dimension. The comparison cancels a common main quantity `H_main`. The remaining imbalance is identified with `R_{d,q}(x)`; a one-sided analytic criterion aims to convert its bound into absence of zeros.

The potentially distinctive point is, therefore, **to make the local arithmetic of theta coincide quantitatively with an error in the distribution of primes**, after cancelling large main terms in determinants. Listing many specialities does not establish that bridge: it is established by the identities, the independence with respect to the twist, the uniform ranks and the final errors.

P57:100–112 says expressly that rows A–C do not enter that deduction and that no Hodge index theorem for those objects is constructed there. For that reason it is not appropriate to present the mechanism as a geometric proof of the sign of the adelic intersection. It is an automorphic and arithmetic route to the sign, reinterpreted afterwards in the Weil framework.

## Which connections already exist

| Connection | Antecedent | What the series would have to add |
|---|---|---|
| Adelic spaces, explicit formula and zeros | [Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068) interprets explicit formulas by means of a noncommutative trace. | Precise additional objects or properties; the association "adeles + trace + RH" is not new. |
| CM theta, algebraic coefficients and Hecke L-values | [Bannai–Kobayashi, *Algebraic theta functions and p-adic interpolation of Eisenstein-Kronecker numbers*](https://arxiv.org/abs/math/0610163) constructs and studies that bridge. | Simultaneous divisibility, non-ordinary cases, exact constants and uniformity required by 49/54; it is not enough to cite the existence of the classical bridge. |
| Masses of hermitian lattices and L-values | [Gan–Hanke–Yu, *On an exact mass formula of Shimura*](https://web.math.princeton.edu/~jonhanke/Web-02/Mass-Formula-of-Shimura/shimura-mass.pdf) gives exact formulas with local factors. | The combination with the moments, the growth of rank and a complete count of measures. |
| Archimedean growth, finite information and arithmetic slopes | The slope method has systematic antecedents; see [Bost, *Evaluation maps, slopes, and algebraicity criteria*](https://ems.press/books/standalone/21/408). | The concrete realisation by means of Poincaré maps and theta chains, with the error on primes as residual quantity. The similarity with slopes is conceptual, not a checked application of a theorem of Bost. |
| Automorphic comparison between unitary forms | [Labesse, *Changement de base CM et séries discrètes*](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf) develops base change, stability and multiplicity under precise conditions. | The exact comparison for the chosen spaces and projectors, or a valid independent proof. |

The bibliographic search carried out identifies antecedents, but it is not an exhaustive priority search. "I did not find an identical result" does not certify novelty.

## What would be a specific contribution if validated

1. **A uniform second-moment theorem with main constant one.** P51 requires simultaneous growth of the rank, weight, field and level. If it is proved with all those parameters and with an error tending to zero, it would be a concrete result that can be studied without mentioning RH. The later deep audit reconstructed its local mechanisms, counts, Bessel, covolume and masses, with explicit local corrections that preserve the bounds; see SPANNING.md. Green's external classification and the ambient data remain identified inputs, not theorems re-proved from scratch.
2. **A multivariable divisibility law with Frobenius action on the CM places.** The distinctive content would be the exact formula for the exponents and its control at each prime, not only the existence of divisibility of theta coefficients.
3. **A covolume principle with a choice of twist depending on each prime.** It must explain why several integral realisations control one and the same global object, how their losses add up and why incompatible lattices are not mixed.
4. **A proved cancellation between those two laws that leaves a recognisable sum over primes.** This is the most important connection for the RH objective. A formal identity between symbols does not prove it: it requires that both sides measure the same forms, the same lattices, the same norms and the same range of parameters.
5. **An integral local treatment outside the Fontaine–Laffaille range.** If the exponents of cup products of P56 are correct in all the generality claimed, it would be an independent contribution. Its validity is decided in the review of P56; it cannot be inferred from the formal success of the chain.

The bibliographic priority of these points is not established. The mathematical state must be read individually: several mechanisms of the second moment were reconstructed; the exchange and the covolume chain present the character failure documented in ERROR-53-CHARACTERS.md.

## An abstract principle that can indeed be isolated

There is an elementary piece that makes the error budget visible. Let `V` be a hermitian space of dimension `d`. Suppose that `s` linearly independent vectors are constructed, with `s≥(1−ε)d`, whose squared norm is at most

\[
\exp(H-mR+E_S).
\]

By Hadamard, the logarithm `c` of their Gram determinant satisfies

\[
c\le s(H-mR+E_S).
\]

Suppose also a lower bound, for that same family and its same integral data,

\[
c+2\delta\ge d(H-E_C).
\]

Then, by exact substitution and rearrangement,

\[
s mR\le (s-d)H+sE_S+dE_C+2\delta.
\]

This is a checked algebraic implication. It is a conditional model; it does not certify that the automorphic hypotheses of the manuscript hold. It shows three aspects that any development must preserve:

- `ε` must be small relative to the magnitude of `H`; omitting `(s−d)H` is illegitimate, in particular if `H` can be negative.
- The index `δ` is a quantitative loss and does not disappear by calling the forms "integral" after a normalisation.
- A constant in the norm for each lift, dimension or place can become a large term after taking logarithms and determinants.

The language of "semistability" must be used with precision. The bound of the manuscript for families of almost full rank does not automatically prove a slope inequality for **all** subspaces and sublattices. To obtain a complete theory of slopes those additional properties have to be formulated and proved.

## Programme that allows progress even if the proof of RH remains open

| Project | Concrete result to be required | Test of success |
|---|---|---|
| CM model of small dimension | Divisibility formula for one theta and one inert prime, with period and lattice fixed | Exact examples and a local proof that includes all the denominators; separate ordinary and supersingular primes. |
| A single theta exchange | Seesaw identity with explicit measures and computed constant | Check in a non-zero case that both sides and their changes under twist coincide. |
| A single determinant | Relation between a Gram and L-values, with saturation indices | Verify both the complex equality and the valuation at each exceptional prime. |
| Second moment in fixed rank | Estimate with exact main term for a family of levels or weights | Compare the constant of mass, formal degree and covolume before pursuing total uniformity. |
| Passage to growing rank | Theorem with explicit error functions in all the parameters | A book of inequalities showing that the final margin remains positive in the required range. |
| Local-to-global twists | Abstract theorem converting a family of local conditions into a bound for a global index | Finiteness, compatibility of the lattices and summability of losses proved, without assuming a non-existent common basis. |
| Modular formalisation | Lemmas on norms, Gram, local products and parameter domains | Each final result carries an inventory of axioms and of analytic inputs; compiling a conditional implication is not equivalent to proving its hypotheses. |

A useful presentation of that programme would be "slope methods for automorphic lattices and theta divisibility". It is a **proposed description of a line of work**, not the name of a new recognised discipline nor a claim of priority. Its value would be measured by reproducible independent theorems, examples and additional applications.

## Attribution and boundary of what is proved

P57:833–843 attributes to Levent Alpoge the mathematics organised by the three theorems and the path to the zero-free half-plane; it attributes to the series its organisation, names and writing into papers. This report preserves that attribution as the author himself declares it. It does not verify here the external authorship nor the claim, also present in that passage, that a complete formal proof of GRH exists.

Therefore, the series' own contribution that can be described without exceeding the evidence is the **expository architecture and the attempt to make a Weil framework compatible with that automorphic route**. The priority of each additional construction and the mathematical validity of the final bridge require the particular reviews. A promising connection can guide research even when one of the theorems it intended to use turns out to be incorrect; to develop that connection it is advisable to reformulate the failed theorem explicitly, keep the valid pieces and measure what weaker conclusion they allow.


## Balance after the deep audit: what to keep and what to redesign

The closure of [HOCHSCHILD-43.md](../deep-review/HOCHSCHILD-43.md) contributes a piece separable from the RH objective: the computation of twisted complexes of the fast semilocal crossed product. Its content is not only a verbal analogy. Continuous contractions are exhibited with explicit losses of weight and conductor, and an equivalence that distinguishes the trivial real twist from the non-trivial one. This construction makes it possible to investigate which arithmetic information that homology retains and which it discards. Its insensitivity result shows, in turn, why it is not enough to identify that shadow with a positive intersection.

The 51/52 front contributes another concrete connection: a Siegel orbital average, the geometry of pairs of frames and the reproduction of coefficients of discrete series combine to control an almost optimal second moment. The weights change along the Heisenberg tower and the moduli cancel exactly. The uniformity is sustained by two distinct mechanisms: gain of depth and control of frequencies. The exact computation of masses and covolumes prevents an absolute constant from appearing for each dimension. These verifications are documented in SPANNING.md, including the repairs of the p-adic cutoff, of the order of multiplication in FJ and of the homogeneous exponent of the tube. It would be reasonable to extract an autonomous theorem from this front and submit it to specialised external review before using it as part of a conclusion about RH.

A third connection, reconstructed by the multiplicities front, is the joint use of integrality and L² analysis to force finiteness: after regularising the orbital integral, its character coefficients are integers; Bessel/Peter–Weyl limits their quadratic sum; hence only finitely many coefficients can be non-zero. It is a concrete mathematical mechanism that deserves comparison with other proofs of character formulas. It is not claimed here that it is new: novelty would require identifying exactly which regularisation, hypotheses and formula are not in the literature.

The failure [ERROR-53-CHARACTERS.md](../deep-review/ERROR-53-CHARACTERS.md) changes the priority of the programme. Before comparing determinants the characters of the Weil representations have to be made compatible under product and restriction. It is not enough to add a scalar factor: a non-trivial character depends on the elements of the groups. The immediate project is to formulate an exchange identity with the correct characters, verify that its source and target spaces are those used by the chain, and recompute its dependence on the twist. Only afterwards can one ask whether the lower covolume still controls the same lattice as the upper short forms.

Thus, the two directions with auditable intermediate results are the semilocal homological computation and the quantitative Poincaré second moment. The decisive bridge between theta divisibility and bounds on primes remains a programme conditional on repairing the exchange identities and their consequences. There is not sufficient evidence to christen a new, already established branch, but there is a set of precise mathematical problems that can be developed without presupposing the RH conclusion.


The subsequent review [COMPLETION-FORM-43.md](../deep-review/COMPLETION-FORM-43.md) also reconstructed the complete symbol, the signature, the completions, the rulings and the relative determinant. An especially useful conceptual result is the proof that approximations to the same rulings can give diagonal values 0, positive or divergent for the scalar form; in the limit over S, some slow families give 1 and others give 0. This delimits exactly what a future intersection theory would have to add: an intrinsic choice of domain/topology or of regularisation that selects the pairing, and a sign principle compatible with it. The present constructions do not give that principle, and their own counterexamples prevent obtaining it simply by extending the scalar form by continuity. It is a checked mathematical restriction for any later development of the framework.
