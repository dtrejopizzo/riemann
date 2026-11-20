# Annex 211 — Files AUDIT_001 … POWER_DEFICIT_LIMIT_013 (61 files)

Complete reading, in alphabetical order (`ls *.md | sort`), of the 61 files of
`../phase-211-sign-sandbox/` lying between `AUDIT_001.md` and `POWER_DEFICIT_LIMIT_013.md`.
Notation of `STATEMENT_001.md` and `POWER_CONE_001.md`: (★) is λ_A(T) ≥ 0 for all T; W is the full
form (ARCH + comb + polar); AP = ARCH + POLAR; u = 63/2 is the fixed rate of the ladder; V_n(u)
is the confluent block {P(s)/(s+u)^n}; f_{N,k} is the atom with transform s^k/(s+u)^{N+k}.
Labels are copied as they appear in each file. Where a source uses an equivalence
with another statement, here «(★)» is written.

## Entries by file

1. **AUDIT_001.md** — Rereading of phases 0–99 against the window form. Object: all the
   prior material (Kreĭn realizations, prolate triples, Fredholm/Feshbach chain) indexed by
   the zero set. Result: «Hits: (honest) empty»; «Mislabels: none»; only a documentary
   gap (empty «why» cell of P60-5 in index 03). No new signed remainder; no reusable positive
   result. Structural analogies (division by depth, symbol calculus of phase 45, parity
   obstruction) declared non-routes.

2. **AUDIT_002.md** — Rereading of phases 100–160. Result: no strong hits and no mislabels.
   Weak hit 1: the identity 𝔊_T = S^{Sch}_T + J of memo M4 (phase 160) was never cross-checked against
   thm:coer-schur/(L2) (does it sharpen the uncontrolled ‖K‖ term?). Hit 2 (administrative): route N
   (Carathéodory–Fejér rigidity in the finite-window first-contact state, without limit)
   was left half-argued; it is not closed in the index; reopening with a written reason why the
   finite window avoids the «dies in the limit» failure. Cited positive: contact-cone lemma of
   M2 (PROVED, convexity, no sign).

3. **AUDIT_003.md** — Rereading of phases 161–210. Result: «None found» (hits), «None»
   (live mislabels). Stopped-not-dead: phase 209 blocked for lack of an ingredient (not NO-GO);
   residue «layer edges κ_{T+log n}» of phase 202 «without proposal»; Lemma RF.1 of phase 205
   (n₊(Φ_N) ≥ 1.95T − 2, PROVED-elementary, not integrated); candidate scalars of phase 210
   pending. Positive: SPD identity −R_α of phase 209 (survives deletions, hence does not
   transfer). Correction already repaired: the ceiling of λ_A is single exponential, not double.

4. **BRIEF_CONSTRUCTOR.md** — Rules for the phase memos. Object: protocol (sandbox, corpus
   check, labels, falsifier test (a) cΛ, (b) a_P, (c) Beurling, (d) finite modification
   of weights). No mathematical result. Mandatory closing «Result / What was proved / What failed /
   Next step».

5. **CORRECTION_RESIDUE_BALANCE_031.md** — Correction of L2_BUILD_031 (phase 188). Object: pairing of
   the Ramanujan component of modulus 2 on a balanced block (B_Q), M=Q=2, s=(1,1), profile with
   2T_0 < log(3/2), explicit smooth interpolant S. Result PROVED: P_2 = v_2/2 = log2/√2 > 0, hence
   the omission of small components in §3 of 031 is false (explicit falsifier). §5 PROVED
   (restricted scope): on rough support R_Q the universal vanishing of the 2-component holds only for
   s = 0. Theorem E of 031 remains intact; no collapse on mixed support is claimed.

6. **CORRECTION_RESIDUE_BALANCE_AUDIT_031.md** — Audit of the previous one. APPROVED: refutes the
   omission of §3/§4 of 031 for the declared interpolation; the transfer of balance by
   non-coprime multiplication fails. The rough repair is approved (only R_Q, all profiles and
   interpolants). No new negativity of W.

7. **DOSSIER_001.md** — Reverse engineering of the sign (Papers 43–48). Object: definitions,
   reduced forms (L2), (N), (S), (L), node, even inertia; PROVED tools; table of barriers;
   clauses of Problem (R) and prop:spec. Own results §6 (PROVED, elementary): (a) the sandwich
   of thm:coer-schur and lem:wh-schurabs(ii) is reversed if λ_S < 0 (correct: λ_S ≤ λ_A ≤ λ_S/(1+‖Ke_S‖²));
   (b) F_0 needs normalizing; (c) «exactly one negative eigenvalue for all T» is false for small
   T (≤1 holds, or =1 for T ≥ 0.12); (d) the half-line identity is not generic in the
   comb (ARGUED); (e) arithmetic squares on (½log2, ½log3) ⟺ λ^{∞,P}_min(T) ≥ v_2 = √2 log2 (a single
   number; should be closed); (f) T ↦ n_−(A_ev(T)) nondecreasing; (g) (L) at fixed window is trivial,
   only uniformity counts; (h) S_η (η↓0) is an exact reduction smaller than (L2), proposed as (L2′).
   OPEN: whether the Nyquist negative set grows like O(T) or e^{A_T}.

8. **LEDGER.md** — Ledger of candidates C1–C51 + F1. Labels per row (NO-GO, PIVOT, PROVED piece,
   NUMERICAL, NOT STARTED). Reusable positives: Thm 1 of C8 (max_c λ_A(T;cΛ) = Θ_T, (★) ⟺
   Θ_T ≥ 0 ∧ 1 ∈ J_T); λ_max(Π_T)/A_T ∈ [¼,½] (C14); cluster bound exp(2e^T(1+o(1))) (C15);
   first-cell coercivity (1/2π)∫m|F̂|² ≥ 0.069611‖F‖² on ∫Fe^{−y/2}=0 (C37, certified);
   λ_A(1) ≥ 10⁻²³, λ_A(1.035) ≥ 2·10⁻²⁶ (C50, computer-assisted); certified falsifiers a_3, Beurling,
   1.1Λ (F1). Open remainders: (SL_T), (EB_C), (HR)/(HR_g), (U) λ_max(A_τ) ≤ m − κ, sign of ∂_tQ.
   NOT STARTED: C4, C6, C7.

9. **LITERATURE_001.md** — Bibliographic sweep (new items only). Result: nothing beats the
   cited frontier ½log15; two new items (simplicity ⟹ parity of the ground state of the truncated
   form; simplicity/parity certificate up to half-width 1.19), both of low value, no sign.
   Categories 2–5 (signed bounds of smoothed Chebyshev, coupling of Λ with the functional equation
   off ζ(½+it), Bochner on ℚ^×_{>0}, Kreĭn extension with prime atoms, de
   Branges spaces) «nothing new». Gap pointed out: Kreĭn extension with atoms at log p, never attempted.

10. **OBJECT_SPEC_001.md** — Specification R1–R5 of the object (round 5 onward). R1 dim E_T → ∞
    (no finite Λ-free subspace carries the sign: ROUND_004_A Prop. B); R2 entries nonlinear
    in v_n, failure for cΛ, a_P, finite modifications, Beurling; R3 exact reduction or
    capture at the margin; R4 joint archimedean + Euler input; the «comb first» family escapes the
    arena count N*(T) ≥ exp(4e^T(1+o(1))); R5 falsifiers. No own result.

11. **POWER_ARCH_CELL_026.md** — Sharp deficit and joint kernel. Object: N = 129, u = 63/2,
    W[g_N]/norm² = ∫ K_N Ω, Ω(t) = d_*D(t) + 2C_B(t) + 2∫k(x)[D(t) − x^{3/2}E_x(t)]dx. PROVED:
    ARCH_sharp[g_129]/norm² < −81/100, hence the guarantee ERR_129 < −33/50 leaves a deficit > 0.15 (it is not
    W<0); JOINT identity with absolute Fubini; exact falsifier Ω(3/2) < −1/10 (lemma «Ω ≥ 0
    pointwise» FALSE). Remainder: one-sided bound of ∫K_NΩ using the real gamma restriction of K_N.

12. **POWER_ARCH_CELL_AUDIT_026.md** — Audit. ARCH_CELL026 and UNIFORM_CUTOFF026 APPROVED.
    Reusable positive (from UNIFORM_CUTOFF026): two uniform cutoffs (Jensen d ≥ 2 with
    t_J = d(d+220)/(330d+6300); Riccati 0 < q′ < M_d) proving K > 0 on the whole declared tail for
    2 ≤ N ≤ 129. Ω(3/2) < 0 and ARCH+0.66 < 0 are not W < 0.

13. **POWER_ARCH_EXACT_032.md** — Stable formula for ARCH. PROVED: for all N,
    A_{N,0} = a(u) − Σ_{j=1}^{d} b_j S_{j+1}(x) (all subtracted terms positive) and
    A_{N,1} = a + (u/2)S_2 − Σ(j+1)b_j[S_{j+1} − (u/2)S_{j+2}] (brackets > 0); absolute Euler–Maclaurin
    remainder (B_16) without next-term hypothesis. Certificate of the atom N=211, k=1: ARCH in an
    interval of width < 10⁻¹⁸. Reusable: the formula (A0)/(A1) for all N and u.

14. **POWER_ARCH_TRIPLE_004.md** — Density bound in dimension 3. PROVED: |ĥ(τ)|²/(2π‖h‖²) ≤
    Σ u_j/[π(u_j²+τ²)] (Malmquist basis) and the bound arch ≥ (2n/π)∫_0^R m·a/(a²+τ²). NUMERICAL: a = 31.5,
    n = 3 gives ≈ −0.0506, insufficient. OPEN: improve the scalar cap by ≥ 0.051 or prove that the lowest
    archimedean energy grows when rates are separated (later resolved by CONFLUENT_004).

15. **POWER_ARITHMETIC_BLOCK_007.md** — Full Laguerre block of dimension 12. PROVED (rational
    certificate): W[h] > 10⁻⁴‖h‖² for all h ∈ V12 = span{√63 e^{−uy}L_j(63y), j ≤ 11}, u = 63/2, with
    all contacts. Uses contact 2 decisively (AP+contact2 > (1/1250 − 10⁻⁸)I; tail n ≥ 3
    in norm < 3/5000). OPEN: dimension ≥ 13 or a uniform principle.

16. **POWER_ARITHMETIC_DIFFERENCES_019.md** — Signed frontier of the comb. PROVED: for all N ≥ 1,
    c_{f_{N,1}}(t) has exactly one simple root χ_N in ut, with √(2N−3) < χ_N < (1+√(8N−11))/2;
    corollary P_{N,1}(u) > 0 for 1 ≤ N ≤ 211, u ≥ 63/2 (every contact favorable); P_{N,0} < 0 always.
    Falsifier: (−Δ)^r P_{1,0} < 0, refutes «Λ ≥ 0 makes the comb differences nonnegative in
    row 1». OPEN: an inequality preserving the ARCH/comb/polar cancellation at variable orders.

17. **POWER_ARITHMETIC_WITNESS_006.md** — Explicit test. PROVED: with rational v of 12 coordinates in
    V12, −2/125 < AP/N < −1/100, every prime-power contact contributes > 0 (Q(x+40) with negative
    coefficients) and contact 2 alone contributes > 1/25; W > N/50. §4: removing only contact 2 gives
    W < −N/125. Counterexample to «AP ≥ 0 on V12»; not to W.

18. **POWER_AUDIT_002.md** — Audit of polarization and bridge. PROVED: W(h_u,h_v) =
    [L(a)+L(b)]/(a+b−1); falsifier H = 3+cosh (det < 0) refutes «positive cosh representation ⟹
    sign of mixtures»; bridge H_η (density of exp(−(31.5+k)y)); fractional bridge to all of PW_N C²;
    finite inversion by Möbius; explicit sufficient obligation: K^{(m)}_{ij} = [L(32+i)+L(32+j)]/(63+i+j)
    ⪰ 0 for all m. THREE002 (order 3 in [u,3u], u ≥ 2³⁰) and its extension to all n with
    u ≥ 2^{40n} approved; the union of those spaces is NOT dense (explicit falsifier). OPEN: sign of orders ≥ 3
    of the fixed ladder.

19. **POWER_AUDIT_004.md** — Pole motion. PROVED: with fixed numerator, the archimedean quotient does not
    decrease when any pole increases (covariance of increasing m and R); weighted bound 1302 in
    dimension ≤ 3; comb < 0.002‖f‖², polar > −0.042‖f‖² for u ≥ 63/2; with CONFLUENT_004: W >
    (7/125)‖f‖² for every triple of powers with exponents ≥ 32. Not extrapolated to arbitrary order
    (B_n = (25^n−1)/12 not uniform).

20. **POWER_AUDIT_005.md** — Motion with polar. PROVED: exact identity (AP)
    E_v − E_u = [Cov_μ(m,R) + (r_0 − E_μ[R])p_u]/E_μ[R]; exact falsifier E(2) − E(1) = 4/5 − π < 0
    (dimension 1, poles 1→2) refutes the transport of AP for all poles > 1/2. OPEN: comparison
    Cov_μ(m,R) ≥ (E_μ[R] − r_0)p_u at order 4 with rates ≥ 31.5. Approved FOUR005 (W > (1/5) on V4),
    quartic D4 > 0.075N² (local transport of 4 poles, no radius) and scalar theorem n=1, u ≥ 8.

21. **POWER_AUDIT_006.md** — Audit of test 006. PROVED and rerun: −2/125 < AP/N < −1/100,
    autocorrelation recomputed independently, W/N > 3/125; extension approved: without contact 2,
    W/N < −1/125. Scope: one explicit test, not the block.

22. **POWER_AUDIT_007.md** — Falsifier of uniform transport in high dimension. PROVED:
    0 ≤ τm′(τ) < 4 globally; P_n = 4^n/[u·binom(2n−2,n−1)](1−1/(4u²))^{−n}; at u = 63/2, n = 131072,
    uE′_diag < −140/31: the AP quotient of a fixed numerator decreases when a pole is moved. Falsified class:
    monotonicity of the AP quotient for all numerators and orders. Does not refute monotonicity of λ_min nor
    transport preserving only the sign.

23. **POWER_AUDIT_008.md** — Audit of the opposite pattern of low contacts. PROVED: f = (D²−¼)g,
    g = y^{n−1}e^{−uy}, n = 131072: both moments vanish, AP/‖f‖² < −383/100, all contacts
    q ≤ 1024 negative; necessary obligation: the tail q > 1024 would have to exceed
    383/100 + Σ_{q≤1024}Λ(q)q^{−1/2}. The «repair by low contacts» pattern (006) is not universal.
    Does not prove W < 0.

24. **POWER_BALANCE_AUDIT_020.md** — Audit of SIGNED_BALANCE020 and INVERSE_KERNEL020. APPROVED:
    FAIL2 at N=211, k=1 (ARCH/norm < −0.74, 0 < P_2 < 0.075, polar < 0 ⟹ form with only contact 2
    < −0.66); full Möbius kernel h ≥ H/4 > 0 on log x ≥ (N−1)/30 for all N, and global for N = 2.
    OPEN: bound on the interior pairing on [1, exp((N−1)/30)] and magnitude of the comb remainder.

25. **POWER_BALANCE_AUDIT_033.md** — Audit of PRIME_BALANCE033 and COEFFICIENT_BALANCE033.
    APPROVED: decay w(mq) ≤ m^{−2}w(q) for q ≥ 5; telescoping with alternating-sign brackets
    (ρ < 2/3); A(w) ≥ 3600L(w)/5989; finite Erlang mixture and Abel; E_22 ∈ (−0.01, −0.006) on a profile
    that is not positive definite. OPEN: sign of the comparator's lower bound; T_m ≥ 0. Warns that margins of
    10⁻¹⁵ require preserving cancellation, not componentwise budgets.

26. **POWER_BLOCK_AUDIT_007.md** — Audit of the block V12. PROVED: W|V12 > 10⁻⁴ I, with review of
    contact factors, Euler–Maclaurin, exact LDL and full tail (Λ ≤ log n for all n ≥ 3). No
    positivity is deduced when adding modes nor for other 12 rates.

27. **POWER_BOUNDARY_AUDIT_035.md** — Audit of BOUNDARY_BALANCE035 and SIGNED_TRANSFORM035.
    APPROVED: terminal W[f_{17,0}] > 0.041 n_17; convex descent; rows 1..17, all k ≥ 0, u = 63/2,
    W > ‖f‖²/40. SIGNED_TRANSFORM035: A_N is the expectation of signed t_m = T_m/h_m under the law P_d; BUDGET
    O(N⁻²) for finite prefixes. OPEN: arithmetic control of the moving window; terminal ≥ 18.

28. **POWER_BOUNDARY_BALANCE_035.md** — Terminal datum and descent. PROVED: W[f_{17,0}]/n_17 > 1/25
    (ARCH_17 > −0.868, polar_17 > 0.911, adverse comb < 1/500 by slope bound q(log2) > 15);
    with a_{N,0} = a_{N,1} + u²a_{N+1,0} (normalized convex combination) and the k=1 column of 034:
    W[f_{N,k}] > ‖f‖²/40 for 1 ≤ N ≤ 17, all k ≥ 0, u = 63/2. Reusable pattern: positive k=1 column
    + one positive k=0 terminal ⟹ descent. OPEN: M ≥ 18, variable rates, mixtures.

29. **POWER_BOUNDARY_WEDGE_029.md** — Uniform region. PROVED: for all N ≥ 1, k ≥ 0, u ≥ 64√N,
    W[f] > (2/5)‖f‖² (bilateral weights ±η cancelling the shift; ARCH > 9/20; comb < 1/5000;
    even polar ≥ 0, odd > −1/1000). Scope: the wedge is not enough for the fixed-rate bridge; positive
    mixtures of its densities do not approximate fixed-rate atoms (SCALE_BRIDGE_LIMIT_029).

30. **POWER_BRIDGE_002.md** — Bridge from powers to PW_N. PROVED: space B (g = e^{5y/4}ρ(e^y) ∈
    H^{1/4}); Q continuous on B (B1/B2); PW_N ⊂ B; density of X^{−(32+n)}; finite realization by Möbius
    of every compact test. CONDITIONAL consequence: K^{(m)} ⪰ 0 ∀m ⟹ W ≥ 0 on every test ⟹ (★).
    Polarization verified (P_ab = R_ab). OPEN: the sign of the ladder.

31. **POWER_CELL_AUDIT_024.md** — Audit of CELL_BALANCE024 and CELL_TEST024. APPROVED: LOCAL/
    BUFFER, OUT-CELL (every cell with n−1 ≥ exp((N−1)/30) favorable), Möbius interface 31Q − Q′ = P;
    first cell N=129: 31/100 < ∫_1²K C_B < 8/25, 33/100 < S(2) < 1/3. K_129(1) < 0 compatible with
    positive means. OPEN: interior cells and ARCH_sharp deficit.

32. **POWER_CELL_BALANCE_024.md** — Budget of negative K. PROVED: S_N(n) = b_nJ_N(n) +
    (H_{n−1}/2)∫_{n−1}^{n}[1 − (n−1)²/t²]K_N; BUFFER S_N(n) ≥ b_nJ_N(n) − [H_{n−1}/(2n)]M_N(n);
    integrated criterion J ≥ 0 and M ≤ 4aJ ⟹ S ≥ 0 (a = ¾ − log2); OUT-CELL for all N. Missing:
    Σ S_N(n) ≥ −ARCH_sharp/[2C_N(0)]. §7: with LOGCONCAVITY025, K_129 > 0 on x ≥ 2, ERR_129 < −33/50.

33. **POWER_CELL_TEST_024.md** — First-cell test. PROVED (rational certificate, full Möbius tail
    < 10⁻¹⁰): for N = 129, 31/100 < ∫_1²K C_B < 8/25, 33/100 < S(2) < 1/3,
    1/2 < ∫_1²K x⁻² < 3/5. No sign of total ERR nor of W.

34. **POWER_CENTERED_CUTOFF_049.md** — Effective cutoff j = 14. PROVED: for every polynomial P of degree
    ≤ 11 and every j ≥ 14, E_{μ_j}[(1−q)/q] < 49/20 (weighted Bernstein proved via Gegenbauer
    eigenpolynomials + integration by parts); therefore E_G[τ⁻²] < 1/405 and ARCH[Q^jF_0] > (859/800)‖·‖²
    for every F_0 ∈ V12. OPEN: indices j < 14, contact 2, polar, prime tail; global sign.

35. **POWER_CENTERED_MOMENT_053.md** — Exact matrix moment. PROVED (13 LDL pivots): (6/5)T_96 −
    T_95 ≻ 0 with (T_j)_{ab} = 4^{−j}binom(2j, j+a−b); monotonicity r_{j+1} ≤ r_j by covariance; for all
    j ≥ 96 and F ∈ V13: ARCH > (12/5)‖·‖², E23 = AP + contacts 2,3 > (1/10)‖·‖². OPEN: segment
    j = 1..95 and contacts n ≥ 4.

36. **POWER_CENTERED_MOMENT_AUDIT_053.md** — Audit. APPROVED: binomial Gram, monotonicity by
    covariance for each numerator, constants; fixes the pending segment j = 1..95 and the tail n ≥ 4.

37. **POWER_COEFFICIENT_BALANCE_033.md** — Erlang mixture and Abel. PROVED: MIX ρ_N = Σ w_{Nj}S_j with
    w_{Nj} ≥ 0, Σ = 1; W[g_N]/norm² = Σ w_{Nj}E_j; ERLANG-FAIL −1/100 < E_22 < −3/500 (profile not
    PD: transform −1/(2048u)); WEIGHT −11/(50d) < w_{N,22}E_22 < 0; ABEL W = Σ(v_m − v_{m+1})T_m,
    T_m = Σ_{j≤m} jE_j. The premise «T_m ≥ 0 ∀m» FALSIFIED in 034. Reopening: change the grouping
    or introduce a genuine compensation.

38. **POWER_COMMON_TRANSFER_010.md** — Common transport criterion. PROVED: if
    η = b − c − DK_n − Cn/(4u²) > 0 (K_n = [(1+X/u²)^n − 1]/X), then AP[f] > c‖f‖² for all
    poles ≥ u; weighted bounds B_Y (Young), B_F = (1−α)⁻¹Σ r_F^{2j} (Fourier), B_T (maximal trace at the
    confluence, monotone in each pole); passage to W with L = 2√B Σ Λ(q)q^{−σ−1/2}. No sign at arbitrary
    dimension.

39. **POWER_COMPARISON_AUDIT_034.md** — Audit of DIVISOR_COMPARISON034 and WEIGHTED_COEFFICIENT034.
    APPROVED: W > ‖f‖²/40 for k = 1 and k ≥ 2 in the region N ≥ 3, u ≥ 31.5, u² ≥ 225N/4; combined
    coverage: rows 1..12 at u = 31.5, rows 1..8 for all u ≥ 31.5. PROVED: T_m takes
    positive and negative values at arbitrarily large indices (Pringsheim + parity), refutes «T_m ≥ 0»
    even eventually; does not refute the Abel combinations nor W.

40. **POWER_CONE_001.md** — Cone of powers. PROVED: Q[Σ c_iX^{−a_i}] = Σ d_id_j[L(a_i)+L(a_j)]/
    (a_i+a_j−1); L(a) > 0 for a > 1; two-generator criterion |u d/du log L| ≤ 1; L − uL′ > 0 for
    a ≥ 32 ⟹ Q ≥ 0 on every plane of two powers with exponents ≥ 32. Falsifier: H = 3+cosh (generic
    theta lemma false). OPEN: 1 < a < 32 and determinants of order 3.

41. **POWER_CONFLUENT_004.md** — Confluent archimedean matrix of order 3. PROVED (rational): with
    d = ψ(16) − log π, b = (63/4)ψ′(16), c = b + (3969/16)ψ″(16), M ≥ (d − √2 b − |c|)I > (1/10)I on
    span{e^{−31.5y}, ye^{−31.5y}, y²e^{−31.5y}}. Comb and polar separately (AUDIT_004).

42. **POWER_CONFLUENT_BRIDGE_014.md** — Bridge with a single rate. PROVED: span{y^k e^{−ay}} dense in
    H¹(0,∞); if for a single u all blocks V_N(u) are W-nonnegative, then (★) (CONDITIONAL).
    §6: strong approximation in H_η with rates u_N ⟺ N/u_N → ∞ (exact MOV-DIST); transported
    falsifier: with u_N = N^{3/4} contact 2 is not suppressed as O(N/u_N²). §7 MOV-TAIL: cutoff
    Q_cut = ⌈exp(40N/u)⌉ with error < e^{−N}. §8 MOV-NEC: a cutoff with log Q ≤ (2−δ)N/u gives W_{≤Q} → −∞.
    §9 PRIM-CUT: primitive with W_{≤Q} < −3 if log Q ≤ 2⁻¹²N/u. OPEN: W_{≤Q_cut} ≥ −ε_N‖f‖² on V_N(N^{3/4}).

43. **POWER_CONFLUENT_BRIDGE_REVIEW_014.md** — Brief review. APPROVED: complex convention,
    integration by parts (h(0)=0), strong norm, passage to the sign without uniform margin, exterior
    confluence with diagonal (−1)^kζ(a). Sufficiency only for complete blocks with all their cross terms.

44. **POWER_CONFLUENT_FOUR_005.md** — Four confluent poles. PROVED: AP > (49/200)I and |comb| <
    (13/1000)I ⟹ W > (1/5)‖h‖² on V4(31.5). Falsifier: Arch[(1,−1,1,−1)]/‖v‖² < −1/10 refutes «ARCH
    positive for any number of poles ≥ 31.5 with small remainder». Not four arbitrary rates.

45. **POWER_CONFLUENT_THIRTEEN_052.md** — Confluent V13. PROVED: W[f] > ‖f‖²/4000 on V13(63/2) with
    all the arithmetic (E2 > 3/10⁴, E23 > 7/25000, tail n ≥ 4 < 10⁻⁵); complementary pivot to ZERO13:
    0.0003 < σ(W) < 0.0005. In the Schur direction, AP ≈ +0.0184 and contact 2 ≈ −0.0180 (adverse),
    contact 3 also adverse. Not thirteen arbitrary poles.

46. **POWER_CONFLUENT_THIRTEEN_AUDIT_052.md** — Audit. APPROVED, five PASS; correct reading of
    components at a fixed vector (not Rayleigh quotients) and of the tail n ≥ 4.

47. **POWER_CONTACT_AUDIT_032.md** — Audit of ARCH_EXACT032 and CONTACT_DECISION032. APPROVED:
    3.4·10⁻¹⁵ < W[f_{211,1}]/‖f‖² < 4.5·10⁻¹⁵. The negative partial sum up to 300 of 021 was due to
    omitted favorable contacts. A single atom.

48. **POWER_CONTACT_BALANCE_021.md** — Scale of cancellation in one atom. PROVED: FAIL234
    (AP + P_2 + P_3 + P_4 < −0.21) and tail 0 < Σ_{q>300}P_q < 5·10⁻¹³. NUMERICAL: partial sum up to 300
    ≈ −6.08·10⁻¹⁴. No sign of W; resolved in 032. Lesson: separating components by coarse bounds does not
    resolve the balance.

49. **POWER_CONTACT_BALANCE_AUDIT_021.md** — Audit. APPROVED with separation between exact
    proofs (FAIL234, tail) and NUMERICAL diagnosis.

50. **POWER_CONTACT_DECISION_032.md** — Decision of the atom F(s) = s/(s+63/2)^{212}. PROVED:
    3.4·10⁻¹⁵ < W/‖f‖² < 4.5·10⁻¹⁵ (ARCH of width < 10⁻¹⁸, exact polar, contacts ≤ 512, tail
    < 1.1·10⁻¹⁵ of favorable sign). Not a row, neighbourhood or window.

51. **POWER_CONTACT_FLOOR_045.md** — Cutoff 240 when 5 enters. PROVED (specific scope): for
    ½log5 < T ≤ ½log7, A_T > 17/4 and m(240) < 15/4, hence s_∞ ≤ m(τ_N) − A_T < −1/2 (FIXED-FLOOR-FAIL):
    the inherited certificate with cutoff 240 and total-mass floor cannot be maintained. Writes down the linear,
    quadratic and polar cross terms that a new representation must preserve. Changing cutoff/floor or
    repeating certifications is already recorded (008/026).

52. **POWER_CONTACT_OSCILLATION_065.md** — Exact oscillation. PROVED: for all N ≥ 1, k ≥ 1,
    K_{N,k} = c_{f_{N,k}} has exactly k simple positive roots, alternates sign, last root
    χ < 4k(N+k−1); therefore, for u log q ≥ 4k(N+k−1), each comb term has sign (−1)^{k+1}
    (favorable tail for k odd, adverse for k even). No magnitude nor sign of W.

53. **POWER_CONTACT_OSCILLATION_AUDIT_065.md** — Audit. APPROVED in full (profile, vanishing
    moments, one-sided convolution lemma, last-root bound, tail sign).

54. **POWER_CORPUS_OPPORTUNITY_AUDIT.md** — Strategic review. Decision table: do not rebuild
    bridges; no more dimensions by filters; do not infer density from a positive union (requires
    liminf r(n)²/n = 0 plus another topology and cross terms); no recurrence alone (a signed remainder bound is missing);
    Schur/Green monotonicities only with a new joint invariant; do not extend the MIXED4 tower; Stieltjes/anti-Löwner
    representation = legitimate target without a candidate; no «make it global/nonlinear»; partial
    completeness only preliminary. Heat/theta/Poisson: reopen only with a concrete joint inequality.
    Reading corrections (O-151.4, 06R4, TB3-neg(ii), REF-D ≠ exclusion).

55. **POWER_CRITICAL_AUDIT_040.md** — Audit. Core and CONSTANT-CUTOFF APPROVED. Genuine opposite signs
    of the full inverse near the center; not W.

56. **POWER_CRITICAL_BALANCE_040.md** — Full inverse near the center. PROVED: 1/ζ(1+z) =
    z − γz² + R_3, |R_3| ≤ 9|z|³ (|z| ≤ 1/8, Re z ≥ 0); expansion of R_c with absolute remainder;
    CURVATURE −2q′/t < q″ < 0; CENTRAL-SIGNS h_N/H_N < −1/N, K_N/G_N > 1/N at v = ½ + N⁻²,
    N ≥ 2⁸⁰; CONSTANT-CUTOFF h_N(e^t), K_N(e^t) > 0 for t ≥ (N−1)/992 + 5. OPEN: interior integral and
    balance with ARCH_sharp.

57. **POWER_CUMULATIVE_AUDIT_023.md** — Audit. APPROVED: CELL criterion (conditional), point 128 and
    falsifier 129; universal hypothesis K ≥ 0 FALSIFIED; §7 (CB-ID, CB-POS, K-MASS, BOUNDARY)
    approved; balance and compensation of ARCH_sharp open.

58. **POWER_CUMULATIVE_INVERSE_022.md** — Compensated primitive. PROVED: J_N = Σμ(m)w_N(m·);
    MASS Σ_n J_N(n) = 1; CELL (if K_N ≥ 0 globally, F_N ≤ −2(¾ − log2)(1 − J_N(1)) ≤ 0); OUT-K; POINT
    0.003 < K_128(1) < 0.004; CB-ID F_N = −2∫K_N C_B; CB-POS; K-MASS; BOUNDARY. FALSIFIED: K_N ≥ 0
    universal (023). OPEN: quantitative control of BUDGET F = −2∫K⁺C_B + 2∫K⁻C_B that also compensates
    ARCH_sharp.

59. **POWER_CUMULATIVE_TEST_023.md** — Test N = 129. PROVED: −1/250 < K_129(1) < −1/251 (full Möbius
    tail < 10⁻¹⁰). Refutes the criterion K ≥ 0; gives no sign of J, ERR or W.

60. **POWER_DEFICIT_AUDIT_013.md** — Audit of DEFICIT_LIMIT013. PROVED for the declared class:
    0 < Rayleigh < 1/25, m(4) < −2/5, L8(c) > 1/20 ∀c ≥ 0. Outside the class: estimates that
    preserve rational measure, positive gains, polar coupling or specific filters.

61. **POWER_DEFICIT_LIMIT_013.md** — NO-GO (PROVED) of the class «separable transport by pointwise
    deficit» at order 8, u = 63/2: with v = (169,−310,405,−460,460,−405,310,−169), b < 1/25; with
    m(4) < −2/5, every pointwise loss L8(c) > 1/20, hence b − c − L8(c) − p_loss < −1/100. Reopening:
    retain gain on m ≥ c, spectral distribution of the numerator, polar coupling, specific filters
    or arithmetic contribution. Does not prove AP[v] < 0 nor W < 0.

## A. Deduplicated «do not relaunch» list (with reopening condition) and cross-check with RULES_AVOID.md

Marks: [OK] present and faithful; [INEXACT] present with a difference; [ABSENT] not listed.

A1. Rebuilding the density bridge or reparametrizing the ladder (POWER_CORPUS_OPPORTUNITY_AUDIT,
    table; BRIDGE_002; CONFLUENT_BRIDGE_014). [OK] = RULES D1.
A2. More dimensions via filters or optimizing thresholds (CORPUS_OPPORTUNITY). [OK] = D2.
A3. Density from a positive union. Source: «Criterio L2 exige liminf r(n)^2/n=0; el puente de
    forma requiere además otra topología y cruces» (the L2 criterion requires liminf r(n)^2/n=0; the form
    bridge additionally requires another topology and cross terms). RULES D3: «only with liminf r(n)² /n = 0 and a block
    that repairs the moment». [INEXACT]: missing «another topology (that of the form) and the cross terms»; the source
    does not say «a block that repairs the moment». Add also, from AUDIT_002 §8 and CONFLUENT_BRIDGE_014
    §5: a union of spaces of bounded dimension or a chain of vectors does not inherit sufficiency.
A4. Recurrence or descent alone (CORPUS_OPPORTUNITY; BOUNDARY_BALANCE_035 §6: only with a genuine positive column
    k = 1 and a genuine positive terminal k = 0). [OK] D4 as regards the remainder; [ABSENT] the reusable positive
    pattern «column + terminal ⟹ descent» of 035.
A5. Schur/Green monotonicities, class BASE (CORPUS_OPPORTUNITY). [OK] = D5.
A6. Extending the MIXED4 tower «by routine; genuine TP2 is not TP of all orders». [INEXACT] D2 says
    «extend the tower of finite orders» without the warning TP2 ≠ TP∞.
A7. Renamed heat/theta/Poisson (CORPUS_OPPORTUNITY, additional contrast). [OK] = D6.
A8. «Make it global/nonlinear» without an operation (CORPUS_OPPORTUNITY). [OK] = A4 of RULES.
A9. Positive representation of Stieltjes/anti-Löwner type: «legitimate target, without a new candidate;
    an independent formula and sign proof are needed». [ABSENT] in RULES (neither as a prohibition
    nor as open ground).
A10. Partial completeness outside a window: «only preliminary investigation: specify E and
    check identification, falsifiers and antecedents». [INEXACT]: RULES F lists it as
    «slot without an object» (O166.802.1) without the condition of specifying E.
A11. Completeness of squares / all powers (CORPUS_OPPORTUNITY). [OK] = D14.
A12. Positivity of all Abel prefixes T_m (COEFFICIENT_BALANCE_033 «Seguimiento034»: «do not
    relaunch positivity of all T_m as a lemma without changing the grouping or introducing a genuine
    compensation»; COMPARISON_AUDIT_034 §3). [ABSENT].
A13. Positivity of each Erlang component E_j (ERLANG-FAIL, 033). [ABSENT].
A14. Pointwise positivity of the joint kernel Ω (ARCH_CELL_026: Ω(3/2) < −1/10); reopening: one-sided
    bound of ∫K_NΩ with the real gamma restriction. [ABSENT] (RULES D10/D11 do not cover it).
A15. Universal positivity of K_N = J_N + xh_N and of h_N (022/023: K_129(1) < 0, h_128(1) < 0);
    reopening: integrated criterion (BUFFER/BUDGET) with a genuine estimate. [ABSENT].
A16. Omission of small Ramanujan components by block balance (CORRECTION_031). [ABSENT].
A17. Separable transport by pointwise deficit at order 8 (DEFICIT_LIMIT_013, class NO-GO PROVED);
    reopening: retain positive gain, spectral measure, polar, filters or arithmetic. [ABSENT].
A18. Monotonicity of the AP quotient under pole motion for all numerators (AUDIT_005
    falsifier 4/5 − π; AUDIT_007 uE′ < −140/31 at n = 131072). [ABSENT].
A19. «ARCH positive for any number of poles ≥ 31.5 with small remainder» (FOUR_005, vector
    (1,−1,1,−1)). [ABSENT].
A20. «AP ≥ 0 on the block and arithmetic as a perturbation» (WITNESS_006; CONFLUENT_BRIDGE_014 §6: the
    contact 2 is not suppressed as O(N/u_N²)). [ABSENT].
A21. Universal pattern of repair by low contacts (AUDIT_008) and sign of one prime uniform in
    all directions (THIRTEEN_052: contact 2 is adverse in the Schur direction). [ABSENT].
A22. Truncated principal part with polynomial cutoff (CONFLUENT_BRIDGE_014 §§8–9: MOV-NEC, PRIM-CUT; even
    with both moments vanishing). Necessary condition: liminf u_N log Q_N/N ≥ 2. [ABSENT].
A23. «Positive cosh/theta representation ⟹ sign of mixtures» (CONE_001 §4, AUDIT_002: H = 3+cosh).
    [INEXACT]: RULES C1 says «closures by cosh products», which does not capture this two-generator
    falsifier.
A24. Positivity on the union of planes of two powers as if it were on the sum (CONE_001 §5,
    BRIDGE_002 §4). [ABSENT].
A25. Total-mass floor m(τ_N) − A_T with fixed cutoff 240 after 5 enters; changing cutoff or floor or
    repeating certifications (CONTACT_FLOOR_045). [ABSENT].
A26. Componentwise budgets of order 1 against margins of 10⁻¹⁵ (BALANCE_AUDIT_033 §4,
    CONTACT_BALANCE_021 §5). [INEXACT]: RULES B2 deals with slack against the global margin; not the
    critical cancellation between ARCH, comb and polar of one atom.
A27. NO-GO LEDGER candidates not captured: C1 (lattice→continuum transfer), C9 (Schur
    with metric δ = log(lcm/gcd)), C12 (finite Λ-free planes, margin ε open), C13 (Krylov at bounded
    j), C17 (class 𝒦_gap), C21 (finite-degree Neumann), C24 (comb-mass-only class),
    C25 (measure bound + Logvinenko–Sereda), C28/C29 (fixed profile, Vaughan class + process B), C30
    (Schur by classes), C31 (sweep of the index axis), C39 (2×2 positivity of rungs), C41/C42
    (tail inequality with gauge; S-lemma multiplier forced to 1), C43 (window J_R → {1}), C48
    (generic contact entry), C49 (local Schur × archimedean), C51 (argmax of the concave background).
    [ABSENT] except C5 (germ) and C18 (homogeneous words), which RULES C1 mentions.
A28. DOSSIER §6(e): «arithmetic squares on (½log2,½log3)» reduces to one number (λ^{∞,P}_min vs
    v_2 = 0.980…; numerically ≈ 0.49 at T ≈ 0.367) and «should be closed rather than listed as open».
    RULES F: «Signed exterior measures; arithmetic squares on (½log2, ½log3)». [INEXACT]:
    presents it as open ground.
A29. Bilateral laws: RULES F lists «λ_A = L(T)(1+o(1)) on unbounded ranges» as not excluded;
    LEDGER C20 records NO-GO of the single exponential law and reduces the lower half to (N1′).
    [INEXACT]: the exclusion of the single law is missing.
A30. Route N (Carathéodory–Fejér at finite window) and C7: not closed; reopening with a written reason
    against the «in the limit» failure. [ABSENT] (neither prohibited nor listed as open ground).

## B. PROVED positive results (exact scope)

B1. Bridges and sufficiencies (CONDITIONAL towards (★)): K^{(m)} ⪰ 0 ∀m ⟹ (★) (BRIDGE_002, AUDIT_002);
    complete blocks V_N(u) W ⪰ 0 for a single u ⟹ (★) (CONFLUENT_BRIDGE_014 §4); moving rates
    require N/u_N → ∞ (§6); W_{≤Q_cut} ≥ −ε_N, ε_N → 0, on V_N(N^{3/4}) ⟹ (★) (§7, MOV-TAIL error < e^{−N}).
B2. Ladder of powers: Q ≥ 0 on every plane {X^{−a}, X^{−b}}, a, b ≥ 32 (CONE_001); every triple with
    exponents ≥ 32: W > (7/125)‖f‖² (AUDIT_004 + CONFLUENT_004).
B3. Confluent blocks at u = 63/2: V3 archimedean > 1/10; V4 W > 1/5 (FOUR_005); V12 W > 10⁻⁴
    (BLOCK_007); V13 W > 1/4000 and pivot ZERO13 ∈ (0.0003, 0.0005) (THIRTEEN_052).
B4. Highpass orbits: dim 12, j ≥ 14: ARCH > 859/800 (CENTERED_CUTOFF_049); dim 13, j ≥ 96: E23 > 1/10
    (CENTERED_MOMENT_053).
B5. Atoms f_{N,k}: wedge u ≥ 64√N, all N, k: W > 2/5 (029); k ≥ 1 and u² ≥ 225N/4, N ≥ 3: W > 1/40
    (034); rows 1..17, all k, u = 63/2: W > 1/40 (035); rows 1..12 at u = 31.5 and 1..8 for all
    u ≥ 31.5 (034 combined); atom (211,1): W ∈ (3.4, 4.5)·10⁻¹⁵ (032).
B6. Comb: one root for k = 1 and P_{N,1} > 0 for N ≤ 211, u ≥ 31.5 (019); exactly k roots and
    sign (−1)^{k+1} of the tail for u log q ≥ 4k(N+k−1) (065).
B7. Tools: stable formula of ARCH for all N (032); archimedean pole-motion lemma
    (AUDIT_004); identity (AP) (AUDIT_005); transport criterion η > 0 and bounds B_Y, B_F, B_T (010);
    0 ≤ τm′ < 4 (AUDIT_007); weighted Bernstein (049); 1/ζ(1+z) = z − γz² + R_3, |R_3| ≤ 9|z|³ (040);
    CURVATURE −2q′/t < q″ < 0 (040); bilateral weights BILAT (029).
B8. Möbius inverse: h ≥ H/4 on log x ≥ (N−1)/30 (all N), global N = 2 (020); MASS, CB-ID, CB-POS,
    K-MASS, BOUNDARY, OUT-K (022); LOCAL/BUFFER, OUT-CELL (024); CENTRAL-SIGNS and CONSTANT-CUTOFF for
    N ≥ 2⁸⁰ (040); uniform cutoffs 2 ≤ N ≤ 129 (UNIFORM_CUTOFF026 via 026-audit).
B9. Mixture identities MIX and ABEL with nonnegative weights (033); oscillation of T_m (034).
B10. DOSSIER §6: correction of the sandwich for λ_S < 0; monotonicity of n_−(A_ev); exact reduction S_η;
    arithmetic squares ⟺ λ^{∞,P}_min ≥ v_2. CORRECTION_031 §5: rough collapse.
B11. LEDGER: max_c λ_A(T;cΛ) = Θ_T; λ_max(Π_T)/A_T ∈ [¼,½]; first-cell coercivity 0.069611;
    λ_A(1) ≥ 10⁻²³, λ_A(1.035) ≥ 2·10⁻²⁶; certified falsifiers a_3, Beurling, 1.1Λ.

## C. OPEN obligations (precise statement; what was attempted)

C1. For all m: [L(32+i)+L(32+j)]/(63+i+j) ⪰ 0, 0 ≤ i, j ≤ m. Attempted: planes (order 2), triples,
    fixed-grid certificates up to 6 pivots; no principle for all m.
C2. For u = 63/2 and all N: W ⪰ 0 on V_N(u). Certified up to N = 13 (and N = 4, 12); obstruction:
    decreasing margin, adverse contacts in the Schur direction.
C3. On V_N(N^{3/4}), Q = ⌈exp(40N^{1/4})⌉: W_{≤Q}[f] ≥ −ε_N‖f‖² with ε_N → 0. Only the
    tail and the necessity of an exponential cutoff were proved.
C4. Full V13 transport: certify j = 1..95 and pay for contacts n ≥ 4 (053).
C5. Rows N ≥ 18 at u = 63/2 (terminal k = 0), variable rates, arbitrary mixtures of atoms (035).
C6. Atoms: Σ_n S_N(n) ≥ −ARCH_sharp[g_N]/[2C_N(0)]; equivalently a BUDGET bound
    −2∫K⁺C_B + 2∫K⁻C_B that compensates ARCH_sharp (022, 024, 026). Attempted: K ≥ 0 (false), Ω ≥ 0
    (false), cellular criterion (exterior cells only).
C7. Bound on ∫K_NΩ using that K_N comes from the gamma autocorrelation (026).
C8. Abel: sign of Σ(v_m − v_{m+1})T_m without requiring T_m ≥ 0 (033/034).
C9. Moving window of SIGNED_TRANSFORM035: arithmetic control of t_m under P_d.
C10. AP at 4 poles ≥ 31.5 with p_u > 0: Cov_μ(m,R) ≥ (E_μ[R] − r_0)p_u (AUDIT_005).
C11. CONE_001: L(a) − uL′(a) > 0 for 1 < a < 32 and determinants of order 3.
C12. DOSSIER: (L2) S_{T,k(T)} ⪰ 0; (N) 𝓕_T ≤ 𝔞^♯ on P_T; (S) Arch_M − Div_M − Near_M ⪰ 0;
    (L2′) S_η ⪰ 0; growth of the Nyquist negative set (O(T) or e^{A_T}); clause (5).
C13. LEDGER: (SL_T) ℛ ≤ κ − |σ_T| on E_T; (EB_C) edge budget ≤ 8πe^{2T}hλ_A; (HR_g) coercivity
    floor on ℓ_g; (U) λ_max(A_τ) ≤ m − κ uniform for T > log2; sign of ∂_tQ in the cluster.
C14. ARCH_TRIPLE_004: monotonicity of the lowest archimedean eigenenergy when rates are separated (not proved).

## D. Objects or ideas not started / not examined

D1. LEDGER C4: corona/symbol lens on M ↦ 𝔸_M (NOT STARTED).
D2. LEDGER C6: transport defect M → M+1 and coercivity of adjacent windows (NOT STARTED).
D3. LEDGER C7 / AUDIT_002 hit 2: route N (Carathéodory–Fejér at finite window, without limit) (NOT
    STARTED; half-argued in phase 160).
D4. AUDIT_002 hit 1: cross-check of 𝔊_T = S^{Sch}_T + J (M4) against thm:coer-schur.
D5. LITERATURE_001: Kreĭn extension with atoms at log p (never attempted).
D6. AUDIT_003: residue «layer edges κ_{T+log n}» (phase 202, without proposal); Lemma RF.1 not integrated.
D7. DOSSIER §6(g)/(A2): gauge-minimized leakage test of the quasi-minimizers; §6(h): growth
    of the Nyquist negative set; §7.3: mean value of |P_{s_w}|² with approximate functional equation
    (cross-check empty cell of P48); §7.7: compression of ½(D_e + HᵀD_oH) to the negative block.
D8. CORPUS_OPPORTUNITY: Stieltjes/anti-Löwner representation (no candidate); selection E of partial
    completeness (preliminary).
D9. AUDIT_005 §4: no falsifier was sought for four rates ≥ 31.5.
D10. LEDGER «next» not executed: Chebyshev resummation (C21), Lanczos sweep r ∈ [1.1,1.3] at T ≥ 4
    (C44/C46), certified Lipschitz bound of the band margin (C46), Schur of the survivor with the
    parity piece (C39).

## E. Coverage

Read in full 61 of 61 files (from AUDIT_001.md to POWER_DEFICIT_LIMIT_013.md, `ls` order),
plus RULES_AVOID.md, OBJECT_SPEC.md (phase 212), STATEMENT_001.md, POWER_CONE_001.md and
POWER_BRIDGE_002.md for notation. No file or portion of the range was left unread. The
.py files and the files cited outside the range (e.g. UNIFORM_CUTOFF026, PRIME_BALANCE033,
SIGNED_TRANSFORM035, DIVISOR_COMPARISON034, THREE002) were not read; what is said about them comes from the
audits within the range.
