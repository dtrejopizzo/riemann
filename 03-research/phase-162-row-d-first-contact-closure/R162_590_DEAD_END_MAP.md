# R162_590 — Row D dead-end map (audit)

Purpose: stop new work from repeating tried routes. Read-only audit. No sign is claimed.
Sources: R160_020 (map), R160_002, R160_S1–S5, R160_010, R160_D2/D4, R160_HANDOFF, phase 150–161
READMEs/syntheses, PATH-TO-D, ROW-D-REDUCED-STATEMENT, phase 162 README and R162_1xx–4xx.

Falsifier key. **F1–F4** = phase 162 mandatory tests (README): F1 spectral (holds on λ>0 eigenvectors),
F2 orientation (A_M→−A_M invariance of the (PC) square), F3 arithmetic (a≠Λ with a*1≠log, finite
modifications, Epstein/DH), F4 linear (PC-ren) graph limit. **Φ** = corpus falsifier family: Λχ₂, Ξ_a, Ξ_Q,
DH/Epstein, Beurling systems, comb models (finite deletion/amplification). **E1/EQUIV** = the target is an
equivalent form of RH (not a falsifier kill, but no progress). **M** = Theorem M (margin ≤ exp(−exp((2−ε)T))),
so no gap/compactness argument can work.

## 1. Tried mechanisms

### 1a. Arcs I–VIII (phases 0–151), compressed (R160_020 §2, S1–S4)

| mechanism | where | why it failed | killer |
|---|---|---|---|
| Per-place / per-prime positivity, OS per prime, semilocal finite S | arcs I, VIII; L-2, L-6 | positivity never prime by prime; finite S does not pass to the limit | Φ (comb models), E1 |
| Kreĭn E*JE, de Branges, canonical systems, global square A*A | arcs I–II; phase 120 (C.1) | equivalences; global square is EQUIV in force | E1 |
| dBN flow, Jensen, hyperbolicity, Lee–Yang, Pólya–Schur | arcs I, IV; phase 159 G2 | arithmetic-blind (S-15, N5, U-9) | Φ (DH, Ξ_a) |
| Li/Keiper, Nyman–Beurling, KEP, Herglotz, κ=0 | arcs II, IX; D4 Thm 4.2 | EQUIV; Li kernel lies on polar boundary δ=0 | E1 |
| Pontryagin index κ=2m, m<∞⇒m=0, APS/η, Maslov, LP-112 | arc II | detectors, no forcer | E1 |
| Statistical: density, proportion on line, PNT, zero-free regions, sieve upper bounds | arcs I, X | give proportion/density only | M, Φ |
| Finite-field transport (Hodge on C_p×C_p, Doc 125, Deligne extraction) | arcs III, VIII; phases 144–149 | no transport to Spec Z; rationality wall (six exponentials) | T1/T2, rationality wall |
| Unitarising metric, installed zeros as spectrum, crossed products/KMS | arcs III, X; phase 158–159 G1 | the metric is the Weil form itself | T1, OT-5′ walls |
| CCM/Ω₇/A1/EG_LOCK, adjugates, cofactors, Doob operator | arcs IV–V (60–106) | the decisive datum reappears as an equivalent condition | E1 |
| Real-valued h⁰ / Riemann–Roch (Connes–Consani) | phases 135–140; S-11 | excluded domains (Thm 19.25, Cor 19.25b) | S-11 |
| Direct virial/Mourre on collar residual | P124_007 | projected virial cancels in the Tate projection defect on first-contact vectors | F1 (exact cancellation) |
| Window variation / retard range / Toeplitz leakage | P124_004–010 | shorting estimate not provided; needs external centering | F1 |
| Negative-witness normal form + opposite-metric trace (F2 arrow) | phase 121 | conservation law missing; F2 equivalent in force to global square | E1 |
| Locality–phase–sign trilemma lifts | phase 120 | common-failure theorem | trilemma |
| Tropical/mixed effectivity, Künneth, finite-S factorisation, nonnegative family | phases 141–149 (Paper 47) | no-go theorems T1+T2+T5+polar/entire | T5, polar/entire |
| Beurling T3, Laumon one-round dictionary | phase 150 | T3 conditional; Laumon inherits rationality wall | Beurling (Φ) |
| Summand vs numerator axis, dlVP | phase 151 | dlVP capped by archimedean density | M |

### 1b. Arc IX–X (phases 152–161)

| mechanism | phase/file | why it failed | killer |
|---|---|---|---|
| FUP / Dolgopyat, Berkovich–Poineau | 152 | Hecke operators unbounded on relevant states (R152_002) | no form |
| Cross-term identity for Ξ_a (Thm A), single-pair, needle | 153 | separates ζ from Ξ_a only; short support = concentration | Ξ_Q, Beurling |
| Finite dual certificates, flat-top LP, Theorem Z | 154 (Paper 46) | no attained dual; no finite truncation; no induction in T | Thm finZ, M |
| Flat-kernel criterion, TK/N/N′, lattice classes M≤24, AL (retracted→AL′) | 155 | class-dependent ceilings; lattice loses Θ(1/M) | TK ceiling, arena ≥12 modes |
| Archimedean positivity | 155 | indefinite from T≈0.58–0.60; primes must create sign | prop:archneg |
| Kreĭn indeterminacy | 155 r5 | RH ⟺ indeterminacy; restatement | E1 |
| Per-window converse primitive→complete | 156 | 2×2 polar-capacity condition; fails in comb models | Φ (combs) |
| New mechanisms under F1–F5 filters | 157 | no survivor with an object | F1–F5 |
| MW-5 / OT-5′ object, adèle class space | 158 | restatement | E1 |
| G1 objects (scaling site, laminations, Borger/Witt/Bost–Connes, motives, Arakelov, operator algebras) | 159 G1 | walls: not prime-local, not algebraic, not covariant, not crossed product | OT-5′ walls |
| G2 (bootstrap in T, SOS, Hermitian squares, finite/random zero universes, mollifiers, jump calculus) | 159 G2 | every ∀T target = von Koch/KEP/κ=0/Weil; twist-covariant args dead | M, I-13, E1 |
| R1 memos C1–C8, M1–M10 | R160_010 | max 3/10; identities hold verbatim for falsifiers | Φ |
| C1 Holomorphic lamination | R160_C1 | one pole ⇒ ≤ one pair of L² zeros (Thm Z) | Thm Z |
| C3 / D2 Meyer H¹, homogeneous and non-homogeneous positivity | R160_C3, D2 | Thm H: off-line blocks in radical; D2: every transfer is RH (G1 collapses to G2) | Thm H, Thm T |
| C8 ε-phase | R160_C8 | Thm 1 verbatim for Λχ₂, Ξ_a | Φ |
| M7 bilinear (operator calculus) | R160_M7 | Thm 4 = eq:form rewritten | E1 (restatement only) |
| M8 two-variable 𝒲₂ Schur | R160_M8 | plus sign is the sign of a square: sterile | Φ |
| D4 ring datum Λ*1=log via tests (dilations, Chebyshev completion, Z[Q_{>0}]) | R160_D4 Thm 5.1 | any convolution identity on tests is a window shift at T+½log X | Thm 5.1, Cor 5.2 |
| Finitely many exact values of Λ | D4 Cor 5.2, U-11 | finite-codimension perturbation flips sign | F3 |
| Sum×product square, generic/scalar/positive-fibre | 161 R161_001–004 | canonical square contains square of truncated Weil operator: sign-blind | F2 |
| Product-Hardy ports, graph decomposition | R161_008–011 | claimed closure retracted; reduces to Sonin range intersection (4.2) | open (4.2) |
| Linear completion of scattering defect | R161_017–018 | tautology [ζ,D_Γ]=0 | F4 |
| Direct Markov pullback | R161_016 | automatic decreasing-norm direction; reverse typing needed | F1 |
| Conjugate test Π_T P_T Z*g | R161_022–023 | recombines tautologically into (PC-ren) | F4 |
| Raw prime contacts / moving discrepancy | R161_027–029 | indefinite cross terms; = reverse-Markov gate | F2 |

### 1c. Phase 162 (Gate 1), all rounds

| mechanism | file | why it failed | killer |
|---|---|---|---|
| Minimality / window shrinking | R162_101 | zero first variation; Hadamard inequalities hold for λ>0 | F1 |
| Gamma-residue uniqueness | R162_102 | trivial; interior uniqueness FALSE for DH | F3 (DH mode) |
| First chamber 0.8<T_*<½log5 | R162_103 | finite-modification models a^κ have genuine first contacts | F3 |
| ESB / Euler-stripped Hardy bound | R162_201, 203 | equivalent to Gate 1 on first-contact class | E1 (reformulation) |
| Multiprime Sonin leakage | R162_202 | PC-ren upper bound open; same content as ESB | E1 |
| Regularised critical jet | R162_204 | invariant under every finite modification of Λ | F3 |
| Ward defect B_a=DS(a*1−log) in Green law | R162_205 | linear, flips under η→−η, zero at a=Λ | F2, F3 |
| Complementary Poisson sum (PC+) | R162_206 | algebraic zero difference with (PC−) | F4 |
| Nonlinear two-parameter Euler/source curvature | R162_207 | flat; no stationarity | F1 |
| Noncommutative Euler-root lift | R162_301 | leakage symbol-independent (Brown–Halmos); anomaly not Λ-specific | F3 |
| Coefficient law ‖R_LF‖²=ε∫c_Fκ_L; (A)+(B) | R162_302, 304 | (A)+(B) ⟺ K^ε={0} | E1 |
| Exterior Ward | R162_305 | derivative is algebraic zero; Ward meets δD only through ζ(−2j)=0 | trivial-zero cancellation |
| Certified numerics λ_A(½log5)>0 | R162_303 | pushes T_*>0.8047 only | M (not a mechanism) |
| Trivial-zero reflection / Hardy | R162_402 | dictionary proved; Hardy mechanism NO-GO | F1 |
| Log-weighted channel | R162_401 | cancels by [X,S_N]=−K_N | F4 |
| Smooth comb P | R162_403 | H^{(P)}=0 exactly; multiplier identities are symbol identities | F1 |
| Compressed kernel | R162_404 | Tate jets enter as λ⟨Γ_PF,φ⟩, vanish at λ=0 | F1 |
| Right minimality at T_*+δ | R162_405 | sign is monotonicity only | F1 |
| Chebyshev threshold across e^{2T_*} | R162_406 | Λ-specific edge coefficient vanishes at composite thresholds by Λ*1=log | F3 inverted (datum cancels) |
| (NE) collar nondegeneracy | R162_408 | proved, weight-blind; Conjecture 7.1 ⟺ no first contact | E1 |
| Local lower bound + virial law | R162_407 | under (REG), (LB) ⟺ 𝒱≤0 on N_{T_*}; weight-blind; DH has first contacts | F3 (DH) |

## 2. Routes marked untried/open in the surveys, not attempted in phase 162

Ranked by the survey's own novelty/falsifiability ordering (R160_020 §6, R160_010 round-2 table, S4 §5).
"Not in 162" means no R162 file addresses it.

1. **Signed bilinear inequality in the alignment band** (R160_020 Option 3; S4 §5.15; P47 Rem 27.15(42)).
   Heath-Brown/Friedlander–Iwaniec applied to the *quadratic form* on the low-frequency block of A_T|P_T, keeping
   Λ*1=log to the end. M7 only rewrote eq:form (restatement); the signed version was never built. First falsifiable
   lemma: signed bound uniform in T with main term a sum×product square, no gap used. Kill: any line valid for Λχ₂.
2. **D3 per-window converse, primitive→complete, T>0.8** (R160_020 Option 4; R160_010 D3; never written).
   Target W_*(Y_1) ≥ ⟨(A_T|P_T)^{-1}b_T,b_T⟩ under RD_T. Infrastructure, not endgame; phase 162 treats only the
   primitive form (R162_303 "W_T not treated"). Highly falsifiable (comb models, phase 156 2×2 condition).
3. **D5 spectral picture of A_T on L²(I_T)** (R160_010 D5; never written): λ₀=−(1+o(1))e^T with Perron/pole
   direction; the sign lives on the second eigenvalue of the complement. Not in 162.
4. **D1 Torelli-failing lamination with fixed points** (R160_020 Option 5; R160_002 C1; D1 never written).
   Only carrier class not excluded by Thm Z/Thm H. Highest cost, lowest falsifiability.
5. **M12 / ×p measure rigidity, Pila–Wilkie, model theory** (S4 §5.14; R151_005 §2.3; M12 partial). Never analysed
   against W_T; phase 152 ran only FUP/Berkovich.
6. **Laumon/ε-factor Fourier transport between additive and multiplicative squares** (S4 §5.12): never run 150–156,
   desk-excluded in 157. Note C8 (ε-phase) failed Φ; any rerun must avoid its Thm 1.
7. **Beurling gate T3 unblocked** (S4 §5.6): (H-DMV) now CITED; Beurling blindness test (P152.2) never applied to
   the phase-161/162 identities. Cheap falsifier check, not a mechanism.
8. **O-D4.2 kernel of 𝒲 / cone 𝒞′ on decaying tests** (D4 §6). Open; unbounded-support tests.
9. Minor open leads (restatements per window, value only across T): Kreĭn–Nevanlinna parametrisation of 𝔖(T)
   (S4 §5.7), polar capacity 𝔊_T across T (§5.10), canonical column s=½ as a family (§5.8), concave value function
   faces (§5.9, but M2 showed prime-blindness), hybrid N≥6 LP (§5.4), Doc 125 toy to semilocal S (§5.11),
   Paper 44 (H_L) and colimit Thm 8bis.4a (S3 L1–L2), semilocal Sonin count #{λ_j(K_I)>1} (S3 L7).

Already in progress in 161/162 (do not relist as untried): O-D4.1 / L161.3 oriented Poisson port, first contact
with δ_Λ=0 (R160_020 Options 1–2), global Sonin lemma R161_011 (4.2), reverse-Markov gate (R161_016).

## 3. Round-6 ideas against the map

**(V) Sign of the virial/dilation form on the first-contact kernel — ALREADY TRIED.**
- P124_007: projected virial on the collar residual cancels identically in the Tate projection defect on a
  first-contact vector; L_T≥0 gives no sign.
- R162_101: outward virial quotient a(F_s)/s; shrinking-window first variation is exactly zero.
- R162_302: the coefficient law is a virial-type law in the position direction, not the weight direction.
- R162_407 Thm 3.2 / Cor 3.3: under (REG), λ_A(T_*+δ)=−(δ/T_*)𝒱(G)+o(δ) and (LB) ⟺ 𝒱|_{N_{T_*}}≤0; with (NE,
  R162_408) this is exactly "no first contact". Weight-blind; DH has first contacts.
- Verdict: the sign of 𝒱 on N is Gate 1 restated (E1). Only admissible residue: evaluate the comb virial
  Σ v_n log n·c_G′(log n) with the Euler product entering *before* regularisation (R162_204 shows the regularised
  jet is invariant under finite modifications, so a post-evaluation use of Λ fails F3). Plus (REG) is unproved.

**(H) Hecke / prime-translation multiplicative equivariance of the Weil form at first contact — ALREADY TRIED (dead).**
- D4 Thm 5.1: span{τ_{log m}F : m≤X} = window at T+½log X and W is translation invariant; any identity on tests
  in Z[Q_{>0}] (Hecke-type prime translations) is a window shift; ∀X it is E1.
- D4 §6 / I-13: argument must not be twist-covariant; (Z2) is not (Thm 2.2(iv)); 159 G2 killed twist-covariant args.
- R162_401 ([X,S_N]=−K_N cancels the log channel), R162_403 (Dirichlet-multiplier identities are symbol identities,
  fail F1), R162_406 (Λ*1=log edge coefficients cancel at composite thresholds).
- Hecke operators proper: R152_002 (unbounded in p on the relevant states); 159 G1_P4_R4/G1_P1_R4 (self-adjoint
  Hecke on L²(Γ\𝔥) falls under exclusion K3); G1_B1_R2 Prop M (a useful + must be non-Frobenius-equivariant).
- Verdict: equivariance is precisely the property the walls say a mechanism must break. Do not pursue unless the
  step is explicitly non-equivariant.

**(S) O-D4.1 sum-product in one quadratic step at the kernel vector — ALREADY THE ACTIVE LINE; generic forms dead.**
- Phase 161 exists for this: R161_001 (joint Poisson–Chebyshev anomaly), R161_002 (canonical square sign-blind:
  contains the truncated Weil square — F2), R161_004 (scalar and positive-fibre completions closed; residual
  narrowed to L161.3 oriented first-contact Poisson port), R161_005–029.
- Phase 162 at the kernel vector: R162_204 (finite-modification invariance, Ward defect must enter before
  evaluation), R162_205 (Ward defect linear, sign-flipping, zero at Λ), R162_206 ((PC+) linearly dependent),
  R162_207 (nonlinear flat), R162_305 (only link is ζ(−2j)=0 after continuum renormalisation).
- Verdict: a new (S) memo is admissible only if its single quadratic step (i) is not the square of (PC)/(PC-ren)
  (F2), (ii) is not a linear graph limit (F4), (iii) breaks the trivial-zero/continuum-renormalisation cancellation
  of R162_305 or supplies the reverse-Markov typing of R161_016, and (iv) fails at a declared line for Ξ_a and DH.
  Otherwise it repeats R161_002/R162_205–206.

## 4. One-line rule for round 6
Before building, check the idea against §1c and R161_002/004/016/018: if its decisive line is weight-blind,
equivariant, linear in (PC-ren), a square of (PC), or evaluated after regularisation, it is already dead.

| Möbius-conjugation square / (B4.1) | R162_502, R162_701 | collapses via Z S² Z⁻¹ = M(Λ)+S²; (B4.1) ⟺ a_T(F)>0, equality on N | E1, F1 |
| O504.1 Perron–Tate angle | R162_702 | class 𝒞={a≥0, supp prime powers} contains κ-models with first contacts (Thm 2); only exact values separate Λ | F3, M |
| D3 Type-II exclusion by minimality | R162_703 | deletion model Λ1_{n≥5}: T_W≤0.4608<T* (cor:convfail), Type II generic | F3 |
| floor ledger / Stirling matching | R162_801 | Möbius automorphism + (PC) sawtooth + window shift; asymptotic use killed by L5 | F1, F2, M |
| T-evolution invariant (flux, index, pole matching) | R162_802 | holds for κ, finmod, DH; deletion model overshoots at 0.4608; Λ*1=log = window shift in the flow | F3, M, F4 |
| Laplace/Mellin transform in T (scalar + operator) | R162_803, G2_B7_R3 | Theorem G = Lagarias Herglotz criterion; first contact invisible to Φ | E1, F1, F3 |
| edge-trace identity O802.1 (Selberg in ε² sum channel) | R162_901 (Selberg already in R162_501) | difference channel uncontrolled; pole ε_c<1; noncommuting transfers | F2, E1, F3, M |
| Terminal value Conj 6.1 | R162_902 | ⟺ RH; unconditional half on record (R160_M4 B(i)); deletion model | F3, DH, E1 |
| nonlinear Möbius / Gram integrality / tensor lift | R162_903 | floors die in L²; log Z=M_T(Λ/log) terminating BCH; Cauchy–Binet unipotent; Moore collapse; Λχ₂, Beurling pass all | F1, F2, M |
| Fourier quasicrystal / crystalline rigidity | R162_1002, R157_002 row 42 | reality presupposed; one-member class (P2); local uniqueness fails (P3) | E1, F2 |
| tensor power / d→∞ limit | R162_1004 | ζ^d form = d·form; trick idempotent (q=1 at contact); dilation bound ⟺ RH; no independent a priori bound | F1, F2, E1, P149 |
| ×p rigidity on circle/torsion | R162_1001, R160_M12_R1 | window measures are trig polynomials → Lebesgue; Φ_Λ cocycle (new, separates Λχ₂/Beurling) pairs to prime term only (band-limited) | F1, F2, F3 |
| sum/difference resummation, Selberg Λ² sieve | R162_1003 | resums to Σ_ρ (Thm R, E1); Weil kernel Toeplitz not GCD (Prop 4.2); holds for DH | E1, F3 |
| Dirichlet character family / orthogonality | R162_1102, G2_B8_R2 | Thm O: sum over χ mod q has no arithmetic (any a); combinations re-index ζ data; full sum = ζ_{Q(μ_q)} (T1, open) | F1, F2, F3, M |
| torsion-atom tests (non-band-limited) | R162_1101 | port = torsion pairing (Thm 2.1) but pole at −2m reads only atom 0 (Thm 2.2, Li inversion); Riesz collapse → Sonin range (E1) | F2, F3, E1 |
| Laumon ε-factor transport | R162_1203 | L4–L6 missing; Thm W rationality/cohomology wall (finZ + sharp bound = RH); ε-data one scalar C₀; DH shares ε | F1–F4, E1 |
| odd-degree / self-referential functionals | R162_1202 | flatness (Thm A), parity (Thm B), polynomial collapse to Sonin range in any degree (Thm C) | F2, F3, E1 |
| Sonin range direct (Gamma-lattice linear system) | R162_1201 | (S_m) family ⟺ HF=0 (Müntz), Jordan resonance; Euler sums evaluate exterior field; holds for all models | E1, F1, F2, F3 |
| Kreĭn Jordan chains / CM of κ / Robin strings | R162_1301, R154_004, R155_046 | Robin-string form (Thm 1) new; isotropy = Gate 1; Douglas bound form (Thm 3) equivalent; DH still CM | F3, E1 |
| q-difference Riemann–Hilbert / dilation Galois | R162_1302 | maximal monodromy (Zariski-dense Euler curve), single additive eq., cut breaks action; separability shared by Λχ₂, Beurling | F1, F3, E1 |
| Douglas bound via Λ*1=log / ZXZ⁻¹ on Gamma rays | R162_1401 | log meets secular X only at pole s=1 (Tate ray, killed by primitivity); m≥1 rays scalar ζ(2m+1) factors; circular via Jordan partner | F3, E1 |
| Q-functions in T (Douglas constants, Markov–Kreĭn) | R162_1402 | monotone + collar laws; square-root law; finitely many moments cannot bound (Thm 5); reflection only rescales; all models | F3, E1 |
| comb spill via torsion cocycle | R162_1502 | C⁺u=−ZXZ⁻¹u on collar (new) ⟺ a=Λ, but bottom pairing pinned by weight-free eigen-identity (Thm 4); Λ-step inert | F2, F3, M |
| single Euler-channel scalar (R-B) | R162_1603 | positivity lock (Thm P): convergent Euler scalars all positive; Λ-specific block cancels at composite thresholds (R162_406); = Gate 1 on coherent class | F2, F3, E1 |
| oscillation budget via total positivity (Karlin/Courant) | R162_1602, R155_046 | resolvent/semigroup not TP₂ (K1); TP₂ ⟹ birth–death (K3); nonlocal Courant gives no budget (Prop C); comb breaks rearrangement | universal |
| B₂/sawtooth positivity on one-pole hyperplane | R162_1902 | B₂ weights cancel (Lemma C); value = Mellin symbol Re ζ (Prop Z), takes both signs (Gram failure, Prop I); linear in c | F2, E1 |
