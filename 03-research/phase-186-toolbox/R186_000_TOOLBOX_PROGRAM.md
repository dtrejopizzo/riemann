# R186_000 — Toolbox program for row D

Phase 186. No new mathematics except where marked. No numerics.
Labels: PROVED / PROVED-CITED / CITED / CONDITIONAL[on X] / OPEN / NO-GO / NUMERICAL / ARGUED / PROGRAM.

A route
is only declared closed if there is a **proof of impossibility within a declared class of methods** or an
**explicit falsifier**. We start from the premise that the positivity is true, and the work consists in building the
tools that prove it. The equivalences that appear below are **equivalences between forms of D**: they say that
two targets are the same target and are used to choose the most constructive form.

Sources: ROW-D-REDUCED-STATEMENT (§1–§4); CROSSWORD-TO-D (§1.2, §2, §3.1–3.3, Addendum);
Paper 47 `main.tex` (thm:Z, thm:Zexh, prop:finite, prop:uniform, prop:band, prop:align, thm:P, thm:index, thm:arena,
thm:parityschur, prop:polarcap, thm:KEP3, thm:finZ, thm:margin, cor:margin2, cor:mono, lem:monoT); Paper 48
§sec:spec (S1–S12); R183_024, R183_028, R183_033; R185_005 (theorem BR), R185_006, R185_008; R169_101; G2_B5_R1
(phase 159, canonical window system); R162_2701 (Tate system); grid R162_2300 §3, §5, §7.

---

## 0. Summary

1. **25 forms of D** are inventoried (§1). For each one we give the exact statement, the objects it needs, the
 PROVED tools available, the **method walls** that apply to it (always a class of methods with its
 falsifier, never a label) and the missing tool.
2. The ranking is by constructive tractability (§2): available objects, proved tools, and whether the first lemma is
 decidable.
 - **(a) Finite window forms:** D-cert, D-conv (v_T ∈ 𝒱_T), D-iner (N ≡ 0) and D-Kreĭn. At fixed T they are decidable.
 The work lies in uniformity over T, and what shape a uniform tool must have is specified (§2.1).
 - **(b) Operator forms:** CCM's semilocal prolate and the canonical window system. An object remains to be built.
 - **(c) Arithmetic forms:** inequalities over Λ. A theorem of analytic number theory is missing.
3. **Top-3** (§3):
 - **TB-1, the jump law at the thresholds:** the window Kreĭn/de Branges system, with an exact invariant in v.
 - **TB-2, the semilocal prolate P_S with exact commutation:** explicit Jacobi and a spectral identity for Π_S.
 - **TB-3, the two-scale bilinear inequality over Λ:** O166.802.1 at degree 2.
4. §4 states honestly what is new and what reopens a closed route, and what each reopening must add.

---

## 1. Inventory of forms of D

Conventions: v_n = 2Λ(n)/√n; W_T is the full form (eq:W of P47); 𝔞_T is the primitive form on 𝒫_T;
λ^W_T and λ^A_T are their minima; N(T) = n₋(W_T | C_c^∞ ∩ 𝒫_T).

"Method walls" lists only statements of the type **"every proof in class 𝒞 fails, because falsifier X satisfies
𝒞 and violates D"**, with its reference. "Missing" is the tool whose construction would turn the form into a theorem.

### 1.1 Window forms (finite at fixed T)

**D-W (full form).** ∀T: W_T ≥ 0 on 𝒟_T.
- Objects: m (Γ), {Λ(n) : n < e^{2T}}, the polar block.
- Tools: positivity PROVED for T ≤ ½log5 (thm:C, thm:log5A, thm:log5W); CITED for (½log2, 0.8] (Zhu); λ^W
 continuous (lem:contA) and non-increasing (lem:monoT); band and alignment structure (prop:band, prop:align).
- Walls:
 - I2/Theorem M: there is no uniform margin, λ^W ≤ exp(−e^{(2−ε)T}).
 - O3 (phase 157): a single weight change of size e^{−14.4T} flips the sign, so no estimate acts.
 - I3/W3: no class property suffices (deletion, finmod, DH, M_m).
 - thm:arena: no finite truncation decides the even Schur complement.
- Missing: a mechanism uniform in T, with no margin, that uses exact values of Λ (§2.1).

**D-A (primitive form).** ∀T: λ^A_T ≥ 0. D-W ⟺ D-A only jointly; window-by-window the converse is not structural
(cor:convfail).
- Tools: thm:C (½log3, 8.86·10⁻⁵); thm:parityschur; prop:polarcap (λ^W > 0 ⟺ λ^A > 0 ∧ 𝔊_T ≻ 0).
- Walls: those of D-W, plus cor:convfail (the primitive → full step needs the exact value Λ(2)).
- Missing: the same as D-W, plus control of the 2×2 polar capacity 𝔊_T.

**D-cert (flat-top certificate; thm:Z, thm:Zexh).** ∀T there exists w ∈ 𝒲^reg with inf_τ f_w(τ) ≥ 0, where f_w is the
right-hand side of the explicit formula at h_τ = w cos(τ·). By thm:Zexh, sup_w inf_τ f_w = λ^W_T exactly.
- Objects: one weight w per window. It is an elementary function of Γ and of the primes in the window.
- Tools: strong duality D1/O (no scope, thm:O); explicit certificates written out up to ½log5.
- Walls:
 - thm:finZ: no finite set of ordinates sustains a certificate. This forbids the class "certificate built from
 finitely many spectral data", not the form.
 - thm:O: the supremum is not attained, so there is no optimal certificate to propagate.
 - Theorem M: the value of the certificate tends to 0.
- Missing: a **family** w_T defined by a formula uniform in T (not by LP) with f_{w_T} ≥ 0 provable.

**D-conv (convex; prop:finite, prop:uniform).** ∀T: v_T(Λ) = (v_n)_{n<e^{2T}} ∈ 𝒱_T, where
𝒱_T = ⋂_F {v : Σ v_n c_F(log n) ≤ C₀ + Lev(c_F)} is convex, closed, and defined only by Γ.
- Objects: a convex set of dimension ⌈e^{2T}⌉ − 2 and an arithmetic point.
- Tools:
 - finiteness (at fixed T the condition is finite);
 - the projection of 𝒱_{T'} onto the first coordinates is contained in 𝒱_T (this is lem:monoT read on 𝒱; PROVED,
 same proof);
 - 0 ∉ 𝒱_T for T ≥ 0.60 (prop:finite(iii));
 - prop:uniform(b): no initial segment decides.
- Walls:
 - Theorem M: v_T(Λ) is at distance ≤ exp(−e^{(2−ε)T}) from ∂𝒱_T in the λ metric, so there is no ball around it.
 - prop:uniform(b): the class "information from an initial segment" does not decide, by falsifiers Λ1_{n<N} and Λ + c1_N.
 - R184_005 N2: the Diophantine route of the hint is NO-GO in its counting form.
- Missing: (i) a closed description of 𝒱_T or of its inverse limit 𝒱_∞ (§2.1, A1–A3); (ii) a theorem locating the
 arithmetic point. The concrete computation is in R186_001.

**D-iner (inertia; R184_004 Prop 2, R162_2602 Thm 6).** N(T) ≡ 0.
- Tools:
 - Lemma 1.1(b) of R183_031, now PROVED (R185_008 §3): sup_T N(T) < ∞ implies only finitely many failures.
 - The gap requirement (R183_031 Thm 1, PROVED).
 - thm:index (exact archimedean n₋ 0/1/2 for T ≤ 0.90) and thm:P (n₋ ≤ 5/7/8).
- Walls:
 - I7: inertia arithmetic over W = A_∞ − C_ε − ΣB_p and any property of the B_p. Falsifier M_m, with N ≡ 2m.
 - "Monotone spectral flow" and "finite-rank compressions" are closed (N5, D.53).
- Missing: something beyond pure inertia. For example, an exact eigenvalue-crossing law that uses Λ (the inertia
 version of TB-1).

**D-lim (limiting margin; cor:margin2).** lim_T λ^A_T ≥ 0 (the limit exists in [−∞, 0]).
- Tools: existence of the limit (PROVED).
- Walls: Theorem M (the limit is 0 or negative; there is no positive margin).
- Missing: a lower bound λ^A_T ≥ −ε(T) with ε(T) → 0, proved with no margin. By monotonicity (lem:monoT) it is the
 same difficulty as D-A.

**D-Q (R184_015 Thm 2(ii)).** W_T ≥ −e^{o(T)} on 𝒫_T for T ≫ 1, which is equivalent to D-A by the detection law.
- Interest: it is a **weak** bound, with subexponential growth allowed. It is the only window form in which a
 large error is admissible.
- Walls: I8. If the error Δ_T is defined from the local source, the bound does not distinguish ζ from M_m (explicit
 falsifier). If it is defined as W^X − Pos_S, the bound is D-Q itself (circular).
- Missing: a third definition of Δ_T that is neither of those two. I8 asserts there is none **within the
 source/form dichotomy**. A Δ_T defined by an operator (TB-2) is outside that dichotomy if it is not a norm
 bound (§3, TB-2).

**D-Kreĭn (thm:KEP3).** ∀T, KEP(T) is indeterminate (equivalently solvable).
- Tools: thm:KEP3(a) gives λ^W > 0 ⟹ indeterminate ⟹ λ^W ≥ 0; the window form is de Branges (G2_B5_R1 Lemma 1);
 the shifted chain is unconditional on [0, T₁] (G2_B5_R1 Cor B′).
- Walls: G2_B5_R1(iii), PROVED. The dynamics g ↦ H is universal across combs, so "H ≥ 0 for all time" does not
 follow from the dynamics; it must come from v. By thm:finmod/cor:void it cannot be a class property. The
 sensitivity near the blow-up is ≳ e^{14.4T}, which rules out perturbative and Lyapunov arguments.
- Missing: TB-1.

**D-canon (canonical window system, G2_B5_R1 Thm B).** The Hamiltonian H(t) ≥ 0 of the window de Branges chain
exists for all t (T* = ∞).
- Tools: existence up to T* (PROVED); Thm C(3): at T* the extensions are atomic in Z_R(F̂*).
- Walls: those of D-Kreĭn.
- Missing: TB-1, a global existence theorem for the non-linear Gelfand–Levitan equation with arithmetic data.

### 1.2 Witness forms (hypothetical first contact)

**D-CL, D-cell, D-TC.** These are, respectively, CL (R163_401 Prop 4.0); (★_cell), i.e. P_j > N_j in every cell
containing an off-line ordinate in the witness; and (TC), the absence of poles of C_{T_c} − iG²𝒯_X in
−½ < Im x < 0.
- Objects: the witness F of prop:witness (P48), real-rooted, with node density T_c/π.
- Tools: prop:witness; Thm Q (nodal quadrature); the R169 chain §1, steps 1–4 (PROVED given (Dom_θ)).
- Walls:
 - I10: critical interlacing is not enough (falsifier without πρz).
 - I12: nodal jets do not read Re G(t_q)².
 - I14: discarding one term does not work.
 - I15: there is no descent.
 - I11: anything that uses only the zero side holds for M_m.
- Missing: an inequality over Λ that excludes a quartet in the witness. This is TB-3.

**D-loc ({P_loc(kL, T)}, R163_601).** The family of local positivities in cells. The cell decomposition is exact.
- Walls: those of D-cell.
- Missing: TB-3 cell by cell.

**D-desc (SUPPORT-DESCENT §2).** "(2) holds on every first-contact vector."
- Walls: I15 (lem:monoT makes the descent's consequent impossible).
- Missing: no constructive tool identified. It remains a verification form, not a construction one.

**D-WS (𝓘_X ∀X, R169).** For every F in the image of the selector and every (γ, δ) ∈ Γ_S(F), Re 𝒮 < B.
- Tools: at fixed X it is a finite computation, because the tail is the Eratosthenes sieve of the window
 (R169_091). The chain up to D is PROVED given (Dom_θ) and (P_gap).
- Walls: I6 (W-sieve, falsifier b_θ); I13 (linear or power-family inequalities: falsifier by circularity);
 R184_016 (with the first-contact selector, A1 is D-cell itself).
- Missing: TB-3.

### 1.3 Spectral and operator forms

**D-Son (C_T, R183_024 §2.5).** I_S ∧ N_T. I_S (the semilocal identity E_S = Son_S − ∫c_h ε_S) is **PROVED**
(R183_029 + 025). N_T is the inertia R'_{S,T} ≥ −b|v⟩⟨v| + c(I − |v⟩⟨v|).
- C_T ⟹ D_T on ker ℓ (PROVED). C_T is strictly stronger than D_T.
- Walls:
 - Szegő falsifier (CONDITIONAL[on ε_S ∈ L¹, Landau–Widom]): if r_S < 0 on a set of positive measure, n₋ ~ cT, so
 C_T is false as a target. It is a falsifier of the **conjecture**, not of D.
 - R183_028 §1.2: the trace of the full Sonin has n₋(R) = ∞.
 - R183_028 §2: (L-Son) with uniform η is false.
- Missing: weaken N_T to a form the Szegő falsifier does not touch (TB-2, step P3).

**D-pro (semilocal prolate operator; CCM 2310.18423, CM 2022).** CCM's stated strategy: compare the trace
of the semilocal prolate with the Weil functional.
- Objects that exist: S_λ(X_S) ≅ S_λ(ℝ) (CCM Thm 4.6, CITED); the prolate UV spectrum (CM 2022, CITED), whose
 counting law matches that of the ordinates.
- Objects that are **missing**: the semilocal prolate operator itself (CCM do not give its Jacobi coefficients) and
 an identity trace = form.
- Corpus tools:
 - scaling law Λ (R183_029 Thm A, PROVED);
 - "prolates are not the obstacle" (‖Y_pro‖₁ ≤ 8/p);
 - form in the ξ metric with no cross terms (R183_030);
 - thm:P (Ky Fan ceiling in the Legendre basis, with explicit spherical Bessel formulas).
- Walls:
 - R185_008 §2.3, W11-sharp: within 𝔐_mult (multiplier + bounded inertia) the positive part has limiting density
 supported on the ordinates.
 - I8 (source/form dichotomy) for norm bounds.
- Outside the walls: class **(ρ-a)** of R185_008 §2.4, with P_T ≥ 0 non-diagonal in frequency, is OPEN and is
 exactly where a prolate projection lives.
- Missing: TB-2.

**D-HP (Hilbert–Pólya).** A self-adjoint operator whose spectrum is that of the ordinates.
- Walls: R158 (OT-5′: a positive form must be given before the spectrum); W10 (neither MW-5 nor h⁰); 18 published
 frameworks fail the object test (R158).
- Missing: an object. D-pro is the most advanced concrete candidate.

**D-dB (global de Branges, Lagarias/Herglotz, P48 W1).** Φ(s) is the Poisson factor for 2Re ξ′/ξ, and E is
Hermite–Biehler.
- Tools: the window chain (D-canon) is its local version.
- Walls: those of D-Kreĭn. Also, the de Branges–Conrey–Li counterexample to their positivity conjecture forbids the
 class "positivity of the de Branges structure of ξ via the de Branges condition" (CITED from memory; verify).
- Missing: TB-1.

**D-Hodge (P46 §5, the Hodge index in the adelic square).**
- Walls: W9 (T1/T2/T5); W10 (no h⁰ with the three properties; falsifier Ξ_a); the frame-defect theorem
 (P46 Thm 19.25 and Cor 19.25b).
- Missing: a carrier with h⁰. Classified as the most distant.

**D-qE (q_E = 0, the canonical exchange, R163_001).**
- Tools: the faithful defect D_test (PROVED, continuous).
- Walls: those of Beurling (I18).
- Missing: a proof that the Frullani current q_E vanishes for ζ. No candidate.

**D-Li (Li coefficients).** λ_n ≥ 0 ∀n.
- Tools: exponential mode of Li (105_02); the Li kernel is outside the flat-top class (phase 155, round 4).
- Walls: the same as D-W, because λ_n is a Weil form with a concrete test. No specific wall recorded.
- Missing: a proof giving λ_n ≥ 0 uniformly in n with no margin (λ_n grows, but its arithmetic part oscillates). No
 better than D-cert.

**D-NB (Nyman–Beurling–Báez-Duarte).** d_N → 0.
- Walls: no specific registered method theorem. It is an L² approximation form, with no window structure in the
 corpus.
- Missing: a bound on d_N with the rate (log N)^{−1/2}, which is Burnol's lower-form computation. No corpus tool.

### 1.4 Arithmetic forms

**D-ψ (P46 W4 + thm:Z).** ψ(x) − x ≪ x^{½+ε}. This is an equivalence between forms of D, recorded in
ROW-D-REDUCED §1.
- Walls:
 - I6: upper sieve, large sieve and uniform BV hold in Beurling DMV/Zhang (falsifier).
 - I13: a single linear inequality or a power family is circular.
 - §3.3 table of the crossword: no known theorem satisfies (α)–(θ).
- Missing: TB-3.

**D-CB (C_B ∧ L8, R184_004).**
- Walls: I7 for C_B (inertia; falsifier M_m). For L8, nothing forbids it. Its strength is of Lindelöf type.
- Missing: two tools, O2601.1 (an individual Euler property) and L8. No candidate.

**D-BF (Beurling frontier).** BF^disc_{θ₀} with θ₀ ∈ (0, ⅓] implies D.
- Walls: Thm BFdisc (it is false for θ₀ > ⅓); prop:analyticnogo (falsifier ζ_θ); B4 (integrality mod 1 must be
 used).
- It is strictly stronger than D.

**D-L*comp (R184_014).** Pure Beurling theory and does not imply D. Listed only as a side tool.

### 1.5 Compact table

| form | decidable at fixed T | complete objects | relevant PROVED tools | hardest method wall | missing |
|---|---|---|---|---|---|
| D-W / D-A | yes | yes | windows ≤ ½log5, continuity, monotonicity, band | Theorem M + O3 | exact uniform mechanism |
| D-cert | yes (LP) | yes | thm:Z, Zexh, D1 | finZ, thm:O | uniform formula w_T |
| D-conv | yes | yes | prop:finite, monotone projection | Theorem M | geometry of 𝒱_∞ + locating v(Λ) |
| D-iner | yes | yes | Lemma 1.1(b), thm:index, thm:P | I7 | exact crossing law |
| D-Kreĭn / D-canon | yes | yes (up to T*) | G2_B5_R1 Thm B, C | comb universality | exact invariant in v (TB-1) |
| D-Q | no (asymptotic) | yes | detection law | I8 | Δ_T outside source/form |
| D-Son | yes | I_S yes, N_T no | I_S, scaling law | Szegő (of C_T) | weakened N_T |
| D-pro / D-HP | — | **no** | Thm 4.6 CCM, thm:P | W11-sharp in 𝔐_mult | the operator (TB-2) |
| D-cell / D-WS | yes (fixed X) | hypothetical witness | R169 chain | I6, I13 | non-linear inequality (TB-3) |
| D-ψ | no | yes | — | I6, I13 | TB-3 |
| D-CB | no | yes | Lemma 1.1(b) | I7 | O2601.1, L8 |
| D-Hodge | — | no | T1/T2/T5 | W10 | h⁰ |

---

## 2. Ranking by constructive tractability

### 2.1 (a) Finite window forms: D-conv, D-cert, D-iner, D-Kreĭn

**What they share.** At fixed T, each is a finite, decidable statement about {Λ(n) : n < e^{2T}} and about m. It
has been decided for T ≤ ½log5. Moreover, R185_006 reduces T ≤ ½log3 to a problem of dimension ≈ 18 with exact
symbol θ = m − √2 log2 cos(s log2). All the difficulty lies in the ∀T quantifier.

**What the uniform tool cannot be (PROVED walls, with their class).**
1. **A margin** (Theorem M, cor:margin2(i)): no bound λ_T ≥ c(T) with c(T) ≥ exp(−e^{(2−ε)T}). O3 adds that no
 estimate of the weights with error ≥ e^{−14.4T} acts within window T.
2. **An ascending scalar induction.** cor:mono/lem:monoT give that λ_T does not increase, so an ascending induction
 would have to *create* positivity. R169_101 closed:
 - (i) the step W_T ≥ 0 ⟹ W_{T+Δ} ≥ 0 as an inequality with polynomial remainders in X: dies by Theorem M;
 - (ii) the Eratosthenes window → tail link used as an exact identity: it is equivalent to "the integers are
 exactly ℕ" (Prop 5), has no class of falsifiers over which it is a law, and at fixed (T, Δ) reduces to a
 finite certificate.
3. **A class property of the weights** (thm:finmod, cor:void, G2_B5_R1(iii)): the dynamics in T is the same for
 any comb.
4. **Pure inertia** (I7) and **monotone spectral flow** (N5, D.53).
5. **Finite truncation** of the even Schur complement (thm:arena).

**What is not closed (the shape the tool must have).**
- (R1) **A recursion in T with an exactly propagated infinite-dimensional state.** The state is not λ_T: it is a
 complete object, such as the de Branges function E_T, the Kreĭn coefficient A(t) or the transfer matrix M_T. The
 step between thresholds is explicit and depends only on Γ. The jump at T_n = ½log n is an exact transformation
 depending on v_n **and on the state**. R169_101 closed the scalar recursion and the Eratosthenes identity, not
 this one. G2_B5_R1 built the state and proved the dynamics is universal across combs, but did **not** prove that
 no exact invariant in v exists. It left open, as HEURISTIC, the question of global existence for the non-linear
 Gelfand–Levitan equation.
- (R2) **A closed qualitative invariant, stable under the jump**, which is the opposite of a margin. An example
 shape: "the state belongs to a cone 𝒦_Euler defined by an Euler-type factorization" (TB-1). It must be a closed
 condition that the jump preserves **exactly**, not "with slack". The e^{14.4T} sensitivity of O3 does not
 contradict this: O3 says that a change of v moves λ away from 0, not that an exact invariant in the true v is
 impossible.
- (R3) **A limit object**: 𝒱_∞ := lim← 𝒱_T ⊂ ℝ^ℕ (product topology). It is convex, closed, and defined only by Γ.
 By the monotone projection, D ⟺ v(Λ) ∈ 𝒱_∞, and uniformity in T is absorbed into the geometry of 𝒱_∞.
 - (A1, PROVED from Bochner–Schwartz, sketch) v ∈ 𝒱_∞ ⟺ the even distribution
 D_v := (Γ-part) − ½Σ v_n(δ_{log n} + δ_{−log n}) + polar is of positive type on 𝒫, i.e. D_v = μ̂_v with
 μ_v ≥ 0 on ℝ. μ_v is called the "spectral measure of v".
 - (A2, consequence of Theorem M; ARGUED) v(Λ) lies on the boundary of 𝒱_∞ in the λ sense.
 - (A3, PROGRAM) Describe the face of 𝒱_∞ formed by v whose μ_v is **discrete with integer masses**, i.e.
 Fourier crystals with an archimedean background (Lev–Olevskii, Kurasov–Sarnak, Olevskii–Ulanovskii, CITED from
 memory). For the comb of Λ, the explicit formula gives μ_{v(Λ)} = Σ δ_{γ_ρ} with γ_ρ ∈ ℂ and integer masses. D
 says that measure sits on ℝ. The tool would be a **classification theorem**: every discrete integer measure of
 polynomial growth whose transform agrees away from 0 with (Γ-part) − (comb supported on log ℕ with weights ≥
 0) is a measure on ℝ.
 - Wall to dodge in A3: Thm R (R164_401, PROVED) already gives "self-dual + gap + sign ⟹ comb", and the
 falsifier classes (DH, Epstein) have integer, discrete μ with atoms off ℝ. So A3 must use the integrality of
 the log ℕ support together with Λ(p^k) = log p (requirement (θ) of the crossword), not discreteness alone.

**Ranking within (a).** D-Kreĭn/D-canon with R1 + R2 (TB-1) comes first, because it has the complete, proven object
and the first lemma is decidable. D-conv with R3/A3 comes second within (a): the object is also complete, but the
classification theorem A3 has no obvious first lemma, and R186_001 develops it. D-cert and D-iner are subordinate: a
uniform w_T would be read off TB-1 (the reproducing kernel of the window space gives a certificate), and D-iner's
crossing law is the spectral version of TB-1's jump.

### 2.2 (b) Operator forms: D-pro, D-Son, D-HP

The object does not exist and the missing tool is **a construction**.

**Construction program (TB-2):**
- P0, the archimedean piece: the prolate W_λ = −∂(λ² − x²)∂ + (2πλx)² commutes with the time-band compression.
 Its spectrum and eigenfunctions are classical (Slepian), and the Legendre basis of thm:P is its λ → 0 limit.
- P1: write the Jacobi matrix of P_∞ in the Legendre basis of I_T. It is tridiagonal by the classical commutation,
 with explicit coefficients in j and c = Ts.
- P2: define the semilocal prolate P_S on L²(X_S), with X_S = ℝ × ∏_{p∈S} ℚ_p / ℤ_S^×, requiring [P_S, Π_S] = 0
 (Π_S the semilocal Sonin projection) and [P_S, I_T compression] = 0. This is the step CCM defer.
- P3: a spectral identity, Tr(ϑ(g) Π_S ϑ(g)*) = Σ_k φ_k(g) e_k(P_S) + (finite-rank remainder past threshold). This
 is the operator version of I_S (PROVED), with the remainder expressed via the negative part of P_S. Thus, N_T is
 replaced by a statement about **how many** negative eigenvalues P_S has in the window, rather than a norm bound.

Why the walls do not kill it:
- W11-sharp refers to frequency-diagonal multipliers, and P_S is not one: it lies in (ρ-a), which is OPEN.
- I8 refers to norm bounds on Δ_T; P3 is a counting identity.
- The Szegő falsifier kills the **bounded** inertia of C_T, but P3 allows n₋ ~ cT if it matches a count of P_S.
- I11 must be watched (M_m has the same local source as ζ): P3's count must depend on the exact values
 (Λ(p^k)) through P_S and not only through S. This is P2's mandatory falsifier proof.

Tractability: P0–P1 high (classical, decidable computation). P2 medium-low: it is an existence-and-uniqueness
problem for a differential-difference operator on an adelic space. P3 low.

### 2.3 (c) Arithmetic forms: D-ψ, D-WS, D-cell

The missing tool is a known-type analytic-number-theory theorem, with the shape required by §3.3 of the
crossword: a non-linear, individual property of Λ that controls a twisted sum at the witness frequency as an upper
bound with exponent strength, that couples with Γ, and that uses integrality.

The only square no PROVED method theorem covers is **O166.802.1**: non-linear, multiscale inequalities over Λ,
outside the single-test or power-family case of I13. Its minimal version is degree 2 with two scales,
window × tail (TB-3).

Tractability:
- The negative question, whether circularity extends to degree 2, is medium-high: it is the extension of
 R166_802 Thm 1/3, which is PROVED in two cases.
- The positive question is low, but it is the only arithmetic entry that is not currently forbidden.

### 2.4 Global ranking

| # | tool | form | objects | first decidable lemma | tractability |
|---|---|---|---|---|---|
| 1 | TB-1 jump law + exact invariant | D-Kreĭn/D-canon/D-iner | complete (G2_B5_R1) | yes: window (½log2, ½log3] | **medium** |
| 2 | TB-2 semilocal prolate | D-pro/D-Son | P_∞ yes, P_S no | yes: P1 (Jacobi of P_∞) | medium-low |
| 3 | TB-3 two-scale bilinear | D-WS/D-cell/D-ψ | complete | yes: the negative case at degree 2 | low (positive), medium-high (negative) |
| 4 | A3, classification of crystals with Γ background | D-conv | complete | not obvious | low (R186_001 explores it) |
| 5 | D-CB (O2601.1 + L8) | — | complete | no | very low |
| 6 | D-Hodge, generic D-HP, D-qE, D-NB, D-Li | — | missing, or no structure in the corpus | no | very low |

---

## 3. Specifications of the top-3

### TB-1 — Jump law at the thresholds (window Kreĭn system with exact invariant)

**Objects (PROVED, G2_B5_R1).** While λ^W > 0, the full form makes L²(I_T) a de Branges space ℋ(E_T), and the
spaces form an isometric chain in T. There is a canonical system J dY/dt = z H(t) Y, with H ≥ 0, up to T*. On
[0, T] the Hamiltonian depends on Γ and on {v_n : log n < 2T}.

**Tool TB-1a (the jump law). Statement to prove.** Let T_n = ½log n with Λ(n) ≠ 0, and let M(T) be the transfer
(monodromy) matrix of the system on [0, T]. Then:
- (i) on each interval (T_n, T_{n⁺}) between consecutive thresholds, M satisfies a Kreĭn equation
 dM/dT = 𝒜_Γ(T; M) M whose coefficient is computed from m and from the state, with no new primes;
- (ii) on crossing T_n, M(T_n⁺) = 𝒥_n(v_n; M(T_n⁻)) for an explicit jump map 𝒥_n.

𝒥_n must be given in closed form. Candidate: the Christoffel/Geronimus modification of the window space induced by
the atom −½v_n(δ_{log n} + δ_{−log n}) in the Kreĭn data, which is a finite-rank perturbation at the boundary of
the autocorrelation interval.

**Tool TB-1b (the invariant). Statement to prove.** There exists a closed cone 𝒦_Euler of states (pairs of
Hermite–Biehler functions, or Hamiltonians) with these properties:
- (α) M(T) ∈ 𝒦_Euler for T ≤ ½log2 (base case, PROVED by Yoshida/Bombieri and thm:C);
- (β) the archimedean flow of (i) preserves 𝒦_Euler;
- (γ) 𝒥_n preserves 𝒦_Euler **when v_n = 2Λ(n)/√n with Λ(p^k) = log p**, i.e. when the jumps arrive
 grouped by the local Euler factor of p;
- (δ) M ∈ 𝒦_Euler ⟹ H ≥ 0 on the next stretch.

Candidate for 𝒦_Euler: states whose Weyl function m_T factors, in the sense of transfer composition,
as (archimedean transfer) ∘ ∏_{p ≤ e^{2T}} (local Tate transfer T_p of R162_2701, with its boundary torsion
R183_028 §1.8). The Tate transfer satisfies T_p* σ₃ T_p = σ₃ on ℝ (PROVED) and H_S ≻ 0 for every chain (Thm P of
R162_2701, PROVED).

**Allowed inputs.**
- Γ (m, K, C₀) and the exact values Λ(p^k) = log p.
- Local Euler structure: all the p^k of the same p are treated as a single factor.
- The transfer identities of R162_2701 and R183_025.
- No zeros, margins or averages over T are used.

**Why no wall forbids it.**
- *Theorem M / O3:* TB-1b is a closed condition preserved exactly, not a bound with slack. It imposes no
 λ_T ≥ c(T) > 0, only T* = ∞.
- *R169_101 (closed induction):* the closure is for scalar steps over λ and for the Eratosthenes link as a
 counting identity (Prop 5). TB-1 propagates an infinite-dimensional state and does not use N(x).
- *G2_B5_R1(iii) (comb universality):* forbids the invariant coming from the dynamics alone. (γ) uses the exact
 value Λ(p^k) = log p and the Euler grouping, so it is not a class property of the comb. That is exactly what
 (iii) leaves open.
- *I7 (inertia):* TB-1 is not inertia arithmetic over B_p; the state is an entire function.
- *R162_2701 (NO-GO of the Tate system):* that system alone does not detect falsifiers, because H_S ≻ 0 holds for
 any chain. In TB-1 the Tate system enters only as the cone's **form**; the condition lies in the compatibility
 (β)+(γ) **with the archimedean flow**, which R162_2701 does not have. This is the crossword's requirement (δ):
 couple primes and Γ.
- *Falsifier obligations (I3/I11), to be verified:*
 - DH has no local factors, so (γ) does not apply (good).
 - Deletion and finmod break the Euler grouping or the value log p.
 - **M_m is the critical case**: it has the same primes and the same H_S (R162_2701 Thm I), and its difference
 lies in the non-atomic density β_m on the prime side. TB-1 separates it only if the archimedean flow (β) does
 not preserve 𝒦_Euler once β_m is added. That is the first mandatory falsifier proof.

**First lemma to attempt (L-TB1.0).** On the window (½log2, ½log3], R185_006 gives the exact identity W_T =
truncated Wiener–Hopf form with symbol θ(s) = m(s) − √2 log2 cos(s log2), with a single jump (n = 2). We ask:
- compute the Kreĭn coefficient A(t) for t ∈ [0, 2T] with data Γ plus an atom at log 2, in closed form or as the
 solution of an explicit Volterra equation;
- prove analytically that the system does not blow up before T = ½log3.

This turns the NUMERICAL residue of R185_006 (gap ≈ 10⁻³, effective dimension 18) into a proof with no
Rayleigh–Ritz, and proves that the jump formalism works. It is completed by **L-TB1.1**: write 𝒥_2 and check (γ)
for the Euler factor of p = 2, with the atoms log 2 and log 4, on the window (½log3, log2], where prop:align gives
the arc structure.

**Decidability.**
- L-TB1.0: **high**. It is a dimension-1 Volterra problem with explicit data, and positivity is already known from
 thm:C.
- TB-1a: medium. It is classical Kreĭn–de Branges theory with atoms.
- TB-1b: low. It is the invented tool, and its falsifier proof against M_m decides quickly whether it is worth
 pursuing: if (β) preserves 𝒦_Euler also with β_m, TB-1b is dead by an explicit falsifier.

### TB-2 — The semilocal prolate P_S with exact commutation

**Statement to prove (TB-2a, construction).** For every S = {∞} ∪ {p < e^{2T}} there exists a self-adjoint operator
P_S on L²(X_S), second-order in the archimedean variable and difference-type in the p-adic variables, such that:
- (i) [P_S, Π_S] = 0, with Π_S the semilocal Sonin projection (CCM Thm 4.6);
- (ii) [P_S, 1_{I_T} ℱ 1_{I_T}] = 0 (the Slepian property);
- (iii) P_{{∞}} is the classical prolate;
- (iv) the matrix of P_S in the semilocal Legendre basis is block-tridiagonal, with explicit coefficients in
 log p, p^{−1/2} and j.

**Statement to prove (TB-2b, spectral identity).** For h ∈ 𝒫_T,
W_T(h) = Σ_k κ_k |⟨h, e_k(P_S)⟩|² + ℛ_T(h), with κ_k ≥ 0 except for the k's in the UV spectrum of P_S, and with
ℛ_T of rank equal to the number of UV eigenvalues of P_S below the window threshold. Then N(T) = 0 reduces to the
UV part of P_S being contained in the kernel of primitivity (ℓ, ĥ(±i/2)). This is the operator form of CC's
"single negative direction aligned with ℓ", which R183_033 §2 observed numerically: λ₁(ker ℓ) = λ₂(𝒫) to 8 digits,
status OPEN.

**Allowed inputs.**
- Slepian theory, CCM Thm 4.6, the scaling law Λ (R183_029 Thm A) and the identity I_S (PROVED).
- thm:P, which gives the basis and the spherical Bessel formulas.
- Exact values of Λ(p^k) through the p-adic variables.

**Why no wall forbids it.**
- *W11-sharp (R185_008 §2.3):* requires P_T to be a frequency-diagonal multiplier with bounded inertia. Π_S and the
 spectral projections of P_S are not frequency-diagonal, so they lie in the residual class (ρ-a), declared OPEN.
- *I8:* classifies bounds ‖Δ_T‖ ≤ e^{o(T)}. TB-2b is a rank/counting identity, not a norm bound.
- *Szegő falsifier of C_T:* refutes uniform bounded inertia. TB-2b allows rank ~ cT as long as it matches the UV
 spectrum.
- *R183_028 §1.2 (n₋ = ∞ for the full trace):* applies to Son without prolate compression. TB-2b uses the
 compression (property (ii)).
- *Falsifier obligation:* M_m has the same local source. It must be checked that P_S depends on the values of Λ
 beyond the source, or that M_m's UV count differs by 2m. Otherwise, TB-2 is refuted by M_m (I11). This is the
 first check after P2.

**First lemma to attempt (L-TB2.0).** Write the exact Jacobi matrix of P_∞ in the Legendre basis of I_T from
thm:P and prove the **identity λ₁(A_∞ | ker ℓ) = λ₂(A_∞ | 𝒫_T)** observed in R183_033 §2. It is purely
archimedean and decidable. If the identity is due to ℓ's representative being an eigenvector of an operator that
commutes with A_∞ (the prolate), the "aligned negative direction" mechanism is structural and P_S inherits the
property. If not, TB-2b loses its candidate form.

**Decidability.** L-TB2.0: high. TB-2a: medium-low (existence in the adelic space; R186_002 works on it).
TB-2b: low.

### TB-3 — Two-scale bilinear inequality over Λ (O166.802.1, degree 2)

**Statement to prove (TB-3+, positive form).** There exist constants and an exponent η < ½ such that, for every
witness F in the image of the selector [S] at scale X = e^{2T}, every (γ, δ) ∈ Γ_S(F) and Y = Xe^{Δ},

 Re Σ_{n ≤ X} Σ_{X < m ≤ Y} Λ(n) Λ(m) (nm)^{−½+iγ} w₁(log n) w₂(log m) Φ(m/n) ≤ 𝔅(F, γ, δ) + O(Y^{η}),

with w₁, w₂, Φ ≥ 0 and the bound 𝔅 given by the archimedean part of the witness. The coupling with Γ, which is
requirement (δ), enters through 𝔅. The second scale is the Eratosthenes tail of the window (R169_091). The
bilinear term replaces the single twisted sum of (WS*).

**Statement to prove (TB-3−, negative form, first).** If every degree-2 inequality in Λ with two scales that
excludes the witness is an O-bound on a single twisted sum with exponent δ′ < δ_q, then I13's circularity extends
to degree 2 and TB-3+ is closed **within the degree-2 polynomial class**.

**Allowed inputs.**
- Λ ≥ 0, Λ = μ ∗ log and the Selberg identity with the μ of ℕ (type-C atoms of R185_004, i.e. completeness,
 outside the class closed under deletion).
- Type-II bilinear forms of Vaughan/Heath-Brown, used **non**-linearly (as a product Λ(n)Λ(m), not as a sieve
 upper bound).
- The witness structure (prop:witness, Thm Q).

**Why no wall forbids it.**
- *I13 (R166_802):* PROVED only for a single test and for power-size families; in general it is ARGUED. Degree 2
 with two scales is outside its hypothesis.
- *I6 (W-sieve):* forbids sieve upper bounds, measure bounds in γ and inputs uniform in γ ≤ Y^A. TB-3+ is an
 inequality on a set Γ_S(F) **defined by the window**, not uniform in γ, and uses the bilinear product, not a
 sieve. It must be checked that b_θ, I6's falsifier, violates TB-3+: b_θ is not multiplicative, so its bilinear
 autocorrelation differs.
- *Theorem BR (R185_005):* it is relative to 𝔐, whose atoms are L, D, C and Q. Its branch (c) (completeness) is
 closed **by circularity with the same scope as (0)**, i.e. that of a single test or power family. A multiscale
 degree-2 inequality with type-C atoms lies on the leaf BR does not cover (R185_005 §2.3, branch (c) and
 (iii-c) OPEN).
- *R184_016 (A1 with first-contact selector):* classifies the single-test form. TB-3+ is bilinear.

**First lemma to attempt (L-TB3.0).** This is TB-3− in model (M1) of R185_005 §1.1: bounded-type tests K and the
quadratic inequality Σ_{n,m} c_{nm} Λ(n)Λ(m) with a rank-2 matrix c (one window scale and one tail scale). We ask
whether the witness set O_U can be excluded with it without implying the single-sum bound. It is a finite-dimensional
moment-cone problem, extending R185_001 Lemmas 2–4.

**Decidability.** L-TB3.0 and TB-3−: medium-high. TB-3+: low. If TB-3− comes out positive, the degree-2 class is
closed by theorem and the program must move up to degree ≥ 3 or non-polynomial, as S2 requires.

---

## 4. Honest section: what is new and what reopens

| program | new relative to Papers 42–48? | reopens | what it must add to escape closure |
|---|---|---|---|
| TB-1a (jump map 𝒥_n) | **partially**. G2_B5_R1 built the chain and left the blow-up as HEURISTIC; the explicit jump map is not written out | G2_B5_R1 ("restatement") | An invariant (TB-1b) using Λ(p^k) = log p and Euler grouping. Without it, it is again G2_B5_R1's chain. |
| TB-1b (cone 𝒦_Euler) | **new**. Combines R162_2701 (Tate, NO-GO alone) with the archimedean flow of G2_B5_R1; neither does this | R162_2701 NO-GO | The condition must lie in the Tate ↔ Γ-flow compatibility, not in H_S ≻ 0, and must fail for M_m (mandatory proof) |
| L-TB1.0 | **new** as an analytic proof; R185_006 only gave the reduction to 18 dimensions + NUMERICAL | — | — |
| TB-2a (P_S) | **new**. CCM defer the operator; the corpus did not build it (R183_028 §2) | — | — |
| TB-2b (counting identity) | **new in form**. Replaces C_T's N_T, whose falsifier is Szegő | C_T (R183_024) | Allow growing rank equal to the UV count; not be a norm bound (I8); separate M_m |
| L-TB2.0 | **new** (the identity observed in R183_033 §2 is OPEN) | — | — |
| TB-3− | direct extension of R166_802 (crossword priority 2) | — | — |
| TB-3+ | registered square (O166.802.1); **no prior candidate** | the R169 chain (A1) | Degree 2 + two scales + completeness atoms; escape I13, which is PROVED only in the single-test and power-family cases |
| A3 (crystals with Γ background) | **new** as a formulation; Thm R (R164_401) is its closest relative | — | Use the integrality of the log ℕ support and the values log p, because DH/Epstein have integer, discrete μ |
| 𝒱_∞ and the monotone projection | the projection is lem:monoT rewritten (not new); the object 𝒱_∞ as an inverse limit is not in P47 | — | — |

**Declared risks.**
- (1) TB-1b may die from M_m on the first proof. That is desirable, because it is fast and decidable.
- (2) TB-2a may not exist. If [P_S, Π_S] = 0 and the Slepian property are incompatible for S ≠ {∞}, that is a
 structural NO-GO and would need to be proved as a theorem.
- (3) TB-3− coming out positive closes degree 2. TB-3+ then remains for degree ≥ 3, with no candidate.
- (4) The literature references marked "CITED from memory" (de Branges–Conrey–Li; Kurasov–Sarnak; Olevskii–Ulanovskii;
 Denisov 2006) are unverified: there is no web access and no PDF in 00-references. They must be verified before any
 integration.

**Proposed execution order.** L-TB1.0 + L-TB2.0 + L-TB3.0,
with a joint audit that first runs the three falsifier proofs (M_m for TB-1b and TB-2; b_θ for TB-3).
R186_001 and R186_002 continue in parallel per the README.

*No file in the record modified except this one. Row D: OPEN. No label changes.*
</content>
