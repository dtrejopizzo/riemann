# AUDIT_001 — Independent review of the O1 specification

2026-10-18. Independent check. Row D independent. Pure mathematics.
Status: initial review in §§1–7; final review of the construction and of the synthesis in §8. Completed.

## 1. Corpus consulted and initial decision

Read: the project rules, README209, CONTROL_001, README208; README index (families and entries 204–207), 06_OPEN_RESIDUES (W₂ and BR leaves), targeted searches in the master grid and crossword; CELL_001 §8–10 and AUDIT_207_001 §B; P1_BBSTAR_001; SPEC_SIGN_OBJECT_005; R185_005B §1–3; BARRIER_X_001 §3 and correction AUDIT_197_HOSTILE_3 §c; Paper 47 main.tex def:PD, thm:sos and rem:sosatoms.

**ARGUED: specification admissible as an examination of the already open O1.** The new written reason is concrete: effective kernel not reducible to a multiplier plus functional reflection, without collapse to a weight of the product mn. It is not equivalent to having a candidate or a new lemma. The README gates avoid repeating Gonek, Gram and factorisation of the target form.

## 2. thm:sos: exact scope

**CITED / checked against the statement.** thm:sos requires simultaneously a pointwise identity

    Σ_i |D_i(t)|² = μ₀ − Σ_n v_n cos(t log n)

plus positivity of the archimedean form minus μ₀ on P_T. The contradiction for T≥½log3 compares μ₀≥Σv_n≥0.9802 with archimedean background ≤0.311. It does not use the specific frequencies of the D_i; the extension to real frequencies is incorporated in the paper.

It is not a theorem against every norm identity. P1_BBSTAR distinguishes: enlarging the space and restricting B*B immediately gives (Bι)*(Bι); proving that some root exists is reformulating the target, while constructing a root of a specified class may have content. With a free positive-definite part and multiplier representation one reaches def:PD, not an impossibility of existence of certificates. An explicit construction in that class would still need to prove the certificate: classifying it does not refute it.

**Gate approved**, with this caution: being outside thm:sos does not imply being outside def:PD nor supplying a sign. A generic B*B positive for all data does not thereby pass the arithmetic gate; its link with Q_T is the whole difficulty. Do not turn the mere norm lemma into the substantive milestone.

## 3. Three distinct two-variable notions

1. Effective kernel K(t,t′) of an operator in Mellin heights.
2. Diagonal two-variable form W₂ of P36-4 recorded in the index.
3. W₂=𝔄−Q^hyp−𝓡−C̄ of R185_005B: relaxed set of remainders in scheme (M2).

Coincidence of notation or number of variables does not produce a translation between them. **CITED:** BR applies only after giving admissible tests, tail identity, arithmetic statement of the class 𝔐 and remainder model. In (M2) it needs coordinatewise lower bounds or the indicated ba/sup regime. The leaf ρ1‴ requires proving precisely the relevant failure of those hypotheses; it is not an automatic exit for integral kernels. The joint statements (Λ,Γ) and certain operator objects lie outside 𝔐; that does not give them positivity either.

**Gate approved.** No candidate is yet translated into that scheme.

## 4. Parity and Gonek

**CITED:** Kronecker parity preserves defects determined by the value distribution of FE quotients under torus rotations. Its antipodality consequence requires an admissible class closed under sign flipping. AUDIT_197_HOSTILE_3 explicitly corrects that the integer class 𝓘 of the original memo is not. Do not cite that obstruction as a theorem for every kernel. A kernel with correlations between heights may lose the invariance; this must be computed, not assumed.

**CITED:** Gonek in CELL_001 computes the scalar component of J via stationary phase and gives weight w(2πmn) plus error. It does not characterise every weight-½ form: such a reading would be too broad. With a=Λ, Λ*Λ is not Λ·d. The sign of its main term for w≥0 is inherited by nonnegative data and does not pay the error; indefinite w has no established sign. A new K needs an exact formula, domain and remainders, not merely that the initial expression use two heights.

## 5. Deletion: required logical proof

Define b^(p)(p^k)=0, b^(p)(n)=Λ(n) otherwise. If p<e^(2T), there is a changed interior datum; at n=p, Λ*1=log fails by log p. The failure is of identification, not of sign.

**PROVED, elementary logic:** to refute a deduction by transfer one needs all its inherited premises and a datum violating the conclusion. Therefore it is not necessary for a candidate to become negative upon deleting any interior prime, nor that every premise fail for all p,T. It suffices to locate, for the deletions relevant to the proposed deduction, the exact arithmetic hypothesis that prevents the transfer. A generic norm may stay positive after deletion and be accompanied by a specific identity that fails: this possibility is legitimate, but the work concentrates on proving that identity without assuming the target sign.

Requiring failure for EVERY interior prime is a stronger design condition, not a universal logical necessity. Do not demand it as a barrier theorem. For p>e^(2T) the target is identical in that window; no local distinction can be demanded. Global premises may distinguish those data without contradiction.

## 6. CONTROL_001

**PROVED:** with the unitary Fourier transform, the projection onto transforms of L²([-T,T]) has sinc kernel sin(T(t−u))/(π(t−u)). For real a∈L∞ the integral of the product of sincs with a converges absolutely by Cauchy–Schwarz, and P_T M_a P_T restricts to the same multiplier form on its image. Also on the polar subspace. The extension to the unbounded symbol is prudently formulated as a form restriction and does not claim the integral.

The control is correct and useful. The condition it excludes is "novelty by writing a kernel"; it does not prove that every nonlocal form is a multiplier nor that the lack of ambient commutation always disappears after restriction.

## 7. Initial verdict

README209 and CONTROL_001: **approved with the precisions of §§2–5**. O1 remains OPEN. No sign mechanism nor new NO-GO has been obtained. The final review must check in the candidate which hypothesis of SOS, PD, BR or parity actually applies; not infer it from its name. Full domain, exact link, remainders, continuous window and sector remain pending until there is a construction.

## 8. Final review of CONSTRUCTOR_001 and SYNTHESIS

**Verdict: approved, PROVED for the declared class; NO CANDIDATE for O1.** No node sign was obtained. The synthesis correctly preserves this limit.

- **§4 / J. PROVED.** On a symmetric interval, |χ_t|=1 and χ_tχ_−t=1 make J unitary and involutive, hence self-adjoint. The free extension from (0,A) via f(−t)=±χ_−t f(t) satisfies Jf=±f and both eigenspaces are infinite.
- **Lemma 4.1. PROVED.** The representation by fibres {t,−t} turns the algebra into matrix multipliers. In a non-atomic measure a nonzero matrix multiplier is not compact: choosing a nonzero column on a set of positive measure and partitioning it gives orthogonal images uniformly bounded away from zero. It holds for norm closure, as the memo says. Strong closure, which is a different operation, is not claimed.
- **Theorem 4.2. PROVED.** Compact approximation by finite rank, intersection of V₋ with ker R and L of finite codimension, and the −1+ε estimate are exact. E remains closed infinite-dimensional. No orthonormal vectors inside the ideal nor arithmetic information are needed. The negative sign is unambiguous.
- **Lemma 5.1. PROVED.** The transform of the orthogonal h has exponential growth linear in the radius. Jensen with nonzero centre bounds the number of zeros by O(r), incompatible with the ≥exp(r/3) points log n in the inner disc for large r. Fourier uniqueness gives h=0. P_b is bounded on the interval and nonzero almost everywhere; the adjoint multiplier argument proves density of the ideal without requiring a bounded inverse.
- **Corollary 5.2. PROVED.** For the continuous map to a finite-dimensional space, the image of the dense ideal is a dense subspace and hence the whole image. The finite preimages used to correct approximations and preserve constraints exist. Continuity of the form gives a negative value inside the restricted ideal. The statement does not claim infinitely many negative directions inside that ideal, although they could be extracted by unnecessary additional arguments.
- **§6. PROVED / correct scope.** The failure already occurs at Λ; hence there is no positive candidate to submit to the deletion test nor link to audit. The null generator gives a null domain, not useful specificity. Arbitrarily changing the dependence b↦C_b does not alter the obstruction as long as each C_b remains compact.

**Two editorial precisions of scope, not affecting proofs.** (i) In §8 "arithmetic domain of infinite codimension" must be read for closed linear domains: if the domain is a nonlinear variety, codimension and density require definition and no such necessary condition follows here. The valid universal formulation is that the positivity domain cannot contain a closed subspace of finite codimension nor the declared dense ideal with only finitely many constraints. (ii) In §7, an inherited positivity does not by itself refute a specific link identity that fails upon deletion: such an identity could still provide content (§5 of this audit). The construction does not build such an identity nor claim a general NO-GO for it; read this way, the table is a screening of generic proposals, not a theorem about every conjugation.

**SYNTHESIS: approved.** I+J≥0 follows from the decomposition into V₊ and V₋ and the non-compact correction I. It is a generic example without arithmetic link, not a candidate. The non-compact exit is only a necessary condition within the chosen ansatz and ambient domain; not a condition of all of O1.

Final result: an elementary control of compressions and an elementary functional NO-GO for J+compact on the specified large domains. No demonstrated progress towards the sign by itself; no closure of O1, no transfer to the global node PW_T with tails. The initial milestone of a specific positive kernel was not reached.
