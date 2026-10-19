# CA_I_000 — Seeds, front I (analysis and PDE of the extremal problem: qualitative theory of the minimizer h*_T)

Phase 193.
Pen and paper; **no numerics run**.
**No sign contact. No certified negative value for ζ.**

Read before seeding: CA_H_SYNTHESIS, CA_H_002 (H0, Thm 2.2 (S⁺), Thm 3.1/3.2 anatomy, Cor 2.3 "purity"), CA_E_001 (Thm 1
separability, Lemma 1 Kronecker line), CA_F_003 (G-F), CA_G_SYNTHESIS (G0, G1), CAMPAIGN_LEDGER, P47 def:shape-ops (O1–O15),
def:quartetmodel / prop:quartetmodel / lem:shape-quartet, prob:region (R)(1)–(11), lem:monoT, prop:archneg, thm:famblind, lem:flowdet;
ROUTES-TRIED-INDEX README (PRINCIPIO RECTOR) + 04_ (W-fam, W-pat, W-loc, flowdet, F-DH) + 06_.

**Corpus grep (done first; hits that make a seed a retry).** virial/Pohozaev: P124_007 (projected virial: Tate projection defect
cancels the commutator, REFUTED), R165_202 §1.4–1.5 (virial derivative PROVED under (REG); Hadamard principle ARGUED), R162_407 (REG,
linear transport), R186_038 α.1–α.4 + R186_111 (Grönwall ⟺ target on finite range; absolute virial bound gives δ ≈ 10⁻¹²).
Perron–Frobenius / Krein–Rutman: P60-1 = phase-60 H1_PROOF (Ω CND, Lévy–Khintchine, e^{−tA} positivity preserving, simplicity; "gives
simplicity, not sign"), R184_003 (parity, constant not eigenvector), E78_1 (ground simplicity). Nodal / real-rootedness: R165_202 1.6–1.8,
R163_501 Thm B (Blaschke flip), R155_046/047 (Sturm/Karlin), W-jet (R166_201). Edge / collar: R165_202 1.2 (activation strips, parity
sign), R186_038 α.1–α.2 (edge amplitude, parity entry cost), R186_048 (component birth, invisibility at entry), SPEC_A Lemma S (edge
component e_min). Almgren/frequency: only nodal-count usages (R162_1701/1602) — no frequency-function monotonicity in T. Carleman / unique
continuation: R186_025/027 (coercivity lemmas), no Carleman estimate on h*. Γ-convergence / concentration–compactness: phase 60
(2b_O4b, scaling limit), not for h*_T. Rearrangement / polarization / Baernstein: 0 relevant hits (phase 145 hits are a different
"polarization"). Maximum principle: R160_M4_R1, R160_X_C1, R163_501 (witness audit) — local uses only.

## Screen key
As CA_H_000. (R)k = clause k of prob:region. (P1)–(P6) = CA_B_SYNTHESIS residual spec. O-labels = P47 def:shape-ops. B′/B″ =
thm:shape (estimate with remainder / identity valid for every weight vector). FE-gen = survives Epstein x²+5y² (CA_C_007, H0(b) ARGUED).
G0 = squares are Gram factorizations; G1 = monoid-functorial positivity survives O11/O12. H-anat = CA_H_002 Thm 3.2 (every term is
additive weight × monoid coefficient, linear in Λ; non-linearity only via minimizer or a new input). REF-D = restatement of the target.
[crit] = must resolve at relative precision M^{−3} (EXP_005 C1, NUMÉRICO). PR = PRINCIPIO RECTOR (+/· use). "dies" = first killing clause.

## Common fact I0 (PROVED; the shape of the qualitative channel)
Let 𝔞_T be the window form on L²(I_T) (P47 eq:form), 𝒫_T = {∫Fe^{±t/2} = 0}, h*_T a unit minimizer, λ_A = 𝔞_T(h*_T). The
Euler–Lagrange equation is (A_T − λ_A)h* = β₀e^{t/2} + β₁e^{−t/2} in 𝒟_T*, A_T the operator of 𝔞_T. Every qualitative property of h* is
either (a) a property of the triple (A_T, span{e^{±t/2}}, λ_A) valid for the whole class of symbol forms σ ↦ ∫σ|F̂|² with the same
structural axioms (evenness, Paley–Wiener support, compact resolvent) — then it is class-generic and dies at O7 (quartet forms are
symbol forms with all those axioms, P47 prop:quartetmodel(iii)); or (b) it uses a property of the specific kernel of A_T. In case (b),
by H-anat, the kernel is (additive-only Lévy/archimedean part) + (monoid-only atoms v_nδ_{log n}); a qualitative property then is a
property of one of the two summands, of their conjunction, or a non-linear functional of h* (REF-D, SPEC_A Lemma S).
*Proof.* The EL equation is the Lagrange condition for a quadratic form on a codimension-2 subspace; the kernel decomposition is
CA_H_002 Thm 3.1/3.2 read in t-space (c_F pairs with ν(u)du on the a.c. side and with v_nδ_{log n} on the comb side). ∎

## Seeds and full pre-screen
| # | seed | Idx retry? | (R) clauses hit | (P1)–(P6) | O-survival | B′/B″ | FE-gen | G0/G1 | H-anat | REF-D | [crit] | PR (+ and · together?) | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | Markov / Beurling–Deny structure of 𝔞_T, nonlocal maximum principle, Krein–Rutman ground state, Tate-constrained PF | partial retry P60-1 (simplicity); new: Markov ∀T as a **rigidity property** separating O7/O9 | (R)(1) ok only jointly with S⁺; (R)(3) fails if used alone (positivity-preservation is a linear-cone property); (R)(5) ok | P2 fails alone, P3 ok (reads the form's kernel), P5 ok (not B″: O7 breaks it) | separates O7, O9 (CA_I_001 Thm 3); survives O2(c>0), O4(c>1), O6, O11, O12, O15 | not B″ | ? (Epstein comb sign not checked) | G1: Λ≥0 half is monoid-only | conjunction of additive (ν≥0) and monoid (Λ≥0) halves | the sign step from it is REF-D | — | **no**: conjunction, not interaction | DEVELOP (least dead; CA_I_001) |
| I2 | sign-changing structure of h* (nodal count, Courant for nonlocal operators, Chebyshev lower bound) | retry R165_202 1.6–1.7, R155_046/047, W-jet | (R)(5) pattern of observables; (R)(11) | P3 ok, P5 fails | survives all O (constraint geometry only) | B″ | yes | — | constraint-only | — | — | none | DEVELOP as lemma inside CA_I_001 (§4), DISCARD as route |
| I3 | symmetrization: Riesz, Baernstein ★, two-point polarization | new (0 hits) | (R)(8): kills positive/negative frequency correlation | P3 ok | the Tate constraint is not rearrangement-invariant; comb kernel not symmetric-decreasing | B″ for the arch part (Pólya–Szegő holds for every Lévy form) | yes | — | arch-only | — | — | none (rearrangement sees order of ℝ only) | DISCARD (CA_I_001 §5, Prop 5.1) |
| I4 | Pohozaev / virial / Hadamard identity for the EL equation | **retry** P124_007, R165_202 1.4–1.5, R186_038/111, F-DH | (R)(11) (B″), (R)(6) | P5 fails | survives O1–O15 (linear in comb) | **B″** | yes | — | linear in Λ | Grönwall form = REF-D (R186_111) | precision λ_A/𝒱 | none | DEVELOP the exact DH statement (CA_I_002 §1) |
| I5 | Almgren frequency / monotonicity formula in T | new as frequency; retry W-fam, R186_111 α | (R)(5) family law; (R)(6) | P1 ok | O13 (bounded range); f_t | — | yes | — | functional of family | yes on bounded range | super-exp | none | DISCARD after Prop 2.2 of CA_I_002 (frequency unbounded) |
| I6 | unique continuation / Carleman for h* | new for h*; neighbours R186_025 | (R)(3)(5) | P2 fails | all (Paley–Wiener only) | B″ | yes | — | none | — | — | none | DISCARD (UC is automatic: ĥ* entire of exponential type; no sign content) |
| I7 | Γ-convergence of 𝔞_T (rescaled to (−1,1)) as T → ∞ | new | (R)(6): Γ-limit gives o(1) absolute, target needs super-exp relative | — | O4^ε, O13 | B′ | yes | — | leading term only | — | fails | none | DISCARD (CA_I_002 §3) |
| I8 | concentration–compactness for minimizing sequences of inf_T λ_A | new | (R)(3) | — | all | B″ | yes | — | — | — | — | none | DISCARD (CA_I_002 §4: quadratic ⇒ no strict subadditivity) |
| I9 | boundary layer at ±T, collar where new primes enter (edge trace, entry cost by parity) | **retry** R165_202 1.2, R186_038 α.1–α.2, R186_048, SPEC_A Lemma S | (R)(5)(7) | P3 ok | survives O7 at the qualitative level | identity part B″ | yes | — | linear in v_n at entry | Lemma S(i) REF-D, (iv) upper direction only | yes | **partial**: entry instants T_n = ½log n (·) × strip translation (+) — but linear in v_n | DEVELOP (second survivor; CA_I_002 §2) |
| I10 | comparison / domination of semigroups in the comb (Ouhabaz), monotonicity of eigenvalues in weights | new as stated | (R)(3) | P2 fails | O2, O4 | — | — | G1 | monoid-only | — | — | none | folded into CA_I_001 §3 (λ₀ monotone, λ_A not) |

Survivors for depth: **I1** (with I2, I3, I10 as lemmas) in CA_I_001; **I4 + I9** (with I5, I7, I8) in CA_I_002.
