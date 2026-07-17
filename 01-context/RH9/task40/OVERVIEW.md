Question: 
Address the following research objective and research hypothesis:
<research-objective>Search the literature on Arakelov theory and related analytic number theory to find a mechanism that could produce spectral rigidity.
            1. Review explicit formulas within Arakelov theory, such as the Arithmetic Riemann-Roch theorem or formulas for arithmetic volumes.
            2. Search for any analysis of the asymptotic behavior of these formulas with respect to the number of primes included or the height of the variety.
            3. Look for any mechanism or error term that would lead to a suppression or change in behavior for correlations involving large ranges, analogous to `Δ₃(L)` saturation for large `L`.
            4. Specifically, investigate if the archimedean components (involving Green's functions and analytic torsion) interact with the finite-prime components in a way that limits long-range statistical fluctuations.</research-objective>
<research-hypothesis>The saturation of the `Δ₃(L)` statistic is a consequence of an intrinsic "finiteness" property within Arakelov theory. Global arithmetic formulas, such as arithmetic Riemann-Roch or formulas for intersection numbers, contain error terms or asymptotic regimes that depend on the set of primes considered. There exists a theorem or analysis showing that for "long-range" effects (analogous to large `L`), the contribution of large primes is suppressed or behaves in a non-random way, causing the saturation.</research-hypothesis>

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
The literature does not currently support a theorem that “large primes are intrinsically suppressed” in Arakelov formulas in a way that directly forces Δ₃(L) saturation, but it does provide multiple rigidity mechanisms—exact cancellation/anomaly compensation (arithmetic Riemann–Roch), bounded subleading errors in arithmetic Hilbert–Samuel/volume asymptotics, and explicit-formula cutoff phenomena—consistent with a finiteness-driven saturation scenario.
</conclusion>
<explanation>
Scope and approach. I searched for (i) explicit global Arakelov formulas mixing finite primes and archimedean data, (ii) asymptotics/error terms when varying tensor power/metrics or truncating local data, (iii) mechanisms analogous to long-range spectral rigidity saturation, and (iv) explicit interactions between archimedean analytic torsion/Green functions and finite-place contributions.

Key findings on explicit formulas (mechanism candidates).
1) Arithmetic Riemann–Roch and anomaly compensation. Gillet–Soulé’s arithmetic Riemann–Roch (Theorem 7) expresses the arithmetic class of det Rf∗(E) endowed with the Quillen metric (L2 metric times exp(analytic torsion)) as an arithmetic pushforward plus explicit correction terms involving Todd classes, Bott–Chern secondary forms, and a characteristic class R built from zeta values (archimedean data). This is precisely a “balancing” identity: metric-dependent analytic torsion contributions are not free, but appear through transgression-type correction terms so that the global class is well-defined and independent of auxiliary choices (embeddings, resolutions) after cancellations. (gillet1992anarithmeticriemannroch pages 49-53, gillet1992anarithmeticriemannroch pages 46-49)

Bismut’s formulation makes the mechanism explicit: analytic torsion forms satisfy a transgression identity
∂∂¯(2iπ)−1T = ch(Rπ∗E,g) − π∗(Td(TZ)ch(E)),
so the archimedean analytic term is exactly the “difference” between a pushforward of local characteristic forms and the Chern form of the direct image with its L2 metric; this is a rigidity mechanism because it constrains how archimedean fluctuations can appear in global arithmetic formulas. (bismut1998localindextheory pages 1-3)

2) Intersection/height formulas as constrained quadratic forms. In Arakelov intersection theory (in an adelic/Berkovich setting), χ-volumes and intersection pairings are governed by Green-function potentials; Chen–Moriwaki show volχ(D,g) = (D,g)·(D,g) and that both sides are stable under uniform approximation of Green functions (sup-norm convergence). The pairing includes integral terms in derivatives of Green functions and yields Hodge/Cauchy–Schwarz-type inequalities with equality criteria (proportionality), again indicating “stiffness” rather than unconstrained accumulation of local randomness. (chen2023arakelovtheoryon pages 52-55)

Asymptotics and explicit error terms (where “suppression” can enter).
3) Arithmetic Hilbert–Samuel / Okounkov-body asymptotics: bounded subleading errors. In the adelic/filtered Okounkov-body framework, Boucksom–Chen provide quantitative control: χ and normalized adelic degree coincide up to O(N log N), and χ(Vk) admits asymptotic descriptions with O(k^n log k) errors while the leading term is a deterministic integral of a concave transform over an Okounkov body. This is an explicit “suppression” mechanism in the sense that long-range (large k, large-dimensional) behavior is dominated by the leading arithmetic volume term and only a controlled, slower-growing error remains. (boucksom2011okounkovbodiesof pages 16-20, boucksom2011okounkovbodiesof pages 20-23)

4) Boundedness/finiteness conditions that limit effective fluctuation range. The same Boucksom–Chen framework emphasizes right-boundedness/linear boundedness of filtrations (under Northcott-type hypotheses), meaning that only a bounded range of filtration “jumps” contribute significantly; this resembles an effective finite correlation length in the arithmetic filtration data. (boucksom2011okounkovbodiesof pages 16-20, boucksom2011okounkovbodiesof pages 1-3)

Archimedean asymptotics: analytic torsion becomes regular at large scale.
5) High tensor powers: analytic torsion has a full asymptotic expansion. Finski proves a full asymptotic expansion of holomorphic analytic torsion for L^p⊗E of the form −2 log T = Σ p^{n−i}(αi log p + βi) + o(p^{n−k}) for arbitrary k, with leading coefficients local and (in part) metric-independent. This suggests archimedean analytic contributions become increasingly structured as p grows, rather than producing long-range random fluctuations. (finski2019onsomeproblems pages 42-44)

6) Effective archimedean bounds under Arakelov metric. Zhou gives explicit upper bounds for scalar analytic torsion (regularized det Laplacian) under the Arakelov metric on arithmetic surfaces, using bosonization to express torsion through Faltings’ delta invariant plus area, and then bounding those quantities. This provides an explicit “cap” on archimedean contributions in at least one central setting. (zhou2019effectiveupperbound pages 1-4)

Truncation/cutoff phenomena that most closely mirror Δ₃(L) saturation.
7) Truncated Weil explicit formula operator (Connes–van Suijlekom framework). Groskin’s study of the truncated Weil quadratic form decomposes the operator as D = D∞ + Dpole + Dprime, where Dprime is a finite sum over primes p ≤ c and D∞ is archimedean (digamma/Mellin multiplier). This is the cleanest example in the retrieved literature where prime cutoffs and archimedean terms are explicitly separated but combined in a single spectral object. (groskin2605highprecisionapproximationof pages 3-5)

Crucially, Groskin reports evidence for a “late regime” of diminishing returns: empirical marginal improvements in a spectral error behave like a power law with exponent α ≈ 1.48 > 1, which would make the tail of improvements summable and hence consistent with a finite asymptotic error floor (saturation) if the exponent persists. The work also notes that interval extension (log c) explains improvements better than prime identity per se, which suggests that “finiteness” may be driven by smoothing/test-function geometry rather than suppression of large primes individually. (groskin2605highprecisionapproximationof pages 30-33, groskin2605highprecisionapproximationof pages 3-5)

Interpretation relative to the research hypothesis.
• What the evidence supports: Arakelov theory contains intrinsic rigidity constraints: exact cancellation/anomaly compensation in arithmetic Riemann–Roch (Quillen/analytic torsion terms constrained by transgression identities) and deterministic leading asymptotic terms with controlled subleading errors in arithmetic Hilbert–Samuel/volume theory. These mechanisms make it plausible that long-range statistics built from such global formulas may saturate or become insensitive to further “range extension,” because new local data must enter through a convergent/controlled remainder or cancel against archimedean corrections. (gillet1992anarithmeticriemannroch pages 46-49, gillet1992anarithmeticriemannroch pages 49-53, bismut1998localindextheory pages 1-3, boucksom2011okounkovbodiesof pages 16-20, boucksom2011okounkovbodiesof pages 20-23)

• What the evidence does not yet provide: I did not find a theorem in standard Arakelov arithmetic Riemann–Roch/volume literature explicitly analyzing “truncating the set of primes up to P” and proving that contributions from primes > P are suppressed in a way directly analogous to Δ₃(L) saturation. The closest explicit cutoff analysis appears in the truncated Weil explicit-formula operator setting rather than in mainstream Arakelov intersection/height formulas. (groskin2605highprecisionapproximationof pages 30-33, groskin2605highprecisionapproximationof pages 3-5)

“Statistical tests performed.” Within the retrieved literature, the only explicit statistical testing relevant to saturation/rigidity was contained in Groskin’s numerical analysis of truncation regimes: (i) a regression-style claim that per-step gains correlate strongly with interval length increment ΔL rather than with prime-specific counts/weights, and (ii) an exponent fit α ≈ 1.48 > 1 used to argue summability (a saturation criterion). I did not perform new computations; I report the tests/fit as described in the paper and interpret them qualitatively as an analogue of Δ₃(L) saturation. (groskin2605highprecisionapproximationof pages 30-33, groskin2605highprecisionapproximationof pages 3-5)

Scientific implication. A coherent “mechanism story” consistent with the objective is:
(a) global Arakelov invariants are sums over places constrained by product-formula structures and by anomaly/transgression identities, so archimedean and finite-place components cannot fluctuate independently; (b) asymptotic invariants (volumes, χ) have leading deterministic growth with explicitly bounded subleading errors; and (c) in explicit-formula-inspired cutoffs, marginal contributions can become summable, yielding saturation. Together these provide an Arakelov/explicit-formula pathway to long-range rigidity, though not yet as a single established theorem matching the hypothesis verbatim. (gillet1992anarithmeticriemannroch pages 46-49, bismut1998localindextheory pages 1-3, boucksom2011okounkovbodiesof pages 16-20, groskin2605highprecisionapproximationof pages 30-33)

For convenience, the main candidate mechanisms are summarized here:
| Domain | Key object/formula | Where archimedean terms enter and how they interact with finite places | Type of suppression/rigidity | Implication for Δ₃(L)-like saturation |
|---|---|---|---|---|
| Arakelov global formulas | Arithmetic Riemann–Roch Theorem 7: determinant of cohomology with Quillen metric equals arithmetic pushforward plus Todd/Chern correction terms | Archimedean contribution enters through Quillen metric and Ray–Singer analytic torsion; these are balanced against algebraic pushforward/Todd terms so the resulting class is independent of auxiliary embeddings/metrics (gillet1992anarithmeticriemannroch pages 49-53, gillet1992anarithmeticriemannroch pages 46-49, bismut1998localindextheory pages 1-3, bismut1992oncertaininfinite pages 1-3) | Cancellation; anomaly compensation; metric/embedding independence | Suggests any long-range statistic built from the global formula is constrained by exact local-global balancing rather than freely accumulating random fluctuations |
| Arakelov global formulas | Heights/intersection as sums of local heights with Green functions; product formula framework | Finite places contribute via local heights/vertical data; archimedean places contribute via Green functions and admissible metrics, all assembled into a convergent global height/intersection (becker2018heightsinarakelov pages 1-5, chen2020arakelovgeometryover pages 1-8) | Global finiteness; convergence of local decomposition | Favors rigidity through a fixed global budget: adding more local places refines a convergent total instead of creating unlimited variance |
| Arakelov asymptotics | χ-volume equals self-intersection: volχ(D,g) = (D,g)·(D,g) | The metric part enters through Green-function potentials and derivative integrals; finite-place-style divisor data and analytic metric data combine in one bilinear pairing (chen2023arakelovtheoryon pages 52-55) | Equality principle; continuity under metric approximation | Indicates asymptotic observables are governed by a deterministic quadratic form, which is compatible with saturation of long-range fluctuations |
| Arakelov asymptotics | Hodge/Cauchy–Schwarz inequality for arithmetic intersections | Cross-terms between Green-function derivatives produce inequalities and equality criteria, forcing positivity and proportionality constraints on pairings (chen2023arakelovtheoryon pages 52-55) | Positivity bound; equality-rigidity | Acts like a stiffness mechanism: correlations cannot grow arbitrarily and are forced toward constrained large-scale behavior |
| Arakelov asymptotics | Arithmetic Hilbert–Samuel / adelic Okounkov asymptotics with O(N log N) discrepancy between χ and degree/minima sums | Archimedean and non-archimedean norms are aggregated into adelic vector bundles; local variation is smoothed in normalized asymptotics and only leaves subleading O(N log N) mismatch (boucksom2011okounkovbodiesof pages 16-20, boucksom2011okounkovbodiesof pages 20-23, chen2207hilbertsamuelformulaand pages 1-7) | Bounded subleading error; asymptotic averaging | Gives a concrete candidate for suppression: large-range behavior is dominated by leading deterministic volume terms, with only slower-growing error left |
| Arakelov asymptotics | Northcott/linear boundedness/right-bounded filtrations in adelic filtered series | Height filtrations sum contributions over all places but remain left/right bounded under adelic triviality/Northcott hypotheses (boucksom2011okounkovbodiesof pages 16-20, boucksom2011okounkovbodiesof pages 1-3) | Finiteness/bounded filtration range | Strongly analogous to finite correlation length: only a bounded effective range of jumps contributes materially to asymptotics |
| Archimedean analytic input | High-power analytic torsion asymptotics for Quillen metrics | Archimedean torsion contributes explicit leading terms in tensor-power expansions; lower-order terms are controlled by asymptotic expansions/remainders rather than arbitrary noise (kohler2602thefullasymptotic pages 1-3, kohler2602thefullasymptotic pages 13-16, finski2019onsomeproblems pages 42-44, puchol2016theasymptoticsof pages 1-2) | Controlled asymptotic expansion; algebraically suppressed remainder | Suggests archimedean corrections become increasingly regular at large scale, which could help enforce saturation instead of late-time fluctuation growth |
| Archimedean analytic input | Effective upper bounds for analytic torsion under Arakelov metric | Analytic torsion is rewritten via Faltings’ delta invariant and Arakelov area, giving explicit genus-dependent bounds on the archimedean contribution (zhou2019effectiveupperbound pages 1-4, zhou2019effectiveupperbound pages 7-10) | Explicit boundedness | Supports the idea that the archimedean sector may cap or regularize long-range contributions rather than amplify them |
| Weil explicit formula truncation | Truncated Weil form with D = D∞ + Dpole + Dprime and prime cutoff c | Archimedean Mellin/digamma part, pole term, and finite prime sum are explicitly separated; truncation changes both interval length and prime content (groskin2605highprecisionapproximationof pages 5-8, groskin2605highprecisionapproximationof pages 3-5) | Explicit truncation/smoothing by test function and cutoff | Gives the closest direct analogue of a finite-range mechanism: large-scale statistics depend on a cutoffed explicit formula, not an unrestricted prime sum |
| Weil explicit formula truncation | Empirical late-regime saturation law with marginal gains decaying like c^{-1.48} | The data suggest interval extension dominates more than prime identity; the tail of improvements can become summable when exponent exceeds 1 (groskin2605highprecisionapproximationof pages 30-33, groskin2605highprecisionapproximationof pages 3-5) | Convergent tail; diminishing returns | Provides a concrete Δ₃-like saturation analogue: beyond some scale, extending the range yields only a finite remaining correction |
| Weil explicit formula truncation | Basis/truncation saturation in Galerkin parameter N | Once the effective support of the eigenvector is captured, increasing basis size gives sharply diminishing returns (groskin2605highprecisionapproximationof pages 8-11) | Effective finite-dimensional support | Analogous to spectral rigidity saturation from finite effective degrees of freedom rather than exact arithmetic cancellation |
| Spectral-statistics analogue | Integrable-system mesoscopic smoothing by temperature/field | Arithmetic structure generates anomalous correlations, but external smoothing suppresses them and removes fragile fluctuations (wickramasinghe2006mesoscopicfeaturesof pages 57-61) | Smoothing-induced suppression | Suggests a model for how analytic smoothing in explicit formulas could quench long-range fluctuation growth |
| Spectral-statistics analogue | Prime-based coherence Hamiltonians with bounded normalized operator and sub-Euclidean spectral dimension | Some rigidity comes from operator normalization/bounds, while stronger compression is attributed to arithmetic sparsity of primes (watson2025spectralgeometryof pages 5-8, watson2025spectralgeometryof pages 8-10, watson2025spectralgeometryof pages 13-15, watson2025spectralgeometryof pages 1-3) | Operator norm bound plus arithmetic sparsity | Indicates that observed saturation can arise from a mix of formal boundedness and arithmetic structure, matching the search target in Arakelov-type settings |


*Table: This table summarizes the main mechanisms in the gathered literature that could plausibly generate spectral rigidity or saturation. It distinguishes exact Arakelov cancellations, asymptotic error suppression, and explicit-formula truncation effects that are most relevant to a Δ₃(L)-style saturation hypothesis.*
</explanation>
<discussion>
Limitations of the evidence relative to the hypothesis.
1) Prime-truncation in Arakelov theory vs. “adelic metrics.” Standard Arakelov formulas are naturally adelic: they incorporate all places at once (finite and infinite) and are typically studied under variations of metrics (archimedean) or models/line-bundle powers, not by explicitly cutting off primes p ≤ P and studying P → ∞. The closest “prime cutoff” phenomenon I found sits in the truncated Weil explicit-formula operator literature, which is adjacent to but not identical with classical Arakelov arithmetic intersection theory. (boucksom2011okounkovbodiesof pages 16-20, groskin2605highprecisionapproximationof pages 3-5)

2) Saturation may be a numerical/finite-dimensional artifact in explicit-formula truncations. Groskin also reports finite-N Galerkin truncation effects and numerical conditioning floors; these can mimic saturation unless one has an analytic remainder bound. Thus the saturation-like behavior in the truncated Weil form should not yet be interpreted as a proven arithmetic finiteness principle. (groskin2605highprecisionapproximationof pages 33-36, groskin2605highprecisionapproximationof pages 8-11)

3) “Suppression of large primes” is not directly identified as an Arakelov theorem. While Arakelov asymptotics show bounded errors and continuity under metric approximation, I did not locate a statement asserting that the contribution of large primes is non-random or suppressed in the manner required for Δ₃(L) saturation. The most defensible rigidity mechanism in Arakelov is instead the exact anomaly compensation/cancellation between archimedean torsion forms and algebraic pushforwards, plus the fact that asymptotics are governed by deterministic volume/intersection forms with controlled remainders. (gillet1992anarithmeticriemannroch pages 49-53, boucksom2011okounkovbodiesof pages 20-23, chen2023arakelovtheoryon pages 52-55)

4) Interpretation gap to Δ₃(L). Δ₃(L) saturation is a specific statistic of spectral fluctuations in random matrix / quantum chaos contexts. The Arakelov literature does not frame results in terms of Δ₃(L), so mapping requires a model choice: which arithmetic quantity is playing the role of the unfolded spectrum, and which truncation parameter corresponds to L? The truncated Weil form gives a direct “spectral” object with a prime cutoff, which is why it emerged as the closest analogue in this retrieval. (groskin2605highprecisionapproximationof pages 3-5, groskin2605highprecisionapproximationof pages 30-33)

Overall assessment. The strongest Arakelov-internal mechanism for “spectral rigidity” is not suppression of large primes per se, but rather the constraint that global arithmetic invariants are determined by (i) exact local-global identities with anomaly correction terms (analytic torsion/Quillen) and (ii) deterministic asymptotic leading terms with small controlled remainders. Whether this yields Δ₃(L) saturation for a specific arithmetic spectrum remains an open modeling and analytic question.
</discussion>
<proposed-next-hypotheses>
1) (Prime-cutoff summability hypothesis) For a fixed arithmetic variety X/OK with an adelic metrized line bundle L̄, define a “prime-truncated” height/intersection invariant by restricting the adelic metric data to primes p ≤ P and keeping archimedean data fixed; then the difference between the full invariant and its truncated version has a convergent tail as P → ∞ (e.g., the tail is absolutely summable or O(P^{-ε})).

2) (Archimedean compensation hypothesis) In families where arithmetic Riemann–Roch applies, the variation of finite-place contributions under changing the integral model (adding/removing bad primes) is asymptotically compensated by the induced change in Quillen/analytic torsion terms, leading to a uniform bound on long-range correlation measures derived from the resulting arithmetic determinants.
</proposed-next-hypotheses>
</output>

References

1. (gillet1992anarithmeticriemannroch pages 49-53): Henri Gillet and Christophe Soul�. An arithmetic riemann-roch theorem. Inventiones mathematicae, 110:473-543, Dec 1992. URL: https://doi.org/10.1007/bf01231343, doi:10.1007/bf01231343. This article has 306 citations and is from a highest quality peer-reviewed journal.

2. (gillet1992anarithmeticriemannroch pages 46-49): Henri Gillet and Christophe Soul�. An arithmetic riemann-roch theorem. Inventiones mathematicae, 110:473-543, Dec 1992. URL: https://doi.org/10.1007/bf01231343, doi:10.1007/bf01231343. This article has 306 citations and is from a highest quality peer-reviewed journal.

3. (bismut1998localindextheory pages 1-3): Jean-Michel Bismut. Local index theory and higher analytic torsion. Proceedings of the International Congress of Mathematicians 1998, pages 143-162, Jan 1998. URL: https://doi.org/10.4171/dms/1-1/1, doi:10.4171/dms/1-1/1. This article has 29 citations.

4. (chen2023arakelovtheoryon pages 52-55): Huayi Chen and Atsushi Moriwaki. Arakelov theory on arithmetic surfaces over a trivially valued field. International Mathematics Research Notices, 2023:5473-5537, Feb 2023. URL: https://doi.org/10.1093/imrn/rnab302, doi:10.1093/imrn/rnab302. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (boucksom2011okounkovbodiesof pages 16-20): Sebastien Boucksom and Huayi Chen. Okounkov bodies of filtered linear series. Compositio Mathematica, 147:1205-1229, Nov 2011. URL: https://doi.org/10.48550/arxiv.0911.2923, doi:10.48550/arxiv.0911.2923. This article has 183 citations and is from a domain leading peer-reviewed journal.

6. (boucksom2011okounkovbodiesof pages 20-23): Sebastien Boucksom and Huayi Chen. Okounkov bodies of filtered linear series. Compositio Mathematica, 147:1205-1229, Nov 2011. URL: https://doi.org/10.48550/arxiv.0911.2923, doi:10.48550/arxiv.0911.2923. This article has 183 citations and is from a domain leading peer-reviewed journal.

7. (boucksom2011okounkovbodiesof pages 1-3): Sebastien Boucksom and Huayi Chen. Okounkov bodies of filtered linear series. Compositio Mathematica, 147:1205-1229, Nov 2011. URL: https://doi.org/10.48550/arxiv.0911.2923, doi:10.48550/arxiv.0911.2923. This article has 183 citations and is from a domain leading peer-reviewed journal.

8. (finski2019onsomeproblems pages 42-44): S Finski. On some problems of holomorphic analytic torsion. Unknown journal, 2019.

9. (zhou2019effectiveupperbound pages 1-4): Changwei Zhou. Effective upper bound of analytic torsion under arakelov metric. Preprint, Jan 2019. URL: https://doi.org/10.48550/arxiv.1903.08779, doi:10.48550/arxiv.1903.08779. This article has 0 citations.

10. (groskin2605highprecisionapproximationof pages 3-5): High-Precision Approximation of Riemann Zeros via the Truncated Weil Form This article has 0 citations.

11. (groskin2605highprecisionapproximationof pages 30-33): High-Precision Approximation of Riemann Zeros via the Truncated Weil Form This article has 0 citations.

12. (bismut1992oncertaininfinite pages 1-3): Jean-Michel Bismut. On certain infinite dimensional aspects of arakelov intersection theory. Communications in Mathematical Physics, 148:217-248, Aug 1992. URL: https://doi.org/10.1007/bf02100860, doi:10.1007/bf02100860. This article has 14 citations and is from a highest quality peer-reviewed journal.

13. (becker2018heightsinarakelov pages 1-5): D Becker. Heights in arakelov geometry. Unknown journal, 2018.

14. (chen2020arakelovgeometryover pages 1-8): Huayi Chen and Atsushi Moriwaki. Arakelov geometry over adelic curves. Lecture Notes in Mathematics, Jan 2020. URL: https://doi.org/10.1007/978-981-15-1728-0, doi:10.1007/978-981-15-1728-0. This article has 48 citations and is from a peer-reviewed journal.

15. (chen2207hilbertsamuelformulaand pages 1-7): Huayi Chen and Atsushi Moriwaki. Hilbert-samuel formula and positivity over adelic curves. Preprint, Jan 2207. URL: https://doi.org/10.48550/arxiv.2207.02033, doi:10.48550/arxiv.2207.02033. This article has 6 citations.

16. (kohler2602thefullasymptotic pages 1-3): The full asymptotic expansion of analytic torsion on homogeneous spaces This article has 0 citations.

17. (kohler2602thefullasymptotic pages 13-16): The full asymptotic expansion of analytic torsion on homogeneous spaces This article has 0 citations.

18. (puchol2016theasymptoticsof pages 1-2): Martin Puchol. The asymptotics of the holomorphic torsion forms. Comptes Rendus Mathematique, 354:301-306, Mar 2016. URL: https://doi.org/10.1016/j.crma.2015.11.004, doi:10.1016/j.crma.2015.11.004. This article has 4 citations and is from a peer-reviewed journal.

19. (zhou2019effectiveupperbound pages 7-10): Changwei Zhou. Effective upper bound of analytic torsion under arakelov metric. Preprint, Jan 2019. URL: https://doi.org/10.48550/arxiv.1903.08779, doi:10.48550/arxiv.1903.08779. This article has 0 citations.

20. (groskin2605highprecisionapproximationof pages 5-8): High-Precision Approximation of Riemann Zeros via the Truncated Weil Form This article has 0 citations.

21. (groskin2605highprecisionapproximationof pages 8-11): High-Precision Approximation of Riemann Zeros via the Truncated Weil Form This article has 0 citations.

22. (wickramasinghe2006mesoscopicfeaturesof pages 57-61): J Wickramasinghe. Mesoscopic features of classically integrable systems. Unknown journal, 2006.

23. (watson2025spectralgeometryof pages 5-8): Douglas F. Watson. Spectral geometry of the primes. Mathematics, Nov 2025. URL: https://doi.org/10.48550/arxiv.2604.03351, doi:10.48550/arxiv.2604.03351. This article has 1 citations.

24. (watson2025spectralgeometryof pages 8-10): Douglas F. Watson. Spectral geometry of the primes. Mathematics, Nov 2025. URL: https://doi.org/10.48550/arxiv.2604.03351, doi:10.48550/arxiv.2604.03351. This article has 1 citations.

25. (watson2025spectralgeometryof pages 13-15): Douglas F. Watson. Spectral geometry of the primes. Mathematics, Nov 2025. URL: https://doi.org/10.48550/arxiv.2604.03351, doi:10.48550/arxiv.2604.03351. This article has 1 citations.

26. (watson2025spectralgeometryof pages 1-3): Douglas F. Watson. Spectral geometry of the primes. Mathematics, Nov 2025. URL: https://doi.org/10.48550/arxiv.2604.03351, doi:10.48550/arxiv.2604.03351. This article has 1 citations.

27. (groskin2605highprecisionapproximationof pages 33-36): High-Precision Approximation of Riemann Zeros via the Truncated Weil Form This article has 0 citations.