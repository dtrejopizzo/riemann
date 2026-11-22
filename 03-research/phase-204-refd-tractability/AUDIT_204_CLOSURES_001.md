# AUDIT_204_CLOSURES_001 — audit, step 4 of phase 204: is any of the five closures wrong?

Phase 204.
ARGUED / OPEN / NO-GO / NUMERICAL. Write only this file.

Sources verified by hand: L2_INTERLACE_001, P1_BBSTAR_001, POLAR_CAP_001, LEMMA_F_HALFLINE_001, P2_SCHUR_001; Paper 46
main.tex: thm:coer-schur (l.5207, definition of S_{T,k}), thm:parityschur (l.4176), prop:polarcap (l.4316), lem:gmono (l.4715),
prop:onewindow, rem:polarcapdiag (l.11151), def:W/eq:nuw (l.1193), prop:opcalc and thm:sos (l.8236–8270), def:ext, thm:ext-half
(l.9692), rem:ext-killing, prop:ext-gauge (l.9725); R186_025 (Theorems A/B), Q2_LADDER_001 §1 (Lemma R).

## Summary (≤300 words)

None of the five closures is WRONG at its core; two are PARTIAL and there is one false statement inside a memo.

1. **L2_INTERLACE: CONFIRMED.** The definition of S_{T,k} (thm:coer-schur) confirms that k is the number of blocks; S is
   continuous and of fixed size at the contacts. The existing finite matrices indexed by contacts (Gram of translates, 4×4 from
   R186_024, 2×2 from thm:parityschur) are either functionals of the vector or already NO-GO or of fixed size. Normalization
   erratum v_7 (factor 2).
2. **P1_BBSTAR: CONFIRMED in K1/K2/K3-polarized; the "no candidate" residue is false as a statement**: there is an obvious
   structural non-convolutive B (evaluation at zeros, rem:ext-killing(iii)), but it inverts the scheme (the identity is PROVED,
   positivity is the content). P1.A is correct and almost trivial.
3. **POLAR_CAP: CONFIRMED as a route, with a false statement in §4.3**: the formula 𝔞_T(h_par) = 1/q_par,
   q_par = ⟨χ_par,𝔄^{−1}χ_par⟩, holds with only invertibility of 𝔄 on the whole sector (positivity is not needed), and the even
   channel **is** a capacity, with q_ev < 0. This gives a criterion without λ_A (Lemma WT below, PROVED) and forces the index's
   reopening clause to be tightened. PC-2 correct.
4. **LEMMA_F: PARTIAL.** F⁻ is exact (verified by hand) but compactly-supported ρ is **outside** the admissible class
   (Paley–Wiener restrictions are analytic). In the admissible class the NO-GO is NUMERICAL + ARGUED; the variant "there exists
   a gauge that convexifies" was not considered and remains OPEN.
5. **P2_SCHUR: CONFIRMED.** Lemma R gives radicality of the complete form (archimedean included) under g core C², Tate moment
   at the pole zero. Outside the class: g with that moment ≠ 0 (polar coupling of rank ≤ 1, ARGUED reducible to 𝔊_T) and
   infinite P (Q-P2.2).

Integrable into P46: Lemma T3 (remark), extension of thm:sos (one sentence), Lemma 2.7 (remark), PC-2 (sentence in
rem:polarcapdiag), Lemma WT (new, proposition). F⁻ and P2-S.3 not.

---

## 1. L2_INTERLACE_001

### 1(a) Correctness of the proof

**Definition verified.** P46 thm:coer-schur: 𝒱 = 𝒱_k ∩ 𝒟_T (Tate per block, k equal blocks), E_k (2k−2 dimensions, piecewise
Tate exponentials e^{±t/2}1_{B_j}), 𝔰_{T,k}(e) = 𝔞_T(e) − 𝔞_T(𝖪e), S_{T,k} its matrix. Requires c(T,k) > 0 (cor:coer-L1). The
memo §1 agrees word for word. Hence (a) "k = blocks, not contacts" is correct: TRACT_001 R13(d) was wrong.

**(c) Continuity at the contact.** Correct: by lem:monoT/U0, the new term −v_n𝒞F(log n) is 0 at T = T_n for F supported in
I_{T_n}; the basis E_k dilates continuously; 𝖪 depends continuously (Lax–Milgram with c(T,k) > 0 uniform on compacts). PROVED.

**Lemma J (verified).** q_n(F) = −v_n∫_{−T}^{T−log n}F(x)F(x+log n)dx. Differentiating at the limits: the upper limit
contributes F(T−log n)F(T) and the lower F(−T)F(−T+log n); at T = T_n both equal F(−T)F(T); the T-dependence of the elements
of E_k contributes δ·O(1) → 0. Total −2v_nF(−T_n)F(T_n). Correct. The reading "basis artifact" is ARGUED (consistent with
INV_U_001 U5b, which is indeed intrinsic); it is not a statement the NO-GO rests on.

**T13.1.** The Hellmann–Feynman identification at the crossing (λ_min(S) = 0 ⟺ λ_A = 0 and the null vector of S extends to that
of 𝔞_T|𝒫_T via v = −𝖪e) is correct by eq:coer-schur. The codimension argument (W3) applies literally in finite dimension.
Correct.

**Erratum (minor, does not change the verdict).** §4.5 writes v_7 = Λ(7)/√7 = 0.7355; in P46 (def:ext, thm:sos)
v_n = 2Λ(n)/√n, so v_7 = 1.471 and the jump of Lemma J is 2v_7F(T)² ≈ 2.94·F(T)², not 1.47. The memo's header
("v_n = Λ(n)/√n·(…)") inherits the ambiguity. Correct it.

### 1(b) Delimitation of the class and what is left out

The objective asks whether **no** natural finite matrix exists that changes by a border at the contacts. I reviewed the
candidates:

- **Gram of translates in the contact basis** {e^{±t/2}1_{I_T}} ∪ {τ_{log n}h : n ∈ 𝒩_T} for a fixed h. It does get bordered
  when n enters (a new row/column) and Cauchy applies. But it is the matrix K_r(m,n)/I(m,n) from thm:ext-half and from
  LEMMA_F: it is indexed by a vector h; its relation to λ_A is by evaluation at a vector (W(F) is linear in the comb, not a
  complement of that Gram). Any sign statement using this matrix is a functional of the chosen vector; if the vector is the
  minimizer, it is 𝒦_H; if fixed, it is an upper bound. It gives no lower bound. Outside the memo's class but falls into
  𝒦_H/W-lin.
- **Dual multiplier matrix** (def:W/eq:nuw certificates with atoms at log n): its support does grow at the contacts, but it is
  an LP/cone (def:PD, thm:D1), not a symmetric matrix whose eigenvalue is λ_A; it admits no interlacing.
- **thm:parityschur block**: fixed 2×2 (𝔊_T), does not change size; Lemma T3 places it above S_{T,k}.
- **Schur 4×4 along T (R186_024)**: indexed by contacts 2,3,4,5; already NO-GO (R186_104).

Conclusion: I found no natural finite matrix, independent of the vector, whose size changes at the contacts and whose sign is
that of λ_A. The class is well delimited.

### 1(c) Independent PROVED sub-results

- **Lemma T3** (inertia tower): n_−(W_T) = n_−(S_{T,k}) + n_−(𝔊_T), n_0 analogous, under c(T,k) > 0 and
  0 ∉ spec(𝔞_T|𝒫_T ∩ 𝒟_T). Verified: thm:parityschur(c) gives n_−(W_T) = n_−(𝔞_T|𝒫_T) + n_−(𝔊_T), and eq:coer-schur with
  𝔞_T ≻ 0 on 𝒱 gives n_−(𝔞_T|𝒫_T) = n_−(S_{T,k}) and n_0 equal (v ↦ v + 𝖪e bijective). **Passes** as a Remark after
  thm:coer-schur (state it in n_−, n_0; "In(𝔞|𝒱_k) = (∞,0,0)" is not written in the paper).
- Lemma J: correct but basis-dependent; **do not integrate**.
- Correction of the reason for lem:monoT (contact = indefinite exchange, monotonicity by zero-extension): is already the proof
  of lem:monoT; no need to integrate.

### 1(d) Verdict: **CLOSURE CONFIRMED** (T13.1 and T13.2 NO-GO). (L2) as objective remains OPEN.

---

## 2. P1_BBSTAR_001

### 2(a) Correctness of the proof

**thm:sos (P46 l.8256) verified.** The proof uses only: (i) Σ|D_i|² ≥ 0 pointwise ⇒ μ_0 ≥ sup S_T = 𝒜_T (lem:mbounds(iii));
(ii) 𝔪_T − μ_0 ≥ 0 on 𝒫_T ⇒ λ_{∞,P} ≥ μ_0; (iii) 𝒜_T ≥ v_2 = 0.9802 > 0.311 ≥ λ_{∞,P}(T) for T ≥ ½log3. The frequencies of
D_i do not come into play. Audit remark: even in the original thm:sos, |D_i|² with D_i in n^{iτ} already has atoms at
log(m/n) ∈ log ℚ, which must cancel within the sum; so the "extension to log ℚ" is literal and the extension to arbitrary ℝ
also holds. **Theorem P1.A: PROVED, legitimate, but is a one-line observation**, not a new theorem. The weights (Λ, μ, Λ₂,
log) are irrelevant: the proof does not see them. Correct.

**Lemma 2.7 verified.** c(p^j/q^i) = Λ(q^i)Λ(p^j)(q^ip^j)^{−½} = log p·log q·(p^jq^i)^{−½}; the representation of p^j/q^i as a
ratio of two prime powers is unique. log(p/q) ∉ log ℕ. Missing step (I add it): equality of forms on 𝒫_T (codimension 2) is
equality of measures **modulo the annihilator of {c_F : F ∈ 𝒫_T}**; that annihilator contains no atoms, by prop:cone(ii) (for
each a ∈ (0,2T) there exist F_± ∈ 𝒫_T with c_{F_±}(a) = ±1 and autocorrelation support concentrated). With that step: PROVED.

**Identity §2.8** σ_T = |1 − ĉ|² + (m − 1 − |ĉ|²): verified (S_T = 2Re ĉ with v_n = 2Λ/√n). Correct.

**Prop 3.1** (term-by-term polarization): correct modulo prop:primeblind.

**Lemma 1.1 / Cor 1.2**: trivial and correct.

### 2(b) Delimitation and what is left out

- **B = mollifier** (M_μ(∂) or Σ μ(n)n^{−½}D_n): convolutive ⇒ K1; P1.A if the archimedean part pays a constant, def:PD if
  not. Covered.
- **B on the extended carrier** (thm:ext-half, modulo the Guo radical): by Lemma 1.1, B̃ = Bι acts on g via Ψ̌_g, whose symbol
  is ĝ·D_μ (identity T.1); B̃ is again convolutive in g with symbol b·D_μ ⇒ K1. Covered (the memo does not say so; I add it).
- **B = "square root of the zero side"**: rem:ext-killing(iii) (PROVED) gives W_T(Ef) = Σ_ρ Φ_{Ψ_f}(ρ)Φ_{Ψ_f}(1−ρ), and
  thm:Z gives f_w = Σ_ρ ŵ(τ−γ_ρ). This is a B **non-convolutive with a PROVED structural identity**: B: g ↦ (Φ_g(ρ))_ρ. Hence
  the memo's statement "K3 residue: empty candidate class" is **false as a statement**. But the candidate does not fit the P1
  scheme: the expression Φ(ρ)Φ(1−ρ) is |Φ(ρ)|² only when 1−ρ = ρ̄, so here the identity is the proven part and the B*B
  character is the content (datum of the location of the ρ). The P1 scheme ("B*B tautological, the content in the identity")
  is inverted. Classification: outside P1, in the already indexed spectral family (A_MU (a), thm:Z, REF-D). Does not reopen
  P1.
- What the memo correctly leaves open: "PSD on 𝒳_T by a non-factored argument" = the h⁰/𝔇-Sch row (indexed).

### 2(c) PROVED sub-results

- **P1.A**: passes as **one sentence** in thm:sos ("the frequencies of D_i may be arbitrary real numbers; the proof uses only
  pointwise nonnegativity"). Not as a separate theorem.
- **Lemma 2.7**: passes as a Remark after thm:sos, with the annihilator step via prop:cone(ii).
- Identity §2.8: correct but contributes nothing; do not integrate.

### 2(d) Verdict: **CLOSURE CONFIRMED** for BB* (K1, K2, K3 polarized, extended carrier). Correct the residue statement:
"class with one structural candidate (evaluation at zeros) that is not tautological B*B; no candidate from the arithmetic
side."

---

## 3. POLAR_CAP_001

### 3(a) Correctness of the proof

**§1 (TRANSFER).** Correct against thm:parityschur(a): the definition uses only 0 ∉ spec(𝔞_T|𝒬^par_T); (a3), (a4), (c) and
lem:gmono use λ^par_A > 0.

**PC-1.** Verified: lem:gmono (with λ^par_A > 0 at both T), prop:onewindow(i) and λ^W ≤ λ_A. Correct.

**PC-2 verified.** For F ∈ 𝒟^par_{T_0}, zero-extension preserves parity, ℓ_par and W (proof of lem:gmono); by (a3) at T,
𝔤_par(T) ≤ W_T(F/ℓ(F)) = W_{T_0}(F)/ℓ(F)². Precision: only λ^par_A(T) > 0 **at T** is needed (not throughout [T_0,T]); the
memo asks for more than necessary. PROVED.

**The number 9·10⁻⁸.** rem:polarcapdiag explicitly states that a Galerkin 𝔤 is a minimum over a subspace, hence W at an
explicit test with ℓ = 1, hence an upper bound of the true 𝔤 (given λ_A > 0). With PC-2 the bound propagates to every
T ≥ ½log3 with λ^ev_A(T) > 0. Correct as NUMERICAL (not certified: quadrature/rounding; certifiable with an interval
evaluation).

### 3(b) Does every use of 𝔤 consume λ_A > 0? — **No: a false statement in §4.3**

Memo §4.3 says that 𝔞_T(h_par) = 1/⟨χ_par, 𝔄_T^{−1}χ_par⟩ requires 𝔞_T|𝒟^par ≻ 0 and concludes "the even channel does not
admit the capacity formula." I verify: let 𝔄_par be the operator of 𝔞_T on **the whole** sector 𝒟^par_T (archimedean **plus
comb**, with no Tate restriction; it is not just the archimedean part). If 0 ∉ spec(𝔄_par) and
q_par := ⟨χ_par, 𝔄_par^{−1}χ_par⟩ ≠ 0, then h := 𝔄_par^{−1}χ_par / q_par satisfies ℓ_par(h) = 1 and
𝔞_T(h,G) = ℓ_par(G)/q_par = 0 for G ∈ 𝒬^par; by the uniqueness of thm:parityschur(a), h = h_par and 𝔞_T(h_par) = 1/q_par.
**Positivity is not used.** With rem:polarcapdiag (𝔞_T(h_ev) ≈ −2): q_ev ≈ −½, and the even channel is a capacity with
negative q. The statement "does not admit" is false; what is true is "does not admit the formula with 𝔄 ≻ 0."

**Lemma WT (Weyl–Tate; PROVED, inertia algebra of a rank-one perturbation, Haynsworth on the bordered matrix
[[𝔄, χ],[χᵀ, −1/(2ε)]]).** Suppose 0 ∉ spec(𝔄_par) (operator with compact resolvent, n_−(𝔄_par) < ∞) and
q_par ∉ {0, −ε_par/2}. Then W_T|𝒟^par = 𝔄_par + 2ε_par ℓ_par², and
- even (ε = +1): n_−(W_ev) = n_−(𝔄_ev) if q_ev > −½; n_−(W_ev) = n_−(𝔄_ev) − 1 if q_ev < −½;
- odd (ε = −1): n_−(W_odd) = n_−(𝔄_odd) if q_odd < ½; n_−(W_odd) = n_−(𝔄_odd) + 1 if q_odd > ½.
Hence W_odd ≻ 0 ⟺ 𝔄_odd ≻ 0 and q_odd < ½; W_ev ≻ 0 ⟺ [n_−(𝔄_ev) = 0 and q_ev > −½] or [n_−(𝔄_ev) = 1 and q_ev < −½].
(The proof requires the infinite-dimensional case: 𝔄 closed, semibounded, compact resolvent — exactly what is established in
the proof of thm:parityschur(a) for 𝔞_T — and the reduction to the bordered matrix over the finite negative spectral space
plus a coercive complement; same technique as (a2).)

Reading: the criterion does not go through (𝔞_T|𝒬^par)^{−1} nor through λ_A, but through the inertia and resolvent of 𝔞_T on
the whole sector. NUMERICAL (from rem:polarcapdiag): n_−(𝔄_ev) = 1, q_ev + ½ ≈ −2·10⁻⁸; n_−(𝔄_odd) = 0, q_odd ≈ ½ − O(10⁻⁴).
The odd channel is "𝔞_T ≥ 0 on all odd functions with no Tate condition" plus a capacity; the even one is "exactly one
negative square of 𝔞_T on the even sector" plus a capacity.

**Does it reopen route R6?** Not as a sign route: 𝔄_par^{−1} is another resolvent of the same form, and "n_−(𝔄_ev) = 1" and
"𝔄_odd ≻ 0" are statements of the same type as λ_A > 0 (they count negatives of 𝔞_T on a different codimension-1 space).
Every T-derivative of q_par is a functional of 𝔄^{−1}χ (𝒦_H). **But** the index's reopening clause ("do not retry without an
object that does not go through (𝔞_T|𝒬)^{−1}") is trivially satisfied by q_par: it must be tightened to "without an object
that does not go through a resolvent of 𝔞_T on any subspace of the window."

### 3(c) PROVED sub-results

- **PC-2**: passes; integrate as one sentence in rem:polarcapdiag ("by Lemma gmono and (a3), the even value 9·10⁻⁸ bounds
  𝔤_ev(T) above for every T ≥ ½log3 with λ^ev_A(T) > 0"), numerically labeled.
- **PC-1**: is prop:onewindow + lem:gmono; do not integrate as new.
- **Lemma WT** (from this audit): passes as a Proposition after prop:polarcap; verified against the notation of
  thm:parityschur (χ_par, ℓ_par, ε_par, h_par). Requires writing the infinite-dimensional case (following the proof of (a)).
  It is a structural result, not a sign result.

### 3(d) Verdict: **CLOSURE CONFIRMED** (T6.1, T6.2 NO-GO/TRANSFER), with correction of §4.3 and tightening of the index
clause. Nothing returns to YES.

---

## 4. LEMMA_F_HALFLINE_001

### 4(a) Hand verification of Theorem F⁻

S_ε(s) = Σ_n n^ε[φ(ns) + cφ(ns/2)], s ≥ 1, supp φ ⊂ (ω₀−w, ω₀+w) ⊂ (1.2, 1.5) (because w < ω₀ − 1.2 and w < 0.05).
- φ(ns) ≠ 0 ⇒ ns ∈ (1.2,1.5); with s ≥ 1, only n = 1 (n = 2 requires s < 0.75).
- φ(ns/2) ≠ 0 ⇒ ns ∈ (2(ω₀−w), 2(ω₀+w)) ⊂ (2.4, 3.0): n = 1 gives s ∈ (2.4,3); n = 2 gives s ∈ (ω₀ ± w); n = 3 gives
  s ∈ (0.8,1), excluded because 2(ω₀+w) < 3; n ≥ 4 excluded.
Hence S_ε = (1 + c2^ε)φ(s) on (ω₀ ± w) and cφ(s/2) on (2ω₀ ± 2w); disjoint (ω₀ > 3w). The nonzero pieces are the pairs
(n, piece) = (1, φ), (2, φ(·/2)), (1, φ(·/2)); the only nonzero cross product is (1,φ)×(2,φ(·/2)) — that is, in the notation
K_r(m,n), only K(1,2) = K(2,1) ≠ 0 off-diagonal; all other cross terms vanish by support. F = λ‖φ‖²[(1 + c2^ε)² + 2c²]
(∫φ(s/2)² = 2‖φ‖²). d²/dε²(1 + c2^ε)²|₀ = 2c²(log2)² + 2(1+c)c(log2)² = 2c(1+2c)(log2)². **Correct formula.** F″(0) < 0 for
c ∈ (−½, 0). Cor F⁻.1 correct via disjoint supports.

### 4(b) Admissibility: the exact falsifier is **outside** the relevant class

In the class of def:ext/thm:ext-half, r = r_f is the restriction to (λ,∞) of 𝓕f with f supported on a compact set: r is the
restriction of an entire function; if it vanishes on an open interval it is identically 0. ρ_c has compact support in (1,∞),
so it **is not admissible**. Moreover the condition g(T) = 0 and the gauge are untouched. Therefore:
- "Universal Lemma F on C_c^∞(1,∞)": NO-GO PROVED (F⁻).
- "Lemma F on the admissible class": NO-GO supported on (i) density + continuity of F″ in weighted norm — **ARGUED**, the L²
  density of PW restrictions on (λ,∞) is correct (Hahn–Banach + holomorphy on the half-plane), the version with weight
  ω^{1+δ} and with g(T) = 0 is not written; (ii) v_min of T10.1 — **NUMERICAL**, with no fixed gauge and no g(T) = 0. The
  memo correctly labels F⁻.2 as ARGUED, but its §7 ("Route 3: closed") and the index ("NO-GO") present it as PROVED. It must
  remain NO-GO (NUMERICAL+ARGUED) in the admissible class.
- **Variant not considered: gauge-existential Lemma F.** W is gauge-invariant (prop:ext-gauge); F is not. The use of Lemma 6.1
  only requires: for each class [r] mod 𝒢̄_T there exists **one** representative whose F is convex on [0,ε]. F⁻ is a
  statement about a vector, not about the class; with 𝒢̄_T infinite-dimensional, the existence of a convexifying
  representative is not refuted. If it held with uniform ε, inf_{[r]} sup_{gauge} L_r(ε) > 0 would suffice for positivity;
  the memo §6.4 mentions it ("one could maximize over the gauge") and dismisses it as "a bound per vector" without
  analyzing it. **OPEN**, not indexed. Expected value low (the quantity sup_gauge L is still a minorant of W, and the inf-sup
  problem is at least as hard), but it is an honest reopening of the statement.

### 4(c) PROVED sub-results

- Theorem F⁻ and Prop 5.1/5.2 are correct and independent, but the objects (Z^{(ε)}, Lemma F from A_MU) are not in P46; P46
  only has Z_log in thm:ext-half. **Do not integrate** unless A_MU is integrated (f); at most a footnote after thm:ext-half
  ("ε ↦ ‖Z^{(ε)}r‖² is not convex in general; counterexample with compact support"), noting that the counterexample is not
  admissible.
- Lemma 6.1: correct, conditional per vector; do not integrate.

### 4(d) Verdict: **PARTIAL CLOSURE.** Closed: universal Lemma F on C_c^∞ (PROVED). Downgraded: in the admissible class
(NUMERICAL + ARGUED, not PROVED). Reopened as OPEN: **gauge-existential Lemma F** (for each class mod 𝒢̄_T, a representative
with convex F on [0,ε], uniform ε). Does not return to YES; moves from NO-GO to OPEN-low-priority.

---

## 5. P2_SCHUR_001

### 5(a) Correctness of the proof

**Lemma R (Q2_LADDER §1) verified.** Hypothesis: g in the core (real, C², vanishes to second order at ±T), and the Tate
moment corresponding to the pole, 𝓕F(0) = 2∫g(s)e^{−s/2}ds = 0 (the memo calls it A(g); the proof uses the integral with
e^{−s/2}, which in P46's convention is B; there is a letter inconsistency between statement and proof in Q2_LADDER — the
content is "the moment that kills ζ's pole" and nothing changes). With F(t) = t^{−½}g(−log t), ζP(∂)g = Φ_{F_P}(−y) and F_P
satisfies the hypotheses of Guo L4.4 (the same ones prop:ext-gauge uses for the gauge). Guo L4.4 gives radicality of the
**complete Weil distribution** 𝒲 from def:ext: archimedean term + full comb + 2AB. **It does include the archimedean part**:
radicality is read on the zero side (Φ_R(ρ) = ζ(ρ)P(ρ)Φ_g(ρ) = 0 for every nontrivial zero, and the absence of a pole at
s = 1 from the zero moment), and the explicit formula distributes that zero across the three terms. Membership of R_P in the
domain of 𝒲 (decay e^{−3|y|/2}) is PROVED in Q2_LADDER (Poisson + 2 IBP).

With that, P2-S.1 (a)–(c) is immediate and correct; P2-S.2 (generalized Haynsworth with null block) correct; V3 (levels)
correct.

**Lemma P2-S.3**: correct and elementary ((i) the radical part separates; (ii) diagonal block ⇒ additive inertia;
(iii) circularity).

### 5(b) What is left out

- **g with nonzero polar moment.** Then R_P = radical + polar defect: 𝒲(R_P, X) is a rank-1 functional in X (proportional to
  the residue of ζP at s = 1 times the moment of X at the other pole). This gives a 𝒲_AB of rank ≤ 1, nonzero: satisfies
  P2-S.3(ii). But the resulting block is the polar channel of thm:parityschur/prop:polarcap (prescribing Φ at {0,1}), i.e.
  𝔊_T. ARGUED: it reduces to POLAR_CAP (TRANSFER). Not indexed as such; I record it.
- **Infinite P / near-radical** (Q-P2.2): the memo correctly leaves it OPEN.
- A-blocks defined by non-Euler arithmetic objects (e.g. pair forms h⁰): outside, already in the h⁰ row.

### 5(c) Sub-results

- P2-S.1 extends prop:ext-gauge (gauge ⊂ radical) to Euler combs. **Would pass** as a Remark after prop:ext-gauge if Lemma R
  is integrated with its explicit hypothesis (g core, zero polar moment, CITED Guo L4.4); the source is Q2_LADDER, not this
  memo.
- P2-S.3: elementary, methodological; **do not integrate** (it is a search specification, not mathematics of the paper).

### 5(d) Verdict: **CLOSURE CONFIRMED.** Note: the residue "g with nonzero polar moment" reduces (ARGUED) to 𝔊_T.

---

## 6. Verdict table

| Memo | Proof | Class | Verdict | What reopens |
|---|---|---|---|---|
| L2_INTERLACE_001 | correct (erratum v_7 ×2) | well delimited | CONFIRMED | nothing |
| P1_BBSTAR_001 | correct; P1.A trivial; L2.7 needs the annihilator step | BB* covered (incl. extended carrier) | CONFIRMED | nothing; correct "empty class" (there is a spectral B, not tautological B*B) |
| POLAR_CAP_001 | PC-1, PC-2 correct; §4.3 false | route well closed | CONFIRMED + correction | Weyl–Tate criterion without λ_A (Lemma WT); tighten index clause |
| LEMMA_F_HALFLINE_001 | F⁻ exact | falsifier outside the admissible class | PARTIAL | gauge-existential Lemma F: OPEN; admissible class: NO-GO only NUMERICAL+ARGUED |
| P2_SCHUR_001 | correct | well delimited | CONFIRMED | nothing (nonzero polar moment ⇒ 𝔊_T, ARGUED) |

No closure is WRONG. No route returns to YES.

## 7. Independent PROVED results from phase 204 that serve as input

1. **Lemma T3** (n_−(W_T) = n_−(S_{T,k}) + n_−(𝔊_T), n_0 likewise) — integrate as a Remark after thm:coer-schur.
2. **thm:sos with arbitrary real frequencies** (P1.A) — one sentence in thm:sos.
3. **Lemma 2.7** (atoms log p·log q/√(pq) of 𝒞^*𝒞 at log(p/q); no multiple of 𝒞^*𝒞 differs from 𝔞_T by a measure on
   log ℕ ∪ a.c.) — Remark after thm:sos, with the step via prop:cone(ii).
4. **PC-2** (𝔤_par(T) ≤ W_{T_0}(F)/ℓ(F)², T ≥ T_0) — sentence in rem:polarcapdiag; with Galerkin: 𝔤_ev ≲ 9·10⁻⁸ ∀T ≥ ½log3
   (NUMERICAL).
5. **Lemma WT** (this audit): 𝔞_T(h_par) = 1/q_par with only invertibility of 𝔄_par on the whole sector; inertia of W per
   sector via (n_−(𝔄_par), sign of q_par ∓ ½) — Proposition after prop:polarcap (write the infinite-dimensional case).
6. **Theorem F⁻** (outside P46; index input): ε ↦ ‖Z^{(ε)}r‖² is not convex on C_c^∞; log-convex on the cones K_r ≥ 0, ρ ≥ 0.
7. **Lemma P2-S.1 / P2-S.3** (methodological input; P2-S.1 depends on Lemma R from Q2_LADDER).
8. **Lemma J** (derivative jump −2v_nF(−T_n)F(T_n) in basis E): correct, basis-dependent; index only.

## 8. Index entry (ROUTES-TRIED-INDEX, phase 204)

- **AUDIT_204_CLOSURES_001 (phase 204, audit, reverse request):** five closures audited; none wrong.
  L2_INTERLACE, P1_BBSTAR, P2_SCHUR CONFIRMED; POLAR_CAP confirmed with correction (§4.3 false: 𝔞_T(h_par) = 1/⟨χ,𝔄_par^{−1}χ⟩
  with only invertibility on the whole sector; Lemma WT PROVED: per-sector inertia criterion without λ_A; even channel = one
  negative square of 𝔞_T + capacity with q_ev < −½); POLAR_CAP's reopening clause tightened to "no resolvent of 𝔞_T in the
  window." LEMMA_F PARTIAL: F⁻ exact but not admissible (compact support vs PW restriction); in the admissible class
  NO-GO = NUMERICAL+ARGUED; **OPEN: gauge-existential Lemma F** (a convexifying representative per class mod 𝒢̄_T). Errata:
  v_7 (L2_INTERLACE §4.5, ×2), "empty class" in P1 (there is a spectral B, not tautological). Integrable into P46: Lemma T3,
  P1.A (sentence), Lemma 2.7, PC-2, Lemma WT.
