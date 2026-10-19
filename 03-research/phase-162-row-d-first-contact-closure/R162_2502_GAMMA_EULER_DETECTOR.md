# R162_2502 — Completing the Γ–Euler detector (grid 4D, ranking #2): **NO-GO (PROVED)**, with three exact structures

Note. Pure mathematics, no numerics. No parallel passes.
Cell: **4D** (Euler × spectrum). Nearest route: R161_068–070 (live residual of 4D). Also R161_071–074, R162_402, R162_1201,
R162_1401, R162_1603.
Walls named up front (grid §0 rule 2): the step has to evade W1 (E1), W3 (F3, weight blindness) and W7/Thm P (the
positivity lock). §3–§5 show it evades none of them.

**Labels.**
- Thm D (what the detector detects: two-sided equivalence C ≍ Gamma pole energy translated by ½log 2) PROVED. **New.**
- Thm K (open step (4.1) of R161_070 ⟺ injectivity of H_T at fixed T; ‖K_T‖ ≥ c/λ(T) along T ↑ T_*) PROVED. **New.** Restatement (E1).
- Prop A (the Euler algebra on the Gamma lattice is commutative and diagonal; every nonlinear Euler use stays inside it) PROVED. **New** (it extends Thm P of R162_1603 from scalars to operator algebras).
- Prop Col (the only non-diagonal part, the collar E_N, consists of the sub-window moments ρ⁺ of R162_1201; it is residual (d) of R162_1603) PROVED (identification).
Gate 1 OPEN. No label moves.

## 0. Corpus check

Grepped "Gamma–Euler", "detector", "C_N", "R*D_N R", "(4.1)", "K_delta", "stabilized", "translation by ½log 2",
"diagonal algebra" in phases 161–162 and the grid. What exists: R161_068 (energy (2.4), faithful); R161_069 (conditional
kernel lemma, corrected by 070); R161_070 (typed C_N, collar (2.1), identity (2.2), stabilisation (3.1), open comparison
(4.1)); R161_071 (parity balance (2.3)); R161_072 (exact recombination Q = −2c; coefficient substitution w ≥ 0);
R161_073–074 (stabilised matrix M = RS⁻¹R*, residual certificate). Not found: Thm D, Thm K, Prop A, the identification
of E_N with residual (d).

## 1. Falsifier lines first

The requested step: construct admissible primitive K and Q ≥ 0 with

  2 Re a_T(f,Kf) = ⟨f,C_N f⟩ + Q(f)    on the primitive space P_T,        (4.1) of R161_070

so that radicality kills the left side and faithfulness of C_N gives f = 0.

| model | detector available? | where (4.1) fails |
|---|---|---|
| **DH** | yes, on its own lattice a_m = 2m+3/2 (odd Gamma factor), with the Gamma pole energy as the weight (faithful by Müntz, same proof). Its Dirichlet weights −L′/L(2m+2) are signed, but faithfulness does not need them (Thm D, R161_072 §2) | DH has first contacts with x ≠ 0 (R162_102). By Thm K, (4.1) fails at T_*^DH. Any proof of (4.1) that uses only the detector's positivity and faithfulness also "proves" it for DH. So it must use what DH lacks, and C_N carries no such term (Prop A) |
| **deletion Λ1_{n≥5}** | yes: weights Σ_{n≥5}Λ(n)n^{−s_m} > 0, faithful (R161_072 with w_5 > 0) | has first contacts, so (4.1) is false there. The detector is identical in form |
| **Λχ₂** | the diagonal −L′/L(2m+1,χ) has, for all large m, the sign of χ(2)Λ(2) (the n = 2 term dominates). With χ(2) = −1, −C^χ is faithful | the sign flip is absorbed by K ↦ −K. The detector sees |D| only |
| **Beurling DMV** | yes: −ζ_B′/ζ_B(σ) > 0 for σ > 1 | Thm P holds verbatim. Zeros are off the line, so a proof of (4.1) that reads only the Euler scalars fails there |
| **two-atom Type I curve** s₂δ_{log2}+s₃δ_{log3} | yes: this is exactly R161_072's substitution with w₂ = s₂, w₃ = s₃ | at s₂ = s₂^c = 0.9997678 (2190) a Type I contact exists, so (4.1) fails. By Thm K, ‖K‖ → ∞ as s₂ ↑ s₂^c. A proof must therefore resolve the weights at the contact scale (W2, Theorem M) |

Conclusion before building. The detector exists and is faithful for every model in the table. It cannot be the
separating ingredient. Any separation has to come from K (the interior law), not from C_N.

## 2. What the detector detects (Thm D)

Notation (R161_070): a_m = 2m+½, s_m = 2m+1, b_m = √a_m e^{−a_m(T+δ)}, (Rf)_m = b_m K_f(a_m), c_m = −ζ′/ζ(s_m),
D = diag(c_m), C = R*DR, and D^Γ_{T,δ}(f) = Σ_m a_m e^{−2a_m(T+δ)}|K_f(a_m)|² (R161_068 (3.1)).

**Thm D.** Put κ₁ := 8c₁/log 2 (a finite constant). For every f ∈ L²(I),

  (log 2/√2)·D^Γ_{T,δ+½log2}(f) ≤ ⟨f,Cf⟩ ≤ κ₁·(log 2/√2)·D^Γ_{T,δ+½log2}(f).

The same holds for every C_N (N ≥ 2), with c_{m,N} in place of c_m and κ₁ replaced by 8c_{1,N}/log 2.

*Proof.* c_m·2^{s_m}/log 2 = 1 + Σ_{n≥3}(Λ(n)/log 2)(2/n)^{s_m}. Each term is positive and decreasing in m, so the ratio
lies in [1, κ₁] (maximum at m = 1). Then write 2^{−s_m} = 2^{−1/2}e^{−a_m log 2} and absorb e^{−a_m log2} into
e^{−2a_m(T+δ)} as δ ↦ δ + ½log 2. ∎

**Reading.** The Γ–Euler detector is, up to a bounded two-sided factor, the Gamma pole energy with the collar parameter
translated by ½log 2. That is the n = 2 term. The rest of the von Mangoldt comb only changes the constant. Hence:
- it detects **exactly the Gamma-lattice moments x_m = εK_F(a_m)**, i.e. by Müntz it detects f ≠ 0 on all of L²(I). It
  does not detect anything specific to first contact;
- its arithmetic content is a window translation T → T + ½log 2 plus a bounded multiplier. That is W7, which is
  why it passes the Type I curve and deletion unchanged;
- by R162_402 Thm 1.3(f), the same energy is Σ a_m e^{−2a_m(T+δ)}|G_+^0(−a_m)/ζ′(−2m)|². It measures the regularity of
  the logarithmic port H_+ at the trivial zeros, which is Gate 1 restated (R162_402 (1.1)).

## 3. What is proved and what is open

Proved (R161_068/070–074, audited here against R161_070's own definitions of R, D_N, E_N, P, Π):
1. C_N = R*D_N R is positive, trace class and injective. C_N → C in trace norm (R161_070 §1).
2. Exact collar R B_N = D_N R − E_N and Hermitian identity (2.2); stabilisation (3.1) (R161_070 §2–3).
3. Parity balance 0 = 2c + Q (R161_071), which recombines exactly to Q = −2c with no extra constraint (R161_072 §1).
4. Faithfulness for any w ≥ 0 with some w_n > 0 (R161_072 §2).
5. The stabilised matrix M = RS⁻¹R* with ker H ≅ ker(I−M) (R161_073), and its residual certificate (R161_074).

**The open step left by R161_070** is (4.1): an admissible primitive K and a form Q ≥ 0 with 2Re a_T(f,Kf) − ⟨f,C_N f⟩ =
Q(f) ≥ 0. Equivalently, a **one-sided inequality**

  2 Re a_T(f,Kf) ≥ ⟨f,C_N f⟩    for all f ∈ P_T ∩ form domain,            (4.1′)

with K source-defined (no H_T⁻¹).

## 4. Attempt at the first contact, and Thm K

The natural source-defined candidates are all exhausted:
- K = ΠG_L (R161_068 §4): it inserts an extra A_∞, so the pairing is not the energy (withdrawn in 068).
- K = ΠS_L, S_L = G_L + JG_LJ (R161_071): exact balance with Q = −2c (R161_072). (4.1′) would then say −2c ≥ c, i.e. c = 0. That is circular.
- K = S⁻¹R*(…) (R161_073): legitimate, but (4.1′) becomes λ_max(M) < 1, the same statement.

The reason is structural.

**Thm K.** Let H = H_T ≥ 0 be the primitive compressed Weil operator (selfadjoint, compact resolvent, as imported in
R161_073), and let C be any faithful positive bounded form on P_T (C_N, C, C^w for any admissible weights w, or D^Γ).
- (i) There is a bounded K: P_T → Dom H satisfying (4.1′) **iff** ker H = {0}.
- (ii) If (4.1′) holds with some bounded K, then for every eigenvector Hψ = λψ, ‖ψ‖ = 1:

  λ ≥ ⟨ψ,Cψ⟩ / (2‖K‖).

- (iii) Consequently, along a first contact T ↑ T_* with bottom eigenvectors ψ_T → F ≠ 0, any family K_T satisfying (4.1′)
  obeys ‖K_T‖ ≥ ⟨ψ_T,Cψ_T⟩/(2λ(T)) → ∞, at the rate 1/λ(T). If λ(T) is the bottom of the primitive form, Theorem M
  (159 G2_B6_R2) makes this doubly exponential in T.

*Proof.* (i) ⟸: ker H = 0 and compact resolvent give H ≥ α > 0, so K := ½H⁻¹C is bounded into Dom H and
2Re⟨Hf,Kf⟩ = ⟨f,Cf⟩ (Q = 0). ⟹: if Hf = 0 then a_T(f,Kf) = ⟨Hf,Kf⟩ = 0, so ⟨f,Cf⟩ ≤ 0 and faithfulness gives f = 0.
(ii) 2Re a_T(ψ,Kψ) = 2λRe⟨ψ,Kψ⟩ ≤ 2λ‖K‖, then (4.1′). (iii) Continuity of ψ ↦ ⟨ψ,Cψ⟩ (C is bounded) and
⟨F,CF⟩ > 0. ∎

**Reading.**
- (i): at a fixed window the open step **is** Gate 1 (E1). Which faithful C is used does not matter, and neither does
  whether the weights are Λ, deletion, Beurling or the Type I atoms. This is the operator form of R161_072 §2.
- (ii)–(iii): "division-free, source-defined" cannot be made uniform in T. A uniform bound on K_T is a lower bound
  on λ(T), which is the rate law (R162_1603 Thm Q; R162_1501 #13) and runs into W2/M. The non-uniform version is (i).
- R161_069's lemma survives as (i) ⟹. R161_070's correction is right that the relevant kernel is ker H_T and not
  ker A_∞. With that correction, (4.1) is not a no-go. It is an equivalence.

## 5. Nonlinear Euler use and the positivity lock (Prop A)

The spec asks for the Euler product before regularisation (S7) and a nonlinear use (S2). Take the finite Euler data
before any continuation, i.e. the multipliers 𝔇_α(s_m) = Σ_{n≤N} α(n)n^{−s_m} for α ∈ {1, μ, Λ, log} and their products
(Dirichlet convolutions truncated at N·N′).

**Prop A.**
- (a) On the observation side, every such multiplier acts as a diagonal operator in the lattice coordinates x_m: R L^α_N ≡ D^α_N R modulo the collar E^α_N (R161_070 (2.1) with w = α).
- (b) The diagonal parts form a commutative algebra 𝔈 ⊂ ℓ^∞(ℕ). Dirichlet convolution becomes pointwise product, so Λ*1 = log becomes D^Λ D^1 = D^{log} (R162_1603 Thm P; R162_1401 Thm 4).
- (c) For m ≥ 1 every element built from Λ, 1, μ, log with nonnegative coefficients and products is a positive diagonal sequence (Thm P). Any faithful positive form R*ΦR with Φ ∈ 𝔈, Φ > 0, satisfies Thm D-type bounds against D^Γ at a translated δ. So Thm K(i) applies to it verbatim.
- (d) Any nonlinear function g(Φ) of Euler data with g(Φ) > 0 stays in 𝔈 and is covered by (c).

*Proof.* (a) R161_070 §2 and R161_072 §2 (coefficient-blind change of variables). (b) Absolute convergence at s_m ≥ 3.
(c) Thm P and positivity of n^{−s_m}. (d) Functional calculus on ℓ^∞. ∎

**Reading.** On the Gamma lattice, "Euler before regularisation, used nonlinearly" produces only positive diagonal
multipliers. That is the positivity lock (Thm P) promoted to the whole algebra. The only place Λ*1 = log can meet the
secular (Jordan) term is the Tate ray a₀ = ½, which primitivity removes (R162_1401 Thm 3). So the detector satisfies S7
formally but fails S2 and S4 in substance.

## 6. Where the non-diagonal content lives (Prop Col)

The only non-diagonal operators in the detector's calculus are the collar E_N and the backward observation R_L B*
(R161_071 (3.1)).

**Prop Col.** For 2 ≤ n < e^{2T}, the n-th summand of (E_N f)_m is b_mΛ(n)n^{−s_m}·ρ_{n,m}(f). Here ρ_{n,m} is the collar
moment of f over the sub-window of length log n at the edge. By parity it equals ρ^±_{n,m} of R162_1201 Thm 2.1. The
backward observation (R161_071 (3.1)) is Λ(n)n^{a_m−1/2} times the complementary sub-window moment. These are exactly
family (d) of R162_1603 Thm X. At composite n their Λ-specific coefficient is (Λ*1 − log)(n) = 0 (R162_406).

*Proof.* Compare R161_070 §2 with R162_1201 (S_m) term by term, using K_{Jf}(a) = K_f(−a) and x_m = εK_F(a_m). ∎

So the Γ–Euler detector adds **no residual of its own**. Its surviving content is the sign of the sub-window moments,
which is already the live residual of R162_1603.

## 7. Classification of the open step (the three options asked)

- (i) **Restatement (E1): YES**, by Thm K(i). At fixed T, (4.1) ⟺ ker H_T = {0}.
- (ii) **Killed by the positivity lock: YES** for everything that reads the Euler data (Prop A, Thm D). The Euler scalars
  on the lattice are positive diagonal multipliers, and replacing them by any w ≥ 0, by Beurling, or by the Type I atoms
  changes nothing.
- (iii) **Genuinely new: NO.** The only non-diagonal content is the collar, and that is residual (d) of R162_1603
  (Prop Col). A uniform-in-T version would be the rate law under Theorem M (Thm K(iii)).

## 8. F1, F2, M

- **F1.** λ = 0 enters only through ker H (Thm K(i)). For T < T_*, (4.1′) holds with K = ½H_T⁻¹C and ‖K‖ ≍ 1/λ(T), so it
  is not a non-perturbative use (S1): it is the λ-shift of R162_1201 Thm 5.1(i). Not passed.
- **F2.** C is a positive square (orientation-blind). The (PC) orientation never appears. Not a W4 death, but not a sign
  source either. Not passed.
- **F3.** Failed: Thm D and Prop A are weight-blind (DH on its own lattice, deletion, κ, Beurling, Type I, |Λχ₂|).
- **F4.** Every identity is exact at finite N, L. C_N → C holds in trace norm. The proof dies at Thm K and Prop A, not
  at a linear limit.
- **M.** Thm K(iii): a uniform source-defined K is a margin λ(T) ≥ c/‖K‖, forbidden by Theorem M. At a single window
  it is a certificate (R161_074 (3)). That fails S12, and per the the rule it is not a closing route.

## 9. Verdict

**NO-GO (PROVED)** for the Γ–Euler detector as a closing mechanism.
- It detects exactly the Gamma-lattice moments. Up to constants it is the Gamma pole energy translated by ½log 2 (Thm D).
- R161_070's open comparison (4.1) is Gate 1 at fixed T (E1) and a doubly-exponential rate law uniformly in T (M) (Thm K).
- Its Euler content is locked (Prop A ⊇ Thm P).
- Its only non-diagonal content is residual (d) of R162_1603 (Prop Col).

Cell 4D: the residual "R161_068–070 detector, primitive Weil comparison open" should be **removed** (superseded by this
file). What remains of it is transferred to the R162_1603 residual (sign of the sub-window moments of a 2-node radical
vector, which must be coupled to a term that fails for deletion). Ranking #2 falls. 4D keeps only the exclusion
conjecture (21/01-02).

Files edited: this file; grid/R162_2300_part8.jsonl (append).
