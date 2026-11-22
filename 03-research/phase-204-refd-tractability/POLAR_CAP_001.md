# POLAR_CAP_001 — Route 2 of TRACT_001 (R6): the polar capacity 𝔊_T = diag(𝔤_ev, 𝔤_odd) as an object in its own right

Phase 204h · pure mathematics · labels PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.
House rule: row D (and L′♯) is treated as an independent goal; no external equivalence is used here.

## 0. Index and corpus check

grep over `05-meta-and-planning/ROUTES-TRIED-INDEX/` («polar cap», «polar capacity», «g_±», «156», «converse», «Tate triple»):

- 04_ l.204 **P156** per-window converse (2×2 polar capacity): FALSIFIED in comb models; l.91 **F-comb**.
- 04_ l.148 **R186-polarcap5**: 𝔊_T ≻ 0 beyond ½log5, existence by continuity PROVED, certified window OPEN; 06_ l.193 same.
- 06_ l.212 **boundary triples**: «Tate triple = polar capacity; no edge trace; KVB hypothesis = λ_A ≥ 0, REF-D» (phase-199 PROOF_L_SHARP_OO_001).
- AUDIT_CONSTRAINTS_001 restriction **11** (SOFT): no flow/continuation in T without a virial-type bound (H).
- L2_INTERLACE_001: Lemma T3 (PROVED) In(W_T) = In(𝔞_T|𝒱_k) + In(S_{T,k}) + In(𝔊_T); R6 ≠ (L2); R6 relies on λ_A > 0.

Definition sources (Paper 46 main.tex): thm:parityschur (l.4176), prop:polarcap (l.4316), lem:gmono (l.4715),
prop:onewindow, cor:convfail (l.4771), rem:polarcapdiag (l.11151), lem:monoT (l.502), eq:target (l.135), lem:polar (l.1742).

New reason relative to P156: TRACT_001 §R6 proposes treating g_± dynamically (Hadamard in T + non-crossing), not as a
condition on a single window. That difference is what is examined here; if it falls, it falls for a new reason that is recorded.

## 1. Exact definition of 𝔊_T (from P46)

P46 notation: χ_ev = cosh(t/2)·1_{I_T}, χ_odd = sinh(t/2)·1_{I_T}, ℓ_par(F) = ⟨F, χ_par⟩, ε_ev = +1, ε_odd = −1,
𝒬^par_T = ker ℓ_par ∩ 𝒟^par_T (the primitive part of the sector), and

  W_T(F) = [𝔞_T(F_e) + 2 ℓ_ev(F_e)²] + [𝔞_T(F_o) − 2 ℓ_odd(F_o)²]       (thm:parityschur(o), PROVED).

**Definition (thm:parityschur(a)).** If 0 ∉ spec(𝔞_T|𝒬^par_T), there exists a unique h_par ∈ 𝒟^par_T with ℓ_par(h_par) = 1 and
𝔞_T(h_par, G) = 0 ∀G ∈ 𝒬^par_T; set 𝔤_par(T) := W_T(h_par) = 𝔞_T(h_par) + 2ε_par, and 𝔊_T := diag(𝔤_ev, 𝔤_odd).
prop:polarcap: 𝔊_T = S^Sch_T + D_pol, S^Sch_T = diag(𝔞_T(h_ev), 𝔞_T(h_odd)), D_pol = diag(2, −2).

**Answer to question 1.** h_par is built in the proof as h = H_0 − Y with Y = (𝔞_T|𝒬)^{-1} 𝔞_T(H_0, ·)
(Lax–Milgram on 𝒬_+, finite matrix on 𝒬_−). Hence

  𝔤_par = 𝔞_T(H_0) − ⟨𝔞_T(H_0,·), (𝔞_T|𝒬^par_T)^{-1} 𝔞_T(H_0,·)⟩ + 2ε_par,

a bordered Schur complement over the primitive part. **It does invert 𝔞_T|𝒫_T.** Honest precision:

- The *definition* consumes only the non-degeneracy 0 ∉ spec(𝔞_T|𝒬^par_T), not positivity (PROVED, thm:parityschur(a)).
- But every property of 𝔤_par connecting to the positivity of W_T consumes λ^par_A(T) > 0: the variational
  characterization (a3) 𝔤_par = min{W_T(F): ℓ_par(F) = 1}, the lower bound (a4), the assembly (c) and lem:gmono.
  Without λ_A > 0, 𝔤_par is an algebraic number from an indefinite Schur and controls nothing (n_−(W_T) = n_−(𝔞|𝒬) + [𝔤<0], (a2)).

Verdict §1: 𝔊_T **is not an object in its own right, independent of the primitive part**: it is the «polar floor» of Lemma T3's
tower and is defined after inverting the primitive floor. Classification: **TRANSFER** (from the primitive form to the 2×2 one,
with the inverse of the primitive built into the coefficients).

## 2. T6.1 — domain variation (Hadamard) of 𝔤_par

**2.1 What varies with T (PROVED, from lem:monoT/lem:gmono).** Under extension by zero I_T ↪ I_{T'}:
the norm, A(F), B(F), ℓ_par(F) (because χ_par|_{I_T'} restricts to χ_par|_{I_T}) and 𝒞_F do not change; the new contacts
n with log n ≥ 2T do not see F (𝒞_F(log n) = 0). Hence W_{T'}|_{𝒟_T} = W_T. **The form does not depend on T
explicitly**: all of 𝔤_par's T-dependence is that of the domain. In particular the «directions e^{±t/2}» do not
change on old functions and the contacts produce no jumps: they enter with zero weight on the old domain.

**2.2 Monotonicity (PROVED, P46 lem:gmono).** If λ^par_A(S) > 0 for S = T, T', then 𝔤_par(T') ≤ 𝔤_par(T).
This is Hadamard's domain principle in its integral form: a minimization problem with a fixed linear constraint over
nested domains.

**2.3 Differential formula (ARGUED).** By (a1), h = h_par(T) satisfies the Euler–Lagrange equation with multiplier

  W_T(h, G) = 𝔤_par(T) · ℓ_par(G)   ∀G ∈ 𝒟^par_T,                                  (EL)

i.e. 𝒲 h = 𝔤_par χ_par on I_T (in the weak sense), with 𝒲 the operator of the full form (archimedean symbol
of logarithmic order + prime comb + rank-2 polar part). The envelope theorem for the nested family gives,
for T outside the (at most countable) set where the minimizer degenerates,

  d𝔤_par/dT = − 𝔅_T[h_par(T)],   𝔅_T[h] ≥ 0,

where 𝔅_T[h] is the first-order gain from admitting support in the layers [T, T+dT] and [−T−dT, −T], i.e. a
quadratic form in the boundary trace (weighted according to the order of the symbol) of the residue r = 𝒲h − 𝔤_par χ_par
evaluated just outside I_T. For local operators of order 2 it is −|∂_n u|²; for P46's symbol (log order)
the exact trace requires a boundary regularity analysis that has not been carried out in the corpus; that is why it is ARGUED
and not PROVED. The sign part (d𝔤/dT ≤ 0) is indeed PROVED (2.2).

**2.4 Functional of what? (decision).** 𝔅_T depends on h_par(T) = H_0 − (𝔞_T|𝒬)^{-1}𝔞_T(H_0,·), i.e. on the
resolvent of the primitive form applied to the polar datum. It is not boundary data independent of the minimizer
(F(±T) of a fixed test, contact positions): the contacts do not even appear in d𝔤/dT except through
h_par. This is exactly the 𝒦_H / W-lin situation from the grid (every first-order discriminant is a functional of h*,
not of σ) and that of L2_INTERLACE_001 T13.1 (Hellmann–Feynman = functional of h*). Moreover the Tate triple's
Weyl-function route (06_ l.212) is the same object: Q_T(0) = E*A_T^{-1}E.

**Verdict T6.1:** formula = PROVED in sign (monotonicity), ARGUED in differential form; as a tool for
fixing the sign of 𝔤_par: **NO-GO** (𝒦_H, resolvent of 𝔞_T|𝒫_T inside the derivative). The only thing the derivative
gives for free is that 𝔤_par decreases, which is the wrong direction for a «does not cross 0» argument.

## 3. T6.2 — «𝔤_± does not cross 0»: what it means with these definitions

**3.1 Is the sign always known? No.** The goal's hypothesis (known inertia of the full form, «exactly one
negative eigenvalue from the pole») conflates two objects. lem:polar: the polar term 2Re(A B̄) has exactly one
negative square (in coordinates (α, β) it is 2αβ, D_pol ≅ [[0,1],[1,0]]). But that is the floor D_pol, not the full
form W_T. The full form has n_−(W_T) = n_−(𝔞|𝒬^ev) + n_−(𝔞|𝒬^odd) + #{par: 𝔤_par < 0} (a2), and P46
takes as its goal the «full version» λ^W_T ≥ 0 ∀T (eq:target, l.135–137): **the inertia of W_T is not a theorem**
beyond the certified windows. I found no claim «(10,0,1)» about W_T in P46; the inertia
(·,0,1) appearing in Mori memos is that of a Galerkin block, not of W_T, and I do not use it.

What is indeed proved:
- 𝔊_T ≻ 0 for 0 < T ≤ T_5 = ½log5 (thm:log5W + thm:parityschur(c); P46, PROVED with computer verifications),
  and on [T_5, T_5+ε] with ε useless (R186-polarcap5). With Mori (CITED) up to ½log15.
- 𝔤_par **can** be negative with λ_A > 0 for modified weights: cor:convfail (PROVED with computer) gives
  𝔤_odd < 0 with λ_A(T;a) > 0 for a = Λ·1_{n≥5}, T ∈ [0.4608, 0.58], and for a_θ with θ ≤ 0.8148 at T = ½log3.
  rem:polarcapdiag (NUMERICAL): with no primes, 𝔤_ev ≈ −0.45, 𝔤_odd ≈ −20 at ½log3.

Hence «does not cross» is **not tautological** (there are crossings in the class closed under deletion/lowering of a
term) nor false (it is true in the certified windows). TRACT_001 was not wrong that it is nontrivial.

**3.2 But it is not independent either (PROVED, combining results from P46).**

> **Proposition PC-1.** Suppose λ_A(T) > 0 for all T > 0. Then the following are equivalent:
> (i) 𝔤_ev(T) ≥ 0 and 𝔤_odd(T) ≥ 0 for all T (R6, «does not cross»);
> (ii) lim_{T→∞} 𝔤_par(T) ≥ 0 for both parities (the limits exist in [−∞, ∞));
> (iii) λ^W_T ≥ 0 for all T (full version of eq:target).
> And (iii) ⟹ eq:target.

*Proof.* lem:gmono gives that 𝔤_par is non-increasing in T (the hypotheses λ^par_A > 0 hold by thm:parityschur(o)),
so the limits exist and (i)⟺(ii). prop:onewindow(i) with arbitrary T_1 = T gives (i)⟺(iii). λ^W_T ≤ λ_A(T)
(l.133) gives (iii) ⟹ eq:target. ∎

Consequences:
1. R6 requires strict eq:target as a hypothesis for it to be well defined (the Schur of §1) and concludes something
   **stronger** than eq:target. It is not a more tractable reformulation of D: it is D plus a floor. Classification
   **TRANSFER (+ extra floor)**, TRAT column = «transfer», not «yes».
2. The form «does not cross 0» is the form «the limit of a monotone decreasing function is ≥ 0», exactly the same
   logical form as eq:target for λ_A (lem:monoT). TRACT_001's continuation argument (if 𝔤(T*) = 0 then
   EL + boundary are incompatible) falls under restriction 11 (SOFT: no flow/continuation without a virial-type
   bound), and at T* with 𝔤_par(T*) = 0, equation (EL) reads 𝒲h = 0 on I_{T*}: h is in the radical of W_{T*}
   ((a2)), which **does not** contradict anything structural; in fact it occurs in the family a_θ at θ = θ_* (cor:convfail(ii):
   the set of θ with λ^W ≥ 0 is [θ_*, 1], so at θ_* there is a radical). Any contradiction must use
   a feature of Λ that neither Λ·1_{n≥5} nor a_{θ_*} have: cor:convfail(iii)'s barrier applies literally.
3. Lemma T3 remains coherent: R6 is the upper floor; it cannot be more accessible than the lower floor it depends on.

**Verdict T6.2: OPEN as a statement; NO-GO as a route** (reason: PC-1 + cor:convfail(iii) + restriction 11).

## 4. Is there any statement of its own left about the polar block?

**4.1 Relation to the Tate mode (PROVED, already in P46).** ℓ_ev(F) = (A+B)/2, ℓ_odd(F) = (A−B)/2 with A = Φ_F(1),
B = Φ_F(0); prop:polarcap: E_T(β, α) = inf{W_T(F): Φ_F(0)=β, Φ_F(1)=α} = (α,β)𝔊^{AB}_T(α,β)ᵀ. 𝔊_T **is** the minimum
energy of prescribing the Tate mode at the poles s ∈ {0,1}. If «f♯(0)» from PI4/PI5 is Φ_F at the pole, the requested
relation is prop:polarcap's identity and there is nothing new (CONDITIONAL on that notation identification, which I did
not verify in PI4/PI5). With the «leak ℓ»: if it is ℓ_par, it is literally the coordinate x of (a1), W_T(G + x h) =
𝔞_T(G) + 𝔤 x²: the leak costs exactly 𝔤 per squared unit (PROVED, (a1)).

**4.2 Uniform ceiling of the even channel (PROVED + NUMERICAL; new as a statement).**

> **Proposition PC-2.** If λ_A(S) > 0 for S ∈ [T_0, T], then for every F ∈ 𝒟^par_{T_0} with ℓ_par(F) ≠ 0,
>   𝔤_par(T) ≤ W_{T_0}(F) / ℓ_par(F)².
> In particular 𝔤_par(T) ≤ 𝔤_par(T_0) for all T ≥ T_0.

*Proof.* (a3) at T and extension by zero (lem:gmono). ∎ (PROVED)

With rem:polarcapdiag's Galerkin test at T_0 = ½log3 (16/24/32 modes, stable): 𝔤_ev(½log3) ≲ 9·10⁻⁸ and
𝔤_odd ≲ 1·10⁻³ (NUMERICAL; a Galerkin bound is legitimately an upper bound up to quadrature/rounding). With PC-2:

  **𝔤_ev(T) ≲ 9·10⁻⁸ for all T ≥ ½log3** (NUMERICAL, certifiable in interval arithmetic at
  finite cost because it is a single evaluation of W on an explicit test).

Together with PC-1, the full version of eq:target forces 𝔤_ev(T) ∈ [0, 9·10⁻⁸] for all T ≥ ½log3: the even
channel lives in a strip of width 10⁻⁷ uniformly in T, and S^Sch ≈ diag(−2, +2) cancels the polar floor up to 10⁻⁷
(rem:polarcapdiag). Reading for D: any non-crossing argument for the even channel must have resolution
≤ 10⁻⁷ in every window, consistent with the margin walls (W-mom, margins 10⁻¹⁸ at T_5). This is a
**quantitative falsifier** for any R6 proposal via perturbation/continuation with loss > 10⁻⁷.

**4.3 Capacity formula when the extended primitive form is invertible (PROVED, routine).** If 𝔞_T is
invertible on the whole sector 𝒟^par_T (not only on 𝒬), minimizing 𝔞_T over {ℓ = 1} gives
𝔞_T(h_par) = 1 / ⟨χ_par, 𝔄_T^{-1} χ_par⟩ (when 𝔞_T|𝒟^par ≻ 0), hence

  𝔤_odd ≥ 0 ⟺ ⟨χ_odd, 𝔄_T^{-1} χ_odd⟩ ≤ ½,  and 𝔤_ev ≥ 0 automatically in that case.

This is the Weyl function of the Tate triple (06_ l.212): nothing new as an object, and the hypothesis 𝔞_T|𝒟^ev ≻ 0 is not
available (rem:polarcapdiag gives 𝔞_T(h_ev) ≈ −2, so 𝔞_T is not positive on the even sector). I record only the
consequence: **the even channel does not admit the positive capacity formula; the positivity of 𝔤_ev is a
−2 + 2 cancellation, not a capacity.** (PROVED given the numerical sign value; NUMERICAL in the sign of 𝔞_T(h_ev).)

## 5. Verdict

| question | answer | label |
|---|---|---|
| 1. Does 𝔊_T invert 𝔞_T|𝒫_T? | Yes: bordered Schur over 𝒬^par; definition needs 0 ∉ spec, its uses need λ_A > 0 | PROVED (P46) |
| 2. T6.1 | d𝔤/dT ≤ 0 PROVED; differential formula = boundary trace of h_par's residue, a functional of the resolvent | PROVED / ARGUED; as a route NO-GO (𝒦_H) |
| 3. T6.2 | Not tautological (cor:convfail: crossings with λ_A > 0 for modified weights), not false (≻ 0 up to ½log5); but ⟺ full version of eq:target and implies it (PC-1) | OPEN; route NO-GO / TRANSFER |
| 4. Statements of its own | PC-1 (equivalence and monotone limit), PC-2 (uniform ceiling; 𝔤_ev ≲ 9·10⁻⁸ ∀T ≥ ½log3), 4.3 (even channel = cancellation, not capacity) | PROVED / NUMERICAL |

TRACT_001 §R6 is thus corrected: R6 is neither «yes» nor «structure of its own»; it is an upward TRANSFER (polar floor over the
primitive floor, Lemma T3) and its dynamics in T is monotone in the bad direction. The goal's hypothesis that 𝔤_±
always has a PROVED sign is **false**; the final classification (TRANSFER/NO) coincides anyway, for a different reason.

Input for D: (a) PC-2 as a quantitative falsifier for any perturbative proposal on the even channel;
(b) the odd channel has margin 10⁻³ at ½log3 and does, in principle, admit the capacity form ⟨χ_odd, 𝔄^{-1}χ_odd⟩ ≤ ½
if 𝔞_T|𝒟^odd ≻ 0 — but any bound on that resolvent is 𝒦_H.

## 6. Entry for the index

| POLAR_CAP_001 (phase 204h) | R6 of TRACT_001: polar capacity 𝔊_T via Hadamard (T6.1) + non-crossing (T6.2) | dual certificates / domain variation | NO-GO (TRANSFER) | 𝔊_T = bordered Schur over 𝒬^par (inverts 𝔞|𝒫_T); d𝔤/dT ≤ 0 (lem:gmono) and the derivative is a functional of the resolvent (𝒦_H); PC-1: with λ_A>0 ∀T, «𝔤_± ≥ 0 ∀T» ⟺ λ^W_T ≥ 0 ∀T ⟹ eq:target (TRANSFER + floor); not tautological (cor:convfail); continuation = restriction 11 and barrier cor:convfail(iii). New PROVED: PC-2 ceiling 𝔤_par(T) ≤ W_{T_0}(F)/ℓ(F)², ⇒ 𝔤_ev ≲ 9·10⁻⁸ ∀T ≥ ½log3 (NUMERICAL). Do not retry without an object that avoids (𝔞_T|𝒬)^{-1}. |
