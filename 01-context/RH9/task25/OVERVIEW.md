Question: 
Address the following research objective and research hypothesis:
<research-objective>Search the literature for explicit computations of metric-dependent arithmetic characteristic classes.
            1.  Find papers that provide an explicit formula for the Bott-Chern secondary class `BC(m₁, m₀)` that measures the difference between arithmetic Chern classes `ĉ₁(m₁) - ĉ₁(m₀)` for two different metrics `m₁`, `m₀`.
            2.  Focus on examples for arithmetic surfaces, ideally over `Spec ℤ` or a number ring.
            3.  Identify a case where this Bott-Chern class is shown to be non-zero in the appropriate Deligne-Beilinson or Arakelov cohomology.
            4.  If such a class `x = ĉ₁(m₁) - ĉ₁(m₀)` is non-trivial, find the formula for the corresponding change in the Lefschetz operator, `ΔL = ∪x`, and assess whether this operator is non-zero.</research-objective>
<research-hypothesis>The "local variation" argument for independence (G1) can be made explicit. For a simple arithmetic surface (e.g., a ruled surface over `Spec ℤ`) and an ample line bundle, there exists a specific change of hermitian metric for which the change in the arithmetic Chern class `ĉ₁` is non-trivial in the relevant arithmetic cohomology, thus proving that the cup-product operator `L = ∪ĉ₁` is non-constant with respect to the metric and therefore independent of the metric-invariant spectral operator `T`.</research-hypothesis>

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
The available literature evidence confirms explicit Bott–Chern formulas for metric variation in Arakelov theory, but does not (within retrieved sources) provide a concrete arithmetic surface example where a pure metric change yields a provably nontrivial class x = ĉ₁(m₁) − ĉ₁(m₀), so the research hypothesis is not yet demonstrated.
</conclusion>
<explanation>
1) Explicit formula for the Bott–Chern secondary class BC(m₁,m₀).

The general Bott–Chern transgression construction for a characteristic form φ is explicitly given as an integral over \(\mathbb{P}^1\). In Weng’s axiomatic construction, the Bott–Chern class associated to a \(\mathbb{P}^1\)-deformation is written in the displayed formula
\(\phi_{BC}(E,\rho):=\int_{\mathbb{P}^1}[\log|z|^2]\,\phi(DE_2,D\rho_2)\) (weng1998relativebottchernsecondary pages 5-9, weng1998relativebottchernsecondary media 67105565).
Specializing to two metrics \(\rho_1,\rho_2\) on the same bundle gives a class \(\phi_{BC}(E;\rho_2,\rho_1)\) satisfying
\(dd^c\,\phi_{BC}(E;\rho_2,\rho_1)=\phi(E,\rho_2)-\phi(E,\rho_1)\), i.e. it measures the difference of Chern–Weil forms (weng1998relativebottchernsecondary pages 5-9).

For the arithmetic setting, Kühn–Kramer–Burgos Gil describe an explicit first-transgression-bundle construction \(\mathrm{tr}_1\) and define the Bott–Chern form by an integral against \(\log|t|^2\) on \(\mathbb{P}^1\), i.e. \(\widetilde\phi(E)=-(2\pi i)^{-1}\int_{\mathbb{P}^1}\phi(\mathrm{tr}_1(E))\log|t|^2\), and they explain that for a change of metrics \(h,h'\) on a bundle \(E\) one uses \(\mathrm{tr}_1(E,h,h')\) (kuhn2005arithmeticcharacteristicclasses pages 56-60). They further record the key differential relation that the Bott–Chern secondary class transgresses the difference of characteristic forms (kuhn2005arithmeticcharacteristicclasses pages 56-60).

2) Relation to arithmetic Chern classes: \(x = \widehat c_1(m_1)-\widehat c_1(m_0)\).

In the arithmetic Chow formalism used in the automorphic/log-singular setting, the change of metric in arithmetic characteristic classes is stated explicitly: for two metrics \(h,h'\) one has
\(\widehat\phi(E,h)=\widehat\phi(E,h')+a\big(\widetilde\phi(E,h',h)\big)\), where \(a\) is the morphism sending suitable differential forms/currents to arithmetic Chow groups (kuhn2005arithmeticcharacteristicclasses pages 82-85). This is the precise template for the metric-dependence statement the objective seeks: in particular, for the first arithmetic Chern class of a hermitian line bundle (taking \(\phi=c_1\)), the difference \(x:=\widehat c_1(L,m_1)-\widehat c_1(L,m_0)\) is represented by an “\(a\)-image” of the corresponding Bott–Chern secondary class \(BC(m_1,m_0)\), up to sign/normalization conventions in \(dd^c\) (kuhn2005arithmeticcharacteristicclasses pages 82-85). The retrieved excerpts did not contain the commonly used simplified scalar expression for line bundles in terms of the pointwise logarithm of the ratio of metrics; instead they provide the general transgression and the arithmetic change-of-metric relation.

3) Arithmetic surfaces and explicit nonvanishing phenomena.

A fully explicit arithmetic-surface calculation with a manifestly nonzero real contribution occurs in Gillet–Soulé (2014), in the context of an exact sequence that is only exact on the generic fibre and a 0-dimensional closed subscheme \(\varphi\). Their Theorem 2 gives an equality of arithmetic degrees/pushforwards that includes the term \(\log\#\Gamma(\varphi,\mathcal O_\varphi)\) (gillet2014onthearithmetic pages 4-7). This term is explicitly nonzero when \(\#\Gamma(\varphi,\mathcal O_\varphi)>1\), so it provides a concrete example on an arithmetic surface where the arithmetic class being pushed forward is nontrivial numerically (gillet2014onthearithmetic pages 4-7). However, this nonvanishing is not presented as coming purely from changing a hermitian metric on a fixed line bundle; rather, it arises from the decomposition of the additivity defect into an archimedean Bott–Chern term and a localized finite-fibre term (gillet2014onthearithmetic pages 1-4, gillet2014onthearithmetic pages 4-7).

Independently, Weng notes that Bott–Chern classes can be nonzero already at the level of Bott–Chern cohomology quotients \(\widetilde A(M)=A(M)/(\mathrm{Im}\,\partial+\mathrm{Im}\,\bar\partial)\), for instance under a rescaling of the metric \(\rho\mapsto c\rho\) one can have \(\phi_{BC}(E;\rho,c\rho)\neq 0\) in \(\widetilde A(M)\) (weng1998relativebottchernsecondary pages 5-9). This establishes nontriviality in the differential-geometric Bott–Chern quotient, but the retrieved evidence does not connect this directly to nontriviality of \(x\) in an arithmetic Chow/Deligne–Beilinson group for a specific regular arithmetic surface over \(\mathrm{Spec}\,\mathbb{Z}\).

4) Change in Lefschetz operator \(\Delta L = \cup x\) and non-zeroness.

Formally, once \(x\in \widehat{CH}^1(X)\) (or the relevant arithmetic/Deligne–Beilinson cohomology group) is nontrivial, the induced change in the Lefschetz operator is exactly
\(\Delta L: y\mapsto y\cup x\), i.e. cup product with \(x\) (by definition of the Lefschetz/cup-product operator). Therefore \(\Delta L\) is nonzero as an operator whenever there exists some class \(y\) with \(y\cup x\neq 0\). The current evidence base does not supply a worked arithmetic-surface example where a metric change produces a proven nontrivial \(x=\widehat c_1(m_1)-\widehat c_1(m_0)\), so the non-zeroness of \(\Delta L\) in the precise sense requested cannot be concluded from the retrieved texts.

No statistical tests were performed: the task is mathematical/literature-based rather than data-driven. The key “test” analogous to a hypothesis test would be an explicit nonvanishing computation of \(x\) in arithmetic cohomology (e.g., by pairing with a known nonzero cycle or computing an arithmetic degree), which was not located for a pure metric change in the retrieved corpus.

To aid navigation, the following summary table captures the main formulas and the best available nonvanishing arithmetic-surface computation:

| Reference | Setting | Formula/Statement | Notes on nonvanishing |
| --- | --- | --- | --- |
| Weng 1998 | Metric change via \(\mathbf{P}^1\)-deformation | \(\phi_{BC}(E,\rho)=\int_{\mathbf{P}^1}[\log |z|^2]\,\phi(DE_2,D\rho_2)\); for two metrics on one bundle, \(dd^c\phi_{BC}(E;\rho_2,\rho_1)=\phi(E,\rho_2)-\phi(E,\rho_1)\) (weng1998relativebottchernsecondary pages 5-9, weng1998relativebottchernsecondary media 67105565) | Weng explicitly notes nonvanishing for a scale change: \(\phi_{BC}(E;\rho,c\rho)\neq 0\) in \(\widetilde A(M)\) (weng1998relativebottchernsecondary pages 5-9) |
| Kühn–Kramer–Burgos Gil 2005 | Transgression bundle for metric change | \(\widetilde\phi(E)=-(2\pi i)^{-1}\int_{\mathbf{P}^1}\phi(\operatorname{tr}_1(E))\log |t|^2\); for metrics \(h,h'\), one uses \(\operatorname{tr}_1(E,h,h')\), locally with metric matrix \(yy\,h+xx\,h'\); then \(d_D\widetilde\phi(E,h,h')=\phi(E,h')-\phi(E,h)\) (kuhn2005arithmeticcharacteristicclasses pages 56-60) | Gives the explicit integral/transgression formula for metric dependence, but no arithmetic-surface numerical example in the cited excerpt (kuhn2005arithmeticcharacteristicclasses pages 56-60) |
| Kühn–Kramer–Burgos Gil 2005 | Arithmetic Chow relation under metric change | \(\widehat\phi(E,h)=\widehat\phi(E,h')+a\big(\widetilde\phi(E,h',h)\big)\); with a smooth reference metric \(h_0\), \(\widehat\phi(E,h)=\widehat\phi(E,h_0)+a\big(\widetilde\phi(E,h,h_0)\big)\) (kuhn2005arithmeticcharacteristicclasses pages 5-7, kuhn2005arithmeticcharacteristicclasses pages 82-85) | This is the arithmetic-Chow mechanism behind \(\widehat c_1(m_1)-\widehat c_1(m_0)=a(BC(m_1,m_0))\); nonvanishing depends on whether the Bott–Chern class survives in the quotient/cohomology (kuhn2005arithmeticcharacteristicclasses pages 82-85) |
| Gillet–Soulé 2014, Thm. 1 | Arithmetic Chern character defect | \(\sum (-1)^i\widehat{ch}(\bar E_i)\cap [X]=\widehat{ch}^{\mathrm{fin}}(E_\bullet\cap [X])+a\big(\widetilde{ch}(\bar E_\bullet)\big)\), with \(dd^c\widetilde{ch}(\bar E_\bullet)=\sum (-1)^i ch(\bar E_{i,\mathbf C})\) (gillet2014onthearithmetic pages 1-4) | Shows explicitly how \((0,\eta)\)-classes arise through \(a\), separating archimedean Bott–Chern and finite-fibre terms (gillet2014onthearithmetic pages 1-4) |
| Gillet–Soulé 2014, Thm. 2 | Arithmetic surface with finite closed subscheme | \(f_*\big(\widehat c_2(\bar E_1)\cap [X]\big)=f_*\big(\widehat c_1(\bar E_0)\widehat c_1(\bar E_2)\cap [X]\big)-\int_{X(\mathbf C)}\widetilde c_2+\log \#\Gamma(\varphi,\mathcal O_\varphi)\) (gillet2014onthearithmetic pages 4-7) | Explicit arithmetic-surface formula with a manifestly nonzero term when \(\#\Gamma(\varphi,\mathcal O_\varphi)>1\) (gillet2014onthearithmetic pages 4-7) |
| Gillet–Soulé arithmetic Chow formalism | \((0,\eta)\)-classes and Green-current variation | The map \(a(\eta)\) is represented by \((0,\eta)\), with \(\omega\circ a(\eta)=dd^c\eta\); Green-current identities imply metric changes alter arithmetic classes by an \(a(\text{potential})\)-term (gillet2014onthearithmetic pages 1-4, gillet1990arithmeticintersectiontheory pages 29-32) | Supports the standard line-bundle heuristic \(\widehat c_1(L,h_1)-\widehat c_1(L,h_0)=a(\log(h_0/h_1))\), up to sign/normalization conventions (gillet2014onthearithmetic pages 1-4, gillet1990arithmeticintersectiontheory pages 29-32) |


*Table: This table compiles the key formulas linking Bott–Chern transgression, metric variation of arithmetic characteristic classes, and explicit arithmetic-surface nonvanishing terms. It is useful for isolating where metric dependence is proven and where concrete nonzero arithmetic contributions are exhibited.*
</explanation>
<discussion>
The literature retrieved here clearly contains explicit transgression formulas for Bott–Chern secondary characteristic classes associated to metric changes (integrals over \(\mathbb{P}^1\) with \(\log|\cdot|^2\) kernels) and explicit arithmetic “anomaly” identities showing that changing a metric changes an arithmetic characteristic class by an \(a\)-image of a Bott–Chern class (kuhn2005arithmeticcharacteristicclasses pages 56-60, weng1998relativebottchernsecondary pages 5-9, kuhn2005arithmeticcharacteristicclasses pages 82-85, weng1998relativebottchernsecondary media 67105565). This supports the general mechanism envisioned in the research objective.

The principal limitation is that, within the retrieved sources, I did not find a fully explicit worked example on a regular arithmetic surface over \(\mathrm{Spec}\,\mathbb{Z}\) (or a number ring) where one fixes an ample line bundle and exhibits two smooth hermitian metrics \(m_0,m_1\) such that the resulting class \(x=\widehat c_1(m_1)-\widehat c_1(m_0)\) is proven nonzero in arithmetic Chow/Deligne–Beilinson cohomology. The closest explicit nonvanishing computation found (Gillet–Soulé 2014, Thm. 2) concerns a situation with a finite subscheme \(\varphi\) and yields a nonzero term \(\log\#\Gamma(\varphi,\mathcal O_\varphi)\), reflecting a localized finite-fibre contribution in addition to an archimedean Bott–Chern component (gillet2014onthearithmetic pages 1-4, gillet2014onthearithmetic pages 4-7). This is valuable evidence of explicit nontrivial arithmetic classes on arithmetic surfaces, but it does not isolate nontriviality coming solely from a change of hermitian metric.

Finally, because nontriviality of \(x\) was not established, the requested assessment of whether \(\Delta L=\cup x\) is nonzero remains conditional.
</discussion>
<proposed-next-hypotheses>
1) For \(X=\mathbb{P}^1_{\mathbb{Z}}\) and \(L=\mathcal{O}(1)\), there exist two smooth hermitian metrics \(m_0,m_1\) such that \(x=\widehat c_1(L,m_1)-\widehat c_1(L,m_0)\) pairs nontrivially with the arithmetic cycle class of a rational point, i.e. \(\widehat{\deg}(x\cdot \widehat{[P]})\neq 0\).

2) On an arithmetic surface admitting a nontrivial space of harmonic \((1,1)\)-forms (e.g., a modular curve fibration or a surface with nontrivial archimedean cohomology), there exists a conformal change of a smooth hermitian metric on an ample line bundle for which the associated Bott–Chern secondary form has nonzero class in the relevant Deligne–Beilinson quotient, implying \(\Delta L\neq 0\) on some arithmetic cohomology group.
</proposed-next-hypotheses>
</output>

References

1. (weng1998relativebottchernsecondary pages 5-9): Lin Weng. Relative bott-chern secondary characteristic classes. Preprint, Jan 1998. URL: https://doi.org/10.48550/arxiv.math/9810117, doi:10.48550/arxiv.math/9810117. This article has 1 citations.

2. (weng1998relativebottchernsecondary media 67105565): Lin Weng. Relative bott-chern secondary characteristic classes. Preprint, Jan 1998. URL: https://doi.org/10.48550/arxiv.math/9810117, doi:10.48550/arxiv.math/9810117. This article has 1 citations.

3. (kuhn2005arithmeticcharacteristicclasses pages 56-60): Ulf Kühn, Jürg Kramer, and José I. Burgos Gil. Arithmetic characteristic classes of automorphic vector bundles. Documenta Mathematica, 10:619-716, Feb 2005. URL: https://doi.org/10.48550/arxiv.math/0502085, doi:10.48550/arxiv.math/0502085. This article has 67 citations and is from a domain leading peer-reviewed journal.

4. (kuhn2005arithmeticcharacteristicclasses pages 82-85): Ulf Kühn, Jürg Kramer, and José I. Burgos Gil. Arithmetic characteristic classes of automorphic vector bundles. Documenta Mathematica, 10:619-716, Feb 2005. URL: https://doi.org/10.48550/arxiv.math/0502085, doi:10.48550/arxiv.math/0502085. This article has 67 citations and is from a domain leading peer-reviewed journal.

5. (gillet2014onthearithmetic pages 4-7): H. Gillet and C. Soulé. On the arithmetic chern character. Annales de la Faculté des sciences de Toulouse : Mathématiques, 23:611-619, Sep 2014. URL: https://doi.org/10.5802/afst.1418, doi:10.5802/afst.1418. This article has 0 citations.

6. (gillet2014onthearithmetic pages 1-4): H. Gillet and C. Soulé. On the arithmetic chern character. Annales de la Faculté des sciences de Toulouse : Mathématiques, 23:611-619, Sep 2014. URL: https://doi.org/10.5802/afst.1418, doi:10.5802/afst.1418. This article has 0 citations.

7. (kuhn2005arithmeticcharacteristicclasses pages 5-7): Ulf Kühn, Jürg Kramer, and José I. Burgos Gil. Arithmetic characteristic classes of automorphic vector bundles. Documenta Mathematica, 10:619-716, Feb 2005. URL: https://doi.org/10.48550/arxiv.math/0502085, doi:10.48550/arxiv.math/0502085. This article has 67 citations and is from a domain leading peer-reviewed journal.

8. (gillet1990arithmeticintersectiontheory pages 29-32): Henri Gillet and Christophe Soulé. Arithmetic intersection theory. Publications Mathématiques de l'Institut des Hautes Études Scientifiques, 72:94-174, Dec 1990. URL: https://doi.org/10.1007/bf02699132, doi:10.1007/bf02699132. This article has 535 citations.