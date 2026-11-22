# CA_K_001 — Diamagnetism in both pictures, the holonomy of the +/· frustration, and the signed-Laplacian reading (seeds K8, K6, K7, K9)

Phase 193. Pen and paper; **no numerics run**. Setting: CA_K_000 §1.
**No sign contact. No certified negative value for ζ.** (Negative numbers below
are values of kernels at nonzero shifts, of the archimedean part alone, or of comparison operators — never values of ζ's form.)

Notation. 𝔸_M = 𝖡(0)I + O_M (O_M zero diagonal). For a real symmetric A = D_A + O put d_m := Σ_{k≠m}|O_{mk}|.
δ ∈ (0, ½) is fixed with 𝖡 ≥ ½𝖡(0) on [−δ, δ] (exists: 𝖡 continuous, 𝖡(0) > 0, CA_E_001 Fact 0). J_M := (M/2, M] ∩ ℕ.

**Lemma 0 (many strong additive edges; PROVED).** For m ∈ J_M, #{k ∈ J_M, k ≠ m : 𝔸_{mk} ≥ ½𝖡(0)} ≥ ⌊δM/2⌋ − 1 =: N_δ(M).
*Proof.* For k, m ∈ J_M, |log(m/k)| ≤ |m − k|/min(m,k) ≤ 2|m − k|/M, so |m − k| ≤ δM/2 implies |log(m/k)| ≤ δ. J_M has length M/2 > δM/2,
so on at least one side of m there are ⌊δM/2⌋ − 1 such k inside J_M. ∎

## 1. Diamagnetism in the integer picture (K8)
**Lemma 1.1 (Kato inequality for matrices; PROVED).** For A = D_A + O real symmetric and s ∈ ℂ^M, s*As ≥ |s|^T(D_A − |O|)|s|, where |O| is the
entrywise modulus. Hence λ_min(A) ≥ λ_min(D_A − |O|), and D_A − |O| is the unfrustrated representative (off-diagonal ≤ 0, Perron–Frobenius).
*Proof.* |Σ_{m≠k}O_{mk}s̄_ms_k| ≤ Σ|O_{mk}||s_m||s_k|. ∎ (Direction: the frustrated matrix is bounded *below* by the |couplings| matrix.)

**Theorem 1.2 (the diamagnetic bound is void for 𝔸_M; PROVED).** λ_min(𝖡(0)I − |O_M|) ≤ 𝖡(0)(1 − ½N_δ(M)) → −∞ (M → ∞).
*Proof.* u = 1_{J_M}/|J_M|^{½}: u^T(𝖡(0)I − |O|)u = 𝖡(0) − |J_M|^{−1}Σ_{m≠k∈J_M}|O_{mk}| ≤ 𝖡(0) − ½𝖡(0)N_δ(M) by Lemma 0. ∎
*Reading.* What Kato's inequality throws away is exactly the additive near-diagonal block: there all vectors u_m (Bochner picture) are
nearly parallel and the block is ≈ 𝖡(0)·11^T (positive); |·| turns its off-diagonal into −𝖡(0) and the bound collapses at rate M.

**Proposition 1.3 (the archimedean part is not a |couplings| version and is indefinite; PROVED).**
(a) α is not positive definite on ℝ; hence there is M₁ with Arch_M indefinite for all M ≥ M₁.
(b) Comb_M has zero trace and Comb_M ≠ 0 (M ≥ 2), so λ_max(Comb_M) > 0 and the Weyl comparison λ_min(𝔸_M) ≥ λ_min(Arch_M) − λ_max(Comb_M)
has negative right side for M ≥ M₁.
(c) Under the premise, every unit bottom eigenvector s₀ of Arch_M (M ≥ M₁) has Comb_M(s₀) ≤ λ_min(Arch_M) − λ_min(𝔸_M) < 0.
*Proof.* (a) α(d) = ∫w(τ)cos(τd)dτ with w = m ĉ₀/2π ∈ L¹ (ĉ₀ = F̂₀² ≍ τ^{−4}, m ~ log τ), even and continuous. If α were PD, Bochner
gives α = μ̂ with μ ≥ 0 finite, and uniqueness of Fourier–Stieltjes transforms gives μ = w dτ; but w(0) = C₀ĉ₀(0)/2π < 0 (C₀ = −5.372…,
ĉ₀(0) = F̂₀(0)² = (¼|ĝ(0)|⁴)² > 0), contradiction. So there are d₁, …, d_K and real s with Σs_js_kα(d_j − d_k) < 0; the approximation
m_j = ⌊e^{C+d_j}⌋ of the proof of prop:AM(i) and continuity of α give a negative value of Arch_M for M ≥ max m_j. (b) Diagonal of Div and
Near vanish (prop:AM(iii)); (Div_M)_{21} = v₂/2 > 0. (c) Rayleigh: λ_min(𝔸_M) ≤ s₀^T𝔸_Ms₀ = λ_min(Arch_M) − Comb_M(s₀); λ_min(𝔸_M) ≥ 0 by premise. ∎
(c) is the integer-picture form of P46 l. 196 ("beyond the threshold the primes supply positivity"). It is a necessary property and a
falsifier test; under the premise it holds. Not computed (not strictly necessary).

## 2. Diamagnetism in the t-picture (K8, K9)
For a real comb a on 𝒩_T put 𝔞^a_T(F) := arch_T(F) − Σ_{n∈𝒩_T}2a(n)n^{−½}c_F(log n) (ζ: a = Λ), λ₀(T;a) its bottom on real L²(I_T),
λ_A(T;a) its bottom on 𝒫_T. arch_T(F) = (1/2π)∫m|F̂|² = C₀‖F‖² + ∫_0^∞K(u)(‖F‖² − c_F(u))du.

**Theorem 2.1 (Λ is the diamagnetic extremum; PROVED).** If |a(n)| ≤ Λ(n) on 𝒩_T, then 𝔞^a_T(F) ≥ 𝔞^Λ_T(|F|) for every real F in the form
domain, and λ₀(T;a) ≥ λ₀(T;Λ). (Complex twists a(n) = Λ(n)y(n), |y| ≤ 1, enter real forms through Re y and are covered.)
*Proof.* ‖F‖² − c_F(u) = ½∫(F(t) − F(t+u))²dt ≥ ½∫(|F(t)| − |F(t+u)|)²dt = ‖F‖² − c_{|F|}(u) and K > 0, so arch_T(F) ≥ arch_T(|F|) (this is
CA_I_001 Thm 1(i)); |Σ2a(n)n^{−½}c_F(log n)| ≤ Σv_n c_{|F|}(log n) since |c_F| ≤ c_{|F|}. ∎
Covered twists: a = 0, a = Λ1_S (O1, O3, deletions), a = Λλ (Liouville), a = Λχ for a real character χ (with ζ's archimedean part, not
the form of L(s,χ)), every Steinhaus twist. **In the t-picture ζ's whole form (archimedean + comb) is the "|couplings|" member** of the
family {|a| ≤ Λ}: all its couplings K(u), v_n are ≥ 0 (Markov), and the diamagnetic inequality bounds the *others* from below by ζ.

**Theorem 2.2 (the constrained problem is anti-diamagnetic; PROVED from CITED inputs).**
(i) λ₀(T;Λ) ≤ λ₀(T;0) → C₀ < 0 as T → ∞; hence every lower bound for ζ obtained through |F| (Theorem 2.1-type comparisons, Kato,
Beurling–Deny, Perron–Frobenius) is a lower bound by λ₀(T;Λ) < 0 for T large.
(ii) The diamagnetic order fails on 𝒫_T: at T = 0.7, λ_A(0.7;0) < 0 < λ_A(0.7;Λ), although |0| ≤ Λ. No inequality
λ_A(T;a) ≥ λ_A(T;Λ) (|a| ≤ Λ) holds; the primes *raise* the constrained bottom.
*Proof.* (i) First inequality: CA_I_001 Prop 1.2(a) (0 ≤ Λ). For F_T(t) = φ(t/T), φ ∈ C_c^∞(−1,1) real nonzero, |F̂_T|²/‖F_T‖² concentrates at
τ = 0 at scale 1/T and m is continuous with m(0) = C₀, so arch_T(F_T)/‖F_T‖² → C₀. (ii) λ_A(T;0) = λ^{∞,P}_min(T) < 0 for T > T*_{∞,P}, and
T*_{∞,P} ≤ 0.60 (P46 cor:Tarch and l. 2425–2426, PROVED there); λ_A(T;Λ) > 0 for T ≤ 0.8 (Zhu, CITED via P46 l. 143). ∎
*Reading (key question of the front).* "Is the archimedean Markov part the |couplings| version, so that diamagnetism gives
λ_min(frustrated) ≥ λ_min(|couplings|)?" Answer: the direction of the diamagnetic inequality is correct (frustrated ≥ unfrustrated), but
(1) in the t-picture the unfrustrated member is ζ itself, whose unconstrained bottom is negative, and the sign lives in the constraint
𝒫_T, where the order reverses (Thm 2.2(ii)); (2) in the integer picture the unfrustrated representative of 𝔸_M has bottom → −∞
(Thm 1.2) and the archimedean part is not unfrustrated, not positive, and not a lower comparison (Prop 1.3). Lieb's flux-phase/paramagnetic
results (K9) need reflection positivity (dead, CA_J_001) and concern sums of eigenvalues; the "paramagnetic" reversal relevant here is Thm 2.2(ii).

## 3. Holonomy of the frustration (K6)
Signed graph Σ_M on {1, …, M}: edge {m,k} iff 𝔸_{mk} ≠ 0, sign sgn 𝔸_{mk} (covariance reading of CA_J_002). Switching by ε ∈ {±1}^M.
Holonomy of a cycle = product of its signs. (Harary 1953; Zaslavsky, *Signed graphs*, 1982; CITED): two signings of one graph are switching
equivalent iff their holonomies agree on every cycle, iff on the fundamental cycles of one spanning tree.

**Proposition 3.1 (the flux is the sign of 𝖡; PROVED).** Let m₀ := ⌈1/δ⌉ + 1. For m₀ ≤ k < m ≤ M with 𝖡(log(m/k)) ≠ 0 the cycle
γ_{k,m} = (k, k+1, …, m, k) has holonomy sgn 𝖡(log(m/k)). The path (m₀, m₀+1, …, M) is a spanning tree of Σ_M|_{[m₀,M]} and the γ_{k,m}
(m − k ≥ 2) are its fundamental cycles; hence the switching class of Σ_M|_{[m₀,M]} is equivalent data to the function
(k,m) ↦ sgn 𝖡(log(m/k)). In particular the frustrated +/· cycle C_m = γ_{m,2m} of CA_J_002 has holonomy sgn 𝖡(log 2) for every m ≥ m₀.
*Proof.* log(1 + 1/j) < 1/j < δ for j ≥ m₀, so every tree edge is positive; holonomy of γ_{k,m} = product over tree edges (all +) × sign of
the closing edge. Fundamental cycles generate the cycle space over 𝔽₂. ∎
*Reading (+/·).* The telescoping ∏_{j=m}^{2m−1}(j+1)/j = 2 (the + producing the ·) carries no information beyond the conjunction
"𝖡 > 0 on (−δ,δ)" (additive-only) ∧ "value of sgn 𝖡 at log 2" (one point of log G). The gauge-invariant content of the frustration is
the sign function of 𝖡, nothing more.

**Proposition 3.2 (the switching class cannot decide; PROVED).** Let 𝖡 be continuous, even, 𝖡(0) > 0, 𝖡(d₀) ≠ 0 for some d₀ ≠ 0. There is a
continuous even 𝖡′ with sgn 𝖡′ = sgn 𝖡 everywhere that is not positive definite. Hence no criterion that factors through the switching
classes of the 𝔸_M (balance, frustration index, cycle-sign counts, holonomy group) proves (eq:target): (B″)-type.
*Proof.* g even continuous, g ≥ 1, g(0) = 1, g(±d₀) = 2𝖡(0)/|𝖡(d₀)|; 𝖡′ = g𝖡 has the 2×2 minor 𝖡(0)² − 4𝖡(0)² < 0 at {0, d₀}. ∎
(d₀ exists for ζ: 𝖡(log 2) < −0.27 when 2T₀ ≤ 0.1, Lemma J0′.)

**Proposition 3.3 (no U(1) flux inside the ratio class; PROVED).** For y ∈ Ĝ, [y(m/k)𝖡(log(m/k))] = U_y𝔸_MU_y*, U_y = diag(y(m)); every
U(1) holonomy of a twisted matrix is ∏y(q_i) = y(∏q_i) = y(1) = 1 times the ℤ/2 holonomy. A genuine magnetic flux needs phases ω(m,k) not
of the form f(m)/f(k), i.e. a kernel that is not a function of m/k: outside the M-uniform ratio class of the target (CA_E_001 Remark (scope)). ∎

**Proposition 3.4 (cycle conditions = spherical subadditivity; PROVED; necessary only).** Under the premise, θ(d) := arccos(𝖡(d)/𝖡(0)) ∈ [0,π]
is subadditive on ℝ, and for every cycle the Barrett–Johnson–Loewy cycle inequalities hold (BJL, Mem. AMS 122 (1996) no. 584, CITED).
On C_m: θ(log 2) ≤ Σ_{j=m}^{2m−1}θ(log(1 + 1/j)) → σ log 2 (m → ∞), σ² := −𝖡″(0)/𝖡(0) = −α″(0)/α(0) (𝖡 = α on |d| < log 2 − 2T₀, and α ∈ C²
because ∫|m|τ²ĉ₀ < ∞).
*Proof.* Premise ⇒ the Gram matrices [𝖡(x_i − x_j)/𝖡(0)] are real PSD with unit diagonal ⇒ unit vectors u_x in a real Hilbert space with
⟨u_x,u_y⟩ = 𝖡(x−y)/𝖡(0); the spherical distance is a metric; θ(d + d′) = dist(u₀, u_{d+d′}) ≤ θ(d) + θ(d′). θ(h) = σ|h| + o(h) as h → 0. ∎
These conditions are implied by positivity of any principal submatrix containing the cycle, so their falsifier power is dominated by the
principal-minor computations already in the corpus (EXP_005, NUMÉRICO positive). Not computed.

## 4. Signed Laplacian: frustration as a source of positivity (K7)
**Lemma 4.1 (exact decomposition; PROVED).** For A = D_A + O real symmetric, s^TAs = Σ_{m<k}|O_{mk}|(s_m + sgn(O_{mk})s_k)² + Σ_m(A_{mm} − d_m)s_m²,
i.e. A = L_σ − (D_d − D_A), with L_σ ⪰ 0 the signed Laplacian of (|O|, σ = −sgn O) and D_d = diag(d_m). ∎
L_σ has bottom 0 iff (|O|,σ) is balanced (Harary/Zaslavsky, CITED), so in this reading frustration *raises* the bottom.

**Theorem 4.2 (the target forces near-maximal frustration; PROVED; a rescaling of the target).** Let 𝔸′ = 𝔸_{J_M} (principal block),
ℒ′ = D′^{−½}L′_σD′^{−½} its normalized signed Laplacian (unit diagonal, tr ℒ′ = |J_M|, spectrum ⊂ [0,2]). Then
 𝔸′ ⪰ 0 ⟹ λ_min(ℒ′) ≥ 1 − 𝖡(0)/d′_min ≥ 1 − 2/N_δ(M),   and   λ_min(ℒ′) ≥ 1 − 𝖡(0)/d′_max ⟹ 𝔸′ ⪰ 0.
*Proof.* 𝔸′ = L′_σ − (D′ − 𝖡(0)I) ⪰ 0 ⟺ ℒ′ ⪰ I − 𝖡(0)D′^{−1}, and (1 − 𝖡(0)/d′_max)I ⪯ I − 𝖡(0)D′^{−1} ⪯ (1 − 𝖡(0)/d′_min)I; d′_min ≥ ½𝖡(0)N_δ(M) by Lemma 0. ∎

**Corollary 4.3 (signed Cheeger NO-GO; PROVED from CITED).** The signed Cheeger inequalities (Atay–Liu, Discrete Math. 343 (2020) 111616;
Bandeira–Singer–Spielman, SIAM J. Matrix Anal. Appl. 34 (2013), for connection Laplacians; CITED with their constants) bound λ_min(ℒ)
below by c·ι² with ι ≤ 1 the frustration constant and c ≤ ½. Hence they certify at most λ_min(ℒ′) ≥ ½, while Theorem 4.2 requires
1 − O(1/M). Every frustration-isoperimetric lower bound with a constant-factor loss fails ((B′), [crit]: the target needs relative
precision M^{−3}). From the upper Cheeger inequality λ_min ≤ 2ι (same reference): the premise forces ι(Σ′) ≥ ½ − O(1/M).
*Reading.* The block that saturates Theorem 4.2 is the additive one: on sites with |log(m/k)| < δ, 𝔸 ≈ 𝖡(0)11^T and ℒ ≈ I + (𝟙𝟙^T − I)/(n − 1),
bottom 1 − 1/(n−1). In the L_σ (Hamiltonian) reading the holonomy of C_m is ∏(−sgn 𝔸_e) = (−1)^{m+1}·sgn 𝖡(log 2) = (−1)^m for 𝖡(log 2) < 0 (m+1 edges): it depends on the
parity of the cycle length, not on the +/· structure. The +/· cycle is visible only in the covariance reading (§3), where it is sgn 𝖡(log 2).

## 5. Screens
| item | REF-D | (B″) | O7 / O10 / O11 / O12 | [crit] | (R) | PR | sign content |
|---|---|---|---|---|---|---|---|
| Thm 1.2 | — | comb-generic (any 𝖡 > 0 near 0) | survive | void (rate −M) | (R)(3) | additive block only | NO-GO |
| Prop 1.3 | (c) necessary property | (a) Γ-only (FE-gen) | (a) survives all | — | — | arch only | primes must pay (P46 l.196) |
| Thm 2.1 | — | holds with any comb in the role of Λ | survive | — | (R)(3) | twist of comb (·) × Lévy (+) side by side | wrong direction |
| Thm 2.2 | — | uses Zhu/cor:Tarch at T = 0.7 | — | — | — | — | reversal PROVED: constrained problem anti-diamagnetic |
| Prop 3.1–3.3 | — | yes (any continuous 𝖡) | survive | — | (R)(5) pattern | conjunction | NO-GO for switching-class criteria |
| Prop 3.4 | necessary only | yes (any PD 𝖡) | survive | — | — | — | dominated by principal minors |
| Thm 4.2 / Cor 4.3 | Thm 4.2 = rescaling | — | survive | Cheeger fails | (B′) | additive block | NO-GO for Cheeger family |
(P1)–(P6): no item is non-linear in Λ at a sign step (P2), none reads the minimizer beyond REF-D (P3). FE-generic: every statement
except Thm 2.2(ii) holds verbatim for Epstein/ζ_K forms (they change 𝖡 but not the arguments). G0: Prop 3.4 uses the Gram vectors (premise).

## 6. Self-review
1. *Thm 1.2 is trivial.* Yes; its content is the identification of the lost block (additive, near rank one). It closes "diamagnetic
   comparison in the integer picture" with a rate.
2. *Prop 1.3(a) and the Γ-factor.* Only C₀ < 0 and ĉ₀(0) > 0 are used; any FE form with the same Γ-factor shares it. It is not a sign step;
   it removes Arch_M as a reference operator.
3. *Thm 2.1 vs CA_I_001 Prop 1.2(a).* Prop 1.2(a) compares nonnegative combs (monotone); Thm 2.1 compares signed and complex twists
   with |a| ≤ Λ (diamagnetic). The extension is elementary; its use is Thm 2.2: the order reverses on 𝒫_T, so no diamagnetic route.
4. *Thm 2.2(ii) uses certified values.* P46 cor:Tarch (PROVED in P46, interval arithmetic) and Zhu (CITED). No zero data.
5. *Prop 3.1 needs 𝖡 ≠ 0 on the closing edges.* Edges with 𝖡 = 0 are absent; the spanning-tree argument is unaffected.
6. *Cor 4.3 constants.* The NO-GO uses only "lower bound ≤ ½ when ι ≤ 1"; exact constants in Atay–Liu / BSS are CITED, not re-derived.
   The structural statement (needed 1 − O(1/M) vs any bound with a fixed loss) is PROVED by Thm 4.2.
7. *Equivalences.* Theorem 4.2 and Prop 1.3(c) are internal restatements/consequences of (eq:target); no equivalence with any statement about
   another object is invoked.
**Verdict.** K8: NO-GO in both pictures (PROVED); answer to the key question: the frustration cannot be used diamagnetically — the
unfrustrated comparison is void (integer picture) or is ζ itself with negative unconstrained bottom, and the constrained order is reversed
(t-picture). K6: flux = sgn 𝖡 (PROVED), insufficient (PROVED). K7: exact decomposition; the target is near-maximal frustration (rescaling);
Cheeger family NO-GO. K9: DISCARD.
