# Annex — Relabelling of the candidates of phase 193

Object: the sign of the window form a_T on the primitive subspace P_T (target λ_A(T) ≥ 0 for all T),
treated only as a problem about that quadratic form. Sources: `03-research/phase-193-creation-campaign/`
(memos CA_*, seed tables CA_*_000, reviews CA_*_REVIEW, syntheses, `CAMPAIGN_LEDGER.md`),
`05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` (sections of phases 190–193 and re-examinations),
`AUDIT_PHASE193_CERTAINTY.md` («AUD», with its row number), `AUDIT_A.md`, `AUDIT_B.md` and `RULES_AVOID.md` §C.

Rule applied: a route is closed only by a proof of impossibility within a declared class of methods or by an
explicit falsifier. An exact reformulation is a valid target, not a closure.

Classes: **(a)** CLOSED–PROVED (explicit falsifier or proved class NO-GO; it is named) · **(b)** CLOSED only
ARGUED (it is said what is missing) · **(c)** EXACT REFORMULATION (valid target; it is said of which statement) · **(d)**
ONE LINE / examination insufficient to count as attempted · **(e)** OPEN residue.

Abbreviations: O1–O15 = modifications of P47 (P47 numbering, ledger errata, round 3); (B″) = identity
valid for every comb (lem:shape-ident, PROVED); (B′) = reading «no estimate carries the sign» (lem:shape-est (iv),
ARGUED); CIRC = death clause that in P47 is ARGUED/CONDITIONAL/OPEN (O11, O12, primitive O10, (B′)(iv), O4^ε/O5,
G1→(R)(10)); [crit] = precision screening M^{−3} (NUMERICAL); (S), (N) = reformulations of P47 §Open problems; «spectral
side» = clause (R)(4). «Ín.» = verdict of the index (README or ledger); «Prim.» = what the primary memo
and its review maintain.

Note on method: for the developed memos the verdict/result section and its review were read (or the
ledger row summarizing it, when the review is joint); for the pre-screening seeds the primary source is the row or
paragraph of table CA_*_000, which in many cases is all that exists.

## 1. Front A — modular group / Hecke

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| A1 | CA_A_001 | Petersson/Maass–Selberg/RS positivity on PSL₂(ℤ)\ℍ | closed (do not retry) | NO-GO PROVED only for the class «Eisenstein norm in spectral variable» (Cor 3); extension «all Eisenstein positivity» WITHDRAWN; general exclusion by O11/O12 = CIRC | (a) for the norm class; rest → A1r |
| A1r | CA_A_001 (open in ledger) | Mellin in y / Rankin–Selberg in w reaching ζ(½+iτ) on the unitary axis | not listed as closed; README audit lists it as «re-examine» | OPEN, never developed | (e) |
| A2 | CA_A_002 | Lewis–Zagier/Mayer transfer operator | «NO-GO» (corrected to ARGUED in README) | NO-GO ARGUED; formula for ψ_s CITED-UNVERIFIED | (b): missing verification of ψ_s and proof that Λ enters only via log det in every reading |
| A3 | CA_A_003 §2 | Hecke multiplicativity on σ_T | NO-GO PROVED | Hecke relations = Chebyshev identities, (B″) PROVED | (a) (B″) |
| A3s | CA_A_003 §3 | Hecke tests on the family | REF-D | = (S) + (B′) | (c) of (S) |
| A3r | CA_A_003 §4 | off-diagonal metaplectic packet form | OPEN in ledger | OPEN, never developed | (e) |
| A4 | CA_A_004 | metaplectic Eisenstein weight ½ P₀⁺, Parseval | closed | Prop 1 CONFIRMED (independent of the comb: O1–O7, O15); Cor 3 («Parseval = arithmetic squares») ARG with FIX | (a) by O7/O15 on the object as formulated |
| A4r | CA_A_004 (open) | Salié/Kuznetsov variant | OPEN-RESIDUE (low) | not developed | (e) |
| A5 | CA_A_005 | RS with test vector of the minimizer | closed | blind to the comb, (B″) PROVED; no continuous kernel = window multiplier (PROVED); continuation = (S) | (a) (B″) |
| A6 | CA_A_006 | abscissa transport 1→½ (Y-integration, Hecke average) | NO-GO PROVED | (ii) PROVED (Thm 2); (i) = (S) | (a) for (ii); (i) is (c) of (S) |
| A7a | CA_A_007 §1 | homotopy from positive endpoint | withdrawn (retry N_012/W5) | non-crossing = positivity | (c) of the target (sign constancy along the path) |
| A7b | CA_A_007 | boundary triples for W_λ | «= polar capacity 𝔊_T, PROVED» | coordinates of thm:parityschur | (c) of the 2×2 polar condition |
| A7c | CA_A_007 Thm 2 | reflection positivity between places | NO-GO PROVED | RP fails for every atomic comb (PROVED) | (a) |
| A7d | CA_A_007 §4 | t-concavity of log\|ξ\| (NG-D2) | no attempt (RULES_AVOID §C, last line) | ARG, not developed | (d) |
| A7e | CA_A_007 §4 | rigged eigenvectors x^{b+iγ} | no attempt | ARG; the escape (rigging built with primes) is named in the memo | (e) |
| A8 | CA_A_008 | integer invariant / spectral flow / Maslov | REF-D | Lemma 1 PROVED: constancy ⟺ target | (c) of the target (no eigenvalue crossing through 0) |

## 2. Front B — tests built with ζ

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| B1 | CA_B_001 | pairing identity J′(½) | closed | identities CONFIRMED; sign on the spectral side; exclusion O11/O12 = CIRC, but (R)(4) is structural | (c) (sign content = spectral side (R)(4)) |
| B2 | CA_B_002 | Riesz/Jensen decomposition of −∂_σH | closed | reading without ζ: (B″); reading with ζ: (R)(4) | (a) (B″) in the generic reading |
| B3 | CA_B_003 | self-pairing Δ_a ≡ 0 ⟺ EF | closed | Thm 1 PROVED; the property survives O7 (quartets) | (a) O7 |
| B3r | CA_B_003 (residual) | inequality that USES Δ≡0 (not the property alone) | pending in ledger | not developed | (e) |
| B4 | CA_B_004 | transport J(σ), Green identity | closed | J(1)=∞ by the pole (PROVED); convexity chain false | (a) |
| B5 | CA_B_005 | inversion «defect ⇒ negative bottom» | closed | (Inv) FALSE (PROVED); Prop 2 = prop:wit-sens | (a) |
| B6 | CA_B_006 | open ball lemma; interior sets | closed | = prop:wit-sens; membership in the Euler tail carries no sign | (a) (only controls I_ζζ) |
| B7 | CA_B_007 | convex decomposition in 𝒱_T^meas | closed | = target or certificate (class (D)) | (c) of the target / dual certificate |
| B8 | CA_B_008 | concavity gap Γ | REF-D (tautology) | Thm 1 coordinate; Γ = tautology | (c) of the target |

## 3. Front C — local–global / adelic and new areas

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| C1 | CA_C_000 C1 | weighted Hasse–Minkowski, convex partition by primes | closed | REF-D reason incorrect (FIX); death correct (cor:Qp) ARGUED | (b): missing the written contradiction with cor:Qp for every choice of c_p |
| C2 | CA_C_000 C2 | Lévy–Khintchine per place | closed | (B″), O7/O15 | (a) (B″), O7 |
| C3 | CA_C_001 | product formula as coupling | NO-GO PROVED | Thm 1 PROVED; 2 cells CONDITIONAL (O4^ε, O5) but they also fall by O7 | (a) O7 / Thm 1 |
| C4 | CA_C_000 C4 | Tate residues / adele class space | REF-D | exact reformulation | (c) (Tate formulation of the target) |
| C5 | CA_C_000 C5, CA_C_002 | classical HM (MW-3) | NO-GO in classical class | Prop 1 PROVED (class 𝓗); well-posed reading = (S) | (a) class 𝓗; rest (c) of (S) |
| C5L | CA_C_002 open; F3 | condensed HM with archimedean (liquid) input | «NO-GO PROVED» (README F) | PROVED only for 3 declared classes (CA_F_001); archimedean case ARGUED | (b): missing a class including archimedean liquid input |
| C6 | CA_C_000 C6, CA_C_002 Prop 2 | torus/line partition into boxes | REF-D | Near = Kronecker line − Haar | (c) of (S) |
| C7 | CA_C_003, CA_C_005 | (Fam_η) = T*₃(η) | criticality retracted | only necessary for η>2/3 (NUMERICAL); μ_M lower bound | (d) (numerical datum; not a sign examination) |
| C8 | CA_C_007 | η family as sign step | EXCLUDED | Lemmas 1–2, Prop 3 PROVED; FE-class genericity NUMERICAL | (b): missing proof of positivity for Epstein/negativity for Beurling (today NUMERICAL) |
| CD1 | CA_C_004 D1 | Γ vs local terms on Nyquist mesh | REF-D | = (N) | (c) of (N) |
| CD2 | CA_C_004 D2 | rationality of ζ(2k)/π^{2k} | closed | O7 with rational quartets, ARG (witness «plausible») | (b): missing explicit rational quartet witness |
| CD3 | CA_C_004 D3 | Kummer / p-adic | closed | ℚ_p not ordered (PROVED, category) | (a) (category: no inequality at p) |
| CD4 | CA_C_004 D4 | Iwasawa / μ=0 | closed | 1 line + (R)(10) CIRC | (d) |
| CD5 | CA_C_004 D5 | unitarity of the EF factor | closed | prop:shape-phase, (B″) | (a) (B″) |
| CD6 | CA_C_004 D6 | local law of the minimizer | REF-D | = Theorem X / C*_A | (c) of the statement about the minimizer (Lemma S) |
| CE1 | CA_C_006 E1 | o-minimality / Pila–Wilkie | NO-GO ARGUED | semialgebraic set ⇒ empty method (almost immediate) | (a) (elementary vacuity; only writing it up is missing) |
| CE2 | CA_C_006 E2 | free probability Arch vs Div | closed | they commute ⇒ not free (PROVED elementary) | (a) for free independence |
| CE3 | CA_C_006 E3 | Ax–Schanuel | closed | O15 (PROVED) | (a) O15 |
| CE4 | CA_C_006 E4 | Helson H²(𝔻^∞) | closed | torus/line (= (S)) + (B′) CIRC | (c) of (S) |
| CE5 | CA_C_006 E5 | Positivstellensatz at η>2/3 | closed | SOS = class (D); premise [crit] retracted | (c) (dual certificate) |
| CE6 | CA_C_006 E6 | spectral-side identity of the family without primes | «keep as classification» | not developed | (d) |

## 4. Front D — phase / Hardy function

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| D1 | CA_D_000 D1 | first spectral moment (Wigner–Smith delay) | closed | 𝔞_T = −2∫u\|ȟ\|²: exact rewriting | (c) of the target (frequency mean ≤ 0) |
| D2 | CA_D_001 | Hardy amplitude transfer | TOOL | Thm 1/1′/1″ PROVED; FE-generic; exclusion O10/O12 CIRC, O7 ARG | (a) as a sign step by (R)(11) only via cited O10; living tool |
| D3 | CA_D_000 D3 | Landau / maximum, Bohr–Jessen | closed | retry R164_102 (falsifier ζ·E) | (a) (falsifier ζ·E) |
| D4 | CA_D_000 D4 | Kramers–Kronig / DtN | closed | (R)(4) or (B″) | (a) (B″) in the identity reading |
| D5 | CA_D_000 D5 | Riemann–Siegel chirp + FM | closed | R163_603 (f_χ) | (a) falsifier f_χ |
| D6 | CA_D_000 D6 | scattering causality | closed | ⟺ half-plane without poles of S_X | (c) (pole-free region of S_X) |
| D7 | CA_D_000 D7 | de Branges/Kreĭn phase | closed | σ_T(0)<0 (PROVED); positive extension = certificate (thm:Z) | (a) σ_T(0)<0 |
| D8 | CA_D_000 D8, CA_R2_001 | exponent homotopy W(α) | death 1L → THM | interpolation from integers NO-GO (class, PROVED); W(0)≥W(1) false in the central cell (PROVED); remaining input on {\|Z_T\|<1} | (a) for interpolation; residue = (c) of the central Nyquist cell |
| D9 | CA_D_002 | closure of the transferred cone | NO-GO PROVED | Thm 2, 2′ PROVED | (a) |
| D10 | CA_D_003 | transfer vs family s_w; amplitude-one residual | closed | residues DEAD/REF-D (2 FIX) | (c) of (R)(7)/central cell |

## 5. Front E — operator algebras / quantum

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| E1 | CA_E_000 | KMS beyond Bost–Connes | dead | real β only (ARG); O11 CIRC; retry 114_d_116 | (b): missing proof that complex β contributes nothing and a PROVED falsifier instead of O11 |
| E2 | CA_E_000 | Connes cocycle | dead | commutative ⇒ pointwise symbol (false at 0); REF-D | (a) (σ_T(0)<0) |
| E3 | CA_E_000 | Jones index / TL | dead | «no object is known» | (d) |
| E4 | CA_E_001 Thm 1 | CP / Choi / entanglement | REF-D | separability PROVED: target ⟺ positivity on Euler product vectors | (c) (form on Euler vectors) |
| E5 | CA_E_001 Thm 2 | Schur multipliers / GCD factorization | NO-GO PROVED | PROVED | (a) |
| E6 | CA_E_000 | CCR / Robertson | dead | retries (R178 NO-GO) | (a) by inheritance from R178 |
| E7 | CA_E_000 | ITPFI / Kakutani | dead | O11 (CIRC), O15 (PROVED), Thm U | (a) O15 |
| E8 | CA_E_000 | Golden–Thompson / Gibbs | dead | equality by commutation (elementary) | (a) |
| E9 | CA_E_000 | Kadison–Singer / MSS / Lee–Yang | dead | retry phase 11; (B′) CIRC; (R)(4) | (b): no own PROVED falsifier; rests on (B′)(iv) |
| E10 | CA_E_000 | Araki / Petz | dead | monotonicity in the wrong direction (lem:monoT) | (a) direction |
| E11 | CA_E_000 | operator systems / Arveson | dead | REF-D (KEP), 1 line | (c) (Kreĭn indeterminacy) |
| E12 | CA_E_000 | NC-SOS / de Finetti | dead | commutative collapse (PROVED) | (a) |

## 6. Front F — topology / geometry

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| F1 | CA_F_000 F1 | Floer beyond Maslov | REF-D | Lemma F1 PROVED: = spectral data | (c) (spectral data of 𝔞_T) |
| F2 | CA_F_000 F2 | Bridgeland | REF-D | Lemma F2: support in ker Z = P_T ⟺ 𝔞_T ≻ 0 | (c) of the target |
| F3 | CA_F_000 F3, CA_F_001 | condensed/liquid MW-3 | NO-GO PROVED (README) | PROVED for 3 classes; Prop 3 (local positivity false at every p) PROVED | (a) in the 3 classes; archimedean case → C5L |
| F4 | CA_F_000 F4 | motivic / A¹ / RO(G) | REF-D | signatures = spectral | (c) (signature of 𝔞_T) |
| F5 | CA_F_000 F5 | Hodge–Riemann / Lorentzian non-AHK | dead | Theorem P miscited (FIX); signature hypothesis ARG | (b): missing proof that the required signature fails (only bound n₋) |
| F6 | CA_F_000 F6 | Weyl laws / heat invariants | dead | 1 line (spectral + (B″)) | (d) |
| F7 | CA_F_000 F7 | Selberg / horocycle equidistribution | dead | estimates (B′) CIRC; L31 | (d) |
| F8 | CA_F_000 F8 | calibrations | dead | dual certificate, 1 line | (c) (dual certificate) |
| F9 | CA_F_000 F9, CA_F_003 §4 | DAG / ∞ traces | dead | object not built; = G-F OPEN | (e) (G-F) |
| F11 | CA_F_000 F11 | cluster algebras | dead | O2/O6 (PROVED) | (a) O2/O6 |
| F12 | CA_F_000 F12 | symplectic capacities | REF-D | spectral | (c) |
| F13 | CA_F_000 F13 | perfectoid tilting | dead | ℚ_p not ordered, 1 line | (d) |
| F14 | CA_F_000 F14 | exact homogeneous dynamics | dead | Bochner class; σ_T(0)<0 | (a) σ_T(0)<0 |
| F15 | CA_F_000 F15 | nef/ample, Nakai–Moishezon | dead | class (D), presupposes the object | (c) (dual certificate) |
| F16 | CA_F_002 | exact trace formulas (TF⁺) | NO-GO PROVED | PROVED for the declared class | (a) class TF⁺ |
| F17 | CA_F_003 | polarized object over ℤ (G-F) | gap OPEN | «OPEN (object unbuilt)»; Prop 2 PROVED (unitary invariants = spectral) | (e) |

(F10 was excluded by the brief and is not classified.)

## 7. Front G — exotic algebras / combinatorics

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| G0 | CA_G_001 | squares = Gram factorizations | PROVED | REF-D or certificate | (c) (Gram factorization) |
| G1 | CA_G_000 G1 | SUSY / Witten / Riccati | dead | factorization ⟺ positivity | (c) of the target |
| G1m | CA_G_001 §1 | free monoid lemma ℕ^× | PROVED | isomorphism PROVED; excludes only via (R)(10) (O11 ARG, O12 OPEN) | (b): missing PROVED Beurling/ζ_K falsifier |
| G2 | CA_G_000 G2 | Clifford / Weitzenböck | dead | natural partition: both summands indefinite (cor:Tarch, cor:Qp) | (a) only for the natural partition |
| G3 | CA_G_001 §3 | Elias–Williamson ladder | REF-D/retry | primitive complement carries the target | (c) (Schur tower) |
| G4 | CA_G_000 G4 | categorification | dead | G0(c), 1 line | (c) |
| G5 | CA_G_000 G5 | VOA / moonshine | dead | only primitive O10 (CIRC) | (b): missing O10 PROVED for the primitive form |
| G6 | CA_G_000 G6 | Lorentzian polynomials | retry | criterion D.15.2 PROVED without sign | (a) by inheritance R138 |
| G7 | CA_G_000 G7 | cluster TP | dead | PF₅ fails (CITED); PF₄ OPEN | (a) order ≥5; order ≤4 → (e) |
| G8 | CA_G_000 G8 | Jordan / symmetric cones | dead | self-duality = thm:D1 | (c) |
| G9 | CA_G_000 G9 | Connes–Kreimer Birkhoff | dead | = Wiener–Hopf (W-det) | (a) by inheritance W-det |
| G10 | CA_G_000 G10 | sign-reversing involutions | dead | G1 (CIRC) + G0(b) | (c) (SOS half) / (b) (monoid half) |
| G11 | CA_G_000 G11 | quantum groups / Shapovalov | dead | retry NG-67, 1 line | (d) |
| G12 | CA_G_000 G12 | Hecke of ℕ^× «Soergel» | dead | monoid form: G1 (CIRC); with ℕ: O7 | (a) O7 in comb form; monoid form (b) |

## 8. Front H — semiring (ℕ,+,·)

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| H1 | CA_H_001 | Buium p-derivations, Wronskian | NO-GO | PROVED/CITED for the declared class | (a) class 𝒦_δ |
| H2 | CA_H_000 H2 | Stepanov over ℤ | dead | retry G1_B9 Lemma 3 (PROVED char 0) | (a) |
| H3 | CA_H_000 H3 | carries / Witt | dead | form blind to carries (ARG, CA_H_001 §1.4) | (b): missing proved statement of blindness |
| H4 | CA_H_000 H4 | sum-product | dead | set statements survive O2/O7/O15 | (a) O2/O7/O15 |
| H5 | CA_H_002 | Erdős invariant (S⁺) | separates but not O7 | survives O7, asymptotic | (a) O7 as sign step |
| H6 | CA_H_002 Thm 3.1 | Kronecker line − Haar | REF-D | = (S) | (c) of (S) |
| H7 | CA_H_000 H7 | integrality gap / Liouville | dead | only density ceiling (thm:ceiling) | (a) necessary direction |
| H8 | CA_H_001 §5 | global Frobenius lifts | NO-GO class | PROVED/CITED, declared class | (a) declared class; non-graph correspondences → F17 |
| H9 | CA_H_000 H9 | CRT divisibility (SPEC_B line 3) | dead | linear W7; REF-D η≤η₀ | (c) |
| H10 | CA_H_000 H10 | arithmetic derivative | dead | only G1 (CIRC) | (b): missing PROVED monoid falsifier |

## 9. Front I — analysis of the minimizer

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| I1 | CA_I_001 Thm 1–2 | Markov / Krein–Rutman / maximum | NO-GO PROVED | Thm 2 via O2 PROVED | (a) O2 |
| I1⋆ | CA_I_001 Cor 6, CA_R1_001 | separating set 𝖯⋆ | REF-D (now PROVED) | REF-D by identification PROVED; every sub-conjunction has a falsifier | (c) (forces a = Λ, K ≡ 0) |
| I1g | CA_I_001 | Markov formula for general E | — | ARG (FIX) | (b): missing the proof of the formula |
| I2 | CA_I_000 I2 | nodal structure of h* | lemma | ≥2 sign changes PROVED; without sign | (a) (B″: only geometry of the constraints) |
| I3 | CA_I_001 §5 | symmetrization | dead | Prop 5.1 PROVED | (a) |
| I4 | CA_I_002 | virial / Pohozaev | dead | holds for every comb (DH included) | (a) (B″) |
| I5 | CA_I_002 | Almgren frequency | dead | Prop 2.2 PROVED | (a) |
| I6 | CA_I_000 I6 | unique continuation | dead | automatic (Paley–Wiener) | (a) |
| I7 | CA_I_002 §3 | Γ-convergence | dead | absolute o(1) vs margin, ARG | (b): missing explicit comparison with the proved margin 4·10⁹Te^{−15.449T} |
| I8 | CA_I_002 §4 | concentration–compactness | dead | quadratic ⇒ no strict subadditivity (short ARG) | (b): write up as a lemma |
| I9 | CA_I_002 §2 | boundary layer ±T | dead (only upper bound) | DH transversality ARG | (b): missing proof of transversality |
| I10 | CA_I_001 §3 | semigroup comparison | folded | λ₀ monotone, λ_A not | (a) (O2) |

## 10. Front J — correlation inequalities

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| J1 | CA_J_002 §1 | GKS with 𝔸_M | NO-GO | frustration Thm 1.3 PROVED | (a) |
| J2 | CA_J_002 §2 | FKG on divisor lattice | NO-GO | equality class = Euler vectors (PROVED) | (a) |
| J3 | CA_J_000 J3 | Ginibre/GHS/Lebowitz | dead | presuppose ferromagnetism ⇒ Thm 1.3 | (a) |
| J4 | CA_J_000 J4 | Brascamp–Lieb variance | dead | input Hess V ⪰ 0 = target | (c) of the target |
| J4′ | CA_J_000 J4′ | geometric BL / BCCT | dead | dimension data; only O11 (CIRC) | (b): missing PROVED falsifier |
| J5 | CA_J_000 J5 | Prékopa–Leindler | retry PF | PF₅ fails; PF₄ OPEN | (a) order ≥5; ≤4 → (e) with G7 |
| J6 | CA_J_001 | checkerboard / RP in prime coordinates | NO-GO PROVED | Thm 1–2 PROVED | (a) |
| J7 | CA_J_000 J7 | Gaussian domination | dead | requires RP ⇒ J6 | (a) |
| J8 | CA_J_000 J8 | strong Rayleigh | dead | zero localization (R)(4), 1 line | (d) |
| J9 | CA_J_000 J9 | FK / random cluster | dead | requires ferromagnetic weights | (a) |
| J10 | CA_J_000 J10 | Dobrushin / Kotecký–Preiss | dead | perturbative, [crit] NUM | (b): missing comparison with the proved margin |
| J11 | CA_J_002 Prop 2.4 | Holley comparison | folded | linear in Λ | (a) (equality class J2) |
| J12 | CA_J_000 J12 | log-supermodularity | folded | φ takes negative values (Lemma J0′) | (a) |

## 11. Front K — frustrated quadratic forms

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| K1 | CA_K_002 §1 | Guerra interpolation | NO-GO PROVED | Thm 1.2: sign of the path = statement about the minimizer | (c) (statement about the minimizer) |
| K2 | CA_K_000 K2 | Talagrand/Parisi | dead | no disorder | (a) (vacuity) |
| K3 | CA_K_000 K3 | ASS cavity | dead | Schur reductions | (c) (Schur tower) |
| K4 | CA_K_000 K4 | Grothendieck / SDP | dead | vector side = Gram | (c) (G0) |
| K5 | CA_K_000 K5 | Lasserre | dead | level 1 = PSD = target; thm:sos | (c) |
| K6 | CA_K_001 §3 | ℤ/2 holonomy | NO-GO | counterexample g𝖡 (PROVED) | (a) |
| K7 | CA_K_001 §4 | signed Laplacian / Cheeger | NO-GO | decomposition PROVED; loss ½ vs 1−O(1/M) ARG/NUM | (b): missing proved loss against the margin |
| K8 | CA_K_001 §1–2 | diamagnetism | NO-GO PROVED | Thm 1.2, Thm 2.2 (reversed order) | (a) |
| K9 | CA_K_000 K9 | Lieb flux | dead | requires RP | (a) |
| K10 | CA_K_002 §3 | heat flow on Ĝ / site independence | REF-D | Thm 3.2/Cor 3.3 PROVED: target ⟺ Arch ≥ Near on prime tests | (c) (Arch ≥ Near on prime sites) |
| K11 | CA_K_000 K11 | Doob transform | retry Paper 41 | 31 inherited no-gos | (a) |
| K12 | CA_K_000 K12 | frustration-free decompositions | dead | CA_F_001 Prop 3 PROVED | (a) |
| K13 | CA_K_000 K13 | TAP / Plefka | dead | perturbative | (b): same as J10 |

## 12. Front L — exact magic constructions

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| L1 | CA_L_001 Thm 1.1 | magic flat-top certificate | NO-GO PROVED | thm:O as complementary slackness | (a) |
| L2 | CA_L_001 | ε-magic family with modular data | NO-GO | level 20: O10 complete form (CITED); level 1 reduces to the comb | (a) level 20; level 1 → (c) of the comb |
| L3 | CA_L_001 Prop 1.3 | Cohn–Elkies | dead | upper direction (PROVED) | (a) |
| L4 | CA_L_000 L4 | RV interpolation | dead | retry P35-4; finZ | (a) |
| L5 | CA_L_002 | LP on prime sites | REF-D | dual attained, slack on Z_s, exact \|X\|≤5 | (c) (site LP = target) |
| L6 | CA_L_002 §3 | certificate on the Bohr torus | REF-D | same | (c) |
| L7 | CA_L_000 L7 | Cohn–Gonçalves sign uncertainty | dead | 1 line | (d) |
| L8 | CA_L_000 L8 | Delsarte/Turán | dead | = certificate | (c) |
| L9 | CA_L_000 L9 | CKMRV | dead | requires lattice, 1 line | (d) |
| L10 | CA_L_000 L10 | self-dual theta + sinc | retry | R164_401: only EF | (a) (EF class falsifier) |

## 13. Front M — problem on prime sites

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| M1 | CA_M_001 §1 | Chen-type decomposition Near = ΣC_s(h) | PROVED | identity (B″) | (a) (B″) |
| M2 | CA_M_001 §2 | parity / residues | NO-GO | trace 0, linear in Λ (PROVED) | (a) |
| M3 | CA_M_001 §3 | integrality of p − np′ | PROVED | Thm 3.1/Cor 3.2: perturbed sites give the same truth value | (a) |
| M4 | CA_M_000 M4 | sieve weights / Chen | dead | W-sieve, NG-A4 | (a) |
| M5 | CA_M_000 M5 | singular series | dead | ARG §1.3; PROVED in decisive class via Thm 3.1 | (a) in the decisive class |
| M6 | CA_M_001 §4 | antidiamagnetic inversion | PROVED | exact EF-generic cancellation | (a) (O10/O12 by EF) |
| M7 | CA_M_000 M7 | Vinogradov arcs | dead | ARG §1.4 | (b): missing proof of negligible weight away from θ≈0 |
| M8 | CA_M_001 Cor 3.3 | Beurling on prime sites | folded | Thm 3.1 | (a) |

## 14. Front N and round R

| id | file | mechanism | Ín. | Prim. | class |
|---|---|---|---|---|---|
| N1 | CA_N_001 | V1 discrete primal attained | 0 admissible | on sites: REF-D; exact+attained impossible in window LP (thm:O) | (a) in window LP; site version (c) |
| N2 | CA_N_002 | V2 positive combs | Thm N2 PROVED (T > ½log3, FIX) | unimodular transfer impossible; non-unimodular OPEN | (a) unimodular; → N2r |
| N2r | CA_N_002 / ledger | non-unimodular transfers | OPEN («expected G0») | not developed | (e) |
| N3 | CA_N_003 | V3 self-structure | NO-GO (declared classes) | no multiplicative self-dual lattice (PROVED); no generating automorphic form (PROVED); Thm 5 via O10 | (a) declared classes |
| R1 | CA_R1_001 | 𝖯⋆ and residue D_∃c | REF-D PROVED; D_∃c OPEN | D ⇒ D_∃c; converse = O4^ε | (e) D_∃c |
| R2a | CA_R2_001 | = D8 | see D8 | — | (a) (see D8) |
| R2b | CA_R2_002, README | SPEC_A (γ) with proved margin | ARG | (γ) fails with power sources (ARG); identities-only version OPEN | (b) for (γ) with estimates; (e) identities version |
| R3 | CA_R3_001 | θ line, L*_j(θ) | «ADMISSIBLE» not endorsed → REF-D | identities CONFIRMED | (c) (step lemma L*_j) |
| R4 | CA_R4_001 | L*_j(θ) at ½log5 → ½log7 | OPEN | reduction PROVED; sign OPEN; test 𝒞_θ at this contact ARG NO-GO | (e) |

## 15. Count by class

| class | n | ids |
|---|---|---|
| (a) | ≈85 | A1, A3, A4, A5, A6, A7c, B2–B6, C2, C3, C5, CD3, CD5, CE1, CE2, CE3, D2, D3, D4, D5, D7, D8/R2a, D9, E2, E5–E8, E10, E12, F3, F11, F14, F16, G2, G6, G7, G9, G12, H1, H2, H4, H5, H7, H8, I1–I6, I10, J1–J3, J5–J7, J9, J11, J12, K2, K6, K8, K9, K11, K12, L1–L4, L10, M1–M6, M8, N1, N3 (counted once; D8 and R2a as one) |
| (b) | 22 | A2, C1, C5L, C8, CD2, E1, E9, F5, G1m, G5, G10 (monoid half), H3, H10, I1g, I7, I8, I9, J4′, J10, K7, K13, M7 (+ R2b-(γ)) |
| (c) | 41 | A3s, A7a, A7b, A8, B1, B7, B8, C4, C6, CD1, CD6, CE4, CE5, D6, D10, E4, E11, F1, F2, F4, F8, F12, F15, G0, G1, G3, G4, G8, H6, H9, I1⋆, J4, K1, K3, K4, K5, K10, L5, L6, L8, R3 |
| (d) | 12 | A7d, C7, CD4, CE6, E3, F6, F7, F13, G11, J8, L7, L9 |
| (e) | 11 | A1r, A3r, A4r, A7e, B3r, F9/F17 (G-F), G7/J5-PF₄, N2r, R1 (D_∃c), R2b-identities, R4 |

Rows with a double class (A6, C5, D8, G7, G10, G12, L2, N1, N2, R2b) are counted in the class of their main
core; their other half appears as its own row or as a residue. That is why the totals per class do not add up exactly to
the number of rows (≈170 rows, ≈165 distinct candidates after identifying D8=R2a, F9≈F17, G7≈J5).

## 16. Wording of RULES_AVOID.md §C that must be changed

§C says «Closed families». With this table, the following words of §C (all from phase 193) are not closed or
are closed only in a partial sense:

1. «**modular/Hecke (Petersson, Rankin–Selberg, Maass–Selberg, metaplectic Eisenstein, spectral flow)**» —
   Petersson/MS only in the «norm» class (A1); RS in w on the unitary axis (A1r), off-diagonal metaplectic
   packet (A3r) and Salié/Kuznetsov (A4r) remain OPEN; «spectral flow» is an exact reformulation (A8), not a closure.
   Rewrite: «modular/Hecke: closed the norm class, the multiplicativity on σ_T and the transport by
   Y-integration; open A1r, A3r, A4r; spectral flow = reformulation».
2. «**KMS, Bost–Connes, Jones, Araki/Petz, NC-SOS**» — KMS is only ARGUED (E1); Jones is one line (E3, without
   object). Move KMS to «argued» and Jones to «without sufficient examination».
3. «**Floer, Bridgeland, motivic, Lorentzian Hodge–Riemann, Selberg/Arthur traces**» — Floer, Bridgeland and
   motivic are exact reformulations (F1, F2, F4); Lorentzian Hodge–Riemann is ARGUED (F5); only traces
   (TF⁺, F16) is PROVED. Move the first three to «reformulations (valid target)».
4. «**supersymmetry, Soergel, VOA, cluster, Jordan**» — supersymmetry and Jordan are reformulations (G1, G8); Soergel
   in monoid form and VOA rest only on CIRC clauses (G12, G5); cluster is closed only in order ≥5, with PF₄
   OPEN (G7).
5. «**p-derivations, Stepanov, sum-product**» — correct as closed; but the «arithmetic derivative» and
   «carries» (H10, H3), if implicitly added, are ARG/CIRC.
6. «**Markov, maximum principle, virial/Pohozaev, Almgren, Γ-convergence**» — Γ-convergence is ARGUED (I7);
   the set 𝖯⋆ is a PROVED reformulation (I1⋆) and leaves the OPEN residue D_∃c.
7. «**OS/checkerboard, GKS, FKG, Lee–Yang, Brascamp–Lieb, Dobrushin, frustrated forms, Lasserre**» — Brascamp–Lieb: the
   variance version is a reformulation (J4) and the geometric one only CIRC (J4′); Dobrushin ARG (J10); Lasserre is
   a reformulation (K5); Lee–Yang/Rayleigh is one line (J8).
8. «**Viazovska-type magic functions**» — the literal magic function is PROVED (L1, N1), but the LP on prime
   sites / certificate on the torus (L5, L6) is an exact reformulation with attained dual; it must be listed as a target.
9. «**prime-site arithmetic (parity, residues, singular series)**» — correct (M2, M3, M5 PROVED in the
   decisive class); Vinogradov (M7) is ARG.
10. «**total positivity, PF, …(fails at PF₂; the kernel is not PF₅)**» — add explicitly «PF₄ OPEN».
11. «**Sonin…; function fields, Hodge, Arakelov, arithmetic site, h⁰ carriers**» — as far as phase
    193 is concerned, the polarized object over ℤ (G-F, F17) is OPEN (object not built), not closed.
12. The heading phrase «Closed families» must be accompanied by the warning of AUDIT_PHASE193_CERTAINTY: for
    phase 193, «0 admissible» means «no seed as formulated passes the PROVED filters», not «the area
    is closed».

Moreover §C, last line: «Still listed without attempt: rigged-space eigenvectors, …, t-concavity» — coincides with
A7e (e) and A7d (d); «anti-Siegel repulsion» does not appear in phase 193.

## 17. Items (c)–(e) deserving examination as construction targets

Each with the precise object that is missing.

1. **K10 / M3 — Arch ≥ Near on tests on prime sites** (c). Missing: a finite matrix inequality
   Arch_M − Near_M ⪰ 0 whose sign step uses the positions log n and the weights Λ(n)n^{−½} of the comb (the only thing
   M3 leaves), with uniform control in M.
2. **L5/L6/N1 — LP on prime sites on the torus** (c). Dual attained, slack on Z_s, exact for \|X\| ≤ 5.
   Missing: a family of constraints containing a datum from the archimedean column (pole/EF) and a control of the
   range of the ellipsotope when \|X\| → ∞.
3. **R1 — D_∃c** (e). Missing: for each T a c>0 with λ_A(T; cΛ) ≥ 0, and then the question O4^ε (κ_T ≠ 0) that
   identifies the common c; each half is a defined object.
4. **R4 / R3 — step lemma L*_j(θ)** (e)/(c). Missing: the exact evaluation of 𝔄_j^{−1} on the exterior field of
   four atoms (near cancellation at relative precision ≲ 1.6·10⁻⁶) with a mechanism other than the certified
   enclosure.
5. **R2b — exact induction with identities only (SPEC_A)** (e). Missing: where log ℕ enters in ‖ℓ_e‖_{𝔄_j^{−1}}
   (coincidence of the contact block v_{n_j} against 2n_j^{−½} at the offset 2T_j) in the form of an identity, not an
   estimate.
6. **N2r — non-unimodular analytic-signal transfers** (e). Missing: the class of admissible amplitudes
   (CA_D_002 §3.6) and a proof that some escapes G0 (is not a Gram factorization).
7. **F17 / F9 — polarized object over ℤ (G-F)** (e). Missing: the object itself — ample class, quadratic h⁰ and
   trace property — whose positivity comes from ampleness and not from the signature of 𝔞_T.
8. **A1r, A3r, A4r — modular residues** (e). Missing: the RS form in w restricted to the unitary axis, the
   off-diagonal metaplectic packet form and the Kuznetsov variant, each with the proof that its
   positivity is not a norm (does not fall into O11/O12 nor into (R)(4)).
9. **G7/J5 — total positivity of order ≤ 4 (PF₄)** (e). Missing: a (non-local) proof of PF₄ of the kernel and an
   inequality connecting order 4 with the window form.
10. **A7e — rigged eigenvectors built with primes** (e). Missing: the rigged space whose rigging uses
    only the comb, and the identity expressing a_T in that basis.
11. **B3r — inequality using Δ_a ≡ 0** (e). Missing: an inequality (not the property alone, which falls by O7) in
    which Δ≡0 is a loaded hypothesis together with a datum the quartets do not have.
12. **D8 / D10 — central Nyquist cell {\|Z_T\| < 1}** (c). Missing: a specific input acting on that
    cell (amplitude one) with the PROVED tool CA_D_001.
13. **E4 — form on Euler product vectors** (c). Missing: a positivity property proper to those
    vectors (not CP, which is equivalent) and that is not a Schur factorization (E5).
14. Items (d) which, if one wants to use them, must be examined before counting them as attempted: A7d (t-concavity),
    CE6 (classification of the family without primes), E3 (Jones), F6, F7, F13, G11, J8, L7, L9, CD4, C7.

## 18. Coverage

- Files in the folder: 128 `.md` (memos, seeds, reviews, syntheses, ledger, README).
- Candidates/families found: ≈165 distinct (A 16, B 9, C 20, D 10, E 12, F 16 + F10 excluded by the brief, G 14,
  H 10, I 12, J 13, K 13, L 10, M 8, N/R 9). Classified: all those found (≈170 rows).
- Reading: AUDIT_PHASE193_CERTAINTY, README of the index (phases 190–193 and re-examinations), AUDIT_A, AUDIT_B, RULES_AVOID,
  CAMPAIGN_LEDGER and CA_A_000_INDEX in full; seed tables CA_*_000 and batches CA_C_004/006 in their verdict
  rows/paragraphs; result sections of CA_A_002 and CA_F_003 §4. For the other developed memos the primary
  verdict was taken from the ledger row summarizing memo + review, not from a complete reading of each memo; that
  difference is the main limitation of this annex. No reading failed; there was no illegible memo.
