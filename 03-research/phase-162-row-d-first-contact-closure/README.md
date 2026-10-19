# Phase 162 — Row D: the first-contact closure

at the request, after the readability revision of Paper 47.

## Target (reformulation)

Gate 0 (first contact). Remove the continuity hypothesis of Paper 47 lem:firstcontact.
Gate 1 (arithmetic). For a primitive parity first-contact vector F (H_{T_*}F=0 at the first window
T_* where λ_A vanishes), prove directly from (PC-ren)

    R_L F = 0     (equivalently K_F(a_m)=0 for the Gamma lattice a_m=2m+1/2),

using essentially: (i) minimality of T_*; (ii) the causal Poisson–Tate orientation; (iii) Λ*1=log
at the step that forces vanishing; (iv) all collars, polar terms and Tate endpoints.

Known equivalences (Paper 47 §firstcontact): R_LF=0 ⟺ ⟨F,Δ_{N,L}F⟩≤0 ⟺ Q_{N,L}(F)≥0 on the radical;
the two-channel inequality ‖x‖²≤Re⟨x,j⟩ ⟺ x=0. The contraction q_0<0.236 is not a closing mechanism.

## Mandatory falsifier tests for any Gate 1 argument

- F1 (spectral). Q<0 on every eigenvector with λ>0 (R161_081 (2.1)); an argument that does not use
  λ=0 and the minimality of T_* non-perturbatively proves a falsehood.
- F2 (orientation). The square of (PC) is invariant under A_M→−A_M (R161_099 §2); no quadratic
  estimate of (PC) alone orients the sign.
- F3 (arithmetic). The step forcing vanishing must fail for a≠Λ with Λ*1≠log (Paper 47 thm:finmod)
  and for Epstein/Davenport–Heilbronn data (functional equation, no Euler product).
- F4 (linear limit). A linear (PC-ren) graph limit cannot prove port vanishing (R161_018).

## Files

- R162_001 — continuity of λ_A (Gate 0): PROVED (R162_190), integrated in Paper 47 as lem:contA.
- R162_101–103 — round 1 fronts: three NO-GOs. R162_199 — synthesis. Gate 1 OPEN.
- R162_201 — round 2: a new sufficient criterion for the global Sonin range. Uniform boundedness of
  the finite Euler-stripped ports `A_Y e^{Tz}G_+^0` in `H2(C_+)` forces every critical jet, hence the
  source, to vanish. The exact one-prime increment and its positive adjoint collar defect are proved.
  Derivation of this uniform bound (ESB) from oriented finite PC-ren remains OPEN.
- R162_202 — the one-prime defect is globalized to an exact finite multiprime Sonin leakage identity.
  It retains every crossed squarefree-divisor term and rewrites ESB as a common bound for the adjoint
  interior history plus one exterior square. The PC-ren upper bound for this quantity remains OPEN.
- R162_203 — audit: ESB exactly removes the product regularisation and is equivalent, on the
  first-contact class, to the desired conclusion. It is a quantitative formulation of Gate 1, not a
  weaker intermediate lemma.
- R162_204 — proves that the regularised critical jet is invariant under every finite modification of
  `Lambda`. The arithmetic falsifier must therefore enter before evaluation, through the exact Ward
  defect `B_a=zeta A_a+zeta'=DS(a*1-log)`. It fixes the required four-term type of a closing finite
  Green identity; that identity remains OPEN.
- R162_205 — inserts that Ward defect into the exact four-block Green calculation. The contribution
  is linear and changes sign under `eta->-eta`; at `a=Lambda` it vanishes and leaves precisely the
  old antisymmetric exterior correlation. Hence literal PC-ren substitution, subtraction against a
  modified comb, and ordinary polarization cannot manufacture the critical-jet square.
- R162_206 — derives the complementary anomaly `(PC+)` using the Poisson sum `C_N`, whose covariant
  derivative has the critical-jet orientation. Its difference from `(PC-)` is an algebraic zero valid
  for every source. Hence the two finite equations have one-dimensional linear content; compression
  merely moves the missing block into the exterior correlation.
- R162_207 — audits the remaining nonlinear two-parameter escape. Scalar Euler/source curvature is
  flat and its apparent compressed return cancels in the complete Green law; an active coefficient
  deformation has no first-contact stationarity or sign. Closure now requires genuinely new input:
  either a noncommutative Euler-root lift with physical Gamma/Tate descent, or an independent
  coefficient-direction equality law at `Lambda`.
- Round 3: R162_301 C1 noncommutative Euler lift NO-GO (leakage = half-line Brown–Halmos,
  symbol-independent; anomaly closed-form, indefinite, not Λ-specific). R162_302 C2 coefficient law
  PARTIAL (‖R_LF‖²=ε∫c_Fκ_L; reduction (A)+(B)); audit R162_390 CORRECT WITH FIXES. R162_304 D1:
  (A)+(B) ⟺ K^ε={0} (reformulation), NO-GO. R162_305 E1 exterior Ward: derivative of PC-ren identity is
  an algebraic zero; Ward meets δD only through ζ(−2j)=0 after continuum renormalization; route (ii)
  CLOSED. Remaining new-input requirement: break the continuum-renormalization (trivial-zero)
  cancellation. R162_303 C3: CERTIFIED λ_A(½log5) ≥ 2.5e-12 (even; odd ≥ 3.0e-10), Arb ball arithmetic;
  audit R162_391 CERTIFIED (full rerun matched). By lem:monoT, λ_A>0 on (0,½log5], hence any first
  contact has T_* > ½log5 = 0.80472 (primitive form; W_T not treated).

- Round 4: G2 R162_402 reflection dictionary PROVED (G_+^0(−a_m)=−εζ'(−2m)K_F(a_m)); Hardy
  mechanism NO-GO. G1 R162_401 log channel survives renormalization (γ_jζ'(−2j)=−ζ(s_j)) but cancels
  by [X,S_N]=−K_N; NO-GO. G1.2 R162_403 smooth comb: H^{(P)}=0 exactly (Λ*1=log on P-smooth), all
  channels cancel; lesson: X,J,Dirichlet-multiplier identities are symbol identities and fail F1.
  G1.3 R162_404 compression: P_TZ_PP_T=Z_T; Tate jets enter only as λ⟨Γ_PF,φ⟩, vanish at λ=0; NO-GO.
  Next: G1.4 right minimality at enlarged window T_*+δ.

- G1.4 R162_405: collar identity λ_δ⟨F_δ,EF⟩=⟨ξ,F_δ|collar⟩; right minimality = non-extendability; NO-GO (sign
  is monotonicity only). G1.5 R162_406: collar formula, compressed Chebyshev across e^{2T_*}; Λ-specific
  edge coefficient vanishes at composite thresholds by Λ*1=log; NO-GO; minimality line exhausted.
  Conjecture 7.1 (closes Gate 1): (LB) λ_A(T_*+δ) ≥ −κ(δ) and (NE) |⟨ξ_G^δ,F_δ⟩| ≥ κ'(δ)‖R_LG‖², κ/κ'→0.

- Round 5: H2 R162_408 (NE) PROVED as exact identity λ_A(T_*+δ)=−q_δ(1+O(q_δ)), κ'=2‖ξ_G‖²/log(1/δ);
  weight-blind. Consequence: (LB*) λ_A ≥ −o(Q_δ(G,G)) forces ξ_G=0, i.e. extendability — so Conjecture 7.1
  ⟺ no first contact (reformulation). H1 R162_407: unconditional λ_A(T_*+δ) ≥ −2A_*Q_*/log(1/δ) (explicit
  continuity rate); under (REG) virial law λ_A(T_*+δ)=−(δ/T_*)𝒱(G)+o(δ); all steps weight-blind; DH has
  first contacts. Status: Gate 1 OPEN; every analytic reduction so far is weight-blind.

- Round 6: R162_590 dead-end map (corpus 0–162; V/H/S already tried; top untried: signed bilinear, D3, D5).
  R162_501 V: Selberg–virial identity (Λlog+Λ*Λ=μ*log² in the value of 𝒱 on N, under REG) PROVED; no sign; (S-W) ⟺ Cor 3.3.
  R162_502 H: Hecke NO-GO; B1 one-sided compression, B2 M_T(Λ)=ZXZ⁻¹−X coupled-square formula PROVED; B3 no allowed
  input orients it; open (B4.1). R162_503 S: two-way quantity exact; Gamma coefficient ≡0 (Thm 3.1); transport to every
  degree-1 Dirichlet series (Thm 4.2) ⇒ no DH line; NO-GO. R162_504 D5: Perron–Frobenius for A_T (step v_n≥0 is the DH
  line), parity ladder, Type I/II dichotomy, Perron–Tate bound; NO-GO for sign; open O504.1.
  Lesson: ζ-specific data enter only as inequalities/support (Λ≥0, supp μ*log², integrality {X/m}), never identities.
- Round 7: R162_701 NO-GO: (B4.1) is an identity (⟨SZ*F,SZ⁻¹F⟩=⟨F,M_T(Λ)F⟩+‖SF‖²), equality on N; B2 square
  is a rewrite; integrality enters only linearly via the sawtooth = (PC) comb.
- R162_702 NO-GO: Perron + Hellmann–Feynman orients only μ_1; support-class blindness (κ-models in 𝒞 have first
  contacts); supp μ*log² is supp Λ in disguise. Open: a use of Λ*1=log that is neither symbol identity nor estimate.
- R162_790 audit round 6: nothing WRONG; 501 L2.1, 502 B1, 504 Thm2 CORRECT; 501 Thm2.2 (B_X term, REG⁺, sign of λ
  term), 502 B2 (𝔞^∞ = archimedean form only), B3 (input list, not theorem), A5 (reason: translation rescales A,B),
  504 Thm1 (irreducibility via k>0 + Reed–Simon XIII.44), Thm3 (pseudo-inverse form) CORRECT WITH FIXES.
- R162_703 D3: exact converse conditions (g_par nonincreasing; Thm 2.2); CERTIFIED (audit R162_791: CERTIFIED, bit-identical rerun)
  λ_W>0 on (0,½log5] (even ≥1e-18, odd ≥1e-16), complete form past Zhu 0.8; T_W ≤ T*; Type II exclusion NO-GO (F3).
- Round 8: R162_801 floor ledger NO-GO: D_a≡0 ⟺ a=Λ (L1) but per window a weight rewrite (L2), floor+Stirling = PC
  sawtooth (L3), λ concave in weights (L4), asymptotic use dead by Thm M (L5). Residual: exact nonlinear use.
- R162_802 T-evolution: collar increment law, monotone flow of f_par, conserved Haynsworth index (first contact = only
  +1 event), T_W≤T* recovered, RH ⟺ two monotone limits (E1); invariant NO-GO. Conj 6.1 f(∞)=∓½; residual O802.1 (edge
  traces at ½log n vs ½log nm).
- R162_803 generating object: Theorem G (Φ(s) = Poisson factor × 2Re ξ′/ξ, s>½) PROVED; positivity = Lagarias Herglotz
  criterion (E1); first contact invisible (Prop 4). T-transform closed.
- Round 9: R162_901 edge-trace identity PARTIAL/NO-GO: Selberg Λ·L+Λ*Λ=μ*L² (already R162_501) sits in the ε² sum
  channel at ½log mn; difference channel |Σw_n n^{it}|² uncontrolled; pole at ε_c<1. Residual: sum/difference cancellation.
- R162_902 asymptote: Conj 6.1 ⟺ RH; unconditional half lim g̃≤0 (already R160_M4 B(i)) with elementary 2nd proof;
  exact expansion f(∞)−f(T)=g/(2(2∓g)); overshoot permanent, not excluded by monotonicity. NO-GO for closure.
- R162_903 nonlinear Möbius NO-GO (PROVED): terminating BCH log Z=M_T(Λ/log) (Thm 3.2, new); Gram = AᵀK_FA unipotent
  integral; Moore collapse; tensor lift (degree 2d = quadratic at N^{⊗d}). Residual: discontinuous functional separating
  ℤ from Beurling and 1 from χ₂, not unipotent-invariant.
- R162_990 audit R7–R8: 703 L2.1, Thm 2.2 (add f(0)≠0), 802 Thm 2.1 CORRECT; 703 Prop 4.1 WRONG as iff (only ⟹);
  802 "RH ⟺ two limits" WRONG (⇐ assumes ι≡0) — label withdrawn; 803 Thm G CORRECT WITH FIXES (c=1, comb +ζ′/ζ);
  Thm H s>½ trivial; 801 L4 monotonicity WRONG (concavity OK). Paper 47 thm:parityschur(b) wording to fix.
- Round 10: R162_1002 quasicrystal NO-GO: rigidity theorems presuppose real zeros; window form local (P1); supp log ℕ +
  Λ*1=log is a one-member class (P2); no local uniqueness (P3). Separating functional must be uniform on a family
  where ζ is not isolated.
- R162_1004 tensor power NO-GO: ζ^d weights dΛ, same T_*; tensor trick idempotent at contact; polynomial-in-d bound
  at X^d ⟺ RH; Deligne needs independent bound (P149 ingredient iii).
- R162_1001 ×p NO-GO but NEW: torsion distribution Φ_a=Σa(d)(ν_d−Leb), cocycle ℒ_pΦ−Φ=log p(δ₀−Leb) ∀p ⟺ a=Λ (Thm 3.1)
  — first object failing for Λχ₂ AND Beurling. Band-limited window tests read only the prime term. Residual: a
  non-band-limited test built from F at T_* that reads torsion atoms.
- R162_1003 sum/difference: Thm S (channels = 4(Re D)², Im² cancels) and Thm R (resummed symbol 2Π_η, ⟺ RH) PROVED;
  Selberg sieve impossible (Toeplitz ≠ GCD kernel); NO-GO. Lesson: exact FE resummation lands on Σ_ρ; Euler product
  must enter after it.
- Round 11 launched: R162_1101 torsion atoms (non-band-limited test from F), R162_1102 character family, R162_1190 audit.
- R162_1102 character family NO-GO (Thm O: family sum weight-free; orthogonality re-indexes). Lesson: the family must
  not be tied to ζ by an exact linear window identity.
- R162_1101 torsion atoms NO-GO: H_+ + Q_+ = ½K_F⟨Φ_Λ,g_{½+z}⟩ (Thm 2.1, new); Li_{−2m} inversion puts the Gate-1 pole on
  atom 0 only (Thm 2.2); Smith gcd self-pairing ≥0 but Λ-free (Thm 4.1); Riesz collapse to Sonin range R161_011 (4.2).
- R162_1190 audit R9–R10 (26 items): 11 CORRECT, 11 WITH FIXES, 2 WRONG (1001 Thm 3.1 failing-prime/Λχ₂ table;
  1004 Thm 3.1 quantifier), 1 relabel (1004 Prop 3.2 → REMARK); 903 Reading paragraph on Λχ₂ wrong; 1001 Thm 2.1 step
  repaired via p.v. cot; 1002 P1′ first form withdrawn. No NO-GO verdict changes.
- Round 12 launched: R162_1201 Sonin range direct, R162_1202 odd-degree functionals, R162_1203 Laumon transport.
- R162_1203 Laumon transport NO-GO: L1–L3 theorems over ℚ, L4–L6 missing; Thm W (rationality wall) PROVED; ε-data =
  scalar C₀. D1 lamination still unbuilt (Teichmüller lemma unproved).
- R162_1202 odd degree NO-GO: Thm C polynomial collapse — any degree reduces to e_m ∈ ran H (Sonin range); Prop H corrects
  1101 (atom placement kernel-dependent; residue −εK_F(a_m) invariant).
- R162_1201 Sonin range NO-GO: x_m = exterior far field of archimedean potential (Thm 1.2); (S_m) exact, Jordan rank-2
  resonance; family ⟺ HF=0; Müntz–Szász all-or-nothing (Thm 4.1); q-difference Riemann–Hilbert dictionary (Prop 4.2).
  Residual: bring H≥0 in — Kreĭn Jordan-chain non-isotropy via complete monotonicity of κ.
- Round 13 launched: R162_1301 Kreĭn Jordan chains, R162_1302 q-difference RH problem, R162_1390 audit R11–R12.
- R162_1301 Kreĭn NO-GO: M_I = C₀+Σ(2/a_k)L_k(a_k²+L_k)⁻¹ Robin strings (Thm 1, new); Gate 1 ⟺ Douglas bound
  |⟨G,e_m⟩|² ≤ C_m 𝔥(G) on harmonic-divergent S (Thm 3; first F1-clean inequality form, still equivalent).
- R162_1390 audit R11–R12: no verdict changes. WRONG: 1101 Thm 4.1(b); 1202 Thm A headline (only on great circles).
  Fixes: 1101 Thm 2.2 atom reading (regularises to 0), 1102 Thm O conductor term log q‖F‖², 1201 sign typo (t−T),
  Thm 3.1 sharper bound, Thm 4.1 all m≥1; 1202 Thm D missing α-term; 1203 Thm W → REMARK.
- R162_1302 q-difference RH NO-GO: exact RH problem on the cut (Thm 2.1, new); 0/∞ connection samples ζ lattice vs DH
  lattice (Prop 2.2); Euler product = separability of symbol, P_Λ=𝔈 log Z (Prop 3.1); maximal monodromy (Thm 3.2).
- Round 14 launched: R162_1401 Douglas bound via Λ*1=log after string decomposition; R162_1402 Q-functions in T.
- R162_1401 Douglas/log NO-GO: secular ledger (Thm 2), Tate-only cancellation (Thm 3, new), ray reduction to truncated
  (−ζ'/ζ)ζ=−ζ' at 2m+1 (Thm 4); Douglas at e_m ⟺ Douglas at Jordan partner. Obstruction: no arithmetic pole on m≥1 rays.
- R162_1402 Q-functions PARTIAL: Q_m(0;T) nondecreasing (Thm 1), collar law (Thm 2), square-root law Q≍|x_m(ψ_T)|²/λ
  (Thm 3), Markov–Kreĭn NO-GO (Thm 5). UNCERTIFIED numerics: ψ_T carries O(1) Gamma data while λ collapses — strategic
  warning: near-null vectors of ζ itself have x_m≠0, so R_LF=0 may be an unnatural intermediate target.
- R162_1502 comb spill PARTIAL+NO-GO: collar spill C⁺u=M(log)Z⁻¹u=−ZXZ⁻¹u (Lemma 1, new); r(ψ′)=λ′⟨ũ,ψ′⟩−x_m(ψ′)
  weight-free (Thm 4); uniform target |x_m(ψ_T)|²≤C_mλ(T) contradicted by ζ data (local form = Gate 1).
- R162_1590 audit R13–R14: NO-GOs stand. WRONG: 1402 Thm 5 (Markov–Kreĭn; only j≤2 survives, near-trivial). Script bug
  in q1402_float_Q.py (abs(sign)·tail) FIXED; corrected λ(½log5,even)=6.6e-12 matches certificate; Q table 10⁴–10⁵ too
  small; corrected |x_m(ψ_T)|²/‖e_m‖² ≈ 0.04–0.09 (stable, nonzero, uncertified). 1401 Thm 3 split only as T→∞.
- R162_1501 target audit: R_LF=0 ⟺ F=0 on radical (not intermediate). Lemma D (Descartes, new, PROVED): K_F has ≤ S(F)
  real zeros ⇒ Gate 1 forces infinitely many sign changes. Float nodal data (RUN WITH THE abs(sign) BUG — fixed, rerun
  pending). Proposed targets R-A oscillation budget, R-B single Euler-channel scalar, R-C Type I rate + Chebyshev pair.
- R162_1601 nodal rerun (fixed script, K=34/46/60, UNCERTIFIED): even bottom S=2, odd S=3 on [0.3,½log5]; level crossings
  and odd anomaly of 1501 were bug artifacts; K_F(a_1..4) one-signed; ζ near-null vectors asymptotically Type I (r≈0.93λ).
  Deletion contact T_c=0.595818: S=2, one-signed, but Type II (r=0.278, ⟨F,ψ⟩=0.141). R-C survives only via (C1) Type I.
- R162_1603 R-B NO-GO: Prop H (S≤3 ⇒ coherent sign), Lemma S (coherence ⇒ dim N=1, new), Lemma E (edge log singularity),
  Thm P positivity lock (new). Open direction: sub-window sign budget for 2-node radical vectors, coupled to a′≠1.
- Round 17 launched: R162_1701 R-C (Type I ⟺ T_W=T_*; nodal contradiction; polar-contact exclusion).
- R162_1602 oscillation budget: Karlin route closed for all models (Thm K1 not TP₂, K3 TP₂⟹local, K2); nonlocal Courant
  identity (Prop C) gives no bound; comb-free ground state symmetric decreasing (Almgren–Lieb), comb breaks it — (C2)
  loses its tool. Residual (OB). Note: deletion contact also has S=2 (R162_1601), so a budget alone is weight-blind.
- R162_1701 R-C: Thm 1 λ_W(T_*)≥0 ⟺ all contacts Type I ∧ 𝔊⪰0; RH ⟸ R-C.a (no polar contact before T_*) + R-C.b (no Type I
  contact). Lemma C, Thm 3 (R-C.b under (C2)+(N2)), Prop 5 (near-Type-I = Perron–Tate alignment), Thm 7 residue window
  κ₋(T)≤1≤κ₊(T) nested; R-C.a ⟺ RH given R-C.b. Split: R-C.b weight-blind structural; all arithmetic in R-C.a.
- Round 18 launched: R162_1801 prove R-C.b, R162_1802 residue window R-C.a, R162_1803 numerics (N2),(C2),⟨u₂,φ⟩, R162_1890 audit.
- R162_1801 R-C.b PARTIAL: even Type I ⟺ μ₂^ev(T_*)=0 (Thm A); homotopy NO-GO (Thm B, 3×3 positive counterexample);
  polarization NO-GO; (C2) fails for large amplification past T_*(s) (Thm D) — proof must use λ_A≥0 up to T_*. Open (R2′).
- R162_1802 residue window: extremal/dual (S-lemma) forms; Thm H width 2(κ₊−κ₋) residue-free; Thm R RH ⟺ window
  nonempty ∀T (residue value 1 never needs proof; E1 as family); Lemma D (d/dt maps even↔odd, z² multiplier).
  Per-T κ₋⇒κ₊ NO-GO. All difficulty moves to width ≥ 0 via integrality (O1802.3).
- R162_1890 audit R15–R17: 1501 Lemma D CORRECT; 1602 K1,K3, Prop R CORRECT; 1603 Prop H, Lemma S, Thm R CORRECT;
  1701 Thm 3, Props 4,5 CORRECT. WRONG: 1602 §3 two-constraint count (→ HEURISTIC). Fixes: 1502 Lemma 1 sign on C₋,
  Thm 5(b) remainder; 1701 Thm 1(1) needs T_* defined with < 0; Thm 7(4) vacuous → "under RH". 14 fixes, no NO-GO overturned.
- R162_1803 numerics (UNCERTIFIED, K=26–76): (C2) FALSE once comb present (from T≈0.38); (N2) true where needed; ⟨u₂,φ̂⟩
  sign flips across sΛ family ⇒ 1701 Thm 3 not weight-blind; μ₂^ev(T_*)>0 at every tested contact (deletion 3.8e-2,
  s=0.5..3 ≥4.6e-4) — R-C.b supported, no counterexample; (R2′) false; ζ: μ₂^ev and ⟨u₂,φ̂⟩ →0 together. Deletion on
  [0.3,0.6] = archimedean operator (first prime 5 at 0.80).
- Round 19 launched: R162_1901 R-C.b via λ_A≥0 up to T_* (no C2), R162_1902 window width ≥0 with integrality.
- R162_1902 width/integrality NO-GO: on {B=0} Φ_c vanishes at 0 and 1; B₂ pairing = Poisson (Lemma C); linear-in-c value
  = ∫|F̂|² Re ζ(½+iz) (Prop Z), both signs (Prop I). Lesson: integrality must enter nonlinearly in c.
- R162_1901 R-C.b minimality NO-GO: Type I ⟺ (μ₂=0, ⟨u₂,φ⟩=0, g(0)≤0) (Thm 1); explicit 3×3 model with Type I first
  contact satisfying all monotone laws (Thm 2); Type I = codim-2 set; generic 2-parameter combs meet it. Decisive test
  O1901.1: a=s₂δ_{log2}+s₃δ_{log3}, sign of ⟨u₂,φ⟩ along {μ₂^ev=0, g<0}.
- Round 20 launched: R162_2001 two-parameter comb Type I search (numerics), R162_2090 audit R18–R19.
- R162_2090 audit R18–R19: no fatal errors. WRONG: 1801 Lemma D1 factor 2 (Thm D survives); 1901 §3(iv) double-zero
  claim. Fixes: 1802 Thm Q (−ε, ζ-only source), 1902 Lemma C signs, Prop I interval (ζ(½)=−1.46 simpler witness).
  (R2′) test in t1803_contact.py used c=⟨ψ,cosh⟩/‖cosh‖² (the instruction) vs 1801's c=ψ(t₀)/cosh(t₀/2): rerun needed.
- R162_2001 Type I search (UNCERTIFIED, K=34/46): falsifier FIRES — curve of Type I first contacts in the positive cone
  a=s₂δ_{log2}+s₃δ_{log3}, at s₂^c∈[0.99976,0.99995] for s₃∈{0..4} (λ,μ₂,⟨u₂,φ̂⟩<1e-13, g(0)≈−0.42, N₋ 1→2). R-C.b false
  weight-blind. STRIKING: the curve hugs the exact ζ weight s₂=1 (margin collapse μ₂~1e-10 on the whole row s₂=1).
- Round 21 launched: R162_2101 explain why s₂=1 is special (exact identity?), R162_2190 independent numerical verification.
- R162_2101 mechanism: no local identity (NO-GO); for s₂=1, T<½log3 the window form IS ζ's complete form, whose truncated
  radical (Pólya-kernel directions (¼+z²)Ξ) is null up to doubly-exp error ⇒ near-kernel of dim ≥2 with a primitive
  direction ⇒ near-Type-I (Lemma 3: Type I ⟺ κ=0, Wx=κφ̂). Curve at 0.9998 = detuning of ζ's κ~1e-5. So R-C.b for ζ has
  a doubly-exponentially small margin: R-C.b needs ζ-specific (zero-side) input too. R-C split does not isolate the arithmetic.
- R162_2190 independent verification (cosine basis, N=60–320): CONFIRMED at float level (uncertified): s₂^c=0.9997678 (6
  digits), Type I point λ=μ₂=⟨u₂,φ̂⟩=0 to 1e-15, s₂=1 collapse real (φ not an eigenvector; constraint does not touch μ₂).
  Explanation of proximity to s₂=1: R162_2101 (window form = ζ's complete form below ½log3).
- R162_2300 MASTER GRID (grid/): whole corpus (phases 0–162, papers 01–47), 910 routes, 8×8 grid, 12 walls, falsifier
  table, tools inventory, 59 never-attempted entries, closing spec, ranking. MANDATORY: consult before every round;
  every new idea names its cell and the wall it evades; append results with source_part ≥ 7.
- Round 22 (Blaschke–torsion, cells 8B×5C): R162_2202 front B PARTIAL+NO-GO: Thm NI node identity w_x = L(x)/F̂′(x)
  (Christoffel), explicit: only n<e^{T_c} enter (contacts in [T_c,2T_c) invisible at node level); Thm ND no descent
  (class-level); Euler self-similarity NO-GO (W3). Residual O2202.2: node-level statements see only n<X^{1/2} — test vs Thm M.
- R162_2201 front A NO-GO: node tests are Paley–Wiener (Lemma N0); minimal atomic object 𝒜(s;G)=Σ q_x(−ζ′/ζ)(s+ix)
  (Thm N1, new) but at s=½ Z′/Z cancels by parity (weights even) → Λ-free θ′ identity; node measure = Kreĭn extension
  (E1); Λχ₂ passes via twisted cocycle. Residual O2201.1: asymmetric node weighting = signed Z′/Z at nodes (zero side).
- Round 23 launched: R162_2290 audit R22; R162_2301 cell 6C Selberg difference channel; R162_2302 cell 5F/4F R161_075–079 limit.
- R162_2301 cell 6C NO-GO: Lemma S (Selberg identity ⟺ a=Λ, recursive); correction to 901 (ω≤2 support separates
  nothing; deletion fails at N=6); Thm DC channels = W-values at nodes; Thm Q node quadrature exact on type ≤2T_c
  (Akhiezer) ⇒ w_x≥0 is just W≥0. 6C → ◩, residual = type >2T_c, i.e. contacts n∈[e^{T_c},e^{2T_c}) = O2202.2.
- R162_2290 audit R22: both NO-GOs stand; 2201 N1(a) factor 2, N1(b) only ⟹, Thm N3 WRONG as a theorem (downgrade to
  proposition on three routes); 2202 NI correct (only n<e^{T_c}), Prop T example false (1+2^{iz}), ND needs ι-invariance.
- Paper 48 (04-papers/48-row-d-route-map, 16 pp) written; TikZ row-label bug fixed.
- CONVERGENCE: R162_2202 and R162_2301 independently isolate the same residual — the contacts n∈[e^{T_c},e^{2T_c})
  invisible to node quadrature (O2202.2). Candidate target for round 24.
- R162_2302 cell 5F NO-GO: Thm N (weak limit ≡0 for every primitive source via ζ(1−ρ)=0; restores W6 for this
  limit); Thm V (radicality ⟺ Gate 1, Volterra has no finite invariant subspace); obstruction = one scalar c_f
  (left-exterior Tate moment); Prop O (Euler/ℕ-Poisson compose as ζ(1−s)ζ′/ζ(s)). 5F → ◩; residual O2302.2 c_f≠0.
- R162_2402 cell 5H NO-GO: node/S_p sets not definable (Thm A); Kronecker images never torsion (Thm B); torsion sits on
  algebraic carriers (Prop B′); two-atom model identical window data at T_c<log2 (Thm C). Obstruction = W10 (no
  ℚ̄-variety attached to F) + W8.
- R162_2401 hidden contacts NO-GO: W=V−H split; Thm HV (H = sum channel of half-witness, cross term of W(F)=2W(F₊)+2W(F₊,F₋));
  Prop P2 (H(F^ev)=−H(F^odd): only witness parity OS-2 fixes sign); Lemma U (cut-off comb determines hidden comb);
  Theorem M does not come from hidden contacts (Cor M2: holds with no comb; scale = zero height). O2202.2 CLOSED.
- Ranking status after rounds 22–24: #1 8B×5C, #2 6C, #3 5H, #5 5F all NO-GO; remaining: #6 8F/4E/7E, #7 4D Γ–Euler
  detector, #8 8D, never-attempted list (§6 of master grid).
- Round 25: R162_2502 Γ–Euler detector (4D) NO-GO: Thm D (detects only Gamma moments, n=2 translation + bounded factor);
  Thm K (bounded source-defined K exists ⟺ ker H_T={0}; ‖K_T‖~1/λ(T); uniform = rate law, M); Prop A (Euler data
  before regularisation = positive diagonal lattice multipliers, contains Thm P); residual folds into 1603 (d).
- R162_2501 C_B (m<∞⇒m=0) NO-GO for route (a): under H(m) −λ_A ~ e^{2β*T}, no clash with Thm M (same direction), floor
  −4e^T; model M_m (ξ × rational factor, m off-line quartets) shares all class-level structure (Thm 3); Prop 3: a C_B
  proof must show the atomic Λ-comb is incompatible with any nonzero finite exponential density (O2501.1, new, concrete).
  Prop 1 upper bound is a sketch (audit needed).
- Round 26 launched: R162_2590 audit R25; R162_2601 O2501.1 atomic comb vs finite exponential density; R162_2602 cell 8D.
- R162_2590 audit R25: nothing WRONG; both NO-GOs stand. 2501 Prop 1 upper bound repaired (θ on ellipse, T-independent
  primitivity) — exponent law 2β* holds; M_m correct (count 2m conjugate pairs); Thm 3 small-T change O(mT); Prop 3 E
  restricted to quartet type; 2502 Thm K only "(4.1) at least as strong as Gate 1".
- R162_2601 O2501.1 NO-GO (false as posed): Thm Λ̃ new falsifier (positive atomic weights 1−Σ2Re n^{ρ_j−1} reproduce E;
  Dirichlet series not a log-derivative); Thm T (idea "tempered" is E1); Thm H Hamburger rigidity (log-derivative
  Dirichlet series + ζ's FE ⇒ F=cζ; cited from memory). C_B needs an individual Euler-product property (O2601.1).
- R162_2602 cell 8D NO-GO: carrier A_T=P_I S P_I with S=S₀−2ℓ₊ℓ₋ (Thm 1); no S≥0 compresses (Thm 2); Thm 3 E1; CC semilocal
  passes deletion (Thm 4); Sonin count run: N(T)=n₋(A_T|P_T) nondecreasing, first jump = T_*, N→2κ_off (Thm 6);
  sup N<∞ ⟺ C_B-type finiteness (8F). 8D → ◩; residual O2602.1 = same lemma as 8F/O2601.1.
- CONVERGENCE (rounds 25–26): 8F, 8D, O2501.1 all reduce to ONE lemma O2601.1 — an individual Euler-product property
  of ζ, using exact Λ values nonlinearly, bounding the off-line count (fails for deletion, M_m, Λ̃).
- Round 27 launched: editor merges part8; R162_2701 cell 4E Tate 2×2 canonical system (O8); R162_2702 1D NG-D4 + doc 107.
- R162_2701 cell 4E Tate 2×2 (O8) NO-GO: T_p = conjugated σ₁-boost, tanh θ_p=p^{-1/2}; Thm TC canonical system
  H_S=½exp(2Θσ₁), Θ=Σ artanh p^{-1/2} (Euler product only at s=½, z-independent); Thm P H≻0 always (RH-neutral);
  phase-61 index κ₀+|S| was an artefact; Thm I M_m gives same H_S ⇒ not O2601.1. W12 in cleanest form.
- R162_2702 cells 1D/4C: doc 107 closed by doc 108 (sieve→index bridge dead, W2+E1), not MW-7; W⊗W signature adds nothing;
  boundary triple for W_λ PROVED (deficiency (2,2), even sector circle B_t, B_CCM=B_∞, rigidity from time-limiting not
  Fourier; Weyl function Nevanlinna); invariants Λ-free ⇒ NO-GO for O2601.1 (W3); NG-D4 DEAD (index count). O2702.1 open.
- Round 28 launched: R162_2890 audit R26–R27; R162_2801/2802 two angles on O2601.1.
- R162_2801 angle A NO-GO: ζ₀=ζ/R Beurling-type outside Selberg class (Lemma 2); Hamburger/KP/SMO return cζ for any m
  (Thm NG); exact C_B form (QR) = C_B in Pontryagin form. New live residual O2801.1 (cell 4F): can the generalized-
  integer measure dN₀ of ζ₀ be ≥0 with all zeros real? (nonlinear in Λ; inside O2601.1).
- R162_2802 angle B NO-GO: Thm PB (Piltz sums see only the pole; H(m) ⇒ Lindelöf ⇒ same α_k; zeros killed by 1/Γ(−z)
  on ℕ); Thm L exact terminating ψ–D_k identity (formal, m-blind); contrast needs Piltz bounds uniform to k≍log x = ψ
  bound (E1). Corrects 2601 §3 (G is a log-derivative of meromorphic F̃; F̃ lacks FE/integrality). Residual O2802.1.
- R162_2890 audit R26–R27: all NO-GOs stand. WRONG: 2701 "phase-61 index was an artefact" (replace: uncertified, index 0
  after normalization); 2702 boundary triple — ±∞ are limit CIRCLE, deficiency (4,4) not (2,2) (phase-60 count should be
  (6,6)); U(2)/B_CCM=B_∞/Weyl function must be redone; Prop 2.5 (invariants Λ-free) survives. Fixes: 2601 Λ̃ gives ½E;
  2602 Thm 6 N→4·(#quartets)… use κ_off=#quartets, N left-continuous; Cor 7 trivial bound doubly exponential.
- Editor merged part9 into R162_2300_MASTER_grid.json (part9_merged; 936 routes; ■10 ◩21 ◧33): 4E loses O8, 4C loses doc 107, 1D ◧→◩ (residue: redo boundary triple (4,4), O2702.1), 4F gets O2801.1/O2802.1, 8D back to ◧ by §8 rule (4 unsuperseded PARTIAL/OPEN). Paper 48 updated (grid, tools, Problem 6 sub-forms).
- Round 29 launched: R162_2901 O2801.1 (dN₀≥0 with real zeros?), R162_2902 cells 6D/6A (P2, lem:degen), editor merge part9.
- R162_2901 O2801.1 NO-GO: explicit dN₀, dΠ₀ (Props 1–2); Thm A dΠ₀≥0 fails for every m≥1 in the strict class (2β*
  oscillation, E1); Thm B: under H(m), ζ·S₁^K·P₀/P is a GENUINE Beurling system (dΠ,dN≥0, ζ's FE, all strip zeros on
  the line). So positivity never separates; the ONLY separator left is integrality of dN (O2601.1 in its sharpest form).
- R162_2902 cells 6D/6A: reflection lemma (T≤log2: c_F(log n)=±⟨f,R_n f⟩, ‖Π_T‖≤½A_T, sharp) PROVED; P2 prime part PROVED
  exactly: path blocks ≤4, ‖Π_{log2}‖=0.9009276162618… closed form (matches record numeric to 1.7e-14); lem:degen PARTIAL
  (open at log 2); P153.17 NO-GO (reduces to closed form for λ^{∞,P}). Tools only; no bearing on O2601.1.
- STATUS after rounds 22–29: the whole ranking is attacked; everything alive reduces to O2601.1 in its sharpest form
  (R162_2901 Thm B): only integrality of the integer measure separates ζ from a genuine Beurling system with ζ's FE
  and all zeros on the line built from a hypothetical H(m).

## Rules

Working rules: pure mathematics; at most 5 parallel lines of attack per step; check R160 survey/brief and R161 notes
before building (feedback-check-corpus-first, feedback-five-agents-max).
