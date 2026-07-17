Question: 
Address the following research objective and research hypothesis:
<research-objective>Conduct a literature review of Arakelov motivic cohomology and related theories to find evidence for a tensor-product-like structure.
            1.  Examine definitions of Arakelov motivic cohomology `H^p_{M,ar}(X, ℚ(q))`. Search for decompositions, either formal or explicit, that separate the dependencies on the cohomological degree `p` and the Tate twist/Adams weight `q`.
            2.  Analyze the action of the Arakelov-Lefschetz operator `L = ∪ĉ₁`. Specifically, find the formula for its action on the indices `p` and `q`. Confirm that it maps `H^p_{M,ar}(X, ℚ(q)) → H^{p+2}_{M,ar}(X, ℚ(q+1))`, as suggested by finding f8.
            3.  Search for any operator `T` in this context whose action depends only on the weight `q`, for instance an operator `T_q` that acts on `H^p_{M,ar}(X, ℚ(q))` by multiplication by a function of `q`.
            4.  Synthesize these findings to assess if `H^p_{M,ar}(X, ℚ(q))` can be modeled as a space where an `sl₂`-triple acts on the `p`-graded component while another operator acts on the `q`-graded component, and document their commutation relations.</research-objective>
<research-hypothesis>The Arakelov motivic cohomology groups `H^p_{M,ar}(X, ℚ(q))` provide a natural realization of the "decoupled compatibility" model. The space decomposes into a geometric factor `H` indexed by cohomological degree `p` and an arithmetic/auxiliary factor `V` indexed by Adams weight `q`. The Lefschetz operator `L = ∪ĉ₁` acts on `p` (defining an `sl₂` on `H`), while the spectral operator `T` acts on `q` (on `V`), satisfying `[T,L]=0` trivially by factor separation and thus resolving the G2/G3 conflict.</research-hypothesis>

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
The retrieved literature supports a natural bigrading and compatible operators (Lefschetz-type degree shift and Adams weight actions) but does not establish a literal tensor-product factorization of \(H^p_{M,ar}(X,\mathbb Q(q))\) into independent \(p\)- and \(q\)-factors with a proven \(\mathfrak{sl}_2\)-triple acting only on the \(p\)-grading.
</conclusion>
<explanation>
| Theory / source | Definition of Arakelov motivic cohomology | Grading convention | Chern / Lefschetz-type operator | Adams / weight operator evidence | Key takeaway for tensor-product-like model | Evidence |
|---|---|---|---|---|---|---|
| Holmström–Scholbach, spectrum version | Arakelov motivic cohomology is represented by the homotopy fiber spectrum `HcB` of `HB -> HB ∧ HD`, and the groups are `bH^n(M,p)` in cohomological degree `n` and twist/weight `p` (equivalently `bH_n(M,p)=Hom(M,HcB(p)[n])` in the paper’s indexing). There is also a `BGL`-version `bH^n(M)` related to arithmetic `K`-theory. | The theory is intrinsically bigraded: one index is the cohomological shift `[n]`, the other is the Tate/Adams weight `(p)`. The notation `M{p}=M(p)[2p]` packages twist plus cohomological shift. | Deligne cohomology has a first Chern class `c1: Pic(X) -> H_D^2(X,1)` and projective bundle formula uses cup product with `c1(O(1))`; hence the Lefschetz-type action has bidegree `(+2,+1)`. Via the Arakelov Chern class and regulator comparison, the same degree bookkeeping carries to Arakelov motivic cohomology. | `HB` is built from Adams eigenspaces; `BGL_Q ≅ ⊕_p HB(p)[2p]`. Arakelov groups decompose rationally by weight, and the Arakelov Chern character gives `bH^n(M)⊗Q ≅ ⊕_p bH^{n+2p}(M,p)`. | Strong evidence for a bigraded structure with separate cohomological and weight indices, but not for a literal tensor factorization `H ⊗ V`. | (holmstrom2010arakelovmotiviccohomology pages 1-3, holmstrom2010arakelovmotiviccohomology pages 3-6, holmstrom2010arakelovmotiviccohomology pages 12-16, holmstrom2010arakelovmotiviccohomology pages 19-22) |
| Goncharov, complex version | The weight-`n` Arakelov motivic complex is `Γ_A^•(X;n) := Cone(Z^•(X;n) -> C_D^•(X(C);n))[-1]` or its real or number-field variants, and the weight-`n` Arakelov motivic cohomology is the cohomology of this complex. | Here the primary grading is by cochain degree in the cone complex, while the second index is the fixed weight `n`. This is a family of complexes indexed by weight, rather than a single explicitly bigraded object. | The Deligne target is the weight-`n` Deligne complex; the construction is regulator-based. The excerpt does not define an explicit Lefschetz operator on the Arakelov cone, but the Deligne side carries the usual Chern-class formalism in weight `1`, compatible with the general `(+2,+1)` shift pattern. | Beilinson’s motivic cohomology is recalled as `H_M^i(X,Q(n)) = K_{2n-i}^{(n)}(X)_Q`, i.e. the weight-`n` eigenspace for Adams operations. This supports a weight grading indexed by Adams eigenvalue. | Good evidence for a weight-indexed family of theories, but weaker evidence for a decoupled `(p,q)` tensor product than in the spectrum formalism. | (goncharov2005polylogarithmsregulatorsand pages 1-4) |
| Deligne cohomology input used by Holmström–Scholbach | Deligne cohomology is represented by a spectrum `HD`; one has `H_D^n(X,p)` represented by the `p`-th level or twist of this spectrum. | The grading is explicit: cohomological degree `n` and weight or twist `p`. In regulator formulas from `K_n`, the target is `⊕_p H_D^{2p-n}(X,p)`, making the `2p` shift visible. | There is a functorial first Chern class `c1: Pic(X) -> H_D^2(X,1)`, and projective bundle formula uses cup product with `c1(O(1))`. Thus cup with `c1` maps `H_D^n(X,p) -> H_D^{n+2}(X,p+1)`. This is the clearest direct confirmation of the proposed `(+2,+1)` rule. | No separate scalar operator `T_q` is introduced here; the evidence is structural through the twist index `p`. | Confirms the Lefschetz-degree shift exactly, but only at the Deligne or regulator side, not as a full `sl2` theorem for Arakelov motivic cohomology. | (holmstrom2010arakelovmotiviccohomology pages 12-16, scholbach2017specialvaluesof pages 10-13, scholbach2012arakelovmotiviccohomology pages 7-11) |
| Adams operations in Scholbach II | The regulator and arithmetic `K`-theory comparison are compatible with Adams operations. Weight pieces are defined by eigenspaces. | Weight `p` is the Adams or `γ`-filtration index. The decomposition `BGL_Q ≅ ⊕_p HB(p)[2p]` and `⊕_p H_D^{2p-n}(X,p)` separates weight from cohomological degree formally. | No explicit arithmetic Lefschetz operator `ĉ1` is defined in the cited excerpt, but cup product constructions are used, and the first Chern class on the Deligne side provides the standard `(+2,+1)` shift. | Explicitly, on the Deligne side `Ψ^k = ⊕_p (k^p · id)` on `⊕_p D(p)`, and arithmetic `K`-theory eigenspaces are `bK_n(X)^{(p)}_Q = {x | Ψ^k(x)=k^p x}`. This is the closest available candidate to an operator depending only on weight. | There is evidence for a weight-only semisimple action via Adams operations, but not for a canonically defined infinitesimal operator `T` acting only by a scalar function of `q` on Arakelov motivic cohomology itself. | (scholbach2012arakelovmotiviccohomology pages 14-17, scholbach2012arakelovmotiviccohomology pages 4-7, scholbach2012arakelovmotiviccohomology pages 11-14) |
| Overall assessment relative to the hypothesis | The literature supports a bigraded formalism and compatible regulator and Chern-class operations, but not an explicit decomposition `H^p_{M,ar}(X,Q(q)) ≅ H_p ⊗ V_q`. | `p` or `n` and `q` or weight are formally separable in notation and in Adams-eigenspace decompositions, but not as an established tensor product of spaces. | The Lefschetz-type operator is well supported to shift cohomological degree and weight by `(+2,+1)` through cup product with `c1` or `ĉ1`-type classes. | Adams operations provide a weight-only diagonalizable action, with `Ψ^k` acting as `k^q` on weight `q`, suggesting a spectral-variable analogue; however, no canonical operator `T_q` or full commuting `sl2 × spectral` package is explicitly constructed in the cited Arakelov motivic cohomology literature. | The hypothesis is partially supported at the level of grading bookkeeping and commuting semisimple weight actions, but not established as a literal decoupled tensor-product model with a proven `sl2` on the cohomological factor and an independent scalar operator on the weight factor. | (holmstrom2010arakelovmotiviccohomology pages 1-3, holmstrom2010arakelovmotiviccohomology pages 12-16, holmstrom2010arakelovmotiviccohomology pages 19-22, scholbach2012arakelovmotiviccohomology pages 14-17, goncharov2005polylogarithmsregulatorsand pages 1-4) |


*Table: This table summarizes the main definitions, gradings, Chern or Lefschetz degree shifts, and Adams-weight actions found in the cited literature on Arakelov motivic cohomology and related theories. It is useful for assessing whether the theory supports a decoupled cohomological-versus-weight model and which parts of that model are directly evidenced.*

1) Definitions and (p,q)-style grading (degree vs. weight).

Holmström–Scholbach define Arakelov motivic cohomology by a spectrum \(\widehat H\) (denoted \(H^c_B\) in their introduction) as the homotopy fiber of \(HB\to HB\wedge HD\), with groups
\[
\widehat H^n(M,p)\;:=\;\operatorname{Hom}_{\mathbf{SH}(S)_\mathbb Q}(M,\,H^c_B(p)[n]),
\]
so the theory is inherently bigraded by the cohomological shift \([n]\) and the Tate/Adams weight (twist) \((p)\). (holmstrom2010arakelovmotiviccohomology pages 1-3)

The same sources emphasize that the input Beilinson spectrum \(HB\) encodes Adams eigenspaces and that rational algebraic \(K\)-theory splits into weight pieces, e.g. \(BGL_\mathbb Q\simeq\bigoplus_p HB(p)[2p]\); this makes the separation between cohomological degree and motivic weight formal at the spectrum level. (holmstrom2010arakelovmotiviccohomology pages 3-6)

Independently, Goncharov defines a weight-\(n\) Arakelov motivic complex \(\Gamma_A^\bullet(X;n)=\mathrm{Cone}(Z^\bullet(X;n)\to C_D^\bullet(X(\mathbb C);n))[-1]\) and defines “weight \(n\) Arakelov motivic cohomology” as the cohomology of this cone. This provides a family of theories indexed by weight, but in that cone construction the weight is fixed and the main grading is the cochain degree. (goncharov2005polylogarithmsregulatorsand pages 1-4)

Evidence for a decomposition that separates dependence on degree and weight is therefore strongest in the spectrum-based approach: the ubiquitous notation \(M\{p\}=M(p)[2p]\) and splittings like \(BGL_\mathbb Q\simeq\bigoplus_p HB(p)[2p]\) separate “weight bookkeeping” (the index \(p\)) from homological degree shifts (the \([2p]\) offset). (holmstrom2010arakelovmotiviccohomology pages 3-6, scholbach2012arakelovmotiviccohomology pages 4-7)

2) Lefschetz / Arakelov–Lefschetz operator action on indices.

A direct, explicit index-shift statement is available for Deligne cohomology, which is a defining ingredient in Arakelov motivic cohomology. Holmström–Scholbach record a functorial first Chern class
\(c_1: \mathrm{Pic}(X)\to H_D^2(X,1)\), and that Deligne cohomology is a graded-commutative ring; combining this with the projective bundle formula (built from cup product with \(c_1(\mathcal O(1))\)) yields the standard Lefschetz-type shift
\[
L=\cup c_1:\; H_D^n(X,p)\to H_D^{n+2}(X,p+1).
\]
(holmstrom2010arakelovmotiviccohomology pages 12-16)

Scholbach’s Arakelov motivic cohomology II further makes the same bidegree bookkeeping visible in the spectrum bonding maps: in the construction of the Chern character map \(\mathrm{ch}:BGL\to\bigoplus_p HD(p)[2p]\), the bonding map \(c^*\) is identified with the first Chern class \(c_1(\mathcal O(1))\in H_D^2(\mathbb P^1,1)\), again reflecting the \((+2,+1)\) shift when cupping with \(c_1\). (scholbach2012arakelovmotiviccohomology pages 7-11)

Within the retrieved Arakelov motivic cohomology texts, however, we did not find an explicitly named “Arakelov–Lefschetz operator” \(\hat c_1\) together with a theorem asserting hard Lefschetz/primitive decomposition or an explicit \(\mathfrak{sl}_2\)-triple acting on \(\widehat H^*(X,*)\); the evidence is instead that the Arakelov theory inherits cup products and degree bookkeeping from its motivic and Deligne constituents. (holmstrom2010arakelovmotiviccohomology pages 1-3, holmstrom2010arakelovmotiviccohomology pages 12-16)

3) Weight-only operator T: Adams operations as the closest supported candidate.

Scholbach explicitly constructs Adams operations \(\Psi^k\) on arithmetic/Arakelov \(\widehat K\)-groups with \(\mathbb Q\)-coefficients and describes their action on the Deligne complex side as purely weight-dependent scalars:
\[
\Psi_D^k:\; D^*=\bigoplus_p D^*(p)\to\bigoplus_p D^*(p),\qquad \Psi_D^k=\bigoplus_p (k^p\,\mathrm{id}).
\]
He defines eigenspaces \(\widehat K_n(X)(p)_\mathbb Q=\{x\mid \Psi^k(x)=k^p x\}\) and proves compatibility with Arakelov motivic cohomology so that weight-\(p\) components can be identified as \(\widehat K_n(X)(p)_\mathbb Q\cong \widehat H^{2p-n}(X,p)\). (scholbach2012arakelovmotiviccohomology pages 14-17, scholbach2012arakelovmotiviccohomology pages 17-21)

This provides a family of commuting operators depending only on the weight index (and not on cohomological degree). It is therefore the strongest “\(T_q\)-like” structure found in the retrieved sources, although it is a family \(\{\Psi^k\}_{k\ge 1}\) rather than a single infinitesimal generator \(T\). (scholbach2012arakelovmotiviccohomology pages 14-17)

4) Synthesis: assessment of the decoupled compatibility model and commutation relations.

> Cup product with the first Chern class gives the confirmed Lefschetz-type shift on Deligne cohomology: if \(L=\cup c_1\), then \(L: H_D^n(X,p) \to H_D^{n+2}(X,p+1)\); this follows from the functorial class \(c_1: \mathrm{Pic}(X)\to H_D^2(X,1)\), the projective bundle formula, and the spectrum bonding map identified with \(c_1(\mathcal O(1))\). (holmstrom2010arakelovmotiviccohomology pages 12-16, scholbach2012arakelovmotiviccohomology pages 7-11)
>
> Adams operations provide the clearest weight-only operators in the retrieved Arakelov-motivic literature: on the Deligne complex \(D^*=\bigoplus_p D^*(p)\), \(\Psi^k_D=\bigoplus_p (k^p\,\mathrm{id})\), and arithmetic/Arakelov eigenspaces are defined by \(\widehat K_n(X)^{(p)}_\mathbf Q=\{x\mid \Psi^k(x)=k^p x\}\), with canonical identification of the \(p\)-piece with \(\widehat H^{2p-n}(X,p)\). (scholbach2012arakelovmotiviccohomology pages 14-17, scholbach2012arakelovmotiviccohomology pages 17-21)
>
> A natural expected compatibility is \(\Psi^k(Lx)=k\,L(\Psi^k x)\) when \(L\) is cup product with a weight-1 class \(c_1\); this matches the degree bookkeeping \((n,p)\mapsto(n+2,p+1)\) and the Adams eigenvalue \(k^p\) on weight \(p\), but this precise commutation formula was not explicitly stated in the retrieved Arakelov motivic cohomology texts. (holmstrom2010arakelovmotiviccohomology pages 12-16, scholbach2012arakelovmotiviccohomology pages 14-17)
>
> No explicit hard-Lefschetz theorem, primitive decomposition, or \(\mathfrak{sl}_2\)-triple was found in the retrieved Holmström–Scholbach / Scholbach Arakelov motivic cohomology sources; the closest positive evidence is the abstract bigraded Lefschetz-module formalism of Consani–Marcolli, where two commuting Lefschetz operators generate an \(SL_2(\mathbf R)\times SL_2(\mathbf R)\)-action, but this is not presented there as a theorem about Arakelov motivic cohomology \(\widehat H^n(X,p)\) itself. (consani2004noncommutativegeometrydynamics pages 9-11, consani2004noncommutativegeometrydynamics pages 23-25, scholbach2012arakelovmotiviccohomology pages 21-24)


*Blockquote: This blockquote summarizes the operator behavior most directly supported by the retrieved literature: the Lefschetz-type degree shift from cup product with c1, the weight-only Adams action, and the limits of the evidence for explicit commutation and sl2-structure in Arakelov motivic cohomology.*

The available evidence supports a decoupling at the level of indexing conventions and semisimple actions:

• Bigrading: Arakelov motivic cohomology (in the spectrum approach) is naturally bigraded by cohomological degree and Tate/Adams weight, and the rational splittings \(BGL_\mathbb Q\simeq\oplus_p HB(p)[2p]\) formally separate degree shifts from weight. (holmstrom2010arakelovmotiviccohomology pages 1-3, holmstrom2010arakelovmotiviccohomology pages 3-6)

• Lefschetz shift: cup product with a Chern class of weight 1 shifts (degree,weight) by \((+2,+1)\) at least on the Deligne side, and this same class controls bonding maps in the spectrum constructions used to define Arakelov motivic cohomology and regulators. (holmstrom2010arakelovmotiviccohomology pages 12-16, scholbach2012arakelovmotiviccohomology pages 7-11)

• Weight-only operator: Adams operations act by the scalar \(k^p\) on the weight-\(p\) summand, providing a clean weight-only operator family. (scholbach2012arakelovmotiviccohomology pages 14-17)

However, the specific strong form of the research hypothesis—an actual tensor-product factorization \(\widehat H^n(X,p) \cong H_n\otimes V_p\) (or similarly for \(H^p_{M,ar}(X,\mathbb Q(q))\)) together with a proven \(\mathfrak{sl}_2\)-triple acting only on the degree-graded factor—was not found in these sources. Moreover, while the degree bookkeeping strongly suggests the expected compatibility \(\Psi^k\circ L = k\,L\circ \Psi^k\) for \(L=\cup c_1\) (since \(c_1\) has weight 1 and \(\Psi^k\) acts by \(k^p\) on weight \(p\)), this explicit commutation formula is not stated in the retrieved Arakelov motivic cohomology excerpts, so it cannot be claimed as established here. (holmstrom2010arakelovmotiviccohomology pages 12-16, scholbach2012arakelovmotiviccohomology pages 14-17)

Finally, while Consani–Marcolli exhibit an \(SL_2(\mathbb R)\times SL_2(\mathbb R)\) action on certain bigraded Lefschetz modules and discuss an additional operator \(\Phi\) with controlled commutators, this is a different (noncommutative/dynamical) Arakelov-related framework and is not presented as a theorem about Holmström–Scholbach Arakelov motivic cohomology groups. (consani2004noncommutativegeometrydynamics pages 9-11, consani2004noncommutativegeometrydynamics pages 23-25)

Statistical tests.

No statistical hypothesis tests are applicable: the objective is a conceptual literature review in pure mathematics. Accordingly, “evidence” is assessed by presence/absence of explicit definitions, theorems, and formulas in the retrieved sources.
</explanation>
<discussion>
Limitations of the evidence base.

• Coverage: Only a subset of Holmström–Scholbach I and Scholbach II was retrieved and searched (selected page ranges). It is possible that explicit hard Lefschetz / \(\mathfrak{sl}_2\) statements (if they exist) occur elsewhere in those papers or in follow-up work (e.g., discussions of Arakelov intersection pairings, projective bundle and hard Lefschetz analogues, or conjectural statements).

• Lefschetz operator in Arakelov motivic cohomology vs. Deligne cohomology: The \((+2,+1)\) shift is explicit for Deligne cohomology and for bonding maps used to build the Chern character/regulator at the spectrum level. Translating this to a named “Arakelov–Lefschetz” operator \(\cup \hat c_1\) acting internally on \(\widehat H^*(X,*)\) would require an explicit construction of \(\hat c_1\in \widehat H^2(X,1)\) and verification that its cup product action is the intended operator; that explicit internal formulation was not located in the retrieved excerpts.

• Weight-only operator: Adams operations give a strong weight-only semisimple action, but the hypothesis’s “spectral operator \(T\)” is closer in spirit to an infinitesimal generator (e.g., a logarithm of Adams operations or a grading operator). The retrieved sources do not define such an operator on Arakelov motivic cohomology; thus only a weaker version of the hypothesis (“there exist commuting weight-only endomorphisms”) is supported.

Implications.

The bigrading and the existence of (i) Lefschetz-type degree shifts via Chern classes and (ii) independent weight-only Adams actions mean that a “decoupled compatibility” picture is plausible at the level of formal gradings and semisimple symmetries. But the stronger claim of an actual factorization and a separate \(\mathfrak{sl}_2\) acting only on the degree-graded component remains unproven by the retrieved evidence and should be treated as conjectural or as a modeling Ansatz rather than a documented theorem.
</discussion>
<proposed-next-hypotheses>
1) (Hard Lefschetz / \(\mathfrak{sl}_2\) hypothesis for Arakelov motivic cohomology.) For regular, projective \(X\) over an arithmetic base equipped with an ample hermitian line bundle \(\bar L\), the class \(\hat c_1(\bar L)\in \widehat H^2_{M,ar}(X,\mathbb Q(1))\) induces a hard-Lefschetz isomorphism on Arakelov motivic cohomology weight pieces, and extends to an \(\mathfrak{sl}_2\)-action on \(\bigoplus_{n,p}\widehat H^n(X,p)\).

2) (Spectral generator hypothesis from Adams operations.) There exists a canonically defined endomorphism \(T\) of \(\bigoplus_{n,p}\widehat H^n(X,p)\) such that on the weight-\(p\) summand \(T\) acts by multiplication by \(p\), and the Adams operations satisfy \(\Psi^k = k^T\) (or \(\log \Psi^k = (\log k)\,T\)); moreover \([T,L]=L\) (reflecting that \(L\) raises weight by 1).
</proposed-next-hypotheses>
</output>

References

1. (holmstrom2010arakelovmotiviccohomology pages 1-3): Andreas Holmstrom and Jakob Scholbach. Arakelov motivic cohomology i. Text, Jan 2010. URL: https://doi.org/10.48550/arxiv.1012.2523, doi:10.48550/arxiv.1012.2523. This article has 25 citations and is from a peer-reviewed journal.

2. (holmstrom2010arakelovmotiviccohomology pages 3-6): Andreas Holmstrom and Jakob Scholbach. Arakelov motivic cohomology i. Text, Jan 2010. URL: https://doi.org/10.48550/arxiv.1012.2523, doi:10.48550/arxiv.1012.2523. This article has 25 citations and is from a peer-reviewed journal.

3. (holmstrom2010arakelovmotiviccohomology pages 12-16): Andreas Holmstrom and Jakob Scholbach. Arakelov motivic cohomology i. Text, Jan 2010. URL: https://doi.org/10.48550/arxiv.1012.2523, doi:10.48550/arxiv.1012.2523. This article has 25 citations and is from a peer-reviewed journal.

4. (holmstrom2010arakelovmotiviccohomology pages 19-22): Andreas Holmstrom and Jakob Scholbach. Arakelov motivic cohomology i. Text, Jan 2010. URL: https://doi.org/10.48550/arxiv.1012.2523, doi:10.48550/arxiv.1012.2523. This article has 25 citations and is from a peer-reviewed journal.

5. (goncharov2005polylogarithmsregulatorsand pages 1-4): A. Goncharov. Polylogarithms, regulators, and arakelov motivic complexes. Journal of the American Mathematical Society, 18:1-60, Nov 2005. URL: https://doi.org/10.1090/s0894-0347-04-00472-2, doi:10.1090/s0894-0347-04-00472-2. This article has 76 citations and is from a highest quality peer-reviewed journal.

6. (scholbach2017specialvaluesof pages 10-13): J Scholbach. Special -values of geometric motives. Unknown journal, 2017.

7. (scholbach2012arakelovmotiviccohomology pages 7-11): Jakob Scholbach. Arakelov motivic cohomology ii. Preprint, Jan 2012. URL: https://doi.org/10.48550/arxiv.1205.3890, doi:10.48550/arxiv.1205.3890. This article has 11 citations.

8. (scholbach2012arakelovmotiviccohomology pages 14-17): Jakob Scholbach. Arakelov motivic cohomology ii. Preprint, Jan 2012. URL: https://doi.org/10.48550/arxiv.1205.3890, doi:10.48550/arxiv.1205.3890. This article has 11 citations.

9. (scholbach2012arakelovmotiviccohomology pages 4-7): Jakob Scholbach. Arakelov motivic cohomology ii. Preprint, Jan 2012. URL: https://doi.org/10.48550/arxiv.1205.3890, doi:10.48550/arxiv.1205.3890. This article has 11 citations.

10. (scholbach2012arakelovmotiviccohomology pages 11-14): Jakob Scholbach. Arakelov motivic cohomology ii. Preprint, Jan 2012. URL: https://doi.org/10.48550/arxiv.1205.3890, doi:10.48550/arxiv.1205.3890. This article has 11 citations.

11. (scholbach2012arakelovmotiviccohomology pages 17-21): Jakob Scholbach. Arakelov motivic cohomology ii. Preprint, Jan 2012. URL: https://doi.org/10.48550/arxiv.1205.3890, doi:10.48550/arxiv.1205.3890. This article has 11 citations.

12. (consani2004noncommutativegeometrydynamics pages 9-11): Caterina Consani and Matilde Marcolli. Noncommutative geometry, dynamics, and ∞-adic arakelov geometry. Aug 2004. URL: https://doi.org/10.1007/s00029-004-0369-3, doi:10.1007/s00029-004-0369-3. This article has 65 citations.

13. (consani2004noncommutativegeometrydynamics pages 23-25): Caterina Consani and Matilde Marcolli. Noncommutative geometry, dynamics, and ∞-adic arakelov geometry. Aug 2004. URL: https://doi.org/10.1007/s00029-004-0369-3, doi:10.1007/s00029-004-0369-3. This article has 65 citations.

14. (scholbach2012arakelovmotiviccohomology pages 21-24): Jakob Scholbach. Arakelov motivic cohomology ii. Preprint, Jan 2012. URL: https://doi.org/10.48550/arxiv.1205.3890, doi:10.48550/arxiv.1205.3890. This article has 11 citations.