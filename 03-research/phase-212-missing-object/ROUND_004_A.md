# Round 4, candidate A — The SP-161 / L161.1 target with signed weights and sieve weights (selection memo)

Selection memo, not a construction memo. Target (★): λ_A(T) ≥ 0 for all T, definitions from
`../phase-211-sign-sandbox/STATEMENT_001.md`. Notation from `../phase-161-row-d-sum-product-square/R161_001`
(S_N, K_N, L_M, A_M = 𝓜 − L_M − L_M*, E_N, H_{M,N}) and from `ROUND_003_6.md` (M_N, U_N, c_N(k), f_0, f_1,
g, R_0, R_1). For a finite Dirichlet polynomial P(s) = Σ p_n n^{−s} I write P(∂) = Σ p_n n^{−1/2}τ_{log n};
the translations form a commutative algebra indexed by ℚ_{>0} (τ_{log r}, r = a/b), and "coefficient at r"
refers to that algebra. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## Cross-check

Searches done (case-insensitive grep, followed by primary reading of what was found):
"Selberg sieve / criba de Selberg / Barban / Vehov / GPY / Λ_R / mollif / Levinson / signed weights /
pesos con signo / truncated Möbius / Möbius truncado / M_N S_N / discrete derivative" across all of
`03-research/`, P47, P48, the index, the grid and the crossword; "Möbius / M_N / truncat" in phases 106,
121, 122, 124 and in R162_405–408, R162_206, R162_401.

Read as primary sources: R161_000–004 in full; `ROUND_003_6.md` in full; R170_853 §0, R170_878 §0 (with its
truncation corrections), R170_879–883 §0, R170_896 §§0–1; phase 200: `Q2_LADDER_001.md` §§0–2,
`SPEC_SIGN_OBJECT_002.md` §B (Q1), `AUDIT_200_SPEC_002.md` §§3–5; index README, entries
PROOF_L_SHARP_GG_001, AUDIT_200_SPEC_002, Q2 ladder, PI_MU_001, MULT_GAUGE_001; R162_1003 §§4–5;
`P121_CAUSAL_MOBIUS_OBSERVABILITY.md` §§1–2; phase 167 (R167_102 Thm. B, R167_103 §§2, 4.1, R167_190);
index 04 rows G3D-159, G3E-159, G1C-R162_1003, P58-1; index 05 L62.

Not opened as primary sources (title or grep line only): the 15 files of phase 106 that name Möbius
(among them 106_40, 106_117, 106_144), `P121_CMO_SOURCE_MATRIX_NO_GO.md` (known to me through R161_004 §3),
R162_405 §4.3 ("Möbius-conjugated tests"), R162_406 Prop. at l. 131, `phase-104/104_87`, phase 33
(82, 83). In 122, 124, R162_206, R162_401 there were no matches. A search without matches does not
prove novelty.

### (1) Closest antecedents

1. **R161_002 §§4–5 and §8** (target L161.1 and Thm. 8.1): no weighting w_N ≥ 0 cancels the hyperbola
   tail; Cor. 8.2 locates the sign in the terminal discrete derivative −log p. The signed branch is not
   written in the phase (confirmed: `RULES_AVOID.md` K5, K7).
2. **`ROUND_003_6.md` (4.2)–(4.5) and R170_878 (0.2)–(0.4)**: the Möbius test, complete in R170_878
   ((PS_N*P)^{−1} = PM*P) and truncated in 003_6; R3-e closes the separate exterior blocks with a test
   independent of the weight.
3. **Phase 200, Q1–Q3 and the Q2 ladder** (`SPEC_SIGN_OBJECT_002` §B, `AUDIT_200_SPEC_002` §5,
   `Q2_LADDER_001`): Selberg form of the quotient lattice with Selberg variance as the positive part
   (Q1: tautology, y^T𝔅y = 𝒲[g]); ladder of truncated mollifiers c^{(Y)}_N (Q2: radical difference,
   𝒲 = 0); correlations of c_N "of Selberg Λ_R type" (Q3: do not depend on the comb, do not see cΛ). Lemma SQ.0:
   every mollified exterior at any level is −g modulo the radical.
4. **MULT_GAUGE_001 (class R-MOM, PROVED)**: every |1 + ζH|², mollifier of any length, gives W_T
   exactly. **PROOF_L_SHARP_GG_001**: "factorization of the mollifier defect as a sign source", do not
   retry.
5. **R162_1003 §4**: the first-contact problem is an extremal problem of Selberg type (Prop. 4.1);
   the Weil kernel is not of gcd type (Prop. 4.2); every Selberg representation Z*DZ with Z unipotent is
   a congruence (Cor. 4.3).
6. **Phase 167, Thm. B** (blindness of sieves: b_θ satisfies every sieve upper bound that Λ satisfies) and
   P121 (unitriangular Möbius elimination on the divisor poset).

Conclusion of the cross-check: question (iii) —Selberg or Barban–Vehov sieve weights as a test or as a
mollifier— is covered by antecedents 3–5 in the radical and line formulations. What is
not written is the version of L161.1 with signed weights in N and the exact comparison between L161.1 and the
Möbius identity of 003_6. That is what this memo writes (§§(4)–(5)); they are format lemmas, without sign.

### (2) Genuinely new object

There is no object (ℋ_T, V_T, ρ_T). Three short lemmas are written, all of declared class and without sign:

- **Lemma 1** (telescoping with signed scalar weights in N): the only finite real weight that makes
  the interior terms of Σ_N w_N S_N*S_N telescope exactly is w = δ_{N=1}, and the
  resulting identity is a_T = a_T with zero boundary. It closes the signed branch of L161.1 in the algebraic class of
  R161_002 Thm. 8.1.
- **Proposition 2** (answer to (i)): identity (4.2) of 003_6 is not an instance of L161.1 for any
  signed weight; its weights live on the dilation index n (μ(n)), not on N.
- **Lemma 3** (answer to (iii)): the identity M^λS_N = I + (exterior) is exact if and only if λ = μ on
  [1, N]; Selberg/Barban–Vehov weights break it with an explicit interior block, and the
  quadratic variant |M^λD_N|² does not produce a square but the form A_M on vectors outside P_T.

### (3) Does it avoid the antecedent's difficulty?

No. The three lemmas confirm the recorded difficulty: Möbius or sieve weights fixed without using the
weight leave the whole identity affine in Λ (R3-e), and the part "quadratic in λ" pairs with A_M, whose sign is
the target (R162_1003 Cor. 4.3; phase 200 Q1). None of the choices introduces dependence of degree ≥ 2
on the weight.

### (4) Identities connecting to the complete form

Conventions: F smooth with support in I_T, T > ½ log 2, M ≥ N ≥ e^{2T}. From R161_001 §1 (CITED from that memo):
𝓕 is a unitary involution, 𝓕τ_a𝓕 = τ_{−a}, and 𝓕 commutes with even multipliers; since m is even and
P_M = L_M + L_M* is even, 𝓕A_M𝓕 = A_M. Hence, for the oriented form of R161_002 (OR),

    B_{M,N}(F) = ⟨A_M𝓕F, S_N*S_N𝓕F⟩ = ⟨A_MF, S_N*S_NF⟩,                                 (4.1)

and a_T(F) = ⟨A_MF, F⟩ (003_6 Step 1).

**Coefficients of S_N*S_N (PROVED).** S_N*S_N = Σ_{m,n≤N}(mn)^{−1/2}τ_{log m − log n}. For r = a/b with
gcd(a,b) = 1 and q = max(a,b), the pairs (m,n) = (ja, jb), j ≤ N/q, give the coefficient
(ab)^{−1/2}Σ_{j ≤ N/q} 1/j. For real weights w_N of finite support and Ω(m) := Σ_{N≥m} w_N,

    [r](Σ_N w_N S_N*S_N) = (ab)^{−1/2} G(q),   G(q) := Σ_{j≥1} Ω(jq)/j.                     (4.2)

**Lemma 1 (signed scalar telescoping; PROVED).** Class 𝒞_w: real weights w_N of finite support, test
S_N𝓕F, and the requirement of L161.1 that, in the translation algebra, Σ_N w_N S_N*S_N = I + (terms at r
with |log r| ≥ 2T). Then w = δ_{N=1}, Σ_N w_N B_{M,N} = B_{M,1} = a_T, the boundary remainder is 0 and the
hyperbola tail is H_{M,1} = L_M in full.

*Proof.* For q ≥ 2 the pair (q, q − 1) is coprime and |log(q/(q−1))| ≤ log 2 < 2T; by (4.2), G(q) = 0
for all q ≥ 2, and G(1) = 1 by the coefficient at r = 1. Inversion over multiples
Ω(m) = Σ_j μ(j)G(jm)/j (check: Σ_j μ(j)j^{−1}Σ_i Ω(ijm)/i = Σ_l Ω(lm)l^{−1}Σ_{j|l}μ(j) = Ω(m); the
sums are finite) gives Ω(1) = 1 and Ω(m) = 0 for m ≥ 2, hence w_1 = 1 and w_N = 0 for N ≥ 2. With S_1 = I,
(4.1) gives B_{M,1} = a_T; K_1 = 0 and H_{M,1} = L_MS_1 − K_1 = L_M. ∎

Reading. The requirement of L161.1 ("the interior terms telescope") already fixes the weights without seeing Λ:
signed or not, the only solution is the trivial one. Moreover, Thm. 8.1 of R161_002 in signed form asks for
something incompatible: with support of w in N ≤ N_1 and a prime p > N_1, the coefficient of Σ w_N H_{M,N} at p is
log p · Σ_N w_N, so cancelling the tail at large primes requires Σ_N w_N = 0, while Lemma 1
requires Σ_N w_N = Ω(1) = 1. **Corollary (PROVED):** in 𝒞_w there is no weight that telescopes the interior and cancels
the tail at the same time. The pure discrete derivative w = δ_{N+1} − δ_N (sum 0) gives S_{N+1} − S_N =
(N+1)^{−1/2}τ_{log(N+1)} and H_{M,N+1} − H_{M,N} = (N+1)^{−1/2}(L_M − log(N+1))τ_{log(N+1)}: it is the
single-translation PC identity, whose coefficient at r = 1 in (4.2) is G(1) = Ω(1) = 0, so a_T does not appear
(PROVED, direct computation). Not excluded: tests other than S_N𝓕F, F-dependent weights, telescoping
only after compression to the window (there 𝓜 is not local and the coefficients with |log r| ≥ 2T do not
vanish), and the use of the leakage squares of C_T, which no weight of this class produces.

**Proposition 2 (answer to (i); PROVED, with Bertrand CITED).** For N ≥ 2, the real multiplier of
(4.2) of 003_6, I + ½(U_N + U_N*), does not belong to span_ℝ{S_{N′}*S_{N′} : N′ ≥ 1}. Hence the identity
a_T = f_0 − f_1 − R_0 + R_1 is not an instance of L161.1 for any signed weight w_N.

*Proof.* If Σ w_{N′}S_{N′}*S_{N′} = I + ½(U_N + U_N*), the coefficients at r = a/b with a, b ≥ 2
are 0 on the right (U_N only has coefficients at integers k ∈ (N, N²]); by (4.2), G(q) = 0 for all
q ≥ 3 (pair (q, q − 1)), and the coefficient at r = 2 is 0 on the right (2 ≤ N), hence G(2) = 0. Then the
left side has coefficient 0 at every integer k ≥ 2, and one would need c_N(k) = 0 for all k ∈ (N, N²]. Let p be
prime with N/2 < p ≤ N (Bertrand) and k = 2p ∈ (N, N²]: the divisors d of k with d ≤ N and k/d ≤ N are d = 2
and d = p (if p ≠ 2), hence c_N(2p) = −2; for N = 2, k = 4 and c_2(4) = μ(2) = −1. Contradiction. ∎

Exact correspondence. L161.1 weights, on the cutoff index N, a family of self-adjoint Grams
S_N*S_N (symbol |D_N(½+iτ)|²). The identity of 003_6 uses a single N and weights on the dilation index
n with μ(n): its test M_N*F is causal (one-sided), and its real symbol Re[M_N D_N] = 1 + Re U_N lies outside the
cone and the span of {|D_{N′}|²}. What both share is the PC algebra; what 003_6 has and L161.1 lacks
is that the coefficient 1 is isolated exactly (M_NS_N = I + exterior); what L161.1 asks for and 003_6 lacks
is the boundary term with C_T. No leakage square appears in (4.2)–(4.3) of 003_6.

**Lemma 3 (exactness forces Möbius; sieve weights; PROVED).** Let λ be real with λ_1 = 1, support in d ≤ R,
M^λ = Σ_{d≤R} λ_d d^{−1/2}τ_{log d} and θ^λ_N(k) = Σ_{d|k, d≤R, k/d≤N} λ_d. Then
M^λS_N = I + Σ_{k>N} θ^λ_N(k)k^{−1/2}τ_{log k} (no coefficients at 1 < k ≤ N) if and only if, extending
λ_d := 0 for d > R, one has λ_d = μ(d) for all d ≤ N. (If R < N this requires μ(k) = 0 on (R, N], which
happens only in degenerate cases such as R = 3, N = 4; if R ≥ N, the λ_d with d > N remain free and only touch
k > N.)

*Proof.* For k ≤ N the condition k/d ≤ N is automatic, and θ(k) = Σ_{d|k}λ_d with λ extended by 0.
Vanishing for 1 < k ≤ N, together with λ_1 = 1, determines by induction λ_k = −Σ_{d|k, d<k}λ_d = μ(k) for
k ≤ N; conversely λ = μ on [1, N] gives Σ_{d|k}μ(d) = 0. ∎

Consequence for the Selberg/Barban–Vehov weights λ_d = μ(d)P(log(R/d)/log R) (P(0) = 0, P(1) = 1): for
a prime p ≤ min(R, N), θ(p) = 1 − P(log(R/p)/log R) ≠ 0 in general, and the identity ceases to be "I plus
exterior". It remains exact as algebra, with an additional interior block:

    Re⟨M^λS_NA_MF, F⟩ = a_T(F) + I^λ(F) + R^λ(F),
    I^λ(F) = Σ_{1<k≤N} θ^λ(k)k^{−1/2} Re⟨A_Mτ_{−log k}F, F⟩,
    R^λ(F) = Σ_{k>N} θ^λ(k)k^{−1/2} Re⟨A_Mτ_{−log k}F, F⟩.                                (4.3)

I^λ is a near-coincidence form inside the window with coefficients θ^λ small on average, without
sign; R^λ is the exterior remainder of 003_6 with c_N replaced by θ^λ.

**The "Selberg square" (answer to (iii); PROVED as an identity).** The only way the square
(Σ_{d|k}λ_d)² enters is with the test M^λS_NF on both sides. With V := M^λS_N − I, for smooth F ∈ P_T,

    ⟨A_M M^λS_NF, M^λS_NF⟩ = a_T(F) + 2 Re⟨A_M VF, F⟩ + ⟨A_M VF, VF⟩,                    (4.4)

whose symbol on the line is s_M(τ)|M^λ(½+iτ)D_N(½+iτ)|² with Dirichlet coefficients θ^λ_N(k). That is:
form = Q^λ(F) − 2Re⟨A_MVF,F⟩ − ⟨A_MVF,VF⟩ with Q^λ the left-hand side of (4.4). Q^λ is not a square: it is the
form A_M evaluated at M^λS_NF, which is not in P_T (support in [−T, T + log(NR)]); A_M on the line is
indefinite (R161_002 §2: negative semilocal background). The remainder 2Re⟨A_MVF,F⟩ + ⟨A_MVF,VF⟩ is affine in Λ
(A_M is) and quadratic in λ. Selberg positivity Σ_k θ(k)²w(k) ≥ 0 uses a measure w ≥ 0 on
the integers; here the place of w is taken by s_M, which is the target. This is exactly the situation of R162_1003
Cor. 4.3 (congruence) and of phase 200 Q1 (tautology). Choosing λ to minimize the quadratic part is the
extremal problem of R162_1003 Prop. 4.1: it installs the answer.

**Answer to (iv): degree in the weight (PROVED).** With λ fixed without using the weight (μ, Selberg, Barban–Vehov,
GPY, Λ_R: all are built with μ and log on the integers, not with the weight), M^λ, S_N, V, E_N, 𝓕 do not
depend on the weight and A_M^{(c)} = 𝓜 − c(L_M + L_M*). Hence (4.3) and (4.4) are affine in c, with I^λ, R^λ and the
remainder of (4.4) of the form (independent block) − c·(prime block). The test is independent of the
weight, so Corollary 2 of 003_6 (R3-e) applies literally to I^λ_1 and R^λ_1: every sign
statement about them separately holds for all c > 0 or for none. The part quadratic in λ does not raise the
degree in the weight: it stays 1. Sieve weights introduce no dependence of degree ≥ 2 on the weight.

Remark (ARGUED). The only way for λ to depend nonlinearly on the weight is to use the "Möbius of the
system": for the weight a, μ_a = coefficients of 1/ζ_a with −ζ_a′/ζ_a = Σ a(n)n^{−s}; for cΛ, ζ_{cΛ} = ζ^c and
μ_{cΛ} are the coefficients of ζ^{−c}, not polynomial in c. But then the analogue of M_NS_N = I + exterior
requires S^{(c)} with coefficients of ζ^c, and L^{(c)}S^{(c)} = K^{(c)} holds for all c: interior vanishing
becomes an identity valid for the whole family (pattern B1), and E_N^{(c)} = S^{(c)}𝓕 − JS^{(c)} loses
the Poisson structure for c ≠ 1. Not written; not excluded.

### (5) cΛ and a_P: why the remainder stops being ≥ 0

There is no signed remainder ρ: none of (4.1)–(4.4) separates a manifestly nonnegative part. The only
thing that can be said precisely is which line changes:

- **cΛ, c ≠ 1.** Lemma 1: the weights do not depend on Λ, the trivial identity a_T = a_T breaks only in the
  trivial sense. (4.3)–(4.4): all blocks that see primes are multiplied by c; a sign of a separate block
  survives every c > 0 (R3-e), hence cannot be the sign step.
- **a_P, P > N.** Lemma 3 and Prop. 2 do not depend on the weight; in (4.3) I^λ_1 and R^λ_1 change (they lose the
  terms with d < P and are not proportional to those of Λ). Since none of them has a written sign, there is no
  "remainder that stops being ≥ 0" to point to.

## Result

No new mechanism. Essentially a repetition for (iii) (phase 200 Q1–Q3 and the Q2 ladder, MULT_GAUGE R-MOM,
GG_001, R162_1003 §4). Three PROVED format lemmas are added, without sign, which close the signed branch of
L161.1 in its algebraic class and answer (i) negatively.

## What was proved

1. Lemma 1 (PROVED): in the class 𝒞_w (finite real scalar weights in N, test S_N𝓕F, exact telescoping
   of interior coefficients), the only weight is δ_{N=1} and the identity is a_T = a_T. Corollary (PROVED):
   telescoping the interior (Σw = 1) and cancelling the hyperbola tail at large primes (Σw = 0) are
   incompatible. The discrete derivative in N is the single-translation PC and does not contain a_T.
2. Proposition 2 (PROVED, Bertrand CITED): the truncated Möbius identity of 003_6 is not an instance of
   L161.1 for any signed weight; c_N(2p) = −2 is the witness.
3. Lemma 3 (PROVED): M^λS_N = I + exterior exactly if and only if λ = μ on [1, N]. Selberg or
   Barban–Vehov weights add the interior block I^λ of (4.3). The quadratic version (4.4) gives A_M on vectors
   outside P_T, not a square.
4. (iv) (PROVED): with sieve weights fixed without the weight, everything is affine in c; R3-e applies literally.

## What failed and why

- L161.1 fixes its weights by a condition that does not see Λ and admits only the trivial solution (Lemma 1).
- Selberg positivity needs a positive measure on the integers; in the form that measure is s_M,
  the target itself (Cor. 4.3 of R162_1003).
- Sieve or Möbius weights are of degree 0 in the weight; the identity stays affine (R3-e).

NOT excluded (no object written):
1. tests not of the form S_N𝓕F or M^λ*F, and weights depending on F;
2. telescoping after compression to the window, with the leakage squares of C_T (no identity of
   this memo produces them; the joint accounting R161_032 (4.2) remains underived);
3. the "Möbius of the system" μ_a (not polynomial in c), with its E_N^{(a)} without Poisson for c ≠ 1;
4. the interior block I^λ of (4.3) as a near-coincidence form with sieve coefficients θ^λ: its
   sign was not examined; by R3-e it cannot give a sign separately if λ does not depend on the weight.

## Concrete next step

Do not build in this zone. Record in index and grid: "Phase 212, round 4A: L161.1 with signed weights in N:
NO-GO with class 𝒞_w PROVED (exact telescoping forces w = δ_1, tautological identity; incompatible with
cancelling the tail); the truncated Möbius identity of 003_6 is not an instance of L161.1 (Prop. 2);
exactness of M^λS_N = I + exterior ⟺ λ = μ on [1, N]; Selberg/Barban–Vehov weights give an interior block
and a form affine in c (R3-e). Repetition of phase 200 Q1–Q3, R-MOM, GG_001 and R162_1003 §4 for (iii). Global
sign OPEN." A second reading should verify (4.1) (𝓕A_M𝓕 = A_M, which depends on the conventions of
R161_001 §1) and the coefficient computation (4.2).
