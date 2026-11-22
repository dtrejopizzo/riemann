# SPEC A — Formal specification of a statement T* by exact induction in T through prime contacts

Design round, not a construction round. Pen and paper; no numerics beyond cited record values; no proof attempts.
 no
equivalence between row D and any other statement is used, invoked or mentioned.
ARGUED / OPEN / NO-GO / NUMÉRICO. "P46" = 04-papers/46-row-d-dual-certificates/main.tex; "186/" = phase-186-toolbox;
"188/" = phase-188-closing-D; "190/" = phase-190 memos; index = 05-meta-and-planning/ROUTES-TRIED-INDEX.

Mandatory reading done: 190/SHAPE_THEOREM.md (with its §0 erratum and SHAPE_THEOREM_REVIEW.md);
crossword §3.2–3.3 and addenda 186/188/189; index README (incl. "Correcciones ", phase 190), 06_ R1–R10 and "Other
open items", 04_ Part I-a/b/c; P46 §sec:coer (lem:coer-decomp, thm:coer-A, thm:coer-B, cor:coer-L1, thm:coer-schur,
rem:coer-honest, rem:coer-nogo), prop:finite, rem:regimes, prop:decide, lem:contA, lem:monoT, thm:wit-Tc, lem:wit-freeze,
thm:wit-asym, thm:margin/cor:margin1, lem:degen, prop:wit-sens, thm:X, lem:flowdet, thm:wh-schur/lem:wh-schurabs,
thm:log5A, cor:void, rem:twohalves; 186/R186_048 (W-cont), R186_029 (Lemma H), R186_031 ((B_T) false); 188/L2_BUILD_001
(contact-entry modulus), L2_BUILD_002 (Schur tower), L2_BUILD_016 (Frobenius doubling NO-GO), L2_BUILD_027; 190/EXP_005;
R166_802 (circularity theorem); R169_000 §7 ("Bombieri–Vinogradov for a selected frequency": does not exist).

**One-line verdict (details in §6): NOT ADMISSIBLE as mandated.** The exact-Schur induction can be written down and its
skeleton passes the transfer clauses O1–O15 formally, but (i) its inductive step is an exact restatement of the target at the
next contact (B8; R186_029 Lemma H(ii)), the inductive hypothesis entering only through the resolvent of the frozen window,
whose only usable datum is 1/λ_A(T_j); (ii) the step must decide a sign of size ≍ λ_A(T_{j+1}) (B1/B9 inherited), i.e.
doubly-exponentially small in T on the record's pattern law, while every "individual power saving" input is at best
exponentially small in T — clause (γ) fails by a doubly-exponential factor, not by a constant; (iii) no line of the
specification uses ℤ-integrality — clause (θ) is not met as written. No sign is certified here; nothing moves λ_A(T) for ζ.

---

## 1. Setting and notation (P46)

- Contacts: n_1 = 2 < n_2 = 3 < n_3 = 4 < n_4 = 5 < n_5 = 7 < n_6 = 8 < n_7 = 9 < n_8 = 11 < … (the support of Λ);
  T_j := ½ log n_j; regimes R_j := (T_j, T_{j+1}]; gap ε_j := T_{j+1} − T_j = ½ log(n_{j+1}/n_j).
- v_n := 2Λ(n)/√n; 𝒩_T := {n : log n < 2T}; on R_j the contact set is constant, 𝒩_T = {n ≤ n_j} ∩ supp Λ (rem:regimes).
- σ_T(τ) = m(τ) − Σ_{n∈𝒩_T} v_n cos(τ log n), m(τ) = Re ψ(¼ + iτ/2) − log π, C₀ = m(0); K(u) = 2e^{−u/2} + K_1(u) the
  Lévy kernel (lem:K, lem:coer-K1); 𝔞_T(F) = C₀‖F‖² + Lev(c_F) − Σ v_n c_F(log n) (eq:Aform); P_T = {A(F) = B(F) = 0};
  λ_A(T) = inf 𝔞_T on the unit sphere of P_T ∩ 𝒟_T; h*_T a real unit minimizer (exists, lem:compact).
- Facts used as PROVED: lem:monoT (λ_A nonincreasing in T; extension by zero ι: P_T → P_{T'} preserves 𝔞), lem:contA
  (continuity), prop:finite (WP_T depends on (Λ(n))_{n<e^{2T}} and m only), R186_048 Lemma 3.1 (entry invisibility:
  𝔞_{T_j^+} ≡ 𝔞_{T_j^−} on L²(I_{T_j}) because c_F(2T_j) = 0), R186_048 Lemma 3.2 (visibility bound: for T = T_j + ε,
  |c_F(log n_j)| ≤ ‖F‖²_{edge,ε}), lem:wh-schurabs / thm:wh-schur (abstract exact Schur reduction on a closed semibounded
  form), L2_BUILD_002 (Haynsworth inertia additivity across nested reductions), thm:margin/cor:margin1
  (λ_A(T) ≤ 4·10⁹ T e^{−15.449T}, T ≥ 1), thm:log5A (λ_A ≥ 2.5·10⁻¹² on (0, ½log5]).
- NUMÉRICO (used only to size quantities, never as input): pattern law −ln λ_A ≈ 13.0 e^{2T} − 24.6T − 18.7 (phase 187);
  the minimizer vanishes at the boundary like (T − |t|)^a, a ≈ 0.15–0.25, so its edge mass on a collar of width ε is
  ≍ ε^{2a+1} ≈ ε^{1.3–1.5} (R186_048 §4); the perturbative regime after an entry covers 25 %, 18 %, 4 % of R_j for
  n_j = 3, 4, 5 and shrinks (R186_048 Prop 4.3(iii)).

### 1.1 A design correction forced by the record
The brief locates the step "across the entry of the next prime power". The record shows the entry instant is empty:
at T = T_{j+1} the atom n_{j+1} changes nothing (Lemma 3.1 above; lem:contA), and λ_A is constant in the comb and
nonincreasing in T inside each regime. Hence an induction on contacts is an induction on the **endpoint values**
λ_A(T_j), and by lem:monoT the interior of every regime is free once the endpoint is positive. The atom whose
row/column is new at the step T_j → T_{j+1} is **n_j** (it entered invisibly at T_j and becomes visible on R_j only
through the collar of width ε near ±T_j, Lemma 3.2), not n_{j+1}. The specification below is written accordingly.

---

## 2. The statement T*

**T* (exact induction through contacts).** There is a sequence μ_j > 0 (j ≥ 1), explicit in j, such that
  (T*_j)   λ_A(T_j) ≥ μ_j   for every j ≥ 1.

**How row D follows (PROVED, given T*).** For any T > 0 choose j with T ≤ T_j (the contacts are unbounded). By lem:monoT,
λ_A(T) ≥ λ_A(T_j) ≥ μ_j > 0. Hence λ_A(T) > 0 for every T, which is eq:target with strict sign at every window. (T* is
strictly stronger than row D; B2e forbids weaker statements, not stronger ones. Any μ_j must respect cor:margin1:
μ_j ≤ 4·10⁹ T_j e^{−15.449T_j} for T_j ≥ 1; a sequence μ_j → 0 is the lower half of a bilateral law, residue R6, which the
record does not exclude — rem:bar-fam, R186_036 Thm 3(b).)

**Base case (PROVED / CITED).** (T*_j) for j = 1, …, 4 (T_4 = ½log5 = 0.8047) with μ_1 = … = μ_4 = 2.5·10⁻¹² (thm:log5A,
PROVED with ball arithmetic; thm:C at ½log3 gives more). Granting Liu Thm B (CITED, complete form, preprint; half-width
17/16 = 1.0625), (T*_j) holds for j ≤ 6 (T_6 = ½log8 = 1.0397 ≤ 17/16 < T_7 = ½log9 = 1.0986) with μ_j = 2^{−49162},
since λ_W ≤ λ_A on P_T. The first unproved instance is j = 5 without Liu (T_5 = ½log7 = 0.973; the record's polar
capacity beyond ½log5 is OPEN, index "polarcap5"), j = 7 with Liu.

**Inductive hypothesis H_j.** (H_j.1) λ_A(T_j) ≥ μ_j > 0 with μ_j known. (H_j.2) The exact window data at T_{j+1}: the
vector (Λ(n))_{n ≤ n_j} = (Λ(n))_{n < e^{2T_{j+1}}}, the kernel K (equivalently m), the two Tate exponentials. Nothing else.
(No property of Λ beyond its values is assumed; no zero information; no statement about T > T_{j+1}.)

**Conclusion C_j.** λ_A(T_{j+1}) ≥ μ_{j+1} > 0 with μ_{j+1} explicit in (μ_j, j).

**The exact objects of the step.**
(a) *Splitting of the window.* I_{T_{j+1}} = L_j ∪ I_{T_j} ∪ R_j with L_j = [−T_{j+1}, −T_j), R_j = (T_j, T_{j+1}], each of
    length ε_j. L²(I_{T_{j+1}}) = L²(L_j) ⊕ L²(I_{T_j}) ⊕ L²(R_j).
(b) *Frozen block.* 𝒳_j := ι(P_{T_j} ∩ 𝒟_{T_j}) ⊂ P_{T_{j+1}} ∩ 𝒟_{T_{j+1}}; 𝔞_{T_{j+1}}(ιx) = 𝔞_{T_j}(x) (lem:wit-freeze,
    Lemma 3.1: the atom n_j is invisible on I_{T_j}). Under H_j, 𝔄_j := 𝔞_{T_j}|_{P_{T_j}∩𝒟_{T_j}} ≥ μ_j > 0 is a closed
    positive form with bounded inverse of norm 1/μ_j.
(c) *Edge space.* ℰ_j := P_{T_{j+1}} ⊖ 𝒳_j (L²-orthogonal complement inside P_{T_{j+1}}). Exactly:
    ℰ_j = { e = α e^{t/2}𝟙_{I_{T_j}} + β e^{−t/2}𝟙_{I_{T_j}} + G : G ∈ L²(L_j ∪ R_j), A(e) = B(e) = 0 }.
    The 2×2 Tate Gram on I_{T_j} is invertible (the determinant argument of lem:coer-decomp(iii)), so (α, β) is determined
    by the Tate moments of G and ℰ_j ≅ L²(L_j ∪ R_j) as a linear space. ℰ_j ⊂ 𝒟_{T_{j+1}} (the interior part is a Tate
    exponential; the edge part is any L² function on a collar — NOTE: 𝒟-membership of G must be imposed; take ℰ_j ∩ 𝒟).
(d) *Coupling functional.* For e ∈ ℰ_j and x ∈ P_{T_j} ∩ 𝒟_{T_j}: ℓ_e(x) := 𝔞_{T_{j+1}}(e, ιx). With supp G disjoint from
    I_{T_j}, eq:Aform gives
      ℓ_e(x) = α 𝔞_{T_j}(e^{+}_{j}, x) + β 𝔞_{T_j}(e^{−}_{j}, x) − ⟨G, 𝒯_j x⟩_{L²(L_j∪R_j)},
      (𝒯_j x)(t) := ∫_{I_{T_j}} K(|t − s|) x(s) ds + Σ_{n ≤ n_j} v_n [x(t − log n) + x(t + log n)],   t ∈ L_j ∪ R_j,
    where e^{±}_j := e^{±t/2}𝟙_{I_{T_j}} and the first two terms are the 𝔞_{T_j}-pairings of x with the two Tate
    exponentials (nonzero in general: P_T is defined by L²-orthogonality, not 𝔞-orthogonality). 𝒯_j x is the **exterior
    trace** (exterior field) of x: the continuation of σ_{T_j}^{+}(D)x outside I_{T_j}. On the right collar only the terms
    x(t − log n) with log n ∈ (t − T_j, t + T_j) survive, i.e. all n ≤ n_j; the atom n_j couples t ∈ R_j to t − 2T_j ∈ L_j-side
    collar of the interior: this is the **contact block**, supported in the 2ε_j-collar of ∂I_{T_j}, with weight v_{n_j};
    its archimedean twin at the same lag is the polar part of the Lévy kernel, K(2T_j) = 2 n_j^{−1/2} + K_1(2T_j), i.e.
    v_{n_j} = Λ(n_j)·2n_j^{−1/2} and the polar coupling 2n_j^{−1/2} sit at the same lag with ratio Λ(n_j) = log p.
(e) *Exact Schur complement onto the edge.* 𝔰_j(e) := 𝔞_{T_{j+1}}(e) − sup_{x} [2 Re ℓ_e(x) − 𝔞_{T_j}(x)]
    = 𝔞_{T_{j+1}}(e) − ‖ℓ_e‖²_{𝔄_j^{−1}} (dual norm of the functional ℓ_e with respect to 𝔄_j), e ∈ ℰ_j ∩ 𝒟.
(f) *Tate constraints across the contact.* The global Tate conditions A = B = 0 on I_{T_{j+1}} are the only constraints;
    they tie G's moments to (α, β). There are no block-Tate conditions on L_j, R_j (unlike 𝒱_k of thm:coer-B); a further
    finite reduction of ℰ_j by thm:coer-schur at T_{j+1} (blocks of size T_{j+1}/k, k ≥ k₀(T_{j+1}), doubly exponential in
    T_{j+1} by rem:coer-size) is available and nests with the T_j-reduction (L2_BUILD_002 Lemma 2), but is not needed to
    state L*.

**Lemma S (exact reduction of the step; PROVED, abstract).** Assume H_j.1. Then: (i) λ_A(T_{j+1}) ≥ 0 ⟺ 𝔰_j ⪰ 0 on ℰ_j ∩ 𝒟,
and λ_A(T_{j+1}) > 0 ⟺ 𝔰_j ≻ 0 with λ_𝔰 := inf 𝔰_j/‖·‖² > 0; (ii) min{μ_j, λ_𝔰}/(1 + ‖𝖪_j‖)² ≤ λ_A(T_{j+1}) ≤ min{μ_j, λ_𝔰}, where
𝖪_j e := 𝔄_j^{−1}ℓ_e, ‖𝖪_j‖ ≤ sup_e ‖ℓ_e‖_{L²-dual}/μ_j; (iii) n_−(𝔞_{T_{j+1}}|_{P}) = n_−(𝔰_j) (Haynsworth); (iv) for the
minimizer h = ιx + e at T_{j+1}: λ_A(T_{j+1}) = 𝔞(ιx + 𝖪_j e) + 𝔰_j(e) ≥ 𝔰_j(e) ≥ λ_𝔰 ‖e‖², hence λ_𝔰 ≤ λ_A(T_{j+1})/‖e_min‖²
with e_min the edge component of h*_{T_{j+1}}.
*Proof.* lem:wh-schurabs / thm:wh-schur with 𝒳 = 𝒳_j (𝔞 + M‖·‖² closed by lem:compact; 𝔄_j ≥ μ_j > 0 by H_j.1); (iii) is
L2_BUILD_002 Cor 4(a) in this decomposition; (iv) is eq:coer-schur read at the minimizer. ∎
This lemma is bookkeeping: it is thm:wh-schur with the frozen window as the coercive block. It contains no sign.

---

## 3. The inductive step as a lemma L*

**L*_j (the step).** Assume H_j. Then 𝔰_j ≻ 0 on ℰ_j ∩ 𝒟 with an explicit ν_j > 0, λ_𝔰 ≥ ν_j, **and** the resulting
bound for λ_A(T_{j+1}) is obtained by an argument sharper than Lemma S(ii): μ_{j+1} ≥ μ_j · exp(−C (n_{j+1} − n_j)) for an
absolute C. (Lemma S(ii) alone gives μ_{j+1} ≥ min(μ_j, ν_j) μ_j²/‖ℓ‖², losing a factor μ_j per step; iterated, that
destroys the sequence. The requirement on the ratio is forced by consistency with the pattern law, NUMÉRICO, and with the
trivial upper bound; it is a design constraint, not a theorem.)

**The inequality, written out.** For every e = (α, β; G) ∈ ℰ_j ∩ 𝒟:
  (L*)   𝔞_{T_{j+1}}(e)  ≥  ‖ℓ_e‖²_{𝔄_j^{−1}} + ν_j ‖e‖²,
with, explicitly,
  𝔞_{T_{j+1}}(e) = C₀‖e‖² + Lev(c_e) − Σ_{n ≤ n_j} v_n c_e(log n)         (edge energy: collars + Tate interior part),
  ℓ_e(x) = α 𝔞_{T_j}(e^{+}_j, x) + β 𝔞_{T_j}(e^{−}_j, x) − ⟨G, 𝒯_j x⟩,       (exterior field of x on the collars),
  ‖ℓ_e‖²_{𝔄_j^{−1}} = sup_{x ∈ P_{T_j}∩𝒟} [2 Re ℓ_e(x) − 𝔞_{T_j}(x)].
Non-linearity: ℓ_e is linear in the weights v (a measure identity on the window, B4); the Schur term is quadratic in ℓ_e
and rational in v through 𝔄_j^{−1} = (𝔪_{T_j} + Π_{T_j})^{−1}|_{P}. That is where the comb enters non-linearly.

**The quantity whose sign is needed, and its size.**
- *Rank-one necessary condition.* Taking x = s·h*_j in the sup: ‖ℓ_e‖²_{𝔄_j^{−1}} ≥ |ℓ_e(h*_j)|²/μ_j. So (L*) requires, for
  every e ∈ ℰ_j, |ℓ_e(h*_j)|² ≤ μ_j (𝔞_{T_{j+1}}(e) − ν_j‖e‖²): the coupling of every edge function to the minimizer of the
  frozen window must be ≤ √μ_j · √(edge energy). With ℓ_e(h*_j) = −⟨G, g*_j⟩ + (Tate terms), g*_j := 𝒯_j h*_j the exterior
  field of the minimizer on the collars. In Fourier terms, Σ_{n ≤ n_j} v_n h*_j(t − log n) = (1/2π)∫ ĥ*_j(τ) e^{itτ}
  2P_{n_j}(½ + iτ) dτ with P_X(s) := Σ_{n ≤ X} Λ(n) n^{−s}: the exterior field is the inverse transform of
  ĥ*_j · (2P_{n_j}(½ + i·) + archimedean multiplier) evaluated outside I_{T_j}. Inside I_{T_j} the Euler–Lagrange equation
  gives σ(D)h*_j = μ_j h*_j + (Tate exponentials); (L*) is a statement about the **continuation of σ(D)h*_j beyond the
  window**.
- *Size of the margin to be decided.* PROVED: λ_𝔰 ≥ λ_A(T_{j+1}) (Lemma S(ii)) and λ_𝔰 ≤ λ_A(T_{j+1})/‖e_min‖² (Lemma S(iv)).
  With ‖e_min‖² ≍ ε_j^{2a+1} (NUMÉRICO, a ≈ 0.15–0.25) the step margin ν_j is λ_A(T_{j+1}) up to a polynomial factor in ε_j:
  ν_j ≤ 4·10⁹ T e^{−15.449T} ε_j^{−1.5} (PROVED modulo the numerical edge-mass exponent) and ≈ exp(−13 n_{j+1}) on the
  pattern law. This is R186_029 Lemma H(ii) for this reduction: the Schur complement inherits thm:margin.
- *Comparison with thm:margin, and the loss budget.* The margin at T_j is μ_j ≈ exp(−13 n_j) (NUMÉRICO law; PROVED only
  ≤ 4·10⁹ T e^{−15.449T}). The step must deliver μ_{j+1} ≈ μ_j exp(−13(n_{j+1} − n_j)) and must therefore lose at most a
  factor exp(−C·gap) relative to μ_j — nothing of size μ_j^{1+δ}. Concretely: if ℓ_e is replaced by ℓ_e + η (an estimate of
  the exterior field with error η in the L²-dual norm), the Schur term moves by up to (2‖ℓ_e‖‖η‖ + ‖η‖²)/μ_j; so the
  permitted error is ‖η‖ ≲ μ_j ν_j/‖ℓ_e‖ ≍ μ_j μ_{j+1}. **How not to lose more than that:** the exterior field must enter
  through identities only (it is linear in Λ and exactly computable from the window data), and the only inequality in L*
  must be (L*) itself; any intermediate estimate of ℓ_e(x), of 𝔄_j^{−1}, or of the edge energy with an error not already
  multiplied by a factor of size μ_j μ_{j+1} violates the budget. In particular Lemma S(ii) (a relative bound, B6(ii)), the
  rank-one replacement 𝔄_j^{−1} ↦ μ_j^{−1}|h*_j⟩⟨h*_j| plus a bound (class (LIN) + Cauchy–Schwarz, B4), L2_BUILD_001 Thm 3
  (loses log(1/δ)), R186_031 (B_T) (FALSE), and every norm bound of the coupling (rem:coer-nogo: the extremals of the
  coupling norm are not the minimizers) are outside the budget.

---

## 4. Clause-by-clause compliance

Tiering follows SHAPE_THEOREM §0 (erratum): tier (A) PROVED falsifiers; tier (A′) CONDITIONAL/ARGUED/CITED/OPEN;
B-clauses structural. "PASS-COND" means: the specification escapes the clause **only if** the proof of L* is exact in the
sense of the loss budget of §3; a proof of L* that bounds instead of computes falls back into the class. "FAIL" means the
specification as written does not escape.

| clause | op / lemma | what the specification does | status |
|---|---|---|---|
| O1 / A1 | finite deletion Λ𝟙_{n≥N} | the step at index j uses v_n for all n ≤ n_j through 𝔄_j^{−1} and 𝒯_j; for the deleted comb the induction must fail at the first j with T_{j+1} ≥ 0.60 and n_j ≥ N (A1), so L* must be false there — it is, provided L*'s proof uses 𝔄_j^{−1} exactly (the deleted block has a different resolvent) | PASS-COND |
| O2 / A2 | amplification Λ + c𝟙_{n=2} | v_2 enters 𝔄_j and the contact structure exactly; same remark | PASS-COND |
| O3 / A3 | tail deletion Λ𝟙_{n<n₀} | at step j with n_j < n₀ the data coincide with ζ's and the step is identical; the induction for the truncated comb must fail at some later j (A3): L* must use the atoms ≥ n₀ when they are in the window — it does, as data | PASS-COND |
| O4 / A4 | cΛ, c large / c → 0 | all weights enter exactly; the Schur term is rational in c, not homogeneous | PASS-COND |
| O4ε, O5 / A4ε, A5 | (1 ± ε)Λ, one weight by ε | the Schur term is Lipschitz in v with constant ≍ ‖ℓ‖²/μ_j² through 𝔄_j^{−1}: 10⁻⁵ changes move it by far more than ν_j — the specification is as sensitive as the target (consistent with prop:wit-sens); hence any bounded continuous functional used inside L* is excluded | PASS-COND (and the budget of §3 is the price) |
| O6 / A6 (ARGUED) | Beurling repositioning | the induction is defined verbatim for any positive comb on any semigroup; **no line of the specification uses that the lags are log ℕ** (the lag set {log(n/n′)} of the contact block and the near-coincidences are present as data but no property of them is invoked) | FAIL as written — see (θ) |
| O7 / A7 | a_P = Λ𝟙_{p≥P} | low atoms absent from 𝔄_j: different resolvent; L* must use them | PASS-COND |
| O8a / A8a | quartets M_m (same comb) | the form of M_m is 𝔞_T + kQ_z (rank-4 perturbation, lem:wh-Q); Lemma S holds for it verbatim, and M₁ is positive at T_3 and negative at 0.573 ∈ R_3 (R186_048 §5.3): so L*_3 is FALSE for M₁ and a proof of L* must use the exact kernel K/resolvent, not the shared properties of prop:quartetmodel | PASS-COND |
| O8b / A8b | f_t = ζ + t g | identical data for n_j < λ₁; beyond, lags m/√M ∉ log ℕ and signed weights change 𝒯_j and 𝔄_j; the separating input is again "the data" | PASS-COND |
| O8c (ARGUED) | ζ̃ = ζ·R | not a window-form falsifier in the record; the specification does not pass through the height flow at σ = 1, so (e)4's holomorphy/order-1 clause is not engaged | N/A |
| O9 / A9 (CITED/ARGUED) | Epstein/DH (form objects, signed comb) | same as O8a: Lemma S applies; separation only through the exact data | PASS-COND |
| O10 / A10 (OPEN) | field change | T* is a computation with ζ's own data; it claims nothing field-uniform; by the erratum's restated (e)10 it uses a property beyond A1–A6 (the exact comb) | PASS |
| O11 / B3 | FE antisymmetry | no σ-family symmetrization anywhere | PASS |
| O12 / A11 | bounded-range families (+ amplification closure) | each step uses data on (0, T_{j+1}] only and concludes only at T_{j+1}; ∀T is the union of all steps, each with more data; the class "exact induction" is not closed under amplification at any fixed n₀ (the step with n_j ≥ n₀ sees it) | PASS |
| O13 / A12 | symbol truncation / locality on U_T | 𝔰_j uses the whole form (positive part of σ through 𝔄_j^{−1} and the edge energy on all frequencies) | PASS |
| O14 / B9 (precision) | moments, norms, O(1)-error determinants | the step decides a sign of size ν_j ≍ λ_A(T_{j+1}) (§3); any criterion with O(1) relative error is useless; the specification honours B9 only through the loss budget | PASS-COND |
| O15 / A16 | Poisson randomization | exact positions, no density argument | PASS |
| A15 | progressions / sieves (𝒞_prog, 𝒞_BT) | not used in the specification. **But the mandated power source (BV-type, sieve-type inputs at a selected frequency) belongs to this class**: if the proof of L* bounds the exterior field by such a statement, cor:void/prop:prog apply at every T > T₀(0) = 0.74921 | PASS as written / FAIL if powered as mandated |
| A17 | zero information | none used; the minimizer h*_j is a prime-side object here (its zero-side structure, EXP_003 Fact N2, is observed, not used) | PASS |
| B1 | margin | ν_j inherits λ_A(T_{j+1}) (Lemma S(iv), Lemma H(ii)); doubly-exponential on the pattern law; acknowledged, budget stated | PASS (constraint acknowledged) |
| B2a–c | criticality at centre, packets, mean square | the Schur complement discards no band; exactness at all frequencies is built in; B2c (RMS of 2P_{n_j}(½+iτ) ≈ 2T, Mertens) means |g*_j| is of size (log n_j)·|ĥ*| pointwise with no cancellation available from size bounds — consistent with §3 | PASS (formally) |
| B2d | density ceiling: win from fluctuation only | the resolvent 𝔄_j^{−1} carries the fluctuation; no main-term argument | PASS (formally) |
| B2e | no asymptotic slack | T* is strict at every contact; stronger than D | PASS |
| B4 | operator calculus linear + C–S | ℓ_e is a measure identity on the window (linear); the Schur term is its square over the resolvent — non-linear. Replacing 𝔄_j^{−1} by its bottom plus a bound is C–S and carries the whole margin (excluded by the budget) | PASS-COND |
| B5 | arithmetic SOS | not an SOS | PASS |
| B6 | orders, relative bounds, positive exterior, termwise | Lemma S(ii) is a relative bound and must not be the mechanism (§3); no termwise comb bound | PASS-COND |
| B7 | flows and new contacts | (i) the induction is the flow across regimes; lem:flowdet's coefficient ⟨A′h*, h*⟩/λ_A is exactly |ℓ_e(h*_j)|²/μ_j, made explicit rather than avoided; the barrier reading (rem:bar-loc, ARGUED) says this is where the whole sign sits — the specification agrees; (ii) thm:X (averaged cancellation on U_{T₀}) is a consequence, not an input | PASS (ARGUED barrier, embraced) |
| B8 | no weaker substatement (REF-D) | **L*_j is an exact restatement of "λ_A(T_{j+1}) > 0 given λ_A(T_j) > 0" (Lemma S(i)).** H_j enters only through 𝔄_j^{−1}, whose only usable datum is μ_j; R186_048 Prop 4.3 ("hereda") and R186_029 Lemma H(ii) ("el enunciado reducido es D por ventana con otro nombre") apply verbatim. The induction has no step smaller than the target | FAIL |
| (α) | individual property of Λ over ℕ distinguishing ζ from f_t and M_m | only "the exact values" — identification, not a named property (W-identification: the question returns unchanged) | PASS vacuously / not a property |
| (β) | non-linear in Λ, not polynomial in the test | rational in Λ via 𝔄_j^{−1}; quadratic in the test as the target is; the proof's input undetermined | PASS-COND |
| (γ) | upper bound on Σ_{n≥X}Λ(n)n^{−½−iγ}w beyond the window with exponent Θ − ½ | **not needed in tail form** (prop:finite: nothing beyond n_j enters the step), replaced by the exterior-field inequality inside the window; **but the required precision is ν_j ≍ exp(−c e^{2T_{j+1}}) (B1) while any individual power saving in n_j is n_j^{−δ} = exp(−2δT): the gap is doubly-exponential vs exponential.** No theorem of the crossword table (VK, BV, MR, Selberg CLT, Weil over 𝔽_q read as a bound) can supply it; R166_802 (circularity) adds that an O-bound of exact strength at the witness frequency is the hypothesis itself | FAIL |
| (δ) | couple primes with ∞ without being D | the contact block does couple v_{n_j} with the polar term 2n_j^{−1/2} at the same lag (explicit); but the coupled statement is the target at T_{j+1} (B8) | FAIL ("without being D" half) |
| (ε) | not a Sonin-remainder norm bound | correct, none | PASS |
| (ζ) | not a sieve / measure-in-γ / uniform-in-γ bound | none in the specification; the mandated power source would be one | PASS as written / FAIL if powered as mandated |
| (η) | not only inertia | Haynsworth is used for bookkeeping (Lemma S(iii)); the sign is in ν_j > 0, beyond inertia | PASS-COND |
| (θ) | integrality of multiplicities and of ℤ | **not used anywhere**; the only place it could enter is the lag set {log(n/n′)} of the contact block (near-coincidences, R9) — unspecified | FAIL |
| (ι) | no margin | the induction carries μ_j > 0 explicitly (R6 lower half, not excluded); the margin is the target's own, not a slack | PASS |
| (κ) | no zeros | none | PASS |
| (λ) | valid on the whole test set defining the window | (L*) is for every e ∈ ℰ_j | PASS |
| (μ) | global in X, not local in jets | the step sees all n ≤ n_j globally; no jet expansion (W5) | PASS |

Summary of the table: tier (A) transfer clauses O1–O5, O7–O9, O12–O15 are escaped **conditionally on exactness**; O6/(θ)
is not escaped as written; A15/(ζ) are escaped as written but not if the step is powered as mandated; B8, (γ), (δ) are not
escaped.

---

## 5. Which theorems of analytic number theory would enter L*, where, and what new property is needed

**Where an input could enter.** Only at one line: the evaluation of the exterior field g*_j = 𝒯_j h*_j on the collars,
i.e. of the function 𝓕^{−1}[ĥ*_j(τ) · 2P_{n_j}(½ + iτ)] on L_j ∪ R_j (plus the archimedean convolution K ⋆ h*_j there), and
of its dual norm against 𝔄_j. Everything else in L* is an identity (Lemma S) or the final inequality.

| theorem | would enter at | what it gives | why it cannot power L* |
|---|---|---|---|
| Perron / explicit formula for P_X(½+iτ) | expansion of 2P_{n_j}(½+iτ) = main term X^{½−iτ}/(½−iτ) − Σ_ρ X^{ρ−½−iτ}/(ρ−½−iτ) + … | an exact identity, but through the zeros: using it as a mechanism is 𝒞_zeros (A17); as a certificate it is thm:Z (REF-D) | excluded as mechanism |
| Vinogradov–Korobov (bounds for ζ′/ζ, P_X on/near the line) | pointwise |P_X(½+iτ)| for |τ| ≲ 1/ε_j | O(X^{½}(log)^c)-type or zero-free-region strength: polynomial in n_j; the ℤ-counting (θ) is present | precision needed ≍ exp(−c n_{j+1}); dlVP cap (R164_601 Thm 3.3); A1/A17 class |
| Bombieri–Vinogradov, large sieve, Montgomery–Vaughan mean value | mean over τ (or over moduli) of |P_X(½+iτ)|² ≈ (log X)² (B2c) | a mean statement, not the value on the minimizer's spectrum; "BV for a selected frequency" does not exist (R169_000 §7; crossword §3.3) | A15/(ζ) class; mean ≠ individual |
| Matomäki–Radziwiłł | short-interval averages of multiplicative functions | o(·), bounded multiplicative, not Λ twisted at height ≲ 1/ε_j | (γ) strength; A15 |
| Weil's bound for curves over 𝔽_q | the function-field model: the comb is 2π/log q-periodic in τ, P_X is a polynomial in q^{−iτ}, the window problem at each T is finite-dimensional and the induction on contacts is a finite computation | the analogue of (L*) over 𝔽_q is a finite identity whose positivity is exactly the content of Weil's theorem for that curve (not a weaker input); over ℤ there is no finite structure (W8 rationality wall, W10) | shows what "exact induction" means in the model; supplies no inequality over ℤ |
| Hardy–Littlewood–Pólya / Hilbert inequality (rem:coer-nogo) | norm of the archimedean coupling across the collar boundary (exactly π/2 on Tate-orthogonal pairs) | a norm bound; the extremals are not the minimizers | outside the budget (B4/B6) |

**The new property C* (stated as a conjecture).**
> **C* (exterior-field conjecture).** For every j ≥ 1 with λ_A(T_j) > 0 and every e ∈ ℰ_j ∩ 𝒟:
>   𝔞_{T_{j+1}}(e) − sup_{x ∈ P_{T_j}∩𝒟_{T_j}} [2 Re ℓ_e(x) − 𝔞_{T_j}(x)] ≥ ν_j ‖e‖²,  ν_j > 0,
> with ν_j/μ_j ≥ exp(−C(n_{j+1} − n_j)) for an absolute C. Equivalently: the continuation of σ_{T_j}^{+}(D)h beyond I_{T_j},
> for every h in the frozen window, is dominated in the 𝔄_j-dual norm by the edge energy of the collar functions, with the
> stated margin.

*Check against the index (not a retry?).* No entry states C* in this exact form (grep: "exterior field", "continuation
beyond the window", "edge Schur": none). Its neighbours are all recorded: R186_048 Prop 4.3 (exact qualitative version,
"hereda"; perturbative quantitative version NO-GO, W-cont); L2_BUILD_001 Thm 3 (one-sided, relative to the deleted-contact
form, loses log(1/δ)); R186_031 Lemma B ((B_T), a uniform boundary bound on c_h near the edge — the weakened rank-one form
of C* — **FALSE**); R186_029 Lemma H(ii) (Schur complements inherit the margin: C* is "D per window under another name");
L2_BUILD_002 (Schur tower in k at fixed T; nesting used here); L2_BUILD_016 (Frobenius dilation: a different transport,
NO-GO; not reused). So C* is new as a statement and REF-D as content: by Lemma S(i) it is the target at T_{j+1} given the
target at T_j. What a proof of C* would need **beyond every listed theorem** is a statement about the minimizer h*_j (the
exterior continuation of σ(D)h*_j is 𝔄_j-small at precision √(μ_j ν_j)) — a functional of h*, not of σ or of Λ, exactly the
object that phases 183–186 identified as every first-order discriminant ("every first-order discriminant is a functional of
h*, not σ"), and that corollary (c) of the shape theorem says is the sign itself. No property of Λ in the literature is of
that type: every one of them is a size statement, and the size needed is below every power of n_j.

---

## 6. Honest verdict

**NOT ADMISSIBLE** as mandated (exact induction powered by individual power-saving inputs). Failing clauses:
1. **(γ) — precision.** The step margin is ν_j ≍ λ_A(T_{j+1}) (Lemma S(iv), Lemma H(ii)): ≈ exp(−13 e^{2T_{j+1}}) on the
   pattern law, ≤ 4·10⁹ T e^{−15.449T} ε_j^{−1.5} proved-modulo-NUMÉRICO. Every individual power saving at a selected
   frequency is exp(−2δT). The mismatch is doubly-exponential against exponential; no refinement of the input closes it.
   (The tail half of (γ) is not even needed — prop:finite — which is the one genuine simplification the induction buys.)
2. **B8 / (δ) — REF-D.** L*_j is an exact restatement of positivity at T_{j+1} given positivity at T_j; the inductive
   hypothesis contributes only 1/μ_j; the regime interior is free (lem:monoT) and the entry instant is empty (invisibility).
   There is no smaller step. This is R186_029 Lemma H(ii) and R186_048 Prop 4.3 for this decomposition.
3. **(θ) / O6 — ℤ-integrality unused.** The specification names no line where the lag set log ℕ, the near-coincidences
   log(n/n′) of the contact block (R9), or integral multiplicities enter. Without such a line the induction is a statement
   about arbitrary positive combs, for which it is false in general (A3, A6-ARGUED).
4. **A15 / (ζ) — if powered as mandated.** BV-, sieve- or mean-value-type inputs for the exterior field place the proof in a
   class closed under finite modification: cor:void at every T > 0.74921.

**What survives, and what is UNDECIDED.** The exact edge-Schur skeleton (Lemma S, the contact block v_{n_j} vs 2n_j^{−1/2}
at the same lag, the exterior-field formulation of the sign) passes the transfer clauses formally and is the structure
corollary (e) leaves open ("exact Schur reductions carrying the whole margin"). It is a correct reformulation of the
contact-to-contact problem and makes explicit that the whole sign at each step is the 𝔄_j-dual norm of the minimizer's
exterior continuation. Whether C* admits a proof mechanism — necessarily a statement about h*_j at precision √(μ_j ν_j),
not a bound on Λ — is OPEN; nothing in the record, in the crossword table, or in the suggested power source supplies
one, and the record's weakened forms of it ((B_T), L2_001, Lemma H) are false or margin-inheriting. **Stop here, as
instructed:** the specification cannot be made to satisfy (γ), (θ) and B8 simultaneously with the mandated power source.

*No numerics were run; no proof was attempted; no sign is certified; no negative value of 𝔞_T for ζ is claimed; no
equivalence between row D and any other statement is used.*

[ nota: ver 03-research/phase-195-modern-tools/VERIFY_CLAMPED_AND_EDGE_LAW.md — el ajuste h*~(T−|t|)^a, a≈0.15–0.25, se reetiqueta: NUMÉRICO como ajuste, lectura de potencia ARGUED como artefacto de resolución de (log 1/δ)^{−1/2}; P_T no impone extremos sujetos sobre F (sí sobre G=(¼−∂²)^{−1}F).]
