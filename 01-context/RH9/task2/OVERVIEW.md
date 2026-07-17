Question: 
Address the following research objective and research hypothesis:
<research-objective>Survey the literature on Shimura varieties, automorphic forms, and Arakelov geometry to find a proof of the invariance of canonical metrics under Hecke correspondences.
            1. Review foundational texts and papers on Shimura varieties (e.g., Milne, Deligne, Rapoport-Zink) and their Arakelov-theoretic treatment (e.g., Künnemann, Howard-Madapusi Pera, Bruinier-Howard-Yang).
            2. Identify the precise definitions of canonical metrics (e.g., Petersson metric on the Hodge bundle) on automorphic line bundles over Shimura varieties.
            3. Search for a theorem, proposition, or explicit proof demonstrating that these metrics are preserved (i.e., that the correspondence induces an isometry `p₁*L̄ ≅ p₂*L̄`).
            4. Document the specific conditions (e.g., on the type of Shimura variety, the compactification, the level structure) under which this invariance holds.</research-objective>
<research-hypothesis>For Shimura varieties, the canonical (e.g., Petersson or log-singular) hermitian metrics on automorphic line bundles (like the Hodge bundle `ω`) are preserved under the action of Hecke correspondences. This invariance is a standard result in the theory of automorphic forms and Shimura varieties, expressed as an isomorphism of hermitian bundles `p₁*L̄ ≅ p₂*L̄` where `p₁, p₂` are the projections of the Hecke correspondence.</research-hypothesis>

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
The literature supports the hypothesis: canonical (Petersson/invariant and “good” log-singular) hermitian metrics on automorphic (in particular, Hodge-type) line/vector bundles on Shimura varieties are preserved under maps underlying Hecke correspondences, yielding the expected hermitian isomorphisms between the two pullbacks along the correspondence.
</conclusion>
<explanation>
Scope and method (non-statistical).
This is a proof-oriented, non-empirical objective; accordingly no statistical tests apply. Instead, I performed targeted full-text retrieval and evidence extraction for explicit metric definitions and for functoriality/isometry statements under (i) adelic translation maps that generate Hecke correspondences and (ii) general morphisms of Shimura data that include Hecke morphisms. The key acceptance criterion was the presence of an explicit descent/isometry proof for the canonical metric (or an explicit canonical pullback isomorphism of hermitian bundles) from which the correspondence identity p₁^*\bar L ≅ p₂^*\bar L follows.

1) Canonical metrics (Petersson/invariant) on automorphic bundles.
Ichino–Prasanna (quaternionic Shimura varieties) explicitly construct a positive-definite hermitian metric on automorphic vector bundles by combining: (a) canonical hermitian forms H_h arising from the Hodge decomposition (including explicit transformation laws under GL₂-actions), and (b) an idelic scaling factor \|\nu(g_f)\|^r on the fiber over (h,g_f) in X_B^+×G_B(A_f). (ichino2021periodsofquaternionic pages 14-17, ichino2021periodsofquaternionic pages 17-19) They then define the Petersson norm of a section by integrating the resulting pointwise norm. (ichino2021periodsofquaternionic pages 17-19)

Hörmann (orthogonal type, toroidal compactifications) constructs “Hermitian automorphic vector bundles” (Ξ^*E, Ξ^*h_E) on toroidally compactified Shimura varieties by starting from P_X-equivariant bundles on the compact dual equipped with P_σX(R)U_σX(C)-invariant metrics, pulling back via the canonical map Ξ, and extending across the boundary with a metric that is “good” (in Mumford’s sense) along a normal-crossings boundary divisor; the extension is characterized by uniqueness. (hormann2014thegeometricand pages 55-59)

2) Explicit invariance/isometry mechanism implying Hecke invariance.
(a) Descent under adelic equivalence implies isometry for adelic-translation (Hecke) maps.
Ichino–Prasanna’s Proposition 1.9 proves that the above hermitian metric descends from X_B^+×G_B(A_f) to the Shimura variety Sh_K(G_B,X_B). The key step checks that when (h',g_f')=(\gamma·h, \gamma_f g_f\kappa) represent the same point (γ∈G_B(Q)^+, κ∈K), the induced identification of fibers is metric-preserving; the proof uses the explicit equivariance \langle gx,gy\rangle_{g·h}=\nu(g)^r\langle x,y\rangle_h together with the product formula and \|\nu(\kappa)\|=1 to show cancellation, yielding
\langle \gamma v_1,\gamma v_2\rangle_{\gamma·h}\,\|\nu(\gamma_f g_f\kappa)\|^r = \langle v_1,v_2\rangle_h\,\|\nu(g_f)\|^r.
(ichino2021periodsofquaternionic pages 17-19)
Because Hecke correspondences are built from double cosets and realized analytically by adelic right-translations (and their induced finite étale maps between level quotients), the metric-preserving property under these adelic translations is precisely the content needed to conclude that for the associated canonical hermitian automorphic bundle \bar L, the two pullbacks along the two legs of a Hecke correspondence are canonically identified isometrically (the usual formulation p₁^*\bar L ≅ p₂^*\bar L). (ichino2021periodsofquaternionic pages 17-19)

(b) Functoriality of hermitian automorphic bundles under morphisms (α,ρ) covering Hecke maps.
In Hörmann’s framework, Remark 10.5 states a canonical isomorphism of hermitian bundles under any morphism of (extended) Shimura data (α,ρ):
M(α,ρ)^*(Ξ^*E,Ξ^*h_E) ≅ (Ξ^*M^∨(α)^*E, Ξ^*M^∨(α)^*h_E),
and emphasizes compatibility with composition. (hormann2014thegeometricand pages 55-59)
Hecke correspondences on Shimura varieties arise from such morphisms determined by adelic elements ρ (double-coset operators), so this canonical pullback isomorphism supplies exactly the hermitian identification needed to compare the two pullbacks along the correspondence projections after identifying the common “automorphic bundle” input on the compact dual. (hormann2014thegeometricand pages 55-59)

3) Conditions under which invariance holds.
From Hörmann, the construction is carried out for pure p-ECSD/p-ECMSD with smooth, projective, complete toroidal compactification Δ and boundary divisor D of normal crossings; the analytic quotient description and metric construction assumes neat level K. The uniqueness of the good metric extension (Theorem 10.3) additionally assumes the automorphic bundle is “fully decomposed” (unipotent radical of stabilizer acts trivially). (hormann2014thegeometricand pages 55-59)
From Ichino–Prasanna, the metric descent argument is at the level of the complex Shimura variety Sh_K(G_B,X_B) for open compact K, using the equivalence relation by γ∈G_B(Q)^+ and κ∈K and the fact \|\nu(\kappa)\|=1; it does not require compactification. (ichino2021periodsofquaternionic pages 17-19)

Scientific implication.
Together, these results show that “canonical metrics” used in Arakelov treatments of Shimura varieties (smooth invariant metrics on the open part and good/log-singular extensions on toroidal compactifications) are constructed to be invariant under the defining group actions and functorial in the Shimura datum. Since Hecke correspondences are induced by such group-theoretic maps, the invariance/isometry property is a built-in feature of the canonical hermitian structures.
</explanation>
<discussion>
Strength of evidence.
The strongest explicit, proof-level evidence found is Ichino–Prasanna Proposition 1.9, which verifies metric preservation under the equivalence relation defining the Shimura variety and thereby under adelic translation maps that generate Hecke operators. (ichino2021periodsofquaternionic pages 17-19) Hörmann provides a general functoriality statement for hermitian automorphic bundles under morphisms (α,ρ) and shows uniqueness of good metric extensions on toroidal compactifications; this is the natural general framework in which Hecke correspondences act by isometries. (hormann2014thegeometricand pages 55-59)

Limitations.
1) Exact p₁/p₂ correspondence phrasing: The retrieved texts provide proofs of metric invariance under the group/level-change morphisms that define Hecke correspondences, but they do not always print the invariance in the exact “p₁^*\bar L ≅ p₂^*\bar L” notation inside a labeled theorem. The implication to that phrasing is standard once one identifies the two legs of a Hecke correspondence with the relevant morphisms/adelic translations. (hormann2014thegeometricand pages 55-59, ichino2021periodsofquaternionic pages 17-19)
2) Coverage of all Shimura types: The explicit descent proof is provided for quaternionic Shimura varieties; the compactification/Arakelov “good metric” formalism is displayed for orthogonal-type Shimura varieties with toroidal compactifications. While both arguments are representation/functoriality-based and broadly portable, additional targeted retrieval (e.g., Hodge type, Siegel type, or more general Shimura varieties with integral models) would be required to cite a single universal reference covering all types with identical language.
3) Integral models: This search emphasized complex-analytic and toroidal-compactified settings. Burgos–Kramer–Kühn indicate an Arakelov framework suitable for Petersson metrics and applications to Hecke correspondences on products of modular curves, but the early pages retrieved did not include the specific invariance statement; deeper extraction of later sections would likely yield more explicit modular-curve p₁/p₂ statements in Arakelov language. (gil2007cohomologicalarithmeticchow pages 1-5)
</discussion>
<proposed-next-hypotheses>
1) For Shimura varieties of Hodge type with Madapusi Pera’s integral canonical models and toroidal compactifications, the canonical extension of the Hodge bundle with its Petersson (good/log-singular) metric is Hecke-equivariant in the strong sense that the isomorphism p₁^*ω ≅ p₂^*ω on the underlying line bundle upgrades canonically to an isometry of hermitian line bundles on the compactification.
2) In the Burgos–Kramer–Kühn “log-log/pre-log-log” arithmetic Chow framework for automorphic line bundles on (noncompact) Shimura varieties, the Hecke action on arithmetic Chow groups can be realized by correspondences whose induced pullbacks preserve the canonical Green currents coming from Petersson metrics (i.e., Hecke operators act by isometries at the level of metrized line bundles/currents, not only at the level of underlying line bundles).
</proposed-next-hypotheses>
</output>

References

1. (ichino2021periodsofquaternionic pages 14-17): Atsushi Ichino and Kartik Prasanna. Periods of quaternionic shimura varieties. i. Preprint, Jan 2021. URL: https://doi.org/10.48550/arxiv.1610.00166, doi:10.48550/arxiv.1610.00166. This article has 26 citations.

2. (ichino2021periodsofquaternionic pages 17-19): Atsushi Ichino and Kartik Prasanna. Periods of quaternionic shimura varieties. i. Preprint, Jan 2021. URL: https://doi.org/10.48550/arxiv.1610.00166, doi:10.48550/arxiv.1610.00166. This article has 26 citations.

3. (hormann2014thegeometricand pages 55-59): Fritz Hörmann. The geometric and arithmetic volume of shimura varieties of orthogonal type. ArXiv, Nov 2014. URL: https://doi.org/10.1090/crmm/035, doi:10.1090/crmm/035. This article has 17 citations.

4. (gil2007cohomologicalarithmeticchow pages 1-5): J. I. Burgos Gil, J. Kramer, and U. Kuehn. Cohomological arithmetic chow rings. Journal of the Institute of Mathematics of Jussieu, 6:1-172, Apr 2007. URL: https://doi.org/10.48550/arxiv.math/0404122, doi:10.48550/arxiv.math/0404122. This article has 105 citations and is from a domain leading peer-reviewed journal.