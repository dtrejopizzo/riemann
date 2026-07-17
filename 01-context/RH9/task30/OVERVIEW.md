Question: 
Address the following research objective and research hypothesis:
<research-objective>Survey the advanced literature on integral prismatization (`Σ_Z`), syntomic cohomology, and topological cyclic/Hochschild homology (TC/THH) over `Spec ℤ`. The search should focus on:
                        1. Functors or objects that take a family of p-adic structures (like Frobenius actions) and produce a single "global" object.
                        2. The definition of the "cyclotomic trace" map from algebraic K-theory to TC, and how it interacts with Frobenius and Adams operations at different primes.
                        3. Any discussion of "interpolating" Frobenius actions or constructing an `ℝ`-action from a `ℤ_p`-action in these contexts.
                        The goal is to identify a formal mechanism for assembling the local `φ_p` into a single, globally defined endomorphism.</research-objective>
<research-hypothesis>The stack `Σ_Z` or a related object in syntomic/topological cyclic homology admits a "universal" endomorphism or is defined by a universal property that takes the collection of all p-adic Frobenius endomorphisms `{φ_p}` as input data, thereby providing a canonical candidate for a global operator.</research-hypothesis>

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
The retrieved literature does not support the strong form of the hypothesis that \(\Sigma_{\mathbf Z}\) (or TC/THH/syntomic avatars) carries a canonical single endomorphism uniquely determined by the local Frobenii \(\{\varphi_p\}\); instead, the formal “globalization” mechanism that is clearly documented is to package \(\{\varphi_p\}\) as a coherent \(\mathbf N_{>0}\)-action (cyclotomic/\(\lambda\)-structure), yielding a universal global object but not a single globally defined Frobenius operator. 
</conclusion>
<explanation>
| Context | Mechanism | Input data | Output/global object | Type of 'global operator' produced | Key limitation / notes |
|---|---|---|---|---|---|
| `\Sigma_{\mathbf Z}` / integral prismatization | Global base stack defined as `\Sigma_{\mathbf Z}=W^{dist}/W^\times`, with `X\mapsto X_{\Delta,\mathbf Z}`; `\delta`-schemes with commuting Frobenius lifts map canonically into the integral prismatization | Family of commuting lifts `\{\varphi_p\}` packaged as a `\delta`-structure | Stack `\Sigma_{\mathbf Z}` and prismatized stack `X_{\Delta,\mathbf Z}` | Not a single endomorphism in the cited text; rather a universal stack receiving compatible prime-wise Frobenius data | Base-changes recover `\Sigma_p` over `\mathbf Z_p` and de Rham over `\mathbf Q`; retrieved evidence does **not** exhibit one canonical global endomorphism on `\Sigma_{\mathbf Z}` itself (gurney2301prismatizationover$\mathbf{z}$ pages 1-4, gurney2301prismatizationover$\mathbf{z}$ pages 24-28, gurney2301prismatizationover$\mathbf{z}$ pages 18-21) |
| TC/THH, Borel cyclotomic spectra | Cyclotomic spectrum = `S^1`-spectrum `X` with maps `\varphi_p: X\to X^{tC_p}` for every prime; `TC` defined by equalizer of `can` and Frobenius maps | Family `\{\varphi_p\}`, one for each prime | Cyclotomic spectrum and `TC(X)` | Family of compatible Frobenius maps; equalizer object rather than one global endomorphism | The structure is explicitly all-primes, but the operator is a coherent family `\varphi_p`, not a single assembled map `X\to X` in general (hesselholt2020topologicalcyclichomology pages 1-4, hesselholt2020topologicalcyclichomology pages 4-7, hesselholt2020topologicalcyclichomology media 19adc3d0) |
| Genuine cyclotomic spectra | Genuine cyclotomic spectra described as homotopy fixed points `(\mathrm{Sp}^{S^1})^{h\mathbf N_{>0}}`, with `\mathbf N_{>0}` acting through geometric fixed-point functors | Prime-wise Frobenius data, coherently extended to all `n\in \mathbf N_{>0}` | Category/object of genuine cyclotomic spectra | Monoid action of `\mathbf N_{>0}` | This is the clearest formal “globalization” in TC-land: the local `p`-Frobenii become one coherent monoid action, but still not a single canonical endomorphism (quigley2112ontheequivalence pages 2-4) |
| `\lambda`-rings / animated `\lambda`-rings | Animated `\lambda`-ring given by an action `B\mathbf N_{>0}\to \mathrm{CAlg}` with coherences; Joyal–Rezk/Wilkerson identify this with pairwise commuting `p`-Frobenius lifts (torsion-free case) | Family of commuting lifts `\{\varphi_p\}` for all primes | Animated `\lambda`-ring / global `\lambda`-structure | Monoid action of `\mathbf N_{>0}`; equivalent to all-primes compatible Frobenius package | Strong universal/categorical packaging of all primes; this is a compelling candidate formalism for “assembling” `\{\varphi_p\}`, but it belongs to `\lambda`/`\delta` algebra rather than directly to `TC` or `\Sigma_{\mathbf Z}` (hubner2404animated$λ$ringsand pages 3-6, hubner2404animated$λ$ringsand pages 28-32, hubner2404animated$λ$ringsand pages 1-3) |
| `\delta`-rings / animated `\delta`-rings | A `\delta`-structure encodes a single `p`-Frobenius lift via `\varphi(x)=x^p+p\delta(x)`; free and pullback/equalizer constructions provide universal objects | Single prime `p` and one lift `\varphi_p` | `p`-typical `\delta`-ring | Single endomorphism at one prime | Excellent local model, but intrinsically `p`-typical; all-primes globalization requires passage to `\lambda`-structures or additional gluing (hubner2404animated$λ$ringsand pages 12-15, hubner2404animated$λ$ringsand pages 6-8, hubner2404animated$λ$ringsand pages 18-21) |
| Jet/prolongation and Witt constructions | Canonical prolongation sequence `J^*X` with universal property; maps from any prolongation sequence into `J^*X` correspond to maps into `X`, packaging compatible Frobenius lifts levelwise | Typically one prime at a time through Witt vectors / levelwise Frobenius | Prolongation sequence / jet tower | Universal compatible tower of Frobenius lifts | Gives a universal object for compatible Frobenius-lift data, but the retrieved evidence is levelwise / `p`-typical rather than a direct all-primes single operator (pandit2302deltacharactersand pages 9-13) |
| Tate-valued Frobenius in higher algebra | For each prime, natural Tate diagonal and Tate-valued Frobenius `R\to R^{tC_p}` | Single prime `p` | Prime-specific Frobenius map in THH/higher algebra | Single prime-indexed map | Nikolaus explicitly notes the construction is prime-by-prime and in general does not yield an endomorphism `R\to R`; no assembly into one global operator is provided here (nikolaus2023frobeniushomomorphismsin pages 7-10) |


*Table: This table compares the main formal devices found in the literature for packaging prime-wise Frobenius data across integral prismatization, cyclotomic spectra, and λ/δ-structures. It is useful for evaluating whether the available theories produce a single global endomorphism or only a coherent family/monoid action.*

1) Integral prismatization \(\Sigma_{\mathbf Z}\) and its global nature over \(\mathrm{Spec}\,\mathbf Z\).  Gurney constructs an “integral prismatization” functor \(X\mapsto X_{\Delta,\mathbf Z}\) landing over a base stack \(\Sigma_{\mathbf Z}\), and defines \(\Sigma_{\mathbf Z}\) explicitly as the quotient \(\Sigma_{\mathbf Z}:=W^{\mathrm{dist}}/W^\times\) (with \(W\) the big Witt vectors and \(W^{\mathrm{dist}}\subset W\) a “distinguished” locus) (gurney2301prismatizationover$\mathbf{z}$ pages 18-21). The associated integral prismatic cohomology is defined by \(H_{\Delta,\mathbf Z}(X):=Rf_{\Delta,\mathbf Z,*}\,\mathcal O_{X_{\Delta,\mathbf Z}}\in D(\Sigma_{\mathbf Z})\) (gurney2301prismatizationover$\mathbf{z}$ pages 1-4). Crucially for “globalizing across primes”, \(\Sigma_{\mathbf Z}\) and \(X_{\Delta,\mathbf Z}\) are characterized by base-change compatibilities: after \(p\)-adic completion one recovers the usual \(p\)-adic prismatization \(\Sigma_p\) / \(X_{\Delta,p}\), and after rationalization one recovers the filtered de Rham stack (gurney2301prismatizationover$\mathbf{z}$ pages 1-4, gurney2301prismatizationover$\mathbf{z}$ pages 18-21). Thus \(\Sigma_{\mathbf Z}\) is a single global object whose fibers encode the local \(p\)-adic prismatic geometries, but in the extracted text there is no exhibited *single* endomorphism \(\Sigma_{\mathbf Z}\to\Sigma_{\mathbf Z}\) that would be determined by (or assemble) the \(\varphi_p\).

Gurney does, however, record a universal way that “all-primes Frobenius lifts” enter the theory: a \(\delta\)-structure (commuting Frobenius lifts \((\varphi_p)_p\)) on a smooth scheme yields a canonical map into the prismatization framework, e.g. giving a faithfully flat map \(X\times \Sigma_{\mathbf Z}\to X_{\Delta,\mathbf Z}\) (gurney2301prismatizationover$\mathbf{z}$ pages 24-28). This is evidence for a *universal receptacle* for the *data* \(\{\varphi_p\}\), but it is not evidence for a uniquely determined global endomorphism produced from that data.

2) Cyclotomic trace \(K\to TC\), Frobenius structure, and Adams operations.  In the prime-by-prime classical construction, TC at a fixed prime \(p\) is built from the tower of fixed points \(\mathrm{THH}(A)^{C_{p^n}}\) with restriction maps \(R\) and Frobenius maps \(F\) (ausoni2002algebraicktheoryof pages 11-15, geisser2003topologicalcyclichomology pages 1-4). Ausoni–Rognes describe the cyclotomic trace as the composite induced from compatible lifts \(\mathrm{tr}_n:K(A)\to \mathrm{THH}(A)^{C_{p^n}}\) (commuting with Frobenius and homotopy-commuting with restriction), yielding \(K(A)\to TF(A;p)\to TC(A;p)\) (ausoni2002algebraicktheoryof pages 11-15). In Nikolaus–Scholze’s formulation (as summarized by Hesselholt–Nikolaus), a cyclotomic spectrum is *by definition* a spectrum with \(S^1\)-action equipped with maps \(\varphi_p:X\to X^{tC_p}\) for every prime \(p\), and TC is obtained as an equalizer of the canonical map \(\mathrm{can}:\mathrm{TC}^-\to \mathrm{TP}\) and Frobenius-type maps (after suitable completion) (hesselholt2020topologicalcyclichomology pages 4-7). The retrieved figures/diagrams in the survey explicitly depict the “equalizer of \(\mathrm{can}\) and \(\varphi\)” definition and the cyclotomic data with \(\varphi_p\) for each prime (hesselholt2020topologicalcyclichomology media 19adc3d0, hesselholt2020topologicalcyclichomology media d765bd60). This is a precise formal mechanism in TC/THH that takes a family \(\{\varphi_p\}\) as input.

Interactions with Adams operations appear in two ways in the retrieved evidence. (i) In the perfectoid computations summarized by Hesselholt–Nikolaus, there is an induced Adams operation \(\varphi\) on \(A\) described as the composite involving \(\mathrm{can}^{-1}\) and Frobenius on degree 0 (hesselholt2020topologicalcyclichomology pages 1-4, hesselholt2020topologicalcyclichomology pages 4-7). (ii) Geisser–Hesselholt use Adams operations on descent spectral sequences and weight arguments to constrain TC/K-theory comparisons, and describe Frobenius scaling behaviors (e.g. \(\varphi=p^iF\) on de Rham–Witt identifications) (geisser2003topologicalcyclichomology pages 35-38, geisser2003topologicalcyclichomology pages 16-19). These results indicate that Adams operations and Frobenius maps coexist and interact, but the evidence does not provide an “all primes simultaneously” compatibility statement of Adams operations across primes that produces a single endomorphism; rather, operations are organized either at a fixed \(p\) (classical TC\((\cdot;p)\)) or as a family \(\{\varphi_p\}\) (cyclotomic spectra).

3) Formal “assembly” mechanisms for \(\{\varphi_p\}\): monoid actions and \(\lambda\)-structures.  The clearest documented global assembly is categorical rather than as one endomorphism. Quigley–Shah explain that genuine cyclotomic spectra can be encoded as homotopy fixed points \((\mathrm{Sp}^{S^1})^{h\mathbf N_{>0}}\), i.e. an \(\mathbf N_{>0}\)-action (multiplicative monoid) packages the prime-wise cyclotomic Frobenii into one coherent global structure (quigley2112ontheequivalence pages 2-4). On the algebraic side, Hübner’s “animated \(\lambda\)-rings” present a parallel mechanism: a \(\lambda\)-structure is equivalent (in torsion-free cases) to giving pairwise commuting Frobenius lifts at all primes, and in the animated setting this is packaged as an action \(B\mathbf N_{>0}\to\mathrm{CAlg}\) with coherences and compatibility with derived mod-\(p\) Frobenius (hubner2404animated$λ$ringsand pages 3-6, hubner2404animated$λ$ringsand pages 1-3). The Joyal–Rezk statement explicitly identifies \(\lambda\)-structures with a compatible family of \(p\)-typical \(\delta_p\)-structures satisfying commutation relations across distinct primes (hubner2404animated$λ$ringsand pages 1-3). These results *do* realize a universal mechanism that “takes \(\{\varphi_p\}\) as input data and outputs a global object”, but the output is naturally a monoid action / structured object (cyclotomic or \(\lambda\)-ring), not a single universally preferred endomorphism.

4) Interpolating \(\mathbf Z_p\)-actions to \(\mathbf R\)-actions.  Within the retrieved TC/THH/\(\Sigma_{\mathbf Z}\) sources, no explicit construction of an \(\mathbf R\)-action canonically induced from a \(\mathbf Z_p\)-action was found. The closest “interpolation heuristic” in the retrieved corpus is external to TC/\(\Sigma_{\mathbf Z}\): Connes–Consani describe a global scaling action of \(\mathbf R_+^\times\) in an adelic/class-field-theory geometry and interpret it as analogous to Frobenius actions at primes (connes2501knotsprimesand pages 3-7), but this is not tied to cyclotomic trace or integral prismatization in the provided evidence.

Methodological note (re “statistical tests”).  This work is a structured literature scan using targeted retrieval and evidence extraction, not an empirical study, so no statistical tests were applicable or performed. The “hypothesis test” is therefore qualitative: we treat the hypothesis as supported only if the literature explicitly states a universal property producing a *single* global endomorphism from \(\{\varphi_p\}\); the retrieved evidence instead supports universal *packaging* of \(\{\varphi_p\}\) as a coherent monoid action (quigley2112ontheequivalence pages 2-4, hubner2404animated$λ$ringsand pages 3-6, hubner2404animated$λ$ringsand pages 1-3), and shows \(\Sigma_{\mathbf Z}\) as a global base that glues the prime-wise geometries without exhibiting a canonical global Frobenius operator (gurney2301prismatizationover$\mathbf{z}$ pages 1-4, gurney2301prismatizationover$\mathbf{z}$ pages 18-21).
</explanation>
<discussion>
Strengths and what is established.  The evidence strongly supports that modern TC/THH and \(\lambda\)/\(\delta\)-algebra formalisms already provide precise “all-primes at once” input mechanisms: cyclotomic spectra require maps \(\varphi_p\) for each prime (hesselholt2020topologicalcyclichomology pages 4-7), and genuine cyclotomic spectra promote this to an \(\mathbf N_{>0}\)-action (quigley2112ontheequivalence pages 2-4). Likewise, animated \(\lambda\)-structures package commuting Frobenius lifts across all primes as a monoid action with coherence, and are equivalent to compatible \(\delta_p\) data (hubner2404animated$λ$ringsand pages 1-3). Separately, \(\Sigma_{\mathbf Z}\) is shown to be a single global stack over \(\mathrm{Spec}\,\mathbf Z\) that simultaneously controls the \(p\)-adic prismatic fibers and the rational de Rham fiber (gurney2301prismatizationover$\mathbf{z}$ pages 1-4, gurney2301prismatizationover$\mathbf{z}$ pages 18-21).

What is *not* established (limitation relative to the hypothesis).  None of the extracted \(\Sigma_{\mathbf Z}\) evidence states a universal property that *outputs a canonical single endomorphism* from the collection \(\{\varphi_p\}\), and the TC/THH evidence suggests that even in TC-land, the natural structure is a family \(\{\varphi_p\}\) (or a monoid action), not an induced endomorphism \(X\to X\) in general (nikolaus2023frobeniushomomorphismsin pages 7-10, quigley2112ontheequivalence pages 2-4). Thus, the strongest reading of the hypothesis (a canonical global Frobenius endomorphism assembling the \(\varphi_p\) into one map) is not supported by the retrieved evidence.

Scope limitations.  (i) The scan did not retrieve dedicated syntomic cohomology sources bridging to \(\Sigma_{\mathbf Z}\) and TC beyond the prismatic-to-\(p\)-adic and de Rham compatibilities stated in Gurney and the TC-to-de Rham–Witt comparisons in Geisser–Hesselholt (gurney2301prismatizationover$\mathbf{z}$ pages 1-4, geisser2003topologicalcyclichomology pages 16-19). (ii) Some central references may be missing from the retrieved set (e.g. original Nikolaus–Scholze paper, Bhatt–Scholze prismatic foundations, and recent “prismatic/TC/syntomic” comparison papers), so a stronger conclusion may be possible with expanded retrieval.
</discussion>
<proposed-next-hypotheses>
1) The integral prismatization base \(\Sigma_{\mathbf Z}\) admits a canonical \(\mathbf N_{>0}\)-monoid action (extending the prime-wise Frobenius maps on its \(p\)-adic fibers \(\Sigma_p\)) such that for any cyclotomic spectrum arising from \(\mathrm{THH}(R)\), the cyclotomic \(\{\varphi_p\}\) correspond under a comparison functor to pullback along this \(\mathbf N_{>0}\)-action. 

2) There exists a functor from (a suitable derived enhancement of) \(\Sigma_{\mathbf Z}\)-sheaves or \(\Sigma_{\mathbf Z}\)-cohomology theories to animated \(\lambda\)-rings such that the “global Frobenius package” on integral prismatic cohomology \(H_{\Delta,\mathbf Z}(X)\) is representable by the universal \(\lambda\)-structure (i.e. a canonical \(\mathbf N_{>0}\)-action), and its restriction to each \(p\)-adic fiber recovers the usual \(p\)-typical Frobenius/Nygaard structure.
</proposed-next-hypotheses>
</output>

References

1. (gurney2301prismatizationover$\mathbf{z}$ pages 1-4): Unknown author(s). Unknown title. Unknown journal, Unknown year. This article has 0 citations.

2. (gurney2301prismatizationover$\mathbf{z}$ pages 24-28): Unknown author(s). Unknown title. Unknown journal, Unknown year. This article has 0 citations.

3. (gurney2301prismatizationover$\mathbf{z}$ pages 18-21): Unknown author(s). Unknown title. Unknown journal, Unknown year. This article has 0 citations.

4. (hesselholt2020topologicalcyclichomology pages 1-4): Lars Hesselholt and Thomas Nikolaus. Topological cyclic homology. Handbook of Homotopy Theory, pages 619-656, Jan 2020. URL: https://doi.org/10.1201/9781351251624-15, doi:10.1201/9781351251624-15. This article has 58 citations.

5. (hesselholt2020topologicalcyclichomology pages 4-7): Lars Hesselholt and Thomas Nikolaus. Topological cyclic homology. Handbook of Homotopy Theory, pages 619-656, Jan 2020. URL: https://doi.org/10.1201/9781351251624-15, doi:10.1201/9781351251624-15. This article has 58 citations.

6. (hesselholt2020topologicalcyclichomology media 19adc3d0): Lars Hesselholt and Thomas Nikolaus. Topological cyclic homology. Handbook of Homotopy Theory, pages 619-656, Jan 2020. URL: https://doi.org/10.1201/9781351251624-15, doi:10.1201/9781351251624-15. This article has 58 citations.

7. (quigley2112ontheequivalence pages 2-4): J. D. Quigley and Jay Shah. On the equivalence of two theories of real cyclotomic spectra. Preprint, Jan 2112. URL: https://doi.org/10.48550/arxiv.2112.07462, doi:10.48550/arxiv.2112.07462. This article has 11 citations.

8. (hubner2404animated$λ$ringsand pages 3-6): Edith Hübner. Animated $λ$-rings and frobenius lifts. Preprint, Jan 2404. URL: https://doi.org/10.48550/arxiv.2404.15040, doi:10.48550/arxiv.2404.15040. This article has 1 citations.

9. (hubner2404animated$λ$ringsand pages 28-32): Edith Hübner. Animated $λ$-rings and frobenius lifts. Preprint, Jan 2404. URL: https://doi.org/10.48550/arxiv.2404.15040, doi:10.48550/arxiv.2404.15040. This article has 1 citations.

10. (hubner2404animated$λ$ringsand pages 1-3): Edith Hübner. Animated $λ$-rings and frobenius lifts. Preprint, Jan 2404. URL: https://doi.org/10.48550/arxiv.2404.15040, doi:10.48550/arxiv.2404.15040. This article has 1 citations.

11. (hubner2404animated$λ$ringsand pages 12-15): Edith Hübner. Animated $λ$-rings and frobenius lifts. Preprint, Jan 2404. URL: https://doi.org/10.48550/arxiv.2404.15040, doi:10.48550/arxiv.2404.15040. This article has 1 citations.

12. (hubner2404animated$λ$ringsand pages 6-8): Edith Hübner. Animated $λ$-rings and frobenius lifts. Preprint, Jan 2404. URL: https://doi.org/10.48550/arxiv.2404.15040, doi:10.48550/arxiv.2404.15040. This article has 1 citations.

13. (hubner2404animated$λ$ringsand pages 18-21): Edith Hübner. Animated $λ$-rings and frobenius lifts. Preprint, Jan 2404. URL: https://doi.org/10.48550/arxiv.2404.15040, doi:10.48550/arxiv.2404.15040. This article has 1 citations.

14. (pandit2302deltacharactersand pages 9-13): Sudip Pandit and Arnab Saha. Delta characters and crystalline cohomology. Preprint, Jan 2302. URL: https://doi.org/10.48550/arxiv.2302.08792, doi:10.48550/arxiv.2302.08792. This article has 7 citations.

15. (nikolaus2023frobeniushomomorphismsin pages 7-10): Thomas Nikolaus. Frobenius homomorphisms in higher algebra. International Congress of Mathematicians, pages 2826-2854, Dec 2023. URL: https://doi.org/10.4171/icm2022/159, doi:10.4171/icm2022/159. This article has 1 citations.

16. (ausoni2002algebraicktheoryof pages 11-15): Christian Ausoni and John Rognes. Algebraic k-theory of topological k-theory. Acta Mathematica, 188:1-39, Mar 2002. URL: https://doi.org/10.1007/bf02392794, doi:10.1007/bf02392794. This article has 150 citations and is from a highest quality peer-reviewed journal.

17. (geisser2003topologicalcyclichomology pages 1-4): Thomas H. Geisser and L. Hesselholt. Topological cyclic homology of schemes. ArXiv, pages 41-87, Jan 2003. URL: https://doi.org/10.1090/pspum/067/1743237, doi:10.1090/pspum/067/1743237. This article has 118 citations.

18. (hesselholt2020topologicalcyclichomology media d765bd60): Lars Hesselholt and Thomas Nikolaus. Topological cyclic homology. Handbook of Homotopy Theory, pages 619-656, Jan 2020. URL: https://doi.org/10.1201/9781351251624-15, doi:10.1201/9781351251624-15. This article has 58 citations.

19. (geisser2003topologicalcyclichomology pages 35-38): Thomas H. Geisser and L. Hesselholt. Topological cyclic homology of schemes. ArXiv, pages 41-87, Jan 2003. URL: https://doi.org/10.1090/pspum/067/1743237, doi:10.1090/pspum/067/1743237. This article has 118 citations.

20. (geisser2003topologicalcyclichomology pages 16-19): Thomas H. Geisser and L. Hesselholt. Topological cyclic homology of schemes. ArXiv, pages 41-87, Jan 2003. URL: https://doi.org/10.1090/pspum/067/1743237, doi:10.1090/pspum/067/1743237. This article has 118 citations.

21. (connes2501knotsprimesand pages 3-7): Alain Connes and Caterina Consani. Knots, primes and class field theory. Contemporary Mathematics, pages 105-132, Jun 2501. URL: https://doi.org/10.1090/conm/842/16852, doi:10.1090/conm/842/16852. This article has 2 citations and is from a peer-reviewed journal.