# Annex 211 — Files POWER_REDUCTION_AUDIT_044 … POWER_THETA_DENSITY_ORIGIN_087 (106 files)

Complete reading, in alphabetical order (`ls *.md | sort`), of the 106 files of
`../phase-211-sign-sandbox/` lying between `POWER_REDUCTION_AUDIT_044.md` and
`POWER_THETA_DENSITY_ORIGIN_087.md`, both included. Notation of `STATEMENT_001.md`,
`POWER_CONE_001.md` and `POWER_BRIDGE_002.md`: (★) is λ_A(T) ≥ 0 for all T; W is the full form
(ARCH + comb + polar); AP = ARCH + POLAR; u = 63/2 is the fixed rate; V_n is the confluent block
{P(s)/(s+u)^n}; f_{N,k} (or h_{N,k}) is the atom with transform s^k/(s+u)^{N+k}; g_N is the gamma
atom y^{N−1}e^{−uy}/(N−1)!; Q = s/(s+u), L = u/(s+u); Φ is the even theta density of CONE_001,
M(u) = L(u+½), K_ij = [L(a_i)+L(a_j)]/(a_i+a_j−1). E_0(x) = ψ_Λ(x) − x + 1;
B(x) = Σ_{m≤x}E_0(x/m); h_N(x) = Σμ(m)mH_N(mx) is the dilation inverse. Labels are copied
as they appear in each file. The POWER_STATE_* files are round summaries: their entry indicates what
they record and what they add (the proof of the source is not repeated).

## Entries by file

1. **POWER_REDUCTION_AUDIT_044.md** — Audit of REFLECTION_TEST_044 and of the candidate L55-B (positive
   primal pair on a shifted archimedean datum). Result: reflection APPROVED (checker PASS);
   L55-B «remains open, with no new floor proved»; «it is not a global no-go». Remainder: a
   positive representation of ALL primitive forms with slack ≤ ε and primal mismatch in total
   variation ≤ η would give λ_A ≥ −ε−η, but «it would already be a positive extension of the form»; the vectors of the dual
   LP only give upper bounds; a mismatch that is a positive measure is not enough (c_F has signs).
   No reusable positive.

2. **POWER_REFLECTION_TEST_044.md** — Hypothesis: eliminate via the symmetry q ↔ 1−q
   (q = τ²/(u²+τ²), R(q) = A(q(1−q)) + (2q−1)B(q(1−q))) the antisymmetric sector of the bridge 017.
   PROVED (PASS), u = 63/2: with g_Q = √(4u)(1−uy)e^{−uy}, g_L = √(4u)uy e^{−uy},
   W[g_Q] − W[g_L] > 3/2 (ARCH gap 2b > 2, polar −2u(1+4u²)/(u²−¼)² > −½, comb
   4uΣΛ(n)log n·n^{−u−½} > 0). Falsifier of the symmetry (B = 1 already fails on the real datum), not of W.
   Reopening: quantitative control of the antisymmetric sector. Positive: ASYMMETRY.

3. **POWER_RENORMALIZED_AUDIT_042.md** — Audit of RENORMALIZED_TAIL_042. APPROVED (PASS):
   identity W = ARCH_♯ + 2γ − (2κ−γ)J(1) − 2R and |R_tail| < e^{−N/1000} for N ≥ 2^80, with all
   boundaries, jumps and divisors. Remainder: the renormalized interior and its balance with ARCH_♯, J(1) «have not been
   decided»; the benefit C_N of 041 is not added without boundary bookkeeping.

4. **POWER_RENORMALIZED_TAIL_042.md** — Global cancellation of the affine −γx by the exact mass
   ΣJ_N(n) = 1: F_N/2 = −γ + (κ−γ/2)J_N(1) + R_N, κ = ½log(2π) − ½,
   R_N = −∫_1^∞h_N B_1({x})(log x+γ)dx + ∫h_N E. PROVED (PASS), u = 63/2, N ≥ 2^80,
   T = (N−1)/992 + 5: |R_N^tail| ≤ N(T+2)e^{−3T/2} < e^{−N/1000} (ABS-TAIL);
   W[g_N]/‖·‖² = ARCH_♯ + 2γ − (2κ−γ)J_N(1) − 2R_N^inside + ε_N, |ε_N| < 2e^{−N/1000};
   DILATION and REAL-DECAY |h_N| ≤ Nx^{−3/2}, |h_N′| ≤ 2Nx^{−5/2} (x ≥ e^T). Remainder: R_N^inside
   (from 1 to e^T) unsigned. Reusable positive: ABS-TAIL and the identity (N ≥ 2^80).

5. **POWER_ROW_FOUR_028.md** — Row N = 4. PROVED (PASS): W[f_{4,k}] > (1/50)‖f‖² ∀k ≥ 0,
   ∀u ≥ 63/2 (ROW4); ARCH_{4,0}/norm² = d − ud′ + (2u²/5)d″ − (u³/15)d‴ with A4(u_0) > 11/400; comb
   < 3/500 (weight η = 12, R4 < 400); odd polar < 1/1000. Corollary (−Δ)³a_{1,k} = u⁶a_{4,k} > 0.
   Remainder: does not close the table of SCALAR_BRIDGE_017; gives no window T. The prohibition on
   replacing a universal proof by a campaign of rows stands. Positive: ROW4 and monotonicity MON of ARCH in u and k.

6. **POWER_ROW_PATTERN_029.md** — Region u² ≥ 256N, k ≥ 1, with Cauchy–Schwarz on weights ±η.
   PROVED (PASS): W[f_{N,k}] > (7/10)‖f‖² ∀N ≥ 2, k ≥ 1, u² ≥ 256N. Lemmas: PSI
   Re ψ(¼+it) ≥ log|t| − 9/(8t²); GAIN A_{N,1} = A_{N,0} + uA_{N,0}′; CENTERED
   |c_f(t)|/norm² ≤ e^{−ηt}[(u²−η²)/(u²−4η²)]^{N−½}. Remainder: at fixed u it only covers N ≤ u²/256 (does not
   close the table at u = 31.5); at k = 0, E τ^{−2} diverges. Positive: REGION, PSI, CENTERED.

7. **POWER_ROWS_AUDIT_028.md** — Audit of ROW_FOUR_028 and ROW_SPLIT_028: both APPROVED (PASS).
   Row 5: W > norm²/25 (k ≥ 0) and > 4norm²/5 (k ≥ 1), u ≥ 31.5; strict third and fourth differences
   of row 1. Remainder: «The complete sufficient table remains open»; the criterion §7 of
   028 is only sufficient; no complete monotonicity nor window T.

8. **POWER_ROW_SPLIT_028.md** — Row N = 5 separating k = 0 (positive polar) from k ≥ 1 (covariance).
   PROVED (PASS): W[f_{5,k,u}] > (1/25)‖f‖² ∀k ≥ 0, u ≥ 63/2; > (4/5)‖f‖² if k ≥ 1;
   ARCH_{5,0}(63/2) ∈ (−13/100, −1/10) («ARCH positive from k0» does not work). Reusable (sufficient)
   criterion for a row N: min(b_0 + p_{N,0}(U), b_U) > L_N, b_1 > L_N + p_1; identity
   A_{N,1} = A_{N,0} + u∂_uA_{N,0}. Remainder: growing rows N require an additional arithmetic inequality.

9. **POWER_SCALAR_BRIDGE_017.md** — Bernstein degree elevation of the rational density.
   PROVED: (A) W[h_{N,k}] ≥ 0 ∀N ≥ 1, k ≥ 0 ⟺ (B) W[f] ≥ 0 ∀F = P/(s+u)^M, degree P < M (u > 1);
   identity FORM W[f] + εW[f_1] = Σ_j b_{D,j}C(D,j)W[g_{D,j}], b_{D,j} > 0 if D > C_R/ε,
   C_R = ½Σ|r_l|l(l−1), with the polar preserved by evaluation at x = −¼; a W[f] < 0 produces a negative
   atom h_{D+1−j,j} at a boundable finite order. Remainder OPEN: (A), «the sign of the whole scalar table with
   the full arithmetic datum»; EVENTUAL_015 and fixed-dimension tails are not enough (W4 of 016).

10. **POWER_SCALE_AUDIT_029.md** — Audit of ROW_PATTERN_029, BOUNDARY_WEDGE_029 and
    SCALE_BRIDGE_LIMIT_029: all three APPROVED (PASS). Records BOUNDARY_WEDGE: W/norm² > 0.4
    ∀N ≥ 1, k ≥ 0, u ≥ 64√N (ARCH > 0.45, comb < 1/5000, polar < 0.001). Remainder: at u = 31.5 the
    region k ≥ 1 only reaches N ≤ 3 and that of k = 0 adds no orders; «new information for large
    N/u²». Positive: region u ≥ 64√N.

11. **POWER_SCALE_BRIDGE_LIMIT_029.md** — Normalized spectral densities p_{N,k,u} on u ≥ C√N.
    PROVED (APPROVED): HEIGHT sup p_{N,k,u} < √N/(u√π); every normalized positive mixture from that
    domain is at L¹ distance more than ½ from p_{M,0,63/2} if 2M−3 > 256u_0²/C² (GAP). NO-GO (class:
    approximation by positive cones of densities, normalized or of mass → 1, from u ≥ C√N): the
    bridge 017 is not transferred automatically. Does not exclude other bridges, identities with additional
    structure nor direct control.

12. **POWER_SCHUR_003.md** — Schur–Nevanlinna step on F(z) = L(z+½), pivot u ≥ 31.5:
    F_1(z) = c[zF − uc]/[zc − uF], c = F(u). PROVED: F_1 > 0 on z ≥ 31.5. OPEN: iterated
    preservation. Falsifiers: 3 + cosh z (F_1 = −129/17); F = (z²−z+10)/10 on [1,3] (all 2×2
    positive, det K(1,2,3) = −13/270000); min((2+3z)/5, (14+z)/10) (concave, det = −53/270000).
    NO-GO (class: F′ ≥ 0 and F/z decreasing, also with piecewise concavity); F_1′ ≥ 0 is not
    invariant. Remainder: jet |u(cd − ud² + uce)| ≤ c² − u²d² and a preserved arithmetic property.

13. **POWER_SCHUR_BASE_AUDIT_081.md** — Audit of SCHUR_BASE_OBSTRUCTION_081. APPROVED / PROVED in
    the declared class: G_p′(1024) < 0 for every pivot p ≥ p_0 = [25(L+2)]²; a positive G_p with
    negative derivative is not globally concave. NO-GO (class: imposing on ALL remainders G_p the conditions
    BASE_073, G′ > 0 and G″ ≤ 0). G_p > 0 remains proved; does not exclude general recursion nor another class.

14. **POWER_SCHUR_BASE_OBSTRUCTION_081.md** — Regularized remainder
    G_p(z) = az[B(p)−B(z)]/[B(p)(z²B(z) − p²B(p))], B(z) = [az/M(z) − 1]/z², a = M′(0); normalization
    C_p = z[B(z)−B(p)]/[1 − g(z)/K_p]. PROVED (audited): F = zB satisfies F′(1024) < −1/(3·1024²);
    G_p′(1024) < 0 ∀p ≥ p_0 (FAIL-BASE). Reopening: «a broader class allowing decreasing
    functions, or a proof that preserves the residue and controls the cross terms directly»; the double
    concavity of 078 is not refuted. Positive: bounds M(z) < √z (z ≥ 128), M′(z) > 1/(3(z+½)).

15. **POWER_SCHUR_TRIPLES_APPLICATION_099.md** — Kernel K_{G_p}(z,w) = [G_p(z)+G_p(w)]/(z+w) and double
    Schur complement on K_M with nodes {0, p}. PROVED (certificate 099 FULL PASS, reproduced):
    T_h > 0 on the whole half-line; R_G″ < 0 and S_G″ < 0 ∀p, x > 0; ALL triples of distinct positive
    nodes of K_{G_p} are PD ∀p > 0; block {0, p, z_1, z_2, z_3} of K_M PD (identity
    S_uv − S_0uS_0v/δ = d_p(u)d_p(v)K_{G_p}(u,v)). Scope: node 0 (exponent ½) is outside the
    carrier; it does not give five admissible generators. Remainder: «The next level requires a new input».

16. **POWER_SELBERG_DROP_AUDIT_067.md** — Audit of SELBERG_DROP_OBSTRUCTION_067: APPROVED.
    Reconfirms S = U − V, 2V > 1/243, 0 < W/c_0 < 27/(2·10^{11}), θ < 3.2805·10^{−8}. Scope: only
    the ISOLATED loss of the positive contribution in that decomposition; «does not rule out preserving the cancellation
    between U and V»; not a global NO-GO.

17. **POWER_SELBERG_DROP_OBSTRUCTION_067.md** — Gamma test N = 129, u = 63/2;
    S = ΣΛ(m)m^{−½}ρ(log m), U = Σ(μ∗log²)(m)m^{−½}ρ(log m)/log m,
    V = Σ(Λ∗Λ)(m)m^{−½}ρ(log m)/log m; from Λ·log + Λ∗Λ = μ∗log²: W/c_0 = ARCH/c_0 + POLAR/c_0 − 2U + 2V.
    PROVED/APPROVED: the criterion W/c_0 ≥ 2V is false (ARCH + POLAR − 2U < −1/250); retaining 1−θ of 2V
    requires θ < 3.2805·10^{−8}. NO-GO (class: suppressing 2V or an isolated fraction θ ≥ 3.3·10^{−8} in
    this decomposition). Does not exclude another organization nor a compensated estimate U−V. Positive: 2V > 1/243.

18. **POWER_SEVEN_AUDIT_012.md** — Audit of SEVEN_GLOBAL_012. PROVED (PASS): AP bands, 196
    DIRECT panels, trace T7 = 176673441, comb < 1/125; W > (1/500)‖f‖². Remainder: «Nothing in this
    certificate implies the result for eight poles or all degrees».

19. **POWER_SEVEN_GLOBAL_012.md** — F = P(s)/Π_{j=1}^7(s+v_j), v_j ≥ 63/2, degree P < 7.
    PROVED (rational certificate, audited): W[f] > (1/500)‖f‖² (SEVEN); BASE7 AP − (69/1000)I PD;
    AP7 AP > (1/100)‖f‖² by the transport identity with deficit DIRECT < 57/1000; comb by weighted
    trace (σ = 21). Remainder: the high-order Tate test and the dimension-twelve block «are not
    resolved by extrapolating AP7». Positive: SEVEN (seven arbitrary poles ≥ 63/2).

20. **POWER_SHIFTED_WRONSKIAN_092.md** — Elimination determinant Δ of the chart F = K/w
    (w = tΦ, ODE F″ + mF′ + AF = s), identity SHIFT Δ = −W_t(w″, v″, w⁗)/[w³k²J]. PROVED (audited):
    W_shift < 0 near 0 (D0 ∈ (−56488961026, −56488961025)) and > 0 on a tail
    (P = 4096(2t²−1)y⁹ + Q, |Q| ≤ C*t²y⁸); there is t* with Δ(t*) = 0. NO-GO (class: global invertible
    chart dividing by Δ; monic homogeneous ODE of order 2 with continuous coefficients on the whole
    half-line containing D3(1/w) and D3(t/w)). Does not exclude cancellation for K, inhomogeneous ODE, another
    order, representation or gauge.

21. **POWER_SHIFTED_WRONSKIAN_AUDIT_092.md** — Audit of 092: APPROVED / PROVED for the declared
    chart; independent reproduction of D0 and of the coefficient 4096(2t²−1) of y⁹. «There is no new negative
    W, decided anchored minor, W/T coverage nor global obstruction»; other charts available.

22. **POWER_SHOULDER_AUDIT_039.md** — Audit of INFINITE_SHOULDER_039 (infinite Euler product
    on σ > 1). APPROVED (PASS): h_N > 0 and K_N > 0 for x ≥ e^{T_N} and N ≥ 4·10^6, with ψ(x) ≤ 2x,
    A ≤ 5/δ, B ≤ 5/δ² and ratios between 0.9U_σ and 1.1U_σ; T_N < d/330. Remainder: «The critical σ1 region and the
    remaining interior are not covered»; no quantitative compensation with ARCH_♯.

23. **POWER_SIGNED_AUDIT_014.md** — Audit of SIGNED_TRANSFER_014. PROVED (PASS): telescoping TEL
    with exact κ_j ≥ 0; restricted block Q(0) = 0 with γ = ¼; AP > 0.03; comb < 29/1000;
    W > 0.001‖f‖² on eight arbitrary poles ≥ 31.5. Scope: changes an essential hypothesis of the class
    discarded in 013 (preserves the signed integral); does not infer higher dimension.

24. **POWER_SIGNED_AUDIT_019.md** — Audit of SIGNED_MEAN_019 and ARITHMETIC_DIFFERENCES_019: both
    APPROVED with local scope. Column k = 1: unique root of r_N = p_N − 2p_N′ + p_N″ (Descartes); for
    N ≤ 211 (u = 31.5) all contacts have negative autocorrelation and the full comb is
    strictly positive; all differences (−Δ)^rP_{1,0} of the isolated comb are negative.
    NO-GO: positivity of each inverse prefix; attributing positive differences to the comb via Λ ≥ 0.
    Remainder: full inverse kernel and global table open.

25. **POWER_SIGNED_AUDIT_038.md** — Audit of SIGNED_MOMENTS_038: APPROVED (PASS), including the
    √N window corollary. Remainder: does not control the infinite complement (m coprime to Q) nor its
    integral with B; the polynomial error is not relative precision against exponential components; does not
    include m = 1. Signed moments are not a probability (no Jensen).

26. **POWER_SIGNED_BALANCE_020.md** — Atom F_{211,1}, u = 63/2. PROVED (PASS): uniform upper bound
    ARCH_{N,1}/norm² ≤ U_N(u) (N ≥ 2, u > 0, by Jensen); U_211(63/2) < −0.74; 0 < P_2/norm² < 0.075;
    [ARCH + POLAR + P_2]/norm² < −0.66 (FAIL2). NO-GO (class: repairing ARCH+POLAR in the column k = 1
    with contact 2 alone). Reopening: «a one-sided bound of several contacts or of their joint mass that
    preserves the compensations with ARCH and the polar». Positive: the bound U_N(u).

27. **POWER_SIGNED_MEAN_019.md** — ERR: W[g_N]/c_0 = Arch_♯/c_0 − F_N, F_N = 2∫H_N E_0,
    H_N(x) = x^{−3/2}[½ρ_N − ρ_N′](log x). PROVED: B(x) = log(n!) − xH_n + n ≤ −(1−log 2)(x−1) (NEG);
    mean of dilations A_N = 2∫H_N B ≤ −2(1−log 2)J_N(½) < 0 ∀N ≥ 2 (MEAN); F_N = 2∫h_N B (PAIR);
    h_N^{[3]}(1) < −19/256 for N ≥ 2^17 (FAIL3). NO-GO: «inversion by dilations preserves
    positivity at each prefix»; replacing h_N by its modulus. OPEN: (SIGNED)
    2∫h_N^+(−B) − 2∫h_N^−(−B) ≥ −Arch_♯[g_N]/c_0.

28. **POWER_SIGNED_MOMENTS_038.md** — Finite Möbius operator
    M_Qf(ℓ) = U_Q^{−1}Σ_{b|Q}μ(b)b^{−1}f(ℓ + log b) on the gamma profile f_N. PROVED (audited): for
    N ≥ 16, B_Q ≤ N/1000, ∀ℓ: |M_Qf_N(ℓ) − f_N(ℓ − A_Q)| ≤ 12000B_Q/N + 65√N(V_Q/U_Q + 1)e^{−N/2000}
    (SIGNED-FOURIER); WIDE-WINDOW (0.8)U_Q/m < K_{N,Q}(m) < (1.2)U_Q/m if A_Q ≤ log m ≤ A_Q + √N/100,
    N ≥ 2^80, Q = Π_{p ≤ N^{1/8}}p. Remainder: exterior sum over m coprime to Q and integral of the
    polar−comb residue.

29. **POWER_SIGNED_TRANSFER_014.md** — Telescoping TEL (R − R_0)|F_0|² = R_0Σκ_j|G_j|²,
    G_j = sP/[(s+u)^{n−j+1}Π_{k≤j}(s+v_k)], and POLTEL. PROVED: EIGHT W > (1/1000)‖f‖² on eight arbitrary
    real poles ≥ 63/2; identity FULL W[f] − c‖f‖² = R_0[(W[f_0] − c‖f_0‖²) +
    Σκ_j(W[G_j] − c‖G_j‖²)]; ONE W[f_v] = ρW[f_u] + (1−ρ)W[sF_u/(s+v)], ρ = u²/v². Criterion (not proved
    at all orders): confluent base with n and n+1 poles with transform vanishing at 0 ⇒ n poles. Remainder: «the
    dimension-twelve test with negative AP remains in force».

30. **POWER_SIGNED_TRANSFORM_035.md** — Abel mean A_N = W[g_N]/norm² = Σ_{m≤d}P_d(m)t_m,
    P_d(m) = a_m m(m²−1)/[2(2d−m)(2d−m−1)], d = N−1. PROVED (audited): TAIL, SMALL, LARGE, WINDOW
    (M(M−1)/(4d) → Gamma(2)), BUDGET Σ_{m≤R}P_d(m)t_m ≥ −B_R·O(N^{−2}). Generic falsifier:
    Θ = 3 + cosh(av) gives A_{2,model} < 0. NO-GO: premise T_m ≥ 0 (refuted in 034). Remainder: estimate the
    arithmetic average in the moving window m ~ √N and its tails weighted by t_m.

31. **POWER_SIMULTANEOUS_SHIFT_AUDIT.md** — Audit of SIMULTANEOUS_SHIFT_OBSTRUCTION: APPROVED.
    Limit determinant −9log²2/32; initial block K(32+i,32+j) − K(34+i,34+j) not PSD; IMS extension
    approved (CrossR → −3√2/8). Only the Loewner order with shift 2 is refuted; not W, nor PSD of
    K, nor other restricted transports.

32. **POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION.md** — Defect D(f,g) = W(f,g) − W(Tf,Tg), Tf = e^{−2t}f,
    packets concentrated on (ε, 2ε) and (log 2 + ε, log 2 + 2ε); IMS remainder R = W[f] − W[Tf] − W[Sf],
    S = √(1−T²). PROVED: det D → −9(log 2)²/32; there is a finite N with
    [K(32+i,32+j) − K(34+i,34+j)]_{i,j≤N} not PSD; R(f_ε, g_ε) → −3v_2/8 (IMS indefinite); Σ_rR[T^rf]
    has coefficient d/(1−TT) → 1 near (0, log 2). NO-GO (class: universal PSD order K − K_shift
    with shift 2; deleting IMS by telescoping). Does not exclude other shifts, normalizations
    with new hypotheses, finer joint signed control.

33. **POWER_SIX_AUDIT_011.md** — Audit of SIX_GLOBAL_011. PROVED (PASS): BASE6 AP − (3/25)I PD;
    25 panels x(c−m)_+ < 9; B6 = (49^6−1)/12; W > (23/500)‖f‖² on six poles ≥ 31.5. Remainder: seven
    or arbitrary dimension «requires new verified hypotheses».

34. **POWER_SIX_GLOBAL_011.md** — Six poles v_j ≥ 63/2; criterion CRIT b − c − DK_n − pη_n > 0 with
    K_n = [(1+X/u²)^n − 1]/X, η_n = 1 − (1−1/(4u²))^n; all-pass bound WT ‖e^{σy}f‖² ≤ B_n(α)‖f‖².
    PROVED: SIX W > (1/25)‖f‖²; CRIT and WT as general theorems (all n, conditional on the
    constants). Remainder: «does not ensure that those constants exist with margin for all n»; the weighted
    improvement «does not replace the positive compensation of the comb when it becomes necessary».

35. **POWER_STATE_003.md** — Status OPEN. Records BRIDGE_002 (K_ij PSD on the ladder
    a = 32+i suffices), FIXED_GRID_003 (orders 1–6 certified), POLYNOMIAL_003 (dilations neither self-adjoint
    nor contractive; identities without sign), falsifiers of SCHUR_003. Do not relaunch: «The union of
    high ranges u ≥ 2^{40n} is not dense […]: do not extrapolate that family»; avoid the monomial Gram near
    the confluence (false negatives).

36. **POWER_STATE_004.md** — Records PROVED three powers a_i ≥ 32: Q[ρ] ≥ (1/20)‖f‖²
    (POLE_MOVEMENT_004; monotonicity of ARCH by covariance when raising poles). NUMERICAL (diagnostic):
    confluent of dimension 4, ARCH ≈ −0.17005, ARCH+POLAR ≈ 0.32259. Remainder: ladder 32+k at all
    orders. «Do not extrapolate triples nor the six sizes already certified».

37. **POWER_STATE_006.md** — Records CONFLUENT_FOUR_005 (W > 1/5), POLAR_MOVEMENT_005 (LOCAL AP
    transport), ARITHMETIC_WITNESS_006 (vector of dimension 12: AP ∈ (−2/125, −1/100), W > norm²/50; without
    contact 2, W < −norm²/125). NO-GO: ARCH+POLAR monotonicity without rate restriction (u: 1 → 2);
    universal monotonicity of the AP Rayleigh quotient at fixed numerator (HIGH_ORDER_PM_NOGO_007). Remainder: joint
    compensation in a dense family, «do not add positive families separately».

38. **POWER_STATE_008.md** — Records ARITHMETIC_BLOCK_007: W > ‖h‖²/10000 on all of V12 (AP indefinite;
    contact 2 necessary). NO-GO: PRIME_PATTERN_FALSIFIER_008, f = (D² − ¼)[y^{n−1}e^{−31.5y}],
    n = 2^17: ARCH < −3.83‖f‖² and each contact ≤ 1024 makes it worse («2 repairs» is not a universal pattern).
    Remainder: (TAIL) of test 008; an inequality for the FULL arithmetic sum with autocorrelation of
    mixed signs. Do not repeat AP monotonicity in dimension nor inference from favorable contacts.

39. **POWER_STATE_012.md** — PROVED table for arbitrary poles ≥ 31.5: ≤ 3 (1/20), ≤ 4 (2/25),
    ≤ 5 (1/100), ≤ 6 (1/25), ≤ 7 (1/500). Tate chain W[f_n] = 992^{2−n}Δ²q_n with open convexity.
    NO-GO (DEFICIT_LIMIT_013): in dimension 8 the best direct pointwise uniform deficit does not allow
    transport (margin < 1/25 < loss > 1/20); excludes refining constants in that class. Reopening:
    preserve the signed integral of the filter (done in 014).

40. **POWER_STATE_014.md** — Records EIGHT and CONFLUENT_BRIDGE_014: for fixed u > ½ the blocks
    span{y^ke^{−uy}: k < N} are dense in a weighted H¹ norm that controls the form; W ≥ 0 on
    each confluent block of one rate suffices, without uniform margin. One-pole identity
    W[f_v] − R_0W[f_u] = (1−R_0)W[sF_u/(s+v)]. Remainder: all confluent sizes > 12.

41. **POWER_STATE_015.md** — Records HIGHPASS_015 (for u > 1, N fixed there is K_N with W > 0 on Q^kV_N,
    k ≥ K_N; normalized ARCH ≥ (log k)/2 − C_N; K_N not effective) and GEOMETRIC_TRANSFER_015 (pole
    transport as a positive mixture of W[Q^kf_base]). Remainder: finite initial segment of blocks for each
    N; eventual positivity does not give the initial one. «Do not repeat a campaign of finite certificates».

42. **POWER_STATE_016.md** — Records DESCENT_016 W[f] = W[Qf] + W[Lf]; binomial refinement;
    JOINT_SCALE_016 (contacts → cos(u√c t) if k/N → c; Jensen prevents making exponential weights uniform in
    N); DESCENT_AUDIT_016 (common strong limit only 0); falsifier W_4 = W − 4‖·‖². Do not relaunch:
    density of tails, uniform disappearance of contacts in linear cones, exponential weights
    uniform in N. OPEN not refuted: spectral quadratic scale and sign cones.

43. **POWER_STATE_017.md** — Records SCALAR_BRIDGE_017; INTERIOR_017 (N = 1, all k, u ≥ 63/2:
    W > 4norm²/3); QUADRATIC_017 (W > 0 for k ≥ cN², N ≥ N_0(c)); QUADRATIC_EXPLICIT_017
    (W > 49norm²/50 for N ≥ 2, k ≥ 10000N², u = 31.5). Remainder: lower regions with both indices
    growing outside the cone.

44. **POWER_STATE_018.md** — Records rows 2 and 3 (> 1/8), recurrence a_{N,k} = a_{N,k+1} + u²a_{N+1,k},
    LOW_TABLE_018 (budget D_N(θ) = 2 + 2θJ_N(θ−½)). NO-GO: arcsine model
    V[f] = 2‖f‖² − (u/100)|F(iu)|² preserves identities, 12 poles, rows 1–3 and the cone, with entry
    (40402, 40401) negative. Remainder: N ≥ 4, k < 10000N². «A campaign row4, row5 will not be continued».

45. **POWER_STATE_019.md** — Records ARITHMETIC_DIFFERENCES_019 (simple root χ_N,
    √(2N−3) < χ_N < (1+√(8N−11))/2; full comb > 0 at k = 1, N ≤ 211; < 0 at k = 0 ∀N) and
    SIGNED_MEAN_019. Remainder: combine the signed comb with ARCH and polar at variable orders; do not extrapolate
    dilations to ERR nor prefixes to the inverse.

46. **POWER_STATE_020.md** — Records INVERSE_KERNEL_020: H_N/4 ≤ h_N ≤ 7H_N/4 if N ≥ 2 and
    log x ≥ (N−1)/30; h_2 ≥ H_2/[2ζ(32)] on the whole half-line (negative part of h_N localized in
    [1, e^{(N−1)/30})), and FAIL2. Remainder: interior pairing of h_N with B.

47. **POWER_STATE_021.md** — Records CONTACT_BALANCE_021 PROVED (atom 211,1): ARCH + POLAR + contacts
    2,3,4 < −0.21norm²; tail q > 300 ∈ [0, 5·10^{−13}]norm². NUMERICAL: partial sum up to 300 ≈
    −6.08·10^{−14}norm² (does not certify). Remainder: an inequality preserving cancellations; do not return to
    repair by a single contact.

48. **POWER_STATE_022.md** — PROVED −2/3 < h_128(1) < −33/50 (Möbius tail < 10^{−10}). NO-GO
    (falsifier): h_N(x) ≥ 0 ∀N, x. Pivot: primitive J_N = ∫_x^∞h_N and K_N = J_N + xh_N. «The global
    positivity of h_N is not relaunched […] nor is the modulus used to erase the adverse region».

49. **POWER_STATE_023.md** — PROVED −1/250 < K_129(1) < −1/251; ΣJ_N(n) = 1;
    ERR = −2∫K_N C_B, C_B(t) = −t^{−2}∫_1^t x dB > 0; damage of K^− on [1, 1+δ] ≤ δ²sup K^−. NO-GO: universal h ≥ 0 and
    K ≥ 0. Remainder: cellular averages or negative part weighted by C_B.

50. **POWER_STATE_025.md** — Records ERR_129 < −33/50 (LOGCONCAVITY_025; CELL_TEST_024
    S_129(2) > 33/100); D_N = 33P_N − P_N′ with D_N′/D_N decreasing ∀N; cellular budget
    S_n = b_nJ(n) + (H_{n−1}/2)∫_cell[1 − (n−1)²/t²]K, b_n ≥ 0.75 − log 2. Remainder: compare ERR with
    ARCH_♯; extension to variable orders. Do not relaunch universal K ≥ 0.

51. **POWER_STATE_026.md** — Records UNIFORM_CUTOFF_026 (K_N(x) ≥ x^{−32}D_N(log x)/4 > 0 after a cutoff
    d/330 + O(1); K_N > 0 for 2 ≤ N ≤ 129, x ≥ e^{2/3}) and ARCH_CELL_026 (ARCH_♯129/norm² < −0.81;
    W[g_N]/norm² = ∫K_NΩ with Ω(3/2) < −0.1). NO-GO: universal pointwise positivity of Ω and of K. Remainder:
    joint balance with the gamma curvature.

52. **POWER_STATE_027.md** — Records DISCRETE_BALANCE_027 (Ω(t) ≥ ℓ − (4log t + 9)/t, ℓ > 1/50; tail
    0 < ∫_{4096}^∞K_129Ω < 10^{−36}) and INTERIOR_CONSTRAINT_027 (W_gamma − W_gauss = ∫L_N(a)G_W″(a)da;
    G_W″(a) < 0 ∀a ≥ 65536). NO-GO: global convexity of the real Gaussian functional. Remainder: interior
    ∫_1^{4096}K_129Ω unsigned; «A positive mixture with signed curvature or another tiny favorable
    tail is not enough».

53. **POWER_STATE_028.md** — Records ROW4 and ROW5; coverage: rows 1..5 ∀k, u ≥ 31.5; cone
    k ≥ 10000N²; eight poles; V12. Remainder: N ≥ 6 below the cone. «The target of all N at
    fixed rate is not replaced by a result with growing rate».

54. **POWER_STATE_029.md** — Records ROW_PATTERN_029 (u² ≥ 256N, k ≥ 1: > 7/10), BOUNDARY_WEDGE_029
    (u² ≥ 4096N: > 2/5) and the GAP obstruction. Remainder: «recover information at large N/u² and preserve
    the arithmetic cancellations».

55. **POWER_STATE_030.md** — Records INTERIOR_SCALE_030: W[g_N]/norm² = ∫_1^∞G_N H,
    H(x) = 1 + [log((x+1)/(x−1)) − γ − log(4π) − 1 − 2Σ_{q≤x}qΛ(q)]/x²; ∫_1^{9/4}G_N H > 1/100
    (N ≥ 2^20); GAMMA_BALANCE_030: 0 < A_♯(EV) − ARCH_♯/norm² < 1/[2(N−3/2)]. NO-GO: positive primitives of H
    (false up to 5/2); cost-free gamma–Gaussian comparison of full forms (false at
    N = 2). Remainder: ∫_{9/4}^∞G_N H.

56. **POWER_STATE_031.md** — Records WEIGHTED_BLOCK_031 (∫_1^{225/64}G_NH < −3/1000, ∫_1^4 > 3/200)
    and GAMMA_WEIGHT_031 (R_N = ρ_N − (2/3)ρ_N′, unique maximum T_N < 2/3;
    W/norm² ≥ ∫_{T_N}^∞I_*(e^t)[−R_N′]dt − M2). NO-GO: universal I_* ≥ 0. Remainder OPEN: signed
    average of I_* against −R_N′; «Enumerating other blocks […] would not replace that obligation».

57. **POWER_STATE_032.md** — Records CONTACT_DECISION_032 PROVED: 3.4·10^{−15} < W[f]/‖f‖² <
    4.5·10^{−15} for F = s/(s+63/2)^{212}; ARCH_EXACT_032. Remainder: structural compensation of all the
    contacts or the average 031; «do not launch a campaign of more points».

58. **POWER_STATE_033.md** — Records PRIME_BALANCE_033 (w(mq) ≤ m^{−2}w(q), contraction ρ = 2389/3600,
    0 < S_K ≤ A(w) ≤ S_K/(1−ρ^{K+1})) and COEFFICIENT_BALANCE_033 (Erlang mixture S_j; −0.01 < L[S_22] <
    −0.006). NO-GO: positive functional per Erlang component. OPEN (later refuted in 034):
    T_m = Σ_{j≤m}jL[S_j] ≥ 0 ∀m.

59. **POWER_STATE_034.md** — Records DIVISOR_COMPARISON_034: W[f_{N,k,u}] > ‖f‖²/40 for N ≥ 3, k ≥ 1,
    u² ≥ 225N/4 (k ≥ 2: > 3/20); at u_0: rows 1..12 complete; at all u ≥ u_0: rows 1..8;
    WEIGHTED_COEFFICIENT_034: T_m changes sign at arbitrarily large indices. NO-GO:
    positivity of T_m component by component (not even except for finitely many indices). Remainder: k = 0 for N ≥ 13.

60. **POWER_STATE_035.md** — Records BOUNDARY_BALANCE_035 (terminal N = 17, k = 0, margin > 0.041;
    recurrence A_{N0} = A_{N1}/(2N) + (2N−1)A_{N+1,0}/(2N)): W > norm²/40 for 1 ≤ N ≤ 17, all k,
    u = 63/2 (individual atoms). Remainder: N ≥ 18 below the cone; signed average of 035 OPEN.

61. **POWER_STATE_036.md** — Records RECURRENCE_BOUNDARY_036 (contribution of the cone at depth L:
    0 ≤ C_L = O(log(L+2)/√(L+1)) → 0) and MOVING_BALANCE_036 (laws weighted by polar and by |comb|:
    m/d → 1/32; phase (3969/3968)^N). NO-GO: omitting the diagonal remainder; discarding tails separately via the
    concentration of 035. Remainder: preserve polar and arithmetic jointly before estimating tails.

62. **POWER_STATE_037.md** — Records ENERGY_GROUP_037: bounds of mH_N(mx_N)/H_N(x_N) ~ 1/m; absolute
    sum of non-principal Möbius terms > 1 (N ≥ 2^16); with Q = Π_{p ≤ N^{1/8}}p, moduli of the
    grouped remainder > 1.48 against principal < 0.505. NO-GO: absolute contraction or domination of the remainder
    (also grouped); «improving only constants of the same absolute bounds does not resolve». Remainder:
    signed complement and its integral.

63. **POWER_STATE_038.md** — Records SIGNED-FOURIER and WIDE-WINDOW (entry 28). Remainder: sum over m
    coprime to Q and its integral in the polar−comb residue; precision against exponential components.

64. **POWER_STATE_039.md** — Records INFINITE_SHOULDER_039: h_N, K_N > 0 for x ≥ e^{T_N},
    N ≥ 4·10^6, T_N = 2(N−1)v_N/(u² − v_N²), v_N = ½ + 1000/√N; ψ_Λ(x) ≤ 2x. Remainder: interior and σ = 1.

65. **POWER_STATE_040.md** — Records CRITICAL_BALANCE_040 (N ≥ 2^80, v = ½ + N^{−2}):
    h_N/H_N < −1/N and K_N/G_N > 1/N at the same center e^{t_v}; h_N, K_N > 0 for t ≥ (N−1)/992 + 5;
    1/ζ(1+z) = z − γz² + R_3, |R_3| ≤ 9|z|³. Remainder: interior contribution and balance with ARCH_♯.

66. **POWER_STATE_041.md** — Records ENERGY_BAND_041: 2∫_{e^T}^{e^{T+L}}h_N B < −C_N/25600
    (N ≥ 2^80, L = √N/100); B(x) = −γx − B_1({x})log x + κ + E(x), −1/x < E < 1/(2x). Remainder: the
    complement; do not add benefits of different representations without boundaries; do not interchange with
    Σ|μ(n)|/n (diverges).

67. **POWER_STATE_042.md** — Records RENORMALIZED_TAIL_042 (entry 4). Remainder: renormalized interior from
    1 to X and then the table/carrier.

68. **POWER_STATE_044.md** — Records ASYMMETRY (reflection false) and the review of L55-B: a discrepant positive
    measure is not enough; primal candidates do not give a lower bound; L55-B «remains open as a pending
    construction». No new region.

69. **POWER_STATE_045.md** — Documentary correction: ROUND_026_A records λ_A(T) ≥ 2·10^{−26} for
    0 < T ≤ 1.035 (computer-assisted certification, logs reviewed, not reproduced); T = 1.098 without
    final certificate. CONTACT_FLOOR_045: m(240) − A_T < −½ when contact 5 enters. PRIMAL_PAIR_045:
    for EVEN measures, fixed real tail + compact correction ⇒ zero correction; at T = 3/5 symbol at 0
    < −15/2. NO-GO: cutoff 240 + total-mass floor in lowercert; even compact ansatz for L55-B. Does not
    exclude noncompact or non-even corrections.

70. **POWER_STATE_048.md** — Records SUBQUADRATIC_048 (N ≥ e^{10^6}, k ≥ 2N²/log log N:
    W > (2/5)log N·‖f‖²) and R12_ENDPOINT_048 (E2[G] > ‖G‖²/50 on V13 with G(0) = 0; E2 = AP + contact 2;
    polar of Q^jV12 with ratio ≤ 9/62). Remainder: lower band; uniform hypothesis of 046; R12 for v ≥ u.

71. **POWER_STATE_049.md** — Records R12 PROVED: E2[sF/(s+v)] > ‖·‖²/2500 ∀F ∈ V12, v ≥ u;
    CENTERED_CUTOFF_049 (j ≥ 14: E[τ^{−2}] < 1/405, ARCH > 859/800; j = 1..13 by LDL). Remainder: contacts
    n ≥ 3 not transported; several moved poles are not iterated automatically.

72. **POWER_STATE_050.md** — PROVED (FULL_TWELVE_050): W[P/Π_{i=1}^{12}(s+v_i)] > ‖·‖²/10000 ∀v_i ≥ 63/2,
    degree P < 12; thirteen poles with numerator divisible by s: W > ‖·‖²/250. Mechanism: MULTI_015 +
    FULLTEL_014 + trace (α = ½). Remainder: arbitrary orders. Positive: twelve arbitrary poles.

73. **POWER_STATE_052.md** — PROVED (CONFLUENT_THIRTEEN_052): W > ‖f‖²/4000 on V13; Schur pivot
    complementary to F(0) = 0 in (0.0003, 0.0005); contact 3 adverse at the pivot; contact 2 adverse in
    the central direction of E2. Do not relaunch: «pattern of improvement with each added contact». Not obtained
    (without declaring it impossible): weighted norm uniform in j for Q^jV_n.

74. **POWER_STATE_053.md** — PROVED (FULL_THIRTEEN_053): W[P/Π_{i=1}^{13}(s+v_i)] > ‖·‖²/4000; fourteen
    poles with D(0) = 0: W > norm²/1000; E23[Q^jF] > norm²/10 for j ≥ 96 and > norm²/500 for j ≤ 95.
    Remainder: uniform control of the initial segment as dimension varies; general fourteen poles.

75. **POWER_STATE_054.md** — PROVED (EFFECTIVE_HIGHPASS_054): C_n = 9n²9^n, D_n = 10C_n n!,
    A_n = 6C_n n·n!, K(n) = max(10000n², A_n3^{4D_n+20}); ∀n, P of degree < n, j ≥ K(n):
    W[Q^jP/(s+u)^n] > ‖·‖². Duplicates: absolute extrapolation of moments (= 016); renaming the remainder
    as negative energy (= 036). Remainder: segment j < K(n), without eliminating it by recurrence or mass.

76. **POWER_STATE_055.md** — Scope audit: W_4 preserves DEF/BIN/MIX/MULTI/FULLTEL and the cutoff K(n)
    but is negative on e^{−63t/2} (effective cutoff + identities do not give the initial sign). Selberg S = U − V
    (update: criterion W ≥ 2V refuted in 067). Turán:
    a_{N,k}a_{N+2,k} − a_{N+1,k}² = W restricted to numerators {1, u² − s²}. Duplicates: pocket
    225/64 + recovery 4 (= 031); recombination 042 (= 030); Turán of full values (= 046).

77. **POWER_STATE_059.md** — Records STRIP_NECESSITY_059 (there is no uniform contour with p < 2). Pending
    (not proved): n-independent contour on a polynomial cone separating even/odd parts; the
    generator −i(y²h′ + yh) does not authorize a global Gaussian comparison. Duplicates 055–058: Selberg/Turán,
    cross terms of filters, exterior representations.

78. **POWER_STATE_060.md** — PROVED (UNIFORM_STRIP_060): J(n) = 10^{12}(nq_n)³, q_n = ⌈log₂(n+1)⌉;
    ∀n, P of degree < n, j ≥ J(n): W[Q^jP/(s+u)^n] > ‖·‖²; density shifted to height 3 with absolute
    integral < 2× the real one, constant independent of n and P. Remainder: j < J(n); no uniform quadratic
    cone.

79. **POWER_STATE_061.md** — PROVED (GAMMA_129_DECISION_061): 1.34·10^{−10} < W[g_129]/‖g‖² <
    1.35·10^{−10}; ARCH_♯ ≈ −1.042193970181, ERR ≈ −1.042193970315. NO-GO (application of 016/029): the
    cone 060 does not replace the full family by positive approximation (mass on [−u,u] ≤ 16·10^{−12}).
    Remainder: control the signed balance at the size of the residue.

80. **POWER_STATE_062.md** — Renormalized balance at the atom 129: AFF ∈ [−60446492280,
    −60446492279]/10^{12}, R ∈ [−30223246208, −30223246207]/10^{12}, W/norm² = AFF − 2R (PROVED,
    diagnostic). NO-GO: the affine part is not a positive base for neglecting the remainder. Duplicates: bounding R
    by cells; factorial/Stirling route. Remainder: differences in N of J, K and ARCH_♯.

81. **POWER_STATE_064.md** — Records STRIP_CUBIC_NECESSITY_064 (p ≥ 3 necessary for STRIP on all
    numerators). Identities B_N = A_N + u∂_uA_N, A_{N+1} = (2NA_N − B_N)/(2N−1) (deduplicated). Remainder
    OPEN: B_N ≤ 2NA_N (would propagate A_N ≥ 0), or B_N ≥ A_N with liminf A_N ≥ 0.

82. **POWER_STATE_065.md** — PROVED (CONTACT_OSCILLATION_065): the autocorrelation of s^k/(s+u)^{N+k}
    has exactly k simple positive zeros, alternation starting from +, last root at ut < 4k(N+k−1);
    contact tail with sign (−1)^{k+1}. Identity W/‖f‖² = ARCH_♯/‖f‖² + 2∫D(x)w′(x)dx; Rodrigues
    for weights φ(t²). NO-GO: attributing convexity φ^{(k)} ≥ 0 to the full weight of W (atoms ⇒ derivative of
    δ). Remainder: compare E_{ν+}D − E_{ν−}D per nodal interval; boundaries [E_1w′] cannot be omitted.

83. **POWER_STATE_067.md** — Records SELBERG_DROP_067. Regrouping by prime support (coefficients of
    μ∗log² and Λ∗Λ: (2a−1)log²p and (a−1)log²p at p^a; 2log p log q at p^aq^b; 0 with ≥ 3 primes) reconstructs
    S. OPEN: G_W(v) ≥ 0 ∀v > 0 (would transfer to the whole row k = 0). Duplicates: cross terms between contacts;
    products ρ(log a)ρ(log b).

84. **POWER_STATE_073.md** — PROVED (THETA_HAZARD_COMPACT_073, THETA_TWO_COPY_073; 4096 panels):
    V‴ > 0 ∀t > 0; M″ < 0, M − uM′ > 0 ∀u > 0; 1 < L(a)/L(b) < (a−½)/(b−½) for a > b > 1; K of two
    distinct exponents > 1 PD (full form). Remainder: three generators, all orders, five tilts of
    103_43. Positive: all pairs a, b > 1.

85. **POWER_STATE_074.md** — PROVED (auxiliary counterexample TWO_COPY_SCOPE_074):
    V(x) = A[x²/2 + x^{2p}/(2p·2^{2p−2})], p = 10^6, A = 4·10^8, satisfies the whole hypothesis of 073 but
    cᵀKc < −53111/(10000A) at nodes A, 2A, 3A, c = (40, −40, 3). NO-GO (class: the potential hypothesis
    of 073 implies order three). OPEN-JET: t ≤ (1−r)(1+2r), r = uM′/M, t = −u²M″/M.

86. **POWER_STATE_075.md** — PROVED (THETA_SCHUR_DENSITY_075): H_u = D_u/[z(z²−u²)] = ∫Φ_ue^{zx} with
    Φ_u > 0, (log H_u)″ > 0; F1 = −cz/u + c²Z/(uzH_u), R = uc²/(ua−c). Query 076: defect T_u with
    density (u/c)[J − βΦ_u] of mass 0; sufficient one-crossing criterion. NO-GO: in the auxiliary 074
    G_A(3A) < 0 (the crossing is not generic).

87. **POWER_STATE_077.md** — PROVED (THETA_REMAINDER_077 and certificates): F_u = J − βΦ_u with a unique
    simple positive zero; T_u > 0, G_u > 0 ∀u, z > 0; C > 0, N > 0 on t > 0. Anchored corollary {0,u,v}.
    Appendix 078: CURVATURE-OPEN (h″, g″ ≤ 0) sufficient for pairs of G_p; g″ ≤ 0 ⟺ OPEN-JET;
    g″ < 0 (u ≥ 63/2), h″ < 0 (u ≥ 128), a > 1/25. Remainder: G_u > 0 does not give a PSD kernel.

88. **POWER_STATE_080.md** — PROVED (THETA_G_COMPACT_080 + THREE_SECANTS_079; 4096 panels, hash): for
    arbitrary a_i > 1, W > 0 on the space of up to three powers. Remainder: four generators (later
    085); inheritance of BASE by G_p is not used (refuted in 081).

89. **POWER_STATE_085.md** — PROVED (FOUR_GENERATORS_085, FOUR_TURAN_084, RECIPROCAL_PFAFFIANS_083;
    16384 panels, hash): for arbitrary a_i > 1, W > 0 on the space of up to four powers;
    det K4 = Pf_R·Pf_S/ΠR. Remainder: five generators, all orders.

90. **POWER_STATE_089.md** — PROVED: W_t(1,A,B,C) < 0 ∀t > 0; T_R = 2R′R‴ − 3R″² > 0 ∀λ > 0; h = 1/b
    strictly concave; all pairs of G_p PD. NO-GO: generic inheritance T_f ⇒ T_H
    (w = (5−e^{−x})/4: T_H(0) = −1/192); G_p does not inherit BASE nor its Turán inequalities. Remainder: global S4; T_h
    (later 099).

91. **POWER_STATE_099.md** — PROVED (EXACT_H_GLOBAL_099, 2048 panels, hash): T_h > 0 ∀x > 0;
    R_G″, S_G″ < 0; all triples of K_{G_p} PD; K_M on {0, p, z_1, z_2, z_3} PD (0 auxiliary). Remainder:
    five admissible generators; inheritance to the next level.

92. **POWER_STRIP_CUBIC_AUDIT_064.md** — Audit of STRIP_CUBIC_NECESSITY_064: APPROVED, threshold
    improved to j ≥ 10^6n. Scope: only excludes the ABSOLUTE uniform contour estimate; «Methods
    preserving signed cancellation and the interior problem remain open».

93. **POWER_STRIP_CUBIC_NECESSITY_064.md** — Numerator P_{n,j} from the orthonormal polynomial of degree
    n−1 for the Student weight (1+y²/j)^{−(n+j)}. PROVED/APPROVED: for n ≥ 4, j ≥ 10^6n,
    ∫|ρ(x+iη)|/∫ρ ≥ 1 + η²n³/(1152u²j). NO-GO (class: absolute STRIP with fixed η, D, uniform over
    all numerators, on cones j ≥ Cn^p, p < 3). Does not exclude a sign cone for W with smaller exponent.

94. **POWER_STRIP_NECESSITY_059.md** — (STRIP) ∫|ρ_{n,j}(x+iη)| ≤ D∫ρ_{n,j} for s^j/(s+u)^{n+j}.
    PROVED: fails along every sequence n ≤ j = o(n²) (exact variance and packet E cos(t_nZ) → 1). NO-GO
    (class: STRIP with fixed η, D, p < 2, already with P = 1). Does not refute n-dependent D nor a sign cone.

95. **POWER_SUBQUADRATIC_AUDIT_048.md** — Audit of SUBQUADRATIC_COROLLARY_048: APPROVED
    (W/norm² > L/2 − (113/2)√L − 20 > (2/5)L, L = log N ≥ 10^6); «extraction from 017, not a new
    arithmetic inequality». Remainder: lower band, lower bound of 046, energy remainder 036.

96. **POWER_SUBQUADRATIC_COROLLARY_048.md** — Four bounds of QUADRATIC_017 valid ∀c > 0, N ≥ 2,
    k ≥ max(cN², 4N), with c_N = 2/log log N. PROVED: N ≥ exp(10^6), k ≥ 2N²/log log N ⇒
    W[f_{N,k}] > (2/5)log N·‖f‖² (SUBQUADRATIC). Remainder: k < 2N²/log log N; the complement of the new
    frontier does not become vanishing energy (036 still applies).

97. **POWER_TABLE_AUDIT_018.md** — Audit of TABLE_DESCENT_018 and LOW_TABLE_018 and of the model
    V[f] = 2‖f‖² − εu_0|F(iu_0)|² (ε = 1/100). APPROVED: rows 2, 3; budget D_N(θ). V preserves
    Pascal, filters, ≤ 12 poles (V ≥ (47/25)‖f‖²), rows 1–3, cone (1.98), eventual positivity, but
    b_{40402,40401} < 0. NO-GO (class: completing the table with recurrences, filter identities and
    positive regions). Reopening: «additional information on the concrete arithmetic form».

98. **POWER_TABLE_DESCENT_018.md** — Rows 2 and 3. PROVED: W[f_{2,k}], W[f_{3,k}] > (1/8)‖f‖² ∀k ≥ 0,
    u ≥ 63/2 (ROWS23); DIFF: a_{1,k} − a_{1,k+1} > c_k/[32u(k+1)], second difference >
    3c_k/[64u(k+1)(k+2)]; ψ′ ≤ 1/x + 1/x², ψ″ ≥ −2/x³ − 1/x². Remainder: N ≥ 4; no complete monotonicity;
    AP monotonicity under pole motion «is false in general». Positive: ROWS23, DIFF.

99. **POWER_TATE_CHAIN_009.md** — Chain f_n = (∂² − ¼)g_n: c_{f_n} = a²C_n − 2aC_{n−1} + C_{n−2},
    a = 992; q_n = a^n(I_n − J_n) + 2, J_n = (2/Γ(n)²)Σβ_{nj}(−1)^jD^{(j)}(u+½), D = −ζ′/ζ. PROVED:
    W[f_n] = a^{2−n}Δ²q_n (CHAIN); normalized ARCH strictly decreasing in n (MON); for
    n ≥ 64u², n ≥ 2u²(log R)², each contact ≤ R is harmful; the individual members are not dense.
    OPEN: Δ²[a^n(I_n − J_n)] ≥ 0 ∀n ≥ 4. Do not relaunch: Λ∗1 = log, H_j > 0, generic convexity.

100. **POWER_THETA_AUDIT_073.md** — Audit of HAZARD_COMPACT_073, exterior 103_43 and TWO_COPY_073:
     APPROVED (4096 panels PASS); (log Φ)‴ < −20 for t ≥ ¼; two copies M″ = 4Cov(S, D²) < 0;
     L′ > 0, L″ < 0, L − (a−½)L′ > 0 ∀a > 1. Scope: it is not «a general Pick principle nor an induction
     over all orders»; the polynomial tilts of 103_43 are another obligation.

101. **POWER_THETA_CURVATURE_AUDIT_078.md** — Audit of the appendix 078: APPROVED.
     g″ = v[2r² − r + t − 1]/(4u⁴), h″ = v[(r−1)(2r+v−3) − (v−1)t]/[4u²(v−1)³]; g″ < 0 (u ≥ 63/2,
     Δ > 423/10000), h″ < 0 (u ≥ 128, v > 3, a_0 > 1/25); b(u²) = Z_K/Z_J. Remainder (then): compact ranges
     of g″ and h″; later closed in 080/089.

102. **POWER_THETA_DENSITY_COMPACT_089.md** — Wronskian of ρ = tΦ(1,A,B,C), A = p² − q − 2p/t,
     B = p/t, C = (p³−3pq+r)/t; K = W_t(ρ) = 64t^{10}W_λ(Ψ). PROVED (1024 + 8192 panels, hash):
     W_t(1,A,B,C) < 0 ∀t > 0 (GLOBAL-R4); determinant of densities < 0 at all nodes (Rolle in the
     B coordinate); kernel sinh(√λt)/√λ TP4; Andreief: T_R = 2R′R‴ − 3R″² > 0 ∀λ > 0. Remainder: S side,
     higher levels; no new W coverage.

103. **POWER_THETA_DENSITY_COMPACT_AUDIT_089.md** — Audit of 089: APPROVED / PROVED (FULL PASS,
     hash); theta tails 304·17⁴/4^{289} and 8576·17⁴/8^{289}; remainders < 10^{−18}, < 10^{−39}; consequence
     h = 1/b strictly concave and all pairs of G_p PD. Remainder: «The other reciprocal curvature of the remainder
     is not discharged, nor its subsequent Turán, no general Schur inheritance. No S4».

104. **POWER_THETA_DENSITY_CONCAVITY_086.md** — Three densities ρ = (tΦ, (tΦ)″, −Φ′) = tΦ(1,A,B);
     (A′/B′)′ = tN/(pD²) > 0 (N of 077). PROVED (audited): det[ρ_l(t_j)] < 0 at ordered nodes;
     sinh TP3 and confluent version; (Z′, u²Z′, uZ) = 2∫sinh(ut)ρ; R(λ) = √λ/M(√λ) satisfies R″(λ) < 0
     ∀λ > 0 (GLOBAL-CURVATURE), hence triples PD without the certificate 080. Remainder: higher densities of
     083 («the sign of their determinant is not obtained from this minor»).

105. **POWER_THETA_DENSITY_CONCAVITY_AUDIT_086.md** — Audit of 086: APPROVED / PROVED for the real Φ
     (identity (A′/B′)′ reproduced symbolically; Andreief with signed densities; factor 8 correct;
     W(f) = f_1³R″). Does not extend admissibility to a_i ≤ 1; no new coverage relative to 080/085; what remains is «a
     concrete structural mechanism for studying those higher obligations».

106. **POWER_THETA_DENSITY_ORIGIN_087.md** — Four densities (1,A,B,C); RAISE
     W_t(1,A,B,C) = −k³J²(E/J)′, coefficient of V^{(6)} in W_t equal to −N/(pt⁴); matrix ORIGIN-MATRIX
     at λ = 0 with a_j = Φ^{(2j)}(0)/[(2j)!Φ(0)]. PROVED (point and unquantified neighbourhood): Wronskian at
     the origin NEGATIVE (≈ −3.56·10^9, rational interval); JET-RAISE [v10]W_R4 = W_R3/840. Remainder
     (then): (E/J)′ > 0 globally, closed later in 089; S4 not treated.

## A. Deduplicated «do not relaunch», with reopening condition

Each item indicates its source in this block and its status in `RULES_AVOID.md` («RA»): **ABSENT**,
**PARTIAL** (covered only by a general formula) or **INEXACT** (both texts are quoted).

A1. Reflection symmetry q ↔ 1−q to eliminate the antisymmetric sector of the scalar bridge (2, 68).
    Reopening: unequal quantitative control of the remaining sector. **ABSENT.**
A2. L55-B with even ansatz, fixed real tail and compact correction; finite total spectral mass; discrepant
    positive measure; primal candidates as a lower bound (1, 68, 69). Reopening: noncompact
    or non-even correction, with equality on the whole primitive carrier and controlled discrepancy. **ABSENT.**
A3. Cutoff 240 and total-mass floor m(240) − A_T in lowercert (69). Reopening: another cutoff or bounds on the
    real symbol (as in ROUND_026_A). **ABSENT.**
A4. Replacing the atom cone of the bridge 017 by regions of growing rate u ≥ C√N or by the cone 060
    via positive mixtures of densities (11, 79). Reopening: another bridge, identity with
    additional structure or direct control. **PARTIAL**: RA D3 says «Inferring density or sign from a
    positive union»; it does not mention the GAP obstruction for L¹ approximation.
A5. Preservation of the Schur step from F′ ≥ 0, F/z decreasing (and concavity); F_1′ ≥ 0 as an invariant
    (12, 35). Reopening: an additional arithmetic property preserved by the transforms. **PARTIAL**:
    RA D5 «Schur–Green monotonicities — only with a different joint invariant preserved by each
    operation» (correct in spirit, without the falsifiers).
A6. Inheriting BASE_073 (G′ > 0, G″ ≤ 0) by each remainder G_p (13, 14, 88). Reopening: a class allowing
    decreasing G_p, or preserving the residue R_p/z and controlling cross terms. **ABSENT.**
A7. Generic potential hypothesis (V‴ > 0, M″ < 0, M − uM′ > 0) as sufficient for order three; the
    crossing of G_u as a generic consequence of 073/075 (85, 86). Reopening: a specific property of Φ or
    quantitative comparison of the crossing. **ABSENT.**
A8. Generic inheritance T_f ⇒ T_H of the Turán inequalities through the Schur step (90). Reopening: specific
    data of Φ (as in 099). **ABSENT.**
A9. Global elimination chart dividing by Δ; monic homogeneous ODE of order 2 common to D3(1/w),
    D3(t/w) (20, 21). Reopening: another chart, inhomogeneous ODE, another order or representation. **ABSENT.**
A10. Loewner order K ⪰ K_shift with simultaneous shift 2; deleting the IMS remainder by telescoping
     (31, 32). Reopening: other shifts, normalizations with new hypotheses, joint signed
     control. **INEXACT by generality**: RA D13 «Matrix order by shift K − K_shift»;
     the source only refutes shift 2 and declares: «Different normalizations with
     new hypotheses and their own proof, other shift sizes not treated here, are not ruled out».
A11. Discarding the positive term 2V of the identity S = U − V, or an isolated fraction
     θ ≥ 3.3·10^{−8}; products ρ(log a)ρ(log b) and cross terms between contacts as a bound (16, 17, 83).
     Reopening: a comparison preserving the U−V cancellation. **ABSENT.**
A12. Repairing the deficit with contact 2 alone (column k = 1); «2 repairs» as a universal pattern;
     improvement with each added contact (26, 37, 38, 47, 73). Reopening: one-sided bound of several
     contacts or of their joint mass. **ABSENT.**
A13. Universal pointwise positivity of h_N, of K_N = J_N + xh_N, of Ω, of I_* and of the primitives of H;
     positivity of prefixes of the Möbius inversion; replacing h_N by its modulus (27, 48, 49, 51, 55, 56).
     Reopening: cellular averages, negative part weighted by C_B or −R_N′. **ABSENT.**
A14. T_m ≥ 0 (even except for finitely many indices); positive functional per Erlang component (30, 58, 59).
     Reopening: compensation with the real weights P_d in the window m ~ √N. **ABSENT.**
A15. Absolute contraction or domination of the Möbius remainder (also grouped with Q = Π_{p≤N^{1/8}}p);
     improving constants of absolute bounds (62). Reopening: signed control of the complement.
     **PARTIAL**: RA B2 («every bound with remainder loses more») covers it in general.
A16. Global convexity of the Gaussian functional G_W; cost-free gamma–Gaussian comparison of full forms
     (52, 55). Reopening: compensate the signed fluctuation together with the ♯ loss. **ABSENT.**
A17. Discarding the polar and arithmetic tails separately via the concentration m ~ √N; omitting the
     diagonal remainder of the recurrence (61). Reopening: preserve them jointly before estimating tails.
     **PARTIAL**: RA D4 keeps only the reopening «R_L ≥ −ε_L».
A18. Completing the table with recurrences, filter identities, positive regions, eventual
     positivity and effective cutoff K(n) (falsifiers W_4 and arcsine) (42, 44, 76, 97). Reopening:
     concrete arithmetic information. **Present** in RA D4 («Recurrence or descent alone»).
A19. Row-by-row, atom or finite-certificate campaigns; extrapolating triples or certified sizes
     (5, 35, 36, 41, 44, 57). **Present** in RA D2 and A4.
A20. Universal AP monotonicity at fixed numerator; ARCH+POLAR monotonicity without rate restriction;
     AP monotonicity under pole motion in arbitrary dimension (37, 98). **ABSENT** in RA.
A21. Refining constants of the direct pointwise uniform deficit in dimension 8 (39). Reopening: preserve the
     signed integral (done in 014). **PARTIAL** (RA D2 «optimizing thresholds»).
A22. Density of high-pass tails, uniform disappearance of contacts in linear cones, exponential
     weights uniform in N, absolute extrapolation of moments (42, 75). **PARTIAL** (RA D3).
A23. Absolute STRIP contour with fixed height and constant, uniform over numerators, on cones
     j ≥ Cn^p with p < 3 (p < 2 already with P = 1) (77, 81, 92-94). Reopening: methods with signed
     cancellation, n-dependent D. **ABSENT.**
A24. Attributing convexity φ^{(k)} ≥ 0 to the full weight of W (82). **ABSENT.**
A25. Using the affine part AFF as a positive base; bounding R by cells or by Stirling (80). **ABSENT.**
A26. Turán of the full values a_{N,k} without a new arithmetic bound (76). Reopening: arithmetic proof
     of the determinant (not ruled out). **ABSENT** (RA D18 only names Pfaffians by reciprocity).
A27. Promoting identities (Λ∗1 = log, H_j > 0, log-convexity of Z_j, MASS, Abel, Rodrigues) to sign;
     sign of the diagonals of a family as sign of combinations (9, 50, 82, 99). **PARTIAL** (RA B1,
     B3).
A28. Generic positive cosh symmetry as a sign argument for an average (30). **Present** in
     RA B4/C1 («closures by cosh products»).
A29. Inferring sign from positivity of each partial contribution or from a pointwise decision (57, 79).
     **PARTIAL** (RA B2/B9 generic).

## B. PROVED positive results, with exact scope

B1. SCALAR_BRIDGE_017: W ≥ 0 on all atoms h_{N,k} ⟺ W ≥ 0 on every P/(s+u)^M (u > 1), with the
    exact identity FORM (polar included).
B2. Families of arbitrary poles ≥ 63/2 (multiplicities, no separation): 6 poles W > ‖f‖²/25 (SIX);
    7 poles > ‖f‖²/500; 8 poles > ‖f‖²/1000; 12 poles > ‖f‖²/10000; 13 poles > ‖f‖²/4000;
    14 poles with transform vanishing at 0: > ‖f‖²/1000; confluent V13 > ‖f‖²/4000.
B3. Exact transport identities: TEL, POLTEL, FULL, ONE (all n, u > ½); criterion CRIT and
    all-pass bound WT (all n, conditional on the constants).
B4. Arbitrary powers a_i > 1 (full form): pairs (073), triples (080, also 086), quadruples
    (085). For the real Φ: V‴ > 0; M″ < 0; M − uM′ > 0; R″ < 0 (086); GLOBAL-R4 and T_R > 0 (089);
    T_h > 0 (099); G_u > 0 (077); pairs and triples of K_{G_p} PD ∀p > 0 (089, 099).
B5. Complete rows at u ≥ 63/2: N = 1 (> 4/3), 2 and 3 (> 1/8), 4 (> 1/50), 5 (> 1/25), all k; rows
    1..8 at all u ≥ u_0 and 1..17 at u = 63/2 (> 1/40, individual atoms); DIFF and 3rd and 4th differences.
B6. Regions: u² ≥ 256N, k ≥ 1 (> 7/10); u ≥ 64√N, all k (> 2/5); u² ≥ 225N/4, N ≥ 3, k ≥ 1
    (> 1/40); k ≥ 10000N², N ≥ 2, u = 31.5 (> 49/50); N ≥ e^{10^6}, k ≥ 2N²/log log N
    (> (2/5)log N); Q^jP/(s+u)^n with j ≥ K(n) (054) and j ≥ 10^{12}(nq_n)³ (060), all P (> ‖·‖²).
B7. Decided atoms: F_{211,1} (3.4·10^{−15} < W/‖f‖² < 4.5·10^{−15}); g_129
    (1.34·10^{−10} < W/‖g‖² < 1.35·10^{−10}).
B8. Auxiliary arithmetic signs: NEG and MEAN (all N ≥ 2); h_N, K_N > 0 on explicit tails (020, 026,
    039, 040); band 041; ABS-TAIL (N ≥ 2^80); SIGNED-FOURIER and WIDE-WINDOW; 2V > 1/243 (g_129);
    full comb of the column k = 1 positive for N ≤ 211; exact oscillation of autocorrelations (065).
B9. Analytic lemmas: PSI Re ψ(¼+it) ≥ log|t| − 9/(8t²); CENTERED; HEIGHT; bound U_N(u); bounds on
    ψ′, ψ″; Abel P_d with TAIL/SMALL/LARGE/WINDOW/BUDGET; one-pole R12 (049); E2 on V13 with G(0) = 0.
B10. Documentary (not reproduced in these rounds): λ_A(T) ≥ 2·10^{−26} for 0 < T ≤ 1.035 (ROUND_026_A).

## C. OPEN obligations (precise statement and what was attempted)

C1. W[h_{N,k}] ≥ 0 for all N ≥ 6 (at u = 63/2: N ≥ 18) and k < 10000N² (or k < 2N²/log log N). Attempted:
    rows, regions, recurrences, descent, mixtures; the falsifiers W_4 and arcsine show that the
    structure is not enough.
C2. W ≥ 0 on the confluent blocks V_n of size n ≥ 14, or on Q^jV_n for j < J(n). Attempted:
    MULTI/FULLTEL transport with LDL per block; effective cutoff; uniform weighted norm not obtained.
C3. K = [K(a_i,a_j)] PSD for five or more powers a_i > 1. Attempted: Schur recursion on the remainder
    G_p (pairs and triples proved), Pfaffian hierarchy 083, linear densities (R4 proved; S4 not
    treated); the next level «requires a new input».
C4. (SIGNED) 2∫h_N^+(−B) − 2∫h_N^−(−B) ≥ −Arch_♯[g_N]/c_0 for all N; equivalent to controlling the
    renormalized interior R_N^inside from 1 to e^T against ARCH_♯ + 2γ − (2κ−γ)J_N(1). Attempted: full
    inverse, tails, band, Möbius grouping, signed Fourier; the margins are of order 10^{−10}.
C5. Average of I_*(e^t) against −R_N′(t) on t ≥ T_N nonnegative (031). Attempted: alternating blocks.
C6. A_N = Σ_m P_d(m)t_m ≥ 0 controlling the window m ~ √N (035). Attempted: T_m ≥ 0 (refuted), BUDGET.
C7. Δ²[a^n(I_n − J_n)] ≥ 0 for all n ≥ 4 (Tate chain 009).
C8. G_W(v) ≥ 0 for all v > 0 (Gaussian functional; would give the whole row k = 0).
C9. B_N ≤ 2NA_N for all N (would propagate A_N ≥ 0), or B_N ≥ A_N with liminf A_N ≥ 0.
C10. E_{ν+}D − E_{ν−}D ≥ 0 per nodal interval of w (065), with boundaries [E_1w′].
C11. Joint comparison U − V (Selberg) uniform in N.
C12. One-sided bound of the joint mass of contacts q ≥ 3 against ARCH + POLAR in the column k = 1.
C13. Local jet of the Schur step |u(cd − ud² + uce)| ≤ c² − u²d² and its preservation (for the arithmetic
     family pairs and triples are already covered; the next level remains open).
C14. L55-B: exact positive representation of the shifted archimedean datum on the whole primitive
     carrier, with controlled arithmetic discrepancy.

## D. Objects or ideas mentioned as not started or not examined

D1. L55-B corrections that are noncompact, non-even, or by exterior singular measures/distributions (entry 69).
D2. Other shift sizes and restricted transports different from K − K_shift(2) (entry 32).
D3. Other charts, gauges, orders or inhomogeneous equations for the ODE of K (entry 20).
D4. S side (four densities) and global S4 transport (entries 90, 102); higher hierarchy of densities (entry 104).
D5. Comparison of higher polynomial tilts (five tilts) of 103_43 (entries 84, 100).
D6. Uniform n-independent contour with even/odd separation of P(iτ) (entry 77, under study).
D7. Route FULL_TRANSFER_PLAN050 keeping contact 3: «it was not necessary to execute» (entry 72).
D8. Weighted norm uniform in j for Q^jV_n: «no impossibility is declared» (entry 73).
D9. Turán determinant with arithmetic proof (entry 76): «does not rule out a future proof».
D10. Estimates exploiting cancellation and sign cones; spectral quadratic scale (entry 42): OPEN,
     not refuted.
D11. Unequal relations between strips and other subfamilies (entry 2).
D12. Comparison of differences in N of J, K and ARCH_♯ (entry 80).
D13. Uniform −o(1) hypothesis on the pending band of 046 (entries 70, 95, 96): mentioned, not proved.
D14. Replacing the auxiliary node 0 by a free positive node (entry 15): «without another proof».
D15. Authorized numerical diagnostic at the atom 211 for separate bounds of components (entry 46): not
     incorporated; later superseded by the decision 032.

## E. Coverage

Files in the range (`ls *.md | sort`, from POWER_REDUCTION_AUDIT_044.md to
POWER_THETA_DENSITY_ORIGIN_087.md inclusive): 106. Files read in full: 106 (≈ 449 KB). No
file or portion was left unread. The sources cited by the POWER_STATE_* files that fall outside the
range (for example POWER_ARITHMETIC_BLOCK_007, POWER_HIGHPASS_015, POWER_CONTACT_DECISION_032,
POWER_GAMMA_129_DECISION_061, POWER_THETA_REMAINDER_077) were not read here; their statements are taken from
the status summaries and from the audits of the range.
