# Cross-check annex — Lorentz-type signature and mechanisms with closure rules (part 2: stability, Lee–Yang, Laguerre–Pólya, total positivity, closure under product or convolution, flows)

Read-only cross-check. It proposes no constructions. Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`.
Labels are quoted as each source declares them; where a reading of my own is added it is marked ARGUED.
When a source uses an equivalence of the target with another statement, this is recorded as "uses an external
equivalence" and not developed.

## 1. What was searched and what was opened

**Search.** Case-insensitive grep in `03-research/` (all phases), `04-papers/`,
`00-references/`, `05-meta-and-planning/` (index, audits, `SURVEY_MODERN_UNTRIED.md`, crossword, master
grid) for: Lee–Yang, Lieb–Sokal, Newman, GKS, FKG, Griffiths, ferromagnet, stable polynomial, stability
preserv, hyperbolic polynomial, Gårding, Borcea, Laguerre–Pólya, multiplier sequence, Pólya frequency, PF_,
PF₂, PF∞, total(ly) positiv, variation diminish, Schoenberg, Karlin, log-concav, Prékopa, Brascamp, de Bruijn,
heat flow, infinitely divisible, Lévy–Khintchine, Hermite–Biehler, Jensen polynomial, interlac, Turán.
Result: 661 .md/.tex files with at least one match. Concentration: phase 102 (39), Paper 47 (37,
almost all in `main_pre_*` copies), 159 (33), 60 (24), 193 (19), 186 (19), 162 (18), 160 (18), 106 (18), 116 (17),
103 (16), 114 (15), 211 (14), 212 (14), Paper 48 (12), index (10), phase 33 (10). Warning: the pattern
"rding" of Gårding matches "regarding"; the matches of phases 114/116 for that term are
false positives (checked). The genuine Gårding matches are in 195 INV_M_001, 201
FAMILIES_A_001, 204 TRACT_D, 106_25, 54 and the index.

**Opened as primary sources (36).** Mandatory (9): README, OBJECT_SPEC, LEDGER, BRIEF_CONSTRUCTOR, REVIEW_003,
REVIEW_004, ROUND_004_E, ROUND_003_8 of this folder; `phase-211/STATEMENT_001.md`. From this part (27):
`phase-70-lee-yang-dbn/README.md`, `E70_2_RESULTS.md`; `phase-11-hyperbolicity-total-positivity/README.md`;
`phase-194-invention/INV_F_001`, `INV_A_001`, `INV_I_001`, `AUDIT_194.md`; `phase-65-signature-continuity/README.md`,
`M3`, `D7`, `D10`; `phase-137/R137_005_ROUND3.md` §1; `phase-159/G2_B8_R1.md`, `G2_B8_R5.md` (and R3/R4 by grep);
`phase-104/104_21`, `104_83` §2; `phase-60-discriminant/H1_PROOF.md`; `phase-155/R155_046` (table N3);
`phase-211/POWER_FOUR_TURAN_084.md`; `04-papers/47-row-d-dual-certificates/main.tex` (rem:PF2, prop:spec (6),
inertia and interlacing passages); `phase-195/INV_M_001`; `phase-193/CA_J_002`; `phase-201/FAMILIES_A_001`,
`FAMILIES_B_001` (by sections); `phase-200/SPEC_SIGN_OBJECT_011` (by sections);
`phase-116/previous-phase-114/114_d_99`; `phase-162/R162_1602`; `phase-197/BARRIER_W_001`;
`phase-168/R168_203`; `phase-102/120_TOTAL_POSITIVITY_AND_LI_SEQUENCE_AUDIT.md`; index `03_PHASES_000-099`,
`04_PHASES_100-189`, `AUDIT_A.md` (rows A14a), `06` (row 215), grid and crossword (only lines by grep).

**Not opened as primary sources.** Phases 8 and 33 (heat flow / de Bruijn–Newman constant: only via index
N6, ES-15, NG-B5, G8E); phase 28 (log-concavity in σ, via NG-D1/D2); 106_98–120 (heat flow of the
prime–Gamma form, via grid G3E); 103_15–42 (log-concavity of the theta measure, via grid G1F); E70_10–12 (via
`ROUND_003_8.md`, which opened them); 211 POWER_RECIPROCAL_* (via the project rules and the memory of selections);
186 (PF_ and Lévy–Khintchine matches); 154 (bibliographic readings); 160 (surveys); Papers 46 and 48;
`SURVEY_MODERN_UNTRIED.md` (grep only); `00-references/` (grep only; preprints not opened).

## 2. Inventory

Column "acts on": the object to which the closure rule or property is applied.

| # | File and section | Object constructed | Declared label | Acts on | Where and why it stopped |
|---|---|---|---|---|---|
| 1 | `phase-70-lee-yang-dbn` README, E70_1–2 | heat flow on the kernel of the completed function; monotonicity of Nevanlinna positivity in the parameter | NUMERICAL; index P70: CIRCULAR | the completed entire function and its logarithmic derivative (zeros) | uses an external equivalence; the monotonicity goes in the already known direction; reduces to Cauchy–Weil positivity (E70_3–4) |
| 2 | `phase-70` E70_10–12 (via ROUND_003_8) | Riccati factorization δV + V² = Z⁻¹δ²Z in the semigroup algebra | PROVED as an identity; no sign | Dirichlet series as an operator (Z, V = Z⁻¹δZ) | "entirely on the Euler side"; the Hermitian square produces V*V with a comb of ratios of positive sign; with Z_c = Σd_c(n)e_n the identity holds for cΛ |
| 3 | `phase-11` README, M11.2–M11.5 | Jensen polynomials, interlacing, Borcea–Brändén preservers, MSS | NO-GO; arithmetic blindness PROVED/ARGUED | Taylor coefficients of the entire function (Laguerre–Pólya class) | uses an external equivalence; the preserver (derivative) preserves the class for every function (control cos t); hyperbolicity is equivalent to PSD of Hermite forms |
| 4 | index N6, ES-15, NG-B5, G8E (phases 8, 33, Paper 13) | heat flow, Lyapunov identity | NO-GO / DEAD | the completed entire function | uses an external equivalence; monotonicity does not fix the terminal parameter; the Lyapunov identity holds for every symmetric configuration (blindness) |
| 5 | grid G3E (106_98–120) | heat flow of the prime–Gamma form | DEAD | the form | no uniform sign (heat order, not uniformity); not opened as primary source |
| 6 | grid G1F (103_15–42) | log-concavity of the theta measure | DEAD [F3] | a measure (theta) | generic positive kernels with zeros off the axis: the property does not separate |
| 7 | `phase-102/120` | total positivity / PF / log-concavity of the Li sequence | audit, no closure | coefficients of the transformed logarithmic derivative | uses an external equivalence; remains a reformulation |
| 8 | `104_21` | compound Poisson arithmetic law on exponents; tests PF₂, TP, complete monotonicity | NO-GO (PROVED with rational minor) | a product probability measure over primes (independence = closure under product) | the kernel on the exponent lattice fails PF₂ by a two-prime minor; the completed cocycle fails complete monotonicity |
| 9 | `104_83` §2; AUDIT_A A14a-1/2; P47 rem:PF2 | Pólya order of the kernel Φ; PF₂ of K(\|·\|) | A14a-1 NO-GO (CITED, PF₅ fails); A14a-2 OPEN (PF₄); rem:PF2 PROVED | de Bruijn–Newman kernel Φ; archimedean kernel K of the form | Φ is not PF∞ (Schoenberg); K is completely monotone ⟹ log-convex ⟹ not PF₂; P47 leaves OPEN whether the transition density of the semigroup C₀ + Lév is PF₂ |
| 10 | `R155_046` N3 | nodal method / Karlin | PROVED (half of the kernel); semigroup t ≥ 1 HEURISTIC | kernel K and associated semigroup | K not PF₂; oscillation route closed for the kernel |
| 11 | `R162_1602` K1–K3 | resolvent and short-time semigroup of A_T; nonlocal Courant identity | NO-GO PROVED (K2 PARTIAL) | operator of the form a_T (resolvent) | no resolvent or short-time semigroup is TP₂; the obstacle is the jump structure, not the comb; Λ∗1 = log does not restore TP₂ |
| 12 | `114_d_99` | matrix Picone; total positivity of the jumps | audit, NO-GO of hypothesis | jump kernels of the form (translation by a prime, Gamma density) | negative 2×2 minor in the translation by a prime; Gamma density log-convex; the rank-two majorant is equivalent to primitive positivity (circular) |
| 13 | `ROUND_004_D` Lemma C (R4-e) | 𝖡 as a kernel | PROVED | the function 𝖡 of a profile | 𝖡 is not totally positive, nor Pólya, nor a Laplace transform on (0,∞) |
| 14 | `211/POWER_FOUR_TURAN_084` (+082, 083, 085, 090, 097) | four-node Pfaffian criterion, Turán-type inequalities | PROVED as a criterion; exterior application; higher orders open | kernel of the power ladder | finite order to finite order; inheritance falsifier (the scalar properties with RS = x do not suffice); no induction on the order |
| 15 | `phase-159/G2_B8_R1–R5` | Euler factors as locally stable objects (Lee–Yang in x = p^{−s}); Lévy–Khintchine distribution of the archimedean place among primes; Theorem D (minimax), L″ | PROVED (L″ machine-verified, without intervals); index G4A: DEAD | **local forms q_p of a_T on P_T**, combined by sum; individual Euler factors | there is no local certificate for T > 0.5925: positivity is sign interference between primes inside an autocorrelation; factor-by-factor operations do not see it. Theorem S (Satake torus) uses an external equivalence in its item (ii)–(iii) |
| 16 | `phase-195/INV_M_001` M1–M2 | multiaffine polarized symbol by prime blocks of 𝔸 (S-smooth); real stability, Gårding cones, interlacing families | NO-GO PROVED | **the form 𝔸_M / 𝖡 in per-prime variables** | p_𝖡 is not real stable (explicit witness); Gårding = PSD reformulation; MSS with the wrong quantifier. Survives cΛ with c near 1 and a_P (screen §6) |
| 17 | `phase-193/CA_J_002` 1.3, 2.1–2.3 | GKS/Griffiths, Ginibre, GHS, FK on 𝔸_M; FKG on the divisor lattice | NO-GO PROVED | **the matrix 𝔸_M** as Hamiltonian or covariance | frustration: cycle with + additive edges and one negative · edge (𝔸_{m,2m} < 0); FKG: Euler tests are the equality class |
| 18 | `phase-201/FAMILIES_A_001` A1, `FAMILIES_B_001` F2–F3 | Lorentzian polynomials / log-concavity; correlation inequalities; Lee–Yang–Newman | NON-VIRGIN; NO-GO by citation | sequences (Λ(n)/√n, c_N); spin measures | log-concavity of a weight sequence is a cone condition; correlations dead by frustration; Lee–Yang requires a measure whose transform is the completed function (uses an external equivalence) |
| 19 | `phase-200/SPEC_SIGN_OBJECT_011` C8 | inventory of nodal counts (Sturm–Hurwitz, Pólya frequency) | class NO-GO ARGUED with two PROVED lemmas | translation kernels; nodal counts | PF fails at PF₂; generic counts on the comb |
| 20 | `phase-194/INV_A_001` | arithmetic Lévy structure; damped form 𝔞^{(ε)} (Cauchy subordination); conjectures Θ, Θ⁺ | Θ⁺ FALSE PROVED; Θ REF-D (AUDIT_194) | **the damped form** as a family in ε; Lévy measure of the series | Θ⁺ false: the coefficient c_F(log n) has a sign; Θ is positivity of the Poisson/Herglotz extension (uses an external equivalence via the spectral measure); the window is not preserved |
| 21 | `phase-194/INV_F_001` F0–F3 | transfer of cones by f ↦ −f′/f | PROVED (F1, F2, F3); OPEN non-conic residue | the series and its logarithmic derivative | see §4 |
| 22 | `phase-194/INV_I_001` | intersection of the orbits cΛ with integrality of coefficients | PROVED | coefficients b_n of f_a | {c : cΛ ∈ integer coefficients} = ℕ; {c : cΛ ∈ {0,1}} = {1} |
| 23 | `phase-60/H1_PROOF` | Perron–Frobenius for the localized form A_λ | PROVED at operator level (except for a finite-rank loose end); index P60-1 PARTIAL | **the form A_λ** (−V improves positivity because Λ ≥ 0) | gives simplicity and parity of the ground state, not sign; the mechanism is Λ(n) ≥ 0, preserved by cΛ (ARGUED here) |
| 24 | `phase-65` D0–D12, M3, D6, D7, D10; `R137_005` §1 | index-graded determinant, topology τ_κ, cone of index ≤ κ closed under Schur limits (shorting); κ(A_P) = 0 for finite P | DEAD at D8.5; R137_005: chain REFUTED (bifurcation: the bound and the identification live on different objects) | **signature of kernels of canonical systems** associated with the comb truncated at P, induction on P | uses an external equivalence (continuity of signature ⟺ the target, in its own terms); the index-0 closure is PROVED but the convergence of the renormalization is the wall; κ(A_P) = 0 comes from Λ ≥ 0, which cΛ preserves (ARGUED here); Davenport–Heilbronn falls by signed weights (D10) |
| 25 | P47 thm:parityschur, prop:polarcap, inertia passages; `ROUND_004_E` (R4-f) | n₋(W_T) = n₋(a_T\|P_T) + n₋(𝔊_T); polar block with signature (1,1); inertia arithmetic, Haynsworth, interlacing | PROVED; class NO-GO (R4-f) | **signature of the form a_T and of its polar border** | indices constant for \|c − 1\| < λ_A(T)/Σ\|v_n\|: a count does not distinguish c = 1; P47 shows that inertia arithmetic holds verbatim for forms with added quartets |
| 26 | `phase-197/BARRIER_W_001` W1–W3 | monotonicity of n₋ in T (extension by zero), homotopy of combs, spectral flow, codimension | PROVED (W3 ARGUED at the level of forms) | **signature of a_T, induction on the window** and on the comb | every invariant of class 𝒮 (extension by zero, concavity, continuity, parity, compact resolvent) holds for a_P, truncations, O_4 = cΛ, O_6 and Beurling; the only datum that reads Λ is the Hellmann–Feynman pairing with the minimizer |
| 27 | `R165_201` (via grid G7A) | critical interlacing ⟹ quartet outside the cone | DEAD, refuted | zeros of model functions | uses an external equivalence; refuted by a sin–cos counterexample |
| 28 | `R168_203` | local Laguerre inequality | OPEN, NEGATIVE answer | the completed entire function near a quartet | uses an external equivalence; logically independent conditions |

## 3. Precise answer

**Is there a closure mechanism applied to the form a_T or to its signature, with induction on primes or on the window?**
Yes, several, and all of them stopped:

- Induction on the window, on the signature of a_T: BARRIER_W_001 (W1: n₋ does not decrease in T; W2: homotopy of
  combs; W3: codimension). This is the closure rule "extension by zero" plus concavity. NO-GO: the five
  structural properties hold for cΛ, a_P and Beurling systems.
- Induction on primes, on a signature: phase 65 (cone of index ≤ κ closed under Schur shorting and
  under limits; κ(A_P) = 0 for finite P). It acts on kernels of a canonical system, not on a_T
  directly; the chain was REFUTED in R137_005 and uses an external equivalence.
- Factor-by-factor closure, on local forms of a_T: G2_B8 (Lévy–Khintchine, local stability, Pólya–Schur).
  The rule combines local forms ≥ 0 by sum, not by product; it fails for T > 0.5925 because the sign is
  interference between primes.
- Real stability / Gårding / interlacing on the multiaffine per-prime symbol of 𝔸: INV_M_001, false.
- Ferromagnetic correlations on 𝔸_M: CA_J_002, frustration.
- Total positivity / Karlin on the kernel of the form, its resolvent or 𝖡: P47 rem:PF2, R155_046, R162_1602,
  114_d_99, ROUND_004_D. Fails already at order two. Remains OPEN in P47 only whether the transition density of the
  semigroup C₀ + Lév is PF₂.
- Perron–Frobenius on the form: H1_PROOF, gives simplicity and parity, not sign.
- Inertia arithmetic: P47 thm:parityschur, ROUND_004_E. It is constant near c = 1.

**Does any of them break for c = 2 because of the fixed archimedean factor?** None was found. No source in this
part treats c = 2 as a falsifier of a closure mechanism. c = 2 appears only in INV_I_001 (the
integrality of coefficients admits exactly c ∈ ℕ, so a mechanism that uses only the Euler product and
integrality survives c = 2) and as a NUMERICAL control in REVIEW_001_ABD and ROUND_003_2. In the sources, the
mechanisms that read the comb do so through Λ ≥ 0 (phase 65, H1_PROOF, G2_B8) or through closed classes that
contain cΛ (BARRIER_W_001, INV_M_001 §6, R4-f). That the archimedean factor stays fixed while the comb
scales appears as a fact in INV_F_001 F2 and in P47 lem:shape-scale, but never as the line where a
closure mechanism breaks.

## 4. Scope of the ∂log wall (INV_F_001; OBJECT_SPEC O10)

Exact hypothesis of Theorem F2: premises of the form "log ζ ∈ K" or "−ζ′/ζ ∈ K′" on Re s > 1, with K, K′ cones
(closed under multiplication by c > 0), together with generic identities on the comb. The conclusion is that
all such premises hold for ζ^c, whose comb is cΛ.

**Reached by the wall:**
- infinite divisibility and Lévy–Khintchine of the series (C2, C5, C10; INV_A_001 §0, Prop. 4.1);
- positivity of the coefficients of −f′/f;
- Bochner in t of φ_σ;
- log-concavity or log-convexity used as the sign of (log f)″ (C9, C11), because it is a cone condition on log f;
- every "closure under product" of Euler factors whose conclusion is a conic statement about log ζ (the
  product of ID factors is ID; that is exactly the rule the wall declares blind to c);
- the compound Poisson measure of 104_21, when read as a property of the log of its generating function;
- the Pick / Laguerre–Pólya cone of the completed function (C6–C8). This one crosses ∂log, but is only verified on
  σ > 1 and its transport to the line is REF-D (uses an external equivalence).

**Not reached by the wall (formally outside its hypothesis):**
- Signature or positivity properties of the form a_T, of 𝔸_M, of 𝖡 or of the ladder kernel.
  a_T^{(cΛ)} = Arch − cΠ is not c·a_T, because the archimedean term does not scale. A statement about its
  signature is not a conic premise on log ζ. This includes the Lorentz signature per parity sector,
  the cones of index ≤ κ (phase 65), the total positivity of K, 𝖡 or the resolvent, the real stability of the
  block symbol, GKS on 𝔸_M and Perron–Frobenius on A_λ.
  But all of these were closed for other reasons (§2 rows 9–17, 23–26), and BARRIER_W_001 together with R4-f
  cover the index invariants definable in class 𝒮 or constant near c = 1.
- Integrality conditions: the set of integer coefficients is not a cone (INV_I_001: its intersection
  with the orbit is ℕ, not ℝ₊). It is not a conic premise, but it does not separate c = 2.
- Lee–Yang spin measures (Newman, Lieb–Sokal) defined from the form and not from log ζ. They are not
  reached by F2, but in the corpus they appear only as a citation (201 F3) or dead by frustration (CA_J_002).
- The conclusion "every positivity that crosses ∂log is ID or Pick" is labelled ARGUED in P47 prop:spec (6)
  beyond the classified list. The list is PROVED in INV_F_001.

Reading (ARGUED): the wall blocks the closure mechanisms that operate on the series or its logarithm. It does not
by itself block those that operate on the form with the archimedean factor fixed. Those are closed in the corpus
by their own falsifiers: PF order, frustration, non-stability, class-𝒮 invariants and constancy of
inertia near c = 1.

## 5. What was not found (without claiming novelty)

1. A closure mechanism under **product** of Euler factors (not under sum of local forms, as in G2_B8)
   applied to the **signature** of a_T, with induction on primes and the archimedean factor treated as fixed.
2. Any mechanism in this part whose breakdown has been checked or sought at c = 2 (or at integer c ≥ 2) because of the
   fixed archimedean factor.
3. Stability preservers of Borcea–Brändén type applied to the symbol s_T or to the form a_T. They appear only
   on the completed function (phase 11) and on the block symbol of 𝔸 (INV_M_001).
4. Measures with the Lee–Yang property constructed from the form, and the Newman or Lieb–Sokal closure under
   ferromagnetic coupling applied to them.
5. Multiplier sequences (Pólya–Schur) acting on the weights Λ(n) or on the coefficients of the comb
   as a closure operation. Pólya–Schur appears only factor by factor in G2_B8.
6. Prékopa–Leindler or Brascamp–Lieb applied to the form. There are only mentions in lists (201, annex 193).
7. Gårding hyperbolic polynomials in the parameter T or in the weight for det of window matrices. Gårding
   appears only as a PSD reformulation in INV_M_001 §3.
8. Total positivity of the transition density of the semigroup C₀ + Lév. It is OPEN and declared so in P47
   rem:PF2; no attempt was found.
9. PF₄ and PF₃ of the kernel Φ: OPEN (A14a-2), no attempt in the corpus.
10. GKS/FKG-type correlations closed under product of per-prime measures, applied to a measure constructed
    from a_T and not from 𝔸_M. CA_J_002 treats 𝔸_M on integer sites; FKG only on the divisor lattice.

The absence of textual matches does not prove that these ideas are new or that they are useful.
