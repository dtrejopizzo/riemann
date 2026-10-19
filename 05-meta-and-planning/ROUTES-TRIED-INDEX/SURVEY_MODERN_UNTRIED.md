# Survey: modern (1990–2026) tools NOT yet in the routes-tried index — 

 Target: positivity of 𝔞_T on P_T (Paper 47, eq:target),
filtered by thm:shape (A)/(A′)/(B)/(B′)/(B″)/(C), cor:shape (a)–(d), Problem (R) clauses (1)–(11), and the six-clause
sign-carrier spec (README, fase 194). Labels: every item here is a SEED (no proof, no numerics). Scores are tractability
of a *first theorem*, not of closing D.

Method. Step 1: read README (familias cerradas, fases 190–194, especificación, principio rector incl. corrección M),
05/05b (L01–L85), keyword-grepped 01–04, 06, audits for each field below. Step 2/3 below.

## A. Fields already in the index (do NOT retry; listed so nobody re-proposes them)

| Field | Where in the index | Status |
|---|---|---|
| Perfectoid tilting | AUDIT_PHASE193 #50 (F13) | one-line discard (ℚ_p unordered) — weak, but indexed |
| Prismatic / TC / Σ_ℤ Frobenius | R9-19; G4H-R160_S1 #27 | DEAD |
| Fargues–Fontaine / condensed slope-½ / polarizations | G1H-159 G1_B3_R1 (REF-D); G8H-R160_S5 #21; MW-3 (NO-GO for 3 declared classes) | closed |
| Motivic / A¹ / RO(G) | R9-13/14; frente F | signatures; dead |
| Tropical, Berkovich | L10, L29; phase-152 | DEAD |
| Lorentzian polys, Hodge–Riemann, AHK Kähler package, matroids | P41-2; G8H-R160_S2; CA frente F/G | NO-GO / = Schur de paridad |
| Free probability | frente C (CA_C_006), AUDIT #17 | commuting ⇒ not free |
| Positivstellensatz / SOS / NC-SOS | G2C-159 G2_B4; frente E | REF-D / class (D) |
| Relative entropy, KL, Wasserstein, max-entropy | P33-11 | CIRCULAR |
| Viazovska magic functions, CKMRV | frentes L, N | NO-GO (thm:O) |
| Fourier interpolation (Radchenko–Viazovska), crystalline | P35-4 NO-GO; L30; L60 (not in corpus, low) | closed / low |
| o-minimality, Pila–Wilkie | frente C | vacuous |
| OS / reflection positivity per place and chessboard | NG-E1; frente J; frente A (between places) | FALSIFIED / NO-GO |
| Lee–Yang, strong Rayleigh, GKS/FKG, Brascamp–Lieb | L32; frente J | dead (frustration Thm 1.3) |
| de Branges, Kreĭn, Hermite–Biehler | L16, L20, frente D | closed |
| Floer, Bridgeland, Selberg/Arthur trace, Soergel, VOA | frentes F, G | closed |
| Determinantal / random combs, GMC | G8D-R160_S5; L77 | DEAD |
| Interlacing (as TP) | P6-31; R165_201 | wrong sign / refuted |
| Jensen hyperbolicity (one-variable real-rootedness) | L22, L50, MW-4 | closed |

## B. Candidates NOT in the index

Columns: mechanism · action on 𝔞_T / sign-carrier clause 5 · shape screen (CG = comb-generic/closed under O1–O6;
CONE = cone on log ζ (F2); SS = sparse-stable (J3)) · score · first theorem.

### B1. Hyperbolic polynomials, Gårding cones, real stability (Borcea–Brändén), MSS interlacing families — score 4
- Mechanism: a polynomial hyperbolic in direction e has a convex Gårding cone; stability is preserved by a classified
  set of linear operators (Borcea–Brändén); interlacing families give "some member beats the expected polynomial".
- Action: the index has the exact separability theorem (frente E, Thm 1: D ⟺ positivity of 𝔞_T on Euler-product vectors
  ⊗_p v_p). The restriction F ↦ 𝔞_T(⊗_p v_p) is multi-affine/multilinear in the per-prime blocks — exactly the object
  Borcea–Brändén/MSS act on, and NOT one-variable real-rootedness (Jensen, closed) nor TP (closed). New reason vs.
  Lee–Yang/Rayleigh (frente J): J used correlation inequalities in a ±1 gauge; here the variables are the prime blocks and
  the question is hyperbolicity of a mixed form, not ferromagnetism.
- Screen: a Borcea–Brändén preserver statement is a class statement → CG unless the preserver uses the window-wise
  vector (Λ(n))_{n<e^{2T}} exactly (cor:shape (a)). Clause 5: the FE enters through the archimedean block, which would
  be one more "variable"; that is the only place the coupling could be non-ζ(½+iτ). Risk: frustration Thm 1.3 may
  imply the multiaffine form is not stable → that itself is a clean NO-GO worth having.
- First theorem: decide whether P_T(z_2,…,z_P) := det or the symbol of 𝔞_T on ⊗_{p≤P} span{1, z_p·e_{log p}} is real
  stable for T = log 2, P = 2,3 (finite, pure algebra); either a stable-preserver structure or an explicit
  non-stability witness tied to the frustrated cycle (m, 2m).

### B2. Bakry–Émery Γ₂ / curvature–dimension CD(K,N) on the Markov semigroup of frente I — score 4
- Mechanism: Γ₂ ≥ KΓ gives spectral gap ≥ K (lower bound on the bottom), via a *quadratic* (not linear) functional of
  the jump measure J_T.
- Action: frente I proved the form without polar term is Markov (λ₀ < λ_A ≤ λ₂) and that Markov/PF/max principle
  don't decide (O2 conserves them). Γ₂ is not in the index (grep: Bakry absent). Γ₂ of a jump process is bilinear in
  J_T: Γ₂(f) = ∫∫ J(dx)J(dy)(…), so it is non-linear in Λ (clause 1) and is not a cone condition (clause 2).
- Screen: must check whether O2 and (1+c)Λ preserve CD(K) — if yes, NO-GO by thm:shape(A) immediately (cheap screen).
  Rigidity Thm 3 (frente I: FE-symmetric twists lose Markov for T ≥ T_E) hints curvature is FE-sensitive → clause 5.
- First theorem: compute the jump-measure Γ₂ for J_T at T = ½log3, and prove or refute CD(K,∞) with explicit K for
  Λ vs. the falsifiers O2, O4^ε, Beurling.

### B3. Modular / conformal bootstrap (Hartman–Keller–Stoica, Mazáč analytic functionals, spinning bootstrap) — score 3
- Mechanism: unitarity (positive spectral density) + crossing/modular invariance ⇒ linear functionals with sign give
  bounds; crossing is an exact functional equation coupling light and heavy states.
- Action: the explicit formula is a crossing equation (primes ↔ zeros, FE as S-transform). Clause 5 asks exactly for a
  coupling of small primes with the FE not through ζ(½+iτ): crossing-kernel functionals (Mazáč–Paulos) are such a
  coupling. New vs. frentes L/N: those built *magic functions* (V1–V3) for sphere-packing LPs; HKS-type bounds use the
  *light-spectrum sparseness* hypothesis, which here is "comb supported on log n, n<e^{2T}" (a finite light spectrum).
- Screen: a functional valid for all positive light spectra is CG (B″) and dual-certificate class (D) — likely REF-D.
  Only escape: functionals that use integrality of light dimensions (log n) and conductor 1 jointly (cor:shape (b)).
- First theorem: write 𝔞_T on P_T as a crossing equation with "light sector" {log n: n<e^{2T}}; prove whether an HKS
  universality bound for the heavy sector holds for every comb (then NO-GO, index it) or needs Λ exactly.

### B4. Proof mining (Kohlenbach) / reverse mathematics of the window statement — score 6 for a meta-result, 0 for sign
- Mechanism: logical metatheorems extract uniform rates from ∀∃ proofs; WP_T is Π⁰₁ for each rational T.
- Action: turns lem:shape-est(iv) ("no estimate carries the sign", ARGUED) into a PROVED statement for proofs in a
  declared formal system (e.g. a monotone functional interpretation would extract a margin ≥ explicit f(T), which
  contradicts thm:margin if f decays slower than e^{−15.449T}). Gives a sign-free but honest closure tool.
- Screen: not a sign carrier; it is a classifier of method classes (closure by impossibility
  within a declared class).
- First theorem: in WKL₀/ACA₀ with an "estimate" schema formalised, any proof of WP_T for all T ∈ [1,2] yields a
  computable margin bound m(T) ≥ g(T) of extractable form; with thm:margin, classify which g are excluded.

### B5. Resurgence / exact WKB / Stokes constants of the window operator at large T — score 3
- Mechanism: transseries of the bottom eigenvalue; Stokes constants are sign-definite in many integrable problems;
  median resummation preserves reality.
- Action: λ_A(T) ≍ (bounded by) e^{−15.449T} is an exponentially small eigenvalue — the natural object of exact WKB
  (instanton splitting). Archimedean Γ-factor is resurgent (Stirling); prime atoms enter as discrete instantons at
  log n. Clause 5: Stokes data couple the Γ-factor (FE) with atoms log n directly, not through ζ(½+iτ). Not in index
  (WKB/resurg absent; L41 spheroidal asymptotics is only the prolate piece, covered).
- Screen: the leading instanton action is probably comb-generic; sign would sit in a Stokes constant depending on the
  exact vector (Λ(n)) — admissible in shape, unproven to exist.
- First theorem: for the two-atom model (n=2,3, T∈(½log3,½log5)), compute the transseries of the bottom of 𝔞_T and the
  first Stokes constant exactly; test its sign under O2/O4^ε.

### B6. Other fields swept — low scores (0–2), recorded so they are not re-surveyed
| Field | Mechanism | Why low (screen) | Score |
|---|---|---|---|
| Geometric Langlands proof (Gaitsgory et al.), categorified trace | trace of Frobenius = functions on Bun_G; positivity absent | function field / no Spec ℤ object (family "cuerpos de funciones" closed); no sign | 1 |
| Fargues–Scholze geometrization | local Langlands over ℚ_p | local, Satake-wrong-side (G4H-R160_S1 #27) | 1 |
| Lurie tempered cohomology | equivariant elliptic/tempered characters | no positivity mechanism; character identities CG | 0 |
| Shifted symplectic / DAG | (−1)-shifted structures, DT sheaves | sign = orientation choice; no global object (MW-5) | 1 |
| GW/DT positivity | enumerative counts ≥ 0 | needs a CY object over ℤ (MW-5 / G-F hole) | 1 |
| Topological recursion | spectral curve → correlators | Weil form has no spectral curve with known sign; CG | 1 |
| Amplituhedron / positive geometry | canonical forms positive on positive Grassmannian | positivity of Plücker coords ≈ TP (closed family) | 1 |
| Spectral networks | BPS counts | no input; same as WKB but less concrete | 1 |
| Arithmetic QUE (Lindenstrauss, Soundararajan) | entropy + Hecke recurrence | Hecke multiplicativity on σ_T is CG (frente A, PROVED); equidistribution is an estimate (B′) | 1 |
| Bhargava geometry of numbers | counting orbits, positive density | estimate (B′); sieve-type; densities cancel (frente M) | 1 |
| Model theory of exp (Zilber, Wilkie) | quasiminimality, Schanuel | no ordering/sign; o-minimal sister closed | 0 |
| Optimal transport (displacement convexity, LSV) beyond P33-11 | convexity along geodesics | entropy/Wasserstein reformulate (P33-11); LSV on log ℕ-graph unexplored but same as B2 | 2 (fold into B2) |
| Ricci flow / Perelman entropy / monotonicity | monotone functional in a flow parameter | flows in T: bootstrap-in-T closed (G3E-159), margin class W2; monotonicity = Problem SPEC_A | 2 |
| Kähler packages for non-algebraic objects (Adiprasito–Huh–Katz beyond matroids, Babaee–Huh currents) | Hodge–Riemann | P41-2 NO-GO (Babaee–Huh obstruction) | 0 |
| Crystalline measures / Kurasov–Sarnak | positive crystalline measures are Poisson-like | L60 low; positivity of zero side only (C_zeros) | 1 |

## C. Ranking (top 5)
1. **B1 hyperbolic/stable/interlacing on Euler-product vectors** (4) — fits the PROVED separability reduction; first
   theorem finite and algebraic; either a mechanism or a clean NO-GO.
2. **B2 Bakry–Émery Γ₂ on the Markov semigroup** (4) — the only lower-bound-on-bottom tool that is quadratic in the jump
   measure; cheap O2 screen first.
3. **B4 proof mining of "no estimate"** (6 as meta, 0 as sign) — upgrades lem:shape-est(iv) ARGUED → PROVED for a
   declared formal class.
4. **B3 modular/conformal bootstrap crossing functionals** (3) — direct candidate for clause 5; high REF-D risk.
5. **B5 resurgence/Stokes constants** (3) — natural for an exponentially small bottom; clause-5 coupling Γ ↔ log n.

Every construction brief for these must include the "no reintentar" rule and this index path, and must run the
thm:shape (A) screen (O1–O6, O2, O4^ε, Beurling, Epstein x²+5y²) before any construction.

Web check (2026-10): no 2024–2026 paper found applying B1–B5 to the Weil form (search hits only 2608.24827, already L14,
and modular-bootstrap papers e.g. arXiv 2503.23761 unrelated to ζ).
