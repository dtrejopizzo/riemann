# CA_L_SYNTHESIS — Front L (exact magic-function constructions), phase 193

 Pen and paper; no numerics. **No sign contact. No certified negative value for ζ. No clause of (R) moved.**
Memos: CA_L_000 (10 seeds, pre-screen, corpus check), CA_L_001 (literal magic certificate: NO-GO), CA_L_002 (prime-site LP on the torus: REF-D).

## Answer
*Can one build, for each T, an exact dual (or primal) certificate for the window form from modular/Eisenstein objects, with vanishing on log n
and the Tate points, so that ℤ, FE and Euler enter jointly?* **No, within the declared classes:**
1. **Window LP (P47):** exact certificates do not exist (thm:O, read as LP slackness: the primal optimum |F̂⋆|²dτ has full support, so the magic
   vanishing set is ℝ) — CA_L_001 Thm 1.1. Flat-top certificates read the zero side (thm:Z): the "explicit modular form" whose sign would be
   read is ŵ on {τ − γ}. Viazovska's three inputs fail: (V1) discrete primal, (V2) positive Poisson sides (prime comb enters with −v_n; CE gives
   upper bounds on the zero side, Prop 3.1), (V3) Fourier eigen-structure (only τ ↦ −τ; Mellin does not map additive PD to multiplicative PD, §5).
2. **Modular-data constructions** are excluded at level 20 by the genus pair x²+5y² / 2x²+2xy+3y² (identical gamma factor, conductor, root number,
   residue; Epstein falsifier O10) — CA_L_001 Thm 4.2. At level 1 Hamburger's theorem makes the data determine ζ, so the exclusion reduces
   to: any level-1 construction uses the comb (support ℤ, coefficients), and then item 1 applies. Honest caveat recorded.
3. **Restoring (V1)** via site independence (CA_K K-S): on prime sites the LP has a discrete primal, the dual lives on the torus 𝕋^X (ℚ-independence of
   log p — the · input), is attained, and exact certificates are supported on the zero locus Z_s of P_s = Σ s_x z_x (the magic vanishing
   condition) — CA_L_002 Thms 2.1–2.3, Cor 2.4. Exact for |X| ≤ 5 (elliptope rank bound); lossy in value only for |X| ≥ 6; target ⟺ λ_𝕋(X) ≥ 0 ∀X.
   This is an exact restatement (REF-D), comb- and FE-generic (Prop 3.1); the magic set is the minimizer (Prop 3.2); modular objects give
   Kronecker-line measures, exactness needs the torus.

## Verdicts
| seed | verdict | killing clause |
|---|---|---|
| L1 exact flat-top magic certificate | NO-GO (PROVED) | thm:O / CA_L_001 Thm 1.1 |
| L2 modular ε-magic | NO-GO for modular-data class (PROVED lvl 20); lvl 1 reduces to L1 + class (D) | CA_L_001 Thm 4.2, Hamburger caveat |
| L3 CE one-sided | DISCARD | wrong direction (Prop 3.1) |
| L4 RV interpolation | DISCARD (retry) | P35-4, finZ |
| L5/L6 site LP / torus certificate | REF-D (PROVED restatement) | CA_L_002 Prop 3.1–3.2 |
| L7 Cohn–Gonçalves | DISCARD | single-function radius, comb-generic |
| L8 Delsarte/Turán | tool only | class (D) |
| L9 CKMRV | DISCARD | needs lattice (V1)+(V3) |
| L10 theta sinc-annihilation | DISCARD (retry R164_401) | FE-only |

## PROVED facts (usable elsewhere)
L-O. Window-LP slackness set = ℝ; exact magic certificates impossible (also for tempered ν with continuous polynomially bounded ν̂, ARGUED).
L-E. Modular-data constructions cannot certify ζ_{ℚ(√−5)} (genus-pair argument).
L-T. Prime-site torus LP: weak duality identity s^TM_Xs = (𝖡(0) − η(𝕋^X)) + ∫|P_s|²dη; attainment; slackness supp η ⊂ Z_s; exact for |X| ≤ 5; target ⟺ λ_𝕋(X) ≥ 0 ∀X;
     Grothendieck-form dual (Cor 2.4).

## Proposed YES→NO moves
- "a Viazovska-type magic function exists for the window form" → NO (PROVED, thm:O as slackness).
- "a construction from modular data (weight, level, character, residues) certifies row D" → NO at level 20 (PROVED); level 1 reduces to comb constructions.
- "Cohn–Elkies sign conditions give a lower bound for the window form" → NO (direction, PROVED).

## +/· reading (PRINCIPIO RECTOR)
The only place where the magic-function architecture fits is the prime-site torus: · gives the torus (Kronecker independence of log p),
+ gives the edge values 𝖡(log p/q), and exactness is the vanishing of the minimizer's Dirichlet polynomial P_s on supp η. ℤ, FE, Euler meet
there jointly, but the meeting point is a restatement; the sign is not read from any explicit object. Area exhausted for front L.
