# Round 7, B — stage predicate for induction over primes

Notation of the common brief: a_T(F) = Arch(F) − Σ_n v_n c_F(log n) on P_T; Π_{T,n}(F) := v_n c_F(log n);
𝔪_T := Arch. A «stage» is a set S of already incorporated contacts; Q_S := 𝔪_T − Σ_{n∈S} Π_{T,n}.

## 0. Four-point filter

**(1) Closest antecedent, read in primary sources.**
- `ROUND_005_G2.md` §3 «Closure theorem that would have to be proved»: predicate I(Q, S) with (i)–(iv); (iv) open;
  the trivial predicate I(Q,S) := «Q + Σ_{p∉S}Π_{T,p} ⪰ 0» is (★)_T (pattern J3). Lemma 2: additive semigroups with
  bounded index, NO-GO for T > ½ log 2.
- `phase-122-.../P122_018_...COCYCLE_PARITY_NO_GO.md` §§1–4: stages Γ_ℝ∏_{p∈S}Z_p with twisted functional equation;
  symmetric coupling vanishes; the causal one is the incoming history.
- `phase-197-barrier-theorem/BARRIER_W_001_...md` §§1–6: W1 (n₋ monotone in T, single-signature crossings),
  W2 (segments in the weight), §6 (the only datum proper to Λ at a crossing is c_{h*}(log n)).
- `REVIEW_005.md` R5-d and `ROUND_005_G4.md` Lemmas 1–3 (at the crossing the incoming weight has no influence).
- `RULES_AVOID.md` §O and `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §10 (DIR split exists up to T ≈ 0.695; at 0.70
  one square is missing).

**(2) New object or claim.** I found no candidate predicate. What is new is a reduction lemma
(§1, PROVED): every stage predicate whose step is *uniform in the history* (depends only on the incoming
contact) and which is of translated-convex-cone or bounded-inertia type is equivalent to a local split with
increments in the cone; i.e. it falls into class O / `G2_B8` or into L6. Plus an observation (§3, NUMERICAL
+ ARGUED) on where the first missing square appears: immediately after the entry of the
power 4 = 2², not of a prime.

**(3) Why it would avoid the difficulty.** It does not: the lemma says exactly what a
candidate would need in order to escape (a history-dependent step through a transported non-quadratic object with
its own formula, which is not the minimizer). I build nothing without that piece.

**(4) Connection with global positivity.** For a cone predicate, (c) would be
a_T + R_∞ ∈ 𝒦 ⟹ a_T ⪰ 0 on P_T for all T; the lemma shows that, with uniform step, this is the
identity a_T = 𝔪_T + R_∅ − R_∞ + Σ_n q_n, q_n ∈ 𝒦, i.e. the split. There is no new connection.

**Gate verdict:** no candidate passes. The rest of the memo justifies the discard and records
the reopening operation.

## 1. Reduction lemma for uniform steps

Let H := P_T (real, Hilbert). The Π_{T,n} are bounded forms on L²(I): |c_F(u)| ≤ ‖F‖².

**Lemma 1 (convex cone; PROVED).** Let 𝒦 be a convex cone of bounded forms on H and R_k bounded forms.
Set 𝒫_k(Q) :⟺ Q + R_k ∈ 𝒦. The following are equivalent:
(a) for every bounded Q, 𝒫_k(Q) ⟹ 𝒫_{k+1}(Q − Π_{T,n_{k+1}});
(b) q_{k+1} := R_{k+1} − R_k − Π_{T,n_{k+1}} ∈ 𝒦.
*Proof.* (b)⟹(a): Q − Π + R_{k+1} = (Q + R_k) + q_{k+1}, a sum of two elements of the cone.
(a)⟹(b): Q := −R_k satisfies 𝒫_k (0 ∈ 𝒦 since a cone is closed under scalars ≥ 0, taking 0·x); (a) gives
q_{k+1} ∈ 𝒦. ∎
Consequence: the full chain is a_T + R_∞ = (𝔪_T + R_0) + Σ_k q_k with q_k ∈ 𝒦. With 𝒦 = forms ⪰ 0 on H
it is the local per-contact split of §O (with prime powers as separate contacts). With 𝒦 ⊋ PSD,
(c) requires a separate final argument that uses Λ, and that argument is the goal.

**Lemma 2 (bounded inertia; PROVED in finite dimension, ARGUED at form level).** Let 𝒫_k(Q) :⟺
n₋(Q + R_k) ≤ r on H, with dim H ≥ r + 2. If D := R_{k+1} − R_k − Π_{T,n_{k+1}} is not ⪰ 0, there exists Q with
𝒫_k(Q) and not 𝒫_{k+1}(Q − Π).
*Proof (finite dimension).* Let v be a unit vector with ⟨Dv,v⟩ = −δ < 0. Take E ⊥ v of dimension r,
V := (E ⊕ ℝv)^⊥ and X := N P_V − N P_E (with P orthogonal projections), X v = 0; n₋(X) = r. Let Q := X − R_k.
On E ⊕ ℝv, X + D has block −N + O(‖D‖) on E and ⟨Dv,v⟩ = −δ on v; the couplings with V are eliminated by
Schur with error O(‖D‖²/N). For N large the restriction to E ⊕ ℝv is negative definite and n₋(X + D) ≥ r + 1. ∎
At form level (H infinite-dimensional) the same argument with E, v in a finite subspace and N P_V on
the complement works because D is bounded; I leave it ARGUED for not writing out the domain details of Arch.
Consequence: inertia predicates with uniform step also require increments ⪰ 0; they fall into L6/W1 or into §O.

**Reading.** Item (b) of the brief, read as «a statement about one contact», only has content if the step is not
uniform in Q; but then 𝒫_k must transport a datum of the stage (not just membership), and that datum
is the one that has to carry the sign.

## 2. Directions examined, one by one

| Direction | Closed entry it falls into | Operation that would reopen it |
|---|---|---|
| Pair (form, measure or auxiliary positive kernel) whose negative part is consumed by the next contact, fixed rule | Lemma 1 ⟹ split with q_n ⪰ 0: §O (O1, O3), `G2_B8_R4` §1, `G2_B8_R5` Thm. D; data §10.2: fails from T ≈ 0.70 in the DIR class | Closed formula for the transferred negative part (a square λℓ⊗ℓ at T ∈ (0.695, 0.72)) as a named term of another contact (reopening of §O) |
| Inertia + negative subspace of fixed description | Lemma 2; L6, BARRIER_W_001 W1 (n₋ monotone, comb-generic) | A condition independent of the Euler–Lagrange equation on the kernel (W3(b)): none known |
| Comparison with Arch on a subspace that shrinks with k | If the subspace is {c_F(log n) = 0 for later contacts}, these are quadratic, not linear, conditions: P47 lem:degen, §P (P1). If it is linear and of prior description, §P requires growing dimension and identity on all of P_T | A linear S_T written without solving the problem (reopening of §P) |
| Moving window: stage k = T ∈ [T_k, T_{k+1}), T_k = ½ log n_k | R162_802 §§4–5, R162_2701, BARRIER_W_001 §6, R5-d. At T_k the incoming weight is invisible (Lemma 1 of G4); between contacts the comb is frozen and only window growth acts, which drives every finite comb negative | See §2.1 |
| Stages with twisted functional equation (Γ_ℝ∏_{p∈S}Z_p) | P122_018 (symmetric coupling vanishes, the causal one is the incoming history 𝓛_{T,−}), G2 Lemma 3 | Reading the cocycle non-symmetrically with a new sign term: not found |
| Admissible interval of the incoming weight, J_{k+1}(T) ∋ v_{n_{k+1}} | R5-d Lemma 2: it is the goal (J3) | — |

### 2.1 What a window–prime coupled predicate would have to add

A natural coupled predicate is one with margin: 𝒫_k :⟺ λ_A(T) ≥ m_k(T) on [T_k, T_{k+1}) with explicit m_k.
The step requires: (i) that the deficit caused by window growth in the frozen gap
[T_{k+1}, T_{k+2}) stay below the gain of the contact n_{k+1}; (ii) the latter, by Hellmann–Feynman,
is v_{n_{k+1}} c_{h*}(log n_{k+1}) on the minimizer (BARRIER_W_001 §6, Theorem X, W-fam). The predicate
would have to add a lower bound of c_{h*_T}(log n) that does not go through h* — exactly the recorded wall.

Additional restriction from the data (NUMERICAL, ROUND_006 §10.3): at T = 0.70 the form is positive only for
c in an interval of width ≲ 10⁻³ around 1, and the bottom at c = 1 is 7·10⁻⁸ (0.70) and 10⁻⁹ (0.75) in that
discretization. ARGUED: no predicate with open slack in the weight (stable under cΛ perturbation of
order 10⁻³) can serve at T ≥ 0.70; the step would have to be an identity or an inequality without uniform
slack, which reaffirms that the fixed rule of a cone (Lemma 1) does not suffice and that the reopening must be exact.

## 3. Observation on the first missing square (NUMERICAL + ARGUED)

½ log 4 = log 2 = 0.6931 and the DIR threshold lies in (0.695, 0.70): the first missing square appears right
after the entry of the contact n = 4. At the optimum q₂ (which contains Π_{T,2} + Π_{T,4}) carries the only negative
eigenvalue and ℓ resembles the projection of cos(2πt/log 2) onto P_T (overlap 0.91–0.93). Reading (ARGUED,
not verified with 4 separated): the stage must be indexed by prime powers, and the necessary transfer
is between the «family of 2» and the archimedean/3 exactly when the term 2² enters. This fixes the **first
non-trivial case** that any future candidate will have to resolve: T ∈ (½ log 4, ½ log 5), contacts {2, 3, 4},
with an explicit square ℓ_T. Falsifiers in that case: delete 4 (changes q₂ and, in those data, the bottom);
c = 2 (negative form); Beurling: the frequency of ℓ ≈ 1/log 2 should move with the lattice.
I have no formula for ℓ_T, so this is not a candidate, only the test target.

## 4. Result

No candidate passes the gate. The directions of the brief fall into §O, §P, L6/BARRIER_W_001, P122_018 or
R5-d, and Lemmas 1–2 explain why: a step that depends only on the incoming contact is a local split
with increments in the cone. Precise reopening: a predicate with non-uniform step that transports a datum
of the stage with its own formula (not the minimizer, not membership in a cone), whose first instance
writes ℓ_T at T ∈ (½ log 4, ½ log 5) as a square compensated by a named term, with the line that
breaks at c = 2 and on deleting 4.

## 5. List of claims

- Lemma 1 (cone predicate with uniform step ⟺ increments in the cone; chain = split): PROVED.
- Lemma 2 (bounded inertia with uniform step requires increment ⪰ 0): PROVED in finite dimension; ARGUED at
  form level.
- Classification of the six directions into closed entries (§2): ARGUED (primary-source cross-check of the
  cited antecedents; not exhaustive).
- §2.1, the coupled predicate with margin needs a bound of c_{h*}(log n): ARGUED (reduction to BARRIER_W_001 §6).
- Window in c of width ≲ 10⁻³ and bottom 10⁻⁸–10⁻⁹: NUMERICAL (cited from ROUND_006 §10.3); consequence
  «no open slack in the weight»: ARGUED.
- Coincidence of the DIR threshold with the entry of n = 4: NUMERICAL (threshold) + arithmetic; reading «stages
  by prime powers»: ARGUED.
- Existence of a stage predicate with its own formula: OPEN.
