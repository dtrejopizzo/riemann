# R162_2702 — Boundary triples for W_λ, doc 107 settled, NG-D4 tested

Phase 162, round 27. Cells: 1D (NG-D4, boundary triples) and 4C (doc 107).
Nearest grid routes: 1D residuals "NG-D4 / I15" and "phase-60 §4.B boundary triples"; 4C residual "doc 107 / I7".
No sign is claimed. Gate 1 stays OPEN.

## 0. Falsifier lines (written before the work)

- **F1 (jets at λ=0).** None of the three items enters as λ·⟨…⟩ or as a first variation. Not fired. It does not apply.
- **F2 (orientation / wrong sign).** NG-D4 *is* an orientation statement (Q ↦ −Q under Fourier). Test it against the index pair (n₊, n₋). **Fires** (§3).
- **M (margin / Theorem M).** No numerical margin is used. Not fired.
- **F3 battery (deletion, M_m, Λ̃, DH, Beurling DMV).** Run on the boundary-triple invariants. **Fires identically.** The operator W_λ contains no Λ (§2.5).

## 1. Doc 107 (two-variable Weil formula): verdict **CLOSED — genuinely, but not by MW-7**

Sources: `phase-36-ABC-forms/107-execution-of-problem-5-4-the-weil.md` and `108-sieve-index-bridge-formulation-unconditional-inventory.md`.

**What 107 left open.** Doc 107 ends as "CANDIDATO VIVO". It has Lemma 5.2 conditions 1 and 2, the mixed zeros×primes terms reabsorbed, and MW-7 absent, and it passes everything to **Missing Lemma 7.2** (the sieve→index bridge = P42 Lemma 6.1).

**What 108 does.** Doc 108 executes exactly Lemma 7.2 step (1) and returns **PUENTE MUERTO**, for four reasons:
1. The test-accessible index is binary: κ_W(Q₂) = 0 for every window under RH, and ≍ m·log T (unbounded) under ¬RH (Prop. 2.3–2.5). So any finite uniform bound is RH. This is **E1**.
2. The literal mechanism "index ≤ sign changes of K(N)" is false, because K ≥ 0 (Obs. 3.5).
3. The needed estimate is second-order asymptotics that is uniform in windows (Conj. 108-N), and it implies RH (Thm 4.3). The in-mean version (Montgomery–Vaughan) is a theorem but is insufficient. This is **W2**, the quantifier.
4. Amplification in k does not help (Prop. 7.3).

**The label needs one correction.** The grid says the residual might be "absorbed by 108/MW-7". MW-7 is *not* what kills it: 107 §4 shows MW-7 does not reappear in the functional. The killer is **W2 + E1**, reached through the sieve→index bridge.

**Independent structural confirmation (PROVED, elementary).** W₂ = W⊗W. For Hermitian forms with finite signatures, sig(W⊗W) = (p²+n², 2pn). So n₋(W⊗W) = 0 ⟺ n₋(W) = 0 whenever p ≥ 1. This passes to compressions and to the inductive limit over windows, because the index of a compression is ≤ the index of the whole and grows to it along exhausting families. Consequences:
- The only sign information in W₂ is n₋(W), i.e. RH itself (E1).
- The (8,8) block of 107 §5 is the tensor count 2·p·n restricted to the quadruple span.
- Nothing in 107 escapes: its doc-106 "amplification" of the index is multiplicative in n₋(W) and vanishes exactly when n₋(W) vanishes.

**What survives from 108 §8.3 (tools only).** Thm 3.3 (sub-resolution positivity of Q₂), the identity ΔK ↔ pair correlation, and the long-range target κ_W ≤ C n_W ⇒ m ≤ C/2. The last one is the 8F residual m<∞ in another form.

**Grid action.** In 4C, remove the "doc 107 / I7" live residual. New route R162_2702a: DEAD, killer "W2;E1", supersedes "doc 107".

## 2. Boundary triples for W_λ: **PROVED (classification + Weyl function); NO-GO for touching O2601.1**

Setting (CCM; phase-60 11.3-bis):

W = −∂((λ²−q²)∂) + (2πλq)² on L²(ℝ).

The formal operator commutes with the Fourier transform F on S(ℝ) (Slepian's commutation, used as in CCM).

### 2.1 Endpoint analysis (PROVED)

- At q = ±λ, from either side: the endpoint is a regular singular point with indicial roots {0,0}. Solutions are 1 + O(q∓λ) and log|q∓λ| + O(…). Both are L², so the endpoint is **limit circle**. Near e ∈ {λ±, (−λ)±}, write f = a_e·log|q∓λ| + b_e + o(1).
- At ±∞: (q²u′)′ ≈ (2πλ)²q²u gives u ~ e^{±2πλ|q|}/|q|. Exactly one solution is L², so the endpoint is **limit point**.
- On C_c^∞(ℝ∖{±λ}) this gives deficiency (4,4), which matches phase 60, with 2 in the even sector.
- Since p·∂_q log|q−λ| → −2λ from both sides, the Lagrange form on D(W_max) is

  ω(f,g) = −2λ Σ_{e} s_e (a_e(f) b̄_e(g) − b_e(f) ā_e(g)),

  with s_e = +1 at inner sides and −1 at outer sides.

### 2.2 The right minimal operator is the Schwartz core (PROVED; corrects the phase-60 set-up)

Let W_S be the closure of W|S(ℝ).
- Schwartz functions have a_e = 0, and b continuous across ±λ.
- The boundary maps are graph-norm continuous. So the boundary image of D(W_S) is I = {a = 0, b_{λ−} = b_{λ+}, b_{−λ−} = b_{−λ+}}, which has dimension 2 and is ω-isotropic.
- Hence **W_S is symmetric but not essentially self-adjoint, with deficiency (2,2)**, and (1,1) in each parity sector.
- The reduced boundary space is I^ω/I ≅ ℂ⁴, with coordinates:
  - A_{±λ}: the common log coefficient (I^ω forces a_{e−} = a_{e+});
  - J_{±λ}: the jump b_{e+} − b_{e−}.
- On it, ω = −2λ Σ_{±λ}(A J̄ − J Ā) up to sign.
- Boundary triple: (ℂ², Γ₀ = (A_λ, A_{−λ}), Γ₁ = −2λ(J_λ, J_{−λ})).

### 2.3 Classification (PROVED)

- Self-adjoint extensions of W_S correspond to self-adjoint relations Θ in ℂ², i.e. to U(2).
- **Even sector:** there is a one-parameter circle B_t, with t ∈ ℝ∪{∞}, defined by J = tA.
- **The CCM extension (regular at q = λ on both sides) is B_∞**, i.e. A = 0: no log term, b free on each side, so the inside and outside are decoupled. This is A₀ = ker Γ₀.

**Theorem 2.3a (Fourier does not select B_CCM).**
- F preserves S and commutes with W_S and W_S*, so it acts on N_±(W_S).
- On the even sector, F is a real involution. Also, N₋ is the complex conjugate of N₊, because W is real and the kernel of F is real there. So F acts on the reduced even boundary space as ε·Id with ε = ±1.
- On the odd sector, F acts as μ·Id with μ = ±i (the same computation, using F̄ = F⁻¹ on odd functions).
- Hence **every** even (and every odd) extension commutes with F. The F-invariant extensions of W_S form the torus U(1)×U(1), namely the parity-preserving ones.
- So B_CCM is **not** the unique Fourier-invariant extension. The phase-60 dichotomy therefore resolves to the "family" branch.

**Theorem 2.3b (what does select it).**
- B_CCM = B_∞ is the unique extension of W_S that commutes with P_λ = 1_{[−λ,λ]}, i.e. that is decoupled.
- Proof: a separated Lagrangian L₋⊕L₊ must contain I ∋ (0,β,0,β). That forces L_± = {a = 0}.
- So CCM rigidity comes from **time-limiting, not from Fourier**.

### 2.4 Weyl function and Kreĭn formula (PROVED)

Even sector, reference A₀ = B_CCM:
- Let φ₋ be the even interior solution and φ₊ the L² exterior solution.
- Near λ, write φ_± = α_±(z) log|λ−q| + β_±(z) + ….
- Put m_±(z) = β_±/α_±.

Then:
- **M_λ(z) = −2λ (m₊(z) − m₋(z))**, a scalar Nevanlinna function (the coupling formula).
- Spec B_t = {E : M_λ(E) = −2λ t}, together with Kreĭn's resolvent formula (B_t − z)⁻¹ = (A₀ − z)⁻¹ + γ(z)(tΘ-normalised − M(z))⁻¹γ(z̄)*.
- The poles of M_λ are Spec A₀ = {interior prolate eigenvalues χ_n(λ) > 0} ∪ {exterior Sonin eigenvalues < 0}, which is CCM's zeta-like negative spectrum.
- The residues are −|Γ₁ψ_n|²/‖ψ_n‖² ≤ 0, so all Nevanlinna data are the boundary values b(ψ_n) of prolate and Sonin eigenfunctions.
- The eigenvalues of B_t interlace with Spec A₀.

### 2.5 Does any extension invariant touch O2601.1? **NO-GO (killer W3/F3; arithmetic-free, "row 8")**

**Proposition 2.5.** W, W_S, the family {B_t}, M_λ, the residues and the interlacing data depend only on (λ, 2π). They contain no Λ.

Consequences:
- Every such invariant takes the same value for ζ, deletion, M_m, Λ̃, DH and Beurling DMV. So it cannot be an individual Euler-product property. S4 fails, and the whole §4 table fires at once.
- It is not E1 either: it does not encode RH at all.
- The Weyl function's Nevanlinna data at "first contact" is also arithmetic-free, e.g. the λ at which an eigenvalue of B_∞ crosses 0, or M_λ(0) changing sign. The first contact of λ_A(T) is a Weil-form event, not a prolate event.

**Inserting arithmetic through the parameter (tested, dead).** The one-parameter family is "the exact locus of arithmetic input" only if t = t(λ; ζ). There are three options:
1. t is fixed by spectral matching of B_t to ζ data, i.e. zeros or the Sonin count N(T) of R162_2602b. That is zero-side / E1.
2. t is a linear functional of Λ. That is linear, so it fails O2601.1's nonlinearity.
3. t is any nonlinear scalar functional Φ(Λ). Then every invariant is g(λ, Φ(Λ)) with g arithmetic-free. All the content is in the scalar Φ, so this is a tautological transfer (W6-type).

Also, the prime part of the truncated Weil form is an infinite-rank nonlocal (shift) operator, not a boundary condition. So it cannot be absorbed into Θ.

**Status.** 1D boundary-triple residual: PROVED-TOOL, killer "W3;F3:all" for the O2601.1 question. Burnol's K_λ/Z_λ comparison was not done: it is recorded as a remark, and it is RH-neutral.

## 3. NG-D4 (Fourier anticommutation): **NO-GO (PROVED)**

**Statement (phase-28-four-fronts/02-front-B.md Prop. B.8, §5).** If Q(f̂,ĝ) = −Q(f,g), then F anticommutes with T₀. Then η(T₀) = 0, hence κ = 0.

**Theorem 3.1 (index obstruction).** Let K be any linear or antilinear bijection of the test domain D with Q(Kf,Kg) = −Q(f,g). Then n₊(Q|D) = n₋(Q|D).
Proof: K maps every Q-positive subspace injectively onto a Q-negative subspace, and conversely. ∎

**Corollary 3.2.**
1. On any window domain, n₊ = ∞, because modulated bumps e^{iξx}φ with ξ → ∞ carry an archimedean term ~ log ξ ‖φ‖² → +∞ on an orthogonal family. Also n₋ < ∞ there (N(T)+δ, R162_2602b). So **no anticommuting K exists on any window, for ζ or for any model**.
2. On the full line, anticommutation forces n₋ = ∞, i.e. infinitely many off-line zeros. So **the NG-D4 hypothesis is incompatible with RH**: the route would prove ¬RH if it worked. The η = 0 mechanism cannot give κ = 0.

**Theorem 3.3 (the actual identity).** The functional equation (Tate/Poisson: ℰ(f̂) has the Mellin transform of ℰ(f) at 1−s, and the zeros are symmetric) gives **Q(f̂,ĝ) = +Q(f,g)** on the even full-line class. So Q(f,g) + Q(f̂,ĝ) = 2Q(f,g): the "boundary terms" of §5 are exactly 2Q. The identity Q + Q∘F = 0 holds iff Q ≡ 0, and it fails for every f with Q(f,f) > 0 (e.g. any small-support f, where Weil positivity is proved). This is the MAP_1 note "J commutes", now made quantitative.

F2 fires: anticommutation is an orientation reversal, and the index pair is maximally unbalanced (∞ vs finite).

**Grid action.** In 1D, remove the NG-D4/I15 residual. New route R162_2702c: DEAD, killer "F2;index".

## 4. Net effect on the grid

**1D** loses both live residuals: NG-D4 is DEAD, and the boundary triple becomes a PROVED-TOOL that does not touch arithmetic. If no other OPEN route survives, 1D becomes ◩ or ■; the editor decides.

**4C** loses the doc-107 residual (DEAD, W2+E1).

**New open items:**
- O2702.1 (RH-neutral, optional): identify B_t for t ≠ ∞ with Burnol's quotient, or with the semilocal CCM operator at S = {∞}.
- O2702.2: none arithmetic.
