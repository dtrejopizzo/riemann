Question: 
Address the following research objective and research hypothesis:
<research-objective>Survey the literature on Arakelov theory, dynamical systems on `p`-adic spaces, and connections to noncommutative geometry to find an alternative formulation of arithmetic intersection theory.
            1. Review works at the intersection of Arakelov geometry and dynamical systems (e.g., by Deninger, Manin, Marcolli) that reinterpret arithmetic schemes in terms of flows or periodic orbits.
            2. Search for any re-formulation of the arithmetic intersection number or arithmetic degree map that is not defined as a sum over closed points of a scheme.
            3. Specifically, look for definitions involving "primitive cycles," "periodic orbits," or objects indexed by primes `p` rather than prime powers `p^m` with degree-based weighting.
            4. Document any theorem that relates such a dynamically-defined intersection number to the classical Gillet-Soulé pairing, or which shows that it reproduces the `Λ(n)` terms of the explicit formula.</research-objective>
<research-hypothesis>The standard arithmetic intersection pairing in Arakelov theory, which is defined over geometric points, can be re-expressed or generalized to an equivalent pairing defined on a basis of "arithmetic cycles" corresponding to primitive prime powers. This alternative formulation will naturally produce weights of `log(p)` for the `m`-th iteration of a primitive cycle `p`, aligning its structure with the von Mangoldt terms in the Weil explicit formula.</research-hypothesis>

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
The literature supports the existence of dynamical/noncommutative trace- or energy-based reformulations that naturally generate \(\log p\) weights via primitive periodic orbits, but it does not (in the retrieved sources) establish a general theorem that such a primitive-cycle pairing is equivalent to the classical Gillet–Soulé arithmetic intersection pairing.
</conclusion>
<explanation>
| Approach | Reference(s) | Objects replacing closed points | How `\log p` or orbit length appears | Intersection/degree definition style | Evidence for reproducing explicit-formula `\Lambda(n)` terms | Explicit relation to Gillet–Soulé pairing? |
|---|---|---|---|---|---|---|
| Deninger dynamical systems / foliations | Deninger 2002, 2005, 2006, 2007, 2023 (deninger2007dynamicalsystemsand pages 1-3, deninger2006adynamicalsystems pages 4-8, deninger2005arithmeticgeometryand pages 33-37, deninger2301primesknotsand pages 6-8, deninger2002numbertheoryand pages 1-5, deninger2005arithmeticgeometryand media 68e97427) | Primitive periodic orbits, closed `\mathbb R`-orbits, fixed points for archimedean places | `l(\gamma)=|o|\log p`, with contributions at multiples `k l(\gamma)` | Distributional Lefschetz trace formula on leafwise cohomology; degree-like information encoded by orbit length and flow cohomology class | Yes; Theorem 7.8 gives delta-masses at multiples of orbit lengths, and Deninger says the elliptic-curve case matches the RHS of the explicit formula for `\zeta_E(s)` (deninger2005arithmeticgeometryand pages 33-37, deninger2005arithmeticgeometryand media 68e97427) | No explicit equivalence theorem found; mainly analogy and conjectural program (deninger2005arithmeticgeometryand pages 33-37, deninger2002numbertheoryand pages 1-5) |
| Connes–Consani–Marcolli adèle class space / cyclic homology trace formula | Connes–Consani–Marcolli 2010; Connes 2011; Connes–Consani 2021, 2024; Khalkhali–Marcolli summary (connes2011thebcsystemand pages 1-3, khalkhali2008aninvitationto pages 95-98, connes2401knotsprimesand pages 1-4, connes2010theweilproof pages 33-36, connes2010theweilproof pages 26-30, connes2010theweilproof pages 1-3, connes2010theweilproof pages 10-13, connes2021weilpositivityand pages 1-3) | Periodic classical points, periodic scaling orbits, correspondences `Z(f)` | For `K=\mathbb Q`, periodic orbits have period `\log p`; degree of scaling correspondences is trace-like, e.g. `d(Z_g)=|g|` | Trace/Lefschetz pairing on cyclic homology; degree and positivity implemented by traces on correspondences | Yes at explicit-formula level; the Riemann–Weil explicit formula is realized as a Lefschetz/trace formula with geometric contributions from periodic orbits of length `\log p` (khalkhali2008aninvitationto pages 95-98, connes2401knotsprimesand pages 1-4, connes2010theweilproof pages 26-30, connes2021weilpositivityand pages 1-3) | Partial only; degree/intersection notions are reinterpreted by traces, but no direct equality with Gillet–Soulé was found (khalkhali2008aninvitationto pages 95-98, connes2010theweilproof pages 10-13) |
| Consani–Marcolli mapping torus `\infty`-adic Arakelov geometry | Consani–Marcolli 2002, 2004 (consani2004noncommutativegeometrydynamics pages 3-4, consani2004noncommutativegeometrydynamics pages 45-47, consani2002newperspectivesin pages 4-7, consani2004noncommutativegeometrydynamics pages 1-3, consani2004noncommutativegeometrydynamics pages 35-37, consani2002newperspectivesin pages 2-4) | Periodic words, primitive cycles in a subshift of finite type, mapping torus `S_T` | Period or word length enters multiplicatively in pairings; primitive cycles counted using Möbius-type formulas | Explicit homology–cohomology pairing on filtered dynamical (co)homology, e.g. `\langle [f],x\rangle = N f(\bar x)` | No direct `\Lambda(n)` theorem in the extracted passages; evidence is structural via periodic-cycle filtrations and zeta/torsion relations (consani2004noncommutativegeometrydynamics pages 45-47, consani2004noncommutativegeometrydynamics pages 35-37) | Partial; framed as intersection theory at infinity, but no explicit theorem relating it to Gillet–Soulé was found (consani2004noncommutativegeometrydynamics pages 3-4, consani2004noncommutativegeometrydynamics pages 45-47) |
| Arithmetic dynamics energy pairings (Arakelov–Zhang / adelic measures) | Fili 2017; Oberly 2023; related expositions (oberly2023aninnerproduct pages 1-10, oberly2023aninnerproduct pages 10-14, yap2025quantitativeaspectsof pages 33-37, fili2017ametricof pages 6-8, oberly2023aninnerproduct pages 113-118, fili2017ametricof pages 1-3) | Adelic measures and canonical invariant measures of rational maps | Not indexed by primitive orbits; logarithmic kernels appear in local-global energy integrals over places | Mutual-energy or inner-product formulation; Arakelov–Zhang pairing as norm or energy of measure differences | No; gives an alternative non-pointwise pairing or height formalism, but not a periodic-orbit `\Lambda(n)` formula in the retrieved evidence (oberly2023aninnerproduct pages 1-10, fili2017ametricof pages 6-8) | Partial; related to Arakelov–Zhang-type pairings, but no explicit equality to classical Gillet–Soulé was found in the extracted texts (oberly2023aninnerproduct pages 1-10, fili2017ametricof pages 6-8, hultberg2024localglobaland pages 116-119) |
| `p`-adic Arakelov (Besser) | Besser 2005; later `p`-adic adelic metrics context (besser2005padicarakelovtheory pages 17-19) | Green functions, admissible log functions, curvature data, determinant-of-cohomology objects | `\log_p` appears in `p`-adic log-functionals, not as primitive-orbit lengths | `p`-adic analogue of integral of log norm; intersection-style data via Green functions, curvature, and cohomological formulas | No evidence in the extracted text for reproducing `\Lambda(n)` by periodic orbits or primitive cycles (besser2005padicarakelovtheory pages 17-19) | Partial in spirit as a `p`-adic Arakelov intersection theory, but no dynamic reformulation or Gillet–Soulé equivalence theorem was found (besser2005padicarakelovtheory pages 17-19) |


*Table: This table compares the main approaches relevant to the hypothesis, showing what replaces closed points, where `log p` enters, and whether each framework gives a trace-, pairing-, or energy-based reformulation. It helps distinguish explicit-formula successes from cases where the link to classical Gillet–Soulé intersection theory remains only partial or conjectural.*

1. Evidence for “primitive cycles” and \(\log p\) weights (von Mangoldt structure)

Deninger’s program makes the prime/periodic-orbit dictionary explicit: closed points (or Frobenius orbits) correspond to closed \(\mathbb R\)-orbits \(\gamma\) of a flow on a foliated “arithmetic” space, and the length satisfies \(l(\gamma)=|o|\log p\), i.e. an iterate \(p^{|o|}\) corresponds to the \(|o|\)-fold traversal of a primitive orbit, with length scaling by \(|o|\) (deninger2006adynamicalsystems pages 4-8, deninger2007dynamicalsystemsand pages 1-3). The central analytic mechanism is a distributional Lefschetz trace formula (Theorem 7.8 in Deninger 2005), where the alternating trace distribution equals a delta mass at 0 plus a sum of delta masses supported at the multiples \(k\,l(\gamma)\) of orbit lengths, weighted by \(l(\gamma)\) and orbit-local factors (deninger2005arithmeticgeometryand pages 33-37, deninger2005arithmeticgeometryand media 68e97427). This is precisely the structural pattern behind von Mangoldt contributions: primitive objects (primes ↔ primitive orbits) contribute at all iterates (prime powers ↔ repeated traversals) with a \(\log p\)-type weight coming from the orbit length and the distribution placing mass at \(k\log p\) (deninger2005arithmeticgeometryand pages 33-37, deninger2005arithmeticgeometryand media 68e97427).

Moreover, Deninger states in the elliptic curve example that the right-hand side of this dynamical trace formula “equals the right hand side in the explicit formulas for \(\zeta_E(s)\),” i.e. the orbit sum reproduces the explicit-formula prime-power side when one identifies \(l=\log p\) (deninger2005arithmeticgeometryand pages 33-37). This addresses part (4) of the research objective: the dynamical formulation reproduces the \(\Lambda(n)\)-type structure (prime powers weighted by \(\log p\)) at the level of explicit formulas/trace identities (deninger2005arithmeticgeometryand pages 33-37, deninger2005arithmeticgeometryand media 68e97427).

Connes–Consani–Marcolli’s noncommutative approach realizes the Weil explicit formula as a Lefschetz/trace formula on a cohomology-like object defined via cyclic homology of the adèle class space (connes2010theweilproof pages 26-30, connes2010theweilproof pages 1-3). In this framework, “classical points” are periodic orbits under the scaling action; a summary explicitly notes that for \(K=\mathbb Q\) these are periodic orbits of period \(\log p\) (khalkhali2008aninvitationto pages 95-98), and Connes–Consani’s later work again emphasizes periodic orbits \(C_p\) with length \(\log p\) (connes2401knotsprimesand pages 1-4). Importantly for the research objective (2), degree-like functionals are defined trace-theoretically (e.g. degrees/codegrees of correspondences as values of trace/Fourier functionals), not by summing over closed points (khalkhali2008aninvitationto pages 95-98, connes2010theweilproof pages 33-36).

2. Alternative “intersection/degree” definitions not as sums over closed points

Several distinct alternatives appear:

(a) Trace distributions over periodic orbits (Deninger). Theorem 7.8 is explicitly a sum over closed orbits of a flow, not over scheme-theoretic closed points, and orbit-length weighting substitutes for degree (deninger2005arithmeticgeometryand media 68e97427). Deninger’s 2006–2007 texts further emphasize that orbit lengths represent \(\log\)-norms \(\log N\mathfrak p\) and that fixed points correspond to archimedean places (deninger2006adynamicalsystems pages 4-8, deninger2007dynamicalsystemsand pages 1-3).

(b) Noncommutative trace pairings (Connes–Consani–Marcolli). The explicit formula is expressed as a trace of operators \(\vartheta(f)\) acting on a cyclic-homology object \(H^1\), with positivity recast as positivity of a trace pairing; degrees of correspondences are implemented by trace/Fourier values (connes2010theweilproof pages 26-30, khalkhali2008aninvitationto pages 95-98).

(c) “Intersection theory at infinity” via mapping-torus dynamics (Consani–Marcolli). Consani–Marcolli define a homology–cohomology pairing on the mapping torus of a shift (subshift of finite type) where homology is generated by periodic sequences (closed orbits), and the period enters multiplicatively in the pairing (e.g. \(\langle[f],x\rangle = N\,f(\bar x)\)), with filtrations controlled by periodic/primitive cycles and Möbius-type counts (consani2004noncommutativegeometrydynamics pages 45-47, consani2002newperspectivesin pages 4-7). This gives an explicit “intersection-like” pairing indexed by periodic/primitive cycles, as requested in (3).

(d) Energy/inner-product formulations in arithmetic dynamics. In arithmetic dynamics, the Arakelov–Zhang pairing is expressed as a (global sum of local) mutual-energy / inner-product of adelic measures via double integrals against logarithmic kernels, avoiding a closed-point sum (fili2017ametricof pages 6-8, oberly2023aninnerproduct pages 1-10). Expositions make the local intersection pairing for metrized line bundles on \(\mathbb P^1\) into a double-integral (energy) pairing (Favre–Rivera-Letelier energy) (yap2025quantitativeaspectsof pages 33-37).

3. Relation to classical Gillet–Soulé intersection theory

On the “classical” side, the Gillet–Soulé arithmetic intersection product is formulated in terms of arithmetic Chow groups with Green currents and curvature forms, rather than explicitly as a raw sum over closed points; the arithmetic degree map is induced via pushforward in arithmetic Chow theory (hultberg2024localglobaland pages 116-119). This shows that even classical Arakelov theory already admits an analytic-current formulation.

However, the specific research-hypothesis claim is stronger: an equivalent pairing “on a basis of arithmetic cycles corresponding to primitive prime powers,” with \(\log p\) weights for iterates, and an equivalence theorem to Gillet–Soulé. In the retrieved sources, the strongest equivalence-type statements are:

• Deninger: equality of the dynamical trace formula’s orbit side with the explicit formula’s prime-power side for \(\zeta_E(s)\) in a special example (elliptic curve), providing the \(\Lambda(n)\) pattern via orbit iterates (deninger2005arithmeticgeometryand pages 33-37, deninger2005arithmeticgeometryand media 68e97427).

• Connes–Consani–Marcolli: explicit formula as a trace/Lefschetz formula, with degrees/codegrees of correspondences defined via trace-like functionals, and periodic orbits of period \(\log p\) providing the geometric side (khalkhali2008aninvitationto pages 95-98, connes2010theweilproof pages 26-30).

• Consani–Marcolli: a dynamical “intersection pairing at infinity” built from periodic/primitive cycles (consani2004noncommutativegeometrydynamics pages 45-47, consani2002newperspectivesin pages 4-7).

None of these, in the retrieved excerpts, provides a theorem identifying a dynamically-defined intersection pairing with the full Gillet–Soulé arithmetic intersection pairing on general arithmetic varieties. Thus, while the dynamical frameworks match the explicit-formula/von-Mangoldt weighting structure (supporting the heuristic part of the hypothesis), the “equivalent pairing” claim remains unproven here.

Statistical tests performed

No statistical tests are applicable. This is a theoretical mathematics literature survey; evidence consists of extracting definitions, formulas, and stated equivalences from primary sources.

Scientific implications

The literature strongly suggests that the von Mangoldt pattern (primitive object + iterates with \(\log p\) weight) is naturally encoded by periodic-orbit trace formulas (dynamical Lefschetz formulas) and by scaling-orbit trace formulas in noncommutative geometry (deninger2005arithmeticgeometryand media 68e97427, khalkhali2008aninvitationto pages 95-98). What remains missing is a fully developed, cycle-level arithmetic intersection theory over \(\mathrm{Spec}\,\mathbb Z\) whose pairing is defined purely in terms of primitive periodic orbits (primes) and proven to coincide with Gillet–Soulé in general.
</explanation>
<discussion>
Scope and limitations

1. Evidence skew toward “explicit formula” rather than “intersection pairing equality.” The retrieved sources contain explicit and even theorem-level links between periodic-orbit sums and explicit formulas (especially Deninger’s Theorem 7.8 and Connes–Consani–Marcolli’s Lefschetz-trace formulation), but they largely stop short of proving that a periodic-orbit/primitive-cycle pairing recovers Gillet–Soulé arithmetic intersections beyond specialized archimedean ‘fiber at infinity’ models or analogy (deninger2005arithmeticgeometryand pages 33-37, khalkhali2008aninvitationto pages 95-98).

2. Multiple notions of “intersection.” The phrase “intersection theory” appears in distinct senses: (i) Gillet–Soulé arithmetic Chow intersections with Green currents (hultberg2024localglobaland pages 116-119), (ii) dynamical trace distributions (deninger2005arithmeticgeometryand media 68e97427), (iii) mapping-torus homology–cohomology pairings at infinity (consani2004noncommutativegeometrydynamics pages 45-47), and (iv) energy pairings of adelic measures in arithmetic dynamics (fili2017ametricof pages 6-8). These are conceptually aligned (pairings + positivity + trace formulas) but not formally unified in the retrieved evidence.

3. Primitive vs prime-power indexing is present but not yet packaged as an Arakelov-style Chow theory. Both Deninger and Connes-style approaches treat primes as primitive periodic orbits with period/length \(\log p\) and generate prime powers by iteration (delta masses at \(k\log p\)), exactly as demanded by the hypothesis’s “primitive cycle + iterates” mechanism (deninger2005arithmeticgeometryand media 68e97427, khalkhali2008aninvitationto pages 95-98). Yet an “arithmetic cycle group” with basis given by primitive orbits and an induced intersection product equivalent to Gillet–Soulé is not exhibited.
</discussion>
<proposed-next-hypotheses>
1. (Testable) For regular arithmetic surfaces \(\mathcal X/\mathrm{Spec}\,\mathbb Z\), there exists a functorial map from Gillet–Soulé \(\widehat{\mathrm{CH}}^1(\mathcal X)\) (or a suitable quotient) to a dynamical homology group generated by primitive periodic orbits (primes), such that the arithmetic degree of \(\widehat{c}_1(\overline L)^2\) is the evaluation of a Deninger/Connes-type trace distribution on a canonical test function; verifying this would require matching local factors and archimedean Green terms.

2. (Testable) In Consani–Marcolli’s mapping-torus model of the fiber at infinity, the dynamical pairing on filtered (co)homology (built from primitive cycles and Möbius counts) equals the archimedean contribution of the Gillet–Soulé intersection pairing for Arakelov divisors on the corresponding arithmetic surface, after identifying the filtration level with the length/period (and hence \(\log p\)-type weights) (consani2004noncommutativegeometrydynamics pages 45-47, consani2002newperspectivesin pages 4-7).
</proposed-next-hypotheses>
</output>

References

1. (deninger2007dynamicalsystemsand pages 1-3): C. Deninger. Dynamical systems and arithmetic geometry. ArXiv, 2007:12-23, 2007. URL: https://doi.org/10.11429/emath1996.2007.spring-meeting\_12, doi:10.11429/emath1996.2007.spring-meeting\_12. This article has 0 citations.

2. (deninger2006adynamicalsystems pages 4-8): Christopher Deninger. A dynamical systems analogue of lichtenbaum's conjectures on special values of hasse-weil zeta functions. Preprint, Jan 2006. URL: https://doi.org/10.48550/arxiv.math/0605724, doi:10.48550/arxiv.math/0605724. This article has 19 citations.

3. (deninger2005arithmeticgeometryand pages 33-37): C. Deninger. Arithmetic geometry and analysis on foliated spaces. Preprint, Jan 2005. URL: https://doi.org/10.48550/arxiv.math/0505354, doi:10.48550/arxiv.math/0505354. This article has 14 citations.

4. (deninger2301primesknotsand pages 6-8): Christopher Deninger. Primes, knots and periodic orbits. Preprint, Jan 2301. URL: https://doi.org/10.48550/arxiv.2301.11643, doi:10.48550/arxiv.2301.11643. This article has 2 citations.

5. (deninger2002numbertheoryand pages 1-5): Christopher Deninger. Number theory and dynamical systems on foliated spaces. Text, Jan 2002. URL: https://doi.org/10.48550/arxiv.math/0204110, doi:10.48550/arxiv.math/0204110. This article has 66 citations and is from a peer-reviewed journal.

6. (deninger2005arithmeticgeometryand media 68e97427): C. Deninger. Arithmetic geometry and analysis on foliated spaces. Preprint, Jan 2005. URL: https://doi.org/10.48550/arxiv.math/0505354, doi:10.48550/arxiv.math/0505354. This article has 14 citations.

7. (connes2011thebcsystemand pages 1-3): Alain Connes. The bc-system and l-functions. Japanese Journal of Mathematics, 6:1-44, Sep 2011. URL: https://doi.org/10.1007/s11537-011-1035-0, doi:10.1007/s11537-011-1035-0. This article has 1 citations and is from a peer-reviewed journal.

8. (khalkhali2008aninvitationto pages 95-98): Masoud Khalkhali and Matilde Marcolli. An invitation to noncommutative geometry. ArXiv, Feb 2008. URL: https://doi.org/10.1142/6422, doi:10.1142/6422. This article has 131 citations.

9. (connes2401knotsprimesand pages 1-4): Alain Connes and Caterina Consani. Knots, primes and the adele class space. Preprint, Jan 2401. URL: https://doi.org/10.48550/arxiv.2401.08401, doi:10.48550/arxiv.2401.08401. This article has 1 citations.

10. (connes2010theweilproof pages 33-36): Alain Connes, Caterina Consani, and Matilde Marcolli. The Weil Proof and the Geometry of the Adelès Class Space, pages 339-405. Birkhäuser Boston, Jan 2010. URL: https://doi.org/10.1007/978-0-8176-4745-2\_8, doi:10.1007/978-0-8176-4745-2\_8. This article has 45 citations.

11. (connes2010theweilproof pages 26-30): Alain Connes, Caterina Consani, and Matilde Marcolli. The Weil Proof and the Geometry of the Adelès Class Space, pages 339-405. Birkhäuser Boston, Jan 2010. URL: https://doi.org/10.1007/978-0-8176-4745-2\_8, doi:10.1007/978-0-8176-4745-2\_8. This article has 45 citations.

12. (connes2010theweilproof pages 1-3): Alain Connes, Caterina Consani, and Matilde Marcolli. The Weil Proof and the Geometry of the Adelès Class Space, pages 339-405. Birkhäuser Boston, Jan 2010. URL: https://doi.org/10.1007/978-0-8176-4745-2\_8, doi:10.1007/978-0-8176-4745-2\_8. This article has 45 citations.

13. (connes2010theweilproof pages 10-13): Alain Connes, Caterina Consani, and Matilde Marcolli. The Weil Proof and the Geometry of the Adelès Class Space, pages 339-405. Birkhäuser Boston, Jan 2010. URL: https://doi.org/10.1007/978-0-8176-4745-2\_8, doi:10.1007/978-0-8176-4745-2\_8. This article has 45 citations.

14. (connes2021weilpositivityand pages 1-3): Alain Connes and Caterina Consani. Weil positivity and trace formula the archimedean place. Selecta Mathematica, Jul 2021. URL: https://doi.org/10.1007/s00029-021-00689-4, doi:10.1007/s00029-021-00689-4. This article has 22 citations.

15. (consani2004noncommutativegeometrydynamics pages 3-4): Caterina Consani and Matilde Marcolli. Noncommutative geometry, dynamics, and ∞-adic arakelov geometry. Aug 2004. URL: https://doi.org/10.1007/s00029-004-0369-3, doi:10.1007/s00029-004-0369-3. This article has 65 citations.

16. (consani2004noncommutativegeometrydynamics pages 45-47): Caterina Consani and Matilde Marcolli. Noncommutative geometry, dynamics, and ∞-adic arakelov geometry. Aug 2004. URL: https://doi.org/10.1007/s00029-004-0369-3, doi:10.1007/s00029-004-0369-3. This article has 65 citations.

17. (consani2002newperspectivesin pages 4-7): Caterina Consani and Matilde Marcolli. New perspectives in arakelov geometry. Preprint, Jan 2002. URL: https://doi.org/10.48550/arxiv.math/0210357, doi:10.48550/arxiv.math/0210357. This article has 17 citations.

18. (consani2004noncommutativegeometrydynamics pages 1-3): Caterina Consani and Matilde Marcolli. Noncommutative geometry, dynamics, and ∞-adic arakelov geometry. Aug 2004. URL: https://doi.org/10.1007/s00029-004-0369-3, doi:10.1007/s00029-004-0369-3. This article has 65 citations.

19. (consani2004noncommutativegeometrydynamics pages 35-37): Caterina Consani and Matilde Marcolli. Noncommutative geometry, dynamics, and ∞-adic arakelov geometry. Aug 2004. URL: https://doi.org/10.1007/s00029-004-0369-3, doi:10.1007/s00029-004-0369-3. This article has 65 citations.

20. (consani2002newperspectivesin pages 2-4): Caterina Consani and Matilde Marcolli. New perspectives in arakelov geometry. Preprint, Jan 2002. URL: https://doi.org/10.48550/arxiv.math/0210357, doi:10.48550/arxiv.math/0210357. This article has 17 citations.

21. (oberly2023aninnerproduct pages 1-10): PJ Oberly. An inner product on adelic measures. Unknown journal, 2023.

22. (oberly2023aninnerproduct pages 10-14): PJ Oberly. An inner product on adelic measures. Unknown journal, 2023.

23. (yap2025quantitativeaspectsof pages 33-37): JW Yap. Quantitative aspects of arakelov theory in arithmetic dynamics. Unknown journal, 2025.

24. (fili2017ametricof pages 6-8): Paul Fili. A metric of mutual energy and unlikely intersections for dynamical systems. Preprint, Jan 2017. URL: https://doi.org/10.48550/arxiv.1708.08403, doi:10.48550/arxiv.1708.08403. This article has 18 citations.

25. (oberly2023aninnerproduct pages 113-118): PJ Oberly. An inner product on adelic measures. Unknown journal, 2023.

26. (fili2017ametricof pages 1-3): Paul Fili. A metric of mutual energy and unlikely intersections for dynamical systems. Preprint, Jan 2017. URL: https://doi.org/10.48550/arxiv.1708.08403, doi:10.48550/arxiv.1708.08403. This article has 18 citations.

27. (hultberg2024localglobaland pages 116-119): N Hultberg. Local, global, and relative problems in arithmetic intersection theory. Unknown journal, 2024.

28. (besser2005padicarakelovtheory pages 17-19): Amnon Besser. P-adic arakelov theory. Apr 2005. URL: https://doi.org/10.1016/j.jnt.2004.11.010, doi:10.1016/j.jnt.2004.11.010. This article has 31 citations and is from a domain leading peer-reviewed journal.