# R184_004 — Conjecture C_B (m<∞ ⟹ m=0) with the inertia machinery of phase 183 — **NO-GO (PROVED): the inertia count, including the prime-by-prime Schur chain, is blind to the class; M_m satisfies all of it. Gap (b) does not narrow.**

* Cell 8F/4E/7E (grid, item 1 of the ranking). Sources read: R162_2501 (§§1–7), R162_2601 (Thm Λ̃, Thm H),
R162_2602 (Def 5, Thm 6), R183_018 §§3–4, R183_031 §1 + editor's note R183_032 §3, MAP_1 (rows L8, LP-112), grid part2/part6.
Walls named in advance: W3 (class blindness), E1, W-identification. Pure mathematics, no numerics. No label moves.*

Conventions (R162_2501). I_T = [−T,T]; for real F in P_T (primitives, Φ_F(0)=Φ_F(1)=0),
Φ_F(s) = ∫F(t)e^{(s−½)t}dt, W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ). n₋(Q) = maximum dimension of a subspace of C_c^∞(I_T)∩P_T
where Q<0 (algebraic invariant; R183_032 §3 asks for restriction to C_c^∞, which is done here). m = number of quartets
{½±β_j±iγ_j}, 0<β_j<½, off the line, with multiplicity.

## 0. Corpus check

grep "C_B", "LP-112", "L8", "n₋", "Schur", "finite index" in phase-136, phase-162 (grid), phase-183. Found: R162_2501
(first-contact NO-GO, Prop 1–3, gap §5), R162_2601 (atomic-vs-exponential NO-GO via Λ̃; Thm H), R162_2602 Thm 6
(N(T) ↑ 2κ_off), R183_031 Lemma 1.1. **No file compares the prime-by-prime Schur chain (R183_018 §4) with M_m.**
§§3–4 are new; §§1–2 rewrite what is known in inertia language with one exact detail (signature per quartet).

## 1. Gap (b) and C_B in inertia language

**1.1 Gap (b), exactly (R162_2501 §5).** (1) RH ⟺ C_B ∧ (κ<∞). (2) κ<∞ (Diana L8) is much stronger than
any theorem: it implies Θ<1 and A ⟹ LH; so C_B leaves a gap of at least quasi-RH ∧ Lindelöf strength. (3) In
λ_A language: under κ<∞, e = 2β*; open whether e<1 ⟹ Θ<1 (O2501.2). (4) LP-112 dissolves under finiteness. (5) The
non-equivalence C_B ≢ RH is NOT-REFUTED, not proved. The live residue of C_B itself is O2501.1, and R162_2601 closed it in its
"atomic vs. exponential" form (NO-GO via Λ̃). What remains: a property that distinguishes ζ within the class fixed
by Thm H.

**1.2 Lemma 1 (exact signature of a quartet, PROVED).** Let z = β+iγ, β>0, and A(F) := Φ_F(½+z) (a complex linear
functional). The contribution of the quartet to W_T is q(F) = 4 Re(A(F)·B(F)), B(F) := Φ_F(½−z). Writing F = F_e + F_o
(even/odd), Φ_{F}(½−z) = A(F_e) − A(F_o), so that

    q(F) = 4 Re(A(F_e)²) − 4 Re(A(F_o)²),

with no cross terms between parities. Re(w²) = (Re w)² − (Im w)² has signature (1,1) in (Re w, Im w). Hence,
if Re A, Im A are linearly independent over each parity of P_T (true for T>0: e^{zt} and e^{z̄t} are
independent on any interval, and the two primitive conditions have codimension 2, which does not make them
dependent except on a discrete set of cases avoided by choosing T outside it), **q has exact signature (2,2):
one even negative direction and one odd direction.** With multiplicity r, the block has rank ≤ 4r and n₋ ≤ 2r.
*Proof.* Φ_{F(−·)}(½+z) = Φ_F(½−z) gives B(F_e)=A(F_e), B(F_o)=−A(F_o); expand. □
(Corrects the "(1,1) per pair {ρ,1−ρ̄}" of R183_032 §3: per conjugate pair there is one negative direction; per quartet, two.)

**1.3 Proposition 2 (C_B in inertia).** Let N(T) := n₋(W_T|C_c^∞(I_T)∩P_T).
(i) (PROVED) N is non-decreasing in T (nested windows).
(ii) (PROVED) If m<∞: N(T) ≤ 2m ∀T. *Proof:* W_T = Z_on + Q_off with Z_on ≥ 0 and Q_off a sum of m blocks from Lemma 1,
n₋(Q_off) ≤ 2m; n₋(Z_on+Q_off) ≤ n₋(Q_off). □
(iii) (CITED R162_2602 Thm 6, proved there with R162_2501a) If m<∞: N(T) = 2m for T ≥ T_m. Mechanism: 2m Gabor
packets at the endpoints of I_T (even/odd per quartet, with φ̂ vanishing at the other points of the same β, as in R162_2501
Prop 1); Q_off ≍ −e^{2β_jT} there, Z_on = O(1), and the matrix is block diagonally dominant.
(iv) (CITED, exact statement not verified in the source: Weil 1952 / Yoshida 1992; R183_031 Lemma 1.1(b)) sup_T N(T) < ∞
⟹ m < ∞.

With (ii)–(iv): **m<∞ ⟺ sup_T N(T)<∞, and then sup N = 2m.** Thus

    C_B ⟺ [ sup_T N(T) < ∞ ⟹ N ≡ 0 ],    RH ⟺ N ≡ 0.

(The "⟺" of the first line is CONDITIONAL on (iv) in the ⟸ direction of m<∞; the direction used below, m<∞ ⟹ N bounded,
is PROVED.)

## 2. The prime-by-prime Schur chain (what the objective asks to derive)

**2.1 Setup (R183_018 §3, PROVED from CITED).** For fixed T, W_T = A_{∞,T} − C_ε − Σ_{p<e^{2T}} B_p, with C_ε
Hilbert–Schmidt, and B_p ≅ ∫^⊕ T_{n(r)}(σ_p) dr, σ_p(θ) = 2 log p Σ_{k≥1} p^{−k/2} cos kθ (mean zero), non-compact,
with directions of both signs (R183_018 Prop 4.1). Order the primes p_1<p_2<…<p_K<e^{2T} and let
W^{(k)}_T := A_{∞,T} − C_ε − Σ_{i≤k} B_{p_i}, so that W^{(K)}_T = W_T.

**2.2 Lemma 3 (exact per-step inertia condition, PROVED; standard linear algebra).** On any finite-dimensional
subspace V ⊂ C_c^∞(I_T)∩P_T, let V = V_+ ⊕ V_− be a W^{(k−1)}-orthogonal decomposition with W^{(k−1)} > 0 on V_+
(assume nondegenerate; the degenerate case is handled by perturbing V). Then, by Haynsworth additivity,

    n₋(W^{(k)}|V) = n₋( (W^{(k)}|V_+) ) + n₋( W^{(k)}/V_+ ),

with W^{(k)}/V_+ the Schur complement over V_−. That total inertia does not grow when p_k is added means exactly:
(a) B_{p_k} is absorbed in V_+: W^{(k−1)} − B_{p_k} > 0 on V_+ except for d_k directions, and (b) the Schur complement
over V_− loses at most the corresponding d_k directions. Taking the sup over V gives the version in
C_c^∞: n₋(W^{(k)}) − n₋(W^{(k−1)}) ∈ [−n₊-rank…, +n₋(−B_{p_k}) ], a useless bound because B_p has infinite rank; the
informative condition is Haynsworth's, applied to each V.
The form requested in the objective is: "N(T) = 2m ∀T ≥ T_m" is equivalent to, at each step k and in each V, the new
negative part of −B_{p_k} (vectors at frequencies s ≈ (2j+1)π/log p_k, R183_018 §4) being absorbed by the positive part of
W^{(k−1)}, except for a net balance of 2m at the last step.

**2.3 Theorem 4 (class blindness of the chain, PROVED).** Let M_m be the model of R162_2501 §1:
ξ_m = ξ · Π_j(quartet j) / Π_{k≤m}(s−½∓iγ^0_k), heights > H_PT. Then, for every T:
(a) Its Weil form is W^{M}_T = W_T + Δ_T with Δ_T(F) = Σ_j q_j(F) − Σ_{k≤m} 2|Φ_F(½+iγ^0_k)|²: rank ≤ 4m + 2m = 6m,
continuous in T, and Δ_T is an explicit form in the zero variable, **not** in the prime variable.
(b) In the decomposition of 2.1, M_m has **the same** A_{∞,T} and the same B_p for every p (the arithmetic side of
ζ_m'/ζ_m differs from that of ζ'/ζ only by an absolutely continuous density E_m, R162_2501 Thm 3); Δ_T is placed in the
compact term: C_ε ↦ C_ε − Δ_T, which remains Hilbert–Schmidt (finite rank).
(c) For every k ≤ K and every V: |n₋(W^{M,(k)}_T|V) − n₋(W^{(k)}_T|V)| ≤ 6m (Weyl interlacing for finite-rank
perturbations). Likewise for each Schur complement of Lemma 3 (rank of the change ≤ 6m).
(d) Under RH: N^ζ ≡ 0 and N^{M}(T) = 2m for T ≥ T_m (Prop 2(iii) applied to M_m, whose off-line zeros are exactly the m
quartets). In particular M_m satisfies "sup_T N < ∞" with N ≢ 0.
*Proof.* (a) Weil/explicit formula for ξ_m: the added zeros give q_j (Lemma 1), the removed ones give −2|Φ_F(½+iγ^0_k)|²
(rank 2 each). (b) ξ_m'/ξ_m = ξ'/ξ + R', R rational; in the variable u = log x the contribution of R' is the density
E_m (finite combination of e^{(ρ−½)u}), absolutely continuous: it does not touch the atoms at log p^k, hence does not touch σ_p.
(c) Weyl/Cauchy: a rank-r perturbation changes n₋ by ≤ r, in each V and in each Schur complement. (d) Prop 2. □

**Corollary 5 (inertia NO-GO, PROVED).** Let 𝒜 be an argument that, from (i) the decomposition in 2.1 with the
operator properties of its pieces (archimedean A_∞, B_p a fiberwise Toeplitz operator with mean-zero, non-compact
symbol σ_p, remaining term compact and continuous in T), (ii) inertia arithmetic (Sylvester, Haynsworth, interlacing,
monotonicity in T, Prop 2), and (iii) any property of the B_p — in particular Λ(p^k) = log p exactly, integrality
of the support {log n}, multiplicativity encoded in σ_p — deduces "N bounded ⟹ N ≡ 0." Then 𝒜 applies verbatim
to M_m (Thm 4(b): same pieces except the compact one) and concludes N^{M} ≡ 0, contradicting Thm 4(d) under RH. Hence 𝒜
proves ¬RH (or is incorrect). If ζ has κ=∞, M_m does too and the argument is vacuous in both cases: no contradiction, but
also no useful C_B. **No property of the Euler product entering through the B_p can help; the prime-by-prime Schur
chain does not see the difference between ζ and M_m.** (Killer: W3, now in the prime variable.)

**2.4 What property, exactly, separates them.** By Thm 4(b), ζ and M_m agree on everything the chain uses except **the
identity of the compact term**: for ζ the remainder is exactly −C_ε (fixed by Γ), for M_m it is −C_ε + Δ_T. That is,
what separates them is the *rigidity of the pair (primes, Γ)*: that the full datum be atoms Λ(n) at log n + the Γ term,
with no extra absolutely continuous part. Comparison with the falsifiers:
* M_m: B_p identical, rigidity fails (a.c. part E_m). Separated only by rigidity.
* Λ̃ (R162_2601 §3): positive atomic datum on {±log n}, but with weights Λ̃(n) ≠ Λ(n) and **not** the log-derivative. Its "B_p"
  are not those of ζ (weights on all n, not only prime powers) — here the chain *does* distinguish, but by the weights, and
  Λ̃ is not a counterexample to C_B within the class of log-derivatives. Λ̃ only kills "atomicity + positivity."
* DH: m=∞, vacuous.
Rigidity is exactly the content of Thm H (R162_2601): atoms + log-derivative + EF ⟹ F = cζ. Hence
**a proof of C_B must use that the archimedean/compact term does not admit a finite-rank exponential perturbation
given the fixed prime part** — which is R162_2501 Prop 3 ("no finite exponential off-line density can be
added to the Λ comb while keeping a real zero measure"), i.e. E1 by configuration. The inertia language does not
add content to that reformulation: gap (b) does not narrow.

**2.5 Remark (why the idea "2m fixed directions ∀T" gives no contradiction).** In M_m under RH this literally
happens: the 2m negative directions are the Gabor packets at the endpoints (Prop 2(iii)), and each new prime
p < e^{2T} is absorbed by the positive part at each step (Thm 4(c) with N^ζ ≡ 0 ⟹ ζ's absorption is complete,
and M_m inherits the same absorption up to ≤ 6m). The negative directions of −B_p (frequencies ≈(2j+1)π/log p) live
inside the frequency band and are absorbed by A_∞ equally in both models. There is no structural incompatibility
between "fixed index 2m" and "non-compact, mean-zero Toeplitz operator per prime."

## 3. LP-112 and L8 (one paragraph each)

**L8 (Diana, phase-37/111; MAP_1 l.100).** Unconditional bound m ≤ C. It stalled because every known zero-density
mechanism is binary (0 or T^θ), never a finite nonzero count; marked "UNREACHABLE with catalogued techniques,"
not proved impossible. The tools of 183 change nothing: Prop 2(ii)–(iv) says L8 ⟺ sup N(T) < ∞, and R183_031
Thm 1 *assumes* finite index (Lemma 1.1) instead of proving it; moreover R162_2501 Prop 2 only gives −λ_A ≲ e^{T}, which is
compatible with N(T) → ∞ (N(T) ~ #quartets with large β). A bound on N(T) uniform in T is κ<∞, forcing quasi-RH.

**LP-112 (phase-37/112–113; audit 38/115).** Sequential self-approximation of ζ in a disk ⟹ m ∈ {0,∞}. It stalled: no
precedent in the literature, its non-equivalence to RH only asserted, and in the grid it was marked DEAD twice: Thm 181.1
(0<I<∞ ⟹ ¬LP-112; part2) and F3 (adapted Hadamard counter-model without arithmetic; "LP-112 is the dichotomy renamed";
part6); P33: conditionally on A, LP-112 ⟺ RH. The tools of 183 do not revive it: self-approximation is a
property of ζ as a function (universality/Bagchi), not of the inertia of W_T; and Thm 4 shows that any inertia
reading of LP-112 would also be true for M_m.

## 4. Verdict

**NO-GO (PROVED), Corollary 5:** the inertia of W_T, its monotonicity, the prime-by-prime Schur chain and every property of
the blocks B_p (including Λ(p^k)=log p) are shared by M_m up to a rank ≤ 6m perturbation in the
compact term; under RH M_m has N ≡ 2m bounded and nonzero. Any proof of C_B by inertia alone would prove ¬RH. New PROVED:
Lemma 1 (exact signature (2,2) per quartet, separated by parity), Prop 2(i)(ii), Lemma 3 (Haynsworth form of the
per-prime condition), Thm 4. What separates ζ from M_m is the rigidity of the archimedean remainder given the prime part (Thm H),
which is equivalent to R162_2501 Prop 3 (E1 by configuration). Gap (b): **unchanged**. No lemma "C_B ⟸ an inequality in
the Schur complement of the prime 2" survives: any inequality on the B_p is also satisfied by M_m (Thm 4(b),(c)).

## State

| statement | label |
|---|---|
| Lemma 1: quartet = signature (2,2), one even negative + one odd | PROVED (except for T in a discrete set, see audit) |
| Prop 2(i)(ii): N monotone, N ≤ 2m under m<∞ | PROVED |
| Prop 2(iii): N = 2m for large T | CITED (R162_2602 Thm 6) |
| Prop 2(iv): N bounded ⟹ m<∞ | CITED, Yoshida statement not verified (as in R183_032) |
| Lemma 3 (per-prime Haynsworth) | PROVED (standard) |
| Thm 4 (chain of M_m = chain of ζ + rank ≤ 6m) | PROVED |
| Cor 5 (inertia NO-GO for C_B) | PROVED |
| C_B | OPEN |
| gap (b) / O2501.1 | OPEN, not narrowed |
| L8, LP-112 | unchanged (OPEN / DEAD) |
| Row D | OPEN; no label moves |

## For the audit

1. **Lemma 1, independence.** The exact signature (2,2) needs Re A, Im A independent on each parity of
   C_c^∞(I_T)∩P_T. In C_c^∞(I_T) without restriction this is clear (cos γt·e^{βt} vs sin γt·e^{βt} restricted to even/odd
   functions). With the two primitive conditions (one per parity) there could be collapse for isolated T; the
   NO-GO does not depend on this (it only uses n₋ ≤ 2 per quartet and Prop 2(iii)).
2. **Thm 4(b): "same B_p."** Verify that the part of ξ_m'/ξ_m coming from R' enters the decomposition of
   R183_018 §3 as a finite-rank term and does not mix with the σ_p. This holds because the decomposition is made on
   the arithmetic-side datum (atoms at log p^k + Γ), and R' contributes in the zero variable via the explicit
   formula; equivalently, Δ_T is defined as the difference of the two Weil forms on the zero side, which is
   exactly rank ≤ 6m. There is no need to interpret Δ_T as a prime density.
3. **Under ¬RH.** If ζ has m_0 ∈ (0,∞) quartets, M_m has m_0+m and both violate C_B; the NO-GO still holds: the
   argument would conclude N^{M} ≡ 0 and N^{ζ} ≡ 0 simultaneously, and for M_m this is false by Prop 2(iii). If m_0 = ∞ the
   NO-GO is vacuous (as in R162_2501 Thm 3). Honest formulation: "any proof of C_B by inertia + prime blocks implies ¬RH or is vacuous."
4. **Is M_m legitimate as a model for the chain?** M_m is not a Dirichlet series (R162_2601 Thm H). Cor 5 only
   requires that 𝒜 use ζ through the pieces (A_∞, B_p, compact) and inertia; if 𝒜 also uses that the compact part is
   *exactly* C_ε, then it is using the rigidity of §2.4 — that is no longer "inertia alone" and falls under R162_2501 Prop 3 / E1.
5. **Lemma 3** is finite-dimensional linear algebra; the passage to C_c^∞ by sup over V is valid for n₋ (Sylvester),
   not for bounds on the increments, which are not used.
6. **It is not claimed** that RH, or the closure of D, or of C_B holds; the correction "(1,1) per pair" of R183_032 §3 is minor and does not affect
   its conclusions.

## Note (R184_091)

* Cor 5 holds only for the class 𝒜 as defined (without quantitative properties of the compact term; in M_m it has norm ~e^{2βT}). The headline "inertia is blind to the class" overstates it. Strengthening: 𝒜 valid ⟹ κ(ζ)=∞, not just ¬RH.
* "Corrects the (1,1) of R183_032" is false: a quartet = two pairs, (2,2) agrees. Lemma 1 holds for all T>0.
