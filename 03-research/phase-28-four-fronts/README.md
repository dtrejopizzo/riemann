# Phase 28 — four fronts; the Laguerre-Pólya equivalence and the sector decomposition

Taking the bridge conjecture of phase 26 as a working hypothesis, the phase
abandons pure reformulation and opens four simultaneous fronts aimed at
causal mechanisms for why zeros cannot leave the critical line: (A) whether
the de Bruijn-Newman flow is the gradient flow of a logarithmic energy that
drives the Kreĭn index to zero; (B) whether the Atiyah-Patodi-Singer
η-invariant of the Weil operator vanishes; (C) whether the negative
spectral projection is the trivial K-theory class of the idèle-class-group
C*-algebra; (D) whether the critical line is the unique minimizer of a
canonical arithmetic energy. The four fronts are shown to collapse into a
single question, which is then pursued analytically to its most concrete
form.

## Results
- Central unification: Fronts A and D are shown to be the same program in
  two languages (de Bruijn-Newman gradient flow = transversal energy
  minimization); Front C is connected to Front A via the same flow as a
  candidate KK-homotopy; Front B is later shown to be the same problem in
  variational language. **PROVED** (structural identifications).
- Front A: $H_t$ has only real zeros for t ≥ 1/2 (de Bruijn, **CITED**);
  Λ ≥ 0 (Rodgers-Tao, **CITED**); Λ = 0 ⟺ RH (**CITED**); the de
  Bruijn-Newman flow is the gradient flow of the logarithmic energy
  (Csordas-Norfolk-Varga, **CITED**); monotonicity of the Kreĭn index along
  the flow is proved but is too weak to force RH. Conjecture A.15 (Λ =
  max_j b_j²/2) is new and **OPEN**.
- Front B: spectral flow equals the Kreĭn index (Proposition B.2,
  **PROVED**); an APS index formula is set up (Corollary B.4); whether the
  η-invariant of the Weil operator vanishes is identified as the heart of
  the front and remains **OPEN**; a conjectural closed form for η in terms
  of ζ'(0) is proposed but unproved.
- Front C: K₀(C*(C_ℚ)) ≅ ℤ (Connes, **CITED**); the negative spectral
  projection [P₋] equals κ(Q) in K₀ (**PROVED** given the bridge), making
  [P₋] = 0 tautologically equivalent to RH; the needed KK-equivalence
  [H_C] = [1] is **OPEN**.
- Front D / Question 28.1 and its correction: the originally posed
  log-concavity-in-σ question is **PROVED FALSE** under RH (negative
  result); the corrected exact equivalence (Theorem 4) is RH ⟺ a curvature
  functional 𝒞(γ) built from ξ''/ξ - (ξ'/ξ)² is positive for all γ — an
  exact analytic restatement, **PROVED** equivalent, not resolved.
- Document 07: RH is restated as f(t) = ξ(1/2+it) belonging to the
  Laguerre-Pólya class, equivalently G(t) = (ξ'/ξ)'(1/2+it) > 0 for all t
  (Question 28.2); this ties together all four fronts as the same LP
  problem. **PROVED equivalence** (new presentation), citing the classical
  de Bruijn/Newman LP fact.
- Document 08: exact closed-form decomposition G(t) = G_poly(t) + G_Γ(t) +
  G_ζ(t), with explicit formulas for the polynomial and Gamma-factor
  sectors (new derivations, **PROVED**) and the explicit identity
  Re ψ⁽¹⁾(1/4+it/2) + Re ψ⁽¹⁾(3/4+it/2) = 2π²sech²(πt) (classical,
  Abramowitz-Stegun). The analytic sector G_ana(t) is shown to change sign
  (becomes negative for large t), so it alone cannot force G(t) > 0; the
  arithmetic sector G_ζ(t) must compensate, and that compensation is
  exactly RH. **PROVED** (new diagnostic); a Proposition shows an off-line
  zero forces G < 0 nearby.
- Final verdict of the phase: every front, after full analysis, reduces to
  the same wall ("Wall A" from phase 27, now localized with maximal
  analytic precision as positivity of G_ζ relative to the explicit,
  sign-changing G_ana); no front closes the gap. **OPEN** throughout,
  explicitly acknowledged as a sharper reformulation, not a resolution.

## Documents
- `00-setup.md` — the four-front plan and the Front A = Front D
  unification.
- `01-front-A.md` — de Bruijn-Newman flow, the Kreĭn-index monotonicity,
  and Conjecture A.15.
- `02-front-B.md` — spectral flow / APS η-invariant front.
- `03-front-C.md` — K-theory / Baum-Connes front.
- `04-front-D.md` — transversal arithmetic energy and Question D.15 (second
  variation).
- `05-second-variation.md` — exact computation of the second variation of
  the Weil form in the transversal direction; introduces the LP-T class and
  Question 28.1.
- `06-curvature-xi.md` — exact Hadamard-product computation of the
  transversal curvature of log|ξ|; shows Question 28.1 false under RH and
  derives the corrected exact equivalence (Theorem 4).
- `07-lp-class-rh.md` — restatement of RH as Laguerre-Pólya membership of
  ξ(1/2+it); unification of all four fronts as the same LP problem
  (Question 28.2).
- `08-decomposition-sectors.md` — exact sector decomposition of G(t) into
  polynomial, Gamma, and zeta components; localizes the final obstacle and
  states the phase's closing verdict.

## Relation to other phases
Builds directly on the bridge conjecture (phase 26) and the Wall A
diagnosis (phase 27); concludes the program's reformulation arc by
identifying RH with Laguerre-Pólya membership and localizing the remaining
obstacle to the arithmetic sector G_ζ(t) of the curvature of log|ξ|, framed
as "Wall A in its most elementary form" with no further phase proposed in
these documents.
