# RFIN_TRACT_001 — Tractability review: the finite reformulation "n₋(𝔄_N(T)) = 1 ∀T" (phase 205, part R-fin)

Pure mathematics, no new computations. The numerical input used is
CALIB_R5 and is cited as NUMERICAL.

Criterion from phase 204:
- **TRACT = YES** if there is a genuine path, i.e. a general theorem plus a missing hypothesis that is not the sign.
- **TRANSFER** if the problem reduces to an already-registered open problem.
- **NO** if the statement is the target in different coordinates.

## Summary (≤250 words)

**Verdict: TRACT = NO.** It is REF-D in block form (N3 / L205.★ weakened in one direction), with death criterion M1
for every size-based proof.

**(1) Direction.** The implication D^ev ⇒ n₋(𝔄_N) ≤ 1 is PROVED, by restriction and Weyl. The converse does not
follow: P1.c′ is OPEN and its 𝓕_T half is M1.
- The finite statement with N = N(T) is **strictly necessary in the abstract class** (NUMERICAL): per CALIB_R5,
  Epstein satisfies it at N(T) for T ≤ 3, but its hyperbolic pair only appears at 4N.
- There is an ARGUMENT (ARGUED) that, ∀T, the 1/γ leakage of the sines eventually catches any hyperbolic pair. In
  that case the finite statement would have full strength.
- This is decided by a calibrator: Epstein at N(T) for T = 4…7.

**(2) Szegő paradox: resolved.** The comb's main term is not a symbol on E_N. By (R1) it is exactly 𝔢 − 2ℓℓᵀ: a
negative rank one plus a kernel ≻ 0 with symbol 1/(¼+τ²).
- What remains is Φ_N = −𝓕_T compressed, with "symbol" σ^E_T.
- Szegő/Widom/Avram–Parter do not apply, because the sampling is **critical**: the support in u of c_{kk′} is
  [0, 2T], equal to the window length. That is why σ^E_T oscillates at the same scale 1/T that resolves the basis.
- The matrix's positivity is not pointwise, but it does not average out to anything useful either.

**(3) Difference from N3.** The canonical block and the cancellation within the block change the **size**: ≈2T
versus exponential k(T) in (L2). They do **not** change the logical class: the statement is still the compression
of the target form.

**(4)** There is a constructible finite lemma: RF.1, an exact three-term identity plus a Weyl budget.

---

## 0. Index and corpus

I ran grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` with the requested terms:
- "Toeplitz": 24 hits. Among them P45-1 (Weil–Toeplitz C*, NO-GO), G8A-phase-118/W3 (Toeplitz/Hankel in log n, DEAD)
  and G8D-R164_502c (Szegő–Widom for σ_T, DEAD).
  - The reading in R164_502c is L0: σ_T(0) ≤ ψ(¼) − log π < 0, the symbol is never positive and the positive symbol
    is REF-D.
- "Hankel": 17 hits.
- "Szegő": 5 hits. Among them W-det (R186_034 Thm 3.1: every determinant that decides the sign factors as λ_A·R).
- "inertia": 19 hits (R183_031, R184_004).
- "(L2)" and "S_{T,k}": R186-ThmAB, L2_002, L2_INTERLACE_001.
- "N3": SPEC_SIGN_OBJECT_004, "block inertia = D in block," and SPEC_008 V6.
- "BARRIER_W": 8 hits (class 𝒦_W).
- "explicit matrix" and "Dirichlet sines": only SKELETON_001/phase 205.
- "truncated symbol": 0 hits.
- "partial sum": 2 hits, one of them the minimizer m^{−½}w(m/M), on the zero side.

**Conclusion of the check.** The statement "n₋(𝔄_N(T)) = 1 with N = N(T) in Dirichlet sines" does not appear as
such. Its three ingredients do appear:
- the symbol reading (R164_502c, W-det);
- the block inertia (N3);
- the finite Schur matrix ((L2)).

So the examination below is "is there a new reason in writing?", not "is it new?"

---

## 1. Logical direction

### 1.1 What is PROVED
(a) **D^ev ⇒ n₋(𝔄_N(T)) ≤ 1 for all N and T.** By prop:WT, W^ev = 𝔄_ev + 2ℓ², with ℓ = ⟨·, χ_ev⟩. If W^ev ≽ 0,
then 𝔄_ev ≽ 0 on ker ℓ, which is a hyperplane. By min–max, n₋(𝔄_ev|_V) ≤ 1 on every subspace V; in particular on
E_N^ev. PROVED.

(b) **Stronger, and also necessary:** D^ev ⇒ Z_N := (W^ev)|_{E_N} ≽ 0 on **all** of E_N^ev, not only off the polar
direction.
- With (R1) and extended prop:sharp(ii), Z = 𝔪 + 𝔢 + Φ_E = 𝔞^♯ − 𝓕_T on L²_ev (AUDIT_205 §3).
- This corrects the formulation "≽ 0 on the complement of the polar direction." The restriction of D gives ≽ 0 on
  the whole block. What holds on the polar complement is the weakened version, which is L205.★ (withdrawn, REF-D by K2).

(c) **Chain of implications within the block** (PROVED, linear algebra):
  Z_N ≽ 0  ⟹  L205.★ (Z_N ≽ 0 on E_N ∩ ker ℓ)  ⟹  n₋(𝔄_N) ≤ 1  ⟺  ∃ hyperplane H ⊂ E_N with 𝔄_N|_H ≽ 0.
None of the arrows reverses in general: there are obvious 2×2 counterexamples for each. So **"n₋(𝔄_N) = 1" is the
weakest of the three block statements**. It is weaker than L205.★ by exactly one degree of freedom: the hyperplane
need not be ker ℓ.

### 1.2 Converse
- **Without restricting N.** The family "∀T, ∀N: n₋(𝔄_N(T)) ≤ 1" is equivalent to "∀T: n₋(𝔄_ev(T)) ≤ 1," because
  n₋ of a closed semi-bounded form is the supremum of n₋ over finite compressions (min–max, CITED). By prop:H this
  is equivalent to D^ev. PROVED, but with no content: it is D.
- **With N = N(T) fixed** (frequencies ≤ t₀), P1.c′ is needed, which is OPEN:
  - its half (i), the upper bound of A∞ on P_T, is a zero-free tool;
  - its half (ii), control of 𝓕_T at high frequencies, is probably-REF-D by M1 (SKELETON_002 §3.3).
- Hence the converse **does not follow from what is available**. The statement with N(T) is, as of today, **only necessary**.

### 1.3 Is it strictly weaker? Two readings in tension
- **(α) In favor of it being weaker** (NUMERICAL, CALIB_R5 §3).
  - Epstein, which has its own archimedean part and a hyperbolic pair, gives n₋(𝔄_ev) = 1 at N(T) for all T ≤ 3.
    Only at 2N or 4N does the second negative direction appear: 2 at T = 2 with 4N; 2 and 3 at T = 3.
  - The hyperbolic pair lives above t₀. In the abstract class {Γ-type archimedean part, comb, pole}, the statement
    at N(T) does not detect that pair **in those windows**.
  - As long as that range of T holds, Epstein is a model of the finite statement in which D fails.
- **(β) Against** (ARGUED).
  - Fix a hyperbolic pair ρ = β + iγ, with β > ½ and γ > t₀. Its contribution to the form in window T, read via
    lem:roughEF as a P47 tool, is an indefinite rank-2 term. Its negative part has size ≍ e^{(2β−1)T}·|F̂(γ + i(β−½))|².
  - For F ∈ E_N^ev, the sines s_k are **not band-limited**: |ŝ_k(γ)| ≍ T^{½}·ω_k/(γ² − ω_k²) ≍ T^{½}/γ², with only
    polynomial decay.
  - So, on E_N, the negative part of the pair is ≳ e^{(2β−1)T}·T/γ⁴. That is exponential in T, whereas the
    archimedean part is O(log T) and the rest of the zero sum is controlled by lem:roughEF.
  - ARGUED conclusion: beyond some T_ρ, the block N(T) **sees** the pair, and n₋(𝔄_N(T_ρ)) ≥ 2.
  - If this holds, "∀T, n₋(𝔄_N(T)) = 1" has **full strength** within the class with an explicit formula. Its
    weakness would only be a finite-T-range effect, not a class effect.
- **What is missing to upgrade (β) to PROVED.**
  - That the projection of the pair's negative direction onto E_N is not cancelled by the positive part of the same
    rank-2 term.
  - That it is not compensated by on-line zeros with γ′ ≈ γ.
  - That is a routine 2×2 Gram estimate with constants.
- **Decisive calibrator (P5′, NUMERICAL).** Epstein at N(T) for T = 4, 5, 6, 7.
  - (β)'s prediction is a jump to n₋ = 2 at some T of order log(γ_E⁴)/(2β_E − 1).
  - If the jump appears, (α) was a small-T effect and the finite reformulation is D^ev in finite coordinates: REF-D
    in the literal sense.
  - If it does not appear up to where it can be certified, a genuine weakness exists, but without proof.

**Answer to question 1.** Today, the statement with N(T) is *necessary* and *possibly* weaker. Being weaker does
not make it a candidate for "closing without touching D":
- the weakness of (α) is invisibility of high frequencies (> t₀) in short windows;
- the content it does have, cancelling ≈N−1 archimedean directions within the block, is exactly D's content in that
  block (§3).
A statement weaker than D that still preserves all of D's low-frequency sign work does not close "without touching
D." It is D with the tail cut off.

---

## 2. Structure: the Szegő paradox and its resolution

### 2.1 The paradox is real if σ_T is read as a symbol
By partial summation (SKELETON_002 Prop 3.2):
  σ_T(τ) = 2Re[(X^{½−iτ} − 1)/(½ − iτ)] + σ^E_T(τ),  X = e^{2T}.
The main term has modulus 2e^T·|cos(2Tτ − θ_τ)|/|½ − iτ| ≍ 4e^T/√(1+4τ²)·|cos(·)|.
- **It is not a narrow peak.** It is wide, with 1/τ decay and fast oscillation of period π/T in τ.
- As a symbol, f = m − σ_T takes values ≍ −4e^T on a positive fraction of each period, over all |τ| ≲ e^T/log τ.
- If Szegő–Widom applied to the symbol, it would give n₋ ≍ N, which contradicts the n₋ = 1 from CALIB_R5.

### 2.2 Exact resolution (PROVED, (R1) compressed to E_N)
For F ∈ L²_ev(I_T) one has the exact identity (AUDIT_205 (R1), SKELETON_002 §1):
  (main term)(F) = −∫∫F(x)F(y)e^{|x−y|/2} = 𝔢(F) − 2ℓ(F)².

Compressing to E_N^ev:
  **𝔄_N = (𝔪 + 𝔢)_N − 2 c cᵀ + Φ_N,**  with c_k = ⟨χ_ev, e_k⟩ (closed formula PROVED) and Φ_N = −𝓕_T|_{E_N}.   (RF.1)

The formulation proposed that the main term was "almost rank one." **It is exactly rank one** in the even sector,
plus 𝔢, which is ≻ 0 and has bounded symbol 1/(¼+τ²).
- The transform of the main term, X^{½−iτ}/(½−iτ), is that of e^{u/2}1_{[0,2T]} = e^T·e^{−(2T−u)/2}1_{[0,2T]}. It is
  the *growing* exponential, truncated at the far end.
- As a form on the window it decomposes into cosh (rank 2: χ_ch, χ_sh) plus the Green kernel e^{−|s|/2} of the line.
- The oscillation cos(2Tτ − θ) of the "symbol" is the reflection, in τ, of the mass sitting at u = 2T, at the edge
  of the window. It is not a sign property of the form.

**Conclusion 2.2.** Reading the main term as a symbol is incorrect. The only direction that contributes is χ. This
explains why CALIB_R5's negative eigenvector has cos(v_min, P_Nχ) ≥ 0.998.
By Weyl (PROVED):
  n₋(𝔄_N) ≤ 1 + n₋(Z_N),  Z_N := (𝔪 + 𝔢)_N + Φ_N.

### 2.3 What does Szegő say about Z_N? Nothing useful: critical sampling
Z_N's "symbol" is m^♯(τ) − σ^E_T(τ).
- The archimedean part m^♯ is smooth, of order log τ. By A∞ with t₀′ it is negative on |τ| < t₀′ = 6.126 and has
  ≈1.95T negative directions in the even sector.
- The fluctuation σ^E_T is the transform of the measure 2t^{−½}dE(t) over t ≤ X, i.e. over u = log t ∈ [0, 2T].

Exact relation between the matrix and the symbol (PROVED, Parseval). For F = Σa_k e_k,
  Z_N(F) = (1/2π)∫ (m^♯ − σ^E_T)(τ)·|F̂(τ)|² dτ,  F̂ = Σa_k ê_k,
and each ê_k is a pair of sincs centered at ±ω_k, with width π/T and tails 1/(T|τ − ω_k|).
That is why "Z_N ≽ 0" is the positivity of a quadratic form on an N-dimensional space of sinc-type functions. It is
not pointwise positivity. It is equivalent to the symbol being ≥ 0 **averaged with the weights |F̂|²**, which have
resolution π/T.

That resolution is exactly σ^E_T's oscillation scale, because its frequencies are log n ≤ 2T. Szegő, Widom and
Avram–Parter (CITED) assume a fixed symbol and N → ∞, so that averaging over the width π/T does smooth it out.
Here there is no scale separation:
- the support in u of the kernel c_{kk′}(u) is [0, 2T], the exact window length (CALIB_R5 §1: L = 2T − u);
- that is why the Hankel part and the truncation factors 1/(a ∓ b) are of the **same order** as the Toeplitz part.
  They are not corrections.

**Proposition RF.2 (PROVED, remark).** For every T, the form Z_N determines the restriction of σ^E_T to the lattice
{ω_k ± ω_{k′}} *and* its truncation derivatives, with the same weight. No asymptotic inertia result that depends
only on the symbol's value distribution determines n₋(Z_N) with error < 1.
- *Proof sketch.* The closed formulas of CALIB_R5 §1 show the entries depend on sin((a−b)L − bu) with L = 2T − u.
  The phase term −b·u = −ω_{k′}log n is not a function of the difference ω_k − ω_{k′}. Hence the matrix is not
  Toeplitz plus a bounded-rank term: the error has full rank and norm comparable to the Toeplitz part. ∎
- This is exactly the L0 reading of R164_502c ("symbol never positive") and W-det, in sine coordinates. **No new reason.**

### 2.4 The size that would be required (already closed as M1)
For Z_N ≽ 0 to hold by size, |Φ_N| ≤ (𝔪 + 𝔢)_N is needed on a subspace of codimension ≤ … More precisely,
n₊(Φ_N) ≥ n₋((𝔪 + 𝔢)_N) ≈ 1.95T is needed, with eigenvalues ≥ |m^♯(0)| ≈ 1.37 in those directions. That is:
**Φ_N must be positive and of size O(1) on almost all of the even block**.

Without zeros, the only information about Φ_N is dlVP: |Φ_N| ≲ e^{T − c√T}. That is exponentially larger than what
is needed, and signless. That Φ_N be positive with size O(1) is a statement about E(t) at scale t^{½}, averaged
with sine weights. It is M1 (SKELETON_002 §3.3), I6 of the index, and K1.

Correction to the formulation: it is not necessary that |σ^E_T(τ)| ≤ m(τ) *pointwise*. That is false, NO-GO of
SKELETON_002 §3.4. What is needed is the version integrated against |F̂|² with F̂ in the sinc space, and that is
still of size √t.

---

## 3. TRACT verdict

### 3.1 A genuine path?
Candidates examined:
- **(a) Finite Toeplitz inequality with oscillating symbol, controlled by an arithmetic identity.** An identity
  expressing Φ_N, or Z_N, as a Gram matrix (Σ_j v_jv_jᵀ) or as Gram minus something controlled would be needed.
  - The only exact arithmetic identity for Σ_n v_n c(log n) is the explicit formula: its zero-side reading is the
    sum over ρ, and there positivity of each term is the target (K2).
  - The Euler Gram alternative (Σ_p |·|² via |a_p|² ≥ 0) is closed by Kronecker parity (BARRIER_X_001 X2,
    SYNTHESIS §4).
  - No new identity proposed. **NO.**
- **(b) Rank argument.** For each u, the matrix G(u)_{kk′} = ⟨τ_u e_{k′}, e_k⟩ is the compression of a truncated
  translation. It has full rank for 0 < u < 2T, with eigenvalues in a symmetric interval of size ≍ 1.
  - Σ_n v_n G(log n) does not have bounded rank, and the confirmation ("it is not rank 2") is correct. The only
    exact low rank is that of the main term, −2ccᵀ, already absorbed in (RF.1). **NO.**
- **(c) Szegő / Widom / Avram–Parter / GLT.** Critical sampling (RF.2). **NO**: it is W-det and R164_502c.
- **(d) Interlacing in T (block continuation).** N(T) jumps by one unit when 2Tt₀/π crosses an integer. Between
  jumps, 𝔄_N(T) varies analytically except at contacts log n = 2T.
  - By L2_INTERLACE_001, U0–U2, T13.1: a first-crossing argument is Hellmann–Feynman at the crossing, i.e. a
    functional of h* (𝒦_W/𝒦_H). At the contacts the boundary is not rank one.
  - **NO**, with no new reason: the basis changed from blocks to sines, but the crossing is still a functional of
    the minimizer.
- **(e) Monotonicity of n₋ in N at fixed T** (Cauchy interlacing). Only gives n₋(𝔄_N) ≤ n₋(𝔄_{N′}) for N ≤ N′.
  Goes in the wrong direction to prove n₋ = 1. **NO.**

### 3.2 What changes relative to N3 and (L2), honestly?
1. **Size.** dim E_N^ev ≈ 2T, polynomial. In (L2), k(T) is exponential (L2_INTERLACE §7, "finiteness does not bring
   tractability because k(T) is exponential"). **This is a genuine complexity change.** It makes the family
   certifiable by intervals up to T considerably larger than (L2), and that is useful for the calibrator.
2. **Canonicity.** The block is fixed by archimedean data (t₀), not by an arbitrary Galerkin choice. **It does not
   change the logical class.** N3 closes the block inertia for a reason independent of which block is chosen: ζ's
   inertia in the block is the compression of the target form, and its value is D in the block. A canonical block
   contributes no datum beyond a functional of the same form.
3. **Cancellation within the block** (CALIB_R5: N−1 directions cancelled in E_N, with no complement). **It makes
   tractability worse.**
   - It shows the block already contains all the low-frequency sign work. The finite statement *inherits that work
     in full*, just as (L2) inherits the margin.
   - The cancelled directions end up with eigenvalues ≈ 1e−15 to 1e−17 for N ≥ 2N(T) and for N(T) with T ≥ ½log15
     (the "tiny" ones). The statement's margin sits at the quadrature floor.
   - This is the exact analogue of (L2)'s 10⁻⁷⁰ margin: a statement with near-zero margin on ≈N directions admits
     no perturbative or size-based proof.
4. **Weaker than L205.★ by one degree** (§1.1(c)). This is the only logical difference.
   - The hyperplane is not fixed to ker ℓ. But CALIB_R5 shows the realizing hyperplane is, to 3–4 digits,
     ker ⟨·, P_Nχ⟩.
   - The slack from that degree of freedom is O(1 − cos²) ≈ 1e−4, with no visible arithmetic content.

**Conclusion 3.2.** What changes (the size) is computational. What would be needed to escape N3, a block datum that
is not a functional of the compressed target form, does not appear. **It does not escape N3.**

### 3.3 Labels
- "n₋(𝔄_N(T)) = 1 ∀T" as a target: **OPEN**. As a route with its own path: **TRACT = NO**, REF-D in block form (N3).
  - Size-based proofs die at M1.
  - Continuation-in-T proofs die at 𝒦_W/𝒦_H (L2_INTERLACE).
  - Symbol-based proofs die at W-det / R164_502c (RF.2).
- It is not a TRANSFER to a different open problem: the only residue with content is P1.c′(i), already recorded.
- If calibrator P5′ shows a jump for Epstein at N(T), the reformulation becomes REF-D in the literal sense:
  necessary and, within the class with an explicit formula, of full strength.

---

## 4. Payoff if proved, first finite lemma, index entry

### 4.1 Payoff if proved
A proof of "n₋(𝔄_N(T)) = 1 ∀T" would give, for each T, the positivity of Z on the realizing hyperplane of E_N^ev.
Together with P1.c′ it would give D^ev (Haynsworth, CITED, plus prop:WT).
Without P1.c′ it remains a low-frequency certificate: "every negative archimedean direction with ω ≤ t₀ is covered
by the comb in each window." This is the clean statement of what the comb does in the low block. Useful for P47 as
a remark, not as a proof step.

### 4.2 First finite lemma (constructible, zero-free)
**Lemma RF.1 (three-term identity and Weyl budget; PROVED-elementary, to be written up).** For all T and N:
(i) (RF.1) holds with closed entries:
  - (𝔪 + 𝔢)_N via eq:Aform plus 𝔢_{kk′} = (1/2π)∫ê_kê_{k′}/(¼+τ²), elementary in ω_k, ω_{k′} and T;
  - c_k = 2ω_k cosh(T/2)/(√T(¼+ω_k²));
  - Φ_N(k,k′) = −∫_{(1,X]}2t^{−½}c_{kk′}(log t)dE(t), with c_{kk′} the formula from CALIB_R5 §1.
(ii) n₋(𝔄_N) ≤ 1 + n₋(Z_N) and n₋(𝔄_N) ≥ n₋((𝔪 + 𝔢)_N) − n₊(Φ_N) − 1.
(iii) Hence "n₋ = 1" requires n₊(Φ_N) ≥ ⌈N′/2⌉ − 2, with N′ = ⌈2Tt₀′/π⌉ − 1 (A∞ with t₀′).
  - It is a **PROVED lower bound on the number of directions in which the compressed Chebyshev remainder must be
    positive**: ≈1.95T − 2.
  - It is the quantitative form of the Theorem X budget in sine coordinates.

Value: it reduces the reformulation to its minimal form. It gives no sign. Its falsifiable consequence is measuring
n₊(Φ_N) in ζ and in Epstein; for a_P, B_P (TOOLS_204U) suffices.

**Lemma RF.3 (ARGUED → PROVED with constants; the one that decides §1.3).** Let ρ be a hyperbolic zero of a model in
the class with an explicit formula (lem:roughEF), with γ > t₀. Then there exists T_ρ ≍ (log γ)/(2β−1) such that
n₋(𝔄_N(T)) ≥ 2 for T ≥ T_ρ.
- Ingredients: |ŝ_k(γ)| ≍ T^{½}/γ², which is PROVED-elementary, plus a 2×2 Gram estimate (χ, P_N v_ρ) as in the
  proof of prop:H.
- If proved, the finite reformulation is literally REF-D and closes as a route.
- Calibrator P5′ (Epstein at N(T), T = 4…7) tests it against the data.

### 4.3 Index entry (`04_PHASES`, phase 205; and `06_OPEN_RESIDUES`, next to (L2))
| RFIN_TRACT_001 (phase 205) | Finite reformulation "n₋(𝔄_N(T)) = 1 ∀T" in Dirichlet sines, with N(T) ≈ 4T | NO-GO as a route (TRACT = NO; REF-D in block form, N3) | Only necessary and weaker than L205.★ by one degree. Szegő paradox resolved: the main term is 𝔢 − 2ccᵀ, exact by (R1). The remainder Φ_N is in **critical sampling** (support in u = window), so Szegő/Widom/GLT do not apply (RF.2 = W-det/R164_502c). Size-based proofs die at M1 and continuation proofs at 𝒦_W (L2_INTERLACE). The only new thing is dim ≈ 2T versus exponential k(T) (computational); the margin sits at ~1e−15. Lemma RF.1 (budget: n₊(Φ_N) ≥ 1.95T − 2) PROVED-elementary. RF.3 (Epstein seen at N(T) beyond T_ρ) ARGUED; decided by calibrator P5′, T = 4…7. |
