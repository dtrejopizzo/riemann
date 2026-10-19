# R166_400 — Corpus mechanisms (phases 0–166) satisfying 2 of the 3 requirements

**Sources:** R166_401 (phases 160–163 + grid, 61 mechanisms), R166_402 (164–166, 29), R166_403 (0–110, 58),
R166_404 (111–159, 82). Total ≈ 230 classified mechanisms. Criteria (R166_190 "Phase 166 closure"):
- **(i)** global over the node set X / the whole witness (Hadamard product, phase, harmonic measure, Wiener–Hopf), not jets at nodes.
- **(ii)** couples with the **atomic prime side beyond the window** (Λ(n), n ≥ e^{2T_c}, Λ ≥ 0, multiplicative) non-linearly.
- **(iii)** does not reduce to (1.1) on a test (E1), nor to a window-only statement (f_t), nor zero-only (M_m).

**Overall result:** no mechanism satisfies all three. **{i,iii} is empty across the whole corpus** (everything
global in X is zero-side and is killed by M_m; the only apparent exception, Levinson–Conrey mollifiers, is
killed by DH and Epstein). The 2-of-3 cases split into two families that never touch:

## Family P — {i,ii}: global in X and with signed atomic Λ; fall by E1 (they are (1.1) on a test or a factorization)

| # | mechanism | phase / file | wall | residual |
|---|---|---|---|---|
| P1 | Prop 4: real-height Λ tail, Σ_ρ G²y/(z²+y²) = 𝔄_y − G(iy)²𝒯(iy), 𝒯 > 0 | R164_501 | identity; quartets weigh y/γ_q² | (★_cell) |
| P2 | dlVP test on G², Ψ = G²[w₀P₀ + w₁(P_{±γ_q})] | R164_601 Prop 2.1 | W2/M (Fejér ceiling + archimedean) | O164.601.1 = weighted (★_cell) |
| P3 | Discarded-term principle | R164_601 Thm 3.1 | every discard inequality holds for the real zeros | lower bound of the other quartets |
| P4 | Tail-sign condition for G²K (g*Ǩ of one sign on [2T,∞)) | R164_601 Props 1.1–1.3 | same as P1–P2 | — |
| P5 | Interpolation identity with tail G²𝒯_X; off-line residues in the tail | R163_801 Thm 3, Cor 3.1 | the tail vanishes on X; M_m satisfies it (Thm 5) | statement about the tail **beyond X** |
| P6 | Minimal nodal atomic object 𝒜(s;G) = Σ q_x(−ζ′/ζ)(s+ix) | R162_2201 Thm N1 | nodal tests are PW ⇒ window only (f_t) | — |
| P7 | Dirichlet square / Wiener–Hopf A − T_Λ = (I−V)*(I−V), V = ΣΛ(n)n^{−½}S_{log n} | phase 70 E70_10 (F54) | F2; quotient comb Σ_{r∈ℚ}c_r S_{log r}, c_r from Λ(aj)Λ(bj) | grading/quotient cancelling the Euler square; cross-check with phase 161 and R166_301 (W-TK) |
| P8 | Lee–Yang / DQPT + Euler–Möbius connection | phase 70 E70_4/7/11 | E1 via AHM→Weil | — |
| P9 | Sign of |ζ|² − |ζ_on|², dν, relative entropy | phase 33 docs 83, 86, 89 | E1 | — |
| P10 | Wiener–Hopf factorization 𝒯 = A*A / D_Euler | phase 136 S6 (1A) | E1 | — |
| P11 | Sharp Douglas gate, contraction over prime-power births | phases 114 D.170, 120 P3 (8A) | E1 | — |
| P12 | Adele-class space as an MW-5 object | phase 158 R158_002/005 | restatement (E1) | — |
| P13 | Deninger/Serre D1–D3 axioms, Lemma T | phase 158 | E1; laminated-carrier piece OPEN | lamination |
| P14 | Meyer H¹ / density of H¹_alg | phase 158 R158_006; R160_C3 Thm B | E1 | density OPEN |
| P15 | Euler determinant lines / Contou-Carrère / Bohr assembly | phase 122 P122_013–017 | E1 | — |

## Family Q — {ii,iii}: atomic arithmetic at every height, killed by neither f_t nor M_m; **never read X** (die by identification, class blindness, orientation, or margin)

| # | mechanism | phase / file | wall | residual |
|---|---|---|---|---|
| Q1 | Tail split 𝒯_X = 𝒯^det + (−ζ′_{≥X}/ζ_{≥X}), zeta of X-rough integers | R166_103 B1–B2 | positivity blind without FE (Thm A), identifies with FE (Cor R.1), one-sided = Landau = E1 | exact relation ζ_{≥X} on ½<Re s<1 ↔ the witness's cosine |
| Q2 | Thm R: positivity off ℕ + gap + FE ⇒ ζ | R164_401 | W-identification | — |
| Q3 | Theorem L (Witt lattice does not go below θ) and Lemma D | R164_201 | blind to zeros | O164.201a |
| Q4 | Discrete Beurling off the lattice below 1/3 | R164_503; R163_101–105, 110, 803 | construction OPEN; positive direction ≥ RH + quadratic GRH | Problem 6 |
| Q5 | Positive tail / Bernstein; Hamburger (Prop I) | R164_102 Thm A, Prop I | blind to zeros; identification | — |
| Q6 | Atomic support ⟹ Dirichlet ⟹ RH, gap-free lemma | R163_114–117, 123–126 | identification (⟺ RH) | — |
| Q7 | Hamburger collapse / Thm O | R163_113, R162_2601c/2801, R163_1001 | W3′ | — |
| Q8 | Positive-factorization lemma | R163_002 | countermodel K | — |
| Q9 | Classical zero-free region, sub-Landau | R163_701 | M | — |
| Q10 | Selberg's zero density Σδ² = o(T) | R163_115, R163_502 | blind to X | — |
| Q11 | Gamma–Selberg tail / rational collision ledger | R163_135, 139–141 | identification | — |
| Q12 | Cross-energy torsion lift with a positive Gamma tail | R163_127–132 | F2 orientation | — |
| Q13 | Same-weight Euler lift | R163_142–145 | class | — |
| Q14 | Moving-graph waves / hyperbola cross channel | R163_148–162 | class | — |
| Q15 | Canonical Tate 2×2 system | R162_2701 | NO-GO | — |
| Q16 | Piltz ledger | R162_2802 | identification | — |
| Q17 | dN₀ ≥ 0 of the quotient ζ/R | R162_2901 | positivity never forced | — |
| Q18 | de la Vallée Poussin / numerator sign T6 | phase 151 | M | O-151.4 |
| Q19 | Summand-vs-numerator axis O-151.4 | phase 151 | OPEN | **open** |
| Q20 | Landau's lemma D.34.5 | phase 143 | — | — |
| Q21 | Beurling T3 (conditional on H-DMV) | phase 150 | conditional | — |
| Q22 | Deligne extraction over the additive pencil D.59 | phase 149 | rationality W8 | — |
| Q23 | Rationality wall Thm R/R′ | phase 159 G1_B4_R5 | W8 | — |
| Q24 | BRS's Thm P | phase 159 G2_B6_R4 | blind to β | — |
| Q25 | Λ = μ*log at the identity level | phase 157 | OPEN | **open** |
| Q26 | Non-local Tauberian with LI input (GAP-157.A) | phase 157 | OPEN | **open** |
| Q27 | Relative correspondence E_(∞,T) | phase 122 | never built | **open** |
| Q28 | Multiplicative chaos / freezing | phase 12 | probabilistic–deterministic gap | — |
| Q29 | Adelic local–global Hasse–Minkowski | phase 27 | MW-3 A/B | — |
| Q30 | Two-variable Weil form W₂ with a Λ*Λ block | phase 36 doc 107 | (iii) only formal; superseded by R162_2702a | — |

## {i,iii}: empty (with the downgraded exception of Levinson–Conrey mollifiers, phase 159 G2_B10, killed by DH/Epstein; Thm H never audited)

## Reading for conjugation

1. **The only P↔Q bridges are P5 (tail beyond X) and P7 (Dirichlet square).** P5 dies because the tail vanishes
   exactly on X and the nodal tests are PW; P7 dies in the quotient comb Λ(aj)Λ(bj), pure multiplicativity.
2. **Conjugation never attempted (R166_404):** pair an open Q residual (Q19, Q25, Q26, Q27, Q1) with G's
   **global phase** at t_q (harmonic measure, R165_201 Thm 2), not with a factorization. Factorizations fall by
   E1; the phase is the jet k = −1 and is exactly what the Q's never read.
3. **P1/P5 + Q1 conjugation:** Prop 4 reads the tail with a sign at real height; Q1 says every off-line residue
   lives in ζ_{≥X}. Missing is the relation reading the cosine: R166_103's box.
4. **P7 + Q25 conjugation:** the Dirichlet square produces Λ*Λ-type terms; the identity Λ = μ*log (Q25, open) is
   the only identity tool treating exactly Λ–Möbius convolutions. Check first against phase 161 (sum–product
   square) and W-TK.
5. Falsifiers every conjugation must pass: M_m (zeros), f_t (window), f_χ and P_{a,c} (class), Λχ₂ and deletion
   (sign of the tail / same tail), ζ_θ (no FE at ½).
