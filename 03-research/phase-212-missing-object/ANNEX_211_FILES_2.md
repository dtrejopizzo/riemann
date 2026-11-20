# Annex 211 — Files, second batch (POWER_DESCENT_016 … POWER_INVERSE_INTERIOR_022)

Complete reading, file by file, of the `.md` files of `../phase-211-sign-sandbox/` lying in alphabetical
order between `POWER_DESCENT_016.md` and `POWER_INVERSE_INTERIOR_022.md` inclusive, except
`POWER_GLOBAL_ROUTE_REVIEW.md` and `POWER_GRAM_SLICES_OBSTRUCTION.md`. Notation of
`../phase-211-sign-sandbox/STATEMENT_001.md`, `POWER_CONE_001.md` and `POWER_BRIDGE_002.md`. In these files
W is the full form on the line (ARCH + POLAR − comb), V_n={P(s)/(s+u)^n: deg P<n}, Q(s)=s/(s+u),
u=63/2 unless stated otherwise; g_N(t)=t^{N−1}e^{−ut}/(N−1)!; L(a), K(a,b) are those of POWER_CONE_001. The
target is (★) of STATEMENT_001. Labels are copied as they appear in each source.

## Entries by file
### 1. POWER_DESCENT_016.md
- Object: complementary filters Q=s/(s+u), L=u/(s+u) (u>1); exact identity W[f]=W[Qf]+W[Lf] (DEF), polar included; binomial iteration (BIN); differences (−1)^rΔ^r a_k=W[L^rQ^k f] (FD); spectral binomial law (LAW).
- Result: PROVED (identities, eventual monotonicity of differences, localization (LOC) with error Lip(φ)/(2√m), (EDGE): the edge of 015 has total mass and energy →0). Falsifier W_4=W−4‖·‖²: preserves DEF/BIN/eventuality and W_4[e^{−63y/2}]/‖·‖²<−1 (2L(32)<3). Global arithmetic descent OPEN.
- Unsigned remainder: the defect W[f]−W[Qf]=W[Lf] (full form of the low-frequency block) in the first steps; the interior j/m≈θ<1 of (BIN).
- Reopening: a descent controlling W[Lf] with the full arithmetic datum or using the spectral distribution of the numerator.
- Reusable PROVED: (DEF)/(BIN)/(FD) for every causal rational f; telescoping W[f]=Σ_k W[LQ^k f] absolutely convergent.

### 2. POWER_DESCENT_AUDIT_016.md
- Object: moments ℓ_r(f)=∫y^r f in L²_η; unions of Q^kV_N; shifted filter Q_δ=(s+δ)/(s+u).
- Result: PROVED and APPROVED: (i) the union of Q^kV_N, k≥1, lies in the hyperplane ℓ_0=0, it is not dense (even in P_T: F=(¼−D²)g); (ii) k_j→∞ ⇒ every strong limit is 0; (iii) logical falsifier W_C, C=4; (iv) §9: span{Q_δ^r f_0: r≥R} dense, W_4[f_r]>0 eventually, but there is a finite combination with W_4<0.
- Falsifier: refutes «dense span + eventual individual sign of generators ⇒ sign on the span» and «partition+positive mixture+eventuality ⇒ initial sign».
- Reopening: an inequality controlling the defect of the initial blocks with additional information, or joint uniformity over the relevant mass; a topology in which the moments are not continuous, with continuity of the full form reverified.
- Reusable PROVED: moment obstructions (hyperplane ℓ_0=0; zero limit) in L²_η, η>0; approval of JOINT_SCALE_016 (law Beta(k+½,N−½)).

### 3. POWER_DIMENSIONAL_AUDIT_051.md
- Object: audit of DIMENSIONAL_CUTOFF_051.
- Result: APPROVED as a moment bound and an ARCH bound, not for W; correction of the factor of the second sector (d−1)(d+2j+1).
- Remainder: initial segment depending on n, polar and full comb. Cited falsifier (PRIME_TRANSFER014): n=2^17, F=(s²−¼)/(s+u)^n, E2[QF]<0 prevents declaring all initial segments of E2 positive.
- Remark: ZERO13 controls a codimension-one subspace; the Schur coupling remains uncontrolled; no new NO-GO is recorded.
- Reusable PROVED: none of its own (validates 051).

### 4. POWER_DIMENSIONAL_CUTOFF_051.md
- Object: r=u²E_G[τ^{−2}] for G=Q^jF, F∈V_n={P/(s+u)^n}, u=63/2.
- Result: PROVED (audited): (GENERAL) t r≤1+2√(d(d+2j)r), d=n−1, t=2j−1; (LINEAR) for all n≥1, j≥⌈7n/6⌉: r<49/20, E τ^{−2}<1/405, ARCH/‖G‖²>859/800; cutoff J(n,b) for any margin h.
- Remainder: the indices j<⌈7n/6⌉, the polar and all contacts; the weighted trace 010 that pays for contacts grows with dimension. Not a sign cutoff for W.
- Reusable PROVED: GENERAL/ROOT/LINEAR/ARCH-b, for all real or complex numerators, archimedean part only.

### 5. POWER_DIRECT_RECIPROCAL_TURAN_097.md
- Object: h(x)=u²M(u)/[au−M(u)], x=u², a=M′(0); T_h=2h′h‴−3h″².
- Result: PROVED the formula (DIRECT) T_h=a[auN_S−4C_h]/[16u³(au−c)^4], the analytic regularization at the origin, T_h(0)=(12a/b_1^4)·det Hankel₃(a,b_1,…,b_4) (ORIGIN-HANKEL) and T_h>0 for all u≥512 (DIRECT-TAIL). Compact range 0<u<512 OPEN in this round (closed later in 099).
- Remainder: joint bound of auN_S−4C_h on 0<u<512; sign of ORIGIN-HANKEL not computed. Inheritance to the next level remains open.
- Reusable PROVED: DIRECT, COST C_h<4c³ for A≥128, T_h>0 for u≥512 (real datum, all contacts).

### 6. POWER_DIRECT_RECIPROCAL_TURAN_AUDIT_097.md
- Object: audit of 097.
- Result: APPROVED / PROVED formula and T_h>0 for u≥512; compact range and sign at the origin OPEN.
- Scope warning: does not give global T_h, R_G″ at all pivots, triples G_p, five/all generators nor new W/T coverage; the anchored lemma applies only if the whole segment between x and P lies in the proved domain.
- Reusable PROVED: confirms 097.

### 7. POWER_DISCRETE_BALANCE_027.md
- Object: joint kernel Ω(t) by floors (FLOOR), masses Σ K_N(n)=3/2 (SAMPLE), Σ K_N(nx)=G_N(x)=x^{−32}D_N(log x) (SCALES).
- Result: PROVED: Ω(t)≥ℓ−(4log t+9)/t, ℓ=1+γ/2−½log(4π)>1/50; Ω>9/1000 for t≥4096; (JOINT-TAIL) 0<(9/4000)∫_T^∞G_N≤∫_T^∞K_NΩ≤(7/4)G_N(T){T(logT+2)+3T²}; at N=129, 0<tail<10^{−36} (SCALE). Interior and sign of W OPEN.
- Remainder: ∫_1^{4096}K_129Ω (interior); two scalar masses do not force the pairing (bump near 3/2 where Ω<−0.1).
- Reusable PROVED: OMEGA-TAIL and JOINT-TAIL for the real gamma K on x≥exp(τ_N).

### 8. POWER_DIVISOR_COMPARISON_034.md
- Object: atoms f_{N,k} (rows N, columns k), comparator B_N+S_K of 033.
- Result: PROVED (audited): for all N≥3, k≥1, u≥63/2, u²≥225N/4: W[f_{N,k}]>(1/40)‖f‖² (NEW-REGION); k≥2 margin >3/20. Corollaries: at u=63/2 rows 3≤N≤12 for all k≥0 (margin >10^{−4}); for all u≥63/2 rows 3≤N≤8 uniformly (margin >10^{−3}).
- Remainder: k=0 for N≥13 at fixed rate; interior N≥18; range N/u² near 2/9.
- Reusable PROVED: NEW-REGION (individual atoms, not combinations), ARCH>7/200 and ARCH2>19/40, |POLAR|<9/1000.

### 9. POWER_EFFECTIVE_HIGHPASS_054.md
- Object: high-pass orbit Q^jF_0, Q=s/(s+u), u=63/2, F_0=P/(s+u)^n, deg P<n.
- Result: PROVED (audited): for every nonzero real P and every j≥K(n)=max{10000n², A_n·3^{4D_n+20}} (C_n=9n²9^n, D_n=10C_n n!, A_n=6C_n n n!): W[Q^jF_0]>‖Q^jF_0‖² (EFFECTIVE). Includes contour STRIP≤D_n, bound on the full comb, polar <‖·‖².
- Remainder: all indices j<K(n) (the cutoff is enormous); gives no sign of the table nor window T.
- Reusable PROVED: EFFECTIVE (variable dimension, all numerators); MOMENTS M_r≤Γ(r+½); |c_{Q^jF_0}(t)|≤D_n e^{−15t}‖·‖².

### 10. POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md
- Object: audit of 054.
- Result: APPROVED; effectivization of the eventuality 015 via COEFF054 and the scalar contour 017; two weights only in dimension 1.
- Remainder: segment j<K(n) and global sign, explicitly outside.
- Reusable PROVED: confirms 054.

### 11. POWER_ENERGY_AUDIT_041.md
- Object: audit of ENERGY_BAND_041 and of its §7 (periodic expansion of B).
- Result: APPROVED; BAND uniform for N≥2^80; SAWTOOTH and PERIODIC-ERROR approved as a classical expansion, not a sign principle.
- Remainder: the complement before and after the band and its balance with ARCH_♯.
- Reusable PROVED: confirms 041.

### 12. POWER_ENERGY_BAND_041.md
- Object: moving energy band [e^T,e^{T+L}], T=2dv/(u²−v²), L=√N/100, full Möbius inverse h_N, B(x)=log(⌊x⌋!)−xH_{⌊x⌋}+⌊x⌋.
- Result: PROVED BAND: for all N≥2^80, 2∫_{e^T}^{e^{T+L}}h_N B dx<−C_N/25600 (favorable in W/‖·‖²=ARCH_♯−2∫hB). Also SAWTOOTH B=−γx−B_1(θ)log x+κ+E, −1/x<E<1/(2x), and PERIODIC-ERROR.
- Remainder: complement of the band (interior before T and other bands); the total residue W may be much smaller than each energy.
- Reusable PROVED: BAND, B-REAL |B+γx|≤log x+1, SAWTOOTH, ELEMENTARY-EM, PERIODIC-ERROR.

### 13. POWER_ENERGY_GROUP_037.md
- Object: dilation D_N(m)=mH_N(mx_N)/H_N(x_N) at the energy center t_N=d/992; groups K_{N,Q}(m)=Σ_{b|Q}μ(b)D_N(mb).
- Result: PROVED: (CENTER), (DILATE) m^{−1}e^{−M_N(...)}≤D_N≤m^{−1}(1+M_N ℓ); falsifier ABS-FAIL: Σ_{m≥2}|μ(m)|D_N(m)>1 for all N≥2^16 (refutes absolute contraction); SIGNED and WINDOW (positive finite groups); §8 with Q=∏_{p≤N^{1/8}}p: positive groups but GROW-ABS Σ|μ||K|>37/25 >K(1)<0.505.
- Remainder: the exterior signed sum FULL Σ_{(m,Q)=1}μ(m)K_{N,Q}(m); the majorant (log m)²/m is not summable.
- Reopening: a signed bound of the complement without summing a nonsummable error.
- Reusable PROVED: DILATE, SIGNED, WINDOW; NO-GO of absolute contraction (even after grouping with growing Q).

### 14. POWER_EXACT_H_GLOBAL_AUDIT_099.md
- Object: audit of the global certificate of T_h (099).
- Result: APPROVED / PROVED (FULL PASS 2048 panels on [0,512], fixed hash): T_h(x)>0 for all x>0 with the real Φ; the reciprocal data R_G, S_G of G_p are strictly concave for all p,x>0; all distinct triples of G_p PD; anchored block {0,p,z_1,z_2,z_3} PD.
- Scope: node 0 corresponds to exponent ½, outside the carrier; does not prove five arbitrary admissible generators nor Turán inheritance nor all orders; 090 (generic counterexample), 091, 092 remain in force.
- Reusable PROVED: T_h>0 globally; triples of the remainder G_p PD; anchored auxiliary five-node block PD.

### 15. POWER_EXACT_H_GLOBAL_DESIGN_099.md
- Object: entire functions U(x)=E′(u)/u, V(x)=[aE(u)−U(x)]/u²; S(u)=Ñ(u)/u^15=(16/a)NUM_x(u²) entire and even (ENTIRE-S), NUM_x=V^4T_h; gauge G_c=exp[−4M(c)(u−c)]S/E(c)^4.
- Result: PROVED (interval certificate 2048 panels on [0,512], FULL PASS; reproduced): T_h(x)>0 for all x>0 (spliced with 097 and 098), for the real Φ with full arithmetic.
- Remainder: no Turán inheritance to the next remainder is inferred, nor iteration to all orders, sign of W nor window T; the temporal Wronskian 093/095 (stronger) still has no global sign.
- Reusable PROVED: T_h>0 globally; regularized entire representation S; bound CAUCHY-S |S|/E(c)^4<2^151.

### 16. POWER_EXACT_H_ORIGIN_AUDIT_098.md
- Object: audit of the jet at 0.
- Result: APPROVED: H_3>0 (≈1.738·10^{−21}) and T_h(0)>0 (≈3.155·10^{−5}) for the real Φ, certified NUMERICAL (Arb intervals, 128 panels, reproduced).
- Remainder (in this round): intermediate interval OPEN (closed in 099).
- Reusable PROVED: T_h(0)>0 with a>0, b<0.

### 17. POWER_EXACT_H_ORIGIN_DESIGN_098.md
- Object: T_h(0)=12aH_3/b^4, H_3=det[[a,b,c],[b,c,d],[c,d,e]] with normalized cumulant coefficients (κ_{2j}) of Φ/Z(0); six even moments I_0..I_10.
- Result: PROVED AT A POINT (interval certificate): T_h(0)>0, neighbourhood without certified radius. Values a≈0.04621, b≈−7.43·10^{−5}.
- Remainder: the compact range 0<u<512 in this round; no global sign nor sign of W.
- Reusable PROVED: T_h(0)>0; temporal tail ∫_2^∞ t^rΦ<2^{−138} (r≤10).

### 18. POWER_FIVE_AUDIT_010.md
- Object: audit of FIVE_GLOBAL_010.
- Result: PROVED / PASS: W>0.01‖f‖² on all spaces of five real poles ≥31.5, with repetition, without separation.
- Remainder: fixed dimension; does not extend to six nor to all orders.
- Reusable PROVED: confirms 010.

### 19. POWER_FIVE_GLOBAL_010.md
- Object: f with Laplace transform P(s)/∏_{j≤5}(s+v_j), v_j≥63/2, deg P<5.
- Result: PROVED (rational certificate): W[f]>(1/100)‖f‖² (FIVE); BASE5 AP>(19/100)‖f_0‖²; AP5 AP>(1/50)‖f‖² by transport; comb |Comb|<1/100 with all-pass weight σ=21, B_5=(49^5−1)/16.
- Remainder: dimension 12 needs an arithmetic contribution with sign; no uniform constant as dimension grows.
- Reusable PROVED: FIVE (includes mixtures of up to five powers X^{−a}, a≥32, and confluent limits); transport identity AP[f]−c‖f‖²=R_0(...)+∫(R−R_0)(m−c)|F_0|²+(r_0−R_0)Polar.

### 20. POWER_FIXED_BLOCK_ASSEMBLY_AUDIT.md
- Object: audit of the obstruction by PSD blocks of bounded support.
- Result: APPROVED; exclusion only in the original basis and for fixed k.
- Reopening (not excluded): another basis, growing size, dense global PSD part, Schur, signed controls of cross terms.
- Reusable PROVED: confirms the obstruction.

### 21. POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md
- Object: certificates C=ΣB_α, B_α PSD supported on ≤k coordinates of the ladder a=32+m; necessary condition 1ᵀC1≤k·tr C.
- Result: NO-GO PROVED (class: sums of PSD matrices of fixed support ≤k in the power basis, closed under limits and diagonal congruences): for each k there is a block of nodes a_j=32+2N+2j, j=0..k, with C_ij→1 violating NECESSARY; scaled diagonal dominance also fails.
- Falsifier: the normalized block of the real ladder itself (does not prove a negative direction).
- Reopening: general changes of basis, blocks of growing size, Schur, dense global PSD part.
- Reusable PROVED: L(a_j)=½log N+O_k(1); LOCAL/NECESSARY condition.

### 22. POWER_FIXED_GRID_003.md
- Object: fixed ladder a_j=32+j, K_ij=(L_i+L_j)/(s_i+s_j), s_j=63/2+j; congruence to B_ij=(1−q_iq_j)/(1−x_ix_j), x_j=j/(63+j), q_j=(L_j−L_0)/(L_j+L_0); elimination recurrence (E) with parameters α_r.
- Result: PROVED: K_n PD ⟺ α_0..α_{n−1} defined and |α_r|<1 (finite algebraic identity); orders 1–6 certified (rational intervals): sign for every real mixture of X^{−32},…,X^{−37}. Algebraic falsifier: s=(1,5/3,3), L=(1,3/2,121/79): L increasing, L/s decreasing, all 2×2 minors >0, det K=−332001/391435520<0.
- Remainder: |α_r|<1 for all r with the real L(32+j); no alternation law nor uniform bound.
- Reopening: a sign remainder preserved under (E).
- Reusable PROVED: Schur/Pick criterion via (E) on the ladder; first six orders.

### 23. POWER_FOUR_GENERATORS_085.md
- Object: N_R, N_S (Turán obligations of R(x)=u/M(u), S(x)=uM(u)) on the compact range ½≤u≤127.5.
- Result: PROVED (certificate 16384 panels, FULL PASS, reproduced): T_R,T_S>0 for all u≥½; with Rolle (084), factorization (083) and minors (080): full W positive on every nonzero combination of up to FOUR powers X^{−a_i}, a_i>1 arbitrary (ARCH, polar and all contacts).
- Remainder: five generators, all orders, full envelope; higher Pfaffian obligations OPEN.
- Reusable PROVED: positivity for four arbitrary generators a_i>1.

### 24. POWER_FOUR_GENERATORS_AUDIT_085.md
- Object: audit of 085.
- Result: APPROVED / PROVED (matching hash). Extends small/mixed exponents beyond the large-rate region 053.
- Remainder: five generators and higher orders OPEN.
- Reusable PROVED: confirms 085.

### 25. POWER_FOUR_GLOBAL_009.md
- Object: spaces of four real poles v_j≥63/2 (with repetition); deficit transport by the filter H=∏(s+u)/(s+v_j).
- Result: PROVED: W[f]>(2/25)‖f‖² (FOUR); AP4 AP>(1/10)‖f‖²; (NEG) m≥1/10 for τ²≥81 and τ²(1/10−m)_+<23; comb <13/1000 with B_4=32552.
- Remainder: growing dimension: BASE can fail without a positive arithmetic contribution (dimension 12).
- Reusable PROVED: transport identity (ID) and coercive bound; FOUR.

### 26. POWER_FOUR_GLOBAL_AUDIT_009.md
- Object: audit of 009.
- Result: PROVED / APPROVED; exact bracket 3669270349/93389776200>3/100.
- Remainder: five poles or arbitrary dimension are not inferred.
- Reusable PROVED: confirms 009.

### 27. POWER_FOUR_TURAN_084.md
- Object: four-node Pfaffian, A_{f,ij}=[f(x_j)−f(x_i)]/(u_i+u_j); Pf(A_f)=−D_f/P (PF-DET), D_f=det[1,x_i,f,x_if]; det K=Pf(A_R)Pf(A_S)/∏R(x_i).
- Result: PROVED: global criterion via Rolle: f′>0, f″<0, T_f=2f′f‴−3f″²>0 on the interval ⇒ Pf(A_f)>0 for every quadruple; OUTER-TURAN N_R>¼, N_S>19/4 for A≥128. Inheritance falsifier: R=1+x−x²/16, S=x/R (RS=x, concavities, triples PD) with det K_4=−ε³V²/[∏R]²<0.
- Remainder (in this round): compact range ½<u<127.5 (closed in 085); or pay for the product of Pfaffians without individual signs.
- Reusable PROVED: PF-DET; sufficient Rolle criterion; REAL-TURAN; bounds on P_j(A).

### 28. POWER_FOUR_TURAN_AUDIT_084.md
- Object: audit of 084.
- Result: APPROVED / PROVED as a sufficient criterion, class falsifier and exterior application. The criterion is sufficient, not necessary for each Pfaffian.
- Remainder: compact range pending in that round; no new W/T coverage (tail already covered by 053).
- Reusable PROVED: confirms 084.

### 29. POWER_FRONTIER_AUDIT_036.md
- Object: audit of RECURRENCE_BOUNDARY_036 and MOVING_BALANCE_036.
- Result: APPROVED: full diagonal frontier 0≤C_L≤M_L(H_L+0.002)=O(log L/√L) on the parabolic cone; stopped frontier (SURVIVAL with positive probability; the region 034 N′≤17 is inaccessible from N≥18); energy window: both real energies (polar and prime) concentrate at m/d→1/32 with coinciding phases λ^N; CHEB ψ≥x/2−16 for real Λ.
- Remainder: the signed lower bound of the complement R_L; Π/P→1 or precision of the residue is not deduced; compensation within the signed functional before averaging not refuted.
- Reusable PROVED: energy bounds of the parabolic cone; concentration m/d→1/32.

### 30. POWER_FULL_THIRTEEN_053.md
- Object: spaces of thirteen real poles v_i≥63/2, numerator P of degree<13; gain ZERO14 (fourteen poles with D(0)=0).
- Result: PROVED (certificate: 95 rational LDLs j=1..95 plus analytic tail j≥96, audited): W[P/∏_{i≤13}(s+v_i)]>‖·‖²/4000 (TARGET); W>‖·‖²/1000 on fourteen poles with zero numerator.
- Remainder: arbitrary dimension; fourteen poles with general numerator; the tail majorant from n=3 (0.0464) is insufficient for E2, which is why contact 3 is kept.
- Reusable PROVED: TARGET (13 poles); ZERO14; identity FULLTEL with κ_j≥0.

### 31. POWER_FULL_THIRTEEN_AUDIT_053.md
- Object: audit of 053.
- Result: APPROVED (reproduction exit 0, 95 LDL PASS, B_T14=947334302964<973312²).
- Remainder: neither arbitrary dimension nor temporal window.
- Reusable PROVED: confirms 053.

### 32. POWER_FULL_TRANSFER_PLAN_050.md
- Object: plan MULTI with contacts {2}, {2,3}, {2,3,4}; MULTI-E2: E2[F]>‖F‖²/2500 on all twelve poles ≥u.
- Result: EXPLORATION SUPERSEDED by FULL_TWELVE_050; PROVED MULTI-E2 (ARCH+POLAR+contact 2) and TAIL-M (tail majorant from M). The obligation NEXT (E_{2,3}≥‖·‖²/2500 on the whole orbit) remained OPEN and was later avoided; «do not treat NEXT as a live obligation».
- Remainder: none of its own in force.
- Reusable PROVED: MULTI-E2; bound TAIL-M with B=1282776893780652.

### 33. POWER_FULL_TWELVE_050.md
- Object: twelve real poles v_i≥63/2, deg P<12; ZERO13.
- Result: PROVED (audited): W[f]>‖f‖²/10000 (TWELVE); ZERO13: W>‖·‖²/250 on thirteen poles with D(0)=0; ORBIT E2[Q^jF_0]>‖·‖²/50 for j≥1.
- Remainder: thirteen poles with general numerator (closed in 053), arbitrary order, global bridge of growing blocks.
- Reusable PROVED: TWELVE; ZERO13; ORBIT; B_T13=109543953194.

### 34. POWER_FULL_TWELVE_AUDIT_050.md
- Object: audit of 050.
- Result: APPROVED; thirteen PASS; tail ≤2942000/186535791<2/125.
- Reusable PROVED: confirms 050.

### 35. POWER_GAMMA_129_AUDIT_061.md
- Object: audit of the decision of the atom N=129, k=0.
- Result: APPROVED; W/‖g‖²∈[13456684165,13456684168]/10^{20}; benefit of the cells n≥3 between 0.3755 and 0.3822.
- Remainder: does not decide rows, blocks, arbitrary orders nor window.
- Reusable PROVED: confirms 061.

### 36. POWER_GAMMA_129_DECISION_061.md
- Object: atom g_129(t)=t^{128}e^{−ut}/128!, u=63/2.
- Result: PROVED (rational certificate): 1.34·10^{−10}<W[g_129]/‖g_129‖²<1.35·10^{−10}; −ERR≈1.04219397031519 and −ARCH_♯≈1.04219397018063 (cancellation to 10^{−10}); K_129(1)<0 did not imply W<0.
- Remainder: propagation in N; the signed balance must be preserved with precision relative to the residue; does not rehabilitate universal K≥0.
- Reusable PROVED: sign of the atom (129,0); 0.3755<2Σ_{m≥3}S_129(m)<0.3822.

### 37. POWER_GAMMA_AFFINE_AUDIT_062.md
- Object: audit of the affine diagnosis 062.
- Result: APPROVED; R is the full global residue of 042; ABS-TAIL (N≥2^80) does not apply to 129; R obtained from ERR061, not an independent estimate.
- Remainder: control of the interior signed balance as N varies.
- Reusable PROVED: confirms 062.

### 38. POWER_GAMMA_AFFINE_BALANCE_062.md
- Object: AFF=ARCH_♯+2γ−βJ_1, β=log(2π)−1−γ; W/‖g_129‖²=AFF−2R (EXACT), R full renormalized residue.
- Result: PROVED (certificate): AFF<−1/100 (≈−0.0604), R<−1/200; pointwise NO-GO: the affine part 042 is not a positive base at N=129.
- Remainder: R (of order 0.03) against W (of order 10^{−10}); uniform cells–ARCH_♯ comparison OPEN.
- Reopening: any continuation from the affine part must genuinely estimate the full residue.
- Reusable PROVED: the BOXES (only N=129).

### 39. POWER_GAMMA_BALANCE_030.md
- Object: real gamma law V=β/G, G~Gamma(b,1), β=u²/4, b=N−½; L_N(a)=E(V−a)_+−(m−a)_+; G_W(v) full form of the Gaussian test; identity FULL-GAP W[g_N]/‖g_N‖²−G_W(m)=∫L_N G_W″.
- Result: PROVED: SHARP-GAP 0<A_♯(m)−ARCH_♯[g_N]/‖·‖²≤½[ψ(b)−log(b−1)]<1/(2(b−1)) for all N≥2. Falsifier (N=2, u=63/2): W[g_2]/‖·‖²<17/20, G_W(u²/2)>7/8, ∫L_2G_W″<−1/40 (NEG-GAP): refutes «the gamma test dominates the Gaussian with the same second moment».
- Remainder: the signed change of ERR together with the loss; the full pairing L_N G_W″.
- Reusable PROVED: SHARP-GAP (lower bound of the sharp part with cost O(1/N)); digamma lower bound Re ψ(a+it)≥log|a+it|−Re[1/(2(a+it))]−1/(6a²).

### 40. POWER_GAMMA_WEIGHT_031.md
- Object: R(t)=ρ(t)−(2/3)ρ′(t), maximum T_N; primitive I_*(X)=∫_1^X(3/2)x^{−½}H(x)dx with H(x)=1+[log((x+1)/(x−1))+c_0−1−2Ψ_1(x)]/x², Ψ_1(x)=Σ_{q≤x}qΛ(q).
- Result: PROVED (audited): T_N≤(2/3)d/(d+20), q″<0, PEAK 0<R(T_N)−1≤2M_2/9, M_2=u²/(2N−3); BUDGET W[g_N]/‖·‖²≥∫_{T_N}^∞I_*(e^t)[−R′]dt−M_2; sufficient criterion E_ν[I_*]>M_2/R(T) (not proved).
- Remainder: I_* takes negative values after 3 (WEIGHTED_BLOCK031); a signed arithmetic inequality for E_ν[I_*] is missing.
- Reusable PROVED: PEAK, BUDGET, concavity of q, IBP identity without boundary.

### 41. POWER_GEOMETRIC_TRANSFER_015.md
- Object: one-pole iteration W[f_v]=ρΣ_{k≤K}a^kW[h_k]+a^{K+1}W[g_{K+1,v}], ρ=u²/v², a=1−ρ; topology X=H^t∩L²(e^{ηy}), 0<t<½, ½<η<u/2.
- Result: PROVED (u>1): W continuous on X; Q^k f→0 strongly; mixture (MIX) and (MULTI) W[f]=Σw_kW[Q^kf_0] with w_k≥0, Σw_k=1; archimedean quotient nondecreasing in k; Polar[h_k]=[−1/(4u²−1)]^kPolar[h_0].
- Remainder: positivity of the initial blocks of the orbit Q^kV_N (finite segment for each N, without a universal effective endpoint).
- Reusable PROVED: MULTI (sufficiency: the whole high-pass orbit positive ⇒ all N poles ≥u); continuity on X.

### 42. POWER_GRAM_SLICES_AUDIT.md
- Object: audit of GRAM_SLICES_OBSTRUCTION (outside the range to be summarized; its audit is in the range).
- Result: APPROVED: refutes only that all layers (disintegration in v=σ²−τ²) are PSD; gain (β−α)²f(R)/R³ divergent; addendum: hazard criterion with negative diagonal by 073; Gaussian multiplier B_op(−Φ′)=tΦ does not control the half-line term of Q_A.
- Remainder: PSD of the integral OPEN; control compensation between layers or build another Gram.
- Reusable PROVED: none new (confirms the layer obstruction).

### 43. POWER_GREEN_PAIR_TP2_AUDIT_111.md
- Object: audit of 111 (balanced Green functions V_p, compact pair J,K).
- Result: APPROVED (base, strict extension r_ε, CM extension in x=p²).
- Remainder: CM of the real family is not claimed nor is a method with more structure excluded.
- Reusable PROVED: confirms 111.

### 44. POWER_GREEN_PAIR_TP2_SCOPE_111.md
- Object: K=1_{|t|<2}, J=[1+1_{1<|t|<2}]K; λ_p=2−1/(2cosh p); V_p balanced Green function with V_p″−p²V_p=J−λ_pK.
- Result: NO-GO PROVED (class: even compact pairs with J/K nondecreasing, even strictly increasing, all V_p>0 with V_p/K decreasing, even with complete monotonicity of V in x=p²): they do not imply TP2; minors OPPOSITE-MINORS of opposite signs with p=1,2 at t∈{¼,½} and {3/2,7/4}.
- Falsifier: the explicit pair (it is not the real Φ; it does not satisfy J′=−tΦ, K″=aΦ−J nor MIXED4).
- Reopening: an induction using the real compatibility J′=−tΦ, K″=aΦ−J or MIXED4.
- Reusable PROVED: COMPLETE-MONOTONICITY for the counterclass; explicit minors.

### 45. POWER_GROUP_AUDIT_037.md
- Object: audit of ENERGY_GROUP_037.
- Result: APPROVED (core, ABS-FAIL, SIGNED/WINDOW and choice of growing Q).
- Remainder: the signed arithmetic complement and its integration with sufficient precision.
- Reusable PROVED: confirms 037.

### 46. POWER_HIGH_ORDER_PM_NOGO_007.md
- Object: f_{n,u}=y^{n−1}e^{−uy}; normalized polar P_n(u)=4^n/[u·binom(2n−2,n−1)](1−1/(4u²))^{−n}; lemma (G) 0≤τm′(τ)<4.
- Result: PROVED / NO-GO: for u=63/2, n=2^17: uE_n′(u)<−140/31 (NEG); increasing a single pole reduces the ARCH+POLAR quotient. FALSIFIED «individually increasing poles ≥63/2 does not reduce the arch+polar quotient of any numerator, uniformly in n».
- Scope: does not refute transport preserving only the sign, nor n=4, nor monotonicity of λ_min; does not include the comb.
- Reusable PROVED: (G) and exact polar formula (P).

### 47. POWER_HIGHPASS_015.md
- Object: orbit f_{k,P} with F=[s/(s+u)]^kP(s)/(s+u)^N, u>1, deg P<N.
- Result: PROVED (audited): EVENTUAL: there is K_N (independent of P) with W[f_{k,P}]>0 for all k≥K_N; uniformly Arch/‖·‖²≥½log k−C_N, Comb/‖·‖²→0, Polar/‖·‖²→0; for fixed P ASYM W/‖·‖²=½log k+log(u/2π)−½ψ(r−½)+o(1).
- Remainder: sign of the first k; K_N not uniform in N; tail positivity does not imply positivity of the mixture.
- Reusable PROVED: EVENTUAL, GRAM/LIMIT, WT ‖e^{ηy}f‖²≤C_{N,η}‖f‖², ASYM.

### 48. POWER_HIGHPASS_AUDIT_015.md
- Object: audit of HIGHPASS_015 and GEOMETRIC_TRANSFER_015.
- Result: PROVED: two tools (exact full mixture and uniformly positive high-pass tail for each fixed N); they reduce the sufficient condition to the sign of a finite segment of initial blocks.
- Remainder: effective endpoint of the segment and its sign for all N; a mixture may contain negative initial terms.
- Reusable PROVED: confirms 015.

### 49. POWER_HIGHPASS_CUTOFF_049.md
- Object: cutoff J=32 for E2 on Q^jV_12; lemma JAC αR≤β+1+2√(m(m+α+β+1)R).
- Result: SUPERSEDED DRAFT (by CENTERED_CUTOFF_049, cutoff 14, and R12_TRANSPORT_049); «do not record this cutoff 32 as an additional result». Contains the proof of JAC and TAIL E2>(99/1000)‖·‖², j≥32.
- Remainder (historical): blocks j=1..31.
- Reusable PROVED: the lemma JAC (weighted polynomials) is a self-contained proof, although the document is superseded.

### 50. POWER_HIGHPASS_DIAGONAL_DENSITY_094.md
- Object: E_{n,r}=Q^rV_n(u) ↔ S_{n,r}={(1+z)^rP(z): deg P<n} in H² (CAYLEY); exact distance dist(1,S_{n,r})²=1−A(n,r), A=[(n+r−1)!]²/[(n−1)!(n+2r−1)!].
- Result: PROVED (audited): BINOMIAL-DET by Dodgson; e^{−r²/n}≤A≤e^{−r²/(n+2r−1)}; DIAGONAL-DENSITY: the union ∪E_{n,r(n)} is dense in L² ⟺ liminf r(n)²/n=0; density NO-GO: the union of blocks with r≥n (including the cone 060 r≥10^{12}[n⌈log_2(n+1)⌉]³) is at distance >½ from 1, even adding finitely many confluent blocks.
- Remainder: linear envelope of the union, cross terms between blocks, continuity of W in the topology used.
- Reopening: a positive cone with r=o(√n) along a subsequence, plus continuity of the full form.
- Reusable PROVED: EXACT-DISTANCE, BINOMIAL-DET, DIAGONAL-DENSITY, POLYNOMIAL-APPROX.

### 51. POWER_HIGHPASS_DIAGONAL_DENSITY_AUDIT_094.md
- Object: audit of 094.
- Result: APPROVED / PROVED.
- Remainder: the non-density of the cone does not exclude its linear envelope, cross terms, signed control, mixtures or compensated descent.
- Reusable PROVED: confirms 094.

### 52. POWER_HYPERBOLIC_MODEL_GRAM.md (71 KB, 13 sections)
- Object: model φ_a(t)=exp(−a cosh 2t), Z_a=y_{u²/4}(0), y_x″=[a²e^{2r}+x]y_x; H=−D_r²+a²e^{2r} (Dirichlet), M_a(u)/u=½Tr(H+u²/4)^{−1} (REP).
- PROVED results (with their class): §5 GRAM: K_ij=(M_a(u_i)+M_a(u_j))/(u_i+u_j) PSD at all sizes (sum of HS squares) for the model; §8 Robin extension φ_{a,β}=[β+a cosh 2t]e^{−a cosh 2t} also PSD. NO-GO: §7.1 Φ is not a positive mixture ∫e^{−a cosh 2t}dμ(a); §7.2 Φ≠φ_a∗ν (ν≥0 finite); §9 the flow −a∂_aK_a is not PSD at all sizes (NEG-MOM); §10 a fixed prefactor q does not give a scalar potential independent of ν (except q constant); §10.1 with first derivative only q=C or C cosh(v/2), excluded for the real q (also with variable spectral weight and change of scale); §11 Φ≠C e^{−a cosh 2t}∏cosh(α_jt) (c_1=π−3/(2π)∉ℕ); §11.4 nor locally uniform approximation at fixed scale 2π; §12 finite vector of fixed prefactors without drift; §12.1 with matrix drift (rational annihilator impossible); §12.2 symmetric infinite dimension without drift (‖Q‖²=A+c log cosh v); §12.3 constant scalar drift (kernel DRIFT-K, even cusp w=2i); §12.4 scale-dependent scalar drift forced to be constant; local metric impossible for the 2×2 example; §12.7 the realization 12.6 admits no compatible bounded positive local metric; §13 shifted cosh products (−1<c<1) give an entire limit, incompatible with the even cusp; §13.1 also with variable scale a_n.
- Additional positive PROVED: §12.5 the operator drift determines L=[G(v+z)+G(v−z)]/2, G=−coth(t/2)F′; §12.6 explicit realization Q,B,C,D in H=L²(ρdω)⊕ℝ³ (ρ=sech(πω/2)) with exact continuous observation ⟨Q(v),h⟩=q_θ(v) and strong equation Y_rr=(b²+ν²)Y+2DY_r+(−C+2bB̄)Y, ⟨Y_ν(2π),h⟩=Z(2ν).
- Remainder: a metric (nonlocal or unbounded) and a POSITIVE Green identity reproducing the full form; the comparison K_Φ≥εK_{2π} is refuted (GLOBAL).
- Reopening (declared): nonlocal or unbounded metrics, new connections, b-dependent prefactors, noncontinuous observations, other realizations; variable base frequency scales, real powers, sums, quotients, relative comparisons of forms.
- Reusable PROVED: Green/trace of the model; THETA-TAIL Φ(t)~2π²e^{9t/2}e^{−πe^{2t}}; even cusp expansion; realization 12.6.

### 53. POWER_INFINITE_SHOULDER_039.md
- Object: full arithmetic inverses h_N, K_N=J_N+xh_N (full Möbius) at the shoulder x=e^{t_v}, t_v=2dv/(u²−v²), v=½+δ, σ=v+½>1; operator M_σf(ℓ)=U_σ^{−1}Σμ(n)n^{−σ}f(ℓ+log n).
- Result: PROVED (audited): ψ_Λ(x)≤2x for all x≥1; A_σ≤2σ/δ, B_σ≤2σ/δ²; (INFINITE) |M_σf(0)−f(−A_σ)|≤12000B_σ/N+…; SHOULDER (9/10)U_σ<h_N/H_N, K_N/G_N<(11/10)U_σ; TAIL: for all N≥4·10^6 and x≥e^{T_N}, T_N=d/992+O(√N): h_N(x)>0, K_N(x)>0.
- Remainder: interior region (critical center δ→0, σ=1 not reached); comparison of the favorable tail of F_N=2∫h_NB with the adverse interior part and ARCH_♯; precision of the polar−comb residue.
- Reusable PROVED: ψ_Λ(x)≤2x elementary; MOMENTS; SHOULDER/TAIL (positivity of the full inverses on x≥e^{T_N}).

### 54. POWER_INTERIOR_017.md
- Object: row N=1, F_k(s)=s^k/(s+u)^{k+1}, u≥63/2; weighted norm N_k(η).
- Result: PROVED: (WR) ‖e^{ηy}h_k‖²/‖h_k‖²≤(u−η)/(u−2η) for all k≥0 (generating function GEN and Vandermonde c_{k−j}c_j≤c_k); ROW1 W[h_k]>(4/3)‖h_k‖² for all k≥0, u≥63/2; §7 WRN: ‖e^{ηy}f_{N,k}‖²/‖f_{N,k}‖²≤R_N(u,η)=(u/a)^{2N−1}S_N(ρ), S_N rational, for all rows, uniform in k.
- Remainder: the joint regime k/N finite with growing N; the N-dependence of R_N is not enough for the table.
- Reusable PROVED: WR, W11, ROW1, WRN; exact polar Polar[h_k]=2(−¼)^k/(u²−¼)^{k+1}.

### 55. POWER_INTERIOR_AUDIT_017.md
- Object: audit of the scalar table: scalar Bernstein bridge (SCALAR_BRIDGE_017), row N=1, WRN, quadratic cone (QUADRATIC_017 and QUADRATIC_EXPLICIT_017).
- Result: PROVED the specific results: Bernstein bridge: W[f]+εW[f_1] is a positive sum of atomic values W[h_{N,k}], so the COMPLETE scalar table (all atoms (N,k)) is SUFFICIENT; ROW1; WRN; quadratic cone: eventual positivity for P=1 on k≥cN², N≥N_0(c); explicit: W>(49/50)‖f‖² for all N≥2, k≥10000N², u=31.5, P=1. Sign of the whole scalar table OPEN.
- Remainder: the atoms (N,k) outside row 1 and the quadratic cone.
- Reusable PROVED: scalar Bernstein bridge (reduction to atoms); explicit quadratic cone; lower bound m(τ)≥log(|τ|/2π)−4 and |m−log(|τ|/2π)|≤1/|τ|+1/(2τ²).

### 56. POWER_INTERIOR_AUDIT_030.md
- Object: audit of GAMMA_BALANCE_030 and INTERIOR_SCALE_030.
- Result: APPROVED: SHARP-GAP; falsifier NEG-GAP (N=2, only of the cost-free comparison); genuine interior block (x∈[1,9/4]): I_*>0.02, error <0.005 for N≥2^{20}, block >0.01; identity JOINT-G with H=1+[log((x+1)/(x−1))+c−1−2Ψ_1(x)]/x².
- Remainder: the rest [9/4,∞) uncontrolled; BLOCK is not total W.
- Reusable PROVED: confirms 030 and the formula for H.

### 57. POWER_INTERIOR_CONSTRAINT_027.md
- Object: real gamma mixture ρ_N(t)=E e^{−V_Nt²}, V_N=β/G, G~Gamma(N−½,1); W[g_N]/‖g_N‖²=E G_W(V_N) (WG); hinge weight L_N(a)=E(V_N−a)_+−(m_N−a)_+≥0; GAP δ_N(t)=t^4∫e^{−at²}L_N(a)da.
- Result: PROVED: UPPER ARCH_♯[g_N]/‖·‖²=E A_♯(V_N)<A_♯(EV_N) (Jensen goes in the WRONG direction for a lower bound); JOINT-GAP W[g_N]/‖·‖²−G_W(m_N)=∫L_N(a)G_W″(a)da; FAIL-CONVEX G_W″(v)<0 for all v≥65536. §8: by INV-MIX and the certificates 022/023 there exist a_h, a_K>0 with h_{a_h}(1)<0 and K_{a_K}(1)<0: the universal Gaussian premises h_a≥0, K_a≥0 are refuted.
- Remainder: G_W(m_N)+∫L_NR≥0, i.e., control one-sidedly the negative part of R=G_W″ against the real law L_N.
- Reusable PROVED: WG, GAP, JOINT-GAP, INV-MIX.

### 58. POWER_INTERIOR_SCALE_030.md
- Object: adjoint inversion H(x)=Σ_{m≤x}μ(m)Ω(x/m)/m=1+[log((x+1)/(x−1))+c−1−2Ψ_1(x)]/x², c=−γ−log 4π; JOINT-G W[g_N]/‖·‖²=∫_1^∞G_N H, G_N=x^{−32}D_N(log x).
- Result: PROVED (audited): BLOCK ∫_1^{9/4}G_N H>1/100 for all N≥2^{20} (u=63/2), with contact 2 included; PRIMITIVE-FAIL ∫_1^{5/2}H<−1/50 and ∫_1^{5/2}x²H<−1/4 (the positive-primitives criterion fails); G_N decreasing for N≥663, G_N/x² for N≥134.
- Remainder: ∫_{9/4}^∞G_N H (all subsequent contacts), uncontrolled.
- Reusable PROVED: formula H, JOINT-G, BLOCK, GAMMA-ERROR |G_N−G_*|≤(7/4)M2_N on [1,9/4].

### 59. POWER_INVERSE_COEFFICIENT_054.md
- Object: R(y)=y^{n−1}P(ia/y), a=u√j, weight w=(1+y²/j)^{−(n+j)}; ‖Q^jF_0‖²=a^{1−2n}D_{n,j}[R]/(2π).
- Result: PROVED (audited): COEFF (Σ|c_r|)²≤C_nD_{n,j}[R], C_n=9n²9^n, for every complex R and every j≥n; EVAL |R(z)R(−z)|≤C_nD·max(1,|z|^{2n−2}); identity DENSITY with the factor (−1)^{n−1}.
- Remainder (in the memo): contour integration and summable tail (developed in 054 EFFECTIVE).
- Reusable PROVED: COEFF/EVAL (effective conditioning depending only on n).

### 60. POWER_INVERSE_COEFFICIENT_AUDIT_054.md
- Object: audit of COEFF/EVAL.
- Result: APPROVED; does not prove a summable arithmetic tail nor the cutoff K(n); an IBP bound ∝1/t does not sum the comb; N′=1 is not imported from N′≥2.
- Reusable PROVED: confirms 054.

### 61. POWER_INVERSE_INTERIOR_022.md
- Object: full Möbius inverse h_128(1)=Σ_{m≥1}μ(m)m^{−32}A_128(log m), A_128 with positive rational coefficients.
- Result: PROVED (rational certificate, tail m≥65 <10^{−10}): −2/3<h_128(1)<−33/50<0. Falsifier: «h_N(x)≥0 for all N≥2, x≥1» is false; there is an interval to the right of 1 with h_N<0 and B<0 (genuine adverse contribution in F_N=2∫h_NB).
- Remainder: the total pairing F_N; W[g_128]<0 is not claimed.
- Reopening: signed budgets that do not assume h_N≥0 remain legitimate.
- Reusable PROVED: the certified value of h_128(1); exterior h_128≥H_128/4 for log x≥127/30 (cited from 020).

## A. Deduplicated «do not relaunch» list, with reopening condition, and cross-check with RULES_AVOID.md

Marks: **[ABSENT]** not listed in `RULES_AVOID.md`; **[PARTIAL/INEXACT]** listed with a different scope or condition
(both are quoted); **[PRESENT]** listed correctly.

A1. **Descent from exact partitions + positive mixture + eventual positivity at each fixed order**
(016 §5, AUDIT_016 §4). Falsifier: W_4=W−4‖·‖² preserves DEF/BIN/MULTI/EVENTUAL and W_4[e^{−63y/2}]<−‖·‖².
Reopening: «a descent controlling W[Lf] with the full arithmetic datum or using the spectral
distribution of the numerator» (016 §5); «an inequality controlling the defect of the initial blocks by
additional information» (AUDIT_016 §5). **[PARTIAL/INEXACT]** RULES_AVOID D4: «Recurrence or descent alone —
only with a signed arithmetic bound on the remainder R_L ≥ −ε_L». It does not mention the falsifier W_4 nor that the
bound must distinguish the real multiplier from the shifted one m−C (016: «even preserving Lambda exactly
is not enough if its interaction with the archimedean constant does not appear in that estimate»).

A2. **Density bridge via unions of high-pass tails** (AUDIT_016 §§2–3, §9; 094). (i) The union of
Q^kV_N, k≥1, lies in ℓ_0=0 (not dense in L²_η); (ii) with k_j→∞ every strong limit is 0; (iii) even
repairing the moment with an invertible filter Q_δ (dense span), «dense span in form norm + eventual individual
sign of its generators» does NOT imply sign (counterexample with W_4); (iv) in unweighted L² the
diagonal union is dense ⟺ liminf r(n)²/n=0, and even then continuity of the full form is missing.
Reopening: positive cone with r=o(√n) along a subsequence plus continuity of W in that topology; or specific
control of cross terms of the real datum. **[PARTIAL/INEXACT]** RULES_AVOID D3: «Inferring density or sign from a
positive union — only with liminf r(n)²/n = 0 and a block that repairs the moment (211/GLOBAL §4)». AUDIT_016
§9 shows that repairing the moment with individually positive generators is not enough: control of
cross terms is missing, and 094 additionally requires continuity of the full form.

A3. **Absolute contraction of the Möbius inversion**, also after grouping with growing Q (037 ABS-FAIL,
GROW-ABS). Reopening: «a signed bound of the complement, without summing a nonsummable error nor converting the sign
of a finite group into that of FULL». **[ABSENT]**.

A4. **Universal positivity of the full inverse** h_N≥0, universal K≥0, and their Gaussian versions h_a≥0,
K_a≥0 (022; 027 §8; 061 «does not rehabilitate universal K≥0»). Reopening: signed budgets that do not assume
that sign. **[ABSENT]**.

A5. **Comparison with the Gaussian of equal second moment / Jensen / convexity** (027 UPPER and
FAIL-CONVEX; 030 NEG-GAP). Jensen gives an UPPER bound on ARCH_♯; G_W″<0 for v≥65536; the gamma test does not dominate
the Gaussian (N=2). Reopening: control the negative part of R=G_W″ against the real law L_N, or the signed
change of ERR together with SHARP-GAP. **[PARTIAL/INEXACT]** RULES_AVOID D11 only says «Jensen /
operator concavity»; it does not record the global convexity of G_W nor the Gaussian comparison.

A6. **Positive-primitives criterion** for the weight H or I_* (030 PRIMITIVE-FAIL; 031: I_* negative after
3). Reopening: a signed arithmetic inequality for E_ν[I_*]>M_2/R(T). **[ABSENT]** (the «compensated
primitives of layers» of D16 is another object).

A7. **Affine part of the renormalized representation 042 as a positive base** (062: AFF<−1/100 at N=129).
Reopening: genuinely estimate the full residue R. **[ABSENT]**.

A8. **Separate bounds of constant order instead of the signed balance** (061: the cancellation is at 10^{−10};
ERR<−0.66 lost the benefit). **[PRESENT]** generically in RULES_AVOID B2.

A9. **Inheritance from pairs to triples and from concavities to four nodes** (003 §4: L increasing and L/s decreasing
are not enough for three; 084 §4: R=1+x−x²/16 preserves RS=x, concavities and triples but det K_4<0). Reopening:
a sign remainder preserved by the elimination (E) (003), or the quantitative TURAN condition (084).
**[ABSENT]** (the memory of the project rules cites 084 only for the Pfaffians by reciprocity).

A10. **Extending to the next dimension** the closures for 4, 5, 12, 13 poles by extrapolating margins
(009 §7, 010 §5, 050 §7, 053 §5) and declaring all initial segments of E2 positive (051 with the
falsifier n=2^17, F=(s²−¼)/(s+u)^n, E2[QF]<0). **[PRESENT]** as D2 («extend the tower of finite
orders»); the falsifier E2 **[ABSENT]**.

A11. **Assembly of PSD certificates of fixed support ≤k** in the power basis (FIXED_BLOCK_ASSEMBLY).
Reopening: another basis, blocks of growing size, Schur complements, dense global PSD part.
**[PARTIAL]** RULES_AVOID D12 names it without a reopening condition.

A12. **Dimension-uniform monotonicity of the ARCH+POLAR quotient when poles increase** (007, n=2^17).
Reopening: transport preserving only the sign. **[ABSENT]**.

A13. **Individual monotonicities (including complete monotonicity in x=p²) ⇒ TP2** for the family of
balanced Green functions (111). Reopening: use the real compatibility J′=−tΦ, K″=aΦ−J or MIXED4. **[ABSENT]**.

A14. **Hyperbolic model and transfers** (HYPERBOLIC §§7–13): positive mixture and positive convolution
(§7), scale flow −a∂_aK_a (§9), fixed prefactors with scalar potential, scalar/matrix drift,
symmetric infinite dimension (§§10–12.4), local metric for the theta realization (§12.7), cosh products
with or without shift and variable scale (§§11, 13). Declared reopening: nonlocal or
unbounded metrics with positive Green identity, new connections, b-dependent prefactors, noncontinuous
observations, other base frequencies, sums/quotients/real powers, relative comparisons of forms.
**[PRESENT]** in B4 («211/HYPERBOLIC §§6–13»), D15 (§12.7) and C1 («closures by cosh products»); the scale
flow §9 and the family of closures §§10–12.4 **[ABSENT]** as explicit entries.

A15. **Inferring density or mass from two scalar masses** (027 DISCRETE §1: a bump near 3/2 where Ω<−0.1
can carry the mass). **[ABSENT]** (minor).

A16. **Positivity in codimension one implies the block** (051, ZERO13: the Schur coupling is not
controlled). **[PARTIAL]** D5 deals with «Schur–Green monotonicities», not this coupling.

A17. **PSD layers of the Gram disintegration** (GRAM_SLICES_AUDIT). **[PRESENT]** via D16/memory of
the project rules.

Remark on D7 of RULES_AVOID («Variants of budget 022»): in this range `POWER_INVERSE_INTERIOR_022`
is a pointwise falsifier, not a budget; the reference of D7 seems to point to CUMULATIVE_INVERSE022
(outside this range). It should be made precise.

## B. PROVED positive results, with exact scope

B1. Exact filter identities (016): W[f]=W[Qf]+W[Lf], binomial, (−1)^rΔ^r W[Q^kf]=W[L^rQ^kf], for causal rational
f, polar included.
B2. Geometric mixture and continuity (015 GEOMETRIC): W continuous on X=H^t∩L²(e^{ηy}); for all v_j≥u>1,
W[f]=Σw_kW[Q^kf_0], w_k≥0, Σw_k=1: positivity of the whole orbit Q^kV_N suffices for all N poles ≥u.
B3. Eventuality (015 HIGHPASS): for fixed N there is K_N independent of P with W>0 on Q^kV_N, k≥K_N.
B4. Effective cutoff (054): W[Q^jF_0]>‖·‖² for all P, all n, j≥K(n) (enormous explicit integer). COEFF/EVAL.
B5. Linear archimedean cutoff (051): for all n and j≥⌈7n/6⌉, ARCH>859/800 (ARCH only).
B6. Row N=1 (017): W[h_k]>(4/3)‖h_k‖², all k≥0, u≥63/2; WR and WRN (weighted norms uniform in k).
B7. Scalar Bernstein bridge (AUDIT_017): if all atoms W[h_{N,k}]≥0 then W≥0 on all
numerators (reduction to the scalar table); explicit quadratic cone W>(49/50)‖f‖² for N≥2, k≥10000N²,
P=1.
B8. Atom region (034): W[f_{N,k}]>‖·‖²/40 for N≥3, k≥1, u≥63/2, u²≥225N/4; rows 3≤N≤12 at u=63/2
for all k≥0; rows 3≤N≤8 uniformly in u≥63/2.
B9. Fixed dimension, all rates ≥63/2 with repetition: 4 poles W>(2/25)‖·‖² (009); 5 poles
W>‖·‖²/100 (010); 12 poles W>‖·‖²/10000 (050); 13 poles W>‖·‖²/4000 and 14 poles with D(0)=0
W>‖·‖²/1000 (053).
B10. Ladder of powers: mixtures of X^{−32},…,X^{−37} (003, orders 1–6); four arbitrary powers
a_i>1 (085, via T_R,T_S>0 globally, Rolle 084, factorization 083); T_h>0 for all x>0 and all triples of the
remainder G_p PD, anchored auxiliary five-node block PD (099; these are not five admissible generators).
B11. Atom (129,0): 1.34·10^{−10}<W[g_129]/‖·‖²<1.35·10^{−10} (061).
B12. Signed partial balances: OMEGA-TAIL and JOINT-TAIL (027); BLOCK ∫_1^{9/4}G_NH>1/100, N≥2^{20} (030);
SHARP-GAP (030); PEAK and BUDGET (031); BAND, N≥2^{80} (041); DILATE/SIGNED/WINDOW (037); SHOULDER and TAIL:
h_N,K_N>0 for x≥e^{T_N}, N≥4·10^6 (039); ψ_Λ(x)≤2x (039).
B13. Hyperbolic model (HYPERBOLIC §§5, 8): kernel [M_a(u_i)+M_a(u_j)]/(u_i+u_j) PSD at all
sizes for φ_a and its Robin extension; explicit realization (§12.6) of Q,B,C,D with exact continuous
observation of q_θ and strong equation for Y_ν. Not transferred to Φ.
B14. Density (094): exact distance, BINOMIAL-DET, DIAGONAL-DENSITY criterion.
B15. Tools: lemma (G) 0≤τm′(τ)<4 and exact polar P_n(u) (007); transport identity with deficit
(009/010); PF-DET and Rolle criterion (084); JAC (049, superseded document).

## C. OPEN obligations as mathematical statements

C1. **Initial segment of the high-pass orbit.** For all n≥1, every real P with deg P<n and every
0≤j<K(n): W[Q^jP/(s+u)^n]≥0 (or, by B2, for a fixed N, for all j<K_N). Attempted: eventuality
(015), effective cutoffs (049, 051, 053, 054), binomial descent (016), dense unions (AUDIT_016, 094).
C2. **Ladder of powers at all orders.** [ (L(32+i)+L(32+j))/(63+i+j) ]_{0≤i,j≤m} ⪰ 0 for
all m; equivalently |α_r|<1 for all r in the recurrence (E) of 003. Attempted: elimination (003),
pairs/triples/four (084, 085), Turán T_h (097–099); Pfaffian obligations of order ≥5 and inheritance to the
next remainder open.
C3. **Complete scalar table.** W[h_{N,k}]≥0 for all N≥1, k≥0 (h_{N,k} with Laplace transform s^k/(s+u)^{N+k});
covered N=1, N≤17 with k≥1 (and other rows), the cone k≥10000N² and the region u²≥225N/4. Missing: the interior
N≥18 with k<10000N², and k=0 for N≥13 at fixed rate.
C4. **Interior gamma balance** (atom k=0): for large N, ∫_1^∞G_N(x)H(x)dx≥0 with H from 030; remaining:
∫_{9/4}^∞G_NH (030), ∫_1^{4096}K_NΩ (027), E_ν[I_*(e^t)]>M_2/R(T_N) (031), the complement of the band
[e^T,e^{T+L}] (041), the signed sum FULL Σ_{(m,Q)=1}μ(m)K_{N,Q}(m) (037) and the interior region x<e^{T_N} of the
inverse (039). Equivalent form: G_W(m_N)+∫_0^∞L_N(a)G_W″(a)da≥0 (027).
C5. **Propagation in N** of the signed balance with precision relative to the residue (061, 062): estimate R (of order
0.03) and W (of order 10^{−10}) without summing independent boxes.
C6. **Transfer of the hyperbolic model to Φ**: a metric (nonlocal or unbounded) and a positive Green
identity reproducing the full form from the realization 12.6.
C7. **Arbitrary dimension of poles**: W>0 on all spaces of n poles ≥63/2 for all n (and 14 poles
with general numerator).
C8. **Density + continuity**: linear envelope of unions of positive blocks and continuity of W in the
topology used (094); cross terms between blocks.

## D. Objects or ideas mentioned as not started or not examined

D1. ORIGIN-HANKEL «that computation was not started here» (097) — carried out later in 098.
D2. Long route E_{2,3} (NEXT) of plan 050: «not executed»; superseded.
D3. Topologies in which the moments ℓ_r are not continuous (AUDIT_016 §3): not examined.
D4. Other groupings or signed estimates of the Möbius complement (037 §8): «not excluded».
D5. Other affine representations different from 042 (062): not examined.
D6. COMPLETE-MONOTONICITY for the real densities of 103: «neither proved nor refuted» (111).
D7. Whether an isolated cosh factor (with or without shift) preserves PSD of the kernel: «neither proved nor
refuted» (HYPERBOLIC §§11, 13).
D8. Nonlocal or unbounded metrics, new connections, b-dependent prefactors, nonsymmetric
systems, noncontinuous observations for the realization 12.6 (HYPERBOLIC §§12.4–12.7).
D9. Variable base frequency scales, real powers, sums and quotients of cosh products (§13.1).
D10. Global sign of the temporal Wronskian of densities 093/095 (097, 099): neither used nor proved.
D11. Sign for all numerators in the quadratic cone (AUDIT_017 §8): not claimed.
D12. A correlation-operator bound different from the Cauchy majorant of the tail from 3 (053 §1):
«does not exclude another bound».

## E. Coverage

Range: the `.md` files of `phase-211-sign-sandbox/` in `ls *.md | sort` order from `POWER_DESCENT_016.md`
to `POWER_INVERSE_INTERIOR_022.md` inclusive, excluding `POWER_GLOBAL_ROUTE_REVIEW.md` and
`POWER_GRAM_SLICES_OBSTRUCTION.md`: **61 files**. Read in full: **61/61** (including
`POWER_HYPERBOLIC_MODEL_GRAM.md`, 966 lines, in two complete portions). No file or portion of the range
was left unread. Also read, for notation, `RULES_AVOID.md`, `OBJECT_SPEC.md`, `STATEMENT_001.md`,
`POWER_CONE_001.md` and `POWER_BRIDGE_002.md`. The checkers `tools/*.py` and the files
cited outside the range (e.g. 018–026, 032–033, 042, 073–096, POWER_STATE_*) were not read; their contents are only
reflected as the files read cite them.
