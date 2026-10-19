# TRACT_E_PHASES_001 — Phase 204, part E: tractability of all REF-D reformulations from phases 100–189 and from `06_`

Index entries written
in another language are rewritten D-only (window form 𝔞_T on P_T, λ_A(T), zeros only as the side of the window's
explicit formula, thm:Z).
This memo **classifies; it proves nothing new**. Only file written: this one.

**Sources.** `TRACT_001.md` (method, criterion, R1–R13: not repeated, their verdict is cited); Paper 47 `sec:spec`
(thm:noimport, lem:spec-collapse, thm:spec-noatom); `MAP_200_001` §2 (Φ200, M200′, R-F2, R-I3, C-pol, HA/HB);
`ROUTES-TRIED-INDEX/04_PHASES_100-189.md` (239 lines with «REF-D»); `06_OPEN_RESIDUES_DEAD_SUBROUTES.md` (11);
targeted audit of R169_101 (Eratosthenes), R157_002 #27 (GAP-157.A), P121_VOLterra.

## Summary (≤300 words)

The 239 «REF-D» lines in `04_` (237 real entries; 2 are headers) and the 11 in `06_` are grouped into **39
distinct reformulations** (K1–K38 plus K7b; table §2). TRAT classification: **4 YES** (two already in TRACT_001: (L2)
S_{T,k} and polar capacity g_±; two new: (Ω_{t₀})/t_∞>0 and Lemma 108, the latter with no input), **14 TRANSFER** (the
applicable general theory consumes the positivity of the window data), **21 NO** (class theorem or explicit falsifier).
Dismissed only by judgment: **11 of 39**; of those, 8 were correct transfers, 3 had their own path.

Main finding, **corrects TRACT_001 §5**: barriers from the corpus on continuation-in-T arguments do exist:
R169_101 Cor 2′ (PROVED given thm:M(b)): every *perturbative* step T→T+Δ requires an exact cancellation to doubly
exponential precision (W2); L2_003 (scalar transfer of a step: 2×2 falsifier); L2_016 (induction by doubling). Hence
R13 and R6 remain TRAT = YES **only in non-perturbative form** (exact rigidity at the crossing), and the first lemma
must declare why it is not an estimation step.

Better-positioned new candidate: **(Ω_{t₀}), t_∞ > 0** (`06_` R3): strictly weaker than D and, by construction, its
margin is O(1−t), not doubly exponential; it escapes W2. Its only registered blockage is a CONDITIONAL collapse to
(E_γ) (N_013). First lemma: audit that collapse for t<1.

Stronger than D with their own path: none except L′♯ (via the Fredholm→R13 bridge, already in TRACT_001). The 89 «NOT
closed» rows are 86 plain rows + 3 of the form «REF-D (NOT closed; …)»: routes whose only killer was REF-D; they fall
into 24 of the 39 reformulations and none is a new TRAT = YES beyond those already listed.

Row D: OPEN. L′♯: OPEN.

---

## 0. Inventory and reading of the 89 «NOT closed»

| source | lines with «REF-D» | entries | note |
|---|---|---|---|
| `04_` Part I (curated) | l.12–202 | 12 | W1, W11′, thm:Z, KEP, ρ*, R186, L2_005/024, N_012, P154 |
| `04_` Part II (auto-extracted) | l.242–1058 | 225 | 2 headers excluded (l.4, l.231) |
| `06_` | l.4, 47, 48, 73, 181, 192, 202, 204, 212, 218–219 | 10 (+header) | open residues R1–R10 and the «never built» list |

Outcome labels of the 225 Part II rows carrying REF-D (grep-verified):
- **86** «REF-D (reformulation of D; NOT closed, see header)» — sole killer REF-D.
- **3** «REF-D (NOT closed; …)» (l.884, 888, 914) — sole killer REF-D with an attached theorem.
- **45** «REF-D;X (reformulation of D; NOT closed)» — REF-D plus another label (F3, F4, W8, T1, OTHER…).
- **39** «DEAD [… REF-D …]» — dead by another killer (F1–F4, M, W#), REF-D secondary.
- rest: PARTIAL / OPEN-RESIDUE / NO-GO with REF-D in the text.

**The 89.** 86 + 3 = 89 matches the README correction (l.108–112): these were automatic rows
labeled «DEAD [REF-D]» whose *sole* killer was REF-D; that contradicted the index's own header (REF-D is not
closure, a methodological order), and they were relabeled «NOT closed». **What they are:** routes that end in a
statement exactly equivalent to D in T (or to ∀T) with no impossibility theorem or falsifier. Their distribution in
table §2: Herglotz/de Branges (K1: 8), Kreĭn (K2: 4), Li/finite order (K3: 3), Douglas/global square (K4: 6), A_T/Schur
(K5: 4), geometric objects/MW-5 (K6: 22), certificates/Problem B (K7: 6), uniformity in T (K8: 8), Sonin (K9: 3),
polar/boundary triple (K11: 1), witnesses (K17: 3), spectral/Hilbert–Pólya (K16: 3), estimates (K14: 4), Euler/
ℚ-indep. (K19: 2), commutators/identities (K22: 3), rest (9) in K21, K24, K31, K33, K36, K38. **Verdict in §5.**

---

## 1. Criterion (inherited from TRACT_001, unchanged)

TRAT = **YES** if there exists a class of general theorems 𝒯 whose domain contains the reformulation and whose
remaining hypothesis is verifiable using information distinct from the sign being sought. **TRANSFER** if the
remaining hypothesis is, rewritten, the positivity of the window data (the general theory consumes it). **NO** if a
class theorem or explicit falsifier closes it. «Judgment» = dismissal without theorem or falsifier.

Filter barriers I use (all PROVED unless noted): lem:shape-est / lem:shape-ident (P47 thm:shape); thm:noimport
(P47 sec:spec, (i)–(iii) PROVED, (iv) ARGUED); lem:spec-collapse; Φ.1 (branch 2 of Φ200); W-lin, W-det, W-fam
(two-sided not excluded), W-pat, W-loc, W-mom; W2/thm:margin (λ_A ≤ exp(−e^{(2−ε)T})); cor:void; T1, T2; W8 (finZ);
W10; W12; **R169_101 Cor 2′** (new in this memo as a continuation filter).

---

## 2. Table of distinct reformulations (39 = K1–K38 + K7b)

Conventions: «=D_T» = equivalent to D in window T; «=D» = equivalent to ∀T; «>D» stronger; «<D» weaker.
Lines are from `04_` unless prefixed «06:». Bold R# refers back to TRACT_001.

| K | reformulation (D-only) | lines | phases | direction proved | strength | TRAT | original dismissal |
|---|---|---|---|---|---|---|---|
| K1 | Herglotz / positive boundary measure / de Branges canonical system in window time: the Weyl function of the window formula is Nevanlinna | 12, 242, 253, 410, 422, 424, 457, 458, 467, 639, 860 | 102, 115, 159, 162, R160 | ⟺ (classical, Lagarias/Herglotz; T*(0)=∞ = thm:KEP3(b)) | =D | TRANSFER (Nevanlinna/de Branges consume positivity; «dλ/dT not usable») | correct judgment; 860 Thm G additionally F1, F3 |
| K2 | Kreĭn indeterminacy of g_T (= **R3**) and determined nodal measure | 58, 393, 598, 622, 864, 1030, 1035 | 153, 155, 162, 184 | R3 ⇒ D PROVED; ⇐ OPEN | >D | TRANSFER (**R3**) | correct judgment |
| K3 | Li/Keiper positivity / Ω₇ / A1 Laguerre / finite order → full order (Hankel, PF, Jensen) | 12, 252, 263, 265, 379, 456, 474, 504, 626, 650 | 102–105, 155, R160 | each finite order PROVED unconditionally; uniformity = D; Li kernel outside 𝒲_T (cor:Li) | =D (full line, not window) | TRANSFER (Jensen/GORZ CITED gives fixed order, not uniformity; uniformity is the square-root bound on Σe^{ρu}/ρ²) | judgment + W8 |
| K4 | Douglas factorization / contraction Y=ΘX / global square K*QK−Q ⪰ 0 / Wiener–Hopf 𝒯=A*A / Sz.-Nagy dilation / Brodskii–Livšic / almost-nilpotent causal Volterra / equation (KZ) | 290, 303, 316, 339, 425, 443, 564, 771, 914, 924, 1033 | 114, 120–121, 136, 159, 164, R160 | ⟺ (Douglas; P121 classification PROVED; KZ = (1.1) term by term) | =D or >D (Sz.-Nagy ⇒ simplicity, overstated) | TRANSFER; Volterra: the rank-one perturbation does not inherit the almost-nilpotency of the standard Volterra operator, requires zero-free rigidity (P121 l.267–276); 924 NO (symbol σ_T(0)<0 PROVED) | locality–phase–sign trilemma; 924 W4/W6 |
| K5 | A_T ≥ 0 / A_T atlas / Schur complement Σ(T)=B−X*L⁻¹X / codim-2 compression / P_loc(γ,T) cells / A_⊥⊥(1) | 298, 314, 331, 617, 872, 901, 1008 | 118, 121, 124, 162, 163, 183 | ⟺ PROVED (Thm 1 R163_601; 872) | =D_T | TRANSFER (= **R4** block; Szegő consumes symbol ≥0) | judgment; 1008 «an aligned direction for all T does not exist» (§7 R183_030, PROVED) |
| K6 | Carrier geometric object: Hodge index on D/rad, h⁰ (RR⁺, bigraded, 2-homogeneous), cone B4 and (P_m), bigness, MW-5/OT-5′, adèle class space, Meyer H¹, foliated Deninger, Lefschetz/Kähler, Sh_Z, Witt W(ℝ), Forni/EKZ, KK, e-invariant, numerical motive M_Z, Fargues–Fontaine, scaling site, Huh/Doc 125, Ansatz A χ(D)=D²/2, Laumon ε | 12, 284, 285, 338, 350, 352, 353, 356, 357, 358, 404, 406, 426, 435, 439, 463, 492, 497, 567, 581, 607, 611, 644, 646, 648, 665, 696, 703–706, 708, 709, 715–717, 721, 723, 730, 733, 734, 787, 986, 1031, 1050, 1057, 1058; 06:218 | 113, 135, 140–145, 157–160, 173, 184, P46 | conditional on existence; «every carrier postulates positivity» | existential / >D | NO (W10 PROVED: frame defect also over 𝔽_q; HA/HB; R173 three families NO-GO; T5) — **R5**; alive only as *construction* (§28.4), not as reformulation | class theorem |
| K7 | Flat-top certificate = explicit formula (thm:Z), P6 alignment band, decidable finite condition v_T ∈ V_T, exterior certificates, ν̂ ≥ 0 on the cone (= **R7**) | 12, 57, 202, 378, 388, 586, 587, 1054; 06:48 | 154–155, R160 | ⟺ PROVED | =D_T | TRANSFER (**R7**; cone duality) | correct judgment; finZ NO-GO for finite Z |
| K7b | Problem B: flat-top w_T built using only primes outside the window | 389, 588, 604, 649; 06:192 | 155, 159, R160 | ⇒ D | >D (constructive) | NO (M1/R160: Thms L, Σ kill both candidates) | theorem |
| K8 | Uniformity in T: ∀T λ^W ≥ 0; gradual law λ_T ≥ −Ce^{κT}; bootstrap/renormalization in T; almost-periodicity in T; Cesàro/L¹ in λ; residue window ∀T (Thm R); Conj 6.1 asymptotics; semilocal sufficiency ∀q | 12, 401, 412, 423, 431, 638, 636, 641, 682, 784, 785, 857, 858, 976, 1009 | 157, 159, 162, 170, 183, R160 | κ=0 ⟺ D; κ>0: gradual converse PROVED (forces a zero-free band of width O(κ)) | κ>0: <D | TRANSFER (the missing hypothesis for κ<κ_triv is a new zero-free band, a classical open problem, no easier); W-fam rules out functionals on bounded range | judgment + M (412) |
| K9 | Sonin: Sonin rank (S_m) ⟺ HF=0, ρ*(T)<1, (L-Son), ESB/multi-prime leak, frequency multiplier, prolate gap, polynomial collapse | 12, 29, 125, 739, 779, 807, 808, 866, 1001, 1003, 1007, 1013, 1029 | 161–162, 183–186 | ⟺ PROVED (ρ*<1; all-or-nothing Müntz) | =D_T; uniform (L-Son) >D | NO: 1007 FALSE (low-band falsifier), 1003 W-Sonin, 1013/1029 W11′; rest TRANSFER | theorems |
| K10 | (L2) finite Schur matrix S_{T,k} ⪰ 0; index n₋, scalar criterion, Γ-moments at first contact, (L2-H), Theorem S B_{F₀}(d) ⪰ 0, Sonin count N(T) | 130, 132, 147, 155, 169, 873; 06:181 | 186, L2_*, P47 | ⟺ PROVED (R186_025/105; thm:oneprofile mod Lemma I) | =D_T | **YES, restricted** (= **R13**; see §3.1: only non-perturbative by R169_101 Cor 2′ and L2_003) | partial judgment (walls W-*) |
| K11 | 2×2 polar capacity g_±(T) / boundary triple of the minimal operator / Robin strings / Loewner continuity | 782, 781, 1014; 06:212 | 156, 162, 184, 199 | ⟺ given RD_T | =D_T | **YES, restricted** (= **R6**; §3.1) | judgment («comb models»); 781 DEAD [F3] by isotropy=Gate 1 |
| K12 | (Ω_{t₀}): fixed fraction t_∞>0 in λ_t=(1−t)ρ_κ+tΛ, κ>κ* | 178; 06:73 | N_011–014 | t_∞=1 ⟺ D; t_∞>0 strictly weaker (PROVED) | <D | **YES (new, conditional)** — §3.2 | judgment («not separable», ARGUED) + CONDITIONAL collapse |
| K13 | Exact chains: determinant/heat trace/Kreĭn shift of A_T in T; spectral flow; secular anchor/RDI/Kato–Euler; Euler–Maclaurin/Fredholm rank; covariant vanishing; self-adjoint determinant = Euler factor | 549, 553, 554, 664, 913, 974, 977 | 110, 164, 170, R160 | identities PROVED, sign-free | =D or empty | NO (W12, W5, W-det PROVED) | theorem |
| K14 | Prime-side estimates: RFB/Carleson magnitudes, per-window entries, sieve→index, pairs/GUE, FI/HB bilinear, frequency-local Tauberian, power saving, local Selberg/Levinson–Conrey, inequality over Λ excluding the witness, (WS*) via sieve | 498, 511, 515, 516, 517, 522, 524, 538, 877, 936, 955; 06:202 | 36, 46, 49, 108, 157, 163, 166, 167, R160 | ⟺ or necessary | =D or <D | NO (lem:shape-est, W-sieve, W4, R166_802 circularity PROVED on simple tests); GAP-157.A non-local: NO by cor:void/F1 (R157_002 #27) | theorem |
| K15 | Transport from function fields (q→1, g→∞, Bombieri–Stepanov, Bochner cone) | 432, 688 | 145, 159 | cone admissibility = D | =D | NO (W8, F3:function-field) | theorem |
| K16 | Spectral realization: Stone unitary evolution, real involution j, K-theory [P₋]=κ, quasicrystal, Hilbert–Pólya E_(∞,T) | 451, 462, 700, 786, 958, 965 | 17, 28, 53, 162, 168 | unitarizing inner product = Weil form | =D | NO (W-identification: the class collapses to {ζ}; Thm 1.1–2.3 R168 PROVED); 462 transfer (symmetry, not positivity) | theorem |
| K17 | First-contact witness: rigid Blaschke, Gauss nodes, nodal measure, parity coupling, 1/δ² singularity, sine–cosine, Lyapunov, quartet detection (H), second moment, zero-side sinc | 447, 657, 844, 863, 908, 921, 945, 947, 948, 950, 952, 1027, 1028 | 121, 124, 162, 163, 164, 166, 184 | ⟺ or empty | =D_T | NO (W5 jets, W-jet Thm 1.3 PROVED, F3) | theorem |
| K18 | Monotone functionals / flows: minimization at b_j=0, Doob Poincaré CD(0,∞), arithmetic monotone functional, dBN heat, probabilistic ladders, monotone laws | 430, 448, 482, 483, 635, 679, 798, 799 | 9, 28, 70, 159, 162, Paper 41 | ⟺ or local maxima | =D | NO (CD(0,∞) flat: no gap, curvature bound ¼; monotone laws hold for DH/finmod; «local max at b=0») | theorem/falsifier |
| K19 | Algebraic Euler structure: ℚ-independence of log p as transversality, prime incoherence, determinant/Contou-Carrère lines, cocycle Φ_Λ, separability, ring data/Λ*1=log | 325, 527, 559, 589, 822, 839 | 122, 158, 162, Paper 12 | coordinate transfer | =D | NO (W7 PROVED; C-MvN; cocycle splits prime by prime) | theorem |
| K20 | Integrality / identification: integer jump in deformation f_t→ζ, window Hamburger, Euler gate, Γ–Euler detector, quantitative Hamburger, generalized integer measure, O(1) collocation | 815, 818, 820, 884, 888, 896, 898, 1019 | 162–163, 184 | ⟺ or empty (Thm C.1) | =D | NO (W3′ Thm O, W-identification, Lemma U) | theorem |
| K21 | Local Laguerre L₁=Ξ′²−ΞΞ″ and (★_cell) small-y; degree-2 L_γ = ζ(s+iγ)ζ(s−iγ) | 959, 961 | 168 | equivalence with (★_cell) FALSE (PROVED); degree 2 ⟸ D (REF-D) | ≠ / <D | NO as a route (the equivalence fails; degree 2 is deduced from D, not the reverse) | theorem |
| K22 | Divisor-singular commutators, canonical conjugate test, four-block Green identity, OAL at poles Γ, (B4.1), channels 4(Re D)², pole at −2m, weak renormalization | 328, 744, 745, 748, 780, 825, 826, 831 | 122, 161, 162 | identities PROVED | =D | NO (W6, F1; Thm N limit ≡0) | theorem |
| K23 | Coupled polar/Frobenius positivity (meta-136), band crossing via Vitali signature continuity | 341, 344, 455 | 136, 137 | meta PROVED; Vitali refuted (D.0) | =D | NO (W11; D.0 refutation) | theorem |
| K24 | SOS/Positivstellensatz (positive-definite free part), Hermitian squares | 408; 06:47 | 159, N_019 | covariant SOS = zero-side SOS | =D | NO for T ≥ ½log3 (thm:sos), REF-D class (D) | theorem |
| K25 | Amplification by tensor power / bivariate index W₂ | 686, 806, 814 | 44–45, 107–108, 162 | sig(W⊗W) = (p²+n², 2pn) PROVED | =D | NO (dilution σ₀=0; W2) | theorem |
| K26 | Lemma 108: κ_W(Q₂) ≤ C·n_W | 661; 06:204 | 108, R160 | — (explicitly not REF-D) | <D (index bound) | **YES (linear algebra), null input** — §3.3 | never attacked; route dead via the sieve→index bridge |
| K27 | Pointwise combs and signed squares: archimedean envelope ≥ comb, per-place OS, sawtooth B₂, Dirichlet²×Λ=μ*log, Thm P lock | 469, 526, 788, 823, 946 | 6, 162, 166 | — | =D | NO (W4 wrong sign; indefinite G_p PROVED) | theorem |
| K28 | Theorem A (phase 153) at large T / self-scale / 153.M′ rigidity | 558, 612, 624 | 153, R160 | Prop 5: the inference fails | =D | TRANSFER (odd box = D) | judgment + inference failure |
| K29 | Angular operator bound from the zero side | 613 | Paper 08 | — | =D | NO (sign-free bounds give ‖K‖² ≳ e^{…}, PROVED) | theorem |
| K30 | Law Ψ1 on the family 𝔈 (uniform over fields) / multigenerator (Q*) | 969, 1026 | 169, 184 | (Q*) false on Type I PROVED | >D (uniform over L-functions) | NO (T1: should hold for ζ_K/Hecke; Thm 3.3 R184_011) | theorem |
| K31 | Split R-C.a given R-C.b | 868 | 162 | D ⟸ R-C.a ∧ R-C.b; R-C.a = D given R-C.b | =D | TRANSFER | judgment |
| K32 | Strong recurrence (Bagchi) / LP-112 | 454 | 35, 102 | recorded as REF-D (the original equivalence is not written D-only; unaudited) | =D (unverified D-only) | TRANSFER (Voronin universality consumes the data; LP-112 open) | judgment |
| K33 | Deficit measure / incidence invariant C_∞(γ_n)=0 | 629 | 29 | ⟺ zero location (MW-7 Hadamard barrier) | =D | NO (MW-7) | theorem |
| K34 | (N)/(N_loc): correlation inequality Σv_n Re c_F(log n) ≤ 𝔞_∞(F) | 06:27–60 (via 156) | L2_006, N_* | (L2) ⟺ (N_loc) PROVED | =D_T | TRANSFER (admissible directions (a),(b) = signed cancellation at scale e^{2T}; 18 NO-GO sub-routes) | theorems |
| K35 | (Ω₀): clamped bending-mode test h_T: Σ2Λ(n)n^{−½}h_T(log n) < 0 ∀T>½log5 | 157; 06:62 | L2_007–009, 190 | necessary for (L2), not sufficient (PROVED) | <D | YES only on a finite range of T (enclosure with verified zeros, NUMERICAL as mechanism); ∀T TRANSFER | judgment («weak filter», phase 190) |
| K36 | (Ω_Φ): Poisson–Euler fixed-point residue r(λ)=λ−Φ(λ) controls negativity | 06:86 | N_009–010 | linearized in Λ tautological PROVED | >D | NO (= **R8**: Φ.1 branch 2) | theorem |
| K37 | (E_γ): Chebyshev twisted at one frequency, critical at each γ | 06:94 | R186_050, N_013 | D ⇒ (E_γ) PROVED | <D | TRANSFER (criticality: the packet limit is exactly m♯(γ); the second-order sign is missing) | theorem (criticality) |
| K38 | Lower half of the two-sided law λ_A ≥ L(T)(1−o(1)); also λ_A ≥ −ε(T), ε→0 (⟹ D by thm:wit-Tc(iv)) | 06:103 | R186_039 | λ_A ≥ −o(1) ⟹ D PROVED | >D (with L) / =D (with −o(1)) | TRANSFER (W-fam excludes the limit alone; Landau–Widom predicts β_max>1, NO-GO; the missing hypothesis is the lower half itself) | partial theorem |

In addition, two `06_` items without their own REF-D that the index cross-references with these rows: R7 (O166.802.1,
nonlinear multiscale inequalities over Λ: OPEN, ARGUED in general; not a reformulation but a class of methods) and R9
Problem (S) (Arch_M − Div_M − Near_M ⪰ 0 ∀M, ⟺ D by prop:AM + thm:oneprofile). I classify R9 as **TRANSFER**: it is a
finite matrix for each M, but the missing hypothesis (joint control of Near at resolution e^{2T}) is the sign; 10
NO-GO sub-routes. R10 (NT gate at σ=1) is not REF-D: it is a search for input, outside scope.

Coverage count: the 237 entries of `04_` and the 10 of `06_` are assigned to K1–K38/K7b (some entries, e.g.
l.12 W1, appear under several K's because they group several reformulations; l.335 «the framed goal of Papers 43–45»
and l.402 «61 mechanisms with no survivor» are umbrellas with no reformulation of their own and are not counted as K).

---

## 3. The TRAT = YES entries

### 3.1 K10 (= R13, (L2)) and K11 (= R6, polar capacity): correction to TRACT_001

TRACT_001 §5 states: «none of the corpus barriers (thm:shape, Φ200, C-pos, W-*) is a theorem about continuation
arguments in T». **That is incorrect**; the index records three:

1. **R169_101, Cor 2′ (PROVED, given thm:M(b) from the record).** In the Schur form of the step W_{T′} = [[W_T, C],[C*, D]]
   (Thm 2, PROVED), the necessary condition (N) |C(F_T,G)|² ≤ λ_T D(G) forces, for T ≥ T₀(ε),
   |C(F_T,G)| ≤ exp(−½e^{(2−ε)T}) D(G)^{½}. No step that estimates the activated term 𝒩 with error ≥ exp(−e^{(2−ε)T})
   (Legendre, Brun, Selberg, BV, Type I/II) proves the step. Row 967: NO-GO [W2; single object].
2. **L2_003** (06 R1): scalar transfer of a step Φ: NO-GO by a 2×2 falsifier.
3. **L2_016** (06 R1): induction by Frobenius doubling in T: NO-GO (Tate does not transport). And l.412/431:
   bootstrap in T DEAD [M].

Consequence for the lemmas of TRACT_001 §6:
- **T13.2 (jump k→k+1 via rank-one border)** is the Schur form of R169_101 restricted to one contact. If proved by
  estimating the scalar complement, it falls into Cor 2′. It remains **open only as an exact statement**: the
  scalar complement must vanish/become positive via an identity using the structure of Λ at the new contact
  (not a bound). CA_R4_001 (near-cancellation of four copies at 1.6·10⁻⁶) is precisely the symptom of Cor 2′.
- **T13.1 / T6.2 (no-crossing between contacts)**: this is not an estimation step but a rigidity claim: «at a
  crossing T*, the extremal would satisfy an overdetermined boundary-value problem». Cor 2′ does not exclude it *if*
  the contradiction is exact (qualitative). W-fam (P47 thm:famblind) excludes functionals of {λ_A(T′)} on bounded
  range — a no-crossing argument that only uses the function T ↦ det S_{T,k} falls there; it must use the
  *eigenvector* at T*, not just the value.
- **Additional filter** (thm:noimport (i)): no-crossing must fail for F_DH at T ≥ 9/5 and for Epstein at T ≥ 1.59.

**Revised TRAT:** K10 and K11 remain YES, **restricted to exact, non-perturbative rigidity arguments**. First lemma
(reformulated): *Lemma E.1 (crossing rigidity).* If λ_A(T*) = 0 with T* between contacts, the eigenvector F* satisfies
(a) the Euler–Lagrange equation of 𝔞_{T*} on P_{T*} and (b) the Hadamard boundary condition ∂_T𝔞_T(F*)|_{T*} = 0
(zero boundary trace at ±T*); prove that (a)∧(b) forces F* ∈ 𝒢̄_{T*} using the contact block Λ(n_j)δ (Prop Θ).
Input toward D if it goes through: sign monotonicity of λ_A between contacts, reducing D to the contact instants
(the discrete set {½log n}). Risk: that (b) is automatic from the core's structure (then the rigidity is empty); it
is falsifiable on the first interval (½log5, ½log7) with the extremal already computed.

### 3.2 K12: (Ω_{t₀}), t_∞ > 0 — new candidate

(a) **D-only statement.** For κ > κ* ≈ 1.343 (Pos convex and ρ_κ ∈ Pos ⟺ κ ≥ κ*, N_011 PROVED), let
t*(T) = sup{t ∈ [0,1] : the window form of the comb λ_t = (1−t)ρ_κ + tΛ is ⪰ 0 on P_T}. (Ω_{t₀}): t_∞ := liminf_T t*(T) > 0.
(b) t_∞ = 1 ⟺ D (PROVED); t_∞ > 0 strictly weaker (PROVED, 06 R3).
(c) **Why it is structurally distinct.** For t < 1 the comb λ_t carries a term (1−t)ρ_κ with κ > κ* contributing a
positive margin of order (1−t)·(κ−κ*)·G_κ. The form's margin stops being doubly exponential: **W2/thm:margin does
not apply**, nor does Cor 2′ (which uses λ_T ≤ exp(−e^{2T})). It is the only reformulation in the inventory that
escapes W2 by construction without being trivial.
(d) **General theorem and missing hypothesis.** Convexity of Pos (PROVED) + relative form criterion: λ_t ∈ Pos ∀T ⟸
‖fluctuation form of Λ‖ ≤ C·G_κ uniformly (sup_{T,F}(𝓕_T − 𝔞♯)₊/G_κ < ∞). It is an **O**-type bound relative
to the deficit symbol (κ*−1)/(¼+τ²), not a sign bound. Applicable theorems: KLMN/relatively bounded forms; but
N_008 (prop:relative) closes «KLMN relative order» for (N) — **for the full comb Λ**, not for the form relative
to G_κ.
(e) **Registered blockage.** N_013: concentrating packets collapse (E_γ,C) to (E_γ) (CONDITIONAL); N_014:
translation/modulation families «not separable from D» (ARGUED); N_012: the decomposition does not give t₀ (NO-GO,
only for that technique). **None is a theorem about (Ω_{t₀}) itself.** N_013's collapse is the decisive piece: if in
the packet at γ the contribution of ρ_κ is strictly larger than m♯(γ) (κ>κ*), the collapse for t<1 should leave slack
(1−t)·δ(γ), which would contradict criticality. This must be audited.
(f) **First lemma.** *Lemma E.2 (packet with fraction).* For κ>κ*, t<1, and concentrating packets F_T at γ:
limsup_T 𝔞^{λ_t}_T(F_T)/‖F_T‖² ≥ (1−t)·c(κ,γ) > 0. If PROVED, N_013's collapse does not apply for t<1 and (Ω_{t₀})
has no registered blockage; if false, (Ω_{t₀}) collapses to (E_γ) and becomes TRANSFER.
**Input toward D:** (Ω_{t₀}) would give an independent theorem — window positivity for every T of the damped comb
λ_{t₀} — and would turn D into an *interpolation* problem t₀ → 1 inside the convex set Pos, with a nondegenerate
margin at t₀. It does not close D; it changes the nature of the margin.
(g) Risk: the uniform bound might require exactly the signed cancellation of (N) (06 R1 (b)); in that case the gain
is null. Filter thm:noimport: (Ω_{t₀}) is affine in the comb → (iii) bounds its margin in Λ by λ_A — **but the
relevant margin is in λ_{t₀}, not Λ**; (iii) does not restrict it.

### 3.3 K26: Lemma 108 — YES, null input

κ_W(Q₂) ≤ C·n_W is a bound on the negative index of the bivariate form in terms of the univariate one; with
sig(W⊗W) = (p²+n², 2pn) (l.814, PROVED) it is linear algebra of inertia (Sylvester). Likely PROVED in a few lines for
finite n_W; **input toward D: none** (the sieve→index route that used it is dead, doc 108; 06 l.204: «sup κ_W
rewrites the target at k=2»). I note it only so the index stops listing it as «never attacked».

### 3.4 K35: (Ω₀) — YES on a finite range, not ∀T

h_T has ĥ_T ≥ 0 on ℝ; by the window's explicit formula, (Ω₀) at T reduces to a sum over zeros weighted by
ĥ_T(γ) with a tail controllable by the decay of ĥ_T and verified zeros; this gives (Ω₀) rigorously on any bounded
range of T (phase 190: margin 0.016–0.091 on [0.55,1.10], NUMERICAL). It is the same technology as the ½log15
boundary (Mori); **not a new path of its own**, and ∀T it is TRANSFER. Input toward D: only a necessary filter
(weak, amp2 and ±10⁻² pass it).

---

## 4. Stronger than D with their own path

Candidates >D in the inventory: K2 (Kreĭn), K4 (Sz.-Nagy ⇒ simplicity), K6 (objects), K7b (Problem B), K9 (uniform
(L-Son)), K30 (uniform over L-functions), K36 (Ω_Φ), K38 (with L(T)), l.502 (height-uniform modulus), L′♯ (R2).
- **With their own path: none new.** K7b, K9-uniform, K30, K36 are closed by theorem or falsifier; l.502 requires
  vertical repulsion (false in the GUE model: >D and probably false); K2/K4/K38 are transfers; K6 is construction.
- Only **L′♯** (R2) retains a path: Fredholm + finite space → K10. See §3.1 for the non-perturbative restriction.

## 5. Tractability ranking (part E, integrated with TRACT_001)

1. **K12 (Ω_{t₀})** — weaker than D, escapes W2 by construction; blockage only CONDITIONAL; Lemma E.2 decides quickly.
2. **K10/R13 (L2)** — finite, but restricted to exact rigidity (Cor 2′, L2_003); Lemma E.1.
3. **K11/R6 polar capacity** — two scalars; same restriction; probably the same object as K10 (check whether 𝔊_T is
   a block of S_{T,k}).
4. R10 Lemma F (TRACT_001; outside this inventory, phases 200–201).
5. K35 (Ω₀) on a finite range (known technique).
6. K26 Lemma 108 (trivial, no input).
7. Transfers with richer general theory: K37 (E_γ), K34 (N_loc), R9 (S), K38, K8 κ>0.
8. Rest of the transfers (K1, K2, K3, K4, K5, K7, K28, K31, K32).
9. NO (15): K6, K7b, K9 (partial), K13–K25, K27, K29, K30, K33, K36.

## 6. Honest count

| class | n | which |
|---|---|---|
| distinct reformulations | **39** | K1–K38 + K7b (06's R9 Problem (S) counted inside the transfers as a note) |
| TRAT = YES | 4 | K10, K11 (restricted to exact rigidity), K12 (conditional on Lemma E.2), K26 (null input) |
| TRANSFER | 14 | K1, K2, K3, K4, K5, K7, K8, K28, K31, K32, K34, K35 (∀T; YES only on bounded T), K37, K38 |
| NO (theorem or falsifier) | 21 | K6, K7b, K9, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K27, K29, K30, K33, K36 |
| dismissed only by judgment | **11** | K1, K2, K5, K7, K8, K10, K11, K12, K28, K31, K32 |
| … of those with their own path | 3 | K10, K11, K12 (K26 was not dismissed by judgment: it was never attacked) |

Mixed sub-parts: K4 (Volterra transfer; symbol l.924 NO), K9 (mostly NO; ρ* transfer), K14 (GAP-157.A NO by
cor:void), K16 (l.462 transfer). Classified by their dominant part.

Reading: of the 237 «REF-D» entries in `04_`, ≈ 60% fall into reformulations closed by theorem (the REF-D was
secondary or a verbal shortcut), ≈ 35% into transfers, and ≈ 5% (≈ 12 entries: l.130, 132, 147, 155, 169, 178, 661,
781, 782, 873, 1014, and 06:181/212/73) into the four with their own path.

## 7. The 89 «NOT closed»: verdict

- **What they are.** Part II rows whose sole killer was REF-D; «DEAD [REF-D]» → «NOT closed» was corrected because
  it contradicted the header. They are reformulations alive *as targets*, not dead routes.
- **Where they fall.** 22 in K6 (geometric objects: alive only as construction, the reformulation is NO by W10), 8 in
  K1, 8 in K8, 6 in K4, 6 in K7/K7b, 4 in K2, 4 in K5, 3 in K3, 3 in K9, 3 in K16, 3 in K17, 4 in K14, 3 in K22, 2 in
  K19, 1 in K11 (l.782, boundary triple), and 9 scattered (K21, K24, K28, K31, K32, K33, l.335, l.402).
- **Is any TRAT = YES?** Only **l.782** (boundary triple of the prolate W_λ, deficiency (2,2) → K11) and, indirectly,
  l.1008 (an aligned direction; its §7 proves it does not exist, PROVED → NO). None of the 89 contributes an own path
  not already in K10–K12. The relabeling was correct as a label (they are not closures), but it does **not** hide
  tractable routes: in ≈ 80 of the 89 the general theory they lead to consumes the positivity (transfer) or a later
  class theorem (W10, W-identification, W-jet, W12) covers them even if the row does not cite it.
- **Recommendation for the index:** add a TRAT column with this memo's K code to those 89 rows; for the ≈ 30 covered
  by a later theorem, cite it (e.g. K6 → W10; K16 → W-identification; K17 → W-jet).

## 8. Proposed index entry (for the coordinator)

«Phase 204 part E (TRACT_E_PHASES_001): the 237 REF-D entries from 04_ and 10 from 06_ reduce to 39 reformulations.
TRAT: 4 YES (L2 and polar capacity, restricted to exact rigidity by R169_101 Cor 2′/L2_003; (Ω_{t₀}) t_∞>0 —escapes
W2, blockage only CONDITIONAL N_013, Lemma E.2—; Lemma 108 with no input), 14 transfers, 21 NO. 11 dismissed by
judgment. The 89 «NOT closed» rows contain no new tractable routes. Corrects TRACT_001 §5: continuation-in-T
barriers do exist (R169_101 Cor 2′, L2_003, L2_016). No new NO-GO. Row D: OPEN.»
