# Annex: file-by-file reading of phase 161, part 3 (R161_056 to R161_099)

Complete reading of the files R161_056 … R161_081 and R161_099 of
`03-research/phase-161-row-d-sum-product-square/`. There are no files R161_082 … R161_098. What each
memo builds and claims is recorded; nothing is proposed. Notation of the memos: Z_N = S_N^ren (integer synthesis minus
continuum), Fcal the additive Fourier involution in log scale, J the reflection, X multiplication by t,
P = P_T the physical compression to (−T, T), Q = I − P, Pi = Pi_T the primitive projection, Tau (or R) = P − Pi the
two-dimensional Tate block, E_N = Z_N Fcal − J Z_N (Poisson defect), C_N = Z_N Fcal + J Z_N,
A_M = 𝓜 − L_M − L_M* (finite Weil operator), K_F(a) the Laplace moments of the source, a_m = 2m + ½.
"First contact" means a vector f of the radical of the compressed primitive operator H_T (H_T f = 0); the memos
reason by contradiction from such an f.

Vocabulary caveat. Several memos (056 §2, 075 §§2–3, 079 §4 and the synthesis 099 §§4, 036–037) evaluate
symbols at zeros of a zeta function or at «critical zeros». It is only recorded that **they use an external
equivalence / a reduction to zeros**; it is not developed.

---

## R161_056 — The finite unitary phase has the wrong tangent

- **Object.** A = Z_N(s), B = Z_N(1−s), e = Au − B (Poisson difference), c = Au + B (complementary sum),
  U = −A′u, V = −Z_N′(1−s). Identities: U + V = −e′ + Au′ (1.1); on the locus Au = B, B·θ′/θ = e′ for the
  unimodular phase θ = Au/B (1.3); U − V = −c′ + Au′ (2.1).
- **Statements.** Chain-rule audit: PROVED (direct computation, upheld). The tangent of the
  unitary phase controls the mean U + V, not the difference U − V: PROVED. The identification of the unitary
  tangent with the critical jet proposed in R161_052–055: rejected. «Off the locus Au = B the main
  term does not change» is ARGUED (not written).
- **Where it stopped.** c is an additive sum of two histories, not a unimodular quotient: the exact
  Toeplitz–Hankel defect of the unitary colligation of R161_052 does not transfer to the critical jet. A
  quadratic Green identity mixing e with c remains open. In §2 it uses an external equivalence (evaluation at a zero).
- **Later correction.** None withdraws it; 057 develops the mixed identity.
- **Cross-check.** U1: no. U2: not directly (yes in the background: the colligation of 052 is one of compression). U3: no.
  U4: no. U5: yes, partially: the finite unitary colligation (dilation by unimodular quotient) is kept
  as transport of the base, but it is proved that its tangent gives the mean orientation, not the difference; it is not
  an isometric source dilation in the sense of exit A of R161_033.

## R161_057 — Exact four-block form of the mixed Green identity

- **Object.** a = Z_N Fcal f, d = J Z_N f, e = a − d, c = a + d, projections P_L, P_0, P_R (commuting with X).
  Re⟨e, Xc⟩ = Σ_j [⟨a_j, X a_j⟩ − ⟨d_j, X d_j⟩] (1.1);
  Re⟨e, Xc⟩ = G_phys − G_wrong + T·Φ_ext + G_0 (1.4), with
  G_phys = ‖(X−T)^{1/2} a_R‖² + ‖(−X−T)^{1/2} d_L‖², G_wrong = ‖(−X−T)^{1/2} a_L‖² + ‖(X−T)^{1/2} d_R‖²,
  Φ_ext = ‖a_R‖² + ‖d_L‖² − ‖a_L‖² − ‖d_R‖², G_0 = ⟨a_0, X a_0⟩ − ⟨d_0, X d_0⟩.
  Blocks of the support commutator: PZ − ZP = PZQ − QZP (4.1).
- **Statements.** (1.4) exact at every cut: PROVED (upheld; algebra of projections commuting with X).
  Separation of oriented flux and interior first moment; total unitarity does not cancel Φ_ext: PROVED
  (formula (2.1) is stated «whenever a and d are the two histories of the same colligation»; it is conditional on
  that normalization). Reduction of the support commutator to the two one-sided discrepancies Δ^R, Δ^L after
  the Tate adjustment: PROVED relative to R161_006 and R161_009.
- **Where it stopped.** Missing (3.3): G_wrong = boundary_commutator_N(f) + o(1), that is, the quadratic
  reciprocity of the two one-sided discrepancies with G_wrong. It is not replaced by adjunction on the whole space
  because (4.1) is exactly what that adjunction omits after compressing. OPEN.
- **Later correction.** 058–060 and 065 show that the route does not produce the sign; 065 identifies the
  candidate of 064 with this commutator.
- **Cross-check.** U2: yes, fully: uses X (= M_t), the compression P_0 and the off-diagonal blocks PZQ, QZP
  (leakage), with Tate accounting. U1, U3, U4, U5: no.

## R161_058 — Positivity of the double commutator and test of reciprocity

- **Object.** For H ⪰ 0, f ∈ ker H, B bounded: ⟨f, [B*, [H, B]] f⟩ = ⟨Bf, HBf⟩ + ⟨B*f, HB*f⟩ ≥ 0 (1.1). With
  JHJ = H, Jf = εf, JBJ = B*: both terms equal, total 2⟨Bf, HBf⟩ (2.2).
- **Statements.** (1.1) and (2.2): PROVED (upheld). Vanishing by parity or trace cyclicity: rejected
  (upheld: it is a vector state, not a trace). Equivalence «reciprocity ⟺ the radical is invariant under
  B and B*»: PROVED (it is a direct reading of (1.1)).
- **Where it stopped.** The vanishing (3.1) is not a formal consequence of Hf = 0; one would need to derive from (PC-ren)
  the negative balance (4.1) «mixed PC pairing = −⟨f,[B*,[H,B]]f⟩ − D_N^Γ(F)». OPEN. Defining the pairing by the right
  side would be circular.
- **Later correction.** 059 gives the block form; 060 substitutes PC-ren and does not obtain (4.1).
- **Cross-check.** U2: yes (H is the primitive compression; B the causal synthesis; blocks P_0BQ, QBP_0). U3: no (the form
  is semidefinite). U1, U4, U5: no.

## R161_059 — Exact block form of the compressed commuting pair

- **Object.** A = A*, AZ = ZA on the whole space; H = PAP, B = PZP, X = QAP, Y = QZP, Ȳ = QZ*P:
  [H, B] = Ȳ*X − X*Y (1.3), [H, B*] = Y*X − X*Ȳ (1.4); on the radical HBf = Ȳ*Xf − X*Yf.
- **Statements.** (1.3)–(1.4): PROVED (Q-insertion computation, upheld). Identification of the exterior
  ports (Xf = exterior Weil image; Yf, Ȳf one-sided Poisson histories): PROVED as a reading.
  Reduction to a negative square from commutation + reflection + Tate: rejected (upheld: the cross
  products are indefinite).
- **Where it stopped.** An additional relation of PC-ren is needed that identifies the cross products with
  a negative Γ/polar boundary form; it is the missing quadratic exterior reciprocity. OPEN.
- **Later correction.** 062 corrects that the power carrier is the anticommutator, not the commutator.
- **Cross-check.** U2: yes (compression, words QZP, QAP, Tate blocks added by Pi). U3: yes, weakly: the
  products Ȳ*X − X*Y are crossed indefinite forms; no neutral vector is sought. U1, U4, U5: no.

## R161_060 — Literal substitution of PC into the double commutator

- **Object.** S A Fcal = R_PC; Af = r + ℓ (r Tate, ℓ exterior); Q_B(f) = ⟨Bf,HBf⟩ + ⟨B*f,HB*f⟩ is rewritten
  as Re⟨R_PC Fcal f, g_B^+⟩ + Re⟨R_PC Fcal f, g_B^−⟩ + explicit polar/Tate terms (2.2).
- **Statements.** Insertion completed; no vanishing or new sign; the extremal exterior correlation of
  R161_023 is reconstructed. Declared labels: «completed», «absent», «open». The form (2.2) is given without the
  polar/Tate terms written out: it is ARGUED in its detail, although the diagnosis is plausible.
- **Where it stopped.** 0 = −Q_B(f) − D_N^Γ(F) is not obtained; an antisymmetric boundary law would be needed for
  the two pairings of (2.2). The mixed Green route remains expanded in all layers (list of §3).
- **Later correction.** None.
- **Cross-check.** U2: yes (same compression and Tate machinery). U1, U3, U4, U5: no.

## R161_061 — Poisson–Tate Lagrangian boundary identity (candidate)

- **Object.** K_T = G_T C (Tate Gram times exchange), symmetric and indefinite; symplectic form
  ω_T((v,j),(w,k)) = ⟨j,w⟩ − ⟨v,k⟩ on V_T ⊕ V_T; the graph L_T = {(v, K_T v)} is Lagrangian (1.4). Infinite
  carrier B_{N,T} = (E_R ⊕ E_L)², Ω((ξ,η),(ξ′,η′)) = ⟨η,ξ′⟩ − ⟨ξ,η′⟩, Ω_total = Ω + ω_T. Proposed identity
  (3.2): Ω_total(Λ_{N,T} f, Λ_{N,T} h) = ⟨PC_N f, h⟩ − ⟨f, PC_N h⟩.
- **Statements.** Lagrangian Tate graph: PROVED (trivial by symmetry of K_T). Green carrier that
  reproduces the compressed commutator: PROVED «at the formal block level». (3.2) and its identification with the
  extremal scalar (5.1) 2Re⟨g, P_R C_log g + εg⟩: OPEN/proposed.
- **Where it stopped.** Withdrawn by 062: the diagonal of an alternating form is identically zero.
- **Later correction.** R161_062 §0 (withdraws the alternating route as a closure argument); 065 closes the family.
- **Cross-check.** U3: yes: indefinite form on the double boundary space; but symplectic, where every vector is
  neutral; the graph is isotropic for every vector, not only for the first-contact one, and therefore carries no
  information. U2: yes (joint accounting with the Tate block, K_T = G_T C of R161_009/032). U1, U4, U5: no.

## R161_062 — The missing identity must be a Hermitian boundary power law

- **Object.** B(b,b′) = ⟨η,ξ′⟩ + ⟨ξ,η′⟩, B(b,b) = 2Re⟨η,ξ⟩; ⟨η,ξ′⟩ = (B + Ω)/2. Tate power
  B_T((v,K_Tv),(v,K_Tv)) = 2⟨v, K_T v⟩ (2.2). Compressed anticommutator (without commutation of A and Z):
  {H, B} = P{A,Z}P − Ȳ*X − X*Y (3.1); 2Re⟨Hf,Bf⟩ = ⟨f,P{A,Z}Pf⟩ − Re⟨Ȳf,Xf⟩ − Re⟨Xf,Yf⟩ (3.2); on the radical
  ⟨f,P{A,Z}Pf⟩ = Re⟨Ȳf,Xf⟩ + Re⟨Xf,Yf⟩ (3.3). Candidate balance (4.1) with 2⟨v_f, K_T v_f⟩ and polar term.
- **Statements.** Correction to 061: PROVED (Ω(b,b) = 0). Form B and Tate power: PROVED algebraically.
  (3.1)–(3.3): PROVED (upheld). (4.1): «bulk proved, primitive/polar expansion open». Limit (5.2) equal to the
  extremal scalar: OPEN.
- **Where it stopped.** It remains to prove that, after the polar/Tate completion, the current of the whole space is
  exactly the compressed anticommutator. Moreover 063 shows that identifying R Z f with the crossed collar is
  ill-typed.
- **Later correction.** R161_063 §3 withdraws the identification P_R(f) = 2⟨v_f, K_T v_f⟩ (introduced in the
  first version of 063 from (4.1) of this memo) and (4.4); 065 closes the family.
- **Cross-check.** U3: yes: B is an indefinite Hermitian form on the double boundary (Kreĭn type on (ξ,η)); non-radical
  neutral vectors are not studied, only its diagonal is used. U2: yes (compression, ports QA, QZ, Tate
  block). U1, U4, U5: no.

## R161_063 — Exact decomposition of the Poisson–Tate power by nested compression

- **Object.** I = Pi + R + Q (R Tate block, Q exterior). H = Pi A Pi, B = Pi Z Pi.
  2Re⟨Hf,Bf⟩ = ⟨f, Pi{A,Z}Pi f⟩ − P_R(f) − P_Q(f) (2.1), P_R, P_Q crossed pairings by block (2.2)–(2.3), without
  a mixed Tate/exterior term. On the radical: ⟨f,Pi{A,Z}Pi f⟩ = P_R(f) + P_Q(f) (2.4). Well-typed mixed pairing
  with y = Z* g(f): Re⟨Af, y⟩ = Re⟨r, Ry⟩ + Re⟨ℓ, Qy⟩ (5.2); Re⟨r,Ry⟩ = Re⟨v_f, G_T C v_f⟩ (3.3).
- **Statements.** (2.1)–(2.4): PROVED (upheld). Diagonal identification R Z_N f = crossed collar:
  rejected/ill-typed. (3.3): PROVED relative to R161_009 and R161_022. (5.2): PROVED but coincides with the
  backward decomposition already audited (R161_022). Vanishing of the complete mixed power
  Re⟨r,Ry⟩ + Re⟨ℓ,Qy⟩ + Re⟨d,y⟩ (5.3): OPEN, terminal.
- **Where it stopped.** (2.4) is a tautology of the radical; (5.3) is the exterior reciprocity of R161_022.
- **Later correction.** It corrects itself (withdraws (3.2) and (4.4) of its own first version). 064–065.
- **Cross-check.** U2: yes, in the most explicit form of the part: exact joint accounting of the primitive,
  Tate and exterior blocks of the compression. U1, U3, U4, U5: no.

## R161_064 — Well-typed mixed power and support concomitant

- **Object.** y_N = Z_N* g_N, Tau P y_N = j_N (collar). Re⟨Af, y_N⟩ = Re⟨r, j_N⟩ + Re⟨ℓ,(I−P)y_N⟩ (1.3), and with
  d = w − Af one reconstructs Re⟨y_N, w⟩ (1.4). Support concomitant K_P(S;g,w) = ⟨Pg,PSw⟩ − ⟨PS*g,Pw⟩ =
  ⟨Pg,PSQw⟩ − ⟨Qg,SPw⟩ (2.2). Target (4.2): C_{M,N,T}(f) = ε Re⟨v_f, j⟩ + D^Γ + ½‖P_R^ext C_log g + εg‖² + o(1),
  and (4.3) C = o(1) on the radical.
- **Statements.** Mixed typing of the collar: PROVED. (2.2): PROVED. Identification of its finite-rank block
  with the collar; (4.2); (4.3): OPEN.
- **Where it stopped.** Neither the algebra of projections nor PC-ren gives (4.2); the placement of Tau occurs before the
  synthesis in (3.1) and after it in the collar.
- **Later correction.** R161_065 proves K_P = ⟨g,[P,S]w⟩ and withdraws (4.2)–(4.3) as consequences.
- **Cross-check.** U2: yes (compression concomitant; Tate placement). U1, U3, U4, U5: no.

## R161_065 — The support concomitant is the exterior commutator already audited

- **Object.** K_P(S;g,w) = ⟨g, [P,S] w⟩ (1.2).
- **Statements.** (1.2): PROVED (one line; upheld). Collision with R161_042–044 and 057: PROVED. Positive
  expansion of 064 (4.2): withdrawn. New Lagrangian/Hermitian route from the current hypotheses: exhausted
  (list of four variants in §3). An additional exterior arithmetic theorem is missing that would exclude the
  three-block countermodel of R161_050, for example Re⟨g, P_R C_log g + εg⟩ = 0.
- **Where it stopped.** Family closure (061–065): alternating form (zero diagonal); diagonal Hermitian power
  (wrong collar type R Z f instead of Tau P Z* g); well-typed mixed power (reconstructs the tautology of
  R161_023); finite-order defect (= [P,S]). «Exhausted» rests on the countermodel of R161_050 for the formal
  package (PC-ren, radicality, parity, unitarity, compression); for the class thus declared it is NO-GO; it does not
  exclude additional arithmetic inputs.
- **Later correction.** None.
- **Cross-check.** U2: yes, and it is the record of failure: every Green/power rewriting over the compression, the
  leakage and the Tate block returns to [P,S] or to the extremal correlation. U3: yes (closes the alternating form and the
  diagonal Hermitian one). U1, U4, U5: no.

## R161_066 — Selection of the new arithmetic input

- **Object.** Oriented Laurent observation R_{m,r}[G] = (1/2πi)∮_{|s−s_m|=r} G(s) ds, s_m = 2m+1;
  R_{m,r}[ζ W_ε^0] = ζ(s_m) K_F(2m+½) (3.2); energy E_T^Laur(F) = Σ ω_m |R_{m,r_m}[ζW_ε^0]|² with
  ω_m = 2^{−m}(2m+½)e^{−2(2m+½)T}/|ζ(2m+1)|², equal to D_T^pole(F). OAL law (4.1): oriented finite germ whose
  contour energies → 0 on the radical.
- **Statements.** Selection of the smallest target (removability of the Γ poles at s = 2m+1): completed.
  Contour realization of the Γ energy: PROVED relative to R161_025. Distinction from the three-block
  countermodel: «only at the level of typing». OAL: OPEN. §2: local Möbius inversion is not the new input
  (collision with P121_CMO_SOURCE_MATRIX_NO_GO: after elimination the logarithmic connection has zero root diagonal
  and the annular transport block remains; the endpoint-regularity variant produces the global Möbius tail
  without control).
- **Where it stopped.** OAL withdrawn by 067.
- **Later correction.** R161_067.
- **Cross-check.** U4: yes, tangentially: records that local Möbius inversion (not the truncated weights
  c_N(k)) does not give the law; it does not examine the remainder of near-coincidences with truncated Möbius weights. U1, U2, U3, U5: no.

## R161_067 — Dichotomy for oriented finite Laurent observations

- **Object.** Case A (without Γ factor): the germ is holomorphic inside C_m and its contour is 0 for all M, N.
  Case B (with Γ factor): residue ζ(s_m) K_F(2m+½) independent of M, N (1.4). Required form of a genuine
  input (3.1): Q^out − Q^in = Σ_{m≤L} ω_m|K_F(2m+½)|² + R, with the left side ≤ 0 by radicality, R ≥ 0
  or → 0 uniformly, and Q^out, Q^in not defined by the moments.
- **Statements.** Dichotomy: PROVED (Cauchy; upheld). OAL: withdrawn (circular or topologically
  equivalent to the target). Quadratic comparison law (3.1): OPEN. §3 claims «a genuine input cannot be
  a linear germ nor a contour limit»: ARGUED; 080 §5 says it does not justify the general exclusion.
- **Later correction.** R161_080 §5 (the exclusion of every linear approach in §3 is not justified by the
  computation).
- **Cross-check.** U1–U5: no. (The form (3.1) is a quadratic comparison with remainder, without an object.)

## R161_068 — Gamma–Euler observability identity

- **Object.** (R_δ F)_m = √a_m e^{−a_m(T+δ)} K_F(a_m); translation τ_b F(t) = F(t−b), R_δ τ_{log n} = D_n R_δ,
  (D_n x)_m = n^{−a_m} x_m. Generator L = Σ Λ(n) n^{−1/2} τ_{log n}; R_δ L F = C_ζ R_δ F, c_m = −ζ′/ζ(2m+1) > 0.
  Theorem 2.1: Re⟨R_δ F, R_δ L F⟩ = Σ_m c_m a_m e^{−2a_m(T+δ)} |K_F(a_m)|² ≥ 0, zero iff F = 0.
- **Statements.** Theorem 2.1: PROVED (for the complete Laplace observation; upheld in that convention).
  (4.2) primitive radical pairing: PROVED but it does not contain the energy. (4.4): withdrawn (wrong operator
  factor: the unprojected pairing is ⟨R_δ L A_∞ F, R_δ F⟩). Division-free factorization (5.1)
  L*G_δ = A_∞ K_δ + Pi_T U_δ + V_δ(I − P_T): OPEN. The header note (added by 070) declares that §§4–5 do not
  establish admissible adjoint identities (distinct domains) and that novelty in the corpus is not
  established.
- **Where it stopped.** Radicality inserts A_∞ into the observed vector; removing or inverting it is circular.
- **Own reading.** The positivity c_m > 0 is linear in the comb and holds for any nonzero nonnegative
  weight (072 §2 proves it): the detector does not distinguish Λ.
- **Later correction.** R161_070 (domains), R161_072 (substitution of coefficients).
- **Cross-check.** U1: no (Λ enters linearly via −ζ′/ζ; there is no term of degree ≥ 2). U2: yes, weakly (in §5 the
  factorization carries blocks Pi_T and (I − P_T)). U3, U4, U5: no.

## R161_069 — A faithful observation does not factor formally through the null-mode operator

- **Object.** Lemma: if C ⪰ 0 is faithful and C = AK as a form, then Af = 0 ⇒ f = 0. Application to
  C_δ = L* R_δ* R_δ: an identity C_δ = A_∞ K_δ would exclude every null mode.
- **Statements.** Abstract lemma: correct as a conditional lemma. The application to first contact: invalid
  according to the header correction of 070 (first contact concerns ker H_T of the primitive compression,
  not ker A_∞; moreover the domain correction is missing). «Impossibility of deriving the factorization»: withdrawn by
  070; «equivalence in strength is not circularity».
- **Later correction.** R161_070 (header of 069 and §4 of 070, with the counterexample A = [[0,1],[1,0]],
  P = diag(1,0): A invertible but PAP = 0 on the range of P).
- **Cross-check.** U2: yes, in the correction (the distinction global kernel / compressed kernel is the effect of the
  compression to the window). U1, U3, U4, U5: no.

## R161_070 — Typed finite Gamma–Euler detector and exact collar

- **Object.** On L²(I), I = (−T,T): (Rf)_m = b_m ∫_I e^{−a_m t} f, b_m = √a_m e^{−a_m(T+δ)} (Hilbert–Schmidt);
  L_N = Σ_{2≤n≤N} Λ(n) n^{−1/2} V_{log n}, c_{m,N} = Σ_{n≤N} Λ(n) n^{−(a_m+½)}, D_N = diag(c_{m,N}),
  C_N = R* D_N R. Right exterior collar (E_N f)_m = b_m Σ Λ(n) n^{−(a_m+½)} ∫_{max(−T,T−log n)}^T e^{−a_m u} f(u) du.
  Identity R B_N = D_N R − E_N (2.1), B_N = P L_N P; C_N = (G B_N + B_N* G)/2 + (R*E_N + E_N*R)/2 (2.2);
  ⟨f, C_N f⟩ = Re⟨Rf, R B_N f⟩ + Re⟨Rf, E_N f⟩ (2.3). Stabilization E_{N′} − E_N = (D_{N′} − D_N) R for
  N′ ≥ N ≥ e^{2T} (3.1). Sufficient comparison (4.1): 2Re a_T(f, Kf) = ⟨f, C_N f⟩ + Q(f), Q ≥ 0, Kf primitive.
- **Statements.** C_N positive, trace class, faithful (completeness of moments R161_019); convergence in trace norm;
  (2.1), (2.2), (3.1): PROVED (upheld; change of variable and cut at T). (4.1): OPEN. No sign for the
  collar pairing Re⟨Rf, E_N f⟩.
- **Where it stopped.** It builds neither K nor Q. The inactive primes (n ≥ e^{2T}) live entirely in the collar:
  discarding the exterior term discards their whole contribution.
- **Later correction.** 071–072 exploit (2.1); 072 shows that the construction does not distinguish Λ.
- **Cross-check.** U2: yes (exact leakage of the translations truncated by the compression: E_N is the exterior part of
  R L_N; finite-rank observation after truncating m). U1: no (linear in Λ). U3, U4, U5: no.

## R161_071 — Parity test and exact Gamma–Euler balance

- **Object.** R_L (m ≤ L), G_L = R_L* R_L, S_L = G_L + J G_L J, test h_L = Pi S_L f (admissible in the logarithmic
  form domain of Γ, since its kernel is a finite sum of exponentials). With N ≥ e^{2T}, B = P L_N P, the
  first-contact equation (𝓜 − B − B*) f = r (r in Tate) gives 0 = Re m_T(f, S_L f) − Re⟨(B+B*)f, S_L f⟩ −
  Re⟨r, S_L f⟩ (1.1). Balance (2.3): 0 = 2c_{N,L} + Q_{N,L}, with c = ⟨R_L f, D R_L f⟩ (positive detector) and
  Q = 2v − 2e − Re m_T(f, S_L f) + Re⟨r, S_L f⟩ (2.4). Truncated backward observation (3.1).
- **Statements.** Admissible test, balance (2.3), formula (3.1): PROVED on the imported form domain.
  Sign of Q on the radical: OPEN. If Q ≥ 0 for all L, f = 0.
- **Where it stopped.** The sign of Q must come from the explicit kernels; neither the positivity of 𝓜 nor that of G_L nor
  parity gives it.
- **Later correction.** R161_072 (Q is the reformulated equation: Q = −2c at first contact); R161_081 (Q cannot
  be ≥ 0 on the whole primitive space).
- **Cross-check.** U2: yes (compression P L_N P; collar; Tate term r; finite rank L). U1: no. U3: no. U4, U5: no.

## R161_072 — Recombination of the balance and test of coefficients

- **Object.** Before using first contact: Q = −2c − Re a_T(f, S_L f) + Re⟨r, S_L f⟩ (1.1). At first
  contact Q = −2c exactly. Substitution Λ(n) → arbitrary w_n ≥ 0: R_L B_N^w = D^w R_L − E^w verbatim;
  faithful detector if some w_n > 0 (w_2 suffices). For N′ ≥ N ≥ e^{2T}: ΔQ = −2Δc.
- **Statements.** (1.1): PROVED (upheld). Test of coefficients: the positivity and faithfulness of the detector do not
  distinguish the von Mangoldt comb: PROVED. Inactive tail exactly balanced: PROVED. «It is not a universal
  impossibility theorem» (declared).
- **Where it stopped.** The test Pi(G_L + J G_L J) f is an exact reformulation without new restriction. A
  bound using the Γ kernel together with the arithmetic relations of the coefficients is needed.
- **Later correction.** None; 081 reinforces it.
- **Cross-check.** U1: yes, as a pertinent negative record: the construction contains arithmetic values but uses Λ
  only linearly; it survives every weight w ≥ 0 (in particular cΛ and a_P), hence it lacks the breaking
  clause; it introduces no term of degree ≥ 2. U2: yes (collar, finite rank). U3, U4, U5: no.

## R161_073 — Stabilized inverse of moments

- **Object.** H = H_T ⪰ 0 with compact resolvent; R : ℋ → C^L injective on ker H (exists by R161_046, not
  effective). S = H + R*R ≥ αI, M = R S^{−1} R* a positive contraction. Identity
  ⟨y,(I−M)y⟩ = ‖y − Ru‖² + ‖H^{1/2}u‖², u = S^{−1}R*y (2.1). ker H ≅ ker(I − M); ker H = {0} ⟺ λ_max(M) < 1 (3.1).
- **Statements.** All PROVED under the imported hypotheses (upheld: standard finite-rank perturbation
  argument). Strict bound λ_max(M) < 1: OPEN.
- **Where it stopped.** M ≤ I is all that (2.1) gives; the finite matrix encodes the complete inverse S^{−1}; there is no
  bound uniform in T.
- **Later correction.** 074 gives the residue certificate.
- **Cross-check.** U2: yes (finite-rank perturbation R*R of the compressed operator). U3: no. U1, U4, U5: no.
  Note: (2.1) is a «form = sum of squares» identity for I − M, but generic (it holds for every H ⪰ 0).

## R161_074 — Upper residue certificate for the stabilized matrix

- **Object.** U approximate, E = R* − SU, M_0 = RU + U*R* − U*SU: M = M_0 + E* S^{−1} E (1);
  M_0 ≤ M ≤ M_0 + α^{−1} E*E (2); sufficient certificate I − M_0 − α^{−1}E*E > 0 (3). 2×2 example:
  H = [[1,−1],[−1,1]], R = [1,0], U = (½,0)ᵗ: M = 1, M_0 = ½, E*S^{−1}E = ½.
- **Statements.** (1)–(3) PROVED; example verified exactly (upheld). Galerkin only gives a lower bound for
  M. No arithmetic certificate built.
- **Where it stopped.** It requires a quantitative α, admissible columns and a bound on the residue in each window; a
  computation on chosen windows does not give all T.
- **Cross-check.** U2: yes (finite rank). U1, U3, U4, U5: no.

## R161_075 — Three senses of the completed zero product

- **Object.** Distinguishes: L² product (maximal multiplication by the function on the line, injective);
  distributional product (multiplication annihilates deltas at real zeros); meromorphic identity
  d_Γ(s) + ζ′/ζ(s) + ζ′/ζ(1−s) ≡ 0.
- **Statements.** L² injectivity (2.1), distributional counterexample (3.1), meromorphic distinction: PROVED. The
  exclusion of R161_018 («every linear limit of PC is a tautological zero operator») is not established by its
  argument.
- **Where it stopped.** Compatible carriers and limits must be given for A_M f, S_N^ren A_M f and the separated
  ports. Uses an external equivalence / reduction to zeros in §§2–3 (recorded without development).
- **Later correction.** Corrects R161_018 (and, by extension, whatever in 099 rests on 018).
- **Cross-check.** U1–U5: no.

## R161_076 — Physical local Weil limit and Poisson domain

- **Object.** f ∈ C_c^∞(−T,T), A_M f stabilizes on |t| ≤ K for M ≥ e^{K+T}; limit A_loc f in D′(ℝ);
  convergence in X_η = L²(e^{−2η|t|}dt), η > ½. Composition S_N A_M f stable on [−K,K] if M ≥ N e^{K+T} (3.1).
  The continuum C_N h(t) = e^{−t/2} ∫_{−∞}^{t+log N} e^{y/2} h(y) dy is not defined on X_η (example
  h = 1_{y<0} e^{−y/2}).
- **Statements.** Local stabilization, convergence in X_η, (3.1), insufficiency of the weighted space: PROVED
  (upheld). Limit of the renormalized product on first-contact sources: OPEN.
- **Cross-check.** U2: not in the strict sense (domain analysis). U1, U3, U4, U5: no.

## R161_077 — Action of the continuum modulo Tate

- **Object.** J_f(x) = ∫_{−∞}^x e^{u/2} f; C_N L_M f(t) = e^{−t/2} Σ Λ(n) J_f(t + log N − log n) (1.1),
  C_N L_M* f = e^{−t/2} Σ Λ(n)/n J_f(t + log N + log n) (1.2). Lower anchor C_{N,a}; the difference of two anchors
  lies on the negative Tate line e^{−t/2} (2.1); Pi_K C_{N,a} h does not depend on the anchor (2.2). Projected limit
  at fixed N (3.2).
- **Statements.** All PROVED at fixed N and for smooth compact sources (upheld). The removed scalar is not
  proved to be zero; no bound uniform in N.
- **Cross-check.** U2: yes, minor: the projection Pi_K off Tate eliminates a rank-one ambiguity. U1, U3, U4, U5: no.

## R161_078 — Convergence of the renormalized tail on smooth sources

- **Object.** With |ψ(x) − x| ≤ C x e^{−c√log x} (CITED, bound not re-proved) and ∫e^{−u/2} f = 0: right Euler
  current l(t) = −∫E(x) d_x[x^{−1/2} f(t − log x)], |l| + |l′| ≤ C_f e^{t/2 − c′√t} (2.1); Σ_{n≤N} q_t(n) −
  ∫_1^N q_t converges uniformly on |t| ≤ K (3.2); S_N h − C_{N,a} h converges locally uniformly.
- **Statements.** PROVED relative to the cited bound on the error term (upheld). Constants depending on
  derivatives of f; it does not extend to radicals; value of the limit not identified.
- **Own reading.** The input is a density bound (error of ψ), generic for any weight with the same
  error; it carries no sign.
- **Cross-check.** U1–U5: no.

## R161_079 — Weak renormalization on primitive L²

- **Object.** T_N h = Σ_{n≤N} n^{−1/2} h(t + log n) − ∫_1^N x^{−1/2} h(t + log x) dx; for f ∈ L²([−T,T]) with
  ∫e^{−u/2} f = 0, T_N A_loc f converges in D′ with |⟨(T_B − T_A)A_loc f, φ⟩| ≤ C ‖f‖_2 p_J(φ) ρ(A) (1.3). Proof
  by convolution k = f * φ̌ (the derivatives pass to the test). Continuum modulo Tate via (∂_t + ½)v = h.
- **Statements.** Theorem: PROVED with the cited bound on the error term (upheld). Transport to the Hilbert
  graph and vanishing: not proved. Warns that smoothing f does not preserve H_T f = 0.
- **Cross-check.** U2: no (it does warn that the compression does not commute with the convolution). U1, U3, U4, U5: no. In §4 it uses
  an external equivalence (a product with the zeta function), without development.

## R161_080 — Escape of the pole and two-scale observation

- **Object.** h_R(t) = −k e^{at} 1_{t<−R}: residue k at z = a for all R, while h_R → 0 in D′, in L² and in
  every Sobolev space (smooth version). Abel observation B_ε(h) = −ε∫e^{−(a−ε)t} h; the limits do not commute (2.1);
  truncated B_{ε,L} requires εR → 0, εL → ∞ (3.2). Conditional estimate |B_{ε,L}(v) − k| ≤ |k|[1 − e^{−εT} +
  e^{−εL}] + ε C_a(r) (4.1).
- **Statements.** Escape formulas, Sobolev example, bound (4.1): PROVED (upheld; (4.1) is CONDITIONAL on
  the weighted-remainder hypothesis). It is not applied to the physical defect. §5: the computation does not justify the general
  exclusion of linear approaches of 067 §3.
- **Cross-check.** U1–U5: no.

## R161_081 — Test of the sign of Q on Weil eigenvectors

- **Object.** Canonical extension of the forcing r_f by Riesz in the Tate space; K_L = Pi S_L Pi;
  Q_{N,L}(f) = −2c_{N,L}(f) − Re a(f, K_L f) (1.1). For Hf = λf, Jf = εf:
  Q_{N,L}(f) = −2 Σ_{m≤L} [d_{m,N} + λ] |(R_L f)_m|² (2.1).
- **Statements.** (1.1), (2.1): PROVED under the form/operator hypotheses (upheld). Universal Q ≥ 0 on the
  primitive space: discarded (NO-GO with class: every proof combining only H ⪰ 0 with positive Γ/Euler
  weights gives the opposite sign on eigenvectors with λ ≥ 0). The inequality specific to the radical: OPEN, not
  circular, but it requires an additional consequence of the equality-state equations.
- **Falsifier.** Any eigenvector of definite parity with λ ≥ 0 and R_L f ≠ 0 on a nonnegative window.
- **Cross-check.** U2: yes (primitive compression, Tate, finite rank). U3: no. U1, U4, U5: no.

## R161_099 — Synthesis of phase 161, first construction

- **Object.** Summarizes 001–045 (does not cover 046–081). Identity (PC): S_N A_M Fcal = {X,E_N} − L_M* E_N − J H_{M,N} −
  H_{M,N} Fcal, with H_{M,N} = L_M S_N − K_N; renormalization S_N^ren = S_N − C_N(D), C_N(s) = N^{1−s}/(1−s).
  Milestones: canonical square blind to the sign (invariant under A_M → −A_M); nonnegative weights do not telescope the tail
  (h_N(p) = log p for N < p and 0 afterwards); exterior ports and one-sided discrepancies (005–006); Sonin–Gamma
  excess ⟨D_Γ g,g⟩ − 2T‖g‖² = 2∫_T^∞(t−T)|g|² ≥ 0 (014); pole energy D_T^pole and Hankel form
  B^Γ_{T,δ} with kernel k_Γ^+(v) = Σ e^{−(2m+½)v} (025–026); image (027–028); oriented variance (030):
  (log k)/2 Σ_d Λ(d)(‖x_d^+‖² + ‖x_d^−‖²) − ‖Σ_d Λ(d) m_d‖² = (log k) Σ_d Λ(d)‖r_d‖² + ½ Σ_{d,e} Λ(d)Λ(e)‖m_d − m_e‖²;
  path vectors (031), Tate sign conversion ε⟨v, G_T C v⟩ = ‖r‖² (032); withdrawal by cross
  interference in k and «exit A»: explicit Parseval/Naimark dilation (033); diagonalization by the ratio and
  product channels of phase 106 and coherent leakage ‖(I − P_T) Σ_{k≤N}(log k) d_k P_T F‖² (034); two-state
  parallelogram ½(‖U_N f‖² + ‖V_N f‖²) − ¼‖(U_N + V_N) f‖² = ¼‖(U_N − V_N) f‖² (035); C² countermodel (038);
  terminal equivalence (039); identification of the two exterior histories (040); orientation (041);
  mixed identity (042); opposite-parity Tate vanishes (043); tautological primitive piece (044); Brown–Halmos and
  determinant anomaly (045).
- **Statements.** Declared verdict: OPEN; «PARTIAL_NEW + STRUCTURAL_NEGATIVE». Uses an external equivalence
  / reduction to zeros in the summaries of 007, 008, 036, 037 (recorded without development).
- **Own reading.** The synthesis claims in §4 (summary of 018) that every linear limit of (PC-ren) is tautological;
  R161_075 says that this exclusion is not established. The synthesis was not updated. It also describes 019 as
  closing the rank-rigidity half, and 024–025 weaken it; that is recorded within the synthesis.
- **Cross-check.** U1: yes: the variance identity of 030 is of degree two in Λ (Λ(d)Λ(e)‖m_d − m_e‖²), enters
  additively and uses Σ_{d|k}Λ(d) = log k; its failure is recorded in 031–033: the path vectors do not depend on d (the
  transversal variance is identically zero) and the physical realization is the coherent sum in k, whose norm
  contains the cross Gram Σ_{k≠l}(log k)(log l)/√(kl) Re⟨Δ_k F, Δ_l F⟩ that the direct sum omits. U2: yes: coherent
  leakage of 034, identification of exterior histories of 040, Tate accounting 032/043. U3: yes, minor: G_T C
  indefinite, positive only on the parity line (032). U4: no (the local Möbius 121/CMO is only mentioned in
  §4 summary of 004). U5: yes: «exit A» of 033 (explicit Parseval/Naimark dilation supplied by
  Poisson) is stated and not built; 035 declares it unnecessary after the coherent parallelogram, and 038 shows
  that (PC), radicality, polarization and parity do not imply the saturation (countermodel in C²).

---

## Summary

### (a) Reusable PROVED pieces

1. Four-block mixed Green identity (1.4) of R161_057 §1 and the support commutator PZ − ZP = PZQ − QZP
   (§4).
2. Radical double commutator ⟨f,[B*,[H,B]]f⟩ = ⟨Bf,HBf⟩ + ⟨B*f,HB*f⟩ ≥ 0 and its equality by reflection
   (R161_058 §§1–2).
3. Block form of the compressed commuting pair [H,B] = Ȳ*X − X*Y (R161_059 §1) and compressed anticommutator
   {H,B} = P{A,Z}P − Ȳ*X − X*Y without commutation hypothesis (R161_062 §3).
4. Three-block primitive/Tate/exterior decomposition without mixed term (R161_063 §2) and well-typed mixed
   pairing (§5, (5.2)).
5. K_P(S;g,w) = ⟨g,[P,S]w⟩ (R161_065 §1).
6. Finite Laurent dichotomy (R161_067 §1).
7. Faithful Gamma–Euler detector C_N = R*D_N R, exact collar R B_N = D_N R − E_N, Hermitian identity and
   stabilization law (R161_070 §§1–3); truncated backward observation (R161_071 §3).
8. Exact balance 0 = 2c + Q and its recombination Q = −2c − Re a_T(f, S_L f) + Re⟨r, S_L f⟩ (R161_071 §2,
   R161_072 §1); spectral formula Q = −2Σ[d_{m,N} + λ]|(R_L f)_m|² (R161_081 §2).
9. Stabilized inverse S = H + R*R, identity ⟨y,(I−M)y⟩ = ‖y − Ru‖² + ‖H^{1/2}u‖², ker H ≅ ker(I−M)
   (R161_073); residue certificate M = M_0 + E*S^{−1}E (R161_074).
10. Local Weil limit and convergence in X_η (R161_076); continuum modulo Tate (R161_077); smooth renormalized
    convergence (R161_078) and weak convergence on primitive L² (R161_079), both relative to the cited bound on the
    error term of ψ.
11. Escape of the pole and two-scale extraction (R161_080; (4.1) conditional).
12. L² / distributional / meromorphic distinction of the zero product (R161_075).

### (b) Closures with class and falsifier

- Lagrangian/Hermitian boundary family (R161_061–065): alternating form (zero diagonal; the graph is isotropic
  for every vector); diagonal Hermitian power (ill-typed collar); well-typed mixed power (reconstructs the
  tautology of R161_023); finite-order defect (= [P,S]). Class: rewritings built only with (PC-ren),
  radicality, parity, unitarity and compression. Falsifier: three-block countermodel of R161_050 (and the
  C² one of R161_038 for the saturation).
- Double commutator + reflection + Tate (R161_058–060): gives no vanishing; the literal substitution of PC-ren
  reconstructs the extremal correlation.
- OAL (R161_066–067): circular (with Γ) or topologically equivalent to the target (without Γ).
- Factorization of a faithful detector through the null-mode operator (R161_069): conditional lemma; the application
  was invalidated by 070 (global kernel ≠ compressed kernel; 2×2 counterexample).
- Gamma–Euler detector as sign carrier (R161_072): falsifier = any weight w ≥ 0 with some w_n > 0
  (in particular only w_2), which gives an equally positive and faithful detector.
- Q ≥ 0 on the whole primitive space (R161_081): falsifier = eigenvectors of definite parity with λ ≥ 0.
- Galerkin as a certificate of λ_max(M) < 1 (R161_074): exact 2×2 example.
- Phase unitary as critical jet (R161_056): gives the mean orientation U + V, not U − V.

### (c) Explicitly open, with its obstacle

- Quadratic reciprocity of the two one-sided discrepancies with G_wrong (R161_057 (3.3)).
- Negative balance «mixed PC pairing = −⟨f,[B*,[H,B]]f⟩ − D^Γ» (R161_058 (4.1)); antisymmetric boundary law for
  the two pairings of R161_060 (2.2).
- Vanishing of the complete mixed power Re⟨r,Ry⟩ + Re⟨ℓ,Qy⟩ + Re⟨d,y⟩ (R161_063 (5.3)).
- Independent quadratic comparison Q^out − Q^in = Σ ω_m|K_F(2m+½)|² + R (R161_067 (3.1)).
- Division-free factorization L*G_δ = A_∞K_δ + Pi_T U_δ + V_δ(I−P_T) (R161_068 (5.1)); comparison
  2Re a_T(f,Kf) = ⟨f,C_N f⟩ + Q(f), Q ≥ 0, Kf primitive (R161_070 (4.1)) — K and Q remain to be built.
- Q_{N,L} ≥ 0 only on the radical (R161_071, R161_081): requires an additional consequence of the
  equality-state equations that does not hold for eigenvectors with λ ≥ 0.
- λ_max(M) < 1 with a certificate uniform in T (R161_073–074).
- Limit of the renormalized product on first-contact sources, uniform in N, and its value (R161_076–079);
  extraction of residues with weighted remainder (R161_080).
- Exterior arithmetic theorem excluding the three-block countermodel, e.g. Re⟨g, P_R C_log g + εg⟩ = 0
  (R161_065 §4).

### (d) What already covers U1–U5 and why it failed

- **U1.** The oriented variance identity of degree two in Λ with Σ_{d|k}Λ(d) = log k (summarized in R161_099,
  entry 030) enters additively; it failed because the physical path vectors do not depend on d (031: zero transversal
  variance) and the physical realization is the coherent sum in k, with uncontrolled cross Gram (033); its
  diagonalization falls into the ratio/product channels of phase 106 (034). In the part itself, 068/070/072
  use Λ only linearly and 072 proves that the construction survives every weight w ≥ 0.
- **U2.** It is the central machinery of the part: physical compression P, blocks PZQ/QZP, leakage, position operator X,
  primitive projection, Tate block K_T = G_T C, finite rank R_L, perturbation R*R. All the
  rewritings (057, 059, 062–065) end in the commutator [P,S] or in the extremal correlation of R161_023;
  the identities with collar (070–072) are the rewritten first-contact equation (Q = −2c); the finite-rank one
  (073) reduces to λ_max(M) < 1 without a bound. The coherent leakage ‖(I − P_T)Σ(log k)d_k P_T F‖² (034) and the joint
  accounting with Tate remained as targets without an identity giving their saturation.
- **U3.** Indefinite forms on the double boundary: symplectic Ω (061, withdrawn: every vector neutral) and Hermitian
  B(b,b′) = ⟨η,ξ′⟩ + ⟨ξ,η′⟩ (062, used only on the diagonal; wrong collar type, 063). K_T = G_T C is
  indefinite and positive only on the parity line (032). No non-radical neutral vector was studied.
- **U4.** Not covered in this part. Only local Möbius inversion appears (066 §2, collision with
  P121_CMO_SOURCE_MATRIX_NO_GO), not the truncated weights c_N(k).
- **U5.** «Exit A» (explicit Parseval/Naimark dilation, 033) was stated and not built; 035
  replaced it with the coherent parallelogram and 038 showed that (PC) + radicality + polarization + parity do not
  imply the saturation. The finite unitary colligation (052–055) is kept as transport but its tangent
  gives the mean, not the difference (056).

### (e) Inconsistencies between memos

- R161_099 does not cover 046–081 and keeps the reading of 018 («every linear limit of PC-ren is tautological»), which
  R161_075 §5 declares not established.
- R161_067 §3 claims that a genuine input cannot be linear; R161_080 §5 says that this computation does not justify
  the general exclusion.
- R161_068 §§4–5 and R161_069 §2 confuse observation domains and global kernel with compressed kernel; this is
  corrected by the header notes written from R161_070 on.
- R161_062 (4.1) uses 2⟨v_f, K_T v_f⟩ as diagonal power; R161_063 §3 declares it ill-typed.
- R161_064 (4.2)–(4.3) are stated as a target «of unique non-circular form»; R161_065 withdraws them as a
  reformulation of the missing theorem.
- R161_065 §3 calls the route «exhausted»; it is exhaustion relative to the current formal hypotheses, not a universal
  NO-GO (the memo itself qualifies this in §4).
- R161_072 and R161_081 declare that they are not universal impossibility theorems; R161_081 does exclude Q ≥ 0 on the whole
  primitive space.

### (f) Files read (complete reading with Read)

Context of phase 212: README.md, OBJECT_SPEC.md, LEDGER.md, BRIEF_CONSTRUCTOR.md, REVIEW_003.md.

Part: R161_056, R161_057, R161_058, R161_059, R161_060, R161_061, R161_062, R161_063, R161_064, R161_065,
R161_066, R161_067, R161_068, R161_069, R161_070, R161_071, R161_072, R161_073, R161_074, R161_075, R161_076,
R161_077, R161_078, R161_079, R161_080, R161_081, R161_099 (662 lines, read in two calls). Twenty-seven
files, all read to the last line. R161_082 … R161_098 do not exist.
