# CA_R3_001 (SPEC_A θ-line, L*_j(θ)) — Review, maximum scepticism
Checked vs SPEC_A Lemma S, EI_001 (2.1), CA_R2_002, P46 thm:shape, cor:shape(a), lem:shape-quartet, prop:quartetmodel(ii), def:shape-class, CA_C_001 Lemma 2, CA_I_001 Thm 3, CA_R1_001 Thm 2.3.

## Verdict
**Identities CONFIRMED (Prop Θ, Lemma C, (Ch)). The label "ADMISSIBLE as a specification" is NOT endorsed. Correct label: REF-D (valid objective, OPEN), with a clause table that overstates.** The θ-clause is "met" only in the sense that the statement is the exact Schur step of the target written in Chebyshev coordinates; it adds no property that a deduction class could carry.

## 1. Identities
| claim | check |
|---|---|
| Prop Θ | right-collar G: r ≥ T_j ≥ s ⇒ u = e^{r−s} ≥ 1; r − s ≤ T_j + T_{j+1} ⇒ u ≤ √(n_jn_{j+1}) < n_{j+1} ✓; density part = e^{−s/2}∫Ge^{r/2}, killed by B(x) = 0 ✓; left collar symmetric with A(x) ✓; polar part likewise ✓. PROVED. **But** the "ψ − u" form is cosmetic: the density term is identically zero on P_{T_j} for *every* comb (any positive or signed measure in place of dψ). Consequence (a) "(R)(7) proved" is the statement that du pairs to zero on P_T — comb-generic (B″), prop:wit-cheb split restated (retry of EI_001 Thm 1). |
| Lemma C | p·m′ = m·n′ with m,m′,n′ < p impossible ✓ PROVED; monoid fact, survives O7/O11/O15 (memo ✓) |
| (Ch) ψ(y) = Σ_{k≤y}μ(k)log⌊y/k⌋! | Chebyshev identity + Möbius inversion ✓ CITED/standard |

## 2. The clause table, item by item
- **O1–O6, O8, O10–O12, O15 "escaped because (Ch) fails".** (Ch) on [1, n_{j+1}) holds iff a = Λ there (H1; CA_C_001 Lemma 2: the exact divisor identity on the window is a singleton). Every deduction that uses the exact data escapes these modifications trivially; the escapes certify only that the hypothesis is "the exact vector", i.e. cor:shape(a)'s minimum, not a mechanism. Not wrong, but vacuous as evidence.
- **O7 / O9 — the decisive rows.** The quartet model keeps the comb exactly, the FE, Γ(s/2), conductor 1, i.e. it satisfies (Ch) *and* clause (ii) "exact K" — its archimedean part is unchanged (prop:quartetmodel(ii), CA_B_007 Prop 1). What distinguishes it is the extra a.c. term +k∫c_Fβ_z, i.e. *purity of the form* (CA_I_001 Thm 3; CA_R1_001 Thm 2.3: purity enters only as the identity K = 0). So the O7/O9 escape is "the step is about the exact form 𝔞_T and nothing else" — the target object itself. The memo's phrase "O7/O9 escaped only through the exact archimedean kernel" is inaccurate: exact K is shared by O7; the escape is through *absence* of β_z, i.e. by identification. Endorsed reading: O7/O9 escaped by identification (W-identification), as for 𝖯⋆.
- **H1 is fatal for the word "mechanism".** thm:shape's deduction classes are defined by property sets of form objects (def:shape-class). "Proof restricted to operations acting on (Ch)'s two factors" is a restriction on *syntax*, not a property of the object; any proof using Λ's values can be rewritten through (Ch). So clause (iii) of 𝒞_θ is unenforceable and cannot move (R)(11). (R)(11) is not "PASS-COND"; it is **not applicable** — there is no sign step to test.
- **H2** (1/ζ on the Mellin side) correctly flagged; (R)(4) PASS-COND acceptable.
- **(R)(3) "PASS: Schur term rational in Λ through 𝔄_j^{−1}"** — non-linearity via the inverse of the target's own frozen block = minimizer channel (SPEC_A Lemma S; EI_003 symbol rigidity): REF-D, not an independent non-linear input.
- **(R)(5),(6)** — the margin bound ν_j ≥ μ_j·exp(−C(n_{j+1} − n_j)) is a requirement, not a result; consistent with CA_R2_002 (1.1) and with super-exponential decay along the product of steps. Fine as specification.
- **(R)(10) PASS (ARGUED)** — fine.

## 3. Conclusion
L*_j(θ) = Lemma S(i) at step j with the exterior field written via Prop Θ and (Ch). By Lemma S, ∀j L*_j ⟺ row D: **REF-D (valid objective)**, as the memo's own B8 line says. Calling it ADMISSIBLE conflicts with prob:region's use of "admissible" (an argument in the region carrying a sign step). Recommended label in the ledger: **"SPEC_A identity-only exact induction, θ-line specified: REF-D / OPEN objective; no admissible candidate."** Value: Prop Θ(b) (contact block = one jump of ψ − u, atom vs its polar partner) and Lemma C (prime contacts: no exact cross-resonances) are useful bookkeeping for the R4 attempt at n_j = 7.
