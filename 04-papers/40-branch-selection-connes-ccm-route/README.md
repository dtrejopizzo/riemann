# Paper 40 — Branch Selection and Global Polarization in the Connes–CCM Route to RH: Finite Prime–Gamma Inertia, Tate Boundary Geometry, and the Divisor-Sensitivity Obstruction

## What the paper studies

The paper arranges the finite semilocal models of Connes–Consani–Moscovici (CCM), Connes' prolate model and Suzuki's localized self-adjoint realization as one route towards the Weil positivity criterion, and asks exactly where the sign needed for RH must enter.

## What is proved

- Theorem 5.1 (Conditional closure of the CCM route): if positive-form convergence, or divisor convergence (each continuum branch has only real zeros in the strip and the logarithmic curvatures converge), holds, then RH follows. The hypotheses are not proved. Proposition 7.4 shows that Problems 7.1 and 7.2 are each sufficient for RH, and that Problem 7.3 is equivalent to Weil positivity on even tests, which gives RH together with the corresponding inequality for odd tests.
- Section 8: for an endpoint-corrected six-mode prolate source, the angle ladder δ₀ ≍ d₄, δ₁ ≍ d₈ (Lemma 8.8, from quoted prolate asymptotics). Bounds O(λ⁷d₄) and O(λ⁴√((1+L)d₄)) for the exterior co-Poisson residual and the cross functional (Theorems 8.10, 8.12) are derived under the standing assumptions (P1)–(P4): quoted prolate asymptotics, radial estimates (8.8n), (8.8q)–(8.8r), (8.8v), the lower bound (8.8e), and an extension of the explicit formula; these are not proved here.
- Section 9: finite prime–Gamma inertia algebra. Finite inertia matching (Haynsworth), scalar Schur innovation, adaptive Krylov recovery, augmented exhaustion and heat-core exhaustion (Theorems 9.4, 9.7, 9.14, 9.12, 9.18, 9.2) reduce the sign on each finite row to one finite inequality, the strict source surplus (9.25bi). That inequality is equivalent to A_∞(q*,q*) > ℓ on the row and is **not proved**; (9.25bi) implies the compensated frontier (9.27), and, under the ground-state identity, (9.27) implies A_∞ ≥ 0 on the complement Q_C, that is, Weil positivity on even tests (Theorem 9.19; Theorem 9.18 also uses this identity). RH would further need the inequality for odd tests.
- Section 10, unconditional local geometry: a cyclic root Laplacian whose determinant increment (log p) and root-stratum incidence (p^{−k/2}) multiply to Λ(p^k)/√(p^k) (Theorem 10.1); a Gamma spin operator and polar plane giving ½s(s−1)π^{−s/2}Γ(s/2) by zeta determinants (Theorem 10.2); a matched Abel finite part on the common Tate–Gamma boundary (Theorem 10.3).
- Lemma 10.6: the Gamma compliance has dense range (operator-valued criterion). Theorem 10.7: the explicitly defined charged completion of (10.20)–(10.29) has absolutely continuous scale spectrum. Under Hypothesis (R) (CCM degree one contains a nonzero eigenclass for each critical-line zero), every equivariant map from degree one into it annihilates those classes. Proposition 10.5: under Hypothesis (R), a global CCM polarization implies RH.
- Six terminal formulations: the implication to Weil positivity is proved for the signed limit, the Schur surplus (on even tests, under the ground-state identity) and (under Hypothesis (R)) the global polarization; the Rosati factorization is a GNS restatement; the Hilbert majorant and closure-faithful descent are only formulated.
- Proposition 10.9: four forgetful functors (half-plane sign class, scalar determinants, homotopy classes, curvature) do not detect the position of the divisor under explicit deformations; for the cyclic Chern character this is stated, not proved.

## Conditional, heuristic, open

- Proposition 8.2 (mesh and exterior defects) is stated under assumed estimates; the six terms of (8.3) are a bookkeeping convention. Problem 7.3 defines its jump energy so that (7.5) holds by definition. The prolate limit (2.4) and Suzuki's limiting conjecture are recorded in remarks and used only as explicit assumptions.
- Everything leading to RH is conditional: on the closure hypotheses, on the strict source surplus, or on a faithful positive global polarization. RH is not proved.
- The large-prime rank-one channel asymptotics (9.23)–(9.25) are proved by Laplace's method, with constant C_Ξ = 2 for the normalization of K by ∫K(x)e^{izx}dx = Ξ(z); no uniform frame bound is proved.
- Section 9 identifies the complete form with the explicit-formula energy of Problem 7.3 only under a ground-state identity that is stated as a hypothesis; (9.15), (9.25bl) and the passage to even Weil positivity in Theorem 9.19 are conditional on it.
- The Lefschetz-parity explanation of the prime-term sign is a heuristic taken from the function-field analogy.
- Open: an arithmetic intersection product with a Hodge-index polarization on a square of the arithmetic curve; a divisor-sensitive (nuclear or derived) completion that keeps evaluation jets.

## Known versus new

Cited: the Weil criterion (Theorem 1.1), the finite CCM–Connes model (Theorem 2.2), Suzuki's realization (Theorem 3.1), and classical matrix tools (Schur complements, Haynsworth inertia additivity, Andreief's identity). New: the finite source estimates of Sections 8–9, the local constructions and the no-go results of Section 10. No other paper of the series is used.

## Files

- `main.tex` — LaTeX source.
- `branch-selection-connes-ccm-route.pdf` — compiled paper, 44 pages.
