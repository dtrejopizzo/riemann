Question: 
Address the following research objective and research hypothesis:
<research-objective>Survey the literature on the K-theory and cyclic homology of C*-algebras relevant to number theory.
            1.  Focus on the Bost-Connes algebra and its generalizations (`GL₂` system, etc.).
            2.  Search for any results defining a `λ`-ring structure or Adams operations `ψ^n` on the K-theory groups `K_*(A_K)`.
            3.  If found, identify whether these operations are proven to be diagonalizable (after tensoring with `ℚ`) with integer-power eigenvalues `n^j`, thus inducing a canonical integer "Adams weight" grading on `K_*(A_K) ⊗ ℚ`.
            4.  Separately, review the structure of cyclic homology `HC_*(A_K)` and search for any known Connes-style `λ`-operations that induce a similar integer-weight decomposition.</research-objective>
<research-hypothesis>The algebraic K-theory `K_*(A_K)` or cyclic homology `HC_*(A_K)` of the C*-algebra `A_K` associated with the adele class space `C_K` (e.g., the Bost-Connes algebra) admits a `λ`-ring structure and associated Adams operations `ψ^n`, providing a canonical decomposition into integer-weight eigenspaces.</research-hypothesis>

Once you have completed your work, submit your answer in the following format:

<output>
<conclusion>
{conclusion}
</conclusion>
<explanation>
{explanation}
</explanation>
<discussion>
{discussion}
</discussion>
<proposed-next-hypotheses>
{proposed_next_hypotheses}
</proposed-next-hypotheses>
</output>

* `conclusion`: A clear, one-sentence conclusion that directly addresses the <research-hypothesis>.
* `explanation`: A detailed explanation of your findings, the statistical tests you performed, the results and the scientific implications for your findings.
* `discussion`: Discuss the results and contextualize your conclusions with any shortfalls in your analysis or any limitations to your findings.
* `proposed-next-hypotheses`: Propose one or two specific, new hypotheses. Frame them as testable statements. For example, instead of asking "I wonder if other genes are involved?", propose "Other key genes in the 'ABC' pathway are also differentially expressed."


<output>
<conclusion>
The retrieved literature does not establish a λ-ring structure or genuine Adams operations ψ^n on the topological K-theory K_*(A_K) of the Bost–Connes/adele-class-space C*-algebras, and while Connes-style λ-operations do give an n^j-eigenvalue weight decomposition on cyclic homology in commutative/epicyclic settings, an analogous canonical integer-weight decomposition is not shown for HC_*(A_K) of these noncommutative operator algebras.
</conclusion>
<explanation>
| System/algebra | Invariant computed | Main result (explicit groups/decomposition if available) | Operations (endomorphisms, λ-ops, scaling actions) and whether diagonalizable with eigenvalues n^j | Key citation IDs |
|---|---|---|---|---|
| Bost-Connes algebra A1 = C*(Q/Z) ⋊ N×; smooth subalgebra | Structure source for K-theory/HC; explicit HC/HP computed for the smooth subalgebra | A1 is presented as a semigroup crossed product and is Morita equivalent to an adele crossed product. For the smooth algebra, Leichtnam-Nistor prove HP_q(C_c^∞(A_f) ⋊ Q×+) ≅ HP_q(C), hence HP_0 ≅ C and HP_1 ≅ 0. For the full Q×-crossed product they obtain HP_*(C_c^∞(A_f) ⋊ Q×) ≅ HP_*(C) ⊕ H^*(Q×, C) ⊗ C[σ,σ^-1]. | No explicit λ-ring or Adams operations on topological K_*(A1) were found in the retrieved BC-specific literature. On the HC side, the computation uses conjugacy-class decompositions and spectral sequences, not a BC-specific λ-weight decomposition. No proof of rational diagonalization with eigenvalues n^j was found for K_*(A1) or HC_*(A1). | (marcolli2004lecturesonarithmetic pages 59-63, leichtnam2000crossedproductalgebras pages 1-4, leichtnam2000crossedproductalgebras pages 4-8) |
| Cuntz's Q_N (contains the BC algebra) | Topological K-theory | Built from the Bunce-Deddens algebra F with K_0(F) = Q and K_1(F) = Z. Finite stages B_n satisfy K_0(B_n) ≅ Z^(2^(n-1)) and K_1(B_n) ≅ Z^(2^(n-1)); computations use inductive limits and repeated Pimsner-Voiculescu sequences. Related fixed-point/crossed variants satisfy K_0(F') = Q ⊕ Z and K_1(F') = 0. | Natural semigroup endomorphisms by multiplication by primes occur in the construction, but the retrieved sources do not define a λ-ring structure or Adams operations ψ^n on K_*(Q_N). No theorem giving a canonical rational weight splitting with eigenvalues n^j was found. | (cuntz2006$c^*$algebrasassociatedwith pages 7-10, cuntz2006$c^*$algebrasassociatedwith pages 10-13, cuntz2006$c^*$algebrasassociatedwith pages 4-7, cuntz2006$c^*$algebrasassociatedwith pages 13-14, cuntz2006$c^*$algebrasassociatedwith pages 1-4) |
| Ring/adele C*-algebras of Cuntz-Li over Z and number fields K | Topological K-theory | For Z, K_*(A) ≅ Λ^*(Q_{>0}), i.e. exterior-algebra-type K-theory. More generally for number fields, K_*(A[O]) is described using the torsion-free part Γ of K×, often as K_*(A) ≅ K_0(C*(μ)) ⊗ Λ^*(Γ), with additional Z/2-terms in some parity/real-place cases; some full adele crossed products are Morita equivalent to group C*-algebras C*(P_K). | Semigroup-induced endomorphisms κ_d on K-theory are computed in some cases and act diagonally on explicit exterior generators by powers d^(n-k). However, the papers do not identify these maps as Adams operations or construct a λ-ring on K_*(A). Hence there is no published BC-type result in the retrieved corpus proving canonical Adams eigenspaces with eigenvalues exactly n^j in the λ-ring sense. | (cuntz2010c*algebrasassociatedwith pages 29-31, cuntz2010c*algebrasassociatedwith pages 1-4, cuntz2010c*algebrasassociatedwith pages 4-7, cuntz2010c*algebrasassociatedwith pages 36-38, cuntz2010c*algebrasassociatedwith pages 31-34, cuntz2016c∗algebrasassociatedwith pages 8-11, cuntz2016c∗algebrasassociatedwith pages 6-8, cuntz2016c∗algebrasassociatedwith pages 11-14) |
| Generalized BC / endomotive viewpoint (BC, imaginary quadratic, multivariable BC endomotives) | Conceptual framework around K-theory and cyclic homology | Endomotives place BC and its generalizations in a framework using KK-theory and cyclic-module methods; multivariable BC endomotives are described as universal torsion-free Λ-rings at the endomotive or arithmetic algebra level, not as λ-rings on operator K_*(A). | Retrieved sources discuss Frobenius lifts and Λ-ring ideas on endomotives and arithmetic subalgebras, and a canonical R_+^×-action on cyclic homology after cooling/distillation. But no source retrieved defines ψ^n on the topological K-groups K_*(A_K) themselves. No BC-specific diagonalizable Adams-weight grading on K_*(A_K) ⊗ Q was found. | (connes2007noncommutativegeometryand pages 1-3, connes2007noncommutativegeometryand pages 3-5, marcolli2009cyclotomyandendomotives pages 1-3) |
| Leichtnam-Nistor smooth BC / adele crossed-product algebras | Hochschild, cyclic, periodic cyclic homology | They compute HH, HC, HP for the smooth BC algebra via C_c^∞(A_f) ⋊ Q×. Main formulas include HP_q(C_c^∞(A_f) ⋊ Q×+) ≅ HP_q(C), HP_q(C_c^∞(A_f) ⋊ Q×) ≅ HP_q(C) ⊕ HP_q(C[Q×]){-1}, and HP_q(C_c^∞(A) ⋊ Q×) ≅ H_q(Q×, C) ⊗ C[σ,σ^-1]. Homogeneous pieces are described using residue-zero de Rham forms on an infinite torus. | The decomposition is by conjugacy classes, group homology, and periodicity, not by λ-operations. No Connes-style λ-weight splitting or n^j-eigenvalue theorem is present in this BC-specific homology computation. | (leichtnam2000crossedproductalgebras pages 20-23, leichtnam2000crossedproductalgebras pages 1-4, leichtnam2000crossedproductalgebras pages 16-20, leichtnam2000crossedproductalgebras pages 8-12, leichtnam2000crossedproductalgebras pages 4-8) |
| Connes-Consani λ-operations framework for cyclic homology (commutative algebras, schemes, epicyclic modules) | Cyclic homology with λ-operations and weight decomposition | For commutative algebras in characteristic 0, λ-operations Λ_m on cyclic homology give a canonical decomposition HC_n = ⊕_{j≥0} HC_n^(j), with Λ_m acting on the j-th summand by m^j. In the epicyclic formalism, θ(k) induces an N×-action, and when the epicyclic module factors through Fin, HC_n ⊗ Q decomposes into weight spaces on which k acts by k^j. | This is the clearest positive result about λ-operations and n^j-eigenvalues in the retrieved corpus. But it applies to commutative, schematic, or suitably finite epicyclic settings; the literature retrieved does not show that the BC C*-algebra A_K or its smooth BC algebra satisfies these hypotheses in a way yielding a published canonical λ-weight decomposition of HC_*(A_K). | (connes2014cyclichomologyserres pages 5-8, connes2015thecyclicand pages 31-34, connes2015thecyclicand pages 34-35, connes2014cyclichomologyserres pages 1-3, connes2014cyclichomologyserres pages 3-5, connes2014cyclichomologyserres pages 10-13) |
| Adele class space / distilled cyclic module D(A,φ) in Connes-Consani-Marcolli | Cyclic homology with scaling or Frobenius-like action | The adele class space literature constructs a canonical R_+^×-action on HC_0(D(A,φ)) after cooling/distillation, interpreted as Frobenius in characteristic zero, and uses it for spectral realization of zeros of zeta and L-functions and Lefschetz trace formulas. | This is a scaling action, not a proven λ-operation decomposition. The retrieved sources do not present a canonical integer Adams-weight grading with eigenvalues n^j for adele-class-space cyclic homology; instead they use spectral decomposition under R_+^×. | (connes2007noncommutativegeometryand pages 3-5, connes2010theweilproof pages 26-30, connes2010theweilproof pages 13-16, khalkhali2008aninvitationto pages 95-98, connes2010theweilproof pages 3-6) |


*Table: This table consolidates the retrieved results on K-theory and cyclic homology for Bost-Connes-related C*-algebras, adele crossed products, and endomotive constructions. It highlights where explicit λ-operation weight decompositions with eigenvalues n^j are known in general cyclic-homology settings and where such results were not found for the operator algebras A_K themselves.*

1. Scope of algebras and computed invariants

The Bost–Connes algebra A1 is classically presented as the semigroup crossed product C*(Q/Z)⋊N× (equivalently C(Ẑ)⋊N×) and is Morita equivalent to adele crossed products, providing the standard entry point for both K-theory and cyclic theory computations in arithmetic noncommutative geometry. (marcolli2004lecturesonarithmetic pages 59-63)

On the K-theory side, explicit topological K-groups are computed for closely related semigroup/ring C*-algebras that contain the Bost–Connes algebra or generalize it: Cuntz’s ax+b semigroup algebra Q_N contains the BC algebra and is analyzed via inductive-limit and crossed-product decompositions starting from the Bunce–Deddens algebra F with K0(F)=Q and K1(F)=Z; finite stages B_n have K0(B_n)≅Z^{2^{n-1}} and K1(B_n)≅Z^{2^{n-1}} with computations via Pimsner–Voiculescu exact sequences. (cuntz2006$c^*$algebrasassociatedwith pages 7-10, cuntz2006$c^*$algebrasassociatedwith pages 4-7)

More generally, Cuntz–Li compute K-theory for ring/adele crossed-product C*-algebras arising from rings of integers in global fields; in the rational case their K-theory is described as an exterior algebra (e.g. K_*(A)≅Λ^*(Q_{>0}) in the text excerpt) and for number fields K they express K_*(A) in terms of an exterior algebra on the torsion-free part Γ of K× (with additional Z/2-effects depending on the number of real places). (cuntz2010c*algebrasassociatedwith pages 1-4, cuntz2010c*algebrasassociatedwith pages 4-7, cuntz2010c*algebrasassociatedwith pages 31-34)

On the cyclic homology side, Leichtnam–Nistor compute Hochschild/cyclic/periodic cyclic homology for dense smooth subalgebras associated with the Bost–Connes system by passing (via Morita invariance/corner arguments) to algebraic crossed products of test functions on adeles by Q×. They obtain explicit periodic cyclic homology decompositions such as HP_q(C_c^∞(A_f)⋊Q×_+)≅HP_q(C) (so HP_0≅C and HP_1≅0), and for the full Q× action, HP_*(C_c^∞(A_f)⋊Q×)≅HP_*(C) ⊕ H^*(Q×,C)⊗C[σ,σ^{-1}] (with the Laurent polynomial variable σ of degree 2). (leichtnam2000crossedproductalgebras pages 1-4, leichtnam2000crossedproductalgebras pages 20-23)

2. Search for λ-ring / Adams operations on K_*(A_K)

Across the retrieved BC/semigroup/ring C*-algebra literature, no paper explicitly defines a λ-ring structure on K_*(A_K) or constructs Adams operations ψ^n on these topological K-groups in the sense familiar from topological K-theory of spaces or algebraic K-theory of schemes. In particular, the BC and endomotive frameworks emphasize KK-theory as the natural setting for correspondences and K-theory computations, but they do not provide ψ^n operations on K_*(A_K) as part of the standard theory presented in the retrieved excerpts. (connes2007noncommutativegeometryand pages 1-3, connes2007noncommutativegeometryand pages 3-5)

The closest analogue found in the retrieved corpus is that in Cuntz–Li’s computations one can track specific semigroup-induced K-theory endomorphisms κ_d arising from multiplication-by-d type maps; these act diagonally on explicit exterior-algebra generators by integer powers of d (e.g. κ_d scales a k-fold exterior generator by a factor d^{n-k} in the excerpt). This gives a concrete diagonal action for these particular endomorphisms, but it is not presented as coming from a λ-ring structure, nor is it identified with Adams operations ψ^d satisfying λ-ring axioms or functoriality expected of Adams operations on K-theory. (cuntz2010c*algebrasassociatedwith pages 29-31)

Because the defining ψ^n are not present as λ-operations on K_*(A_K) in the retrieved literature, the hypothesis’s stronger claim—canonical diagonalizability of ψ^n after tensoring with Q with eigenvalues exactly n^j and a resulting Adams weight grading on K_*(A_K)⊗Q—cannot be confirmed from the available evidence.

3. Connes-style λ-operations on cyclic homology and weight decompositions

For cyclic homology, the situation is different at the level of general theory: Connes–Consani recall and construct λ-operations Λ_m (m∈N×) on cyclic homology of commutative algebras (over characteristic 0), with the defining compatibility that Λ_m commutes with the Hochschild differential b and scales the Connes operator B by Λ_m B = m B Λ_m. They state that this yields a canonical λ-decomposition HC_n(A)=⊕_{j≥0}HC_n^{(j)}(A) by simultaneously diagonalizing the Λ_m, and that on the jth summand Λ_m acts via the eigenvalue m^j. This is precisely the “integer-weight” eigenspace pattern asked for in the research objective, but it is established here for commutative (scheme-like) inputs rather than BC-type operator algebras. (connes2014cyclichomologyserres pages 5-8)

Connes–Consani further develop λ-operations in the epicyclic framework: for an epicyclic module E there are endomorphisms θ(k) inducing an action of N× on HC_n(E); under the additional hypothesis that E factors through Fin, after tensoring with Q one obtains a decomposition HC_n(E)=⊕_{j≥0}HC_n^{(j)}(E) that diagonalizes the N×-action with characters k↦k^j. The same reference stresses that this rational weight decomposition does not hold for a general epicyclic module. (connes2015thecyclicand pages 34-35, connes2015thecyclicand pages 31-34)

For the adele class space and endomotives, Connes–Consani–Marcolli emphasize a canonical scaling action of R^×_+ on cyclic homology of a “distilled” cyclic module D(A,φ), interpreted as a characteristic-zero Frobenius analogue and used for spectral realization of zeros of zeta/L-functions. However, in the retrieved excerpts this is not presented as a Connes λ-operation decomposition of HC_*(A_K) into integer-weight eigenspaces with eigenvalues n^j; rather, it is a spectral/scaling action used in trace/Lefschetz formulas. (connes2007noncommutativegeometryand pages 3-5, connes2010theweilproof pages 13-16)

4. Implications for the research hypothesis

Taken together, the retrieved literature supports a partial analogue of the hypothesis only on the cyclic-homology side and only in commutative/epicyclic settings: Connes-style λ-operations yield a weight decomposition with eigenvalues m^j there. (connes2014cyclichomologyserres pages 5-8, connes2015thecyclicand pages 34-35)

For the actual Bost–Connes/adele-class-space operator algebras A_K, the retrieved evidence does not show:

(i) a λ-ring structure and Adams operations ψ^n on K_*(A_K); or

(ii) a Connes λ-operation decomposition on HC_*(A_K) analogous to the commutative case.

Instead, the BC-specific cyclic-homology computations available (Leichtnam–Nistor) are obtained via crossed-product and group-(co)homology decompositions and do not invoke λ-operations. (leichtnam2000crossedproductalgebras pages 1-4, leichtnam2000crossedproductalgebras pages 20-23)

Methodological note: no statistical tests were performed because the task is a qualitative literature survey rather than a quantitative meta-analysis. The “tests” in this context consisted of targeted full-text evidence extraction for keywords/structures (λ-ring, Adams ψ^n, λ-operations, eigenvalues n^j, diagonalization) across the retrieved BC-related K-theory papers and cyclic-homology papers, and checking whether the defining eigenspace/eigenvalue properties were proved for A_K itself.
</explanation>
<discussion>
The current evidence base is sufficient to conclude that the strong form of the hypothesis (existence of a canonical λ-ring structure on K_*(A_K) or a Connes λ-decomposition on HC_*(A_K) yielding an integer-weight grading) is not supported by the retrieved BC-specific operator-algebra literature. The negative result should be interpreted cautiously: absence of evidence in the retrieved set does not imply nonexistence, but it indicates that such structures are not standard or widely documented in the main computational papers on BC-type K-theory and cyclic homology that were retrieved.

Important limitations:

1) K-theory computations were mostly for BC-adjacent semigroup/ring C*-algebras (Cuntz’s Q_N; Cuntz–Li ring/adele algebras), not always for the BC algebra A1 itself. These results show strong arithmetic structure (exterior-algebra K-theory) and exhibit semigroup-induced endomorphisms κ_d on K-theory in some settings, which is suggestive of an “Adams-like” scaling pattern but does not provide the λ-ring axioms or functorial ψ^n structure required by the hypothesis. (cuntz2006$c^*$algebrasassociatedwith pages 7-10, cuntz2010c*algebrasassociatedwith pages 29-31, cuntz2010c*algebrasassociatedwith pages 1-4)

2) For cyclic homology, the commutative λ-operations theory is well-developed and yields the desired eigenvalue decomposition, but applying it to noncommutative C*-algebras requires additional structure (e.g., suitable models in the category of cyclic/epicyclic modules, factorization-through-Fin conditions, or explicit λ-operations on the relevant cyclic modules). The epicyclic-site framework explicitly notes that the rational weight decomposition may fail for general epicyclic modules, which is consistent with the lack of a known canonical weight splitting for BC/adele-class-space cyclic modules in the retrieved excerpts. (connes2015thecyclicand pages 34-35)

3) The adele class space literature emphasizes a scaling (R_+^×) action on cyclic homology after a distillation procedure, playing the role of Frobenius. This provides an alternative “weight-like” spectral structure, but it does not directly match the discrete Adams-weight eigenspace requirement (integer j with eigenvalues n^j) and may be fundamentally different in nature. (connes2007noncommutativegeometryand pages 3-5, connes2010theweilproof pages 13-16)
</discussion>
<proposed-next-hypotheses>
1) The semigroup endomorphisms κ_d computed on K-theory for Cuntz–Li ring/adele C*-algebras extend (possibly after passing to a suitable bivariant K-theory theory or adding extra structure such as symmetric power operations on appropriate categories of Hilbert modules) to a genuine λ-ring structure on a refined K-theory object associated to A_K, and their diagonal scaling d^{n-k} matches the eigenvalue pattern of Adams operations on an exterior algebra. (cuntz2010c*algebrasassociatedwith pages 29-31, cuntz2010c*algebrasassociatedwith pages 1-4)

2) The cyclic module D(A,φ) arising from the Connes–Consani–Marcolli “cooling–distillation–dual action” construction for the BC endomotive admits an enhancement to an epicyclic module factoring through Fin after an appropriate “commutative approximation” (e.g., at the level of an arithmetic subalgebra), yielding a Connes–Consani λ-decomposition of HC_*(D(A,φ))⊗Q with discrete weight eigenspaces k↦k^j compatible with the R_+^× scaling/Frobenius action. (connes2007noncommutativegeometryand pages 3-5, connes2015thecyclicand pages 34-35)
</proposed-next-hypotheses>
</output>

References

1. (marcolli2004lecturesonarithmetic pages 59-63): Matilde Marcolli. Lectures on arithmetic noncommutative geometry. Preprint, Jan 2004. URL: https://doi.org/10.48550/arxiv.math/0409520, doi:10.48550/arxiv.math/0409520. This article has 9 citations.

2. (leichtnam2000crossedproductalgebras pages 1-4): Eric Leichtnam and Victor Nistor. Crossed product algebras and the homology of certain p-adic and adélic dynamical systems. K-theory, 21:1-23, Sep 2000. URL: https://doi.org/10.1023/a:1007847331024, doi:10.1023/a:1007847331024. This article has 7 citations and is from a peer-reviewed journal.

3. (leichtnam2000crossedproductalgebras pages 4-8): Eric Leichtnam and Victor Nistor. Crossed product algebras and the homology of certain p-adic and adélic dynamical systems. K-theory, 21:1-23, Sep 2000. URL: https://doi.org/10.1023/a:1007847331024, doi:10.1023/a:1007847331024. This article has 7 citations and is from a peer-reviewed journal.

4. (cuntz2006$c^*$algebrasassociatedwith pages 7-10): Joachim Cuntz. $c^*$-algebras associated with the $ax+b$-semigroup over ℕ. Preprint, Jan 2006. URL: https://doi.org/10.48550/arxiv.math/0611541, doi:10.48550/arxiv.math/0611541. This article has 5 citations.

5. (cuntz2006$c^*$algebrasassociatedwith pages 10-13): Joachim Cuntz. $c^*$-algebras associated with the $ax+b$-semigroup over ℕ. Preprint, Jan 2006. URL: https://doi.org/10.48550/arxiv.math/0611541, doi:10.48550/arxiv.math/0611541. This article has 5 citations.

6. (cuntz2006$c^*$algebrasassociatedwith pages 4-7): Joachim Cuntz. $c^*$-algebras associated with the $ax+b$-semigroup over ℕ. Preprint, Jan 2006. URL: https://doi.org/10.48550/arxiv.math/0611541, doi:10.48550/arxiv.math/0611541. This article has 5 citations.

7. (cuntz2006$c^*$algebrasassociatedwith pages 13-14): Joachim Cuntz. $c^*$-algebras associated with the $ax+b$-semigroup over ℕ. Preprint, Jan 2006. URL: https://doi.org/10.48550/arxiv.math/0611541, doi:10.48550/arxiv.math/0611541. This article has 5 citations.

8. (cuntz2006$c^*$algebrasassociatedwith pages 1-4): Joachim Cuntz. $c^*$-algebras associated with the $ax+b$-semigroup over ℕ. Preprint, Jan 2006. URL: https://doi.org/10.48550/arxiv.math/0611541, doi:10.48550/arxiv.math/0611541. This article has 5 citations.

9. (cuntz2010c*algebrasassociatedwith pages 29-31): Joachim Cuntz and Xin Li. C*-algebras associated with integral domains and crossed products by actions on adele spaces. Journal of Noncommutative Geometry, 5:1-37, Dec 2010. URL: https://doi.org/10.4171/jncg/68, doi:10.4171/jncg/68. This article has 53 citations and is from a peer-reviewed journal.

10. (cuntz2010c*algebrasassociatedwith pages 1-4): Joachim Cuntz and Xin Li. C*-algebras associated with integral domains and crossed products by actions on adele spaces. Journal of Noncommutative Geometry, 5:1-37, Dec 2010. URL: https://doi.org/10.4171/jncg/68, doi:10.4171/jncg/68. This article has 53 citations and is from a peer-reviewed journal.

11. (cuntz2010c*algebrasassociatedwith pages 4-7): Joachim Cuntz and Xin Li. C*-algebras associated with integral domains and crossed products by actions on adele spaces. Journal of Noncommutative Geometry, 5:1-37, Dec 2010. URL: https://doi.org/10.4171/jncg/68, doi:10.4171/jncg/68. This article has 53 citations and is from a peer-reviewed journal.

12. (cuntz2010c*algebrasassociatedwith pages 36-38): Joachim Cuntz and Xin Li. C*-algebras associated with integral domains and crossed products by actions on adele spaces. Journal of Noncommutative Geometry, 5:1-37, Dec 2010. URL: https://doi.org/10.4171/jncg/68, doi:10.4171/jncg/68. This article has 53 citations and is from a peer-reviewed journal.

13. (cuntz2010c*algebrasassociatedwith pages 31-34): Joachim Cuntz and Xin Li. C*-algebras associated with integral domains and crossed products by actions on adele spaces. Journal of Noncommutative Geometry, 5:1-37, Dec 2010. URL: https://doi.org/10.4171/jncg/68, doi:10.4171/jncg/68. This article has 53 citations and is from a peer-reviewed journal.

14. (cuntz2016c∗algebrasassociatedwith pages 8-11): Joachim Cuntz. C∗-Algebras Associated with Algebraic Actions, pages 151-165. Springer International Publishing, Jan 2016. URL: https://doi.org/10.1007/978-3-319-39286-8\_6, doi:10.1007/978-3-319-39286-8\_6. This article has 1 citations.

15. (cuntz2016c∗algebrasassociatedwith pages 6-8): Joachim Cuntz. C∗-Algebras Associated with Algebraic Actions, pages 151-165. Springer International Publishing, Jan 2016. URL: https://doi.org/10.1007/978-3-319-39286-8\_6, doi:10.1007/978-3-319-39286-8\_6. This article has 1 citations.

16. (cuntz2016c∗algebrasassociatedwith pages 11-14): Joachim Cuntz. C∗-Algebras Associated with Algebraic Actions, pages 151-165. Springer International Publishing, Jan 2016. URL: https://doi.org/10.1007/978-3-319-39286-8\_6, doi:10.1007/978-3-319-39286-8\_6. This article has 1 citations.

17. (connes2007noncommutativegeometryand pages 1-3): Alain Connes, Caterina Consani, and Matilde Marcolli. Noncommutative geometry and motives: the thermodynamics of endomotives. Advances in Mathematics, 214:761-831, Dec 2007. URL: https://doi.org/10.48550/arxiv.math/0512138, doi:10.48550/arxiv.math/0512138. This article has 76 citations and is from a highest quality peer-reviewed journal.

18. (connes2007noncommutativegeometryand pages 3-5): Alain Connes, Caterina Consani, and Matilde Marcolli. Noncommutative geometry and motives: the thermodynamics of endomotives. Advances in Mathematics, 214:761-831, Dec 2007. URL: https://doi.org/10.48550/arxiv.math/0512138, doi:10.48550/arxiv.math/0512138. This article has 76 citations and is from a highest quality peer-reviewed journal.

19. (marcolli2009cyclotomyandendomotives pages 1-3): Matilde Marcolli. Cyclotomy and endomotives. Aug 2009. URL: https://doi.org/10.1134/s2070046609030042, doi:10.1134/s2070046609030042. This article has 27 citations.

20. (leichtnam2000crossedproductalgebras pages 20-23): Eric Leichtnam and Victor Nistor. Crossed product algebras and the homology of certain p-adic and adélic dynamical systems. K-theory, 21:1-23, Sep 2000. URL: https://doi.org/10.1023/a:1007847331024, doi:10.1023/a:1007847331024. This article has 7 citations and is from a peer-reviewed journal.

21. (leichtnam2000crossedproductalgebras pages 16-20): Eric Leichtnam and Victor Nistor. Crossed product algebras and the homology of certain p-adic and adélic dynamical systems. K-theory, 21:1-23, Sep 2000. URL: https://doi.org/10.1023/a:1007847331024, doi:10.1023/a:1007847331024. This article has 7 citations and is from a peer-reviewed journal.

22. (leichtnam2000crossedproductalgebras pages 8-12): Eric Leichtnam and Victor Nistor. Crossed product algebras and the homology of certain p-adic and adélic dynamical systems. K-theory, 21:1-23, Sep 2000. URL: https://doi.org/10.1023/a:1007847331024, doi:10.1023/a:1007847331024. This article has 7 citations and is from a peer-reviewed journal.

23. (connes2014cyclichomologyserres pages 5-8): Alain Connes and Caterina Consani. Cyclic homology, serre's local factors and <i>λ</i>-operations. Jul 2014. URL: https://doi.org/10.1017/is014006012jkt270, doi:10.1017/is014006012jkt270. This article has 27 citations and is from a peer-reviewed journal.

24. (connes2015thecyclicand pages 31-34): Alain Connes and Caterina Consani. The cyclic and epicyclic sites. Rendiconti del Seminario Matematico della Università di Padova, 134:197-237, Jul 2015. URL: https://doi.org/10.48550/arxiv.1407.3945, doi:10.48550/arxiv.1407.3945. This article has 7 citations.

25. (connes2015thecyclicand pages 34-35): Alain Connes and Caterina Consani. The cyclic and epicyclic sites. Rendiconti del Seminario Matematico della Università di Padova, 134:197-237, Jul 2015. URL: https://doi.org/10.48550/arxiv.1407.3945, doi:10.48550/arxiv.1407.3945. This article has 7 citations.

26. (connes2014cyclichomologyserres pages 1-3): Alain Connes and Caterina Consani. Cyclic homology, serre's local factors and <i>λ</i>-operations. Jul 2014. URL: https://doi.org/10.1017/is014006012jkt270, doi:10.1017/is014006012jkt270. This article has 27 citations and is from a peer-reviewed journal.

27. (connes2014cyclichomologyserres pages 3-5): Alain Connes and Caterina Consani. Cyclic homology, serre's local factors and <i>λ</i>-operations. Jul 2014. URL: https://doi.org/10.1017/is014006012jkt270, doi:10.1017/is014006012jkt270. This article has 27 citations and is from a peer-reviewed journal.

28. (connes2014cyclichomologyserres pages 10-13): Alain Connes and Caterina Consani. Cyclic homology, serre's local factors and <i>λ</i>-operations. Jul 2014. URL: https://doi.org/10.1017/is014006012jkt270, doi:10.1017/is014006012jkt270. This article has 27 citations and is from a peer-reviewed journal.

29. (connes2010theweilproof pages 26-30): Alain Connes, Caterina Consani, and Matilde Marcolli. The Weil Proof and the Geometry of the Adelès Class Space, pages 339-405. Birkhäuser Boston, Jan 2010. URL: https://doi.org/10.1007/978-0-8176-4745-2\_8, doi:10.1007/978-0-8176-4745-2\_8. This article has 45 citations.

30. (connes2010theweilproof pages 13-16): Alain Connes, Caterina Consani, and Matilde Marcolli. The Weil Proof and the Geometry of the Adelès Class Space, pages 339-405. Birkhäuser Boston, Jan 2010. URL: https://doi.org/10.1007/978-0-8176-4745-2\_8, doi:10.1007/978-0-8176-4745-2\_8. This article has 45 citations.

31. (khalkhali2008aninvitationto pages 95-98): Masoud Khalkhali and Matilde Marcolli. An invitation to noncommutative geometry. ArXiv, Feb 2008. URL: https://doi.org/10.1142/6422, doi:10.1142/6422. This article has 131 citations.

32. (connes2010theweilproof pages 3-6): Alain Connes, Caterina Consani, and Matilde Marcolli. The Weil Proof and the Geometry of the Adelès Class Space, pages 339-405. Birkhäuser Boston, Jan 2010. URL: https://doi.org/10.1007/978-0-8176-4745-2\_8, doi:10.1007/978-0-8176-4745-2\_8. This article has 45 citations.