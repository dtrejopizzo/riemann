# Annex — Complete primary reading of phase 193 and contrast with ANNEX_PHASE_193_LABELS.md

Object: the sign of the window form 𝔞_T on the primitive subspace P_T (target λ_A(T) ≥ 0 for all T),
treated only as a problem about that quadratic form. When a source uses wording linking the target to another
statement, «(★)» is written here and it is not used.

Source: the 128 `.md` files of `03-research/phase-193-creation-campaign/`, read in full (memos, seed
tables, reviews, syntheses, ledger, index, README). Abbreviations as in `ANNEX_PHASE_193_LABELS.md` («LABELS»):
O1–O15 P47 numbering (ledger errata); (B″) identity valid for every comb; (B′) estimate with remainder;
REF-D exact reformulation; CIRC death clause that in P47 is ARGUED/OPEN. Labels: PROVED / CITED / CONDITIONAL /
OPEN / NO-GO / NUMERICAL / ARGUED.

Basis of the discard: **(i)** explicit falsifier (it is named and it is said whether its failure is PROVED, CITED, NUMERICAL or
ARGUED); **(ii)** proved class NO-GO; **(iii)** argument only; **(iv)** reduction to the target (REF-D);
**(v)** nothing (not examined). Class: (a)–(e) as in LABELS.

Numbering note: the reviews of CA_A_001–004 and CA_B_001–005 use the numbering of the brief («O7 Beurling», «O8
quartets», «O11 Epstein»); here it is always translated to P47 (O11 Beurling, O7 quartets, O10 Epstein).

---

## 1. Entries by file

### Front A

| file | mechanism | primary verdict (with labels) | basis | class |
|---|---|---|---|---|
| CA_A_000_INDEX | index of front A | summarizes A001–A008; no own content | — | — |
| CA_A_001 | norm positivity (Maass–Selberg, Petersson, RS with weights E(·,w)>0) on PSL₂(ℤ)\ℍ | Lemma 1 PROVED; Lemma 2 (no positive invariant form on Re s=¼) PROVED; Cor 3 (class «norm in spectral variable»: comb Λ(n)/n at abscissa 1) PROVED; extension to «all Eisenstein positivity» WITHDRAWN (addendum) | (ii) for the norm class; moreover O10/O12 survive (failure of O10/O12: CITED in P47) | (a) norm class |
| CA_A_001_REVIEW | — | confirms Lemma 2 (FIX: irreducibility unnecessary), Cor 3 (FIX of the comb sign); rejects «line doubling» as a general barrier: Mellin in y and RS in w reach ζ(½+iτ) on the unitary axis | = memo | (a) norm class |
| CA_A_002 | transfer operator / period functions | Prop 1 PROVED (identity Σ(m+n)^{−2s}); NO-GO ARGUED overall; formula for ψ_s CITED-UNVERIFIED; «does not preserve cones on Re s=¼» ARGUED | (ii)-trivial: the object does not contain Λ ⇒ O1–O7, O15 leave it invariant (pattern lem:shape-ident); Λ only via det (zero side); O12 survives (CITED in sketch) | (a) object as formulated (see disagreement D3) |
| CA_A_002_REVIEW | — | EXCLUDED by (R)(1),(3),(4) and absence of Λ; withdraws «line doubling» as a reason | = memo | (a) |
| CA_A_003 | Hecke multiplicativity on σ_T; Hecke tests; metaplectic escape | §2 Thm PROVED (Hecke relations = cosine product identities, valid for every position) ⇒ (B″); §3 test side = (S) and (B′); §4 off-diagonal metaplectic packet form OPEN, not built | §2 (ii) via (B″); §3 (iv); §4 (v) in this memo | §2 (a); §3 (c); §4 → developed in CA_A_004 |
| CA_A_003_REVIEW | — | confirms; §4 CITED-UNVERIFIED, pre-warning: packet positivity is a norm | = memo | — |
| CA_A_004 | weight ½ Eisenstein series on Γ₀(4), Parseval on a horocycle | citation verified (coefficients L_D(2s−½)/ζ(4s−1)); Prop 1 off-diagonal kernel of rank one per index PROVED; Cor 2 (matching a multiplier requires orthogonality in D) PROVED as a necessary condition, «⇒ (B′)» ARGUED; Cor 3 ARGUED with FIX (thm:sos does not literally cover squares of smoothed L_D); Kuznetsov/Salié variant OPEN-RESIDUE | (ii)-trivial: object without Λ ⇒ O1–O7, O15 invariant; O12 in sketch | (a) object; variant → (e) |
| CA_A_004_REVIEW | — | EXCLUDED; Cor 2 only a reduction; addendum R3 (opening) not endorsed | = memo | (a) |
| CA_A_005 | regularized RS with test vector from the minimizer polynomial | Prop 1 (RS_w ≥ 0 for every test, w>1, without comb) PROVED; Prop 2 (no continuous kernel is the window multiplier) PROVED; Prop 3 PROVED; Prop 4 (continuation to ½ loses positivity: PROVED; continued kernel = second moment: ARGUED) | (ii) via (B″) for w>1; (iv) for the continuation (ARGUED) | (a) w>1; continuation (c)/(b) |
| CA_A_005_REVIEW | — | confirms Props 1–3; Prop 4 ARGUED; O12 survives | = memo | (a) |
| CA_A_006 | abscissa transport 1→½ of Maass–Selberg: (i) Hecke average, (ii) integration in Y | Lemma 1 PROVED; Thm 2 (positive integration in Y does not move the arithmetic abscissa) PROVED; Obs. 3 (MS = window form of ζ(2s) on squares) PROVED as an identity, «class 𝒞_PNT» ARGUED; (i) = (S): indefinite truncation PROVED, value |ζ|² only formal | (ii) for (ii); (iv) for (i) | (a) (ii); (c) (i) |
| CA_A_006_REVIEW | — | confirms; §6 (homotopy) pre-warned as a retry: by concavity, non-crossing on a segment = target | = memo | — |
| CA_A_007_SEED_TRIAGE… | homotopy/non-crossing; boundary triples; RP between places; t-concavity; rigged eigenvectors | homotopy withdrawn (retry N_012/W5/flowdet/W-cont); triples = coordinates of thm:parityschur (Prop 1 PROVED reduction); Lemma 1 (𝔞(f+Θf)=2𝔞(f)+2H_K(f), Toeplitz level) PROVED; Thm 2 (RP fails for every comb with an atom) PROVED; t-concavity and rigged eigenvectors: one line ARGUED | homotopy (iv)+retry; triples (iv); RP (i) falsifier: symmetric bump at ½log n₀, failure PROVED, for every comb; t-concavity (iii); eigenvectors (iii) | (c), (c), (a), (d), (e) |
| CA_A_007_REVIEW | — | confirms; §6 (index) pre-warned: n₋ / first contact | = memo | — |
| CA_A_008 | integer invariant (spectral flow, Maslov, signed index) | Lemma 1 (constancy ⟺ no crossing) PROVED; COLLAPSES (REF-D); forcing mechanisms dead by NO-GOs cited from the corpus | (iv) | (c) |
| CA_A_008_REVIEW | — | confirms; Cayley index (corpus 632) still unbuilt | = memo | (c) |
| CA_A_SYNTHESIS | closure of front A | lists PROVED facts; residues: Kuznetsov/Salié, general propagation (M), Cayley index | — | — |

### Front B

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_B_001 | pairing identity I_ζζ = −J′(½)/2π | identities (1.1)–(1.3) PROVED; sign of J′(½) = zero geometry ARGUED (later bounded by CA_D_001 to its frozen weight) | (iv) (sign = piece of the form itself) + O10/O12 survive | (c) |
| CA_B_001_REVIEW | — | EXCLUDED (O10, O12; (R)(4),(9)); REF-D | = memo | (c) |
| CA_B_002 | Riesz/Jensen of −∂_σ log|ζ/Z_{<X}| in the strip | (2.1) PROVED modulo CITED potential; zero-free reading = identity for every comb | (ii) via (B″) in the zero-free reading; (R)(4) in the other | (a) |
| CA_B_002_REVIEW | — | EXCLUDED; adds local (R)(5) | = memo | (a) |
| CA_B_003 | self-pairing Δ_a ≡ 0 | Thm 1 (Δ_a≡0 ⟺ functional equation) PROVED; uniqueness a=Λ CONDITIONAL (cited uniqueness theorem), case ε=−1 OPEN; sign step by penalization ARGUED false | (i) falsifier O7 (quartets keep the comb; failure PROVED in P47 lem:shape-quartet) | (a) O7 for the property alone |
| CA_B_003_REVIEW | — | confirms; FIX on DH; exclusion by O7 | = memo | (a) |
| CA_B_004 | symbol on the line without ζ; transport J(σ), Green identity | Prop 1 PROVED (rewriting); (3.1) PROVED on [½,1) and (1,2]; convexity chain (3.3) FALSE by J(1)=∞ (PROVED); (W_σ) for g_X: OPEN, generically false ARGUED | (ii) (B″) for the identity; NO-GO PROVED for convexity across σ=1 | (a); residue (W_σ) on [½,1) unrecorded (see §3) |
| CA_B_004_REVIEW | — | major FIX (pole); NO-GO convexity PROVED | = memo | (a) |
| CA_B_005 | inversion «defect ⇒ negative bottom» | Prop 2 PROVED after FIX (it is prop:wit-sens); (Inv) FALSE; §3 (openness excludes fine properties) NON-SEQUITUR; §4 pairing distances ARGUED | (i) falsifier Λ+cδ₂ with small c (positive and with Δ≢0), PROVED | (a) for (Inv) |
| CA_B_005_REVIEW | — | Prop 2 corrected (ℓ¹ radius); §3 not endorsed | = memo | (a) |
| CA_B_006 | open ball lemma; interior sets; (W_X) | Lemma B (i)–(iii) PROVED (= prop:wit-sens); (iv) methodological reading WITHDRAWN; (W_X) passes (R)(4) (PROVED) but controls only I_ζζ | (iv)-partial: I_ζζ is one of four pieces (PROVED via EI_002) | (a) for (W_X) as complete carrier |
| CA_B_006_REVIEW | — | confirms (i)–(iii); scale FIX; repeated pole FIX | = memo | (a) |
| CA_B_007 | O7/O8 as point moves; convex decomposition | Prop 1(a) PROVED, 1(b) ARGUED; decomposition = target / extended segment / class (D); Prop 2 (Γ=0 ⟺ common minimizer) PROVED | (iv) | (c) |
| CA_B_007_REVIEW | — | confirms; Γ OPEN pre-warning REF-D | = memo | (c) |
| CA_B_008 | concavity gap Γ, angle bound | Thm 1 (Γ ≥ min(θg₁,(1−θ)g₂)(1−|⟨h₁,h₂⟩|)) PROVED; REF-D tautology PROVED; (B″); (R)(5) | (iv) + (ii) (B″) | (c) |
| CA_B_008_REVIEW | — | confirms; family of decompositions closed | = memo | (c) |
| CA_B_SYNTHESIS | closure B; list (P1)–(P6) | — | — | — |

### Front C

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_C_000_SEEDS | C1–C6 | C1 discarded (weighted HM division; negative cone argument «implausible», ARGUED); C2 (B″) and jump identity PROVED; C3 → C_001; C4 REF-D; C5 → C_002; C6 → C_002 | C1 (iii); C2 (ii); C4 (iv) | C1 (b); C2 (a); C4 (c) |
| CA_C_000_REVIEW | — | C1: discard correct, reason partly wrong; archimedean condensed ARGUED | = | — |
| CA_C_001 | product formula as coupling | Lemmas 1–4 PROVED; Thm 1 (local/global table) PROVED, two cells CONDITIONAL (κ_T≠0); (Fam_η) OPEN sub-statement | (i) falsifiers Λ±c1₆, Λ±c1_{p₀}, a_P, Λ+c1₂, failure PROVED (Lemma 3 + lem:cpos); review adds O7 for all cells | (a) |
| CA_C_001_REVIEW | — | confirms; adds exclusion O7 | = | (a) |
| CA_C_002 | classical Hasse–Minkowski; torus vs line | Prop 1 (class 𝓗) PROVED with falsifier ⟨−1,−1,−1,−1⟩⊥r; Prop 2 (Near = line − Haar on boxes) PROVED, coordinates; positivity = (S); condensed with archimedean input ARGUED | (i) PROVED for 𝓗; (iv) | (a) 𝓗; (c) |
| CA_C_002_REVIEW | — | confirms | = | — |
| CA_C_003 | (Fam_η) = T*₃(η), η>2/3 | Prop 1 PROVED; Prop 2 deduction PROVED from NUMERICAL input (minimizer outside the span); obstruction §3 ARGUED | (iii)+NUMERICAL: «only necessary» | (b) (see D6) |
| CA_C_003_REVIEW | — | confirms; do not run μ_M | = | — |
| CA_C_004_SEEDS_BATCH2 | D1–D6 | D1 = (N) REF-D and pointwise false at 0 (σ_T(0)<0 PROVED); D2 O7 with rational parameters ARGUED; D3 category (ℚ_p not ordered) + O7 ARGUED; D4 category (λ, μ are ranks/valuations) + (R)(10); D5 retry prop:shape-phase (B″); D6 REF-D | D1 (iv); D2 (iii); D3 (ii)-category; D4 (ii)-category (same basis as D3); D5 (ii); D6 (iv) | (c), (b), (a), (a)/(b) same as D3, (a), (c) |
| CA_C_004_REVIEW | — | confirms; D2 O7 witness ARGUED | = | — |
| CA_C_005 | numerical μ_M(η) | NUMERICAL all positive; conclusion «critical» WITHDRAWN (wrong ℓ² norm) | — | — |
| CA_C_005_REVIEW | — | direction error (lower bound) | = | — |
| CA_C_006_SEEDS_BATCH3 | E1–E6 | E1 semialgebraic set ⇒ Pila–Wilkie empty ARGUED; E2 commuting not free PROVED elementary, asymptotic ARGUED; E3 O11/O15; E4 = torus/line + (B′); E5 SOS class (D); E6 discarded as a route, kept as a classification | E1 (iii); E2 (ii) exact/(iii) asymptotic; E3 (i) CITED/ARGUED in P47; E4 (iv); E5 (iv); E6 → developed in C_007 | (b), (a)/(b), (a), (c), (c), see C_007 |
| CA_C_006_REVIEW | — | confirms; FIX premise [crit] | = | — |
| CA_C_007 | η family: Gram norm, reduction to a scalar, falsifier test | critical premise retracted; Lemmas 1–2, Prop 3 (s_M Schur scalar) PROVED; zero-side identity PROVED, mechanism ARGUED; positivity of the family FE-generic (x²+5y² positive on the family, complete form negative: NUMERICAL) | (i) falsifier x²+5y² for the «ζ-specific» property, failure NUMERICAL (and CITED in P47 for the complete form) | (b) |
| CA_C_007_REVIEW | — | confirms; exclusion by thm:shape(C) with label NUMERICAL | = | (b) |

### Front D

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_D_000_SEEDS | D1–D9 | D1 coordinate (B″); D2 → tool; D3 retry (falsifier ζ·E, PROVED in corpus); D4 (R)(4)/(B″); D5 retry (f_χ); D6 ⟺ half-plane without zeros of Z_X; D7 σ_T(0)<0 + certificate; D8 one line (corrected in CA_R2_001); D9 → D_002 | D1 (iv); D3 (i) PROVED; D5 (i) corpus; D6 (iv); D7 (i) σ_T(0)<0 PROVED | (c),(a),(a),(c),(a) |
| CA_D_000_REVIEW | — | confirms; O7 for D2 pre-warned | = | — |
| CA_D_001 | Hardy amplitude transfer | Thm 1, 1′, Cor 1.1, central cell bound PROVED; Thm 1″ (FE class) PROVED; excluded as a sign step because it holds in O10/O12 | (i) O10/O12: the theorem holds on objects whose form is negative (failure CITED in P47; NUMERICAL in CA_C_007) | (a) as sign step; living tool |
| CA_D_001_REVIEW | — | rederived; bounds the scope of CA_B_001 §4 | = | — |
| CA_D_002 | closure of the transferred cone | Thm 2, 2′, Cor 2.1 PROVED (Thm 2 uses classical CITED results only inside the NO-GO; Thm 2′ without zeros); classification of amplitudes §3.6 OPEN | (ii) | (a) |
| CA_D_002_REVIEW | — | confirms | = | (a) |
| CA_D_003 | transfer vs family s_w; amplitude-one residue | §1 (a)(b)(c) PROVED (2 FIX); §2 five residues DEAD/REF-D | (iv)/(R)(4)/(R)(5) | (c) |
| CA_D_003_REVIEW | — | confirms | = | — |
| CA_D_SYNTHESIS | closure D | «the defect lives in {|ζ/Z_{<X}|<1}», a reading, not a reduction | — | — |

### Front E

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_E_000_SEEDS | E1–E12 | E1 real β only (ARGUED), O11, retry; E2 commutative ⇒ pointwise criterion false at 0; E3 «there is no object»; E4/E5 → E_001; E6 retry; E7 density (O11/O15) + Thm 2 of E_001; E8 (B′) + equality before compression, compression «closed territory» ARGUED; E9 retry, (B′), (R)(4); E10 direction (lem:monoT); E11 REF-D; E12 commutative collapse PROVED | E1 (iii); E2 (i) σ_T(0)<0 PROVED; E3 (v); E6 inheritance; E7 (ii); E8 (ii)/(iii); E9 (iii); E10 (ii); E11 (iv); E12 (ii) | (b),(a),(d),—,(a),(a),(a)/(b),(b),(a),(c),(a) |
| CA_E_000_REVIEW | — | confirms | = | — |
| CA_E_001 | commutative collapse; Schur factorization NO-GO | Lemmas 0–1, Thm 1 (product vectors suffice), Cor 1.1 (Fejér means at points y∈Ĝ), Cor 1.2, Thm 2 PROVED; line-type factorization (ν=ν₁∗ν₂) ARGUED; 𝔸_M=𝔾_M∘𝔹_M at fixed M not excluded | Thm 1 (iv); Thm 2 (ii) | (c) E4; (a) E5 |
| CA_E_001_REVIEW | — | confirms | = | — |
| CA_E_SYNTHESIS | closure E | — | — | — |

### Front F

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_F_000_SEEDS | F1–F15 | F1 Lemma F1 PROVED (spectral); F2 Lemma F2 formal; F3 → F_001; F4 signature; F5 Lemma F5 with FIX, signature hypothesis ARGUED; F6 retry R164_502 + (B′)/(B″) (later covered by F_003 Prop 2); F7 → F_002; F8 certificate; F9/F13/F15 → F_003; F11 O2/O6; F12 spectral; F14 σ_T(0)<0 | F1/F2/F4/F12 (iv); F5 (iii); F6 (iv) via F_003 Prop 2; F8 (iv); F11 (i) O2/O6 PROVED in P47; F14 (i) | (c),(c),(c),(b),(c),(c),(a),(c),(a) |
| CA_F_000_REVIEW | — | confirms; FIX F5 | = | — |
| CA_F_001 | condensed/liquid MW-3 | Lemmas 1–2 (condensed or liquid reformulation = same statement, for every Hausdorff topology with density) PROVED; Prop 3 (bare local positivity false at every p) PROVED; Prop 4 (assigned = convex division) REF-D | (iv) + (i) test F₊ of prop:cone(ii), PROVED | (a)/(c) — also covers C5L (see D5) |
| CA_F_002 | exact trace formulas, horocycles, Heegner | Lemma 1 PROVED (FIX multiplicity, parity); Cor 2–3 PROVED; NO-GO class TF⁺ PROVED; Arthur (G,M) ARGUED | (ii) | (a) — covers exact F7 |
| CA_F_003 | polarized object over ℤ | Lemma 1 tautological PROVED; Prop 2 (unitary invariants = spectral data) PROVED; trichotomy outside 𝒢_u ARGUED; gap G-F OPEN | Prop 2 (iv); G-F (v)-object | (c); G-F (e) |
| CA_F_001_003_REVIEW | — | confirms; upgrades F_001 to PROVED | = | — |
| CA_F_SYNTHESIS | closure F | — | — | — |

### Front G

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_G_000_SEEDS | G1–G12 + facts G0 (squares = Gram) and G1 (monoid) | G1 REF-D; G2 both summands indefinite; G4 G0(c); G5 O10 by lattice characters; G6 retry; G7 PF₅ fails CITED, PF₄ OPEN; G8 = thm:D1; G9 = Wiener–Hopf; G10 G1+G0; G11 retry; G12 G1 / O7 | G1 (iv); G2 (ii) natural partition; G5 (iii); G7 (i) CITED order ≥5; G12 (iii)/(i) | as in LABELS |
| CA_G_001 | monoid lemma; SUSY; Elias–Williamson-type ladder | Lemma G1 PROVED (isomorphism); exclusion via (R)(10) (review), not by thm:shape(A) because O11 ARGUED, O12 OPEN in P47; §2 REF-D; §3 REF-D/retry | G1 (iii)-clause (R)(10); §2–§3 (iv) | (b) monoid; (c) |
| CA_G_000_REVIEW | — | confirms; FIX scope of G1 | = | — |
| CA_G_SYNTHESIS | closure G | — | — | — |

### Front H

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_H_000_SEEDS | H1–H10; fact H0 (test +/·) | H0(a),(c) PROVED, (b) ARGUED; H3 folded into H_001 §1.4; H4 survives O11/O15 and (B′); H7 necessary direction; H9 retry; H10 G1 | H3 (ii)-definitional; H4 (i) O11/O15; H7 (ii); H10 (iii) | (a),(a),(a),(c),(b) |
| CA_H_000_REVIEW | — | confirms; FIX H0(b) | = | — |
| CA_H_001 | p-derivations, Wronskian, δ-log of ζ, Frobenius lifts | Props 1.1–1.3, 2.2, 3.1–3.5, 5.1, 5.3, Cor 5.4 PROVED (+CITED); Cor 2.3 PROVED product case, ARGUED general; §1.4 «form blind to carries» PROVED (definitional) | (ii) declared classes | (a) |
| CA_H_002 | successor invariant (S⁺); Div = Haar, Near = line − Haar | Thm 2.2 PROVED (from cited theorem); Cor 2.3 O7; Prop 2.4 PROVED; Thm 3.1/3.2 PROVED (extension of CA_C_002 Prop 2); Prop 3.4 PROVED, reading ARGUED; Cor 3.5 REF-D | H5 (i) O7 PROVED; H6 (iv) | (a); (c) |
| CA_H_001_002_REVIEW | — | confirms; FIX Lemma 4.1(ii) | = | — |
| CA_H_REVIEW | — | line-by-line self-check | = | — |
| CA_H_SYNTHESIS | closure H | — | — | — |

### Front I

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_I_000_SEEDS | I1–I10; fact I0 | I6 automatic (exponential type); the rest → memos | I6 (ii) | (a) |
| CA_I_J_000_REVIEW | — | confirms I_000 and J_000; recomputes J0/J0′ | = | — |
| CA_I_001 | Markov / Krein–Rutman / maximum; rigidity «Markov ∀T»; 𝖯⋆ | Thm 1 PROVED; Prop 1.1–1.2 PROVED; Thm 2 (class 𝒦_M closed under O2, λ_A→−∞) PROVED; Thm 3 PROVED (formula for general rational E ARGUED); Lemma 4 (≥2 sign changes) PROVED; Prop 5 PROVED; Cor 6 separation, REF-D as a route | I1 (i) falsifier Λ+c1_{n₀}, failure PROVED (three-bump construction); I1⋆ (iv) | (a); (c) |
| CA_I_002 | virial, boundary layer, frequency, Γ-convergence, concentration–compactness | Prop 1.1 (B″) PROVED; Prop 1.2: V3 falsified by DH with transversality ARGUED, V3 is REF-D; Props 2.1–2.3 PROVED (one-sided boundary information, Lemma S(iv)); §3 uses an internal CITED upper bound (also concludes with cor:margin1 of P47); §4 absolute o(1) (ARGUED vs margin); §5 I(α)=αL linear PROVED | I4 (ii) identities + (iv) V3; I9 (iv); I5 (ii); I7 (iii); I8 (ii) | I4 (a)/(c); I9 (c); I5 (a); I7 (b); I8 (a) |
| CA_I_001_002_REVIEW | — | confirms; Thm 3 highlighted new fact | = | — |
| CA_I_SYNTHESIS | closure I | O14 open (closed later in CA_R1_001) | — | — |

### Front J

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_J_000_SEEDS | J1–J12; Lemmas J0, J0′ | J0/J0′ PROVED (kernel values, not form values); J4 REF-D; J4′ dimension data (O11); J5 retry PF; J8 one line; J10 perturbative | J4 (iv); J4′ (iii); J5 (i) CITED; J8 (iii); J10 (iii) | (c),(b),(a),(d),(b) |
| CA_J_001 | lattice RP per prime; checkerboard | Thm 1 PROVED (small T₀, explicit p=2); Thm 2 (RP_p ⟺ support of ν in (π/log p)ℤ) PROVED; Cor 3 PROVED (CITED); Cor 4 PROVED p≤7, ARGUED general; Prop 5 PROVED transpositions | (i) δ_{e_p}: R_p=𝖡(2log p)<0, PROVED | (a) |
| CA_J_002 | GKS (frustration); FKG on the divisor lattice | Lemmas 1.1–1.2 PROVED; Thm 1.3 PROVED (unconditional for 2T₀≤0.1); Prop 2.1, Cor 2.2, Prop 2.3 PROVED; Prop 2.4 (Holley) ARGUED | J1 (ii); J2 (ii); J11 (iii) | (a),(a),(b) |
| CA_J_001_002_REVIEW | — | confirms | = | — |
| CA_J_SYNTHESIS | closure J | — | — | — |

### Front K

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_K_000_SEEDS | K1–K13 | K3 REF-D; K4 exact SDP = class (D); K5 = PSD; K9 requires RP; K11 retry; K12 local; K13 perturbative | K3/K4/K5 (iv); K9 (i) via J_001; K13 (iii) | (c),(c),(c),(a),(a),(a),(b) |
| CA_K_000_REVIEW | — | confirms | = | — |
| CA_K_001 | diamagnetism, holonomy, signed Laplacian | Lemma 0, Lemma 1.1, Thm 1.2, Prop 1.3, Thm 2.1, Thm 2.2 (reversed order: λ_A(0.7;0)<0<λ_A(0.7;Λ), CITED inputs), Props 3.1–3.4, Lemma 4.1, Thm 4.2 PROVED; Cor 4.3 PROVED with CITED Cheeger constants | K8 (ii); K6 (i) falsifier g𝖡 (Prop 3.2, PROVED, generic class); K7 (ii) structural gap PROVED | (a),(a),(a) |
| CA_K_002 | Guerra interpolation; disorder; heat flow on Ĝ; site independence | Thm 1.2 PROVED (sign of the path = statement about the minimizer); Prop 2.1 PROVED; Prop 3.1 PROVED; Thm 3.2, Cor 3.3 PROVED; «Comb_M(s₁) ≤ 0» OPEN (statement about the minimizer) | K1 (iv); K2 (ii); K10 (iv) | (c),(a),(c) |
| CA_K_001_002_REVIEW | — | confirms | = | — |
| CA_K_SYNTHESIS | closure K | — | — | — |

### Front L

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_L_000_SEEDS | L1–L10; table V1–V3 | L7 one line; L9 one line; L10 retry | L7/L9 (iii) | (d),(d),(a) |
| CA_L_000_REVIEW | — | confirms | = | — |
| CA_L_001 | literal magic function; CE direction; class of modular data | Thm 1.1 (= thm:O as slackness) PROVED; Rem 1.1′ ARGUED; Prop 2.1, 3.1 PROVED; Thm 4.2 (level 20) PROVED modulo CITED falsifier O10; level 1 reduced to constructions on the comb | L1 (ii); L2 (i) genus pair x²+5y², failure CITED; L3 (ii) direction | (a),(a),(a) |
| CA_L_002 | prime-site LP; certificates on the torus | Props 1.2, 1.3, Thms 2.1–2.3, Cor 2.4, Props 3.1–3.2 PROVED (2.2 with CITED); REF-D with attained duals | (iv) | (c) |
| CA_L_001_002_REVIEW | — | confirms | = | — |
| CA_L_SYNTHESIS | closure L | — | — | — |

### Front M

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_M_000_SEEDS | M1–M8 | M4 retry; M5/M7 discarded after §1.3–§1.4 and proved in the decisive class by §3 | M4 (i) corpus; M5/M7 (ii) decisive class | (a),(a),(a) |
| CA_M_000_REVIEW | — | confirms | = | — |
| CA_M_001 | form on prime sites; parity; integrality; antidiamagnetic inversion | Prop 1.1 PROVED; §1.2 (each Near_q trace 0 ⇒ indefinite) PROVED; §1.3 PROVED; §1.4 ARGUED; Thm 3.1, Cor 3.2, Prop 3.3 PROVED; Prop 4.1 PROVED; Cor 4.2 (i),(iii) PROVED, (ii) ARGUED; Prop 4.3 ARGUED | M2 (ii); M3/M8 (ii)/(iv); M6 (i) O10/O12 (identity only uses FE) | (a),(a),(a) |
| CA_M_001_REVIEW | — | confirms | = | — |
| CA_M_SYNTHESIS | closure M | — | — | — |

### Front N and round R

| file | mechanism | primary verdict | basis | class |
|---|---|---|---|---|
| CA_N_000_PLAN | plan V1–V3 | — | — | — |
| CA_N_001 | V1 discrete primal attained | Lemma 1.1, Prop 1.2 PROVED; Cor 1.3 «M(T) unbounded» ARGUED; Prop 2.1 PROVED (|X|=2; general ARGUED); Prop 2.2 PROVED, identification with zero comb ARGUED; Prop 2.3 PROVED | (ii) window LP; (iv) sites | (a)/(c) |
| CA_N_002 | V2 positive combs | Prop 1.1, 2.2, 2.3 PROVED/CITED; Thm N2 PROVED (for T>½log3 after FIX); 𝒰_T for T≤½log3 undecided | (ii) class 𝒰_T | (a) |
| CA_N_003 | V3 self-structure; assembly | Prop 1.1; Thm 3 PROVED (scope: declared candidates); Thm 4 PROVED moderate growth, ARGUED weakly holomorphic; Thm 5 conditional on falsifier O10 (complete form CITED, primitive ARGUED) | (ii) Thms 3–4; (i) O10 for Thm 5 | (a) |
| CA_N_REVIEW | — | confirms; FIX threshold N2 | = | — |
| CA_N_SYNTHESIS | closure N; residue: non-unimodular transfers | — | — | N2r (e) |
| CA_SYNTHESES_REVIEW | review of syntheses A–H | endorses; specifies: self-pairing by O7 alone; monoid by (R)(10) | — | — |
| CA_R1_001 | 𝖯⋆: separation vs inequality; O14 | §0 jump-measure criterion PROVED; Props 1.1–1.3 PROVED (O14 closed); Prop 1.2 Markov at small T PROVED, large T OPEN; Thms 2.1–2.3 PROVED; non-identifying remainder ARGUED; D_∃c OPEN | (iv) by identification | (c); D_∃c (e) |
| CA_R2_001 | amplitude homotopy W_F(α) | §1 zero-free family PROVED (corrects D8); §2 PROVED; Prop 3.1 method-class NO-GO PROVED (two-atom model); Prop 3.2 pointwise FALSE PROVED, integrated ARGUED; Prop 4.1 PROVED main term, ARGUED complete; §5 REF-D | (ii) method class | (a); rest (c) |
| CA_R2_002 | SPEC_A (γ) with proved margin | (1.1) PROVED; (γ) fails with exponent ≥7.72 vs δ≤½ (δ≤½ ARGUED); identities-only version OPEN | (iii) + PROVED margin | (b); identities (e) |
| CA_R1_R2_REVIEW | — | confirms all three | = | — |
| CA_R3_001 | θ line, L*_j(θ) | Prop Θ, Lemma C PROVED; (Ch) CITED; «ADMISSIBLE» not endorsed → REF-D | (iv) | (c) |
| CA_R3_001_REVIEW | — | REF-D; O7/O9 escape only by identification | = | (c) |
| CA_R4_001 | L*_j(θ) at ½log5 → ½log7 | Props R4.1, R4.2 PROVED; sign OPEN; method NO-GO ARGUED; living line: exterior continuation of the Euler–Lagrange equation | (iv) + (iii) | (e) |
| CA_R4_001_REVIEW | — | confirms; pre-warning: the living line is REF-D | = | (e) |

### Control documents

| file | content | observation |
|---|---|---|
| CAMPAIGN_LEDGER | master table by rounds | agrees with reviews; records errata O1–O15, O14 closed, D_∃c |
| README | phase summary | agrees with ledger |

---

## 2. Disagreements with ANNEX_PHASE_193_LABELS.md

| # | candidate | class in LABELS | class according to primary memo | reason | citation / line |
|---|---|---|---|---|---|
| D1 | A1r (Mellin in y / RS in w) | (e) «OPEN, never developed» | (a) for RS in w with w>1 (= A5); (b) for the continuation to Re w=½; (d) for Mellin in y | CA_A_005 is exactly RS in w with test from the minimizer: positivity w>1 blind to the comb (PROVED); the continuation loses positivity (PROVED) and its identification with (S) is ARGUED; Mellin in y only gets one ARGUED line in CA_A_004 §6 R1 | CA_A_005 §2 Prop 1, §3 Prop 4 «(ARGUED: the off-diagonal part of the continued kernel is not evaluated.)»; CA_A_004 §6: «This is ARGUED, not built.» |
| D2 | A3r (off-diagonal metaplectic packet) | (e) «never developed» | (b), absorbed into A4/A4r | CA_A_004 Q3 and Prop 1 treat precisely the off-diagonal term: rank one per index (PROVED); the exclusion via (B′) is ARGUED; what is not excluded is the exact Kuznetsov-type resolution = A4r | CA_A_004 §1 «Q3 … No. See §2, Prop. 1: per index n the off-diagonal kernel is rank one»; review: «"⇒ estimate (B′)" ARGUED (an exact Kuznetsov-type resolution is not excluded)» |
| D3 | A2 (transfer operator) | (b) | (a) for the object as formulated — same basis as A4, which LABELS puts in (a) | the review excludes by absence of Λ (all O1–O7, O15 leave the object unchanged), not by the cone argument; what is ARGUED/CITED-UNVERIFIED is not load-bearing | CA_A_002_REVIEW: «EXCLUDED ((R)(1),(3): Λ absent ⇒ invariant under O1–O7, O14, O15 trivially…)» |
| D4 | CD4 (Iwasawa) vs CD3 (Kummer) | CD4 (d), CD3 (a) | same class for both | both rest on the same category reason (ranks/valuations; ℚ_p not ordered, CA_C_002 Prop 1 PROVED) plus one ARGUED O7 line; there is no basis to separate them | CA_C_004 D4: «the invariants λ, μ ≥ 0 are ranks and valuations… They carry no real sign (CA_C_002 Prop 1)» |
| D5 | C5L (condensed HM with archimedean liquid input) | (b) «missing class with liquid input» | (c) (and (a) for the local parts) | CA_F_001 Lemma 2 (PROVED) covers every Hausdorff completion, liquid included: the condensed/liquid statement is literally the same; Prop 4 the local assignment is convex division (REF-D); the review upgrades to PROVED | CA_F_001 Lemma 2: «Suppose q is continuous for a p-liquid (or any Hausdorff) topology … q ≥ 0 on V ⟺ q̂ ≥ 0 on V̂»; CA_F_001_003_REVIEW: «upgrade from my F_000 review's ARGUED» |
| D6 | C7 ((Fam_η) = T*₃(η), η>2/3) | (d) «numerical datum; not a sign examination» | (b) | examined in three memos (C_003, C_005, C_007): reduction to a scalar PROVED; separation of falsifiers NUMERICAL (x²+5y² positive on the family; Beurling negative); exclusion as sign step by thm:shape(C) with NUMERICAL falsifier — same situation as C8 | CA_C_007 §6: «Its positivity is FE-generic (NUMÉRICO …), so it is excluded as a sign step by O10» |
| D7 | CE6 (zero-side identity for the family) | (d) «not developed» | (b) (classification done, mechanism ARGUED) | it was the main task of CA_C_007 §1: identity PROVED; «criticality produced by zeros» ARGUED | CA_C_007 header: «make E6 the main task»; §1 «Label: ARGUED (the identity is PROVED…)» |
| D8 | CE1 (o-minimality) | (a) «only writing it up is missing» | (b) | the memo and the review label it ARGUED; by LABELS' own rule, what is not written up is not (a) | CA_C_006 E1: «semialgebraic (ARGUED)»; review: «"never constructed → pre-screened NO-GO (ARGUED)" ENDORSED» |
| D9 | F6 (Weyl laws / heat) | (d) | (c) | CA_F_003 Prop 2 (PROVED) explicitly includes heat/Weyl invariants among the unitary invariants = spectral data; moreover retry DEAD R164_502 | CA_F_003 §3: «This covers Floer homology, capacities, signatures, A¹-/GW-degrees of real forms, and heat/Weyl invariants (F1, F2, F4, F6, F12)» |
| D10 | F7 (Selberg trace / horocycles) | (d) | (a) for the exact form (class TF⁺, = F16); (B′) for rates | CA_F_002 «develops F6, F7 and F14 … in their exact forms»; NO-GO PROVED for TF⁺; exact horocycle at abscissas 0 and 1 | CA_F_002 header and §3 |
| D11 | F13 (perfectoid tilting) | (d) | (a) in the local part; the rest is G-F (e) | CA_F_003 §4: the local part is CA_F_001 Prop 3 (PROVED); it produces no surface | CA_F_003 §4: «F13 … local at one p … The local part is CA_F_001 Proposition 3» |
| D12 | H3 (carries / Witt) | (b) «missing proved statement of blindness» | (a) (definitional) / (c) by its only channel (Near = H6) | the memo states the blindness and labels it PROVED: the form object = (Γ factor, comb), no C_p(a,b) enters; index sums only enter through Near | CA_H_001 §1.4: «Carries (seed H3 folded here; PROVED) … no quantity C_p(a,b) for a pair of integers enters the definition» |
| D13 | I9 (boundary layer) | (b) «missing proof of DH transversality» | (c) | DH transversality belongs to I4 (V3), not to I9; I9 rests on Props 2.1–2.3 PROVED: boundary information only bounds from above (Lemma S(iv)) and is class-generic (dies at O7) | CA_I_002 §2 Prop 2.2 «bounds the Schur margin from above … a lower bound on λ_A needs 𝔰_j ⪰ 0, the target (REF-D)»; §7.1 «Prop 1.2(V3) DH falsification relies on a transversal DH crossing: ARGUED» |
| D14 | I8 (concentration–compactness) | (b) «write up as a lemma» | (a) | the proof (I(α)=αL linear ⇒ no strict subadditivity) is written and labelled PROVED | CA_I_002 §5 «(PROVED inadequacy)» |
| D15 | I5 (Almgren frequency) | (a) «Prop 2.2 PROVED» | (a), but for another reason | Prop 2.2 belongs to I9; I5 rests on §3: bounded frequency ⇒ polynomial decay, incompatible with the exponential upper bound of P47 (cor:margin1); the internal superexponential citation is not needed | CA_I_001_002_REVIEW: «with only P47 cor:margin1 the frequency is still ≥ 15.449T-scale, conclusion (R)(6) unchanged» |
| D16 | J11 (Holley) | (a) «equality class J2» | (b) | Prop 2.4, which treats it, is labelled ARGUED | CA_J_002 Prop 2.4 «(ARGUED)»; synthesis: «linear in Λ and local (Prop 2.4, ARGUED)» |
| D17 | K7 (signed Laplacian / Cheeger) | (b) «loss ARG/NUM» | (a) | Thm 4.2 PROVED (1−O(1/M) is required); Cor 4.3 PROVED with CITED Cheeger constants (≤½); there is no NUMERICAL | CA_K_001_002_REVIEW: «Cheeger constants CITED, structural gap PROVED» |
| D18 | M7 (Vinogradov arcs) | (b) «missing proof of negligible weight away from θ≈0» | (a) in the decisive class (same as M5) | §1.4 is ARGUED, but the final verdict rests on Thm 3.1/Cor 3.2/Prop 3.3 (PROVED): site arithmetic carries no information and bounded shifts weigh zero | CA_M_001 §6: «M5/M7: DISCARD (resolution; PROVED in decisive class)» |
| D19 | E8 (Golden–Thompson) | (a) | (a) without compression; (b) with compression | equality by commutation holds before compressing; the content of the compression is declared «closed territory» only ARGUED | CA_E_000 E8; CA_E_SYNTHESIS «(ARGUED)» |
| D20 | CE2 (free probability) | (a) | (a) for exact freeness; (b) for asymptotic freeness | commuting ⇒ not free PROVED; the truncated case and the [crit]/O5 argument remain ARGUED (FIX) | CA_C_006 E2 «ARGUED: asymptotic freeness fails»; review FIX (2) |
| D21 | §17 item 12 of LABELS (central cell with the tool CA_D_001) | proposed as a target | contradicted by the source | CA_D_002 Thm 2′ (PROVED) shows that the closure of the transferred cone is doubly exponentially small in the central cell; CA_D_003 §2 closes the five residues in {Z_T²<1}; the tool is blind exactly there | CA_D_002 §2.2 «CA_D_001 proves the sign where the Hardy amplitude is large … Row D asks for it with amplitude one» |
| D22 | B4 (transport J(σ)) | (a) | (a) for convexity across σ=1; unrecorded residue | (W_σ) on [½,1) for g_X remained OPEN (only «generically false» ARGUED); the pole does not exclude it on [½,1) and CA_B_006 §3 proved that the transport of g does not use zeros | CA_B_004 §3 «Status: OPEN for g_X; ARGUED false as a comb-generic statement» |

Agreements worth noting (not class disagreements): G1m, H10, G5, G12-monoid, J4′ remain in (b) — the
primary review says «PROVED as a (R)(10) exclusion», but (R)(10) is a clause and not a falsifier with negative
bottom; with the closure rule of LABELS class (b) is correct. I4 in LABELS as (a)(B″) is correct for the
identities; the claim «DH falsifies V3» is ARGUED, and V3 is REF-D anyway.

Total: **22 disagreements** (D1–D22): 7 in which the closure is weaker than recorded (D1, D2, D8, D16, D19, D20, D22);
11 in which the memo supports a stronger closure or a proved reformulation (D3, D4, D5, D9, D10, D11, D12, D13, D14, D17,
D18); 2 rows marked (d) that were in fact examined in depth and remain in (b) (D6, D7); 2 corrections of
reason or of recommendation (D15, D21).

---

## 3. Discards weaker than recorded and missing object

1. **A1r — continuation of RS in w to Re w = ½.** Missing: (a) exact evaluation of the continued kernel off the diagonal
   (CA_A_005 Prop 4 only identifies it on the diagonal); (b) a positivity of the continued kernel that is neither a norm nor a
   second moment. For Mellin in y: a first real examination (today one line).
2. **A3r/A4r — exact Kuznetsov-type resolution in weight ½.** Missing: an inequality on the Salié-sum side that fails
   for a_P and is stable at the λ_A scale; without it the exact formula is generic in the spectrum of Γ₀(4) ((B″)).
3. **B4 residue — (W_σ) on [½,1).** Missing: the weighted Wirtinger inequality ∫ω″|g_X|² ≤ 4∫ω|g_X′|² on [½,1) with
   control of the pole. Even if proved, it covers only I_ζζ (one of four pieces, EI_002): low value.
4. **C1 — weighted Hasse–Minkowski division.** Missing a written lemma: for T ≥ 0.60 and every (c_p), Σc_p ≤ 1, there exists
   F ∈ P_T with 𝔞_∞(F) < 0 and 𝔮_{p,T}(F) > c_p𝔞_∞(F) for some p with c_p > 0 (for example, F in the negative cone of 𝔞_∞ with
   c_F(log p) = 0 for a prime p); today the death is ARGUED.
5. **CD2 — rationality of ζ(2k)/π^{2k}.** Missing the explicit witness: a quartet with rational parameters and negative
   bottom in some window (lem:shape-quartet with parameters in a dense set).
6. **CE1 — o-minimality.** Missing the write-up of the lemma: the set {xy/z ∈ (a,b)} is semialgebraic and its transcendental part
   is empty, so the Pila–Wilkie count contributes nothing; plus the statement (B′) for the counts.
7. **C7/C8/CE6 — η family.** Missing: manual proof of s_M = κM + O(1) with κ > 0 (suggested in CA_C_007), and a (non-
   numerical) proof of the sign of s_M for x²+5y² and for a Beurling system. It is a necessary statement, not a route.
8. **E1 — KMS.** Missing: a lemma that complex β defines neither a state nor a useful positive form, and a proved falsifier instead
   of the density O11.
9. **E9, F5, J4′, J10, K13, I7.** Missing, respectively: own falsifier (E9); proof that the signature hypothesis
   of the complete space fails (n₋ of the complete space > 2, thm:inertia-nogo-type information) (F5); proved falsifier
   for dimension data (J4′); explicit comparison of the perturbative loss with the proved margin
   4·10⁹Te^{−15.449T} (J10, K13, I7).
10. **Group depending on the falsifier O11/O12 (G1m, H10, G5, G12-monoid; also part of E1).** A single lemma
    would close several rows: **a Beurling (O11) or ζ_K (O12) falsifier with PROVED negative bottom**. Today O11 is
    ARGUED and O12 OPEN in P47.
11. **Group depending on the falsifier O10 in the primitive form (D2 as sign step, L2, N3 Thm 5, M6, C7/C8).** A
    single lemma would reinforce them all: **negative primitive bottom PROVED for x²+5y²** (today CITED for the complete form, ARGUED
    for the primitive; NUMERICAL in CA_C_007 for the complete form).
12. **I1g — Markov for general rational E.** Missing the explicit-formula bookkeeping for general E (confirmed only
    for quartets).
13. **J11 — Holley.** Missing the proof of Prop 2.4 (linearity in Λ and coordinate separation in the decisive class).
14. **R4 — step L*_j(θ) at ½log5 → ½log7.** Living line: exterior continuation of the Euler–Lagrange equation (SPEC_A §3);
    pre-warned as REF-D. Missing object: an identity evaluating 𝔄_j^{−1} on the exterior field of four atoms.

Residues present in the source that LABELS does not collect:
- **Fejér means at points y ∈ Ĝ ∖ ι(ℝ)** (CA_E_001 Cor 1.1): family of tests never used (divisor boxes twisted
  by unimodular completely multiplicative functions off the line). Under the target they are ≥ 0; a negative value
  would be a falsifier. Not computed.
- **Schur factorization at fixed M** 𝔸_M = 𝔾_M ∘ 𝔹_M (CA_E_001 Remark (scope)): not excluded; and line-type
  factorization ν = ν₁ ∗ ν₂, excluded only ARGUED.
- **Signed Cayley index** (corpus 632): unbuilt (CA_A_007, CA_A_008, synthesis A).
- **Propagation (M)** in general (L2_027): only its Maass–Selberg/Hecke instance closed (CA_A_006).
- **Comb_M(s₁) ≤ 0** on the lower vector of 𝔸_M (CA_K_002 Thm 1.2): OPEN, statement about the minimizer.
- **Courant-type upper bound** on the number of sign changes of h* (CA_I_001 Lemma 4): OPEN.
- **Case ε = −1** of the self-pairing (CA_B_003 Cor): OPEN.
- **Class 𝒰_T for T ≤ ½log3** (CA_N_002): undecided (irrelevant where the sign is already proved).
- **Non-identifying remainder of 𝖯⋆**: class {a = Λ, 0 ≤ K ≤ ν} (CA_R1_001 §2), not sign-stable, ARGUED.
- **Non-graph correspondences** (Hecke, scale) for G-F (CA_H_001 Cor 5.4, scope): outside 𝒦_δ, OPEN.
- **Direct reading of a reference for the G-F gap** (CA_F_003 §1, last item): pending, low priority.

---

## 4. Reusable PROVED lemmas found in the memos

Those giving positivity or exact reductions useful for the sign:
- **CA_D_001 Thm 1 / 1′ / Cor 1.1.** For F ∈ P_T: (1/π)∫Θ_X′|F̂|²Z_T² = 2∫_T^∞u(|R_E|²+|R_O|²) ≥ 2Tρ_F ≥ 0; mean value
  inequality ∫|F̂|²|ζ(½+iτ)|²e^{−2C_X} ≥ ∫|F̂|². Bound in the central cell: Z_T² ≤ 6.6e^{−√2B_X}.
- **CA_D_002 Thm 2′.** Elements of the closure of the transferred cone are ≤ ε·η_T on |τ| ≤ π/(8T) (without zeros).
- **CA_N_002 Thm N2.** For T > ½log3 there is no unimodular multiplier with window phase making (WF̂)ˇ one-sided;
  bound φ′ ≥ T − 1/(τ²+¼).
- **CA_I_001 Thm 1.** The form (without polar term) is a positivity-improving Markov form; λ_A > λ₀ strictly.
- **CA_I_001 Thm 3 + CA_R1_001 §0.** Markov at T ⟺ jump measure J_T = ν − K + ½Σv_nδ_{log n} ≥ 0; every entire ξE with E
  non-constant rational ceases to be Markov for large T.
- **CA_C_007 Lemma 1, Prop 3.** Tail block of the η family = small window with A_t ⪰ λ_A(T_eff)G_t; positivity on the
  family ⟺ a Schur scalar s_M ≥ 0.
- **CA_E_001 Thm 1, Cor 1.1, Thm 2.** Product (Euler) vectors suffice; Fejér-mean form on Ĝ; there is no Schur
  factorization with an atomless or absolutely continuous product factor.
- **CA_K_002 Thm 3.2, Cor 3.3 / CA_M_001 Thm 3.1, Cor 3.2.** Any discrete set of sites with consecutive
  ratios → 1 is decisive; on prime sites Div ≡ 0 and the target is Arch ≥ Near; the integer arithmetic of the sites
  contributes no information.
- **CA_L_002 Prop 1.2, Thms 2.1–2.3, Cor 2.4.** LP on the torus: s^TM_Xs = (𝖡(0) − η(𝕋^X)) + ∫|P_s|²dη; dual attained;
  slack on Z_s; exact for |X| ≤ 5; Grothendieck-type dual.
- **CA_H_002 Thm 3.1/3.2.** Div = ∫g_s dHaar, Div + Near = ∫g_s dν₀ on Ĝ; anatomy Σ_q[α(log q)N_s(q) − c₀(log q)M_s(q)].
- **CA_M_001 Prop 4.1.** m(τ) + 2Re(ζ′/ζ)(½+iτ) = 0 away from ordinates (FE only); C₀ = −2ζ′/ζ(½).
- **CA_R3_001 Prop Θ / CA_R4_001 Prop R4.1–R4.2.** In the Schur step, the density part and the polar part vanish
  exactly on P_{T_j}; (Ch) + positions ≡ data at each contact.
- **CA_R2_002 (1.1).** 𝔰_j(e_min) ≤ λ_A(T_{j+1}) ≤ 4·10⁹T_{j+1}n_{j+1}^{−7.7245}.

Proved coordinates and obstructions (useful for filtering): CA_A_001 Lemma 2; CA_A_003 §2; CA_A_005 Prop 2; CA_A_006 Thm 2;
CA_A_007 Lemma 1, Thm 2; CA_A_008 Lemma 1; CA_B_003 Thm 1; CA_B_004 Prop 1 and (3.1); CA_B_007 Prop 1(a); CA_B_008 Thm 1;
CA_C_001 Lemmas 2–4, Thm 1; CA_C_002 Props 1–2; CA_F_001 Prop 3; CA_F_002 Lemma 1; CA_F_003 Prop 2; G0, G1; CA_H_001 Props
1.1–5.3; CA_H_002 Thm 2.2; CA_I_001 Thm 2, Lemma 4, Prop 5; CA_J_000 J0/J0′; CA_J_001 Thm 2, Prop 5; CA_J_002 Thm 1.3, Prop
2.1; CA_K_001 Thm 2.1–2.2, Prop 1.3, Prop 3.2, Lemma 4.1, Thm 4.2; CA_K_002 Thm 1.2, Prop 2.1; CA_L_001 Thm 1.1; CA_M_001 §1.2,
Prop 3.3; CA_N_001 Lemma 1.1, Prop 2.1; CA_N_003 Thms 3–4; CA_R1_001 Thms 2.1–2.3, Prop 1.3; CA_R2_001 §1, Prop 3.1.

---

## 5. Coverage

- Files in the folder: **128** `.md`.
- Read in full: **128** (all memos CA_*_001 onwards, their reviews, the seed tables CA_*_000 and batches
  CA_C_004/006, syntheses, CA_SYNTHESES_REVIEW, CAMPAIGN_LEDGER, CA_A_000_INDEX, README).
- Not read: none. No illegible file.
- Nothing outside the folder was read except ANNEX_PHASE_193_LABELS.md; the references of the memos to P47 and to the routes
  index were taken as cited by the memos and their reviews, without verifying them against P47.
