# R186_050 — Witness theory: characterization of 𝒲_T, absorption and the asymptotic route 

NUMERICAL. Sources: Paper 47 (eq:Aform, eq:W, lem:mbounds, lem:monoT, lem:contA, lem:roughEF, thm:parityschur, thm:margin,
thm:A), Paper 48 thm:M, R185_005B (BR), R186_024/026/028/036/039/040/044/047/048/049/112/114/115.

**Contact with the sign: none.** Nothing that follows decides λ_A(T) < 0 nor λ_A(T) ≥ 0 for ζ in any window.

## 0. Verdict in ten lines

1. 𝒲_T := {F ∈ 𝒫_T : 𝔞_T(F) < 0}. PROVED: 𝒲_T ≠ ∅ ⟺ λ_A(T) < 0 ⟺ h*_T ∈ 𝒲_T; 𝒲_T is an open, J-invariant cone.
2. **Absorption (PROVED, trivial from lem:monoT):** 𝒲_T ↪ 𝒲_{T′} by extension by zero, with the SAME value 𝔞_{T′}(F) = 𝔞_T(F).
 Hence 𝒯 := {T : λ_A(T) < 0} = (T_c, ∞) with T_c ≥ ½log5 (open by lem:contA), λ_A(T_c) = 0 if T_c < ∞, and
 D ⟺ T_c = ∞ ⟺ L := lim λ_A(T) = 0 ⟺ λ_A(T_k) ≥ 0 for some T_k → ∞ ⟺ ∃ε(T) → 0 with λ_A(T) ≥ −ε(T) ∀T.
3. Necessary conditions (1)–(9) formulated in §2 with their actual label: only (N1-a), (N3-a), (N4-a), (N5), (N6), (N8) are
 PROVED; (1) "even", (2) "vanishes at zeros ≤ T*", (3) "piecewise Tate", (4) "coupling only", (7) are CONDITIONAL or NUMERICAL.
4. **Freezing lemma (PROVED, §4.1):** a witness F₀ ∈ 𝒲_{T₀} is a witness in every window T ≥ T₀ without anything changing: its
 spectral measure, its parity, its value, its autocorrelation; new primes see it as c_{F₀}(log n) = 0. Therefore
 **no asymptotic condition (T → ∞) on witnesses can be incompatible if it is not already incompatible in a fixed window**: the route
 "equidistribution of new primes vs. growing coherent coupling" is **NO-GO as an exclusion mechanism** (§4.2).
5. **Node lemma (PROVED, §3.1):** a quartet {½ ± δ ± iγ} is worth Q_δ(F) = 4|Φ_c|² − 4|Φ_s|² and is ≥ −4S_δ(T)‖F‖² with
 S_δ(T) = sinh(2δT)/(2δ) − T; to a test with F̂(γ) ≠ 0 and zero slope the quartet looks like a double zero ON the
 line (it is penalized). The witness that exploits a quartet is the **direction of spectral derivative** in γ (node + slope):
 F_T ≈ (¼ − ∂²)[t·sin(γt)·η_T(t)], with gain ≍ e^{2δT}/T (reproduces R186_039/044 with no new number, §4.3, ARGUED).
6. **Consistency theorem (PROVED by inspection, §4.4):** M₁ satisfies (1)–(7) and has witnesses ∀T > 0.573; hence (1)–(7)
 are not mutually incompatible as abstract conditions; any proof of incompatibility for ζ must use the ONLY thing that
 separates ζ from M₁: the Λ side of M₁ is Λ_ζ + coherent density 4cos(γ₁u)cosh(δu)du; that of ζ is the positive atomic comb.
7. That separation, in the adapted family F_T^{γ}, is the inequality (E_γ) of §4.3: **a statement with content, not tautological
 with D, but on the zero side (O2 of BR, = cell S2 of Ω)**: no zero-free proof. NO-GO as a new route; it is
 kept as the most precise form of the object "growing coherence of the comb in (γ, slope)".
8. Dichotomy of the limit (§4.5): L ∈ {0} ∪ [−∞, 0); ARGUED (via zeros): L ∈ {0, −∞}.

## 1. Framework

Notation (Paper 47): I_T = [−T, T]; 𝔞_T(F) = C₀‖F‖² + Lev(c_F) − Σ_{n∈𝒩_T} v_n c_F(log n) (eq:Aform), 𝒩_T = {n < e^{2T}},
v_n = 2Λ(n)/√n, Lev(Φ) = ∫₀^∞(Φ(0) − Re Φ(u))K(u)du ≥ 0, c_F(u) = ∫F(t)F(t+u)dt; equivalently 𝔞_T(F) = (2π)⁻¹∫m|F̂|² −
Σ v_n c_F(log n) with m(τ) = C₀ + ∫(1 − cos τu)K, C₀ = ψ(¼) − log π = −5.3721. 𝒫_T = {A = B = 0}, A(F) = ∫Fe^{t/2},
B(F) = ∫Fe^{−t/2}; λ_A(T) = min 𝔞_T over the unit sphere of 𝒫_T, attained (compact resolvent, Paper 47 §lem:contA);
h*_T a minimizer. 𝔄_T := Σ_{n∈𝒩_T} v_n = sup_τ Σ v_n cos(τ log n) (lem:mbounds(iii)); M₀(T) := 𝔄_T − C₀.
J F(t) = F(−t); A(JF) = B(F), so that 𝒫_T is J-stable and 𝔞_T is J-invariant (thm:parityschur(o)).

**Definition 1.1.** 𝒲_T := {F ∈ 𝒫_T ∩ dom(𝔞_T) : 𝔞_T(F) < 0} (witnesses). 𝒯 := {T > 0 : 𝒲_T ≠ ∅}.

**Lemma 1.2 (PROVED).** (i) 𝒲_T ≠ ∅ ⟺ λ_A(T) < 0 ⟺ h*_T ∈ 𝒲_T. (ii) 𝒲_T is a cone (F ∈ 𝒲_T ⇒ cF ∈ 𝒲_T, c ≠ 0), open in the
form norm, J-invariant, and F ∈ 𝒲_T ⇒ F_e ∈ 𝒲_T or F_o ∈ 𝒲_T (F_e, F_o the even and odd parts).
*Proof.* (i) definition of infimum and existence of the minimizer. (ii) homogeneity of degree 2; continuity of 𝔞_T in the form
norm; A(F_e) = ½(A(F) + B(F)) = 0 and B(F_e) = A(F_e), so F_e, F_o ∈ 𝒫_T; 𝔞_T(F) = 𝔞_T(F_e) + 𝔞_T(F_o) (thm:parityschur(o)),
and a negative sum has a negative term. ∎

**Lemma 1.3 (absorption; PROVED = lem:monoT).** For T < T′, extension by zero ι : L²(I_T) → L²(I_{T′}) satisfies ι(𝒫_T) ⊂ 𝒫_{T′}
and 𝔞_{T′}(ιF) = 𝔞_T(F). Hence ι(𝒲_T) ⊂ 𝒲_{T′}, 𝒯 is an upward set, and λ_A is non-increasing.
*Proof.* Lem:monoT: the norm, Tate moments and c_F do not change; the new contacts have log n ≥ 2T, where c_F = 0. ∎

**Theorem 1.4 (structure of 𝒯; PROVED).** (a) 𝒯 = (T_c, ∞) with T_c := inf 𝒯 ∈ [½log5, ∞] (𝒯 open by lem:contA; ½log5 by
thm:log5W, CITED Zhu up to 0.8). (b) If T_c < ∞: λ_A(T_c) = 0, there exists h_c ∈ 𝒫_{T_c}, ‖h_c‖ = 1, with 𝔞_{T_c}(h_c) = 0 and
𝔞_{T_c}(h_c, G) = 0 ∀G ∈ 𝒫_{T_c} (null vector of the first contact); 𝒲_{T_c} = ∅ and 𝒲_T ∩ ι(L²(I_{T_c})) = ∅ for every T > T_c.
(c) L := lim_{T→∞} λ_A(T) exists in [−∞, 0] (monotonicity + thm:margin: limsup ≤ 0) and
 D ⟺ T_c = ∞ ⟺ L = 0 ⟺ [∃T_k → ∞ : λ_A(T_k) ≥ 0] ⟺ [∃ε : (0,∞) → [0,∞), ε(T) → 0, λ_A(T) ≥ −ε(T) ∀T].
(d) D ⟺ λ_A(½log n_k) ≥ 0 for any sequence n_k → ∞ (e.g. n_k = 2^k, or the primes).
*Proof.* (a) Lemma 1.3 + continuity. (b) λ_A ≥ 0 on (0, T_c), < 0 afterward, continuous ⇒ λ_A(T_c) = 0; h_c = h*_{T_c};
𝔞_{T_c} ≥ 0 on 𝒫_{T_c} and vanishes at h_c ⇒ h_c lies in the radical (Cauchy–Schwarz for forms ≥ 0); the last statement is
Lemma 1.3 read backwards: a witness supported in I_{T_c} would be a witness at T_c. (c) If λ_A(T) ≥ −ε(T) with ε → 0, then
λ_A(T) ≥ L = lim λ_A(T′) ≥ lim(−ε(T′)) = 0 for every T. The other arrows are monotonicity. (d) particular case of (c). ∎

*Comment.* (c) is the precise form of "negativity is absorbing": ¬D is equivalent to "∃c > 0, T₀ : λ_A(T) ≤ −c ∀T ≥ T₀".
It is the "two-sided asymptotic law" cell of R186_110/README round 18, here PROVED as a reformulation (already CITED R155_053,
R160_M4); it is not a tool: deciding L = 0 is deciding D. What is new is how it is used in §4.

**Lemma 1.5 (births; PROVED = R186_048 Lemmas 3.1–3.2).** At T_n = ½log n, c_F(log n) = 0 ∀F ∈ L²(I_{T_n}): the form, λ_A and h*
do not change at T_n. For T = T_n + ε: |c_F(log n)| ≤ ½(‖F‖²_{[−T,−T+2ε]} + ‖F‖²_{[T−2ε,T]}). Consequence: **T_c can be some T_n
(nothing excludes it), but the witness does not "arise" from the new prime**: in (T_n, T_n + ε) the new prime contributes at most
v_n·(boundary mass of width 2ε), and every witness at T > T_c has positive mass outside I_{T_c} (Theorem 1.4(b)).

## 2. The set 𝒲_T as an intersection of necessary conditions

Each condition is stated as a set 𝒩_j ⊂ 𝒫_T with 𝒲_T ⊂ 𝒩_j, and its label is that of the inclusion.

**(N1) Parity.** (a) PROVED (Lemma 1.2(ii)): 𝒲_T ≠ ∅ ⇒ 𝒲_T ∩ (even) ≠ ∅ or 𝒲_T ∩ (odd) ≠ ∅. (b) "the witness is even":
𝒲_T ∩ 𝒫_T^{odd} = ∅ ⟸ W_T ≥ 0 on L²_odd(I_T) (because on 𝒫_T, W_T = 𝔞_T; R186_028 Lemma 1.1): PROVED mod. CITED for
T ≤ ½log5 (R186_028 Thm 1.4; Zhu + thm:log5W), **CONDITIONAL[W_T|odd ≥ 0]** afterward (statement for the full form, no
weaker than D on the odd sector). A primitive odd witness is, without more, an odd witness of the full form.

**(N2) Zero side.** Let F ∈ 𝒫_T with (a) ∫log(2+|τ|)|F̂|² < ∞ and (b) Σ_ρ|Φ_F(ρ)Φ_F(1−ρ)| < ∞. Then (lem:roughEF)
𝔞_T(F) = Σ_{ρ on the line}|F̂(γ_ρ)|² + Σ_{quartets} Q_{δ_q,γ_q}(F), Q as in §3.1. Hence **CONDITIONAL[(a),(b)]**:
 F ∈ 𝒲_T ⇒ Σ_{quartets} Q_{δ_q,γ_q}(F) < −Σ_{line}|F̂(γ_ρ)|² ≤ 0. (2.1)
(a) holds for h*_T (form domain). *Circularity warning:* (2.1) is a condition on ζ (a quartet exists),
not a usable condition on F; using it to exclude witnesses requires an input on the position of the zeros, which is (O2)
of BR and outside 𝔐. Here it is used only as an **identity** (the zeros as objects of the carrier), never as a criterion. The
reading "the nearly balanced directions vanish at zeros ≤ T*" (R186_040/112, NUMERICAL) is (2.1) with 𝔞_T(u) ≈ 0 and is
**CONDITIONAL[zeros ≤ 1.4T* on the line, CITED]**, not a fact about (m, Λ).

**(N3) Low frequency.** (a) PROVED: F ∈ 𝒲_T ⇒ Lev(c_F) < M₀(T)‖F‖², and for every R > 0 with m(R) > C₀,
 μ_F(|τ| > R) < M₀(T)/(m(R) − C₀), μ_F := |F̂|²dτ/(2π‖F‖²), m(R) ≥ log(R/2π) − 1/R − 1/(2R²). (2.2)
*Proof.* 𝔞_T(F) < 0 and Σ v_n c_F(log n) ≤ 𝔄_T‖F‖² (|c_F| ≤ ‖F‖²) give Lev(c_F) < (𝔄_T − C₀)‖F‖²; Lev(c_F) = (2π)⁻¹∫(m − C₀)|F̂|²
with m − C₀ ≥ 0 increasing in |τ| (lem:mbounds(i)) bounds (m(R) − C₀)‖F‖²μ_F(|τ| > R) ≤ Lev(c_F); bound on m: lem:mbounds(ii). ∎
Scale: 𝔄_T ≤ 4.16e^T (ψ(x) ≤ 1.03883x, CITED Rosser–Schoenfeld, plus partial summation), so (2.2) only bites for
log R ≳ 4e^T: the PROVED low-frequency bound is doubly exponential in T, much weaker than observed.
(b) "99% in E_k = piecewise Tate, k ≍ T/τ₀" (R186_024): **NUMERICAL**; the PROVED fact behind it (R186_024 §1.3) is that each
block with its Tate contributes the archimedean background of a window of half-length T/k, not a property of the witness.
(c) PROVED: the negative set of the symbol σ_T = m − Σv_n cos(τ log n) is in |τ| ≤ τ_𝔄 := m⁻¹(𝔄_T) (m increasing,
Σ ≤ 𝔄_T), and m < 0 only for |τ| < τ₀ with τ₀ ∈ (5, 7.5) (lem:mbounds(ii) evaluated at 5 and 7.5). A witness has
(2π)⁻¹∫_{|τ|≤τ_𝔄} σ_T⁻|F̂|² > (2π)⁻¹∫ σ_T⁺|F̂|² (Pos < Neg in the R186_034 bundle).

**(N4) Alignment and coupling.** (a) PROVED (dichotomy): let Γ_T := C₀‖·‖² + Lev (form without primes). F ∈ 𝒲_T ⇒
Σ_n v_n c_F(log n) > Γ_T(F). Hence 𝒲_T = 𝒲_T^{Γ<0} ∪ 𝒲_T^{al}, with 𝒲_T^{al} := {Γ_T(F) ≥ 0, Σ v_n c_F(log n) > Γ_T(F) ≥ 0}:
in 𝒲_T^{al} the witness's autocorrelation is **positively aligned with the comb** (weighted average with weights v_n > 0 of
c_F(log n) strictly positive); Γ_T < 0 on 𝒫_T occurs from T ≈ 0.37 on (R186_028, NUMERICAL; prop:archneg ≤ 0.4608 PROVED).
(b) "it does not win on the diagonal by components, only by the coupling G" (R186_044 Thm 2, R186_047): **PROVED in the three
windows ½log3, log2, ½log5 modulo floating-point quadrature** (A_WW ≻ c_W > 0, D ≻ 0 componentwise), **CONDITIONAL** for other T
(extension of Lemma 3 of R186_047). Precise form: with V = span of prolates, W = 𝒫_T ∩ V^⊥, F ∈ 𝒲_T ⇒ P_V F ≠ 0 and
𝔞_T(F_V) + 2𝔞_T(F_V, F_W) + c_W‖F_W‖² < 0 (Schur).

**(N5) Between prime entries.** PROVED (Lemma 1.5): T_c = T_n is not excluded; what is PROVED is that the form does not change
at T_n and that the cost of the new prime in (T_n, T_n + ε) is bounded by the boundary mass. The sign jump of M₁ at T ≈ 0.573
(between boundaries) is NUMERICAL (R186_048).

**(N6) Quartet and Kreĭn threshold.** PROVED (R186_044 Lemma Q, Prop. K; §3.1 here): the perturbation has rank (2,2) and the
sign condition on a subspace X with 𝔞_T|X ≻ 0 is max spec(4S_X H₊⁻¹S_X*) < 1. Lemma P (δ_c = √(λ_A/4|ĥ*′(γ₁)|²)): **ARGUED**.
It is a description of the falsifier, not a condition on witnesses of ζ; its role is in §4.

**(N7) Old prolates.** ν(T₀, T) = O(1) and is blind to the sign (R186_049): **NUMERICAL**; does not constrain 𝒲_T.

**(N8) Value bounds.** PROVED: λ_A(T) ≥ C₀ − 𝔄_T ≥ −(5.38 + 4.16e^T) (Lev ≥ 0; lem:mbounds). thm:margin / Thm M (Paper 48)
are UPPER bounds: λ_A(T) ≤ exp(−e^{(2−ε)T}) for T ≥ T₀(ε). Hence for every F ∈ 𝒲_T: (C₀ − 𝔄_T)‖F‖² ≤ 𝔞_T(F) < 0, and
there is no lower bound of the type λ_A ≥ −exp(−e^{cT}) in the corpus (the phrase had the direction
reversed; Thm M(b) is an upper bound). Remark: the lower bound grows as e^T = e^{2δT} with δ = ½, the edge of the band:
it is exactly the rate of Lemma 3.1 for a quartet at the edge (§3.1), consistency with no new content.

**(N9) Falsifiers.** M_m (ζ + m quartets, PROVED as a form object; primitive witness PROVED R162_2501) and f_t (primitive
witness ARGUED → CONDITIONAL) (R186_114). Every necessary condition that also holds for M₁ does not by itself exclude witnesses.

**Definition 2.1 (candidate set).** 𝒲_T^{cand} := 𝒩_1a ∩ 𝒩_3a ∩ 𝒩_3c ∩ 𝒩_4a ∩ 𝒩_8 (the PROVED ones) and
𝒲_T^{cand,+} := 𝒲_T^{cand} ∩ 𝒩_1b ∩ 𝒩_2 ∩ 𝒩_4b (adding the CONDITIONAL ones). We have 𝒲_T ⊂ 𝒲_T^{cand,+} ⊂ 𝒲_T^{cand} and
**neither inclusion is known to be strict in any window** (for T ≤ ½log5, 𝒲_T = ∅ and 𝒲_T^{cand} ≠ ∅: the example
h*_T is in every PROVED 𝒩_j with 𝔞_T(h*) = λ_A > 0, which shows that the PROVED conditions do not "see" the sign).

## 3. Search for a contradiction

### 3.1 Node lemma (what makes a quartet negative)

**Lemma 3.1 (PROVED).** Let z = δ + iγ, 0 < δ < ½, and for F ∈ L²(I_T) real Φ_c(F) := ∫F cosh(δt)e^{iγt}dt, Φ_s(F) := ∫F sinh(δt)e^{iγt}dt.
The quartet {½ ± δ ± iγ} contributes to Σ_ρ Φ_F(ρ)Φ_F(1−ρ) exactly Q_{δ,γ}(F) = 4|Φ_c(F)|² − 4|Φ_s(F)|² (R186_044 Lemma Q), and
 −4S_δ(T)‖F‖² ≤ Q_{δ,γ}(F) ≤ 4(S_δ(T) + 2T)‖F‖², S_δ(T) := ∫_{−T}^{T}sinh²(δt)dt = sinh(2δT)/(2δ) − T.
Moreover Φ_s(F) = δ·(−i)F̂′(γ) + O(δ³T³‖F‖) and Φ_c(F) = F̂(γ) + O(δ²T²‖F‖) (F̂(γ) := ∫F e^{iγt}).
*Proof.* Cauchy–Schwarz on I_T: |Φ_s|² ≤ ‖F‖²∫sinh², |Φ_c|² ≤ ‖F‖²∫cosh² = ‖F‖²(S_δ + 2T). The expansions are those of
sinh(δt) = δt + O(δ³t³), cosh(δt) = 1 + O(δ²t²). ∎

**Corollary 3.2 (PROVED, Weyl for forms).** λ_A(T) − 4Σ_q S_{δ_q}(T) ≤ λ_A^{M_m}(T) ≤ λ_A(T) + 4Σ_q(S_{δ_q}(T) + 2T). In particular
the negativity of M₁ grows at most as e^{2δT}/(2δ), and the threshold δ_c of M₁ at T satisfies (8/3)δ_c²T³(1 + O(δ_c²T²)) ≥ λ_A(T)
(with S_δ(T) ≈ (2/3)δ²T³), in the same form as δ_c = √(λ_A/4|ĥ*′(γ₁)|²) with |ĥ*′(γ₁)|² ≤ (2/3)T³ (R186_044 Lemma P, ARGUED).

**Reading (PROVED by Lemma 3.1).** For a test F with F̂(γ) ≠ 0 and F̂′(γ) = 0 (e.g. symmetric in time about the center
with adjusted phase), the quartet costs it +4|F̂(γ)|²(1 + O(δ²T²)): **it behaves like a double zero on the line**. The quartet
only pays in the direction of the **slope** F̂′(γ) (node at γ plus slope), with gain 4δ²|F̂′(γ)|² to first order.
This is the structural explanation of (N2) and of R186_044 Lemma P (blind regime: node of ĥ* at γ₁ and V/W cancellation).

### 3.2 (2)+(4): vanishing at the zeros and winning only through coupling

With identity (2.1), "vanishing at the zeros on the line ≤ T*" is the cost term Σ_{line}|F̂(γ_ρ)|² that a witness
minimizes, and "winning through coupling" is that the gain −Σ Q < 0 is not local in the symbol σ_T (R186_044). There is no
possible contradiction via this route: M₁ realizes it (node of h* at γ₁, gain in G, R186_044/115). As a tool for ζ,
(2.1) only excludes witnesses if it is known that there are no quartets: **circular** (it is (O2)); it is noted and not used.

### 3.3 (3)+(4) without zeros: the inequality and its content

Let E_k ⊂ 𝒫_T be the space of piecewise Tate (k blocks B_j, F|_{B_j} = a_je^{t/2} + b_je^{−t/2}; dim 2k − 2). Writing
𝔞_T|E_k = Σ_j D_j + Σ_{i≠j} G_{ij} (block diagonals, couplings: archimedean cross terms ≤ 0 and prime overlaps
E(γ; B_i ∩ (B_j + log n)), R186_026 Lemmas 1.1–1.4, closed form PROVED), the inequality that would express "(3) ∧ (4) ⇒ no witness" is
 (★_k): Σ_{i≠j} G_{ij}(F_i, F_j) ≥ −Σ_j D_j(F_j) ∀F ∈ E_k, i.e. λ_min(𝔞_T|E_k) ≥ 0.
**Evaluation (PROVED, R186_026 Thm 3.3 + R186_025/105 Thm A/B):** D(T) ⇒ (★_k) ∀k; (★_k) for a fixed k does not imply D(T)
(λ_min(𝔞_T|E_k) ≥ λ_A, strictly in the computed cases); (★_k) ∀k ⟺ D(T) (λ_min(𝔞_T|E_k) ↓ λ_A). Hence (★_k) is
**strictly weaker than D for fixed k and exactly D in the limit**: it is not tautological as a finite statement, but
every proof of (★_k) uniform in k is a proof of D, and what separates fixed k from the limit is the same coupling G. Without
input on Λ beyond the window (Lemma 0 of R186_038: every Toeplitz/Hankel form in L²(I_T) is blind to Λ outside
e^{2T}), (★_k) lies in W-lin. **Actual content:** the Gram matrix of the coupling {log, artanh, Li₂, χ₂} × prime
overlaps dominates the Tate diagonal; this is (L2) of Thm A/B, OPEN since R186_025. Nothing is added.

## 4. Absorption and the asymptotic route

### 4.1 Freezing lemma

**Lemma 4.1 (PROVED).** Let F₀ ∈ 𝒲_{T₀}. For every T ≥ T₀, ιF₀ ∈ 𝒲_T and: (i) 𝔞_T(ιF₀) = 𝔞_{T₀}(F₀) (constant in T);
(ii) c_{ιF₀} = c_{F₀}, so c_{ιF₀}(log n) = 0 for every n ∉ 𝒩_{T₀}: **new primes do not interact with F₀**;
(iii) the spectral measure μ_{F₀}, the parity, the Tate moments (= 0), Lev(c_{F₀}), Γ_T(F₀) and the alignment
Σ_{n∈𝒩_{T₀}}v_n c_{F₀}(log n) are independent of T; (iv) under (a),(b) of lem:roughEF, the decomposition (2.1) of 𝔞_T(ιF₀)
is the same for every T (the zeros are the same objects). *Proof.* Lemma 1.3 term by term (eq:Aform). ∎

### 4.2 Consequence: NO-GO of asymptotic incompatibility

**Theorem 4.2 (NO-GO; PROVED as a meta-statement).** Let 𝒞 = {𝒞_T}_{T>0} be a family of necessary conditions on witnesses
(𝒲_T ⊂ 𝒞_T ∀T). If 𝒞_T is empty (or contradictory) for every T ≥ T₁, then 𝒲_T = ∅ for every T ≥ T₁, and by absorption
𝒲_T = ∅ for every T, i.e. D. Conversely, **every proof that "𝒞_T = ∅ for large T" is a proof of D in the fixed window
T₁**, since the frozen witness ιF₀ (Lemma 4.1) of any T₀ < T₁ belongs to 𝒞_T for every T ≥ T₀ with all its
invariants fixed. In particular:
(a) the mechanism "equidistributed new primes cannot sustain a coherent coupling over a growing component"
does not apply to ιF₀: there is no coupling with new primes (c_{F₀}(log n) = 0), and there is no growing component (μ_{F₀}
is fixed). The limit T → ∞ does not simplify the witness; it only simplifies the ambient operator, which the frozen witness does not see.
(b) exact Landau–Widom, components → density, exact Weyl: all are statements about σ_T and its prolates, of which ιF₀
is independent. No limit law of the symbol constrains ιF₀ beyond what σ_{T₀} already constrains.
(c) it escapes W-fam and W-loc as the goal states, but falls into the simplest form of the circularity of Lemma H/R185_001:
the asymptotic statement about witnesses IS the per-window statement. **NO-GO as an exclusion mechanism.**

What Theorem 4.2 does **not** close: asymptotic statements about ADAPTED families {F_T} (e.g. h*_T, or the coherent
family of §4.3), which are not necessary for ¬D. A theorem of the type "no adapted family has coherent growth" would not
exclude frozen witnesses; it would only bound the rate of L. This is the content of §4.3–4.5.

### 4.3 The adapted family: growing coherence vs. equidistribution, and the inequality (E_γ)

**Construction 4.3 (PROVED as membership).** For γ > 0, T > 0 and η_T ∈ C_c^∞(I_T) even, 0 ≤ η_T ≤ 1, η_T = 1 on I_{T−1},
set g_T(t) := t·sin(γt)·η_T(t) (even) and F_T := (¼ − ∂_t²)g_T. Then F_T ∈ 𝒫_T: F̂_T(τ) = (τ² + ¼)ĝ_T(τ) vanishes at
τ = ±i/2, which is A(F_T) = B(F_T) = 0. To first order F_T = (γ² + ¼)g_T − 2γ cos(γt)·η_T − (t sin γt)η_T″ − 2(sin γt + γt cos γt)η_T′,
‖F_T‖² = (γ² + ¼)²(T³/3)(1 + O(1/T)), and F̂_T is (τ²+¼) times the derivative in γ of the sinc kernel of I_T: **node at
±γ with maximal slope** (R186_044 Lemma P, "spectral derivative direction"). With a quartet at ½ ± δ₀ ± iγ:
 Φ_s(F_T) = i(γ²+¼)∫t sinh(δ₀t) sin²(γt)η_T dt + O(γ e^{δ₀T}) = i(γ²+¼)(T e^{δ₀T}/(2δ₀))(1 + O(1/(δ₀T))), Φ_c(F_T) = O(γ e^{δ₀T}/δ₀)
(parity: t sinh(δ₀t) even, t cosh(δ₀t) odd), so by Lemma 3.1
 Q_{δ₀,γ}(F_T)/‖F_T‖² = −(3/δ₀²)·e^{2δ₀T}/T·(1 + O(1/(δ₀T)) + O(δ₀²/γ²)). (4.1)
**(4.1) reproduces the law L ≈ −c·e^{2δT}/T observed for M₁ (R186_039, NUMERICAL) with the correct exponent and power of T;
ARGUED (constants not closed; the O terms are not written with bounds).** The archimedean term of F_T is
(2π)⁻¹∫m|F̂_T|²/‖F_T‖² → m(γ) (μ_{F_T} → δ_{±γ} at scale 1/T; m continuous). It is the adapted family of the witness of a quartet.

**Definition 4.4 (comb coherence in (γ, slope)).** 𝔖_T(γ) := Σ_{n∈𝒩_T} v_n c_{F_T}(log n)/‖F_T‖². By eq:Aform,
𝔞_T(F_T)/‖F_T‖² = (2π)⁻¹∫m|F̂_T|²/‖F_T‖² − 𝔖_T(γ). Note: c_{F_T} = (¼ − ∂_u²)²c_{g_T} is **orthogonal to cosh(u/2)** (F_T ∈ 𝒫_T),
so that 𝔖_T(γ) is the twisted Chebyshev sum Σ Λ(n)n^{−½}cos(γ log n)·P_T(log n) with weight P_T having no polar
component: the x^{½}/… Perron term does not appear. This is what makes 𝔖_T an O(1) quantity and not e^{T}.

**Proposition 4.5 (the inequality; PROVED as an implication).** D ⇒ for every γ > 0:
 (E_γ): limsup_{T→∞} 𝔖_T(γ) ≤ m(γ).
*Proof.* 𝔞_T(F_T) ≥ 0 ∀T and the limit of the archimedean term. ∎
**Evaluation of (E_γ).** (i) It is not tautological with D: it is D on a one-dimensional family indexed by γ, strictly weaker
(it does not imply D: it says nothing about frozen witnesses of another form). (ii) It has content on (m, Λ): it says that the
atomic comb v_nδ_{log n}, tested against the autocorrelation of the spectral derivative direction at γ, does not asymptotically
exceed the archimedean level m(γ) = log(γ/2π) + O(1/γ). (iii) Its content IS on the zero side: with (2.1), 𝔖_T(γ) = archimedean
term − Σ_{line}|F̂_T(γ_ρ)|²/‖F_T‖² − Σ_{quartets}Q/‖F_T‖²; the line term is worth ≈ (2π)⁻¹∫|F̂_T|²dN(τ)/‖F_T‖² →
log(γ/2π) + o(1) (Riemann–von Mangoldt, CITED: the zero density is m to leading order), so that (E_γ) is equivalent,
modulo o(1), to **"limsup_T −Σ_{quartets}Q_{δ_q,γ_q}(F_T)/‖F_T‖² ≤ 0"**, which by (4.1) fails if there is a quartet at height γ (and by
the oscillating terms of size e^{2δ_qT}/(T(γ_q − γ)²) at other heights). That is, **(E_γ) is, by the identity, a
statement of absence of quartets: (O2) of BR, cell S2 of Ω (Λ beyond the window at frequency γ with strength
(N′)) and the circularity of R166_802 item 2**. There is no zero-free proof of (E_γ) in the corpus nor in the literature
consulted (R186_020/027). **NO-GO as a new route**; it is kept as the exact formulation of the object.

**What distinguishes M₁ from ζ (answer).** For M₁, 𝔖_T^{M₁}(γ₁) = 𝔖_T(γ₁) + ∫c_{F_T}(u)β₁(u)du/‖F_T‖² with
β₁(u) = 4cos(γ₁u)cosh(δu) (R186_114 §1.1), and the second term is −Q_{δ,γ₁}(F_T)/‖F_T‖² ≍ +(3/δ²)e^{2δT}/T by (4.1): M₁ violates
(E_{γ₁}) because its Λ side contains a **coherent density of growing amplitude** at frequency γ₁. ζ has only the
positive atomic comb. That is the only object that separates them: "growing coherence of the atomic comb in (γ, slope)"
against "added coherent density". But proving that a positive atomic comb with v_n = 2Λ(n)/√n CANNOT be coherent
in (γ, slope) is exactly (E_γ), i.e. (iii). The route reduces to S2; it neither closes it nor moves it.

### 4.4 Consistency theorem for (1)–(7)

**Theorem 4.6 (PROVED by inspection, modulo the NUMERICAL labels of each item).** M₁ (δ = 0.1) satisfies (1)–(7) in all
the computed windows and has witnesses for T > 0.573: (1) Q_δ commutes with J (R186_044 §4.2), its witnesses have pure
parity; (2) the zeros on the line of M₁ are those of ζ (M₁ = ξ × rational factor), and its nearly balanced directions vanish at
them in the same way (same identity (2.1)); (3) the negativity sits at τ ≈ γ₁ = 14.13 < T* for T ≥ 0.4; (4) the sign of M₁ is in G,
not in the diagonal (R186_044/115); (5) it changes sign between boundaries (R186_048); (6) by construction; (7) ν independent
of δ (R186_049). Hence **the conjunction (1)–(7) is satisfiable by an object with witnesses**, and no proof of incompatibility
of (1)–(7) for ζ can be valid unless it uses a property of ζ that M₁ does not have. The only thing M₁ does not have: a Λ side
purely atomic on log ℕ with weights 2Λ(n)/√n (§4.3). This is the falsifier principle of W3 (Paper 48) applied to the list.

### 4.5 Dichotomy of the limit

**Proposition 4.7.** (a) PROVED: L ∈ [−∞, 0]; D ⟺ L = 0; if L = 0 then 0 ≤ λ_A(T) ≤ exp(−e^{(2−ε)T}) for T ≥ T₀(ε) (Thm M(b),
Paper 48, "unconditional in the record", CITED). (b) ARGUED: if L < 0 then L = −∞, with λ_A(T) ≤ −c e^{2δ₀T}/T for some
δ₀ ∈ (0, ½). *Argument.* If 𝒲_{T₀} ≠ ∅ with h*_{T₀} satisfying (b) of lem:roughEF, (2.1) gives a quartet {½ ± δ₀ ± iγ₀} (use of
the identity, not of a criterion), and the family F_T of §4.3 at (γ₀, δ₀) gives (4.1), whose constant is not closed. ∎
There is no intermediate regime: either λ_A ↓ 0 doubly exponentially, or λ_A → −∞ exponentially. Bound (N8) λ_A ≥ C₀ − 𝔄_T ≈
−4e^T is compatible with (b) for every δ₀ < ½ and saturates only at δ₀ = ½ (edge of the band): consistency, with no new content.

## 5. Self-checks

1. lem:monoT reread: extension by zero preserves ‖·‖, A, B, c_F; c_F = 0 for |u| ≥ 2T; new contacts log n ≥ 2T. Lemma 1.3 ✓.
2. lem:contA: continuity of λ_A on (0, ∞) ⇒ 𝒯 open; λ_A(T_c) = 0 by the intermediate value theorem at the boundary ✓.
3. thm:margin: limsup λ_A ≤ 0 (no lower bound). Paper 48 thm:M(b): λ_A ≤ exp(−e^{(2−ε)T}) is an UPPER bound ✓ ((N8) corrects the target).
4. C₀ = ψ(¼) − log π = (−γ_E − π/2 − 3log2) − log π = −4.2274 − 1.1447 = −5.3721 ✓ (matches Paper 47).
5. 𝔄_T ≤ 4.16e^T: Σ_{n≤x}Λ(n)n^{−½} = ψ(x)x^{−½} + ½∫₁^x ψ(t)t^{−3/2}dt ≤ 1.03883(√x + √x), x = e^{2T}; v_n = 2Λ(n)/√n ✓.
6. τ₀ ∈ (5, 7.5): lower bound of lem:mbounds(ii) at 7.5: 0.1770 − 0.1333 − 0.0089 > 0; upper bound at 5: −0.2285 + 0.2 + 0.0050 < 0 ✓.
7. Lemma 3.1: Q = 4|Φ_c|² − 4|Φ_s|² re-derived from Σ_z e^{zu} = 4cos(γu)cosh(δu) (R186_114 §1.1) and Re[Φ(½+z)Φ(½−z)] = P₊P₋ + R₊R₋
 = ¼[(P₊+P₋)² − (P₊−P₋)² + (R₊+R₋)² − (R₊−R₋)²] ✓; ∫_{−T}^T sinh²(δt)dt = sinh(2δT)/(2δ) − T ✓; ∫cosh² = sinh(2δT)/(2δ) + T ✓.
8. Construction 4.3: F̂ = (τ² + ¼)ĝ ⇔ F = (¼ − ∂²)g with convention F̂(τ) = ∫F e^{iτt}; Φ_F(0) = F̂(i/2)·(sign), Φ_F(1) = F̂(−i/2):
 both vanish ✓. g = t sin(γt)η even ✓ ⇒ F even. g″ = 2γcos(γt) − γ²t sin(γt) (without η) ⇒ F = (γ² + ¼)g − 2γcos(γt) + terms in η′, η″ ✓.
9. Parity of Φ_s, Φ_c for F even: ∫F sinh(δ₀t)e^{iγt} = i∫F sinh(δ₀t)sin(γt) (even×odd×odd = even ✓ not zero);
 ∫F cosh(δ₀t)e^{iγt} = ∫F cosh(δ₀t)cos(γt) (even) — with F ≈ (γ²+¼)t sin(γt)η: integrating t sin cos cosh = ½ t sin(2γt)cosh(δ₀t),
 oscillating, of size O(e^{δ₀T}·T/γ) ⇒ |Φ_c|²/|Φ_s|² = O(δ₀²/γ²) ✓ (matches "Φ_c(h*) ≈ ĥ*(γ₁) nodal", R186_044).
10. (4.1): ∫₀^T t sinh(δ₀t)sin²(γt)dt = ½∫t sinh(δ₀t)dt + oscillating = (T cosh(δ₀T)/(2δ₀) − sinh(δ₀T)/(2δ₀²))·(1+o(1)) ≈ Te^{δ₀T}/(4δ₀);
 by symmetry the full interval gives Te^{δ₀T}/(2δ₀); 4|Φ_s|²/‖F‖² ≈ 4(γ²+¼)²T²e^{2δ₀T}/(4δ₀²) ÷ ((γ²+¼)²T³/3) = 3e^{2δ₀T}/(δ₀²T) ✓.
 ‖F‖² ≈ (γ²+¼)²∫t²sin²η ≈ (γ²+¼)²T³/3 ✓. Exponent 2δ₀ and power 1/T match R186_039 (L ≈ −ce^{2δT}/T).
11. Zero density (2π)⁻¹log(τ/2π) vs m(τ) = log(τ/2π) + O(1/τ) (lem:mbounds(ii)): the line term in 4.5(iii) cancels
 the archimedean term to leading order ✓ (same reading as R186_041/113: nodal measure = rewritten roughEF).
12. Corollary 3.2 vs R186_044: S_δ(T) ≈ (2/3)δ²T³ and |ĥ*′(γ₁)|² ≤ ‖h*‖²∫t² = (2/3)T³ give the same form δ_c² ≍ λ_A/T³ ✓.
13. Theorem 4.6: each item checked against the cited file; (1) uses R186_044 §4.2 "Q_δ commutes with reflection" ✓.
14. No line invokes an equivalence of D with another statement; (2.1) and 4.5(iii) use lem:roughEF as an identity and are
 marked CONDITIONAL/circular where they would be used as a criterion ✓. Lemma H (R186_107: ARGUED, not a theorem) is not used.

## 6. Table of labels and loose ends

| statement | label |
|---|---|
| Lemma 1.2, Lemma 1.3, Theorem 1.4(a)–(d), Lemma 1.5 | PROVED (trivial over lem:monoT, lem:contA, thm:margin, R186_048) |
| (N1-a), (N3-a,c), (N4-a), (N5), (N6) Lemma Q/Prop K, (N8) | PROVED |
| (N1-b) | PROVED mod. CITED T ≤ ½log5; CONDITIONAL[W_T|odd ≥ 0] afterward |
| (N2) (2.1) | CONDITIONAL[(a),(b) of lem:roughEF]; circular as a criterion |
| (N3-b), (N4-b) outside the three windows, (N5) jump of M₁, (N7) | NUMERICAL / CONDITIONAL |
| Lemma 3.1, Corollary 3.2 | PROVED |
| (★_k): strictly weaker than D for fixed k, = D in the limit | PROVED (R186_026 Thm 3.3); content = (L2) OPEN |
| Lemma 4.1, Theorem 4.2 (NO-GO of the asymptotic route via frozen witnesses) | PROVED |
| Construction 4.3 (membership in 𝒫_T), Prop. 4.5 (D ⇒ (E_γ)) | PROVED |
| (4.1) law e^{2δT}/T of the adapted family | ARGUED (matches R186_039 NUMERICAL) |
| (E_γ) as a statement on (m, Λ) | actual content, zero side (O2) = S2; NO-GO as zero-free route; OPEN |
| Theorem 4.6 (consistency of (1)–(7) via M₁) | PROVED by inspection mod. NUMERICAL of the items |
| Prop. 4.7(a) | PROVED; 4.7(b) L ∈ {0, −∞} | ARGUED |

**Loose ends remaining:** (H1) is 𝒲_T^{cand} ∩ 𝒫_T^{par} larger than 𝒲_T in any window by a new PROVED condition? (no
candidate); (H2) zero-free (E_γ) = S2 (blank since R166_802); (H3) close the constants of (4.1) (PROVED possible,
without consequence for D); (H4) quantitative Lemma 3.2 of boundary mass for witnesses in (T_c, T_c + ε) (= W-loc, not recommended).

**Row D: OPEN. Contact with the sign: none.**
