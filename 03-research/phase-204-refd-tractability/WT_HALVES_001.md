# WT_HALVES_001 — The two halves of Lemma WT (prop:WT of Paper 46) as independent statements

Phase 204n · pure mathematics; numerics only on already-existing data (NUMERICAL).


## Summary (≤300 words)

Prior correction: in prop:WT, 𝔄 is the form 𝔞_T (archimedean + comb, WITHOUT the polar term) on the sector 𝒟^par_T,
not the full form. The full form is W^par = 𝔄 + 2ε χχᵀ (rank-one perturbation).

**(H1) n₋(𝔄_ev) = 1, 𝔄_odd ≻ 0 ∀T.** (a) n₋(𝔄_par(T)) is non-decreasing in T (PROVED: extension by zero, as W1 of
BARRIER_W_001). (b) The lower bound n₋(𝔄_ev(T)) ≥ 1 for all T ≥ T₀ reduces to ONE explicit comb-free evaluation:
𝔪_{T₀}(χ_ev) < 0 (the comb favors this, Π_T(χ_ev) ≤ 0, PROVED); verified numerically for T₀ = 0.12
(rem:wh-index). CONDITIONAL on a certifiable one-dimensional evaluation → this is the piece that closes without
touching D. (c) The upper bound n₋(𝔄_ev) ≤ 1 ∀T ⟺ the second eigenvalue of 𝔞 on the infinite even sector is ≥ 0:
weaker than WP^ev, OPEN, the same class as (L2). 𝔄_odd ⪰ 0 ∀T is STRONGER than WP^odd and fails with erased primes
(existing datum).

**(H2) q_ev < −½ ∀T.** Exact identity (PROVED, new): q_par + ε/2 = −λ^W_par·⟨𝔄⁻¹χ, (𝔄−λ^W)⁻¹χ⟩ with bracket
> 0, and the minimizer of W^par is exactly (𝔄 − λ^W)⁻¹χ. Hence sign(q_ev + ½) = −sign(λ^W_ev) and
q_ev + ½ ≈ −λ^W‖h_ev‖²/4 = −𝔤_ev/4: the "1e−8 margin" is 𝔤_ev/4 at T = ½log3 (not at Mori μ=15) and is λ^W
multiplied by a normalization; there is no quantity 60 orders of magnitude larger. q_ev(T) is non-decreasing in T
(PROVED via lem:gmono; and on every interval of constant inertia by the Lemma WT-R of §7, which gives the exact law
q(T′)−q(T) = ⟨S⁻¹r,r⟩ of the ring: its bound is 𝒦_H, it does not evade restriction 11) and tends to −½ from below
exactly when 𝔤_ev → 0⁺. (iii) h_par does NOT escape restriction 11: h_par = resolvent at 0, h* = resolvent at λ^W;
they differ by O(λ^W); h_par is moreover the constrained minimizer (a3). NO-GO as an escape route; no explicit
solution of 𝔄g = χ (truncated Wiener–Hopf; the Kreĭn route is already indexed).

**(H3)** Erased primes at ½log3 (rem:polarcapdiag): the even sector fails H2 (q_ev ≈ −0.408 > −½, n₋ = 1), the odd
sector fails H1 (q_odd ≈ −0.056 < 0 ⇒ n₋(𝔄_odd) = 1). Both halves are falsifiable at the comb level.

---

## 0. Corpus check and relation to the index

grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` for "prop:WT," "Lemma WT," "n₋," "inertia," "capacity," "q_ev," "q_odd,"
"thm:parityschur," "prop:wh-polarres," "Weyl," "secular," "Mori (10,0,1)":

- AUDIT_204_CLOSURES_001 and INTEGRATION_204_001 (README l.606, 608): Lemma WT PROVED and integrated; values
  q_ev + ½ ≈ −2e−8, q_odd ≈ ½ − 2.5e−4, n₋(𝔄_ev) = 1, all NUMERICAL and all at **T = ½log3** (rem:polarcapdiag,
  rem:wh-index), not at Mori μ = 15. The target's premise "1e−8 margin at Mori μ=15" is incorrect; I correct it in §2.
- POLAR_CAP_001 (l.598): 𝔤_par as a Schur complement; T6.1 (differential formula = functional of the primitive
  resolvent, NO-GO 𝒦_H/W-lin); PC-1 (lim 𝔤 ≥ 0 takes D as a hypothesis); PC-2 (𝔤_ev ≲ 9e−8 ∀T ≥ ½log3).
- BARRIER_W_001 (l.424–427): W1 PROVED "n₋ non-decreasing, single-sign crossings"; class 𝒦_W (Morse index, spectral
  flow, no-crossing) NO-GO. I use it for H1(a) and do NOT propose homotopy in T as a sign route.
- W12 (04_ l.30): chains of exact identities (secular, Kato, cofactor) NO-GO "signless." The secular identity of §2
  is in that family; I record it as a reading tool (it quantifies what q measures), not as a route.
- LEMMA_I3_001 / GRAM_INERTIA_001 (l.481, 538): inertias in a Galerkin block, (10,0,1) at Mori with null μ⊕1;
  POLAR_CAP_001 l.96 warns that this inertia belongs to a Galerkin block, not to W_T. I do not use it as data for 𝔄.
- R155 round 5 (memory): the Kreĭn reformulation, indexed; relevant for H2(iii).

New reason to enter: the WT halves were never classified by tractability (AUDIT_204_CLOSURES §3 only integrated it).
I am not retrying any indexed route: everything below is a classification of the two halves plus two identities.

## 1. Exact setup (PROVED, reading of P46)

Fixing parity, ε_ev = +1, ε_odd = −1, ℓ_par = ⟨·, χ_par⟩ with χ_par ≥ 0 (even: χ_ev ∝ cosh(x/2) on I_T).
By thm:parityschur(o):

  W^par(F) = 𝔄(F) + 2ε ℓ_par(F)²,  𝔄 := 𝔞_T|𝒟^par_T = 𝔪_T + Π_T  (archimedean + comb, no pole).

prop:WT (hypothesis 0 ∉ spec 𝔄, q ≠ 0): g = 𝔄⁻¹χ, q = ⟨χ, g⟩, h_par = g/q, 𝔞_T(h_par) = 1/q, 𝔤_par = (1 + 2εq)/q, and

  n₋(𝔄) = n₋(𝔞|𝒬^par) + [q < 0],  n₋(W^par) = n₋(𝔞|𝒬^par) + [𝔤_par < 0].  (1.1)

A consequence worth keeping in view (PROVED, from (1.1)): the "halves" of WT are not those of thm:parityschur. The
natural partition (primitive, capacity) = (n₋(𝔞|𝒬), sign of 𝔤) is indexed; WT's partition is (n₋(𝔄), sign of q + ε/2),
which is obtained from the former by moving the bit [q < 0] from one side to the other. This settles part of H3.

## 2. (H2) q and λ^W: exact secular identity

### Proposition S (PROVED)
Let λ := λ^W_par be the bottom of W^par, suppose λ ∉ spec(𝔄) (generic; see note) and v := (𝔄 − λ)⁻¹χ. Then

 (i) v is an eigenvector of W^par with eigenvalue λ and 1 + 2ε⟨χ, v⟩ = 0;
 (ii) q + ε/2 = −λ ⟨𝔄⁻¹χ, (𝔄 − λ)⁻¹χ⟩;
 (iii) if n₋(𝔄) ≤ 1 and λ is the minimum eigenvalue of W^par, the bracket K := ⟨𝔄⁻¹χ,(𝔄−λ)⁻¹χ⟩ is > 0. In particular,
   in the even sector with n₋(𝔄_ev) = 1: sign(q_ev + ½) = −sign(λ^W_ev); in the odd one with 𝔄_odd ≻ 0:
   sign(½ − q_odd) = sign(λ^W_odd).

Proof. (i) W^par v = 𝔄v + 2εχ⟨χ,v⟩ = λv + χ(1 + 2ε⟨χ,v⟩); if W^par u = λu with u ≠ 0, then
(𝔄−λ)u = −2ε⟨χ,u⟩χ, ⟨χ,u⟩ ≠ 0 (otherwise λ ∈ spec 𝔄), u ∝ v and the secular equation 1 + 2ε⟨χ,v⟩ = 0 follows.
(ii) By (i), ⟨χ,v⟩ = −ε/2, so q + ε/2 = q − ⟨χ,v⟩ = ⟨χ,[𝔄⁻¹ − (𝔄−λ)⁻¹]χ⟩ = −λ⟨χ, 𝔄⁻¹(𝔄−λ)⁻¹χ⟩
(resolvent identity). For ε = +1 this gives q + ½ = −λK; for ε = −1,
q − ½ = −λK, i.e. ½ − q = λK. (iii) Spectrally K = Σ_k |χ_k|²/(a_k(a_k − λ)) with a_k the eigenvalues of 𝔄. W^par ≥ 𝔄
(even) or W^par ≤ 𝔄 (odd) differ by rank one; by interlacing (rank-one Cauchy/Weyl), in the even case
a₁ ≤ λ ≤ a₂, and in the odd one λ ≤ a₁. Even with n₋ = 1: a₁ < 0, a₁ − λ < 0 (λ > a₁ strictly because ⟨χ,u⟩ ≠ 0),
positive term; for k ≥ 2, a_k ≥ a₂ ≥ λ, and a_k > 0 if λ > 0 (and if λ ≤ 0 all a_k − λ ≥ a_k > 0), terms ≥ 0;
the sum is > 0 because χ is not orthogonal to all eigenvectors. Odd with 𝔄 ≻ 0 and λ < a₁: all positive. ∎

Note. λ ∈ spec(𝔄) occurs only if 𝔄's eigenvector is orthogonal to χ (non-generic); in that case λ is a common
eigenvalue and the identity holds by continuity in T (outside a discrete set). ARGUED for the degenerate case.

### Corollary S1 (PROVED): what the "1e−8 margin" is
From (i): the minimizer of W^par is exactly h* ∝ (𝔄 − λ^W)⁻¹χ, and h_par = 𝔄⁻¹χ/q is the same resolvent evaluated
at 0. With λ^W small, K = ‖g‖² + O(λ^W) = q²‖h_par‖² + O(λ^W) ≈ ¼‖h_ev‖², hence

  q_ev + ½ ≈ −¼ λ^W_ev ‖h_ev‖² ≈ −¼ 𝔤_ev   (consistent with thm:parityschur(a4): 𝔤 ≍ λ^W‖h‖²).

NUMERICAL check with existing data at T = ½log3: 𝔤_ev ≈ 9e−8 (rem:polarcapdiag) ⇒ q_ev + ½ ≈ −2.25e−8 ✓ (EDITOR:
−2e−8). The "size 1e−62" factor the target asked for does not exist: the number 1e−8 is at ½log3, and the ratio
between q + ½ and λ^W is ‖h‖²/4, a NORMALIZATION (h has ℓ = 1 and W(h) small ⇒ ‖h‖ large). Going from λ^W to q + ½ is
rescaling by ‖h_par‖²; the sign is the same (S(iii)) and there is no new slack. At Mori μ = 15 (λ^W ~ 1e−70 in its
normalization), q_ev + ½ ≈ −¼λ^W‖h_ev‖², and by PC-2 |q_ev + ½| ≲ 2.3e−8 for every T ≥ ½log3; I do not have ‖h_ev‖
at μ = 15 (no datum; I am not inventing one). OPEN as a number; irrelevant as a sign.

### Proposition S2 (PROVED): law in T
If λ^ev_A(S) > 0 at S = T, T′ (T < T′), lem:gmono gives 𝔤_ev(T′) ≤ 𝔤_ev(T). With q_ev = 1/(𝔤_ev − 2) (prop:wh-polarres)
and 𝔤_ev < 2, the function x ↦ 1/(x − 2) is decreasing for x < 2, so **q_ev(T′) ≥ q_ev(T)**: q_ev is non-decreasing
in T. Likewise q_odd = 1/(𝔤_odd + 2) is non-decreasing in T (𝔤_odd > −2). So: q_ev rises toward −½ and q_odd rises
toward ½. WT's condition at each T is "q does not reach ±½"; with (PC-1) this is lim_{T→∞} q_ev ≤ −½ (and < ½ for
odd) — the same statement as lim 𝔤 ≥ 0, already indexed as PC-1 (takes D as a hypothesis). Monotonicity does NOT
give a sign: it says the barrier −½ is approached from below and that all the content is at the limit. By PC-2,
q_ev(T) ∈ [−½ − ε₀, −½) with ε₀ ≈ 2.3e−8 for every T ≥ ½log3 where the hypothesis holds (NUMERICAL for ε₀).

Question (ii) of the target, "does q(T) → −½?": under the hypothesis that λ_A^ev > 0 and λ^W_ev > 0 ∀T, q_ev(T) is
monotone and bounded, converging to q_∞ ≤ −½; q_∞ = −½ ⟺ 𝔤_ev(T) → 0. That 𝔤_ev → 0 is plausible (thm:Z /
λ^W → 0 exponentially and ‖h‖ bounded below) but I do not prove it: ARGUED. There is no q data at ½log5 or ½log15
in the corpus.

### (H2)(iii) A characterization of h_par without minimization? — NO-GO as an escape from restriction 11

1. h_par solves the linear equation 𝔞_T(g, G) = ℓ_par(G) ∀G (Lax–Milgram on the finite negative subspace plus its
   coercive complement). Correct, and on the even sector 𝔄 is indefinite, so g is a saddle point of 𝔞 − 2ℓ, not a
   minimum of 𝔞. But:
2. by thm:parityschur(a3), under WP^par, h_par = argmin{W_T(F) : F ∈ 𝒟^par, ℓ(F) = 1}: it IS a constrained
   minimizer of the full form. The "equation without minimization" is its Euler–Lagrange equation with a multiplier
   on ℓ.
3. by S(i), the free minimizer h* (bottom eigenvector of W^par) is (𝔄 − λ^W)⁻¹χ, and h_par ∝ 𝔄⁻¹χ. Hence
   h_par = h*/⟨χ,h*⟩ + O(λ^W ‖𝔄⁻²χ‖) (PROVED with gap a₂ − λ^W > 0 of 𝔄's spectrum away from 0; the gap is datum:
   at ½log3 the primitive bottoms are ≈ 0.08 and 0.38 with erased primes and ≥ 1e−18 for ζ, prop:wh-index(ii)).
   Every first-order functional of h_par is a functional of h* up to error O(λ^W): Theorem X and restriction 11
   apply to h_par exactly as to h* (branch 1 of P4_SIGNPATTERN, "gradient direction").
4. Explicit solution of 𝔄g = χ: it is an integral equation on I_T with an archimedean kernel + a comb of deltas at
   log n (truncated Wiener–Hopf / Kreĭn problem on a finite interval). The diagonalization via the explicit formula
   (W(F) = Σ_ρ Φ(ρ)Φ(1−ρ), rem:ext-killing(iii)) exists only for W on ℝ, not for the resolvent of 𝔞 restricted to
   I_T; inverting on I_T is exactly the already-indexed Kreĭn problem (R155 round 5). There is NO closed formula;
   NO-GO, recorded.

Verdict (iii): **NO-GO** — h_par is not an object distinct from the minimizer at first order; the linear equation
does not evade Theorem X. What does remain (PROVED, tool): the resolvent pair {𝔄⁻¹χ, (𝔄 − λ^W)⁻¹χ} and formula
S(ii), which converts λ^W into q + ½ with an explicit positive factor.

Verdict (H2): q_ev < −½ ∀T, given n₋(𝔄_ev) = 1, has the same sign as λ^W_ev at each T (S(iii)). It is not "weaker";
it is the same condition rescaled. **TRANSFER (REF-D by S(iii))**. New content: S, S1, S2 (PROVED).

## 3. (H1) The inertia half

### 3.1 Monotonicity in T (PROVED)
Extension by zero 𝒟^par_T ↪ 𝒟^par_{T′} (T < T′) preserves parity, ℓ_par and 𝔞 (proof of lem:monoT/lem:gmono; 𝔞 = W − polar
and both are preserved). By min–max, n₋(𝔄_par(T′)) ≥ n₋(𝔄_par(T)). (This is W1 of BARRIER_W_001 applied to 𝔄 instead
of W; same argument.) Consequences:
- "𝔄_odd ≻ 0 ∀T" ⟺ 𝔞 ≥ 0 on all compactly supported odd functions (and no kernel at each T): a T-free statement.
- "n₋(𝔄_ev) ≤ 1 ∀T" ⟺ sup_T n₋(𝔄_ev(T)) ≤ 1 ⟺ 𝔞 has at most one negative square on compactly supported even
  functions.
- "n₋(𝔄_ev) ≥ 1 ∀T ≥ T₀" ⟸ n₋(𝔄_ev(T₀)) ≥ 1, a datum at a single window.

### 3.2 Lower bound: the piece that closes without D
**Proposition H1⁻ (CONDITIONAL on a one-dimensional evaluation).** If 𝔪_{T₀}(χ_ev) < 0 for some T₀, then
n₋(𝔄_ev(T)) ≥ 1 for every T ≥ T₀.
Proof. prop:wh-index(iii): 𝔞_T(χ_ev) = 𝔪_T(χ_ev) + Π_T(χ_ev) with Π_T(χ_ev) = −Σ v_n c_{χ_ev}(log n) ≤ 0 because
χ_ev ≥ 0 ⇒ c_{χ_ev} ≥ 0 (PROVED in P46). Hence 𝔞_{T₀}(χ_ev) < 0, n₋(𝔄_ev(T₀)) ≥ 1, and §3.1 propagates to T ≥ T₀. ∎
Status of the input: 𝔪_T(χ_ev) is an explicit function of T (C₀, K, autocorrelation of cosh(x/2)·1_{I_T}), WITHOUT
the comb and WITHOUT zeros; rem:wh-index gives it as negative for T ≥ 0.12, NUMERICAL and uncertified. Certifying it
at a single T₀ (e.g. T₀ = 0.12 or ½log3) by interval arithmetic is a standard 1-D quadrature: a task for the
calibrator. With that, H1⁻ becomes PROVED for T ≥ T₀, without touching D or the comb. It is small, but it is
exactly what was asked: a half of a half that closes on its own. It also settles the branch of WT that matters: the
branch "n₋(𝔄_ev) = 0 ∧ q_ev > −½" is EXCLUDED for T ≥ T₀, and the even criterion reduces to
"n₋(𝔄_ev) ≤ 1 ∧ q_ev < −½".

Remark (ARGUED): for large T, |χ̂_ev(τ)|² ~ e^T·(Lorentzian of width ½ with cos 2τT oscillation), whose mass sits
mostly in |τ| ≲ 6.29 where m(τ) < 0 (SPEC_002); this explains why 𝔪_T(χ_ev) < 0 persists, but by §3.1 that is not
needed: a single T₀ suffices.

### 3.3 Upper bound n₋(𝔄_ev) ≤ 1 ∀T
By Cauchy (interlacing with hyperplane 𝒬^ev = ker ℓ_ev): λ₂(𝔄_ev) ≥ λ^ev_A. Hence
  WP^ev_T (λ^ev_A ≥ 0, no kernel) ⇒ n₋(𝔄_ev(T)) ≤ 1,
and n₋(𝔄_ev) ≤ 1 ⟺ λ₂(𝔄_ev) ≥ 0 ⟺ SOME even hyperplane exists (not necessarily Tate's) where 𝔞 ≥ 0. Hence:
  D_ev ⇒ WP^ev ⇒ [n₋(𝔄_ev) ≤ 1]  (strictly weaker, PROVED as implications).
It is also necessary for D (by WT(i) or by rank one: n₋(𝔄) ≤ n₋(W^ev) + 1). On the requested "the pole has rank 1 ⇒
n₋(𝔄) ≤ n₋(A_∞ + C) + 1" argument: here the pole is NOT in 𝔄; the correct relation is
n₋(W^ev) ≤ n₋(𝔄_ev) ≤ n₋(W^ev) + 1 (PROVED, positive rank one). Weyl with the comb (rank₊/rank₋ of Π_T, infinite or
of order #{n ≤ e^{2T}}) gives bounds that grow with T: useless, as the target anticipated. On the archimedean part
alone: n₋(𝔪_T|𝒟^ev) grows with T (m < 0 on |τ| < 6.29 and the window I_T hosts ~ 2T·6.29/π prolate degrees of
freedom with spectral support in that band ⇒ n₋(𝔪_T,ev) ≳ 4T − O(log T), ARGUED via Landau–Pollak–Slepian); the comb
must compensate all but one. So the upper bound is a quantitative statement about the comb at every scale — the
same class as (L2)/WP ∀T (λ_A > 0 ⟺ S_{T,k} ≻ 0, phase 186).
**OPEN; TRACT = transfer to the class of (L2)**, weaker than WP^ev at each T (it allows the positive hyperplane to
not be Tate's) but with no known method of its own: every continuation-in-T argument for n₋ falls into 𝒦_W
(BARRIER_W_001: single-sign crossings; a zero crossing of 𝔄_ev is codimension 1 and nothing forbids it without
Λ-specific data).

### 3.4 Odd sector
𝔄_odd ≻ 0 ⟺ 𝔞 > 0 on all of 𝒟^odd ⟺ [WP^odd and q_odd > 0] by (1.1). It is STRONGER than WP^odd (it also asks for
the bit q_odd > 0, i.e. 𝔤_odd > −2, i.e. 𝔞(h_odd) > 0). prop:wh-index(ii) gives it for T ≤ ½log5 (via thm:log5W,
PROVED in that range). For large T: OPEN, and falsifiable at the comb level (§4).

Verdict (H1): **H1⁻ (n₋(𝔄_ev) ≥ 1 ∀T ≥ T₀): CONDITIONAL on a certifiable quadrature, without D — closable.**
**H1⁺ (n₋(𝔄_ev) ≤ 1 ∀T): OPEN, strictly weaker than WP^ev ⇒ than D; transfer to class (L2); necessary, not
sufficient.** **H1-odd (𝔄_odd ≻ 0 ∀T): OPEN, stronger than WP^odd, falsifiable by erasure.**

## 4. (H3) Falsifiers: which half fails

Existing data (rem:polarcapdiag, T = ½log3, erased primes, Galerkin, NUMERICAL): 𝔤_ev ≈ −0.45, 𝔤_odd ≈ −20,
primitive bottoms ≈ +0.08 (even), +0.38 (odd). With q = 1/(𝔤 − 2ε) (prop:wh-polarres, valid since the primitive
bottoms are > 0):
- even: q_ev = 1/(−2.45) ≈ −0.408. n₋(𝔄_ev) = 0 + [q < 0] = 1. q_ev > −½ ⇒ **H2 fails, H1 holds**.
- odd: q_odd = 1/(−18) ≈ −0.056. n₋(𝔄_odd) = 0 + [q < 0] = 1 ⇒ **H1-odd fails** (𝔄_odd not ≻ 0); q_odd < ½ holds.
(Galerkin gives upper bounds on 𝔤; the negative signs are evidence of true negatives, barring quadrature error.)
cor:convfail(ii) (a_θ, one contact): WP holds and W fails for θ ≤ 0.8148; the even channel already fails at
θ = 1.001 (rem:polarcapdiag) — the boundary of the H2 half sits ~1e−3 from Λ in the weight of n = 2: the H2 half is
as fine as D.

Epstein (Lemma E) and a_P: witnesses in P_T with A = B = 0 (R11_2_ORIGIN, Theorem O3): the negativity lives in 𝒬,
i.e. in n₋(𝔞|𝒬^par) ≥ 1. By (1.1): in the odd sector H1 always fails; in the even sector H1 fails if q_ev < 0
(n₋ ≥ 2) and H2 fails if q_ev > 0. I do not have q_ev for Epstein; without new computation I cannot decide. DH
(parity, odd witness, T ≥ 9/5): the negativity is odd ⇒ the odd condition fails; if the witness is primitive,
H1-odd fails; otherwise it may be q_odd > ½. Request to the calibrator: (a) 𝔪_{T₀}(χ_ev) with intervals; (b) ℓ_odd
of the DH witness and q_odd of DH at T = 9/5; (c) q_ev of Epstein at T = 1.59. All three use existing pipelines.

Reading: both halves break at the comb level (each with its own falsifier: even erasure → H2, odd erasure → H1);
neither is comb-generic ⇒ neither closes under comb-generic hypotheses (barrier theorem, phase 197), except H1⁻,
which does not use the comb (it only uses its favorable sign Π_T(χ_ev) ≤ 0, valid for every comb ≥ 0 — and that is
exactly why it is generic: it holds for Λ, a_P, erased combs, and DH with the same proof, as long as the
archimedean part is that of ζ).

## 5. Verdicts by half

| Statement | Relation to D | Status | TRACT |
|---|---|---|---|
| H1⁻: n₋(𝔄_ev(T)) ≥ 1, T ≥ T₀ | neither implies nor uses it; excludes WT's n₋ = 0 branch | CONDITIONAL (one 1-D quadrature) → PROVED once certified | YES (closable now) |
| Monotonicity n₋(𝔄_par(T)) | tool | PROVED | — |
| H1⁺: n₋(𝔄_ev) ≤ 1 ∀T | necessary; ⇐ WP^ev ⇐ D; strictly weaker | OPEN | transfer to class (L2) |
| H1-odd: 𝔄_odd ≻ 0 ∀T | necessary; stronger than WP^odd | OPEN; falsified by erasure | transfer |
| H2: q_ev < −½ (given n₋ = 1) | sign(q_ev+½) = −sign(λ^W_ev) exact | REF-D (Prop S) | NO |
| H2-odd: q_odd < ½ (given 𝔄_odd ≻ 0) | sign(½−q_odd) = sign(λ^W_odd) | REF-D | NO |
| Prop S (secular identity), S1, S2 (q non-decreasing) | tools | PROVED | — |
| Lemma WT-R (§7): ring law, q monotone with constant inertia | tool; rate bound 𝒦_H | PROVED (formula); bound OPEN | transfer |
| (iii) h_par without minimization | h_par = h* + O(λ^W); is the constrained minimizer (a3) | NO-GO (Theorem X / restr. 11) | NO |

Answer to the target's central question: **no**, D is not encoded in a number 60 orders of magnitude larger than
λ^W. q + ε/2 is λ^W multiplied by K = ⟨𝔄⁻¹χ,(𝔄−λ^W)⁻¹χ⟩ ≈ ‖h_par‖²/4 > 0; the "1e−8" is 𝔤_ev/4 at ½log3 and
decreases with T (PC-2). The quantity carrying the sign is still λ^W, with a different normalization.

What brings us closer to the sign: (1) the even criterion of WT becomes, for T ≥ T₀ and after one quadrature,
"n₋(𝔄_ev) ≤ 1 ∧ q_ev < −½," and the first conjunct is weaker than WP^ev; (2) the sign-carrying half (q) has a
monotone law in T and an exact identity with λ^W, so that all of D's content in the even channel concentrates in
lim_T q_ev(T) ≤ −½ with q_ev non-decreasing — the same statement as PC-1, now with an object (the resolvent 𝔄⁻¹χ)
that does not require inverting 𝔞|P_T (an improvement over POLAR_CAP §4.3, already recorded in AUDIT_204_CLOSURES).

## 6. Entry for the index (README, phase 204)

- **WT_HALVES_001 (204n, halves of Lemma WT; new reason: never classified by tractability).** Note: 𝔄 = 𝔞_T|𝒟^par
  WITHOUT the pole. **Prop S PROVED (secular): h* = (𝔄−λ^W)⁻¹χ exactly; q + ε/2 = −λ^W⟨𝔄⁻¹χ,(𝔄−λ^W)⁻¹χ⟩, bracket > 0 ⇒
  sign(q_ev+½) = −sign(λ^W_ev): H2 = REF-D; "1e−8" = 𝔤_ev/4 at ½log3 (not Mori), normalization ‖h‖²/4.** S2 PROVED:
  q_par non-decreasing in T (lem:gmono). (iii) h_par = h* + O(λ^W) and constrained minimizer (a3): NO-GO,
  Theorem X/restr. 11. **H1⁻ CONDITIONAL→closable: n₋(𝔄_par) non-decreasing in T (PROVED) + Π_T(χ_ev) ≤ 0 ⇒
  n₋(𝔄_ev) ≥ 1 ∀T ≥ T₀ if 𝔪_{T₀}(χ_ev) < 0 (one 1-D quadrature, pending intervals).** H1⁺ (n₋ ≤ 1) OPEN, ⇐ WP^ev,
  class (L2); 𝔄_odd ≻ 0 OPEN, stronger than WP^odd. Erased primes ½log3: even fails H2 (q ≈ −0.408), odd fails H1
  (q ≈ −0.056). Do not retry: "q + ½ as a large margin," "h_par outside Theorem X." (`03-research/phase-204-refd-tractability/WT_HALVES_001.md`)

## 7. Addendum (coordinator): even monotonicity and the variation law of q (WEAKEN_001 §3.1, K11, L-b)

Having read WEAKEN_001 §3.1: Lemma W1 (q_odd = sup ℓ²/𝔞 non-decreasing while 𝔄_odd ≻ 0, PROVED), Cor W1′, Lemma W2
(even: monotonicity declared OPEN "due to indefinite min-max"), (L-b) ring Schur formula, (L-c) probable NO-GO.

### 7.1 Lemma WT-R (exact variation law; PROVED in finite dimension, technically CONDITIONAL in the form case)
Let T < T′, 𝒟^par_{T′} = 𝒟^par_T ⊕ 𝒟^par_R with R = {T < |t| < T′} (L²-orthogonal sum; extension by zero is the
inclusion of the first summand). In blocks, 𝔄′ := 𝔄_par(T′) = [[A₁₁, A₁₂],[A₂₁, A₂₂]] with A₁₁ = 𝔄_par(T)
(lem:monoT: the restriction of 𝔞_{T′} to 𝒟_T is 𝔞_T), A₂₂ = 𝔞_{T′}|𝒟_R, A₁₂ = interior–ring coupling (archimedean
kernel off the diagonal + crossed contacts c_{F,G}(log n)), χ′ = (χ_T, χ_R). If 0 ∉ spec(A₁₁) and 0 ∉ spec(S),
S := A₂₂ − A₂₁A₁₁⁻¹A₁₂, then

  q(T′) − q(T) = ⟨S⁻¹r, r⟩,  r := χ_R − A₂₁ A₁₁⁻¹ χ_T = χ_R − q(T)·A₂₁ h_par(T),          (7.1)
  n₋(𝔄(T′)) = n₋(𝔄(T)) + n₋(S)   (Haynsworth).                                          (7.2)

Proof: block-inversion formula (Banachiewicz) applied to ⟨χ′, 𝔄′⁻¹χ′⟩; (7.2) is additivity of inertia. In the case
of closed forms on L² with compact resolvent, both hold by the same Lax–Milgram argument of prop:WT on the finite
negative subspace plus its coercive complement (technically CONDITIONAL: one must verify that A₁₂ is bounded
relative to the form domain — the archimedean kernel between interior and ring is smooth except at t = ±T, where
the log singularity is integrable; ARGUED).

### 7.2 Answer to (a): monotonicity of q_ev — PROVED (resolves Lemma W2 of WEAKEN)
**Corollary WT-R1.** If n₋(𝔄_par) is constant on [T, T′] (and there is no kernel at the endpoints or in S), then
S ≻ 0 by (7.2), and (7.1) gives q_par(T′) − q_par(T) = ⟨S⁻¹r,r⟩ ≥ 0. **q_par is non-decreasing on every interval of
constant inertia of 𝔄_par, in either parity.** In particular q_ev is non-decreasing while n₋(𝔄_ev) = 1, with no
hypothesis on λ_A (an improvement over my S2, which required λ^ev_A > 0, and over Lemma W1, which required 𝔄 ≻ 0).
WEAKEN's objection ("indefinite min-max") is evaded because monotonicity is not taken from a variational
characterization but from the positivity of S, which is a consequence of constant inertia. With §3.1 (n₋
non-decreasing) and H1⁻: for T ≥ T₀ the intervals of constant inertia are maximal until n₋ jumps; at a jump,
n₋(S) ≥ 1 and the increment can have any sign — this matches WT: after a jump to n₋ = 2 the even sector stops being
positive, so **under D the even channel is a single interval of inertia 1 on [T₀, ∞) and q_ev rises monotonically
toward −½ from below**; the even margin (≈ 2e−8 at ½log3) is consumed just like the odd one.

### 7.3 Answer to (b): does the bound in (7.1) evade restriction 11? — NO (𝒦_H), with a useful nuance
1. r depends on h_par(T) and on the coupling with the ring. By Prop S(i), h_par(T) = h*_T/ℓ(h*_T) + O(λ^W_T/gap):
   **h_par is the minimizer of W_T up to an error of the order of the bottom itself.** "It depends on h_par and not
   on the minimizer" is therefore false at every relevant precision: any bound on ⟨S⁻¹r,r⟩ obtained from properties
   of h_par is a bound in terms of h*. Pattern 𝒦_H (inequalities evaluated at the minimizer), restriction 11.
   Moreover A₂₁ contains exactly the new contacts n ∈ (e^{2T}, e^{2T′}] and the crossed interior–ring contacts: the
   Λ-specific content of the increment is "how the new primes see h*," which is the form of Theorem X (new primes
   must cancel σ on U at resolution π/T).
2. Nuance (PROVED as an identity; useful as a diagnostic): (7.1) is EXACT and second order (a quadratic form in r
   with S ≻ 0), not a first-order discriminant; that is why it is not literally a linear functional of h*, and
   Theorem X, which concerns first order, does not kill it by itself. But the size of r is fixed: χ_R ~ e^{T′/2}
   and the sum of increments ∫ ≤ margin (2.3e−8 even, 2.5e−4 odd) forces a relative cancellation
   |r|/|χ_R| ≲ (margin·‖S‖)^{1/2} e^{−T/2} between χ_R and q·A₂₁h_par: h_par must "predict" χ on the ring to simple
   exponential precision. This is the scalar version of the perturbative step of Cor 2′ (W2); the required scale is
   simple exponential in T per unit of ring, not double — ARGUED (I do not have ‖S‖ or r measured).
   This matches WEAKEN's warning (L-b): if it dies, it dies at scale 10⁻⁴ (odd) / 10⁻⁸ (even).
3. Comb-genericity: a bound ⟨S⁻¹r,r⟩ ≤ Ce^{−δT}(T′−T) with comb-generic constants is impossible: with erased
   primes, q_ev(½log3) ≈ −0.408 is already above −½ (§4) and in a_θ the even channel crosses at ~1e−3 from Λ
   (rem:polarcapdiag); the bound has to be Λ-specific. NO-GO for comb-generic classes (ARGUED with existing data;
   PROVED via cor:convfail in the odd case for a = Λ1_{n≥5}).
Verdict (b): **formula (7.1)–(7.2) PROVED; even monotonicity PROVED; the rate bound is OPEN and lives in 𝒦_H — it
does not evade restriction 11.** What changes relative to λ^W is the NORMALIZATION of the target (accumulated
budget 2e−8 / 2.5e−4 instead of a bottom of 1e−70), not the class of the object. CALIB_R4's data (q at 8 windows)
will directly measure the increments (7.1): the empirical question is whether Δq per unit of T decays (e.g. like
e^{−T}) or stays constant; if it decays geometrically with a measurable ratio, conjecture W1-c (and its pair) remain
as a scalar target with a budget, now in both sectors.

Additional entry for the index: **Lemma WT-R PROVED (Banachiewicz + Haynsworth on 𝒟_T ⊕ ring): q(T′) − q(T) = ⟨S⁻¹r,r⟩,
n₋(𝔄(T′)) = n₋(𝔄(T)) + n₋(S) ⇒ q_par non-decreasing on every interval of constant inertia (resolves W2 of WEAKEN:
q_ev monotone while n₋(𝔄_ev) = 1). r = χ_R − q·A₂₁h_par and h_par = h* + O(λ^W) (Prop S) ⇒ the rate bound is 𝒦_H,
does not evade restriction 11; comb-generic is impossible (erased primes).**
