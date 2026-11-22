# CA_G_000 — Seeds, front G (exotic algebras, representation theory, combinatorics)

Phase 193. Pen and paper, no numerics.
**No certified negative value for ζ. No sign contact.**
Read before seeding: CAMPAIGN_LEDGER, CA_A/B/D_SYNTHESIS, CA_C_004/007, CA_SYNTHESES_REVIEW, P46 §20 (lem:transfer, thm:shape,
prob:region (R)(1)–(11), thm:sos, prop:cone), ROUTES-TRIED-INDEX README/03/06 (NG-67 CQG, CAT rows, P82/P92 cluster = FRED loops),
AUDIT_A (A14a-1 PF₅ fails, CITED; A14a-2 PF₄ OPEN), R138 D.15.2 (Lorentzian criterion, PROVED).
Screen key as CA_C_000. O-labels are Paper 46's. Idx = retry of an indexed route.

## Common fact G0 (PROVED, linear algebra): every "square" mechanism is a Gram factorization
Let 𝔞 be a bounded symmetric form on P_T. (a) 𝔞 = Q*Q for some bounded Q: P_T → ℋ ⟺ 𝔞 ≥ 0 (take Q = 𝔞^{1/2}). (b) If Q is required to be
translation-covariant (a multiplier in τ), 𝔞 = Q*Q + (free PD part) is exactly an arithmetic square decomposition / certificate, so
thm:sos (none at T ≥ ½log3 without free part) and thm:D1 (with free part, content = the bottom) apply. (c) "Positivity because the
number is a dimension/trace" means 𝔞(F) = Tr A(F)*A(F) with A linear in F — case (a). Hence a square mechanism is admissible only if
Q is *constructed* from ζ independently of the sign, and then the sign step is the construction (P1). Every seed below that produces
positivity as a square, a norm, a dimension or a unitary character meets G0.

## Common fact G1 (PROVED): the abstract multiplicative monoid sees no difference between ζ, Beurling systems and ζ_K
ℕ^× is the free commutative monoid on countably many generators. A Beurling g-integer system with free generators (O11), and the ideal
monoid of any number field K (O12, unique factorization of ideals), are isomorphic to it as monoids. Only the norm map N: monoid → ℝ_{>0}
differs. Therefore any positivity that is functorial in the monoid (Hecke algebra ℚ[ℕ^×], its Soergel-type bimodule category, its
Hopf/incidence algebra, its Möbius involutions) survives O11 and O12, and is excluded by (R)(10)/(B″) unless it uses N — i.e. the additive
embedding n ↦ log n of ℕ ⊂ ℝ, or the integrality/multiplicity-one of the norms. CA_G_001 §1 writes this out.

## Seeds
| # | seed | Idx | (R) | (P1)–(P6) | O-screen | B′/B″ | REF-D | verdict |
|---|---|---|---|---|---|---|---|---|
| G1 | SUSY: 𝔞_T = {Q,Q*} with supercharge Q (Witten/Riccati factorization H = (−∂+W′)(∂+W′)) | new | (3) ✗ square | P1 ✗ | Riccati factorization exists for every potential with H≥0 (ground-state lemma, CA_G_001 §2) ⇒ survives all O | B″ for the Witten identity | yes: factorization ⟺ positivity | DISCARD (G0(a), REF-D) |
| G2 | Clifford/spin, Weitzenböck–Lichnerowicz: 𝔞 = ∇*∇ + curvature | new | (3),(5) | P5 ✗ (Weitzenböck is an identity for every comb) | natural split = 𝔞_∞ − Σ𝔮_p: both summands indefinite (cor:Tarch, cor:Qp) | B″ | — | DISCARD (no summand carries a sign) |
| G3 | Elias–Williamson HL+HR induction on the window ladder T_k, Lefschetz L = convolution by a positive kernel | partly CA_A_008 / L2_002 | (5) ladder law ✗ unless unbounded | P1 risk | — | — | primitive complement carries the whole target | DEVELOPED in CA_G_001 §3 → REF-D/retry |
| G4 | Categorification: 𝔞_T(F) = graded dimension (KL/Soergel, Macdonald, crystals, LR) | new | (3) | P1 ✗ | G0(c) | — | yes | DISCARD |
| G5 | VOA/moonshine: modular invariance + unitarity (positive character coefficients) | new | (10) ✗ | P3 ✗ (comb-only q-coefficients) | O10 survives: Epstein = Mellin of a lattice-VOA character with the same unitarity | B″ | — | DISCARD |
| G6 | Lorentzian polynomials (Brändén–Huh), Hessian signature (1,n−1) | R138 D.15.2 | — | — | output is one positive direction; target is zero negative ones (P46 Theorem P bounds n₋ only) | — | Lorentzian criterion D.15.2 already PROVED, no sign | DISCARD (retry) |
| G7 | Cluster algebras: Laurent/theta-function positivity, TP of cluster coordinates | P82/P92; A14a-1/2 | — | positivity is for positive variables; F̂ is signed | TP of the dBN kernel fails at order 5 (CITED 2602.20313); order ≤ 4 OPEN, local only | — | — | DISCARD |
| G8 | Jordan algebras / symmetric cones (self-duality of the PSD Toeplitz cone) | thm:D1 | (3) ✗ | — | — | — | self-duality = certificate duality thm:D1 | DISCARD |
| G9 | Connes–Kreimer Hopf algebra / Birkhoff factorization ψ = ψ₋^{-1}ψ₊ | R186-WH | (5) | — | — | — | Birkhoff = Wiener–Hopf factorization (W-det, R186_042–047) | DISCARD |
| G10 | Sign-reversing involutions (Möbius Λ = μ * log, Garsia–Milne) | new | (10) ✗ | P5 ✗ | G1: the involution is monoid-functorial ⇒ O11/O12 survive; and the form has signed F, so a combinatorial certificate is an SOS (G0(b)) | B″ | — | DISCARD |
| G11 | Quantum groups / q-Shapovalov | NG-67 | — | — | — | — | — | DISCARD (retry NG-67) |
| G12 | Hecke algebra of ℕ^× with a "Soergel calculus" (template applied to the monoid) | new | (10) ✗ | — | G1 | B″ | — | DISCARD unless it uses N; with N it becomes a statement on the comb (P3 ✗, O7 keeps the comb) — CA_G_001 §1 |

**[crit] precision.** No seed produces an estimate; all fail before precision M^{−3} matters.
**Survivors:** G3 only (structural template, developed in CA_G_001). Second batch not opened: G0 + G1 cover every positivity mechanism of
the area (dimension, unitarity, square, involution, total positivity, Hodge–Riemann); see CA_G_SYNTHESIS.
