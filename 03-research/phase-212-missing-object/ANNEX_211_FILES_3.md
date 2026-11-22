# Annex 211 — third portion of files (POWER_INVERSE_INTERIOR_AUDIT_022 … POWER_RECURRENCE_BOUNDARY_036)

Complete reading, file by file, of the 66 `*.md` files of `../phase-211-sign-sandbox/` that
lie between `POWER_INVERSE_INTERIOR_AUDIT_022.md` and `POWER_RECURRENCE_BOUNDARY_036.md` inclusive, in the
alphabetical order of `ls *.md | sort`. Notation of `STATEMENT_001.md`, `POWER_CONE_001.md` and
`POWER_BRIDGE_002.md`. (★) denotes the sign λ_A(T) ≥ 0 for all T. Recurrent abbreviations of the
sources: u = 63/2; W = full form (ARCH + POLAR − comb); f_(N,k) with transform s^k/(s+u)^(N+k);
g_N = y^(N−1)e^(−uy)/(N−1)!; Φ = real even theta density; J(t)=∫_|t|^∞ sΦ, K even with K''=aΦ−J,
a=M'(0)=I2/I0; τ=J/Φ; V12 = confluent block of 12 Laguerre functions at rate u; E2 = ARCH+POLAR−contact 2.
Labels are copied as they appear in each source. «Certified computational» = outer rational/Arb
intervals with a checker; it is indicated when the result depends on it.

---

## Entries by file

**1. POWER_INVERSE_INTERIOR_AUDIT_022.md** — Audit of `POWER_INVERSE_INTERIOR_022` (outside the range).
Object: h_128(1)=Σ_m μ(m)m^−32 A_128(log m), full Möbius inverse of the gamma kernel of 020.
Result: APPROVED, checker PASS: −2/3 < h_128(1) < −33/50 with full tail m≥65 < 10^−10.
Falsifier: refutes «h_N(x) ≥ 0 for all N,x». Does not prove negativity of F_N, of the pairing with B nor
of W; continuity + OUTER020 give at least one sign change before log x = 127/30.
Reusable positive: certified (computational) pointwise value of the full inverse at x=1, N=128.

**2. POWER_INVERSE_KERNEL_020.md** — Inverse h_N(x)=Σ μ(m) m H_N(mx), H_N = x^−33 A_N(log x),
A_N = 32P_N − P_N′ (positive coefficients). Label: PROVED (explicit region all N; global N=2).
Results: (OUTER) H_N/4 ≤ h_N ≤ 7H_N/4 if log x ≥ (N−1)/30; (ROW2) h_2 ≥ H_2/[2ζ(32)] > 0 on x≥1;
(RANGE) |h_N/H_N−1| ≤ 2^−q[1+2/(q−1)], q=32−d/log x>1; (LOCAL) F_N bounded by an interior pairing on
[1,X_N] plus an explicit favorable tail. Unsigned remainder: interior pairing ∫_1^{X_N} h_N B; sign of ERR.
Reusable positive: OUTER and ROW2 as they stand, only for this gamma kernel at u=63/2.

**3. POWER_INVERSE_LOGCONCAVITY_025.md** — D_N=33P_N−P_N′, c_j=p_j(3d+30j)/(2d−j); compensated inverse
K_N(x)=x^−32 Σ μ(m)m^−32 D_N(log x+log m). Label: PROVED (LC all N; cutoff N=129; ERR129<−33/50).
Results: (LC) log D_N concave for all N≥2 (covariance of decreasing ratios); (CUT) if
D_N′(t0) ≤ 30D_N(t0) then K_N ≥ x^−32 D_N(log x)/4 > 0 for log x ≥ t0; N=129, t0=2/3 (Fraction
certificate): K_129>0 on x≥2; (FULL) ERR_129 = −2Σ S_129(n) < −33/50 (with CELL_TEST024 for n=2).
Remainder: compare the deficit ARCH_♯ with −ERR: W[g_129]/C(0)=ARCH_♯/C(0)−ERR still has no sign.
Positive: LC for all N; FULL only at N=129.

**4. POWER_INVERSE_LOGCONCAVITY_AUDIT_025.md** — Audit of 025. APPROVED, checker PASS.
Confirms LC, CUT (K_129>0 on x≥2), ERR_129<−33/50 on the whole half-line, K_129(1)<0 intact.
States: covariance and coefficient ratios are classical; the advance is the improved cutoff. It is not W≥0;
it does not extend to other N nor to a new window T.

**5. POWER_JOINT_AUDIT_027.md** — Audit of DISCRETE_BALANCE027 and INTERIOR_CONSTRAINT027 (outside the
range) and of an extension §8. Label: APPROVED, PASS.
Results: (JOINT-TAIL) W/C0 = ∫_1^4096 K·Ω + R with 0<R<10^−36 (N=129, real joint tail); Ω ≥ ℓ −
(4log t+9)/t, Ω>0.009 on the tail. (JOINT-GAP) exact Jensen identity for the Gaussian mixture
V=β/G; negative curvature of the full Gaussian functional for v ≥ 65536 (refutes global convexity).
§8: h_N = E h_a, K_N = E K_a (mixture of Gaussian inverses), NEG128/NEG129 force a_h,a_K.
Unsigned remainder: ∫_1^4096 K Ω (interior). The deficit .15 of 026 belonged to the comparator, not to W.

**6. POWER_JOINT_SCALE_016.md** — Family f_(N,k). Label: PROVED formulas; OPEN sign cone;
FALSIFIED two justifications. Results: (BETA) Z=τ²/(u²+τ²) ~ Beta(k+½, N−½); (PACKET) for k/N→c,
c_f(t)/‖f‖² → cos(u√c t): contact 2 does not disappear in the linear cone; (MEAN) E y = (N−½)/u;
(WEIGHT) ‖e^{ηy}f‖²/‖f‖² ≥ exp[2η(N−½)/u] for all k; (VAR) dispersion; (GRAM) full beta Gram.
NO-GO (falsifier): uniform disappearance of contacts in the linear cone; weighted exponential constant
uniform in N in any cone of k; also for two centered weights of fixed amplitude.
OPEN: ∃C with W ≥ 0 for all numerators and k ≥ CN or k ≥ CN². Positive: BETA, MEAN, VAR, GRAM.

**7. POWER_LOGCONVEX_CURVATURE_AUDIT_101.md** — Audit of 101. APPROVED / PROVED for the auxiliary
class. Reproduces coefficients, inverse, concentration and margin −393/250 δ⁴. Scope: refutes only
generic sufficiency of strong convexity + log-convex V″ + derivative signs for triples; it is not the real Φ
nor negative W; does not refute an invariant class incorporating the real data 077/089/099.

**8. POWER_LOGCONVEX_CURVATURE_OBSTRUCTION_101.md** — Potential v=cosh t + 10^−4 cosh 10t, A=10^46,
three nodes u_i = i·10^−4, vector (1,−2,1), kernel K_M(U,W)=[M(U)+M(W)]/(U+W).
Label: PROVED (analytic falsifier of an auxiliary class). Result: c^t K_M c < −3δ⁴/(2A) < 0.
Countermodel for the class: V even, v″ ≥ 101/100, (log V″)″ > 0, all even derivatives > 0, odd ones > 0
for t>0. Reopening: only a class preserving the real pair inputs 077/089/099; a
«succession of generic strengthenings» omitting them is not justified. Reusable positive: none for the sign.

**9. POWER_LOW_TABLE_018.md** — Row k=0, g_N; ERR: F_N = (2/c0)∫_0^∞ E0(e^t)e^{−t/2}[C_N/2−C_N′]dt with
E0 = ψ_Λ(x)−x+1. Label: PROVED budget formula; OPEN interior sign.
Result: with only |E0| ≤ A x^θ, exact budget D_N(θ)=2+2θ J_N(θ−½); D_N(0)=2; D_N(θ)→1/(½−θ)
(θ<½); D_N(½) ~ (√π/u)√N; for θ>½, D_N(θ)=Θ(√N[1−b²/u²]^−N) (exponential growth).
Remainder: W[g_N]/c0 = ARCH_♯/c0 − F_N, limit C0+4<0: a SIGNED arithmetic inequality on ERR is missing.
Positive: formula (ERR) with correct endpoint and (D), for this test.

**10. POWER_MIXED_FOUR_CAUCHY_CLIP_AUDIT_109.md** — Audit of design 109 (intersection of coefficients
with Cauchy bounds |φ_k| ≤ 2^{40+k}, |J_k|,|K_k| ≤ 2^{42+k}). Design and literal APPROVED; final result:
exit2 / INCONCLUSIVE due to budget (8192 REST evaluations), origin PASS 16/16, REST certified only on
[½, 2645/512]. No independent reproduction of 109. Insufficient enclosure, not an obstruction.

**11. POWER_MIXED_FOUR_CAUCHY_CLIP_DESIGN_109.md** — Design 109 on the compact range of the mixed Wronskian
W_t(K,J,Φ,J″), 0<t<64. Label: BUILD FINISHED exit2/INCONCLUSIVE. Same result as 10.
Condition: 110 runs only if 109 does not give FULLPASS (fulfilled). No new sign.

**12. POWER_MIXED_FOUR_COMPACT_AUDIT_107.md** — Audit of design 107. Design and literals APPROVED;
fixed INCONCLUSIVE run reproduced: 11 evaluations, 0 accepted leaves, depth 10 at
λ∈[0,1/65536], determinant [±2.94e−3]; REST did not start. Enclosure failure, not refutation. Reopening:
another object or representation, designed and audited before running; do not readjust depth/precision.

**13. POWER_MIXED_FOUR_COMPACT_DESIGN_107.md** — Design of the compact certificate of W_t(K,J,Φ,J″)>0 on
(0,64): origin in λ=t² (polynomials of degree 512, 128 modes), REST with the normalized integrals of 106 and
Gauss–Legendre 64. Label: AUDITED DESIGN; RUN INCONCLUSIVE AT THE ORIGIN. Reusable formulas:
J_k=−φ_{k−1}/(2k), K_k=(aφ_{k−1}−J_{k−1})/(2k(2k−1)); W_t=64t⁶W_λ; bounds |φ|<2^40, |J|,|K|<2^42 on |λ|≤½.
Recorded suggestion: form the determinant as a polynomial in λ before evaluating (carried out in 108).

**14. POWER_MIXED_FOUR_FACTORED_RATIO_AUDIT_110.md** — Audit of design 110. Design and literal
APPROVED; main run and independent reproduction ended exit2/INCONCLUSIVE at 8192
evaluations, logs byte-for-byte identical; certified coverage: origin λ∈[0,¼] and REST [½, 845/32].
Update: with the analytic tail of 104 (t≥16) **WM: W_t(K,J,Φ,J″)>0 for all t>0** is declared
(PROVED, certified computational + analytic) and the implications of 112 are activated. Global OPEN.

**15. POWER_MIXED_FOUR_FACTORED_RATIO_DESIGN_110.md** — Exact identity Θ16(y)=d(1+R16(y)), d=2y−3,
B_m=m⁴+3m²(m²−1)/d; quotient Θ16(y+v)/Θ16(y)=(1+2v/d)(1+R16(y+v))/(1+R16(y)); p16 = 2y−9/2−6/d−R_t/(1+R16).
Label and result: as in 14 (INCONCLUSIVE alone; WM activated together with 104). Reusable positive:
the algebraic factorization of the theta quotient.

**16. POWER_MIXED_FOUR_ORIGIN_AUDIT_104.md** — Audit of 104. PROVED / approved; gate PASS
(Dmix>0) reproduced. Analytic exterior: W_mixed/Φ⁴ > 6t²/y² for t≥64, improved to **t≥16**.
Recorded warning: Dmix<0 would have discarded only global Chebyshev4 of that family; Dmix>0 only gives a
sign on a neighbourhood without radius. Intermediate compact range OPEN at that time (closed later by 110).

**17. POWER_MIXED_FOUR_ORIGIN_DESIGN_104.md** — Mixed system [K,J,Φ,J″] (K even). Label: PROVED positive
pointwise gate and analytic tail. Results: W_t = 64Φ0⁴ t⁶[Dmix+O(t²)], Dmix>0 (outer rational
interval, certified computational); exterior model W[a/P²,t/P,1,tP]=128a(6t²+4t−1)/P²; (POSITIVE-TAIL)
W_mixed(t)/Φ(t)⁴ > 6t²/y² > 0 for all t ≥ 64, extended to t ≥ 16. Reusable holomorphic bounds on the
strip (|p−2y|<6, |p′|≤5Y, Re p ≥ Y; |T1−1/p²|≤15/Y³; |K/Φ − a/p²| < (16+|z|)/Y³).

**18. POWER_MIXED_FOUR_POLYNOMIAL_AUDIT_108.md** — Audit of 108. Design and literal APPROVED;
INCONCLUSIVE run reproduced: degree 2042, 15 evaluations, 4 leaves, coverage λ∈[0,141/8192], stop
at depth 10 with central coefficient already [±1.79e−4]. Neither falsifier nor obstruction.

**19. POWER_MIXED_FOUR_POLYNOMIAL_DESIGN_108.md** — Determinant formed in the ring of interval
polynomials in λ before evaluating; bound |exact det − P| ≤ 96·2^−400·(2^62+1)³ < 2^−200; exact Taylor
shift. Label: EXECUTED / INCONCLUSIVE. No new sign.

**20. POWER_MIXED_NORMALIZED_INTEGRAL_106.md** — Holomorphic normalized integrals τ=J/Φ, κ=K/Φ on the
strip S={Re z ≥ −1/16, |Im z| ≤ 1/16}. Label: ANALYTIC LEMMA PROVED; GLOBAL SIGN OPEN.
Results: (ZERO-FREE) |Rθ|<1/4: Θ and Φ zero-free on S; (NORMALIZED) τ=∫(z+r)A dv, κ=∫[ar−(z+r)r²/2]A dv
with factor e^{−v}; (COLUMN), (V-TAIL) < 2^−450, (MODE-TAIL) < 2^−698, (W-BOUND) 2^108,
(REGULARIZED-BOUND) 2^168; §8 (GAUSS-ERROR) 2^(−83+5j). Reusable positive: all these bounds
(an evaluation tool, not a sign tool).

**21. POWER_MIXED_NORMALIZED_INTEGRAL_AUDIT_106.md** — Audit of 106 and §8. ANALYTIC LEMMA APPROVED,
without execution. Confirms all bounds; warns that the compact range, mixed Chebyshev4, the finite crossing of U
and global W remain OPEN (at that time).

**22. POWER_MIXED_VOLTERRA_AUDIT_105.md** — Audit of 105. Proof and literal APPROVED. Confirms the
identity E w′ + (2−2qτ)w + X′S − Y′D = E y and the sign change of the raw kernel H(t,s)=R(t)−T(t)τ(s)
(H(t,t)<0 for large t; H(t,s)→R(t)>0 as s→∞). Scope: only positivity of the RAW kernel.

**23. POWER_MIXED_VOLTERRA_OBSTRUCTION_105.md** — Equation (RAW-VOLTERRA) w′+Bw+∫_t^∞ H(t,s)w(s)ds = 1,
w = −S′, S = κ′/τ′. Label: PROVED analytic. NO-GO (class: raw Volterra kernel pointwise
nonnegative): [X′−τY′]/(tp) → −2, hence H changes sign for every large t. Explicit reopening: other
equations obtained by gauge, integration by parts, compensation, change of unknown or reordering
are not excluded. Auxiliary positives: τp/t → 1 (TAU-LIMIT); S(∞)=0; D=∫_t^∞ τw.

**24. POWER_MIXTURE_AUDIT_015.md** — Filter H=(s+u)/(s+v), Q=s/(s+u). Label: PROVED identities and
convergence for u>1; no sign of components. Results: (FIN) W[f_v]=R0Σ_{k≤K}a^kW[Q^k f0] +
a^{K+1}W[Q^{K+1}f_v]; (INF) W[f_v]=R0Σ_k a^k W[Q^k f0] absolutely convergent (u>1); mixture over all
the new poles with weights w_k ≥ 0; Rayleigh_ARCH(Q^{k+1}f0) ≥ Rayleigh_ARCH(Q^k f0) (not for W).
Warning: for ½<u<√½ the polar multiplier of Q has modulus >1. Obligation: W[Q^k f0] ≥ 0 for
all k and every P of degree <n would transport the sign to all rates ≥ u.

**25. POWER_MOVING_BALANCE_036.md** — Law P_d(m) of 035, energy tilts Q^P, Q^Π (polar and
modulus of the real comb). Label: PROVED. Results: binomial representation (BETA)/(BINOMIAL);
(CONCENTRATION) M/d → 1/32 under both energies (not √N); (POLAR-DOM) factor 3969; (CHEB)
ψ_Λ(x) ≥ x/2 − 16 (proof via central binomial); (PRIME-LOWER) Π_N ≥ P_N/2 − 33; log Π_N/N → log(3969/3968).
Procedural NO-GO: «the tail outside C√N has small probability, hence polar and comb are omitted
separately» is false. Reopening: signed compensation done BEFORE separating components, within t_m.

**26. POWER_PACKET_SCOPE_AUDIT_009.md** — Family f_n=(D²−¼)y^{n−1}e^{−uy}. Label: PROVED
concentration, identities, re-audit of the bridge; OPEN finite arithmetic inequality.
Results: E_n τ² = u²/(2n)(1+O(1/n)); W_n = Arch_n + e_n − 𝓕_n, limit threshold C0+4 (same center E0
already recorded); recurrence J_{n+1} = −(2nu)^{−1}∂_u J_n; Arch_{n+1} − Arch_n = Cov(m,w)/E(w) ≤ 0.
Remainder: W_{n+1}−W_n = (Arch) − Σ 2Λ(q)q^{−½}[ρ_{n+1}−ρ_n](log q), unsigned. Bridge 002 re-audited without
defect: positivity of ALL sizes of the ladder 32+n would suffice; it does not supply its sign.

**27. POWER_PAIR_OBSERVABLE_SCOPE_100.md** — Observable η = −K′/J of the real pair. Label: PROVED.
Result: 0 < η(t) < a/t for t>0 (POINTWISE), η(0)=0: η is not monotone in any sense;
E_{J,u}[η] = a/M(u) − 1/u, h(u²) = u/E_{J,u}[η]. NO-GO: using this η in a two-copy comparison class
that REQUIRES an increasing observable (extension of 073). Open: comparisons admitting ascent and
descent, other observables or pairs.

**28. POWER_PAIR_OBSERVABLE_SCOPE_AUDIT_100.md** — Audit of 100. APPROVED. Confirms −K′>0, the bound
a/t and the identity of means; attributes the non-monotonicity of F(u) to 081; scope bounded to the class requiring
monotonicity.

**29. POWER_PARTICULAR_ORIGIN_AUDIT_093.md** — Audit of 093. APPROVED; run and reproduction
FULL PASS 128 panels; NUM<0, Dpart ≈ −21658.198 (strict enclosure). Scope: sign near 0 without radius;
no global sign of the particular Wronskian nor cone invariance.

**30. POWER_PARTICULAR_ORIGIN_DESIGN_093.md** — Particular Wronskian W(w,v,w″,K), w=tΦ, v=−Φ′,
K″ = v − cw, c=1/a, K odd with K(0)=K(∞)=0; W = 64Φ0⁴t^10[Dpart + O(t²)], Dpart = Pκ + Qc + R (explicit
formulas for P,Q,R in a_1..a_4). Label: PROVED AT A POINT (certified computational).
Result: Dpart < 0, hence W_t(w,v,w″,K) < 0 for small t>0 (required sign, verified locally).
Reusable certified intervals of I0, I1, I2, a, τ0.

**31. POWER_PARTICULAR_TAIL_095.md** — Same particular family. Label: PROVED analytic.
Result: (TAIL-PARTICULAR) W_t(tΦ, −Φ′, (tΦ)″, K) < 0 for all t ≥ 64, with model
W[t,q,tq²,1/q] = −128q²(6t²+4t−1) and remainder C t³y0, C<2^98. Holomorphic bounds (COMPLEX) on Re z ≥ 3:
|p−2y|<6, |p′| ≤ 5Y, Re p ≥ Y; (IBP-REM) |K/Φ − 1/p| < (6+25|z|)/Y². Intermediate interval OPEN in the source.

**32. POWER_PARTICULAR_TAIL_AUDIT_095.md** — Audit of 095. APPROVED / PROVED for t ≥ 64.
Reproduces the model determinant and the 7 multilinear terms; specifies that 093 (neighbourhood of 0) and 095
(t ≥ 64) do not join into a coverage of all t>0.

**33. POWER_PEANO_MONOTONICITY_AUDIT_091.md** — Audit of 091. APPROVED / PROVED in the declared
class. Confirms REAL-W3 = w³(B′)²J > 0, cofactors ε³W3(−1,3,−3,1) and the two prefixes of opposite
signs. Sign of the Peano integral, anchored minor and real T_h: OPEN at that time.

**34. POWER_PEANO_MONOTONICITY_OBSTRUCTION_091.md** — det[w,v,w″,K] at four nodes = ∫_0^∞ sζ(s)
[Π(s)/s − Π(b)/b]ds (PEANO), ζ = v − w/a, Π = Σ ℓ_i (s−t_i)_+. Label: PROVED.
NO-GO (class: global monotonicity of Π(s)/s for all four-node sets): for equispaced nodes
near any t0>0, Π/s decreases on (t1,t2) and increases on (t2,t3).
Reopening: compensation between intervals, comparison with the position/mass of the crossing b, or a different kernel.
Positive: (REAL-W3) W(w,v,w″) = w³(B′)²J > 0 for all t>0; ∫_0^∞ sζ = 0, unique crossing of ζ.

**35. POWER_POLAR_MOVEMENT_005.md** — Pole motion with polar: (F) E_new − E_old =
[Cov_μ(m,R) + (r0 − E_μR)P_old]/E_μR. Label: PROVED (identities, sector, falsifier, high order one,
order-4 derivative); OPEN global order-4 transport. Results: the sector P_old ≤ 0 is transported; falsifier:
E(2) − E(1) = 4/5 − π < 0 at order one (refutes «arch+polar grows when poles increase» in general); order one with
u ≥ 8 PROVED; (D4) quartic identity; rational SOS certificate: dE/dv_j > 1/420 at (u,u,u,u), u=63/2,
for every numerator of degree <4 (certified computational, Fraction). Remainder: dominate (E_μR − r0)P_old by
the covariance when P_old > 0; an absolute bound on the polar is not enough.

**36. POWER_POLE_MOVEMENT_004.md** — Rayleigh_v(P) − Rayleigh_u(P) = Cov_μ(m,R)/E_μR ≥ 0. Label:
PROVED (CITED the confluent certificate 004). Results: (PM) all compressed archimedean eigenenergies
increase when poles are increased individually; (WT) ‖e^{uy/2}f‖² ≤ B_n‖f‖², B_n=(25^n−1)/12;
comb ≤ 3/1000, polar ≥ −21/500 for n=3; Q[Σ c_i X^{−a_i}] ≥ ‖f‖²/20 for ALL triples of exponents
≥ 32. Limit: B_n grows like 25^n and the lowest confluent eigenenergy decreases with n; there is no uniformity in n.

**37. POWER_POLYNOMIAL_003.md** — h = e^{−63y/2}P(e^{−y}), z=e^{−y}, ⟨P,Q⟩_J = ∫_0^1 z^62 PQ,
D_nP(z)=P(z/n). Label: PROVED identities; OPEN uniform sign. Results: (C) Comb = −2Σ Λ(n)n^−32
⟨P,D_nP⟩_J; (P) polar with moments z^30, z^31; (A) archimedean matrix; Jacobi basis via Rodrigues with
rational norms and moments; D_n triangular, not self-adjoint (cannot be replaced by a positive
contraction). Goal not achieved: an estimate in the basis e_j controlling C+P against A while preserving the
triangularity of D_n.

**38. POWER_POST013_CONSTRAINTS_014.md** — Scope audit (does not close routes). Specifies: prop:opcalc
covers convolution identities, does not exclude inequalities preserving a restricted spectral measure,
positive terms or exact coupling with the polar. Records: WITNESS006 (dimension 12) gives negative AP and
negative sign if ONLY contact 2 is deleted — any theorem valid after that deletion does not give (★).
Sufficient target: semidefiniteness of ALL Laguerre blocks at a single rate (CONFLUENT_BRIDGE_014).
A single scalar chain f_n or a union of small spaces does not inherit that sufficiency.

**39. POWER_PRIMAL_AUDIT_045.md** — Audit of CONTACT_FLOOR045 and PRIMAL_PAIR045. APPROVED, PASS.
Raw floor m(240) − A_{2345} < −0.5: only that cutoff-240 criterion fails. Documentary correction: the
largest PROVED endpoint located in the local certificate pipeline is T = 207/200 (logs certified:true
μ = 2·10^−26); for T ≈ 1.098 there is no final certification log. Conditions L55-B: explicit positive
representative pair on the WHOLE primitive carrier, with controlled slack and in-band arithmetic coincidence.

**40. POWER_PRIMAL_PAIR_045.md** — Representative pair (μ, ν) with ARCH + ε‖F‖² = ∫Φ_F dμ + ∫c_F dν and
ν|(−2T,2T) = ν_Λ, at T = 3/5 (contacts 2, 3). Label: PROVED. Rigidity lemma: if η = μ − (q_T+ε)dτ
is an even compact measure, η = 0. Falsifier: q_T(0) < −15/2, hence there is no fixed-tail pair with
compact correction and ε ≤ 15/2. Noncompact subcase (r even tempered, exterior remainder an even finite measure)
coincides EXACTLY with a certificate of the dual program (D) of Paper 46. Reopening: noncompact
corrections outside that subcase (singular measures, distributions). Contact 4 is not added as a
compact repair.

**41. POWER_PRIME_AUDIT_014.md** — Audit of PRIME_TRANSFER014. PROVED identities and universal falsifier
of E2; OPEN restricted inequalities. Confirms the exact identity W[f_v] − R0W[f0] =
(1−R0)W[G], G = sF0/(s+v); the counterexample only proves E2[G] < 0, not W[G] < 0. R12 suffices for the first
move, not for a sequence without hypotheses on intermediate spaces.

**42. POWER_PRIME_BALANCE_033.md** — Normalized comb Σ Λ(q)w(q), w(q)=2q^−½C″_{N+1}(log q)/‖f_{N,1}‖²,
on REGION (u ≥ 63/2, 3 ≤ N ≤ 2u²/9 − u/3 + 3/2). Label: PROVED. Results: (DECAY) w(mq) ≤ m^−2 w(q),
q ≥ 5; operator D f(q) = Σ_{m≥2} f(mq) with 0 ≤ D^j w ≤ ρ0^j w, ρ0 = 2389/3600; b(n) = log n −
log2·1_{2|n} − log3·1_{3|n} − log2·1_{4|n} ≥ 0; (BRACKET) for K odd S_K ≤ A(w) ≤ S_K + ρ0^{K+1}L(w);
(FULL) B_N + S_K ≤ W/‖·‖² ≤ B_N + S_K + ρ0^{K+1}L(w). OPEN: B_N(u) + S_K > 0 on a new range.

**43. POWER_PRIME_PATTERN_FALSIFIER_008.md** — f = (d²/dy² − ¼)y^{n−1}e^{−uy}, n = 2^17, zero polar.
Label: PROVED. Results: E_f τ² < 1/100; Arch/‖f‖² < −383/100; each contact q ≤ 1024 contributes
< −Λ(q)q^−½‖f‖² (all harmful). NO-GO of the universal pattern «low contacts always repair the
negative arch+polar directions» in the fixed confluent family. Obligation (TAIL): the segment q > 1024
must exceed 383/100 + Σ_{q≤1024} Λ(q)q^−½. W[f] < 0 is not claimed.

**44. POWER_PRIME_TRANSFER_014.md** — One-pole filter. Label: PROVED identities and falsifier;
OPEN transport restricted to V12. Results: (C) c_{f_v} − R0c_{f0} = (1−R0)[c_{f0} − P_v∗c_{f0}] with
kernel δ − P_v of mass zero; (T2) coupled identity ARCH+contact2+POLAR; (GAIN) W[f_v] − R0W[f0] =
(1−R0)W[G]. Falsifier: E2[f_v] < (u²/v²)E2[f0] for the Tate test of order 2^17 and v = 65/2.
Declared route: a signed inequality for W on corrections G_j with numerator divisible by s, with ALL
contacts; condition R12 (resolved later in 049 for the first step).

**45. POWER_QUADRATIC_017.md** — Cone k ≥ max(cN², 4N), P=1. Label: PROVED. Results: (STRIP),
(CORR) |R_{N,k}(t)| ≤ C(c)e^{−|t|} by shifting the density (not the norms); (PRIME) |Comb| ≤ 14C(c)‖f‖²;
eventual sign theorem: W[f_{N,k}] > 0 for N ≥ N0(c), k ≥ cN²; (GAUSS) and (PROFILE)
W/‖f‖² = ½log N + log[u√c/(2π)] − 2ΣΛ(q)q^−½ e^{−u²c(log q)²/8}cos(μ_N log q) + o(1); appendix:
m(τ) ≥ log(|τ|/2π) − 4. Limit: only P=1; not the first dimensions; the PROFILE series has no proved sign.

**46. POWER_QUADRATIC_EXPLICIT_017.md** — Same object with band Im z = 15. Label: PROVED.
Result: for N ≥ 2, k ≥ 10000N²: |c_f(t)|/‖f‖² < 5e^{−15|t|} (CORR15) and W[f] > (49/50)‖f‖² (CONE),
all contacts included. Limit: only P = 1; not k < 10000N².

**47. POWER_QUADRATIC_EXPLICIT_AUDIT_017.md** — Audit of 46. APPROVED, PROVED, checker PASS.
Confirms each constant and direction of inequality; also re-audits QUADRATIC017 without defects.

**48. POWER_R12_AUDIT_048.md** — Audit of ENDPOINT048. The endpoint and the polar complement APPROVED;
uniform R12 OPEN (at that time). Confirms E2[G] > ‖G‖²/50 on V13 ∩ {G(0)=0} and |Polar[Q^jF]|/M_j ≤
(9/62)^j|Polar[F]|/M_0. Continuity only gives a neighbourhood without effective radius.

**49. POWER_R12_AUDIT_049.md** — Audit of CENTERED_CUTOFF049 (outside the range) and R12_TRANSPORT049.
APPROVED; finite certificate PASS for j = 1..13. Analytic cutoff: E(τ^−2) < 1/405 and ARCH > 859/800 for
all j ≥ 14. Resolves R12 at the first move from V12 with c = 1/2500; not full W nor iteration.

**50. POWER_R12_ENDPOINT_048.md** — Endpoint v=u of R12. Label: rational certificate of the endpoint;
uniform R12 OPEN (in the source). Result: (ENDPOINT) E2[G] > (1/50)‖G‖² for G ∈ V13, G(0)=0
(certified computational, rational LDL). Complement: tridiagonal compression of q, ⟨qF,F⟩ ≥ ‖F‖²/576,
M_j ≥ 576^−j M_0, Polar[Q^jF] = (−1/3968)^j Polar[F].

**51. POWER_R12_TRANSPORT_049.md** — Label: PROVED. Result: (R12-PROVED) E2[G_v] > (1/2500)‖G_v‖²
for all F ∈ V12∖{0} and all v ≥ u, G_v = sF/(s+v) (FINITE j=1..13 computational + TAIL j ≥ 14 analytic +
mixture MIX). Consequence: (E2 − c‖·‖²)[f_v] ≥ (u²/v²)(E2 − c‖·‖²)[F]. Remainder: contacts q ≥ 3 on the
shifted space unbounded; iteration to intermediate bases not proved.

**52. POWER_REAL_PAIR_DOUBLE_LIMIT_103.md** — Pair (D_p, Ψ_p), next step E = G_q(dA − qB),
U = B − γE. Label: PROVED analytic + NEGATIVE pointwise test; criterion §11 CONDITIONAL. Results:
(PAIR-LIMIT) pD_p → J, (ap/c)Ψ_p → K; U_lim(0) < 0 (certified computational; later redundant);
(H-RATIO) (H/K)′ < 0; (ALL-Q-RATIO) (E_q/K)′ < 0 and Ξ_q > 0 for all q > 0 in the limit pair;
(FINITE-BRIDGE) βD_p + p²Ψ_p = λK, Ψ_p = (λ/p)E_p, (Ψ_p/K)′ < 0, (D_p/K)′ > 0 for every finite p;
(MIXED-FORCING); §11.4: [K,Φ,J] Chebyshev3, S′ < 0 (MIXED-CONVEXITY), first three Wronskians of
[K,J,Φ,J″] positive. Pending in the source: fourth Wronskian (closed later by 104+110).

**53. POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md** — Audit of 103 and its extensions. PROVED /
APPROVED; FULLPASS reproduced. Confirms the iterated order of limits (p→∞ then q→0), that convergence
on compacts does NOT transfer the global root count to finite p, and that mixed Chebyshev4 is not deduced from EVEN4.

**54. POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103.md** — Test P = 720I0²(K0Hmass − Kmass H0) (homogeneous
polynomial of degree 4 in I0..I6). Label: FIXED DESIGN executed; NEGATIVE result reproduced:
P ∈ [−3.168e−13 ± 2.2e−30]. Verifies a necessary condition; not a falsifier.

**55. POWER_REAL_PAIR_MONOTONICITY_102.md** — Label: PROVED analytic (uses 075/077/078/089).
Results: Rolle lemmas with multiplicities and boundaries (one endpoint, D2, Lp, GAIN); (K-RATIO) (K/J)′ < 0;
(EVEN4) [J,Φ,J″,Φ″] Chebyshev of dimension 4; (PAIR-RATIO) (Ψ_p/D_p)′ < 0 for all p,t > 0; §8:
(NEXT-DENSITY) E > 0, (NEXT-TRANSFORM), (NEXT-RESIDUE) r_q > 0; complement with 099: R_next(z) > 0 for
all p,q,z > 0. Pending in the source: crossing of U = B − γE (closed later in 112 under WM).

**56. POWER_REAL_PAIR_MONOTONICITY_AUDIT_102.md** — Audit of 102 and §8. APPROVED / PROVED for the real Φ
and all p,t > 0. Specifies that node 0 of the congruences is auxiliary, not an admissible generator of W.

**57. POWER_REAL_SECOND_PAIR_AND_TP2_112.md** — Under WM (activated by 110+104). Header label:
implications activated, global OPEN. Results: (SECOND-POSITIVE) U has a unique −/+ crossing and Ξ > 0
for all p,q > 0; (SECOND-RATIO) (E_{p,q}/Ψ_p)′ < 0; (DIVIDED-GREEN) E_{p,q} = η(Ψ_p − Ψ_q)/(q²−p²);
(STRICT-TP2) for V(x,t)=Ψ_{√x}(t); (STRICT-CONFLUENT) ∂_t∂_x log V > 0; §8 (STAR-RATIO), (ZERO-STAR-RATIO).
Remainder: for the finite pair, Ξ_{p,q}/E_{p,q} decreasing requires the five-function family
[K,J,Φ,J″,Φ″] (Φ″ appears in the forcing); not TP3, not all orders.

**58. POWER_REAL_SECOND_PAIR_AND_TP2_AUDIT_112.md** — Audit of 112. The implication APPROVED; real
application activated by the WM update. Confirms that TP2 is not deduced from individual monotonicities (111) and that
the next forcing contains Φ″ with coefficient −raC: mixed ECT4 is not repeated automatically.

**59. POWER_REASSESSMENT.md** — Strategic review. Global sign OPEN. Explicit antecedent:
M(u) = L(u+½) and K_M is the same generating function of the corpus (R162_803 Theorem H, D-16 of the crossword).
Balance: bridges in norm; four arbitrary powers with exponents > 1; thirteen with exponents ≥ 32;
WM and consequences 112; no new window T (the assisted certificate 207/200 stands). Operational
rule: do not launch another higher-order certificate; before building, write down which property
simultaneously controls all sizes, how it is proved without assuming the sign and which hypothesis avoids the
obstruction of the antecedent.

**60. POWER_RECIPROCAL_PFAFFIANS_083.md** — K_ij = (F_i+F_j)/(u_i+u_j), R = u/F, S = uF.
Label: PROVED as an algebraic identity; appendix: identities and sufficient criterion PROVED, real
discharge CONDITIONAL/OPEN. Result: (ALL-ORDERS) det K = P_n(A_R)P_n(A_S)/∏R_i (bordered Pfaffians at
odd order); (INTERPOLATION-EVEN/ODD); Rolle hierarchy D_{k,j}; (TAYLOR-HANKEL). Obligation:
P_n(A_R)P_n(A_S) ≥ 0 for all principal subsets and all n; unverified sufficient condition:
μ_m = (−1)^m a_{m+1} a moment sequence with positive shifted minors, for R and S.

**61. POWER_RECIPROCAL_PFAFFIANS_AUDIT_083.md** — Audit of 083. APPROVED / PROVED identity.
Specifies: a positive total determinant is not enough for PSD; signs of Pfaffians at arbitrary order not
proved; positivity of J/K does not give the moment condition.

**62. POWER_RECIPROCAL_SECANT_CONCAVITY_090.md** — Label: PROVED (lemma; theta application with input
089). Results: (SECANT-CONCAVITY) f′ > 0, T_f = 2f′f‴ − 3f″² > 0 ⇒ x/(f(x)−f(0)) strictly concave
(also with interior anchor, both orientations); h″ < 0 globally; pairs of G_p PD; (ONE-REST-CURVATURE)
S_G″ < 0 for all p,x > 0; (ANCHORED-FIVE) W(x,x²,G,xG) = −a²G⁴T_h. NO-GO (§9, explicit falsifier
w = (5−e^{−x})/4): T_f > 0 globally does not imply T_H > 0, T_H(0) = −1/192. Real T_h: closed later by 099
according to the header update; inheritance to the next level open.

**63. POWER_RECIPROCAL_SECANT_CONCAVITY_AUDIT_090.md** — Audit of 090 and appendices. APPROVED.
Confirms the lemma, the promotion to PROVED after 089 FULL PASS, S_G″ < 0, ANCHORED-FIVE and the falsifier of
generic inheritance (only that automatic promotion).

**64. POWER_RECIPROCAL_SECANTS_082.md** — Label: PROVED as an algebraic criterion. Result: under
strictly PD pairs, all triples of K_F are PSD ⟺ R and S concave in x = u²; (DET2), (RECIPROCAL),
(DET3) det K_F = Vandermonde²/(H1H2H3)·R[u²,v²,w²]S[u²,v²,w²]. Admits nonmonotone F. Pending in the source:
discharge for G_p and preservation under Schur.

**65. POWER_RECIPROCAL_SECANTS_AUDIT_082.md** — Audit of 082. APPROVED / PROVED. Confirms that δ_R,
δ_S cannot both be negative and that the criterion is exact at order 3, not a pattern for order 4.

**66. POWER_RECURRENCE_BOUNDARY_036.md** — Recurrence A_{N,k} = (α/S)A_{N,k+1} + (β/S)A_{N+1,k}.
Label: PROVED. Results: (FRONT) finite boundary identity with beta-binomial weights; (INV)
E[1/(N+J−3/2)] = (S−1)/[(N−3/2)(S+L−1)]; (ARCH-UP); (ENERGY) energy of the cone 017 on the diagonal
frontier = O(log L/√L) → 0; (REMAINDER) R_L → A_{N,k}; (STOP-WEIGHT); (SURVIVAL) mass that never touches the
cone > 0. Exact remainder: R_L. Sufficient condition: R_L ≥ −ε_L with ε_L → 0 (genuine arithmetic estimate);
no new route is declared. Does not exclude other frontiers with energy control.

---

## A. Deduplicated «do not relaunch» list and cross-check with RULES_AVOID.md

Format: item — source — reopening condition — status in `RULES_AVOID.md`.

A1. Absolute budgets |ψ−x| ≤ A x^θ as the decisive step in row k=0 — 018 — only with a SIGNED
arithmetic inequality on ERR compensating C0+4. **Present generically** (B2: «Includes bounds in absolute
value of ψ(y) − y»); the quantification is missing: «D_N(θ) grows exponentially in N for θ > ½ and like √N
at θ = ½».

A2. Uniform disappearance of contacts in the linear cone; weighted exponential constant uniform in N
(also centered, fixed amplitude) — 016 — reopening: weights with N-dependent η or cancellation instead of
absolute values. **Absent.**

A3. Omitting polar and comb separately in the tail of the mass law P_d — 036 MOVING — only signed
compensation BEFORE separating, in the band m ~ N/32. **Absent.**

A4. Recurrence/diagonal frontier alone — 036 RECURRENCE — only with R_L ≥ −ε_L. **Present and exact** (D4:
«Recurrence or descent alone — only with a signed arithmetic bound on the remainder R_L ≥ −ε_L»).

A5. Universal ordering E2[f_v] ≥ R0E2[f0] — 014 — only on a positive restricted base (R12, resolved
for the first step). **Absent.**

A6. «Low contacts always repair the negative arch+polar directions» — 008 — no reopening;
the obligation is (TAIL) with the full tail. **Absent** (B8 «pattern of observables» is something else).

A7. «Arch+polar grows when poles increase» in general; absolute bound |polar| at order 4 — 005 — only with
rank and dimension hypotheses, preserving P_old > 0 with the covariance. **Absent.**

A8. Pointwise positivity of the Möbius inverse h_N ≥ 0 for all N,x — 022 audit — falsified; reopening not
indicated. **Absent.** D7 of RULES_AVOID («Variants of budget 022 — only if they also pay ARCH_♯ and
justify their scope in k») is consistent with 025/027 (comparison with ARCH_♯ is missing), but does not mention this
pointwise falsifier.

A9. Representative pair with compact spectral correction and fixed tail — 045 — reopening: noncompact
corrections outside the subcase that returns to (D). **Absent.**

A10. Raw Volterra kernel H(t,s) = R(t) − T(t)τ(s) treated as positive — 105 — reopening: gauge, IBP,
change of unknown or reordering. **Absent.**

A11. Global monotonicity of Π(s)/s (Peano) for all nodes — 091 — reopening: compensation between
intervals or comparison with the crossing. **Absent.**

A12. Generic strengthenings of hypotheses on the potential (strong convexity, log-convex V″, signs of
derivatives) as sufficient for triples — 101 (and 074) — only a class preserving the real inputs
077/089/099. **Absent.**

A13. Observable η = −K′/J in classes requiring an increasing observable — 100 — reopening: comparisons with
ascent and descent. **Absent.**

A14. Generic inheritance T_f > 0 ⇒ T_H > 0 under H = x/(f − f0) — 090 §9 — falsified; real T_h requires specific
data (anchored five-column minor). **Absent.** D5 («Schur–Green monotonicities — only with a
different joint invariant preserved by each operation») covers the spirit, not this falsifier.

A15. Transferring global root counts from p → ∞ to finite p by convergence on compacts — 103 —
falsifiable only with uniform control of tails; resolved later by a different route (WM). **Absent.**

A16. TP2 deduced from individual monotonicities — 111 (cited in 112) — **Absent.**

A17. Repeating interval certificates while readjusting depth, precision or budget after seeing data —
107–110 — only a new object or representation, audited before running. **Partially present**
(D2: «Adding filter dimensions, optimizing thresholds, extending the tower of finite orders»; the operational
rule of REASSESSMENT «do not launch another higher-order certificate» is not cited).

A18. Global convexity of the full Gaussian functional — 027 audit — falsified (negative curvature for
v ≥ 65536). **Absent.**

A19. Comparing only AP for all degrees; theorems valid after deleting only contact 2 — 014 POST
(WITNESS006) — reopening: exact use of weights distinguishing that deletion. **Present generically** (B5,
E «finite deletion»), without the mention «exclusive deletion of contact 2».

A20. Joint cancellation of Pfaffians using only reciprocity — 083 — **Present and exact** (D16,
memory of the project rules): «Expanding matchings and again using only reciprocity provides no new
mechanism». The source adds the concrete sufficient condition (Taylor moment sequence for R and S) that
RULES_AVOID does not capture.

A21. Bridge: rebuilding the density bridge — 002/009 — **Present and exact** (D1).

Inexactitudes detected: no statement of RULES_AVOID contradicts these files. Two points of
precision: (i) C5 «total positivity of order ≤ 4 (PF₄ OPEN)» and C1 «total positivity of order ≥ 5»
refer to another kernel; 112 proves STRICT-TP2 for the family V(x,t) = Ψ_{√x}(t), which must not be read
as progress on that PF₄; (ii) D7 cites «budget 022» without distinguishing the INTERIOR inverse 022 of this
portion, whose conclusion is a pointwise falsifier, not a budget.

## B. PROVED positive results with exact scope

B1. 020 OUTER/RANGE (all N, log x ≥ (N−1)/30) and ROW2 (N = 2, all x ≥ 1): full Möbius inverse of the
gamma kernel at u = 63/2.
B2. 025 LC: log(33P_N − P_N′) concave for all N ≥ 2; general CUT; K_129 > 0 on x ≥ 2; ERR_129 < −33/50
(certified computational in the cell n = 2).
B3. 027: JOINT-TAIL (N = 129, T = 4096, 0 < R < 10^−36) and JOINT-GAP (exact identity).
B4. 016: BETA, MEAN, VAR, GRAM (exact formulas for f_{N,k}).
B5. 015: FIN (u > 1/2), INF (u > 1), mixture of poles; monotonicity of Rayleigh_ARCH under Q.
B6. 017: eventual sign W[f_{N,k}] > 0, N ≥ N0(c), k ≥ cN², P = 1; 017 explicit: W > (49/50)‖f‖² for
N ≥ 2, k ≥ 10000N², P = 1; m(τ) ≥ log(|τ|/2π) − 4.
B7. 018: ERR formula with endpoint and budget D_N(θ) with its three regimes.
B8. 004: PM (all archimedean eigenenergies when moving poles); WT; Q ≥ ‖f‖²/20 on all triples
of exponents ≥ 32 (uses the confluent certificate 004, CITED).
B9. 005: identity (F); sector P_old ≤ 0; order one u ≥ 8; dE/dv_j > 1/420 at the confluent point
u = 63/2, degree < 4 (rational SOS), with a neighbourhood without radius.
B10. 003: exact Jacobi coordinates (C), (P), (A), (D).
B11. 033: DECAY, CONTRACT, BRACKET, FULL, MAGNITUDE on REGION.
B12. 036 MOVING: CONCENTRATION, POLAR-DOM, PRIME-DOM, CHEB ψ_Λ(x) ≥ x/2 − 16, PRIME-LOWER.
B13. 036 RECURRENCE: FRONT, INV, ARCH-UP, ENERGY, REMAINDER, STOP-WEIGHT, SURVIVAL (u = 63/2, N ≥ 18
for the frontier part; N ≥ 2 for ARCH-UP).
B14. 045: rigidity lemma for even compact measures; q_{3/5}(0) < −15/2; identification of the noncompact
subcase with (D).
B15. 048 ENDPOINT (E2 > ‖·‖²/50 on V13 ∩ {G(0)=0}); polar remainder (9/62)^j of the orbit Q^jV12.
B16. 049 R12-PROVED: E2[G_v] > ‖G_v‖²/2500, F ∈ V12, all v ≥ u (E2 = ARCH+POLAR+contact 2 only).
B17. 082 exact order-3 criterion (DET2, DET3); 083 ALL-ORDERS (identity), INTERPOLATION, TAYLOR-HANKEL.
B18. 090 SECANT-CONCAVITY (with interior anchor); h″ < 0; pairs of G_p PD; S_G″ < 0 for all p; ANCHORED-FIVE.
B19. 091 REAL-W3 > 0. 093 Dpart < 0 (neighbourhood of 0). 095 W_part < 0 for t ≥ 64. 100 0 < η < a/t.
B20. 102: Rolle lemmas; K-RATIO; EVEN4 Chebyshev4; PAIR-RATIO; NEXT-DENSITY; R_next > 0 (all p,q,z).
B21. 103: PAIR-LIMIT; H-RATIO; ALL-Q-RATIO and Ξ_q > 0 (limit pair, all q > 0); FINITE-BRIDGE;
FINITE-RATIOS; Chebyshev3 of [K,Φ,J]; MIXED-CONVEXITY.
B22. 104 + 110: **WM, W_t(K,J,Φ,J″) > 0 for all t > 0** (analytic for t ≥ 16; certified
computational and reproduced on [0, 845/32]); 106 holomorphic evaluation lemmas.
B23. 112 (under WM, activated): SECOND-POSITIVE, SECOND-RATIO, DIVIDED-GREEN, STRICT-TP2, STRICT-CONFLUENT,
STAR-RATIO, ZERO-STAR-RATIO.
None of B1–B23 is a lower bound of λ_A(T) on a new window.

## C. OPEN obligations (precise statement and what was attempted)

C1. ∃C: W[f] ≥ 0 for every f = P(s)/(s+u)^{N+k}·s^k with deg P < N and k ≥ CN (or CN²). Attempted: beta scale,
PACKET, uniform weights (falsified), analytic band (only P = 1).
C2. W[g_N] ≥ 0 for all N, i.e. F_N ≤ ARCH_♯[g_N]/c0 with limit C0 + 4 < 0. Attempted: absolute
budgets (018), Möbius inverses 020–025, cellular balance (ERR_129 < −33/50), joint tail 027.
C3. Sign of ∫_1^{4096} K_129(x)Ω(x)dx (interior of N = 129) and of ∫_1^{X_N} h_N B (020 LOCAL).
C4. (TAIL of 008): −Σ_{q>1024} 2Λ(q)q^{−½}c_f(log q)/‖f‖² > 383/100 + Σ_{q≤1024}Λ(q)q^{−½}.
C5. R_L ≥ −ε_L, ε_L → 0, on the diagonal frontier (036); cancellation in t_m in the band m ~ N/32.
C6. B_N(u) + S_K > 0 on REGION for a new range (033).
C7. W[G_j] ≥ 0 (or W − c‖·‖² ≥ 0) on corrections G with numerator divisible by s, with ALL
contacts and at all orders (014 GAIN); extension of R12 to intermediate bases; contacts q ≥ 3 on
the shifted space of V12 (049).
C8. Order 4: sign transport when P_old > 0, dominating (E_μR − r0)P_old by Cov_μ(m,R) (005).
C9. W[Q^k f0] ≥ 0 for all k and every P of degree < n (015); positivity of the triples of 004 uniform in n.
C10. PSD of K_ij = (L(32+i) + L(32+j))/(63+i+j) for all m (bridge 002, re-audited in 009).
C11. P_n(A_R)P_n(A_S) ≥ 0 for all subsets and all n (083); or the Taylor moment condition
for R and S.
C12. Ξ_{p,q}/E_{p,q} decreasing for finite p,q: requires a comparison for [K,J,Φ,J″,Φ″] or for
its restricted coefficients (112 §7); indefinite preservation; TP3.
C13. Sign of the PEANO integral (091) — pending in the source; real T_h resolved later according to 090.
C14. W_{n+1} − W_n with sign for the rational Tate family (009).
C15. Positive representative pair L55-B on the whole primitive carrier (045).
C16. An estimate in the Jacobi basis e_j controlling C + P against A while preserving the triangularity of D_n (003).

## D. Objects or ideas mentioned as not started or not examined

D1. Quadratic cone for ALL numerators (joint control of the complex polynomial factor and of its
Gram) — 017, 017 explicit.
D2. Centered weights with N-dependent η; analysis by cancellation instead of absolute values — 016.
D3. Signed compensation within t_m before averaging — 036 MOVING.
D4. Other frontiers (stopped or otherwise) with energy control — 036 RECURRENCE.
D5. Noncompact spectral corrections outside the subcase (D): singular measures, distributions — 045.
D6. Other Volterra representations (gauge, IBP, reordering) — 105.
D7. Compensation between intervals of the Peano kernel; comparison with the position/mass of the crossing — 091.
D8. Two-copy comparisons admitting ascent and descent; dual classes — 100.
D9. Invariant class incorporating the real pair inputs 077/089/099 — 101.
D10. Positive integral representation (anti-Löwner type) for the real M; a recurrence preserving the
TAYLOR-HANKEL minors — 083.
D11. Inequalities preserving a restricted spectral measure, positive frequency terms or
exact coupling with the polar (not covered by prop:opcalc) — 014 POST.
D12. Representation C_B of 022 as an alternative allocation of the pairing (not added to S_2) — 025.
D13. Comparison for the five-function family [K,J,Φ,J″,Φ″] — 112 §7.

## E. Coverage

Files in the range (`ls *.md | sort` order, from POWER_INVERSE_INTERIOR_AUDIT_022.md to
POWER_RECURRENCE_BOUNDARY_036.md): 66. Files read in full: 66. None omitted or sampled.
Also read, for notation and cross-check: `RULES_AVOID.md`, `OBJECT_SPEC.md`, `STATEMENT_001.md`,
`POWER_CONE_001.md`, `POWER_BRIDGE_002.md`. The sources cited outside the range were not read (e.g.
INVERSE_INTERIOR_022, DISCRETE_BALANCE027, CENTERED_CUTOFF049, 077–089, 099, 111, logs and checkers);
their contents are recorded only as the files in the range summarize them.
