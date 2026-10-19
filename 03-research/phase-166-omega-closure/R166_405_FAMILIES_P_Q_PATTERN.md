# R166_405 — Families P and Q: how each member satisfies (i), (ii), (iii), and the common pattern

Source: R166_400 (merge), R166_401–404. "—" = does not satisfy. Criteria in R166_190.

## Family P — {i, ii}, fails (iii)

| # | mechanism | (i) global in X: how | (ii) atomic Λ beyond the window: how | (iii) |
|---|---|---|---|---|
| P1 | Prop 4 (R164_501) | the test is G²·y/(z²+y²): the witness's whole Hadamard product | the tail 𝒯(iy) = Σ_{n≥X}Λ(n)n^{−½−y} > 0 appears with a sign in the identity | — : it's (1.1) on a test; the quartet weighs y/γ_q² |
| P2 | dlVP on G² (R164_601) | same, G² via Poisson kernels at 0 and ±γ_q | tail with sign via the triangle inequality w₀|G(is)|² ≥ 2w₁|G(a+is)|² | — : W2/M (Fejér + archimedean) |
| P3 | discarded term (R164_601 Thm 3.1) | any global test G²K | discards the signed tail | — : the inequality holds for ζ's real zeros |
| P4 | tail sign for G²K (R164_601 Props 1.1–1.3) | G²K | g*Ǩ of one sign on [2T,∞) | — : same as P1–P3 |
| P5 | interpolation with tail (R163_801 Thm 3) | Σ_ρ G(t_ρ)²/(t_ρ−x) over the whole zero set, G global | off-line residues in G²𝒯_X, Λ(n), n ≥ e^{2T} | — : the tail vanishes on X; M_m satisfies it |
| P6 | 𝒜(s;G) = Σ q_x(−ζ′/ζ)(s+ix) (R162_2201) | sum over every node with weights q_x | −ζ′/ζ at every height | — : nodal tests are PW ⇒ window only (f_t) |
| P7 | Dirichlet square / Wiener–Hopf (phase 70) | operator A − T_Λ on the whole line, (I−V)*(I−V) | V = Σ_n Λ(n)n^{−½}S_{log n}, **quadratic in Λ** (Λ(aj)Λ(bj)) | — : F2; non-absorbable rational-quotient comb |
| P8 | Lee–Yang / Euler–Möbius (phase 70) | global partition function | Euler product as a factorization | — : E1 via AHM→Weil |
| P9 | sign of |ζ|²−|ζ_on|², relative entropy (phase 33) | functional over the whole line | Euler in |ζ|² | — : E1 |
| P10 | 𝒯 = A*A / D_Euler (phase 136 S6) | Wiener–Hopf factorization of the symbol | atomic D_Euler | — : E1 |
| P11 | Douglas gate (114, 120) | contraction over the whole operator | prime-power births p^k | — : E1 |
| P12 | adele-class space (158) | global object | finite places = primes | — : restatement |
| P13 | Deninger D1–D3 (158) | global flow/foliation | closed points = primes | — : E1; lamination OPEN |
| P14 | Meyer H¹ (158) | global cohomology | atomic measures at log p | — : E1 |
| P15 | Euler determinants / Bohr (122) | global Bohr assembly | per-prime determinant lines | — : E1 |

**Common trait of P:** all of them are **a single quadratic form (or a single factorization) on a global
object** — the test G² or an operator on the whole line — in which the zero side and the prime side are **the
two faces of the same explicit formula**. They are quadratic in the witness and **linear in Λ** (except P7,
quadratic in Λ). That is why (iii) always fails: equality between the two faces is already given, and an
identity produces no sign.

## Family Q — {ii, iii}, fails (i)

| # | mechanism | (i) | (ii) Λ at every height: how | (iii) why f_t / M_m don't kill it |
|---|---|---|---|---|
| Q1 | split 𝒯^det + ζ_{≥X} (R166_103) | — : X is the cutoff e^{2T}, not the nodes | zeta of rough integers, Euler product over p ≥ X | separates f_t (no Euler), f_χ, M_m (β_m density) |
| Q2 | Thm R (R164_401) | — : identifies ζ, no witness | N ≥ 0 off ℕ + gap, global positivity | excludes f_t (negative coefficients off ℕ) |
| Q3 | Theorem L / Lemma D (R164_201) | — | integer multiplicities on the Witt lattice | discrete class statement; ζ_θ excluded |
| Q4 | Beurling below 1/3 off the lattice (R164_503) | — | multiplicity integrality | same |
| Q5 | positive tail / Hamburger (R164_102) | — | Λ ≥ 0 on (log X, ∞); support on log ℕ | Thm A is blind to zeros; Prop I identifies |
| Q6 | atomic support ⟹ Dirichlet ⟹ RH (R163_114–126) | — | atomic support of the exchange on log ℕ | ⟺ RH (identification) |
| Q7 | Hamburger / Thm O (R163_113, R163_1001) | — | frequencies on ℕ + FE | identifies at conductor 1 |
| Q8 | positive factorization (R163_002) | — | ν_N = ν₀*κ positive ⇒ support on log ℕ | countermodel K with no FE |
| Q9 | classical zero-free region (R163_701) | — | Λ ≥ 0 + 3+4cos+cos2 | holds for ζ with margin 1/log γ |
| Q10 | Σδ² = o(T) (R163_115) | — | zero density via Euler | statement about ζ alone |
| Q11 | Gamma–Selberg tail (R163_135–141) | — | Selberg Λ·log + Λ*Λ | identifies |
| Q12 | cross-energy torsion (R163_127–132) | — | positive Gamma tail | dies by F2 orientation |
| Q13 | Euler lift (R163_142–145) | — | multiplicative weights | class |
| Q14 | graph/hyperbola waves (R163_148–162) | — | cross channel Λ(a)Λ(b) | class |
| Q15 | Tate 2×2 (R162_2701) | — | per-prime Tate transfer | NO-GO |
| Q16 | Piltz ledger (R162_2802) | — | multiplicative b ≡ 1 | identifies |
| Q17 | dN₀ ≥ 0 (R162_2901) | — | integer measure of the quotient | positivity never forced |
| Q18 | dlVP / numerator T6 (151) | — | trigonometric Λ ≥ 0 | margin M |
| Q19 | summand-vs-numerator axis O-151.4 (151) | — | same | ~~OPEN~~ → CLOSED (R168_202 Thms 1.1–1.4: summand = restatement; numerator = dlVP or identification) |
| Q20 | Landau's lemma D.34.5 (143) | — | coefficients ≥ 0 | real singularity |
| Q21 | Beurling T3 (150) | — | generalized system | conditional on H-DMV |
| Q22 | Deligne over the pencil (149) | — | per-prime Frobenius | W8 |
| Q23 | Thm R/R′ rationality (159) | — | weight rationality | W8 |
| Q24 | BRS's Thm P (159) | — | prime sums | blind to β |
| Q25 | Λ = μ*log identity (157) | — | exact Möbius | ~~OPEN~~ → **DONE for P7** in E70_11/12 (Möbius connection V = Z⁻¹δZ; Riccati = Selberg identity) ⇒ E1; R157_002 #30 no object; positive variant #55 excluded by F3 (R166_502) |
| Q26 | non-local Tauberian with LI (157) | — | linear independence of log p | **OPEN** |
| Q27 | correspondence E_(∞,T) (122) | — | — (never built) | ~~OPEN~~ → CLOSED (R168_202 Thms 2.2–2.4: identification with FE, blind without FE) |
| Q28 | multiplicative chaos (12) | — | randomized Euler product | probabilistic gap |
| Q29 | adelic Hasse–Minkowski (27) | — | per-prime local–global | MW-3 |
| Q30 | W₂ with a Λ*Λ block (36/107) | — | Λ*Λ | (iii) only formal |

**Common trait of Q:** all are **statements about the arithmetic object alone** (Λ, N, θ, ζ_{≥X}, the Euler
product) in which the witness F **does not appear**; zeros enter only as a conclusion ("⟹ RH") or as a class.
They are **non-linear in Λ** (exp_*, integrality, positivity, Möbius, multiplicativity) and **degree zero in F**.

## The pattern separating them, and what the union demands

| | degree in witness F | degree in Λ | where zeros and primes live |
|---|---|---|---|
| P | quadratic (c_F, G²) | linear (except P7: quadratic) | the two faces of an identity |
| Q | zero | non-linear | the prime side only; zeros as a conclusion |
| **needed union** | **≥ quadratic and global in F** | **non-linear in Λ beyond the window** | **a relation that is not the explicit formula** |

The only member already mixing both columns is **P7**: quadratic in F (operator) and quadratic in Λ. It died
exactly at the term where Λ's non-linearity appears (the quotient comb Λ(aj)Λ(bj)). And the only Q member
treating that term is **Q25** (Λ = μ*log, open). The unions to test, in order: P7+Q25 (after checking against
phase 161 and W-TK), P1/P5+Q1 (R166_103's box), and "open Q + G's global phase at t_q" (R165_201 Thm 2).


## Addendum (R166_502): the P7 + Q25 crossing is a REPEAT, not admissible
Phase 70 already built it (E70_11 Möbius connection, E70_12 Riccati = Selberg) and it ends in E1. New lemma
(R166_502): in V*V the non-integer comb is exactly the cross part Σ_{p≠q} V_p*V_q (ratios p^k/q^l, only j = 1
contributes); Selberg rewrites the convolution square V² (products p^k q^l), not the Hermitian square V*V
(ratios): Möbius acts on ℕ's Dirichlet algebra, not on ratios. The same comb kills F36 (E70_7). Phase 161 is
another square (of the Weil operator, sign-blind) and closes the repair by Möbius elimination (R161_004 Cor
3.1 / P121 CMO). W-TK does not apply (P7 is one-sided, not truncated). Next crossing in order: **P1/P5 + Q1**
(R166_103's box). Surviving form: a separate-sign sector exactly cancelling Σ_{p≠q} V_p*V_q, to be built before
any crossing.
