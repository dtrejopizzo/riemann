# R186_032 — Synthesis of round 15: what remains attackable after wall W-lin?

Phase 186, decision round (not a construction round). Paper 47, grid and crossword are not touched.

Read: README rounds 14–15; R186_029/107/030/031; grid entries 25–27 and §3 (walls); phase 186 crossword addendum
(§1–§3); R185_005 (BR, §1.3 O1–O5); R164 README ((TC)); R163_401 §4.8 and status table; R166_501 Cor A.2 ((G),(N));
R166_190 rounds 9–12 ((N′)); R155_010 (Theorem N) and R155_049 (AL′); Paper 47 def:PD, def:W/eq:nuw, thm:Z, lem:Rrig,
cor:nontermwise, thm:O, thm:C, thm:N, thm:AL, rem:comblp; R186_025 (Thm A/B), R186_026 (Gram, Thm 4.1),
R186_028 (Thm 1.2), R186_012/015 (ε_S).

## 0. Verdict in one line

**None of (i), (ii), (iii) today has a positive statement that the new tools allow attacking without falling into
W-lin.** (i) has no object in the toolbox (all the new tools belong to family P: quadratic in F, linear in Λ,
interior to the window); (ii) has a decidable statement, but it is linear in the masses, is verified by evaluation,
and its structural reading dies against thm:C; (iii) in its mixed form is exactly the numerics of thm:C, and its
primal twin (Thm B) is the Fejér tail, not the body. What there is: two pure impossibility lemmas of class, which
close residues (R30.1 and the dichotomy of eq:nuw), and the specification of the missing tool (§4).

## 1. What W-lin says and what the escape criterion is

W-lin (grid, entry 27): certificates linear in a fixed basis, reductions by congruence/Schur/inertia, and norm
bounds do not decide any new window. Its proved content is: (a) every quadratic form in F with fixed basis and
coefficients linear in Λ within the window is W_T rewritten (R186_026 Thm 3.3, R186_028 Thm 1.2, R186_031 Dom);
(b) every operator-norm bound loses against 𝒜_T (R186_104, R186_025 §3.3, R186_031 Y). The correct escape criterion
is not "Lemma H" (ARGUED, R186_107 1b/1d) but that of R186_107 §3: what distinguishes a route is whether its
verification is **structural** (an identity with O(1) data) or **numerical** (deciding a sign of size ≤ λ_A). With
R186_030 Thm 1 (Szegő tautology) this is refined: "identity" is not a class of certificates but of presentations,
and the three explicit presentations are closed (Thm 4 (i)–(iii)). So a route escapes W-lin only if
(E1) it is not linear in F (or is of projective degree 0: (G) of R166_501), and (E2) it uses Λ beyond the window
with localization strength ((N′), R166_802), or else (E3) it exhibits a new presentation, not enumerated in Thm 4.

## 2. The three candidates, one by one

### (i) Tools nonlinear in the test function: (TC), (★_cell), (G)+(N)

*Precise statement.* (★_cell) (R163_401 §4.8): in every real-rooted first-contact witness with an ordinate off the
line, P_j > N_j in every nodal cell. (TC) (R164 README): C_{T_c} − iG²𝒯_X has no poles with Im x ∈ (−½, 0),
𝒯_X = Σ_{n≥X}Λ(n)n^{−1/2+ix}, X = e^{2T_c}. Requirements of every proof (R166_501 Cor A.2, R166_802): (G) nonconstant
projective invariant of the witness, global in X; (N′) control of Λ beyond the window at the node's frequency with
localization strength Θ − ½.
*Why it escapes W-lin.* It satisfies (E1) and (E2) by definition: Re G(t_q)² is the jet k = −1 (W-jet), not a
polynomial function of any nodal datum; (TC) concerns the tail of −ζ′/ζ.
*What new tool would be used.* **None applies.** Inventory: Thm A/B (archimedean coercivity: only m and the geometry
of 𝒱_k, without Λ); 𝒱_k ⊕ E_k and K₁ (change of basis); index by sectors (inertia accounting, passes exactly but
without margin); closed Gram matrix and jump kernel 𝒢_T (R186_026 Thm 4.1: linear reformulation of D by window, with
the primes already inside G via K); semilocal chain (ε_S uses the complete local factors ρ_p, i.e. all powers p^k
including those > e^{2T}, but enters via identity (84)_S and one-sided positivity Son_S ≥ 0: W12 + W11, not (N′);
M_m shares the atomic side); accounting at τ=0 (linear in ν). All belong to family P of R166_405 (quadratic in F,
linear in Λ). No toolbox object is of degree ≠ 2 in F nor sees Λ beyond the window with localization strength.
*Check.* (★_cell) OPEN: R163_401 table (§4.8 ARGUED, Rem 4.8a), R164 README "Phase closed; (★_cell) OPEN",
R185_005 §1.3 (O1) and §4. Partial closures that bound the shape of any proof, not the statement: R166_201 Thm 1.3
(jets), R166_501 Thm A ((iii) ⟹ (ii)), R166_802 Thm 1–4 (circularity of inequalities over Λ; exponent-½ sieves),
R164_401 Thm R (identification). No new object since phase 169 (R186_107 4c).
*Falsifiers every object must fail.* M_m (R163_801 Thm 5), f_t (R163_901), P_{a,c} (R166_101), erasure (R185_004),
combs (phase 156).
*Verdict.* Valid goal, no attackable statement RIGHT NOW. What is missing is the tool of §4.

### (ii) Certificates with ν⁻ of ≤ k atoms (R30.2)

*Precise statement (in def:PD).* Cert_k(T): there exists (ν, β) with ν = ν⁺ − ν⁻, ν⁺ ≥ 0 (density or measure),
ν⁻ = Σ_{i≤k} m_i(δ_{u_i}+δ_{−u_i}), supp ν ⊂ {|u| ≥ 2T}, and f = σ_T + ν̂ + β·ĝ ≥ 0. NoCert_k(T): sup over that class
of inf f ≤ −κ_k(T) < 0. Case k = 0 = class B: NoCert_0 PROVED at ½log3, ½log5 (R186_030 Thm 3), OPEN at log2⁺ (R30.1).
*Check (not closed, but bounded on both sides).* thm:N: no lattice certificate with step 2T/M, M ≤ 8, at ½log3 (any
number of atoms). thm:C: lattice certificate with M = 24, 437 signed atoms, ‖ν‖_TV = 90.75, ν(ℝ) = 1.73. thm:O:
‖ν‖ → ∞ in every maximizing sequence, so a certificate with bounded k has value < λ^P strictly (consistent, does not
decide). rem:comblp (NUMERICAL): the comb-vanishing class (no atoms, ν⁻ only a density) gives negative minima at
½log3, 0.58, 0.62, log2. AL′: lattice sampling loses Θ(1/M). No one has formulated NoCert_k with k ≥ 1; R30.2 is the
first mention.
*Why it does NOT escape W-lin (argument).* (1) The certificate is linear in the masses (m_i, ν⁺) with fixed basis
except for k real parameters (positions); the verification of f ≥ 0 is evaluation (R186_030 Thm 1: there is no
presentation), so Cert_k(T) is an LP by window: numerical and by window. (2) The structural reading that would save
it — "the negative mass is the primes outside the window", i.e. the dual of (N) — is **false in def:PD**: in thm:C
the negative atoms sit on the lattice j·log3/24, not at log n (log4/d = 30.28 ∉ ℤ). In 𝒲_cl (eq:nuw) the negative
mass comes from w(log n) > 0 at prime powers outside the window **or** from w < −K/(4cosh(u/2) − K) in density; the
second source is linear and free in w, and the weak-duality method of Thm 3 does not reach it: a test μ that bounds
∫f_w dμ for every w free outside the window must have μ̌ = 0 on |u| ≥ 2T, i.e. μ = |F̂|² dτ: it is the primal (strong
duality, thm:O). (3) NoCert_k is an impossibility lemma (a tool), not a sign; and κ_k must vanish before k ≈ the
number of negative atoms of thm:C, so it is a statement for small finite k.
*New tool that would be used.* None from the list above; only the weak duality of R186_030 with tests Φ having
prescribed zeros at the positions (Φ(u_i) = 0, Φ ≤ 0 outside the window, Φ̂ ≥ 0) and compactness in the positions.
*Falsifier of Cert_k.* NoCert_k. *Falsifier of NoCert_k.* an LP with cardinality giving value > 0.
*Verdict.* Decidable, numerical, no contact with the sign. Does not meet the criterion.

### (iii) Bochner's archimedean mechanism (A), mixed form

*Precise statement.* Exhibit, for T ∈ (½log2, ½log5], w ∈ 𝒲_cl with f_w = m + \hat{β_w} ≥ 0 proved by an explicit
reorganization (not by evaluation), with β_w of eq. (1.2) of R186_030 (mixed sign). Proper object: exact accounting
at τ = 0 (ν_w(ℝ) ≥ Δ(T) > 0, PROVED) and the first negative lobe of 2ĝ₀ at τ ∈ (π/2T, π/T), where the positive mass
that fixes τ = 0 spoils the sign.
*Check.* R186_030 Thm 3 (class ν ≥ 0 NO-GO at ½log3, ½log5; log2⁺ R30.1), Thm 4 (excluded class (i)–(iii); (iv) =
thm:C). R185_006 (symbol θ = m − v₂cos, θ(0) = −6.35: the positivity belongs to the compressed operator). R186_022
(zero of the Sonin density NO-GO). R155_033 (the τ = 0 cap forces w substantially negative elsewhere). R186_030 §3.3:
Fejér on the cosine proves only the tail |τ| ≥ τ_* = 2π exp(𝖠_T + ‖ν_w‖_TV + 2|ĝ₀|_∞ + 1).
*Why it does NOT escape W-lin.* The mixed form is linear in ν with evaluation-based verification: it is (ii) with
free k, i.e. thm:C. And the **primal twin** of (A) is already in the toolbox and shows exactly its reach: Thm B
(R186_025) is "increasing m + high-pass" = Fejér, giving coercivity log(k/T) − C_B on 𝒱_k and leaving positivity on
E_k intact (dim 2k − 2, which inherits thm:margin: R186_104, crossword §3). Dually: (A) proves the tail τ ≥ τ_* and
leaves the body [0, τ_*] intact, with τ_* doubly exponential in T (𝖠_T ≈ 2e^T), which is where |F̂|² lives for
F ∈ E_k. They are the same mechanism seen from both sides, and in both the content is the cancellation between
cos(τ log n) and m in the body, which by thm:Z(ii) is Σ_ρ ŵ(τ − γ_ρ) (cor:nontermwise: never term by term). The
only thing left with a "proper object" is residue **R30.1**: closing class B for every T > ½log2 (today two points),
which is a negative lemma.
*Falsifier.* A w ∈ 𝒲_cl^reg with f_w ≥ 0 verified by an explicit sum-of-squares identity (not enumerated in Thm 4) in
a window T > ½log2.
*Verdict.* No attackable positive statement; only R30.1 as a class closure.

## 3. Table

| front | attackable positive statement now | escapes W-lin | applicable new tool | closed by | status |
|---|---|---|---|---|---|
| (i) (★_cell)/(TC), (G)+(N′) | no (no object since phase 169) | yes, by definition | none (all family P) | nobody: OPEN (R163_401 §4.8, R164, R185_005 O1) | valid goal without a tool |
| (ii) ν⁻ ≤ k atoms | Cert_k(T): LP by window | no (linear in masses, verification by evaluation; reading (N) false by thm:C) | weak duality of 030 | k=0: 030 Thm 3 (½log3, ½log5); k≥1: nobody | decidable, numerical, no sign |
| (iii) mixed Bochner | no (= thm:C) | no (Thm 1 of 030; primal twin = Thm B = tail) | Thm B (already used) | class B: 030 Thm 3/4; mixed: OPEN = thm:C | only R30.1 |

## 4. The missing tool: specification Ω

A tool that closes D (or a new window without numerics) must be a functional 𝔍(F; Λ) ≥ 0 on the witness class with:
- **(S1) nonlinear in F**: even projective degree ≥ 4, or degree 0 (phase of G at t_q, harmonic measure of the node
 set; R165_201 Thm 2, R166_501 (G)). Excludes every quadratic form in a fixed basis (W-lin) and every rewriting of
 𝔞_T.
- **(S2) uses Λ|[X, ∞) at the frequencies of the nodes of F̂** and not as a single test of (1.1) nor as the cone
 Λ ≥ 0: (N′) requires, in the witness, the O-bound of the sum Σ_{n>X}Λ(n)n^{−½−iγ_q}φ(·) with strength equal to the
 absence of the zero; sieves give exponent ½ (R166_802 Thm 4) and identities + Perron give zero density (Thm D,
 ARGUED): Ω must contain an arithmetic input that is neither a sieve nor Perron. This is the blank box; it is
 unknown.
- **(S3) structural verification**: O(1) data, no sign of size λ_A to decide (R186_107 1d).
- **(S4) not an identity (W12), not one-sided positivity (W11/W11′), not a class property with EF
 (W-identification)**: the named class must be strictly larger than {ζ} and exclude M_m, f_t, P_{a,c}, Ξ_a,
 erasure, combs.
- **(S5) coupling**: 𝔍 couples the node set X of F̂* (zero side) with the atomic side of Λ beyond the window
 (dichotomy R166_190 §0); the only datum proper to ζ is the exact duality Z_ζ ↔ atomic Λ in log ℕ at all heights
 (R163_114).
- **(S6) admission proof**: before building, show that 𝔍 fails on M_m and f_t with their own witnesses (if it does
 not fail, it is family P or Q of R166_405 and falls into W3 or identification).
The only nonlinear object in the corpus satisfying (S1) and (S2) is the moment/Kreĭn reformulation (phase 155 round
5, R157_004 O4), which is a RESTATEMENT (with no direction proved from arithmetic); Ω must be what proves it. None
of the tools from phases 163–186 is a candidate: all violate (S1) or (S2).

## 5. Recommendation for round 16

**Single front (tool, pure mathematics): class closure of mechanism (A) and dichotomy of the certificate.**
First lemma to prove: **Lemma B(T)** (= global R30.1): for every T > ½log2 there exists an even probability test μ_T
with Φ_T = μ̌_T ≤ 0 on |u| ≥ 2T and Φ̂_T ≥ 0 such that ∫k̂ dμ_T ≤ −κ(T) < 0, with k̂ = m − Σ_{𝒩_T}v_n cos(τ log n) + 2ĝ₀;
explicit family of 2–3 Gaussians with parameters as a function of T (α, β, b as in R186_030 §3.2), verifiable
elementary quadrature. Immediate consequence (one line with eq:nuw): **Lemma D (dichotomy)**: every certificate
(ν_w, 2, 0) with w ∈ 𝒲_cl and T > ½log2 has w(log n) > 0 at some prime power n > e^{2T}, or w < −K/(4cosh(u/2)−K) on
a set of positive measure outside the window. Expected labels: both PROVED. Falsifier of Lemma B(T): a T > ½log2
where the LP with ν ≥ 0 (r030_class_B.py) gives value ≥ 0. What it contributes: closes R30.1, turns the "exact
obstruction" of R186_030 into a theorem for every T, and leaves (A) closed in Paper 47 as a declared class. **No
contact with the sign; no new window is promised.**

**Reserve front:** NoCert_k(½log3) for k ≤ 3 by weak duality with tests Φ having prescribed zeros at the positions
(k parameters, compactness on [2T, U] + tail): decides whether the negative mass must be "diffuse". Probably ends in
an LP with cardinality (NUMERICAL); that is why it is a reserve.

**What is not done:** (★_cell)/(TC) are not relaunched without a candidate 𝔍 that passes (S6); Cert_k and the mixed
form of (A) are not promoted as routes (they are thm:C); the semilocal chain is not presented as (N) (it is
(84)_S + Son_S ≥ 0).

*Row D: OPEN. No grid symbol changes. Nothing is claimed about T > ½log5.*
