# R160_000 — Blueprint, phase 160: survey + 20 memos + 5 panelists

Plan. Stage 1: five surveyors cover the whole corpus and the papers through phase 159. Stage 2:
twenty memos and a panel of five run in rounds until one of the two objectives is built in full, or the
round limit is reached.

## Objectives (unchanged from phase 159)
* **G1 — THE OBJECT (OT-5′):** a carrier over Spec Z with a positive form defined BEFORE the spectrum and without the
  zeros, compatible with the flow/Frobenius, whose Lefschetz formula is the explicit formula of ζ (R158_001 OT-1…OT-12
  as amended by R158_003). Its Hodge-index/Castelnuovo inequality must then give the sign.
* **G2 — THE MECHANISM:** an argument that uses the EXACT values of Λ(n), is uniform in T, has no margin and no
  truncation, and proves `∀T: λ^A_T ≥ 0` or `∀T: λ^W_T ≥ 0`.

Either one, completed, is a proof of RH. The panel treats it at that level of scrutiny.

## Premises of record (they bind every memo)
1. Rows A, B, C are WEIL-STRENGTH-COMPLETE on the declared carrier. That is **not** a proof of RH: row D, the sign, is
   RH itself (ROW-D-REDUCED-STATEMENT §1). The proved sign for ζ is: primitive form `T ≤ log 2` (Paper 42), ½log3
   endpoint (P47 thm:C); complete form `T ≤ ½log2` classical and `(½log2, 0.8]` (Zhu, CITED). **Nothing for T > 0.8.**
2. `thm:finZ`: no finite zero set carries a certificate. `cor:void`: class-level positivity is void. Theorem M
   (G2_B6_R2): `λ^A_T ≤ exp(−e^{(2−ε)T})`. The phase-159 walls (R159_099 §1.2, §2.2) exclude prime-local,
   tail-factorizable, algebraic, covariant, finite-trace conformal, ergodic conformal and canonical-crossed-product
   carriers, and class-level, twist-covariant, resolving-SOS and proportion-of-zeros mechanisms.
3. A new route must say, in its §0, why it lies outside every excluded class, with the file reference of each wall.

## Memos (profile — angle). Memos may pivot from round 2 on, to repair their own lead or to join a panel lead.
| # | profile | angle | front |
|---|---|---|---|
| B1 | Connes | prolate wave operator, Sonin spaces, semilocal trace formula (Connes–Moscovici 2022, CCM 2024): positivity from self-adjointness, λ→∞ | G1 |
| B2 | Consani | Riemann–Roch for Spec Z̄ over the sphere spectrum / ζ-cycles; Hodge index from an RR inequality | G1 |
| B3 | Jaffe | Osterwalder–Schrader reflection positivity: a Euclidean model whose OS form is the Weil form | G1 |
| B4 | Haagerup/Popa | natural cone and Tomita–Takesaki for an entangled (non-product) state over the primes | G1 |
| B5 | Scholze | analytic stacks / Gelfand rings; Hodge–Riemann on an analytic arithmetic curve | G1 |
| B6 | Bost | θ-invariants, infinite-dimensional Hermitian bundles over Spec Z̄; arithmetic Hodge index | G1 |
| B7 | S.-W. Zhang | height positivity of a canonical arithmetic cycle, towers of CM cycles | G1 |
| B17 | Lichtenbaum/Morin | Weil-étale cohomology of Spec Z̄, Artin–Verdier pairing, a positivity structure on H¹_W | G1 |
| B18 | Morishita/Mazur | arithmetic topology: knots, primes and the adèle class space (Connes–Consani 2024), linking forms | G1 |
| B19 | Huh | Lorentzian polynomials / combinatorial Hodge theory: a Kähler package built from the primes | G1 |
| B8 | Deligne/Katz | tensor-power trick across a tower of number fields; field-uniform proofs (T1 allows them) | G2 |
| B9 | Sarnak | Lax–Phillips / Pavlov–Faddeev scattering on SL₂(Z)\H: zeros as resonances, unitarity of the wave group | G2 |
| B10 | Iwaniec | Maass–Selberg relations, truncated Eisenstein norms, exact positivity identities | G2 |
| B11 | Tao | de Bruijn–Newman heat flow with Euler-product input (Rodgers–Tao dynamics) against the window forms | G2 |
| B12 | Tao | multiplicative positivity: Schur/Hadamard products of kernels, Euler product used multiplicatively, not additively | G2 |
| B13 | Maynard | large-sieve duality and Montgomery–Vaughan with exact Λ, a quadratic-form identity for W_T | G2 |
| B14 | Ono | Jensen polynomials (Griffin–Ono–Rolen–Zagier), uniformity in degree as the analogue of uniformity in T | G2 |
| B15 | Green | compactness + rigidity: ultralimits of normalized windows at T = ∞, a classification of limits | G2 |
| B16 | Villani | positivity as entropy/transport: W_T as the second variation of a convex functional | G2 |
| B20 | Connes | semilocal-to-global: Connes–Consani archimedean Weil positivity, finite S, S → all primes uniformly | G2 |

## Panel (critical, every round, reads every memo)
P1 Deligne-profile (line-by-line proof check) · P2 Sarnak-profile (restatement/equivalence and zero-installation
detector) · P3 Tao-profile (counterexamples: comb models, Davenport–Heilbronn, Epstein ζ, sign-flipped ζ, thm:finZ,
cor:void) · P4 Bombieri-profile (literature and corpus: is it known, is it contradicted by a wall) · P5 Connes-profile
(does it meet G1/G2 as defined, against the papers' own definitions).

Success: one memo judged COMPLETE by at least 4 of the 5 panelists. Otherwise the last stage writes the strongest
construction, with the full argument first and the open step marked as open.

Files: `R160_S{k}_SURVEY.md`, `R160_001_BRIEF.md`, `R160_B{k}_R{r}.md`, `R160_P{k}_R{r}.md`,
`R160_098_STRONGEST_CONSTRUCTION.md`, `R160_099_SYNTHESIS.md`.
