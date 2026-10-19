# R186_036 — Candidate tool Ω: the family {𝔞_T}_T as a degree-0 object (transport between nested windows)

Phase 186, round 17. Paper 47, grid and crossword are not touched. No numerics (nothing decided; no script r036).

Read: R186_032 §4 (Ω: S1–S6), README 186 rounds 14–16 (W-lin, W-det), grid §3 (walls), §4 (falsifiers M_m, f_t,
P_{a,c}), log 27–28; R185_005 §1.3 (O1–O5); R163_401 §4.8 ((★_cell) ARGUED, Rem 4.8a); R164 README ((TC), L1/L2, Thm R);
R166_190 §0 (dichotomy), R166_501 Cor A.2 ((G),(N)); R169_000 §1–3 (A1–A7); R165_202 (1.1–1.5); R157_004 Lemma C;
R155_053 Prop 4.1, R155_055 §(ii); R160_M4_R1 (S, U-2); Paper 47 thm:A/eq:Aform, cor:mono, lem:monoT, lem:contA, def:PD,
prop:weak, rem:Kprim, rem:Cheb; R186_033/109 (PNT-window identity).

Notation (Paper 47): I_T = [−T,T]; c_F autocorrelation (supp ⊂ [−2T,2T]); 𝒩_T = {n ≥ 2: log n < 2T}; v_n = 2Λ(n)/√n;
𝔞_T(F) = C₀‖F‖² + Lev(c_F) − Σ_{n∈𝒩_T} v_n c_F(log n) (eq:Aform), Lev(Φ) = ∫₀^∞(Φ(0) − Φ(u))K(u)du, K ≥ 0 independent of T;
𝒫_T = {A(F) = B(F) = 0}; λ_A(T) = λ_min(𝔞_T|𝒫_T); h*_T a unit minimizer.

## 0. Verdict in one line

Direction (i) (transport between nested windows) computes exactly and gives **vanishing terms**: there is no
archimedean boundary term nor new-prime term (Lemma 1). Every degree-0 tool built from the family
{λ_A(T′)}_{T′} uses Λ beyond e^{2T} only through λ_A(T′), T′ > T (Theorem 3: regression), and the condition that
closes the regression is lim_{T′→∞} λ_A(T′) ≥ 0, which is the statement of the family itself (CITED R155_053/R160_M4).
**NO-GO as a tool Ω within the declared class 𝔉 (functionals of the family); box S2 remains blank.** What remains
PROVED and reusable: Lemma 1 (exact primal and dual transport), Lemma 2 (entry fold of each prime power),
Theorem 3 (regression with falsifier f_t). No contact with the sign.

## 1. The candidate and its S1–S6 verification

**Candidate 𝔍.** 𝔍 := L := lim_{T→∞} λ_A(T) (exists in [−∞, 0] by lem:monoT and Thm M of Paper 48, CITED R155_055 §(ii)),
with the "transport inequality" λ_A(T) ≥ L for every T, and the T-free reading
L = inf{𝔞_∞(F): F ∈ 𝒫_∞}, 𝒫_∞ := ∪_T 𝒫_T (compactly supported primitives), 𝔞_∞ = C₀‖·‖² + Lev − Σ_{n≥2} v_n c_F(log n)
(finite sum for each F). Then: λ_A(T) ≥ 0 ∀T ⟺ L ≥ 0 ⟺ L = 0 (the last by Thm M, CITED).

Verification, one by one:
- **S1 (nonlinear in F / degree 0).** Formally yes: L is an infimum, not a quadratic form in a fixed basis. But it
 is the same degree-0 type as λ_A(T): every proof of L ≥ −o(1) goes through lower bounds by window, which are
 certificates (def:PD) or reductions, i.e. W-lin. S1 holds only vacuously. **NOT in the sense of R186_032 §1 (E1).**
- **S2 (Λ beyond the window at the node frequencies, strength (N′)).** L uses all of Λ, but with no frequency
 localization and no input at all: Λ|[e^{2T},∞) enters only through λ_A(T′), T′ > T (Theorem 3). **NO.**
- **S3 (structural verification).** Deciding L ≥ 0 means deciding λ_A(T′) ≥ −ε(T′) with ε → 0 (squeeze S of
 R160_M4, CITED). The only relaxation relative to Thm M: the precision required at window T′ is o(1) and not
 exp(−e^{2T′}); but the comb that must be canceled has size 𝖠_{T′} ≍ 2e^{T′} (lem:mbounds), so the relative
 precision is still e^{−T′}. **NO.**
- **S4 (not an identity, not one-sided, not a class).** It is none of the three: it is the target statement
 rewritten without T. **Yes, vacuously.**
- **S5 (couples nodes ↔ atomic Λ).** There is no coupling: neither the nodes of h*_T nor the atomicity of Λ appear
 in L. **NO.**
- **S6 (admission against M_m, f_t).** L^{M_m} < 0 and L^{f_t} < 0 (their families have a witness: R163_801 Thm 5,
 R163_901 Thm F), so 𝔍 "fails" on both, but only because 𝔍 IS the statement; the test gives no information.
 **Vacuous.**

Conclusion of §1: 𝔍 is not a tool; it is a T-free reformulation, already on record (R155_053 Prop 4.1 for λ^W;
R155_055 for λ^A; R160_M4_R1 S and U-2). What follows proves that no variant within class 𝔉 (§3) improves it.

## 2. Lemma 1 — exact transport between nested windows (primal and dual). PROVED (primal = lem:monoT / R165_202 1.1)

**Lemma 1 (primal).** Let 0 < T < T′ and F ∈ L²(I_T) extended by zero to I_{T′}. Then, term by term in eq:Aform,
 (a) ‖F‖, A(F), B(F), c_F do not change; in particular 𝒫_T = 𝒫_{T′} ∩ L²(I_T) exactly;
 (b) archimedean boundary term: Lev(c_F) does not depend on T (K is T-free); the boundary contributes nothing;
 (c) new primes: Σ_{n∈𝒩_{T′}∖𝒩_T} v_n c_F(log n) = 0, because log n ≥ 2T and supp c_F ⊂ [−2T,2T] (c_F(±2T) = 0 by continuity);
 (d) hence 𝔞_{T′}(F) = 𝔞_T(F), and λ_A(T) ≥ λ_A(T′) with constant c(T,T′) = 1 and prime term ≡ 0.
*Proof.* (a)–(c) are direct readings of eq:Aform; (d) is lem:monoT. ∎
*Consequence.* The only transport inequality given by the nesting is the trivial one. Every nontrivial comparison
between 𝔞_{T′} and 𝔞_T on the same space (e.g. via dilation U_r, lem:contA: the kernel becomes rK(r·) and the comb
{(log n)/r}) is a quadratic form in F in a fixed basis with coefficients linear in Λ, i.e. family P of R166_405 and
falls into W-lin (R186_026 Thm 3.3, R186_031 Dom). The limit r → ∞ of the dilation reproduces rem:Cheb/R186_033
Lemma 1 (the "4" = 2r∫₀^{2T} e^{−ra/2}c_G → 4c_G(0); the leading term 2r∫e^{ra/2}c_G is A_r(G)B_r(G) = 0 on the
primitive): nothing new.

**Lemma 1′ (dual).** Let (ν′, β) be a certificate of value c at window T′ (def:PD: supp ν′ ⊂ {|u| ≥ 2T′}, f_{T′} = σ_{T′} + ν̂′ +
β·ĝ ≥ c). Then ν_T := ν′ − ½Σ_{n∈𝒩_{T′}∖𝒩_T} v_n(δ_{log n} + δ_{−log n}) has supp ⊂ {|u| ≥ 2T} and (ν_T, β) is a certificate
of value c at window T, with f_T ≡ f_{T′}.
*Proof.* σ_T = σ_{T′} + Σ_{new} v_n cos(τ log n) and the transform of the added atoms is exactly −Σ_{new} v_n
cos(τ log n). ∎
*Reading.* Certificates "inherited" from larger windows are precisely those carrying negative mass −v_n at log n
for prime powers outside the window (the branch "w(log n) > 0 at n > e^{2T}" of Lemma D of R186_032 §5). This does
not correct the finding of R186_032 §2(ii) (thm:C places its atoms on a lattice, not at log n): it only says that
the class of certificates with ν⁻ atomic at log ℕ is the image of the dual transport, and that its value never
exceeds D_{T′}; regression also holds in the dual.

## 3. Theorem 3 — regression: no functional of the family decides a window. PROVED (modulo Thm F CITED)

**Declared class 𝔉.** Statements P(T₀; (λ_A(T′))_{T′∈J}) whose validity depends on the family only through the
values λ_A(T′), T′ ∈ J ⊂ (0,∞), and their qualitative properties (monotonicity lem:monoT, continuity lem:contA,
upper bound Thm M). Includes (i)–(iii): functions of T ↦ λ_A(T), derivatives dλ_A/dT (R165_202 1.4), ρ*(T) of
R186_021 as a ratio of bottoms, and any "law" in T (log-convexity, R186_033 Idea 2 NO-GO).

**Theorem 3.** (a) If J is bounded, J ⊂ (0, T₁), no P ∈ 𝔉 valid for ζ implies λ_A(T) ≥ 0 for every T.
(b) If J is unbounded, P implies λ_A(T₀) ≥ 0 only if it implies λ_A(T′) ≥ −ε(T′) for a sequence T′ → ∞ with ε → 0,
i.e. only through L ≥ 0 (Lemma 1(d) + squeeze S, CITED R160_M4).
(c) The qualitative properties of the family do not separate: the family of M_m is monotone, continuous and
satisfies the bound of Thm M (same proofs: eq:Aform with the same atomic side; lem:contA only uses lem:mbounds),
and has L^{M_m} < 0.
*Proof.* (a) f_t = ζ + t·g (R163_901 Thm F, CITED) shares with ζ all coefficients Λ(n) with log n < 2T₁ (N₀ = e^{2T₁}),
so 𝔞_T^{f_t} = 𝔞_T^ζ and λ_A^{f_t}(T′) = λ_A^ζ(T′) for every T′ < T₁; P would then hold for f_t, and its conclusion
would give λ_A^{f_t}(T) ≥ 0 ∀T, against the witness of f_t (T_c(f_t) ≥ T₁ exists). (b) By Lemma 1(d) the
information of J ∩ (T₀, ∞) about λ_A(T₀) is exactly λ_A(T₀) ≥ sup_{T′∈J, T′>T₀} λ_A(T′) ≥ L; any lower bound used
at T′ is a lower bound by window (R186_029/107: its verification is a certificate or a reduction). (c) It is the
observation of grid §4 (M_m shares lem:contA, first contact, Theorem M). ∎

**Corollary 3.1 (what closes the regression).** Within 𝔉 the regression T → T′ → ∞ closes only by L ≥ 0, equivalent
to: there exist T_k → ∞ and lower bounds λ_A(T_k) ≥ −ε_k, ε_k → 0, each proved at window T_k. The relative
precision required is ε_k/𝖠_{T_k} ≍ ε_k e^{−T_k} (cancellation of the comb of size 2e^{T_k} down to o(1)). The
input that would produce those bounds is not in 𝔉; it is box S2 of Ω, unchanged.

**Corollary 3.2 (direction (iii)).** Every "alignment condition" between the peak/nodes of ĥ*_T and
cos(s log p), p > e^{2T}, formulated as an inequality in T, either (α) is a functional of h*_T alone — a window
datum, identical in f_t for T < T₁ — or (β) contains Λ(p), p > e^{2T}, explicitly, in which case its validity for ζ
is a statement about Λ outside the window that the family does not supply (A3–A4 of R169_000; (N′) of R166_802).
In both cases it falls under Theorem 3.

## 4. Lemma 2 — entry fold of each prime power. CONDITIONAL ((REG) of R162_407/R165_202)

The only place where a prime power n "beyond the window" acts on the family is its entry instant T_n = ½log n.
R165_202 1.4 (PROVED under (REG)): where λ_A is differentiable, λ_A′(T) = −𝒱_T(h*_T)/T with
𝒱_T(F) = (1/2π)∫τ m′(τ)|F̂|² dτ − Σ_{log n<2T} v_n log n·Re c_F′(log n) + 𝒯_T(F) (𝒯_T polar), and 𝒱_T(h*_T) ≥ 0.

**Lemma 2.** Let h = h*_T be real, continuous up to the boundary and with c_h ∈ C¹ near 2T ((REG)). Then
c_h′(2T⁻) = −h(−T)h(T), and when n enters (2T_n = log n) the new comb term contributes to 𝒱 the jump
+2T_n v_n h(−T_n)h(T_n); hence the slope of λ_A jumps by
 Δλ_A′(T_n) = −2 v_n h*(−T_n)h*(T_n) = ∓2 v_n h*(T_n)² (sign − on the even sector, + on the odd),
and λ_A is continuous at T_n (lem:contA) but in general not C¹: each prime power enters as a fold, not a jump.
*Proof.* c_h(u) = ∫_{−T}^{T−u} h(t)h(t+u)dt ⟹ c_h′(u) = −h(T−u)h(T) + ∫_{−T}^{T−u} h(t)h′(t+u)dt, and as u → 2T⁻ the
integral tends to 0 and the first term to −h(−T)h(T). The rest is formula 1.4 with the n term added (R165_202
line 79 notes it without evaluating). ∎
*Scope.* (REG) is OPEN: the form domain of Lev is only H^{log} (1_{I_T} is in it; an h ~ (T−t)^{−1/4} gives
c_h′(2T⁻) = ∞); the boundary behavior of the ground states of the logarithmic symbol "is not established"
(R165_202 §1.5). Lemma 2 is an accounting tool: it shows that the prime ↔ minimizer coupling at entry is read in the
**boundary values** h*(±T_n), not in the nodes of ĥ*; it is linear in Λ(n) and quadratic in h*: family P. It
decides nothing (Theorem 3(b)).

## 5. Check against the corpus (what is closed and why)

| object | status | where | why it is not Ω |
|---|---|---|---|
| exact transport T → T′ (zero terms) | PROVED | lem:monoT; R165_202 1.1 | identity, no sign (W12) |
| continuity of λ_A, λ_W | PROVED | lem:contA; R157_004 Lemma C; Bombieri Thm 5 | qualitative; M_m shares it |
| asymptotic criterion D ⟺ lim λ ≥ 0 | PROVED (reformulation) | R155_053 Prop 4.1 (λ^W), R155_055 §(ii) (λ^A), R160_M4 S/U-2 | it is the statement without T |
| λ_A ≤ exp(−e^{(2−ε)T}) | CITED | Paper 48 thm:M; grid W2 | L = 0 under D; no margin |
| derivative λ_A′ = −𝒱/T | PROVED under (REG) | R165_202 1.4; R162_407 | uses only Λ|𝒩_T and h*_T: local to the window |
| Hadamard: the drop lives at the boundary | ARGUED | R165_202 1.5 | differentiability of T ↦ h*_T not proved |
| log-convexity of λ_A | NO-GO NUMERICAL | R186_033 Idea 2, R186_109 | — |
| ρ*(T) as a function of T | NUMERICAL | R186_021 | ratio of bottoms: 𝔉, Theorem 3 |
| (★_cell), (TC), (G)+(N′) | OPEN without object | R163_401 §4.8, R164 README, R166_501 Cor A.2, R166_802 | what Ω should prove |
| input architecture A1–A7 | specification | R169_000 §3 | the family does not supply A3 with strength |

New contribution of this file: Lemma 1′ (explicit dual transport), Theorem 3 in the form of a declared class with
falsifier f_t, Lemma 2 (explicit value of the fold). Everything else is CITED.

## 6. Explicit falsifiers

- **Of Theorem 3(a):** a statement P over {λ_A(T′)}_{T′<T₁} valid for ζ that implies λ_A ≥ 0 ∀T. By Thm F
 (R163_901) none exists: f_t satisfies it and has a witness. Falsifier of the proof: an f_t whose λ_A differs
 from ζ at some window T′ < T₁ (impossible: eq:Aform only sees Λ(n), log n < 2T′).
- **Of Theorem 3(b)/Cor 3.1:** a lower bound λ_A(T_k) ≥ −ε_k, ε_k → 0, T_k → ∞, proved without a per-window
 certificate or reduction; it would be the S2 input. None exists in the corpus (R186_032 §4).
- **Of Lemma 2:** a minimizer h*_T (Galerkin M ≥ 24, R186_024/026) with c_h′(2T⁻) nonexistent or with h*(T_n)²
 that does not reproduce the slope jump of λ_A at T_n = ½log2, ½log3 (a numerical test is possible; not run
 because it decides nothing).
- **Of candidate 𝔍 = L:** vacuous (S6): M_m and f_t refute it only because it is the statement.

## 7. Answer to the four tasks

(1) Candidate stated (§1) and verified: S1 vacuous, S2 NO, S3 NO, S4 vacuous, S5 NO, S6 vacuous. (2) First lemma
proved: transport between nested windows is exact with archimedean boundary term 0 and new-prime term 0 (Lemma 1);
dual version with the negative mass at log n (Lemma 1′). (3) The tool decides no new window: it reduces to
λ_A(T′), T′ > T, with infinite regression; the limiting condition that closes it is lim λ_A(T′) ≥ 0 (⟺ L = 0), i.e.
lower bounds −o(1) by window for T′ → ∞ with relative precision e^{−T′}: it is the statement of the family, not a
mechanism. (4) Falsifiers in §6.

**Labels.** Lemma 1 PROVED (CITED lem:monoT); Lemma 1′ PROVED; Theorem 3 PROVED (modulo Thm F CITED); Cor 3.1–3.2
PROVED; Lemma 2 CONDITIONAL ((REG)); candidate 𝔍 as tool Ω: **NO-GO within class 𝔉** (impossibility proof: Theorem
3 + falsifier f_t). Row D: OPEN. No grid symbol changes. No contact with the sign. Nothing is claimed about T > ½log5.
