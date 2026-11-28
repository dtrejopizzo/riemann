# Conceptual pattern and research programme — analysis of connections

28 November 2026. Internal sources read: Paper 57, in particular the introduction, the §§ on lattices/three theorems and the Acknowledgement; statements and assembly of 46; GLOBAL-ASSEMBLY and the V2 supplements. This report studies the architecture and its possibilities of generalisation. It does not certify the proof again, nor does it establish bibliographic priority by absence of antecedents. The old objections concerning the exchange of 53 are not premises of this analysis.

## 1. The pattern that deserves study

The specific bridge is **to convert excess divisibility of theta coefficients into a restriction on a sum over primes, passing through the covolume of automorphic lattices of almost full rank**. The structure combines three proofs of different nature:

1. Construction of short vectors in all the complex embeddings, after dividing by prime factors guaranteed by the CM arithmetic.
2. A second moment that prevents those vectors from living only in a small part of the space.
3. A lower bound for the covolume, obtained from L-values, congruences, twists chosen prime by prime and the product formula.

The comparison cancels the same main term computed in two ways. The remainder is an explicit sum over primes. The candidate novelty lies in the quantitative compatibility of those three operations, not in the separate existence of theta, Frobenius, products of norms or determinants.

The long chain of lifts plays the role of a multiplicity: the benefit sought is multiplied by m. But this is of use only if the cost added by each lift cancels or remains under control. An undetermined factor K at each step can introduce m log K, which after division by m leaves an error that does not improve. This is the conceptual reason for demanding exact constants and uniformity: they allow the length to be an effective gain and not merely a complication of the object.

The intellectual origin of this analogy is already documented. The [note of Alpoge, pp. 1 and 4](https://alpo.ge/remark.pdf) describes the passage from Stepanov's multiplicity to theta chains of length comparable with the square root of the parameter, and mentions slopes, cancellation of costs and integral structures common to several characters. That establishes an explicit antecedent of the pattern; it does not by itself verify its assertions about a complete or formalised proof.

## 2. The connection with the primes is an identity, not an analogy

The scheme visible in 57 is

    s_fin(y,σ) = Σ_ν Λ(ν)(1−χ_K(ν)) · (y/ν − κ(u(−ν)σ))_+.

Frobenius moves the CM places, which is why the divisibility at one place depends on the weight located at another. The choice of two levels of weight works as an arithmetic selector. If y=a and the weight of the partner place is b, with x=a/b, then

    (a/ν−b)_+ = a(1/ν−1/x)_+.

The condition on the class of that partner place selects the congruence of ν. The factor 1−χ_K(ν) selects the excess coming from non-split primes. The logarithms of primes appear on adding valuations. Thus the truncated kernel of the sum over primes comes from a concrete operation of divisibility: the positive part of the difference between order of differentiation and transported weight.

This suggests an autonomous question: **which family of kernels over primes can be realised by means of admissible CM weight profiles?** One cannot assert that any test function or any L-function is realisable. The Frobenius actions, the restrictions on weights, the integrality, the growth of rank and the levels limit the family. To characterise those restrictions would already be a new result independent of the destination RH.

## 3. An abstract principle that delimits the essential

Let d>0, 1≤n≤d, n≥(1−ε)d with 0≤ε<1. Suppose that H≥0, m>0 and that the same independent family of n vectors satisfies

    c ≤ n(H−mR+E_S),
    c+2δ ≥ d(H−E_C),

with E_S,E_C,δ≥0. The first may come from Hadamard and a norm bound; the second requires real arithmetic and is not derived from the first. Subtracting, one obtains exactly

    n mR ≤ (n−d)H+nE_S+dE_C+2δ.

Since H≥0 and n≤d, it follows that

    mR ≤ E_S + (E_C+2δ/d)/(1−ε).

This is a proved elementary implication, not a new theory. Its use is to show what the deep theorems must supply: the same norms and lattices, almost all the rank, a small index and errors smaller than the gain m.

**Clarification with respect to the historical report:** in the application H_main≥0 there is no inevitable loss εH_main; the term (n−d)H_main has favourable sign and can be discarded. If H were negative, that loss would indeed have to be kept. The rank defect still matters through d/n and, in the construction of Cv, through the cost of completing the family with auxiliary vectors.

Semistability in the full sense of slopes does not follow from these hypotheses: only families of almost full rank are controlled. A Harder–Narasimhan theory would demand bounds for all subobjects, compatibility of saturation and well-defined metrics. That strengthening is a future question, not a free reformulation of what has already been proved.

## 4. Three research priorities

### Priority 1: isolate the covolume principle with twists per prime

**Object.** A space of forms with several integral realisations by means of lifts and a fixed archimedean metric. At each prime one is allowed to choose a different twist to obtain a good valuation; a global twist that works at all of them simultaneously is not required.

**Desirable autonomous result.** A theorem which, from a common integral structure, determinant identities and summable local budgets, gives a covolume bound with all the losses visible. It must explain why the changes of basis serve for all the realisations admitted at that prime and why the local selection controls the same global determinant.

**What is classical and what remains to be isolated.** The product formula is classical. The specific content would be to supply verifiable hypotheses for this family of automorphic realisations, with uniform control of the denominators and congruences. The mere fact of adding valuations must not be sold as new.

**Test of success.** Formulate the theorem without RH and apply it to a non-trivial example with at least two different local choices. Prove that the integral structure is a full lattice, that the total index converges and that a rational change of basis preserves the inequality by the product formula. A genuinely different norm does modify the degree: do not assert invariance under any change of metric. In incomplete rank, include the cost of the complement.

### Priority 2: classify the analytic kernels codable by CM divisibility

**Object.** A profile κ on the CM places, transported by Frobenius; the local excesses are positive-part functions like that of §2.

**Desirable autonomous result.** Characterise a cone of test functions realisable with profiles of two, three or more levels; compute their main terms and their costs in rank, conductor and differentiation. Specify which of them allow a useful one-sided bound to be extracted.

**First concrete step.** Generalise the exact computation from two levels to three, before increasing the number of variables. Identify the combinations of truncated kernels that appear and prove that the data remain admissible. Separate formal identity, effective divisibility and global cost; none of those three things replaces the others.

**Test of success.** A realisation theorem for a family of kernels wider than the single profile used for RH, accompanied by an integral and archimedean bound with the same period and all the exceptional places. If it cannot be widened, an obstruction theorem explaining the limitation would also be a contribution.

### Priority 3: express the multiplicity gain by a uniform theorem of rank and cost

**Object.** A chain of theta operators and a Poincaré map whose second moment controls the proportion of directions reached.

**Desirable autonomous result.** A theorem with separated variables: length m, rank, weight, level, degree of the field and discriminant. It must show the benefit that grows with m and the cost that survives after the main terms are cancelled.

**Elementary control piece.** For A≥0 of rank r with non-zero eigenvalues λ_i, Cauchy–Schwarz gives

    rank(A) ≥ (tr A)^2 / tr(A^2).

What is new, if it is proved in a range not available before, is the uniform computation of the two traces and the control of the necessary translates, not this matrix inequality.

**Test of success.** First a result in fixed rank that recovers the principal constant exactly; then an explicit region of simultaneous growth. Present a cost function C(m) and prove that C(m)/m decreases in the relevant region. If the inevitable costs are linear or larger, explain what additional cancellation is needed. The length comparable with sqrt(x) must come out of a proved budget, not out of its resemblance to the expected exponent of RH.

## 5. An especially valuable independent result: the local branch of 56

Although it is not one of the three priorities of the central mechanism, it is worth extracting the integral exponents of cup products as a project of its own. A precise contribution would be a bound in terms of the windows of weights, their distribution among the letters and the number of bad indices, including a table of the cases ℓ=2, ramified and tame. This can feed other arguments on congruences and Selmer without mentioning RH.

The next step would be to study optimality and examples where the exponent is attained, and to distinguish sufficient conditions from necessary ones. In particular, the condition NM must not be presented as a characterisation if only sufficiency is proved. The existence of integral Hodge theory beyond Fontaine–Laffaille is an antecedent; the candidate novelty resides in the exponent and in its concrete summability for the application.

## 6. What could constitute a new line, and what could not

A reasonable descriptive name is **divisibility and covolumes in automorphic families**. It places the research between geometry of numbers/Arakelov, theta and CM, moment methods and congruences. It does not presuppose that a new recognised discipline already exists.

For the name to come to represent a subarea, there would have to be reusable objects, theorems stable as the families vary, examples not designed only for one proof, and different applications. The three priorities supply concrete criteria. A set of hundreds of pages combining many techniques may be an important proof, but its length and difficulty do not by themselves prove that a field has been born.

Nor was a Hodge index theorem for the objects of 43–45 constructed automatically. Paper 57 itself declares that those rows are not premises of the deduction of signs: the absence of zeros is obtained first by the automorphic route. An intrinsic geometry that produced the positivity would be another direction, much more open. The completion results of 43 even warn that a regularisation not chosen with care has no sign independent of the path.

## 7. Attribution and level of novelty

Three questions have to be separated:

- **Mechanism:** what connection the strategy realises. It is identified above by means of identities and budgets.
- **Priority:** who first formulated or proved that exact mechanism. This demands literature and dated documents; a favourable audit does not establish it.
- **Contribution of this series:** what its author adds to the earlier sources. The Acknowledgement of 57 expressly attributes to Alpoge the organised mathematics and the route to the zero-free half-plane; it attributes to the series the division SF/Sp/Cv, the names and the writing of its proofs, together with the frame A–C and the radial study.

For this reason it would not be faithful to the manuscript to say that its author discovered for the first time the Stepanov–theta connection or the strategy of slopes. One can, however, investigate whether its formulation, its particular results, its repairs and its extensions offer contributions of their own. That attribution must be made theorem by theorem, keeping the declared provenance and separating what is written in the supplement from what appears in the original sources.

**Conclusion of the analysis:** the most fertile aspect is not "using many areas for RH", but designing integral structures whose local excess of divisibility produces an analytic test function, and converting that gain into a global bound by means of spanning of sufficient rank and cancellation of covolumes. It is a precise research agenda; its full priority and its eventual status as a subfield still require additional work.
