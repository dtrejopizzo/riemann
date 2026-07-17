Question: 
Address the following research objective and research hypothesis:
<research-objective>Perform a comparative analysis of Deninger's program on zeta functions and the formalism of absolute prismatic cohomology. Systematically map the conjectural objects and properties in Deninger's work to potential counterparts in prismatic theory. Specifically, investigate:
            1. Can the conjectural cohomology `H*(Spec Z, *abs)` be defined as a form of prismatic cohomology over the `Σ_Z` stack?
            2. Does the Nygaard filtration or other structures in prismatic cohomology provide a candidate for the weight filtration conjectured by Deninger?
            3. Can the local prismatic Frobenius operators `φ_p` be assembled or interpolated in a way that relates to the global operator `θ`?
            The objective is to synthesize these two lines of research to see if they are compatible and can inform each other.</research-objective>
<research-hypothesis>Deninger's conjectural framework for a global cohomology `H*(Spec O_K)` and a spectral operator `θ` can be formally realized using the language and tools of absolute prismatic cohomology, providing a bridge between the desired spectral properties and a concrete geometric formalism.</research-hypothesis>

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
Deninger’s conjectural global cohomology-with-operator package is not yet formally realized by absolute/integral prismatic cohomology, but the prismatization stacks (especially \(\Sigma_{\mathbf Z}\)) and the Nygaard/Frobenius/Sen-operator structures provide a plausible geometric scaffold on which substantial parts of his framework could be reformulated, leaving the key missing ingredient as a genuinely global “spectral” operator \(\theta\) interpolating local Frobenius data.
</conclusion>
<explanation>
This analysis compared (i) Deninger’s axioms for a conjectural cohomology \(H^i(Y_K,\mathbf C)\) (or \(H^*(\mathrm{Spec}\,\mathbf Z,*_{abs})\)) equipped with an unbounded operator \(\theta\) whose spectrum encodes zeros of \(\widehat\zeta_K(s)\), together with a trace \(H^2\to \mathbf C(-1)\), cup products, and dualities, against (ii) absolute/integral prismatic cohomology and its stacky prismatization formalism.

Deninger’s package (baseline objects to map). Deninger posits cohomology groups \(H^i(Y_K,\mathbf C)\) vanishing in degrees \(\ge 3\), with \(H^0\cong \mathbf C\) and \(\theta=0\) on \(H^0\), and a trace identification \(H^2\xrightarrow{\mathrm{tr}}\mathbf C(-1)\) with \(\theta\) acting as the identity on \(H^2\). He requires a cup product \(H^1\times H^1\to H^2\) and that \(\theta\) acts as a derivation for cup products. On \(H^1\) there is an antilinear \(*\)-operator with \(*^2=-1\) that commutes with \(\theta\) and yields a hermitian form \(\langle h,h'\rangle = \mathrm{tr}(h\cup *h')\); this forces symmetry properties of \(\theta\) (e.g. skew-symmetry after shifting), and provides pairings between \(\theta\)-eigenspaces at \(\rho\) and \(1-\rho\). Finally, the completed Dedekind zeta \(\widehat\zeta_K(s)\) is expressed via zeta-regularized determinants of shifts of \(\theta\) on the \(H^i\), and the multiplicity of a zero at \(s=\rho\) matches \(\dim (H^1)_{\theta=\rho}\); since \(\widehat\zeta_K\) has infinitely many zeros, \(H^1\) must be infinite dimensional and \(\theta\) unbounded. (deninger2504istherea pages 1-4, deninger2504istherea pages 4-7)

Prismatic scaffold for a “global cohomology over \(\mathbf Z\)”. Independently of any zeta-spectral claims, integral prismatization over \(\mathbf Z\) constructs a base stack \(\Sigma_{\mathbf Z}:=\mathrm{Spec}(\mathbf Z)^{\Delta}_{\mathbf Z}\) and, for any \(\mathbf Z\)-scheme \(f:X\to \mathrm{Spec}(\mathbf Z)\), a prismatized stack \(X_{\Delta_{\mathbf Z}}\to \Sigma_{\mathbf Z}\) whose “integral prismatic cohomology” is defined as \(H_{\Delta_{\mathbf Z}}(X):= Rf_{\Delta_{\mathbf Z},*}(\mathcal O_{X_{\Delta_{\mathbf Z}}})\in D(\Sigma_{\mathbf Z})\). This directly answers sub-question (1) at the level of availability of a definition: there is already a natural candidate construction of a cohomology-like object attached to \(X\) living over \(\Sigma_{\mathbf Z}\), i.e. exactly the kind of global base where a conjectural \(H^*(\mathrm{Spec}\,\mathbf Z,*_{abs})\) could be placed. (gurney2301prismatizationover$\mathbf{z}$ pages 1-4)

However, Deninger’s \(H^*(\cdot,\mathbf C)\) is designed to produce a complex-analytic regularized determinant formula and a spectral operator with critical-line symmetry, while the prismatic object \(H_{\Delta_{\mathbf Z}}(X)\) is an object of a derived category over a geometric stack; no source in the retrieved evidence equips \(H_{\Delta_{\mathbf Z}}(\mathrm{Spec}\,\mathbf Z)\) with Deninger’s \(\theta\), trace to \(\mathbf C(-1)\), or determinant formalism.

Nygaard filtration as a candidate “weight filtration”. In prismatic theory, a central additional structure is the Nygaard filtration: a complete, exhaustive, decreasing, multiplicative filtration on absolute prismatic cohomology that is tightly controlled by Frobenius. One way to package it is via the Nygaard prismatization \(X^N\): for qrsp affines \(X=\mathrm{Spf}(R)\), one has an explicit formula \(\mathrm{Spf}(R)^N\simeq \mathrm{Spf}(\oplus_i \mathrm{Fil}^i\Delta_R)/\mathbf G_m\), and the morphism \(X^N\to \mathbf A^1/\mathbf G_m\) has generic fiber \(X^{\Delta}\) and “encodes the Nygaard filtration.” (gregoric2511prismatizationviaspherical media 08c02ee9)

Moreover, divided prismatic Frobenii \(\varphi_i\) act on Nygaard-filtered pieces, and graded Nygaard pieces relate to Hodge–Tate / derived de Rham data. (andriopoulos2412trandthe pages 16-18)

These properties make the Nygaard filtration the strongest available prismatic candidate for Deninger’s conjectural “weight filtration” (sub-question 2): it is functorial, multiplicative, and interacts with Frobenius in a way reminiscent of weight decompositions in \(p\)-adic Hodge theory. (andriopoulos2412trandthe pages 16-18, gregoric2511prismatizationviaspherical pages 1-3, gregoric2511prismatizationviaspherical media 08c02ee9)

Nonetheless, none of the retrieved sources asserts that Nygaard equals (or canonically induces) Deninger’s weight filtration, and Deninger’s filtration is meant to underpin global zeta-spectral phenomena, including archimedean input, whereas Nygaard is intrinsically \(p\)-adic.

Local Frobenius operators \(\varphi_p\) vs a global \(\theta\). Prismatic cohomology comes naturally with Frobenius actions (coming from δ-structures/Frobenius lifts on prisms) and, in the stacky prismatization, with a Frobenius endomorphism \(F_X: X_{\Delta}\to X_{\Delta}\) induced by Witt-vector Frobenius on Cartier–Witt divisors. (hauck2409astackyapproach pages 24-28, bhatt2022prismsandprismatic pages 1-3)

This provides a clear prismatic analogue of “local Frobenius operators” at a fixed prime \(p\). But Deninger’s \(\theta\) is an infinitesimal/global generator whose spectrum is expected to encode the zeros of \(\widehat\zeta_K\); by contrast, prismatic Frobenius is a discrete endomorphism (and depends on \(p\)), and the retrieved evidence does not provide any construction assembling the family \(\{\varphi_p\}_p\) into a single global operator on a cohomology object over \(\mathbf Z\). This addresses sub-question (3) negatively at present: the compatibility is heuristic (both play “Frobenius-like” roles), but there is no demonstrated interpolation mechanism.

A further suggestive bridge is the appearance of Sen operators \(\Theta\) in prismatic-adjacent contexts: in the prismatic/Hodge–Tate picture, Sen complexes \((E,\Theta)\) appear and \(\Theta\) acts by explicit integers on graded pieces of an associated filtration, mimicking a “weight operator” more than a Frobenius does. (bhatt2023algebraicgeometryin pages 7-9) This is conceptually closer to Deninger’s infinitesimal \(\theta\), but \(\Theta\) is not currently shown to control global zeta zeros or to be derived from assembling the \(\varphi_p\).

Statistical tests. No statistical inference tests (e.g. hypothesis tests, regression) were applicable because the objective is purely theoretical/comparative and the evidence consists of definitions and structural theorems rather than numerical datasets. The “results” here are therefore logical entailments/compatibility checks from the cited sources.

Scientific implications. The evidence supports a compatibility-at-the-level-of-geometry claim: prismatization provides a concrete geometric home for cohomology objects over \(\mathbf Z\) (via \(\Sigma_{\mathbf Z}\) and \(H_{\Delta_{\mathbf Z}}\)), and prismatic theory supplies canonical filtrations (Nygaard) and operators (Frobenius/divided Frobenius, Sen operators) that resemble some of the formal roles in Deninger’s conjectures. (gurney2301prismatizationover$\mathbf{z}$ pages 1-4, andriopoulos2412trandthe pages 16-18, hauck2409astackyapproach pages 24-28, bhatt2023algebraicgeometryin pages 7-9)

At the same time, the decisive spectral features of Deninger’s program—regularized determinants yielding \(\widehat\zeta_K(s)\) and a global unbounded \(\theta\) with critical-line symmetry enforced by duality—are not currently realized in the prismatic sources collected. (deninger2504istherea pages 1-4)
</explanation>
<discussion>
The comparison indicates partial conceptual alignment but large technical gaps.

(1) Defining \(H^*(\mathrm{Spec}\,\mathbf Z,*_{abs})\) via prismatic theory over \(\Sigma_{\mathbf Z}\): there is strong evidence that the stack \(\Sigma_{\mathbf Z}\) and the functorial complexes \(H_{\Delta_{\mathbf Z}}(X)\in D(\Sigma_{\mathbf Z})\) exist and provide a robust “absolute” cohomological receptacle attached to \(\mathbf Z\)-schemes. (gurney2301prismatizationover$\mathbf{z}$ pages 1-4) This supports the research objective’s first direction at the level of formal definitions. What is missing is any established comparison between \(H_{\Delta_{\mathbf Z}}(\mathrm{Spec}\,\mathbf Z)\) and the type of cohomology Deninger needs (complex coefficients, regularized determinants, archimedean components, functional equation symmetry).

(2) Weights vs Nygaard: Nygaard filtration is the best available prismatic candidate for a weight filtration because it is canonical, multiplicative, complete, and Frobenius-controlled, and it is even geometrized by a dedicated stack \(X^N\). (andriopoulos2412trandthe pages 16-18, gregoric2511prismatizationviaspherical media 08c02ee9) Nonetheless, Deninger’s weights are conjectural global objects designed to interact with \(\theta\) and zeta zeros; an actual identification would require, at minimum, a construction of Deninger’s \(\theta\) (or something playing its role) within the prismatic setting.

(3) Local Frobenius vs global \(\theta\): prismatic theory natively provides (a) local Frobenius endomorphisms and (b) divided Frobenius maps compatible with Nygaard. (andriopoulos2412trandthe pages 16-18, hauck2409astackyapproach pages 24-28) Deninger’s operator is global and infinitesimal. The current evidence offers only suggestive potential substitutes: the Sen operator \(\Theta\) has weight-like eigenvalues on graded pieces, and might be a more plausible bridge to an infinitesimal generator than Frobenius itself, but no global interpolation statement exists in the cited texts. (bhatt2023algebraicgeometryin pages 7-9)

Limitations. This work is limited by (i) the absence (in the retrieved corpus) of any paper explicitly attempting to identify Deninger’s \(\theta\) with prismatic data, (ii) the unobtained Drinfeld “Prismatization” paper (not accessible in the search results), and (iii) the fact that Deninger’s program involves analytic notions (regularized determinants, spectral theory) that lie outside the algebraic definitions captured in the prismatic references retrieved here. Consequently, the outcome is best viewed as a structured compatibility/mapping assessment rather than a proof of the hypothesis.

To summarize the mapping succinctly, the following table records the most evidence-supported correspondences and the major missing links.

| Deninger object/property | Candidate prismatic / prismatization counterpart | Basis for mapping | Status |
|---|---|---|---|
| Conjectural global cohomology `H^*(Spec Z,*abs)` / `H^*(Y_K,\mathbf C)` | Integral prismatization over `\Sigma_Z := Spec(\mathbf Z)^\Delta_{\mathbf Z}` with `H_{\Delta_Z}(X) := Rf_{\Delta_Z,*}\mathcal O_{X_{\Delta_Z}} \in D(\Sigma_Z)`; p-adically, absolute prismatization `X_\Delta` / `WCart_X` with `R\Gamma(X_\Delta,\mathcal O) \simeq R\Gamma_\Delta(X)` | This is the strongest structural bridge: Deninger asks for a global cohomology attached to arithmetic schemes, while integral prismatization over `\Sigma_Z` already packages a global-over-`\mathbf Z` cohomology object; in the p-adic setting, prismatization stacks are known geometric realizations of absolute prismatic cohomology. However, Deninger’s complex coefficients, regularized determinants, and spectral axioms are not yet built into `H_{\Delta_Z}`. (deninger2504istherea pages 1-4, gurney2301prismatizationover$\mathbf{z}$ pages 1-4, andriopoulos2412trandthe pages 16-18, bhatt2201theprismatizationof pages 1-3, hauck2409astackyapproach pages 24-28) | **Supported by evidence** as a formal candidate for the cohomology object, but **speculative** as a realization of Deninger’s full package |
| Spectral operator `\theta` on `H^1`, whose eigenvalues encode zeros and enter `\det_\infty(s-\theta)` | No global prismatic `\theta` is presently defined; only local/prismatic Frobenius structures: Frobenius endomorphism `F_X:X_\Delta\to X_\Delta`, Frobenius `\varphi` on `R\Gamma_\Delta`, and divided Frobenii `\varphi_i` on Nygaard pieces | Deninger’s `\theta` is an infinitesimal/global spectral generator, while prismatic theory provides arithmetic Frobenius operators indexed by `p` and filtration-compatible divided Frobenii. The analogy is conceptually strong, but current evidence only gives discrete/local Frobenius actions, not a globally assembled infinitesimal operator interpolating them. (deninger2504istherea pages 1-4, deninger2006adynamicalsystems pages 8-12, andriopoulos2412trandthe pages 16-18, hauck2409astackyapproach pages 24-28, bhatt2023algebraicgeometryin pages 3-5) | **Speculative** |
| Weight filtration conjectured by Deninger | Nygaard filtration on absolute prismatic cohomology; related conjugate filtration on Hodge–Tate cohomology; `r`-Nygaard refinements | Nygaard is a complete, multiplicative, decreasing filtration functorially tied to Frobenius, and its graded pieces compare to Hodge–Tate / derived de Rham / conjugate pieces. This makes it the most natural prismatic candidate for a “weight-type” filtration, but no source explicitly identifies it with Deninger’s conjectural weights. (andriopoulos2412trandthe pages 16-18, andriopoulos2412trandthe pages 1-2, bhatt2023algebraicgeometryin pages 7-9, gregoric2511prismatizationviaspherical pages 1-3) | **Speculative** but well-motivated |
| Tate/trace target `H^2 \xrightarrow{tr} \mathbf C(-1)` with `\theta=1` on top degree | Breuil–Kisin twist `\mathcal O_\Delta\{1\}` and its realizations of `\mathbf Z_p(1)` / Tate twists; top-degree trace/duality in prismatic `F`-gauges | The twist notation and étale realization as `\mathbf Z_p(1)` make Breuil–Kisin twists the closest integral analogue of a Tate object such as `\mathbf C(-1)`. What is missing is a global archimedean/complex realization and a direct prismatic construction of Deninger’s trace map to `\mathbf C(-1)`. (deninger2504istherea pages 1-4, bhatt2023algebraicgeometryin pages 7-9, bhatt2023algebraicgeometryin pages 11-14, hauck2409astackyapproach pages 24-28, bhatt2201theprismatizationof pages 1-3) | **Speculative** |
| Cup product on `H^1`, `*`-operator, hermitian pairing, and duality between `\theta`-eigenspaces `\rho \leftrightarrow 1-\rho` | Monoidal structure on prismatic/crystalline categories, duality for prismatic `F`-gauges, and geometric packaging via `WCart_X` / prismatization stacks | Prismatic theory has robust tensor, crystal, and duality formalisms, and some `F`-gauge results exhibit duality/Lagrangian behavior. But the specific Deninger package—hermitian form, `*`-operator, and symmetry pairing eigenvalues `\rho` with `1-\rho`—has no explicit prismatic counterpart in the retrieved evidence. (deninger2504istherea pages 4-7, deninger2504istherea pages 1-4, bhatt2023algebraicgeometryin pages 11-14, bhatt2201theprismatizationof pages 1-3) | **Missing / highly speculative** |
| Local Euler factors at primes and their relation to the global spectral formalism | Local prismatic Frobenius data at each `p`; `p`-adic fibers of `\Sigma_Z` recover `\Sigma_p`; absolute prismatic cohomology specializes prime-by-prime | Integral prismatization over `\Sigma_Z` is compatible with p-adic specializations, so local prime data are naturally visible in the prismatic formalism. This supports the idea that local factors should be encoded by the family of local Frobenii, but no determinant formula matching Deninger’s global spectral expression is currently available. (deninger2007analogiesbetweenanalysis pages 6-8, gurney2301prismatizationover$\mathbf{z}$ pages 1-4, gurney2301prismatizationover$\mathbf{z}$ pages 18-21, bhatt2023algebraicgeometryin pages 3-5) | **Supported by evidence** for local encoding; **speculative** for reconstruction of the global factorization |
| Assembly/interpolation of local `\varphi_p` into a single global operator `\theta` | Possible only at the level of heuristic comparison through `\Sigma_Z`, Sen operators `\Theta` on Hodge–Tate crystals, and the family of Frobenius/divided Frobenius maps | The evidence suggests two possible shadows of `\theta`: (a) the collection of local Frobenius operators across primes; (b) the Sen operator `\Theta`, which acts on Hodge–Tate/conjugate graded pieces by weight-like integers. Neither construction is shown to interpolate all `\varphi_p` into a single operator controlling zeta zeros. (bhatt2023algebraicgeometryin pages 7-9, hauck2409astackyapproach pages 24-28, andriopoulos2412trandthe pages 2-5) | **Speculative** |
| Infinitesimal spectral behavior of `\theta` | Sen operator `\Theta` on Hodge–Tate crystals / Sen complexes | Among prismatic-adjacent structures, `\Theta` is the closest infinitesimal operator: it acts with explicit integral weights on graded pieces of the conjugate filtration. This is suggestive because Deninger’s `\theta` is also infinitesimal rather than discrete. But `\Theta` lives on Hodge–Tate/crystalline realizations, not on the full absolute prismatic complex as a global zeta-spectral operator. (bhatt2023algebraicgeometryin pages 7-9, andriopoulos2412trandthe pages 2-5) | **Speculative** |
| Regularized determinant formula for completed zeta functions | No established prismatic analogue in the retrieved evidence; possible future target via TP/TC/prismatization enhancements and Frobenius structures | Prismatic theory and prismatization enhancements recover rich cohomological and cyclotomic structures, but none of the cited sources derive a Deninger-style `\det_\infty(s-\theta)` formula for `\widehat\zeta_K(s)`. This is a major gap between the two programs. (deninger2504istherea pages 1-4, bhatt2023algebraicgeometryin pages 11-14, gregoric2511prismatizationviaspherical pages 1-3) | **Missing** |


*Table: This table maps the main conjectural ingredients in Deninger’s zeta-cohomology program to the closest currently available structures in absolute/integral prismatic cohomology and prismatization stacks. It distinguishes what is already structurally supported by the literature from what remains heuristic or absent.*
</discussion>
<proposed-next-hypotheses>
1. (Nygaard-as-weights via \(\Sigma_{\mathbf Z}\)) There exists a functorial filtration \(W_\bullet\) on the integral prismatic complex \(H_{\Delta_{\mathbf Z}}(\mathrm{Spec}\,\mathbf Z)\) whose \(p\)-adic base change recovers the Nygaard filtration on \(R\Gamma_\Delta(\mathrm{Spf}\,\mathbf Z_p)\) and whose graded pieces control the \(\mathbf Z_p(i)\)-realizations (Tate twists) in a manner compatible with Deninger’s expected weights.

2. (Global generator from local Frobenius + Sen) After suitable linearization (e.g. taking logarithms on a “universal” prismatic/TP object over \(\Sigma_{\mathbf Z}\)), the family of local Frobenius actions \(\{\varphi_p\}\) and the Sen operator \(\Theta\) assemble into a single endomorphism \(\theta\) on a derived \(\mathbf R\)-vector space obtained from \(H_{\Delta_{\mathbf Z}}(\mathrm{Spec}\,\mathbf Z)\) whose regularized determinant recovers (or approximates) \(\widehat\zeta(s)\).
</proposed-next-hypotheses>
</output>

References

1. (deninger2504istherea pages 1-4): Christopher Deninger. Is there a birch and swinnerton-dyer conjecture for dedekind zeta functions? Sep 2504. URL: https://doi.org/10.1016/j.jnt.2026.02.004, doi:10.1016/j.jnt.2026.02.004. This article has 0 citations and is from a domain leading peer-reviewed journal.

2. (deninger2504istherea pages 4-7): Christopher Deninger. Is there a birch and swinnerton-dyer conjecture for dedekind zeta functions? Sep 2504. URL: https://doi.org/10.1016/j.jnt.2026.02.004, doi:10.1016/j.jnt.2026.02.004. This article has 0 citations and is from a domain leading peer-reviewed journal.

3. (gurney2301prismatizationover$\mathbf{z}$ pages 1-4): Unknown author(s). Unknown title. Unknown journal, Unknown year. This article has 0 citations.

4. (gregoric2511prismatizationviaspherical media 08c02ee9): Rok Gregoric. Prismatization via spherical loop spaces. ArXiv, Nov 2511. URL: https://doi.org/10.48550/arxiv.2511.00756, doi:10.48550/arxiv.2511.00756. This article has 1 citations.

5. (andriopoulos2412trandthe pages 16-18): Faidon Andriopoulos. Tr and the $r$-nygaard filtered prismatic cohomology. Preprint, Jan 2412. URL: https://doi.org/10.48550/arxiv.2412.00914, doi:10.48550/arxiv.2412.00914. This article has 3 citations.

6. (gregoric2511prismatizationviaspherical pages 1-3): Rok Gregoric. Prismatization via spherical loop spaces. ArXiv, Nov 2511. URL: https://doi.org/10.48550/arxiv.2511.00756, doi:10.48550/arxiv.2511.00756. This article has 1 citations.

7. (hauck2409astackyapproach pages 24-28): Maximilian Hauck. A stacky approach to $p$-adic hodge theory. Preprint, Jan 2409. URL: https://doi.org/10.48550/arxiv.2409.10557, doi:10.48550/arxiv.2409.10557. This article has 1 citations.

8. (bhatt2022prismsandprismatic pages 1-3): Bhargav Bhatt and Peter Scholze. Prisms and prismatic cohomology. Nov 2022. URL: https://doi.org/10.4007/annals.2022.196.3.5, doi:10.4007/annals.2022.196.3.5. This article has 411 citations and is from a highest quality peer-reviewed journal.

9. (bhatt2023algebraicgeometryin pages 7-9): Bhargav Bhatt. Algebraic geometry in mixed characteristic. Preprint, Jan 2023. URL: https://doi.org/10.48550/arxiv.2112.12010, doi:10.48550/arxiv.2112.12010. This article has 9 citations.

10. (bhatt2201theprismatizationof pages 1-3): Bhargav Bhatt and Jacob Lurie. The prismatization of $p$-adic formal schemes. Preprint, Jan 2201. URL: https://doi.org/10.48550/arxiv.2201.06124, doi:10.48550/arxiv.2201.06124. This article has 73 citations.

11. (deninger2006adynamicalsystems pages 8-12): Christopher Deninger. A dynamical systems analogue of lichtenbaum's conjectures on special values of hasse-weil zeta functions. Preprint, Jan 2006. URL: https://doi.org/10.48550/arxiv.math/0605724, doi:10.48550/arxiv.math/0605724. This article has 19 citations.

12. (bhatt2023algebraicgeometryin pages 3-5): Bhargav Bhatt. Algebraic geometry in mixed characteristic. Preprint, Jan 2023. URL: https://doi.org/10.48550/arxiv.2112.12010, doi:10.48550/arxiv.2112.12010. This article has 9 citations.

13. (andriopoulos2412trandthe pages 1-2): Faidon Andriopoulos. Tr and the $r$-nygaard filtered prismatic cohomology. Preprint, Jan 2412. URL: https://doi.org/10.48550/arxiv.2412.00914, doi:10.48550/arxiv.2412.00914. This article has 3 citations.

14. (bhatt2023algebraicgeometryin pages 11-14): Bhargav Bhatt. Algebraic geometry in mixed characteristic. Preprint, Jan 2023. URL: https://doi.org/10.48550/arxiv.2112.12010, doi:10.48550/arxiv.2112.12010. This article has 9 citations.

15. (deninger2007analogiesbetweenanalysis pages 6-8): C. Deninger. Analogies between analysis on foliated spaces and arithmetic geometry. Preprint, Jan 2007. URL: https://doi.org/10.48550/arxiv.0709.2801, doi:10.48550/arxiv.0709.2801. This article has 3 citations.

16. (gurney2301prismatizationover$\mathbf{z}$ pages 18-21): Unknown author(s). Unknown title. Unknown journal, Unknown year. This article has 0 citations.

17. (andriopoulos2412trandthe pages 2-5): Faidon Andriopoulos. Tr and the $r$-nygaard filtered prismatic cohomology. Preprint, Jan 2412. URL: https://doi.org/10.48550/arxiv.2412.00914, doi:10.48550/arxiv.2412.00914. This article has 3 citations.