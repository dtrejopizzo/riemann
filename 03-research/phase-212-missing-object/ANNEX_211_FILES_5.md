# Annex 211, block 5 — complete reading of `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md` … `ROUND_001_A.md`

Source: `03-research/phase-211-sign-sandbox/`, files `*.md` in alphabetical order (`ls *.md | sort`), from
`POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md` to `ROUND_001_A.md` inclusive: 41 files, about 454 KB, read
in full. Notation of `STATEMENT_001.md`, `POWER_CONE_001.md` and `POWER_BRIDGE_002.md`: (★) is λ_A(T) ≥ 0 for all
T; W is the complete exterior form (ARCH + polar + comb); L(a) = 1/a + 1/(a−1) − (log π)/2 + ψ(a/2)/2 + ζ′/ζ(a);
K_ij = [L(a_i)+L(a_j)]/(a_i+a_j−1) is the matrix of W on exponentials e^{−(a−½)y}1_{y>0}; Φ is the even positive theta
density of CONE_001 §7; Z(u) = ∫Φ e^{ut}, M = Z′/Z (M(u) = L(u+½)); V = −log Φ. Labels as recorded in
the source. When a source uses a statement external to the form, it is paraphrased as «(★)» or «outside the sandbox».
Two file names carry a date suffix that is omitted here (`*_[sufijo]`).

## Entries by file

**1. POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md** — Audit of the sign at the origin of the Wronskian of four
R4 densities: W_λ(1,A,B,C)(0) with A = p²−q−2p/t, B = p/t, C = (p³−3pq+r)/t (p,q,r jets of V), via the jet matrix
of Φ up to order 10 and the RAISE identity W(1,A,B,C) = −k³J²(E/J)′, k = B′. Label: APPROVED / PROVED for
the point t = 0 and an unquantified neighbourhood (rational interval certificate, theta tail paid). Remainder: global
sign in t > 0 and Chebyshev property of the four densities on the half-line; global Darboux criterion and branch
S4 OPEN. Reusable positive: W_λ(1,A,B,C)(0) < 0 (only the origin and a neighbourhood without radius).

**2. POWER_THETA_DENSITY_OUTER_088.md** — Same Wronskian in t ≥ 1. PROVED (polynomial/rational certificate
exit0/PASS, audited): G = t⁴W_t(1,A,B,C) < −4000 t²y⁶ and W4 < −4000y⁶/t² for all t ≥ 1, y = πe^{2t}; first mode
by a polynomial with 27 positive coefficients after t = 1+T, y = 21+Y; complete theta tail up to order 6 paid
(E = 62523502209/6553600000000000000000). Consequence: (E_raise/J)′ > 0 in t ≥ 1 and density determinant
negative for four nodes all ≥ 1. Remainder: the compact 0 < t < 1 (pending for Andreief on the half-line). No
global PF4 transport, no new W region, no five orders.

**3. POWER_THETA_DENSITY_OUTER_AUDIT_088.md** — Audit of 088. APPROVED / PROVED for all t ≥ 1 (same hash).
Confirms normalization of the first mode, tail up to V⁽⁶⁾, generic polynomial with 55 monomials and K = 30936927338496.
Limit: no Andreief on the whole half-line while 0 < t < 1 is missing; 087 only gives a neighbourhood of the origin.

**4. POWER_THETA_DENSITY_TRANSPORT_089.md** — Transport of the R4 sign to the global Turán. PROVED (uses the
compact certificate 089 in 0 < t ≤ 1, file `POWER_THETA_DENSITY_COMPACT_089.md`, outside this block, plus 088 in t ≥ 1).
System [1,B,A,C] with Wronskians 1, k, k²J, −W(1,A,B,C) > 0 ⇒ extended Chebyshev system ⇒
det[ρ_j(t_i)] < 0 for all 0 < t1 < … < t4; sinh(ut) strictly TP4; Andreief ⇒ det[Z′, u²Z′, uZ, u³Z](u_i) < 0;
confluence ⇒ **T_R = 2R′R‴ − 3(R″)² > 0 for all λ > 0** (R(λ) defined by f = f₁(1, λ, R, λR)). With 090 (outside
the block) and 086: h = 1/b strictly concave and all distinct pairs of the regularized remainder G_p PD for all
p > 0. Remainder: concavity of both reciprocal data of G_p, their Turán, a second Schur step, S4, five/all
orders. Reusable positive: T_R > 0 global; det of four densities < 0 at all positive nodes.

**5. POWER_THETA_G_COMPACT_080.md** — Curvature Δ(u) = c² + ucd + u²ce − 2u²d² (c,d,e = M, M′, M″) with
g″(u²) = −aΔ/(4u³c³), g(x) = a√x/M(√x) − 1, a = M′(0), on the compact 1/2 ≤ u ≤ 63/2. PROVED (certificate with 4096
panels, uniform Cauchy remainder r = 1/16, B = 6·10⁷, tail < 10⁻¹², entire function E(A) = A(A−1)ζ(A)Γ(A/2)π^{−A/2}).
With 078 (u ≥ 63/2, outside the block): **g″(x) < 0 for all x ≥ 1/4**; with 079: **K is positive definite for any three
distinct exponents a_i > 1** (complete form ARCH + polar + all contacts; diagonal congruence
to powers X^{−a}). History: direct/Taylor2/Taylor4 enclosures failed because of dependency, they are not counterexamples.
No four generators, not all orders, no window T.

**6. POWER_THETA_G_COMPACT_AUDIT_080.md** — Audit of 080. APPROVED in mathematics and code; independent
reproduction FULL PASS. Confirms deflation, Cauchy remainder, exact dyadic mesh without gaps. Result:
positive triples for all a_i > 1; not four nor all orders; 081/082 and recursive obligations separate.

**7. POWER_THETA_HAZARD_COMPACT_073.md** — (log Φ)⁗ < 0 on [0, 1/4] (five theta sums S⁽ʳ⁾, polynomials
Q_{r+1} = 2y(Q_r′ − Q_r), numerator NUM = ea³ − 4dba² − 3c²a² + 12cb²a − 6b⁴, tail from m = 5, mesh 4096).
PROVED/APPROVED. With the exterior of phase 103 (t ≥ 1/4): **V‴(t) > 0 for all t > 0 (HAZARD)**. Scope: structural
property of Φ; does not give W ≥ 0, nor does it order the five covariants of 103_43 §4.

**8. POWER_THETA_RATIO_COMPACT_077.md** — Two local signs C > 0, N > 0 in 0 < x ≤ 1, with
C = p³ + xp²q − pq − xpr + xq², N = (xq−p)C′ − xrC (p,q,r,s = V′…V⁗). PROVED/APPROVED: desingularized origin
(V⁽⁶⁾ < 0 on [0,1/16] and b < 2a², a = V″(0), b = V⁗(0), by 1024 panels) and 8192 panels on [1/16,1]. Gives L = (xq−p)/C > 0
and L′ < 0 there. Alone, it does not give G_u > 0; with 077 OUTER and REMAINDER it does.

**9. POWER_THETA_RATIO_OUTER_077.md** — The same C, J in x ≥ 1. PROVED/APPROVED (Fraction verifier, three PASS):
C > 3(1+x)y³, J > 31x²y⁴, y = πe^{2x}; first mode with 16 and 36 positive coefficients; theta tail up to order 4.
Boundaries: 0 < L ≤ 20/(3y²) → 0, wΦ → 0. Does not settle 0 < x < 1 (done in 8).

**10. POWER_THETA_REMAINDER_077.md** — One-valley criterion for the real Schur remainder. Object: F_u = J − βΦ_u,
J(x) = ∫_{|x|}^∞ yΦ, β = u²a/(ua−c); hypothesis R-HYP: R = (V′+xV″)/(−τ′) increasing and → ∞ (τ = J/Φ). Proof: forcing
f_u = Φ·B_λ with two vanishing moments ⇒ pattern +,−,+; convex interpolation of H(v) = v − √(v²−1) ⇒ F_u(0) < 0; zero
counting by Rolle ⇒ a unique simple positive zero. Sufficient local condition LOCAL-HYP (C > 0, L decreasing → 0,
wΦ → 0), discharged by 8 and 9. **PROVED: T_u(z) > 0 and G_u(z) > 0 for all u, z > 0 (REAL-REMAINDER)**. §9 corollary
PROVED: matrix anchored at {0,u,v} positive definite for u ≠ v > 0 (via K_F with F = uB, |uF′/F| < 1); the node 0 is the
exponent ½, outside the class a > 1, it is not a third W test. Remainder: positivity of the two-node kernel of G, three
generators (later done by 080 by another route), all orders.

**11. POWER_THETA_REMAINDER_AUDIT_077.md** — Audit of the 077 assembly. APPROVED for real Φ (forcing, two
moments, interpolation, negative Green, zero counting, LOCAL-HYP, compact/exterior certificates, anchored
corollary). Explicit remainder: «control the cross terms of the two-node kernel of G or a property that
dominates them». Not three generators (in this round), no W, no window T.

**12. POWER_THETA_SCHUR_DENSITY_075.md** — Positive density of the regularized denominator:
h_u = Φ[cV′ − ux], k_u = ∫_x^∞ h_u, Φ_u(x) = (1/u)∫_{|x|}^∞ sinh(u(y−|x|))k_u(y)dy. PROVED/APPROVED: k_u has a single
crossing (−/+), balance ∫cosh(uy)k_u = 0, **Φ_u > 0 on the whole line**, Φ_u″ − u²Φ_u = k_u,
H_u(z) = ∫Φ_u e^{zx} = D_u(z)/[z(z²−u²)], D_u = zcZ − uZ′, H_u > 0 and log H_u strictly convex on ℝ. Remainder: compare Φ
with Φ_u to order Z/H_u and control the kernel of G_u = (c²/(uz))[Z/H_u − Z(0)/H_u(0)] − cz/u (open in this round).

**13. POWER_THETA_SCHUR_DENSITY_AUDIT_075.md** — Audit of 075. APPROVED (Fubini clarification in NEG-MASS).
Confirms F₁(z) = −cz/u + c²Z/(uzH_u) and residue uc²/(ua−c). Nothing turns F₁ into H_u′/H_u; V_u‴ > 0 is not preserved; no
order-two Pick kernel for F₁. Φ–Φ_u comparison OPEN.

**14. POWER_THETA_TWO_COPY_073.md** — Concavity of the tilted mean via two copies. Theorem under (H): V even C³,
V‴ > 0 in x > 0, V/|x| → ∞: **M″ < 0, M − uM′ > 0, 0 < uM′ < M for u > 0** (identity 4Cov(S,D²) = M″, conditional
variance decreasing in |S|). PROVED/APPROVED also for real Φ (THETA-H by 7). Corollary PROVED: **for all
a ≠ b > 1 the 2×2 matrix K is positive definite; W[c₁e^{−(a−½)t} + c₂e^{−(b−½)t}] > 0** and the same for exterior
powers (congruence ζ(a_i)). Extends CONE_001 §5 (a ≥ 32) to all a > 1. Not three generators, no window T.

**15. POWER_THREE_002.md** — Three powers by concentration. PROVED: for A ≥ 2³¹, 0 < h ≤ A/2,
Q[Σ_{j≤2}c_jX^{−(A+jh)}] ≥ 9‖f‖² (rational all-pass basis, m(τ) ≥ log|τ| − 8, comb < 1/10, polar < 1/10); §7 PROVED:
**for each n, n distinct rates in [u,3u] with u ≥ 2^{40n} give W ≥ 9‖f‖²** (all orders with increasing threshold,
not uniform in n). §8 obstruction PROVED: the union of these families is not dense in L²(0,∞) (distance > 1.4 to every
unit function on [1,2]); sums of translated packets not controlled. Remainder: lower the threshold to a common family
of exponents or control the crossings between packets.

**16. POWER_THREE_SECANTS_079.md** — Three generators from one concavity. PROVED (implication and converse, under BASE:
M > 0, M′ > 0, M″ < 0, M(0) = 0, M/u decreasing): **all 3×3 blocks of K_ij = [M(u_i)+M(u_j)]/(u_i+u_j) with
nodes in I are PSD if and only if g(x) = a√x/M(√x) − 1 is concave on {u²: u ∈ I}**; exact identities DET, CONC, GAP
(δ_crit − δ_conc > 0). Reduced obligation: g″ ≤ 0 in 1/2 < u < 63/2 (later discharged by 5). Concavity of 1/b is not
necessary. Region u ≥ 63/2 already covered by 053 (thirteen poles).

**17. POWER_THREE_SECANTS_AUDIT_079.md** — Audit of 079. APPROVED / PROVED (implication and converse under BASE).
Falsifiers 003/074 remain in force: BASE alone does not suffice for three nodes.

**18. POWER_TWO_COPY_SCOPE_074.md** — Class falsifier. PROVED/APPROVED: explicit potential
V = A[x²/2 + x^{2p}/(2p·2^{2p−2})], p = 10⁶, A = 4·10⁸, satisfying all hypotheses (H) of 14 (V‴ > 0, all pairs
PD, M″ < 0), with nodes A, 2A, 3A and vector (40,−40,3): c^T K c < −53111/(10000A) < 0. Refutes «potential hypotheses
of 073 ⇒ 3×3 positivity». Jet test of x⁶ positive (does not falsify). Auxiliary counterexample, not of the theta datum nor of W.
Reopening: «additional specific property of Φ or concrete estimate of its crossing».

**19. POWER_TWO_COPY_SCOPE_AUDIT_074.md** — Audit of 074. APPROVED, exit0/PASS. Same scope.

**20. POWER_UNIFORM_CUTOFF_026.md** — Analytic cutoffs in N for the compensated kernel K_N (complete Möbius sum,
D_N = 33P_N − P_N′, u = 63/2). PROVED: t_J(d) = d(d+220)/(330d+6300) by Jensen on coefficients; t_R(d) by Riccati
(0 < q′ < u²/(2d−1)); **D_N′/D_N ≤ 30 and K_N(x) ≥ x^{−32}D_N(log x)/4 > 0 for x ≥ e^{t_*(N)}**; **K_N > 0 for
2 ≤ N ≤ 129, x ≥ e^{2/3}**; favourable tail cells S_N(n) ≥ (3/4 − log 2)J_N(n). Remainder: the interior cells
(number ≤ ⌈X_N⌉, exponent d/330 + O(1), increasing in N); sign of W not proved.

**21. POWER_UNIFORM_STRIP_060.md** — Uniform contour. PROVED: for real P of degree < n,
F(s) = (s/(s+u))^j P(s)/(s+u)^n and **j ≥ J(n) = 10¹²(nq_n)³** (q_n = ⌈log₂(n+1)⌉; j ≥ 10¹²n⁶ suffices):
∫|ρ(x+3i)| < 2∫ρ and **W[F] > ‖F‖²** (orthogonal polynomials of the Student weight, amplitude derivative without phase,
Taylor tail by Cauchy). Remainder: the interior j < J(n); no uniform quadratic cone, no window T.

**22. POWER_UNIFORM_STRIP_AUDIT_060.md** — Audit of 060. APPROVED. Interior open; NECESSITY059 and 016 intact.

**23. POWER_VARIABLE_RATE_HIGHPASS_096.md** — Projection of a fixed exponential f₀ = √(2u₀)e^{−u₀t} onto
Q_u^rV_n(u) uniform in the rate u. PROVED: A_{n,r}(ξ) = (1−ξ²)(1+ξ)^{2r}vᵀG^{−1}v ≤ 200n/√r for all n ≥ 1,
r ≥ 10¹²n³, ξ ∈ (−1,1) (Gegenbauer in ξ = e^{−η}, Gram in the rest). Consequence: **distance from f₀ to the union of
all those spaces, with all rates, ≥ √(1 − 1/5000)**; varying the rate does not repair the L² density of the
union (includes the cone 060). Does not treat the linear span, crossings between blocks, other continuous families.

**24. POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096.md** — Audit of 096. APPROVED / PROVED. No negative W, no
global impossibility, no new W/T coverage.

**25. POWER_WEIGHTED_AUDIT_031.md** — Audit of WEIGHTED_BLOCK031 and GAMMA_WEIGHT031 (the latter outside the
block). APPROVED. Of the real gamma factor: unique maximum of R = e^{−ut}D/(3/2) at t₀ = (2/3)d/(d+20), q″ < 0 global,
adverse cost of the increasing branch ≤ M2 = u²/(2N−3); sufficient expectation criterion without proof. The negativity of the
prefix refutes universal I_* ≥ 0, not W. Remainder: [4, ∞).

**26. POWER_WEIGHTED_BLOCK_031.md** — Weighted prefix I_*(X) = ∫_1^X (3/2)x^{−1/2}H(x)dx, H the real integrand of
W[g_N]/‖·‖² = ∫G_NH. PROVED: I_*(225/64) < −1/250, I_*(4) > 1/50; transfer to real G_N:
**∫_1^{225/64}G_NH < −3/1000 (N ≥ 2²⁴), ∫_1^4 G_NH > 3/200 (N ≥ 2²²), ∫_{225/64}^4 G_NH > 9/500 (N ≥ 2²⁴)** at rate
u = 63/2. Falsifier: «I_* ≥ 0 for all X» is false. Remainder: ∫_4^∞ G_NH; pairing inequality of all the
contacts against the complete gamma weight.

**27. POWER_WEIGHTED_COEFFICIENT_034.md** — Erlang prefixes T_m = Σ_{j≤m} jL[S_j] of 033. PROVED: generator
F(z) = [E(v) − vE′(v)]/(1−z)³, v = u(1−z), E = 2Θ′/Θ odd ⇒ F(1+s) = F(1−s); elementary Pringsheim-type lemma ⇒
**T_m takes both signs at arbitrarily large indices** (neither eventual T_m ≥ 0 nor ≤ 0). Refutes the sufficient criterion
«T_m ≥ 0 ∀m» (and up to finitely many exceptions). Does not say that the gamma combination is negative. Remainder: signed bound of the
adverse contributions against the real gamma weights, or an arithmetic grouping that preserves the compensation.

**28. PROPOSAL_POWER_CASES_*_[sufijo].md** — Proposal (OPEN, resting on a PROVED case of CONE_001): study P3,
(r₂₃ − r₁₂r₁₃)² ≤ (1−r₁₂²)(1−r₁₃²) for exponents in progression A ≥ 32; then unequal triples, four generators,
and bridge PW_N in form norm. Falsifier recalled: H(u) = 3+cosh u (log-convex) gives −129/(34 log 2) at (42,−41).
Warns: «do not extrapolate finite cases to all orders»; L² density alone does not suffice. Later status: P3 superseded
by 5 and 14 (pairs and triples for all a > 1).

**29. README.md** — Framework of the phase: internal forms (L2), (S), (B); east tunnel (archimedean, Nyquist, Schur) and
west tunnel (fluctuation Σ Λ(n)φ(n/x)); meeting point: an object with exact Λ, coupled to the functional equation by a route
different from the factor ζ(½+iτ), nonlinear, that decides at near-coincidences. Threads stopped without NO-GO: nonlocal kernel
(209), «layer edges κ_{T+log n}» (202), finite-window Carathéodory–Fejér route N (160), Lemma RF.1 (205).
Tools never aimed at P47: Toeplitz/corona symbol (Paper 26), coercivity of adjacent windows (38),
exact transport defect (39), Carleman determinacy (22), finite-to-total uniformity (15), PNT
truncation (7). Candidates C1–C5.

**30. NEAR_CASES_RESULTS_*_[sufijo].md** — Elementary cases. Auxiliary PROVED: improvement of nearfree with ε = 1/(KM)
(without log log M): a(F_b)/‖F_b‖² ≥ log K − C′_χ − E − 2ζ(5)C_χ/K⁵. Algebraic falsifiers: (i) «activating a nearby contact
improves/worsens in Loewner order» false already in dimension 2; (ii) 3×3 matrix with diagonal 1 and off-diagonal entries
−0.6: pairs PD, eigenvalue −0.2 (pairs do not suffice); (iii) **cycle (p,p,p²) with Λ(p²) = Λ(p): cubic term −2x²z < 0
for p = 2** (x = log2/√2, z = log2/2); there is no favourable cancellation of the first cycle. None is negativity of the
form (d → ∞). Remainder: control the collective norm of the near-contact matrix against the archimedean energy.

**31. REVIEW_001.md** — Review of STATEMENT_001 and DOSSIER_001. Confirmations and corrections: §3 of STATEMENT is
P47 lem:transl(iv) + thm:band (not new; needs 2T₀ < log 2); the 2×2 band is necessary, without sign. Errors of P47
pointed out: «λ_A ≤ λ_S» false if Ke_S ≠ 0, lower bound λ_S/(1+‖K‖)² ≤ λ_A false if K ≠ 0 (valid only with λ_S ≥ 0);
normalization of F₀ (c₀(0) = ‖F₀‖²); «exactly one negative eigenvalue for every window» false (n₋ = 0 for small
T; correct «≤ 1» or «= 1 for T ≥ 0.12»). Half-line identity: non-genericity in the comb ARGUED. Arithmetic
squares in (½log2, ½log3): exist iff λ^{∞,P}_min(T) ≥ v₂ = √2 log 2 (PROVED); the value OPEN (NUMERICAL).
Monotonicity of n₋(A_ev(T)) PROVED; «birth window» not proved. Two-sector reduction with η ↓ 0: «smaller
than (L2)» REFUTED (same order).

**32. REVIEW_002.md** — Review of ROUND_001_A–D (B–D outside the block). A: Theorem 1(a)–(c) PROVED, ℛ_M ARGUED
(crude bound O(M^{−7/3+ε})); robustness against falsifiers ARGUED; new necessary condition: (★) ⇒ 𝒜(w) =
a_{T′}(F₀∗W) ≥ 0 with B(F₀∗W) = −iF̂₀′(i/2) ≠ 0. B: Thm 1.1 (half-line identity) PROVED without the citation (σ₂ ∈ (−½,0));
Prop 1.3 note on P > N REFUTED; §1.6(i) indefiniteness ARGUED; Lemma 1.6 (cell positivity monotone under
w ≤ Λ) = cor:ext-cfals(i); Prop 2.3 (forced scalar coupling of φ₀) ARGUED. C: (L2′) PROVED; block of 11
modes NUMERICAL; block dimension monotone in the comb (blind under Λ). D: Prop 2 «never determinate» REFUTED;
NO-GO PROVED (given the CITED falsifiers): **criteria using only the moments of μ (germ of B at 0) are
blind to the comb**. Table of NO-GOs with corrected classes (§5).

**33. REVIEW_003.md** — Review of 002_D, 002_E, 002_A, 002_B, 003_B. CONFIRMED: Θ_T = max_c Φ_T and J_T an interval
(Toeplitz–Hausdorff), Lemmas 1–3 and Cor 4 of 002_E (ℓ¹ Lipschitz in w), Theorem F (layered Schur floor), Props S,
L, M; 003_B Props 1, 5, Lemma 2, Theorems 3–4. Downgrades: «Π(F*) = 0 iff c* = 1» CONDITIONAL; «rigorous» Galerkin →
NUMERICAL (requires strong duality in V_ℂ and primal witness); 002_B Thm 3.1(b) CONDITIONAL. NO-GO: Schur floor
NUMERICAL; exterior sector monotone in the comb ARGUED and asymptotic; Schur prescriptions 𝔸_M = 𝕏∘𝕂_t + ℝ with diagonal
remainder (Thm 3) and Div/Near (Thm 4, «some M») PROVED; the whole class is not NO-GO (it contains 𝕏 = 0).

**34. REVIEW_004.md** — Review of 005_C, 005_A, 005_E, 006_A. CONFIRMED: exact sign budget in P_T
(σ_T = C₀ + 4 + Σ_{j≥1}2e^{−(4j+1)T}/(2j+½)), with correction: σ_T < 0 only for T > 0.0520; Thm 2 of 005_C (exact archimedean
coupling after one comb step with Tate responses); Thm 1 of 006_A (π_± attained by modulated packets
in P_T); π_+(P_T) ≥ e^T(1+o(1)) (PNT, CITED); Weyl bounds. REFUTED: identity C_q² as a complete convolution
(it is truncated for N ≥ e^{2T}); «family A attains λ_A»; «λ_max(Π_T)/A_T → 0». NO-GOs recorded: Schur floor
on responses (NUMERICAL); mechanisms by identities on E_T (logic PROVED, numerical falsifier);
Π-Krylov from the Λ-free archimedean cone (NUMERICAL/ARGUED); lower counts by pointwise comparison (PROVED,
trivial); Weyl caps from a_T ≥ Arch_T − θ (PROVED given PNT).

**35. REVIEW_005.md** — Review of 005_D, 006_B, 006_C, 007_B, 007_C, 007_D, 008_D. CONFIRMED: jump form
h_T, Theorem 3.1 (W(z) parity Schur), Prop 4.2 (a_T(F,χ_+) = ⟨F, χ_+ω_+⟩); Thm A, Lemma B.0, Thm B (large values);
**certified witnesses: λ_A(½log5+10⁻⁴; a₃) ≤ −0.50528, λ_A(½log5+10⁻⁴; w_{3.2}) ≤ −0.23448, λ_A(1; 1.1Λ) ≤ −0.078244** and
every larger window by extension by zero; λ_W^{par} ≤ λ_A^{par} ≤ λ_{W,2}^{par}; Neumann expansion (conditional on
(H₋), OPEN). REFUTED: W_ev(0) = −½ exact (it is a near-degeneracy that follows λ^W_{T,par}); Danskin clause of 006_B;
μ₀ < 0 by prop:archneg; «K ≈ 7» (K = 1 suffices). Simplicity of λ_A OPEN. NO-GO: 𝒦_gap (ARGUED), families of
v-homogeneous words (PROVED mechanism + NUMERICAL), moment/large values (ARGUED), budget by minimizer (PROVED
countable), subpart of the response cubic (ARGUED), fitted laws (NUMERICAL), Neumann truncation (ARGUED).

**36. REVIEW_006.md** — Review of 008_E and 008_C. CONFIRMED: Theorem 3.1 of 008_E (exterior upper bound given
thm:ext-half), Cor 3.2, index count (four restrictions in dim ≥ 5 for λ_A, two in dim ≥ 3 for λ_W), Lemma 4.3;
008_C: Hadamard variation in T (under (R_E)), Prop 4 (discrete Grönwall: statement correct, proof replaced).
Downgrades: Prop 5.1 of 008_E for c < 1 NUMERICAL; Prop 3 of 008_C CONDITIONAL (boundedness of the minimizer near ±T);
(EB_C) is not (★) + Lipschitz. NO-GO: margin law with PEψ₀ (NUMERICAL); robustness under cΛ fails at first order for
c > 1 (PROVED); index improvement by restricted filtration stops at 6 (ARGUED); Grönwall in T (reformulation, class
𝒦_H; (EB_C) with C = 8πe^{2T} OPEN and stronger than (★)).

**37. REVIEW_007.md** — Review of 009_A (mollified prolate filtration bound). CONFIRMED (PROVED given
thm:ext-half, with constant K not computed): **λ_A(T) ≤ 4KC₅N⁹(1 − χ₈(2πN)), λ_W(T) ≤ 4KC₃N⁹(1 − χ₄(2πN))** for
N ≥ 1.6·10⁶ (C₅ = 1.3·10¹⁶, C₃ = 8·10¹⁵) and with a non-explicit constant for 3 ≤ N ≤ 1.6·10⁶. Prolate lemmas with all
constants. Downgrades: Lemma 2.3 requires c ≥ 12; N ≥ 410; «doubly exponential» reading only CITED in rate,
explicit constants OPEN. It is an upper bound: no sign.

**38. REVIEW_008.md** — Review of 009_B (Fourier class selection rule). CONFIRMED/PROVED: Poisson identity in a
window (1.0); Thm 1.1 P_{−ε}Π_TEf = ½RΠ_TEh (even compact C¹ data; ARGUED for raw prolates);
Thm 1.2 diagonal Fourier defect 2(1 − εε_k√χ_k); Lemma 1.3; Lemma 2.1; Prop 2.2; parity correction:
a_T(w_+, w_−) ≡ 0 and a_T(P_+Ef_+) = 𝒲[Ψ_{f_+}] − a_T(w_+). Downgrades: bound (2.1) CONDITIONAL with κ(K) → 0 expected; §1.7
ARGUED. NO-GO: the Poisson–ℱ class rule is Λ-free, it is not a sign step (PROVED); for a_P the exact
intertwining fails (PROVED); «no rule holds» ARGUED. (HR) OPEN.

**39. REVIEW_009.md** — Review of 010_A, 011_A, 011_C, 012_A, 012_B, 013_A. CONFIRMED: cos² certificate
(Thm 2.2 of 012_A, first failed cell [2.660; 2.661]); Prop 3.3 of 010_A (NO-GO 𝒦_S). REFUTED: open range of
(HR)(a) «2T ≲ log τ < log Ω_B» (it is 2T ≲ log τ < Σ₀ + O(1)); reading Ω_* ≍ e^{λ+O(1)} (it is e^{𝒜_T+λ+O(1)}). Thm 3.1 of 011_A
superseded by the trivial bound P ≤ Σ₀. Identity (2.2) of 013_A = explicit formula (CITED, P47 thm:Z); its remainder R_w lives
outside the sandbox. NO-GO record (10 items, §8): 𝒦_S PROVED; lem:ext-hf empty at polynomial index PROVED;
large values + Kovrijkine collapses to a pointwise bound; moment class ARGUED; trivial bound with fixed profile PROVED;
short packets with crossings in absolute value ARGUED; mean value + Sobolev/Gallagher (closed quadratic family);
three-block Schur LM/H± NUMERICAL; smallness of the H₊–H₋ coupling by class rule PROVED; class 𝒱
(Vaughan/process B) ARGUED.

**40. REVIEW_010.md** — Review of rounds 014_A–024_A (18 memos). Definitional point: 𝒲 must include the polar
term 2A(Ψ)B(Ψ) (14A/15A without it are false in general); ℓ_g of the rounds = ½ℓ of P47. CONFIRMED: certificates
17C Thm 3.1 (μ₀ ∈ [0.06961173221 ± 4.38·10⁻¹²]) and 18A Thm 3.4 (T = 0.8) reproduced; 19B Thm 2.1 (𝒜𝒫 − c𝒞 unbounded
below for c ≠ 1) PROVED; 19A Prop 1.1 PROVED; 20A Thm 1.3; 21A, 22A, 23A, 24A identities. REFUTED: written proof
of «ℕ the unique additively closed ℕ^{1+t}» (statement true, proof corrected); constant 5.72 of 16A.
NO-GO record (16 items, §19). «No step of rounds 14–24 is a sign step.»

**41. ROUND_001_A.md** — Near-coincidence form Q_M(s) = sᵀ𝔸_Ms in the smooth family s_w = m^{−1/2}w(m/M).
PROVED: Lemma 1 (P_{s_w} = ζ(½−iτ) + M^{½+iτ}w̃(½+iτ) + R_M); Theorem 1 (a)–(c): Q_M = M𝒜(w) + 𝒳_M + 𝒵_N + ℛ_M with
𝒜(w) = a_{T′}(F₀∗W) (vector with B ≠ 0, outside P_{T′}), 𝒳_M = O(M^{−K}) (superpolynomially small boundary
term), 𝒵_N = O(N^{−5/2+ε}); ℛ_M = O(M^{−3+ε}) ARGUED. Result: NO-GO, class «lattice→continuum transfer by
Poisson/AFE in the smooth-cutoff family» (renamed by review 32 to «family m^{−1/2}w(m/M), leading order
in M»); robustness of falsifiers ARGUED. Proposed next step: regularity test (profile with |F̂₀|² ≍ |τ|^{−8})
and look for the sign in non-smooth (arithmetic) vectors.

---

## A. Deduplicated «do not relaunch» (with reopening condition) and cross-check with RULES_AVOID.md

Mark: **[ABSENT]** not in RULES_AVOID; **[PARTIAL]** present with another scope or wording; **[OK]** present.

A1. **Promoting generic hypotheses on the potential (V even, V‴ > 0, superlinear, all pairs PD, M concave) to
3×3 or higher positivity.** Explicit falsifier (18). Reopening: «additional specific property of Φ or a
concrete estimate of its crossing» (18 §7). **[ABSENT]** RULES_AVOID B4 mentions cosh products and «positive model»,
not this class falsifier.

A2. **Inferring positivity of matrices from pairs (2×2) or from independent edges.** −0.6 matrix (30 §3); cycle
(p,p,p²) with negative cubic term (30 §4). Reopening: control of the collective norm of the near-contact matrix
against the archimedean energy. **[ABSENT]**

A3. **«Activating a nearby contact improves (or worsens) the form in Loewner order».** False in dimension 2 (30 §2).
**[ABSENT]**

A4. **Positive cosh representation or log-convexity as control of two generators.** 3+cosh u (28; CONE_001 §4).
**[PARTIAL]** RULES_AVOID B4: «exact representation by products of cosh (§§11, 13; does not decide whether multiplying by cosh
preserves positivity)»; does not cite this two-point counterexample.

A5. **Sufficient criterion «Erlang prefixes T_m ≥ 0 for all m» (or up to finitely many exceptions).** Refuted (27).
Reopening: signed bound of the adverse contributions against the real gamma weights, or a new arithmetic grouping.
**[ABSENT]**

A6. **Premise «the weighted primitive I_*(X) ≥ 0 for all X».** False at X = 225/64 (26). Reopening: pairing
inequality that uses the gamma factor and controls all contacts. **[ABSENT]** (D18 «discrete summation by parts»
and «compensated layer primitives» have another object).

A7. **Passing from a union of positive families (increasing threshold 2^{40n}, cone 060, any rate) to density or to the
linear span.** Not dense (15 §8; 23). Reopening: lower the threshold to a common family of exponents, or explicit
control of the crossings between translated packets; 23 does not cover other initial continuous families. **[PARTIAL]**
RULES_AVOID D3: «Inferring density or sign from a positive union… Reopens with liminf r(n)²/n = 0, a block that
repairs the moment and control of its crossings»; missing: that **varying the rate does not repair density** (096) and the
explicit obstruction of 15 §8.

A8. **Criteria using only the moments of the representing measure of B (germ of B at 0).** Blind to the comb
(32, NO-GO PROVED given the cited falsifiers). **[OK]** C1 «Carleman germ criteria».

A9. **Lattice→continuum transfer by Poisson/AFE in the smooth family s_w = m^{−1/2}w(m/M), leading order in
M.** (41, class corrected in 32). Implicit reopening: non-smooth (arithmetic) vectors. **[OK]** D8 «smooth family
s_w».

A10. **Cell positivity (key cancellation of cor:ext-cfals) as the whole sign step.** Monotone under w ≤ Λ (32,
Lemma 1.6). Not excluded as an ingredient. **[ABSENT]** as such (B5 «sparse-stable properties» is related).

A11. **Dimension of the Nyquist block (or sample count) as sign carrier.** Monotone in the comb, blind under
Λ (32 C). **[ABSENT]**

A12. **Floor-only Schur inequalities (scalar c): λ_min(A_EE) − ‖B‖²/c ≥ 0**, on the block or its responses.
NUMERICAL (33, 34). **[OK]** D17 «Schur floor class».

A13. **Schur factorization prescriptions 𝔸_M = 𝕏∘𝕂_t + ℝ with diagonal remainder or with Div/Near.** NO-GO PROVED (33,
003_B Thms 3–4); the complete class is not closed (it contains 𝕏 = 0). **[ABSENT]**

A14. **Sign mechanisms by identities valid for every Beurling system and for a_P on E_T** (Λ∗1 = log,
Selberg, local Euler factors, Lévy identity). (34). **[OK]** B1.

A15. **Krylov families / v-homogeneous words of (M, Π) from a Λ-free seed below the capture dimension.**
(34, 35). **[OK]** D17.

A16. **Lower counts by archimedean pointwise comparison; Weyl caps from a_T ≥ Arch_T − θ.** (34). **[OK]**
D17 «Weyl bounds from Arch − θ».

A17. **Lower bounds on the gap of the jump form h_T with comb-independent loss (𝒦_gap)**, in
windows with λ_A^{ev}/|μ₀| below the loss (35, ARGUED). **[ABSENT]**

A18. **Budget-by-minimizer statements / crossing window T_×** (35, countable PROVED). **[ABSENT]**

A19. **Signing a proper subpart of the response cubic with error larger than λ_A** (35, ARGUED). **[ABSENT]**

A20. **Fitted laws as sign carriers** (35, NUMERICAL). **[ABSENT]** (B8 «law on a bounded range of
windows» is related but not identical.)

A21. **Finite-degree Neumann truncation of the Schur coupling on E_T with tail bounded by ρ(X)** (35;
conditional on (H₋), OPEN). **[ABSENT]**

A22. **Grönwall in the window variable (D ≤ Cλ_A, (EB_C), (VE_C)).** Reformulation, class 𝒦_H; (EB_C) with
C = 8πe^{2T} OPEN and stronger than (★); weaker structured version «ARGUED absent» (36). **[ABSENT]**

A23. **Upper margin law with the single test function PEψ₀; robustness of the law under cΛ** (fails at first order for
c > 1, PROVED) (36). **[ABSENT]**

A24. **Improvement of the lower index by restricted filtration (Lemma 4.3 route)**: stops at index 6 (36, ARGUED;
conditional on polynomial conditioning κ_C(T), OPEN). **[ABSENT]**

A25. **Smallness of the coupling between classes H₊–H₋ derived from the selection rule ℱ** (PROVED NO-GO, 39); Poisson–ℱ
class rule as a sign step (Λ-free, 38). **[PARTIAL]** D17 «Poisson/ℱ rule» without the coupling part.

A26. **Mass-only estimates of the comb at high frequency (𝒦_S)** (PROVED, 39); **lem:ext-hf with polynomial
index data** (empty unless K ≥ c′N^{−1/2}e^{(K_T+λ+1)/4}, PROVED). **[ABSENT]**

A27. **Large-value measure + Logvinenko–Sereda/Kovrijkine** (collapses to a pointwise bound); **moment class with
integer spacing error** (irrelevant: the trivial bound P ≤ Σ₀ already clears those heights) (39). **[ABSENT]**

A28. **Trivial bound with fixed profile** (PROVED: T_β finite for all β, 39); **short packets with crossings in absolute
value** (ARGUED); **mean value + Sobolev/Gallagher** (closed quadratic family). **[PARTIAL]** B2 covers the
quadratic family; the first two absent.

A29. **Three-block Schur assembly LM/H₊/H₋ with block-diagonal ℓ_g normalization** (NUMERICAL, 39).
**[PARTIAL]** D17 «two- and three-block assemblies» (without the normalization).

A30. **Class 𝒱 (Vaughan/Heath-Brown + Poisson/process B on the packet polynomial)**: ARGUED; the complete dual
returns the explicit formula, whose remainder lives outside the sandbox (39). **[OK]** D17 «process B / Vaughan».

A31. **Symbol on the index axis + band/Toeplitz error in D units** (NUMERICAL, 40; does not cover sweeps
normalized by ℓ_g). **[ABSENT]**

A32. **Idealized R-cell class with transported restrictions, κ uniform in R** (NUMERICAL); **step
piece of the Schur inequality with collapsed weight c·log N** (NUMERICAL) (40). **[ABSENT]**

A33. **Qualitative band restriction on R-cell data** (PROVED, 40); **absolute band-defect bounds**
(NUMERICAL). **[ABSENT]**

A34. **Robust bounds in the comb 𝒜𝒫 − c𝒞 ≥ 0 over the whole class of admissible tails, c ≠ 1** (PROVED, 40). **[OK]**
D17.

A35. **Existentially gauge-fixed representative with comb margin** (PROVED, 40); **Λ-free canonical
sections with uniform δ** (PIVOT NUMERICAL). **[ABSENT]**

A36. **Positivity windows in the comb weight on R-cell data** (40). **[ABSENT]**

A37. **R-cell sign as a monoid invariant / additive characterization on the exponent ray** (NUMERICAL,
«addition singles out ℕ» ARGUED closed) (40). **[PARTIAL]** B7 «monoid only».

A38. **Finitely many strict Chebyshev floor relations** (NO-GO CONDITIONAL on the numerical width of J_T, 40).
**[ABSENT]**

A39. **Propagation of positivity through the contact entries along N** (PROVED NO-GO for the sign
of the entry term; the rate bound (EB_C) remains) (40). **[ABSENT]**

A40. **Extremality of prolates in the index-8 subspace (Design C)**: retry of L′/L′♯ (40, ARGUED). **[OK]**
C1 «L♯ programme».

A41. **«Long-range band = finite-rank radical correction»** (NUMERICAL falsification, 40) and **D-floor of the
high block** (ARGUED). **[ABSENT]**

A42. **Two-sector reduction with η ↓ 0 as a reduction smaller than (L2)** (REFUTED, 31: same order; requires
sparsity of the non-positive set, OPEN). **[ABSENT]**

Inaccuracies detected in RULES_AVOID relative to this block:
- C5: «total positivity of order ≤ 4 (PF₄ OPEN)». In this block: four generators of K PROVED (085, cited in
  4, 2, 5) and the Wronskian of four densities of Φ with global sign and global Turán T_R > 0 (4); «global PF4»
  transport is still not asserted (2: «Global PF4 transport is not asserted»). The line should distinguish which part of
  order 4 is proved.
- D3 (cited above) does not record the rate-variation obstruction (23) nor that of 15 §8.
- B4 «positive model + transfer»: does not mention that the class of potentials with V‴ > 0 has an explicit 3×3
  counterexample (18), which is precisely the limit of the theta tools used for pairs and triples.
- D17 lists «𝒜𝒫 − c𝒞 with c ≠ 1» and «Poisson/ℱ rule» without their exact scope: the first is «over the whole class of
  admissible tails» (not over a fixed subspace); the second is NO-GO for the sign and for the smallness of the
  coupling between classes, not for the use of identity (1.0), which is PROVED and reusable.

## B. PROVED positive results (exact scope)

B1. HAZARD: V‴(t) > 0 for all t > 0, V = −log Φ (7 + phase 103).
B2. Two copies (14): under V even C³, V‴ > 0 (x > 0), V/|x| → ∞: M″ < 0, 0 < uM′ < M (u > 0); applied to real Φ.
B3. Pairs (14): 2×2 K positive definite for all a ≠ b > 1; W > 0 on every real plane of two exponentials or two
exterior powers (strict energy for a nonzero represented function).
B4. Triples (5 + 16): g″(x) < 0 for all x ≥ 1/4; 3×3 K positive definite for every distinct triple a_i > 1; general
criterion: under BASE, 3×3 blocks PSD ⇔ g concave on squares (implication and converse).
B5. Real Schur remainder (10): T_u(z) > 0 and G_u(z) > 0 for all u, z > 0; F_u has a unique simple positive zero.
Corollary: anchored matrix {0,u,v} positive definite (node 0 outside the admissible class).
B6. Positive density Φ_u > 0 on ℝ, H_u(z) = D_u(z)/[z(z²−u²)] > 0, log H_u strictly convex (12).
B7. C > 0, L′ < 0, L → 0 for real Φ on all x > 0 (8, 9).
B8. Wronskian of four densities: < 0 at the origin (1), < −4000y⁶/t² in t ≥ 1 (2); with the compact 089: global sign,
det[ρ_j(t_i)] < 0 for all positive nodes and Turán T_R = 2R′R‴ − 3R″² > 0 for all λ > 0 (4).
B9. Three powers with A ≥ 2³¹, h ≤ A/2: Q ≥ 9‖f‖²; every order n with rates in [u,3u], u ≥ 2^{40n}: W ≥ 9‖f‖² (15).
B10. Uniform cone (21): W[F] > ‖F‖² for every real numerator of degree < n and j ≥ 10¹²(n⌈log₂(n+1)⌉)³.
B11. Analytic cutoff (20): K_N(x) > 0 for x ≥ e^{t_*(N)} (t_* = d/330 + O(1)); K_N > 0 in 2 ≤ N ≤ 129, x ≥ e^{2/3};
favourable tail cells.
B12. Real weighted block at u = 63/2 (26): ∫_1^4 G_NH > 3/200 (N ≥ 2²²); recovery ∫_{225/64}^4 G_NH > 9/500 (N ≥ 2²⁴).
B13. Improvement of nearfree with ε = 1/(KM) (30 §1): margin ≥ 1 for K ≥ K₀(χ), all M.
B14. Projection uniform in the rate (23): A_{n,r}(ξ) ≤ 200n/√r for r ≥ 10¹²n³ (a distance result, not a sign result).
B15. Upper bounds (37): λ_A ≤ 4KC₅N⁹(1 − χ₈(2πN)), λ_W ≤ 4KC₃N⁹(1 − χ₄(2πN)) given thm:ext-half (K not computed).
B16. Certified falsifier witnesses (35): λ_A(½log5 + 10⁻⁴; a₃) ≤ −0.50528; λ_A(½log5 + 10⁻⁴; w_{3.2}) ≤
−0.23448; λ_A(1; 1.1Λ) ≤ −0.078244, and every larger window.
B17. Positivity certificates in restricted classes (39, 40): cos² up to the cell [2.660; 2.661] (fixed profile);
17C Thm 3.1 μ₀ ∈ [0.06961173221 ± 4.38·10⁻¹²]; 18A Thm 3.4 at T = 0.8 (class of transported restrictions).
B18. Reusable identities: Poisson in a window (1.0) and P_{−ε}Π_TEf = ½RΠ_TEh (38); diagonal Fourier defect
(38); a_T(w_+, w_−) ≡ 0 by parity (38); half-line identity without the external citation, σ₂ ∈ (−½,0) (32); exact budget
σ_T in P_T (34); a_T(F,χ_+) = ⟨F, χ_+ω_+⟩ (35); Theorem 1 (a)–(c) of 41 (decomposition of Q_M in s_w);
necessary condition (★) ⇒ a_{T′}(F₀∗W) ≥ 0 with B(F₀∗W) ≠ 0 (32); monotonicity of n₋(A_ev(T)) (31); π_+(P_T) ≥ e^T(1+o(1))
(34, PNT CITED); λ_W^{par} ≤ λ_A^{par} ≤ λ_{W,2}^{par} (35).

## C. OPEN obligations (precise statement; what was attempted)

C1. **Four or more generators / all orders of K on the complete ladder a > 1 (or a = 32+n):** prove that
[(L(a_i)+L(a_j))/(a_i+a_j−1)]_{i,j≤m} ⪰ 0 for all m. Attempted: pairs (14), triples by a curvature (16, 5),
four (085, outside the block), increasing thresholds (15, 21); the generic potential tools do not suffice (18).
C2. **Two-node kernel of the regularized remainder G_p** (and concavity of both reciprocal data, their Turán and a
second Schur step) (4, 10, 11). Attempted: pointwise positivity (10), pairs of G_p via 090 (4).
C3. **Step S4 / higher-order transport and global Darboux criterion** (1, 2, 4).
C4. **Interior of the uniform cone:** sign of W[F] for j < J(n) (21); interior cells of the cutoff of K_N (number
≤ ⌈X_N⌉) (20).
C5. **Tail ∫_4^∞ G_N H** and pairing inequality of all contacts against the gamma weight (26, 25);
**signed bound of the adverse contributions against the gamma weights** in Σ_m (v_{N,m} − v_{N,m+1})T_m (27).
C6. **Density of a positive span in form norm:** common family of exponents with fixed threshold or control
of crossings between translated packets (15 §8, 23).
C7. **Collective norm of the near-contact matrix ≤ archimedean energy** (30).
C8. **Φ–Φ_u comparison** that orders Z/H_u (13; partially replaced by 10).
C9. **(H₋) for the Neumann truncation** (35); **simplicity of λ_A(T)** (35); **(R_E)** and boundedness of the minimizer
near ±T (36); **(EB_C)** with C = 8πe^{2T}(1+o(1)) (36); polynomial conditioning κ_C(T) (36); eq:ext-L (36).
C10. **(HR)(a) in packet form** on the finite range Ω_lo ≤ τ ≤ 2π·exp(Σ₀ + κ + O(1)) (39); (HR) in the range k > 4N
(38); (U) of 012_A is only necessary (39).
C11. **Value λ^{∞,P}_min(½log2⁺) ≥ v₂** that decides the arithmetic squares in (½log2, ½log3) (31); **sparsity of the
non-positive Nyquist set** (31); **continuity of the second eigenvalue of A_ev(T)** («birth window») (31).
C12. **ℛ_M = O(M^{−3+ε})** and robustness of the decomposition of 41 against falsifiers (32, ARGUED); regularity test
with |F̂₀|² ≍ |τ|^{−8} (41).
C13. Explicit non-asymptotic constants for 1 − χ_k(c) (37).

## D. Objects or ideas mentioned as not started or not examined

D1. Threads stopped without NO-GO (29): nonlocal kernel of phase 209 (missing operator/identity/sign lemma);
«layer edges κ_{T+log n}» of phase 202 (later declared empty for the defined archimedean residue, 32;
layered comb pairs are not covered); finite-window Carathéodory–Fejér route N (phase 160); Lemma RF.1
(phase 205).
D2. Tools never aimed at the finite objects of P47 (29): Toeplitz/corona symbol, coercivity of adjacent
windows, exact transport defect between successive quotients, Carleman determinacy, finite-to-total
uniformity, truncation bound with PNT only.
D3. Candidates C1–C5 of the README (29): exact identity for ∫|P_s|²F̂₀²m non-generic in the comb; the two-moment
fluctuation as an iterated difference with transfer M → M+1; symbol of the field M ↦ 𝔸_M; the two unfinished threads;
Carleman measure forced by the moments of B (the latter closed by 32).
D4. Regularity test with a smoother profile and search for the sign in non-smooth vectors (41).
D5. Beurling falsifier (c) not run for Prop 4 of 008_D (35); falsifiers (b) with P ≤ e^{2T}, (c), (d)
of 002_D (33).
D6. Addition of other continuous families of initial blocks to the union, sums with uncertified crossings, mixtures of
densities (23, 24).
D7. Extension of the Poisson identity (1.0) to data with a jump at the boundary (raw prolates) (38).
D8. 𝒢 with an independent definition on a common domain across classes (sweep in b = Sa) (39).
D9. Design C (index-8 prolates) not pursued (40).

## E. Coverage

Files in the range (`ls *.md | sort` from `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md` to `ROUND_001_A.md`): 41.
Read completely: 41. No file or stretch left unread. The files cited by these sources and located outside the
range (for example 078, 085, 086, 090, `POWER_THETA_DENSITY_COMPACT_089.md`, `POWER_GAMMA_WEIGHT_031.md`, the memos
ROUND_001_B–D and ROUND_002–024 reviewed in REVIEW_002–010) were not read; what is said about them comes from what
these 41 sources state.
