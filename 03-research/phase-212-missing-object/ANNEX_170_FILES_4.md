# Annex 170 — stretch 4: files R170_863 to R170_900

Reading record of the 38 files of the stretch, in order. Notation of each memo. Labels
are cited as "declared"; when the proof read does not sustain them this is indicated separately. Cross-check
with the terrain not excluded by round 1 of phase 212:

- T1: continuous squares with the arithmetic in the index or in the dilation weights;
- T2: explicit factorization of type [log gcd(i,j)] = E diag(Λ) Eᵀ (divisor incidence) as a Gram model;
- T3: total identification of Λ by Σ_{d|n}Λ(d) = log n converted into a quadratic bound;
- T4: converting the mixed pairings of the finite Poisson–Chebyshev identity (H_{M,N}, E_N) into Σ_{k>N} h(k)|ℓ_k(F)|² with h ≥ 0.

Common frame of the stretch. All memos work inside the "first contact" programme of phase 170:
a vector F in the radical ker H_T (or Z_T) of the primitive form at the threshold, the renormalized PC
(Poisson–Chebyshev) identity of R170_856, the Tate port (b, h = (PS_N^*P)^{-1}b, q = QS_N^*h,
z = QAF − ρq, ρ_F with PA_MF = ρ_F b) and the sought "exterior law" β_phys(F) = 𝔚_K(F) + Θ_ext(F) = 0
(labels VIR–LB / D always OPEN). No memo of the stretch writes an identity of the form
a_T(F) = ‖V_T F‖² + ρ_T(F). Several memos reflect a reading that uses an external equivalence
only in their status header ("VIR–LB / D OPEN"); they do not develop it.

---

## 1. Entries by file

### R170_863 — Null anchor of divisor incidence
- **Object.** Finite incidence complex, M ≥ N: paths 𝒫^{int}_{M,N} = {(d,m): dm ≤ N};
  C₁ = ℝ^{𝒫} ⊕ ℝ^{N}, C₀ = ℝ^{N}; boundary (∂(x,y))_k = Σ_{dm=k} x_{d,m} − y_k (1.3);
  Laplacian Δ_{M,N} = ∂^*∂ ⪰ 0 (1.4). Anchor x^Λ_{d,m} = Λ(d)/√(dm), y_k = log k/√k (2.1);
  ∂e_Λ = 0 by Σ_{d|k}Λ(d) = log k (2.2–2.3). Rigidity: with y = log fixed, e_a ∈ ker ⇔ a∗1 = log ⇔ a = Λ on [1,N] (3.2–3.3).
  Operator version x_{d,m}(F) = Λ(d)/√(dm) τ_{log dm}F (4.1); two-scale deformation (5.1)
  with antidiagonal jet ∂_−(∂e_Λ(r,q;F))|_{1,1} = (𝒜^{raw} − K_−)_{≤N}F (5.4).
  Energy E(r,q;F) = ‖∂e_Λ(r,q;F)‖²: E = 0, ∂_−E = 0, ∂_−²E = 2‖(𝒜^{raw} − K_−)_{≤N}F‖² (6.2–6.3).
- **Claims.** Complex, Δ ⪰ 0, e_Λ in the kernel, rigidity, operator version, normal jet,
  "the energy only sees the square of the jet": PROVED (declared; sustained as identities).
  The claim in §0 that the nullity is a "realization as a null vector of a positive form" with
  F3 selectivity: declared in the body, downgraded by its own header (audit R170_865).
  Green map of the isolated hyperbolic cell (7.3): INADMISSIBLE; of the glued complex: OPEN.
- **Stopping point.** The positive form Δ loses the orientation of the first-order jet (it only
  appears at order two as a square); the incidence Dirac (6.4) keeps orientation but is
  indefinite. Missing a Green map 𝔊_T with 𝔊_T((𝒜^{raw} − K_−)f) = 𝔚_K(f) + Θ_ext(f) (7.3).
- **Corrected by.** R170_864 (Poisson gluing: the jet K_− cancels) and R170_865 (∂ = [B, −I]
  surjective: the kernel is the universal graph y = Bx; the rigidity comes from fixing y = log from outside).
- **Cross-check.** T2: yes, directly — it is a Gram model by divisor incidence (B sums paths
  (d,m) over dm = k); its positive form is ∂^*∂, blind to the weights. T3: yes — the nullity encodes
  Σ_{d|k}Λ(d) = log k, and ∂_−²E is a square; but the square is ‖(𝒜^{raw}−K_−)F‖², of second
  order, unrelated to a_T. T1: partial (translations τ_{log d/r + log m/q} with weights Λ), without a
  useful square. T4: no.

### R170_864 — Glued incidence–Poisson complex
- **Object.** Hyperbolic cell H(r,q) = L(r)S(q) − K(r,q), normal H_− = 𝒜^{raw} − K_−; oriented PC normal
  𝒩_H = −H_−; Poisson–X cell with jet 𝒩_X = −K_− (from {X_r,E}𝓕_r = S𝓜_r − K − JK𝓕_r, (1.3)).
  Gluing: 𝒩_X + 𝒩_H = −𝒜^{raw} (0.4), and reflected −JK_−𝓕 − JH_−𝓕 = −J𝒜^{raw}𝓕 (0.5).
  Complete PC normal 𝒩_{PC} (3.1) = R170_856(3.5); boundary after compression 𝓡_cross + 𝒫^{comb}_{N,T} + B_μP𝒫_{C,A} (3.2).
- **Claims.** All PROVED (ledger identities); "the isolated incidence normal is a
  physical observable": REFUTED; anchor "RETAINED"; null extension of the anchor to the port: OPEN.
- **Stopping point.** The gluing eliminates all of K_− (and K2, Selberg); the correct Green target acts
  on the tuple (𝒩_PC, 𝓡_cross, 𝒫^{comb}, B_μP𝒫_{C,A}) (5.1–5.2), not built.
- **Cross-check.** T2: yes (continues the incidence model; remains as an "exact gluing condition,
  not a terminal positive energy", §4). T4: grazes — the glued normal is that of the complete PC with tails H,
  but without squares. T1, T3: no beyond 863.

### R170_865 — Audit of the incidence anchor
- **Object.** ∂ = [B, −I], (Bx)_k = Σ_{dm=k}x_{d,m}; Ran ∂ = C₀, ker ∂ = {(x,Bx)} (0.2);
  Δ = [[B^*B, −B^*],[−B, I]] (2.1), ∂∂^* = BB^* + I ⪰ I (2.2); pseudoinverse ∂^† = ∂^*(BB^*+I)^{-1} (2.3);
  projector P_{ker∂} = I − ∂^*(BB^*+I)^{-1}∂ (6.1).
- **Claims.** Identities of 863: CORRECT. Surjectivity and universal graph: PROVED.
  "The positivity of Δ selects Λ": FALSE. "Section y = log plus Möbius selects Λ": PROVED
  (only reformulates the uniqueness of a∗1 = log). Algebraic Green: BUILT / WEIGHT-BLIND. Anchor closes
  the port: REFUTED. Projector (6.1): TOOL. Sustained.
- **Stopping point.** Nullity = universal graph; the first jet of ‖v(s)‖² at v(0) = 0 is zero for a
  purely differential reason (4.2); converting the anchor into an exterior anchor is equivalent to 𝔚_K + Θ_ext = 0 (5.1).
- **Corrected by.** R170_866 (header): impose multiplicative compatibility.
- **Cross-check.** T2: yes — it is exactly the failure of incidence as a Gram: the form ∂^*∂ and its
  inverse depend only on the divisor graph, not on Λ. T3: yes — the quadratic bound ‖Bx − y‖² is
  blind; the specificity of Λ enters only through the fixed section. T1, T4: no.

### R170_866 — Multiplicatively compatible null line
- **Object.** 𝒟_N: ℝ^N ⊕ ℝ → ℝ^N, (𝒟_N(a,c))_k = k^{-1/2}(Σ_{d|k}a_d − c log k) (0.1);
  ker 𝒟_N = ℝ(Λ|_{[1,N]}, 1) (0.2); 𝓛_N = 𝒟_N^*𝒟_N ⪰ 0 with a unique null line (0.3).
  U_N a = a∗1 unitriangular, det 1, truncated Möbius inverse (1.1–1.3).
  Energy ‖𝒟_N(a,1)‖² = Σ_{k≤N} |(a∗1)(k) − log k|²/k (4.1), zero ⇔ a = Λ on [1,N] (4.2).
  Tensorization (5.1), kernel ℝ(Λ,1) ⊗ 𝓗 (5.4); normal jet (6.1) = (𝒜^{raw}_{M,N} − K_−)_{≤N}F.
- **Claims.** All PROVED (declared and sustained: triangular linear algebra + μ∗log = Λ).
  Positive extension to the glued PC complex: OPEN.
- **Stopping point.** The first derivative of the energy vanishes on the kernel; the second is the square
  of (6.1): it does not sign the port. The line must be extended to Poisson, reflected, polar and Tate cells.
- **Corrected by.** R170_867–868 (every linear extension factors: only the normal metric changes).
- **Cross-check.** T3: yes, fully — it is literally "total identification of Λ by Σ_{d|n}Λ(d) = log n
  converted into a quadratic form" (4.1), with a nullity that separates Λ from every finite modification (and from
  cΛ, c ≠ 1, up to the rescaling of the column c). It fails because the form lives in the space of
  coefficients (a,c), not in F, and its content in F is only the second-order square of the jet.
  T2: yes (compatible version of the incidence Gram). T1, T4: no.

### R170_867 — PC graph extension of the null line
- **Object.** Homogeneous PC in (a,c): L_a = Σ_{d≤M} a(d)d^{-1/2}τ_{log d}, A_{a,c} = c𝓜 − (L_a + L_a^*),
  H_{a,c} = L_aS_N − cK_N; S_N A_{a,c}𝓕 = c{X,E_N} − L_a^*E_N − JH_{a,c} − H_{a,c}𝓕 (1.3).
  H^{≤N}_{a,c} = V_N(𝒟_N(a,c)), V_N(v) = Σ v_kτ_{log k} (2.3–2.4); residue with tail only
  𝓡_{PC} = 𝒯_{PC}𝒟_N(a,c), 𝒯_{PC}(v) = −JV_N(v) − V_N(v)𝓕 (3.2–3.3).
  Extended Laplacian 𝒟_N^*(I + 𝒯^*𝒯)𝒟_N, kernel ℝ(Λ,1) (0.3–0.4). Prop. 5.1: every extension
  (I; Q)𝒟_N gives 𝒟_N^*(I + Q^*Q)𝒟_N with the same kernel.
- **Claims.** PROVED (sustained). "Factored extension produces a first-order mixed block":
  REFUTED. Non-factored boundary component: NECESSARY / OPEN.
- **Stopping point.** The jet is transported linearly (6.2) but the energy starts again at order two.
- **Corrected by.** R170_868 (closure: such a component is impossible if it is linear in (a,c) and kills the line).
- **Cross-check.** T2/T3: yes — incidence Gram with metric I + Q^*Q; change of metric without sign. T4:
  grazes — 𝒯_{PC} contains the interior block of the PC hyperbola, but only as normal metric. T1: no.

### R170_868 — Universal factor-through theorem
- **Object.** Theorem: ℓ: ℝ^N ⊕ ℝ → Y linear with ℓ(Λ,1) = 0 ⇒ ∃! Q with ℓ = Q𝒟_N (0.5);
  operator version (4.4); linear positive extensions = 𝒟_N^*(I + ΣQ_j^*Q_j)𝒟_N (3.3).
  "Boundary-augmented" way out: domain Ê_N = (ℝ^N⊕ℝ)⊗𝓗 ⊕ B_T, null vector ê_T(f) = ((Λ,1)⊗f, β_T(f)),
  joint cancellation ℓ_ar((Λ,1)⊗f) = −ℓ_bd(β_T(f)) (5.4) and mixed block (5.5).
- **Claims.** Factorization, change of metric, tensor version: PROVED (sustained, first
  isomorphism theorem). Non-factored component in the same space: IMPOSSIBLE. Augmentation by
  boundary: NECESSARY. Construction of β_T: OPEN.
- **Stopping point.** Class NO-GO: every extension linear in (a,c) killing the line is a change of metric.
- **Cross-check.** T2/T3: yes — it is the NO-GO closing the linear use of incidence and of the divisor
  identity as a quadratic form on the coefficient space. T1, T4: no.

### R170_869 — Null line splitting and boundary class
- **Object.** Section σ_N(v) = (U_N^{-1}W_N^{-1}v, 0); x = σ_N(𝒟_Nx) + c(Λ,1) (1.6).
  Every row ℓ = Q𝒟_N + cβ_ℓ, β_ℓ(F) = ℓ((Λ,1)⊗F) (0.2–0.3). Exact sequence
  0 → 𝓘_D → Hom(E,Y) → Hom(𝓗,Y) → 0 (3.3). Physical class β_phys = g_εΔ^{Tate} = 𝔚_K + Θ_ext (0.4).
- **Claims.** Decomposition, classification, quotient: PROVED. β_phys: IDENTIFIED (under REG/C1
  imported from R170_859). "PC/Möbius determine β_phys": REFUTED. "Minimality ⇒ β_phys = 0": OPEN LAW.
- **Stopping point.** The arithmetic fixes the subspace where the class lives, not its value; manipulating only
  the ideal 𝓘_D is circular (§4).
- **Cross-check.** T3: yes (everything deduced linearly from Λ∗1 = log falls into the ideal and is silent about
  the class). T1, T2, T4: not directly.

### R170_870 — Odd boundary class vs even minimality
- **Object.** β_phys linear, odd in F (0.3); minimality Z_T Ḣ_T Z_T ⪯ 0 even (0.2). Lemma 2.1: the dual
  of the whole linear space is {0}. Independence theorem (§4): ℓ_β((a,c)⊗F) = Q𝒟_N(·) + cβ(ZF)
  for any β ∈ Z^*, without changing H_s, radical, tangent cone or arithmetic line.
- **Claims.** Parity, equivalence "one-sided sign ⇔ β = 0", independence: PROVED.
  Minimality + coefficient algebra ⇒ β = 0: REFUTED. Odd coupling or common second radical:
  NECESSARY / OPEN.
- **Textual remark.** §§6–7 are a literal copy of §§6–7 of R170_871 (they mention (3.5) and (4.4),
  which do not exist in 870): editing error.
- **Cross-check.** T1–T4: no; it is the parity wall affecting every linear functional.

### R170_871 — Factor swap exterior cycle
- **Object.** ι(d,m) = (m,d); anchors x^L = Λ(d)/√(dm), x^R = Λ(m)/√(dm), both with column log;
  cycle ω_Λ = x^L − x^R with fibre sum zero and ιω = −ω (1.4–1.6). With P = P_T, Q = I − P:
  PLQSP − PSQLP = −(PLPSP − PSPLP) (0.3), Φ_ext + Φ_int = 0 (3.5); antidiagonal derivative (4.4).
- **Claims.** PROVED (sustained, insertion of I = P + Q into P(LS − SL)P = 0). Odd channel:
  REALIZED / CLASS ALREADY IN R161. Identification with β_phys: PARTIAL. Vanishing by minimality: OPEN.
- **Corrected by.** R170_872 (collision with the support concomitant R161_057/064).
- **Cross-check.** T2: grazes (incidence paths (d,m)). T1, T3, T4: no.

### R170_872 — Factor swap corpus collision
- **Object.** Audit: (0.1) = polarization of the concomitant 𝒦_P(S;g,w) = ⟨Pg,PSQw⟩ − ⟨Qg,SPw⟩ of R161_064(2.2).
  Dictionary table 871 ↔ R161. Operator falsifier: commuting L, S, projection P with PLQSP − PSQLP ≠ 0
  (finite nilpotent shifts).
- **Claims.** Identity correct; new class: NO (collision); "swap/commutativity ⇒ zero
  flux": REFUTED; Tate/exterior reciprocity: OPEN.
- **Cross-check.** T1–T4: no.

### R170_873 — Tate modular cocycle and virial jet
- **Object.** Cocycle 𝐜_n(s) = a_n(e^{su_n}, e^{−su_n}), u_n = log n, a_n = Λ(n)/√n (0.1);
  𝐜_n(1/2) = (Λ(n), Λ(n)/n); 𝐜_n'(0) = Λ(n)log n/√n (1,−1) (0.2); generator A_n = diag(u_n, −u_n).
  Deformed port 𝒥^{ar}_T(s;F) = Σ_{2≤n<e^{2T}} a_n(e^{su_n}R_{n,+}(F), e^{−su_n}R_{n,−}(F)) (3.1),
  plus collar Γ (3.3). Open sufficient identity β_phys(F) = 𝔅_T(ZF, ∂_s𝒥^{full}_T(0;F)) (4.3).
- **Claims.** PROVED on weights/collars; the novelty header says the jet is not a new
  class (R170_845, R161_036/041). Realization as second null vector and (4.3): OPEN.
- **Corrected by.** R170_874 (does not determine the exterior class), R170_876.
- **Cross-check.** T1: yes, partially — arithmetic weights Λ(n)n^{±s} in the dilation parameter
  and virial weight Λ(n)log n/√n; but without a square: A_n has opposite signs (§2). T2–T4: no.

### R170_874 — Modular cocycle quotient no-go
- **Object.** Independent extension lemma: ℰ_β((a,c)⊗F) = (D_N(a,c)⊗F, cβ(F)) (1.2) preserves
  cocycle, jet, line (Λ,1), linear PC and diagonal minimality for every β. Continuation criterion:
  operator 𝒥̂ with 𝒥̂ℰ_phys = ℰ_phys𝒥 and pr_∂𝒥̂ = −1 (3.1–3.2).
- **Claims.** Independence: PROVED; "interior swap determines Θ_ext": REFUTED; criterion:
  FORMULATED; literal extension: OPEN.
- **Corrected by.** R170_876 (the pure involution is incompatible: A_L ↦ A_S).
- **Cross-check.** T1–T4: no.

### R170_875 — Static Tate port typing and falsifier
- **Object.** Type repair 𝔓̂^{ren} = Z_NA_M (0.2). Formula RZ_NA_MF − r_F = (RPZ_Nr_F − r_F)
  + RΔ^R_{N,T}ℓ_F − φ_−a_−(ℓ_F) (1.1). Gram G = Φ^*Φ = 2[[sinh T, T],[T, sinh T]]; explicit
  coordinates (2.1). NUMERICAL falsifier: T = ½log5, ℓ = 0, r = b_+: RZ_Nr ≈ (0.95543, −1.03070) ≠ (1,1) (2.4).
  Wronskian identity gΔ^{Tate} = ρ(κ−1)g + ((q̇,z) − (q,ż)) (3.1).
- **Claims.** Original defect MISTYPED; repair and finite formula: PROVED; static
  equality: REFUTED (by a numerical value, not verified here); sign law: OPEN.
- **Cross-check.** T1–T4: no.

### R170_876 — Full PC factor swap obstruction
- **Object.** σ(L,S) = (S,L) fixes H_L = LS − K but A_L = 𝓜 − (L+L^*) ↦ A_S ≠ A_L (0.2–0.3);
  defect 𝔒_{L,S} = SA_L − LA_S = (S−L)𝓜 + LS^* − SL^* (2.2); derivation −[X,S_N] = K_N^{(1)},
  −[X,L_N] = Σ Λ(n)log n/√n τ (3.1–3.2), Ω_N = K^{(Λ,1)} − K^{(1)} (3.3); jet (4.2); covariant law (5.1).
- **Claims.** PROVED/REFUTED according to table; Ω_N "COMPUTED / CANCELS IN PC" (corrected by 877).
- **Corrected by.** R170_877.
- **Cross-check.** T1–T4: no.

### R170_877 — Swap PC cancellation and extraction obstruction
- **Object.** K_B = −[X,B]; H_{L,S} − H_{S,L} = −D_K (1.5); complete cancellation of D_K and its
  reflection in PC (2.1–2.4); residual even defect (3.2); non-canonical polar variant −𝒫_C(A_L) − 𝒫_C(A_S).
  Theorem: S = I + N_S, L = N_L (Λ(1) = 0), (PL^*P)^m = 0 for m log 2 > 2T, PL^*P not invertible (4.3–4.4).
  Pre-extraction law (5.1): class of ∂_−𝔒 − 𝒫_C(A_L) = −β_phys.
- **Claims.** PROVED (sustained); law (5.1): FORMULATED / OPEN.
- **Cross-check.** T1–T4: no (the asymmetry uses the exact value Λ(1) = 0, an arithmetic datum, without a square).

### R170_878 — Möbius exterior loop for q
- **Object.** M = Σ μ(n)n^{-1/2}τ_{log n}, MS = SM = I; (PS_N^*P)^{-1} = PM^*P (N ≥ e^{2T}) (0.3);
  q_N = QS_N^*PM^*Pb (0.4a) = −QS_N^*QM^*Pb − QU_N^*M^*Pb, U_N = S − S_N (0.4b). Frozen derivative
  q̇ = QṠ_N^*PM^*Pb (2.1); 𝔚_ext = (q̇, z_F) − (q_N, ż_F) (2.3). L = MK by Λ = μ∗log (3.2);
  ℓ_F = Q𝓜F − QMKF − QK^*M^*F + Q(R_M + R_M^*)F (3.5); z_F (3.6).
- **Claims.** All PROVED; sign/vanishing of (2.3): OPEN.
- **Corrected by.** Cutoff headers (truncation L_M, tail U_N; R170_884).
- **Inconsistency.** (3.6) writes +ρ_F QS^*QM^*Pb, which corresponds to the complete-comb formula
  prior to the correction; with (0.4b) it should be +ρ_F(QS_N^*QM^*Pb + QU_N^*M^*Pb) (or the
  equivalent form of R170_884(0.2)). The header says §3 is corrected, but (3.6) is not.
- **Cross-check.** T3: yes, linear — inserts Λ = μ∗log at the operator level (L = MK), not as a quadratic bound;
  the memo warns that separating terms of (3.6) and bounding them would lose the cancellations. T1, T2, T4: no.

### R170_879 — Boundary Möbius divisor law
- **Object.** q_N(t) = Σ_k b(t − log k)k^{-1/2} 𝔪_{N;T,t}(k), 𝔪_{N;T,t}(k) = Σ_{n|k, n≤N, |t−log n|≤T} μ(k/n) (0.2–0.3);
  excluded form 𝔪 = −Σ_{n>N or t−log n∉[−T,T]} μ(k/n) (2.2); boundary operator 𝔅_{N,T} (4.1);
  𝔚_ext = (𝔅̇b, z_F) − (𝔅b, ż_F) (4.2). Sign example: k = 6, divisor windows {6} → +1, {2,3,6} → −1.
- **Claims.** Pointwise expansion, coefficient as a partial Möbius sum, interior/excluded
  equivalence, local finiteness: PROVED. Individual sign of 𝔪: FALSE IN GENERAL. Summation-by-parts
  law with tail and polar: OPEN.
- **Stopping point.** 𝔪 changes sign; term-by-term vanishing is false.
- **Cross-check.** T3: yes, linear — partial Möbius sum on the boundary, without a square. T2: grazes (poset of
  divisors). T1, T4: no.

### R170_880 — Boundary first moment is Mangoldt
- **Object.** 𝔪_{T,t}(k) = Σ_{n|k} μ(k/n) 1_{[log n − T, log n + T]}(t) (0.1); ∫𝔪 dt = 2T·1_{k=1} (0.2),
  ∫t𝔪 dt = 2TΛ(k) (0.3). Interior moment 𝔍_T(k) = ½Σ_{n|k, n<e^{2T}} μ(k/n)(T² − (log n − T)²) (2.4);
  law 𝔈_T(k) = 2TΛ(k) − 𝔍_T(k) (2.2). With cutoff: physical first moment for k > N:
  2TΛ(k) − 2TΣ_{n|k, n>N} μ(k/n)log n (2.8). Ward law (3.1): Σ w(k)𝔈_T + Σ w(k)𝔍_T = 2TΣΛ(k)w(k).
- **Claims.** PROVED (sustained; μ∗1 = δ, μ∗log = Λ). Identification of the weight of the physical
  Wronskian and cancellation of the polar continuum: OPEN.
- **Corrected by.** R170_884 (the physical predictor uses 𝔪_N, with tail).
- **Cross-check.** T3: yes — exact identification of Λ as the first moment of the Möbius incidence;
  identity linear in the weights, without a square. T1, T2, T4: no.

### R170_881 — Affine Mangoldt extraction and shape remainder
- **Object.** ℳ_{T,k}[φ] = ∫𝔪_{T,t}(k)φ(t)dt = 2TaΛ(k) + ℛ_{T,k}[φ;a,c], ℛ = ∫𝔪(φ − at − c) (0.2–0.3).
  Hypothetical disintegration 𝔚_ext + 𝔓_pol = Σ k^{-1/2}ℳ_{T,k}[φ_{F,k}] (3.1) ⇒ Mangoldt channel + shape residue (3.2).
- **Claims.** Affine extraction, definition of the residue: PROVED. "The first moment determines
  general tests": REFUTED (ψ ≥ 0 on an interval of constant sign). Direct application to S_N for
  k > N: REFUTED. (3.1) and (3.3) Σ k^{-1/2}ℛ = 0: OPEN.
- **Cross-check.** T3: yes, linear (extracts Λ from the affine component; the rest, the quotient by span{1,t}, is left free).
  T1, T2, T4: no.

### R170_882 — Log-weighted boundary Möbius Ward law
- **Object.** 𝔩_{N;T,t}(k) = Σ_{n|k, n≤N, |t−log n|≤T} μ(k/n)log n = Λ(k) + 𝔢_{N;T,t}(k) (0.1, 0.4),
  𝔢 = −Σ_{n>N or |t−log n|>T} μ(k/n)log n (0.5); q̇^0 = Q∂_t(Σ Λ(k)k^{-1/2}b(·−log k) + ℰ_{N,T}b) (2.3);
  𝔚_ext = −ΣΛ(k)k^{-1/2}∫b(t−log k)z_F' − ∫ℰ_{N,T}b z_F' − ∫q_N ż_F (3.3);
  route residue 𝔑_route (4.1); pending law 𝔑_route + 𝔓_pol + Θ_Γ = 0 (4.2).
- **Claims.** PROVED (on the core); coefficient-by-coefficient cancellation with the polar:
  REFUTED BY TYPE; identification of the Mangoldt collar with the prime channel of the virial and (4.2): OPEN.
- **Cross-check.** T3: yes, linear (μ∗log = Λ localized in (t,k)); the defects 𝔢 change sign. T4:
  grazes — it is a pairing of the route tail with z_F', but linear in F. T1, T2: no.

### R170_883 — Boundary Dirichlet covariant derivative
- **Object.** Series 𝓜_{N;T,t}(s) = A_{N;T,t}(s)/ζ(s), A = Σ_{n≤N, e^{t−T}≤n≤e^{t+T}} n^{-s} (0.2–0.3);
  𝓛 = (1/ζ)Σ log n n^{-s} (0.4); ∇_ζ = ∂_s + ζ'/ζ, 𝓛 = −∇_ζ𝓜 (0.6); series of excluded routes
  (2.3–2.4); polar continuum c_N(s) = N^s/s (3.2); A^{cont} (3.3–3.4); sum–continuum defect 𝒟_{N;T,t} = A − A^{cont} (3.5).
- **Claims.** PROVED in Re s > 1 (sustained; continuation is not used). Type comparison with
  the polar continuum: PROVED. Transformed identification §4 and sign: OPEN.
- **Cross-check.** T3: yes, linear (generating-function reformulation of μ∗log = Λ). T4: grazes — (3.5) is the
  sum–continuum defect, but without a square. T1, T2: no.

### R170_884 — Finite cutoff and continuous polar audit
- **Object.** Correction S → S_N: q_N = −QS^*QM^*Pb − QU_N^*PM^*Pb (0.2); physical incidence and
  moments with tail (1.2–1.4); finite logarithmic Ward law (2.2–2.3); polar C_N = ∫_0^N x^{-1/2}τ_{log x}dx,
  continuous coefficients 𝔠_{N;T,t}(y) = Σ_{m, y/m≤N, |t−log(y/m)|≤T} μ(m)/m (3.3); minimal residue 𝔑_min (4.1).
- **Claims.** PROVED; polar/discrete coefficient-by-coefficient cancellation: REFUTED (type);
  paired Euler–Maclaurin identity: OPEN.
- **Note.** (0.2) and R170_878(0.4b) are two equivalent forms of the same identity (checked:
  both come from QS^*M^*Pb = 0 decomposed differently); there is no contradiction.
- **Cross-check.** T4: yes, in the sense of identifying the location — discrete comb vs polar continuum with
  tails U_N and R_M; converts nothing into squares. T3: linear. T1, T2: no.

### R170_885 — Exact Euler–Maclaurin Wronskian port
- **Object.** W(u,v) = (u̇,v) − (u,v̇); Z_N = S_N − C_N; identity 𝔚_ext + (h, P𝒫_{C,A_M}F) =
  W(QZ_N^*h, ℓ) − W(PC_N^*h, r) (0.2). Discrete–continuous disintegration QZ_N^*h = Q[Σ_k b(t−log k)k^{-1/2}m^d_N(k,t)
  − ∫ b(t−log y)y^{-1/2}c_N(y,t)dy] (2.3), logarithmic analogue (2.6); separation
  (QZ_N^*h)˙ = Q∂_t[L_M^*b + R_M^*b + ℰ_{N,T}b − 𝓛^{cont}_{N,T}b] (3.1). Falsifiers of algebraic
  closure: multiplier Σ_{n≤N}n^{-s} − N^{1−s}/(1−s) ≢ 0 (4.1); for t < −T, QS_N^*h = 0 but
  C_N^*h(t) = e^{t/2}∫e^{-u/2}h ≠ 0 (4.2). Residue 𝔑_EM (5.2–5.3).
- **Claims.** PROVED (sustained algebraically); algebraic vanishing of the renormalized
  predictor: REFUTED; sign via minimality: OPEN.
- **Cross-check.** T4: yes — it is the Euler–Maclaurin version of the mixed comb/continuum pairing (Z_N) with
  tails, written as a Wronskian (alternating form, linear in F); there is no h(k)|ℓ_k(F)|². Recorded
  failure: Z_N is not zero and the Wronskian has no sign of its own. T3: linear. T1, T2: no.

### R170_886 — Euler–Maclaurin anchor range law
- **Object.** Anchor e_EM = q_N − C_N^*h; 𝔚_ext + (h,P𝒫_{C,A_M}F) = W(e_EM, A_MF) (0.2); representative
  ω_EM = Π_{𝒫_T}(A_M^*ė_EM − Ȧ_M^*e_EM) (0.3), operator form (2.4); exterior law ⇔ ω_EM ∈ cl Ran H_T
  (3.1); Poisson equation H_Tg_EM = ω_EM (3.2, 5.1); sufficient factorization (5.2).
- **Claims.** Fusion, representative, equivalence: PROVED. "Strictly new reduction":
  NO (Fredholm criterion, self-corrected in the header). Quadratic minimality ⇒ range: REFUTED.
  Arithmetic construction of g_EM: OPEN.
- **Corrected by.** R170_887 (connection of the moving branch), R170_889 (validated).
- **Cross-check.** T4: grazes (same object as 885). T1–T3: no.

### R170_887 — Covariant EM anchor and minimality audit
- **Object.** e_s = Q_sS^*_{N,s}h_s − C^*_{N,s}h_s; de/ds = ė_fr + χ_e, χ_e = −ṖS_N^*h + (QS_N^* − C_N^*)ḣ (0.2–0.4);
  𝔚_cov = W_fr(e_EM, A_MF) + (χ_e, A_MF) − (e_EM, A_MḞ) (0.5); Pḣ = B^{-1}P(ḃ − Ḃh) (1.3);
  invariant Wronskian W_∇ (2.6); Hellmann–Feynman ν = Re(F,ȦF) + 2Re(AF, Π̇F) ≤ 0 (3.2);
  parity wall ν(−F) = ν(F), 𝔚_cov(−F) = −𝔚_cov(F) (4.1–4.2).
- **Claims.** PROVED (some under REG/C1); sign of a linear functional by minimality: REFUTED
  BY PARITY; covariant law (5.1): OPEN.
- **Cross-check.** T1–T4: no.

### R170_888 — Z_N minimality ledger and parity wall
- **Object.** P Ȧ_MF = 𝒷_NP(Z_NȦ_M − Ż_NA_M)F + 𝒷_NP𝒫_{C,A_M}F + 𝒫^{comb}_{N,T}(F), 𝒷_N = (PS_NP)^{-1} (0.2);
  ledger ν = four lines ≤ 0 (0.3), only the sum is gauge invariant; imported finite-collar
  version (λ_δ − λ_0)⟨F_δ, E_δF⟩ = ⟨ξ^δ_F, F_δ|_{C_δ}⟩ (4.1).
- **Claims.** Ledger: PROVED UNDER REG/C1; sign of the linear EM residue: REFUTED BY PARITY;
  identification 𝔑_EM = λ̇: REFUTED; odd lifting to the finite identity: OPEN.
- **Cross-check.** T1–T4: no. (It is the only expression quadratic in F in the stretch, but it is the derivative of the
  eigenvalue, with sign inherited from minimality, not a sum of squares.)

### R170_889 — Double neutral audit of the EM chain
- **Object.** Double-check protocol and classification of objections (A–E). Gauge counterexample
  in ℝ²: rotation with U̇e₁ = e₂, U̇e₂ = −e₁ makes W(Ue, Uv) = 2 with W(e,v) = 0.
- **Claims.** 886(0.2) validated (NUMERICAL check declared on 300 finite matrix
  models); range criterion = Fredholm; 887 validated with gauge correction; 888 validated under
  hypotheses; covariant law: OPEN.
- **Cross-check.** T1–T4: no.

### R170_890 — Tate quadratization and correct moving coordinate
- **Object.** ρ(F) = (a,F); ρΩ_EM = (F, K_EM F), K_EM = (a⊗ω + ω⊗a)/2, rank ≤ 2 (0.3); physical coordinate
  σ_ε(F) = 2Re(Π̇F, b_ε) = −2Re(F, t b_ε') (1.1), defect 𝔑_Tate = Δσ_ε (1.3); eigenvalues
  ((a,ω) ± ‖a‖‖ω‖)/2 (2.1); finite counterexample in basis (e₁,e₂,b) (3.1–3.4): ρΩ = xy of both signs;
  normal Tate energy ρβ = ½D‖r‖² − … (4.2).
- **Claims.** PROVED; sign from minimality: REFUTED (counterexample verified on reading:
  Π(A₀+sV)Π = −sI and Ω(F) = y); signed ρ–σ–Ω relation: OPEN.
- **Cross-check.** T1–T4: no. (Quadratizes a linear functional by the product of two functionals: a form of
  rank two, indefinite except under collinearity.)

### R170_891 — ρ/σ Gram and prime node separation
- **Object.** b_ε = e^{−t/2} + εe^{t/2}, g_ε = 4(sinh T + εT); a_ε = g_ε^{-1}Π_εPA_Mb_ε, s_ε = −2Π_ε(t b_ε') (0.3–0.4);
  det G(a_ε, s_ε) by (2.4) with d = 2(T cosh T − sinh T), E = T² sinh T − 2T cosh T + 2 sinh T − εT³/3;
  separation by the node x₀ = T − log 2 (jumps ℓ₂b_ε(T), ℓ₂b_ε'(T), possible collision with d' = e^{2T}/2) ⇒ det G > 0 for T > ½log 2 (0.5).
- **Claims.** Representatives and Gram: PROVED; primitive independence: PROVED TWICE (regularity
  argument: P𝓜b_ε smooth in the interior, Π_εḃ_ε analytic; sustained in outline); independence after
  projection to the radical: OPEN / FALSE IN DIM 1.
- **Cross-check.** T1–T4: no (Gram of two vectors; the node of 2 is an arithmetic datum, without the sign of a_T).

### R170_892 — Bordered KKT and Tate virtual work
- **Object.** Lagrangian 𝓛_s = ½(F,A_sF) + α(F,b_s) + β/2(‖F‖² − 1); linearized KKT system (1.3);
  2Re(Π̇F, Δb) = σΔ (2.2), block [[0,½],[½,0]] of signature (1,1) (2.4); Schur −(y, H_𝒯^{-1}y) (3.4);
  counterexample in ℝ² with moving constraint: σΔ = −2κδ of either sign (4.6).
- **Claims.** PROVED / PROVED UNDER SIMPLE/REG; "KKT signs σΔ": REFUTED BY COUNTEREXAMPLE;
  Ω_EM,cov = gΔ_tot and stabilization in N: OPEN. The memo declares that the independent audit could not
  be run and did not replace it with acceptance.
- **Cross-check.** T1–T4: no.

### R170_893 — Exact polar normalization defect
- **Object.** Ω_EM := 𝔚_ext + (h, P𝒫_{C,A_M}F); gΔ^{Tate} − Ω_EM = ρ[(ḃ^0,b) − g] − (h,P𝒫_{C,A_M}F) (0.4);
  Ω_EM = gΔ ⇔ (h,P𝒫_{C,A_M}F) = ρ[(ḃ^0,b) − g] (0.5, "polar normalization law"); literal expansion (2.1);
  typed virtual work σΔ = (σ/g)[Ω_EM + ρ((ḃ^0,b) − g) − (h,P𝒫F)] (4.1).
- **Claims.** PROVED (algebra from R170_856(8.4)); law (0.5): OPEN.
- **Cross-check.** T1–T4: no.

### R170_894 — Polar moment residual and moving face
- **Object.** With N ≥ e^{2T}: α(f) = ∫_I e^{u/2}f, β(f) = ∫_I u e^{u/2}f, H₀, H₁ (0.1–0.2);
  (h,PC_Nf) = H₀α(f), (h,PĊ_Nf) = (H₀ − H₁/2)α(f) + (H₀/2)β(f) (0.3–0.4); exterior moments
  𝖷_N(v), 𝖣_N(v) with moving face −(log N)√N v(t + log N) (2.3); minimal polar residue 𝔑_pol (3.2).
  Abstract independence: vary Qv with 𝖷_N(v) ≠ 0 keeping the interior datum (§4).
- **Claims.** PROVED; "interior first contact ⇒ 𝔑_pol = 0": REFUTED IN THE ABSTRACT; arithmetic
  identity of the moving face: OPEN.
- **Cross-check.** T4: grazes (face t + log N = cutoff boundary of the comb/continuum), linear. T1–T3: no.

### R170_895 — Integer jump EM collar balance
- **Object.** N(T) = e^{2T}, T_n = ½log n; anchor a_T = Q_TZ^*_{N(T)}h_T; balance of measures in T:
  D_Ta_T = −Ṗ_TZ_N^*h_T + Q_TΣ_n n^{-1/2}τ_{−log n}h_T δ_{T_n} − 2√N Q_Tτ_{−log N}h_T dT + Q_TZ_N^*D_Th_T (0.2);
  d_NZ_N = Σ n^{-1/2}τ_{log n}δ_n − N^{-1/2}τ_{log N}dN (1.2); D_Th_T (2.2), Ṗ_Tf = f(T)δ_T + f(−T)δ_{−T} (2.3);
  jump [a_T]_{T_n} = Q_{T_n}n^{-1/2}τ_{−log n}h_{T_n} (3.1); Möbius insertion (4.1) and fibres (Λ∗μ)(r) (4.2).
- **Claims.** PROVED; "automatic algebraic conservation": REFUTED; law of measures cancelling
  the balance: OPEN. The reading (4.2) with Λ∗μ was corrected by R170_896 (unnecessary composition).
- **Cross-check.** T4: grazes — integer/continuous Euler–Maclaurin balance, linear; T3: linear (Möbius). T1, T2: no.

### R170_896 — Exact Möbius extraction of cutoff measure
- **Object.** K = Σ log d d^{-1/2}τ_{log d}, M (Möbius), L (Mangoldt); K(d_NZ_N)M = L(d_NZ_N) (0.1) by
  Σ_{dm=r} log d μ(m) = Λ(r); expansion (1.2–1.3); adjoints [K dZ M]^* = (dZ)^*L^* (1.4); forbidden to
  insert P or Q between factors (§2). Comparison: the dilation Wronskian carries
  −Λ(r)log(r/n)∂_tτ_{log nr} (3.2), which (0.1) does not give.
- **Claims.** PROVED (sustained; commutativity in the causal algebra); "coincides with the
  degree-one virial channel": FALSE; antidiagonal lifting: OPEN (solved algebraically in 897).
- **Cross-check.** T3: yes, linear — exact extraction of Λ in the cutoff measure (degree zero), without
  quadratic conversion. T1: grazes (translations in the dilation with weight Λ(r)). T2, T4: no.

### R170_897 — Antidiagonal lift of cutoff measure
- **Object.** δτ_{log a} = log a ∂_tτ_{log a}, E = d_NZ_N; 𝔚_ad(E) = (δL)E − L(δE) = (δK)EM + KE(δM) − K(δE)M (0.2);
  atomic part Σ_{n,r} Λ(r)log(r/n)(nr)^{-1/2}∂_tτ_{log nr}δ_n (0.3) by Σ_{dm=r} μ(m)[(log d)² + log d log m] = Λ(r)log r (2.2);
  δM = −M(δS)M (3.1); continuous part Σ_r Λ(r)log(N/r)(Nr)^{-1/2}∂_tτ_{log Nr}dN (4.2).
- **Claims.** PROVED (sustained, Leibniz rule); "degree-one prime virial channel CLOSED
  ALGEBRAICALLY"; Γ/adjoint/tail/Tate assembly: OPEN.
- **Cross-check.** T3: yes, at degree two, linearly (the degree-two Leibniz relation on Λ∗1 = log, which
  OBJECT_SPEC O2 already identifies), without a square in F. T1: grazes (arithmetic weights in the
  dilation derivation). T2, T4: no.

### R170_898 — Finite integrated cutoff Wronskian
- **Object.** Physical convention τ̇_{log a} = −log a ∂_tτ_{log a}; 𝒲_{M,N} = L̇_MZ_N − L_MŻ_N (0.3);
  d_N𝒲 = 𝓘_{M,N} (0.4) with 𝓘^{at} = Σ_n Σ_{r≤M} Λ(r)log(n/r)(nr)^{-1/2}∂_tτ_{log nr}δ_n,
  𝓘^{cont} = Σ_{r≤M} Λ(r)log(r/N)(Nr)^{-1/2}∂_tτ_{log Nr}dN (0.5); law integrated from N = 1:
  𝒲_{M,N} = 𝒲_{M,1} + ∫_{(1,N]}𝓘, 𝒲_{M,1} = L̇_M(I − C_1) + L_MĊ_1 (0.6), or (0.7) with the atom n = 1 included;
  C_1, Ċ_1 explicit (2.1–2.2), Ċ_N integrated with moving face (2.5); 𝖷_N, 𝖣_N from N = 1 (4.1–4.2).
- **Claims.** PROVED; passage to the infinite prime comb: NOT JUSTIFIED (series ΣΛ(r)/r divergent in
  LC_Nf); assembly: OPEN.
- **Cross-check.** T4: grazes — finite law of the comb–continuum Wronskian with tails, linear. T1: grazes. T2, T3: no.

### R170_899 — Finite polar Green assembly
- **Object.** 𝒢_B(N) = ḂC_N − BĊ_N; 𝒫_{C,A_M}(N) = 𝒢_𝓜(N) − 𝒢_{L_M}(N) − 𝒢_{L_M^*}(N) (0.2);
  𝒢_B(N) = 𝒢_B(1) + ∫_1^N[Ḃ dC_x − B dĊ_x] (2.1); Γ block 𝒥_Γ(x) = x^{-1/2}τ_{log x}[𝓜̇ + (log x)𝓜∂_t] (3.2);
  𝒥_+(x) = Σ_{r≤M} Λ(r)log(x/r)(rx)^{-1/2}∂_tτ_{log rx} (4.1), 𝒥_−(x) = Σ Λ(r)log(xr)(rx)^{-1/2}∂_tτ_{log(x/r)} (4.2);
  normalization residue 𝔑^{M,N}_pol (5.2–5.3); typed residue 𝔑_rem = Re(h,P[𝒢_𝓜 − 𝒢_{L_M^*}]F) − ρRe[(PṠ_N^*Ph,b) − g] (7.2);
  𝒜^{ren} = 𝒜^{raw} − 𝒢_{L_M} (7.3).
- **Claims.** PROVED; finite residue: EXPLICIT; vanishing or sign: OPEN.
- **Remark.** (4.4) defines 𝓑_1 = 𝒫_{C,A_M}(1), but in (5.3) "Re(h,P𝓑_1F) + ρg" appears, and the
  ρg comes from −ρ(−g); consistent. The claim "Ṡ_N^* = Σ log n n^{-1/2}∂_tτ_{−log n}" (5.1) uses the
  sign of the physical convention for negative translations; coherent with (4.2).
- **Cross-check.** T1: grazes (weights Λ(r)log(x/r) in the dilation, without a square). T4: grazes (polar
  comb/continuum assembly, linear). T2, T3: no.

### R170_900 — PC–Tate collision audit
- **Object.** 𝒢_𝓜(C_N) − 𝒢_{L_M^*}(C_N) = 𝒞_PC + 𝒜^{raw} − 𝒢_{A_M+L_M}(Z_N), 𝒞_PC = S_NȦ_M − Ṡ_NA_M (0.1);
  𝒟_PC = 𝒞_PC + 𝒜^{raw} expanded (1.1) with H_{M,N} = Σ_{N<k≤MN} h_{M,N}(k)k^{-1/2}τ_{log k} (1.3);
  𝔑_rem = Re(h,P[𝒟_PC − 𝒢_{A_M+L_M}(Z_N)]F) − ρRe[…] (1.2) and collision form (2.2) with factor 2 in
  −2ρRe(ḃ^0, b), mandatory unless a tangency law (not proved) holds.
- **Claims.** Identity (0.1): PROVED (checked in two ways); new logical reduction: NO;
  tangency: NOT PROVED; sign/vanishing: OPEN.
- **Cross-check.** T4: yes, in the sense that the final residue literally keeps H_{M,N} (tails
  N < k ≤ MN) and the mixed PC pairings, but only as a functional linear in F; there is no
  conversion to Σ h(k)|ℓ_k(F)|². T1–T3: no.

---

## 2. Synthesis

### (a) Reusable PROVED pieces
1. Unique null line of the multiplicatively compatible incidence: ker 𝒟_N = ℝ(Λ,1),
   ‖𝒟_N(a,1)‖² = Σ_{k≤N}|(a∗1)(k) − log k|²/k — R170_866 §§1–4.
2. Universal graph and gluing projector P_{ker∂} = I − ∂^*(BB^*+I)^{-1}∂ — R170_865 §§1–2, §6.
3. Universal factorization theorem ℓ(Λ,1) = 0 ⇒ ℓ = Q𝒟_N; linear positive extensions = change of metric — R170_868 §§1–4; decomposition ℓ = Q𝒟_N + cβ_ℓ and exact sequence — R170_869 §§1–3.
4. Homogeneous PC in (a,c) and H^{≤N}_{a,c} = V_N(𝒟_N(a,c)) — R170_867 §§1–3.
5. Incidence–Poisson gluing: 𝒩_X + 𝒩_H = −𝒜^{raw} — R170_864 §2.
6. Cut identity PLQSP − PSQLP = −(PLPSP − PSPLP) — R170_871 §3.
7. Tate cocycle 𝐜_n(s) and jet Λ(n)log n/√n — R170_873 §§1–3.
8. Physical swap defect SA_L − LA_S = (S−L)𝓜 + LS^* − SL^*; PC cancellation of D_K; PL^*P nilpotent (Λ(1) = 0) — R170_876 §2, R170_877 §§1–4.
9. (PS_N^*P)^{-1} = PM^*P (N ≥ e^{2T}) and Möbius loop of q_N — R170_878 §1, R170_884 §0.
10. Pointwise expansion of q_N with 𝔪_{N;T,t}(k) — R170_879 §1; moments ∫𝔪 = 2Tδ_{k1}, ∫t𝔪 = 2TΛ(k), formula of the interior moment — R170_880 §§1–2; affine extraction — R170_881 §1.
11. Logarithmic Ward law 𝔩 = Λ + 𝔢 and q̇^0 — R170_882 §§1–2, R170_884 §2; Dirichlet series 𝓜 = A/ζ, 𝓛 = −∇_ζ𝓜 (Re s > 1) — R170_883 §§1–2.
12. Euler–Maclaurin identity 𝔚_ext + (h,P𝒫_{C,A_M}F) = W(QZ_N^*h,ℓ) − W(PC_N^*h,r) = W(e_EM, A_MF) and discrete–continuous disintegration — R170_885 §§1–3, R170_886 §§1–2.
13. Total derivative of the EM anchor and covariant Wronskian W_∇ — R170_887 §§1–2; Z_N ledger of ν (under REG/C1) — R170_888 §1.
14. Gram of (a_ε, s_ε) and det > 0 for T > ½log 2 — R170_891 §§1–3.
15. Difference gΔ^{Tate} − Ω_EM = ρ[(ḃ^0,b) − g] − (h,P𝒫F) — R170_893 §1; interior/exterior polar moments — R170_894 §§1–2.
16. Cutoff measure d_NZ_N, balance (0.2) and integer jumps — R170_895 §§1–3; K(d_NZ_N)M = L(d_NZ_N) — R170_896 §1; antidiagonal lifting with Λ(r)log(r/n) — R170_897 §§1–4; finite integrated law 𝒲_{M,N} from N = 1 — R170_898 §§1–2, §4; decomposition 𝒫_{C,A_M} = 𝒢_𝓜 − 𝒢_{L_M} − 𝒢_{L_M^*} — R170_899 §§1–4; identity (0.1) of R170_900.

### (b) Closures (class and falsifier)
1. **Free incidence as a selecting positive form** — class: Laplacian ∂^*∂ of ∂ = [B,−I]; falsifier: ker = universal graph, every a gives a null vector with y^a (R170_865).
2. **Linear extensions of the null line** — class: rows linear in (a,c) killing (Λ,1); NO-GO: they factor through 𝒟_N and only change the normal metric (R170_867 Prop. 5.1, R170_868).
3. **Determination of the boundary class by PC/Möbius/cocycle/minimality** — class: factored identities + even minimality; falsifier: augmented model ℓ_β with arbitrary β (R170_869 §3, R170_870 §4, R170_874 §1).
4. **One-sided sign of a linear functional on the radical** — class: quadratic minimality; NO-GO by parity (Lemma 2.1 of R170_870; R170_887 §4; R170_888 §3).
5. **Swap / commutativity ⇒ zero exterior flux** — falsifier: finite nilpotent shifts (R170_872 §4).
6. **Pure involution of the swap in the physical port** — falsifier: A_L ↦ A_S ≠ A_L (R170_876); symmetric extraction impossible: PL^*P nilpotent (R170_877 §4).
7. **Static Tate port R Z_NA_MF = r_F** — NUMERICAL falsifier at T = ½log5: (0.95543, −1.03070) ≠ (1,1) (R170_875 §2).
8. **Term-by-term sign of 𝔪 or 𝔢** — falsifier: k = 6, divisor windows {6} → +1, {2,3,6} → −1 (R170_879 §3).
9. **First moment determines general tests** — falsifier: ψ ≥ 0 on an interval of constant sign of 𝔪 (R170_881 §2).
10. **Polar/discrete coefficient-by-coefficient cancellation** — type error: comb in k vs continuum in y (R170_882, R170_883 §3, R170_884 §3).
11. **Algebraic closure Z_N = 0** — falsifiers: multiplier Σ_{n≤N}n^{-s} − N^{1−s}/(1−s) ≢ 0 and C_N^*h ≠ 0 for t < −T (R170_885 §4).
12. **Range equation as a new reduction** — it is the Fredholm criterion (R170_886, R170_889 B).
13. **Quadratization ρΩ_EM signed by minimality** — counterexample in ℝ³ with ρΩ = xy (R170_890 §3).
14. **KKT signs σΔ** — counterexample with moving constraint σΔ = −2κδ (R170_892 §4).
15. **Interior first contact ⇒ 𝔑_pol = 0** — abstract independence of the exterior block (R170_894 §4).
16. **Automatic algebraic conservation of the anchor** (R170_895); **degree-zero coincidence with the virial** (R170_896 §3).
17. **Gauge-invariant ordinary Wronskian** — rotation counterexample in ℝ² (R170_889 §2).

### (c) Explicitly open, with exact obstacle
1. Positive extension of 𝓛_N to the glued PC complex with nullity one in the arithmetic coordinate and boundary = combined port (R170_866 §7); obstacle: R170_868 forces leaving the space (a,c) or linearity, with joint cancellation ℓ_ar((Λ,1)⊗f) = −ℓ_bd(β_T(f)) (5.4) and mixed block (5.5).
2. Boundary class law: β_phys|_{ker H_T} = 0 (R170_869 §5, R170_870 §7, R170_871 (7.1)); obstacle: β odd, minimality even; an odd coupling or a common second radical is needed.
3. Positive mixed identity (4.3) of R170_873 from PC-ren with Tate in the position of R161_064(1.1).
4. Exterior naturality: operator 𝒥̂ with (3.1)–(3.2) of R170_874; replaced by the covariant law 𝒥̂ℰ_L(F) − ℰ_S(𝒥̂F) = Γ_{L,S}(F) (R170_876 (5.1)) and the pre-extraction law: class of ∂_−𝔒 − 𝒫_C(A_L) = −β_phys (R170_877 (5.1)).
5. Sign/vanishing of the exterior Wronskian in Möbius blocks (R170_878 (2.3)); summation-by-parts identity on the divisor poset with tail R_M and polar continuum (R170_879 §4).
6. Coefficient-by-coefficient physical disintegration (R170_881 (3.1)) and vanishing of the shape residue Σ k^{-1/2}ℛ_{T,k} = 0 (3.3).
7. Identification of the Mangoldt collar with the prime channel of the virial and 𝔑_route + 𝔓_pol + Θ_Γ = 0 (R170_882 (4.2)); version transformed in s (R170_883 §4).
8. Paired Euler–Maclaurin identity in the minimal residue (R170_884 (4.1)); arithmetic construction of g_EM with H_Tg_EM = ω_EM (R170_886 (5.1)–(5.2)); covariant law (R170_887 (5.1)); odd lifting to the finite collar identity (R170_888 §4).
9. Signed ρ–σ–Ω relation on the radical (R170_890); independence after projection to the radical (R170_891 §4, false in dimension 1).
10. Ω_EM,cov = gΔ_tot and stabilization in N of all ports (R170_892 §5).
11. Polar normalization law (h,P𝒫_{C,A_M}F) = ρ[(ḃ^0,b) − g] (R170_893 (0.5)); obstacle: two exterior moments 𝖷_N(QȦ_MF), 𝖣_N(QA_MF) with moving face not determined by the interior datum (R170_894 (3.3)).
12. Law of measures in T cancelling the balance (R170_895 §5); Γ/adjoint/tail/Tate assembly (R170_897–899); vanishing of the finite residue (R170_899 (5.3), (7.2)); tangency law removing the factor 2 in (2.2) of R170_900.

### (d) What in this stretch already walks T1–T4, with reason for failure
- **T2 (divisor incidence as Gram).** R170_863 (complex ∂ = [B,−I], Δ = ∂^*∂), R170_865 (audit),
  R170_866 (compatible version 𝒟_N with unitriangular U_N), R170_867–868 (extensions). Reasons: (i) with
  free coordinates the positive form is universal and blind to the weights (graph y = Bx, pseudoinverse
  depending only on the graph); (ii) with multiplicative compatibility, the form ‖𝒟_N(a,c)‖² lives in the space
  of coefficients and only says a = Λ; (iii) its content in F is the energy ‖∂e_Λ(r,q;F)‖², whose first
  jet is zero for a differential reason and whose second jet is ‖(𝒜^{raw} − K_−)_{≤N}F‖², which loses the
  orientation; (iv) gluing with the Poisson cell cancels K_− and leaves −𝒜^{raw} (R170_864); (v) every
  linear extension preserving the line is a change of metric (R170_868). The factorization
  [log gcd(i,j)] = E diag(Λ)Eᵀ itself is not used: the Gram used is BB^* + I or 𝒟_N^*𝒟_N, not the gcd matrix.
- **T3 (Σ_{d|n}Λ(d) = log n converted into a quadratic form).** R170_866 (4.1) is literally
  Σ_k |(a∗1)(k) − log k|²/k, zero only at a = Λ; it fails by (ii)–(v) above. Also, as linear
  uses: R170_878 (L = MK), R170_879–884 (μ∗1 = δ, μ∗log = Λ on the boundary, moments, Ward), R170_883
  (Dirichlet series), R170_896 (K dZ M = L dZ), R170_897 (degree-two Leibniz). Common reason: everything
  deduced linearly from the identity falls into the factored ideal 𝓘_D (R170_869) and is silent about
  the boundary class; the boundary coefficients 𝔪, 𝔢 change sign (R170_879 §3); the first moment
  does not determine general tests (R170_881 §2).
- **T1 (continuous squares with arithmetic in the dilation).** Only grazes: R170_873 (cocycle
  Λ(n)n^{±s}, generator diag(log n, −log n) of opposite signs), R170_897–899 (weights Λ(r)log(r/n),
  Λ(r)log(x/r), Λ(r)log(xr) in the dilation derivation). In no case is a square formed; the
  objects are alternating Wronskians or linear jets. There is no reason for failure of T1 properly speaking:
  T1 is not tried.
- **T4 (mixed PC pairings → Σ_{k>N} h(k)|ℓ_k(F)|²).** R170_885–886 (Euler–Maclaurin Z_N = S_N − C_N),
  R170_894–895, R170_898–900 (moving face t + log N, integer jumps, integrated law, H_{M,N} with
  N < k ≤ MN preserved in the final residue (R170_900 (1.2)–(1.3))). Everything is written as a functional
  LINEAR in F (Wronskians and moments) and its fate is fixed by the parity wall (R170_870, R170_887 §4,
  R170_888 §3): a linear functional does not inherit a sign from minimality. The conversion to a
  sum of squares with weight h(k) ≥ 0 is never attempted; the T4 route in the strict sense is not walked in this stretch.

### (e) Inconsistencies or errors seen
1. R170_870 §§6–7 are a literal copy of R170_871 §§6–7 (they cite (3.5), (4.4) and the swap L ↔ S, nonexistent in 870).
2. R170_878 (3.6): the term +ρ_F QS^*QM^*Pb does not incorporate the cutoff correction of its own
   header; with (0.4b) it should be +ρ_F(QS_N^*QM^*Pb + QU_N^*M^*Pb). Moreover "M" denotes both the
   Möbius comb and the cutoff index of L_M in the same memo.
3. R170_863 §3 presents the rigidity as "exact" F3 selectivity; its own header (R170_865)
   downgrades it to an external fixing of y = log. The label in the body is not corrected, only annotated.
4. R170_876 declares Ω_N as a derivation defect; R170_877 proves that it cancels in PC; 876 notes it
   in the header and in its table ("CANCELS IN PC"). Coherent after correction.
5. R170_895 (4.2) reads fibres Λ∗μ; R170_896 corrects it (the correct composition is K dZ M).
6. R170_875 (2.4) and R170_889 (300 models) support claims with NUMERICAL checks not reproduced in the text.
7. R170_892 declares that one of its two reviews could not be run; the label "audited twice"
   in the title is therefore stronger than what the text describes.
8. R170_884 (0.2) and R170_878 (0.4b) look different but are equivalent (two decompositions of QS^*M^*Pb = 0); not an error.

### (f) Files read (complete reading with Read, each one to its last line)
R170_863, R170_864, R170_865, R170_866, R170_867, R170_868, R170_869, R170_870, R170_871, R170_872,
R170_873, R170_874, R170_875, R170_876, R170_877, R170_878, R170_879, R170_880, R170_881, R170_882,
R170_883, R170_884, R170_885, R170_886, R170_887, R170_888, R170_889, R170_890, R170_891, R170_892,
R170_893, R170_894, R170_895, R170_896, R170_897, R170_898, R170_899, R170_900 — 38 files, all complete.
