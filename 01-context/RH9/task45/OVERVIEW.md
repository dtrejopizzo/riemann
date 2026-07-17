Question: 
Address the following research objective and research hypothesis:
<research-objective>Conduct a comprehensive literature survey on F1-geometry, λ-rings, and associated motivic theories. The primary goal is to find any existing definition for a cohomology theory `H*(Spec Z x_{F1} Spec Z)` that satisfies the following:
            1.  Provides a non-trivial candidate for `H^1` that could plausibly be related to the space of zeros `Π⊥`.
            2.  Is inherently integer-graded (i.e., passes the "Integrality Gate").
            3.  Contains a natural geometric class (e.g., a "diagonal class" `[Δ]`) that could serve as the Lefschetz operator `L`.
            4.  Mentions or speculates on structures analogous to Poincaré duality or a Hodge-Riemann bilinear form.
            Document any explicit obstructions or stated difficulties in defining such structures.</research-objective>
<research-hypothesis>The formalism of λ-rings and F1-geometry (e.g., Borger, Connes-Consani, Soulé) contains constructions for a hypothetical "absolute surface" `Spec Z x_{F1} Spec Z` that either implicitly or explicitly define a non-trivial integer-graded cohomology theory and a candidate for a diagonal (Lefschetz) class.</research-hypothesis>

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
The surveyed λ-ring and \(\mathbb F_1\)-geometry literature does not currently contain an explicit, nontrivial, integer-graded cohomology theory \(H^*(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z)\) with a diagonal/Lefschetz class and Poincaré/Hodge–Riemann-type structures; instead it offers only partial analogues (notably Connes–Consani’s \(H^1\) realizing zeta/L-function zeros on \(\mathbb P^1_{\mathbb F_1}\)) and largely frames the absolute surface as a motivating but unresolved construction.
</conclusion>
<explanation>

## 1. Scope and method
This survey used tool-based retrieval and evidence extraction across core sources representing the main paradigms explicitly mentioned in the hypothesis: Borger’s \(\Lambda\)-rings-as-descent formalism, Connes–Consani’s functorial \(\mathbb F_1\)-schemes (Mo-schemes) and later scaling-site/\(\Gamma\)-ring program, and expository syntheses emphasizing Deninger/Manin “absolute motives” language (Le Bruyn; Thas; Manin–Marcolli). No statistical tests were performed, because the objective is definitional/existential rather than empirical; the analysis is based on direct textual evidence and comparison.

## 2. Does an explicit cohomology \(H^*(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z)\) exist in these frameworks?
Across the retrieved corpus, the expression “absolute surface” \(\operatorname{Spec}(\mathbb Z)\times_{\mathbb F_1}\operatorname{Spec}(\mathbb Z)\) appears as a central *motivation* but not as a constructed object equipped with a cohomology theory.

* Le Bruyn’s notes recount that Smirnov’s original aim was to study intersection theory on the “surface” \(\operatorname{Spec}(\mathbb Z)\times_{\mathbb F_1}\operatorname{Spec}(\mathbb Z)\), but “he could not invent what this ‘surface’ might be,” motivating work instead on the easier \(\mathbb P^1_{\mathbb F_1}\times \operatorname{Spec}(\mathbb Z)\) and on topological refinements (Habiro topology). This is explicit in both the text evidence and the extracted page region containing the phrase \(\operatorname{Spec}(\mathbb Z)\times_{\mathbb F_1}\operatorname{Spec}(\mathbb Z)\). (bruyn2013absolutegeometryand pages 1-4, bruyn2016absolutegeometryand media 232f7bc7)
* Thas emphasizes that in ordinary scheme theory one has \(\operatorname{Spec}(\mathbb Z)\times \operatorname{Spec}(\mathbb Z)\simeq \operatorname{Spec}(\mathbb Z)\) (final object issue), hence a “deeper” absolute base \(\Upsilon\) (identified with \(\mathbb F_1\)) is needed for a meaningful product \(\times_{\Upsilon}\); but the required absolute base and absolute cohomology remain conjectural. (thas2016thecombinatorialmotivicnature pages 3-6)
* Borger explicitly frames \(\operatorname{Spec}\mathbb Z\otimes_{\mathbb F_1}\mathbb Z\) as a hoped-for surface “bearing some kind of intersection theory,” but also stresses that the map \(\operatorname{Spec}\mathbb Z\to \operatorname{Spec}\mathbb F_1\) is meaningful only at the level of big étale topoi with \(\Lambda\)-structure (“not on the level of schemes”), which blocks naïve formation of \(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z\) as a scheme. (borger2009lambdaringsandthe pages 1-3)

**Result:** No retrieved work supplies a definition of \(H^*(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z)\) (as a Weil-style cohomology or otherwise) satisfying the four requested criteria.

## 3. Criterion-by-criterion analysis

### (1) Nontrivial candidate for \(H^1\) plausibly related to zeros \(\Pi_\perp\)
The strongest explicit “nontrivial \(H^1\) related to zeros” construction found is **not** attached to the absolute surface, but to \(\mathbb P^1_{\mathbb F_1}\) (and its evaluation on the adèle-class monoid):

* Connes–Consani define a sheaf \(\Omega\) on the geometric realization of \(\mathbb P^1_{\mathbb F_1}\) and compute its sheaf cohomology, stating that \(H^1(\mathbb P^1_{\mathbb F_1},\Omega)\) provides the **spectral realization of zeros of \(L\)-functions**; \(H^0\) gives a Fourier-transform graph. This gives a concrete, integer-graded cohomology group whose spectral content is directly linked to zeta/L-function zeros. (connes2010schemesover𝔽1 pages 3-5)

In Deninger/Manin-style accounts (as summarized by Thas), one expects “absolute cohomology groups” \(H^i(\operatorname{Spec}\mathbb Z,*_{abs})\) and an “absolute Frobenius” \(\Theta\) whose regularized determinants yield zeta factors; in such a picture \(H^1\) must be nontrivial to encode zeros, but the construction is explicitly presented as *proposed/conjectural*. (thas2016thecombinatorialmotivicnature pages 3-6)

### (2) Integrality gate: inherently integer-graded
The Connes–Consani \(H^0/H^1\) on \(\mathbb P^1_{\mathbb F_1}\) is standard sheaf cohomology, hence integer-graded. (connes2010schemesover𝔽1 pages 3-5)

However, none of the retrieved texts provides an integer-graded theory for \(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z\). In the \(\Gamma\)-ring direction, Connes–Consani relate homotopy groups \(\pi_1,\pi_0\) of an \(\mathbb S\)-module construction to classical \(H^0,H^1(\operatorname{Spec}\mathbb Z,\mathcal O(D))\), which is also integer-graded (by homotopy degree), but again not for the absolute surface. (connes2021segalsgammarings pages 23-25)

### (3) Natural geometric diagonal class \([\Delta]\) to serve as Lefschetz operator \(L\)
No retrieved source constructs \([\Delta]\in H^*(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z)\) or any diagonal cycle class for the hypothetical absolute surface.

Borger’s program explicitly motivates the absolute surface by the desire for intersection theory (and thus implicitly diagonals/correspondences), but the evidence available here does not provide a diagonal class or a Lefschetz operator as cup product with a geometric class. (borger2009lambdaringsandthe pages 1-3)

Thas (via Deninger/Manin) uses the phrase “absolute Lefschetz motive” for the conjectural \(h^2\) of \(\operatorname{Spec}\mathbb Z\), but this is not the same as constructing a diagonal class on an absolute surface, and no operator \(L\) is defined in the sense requested. (thas2016thecombinatorialmotivicnature pages 3-6)

### (4) Poincaré duality or Hodge–Riemann bilinear form analogues
No retrieved paper provides a Poincaré duality statement or Hodge–Riemann bilinear relations for a cohomology of \(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z\).

There are, however, adjacent structures that show what such a package might resemble:

* Borger proves strong restrictions on cohomology of finite-type \(\Lambda\)-schemes (e.g., diagonal Hodge numbers \(h^{i,j}=0\) for \(i\neq j\)) and abelianization constraints on Galois actions, which is compatible with a “Tate-type” (and hence potentially polarizable) picture, but does not supply a duality or positivity form for the absolute surface. (borger2009lambdaringsandthe pages 3-5)
* Consani–Marcolli’s archimedean cohomology program describes mixed \(\mathbb Q\)-Hodge structures with filtrations and monodromy-type operators, which is conceptually adjacent to Lefschetz/duality formalisms, but it is not formulated as a cohomology of \(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z\). (consani2006archimedeancohomologyrevisited pages 13-15)

## 4. Explicitly stated obstructions/difficulties
The evidence contains several concrete obstructions that directly bear on why the hypothesis (as stated) is not yet realized:

1. **The absolute surface itself is not defined/constructed.** Smirnov’s inability to “invent” \(\operatorname{Spec}(\mathbb Z)\times_{\mathbb F_1}\operatorname{Spec}(\mathbb Z)\) is explicitly reported, and the literature uses easier substitutes. (bruyn2013absolutegeometryand pages 1-4, bruyn2016absolutegeometryand media 232f7bc7)
2. **Naïve scheme-level base change/fiber products over \(\mathbb F_1\) are not available in Borger’s approach.** Borger states the relevant map \(\operatorname{Spec}\mathbb Z\to \operatorname{Spec}\mathbb F_1\) is topos-level, “not on the level of schemes,” making the desired fiber product “meaningless” as an ordinary scheme. (borger2009lambdaringsandthe pages 1-3)
3. **Scarcity of descent/finite type objects.** Borger stresses few finite-type \(\mathbb Z\)-schemes descend to \(\mathbb F_1\), and most \(\mathbb F_1\)-objects produced are not finite type, complicating classical intersection/cohomological formalism. (borger2009lambdaringsandthe pages 3-5)
4. **Missing Frobenius-equipped cohomology.** Manin–Marcolli explicitly state that “cohomology with action of a Frobenius” is “conspicuously missing” in various \(\mathbb F_1\) geometries, undermining direct import of Weil cohomology patterns (including Lefschetz/duality). (manin2020homotopytypesand pages 1-4)
5. **Conjectural nature and analytic regularization in Deninger’s program.** Thas emphasizes that \(H^i(\operatorname{Spec}\mathbb Z,*_{abs})\) and \(\Theta\) are only proposed and involve regularized determinants on infinite-dimensional spaces. (thas2016thecombinatorialmotivicnature pages 3-6)
6. **Restrictions/degeneracies in candidate absolute points and accessible objects.** Connes–Consani note obstructions such as “no morphism \(\mathbb B\to \mathbb Z\)” for a naïve base and state their class of \(\mathbb F_1\)-varieties is still restrictive and excludes positive genus curves, leaving \(\overline{\operatorname{Spec}\mathbb Z}\) out of reach. (connes2011characteristic1entropy pages 3-5, connes2010schemesover𝔽1 pages 1-3)

## 5. Implication for the research hypothesis
The hypothesis predicts that λ-rings/\(\mathbb F_1\)-geometry already “contains constructions” that (implicitly or explicitly) define a nontrivial integer-graded cohomology for the absolute surface and a diagonal (Lefschetz) class. The survey finds:

* There **are** concrete, integer-graded cohomology theories in the ecosystem (e.g., \(H^1(\mathbb P^1_{\mathbb F_1},\Omega)\)) that are explicitly tied to zeta/L-function zeros, hence they plausibly relate to a “zero space” \(\Pi_\perp\) in spirit. (connes2010schemesover𝔽1 pages 3-5)
* But these constructions do **not** extend (in the retrieved literature) to a cohomology of \(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z\), nor do they provide the diagonal/Lefschetz class and duality/positivity package.

Accordingly, the hypothesis is **not supported** by the retrieved evidence, though it remains plausible as a *direction* because several frameworks are explicitly designed to make such a surface meaningful (Borger’s descent, Connes–Consani’s absolute bases, Deninger’s motives).

| Framework/authors | Object(s) with defined cohomology | Definition of H^1 candidate | Integer-graded? | Diagonal/Lefschetz class? | Duality/Hodge-Riemann? | Explicit obstructions/difficulties | Key citation IDs |
|---|---|---|---|---|---|---|---|
| Borger, Λ-rings as descent to \(\mathbb F_1\) | No explicit cohomology for \(\operatorname{Spec}\mathbb Z \times_{\mathbb F_1} \operatorname{Spec}\mathbb Z\); uses classical étale/Hodge-theoretic consequences for finite-type \(\Lambda\)-schemes over \(\mathbb Z\) | None for the absolute surface; only indirect restrictions on cohomology of \(\Lambda\)-schemes (abelian Artin–Tate, diagonal Hodge numbers) | Not as a new theory for the surface; only ordinary integer grading in imported classical cohomology | No explicit diagonal class; "intersection theory" on the hoped-for surface is motivational only | No explicit Poincaré duality or Hodge–Riemann package for the absolute surface; only classical inputs such as Lefschetz theorems/fixed-point formula are cited | Fiber product over \(\mathbb F_1\) is meaningful only at topos/\(\Lambda\)-level, not naïve schemes; very few finite-type schemes descend; most resulting spaces are not finite type; archimedean place not captured | (borger2009lambdaringsandthe pages 1-3, borger2009lambdaringsandthe pages 3-5) |
| Connes–Consani, Mo-schemes / early \(\mathbb F_1\)-schemes | \(\mathbb P^1_{\mathbb F_1}\) with sheaf \(\Omega\) on geometric realization; adèle-class monoid examples | Explicitly \(H^1(\mathbb P^1_{\mathbb F_1},\Omega)\), used for spectral realization of zeros of \(L\)-functions; this is the clearest nontrivial \(H^1\) candidate in the surveyed literature, though not for \(\operatorname{Spec}\mathbb Z \times_{\mathbb F_1} \operatorname{Spec}\mathbb Z\) | Yes, ordinary sheaf-cohomological grading \(H^0,H^1\) | No diagonal or Lefschetz class for the absolute surface is provided | No Poincaré duality or Hodge–Riemann analogue stated for this \(H^1\) construction | The hypothetical curve \(C=\overline{\operatorname{Spec}\mathbb Z}\) is still out of reach; accessible class of \(\mathbb F_1\)-varieties remains restrictive and excludes positive-genus curves in the cited discussion | (connes2010schemesover𝔽1 pages 3-5, connes2011characteristic1entropy pages 3-5, connes2010schemesover𝔽1 pages 1-3) |
| Connes–Consani, scaling site / Hochschild-sheaf methods | Scaling site \(\mathscr S\); quotient sheaf \(\mathcal L^2/\Sigma_E\); also Hochschild homology of the noncommutative adèle-class space | Spectral realization appears in \(H^0(\mathscr S,\mathcal L^2/\Sigma_E)\), not \(H^1\); thus relevant to zeros but not an \(H^1\) theory for the absolute surface | Yes, integer-graded as sheaf cohomology/Hochschild homology degrees | No natural diagonal class \([\Delta]\) or Lefschetz operator for \(\operatorname{Spec}\mathbb Z \times_{\mathbb F_1} \operatorname{Spec}\mathbb Z\) identified in the cited evidence | No Poincaré duality or Hodge–Riemann statements in the cited evidence | Gives spectral/cohomological realizations of zeta zeros on a different geometric object than the desired absolute surface | (connes2207hochschildhomologytrace pages 1-3) |
| Connes–Consani, Segal \(\Gamma\)-rings / absolute base \(\mathbb S\) | \(\mathbb S\)-algebraic approach to \(\operatorname{Spec}\mathbb Z\); \(H(D)\) with homotopy groups related to \(H^0,H^1(\operatorname{Spec}\mathbb Z,\mathcal O(D))\) | Candidate appears indirectly via \(\pi_0(H(D))\) related to \(H^1(\operatorname{Spec}\mathbb Z,\mathcal O(D))\), but not for the absolute surface | Yes: homotopy groups \(\pi_1,\pi_0\) and vanishing for higher \(n>1\) are explicitly degree-indexed | No diagonal/Lefschetz class for an absolute surface in cited text | No duality/Hodge–Riemann analogue in cited text | Relation defining \(\pi_0\) is not generally an equivalence relation; topos of reflexive graphs is invoked to retain information; still no explicit \(\operatorname{Spec}\mathbb Z \times_{\mathbb F_1} \operatorname{Spec}\mathbb Z\) | (connes2021segalsgammarings pages 1-3, connes2021segalsgammarings pages 23-25) |
| Deninger–Manin conjectural absolute motives as surveyed by Thas | Hypothetical absolute cohomology \(H^i(\operatorname{Spec}\mathbb Z,*_{abs})\) and motives \(h^0,h^1,h^2\) for \(\operatorname{Spec}\mathbb Z\) | Nontrivial \(H^1\) is conjecturally required to account for zeta zeros, but no concrete construction is given | Intended to be integer-graded by degree \(i\), but only conjecturally | Absolute Lefschetz motive is discussed conceptually for \(h^2\), but no geometric diagonal class \([\Delta]\) on the absolute surface is defined | No formulated Poincaré duality or Hodge–Riemann bilinear form in the cited evidence | \(\mathbb F_1\) / absolute base remains conjectural; cohomology groups and absolute Frobenius are unconstructed; regularized determinants are infinite-dimensional and analytically delicate; ordinary category gives \(\operatorname{Spec}\mathbb Z\times \operatorname{Spec}\mathbb Z\cong \operatorname{Spec}\mathbb Z\) so a deeper base is required | (thas2016thecombinatorialmotivicnature pages 3-6) |
| Le Bruyn / Smirnov-style absolute surface heuristics with Habiro topology | No cohomology theory defined for the absolute surface; simpler object \(\mathbb P^1_{\mathbb F_1}\times \operatorname{Spec}\mathbb Z\) discussed instead | None | No | No | No | Absolute surface explicitly sought but not invented; exotic/noncompact Habiro topology, non-co-maximal cyclotomic ideals, non-split extensions, and possible noncommutative character of \(\mathbb F_1\)-geometry obstruct a classical cohomological theory | (bruyn2013absolutegeometryand pages 1-4, bruyn2013absolutegeometryand pages 4-9, bruyn2016absolutegeometryand media 232f7bc7) |
| Manin–Marcolli homotopy-theoretic "geometries below \(\operatorname{Spec}\mathbb Z\)" | No explicit cohomology for the absolute surface; proposes homotopical/Grothendieck-ring enrichments | None | Not in the sense requested; no concrete cohomology groups supplied | No | No | A key missing ingredient is explicitly "cohomology with action of a Frobenius"; defining schemes below \(\operatorname{Spec}\mathbb Z\) requires strong categorical/Grothendieck-topology choices; partial Frobenius lifts may yield objects below \(\operatorname{Spec}\mathbb Z\) but not genuine \(\mathbb F_1\)-geometry | (manin2020homotopytypesand pages 1-4) |
| Archimedean cohomology (Consani–Marcolli) as analogue, not surface theory | Archimedean cohomology of arithmetic varieties with filtrations \(W_\bullet,L_\bullet,F^\bullet\) and monodromy operator \(N\) | Not an \(H^1\) for the absolute surface, but supplies a model where Lefschetz/monodromy-type operators act on a graded cohomology | Yes, with degree and mixed \(\mathbb Q\)-Hodge structures | Lefschetz/Picard–Lefschetz filtration appears, but no diagonal class on \(\operatorname{Spec}\mathbb Z \times_{\mathbb F_1} \operatorname{Spec}\mathbb Z\) | Mixed \(\mathbb Q\)-Hodge structure is explicit, but no Hodge–Riemann statement for the absolute surface | Relevant only as an analogue at arithmetic infinity; does not construct the desired absolute surface cohomology | (consani2006archimedeancohomologyrevisited pages 13-15) |


*Table: This table compares the main frameworks in the provided evidence that come closest to a cohomology theory for an absolute surface \(\operatorname{Spec}\mathbb Z \times_{\mathbb F_1} \operatorname{Spec}\mathbb Z\). It highlights that nontrivial cohomology exists in related settings, especially Connes–Consani’s \(H^1(\mathbb P^1_{\mathbb F_1},\Omega)\), but no source supplies the full requested package for the absolute surface itself.*

</explanation>
<discussion>

## Limitations of this survey
1. **Coverage limits:** This tool-driven survey was constrained to retrieved texts. It likely misses specialized papers explicitly attempting “absolute intersection theory” on \(\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z\) (if any exist) outside the queried set.
2. **Model mismatch:** Several major programs relevant to the *spirit* of the question (e.g., Deninger’s conjectural cohomology, noncommutative geometry approaches) intentionally do not model the object as a classical scheme fiber product. Thus, negative results about \(\times_{\mathbb F_1}\) as a scheme do not preclude alternative definitions of an “absolute surface” in different categories.
3. **Diagonal/Lefschetz ambiguity:** The requirement of a geometric diagonal class \([\Delta]\) presupposes a setting with products and correspondences. Many \(\mathbb F_1\)/absolute frameworks (topos-theoretic, homotopical, noncommutative, or \(\Gamma\)-ring based) may encode “Lefschetz operators” differently (e.g., via endomorphisms/flows rather than cup product with a cycle). The retrieved evidence did not expose such alternative identifications in a form that matches the objective’s criterion (3).

## Practical takeaway
At present, the literature most directly meeting your Criterion (1) and (2) is Connes–Consani’s explicit sheaf cohomology \(H^1(\mathbb P^1_{\mathbb F_1},\Omega)\) with spectral realization of zeros. This suggests a concrete “test bed” for any attempted extension toward an absolute surface. (connes2010schemesover𝔽1 pages 3-5)

</discussion>
<proposed-next-hypotheses>
1. A topos-level fiber product in Borger’s \(\Lambda\)-topos setting (constructed from the topos map \(v: \operatorname{Spec}\mathbb Z\to \operatorname{Spec}\mathbb F_1\) and its adjoints) admits a natural notion of “diagonal correspondence” whose induced endomorphism on a derived/global-sections functor yields an integer-graded Lefschetz operator compatible with Frobenius lifts.
2. The sheaf \(\Omega\) on \(\mathbb P^1_{\mathbb F_1}\) used by Connes–Consani can be extended (via a suitable site/topology such as Habiro-type refinements) to a sheaf on an \(\mathbb F_1\)-model of \(\overline{\operatorname{Spec}\mathbb Z}\) so that its \(H^1\) carries a natural bilinear pairing satisfying a positivity condition analogous to Hodge–Riemann.
</proposed-next-hypotheses>
</output>

References

1. (bruyn2013absolutegeometryand pages 1-4): Lieven Le Bruyn. Absolute geometry and the habiro topology. arXiv: Rings and Algebras, Apr 2016. URL: https://doi.org/10.48550/arxiv.1304.6532, doi:10.48550/arxiv.1304.6532. This article has 6 citations.

2. (bruyn2016absolutegeometryand media 232f7bc7): Lieven Le Bruyn. Absolute geometry and the habiro topology. arXiv: Rings and Algebras, Apr 2016. URL: https://doi.org/10.48550/arxiv.1304.6532, doi:10.48550/arxiv.1304.6532. This article has 6 citations.

3. (thas2016thecombinatorialmotivicnature pages 3-6): K Thas. The combinatorial-motivic nature of -schemes. Unknown journal, 2016.

4. (borger2009lambdaringsandthe pages 1-3): James Borger. Lambda-rings and the field with one element. Preprint, Jan 2009. URL: https://doi.org/10.48550/arxiv.0906.3146, doi:10.48550/arxiv.0906.3146. This article has 95 citations.

5. (connes2010schemesover𝔽1 pages 3-5): Alain Connes and Caterina Consani. Schemes over 𝔽1 and zeta functions. Compositio Mathematica, 146:1383-1415, Mar 2010. URL: https://doi.org/10.48550/arxiv.0903.2024, doi:10.48550/arxiv.0903.2024. This article has 172 citations and is from a domain leading peer-reviewed journal.

6. (connes2021segalsgammarings pages 23-25): Alain Connes and Caterina Consani. Segal's gamma rings and universal arithmetic. Jan 2021. URL: https://doi.org/10.48550/arxiv.2004.08879, doi:10.48550/arxiv.2004.08879. This article has 13 citations.

7. (borger2009lambdaringsandthe pages 3-5): James Borger. Lambda-rings and the field with one element. Preprint, Jan 2009. URL: https://doi.org/10.48550/arxiv.0906.3146, doi:10.48550/arxiv.0906.3146. This article has 95 citations.

8. (consani2006archimedeancohomologyrevisited pages 13-15): Caterina Consani and Matilde Marcolli. Archimedean cohomology revisited. arXiv: Algebraic Geometry, pages 109-140, Jul 2006. URL: https://doi.org/10.48550/arxiv.math/0407480, doi:10.48550/arxiv.math/0407480. This article has 17 citations.

9. (manin2020homotopytypesand pages 1-4): Yuri I. Manin and Matilde Marcolli. Homotopy types and geometries below spec z. Preprint, Jan 2020. URL: https://doi.org/10.48550/arxiv.1806.10801, doi:10.48550/arxiv.1806.10801. This article has 6 citations.

10. (connes2011characteristic1entropy pages 3-5): A Connes and C Consani. Characteristic 1, entropy and the absolute point. Unknown journal, 2011.

11. (connes2010schemesover𝔽1 pages 1-3): Alain Connes and Caterina Consani. Schemes over 𝔽1 and zeta functions. Compositio Mathematica, 146:1383-1415, Mar 2010. URL: https://doi.org/10.48550/arxiv.0903.2024, doi:10.48550/arxiv.0903.2024. This article has 172 citations and is from a domain leading peer-reviewed journal.

12. (connes2207hochschildhomologytrace pages 1-3): Alain Connes and Caterina Consani. Hochschild homology, trace map and $ζ$-cycles. Text, Jan 2207. URL: https://doi.org/10.48550/arxiv.2207.10419, doi:10.48550/arxiv.2207.10419. This article has 0 citations and is from a peer-reviewed journal.

13. (connes2021segalsgammarings pages 1-3): Alain Connes and Caterina Consani. Segal's gamma rings and universal arithmetic. Jan 2021. URL: https://doi.org/10.48550/arxiv.2004.08879, doi:10.48550/arxiv.2004.08879. This article has 13 citations.

14. (bruyn2013absolutegeometryand pages 4-9): Lieven Le Bruyn. Absolute geometry and the habiro topology. arXiv: Rings and Algebras, Apr 2016. URL: https://doi.org/10.48550/arxiv.1304.6532, doi:10.48550/arxiv.1304.6532. This article has 6 citations.