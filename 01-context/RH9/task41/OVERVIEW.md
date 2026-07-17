Question: 
Address the following research objective and research hypothesis:
<research-objective>Perform a targeted search of the literature to locate the proof of adjointness for the `sl₂` operators on arithmetic Chow groups of abelian varieties.
            1.  Prioritize locating and analyzing Künnemann's 1994 paper in Mathematische Annalen, "Arakelov Chow groups of abelian schemes..." which is cited as foundational for these constructions.
            2.  Search this paper and related works by Künnemann, Bachmat, and Bost for a theorem or calculation demonstrating that the Pontryagin convolution operator `A` and the intersection operator `L` are adjoints with respect to the defined height pairing.
            3.  Document the precise statement of the theorem, the definition of the pairing, and the key steps in the proof.
            4.  If the explicit adjointness proof is not found, document any related results, such as self-adjointness of the full Lefschetz operator `L+A`, which would imply the desired relation up to signs and normalizations.</research-objective>
<research-hypothesis>In the framework of arithmetic Chow groups for abelian varieties, the Fourier-Mukai-based lowering operator `A` is the formal adjoint of the Lefschetz raising operator `L` (cup-product with a polarization) with respect to the Gillet-Soulé/Künnemann height pairing. A proof of this adjointness relation, `⟨La, b⟩ = ⟨a, Ab⟩`, exists in the literature, likely in Künnemann's foundational papers.</research-hypothesis>

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
The targeted adjointness identity ⟨La,b⟩=⟨a,Ab⟩ for the specific `sl₂` raising/lowering operators (L = cup with a polarization, A = Pontryagin/Fourier–Mukai lowering) is not stated verbatim in the accessible texts, but Künnemann proves a general theorem that any correspondence and its transpose are adjoint for the height pairing; this yields the desired conclusion once L and A are identified with transpose-related correspondences as in Künnemann’s (unobtainable here) 1994 Math. Ann. construction.
</conclusion>
<explanation>
1. Target object: the height pairing

Künnemann’s later work gives a canonical “height pairing” on homologically trivial Chow groups of an abelian variety over a number field, of the form

⟨·,·⟩_{A_K}: CH^p(A_K)_0 ⊗ CH^{g+1-p}(A_K)_0 → ℝ,

generalizing the Néron–Tate height pairing (stated explicitly as (1) in his 2001 paper, with precise construction via regular models and arithmetic intersection theory of Gillet–Soulé). (kunnemann2001heightpairingsfor pages 1-3, kunnemann2001heightpairingsfor pages 3-7)

Although the research objective asks specifically for arithmetic Chow groups (Arakelov Chow groups) and `sl₂` operators, the fundamental adjointness mechanism for operators induced by correspondences is already explicit at the level of this height pairing.

2. Explicit adjointness theorem available in the literature (correspondences)

In Künnemann (1996), adjointness is proved in two steps:

(i) Model-level arithmetic intersection adjointness (Lemma 4.1).
For a correspondence α between regular models (maps f,g in the paper’s notation) the arithmetic intersection pairings satisfy an adjointness relation between α and its transpose tα:

⟨ y, (tα)_{CH}(v) ⟩_f = ⟨ v, α_{CH}(y) ⟩_g.

This is stated as Lemma 4.1. (kunnemann1996higherpicardvarieties pages 4-8, kunnemann1996higherpicardvarieties media 818168c7)

(ii) Generic-fiber height pairing adjointness (formula (18)).
Passing to the induced height pairing on varieties over a number field, Künnemann states the key identity:

⟨ x, α_{CH}(y) ⟩_{X_K} = ⟨ (tα)_{CH}(x), y ⟩_{Y_K}.

This is formula (18) in the paper. (kunnemann1996higherpicardvarieties pages 4-8, kunnemann1996higherpicardvarieties media e9ef9238)

These two statements are already a complete “proof of adjointness” framework: if an operator is defined as action of a correspondence, its adjoint (w.r.t. ⟨·,·⟩) is the action of the transpose correspondence.

3. How this connects to `sl₂` operators L and A on (arithmetic) Chow groups of abelian varieties

The research hypothesis concerns operators in an `sl₂` package on arithmetic Chow groups of abelian varieties:

• L: raising operator given by intersection/cup-product with a polarization class.
• A: lowering operator defined via Pontryagin convolution / arithmetic Fourier transform (Fourier–Mukai type).

The accessible sources do not contain (verbatim) a theorem labelled “A is the adjoint of L”, i.e. ⟨La,b⟩ = ⟨a,Ab⟩ with L and A named as such.

However, Künnemann (1995) explicitly indicates that the “arithmetic Fourier transform” (introduced in his foundational 1994 Math. Ann. paper and referenced as [10]) is related to the Lefschetz operator via a specific formula (labelled (36) there), and also notes orthogonality properties of decompositions with respect to the arithmetic intersection product. This is strong indirect evidence that the 1994 construction packages Fourier/Pontryagin and Lefschetz operators in the way needed to identify A as a transpose/adjoint of L (up to signs and normalizations). (kunnemann1995someremarkson pages 13-19, kunnemann1995someremarksona pages 19-21)

Therefore, given Künnemann’s general adjointness theorem for correspondences (formula (18)), proving ⟨La,b⟩ = ⟨a,Ab⟩ reduces to verifying that:

• L is induced by some correspondence α_L (typically “multiplication by a polarization” corresponds to intersecting with c1(L), i.e. a class on A×A), and
• A is induced by the transpose correspondence tα_L after conjugation by Fourier transform, or more directly by a correspondence α_A satisfying α_A = tα_L in the relevant correspondence category used to define the operators.

This “reduction to transpose” is exactly what (18) provides.

4. Auxiliary structural evidence: expression via higher Picard varieties

Künnemann (1996) also provides an interpretation of the height pairing in terms of Néron–Tate pairings on higher Picard varieties (Theorem 8.2, equation (23)), and compatibility of correspondences with the canonical duality isogenies λ (equation (22)). (kunnemann1996higherpicardvarieties pages 8-11)

Conceptually, (22)+(23) explain why transposition corresponds to taking adjoints with respect to a polarization (Néron–Tate pairing). This is precisely the structure one expects behind an `sl₂` adjointness relation (raising/lowering operators adjoint under a polarization-defined pairing).

5. Statistical tests performed

No statistical tests were applicable. This is a pure-mathematics literature search and evidence extraction task; the “tests” are logically checking whether the literature contains (a) an explicit theorem statement and (b) enough structure to infer the desired adjointness relation. The key positive result is the explicit general correspondence-adjointness identity (18). (kunnemann1996higherpicardvarieties media e9ef9238)
</explanation>
<discussion>
Limitations and shortfalls:

• The foundational source requested—Künnemann (1994), Mathematische Annalen 300:365–392, “Arakelov Chow groups of abelian schemes, arithmetic Fourier transform, and analogues of the standard conjectures of Lefschetz type” (doi:10.1007/BF01450492)—was identified but could not be retrieved with the available tools (listed as unobtainable). Consequently, I could not verify whether it contains an explicit theorem phrased exactly as ⟨La,b⟩=⟨a,Ab⟩ for the specific operators named L and A.

• The accessible Künnemann sources prove something slightly more general but also more abstract: adjointness for arbitrary correspondences and their transposes with respect to the (arithmetic) height pairing (Lemma 4.1 and formula (18)). (kunnemann1996higherpicardvarieties media 818168c7, kunnemann1996higherpicardvarieties media e9ef9238)

• Bridging from that general result to the specific `sl₂` operators requires checking that the Fourier/Pontryagin lowering operator A is indeed the transpose (or conjugate-transpose under Fourier transform) of the Lefschetz correspondence defining L, with the correct sign and normalization conventions. Künnemann (1995) signals that such explicit operator relations exist (formula (36) relating arithmetic Fourier transform to Lefschetz), but without the 1994 paper text we cannot document the exact displayed identity or the normalization. (kunnemann1995someremarkson pages 13-19)

Contextualization:

• In the standard theory of algebraic cycles on abelian varieties, the `sl₂`-action is implemented by correspondences; the adjointness of raising and lowering operators is typically a manifestation of “transpose correspondence = adjoint operator” under a polarization pairing. Künnemann’s formula (18) provides exactly this principle in the arithmetic/height-pairing setting. (kunnemann1996higherpicardvarieties media e9ef9238)

• Thus, while an operator-specific statement is missing from the accessible corpus, the evidence strongly supports the research hypothesis as “true modulo identification of A with the transpose-correspondence operator”.
</discussion>
<proposed-next-hypotheses>
1) In Künnemann (1994) Math. Ann. 300:365–392, there is an explicit displayed identity showing that the arithmetic Fourier transform conjugates the Lefschetz operator L to a Pontryagin/Fourier lowering operator A (i.e., an arithmetic-cycle analogue of F L F^{-1} = ±A), and the paper states (or immediately implies) ⟨La,b⟩=⟨a,Ab⟩ with respect to Künnemann’s height pairing.

2) After fixing Künnemann’s normalizations of the arithmetic Fourier transform and the polarization class, the composite operator (L + A) is self-adjoint with respect to the height pairing (or equivalently, L and A are mutual adjoints), and this self-adjointness is stated explicitly either in §7–§9 of Künnemann (1994) or in a paper by Bost–Gillet–Soulé/Künnemann cited therein.
</proposed-next-hypotheses>
</output>

References

1. (kunnemann2001heightpairingsfor pages 1-3): Klaus Künnemann. Height pairings for algebraic cycles on abelian varieties. Annales Scientifiques De L Ecole Normale Superieure, 34:503-523, Jul 2001. URL: https://doi.org/10.1016/s0012-9593(01)01068-0, doi:10.1016/s0012-9593(01)01068-0. This article has 25 citations and is from a highest quality peer-reviewed journal.

2. (kunnemann2001heightpairingsfor pages 3-7): Klaus Künnemann. Height pairings for algebraic cycles on abelian varieties. Annales Scientifiques De L Ecole Normale Superieure, 34:503-523, Jul 2001. URL: https://doi.org/10.1016/s0012-9593(01)01068-0, doi:10.1016/s0012-9593(01)01068-0. This article has 25 citations and is from a highest quality peer-reviewed journal.

3. (kunnemann1996higherpicardvarieties pages 4-8): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.

4. (kunnemann1996higherpicardvarieties media 818168c7): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.

5. (kunnemann1996higherpicardvarieties media e9ef9238): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.

6. (kunnemann1995someremarkson pages 13-19): K Künnemann. Some remarks on the arithmetic hodge index conjecture. Unknown journal, 1995.

7. (kunnemann1995someremarksona pages 19-21): K Künnemann. Some remarks on the arithmetic hodge index conjecture. Unknown journal, 1995.

8. (kunnemann1996higherpicardvarieties pages 8-11): Klaus Künnemann. Higher picard varieties and the height pairing. American Journal of Mathematics, 118:781-797, Aug 1996. URL: https://doi.org/10.1353/ajm.1996.0033, doi:10.1353/ajm.1996.0033. This article has 23 citations and is from a highest quality peer-reviewed journal.