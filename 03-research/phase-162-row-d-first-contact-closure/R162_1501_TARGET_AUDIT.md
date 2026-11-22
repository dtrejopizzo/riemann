# R162_1501 — Target audit: is "R_L F = 0 at first contact" the right intermediate target?

Strategist audit. Pure mathematics, with two UNCERTIFIED float checks (§4), used as guidance only.
Inputs: README, R162_590, R162_1402 (Thm 3, §7), R162_504 (Thms 1–3), R162_703, R155_044–046 (nodal round),
Paper 46 §sec:firstcontact (lem:firstcontact, eq:Gammaenergy, eq:Qspectral, prop:GEgap, eq:equivgate, prob:annihilate).

**Verdict.**
- R_LF = 0 is **not an intermediate target**. On the radical it is F = 0 written in Müntz coordinates (§1).
- It also **works against the structure**. A new, elementary Descartes–Laplace lemma (Lemma D, PROVED) turns
  "K_F(a_m) = 0 for m ≤ L" into "F has at least 2L+2 sign changes". The collapsing bottom branch of ζ has exactly
  the minimal 2 sign changes (float, §4). A contact vector on that branch would therefore have K_F(a) ≠ 0 at
  **every** real a ≠ ±½, with one common sign for all a > ½. This explains the R162_1402 warning structurally.
- So Gate 1 can only be reached as the output of a contradiction. Its natural form is "a first-contact vector with
  finitely many (in fact 2) sign changes cannot exist", not "these moments vanish".
- Recommendations (§3): R-A oscillation budget; R-B one Euler-channel sign; R-C Type-I rate plus a Chebyshev pair.
  None of them closes row D. Each has a declared falsifier line.

No sign is claimed. No label moves.

## 1. (a) How Gate 1 was derived, and what it is equivalent to

Derivation (Paper 46 §sec:firstcontact):
1. lem:firstcontact: if λ_A < 0 somewhere, then T_* = inf{λ_A < 0} ≥ log 2. By lem:contA, 0 is an eigenvalue of H_{T_*}
   with a parity eigenvector F ∈ P_{T_*}.
2. eq:Gammaenergy: R: F ↦ (b_m K_F(a_m))_m is **faithful**. Substitute x = e^{−2t}; the powers x·p(x) are dense on
   [e^{−2T}, e^{2T}], an interval that does not contain 0. Hence RF = 0 ⇒ F = 0. The radical is finite-dimensional,
   so some finite L makes R_L injective on it.
3. eq:Qbalance and eq:Qspectral: on an eigenvector, Q_{N,L} = −2Σ(d_{m,N}+λ)|(R_LF)_m|². So
   Q ≥ 0 ⟺ ⟨F,ΔF⟩ ≤ 0 ⟺ R_LF = 0 (eq:equivgate).
4. prob:annihilate asks for R_LF = 0, proved from PC-ren using minimality, orientation and Λ*1 = log.

What it is equivalent to:
- For F in the radical: R_LF = 0 ⟺ F = 0 (step 2). Gate 1 at T_* ⟺ ker H_{T_*} = {0} ⟺ no first contact at T_*.
- Over all T this is λ_A ≥ 0 ∀T ⟺ RH (lem:firstcontact converse).
- The "reduction" R_LF = 0 ⇒ F = 0 takes one line. All the content sits in the vanishing statement. The other known
  forms are all the same statement:
  - ESB (R162_203);
  - (A)+(B) ⟺ K^ε = {0} (R162_304);
  - the Douglas bound (R162_1301 Thm 3);
  - the rate |x_m(ψ_T)|² = O(λ(T)) (R162_1402 Thm 3c).
- The only thing R_LF = 0 adds over F = 0 is the **output format**: a linear vanishing at an arithmetic lattice whose
  residues are ζ(s_m)K_F(a_m) (eq:residue).

Why this format is unnatural (the F1 point sharpened):
- Gate 1 is a linear condition. Any argument yielding it must fail on near-null vectors, since those have x_m = O(1)
  (R162_1402 §7).
- Lemma D below shows that x_m ≠ 0 is **forced by the sign structure** of those vectors. It is not a numerical
  accident.

## 2. The oscillation facts (Lemma D is new; Props N1 and N2 are corpus)

Definition. S(F) is the number of sign changes of F ∈ L²(I_T), in the a.e. sense of R155_045 §2.

- **Prop N1** (R155_044/045/046, PROVED): the unconstrained ground state ψ_T of A_T is simple, even and > 0.
  R162_504 Thm 1 proves this with the comb (v_n ≥ 0).
- **Prop N2** (R155_046, PROVED): {e^{t/2}, e^{−t/2}} is a Chebyshev system. Hence S(F) ≥ 2 for every 0 ≠ F ∈ P_T.

**Lemma D (Descartes rule for the Gamma moments) — PROVED.** Let 0 ≠ F ∈ L²(I_T) with S(F) < ∞. Then the real zeros
of the entire function a ↦ K_F(a) = ∫e^{−at}F(t)dt, counted with multiplicity, number at most S(F). Consequently, for
F ∈ P_T (so K_F(±½) = 0):
- (i) If F is even, K_F is even. R_LF = 0 forces zeros at ±a_1, …, ±a_L, ±½. Hence **S(F) ≥ 2L+2**.
- (ii) If F is odd, K_F is odd and also vanishes at 0. Hence **S(F) ≥ 2L+3**.
- (iii) Gate 1 in its Müntz form (K_F(a_m) = 0 on a harmonic-divergent set, R162_1201 Thm 4.1) forces S(F) = ∞.
- (iv) If S(F) = 2 (the minimum for P_T), then K_F has only the simple zeros ±½. Hence K_F(a) ≠ 0 for every real
  a ≠ ±½, and sgn K_F(a) is constant on (½, ∞). All the x_m = ζ(s_m)b_mK_F(a_m) share one sign.

*Proof.* The kernel e^{−at} (equivalently e^{a(−t)}) is extended totally positive in (a, −t). Hence the Laplace
transform is variation-diminishing: Pólya–Szegő II, Part V, Problem 80, or Karlin, *Total Positivity*, Ch. 5, Thm 3.1
(CITED). For finite S one splits I_T at the S sign-change points and applies Rolle inductively to
e^{a t_1}K_F(a). (i)–(iv) are counting. ∎

Remark (not in the dead-end map).
- R155 used nodes only to predict matrix-entry signs in the archimedean basis. That route (P8) is CLOSED.
- The link "node count ⇒ Gamma-moment non-vanishing" does not appear in phases 150–162. (I grepped "Descartes",
  "variation-diminish", "sign change", "nodal", "Sturm".)

**Corollary D′ (closedness).** {F : S(F) ≤ S₀} is closed in L². So a norm limit of primitive vectors with exactly 2
sign changes has S = 2, by Prop N2. If a first contact is reached by a bottom branch whose vectors have 2 sign changes
near T_*, then the contact vector violates Gate 1 at **every** m. There is no m for which a proof of "K_F(a_m) = 0"
could be locally true.

## 3. (b) All contradiction targets derivable from a first contact, audited

Legend:
- "Near-null" means consistency with ζ's float near-null vectors (§4, and R162_1402 §7).
- "Map" is the R162_590 status.

| # | Target: a property of F forced at contact, versus another exact constraint | Near-null consistent? | Map / verdict |
|---|---|---|---|
| 1 | Gate 1, R_LF = 0 (Gamma moments vanish) | **No.** x_m = O(1), sign-coherent (Lemma D(iv)) | = F = 0 (§1). Keep only as output format |
| 2 | Tate endpoints K_F(±½) = 0 | Yes (built in; uses 2 of the node budget) | Constraint, not a target |
| 3 | Parity ladder: odd contact ⇒ μ_2(A) ≤ 0; even ⇒ μ_1 < 0 ≤ μ_2^ev (504 Thm 2/3) | Yes (odd bottom stays above even) | μ_2 ≥ 0 ∀T is E1 (504 Cor 2.1) |
| 4 | Type I (r = 0: AF = 0, F ⊥ ψ_T) or Type II (F = cA⁻¹φ, f(0) = 0) | Mixed: Tate residue ‖r‖ ≈ 0.6λ → 0 (near Type I), but S = 2 | Type II exclusion by minimality NO-GO (703). **Nodal refinement new: R-C** |
| 5 | Support hull / collar non-extendability, right minimality | Yes (weight-blind) | Dead (405, 406, 408) |
| 6 | T_W ≤ T_* (complete contact first) | Yes | Proved (703, 802). Transfers the problem to W; the W null vector has no Tate budget. Open, no mechanism |
| 7 | Perron positivity: ⟨F, ψ_T⟩ vs Tate alignment c_T | Yes; ⟨F,ψ⟩ ≈ λ/|μ_1|·O(1) | Quantitative alignment dead by Thm M (504 Prop 4.3, 702) |
| 8 | Fixed nodal count of the bottom of H_T for all T (Sturm) | **No** (float): even bottom has S = 2 at T = 0.3, 0.5, then 6, 4, 4, 6 at 0.6–0.75 (level crossings), then 2 from 0.78 to 1.2 | Refuted as "∀T". The Karlin kernel route is closed (R155_046 N3) |
| 9 | Finite oscillation budget of radical vectors, S(F) ≤ S₀ < ∞, plus Lemma D | Yes (S = 2 on the collapsing branch) | **Not in map: R-A** |
| 10 | Sign-coherent exterior Gamma field σΣx_m e^{−a_m t} (CM, definite for t > T), versus an exact signed Euler-channel identity | Yes (K_F(a_m) one sign for m = 1..4 at every T tested) | **Not in map: R-B** |
| 11 | Reflection alternation G_+^0(−a_m) = −εζ′(−2m)K_F(a_m) (sign (−1)^m) | Yes | Alternation comes from ζ′'s own real zeros; G_+^0 is not a real-line Laplace transform in that half-plane. No contradiction (402, 1101) |
| 12 | Balance 0 = 2c + Q (eq:Qbalance) | Yes (holds with λ in Q-spectral) | Quadratic, equivalent to Gate 1 (eq:equivgate) |
| 13 | Rate law |x_m(ψ_T)|² = O(λ) (1402 Thm 3) | **No** (x_m = O(1), λ collapses) | E1; pushes against the data exactly like #1 |
| 14 | Analyticity / real-analytic interior regularity of F (kernel equation is a log-order nonlocal difference equation) | Unknown | No gain mechanism (log order, shifts preserve regularity). Useful only as the input "S(F) < ∞" to R-A |
| 15 | Zero-side kernel equation Σ_ρ c_ρ e^{(ρ−½)t} ∈ Tate span on I_T | Not testable | Zero-side reverse engineering always negative (memory, R155 reverse track); E1 |
| 16 | Virial / Selberg sign 𝒱 ≤ 0 on N | — | E1 (407, 501) |

Summary of (b):
- Every target phrased as **vanishing of a linear Gamma/Euler datum** (#1, #13) is contradicted by the near-null data.
  Lemma D shows why.
- Every quadratic balance (#12, #16) is equivalent to Gate 1.
- The unused structure consists of the **sign and oscillation data**: #4 refined, #9, #10. Those are robust on
  near-null vectors, so an argument based on them does not fight F1.

## 4. Float checks (UNCERTIFIED; scripts `scripts/c3/t1501_nodal_counts.py`, `t1501_gamma_sign_tate_residue.py`)

Method:
- The Galerkin setup is that of R162_1402 (Legendre K = 34), with contacts n < 400.
- S is counted on a 4001-point grid, ignoring values below 10⁻⁶·max.
- λ is not converged for T ≥ 0.8 (float 4.4e−7 against the certified ≈ 2.5e−12 at ½log5).

Findings:
- **Unconstrained A.** Bottom S = 0 at every T (Prop N1 ✓).
- **Even primitive bottom.** S = 2 at 0.3 and 0.5; 6, 4, 4, 6 at 0.6, 0.65, 0.7, 0.75; 2 at 0.78, 0.8047, 1.0 and 1.2.
  From 0.78 on, the collapsing branch is the 2-node one. It coincides to float precision with μ_2(A).
- **Gamma moments.** K_F(a_1..a_4) on the even bottom has one sign at every T (for example 0.48, 2.56, 10.3, 38.5 at
  ½log5). Lemma D(iv) ✓.
- **Tate residue.** ‖AF − λF‖ / λ ≈ 0.21, 0.57, 0.58, 0.59 at T = 0.5, 0.78, 0.8047, 1.0. ⟨F, ψ_T⟩ ≈ 0.6λ/|μ_1|.
  The near-null vectors have Tate residue r = O(λ), so they are asymptotically Type I.
- **Odd primitive bottom.** S = 7 at 0.78–1.0 and 5 at 1.2. This is not minimal; the odd minimum is 3. Low
  reliability.
- **Chebyshev-pair test.** Monotonicity of ψ_T / cosh(t/2) on (0,T) is inconclusive: 55–69 % of grid steps are
  decreasing. This is likely derivative noise. It is not established.

## 5. (c) Recommended targets (not refuted by the near-null behaviour, not in R162_590)

**R-A. Oscillation budget ⇒ finite explicit Gate 1.**
- Target: every radical vector at a first contact has S(F) ≤ S₀ < ∞, with S₀ explicit. A natural conjecture is
  S₀ = 2 in the even sector, when the contact is reached by the collapsing branch.
- Consequence (by Lemma D): Gate 1 collapses from infinitely many moments to ⌈(S₀−2)/2⌉ + 1 of them. For S₀ = 2, the
  **single** condition K_F(5/2) = 0 already forces F = 0.
- Reading: this does not make Gate 1 easier. It shows that a contact must be excluded by "a 2-node even radical
  vector does not exist", and it gives the precise object to attack.
- Tools: the Beurling–Deny form of the Dirichlet part plus the positive comb, and Courant-type counts for Markov
  generators. Karlin total positivity is unavailable (R155 N3), so use a direct two-cell rearrangement argument in
  the style of 504 Thm 1 (iii).
- **Falsifier line:** the step "S(F) ≤ S₀" uses v_n ≥ 0. It holds verbatim for deletion and κ-models, which have
  first contacts (F3). So R-A is infrastructure. The closing step must be the one that makes a 2-node contact
  impossible, and it must use Λ*1 = log at that step (it must fail for Λ1_{n≥5}). For DH, v_n changes sign and
  Prop N1 fails; declare that line.

**R-B. One signed Euler-channel scalar (replaces infinitely many vanishings).**
- On a 2-node even contact, E_t(F) = Σx_m e^{−a_m t} is σ-definite and completely monotone for t > T_*. The same
  holds for the Euler functionals w_nE_{log n}(F) = Σ_m Λ(n)n^{−2m−1}x_m (R162_1402 Thm 4c: a positive combination of
  coherent-sign data).
- Target: an exact λ = 0 identity in which one Euler-channel scalar is forced to vanish, or to take the sign −σ. That
  single scalar would contradict coherence.
- The candidate source is the collar residual of R162_1402 Thm 2(iii) at the thresholds ½log n versus ½log nm
  (O802.1, with the Gamma probe). Its comb spill C_Nu is the only Λ-dependent term. It must be evaluated **before**
  regularisation (R162_204).
- Near-null consistent: coherence holds on ψ_T for every T tested.
- **Falsifier line:** coherence is weight-blind. The forcing identity must fail for deletion (edge coefficient at a
  deleted prime) and for Λχ₂, and must use Λ*1 = log at a composite threshold without the R162_406 cancellation.
  Kill test: if the identity is linear in PC-ren it is F4-dead; if it is a square it is F2-dead.

**R-C. Type-I rate plus Chebyshev pair.**
- Two sub-targets:
  - (C1) ⟨F_T, ψ_T⟩ = O(λ(T)) along the bottom branch, equivalently ‖r_T‖ = O(λ(T)). Float: ratio ≈ 0.6.
  - (C2) {cosh(t/2), ψ_T} is a Chebyshev pair on [0,T], i.e. ψ_T / cosh(t/2) strictly monotone.
- Consequences:
  - (C1) makes the contact **Type I**: AF = 0, F ⊥ ψ, and μ_2^ev(A_{T_*}) = 0.
  - (C2) forces every even vector ⊥ {ψ, cosh} to have S ≥ 4.
  - Together with a 2-node branch (R-A), this is a contradiction.
- This is the first target in which "Type I versus Type II" (dead as a minimality question, 703) acquires a
  non-minimality lever: a rate plus a node count. Each piece is robust on near-null vectors.
- **Falsifier lines:**
  - (C2) is a Perron/comb-positivity statement, so it is F3-blind.
  - (C1) is a rate between two infinitesimals, like 1402 Thm 3. It must be tested on the deletion model's contact at
    0.58–0.60 before any proof attempt. If the deletion contact is also Type I with S = 2, then (C1)+(C2) are
    contradictory there too, i.e. one of them is FALSE for deletion, and R-C is weight-blind and dead.
  - This makes R-C the **cheapest to falsify**: one float run of the deletion model.

Ordering:
1. R-C deletion test first: cheap, and decisive for R-C.
2. Then R-A (S₀ = 2): this is the structural theorem the other two need.
3. R-B last. It is the only one whose closing step is a single Λ-specific scalar.

## 6. For R162_590

- Add to §1c: "Fixed nodal count of the bottom of H_T ∀T — float crossings 0.6–0.75 — REFUTED as ∀T (UNCERTIFIED)".
- Add to §1c: "Linear-vanishing targets (Gate 1, rate law) — contradicted on near-null vectors by Lemma D (2 sign
  changes ⇒ all K_F(a_m) ≠ 0) — use only as output format".
- Add to §2: R-A, R-B, R-C as untried, with the falsifier lines above.

Files: this file; `scripts/c3/t1501_nodal_counts.py`, `scripts/c3/t1501_gamma_sign_tate_residue.py` (float, uncertified).
