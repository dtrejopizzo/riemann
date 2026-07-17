Question: 
Address the following research objective and research hypothesis:
<research-objective>Search the Arakelov geometry literature for a definition of the Lefschetz lowering operator `Λ` as the adjoint of the raising operator `L` with respect to the arithmetic intersection pairing.
                        1. Identify foundational texts (e.g., by Gillet, Soulé, Zhang, Moriwaki) that define a non-degenerate, symmetric bilinear form on arithmetic Chow groups `widehat{CH}^*(X)` or related cohomology theories (e.g., Deligne-Beilinson), which could serve as the inner product for defining an adjoint.
                        2. Search for any explicit definition of a lowering operator `Λ` as the adjoint of `L = ∪ĉ₁(H)` with respect to such a pairing.
                        3. Look for any calculations of the commutator `[L, Λ]` in this context, and check if the resulting operator `H` acts diagonally on `widehat{CH}^p(X)` with integer eigenvalues (e.g., `(2p-d)·id`), as required for a Hard Lefschetz structure.
                        4. Document whether such a geometrically constructed `Λ` satisfies the axiomatic `[Λ,L]|V_i = (n−2i)·id` relation found in abstract Lefschetz-module formalisms (e.g., Zhang 2020).</research-objective>
<research-hypothesis>A non-degenerate arithmetic intersection pairing `⟨a, b⟩_{ar} = deg(a ⋅ b)` exists on a suitable subspace of arithmetic Chow groups `widehat{CH}^p(X)`. The lowering operator `Λ` can be defined as the formal adjoint of the Lefschetz operator `L = ∪ĉ₁` with respect to this pairing. The resulting commutator `H = [L,Λ]` will act on `widehat{CH}^p(X)` by multiplication by an integer `2p - d`, satisfying the integrality gate.</research-hypothesis>

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
The retrieved Arakelov-geometry sources support the existence of an arithmetic intersection/degree pairing and a Lefschetz raising operator L, but they do not provide (in the accessible excerpts) a general geometric definition of the lowering operator Λ as the adjoint of L with respect to that pairing; instead, Λ is introduced axiomatically via the Lefschetz-module commutator relation [Λ,L]=H with integer eigenvalues.
</conclusion>
<explanation>
1. Foundational pairing (“inner product”) on arithmetic Chow groups.

Gillet–Soulé’s arithmetic Chow groups and intersection product are summarized in Iyengar–Soulé (2017): arithmetic cycles are pairs (Z,gZ) with Green currents, one has an arithmetic intersection product (via the star product on Green currents) and an arithmetic degree map deg: \widehat{CH}^{n+1}(X)_\mathbb{R}\to\mathbb{R}. This yields a bilinear intersection pairing \widehat{CH}^p(X)_\mathbb{R}\times\widehat{CH}^{n+1-p}(X)_\mathbb{R}\to\mathbb{R} by (a,b)\mapsto\deg(a\cdot b). The nondegeneracy of this pairing is explicitly formulated there as an “arithmetic standard conjecture,” not as a theorem in general. (iyengar2017theclassicaland pages 44-47)

Zhang (2020) works with a refined “Arakelov Chow group of admissible cycles” Ch^*(X) inside Gillet–Soulé’s arithmetic Chow group and states it carries a symmetric pairing (used to relate to Beilinson–Bloch height pairings and to define/characterize splittings). In the Lefschetz-module appendix, Zhang explicitly records that L is self-adjoint for the symmetric pairing: (Lx,y)=(x,Ly). (zhang2020standardconjecturesand pages 3-7, zhang2020standardconjecturesand pages 40-44)

Additional evidence for nondegeneracy on restricted subspaces exists (e.g., divisors): Dolce–Gualdi (2022) explains that nondegeneracy of the arithmetic intersection pairing on divisors is equivalent to numerical triviality implying rational equivalence (and proves related results for arithmetic \mathbb{R}-divisors). (dolce2022numericalequivalenceof pages 8-10)

2. Raising operator L.

Iyengar–Soulé define the arithmetic first Chern class of a metrized line bundle \widehat{c}_1(H) and define the Lefschetz operator L to be intersection with \widehat{c}_1(H). (iyengar2017theclassicaland pages 44-47)

Zhang likewise takes L to be the Lefschetz operator given by the first Chern class, acting on (Arakelov) cycle groups and used to define harmonic/admissible splittings and liftings. (zhang2020standardconjecturesand pages 3-7)

3. Does the literature define Λ as the adjoint of L w.r.t. the arithmetic intersection pairing?

In the retrieved excerpts, no source gives an explicit definition of Λ as the formal adjoint of L with respect to the arithmetic intersection pairing (a,b)↦deg(a·b). Iyengar–Soulé do not introduce Λ at all in the relevant pages. (iyengar2017theclassicaland pages 44-47)

Zhang (2020) frequently refers to an “adjoint Λ” in the sense of Lefschetz-module formalism and uses Λ-linearity/Λ-equivariance of canonical splittings, but his appendix defines Λ by the standard sl2/Lefschetz commutator relation rather than by an adjointness condition with respect to the arithmetic degree pairing. In particular, he defines Λ as the unique degree −1 operator satisfying [Λ,L]|V^i = n−2i, and then uses this Λ to formulate Λ-linear splittings and module structures. (zhang2020standardconjecturesand pages 25-29, zhang2020standardconjecturesand pages 36-40)

Thus, the hypothesis “Λ can be defined as the formal adjoint of L with respect to the arithmetic intersection pairing” is not directly confirmed by the retrieved texts; the available construction is instead an abstract Λ obtained from the Lefschetz-module axioms (and then transported to arithmetic situations under standard conjectures). (zhang2020standardconjecturesand pages 36-40, zhang2020standardconjecturesand pages 25-29)

4. Commutator [L,Λ] and integrality of eigenvalues (Hard Lefschetz/sl2 package).

Zhang’s Appendix A gives the explicit commutator relation in the abstract Lefschetz-module setting: for a Lefschetz structure with center n/2 there exists a unique Λ of degree −1 with [Λ,L]|V^i = n−2i. This is exactly the integer-eigenvalue relation required in abstract Lefschetz-module formalisms, and it implies H acts diagonally with integer eigenvalues on graded pieces (with H=[Λ,L]). (zhang2020standardconjecturesand media c6bc7766, zhang2020standardconjecturesand pages 36-40)

However, this is presented as an abstract linear-algebraic consequence/axiomatics of a Lefschetz module; the retrieved excerpts do not provide a general geometric computation on \widehat{CH}^p(X) showing that a geometrically constructed Λ (as an adjoint or otherwise) yields H=(2p−d)·id. The arithmetic standard conjectures in Iyengar–Soulé state Hard Lefschetz-type isomorphisms for powers of L as conjectures, but do not compute [L,Λ]. (iyengar2017theclassicaland pages 44-47)

There is special-case geometric evidence for abelian schemes: Bachmat (1994), building on Künnemann, defines a raising operator L via multiplication by a canonical class d and a lowering-type operator A via Pontrjagin/convolution with a class c (Fourier-transform construction), and reports that these satisfy “Kähler–Lefschetz commutation relations.” This suggests an sl2-type structure in the abelian-scheme Arakelov Chow context, but the explicit eigenvalue formula [Λ,L]|V^i=n−2i (or equivalently H=(2p−d)·id) is not visible in the retrieved excerpts. (bachmat1994onthearakelov pages 17-21, bachmat1994onthearakelov pages 21-25)

5. Summary against the research-hypothesis.

The hypothesis decomposes into three claims:

(i) Existence of a nondegenerate pairing on a suitable subspace: supported conditionally/conjecturally in general (arithmetic standard conjecture) and established in some restricted settings (e.g., divisors). (iyengar2017theclassicaland pages 44-47, dolce2022numericalequivalenceof pages 8-10)

(ii) Defining Λ as the adjoint of L with respect to this pairing: not found explicitly; Zhang’s Λ is characterized by commutator relations, while L is shown self-adjoint with respect to a symmetric pairing. (zhang2020standardconjecturesand pages 40-44, zhang2020standardconjecturesand pages 36-40)

(iii) Commutator H=[L,Λ] acting with integer eigenvalues (2p−d): confirmed in Zhang’s abstract Lefschetz-module formalism as [Λ,L]|V^i=n−2i; not recovered as a general geometric operator identity on arithmetic Chow groups in the retrieved excerpts. (zhang2020standardconjecturesand media c6bc7766, zhang2020standardconjecturesand pages 36-40)

For quick comparison across sources, see the evidence table below.

| Source | Pairing defined? | L defined? | Λ defined? (how) | Adjontness Λ=L*? | Commutator/eigenvalue formula | Notes/limitations | Key citations (pqac-IDs) |
|---|---|---|---|---|---|---|---|
| Gillet–Soulé framework as summarized in Iyengar–Soulé (2017) | Yes: arithmetic intersection product on arithmetic Chow groups and arithmetic degree; nondegeneracy stated as conjecture | Yes: L is intersection with arithmetic first Chern class | No explicit Λ in cited pages | No | No explicit [Λ,L] or diagonal eigenvalue formula; Hard Lefschetz stated conjecturally | Foundational source for pairing and L, but not for a geometrically constructed lowering operator | (iyengar2017theclassicaland pages 44-47) |
| Künnemann (1996), Higher Picard varieties and the height pairing | Yes: Beilinson–Bloch height pairing and Néron–Tate pairing on higher Picard varieties; positivity results | Yes: Lefschetz operator from ample line bundle on Chow groups or subquotients | No explicit global Λ on arithmetic Chow groups in retrieved pages; symbols such as Λ_p^λ are polarization maps, not clearly the lowering operator adjoint to L | No explicit statement in retrieved pages | No explicit [Λ,L] formula in retrieved pages | Important for height pairings and Hard Lefschetz or Hodge index on certain subquotients, but not an explicit adjoint-lowering construction on arithmetic Chow groups | (kunnemann1996higherpicardvarieties pages 1-4, kunnemann1996higherpicardvarieties pages 11-14, kunnemann1996higherpicardvarieties pages 4-8, kunnemann1996higherpicardvarieties pages 14-15, kunnemann1996higherpicardvarieties pages 8-11) |
| Zhang (2020), global Arakelov Chow groups | Yes: symmetric pairing on Arakelov Chow group of admissible cycles; L self-adjoint in appendix; height and intersection pairings used in arithmetic splitting theory | Yes: L from first Chern class; acts on graded pieces and admissible Chow groups | Yes, but in abstract Lefschetz-module formalism; on arithmetic side treated via induced R[L,Λ]-module structure and Λ-linear splittings | Not explicitly defined as the adjoint of L with respect to the arithmetic intersection pairing in retrieved pages; only says adjoint Λ and proves L self-adjoint | Yes in appendix, abstractly: unique degree -1 operator with [Λ,L] on V^i equal to n-2i; no full geometric computation on arithmetic Chow groups yielding (2p-d) id found | Best match to abstract Lefschetz-module axiom; arithmetic application depends on standard conjectures or assumptions and does not present Λ as formal adjoint via degree pairing | (zhang2020standardconjecturesand pages 3-7, zhang2020standardconjecturesand pages 36-40, zhang2020standardconjecturesand pages 40-44, zhang2020standardconjecturesand pages 25-29, zhang2020standardconjecturesand media c6bc7766) |
| Bachmat (1994), Arakelov Chow groups of abelian schemes | Yes: intersection pairing on Arakelov Chow groups referenced or used | Yes: L defined by product with a canonical class d | Yes in special abelian-scheme setting: lowering operator A defined by convolution with a class c via Fourier construction | Not defined as adjoint to L via the intersection pairing in retrieved pages | Kähler–Lefschetz commutation relations asserted; explicit diagonal eigenvalue formula not visible in retrieved excerpts | Strongest geometric special-case evidence for an arithmetic lowering operator, but only for abelian schemes and without explicit adjointness or eigenvalue formula in retrieved text | (bachmat1994onthearakelov pages 17-21, bachmat1994onthearakelov pages 21-25, bachmat1994onthearakelov pages 1-8, bachmat1994onthearakelov pages 25-28) |
| Künnemann (1993), Chow motives of abelian schemes | No arithmetic pairing; motivic or Chow-motive setting instead | Yes | Yes: motivic analogue of Λ via Fourier theory | No adjointness statement in retrieved excerpt | Yes: commutator relation with L proved motivically; yields hard Lefschetz and Lefschetz decomposition | Highly relevant precedent, but not Arakelov or arithmetic Chow groups and not defined from arithmetic intersection pairing | (k�nnemann1993alefschetzdecomposition pages 1-4) |
| Dolce–Gualdi (2022), arithmetic R-divisors | Yes: generalized arithmetic intersection pairing; nondegeneracy for divisors tied to numerical equals rational equivalence | Not the focus | No | No | No | Useful evidence that nondegeneracy of arithmetic pairing is known at least for divisors, but unrelated to a Lefschetz lowering operator | (dolce2022numericalequivalenceof pages 8-10) |
| Bost (1999), arithmetic surfaces | Yes: nondegenerate bilinear form or intersection product for arithmetic surfaces | Not the focus in retrieved pages | No | No | No | Important for arithmetic-surface pairings, but not for Λ as adjoint of L | (bost1999potentialtheoryand pages 1-4) |


*Table: This table summarizes the main sources found for arithmetic intersection pairings, the status of the Lefschetz raising operator L, and whether a lowering operator Λ is explicitly defined as its adjoint or shown to satisfy sl2-style commutator relations. It helps distinguish foundational pairing results from the much weaker evidence for a geometrically defined arithmetic Λ.*
</explanation>
<discussion>
Scope and limitations of this review.

• Source accessibility: The foundational Gillet–Soulé 1990 “Arithmetic intersection theory” paper was flagged as unobtainable in the tool output, so this review relies on later expositions/surveys and on Zhang’s 2020 preprint excerpts; this may miss an explicit adjoint-definition of Λ if it exists in GS90 or other hard-to-access sources.

• Definition of “adjoint”: In Kähler geometry, Λ is often the adjoint of L with respect to the Hodge inner product. In the arithmetic setting, the natural pairing is the arithmetic intersection/degree pairing (a,b)↦deg(a·b), which is not automatically positive definite and may be degenerate outside conjectural subspaces. The retrieved texts show (a) the pairing and (b) an sl2/Lefschetz-module Λ defined by commutator axioms, but do not connect them via an explicit adjointness identity of the form ⟨Lx,y⟩=⟨x,Λy⟩.

• Geometric vs axiomatic Λ: Zhang’s framework is consistent with abstract Lefschetz-module axioms and yields the desired integer-eigenvalue commutator relation by construction. This meets objective (4) (“axiomatic [Λ,L]|V_i=(n−2i)id”) but does not establish the research-hypothesis’s geometric mechanism (“Λ is the adjoint w.r.t. arithmetic intersection pairing”) as a proven definition.

• Special cases: For abelian schemes, Bachmat/Künnemann provide a geometric lowering operator built from Fourier theory and assert Kähler–Lefschetz commutation relations, making this the most promising setting to test whether that operator coincides with an adjoint with respect to the arithmetic intersection pairing. The present excerpts do not provide the explicit diagonal eigenvalue statement, so verifying H=(2p−d)·id in this geometric construction remains open from the retrieved evidence.
</discussion>
<proposed-next-hypotheses>
1) (Abelian-scheme test) For an arithmetic abelian scheme with canonical Fourier-transform lowering operator A (Bachmat/Künnemann), A equals the adjoint of L (intersection with \widehat{c}_1 of a symmetric polarization) with respect to the arithmetic intersection pairing restricted to the “harmonic/admissible” Arakelov Chow subgroup.

2) (Zhang-compatibility test) Under Zhang’s arithmetic standard conjectures ensuring a Lefschetz-module structure on an admissible Arakelov Chow group, the induced Λ characterized by [Λ,L]|V^i=n−2i is uniquely determined by requiring L to be self-adjoint and Λ to be the adjoint of L with respect to the symmetric pairing on Ch^*(X); i.e., the commutator-defined Λ coincides with the pairing-adjoint when the pairing is nondegenerate.
</proposed-next-hypotheses>
</output>

References

1. (iyengar2017theclassicaland pages 44-47): A IYENGAR and SBYC SOULÉ. The classical and arithmetic standard conjectures. Unknown journal, 2017.

2. (zhang2020standardconjecturesand pages 3-7): Shou-Wu Zhang. Standard conjectures and height pairings. Preprint, Jan 2020. URL: https://doi.org/10.48550/arxiv.2009.07089, doi:10.48550/arxiv.2009.07089. This article has 10 citations.

3. (zhang2020standardconjecturesand pages 40-44): Shou-Wu Zhang. Standard conjectures and height pairings. Preprint, Jan 2020. URL: https://doi.org/10.48550/arxiv.2009.07089, doi:10.48550/arxiv.2009.07089. This article has 10 citations.

4. (dolce2022numericalequivalenceof pages 8-10): Paolo Dolce and Roberto Gualdi. Numerical equivalence of ℝ-divisors and shioda–tate formula for arithmetic varieties. Journal für die reine und angewandte Mathematik (Crelles Journal), 2022:131-154, Jan 2022. URL: https://doi.org/10.1515/crelle-2021-0081, doi:10.1515/crelle-2021-0081. This article has 0 citations.

5. (zhang2020standardconjecturesand pages 25-29): Shou-Wu Zhang. Standard conjectures and height pairings. Preprint, Jan 2020. URL: https://doi.org/10.48550/arxiv.2009.07089, doi:10.48550/arxiv.2009.07089. This article has 10 citations.

6. (zhang2020standardconjecturesand pages 36-40): Shou-Wu Zhang. Standard conjectures and height pairings. Preprint, Jan 2020. URL: https://doi.org/10.48550/arxiv.2009.07089, doi:10.48550/arxiv.2009.07089. This article has 10 citations.

7. (zhang2020standardconjecturesand media c6bc7766): Shou-Wu Zhang. Standard conjectures and height pairings. Preprint, Jan 2020. URL: https://doi.org/10.48550/arxiv.2009.07089, doi:10.48550/arxiv.2009.07089. This article has 10 citations.

8. (bachmat1994onthearakelov pages 17-21): E Bachmat. On the arakelov chow group of arithmetic abelian schemes and other spaces with symmetries. Unknown journal, 1994.

9. (bachmat1994onthearakelov pages 21-25): E Bachmat. On the arakelov chow group of arithmetic abelian schemes and other spaces with symmetries. Unknown journal, 1994.

10. (kunnemann1996higherpicardvarieties pages 1-4): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.

11. (kunnemann1996higherpicardvarieties pages 11-14): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.

12. (kunnemann1996higherpicardvarieties pages 4-8): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.

13. (kunnemann1996higherpicardvarieties pages 14-15): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.

14. (kunnemann1996higherpicardvarieties pages 8-11): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.

15. (bachmat1994onthearakelov pages 1-8): E Bachmat. On the arakelov chow group of arithmetic abelian schemes and other spaces with symmetries. Unknown journal, 1994.

16. (bachmat1994onthearakelov pages 25-28): E Bachmat. On the arakelov chow group of arithmetic abelian schemes and other spaces with symmetries. Unknown journal, 1994.

17. (k�nnemann1993alefschetzdecomposition pages 1-4): Klaus K�nnemann. A lefschetz decomposition for chow motives of abelian schemes. Inventiones mathematicae, 113:85-102, Dec 1993. URL: https://doi.org/10.1007/bf01244303, doi:10.1007/bf01244303. This article has 76 citations and is from a highest quality peer-reviewed journal.

18. (bost1999potentialtheoryand pages 1-4): JB Bost. Potential theory and lefschetz theorems for arithmetic surfaces. Annales Scientifiques De L Ecole Normale Superieure, 32:241-312, Mar 1999. URL: https://doi.org/10.1016/s0012-9593(99)80015-9, doi:10.1016/s0012-9593(99)80015-9. This article has 95 citations and is from a highest quality peer-reviewed journal.