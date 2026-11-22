# Round 7, memo A: the square of the deficit, the ground-state representation of the contacts, and the optimality conditions of the split

Notation: I = (−T, T), u_p = log p, v_p = 2 log p/√p, S_u F(t) = F(t − u) truncated to I, Π_p(F) = Σ_{n=p^k} v_n c_F(log n)
(for p = 2 it includes n = 4), ε_F(u) = ½‖F − F_u‖². DIR split (`ROUND_006` §§2, 7–10):
q_p(F) = ∫W_pF² + ¼∬θ_p(t,s)K(|t−s|)(F(t)−F(s))² − Π_p(F), θ_p ≥ 0, Σθ_p = 1, ΣW_p = W.

## 0. Four-point filter

**(1) Antecedents read in primary sources.**
- `phase-212-missing-object/REVIEW_006.md` A1–A4 and D (reopening condition); `ROUND_006_WINDOW_SPLIT_NUMERIC.md`
  §§5, 7–10 (discrete duality, obstructing pair, minimal transfer X = λℓ⊗ℓ).
- `phase-211-sign-sandbox/ROUND_005_D.md` §2 Thm. 2.1 (ground-state representation with the comb as an atomic jump
  measure, relative to the ground state h_T **of the full form**) and Thm. 6.1 (NO-GO of the class 𝒦_gap:
  gap bounds with intrinsic loss). LEDGER 211 C17.
- `phase-195-modern-tools/INV_N_001_BAKRY_EMERY_GAMMA2_GAP_CEILING_NO_GO.md` §1: −v c_F(u) = ½v∫(F − F_u)² − v‖F‖²,
  i.e. the case φ ≡ 1 of the identity of §1 of this memo.
- P46 cor:Tarch (cited in `ANNEX_COTEJO_NULLDIR.md` §2.1; PROVED with intervals): 0.58 ≤ T*_{∞,P} ≤ 0.60, the bottom of
  Arch on P_T is < 0 for all T ≥ 0.60. P46 thm:index: n₋(Arch|P_T) = 0, 1, 2 on (0,T*_ev), (T*_ev,T*_odd),
  (T*_odd, 0.90], log 2 ≤ T*_odd ≤ 0.81. `R155_029` l.27: «above T*_{∞,P} the primes are necessary».
- `phase-159-row-d-two-front-construction/G2_B8_R5.md` Def. 1 and Theorem D step 4 (via `REVIEW_006` A1; all-or-nothing
  complementary slackness).
- Phases 202 and 205 (exterior plank, Toeplitz−Hankel of the tail): cross-checked by grep for «estado fundamental», «ground
  state», «gauge», «Schur»; they contain no per-prime bound of the contact by a potential. No value as proof of
  absence.

**(2) What is new.** There is no object with a sign. What the memo asserts and is not in the corpus:
(a) an impossibility proof for the class 𝒢 of certificates that bound each contact Π_p by a potential
V_p ≥ 0 (gauge, Schur test, per-prime ground state with positional φ_p, chains of any length,
combined with any θ_p(t,s) and W_p(t)); the class dies at T*_{∞,P} ≤ 0.60, before log 2;
(b) the continuous dual of the DIR split and of the minimal transfer, and the equation satisfied by ℓ;
(c) the reading of ℓ as a direction «periodic with period log 2 along the chains» (ARGUED).

**(3) Why it avoids the difficulty of the antecedent.** It does not: the working hypothesis falls under (a). The difference
with 211 ROUND_005_D (global ground state h_T, comb included, and class 𝒦_gap on the second eigenvalue) is real
—here φ_p is per prime and the bound is on the bottom of each q_p—, but result (a) shows that this difference does not
create a sign: the mechanism is lost by an already proved archimedean fact, not by the geometry of the chains.

**(4) Link with global positivity.** No positive one. (a) is a class closure; (b) gives the equation that any
closed formula for ℓ, θ_p, W_p would have to satisfy, i.e. the check a future candidate must pass.
By the filter rule all construction of a formula for ℓ inside 𝒢 was stopped; the rest of the effort went
to (b) and (c).

## 1. The per-prime ground-state identity (PROVED, elementary)

**Lemma 1.1.** Let u > 0, v > 0, φ > 0 measurable on I, F ∈ L²(I) real. Let J_u = {t ∈ I : t + u ∈ I}. Then

v∫_{J_u} F(t)F(t+u)dt = ∫_I V F² − (v/2)∫_{J_u} φ(t)φ(t+u)(F(t)/φ(t) − F(t+u)/φ(t+u))² dt,

V(t) = (v/2)[𝟙_{J_u}(t)φ(t+u) + 𝟙_{J_u}(t−u)φ(t−u)]/φ(t).

*Proof.* Expand the square: (v/2)∫_{J_u}[φ(t+u)F(t)²/φ(t) + φ(t)F(t+u)²/φ(t+u)] − v∫_{J_u}F(t)F(t+u); in the
first summand change t + u → t. □

For n = p^k one sums over u = k u_p with its own φ_{p,k} (or a common φ). With φ ≡ 1 one recovers INV_N_001 §1. For
T < u_p, J_u and J_u + u are disjoint (the pairs form a matching) and α(t) = φ(t+u)/φ(t) is the free gauge
of the working hypothesis; for T > u_p there are chains t − u, t, t + u and V(t) sums two neighbours. **The identity holds equally in both
regimes; the matching/chain distinction does not change the type of bound** (in both cases it is the Schur inequality
Π_p ≤ ∫V_pF², exact at F ∝ φ along the chains).

## 2. NO-GO of the class 𝒢 (PROVED relative to P46 cor:Tarch, CITED)

**Class 𝒢.** Certificates of a_T ⪰ 0 on P_T of the form: for each prime p, a bound Π_p(F) ≤ ∫V_pF² on P_T
with V_p ≥ 0 a.e. (in particular the one of Lemma 1.1 discarding the square, with arbitrary, positional φ_p, with chains
of any length, for any number of primes), and positivity of the remainder
R_p := ∫W_pF² + ¼∬θ_pK(F(t)−F(s))² − ∫V_pF² ⪰ 0 on P_T, with θ_p ≥ 0, Σθ_p = 1, ΣW_p = W free (also θ_p with
two positions, also optimized jointly with the φ_p). One also admits any fraction κ_p ∈ [0,1) of the
square of Lemma 1.1 discarded (the remainder with retained fraction is the class with v_p replaced by κ_pv_p plus a
term ⪰ 0 added to R_p, and the argument applies equally because it only uses V_p ≥ 0).

**Theorem 2.1.** For all T ≥ 0.60 no certificate of 𝒢 exists. For T ∈ (T*_{∞,P}, 0.60) neither.

*Proof.* Σ_p R_p = Arch − ∫(Σ_pV_p)F² ⪯ Arch on P_T because ΣV_p ≥ 0. If each R_p ⪰ 0, Arch ⪰ 0 on P_T.
By cor:Tarch the bottom of Arch on P_T is < 0 for T > T*_{∞,P}, and T*_{∞,P} ≤ 0.60. □

**Corollary 2.2.** The ground-state representation of the contacts (the working hypothesis) does not explain the
DIR threshold at 0.695–0.70: the class that uses that representation as a bound dies at T*_{∞,P} ∈ [0.58, 0.60],
below log 2 = 0.6931, and in the same way in the matching regime as in the chain regime. Past T*_{∞,P} the
contacts must contribute **positively** (−Π(e) > 0 in the bottom direction e of Arch, since a_T(e) ≥ 0 >
Arch(e)); every upper bound of Π_p by a nonnegative potential throws away exactly that contribution. This is the
per-prime form of the sentence «above T*_{∞,P} the primes are necessary» of R155_029; the theorem is its
immediate consequence and has no more content than that.

What 𝒢 does not cover: bounds Π_p ⪯ M_{V_p} on P_T with sign-changing V_p (possible because of the Tate restriction, since
Π_p is indefinite), and certificates that keep the square of Lemma 1.1 with full weight (then the lemma is an
exact rewriting of q_p and contributes no mechanism: q_p ⪰ 0 is again the problem). OPEN, no object.

**Answer to (ii).** The identity is in the corpus for φ ≡ 1 (INV_N_001 §1) and for φ = h_T global (211 ROUND_005_D
Thm. 2.1). Neither of the two recorded NO-GOs (𝒦_gap: second eigenvalue with loss; INV_N_001: curvature
ceiling) literally covers the per-prime variant with positional φ_p and joint DIR split; that variant is now
covered by Theorem 2.1, for a different reason (archimedean index, not gap loss).

## 3. Optimality conditions of the split in the continuum

**3.1 Dual of the DIR split (ARGUED in the continuum; PROVED in each Galerkin discretization by SDP duality with
Slater, which holds: θ_p = ½, W_p = W/2, τ very negative is strictly feasible).** Primal:
τ* = sup{τ : q_p − τ ⪰ 0 on P_T, p = 2, 3}. Lagrangian with Y_p ⪰ 0 (trace-class kernels on P_T):
τ + Σ_p tr(Y_p(q_p − τ)). Maximizing in τ gives Σ tr Y_p = 1; in W_p with ΣW_p = W it gives diag Y_2 = diag Y_3 =: ρ (otherwise
+∞); in θ_2 ∈ [0,1] (θ_3 = 1 − θ_2), with E_Y(t,s) = ¼K(|t−s|)(ρ(t)+ρ(s)−2Y(t,s)), it gives max(E_{Y_2}, E_{Y_3}). Hence

τ* = inf { ∫Wρ + ¼∬K(|t−s|)[ρ(t)+ρ(s) − 2 min(Y_2(t,s), Y_3(t,s))] − tr(Y_2Π_2) − tr(Y_3Π_3) :
           Y_p ⪰ 0 on P_T, diag Y_2 = diag Y_3 = ρ, ∫ρ = ½ }.

With Y_2 = Y_3 = Y the functional is tr(Y a_T); the deficit of the split relative to the ceiling is exactly what is gained
by separating the two states while keeping a common density: the kernel energy is charged with min(Y_2,Y_3) instead of with
Y. This reproduces the formula verified in `ROUND_006` §9.1.

**Complementary slackness.** (K1) Y_p(q_p − τ*) = 0: the range of Y_p lies in the bottom eigenspace of q_p.
(K2) θ_2(t,s) = 1 where Y_3(t,s) > Y_2(t,s), = 0 where Y_3 < Y_2 (all-or-nothing, `G2_B8_R5` Thm. D step 4, now with
two positions). (K3) W_p free only where ρ = 0; where ρ > 0 the split of W is undetermined by the dual and is fixed by
(K1).

**3.2 Minimal transfer (`ROUND_006` §10.2).** Primal: min ‖X‖_* with q_2 + X ⪰ 0, q_3 − X ⪰ 0 (θ, W in DIR).
Dual: Y_2, Y_3 ⪰ 0 with the same density and θ conditions, and Y_3 − Y_2 ∈ ∂‖X‖_*. If X = λℓ⊗ℓ, ‖ℓ‖ = 1,
λ > 0, then

(E_ℓ)  (Y_3 − Y_2)ℓ = ℓ,  ‖Y_3 − Y_2‖_op ≤ 1,  (q_2 + λℓ⊗ℓ)Y_2 = 0,  (q_3 − λℓ⊗ℓ)Y_3 = 0,

and by (K1) ℓ is the negative-eigenvalue direction of q_2 at the optimum (the data: overlap 0.92–0.95).
**Equation for ℓ:** eigenvector of eigenvalue 1 (the maximum) of Y_3 − Y_2, with Y_p the obstructing pair; equivalently
ℓ ∝ (q_3 − λℓ⊗ℓ)-kernel ∩ negative direction of q_2. It is a fixed-point problem coupled to the obstructing pair; it gives no
formula without solving it (ARGUED; no existence proof in the continuum).

## 4. Reading of ℓ (ARGUED, no proof)

By Lemma 1.1 with φ ≡ 1, the contact of 2 is maximal relative to ‖F‖² on the F with F(t) = F(t + log 2) along
the chains, and on them the kernel energy at distance log 2 vanishes. For T < log 2 that condition only
pairs points and leaves half the window free; for T > log 2 it binds triples and forces periodicity in the central
zone (−T + log 2, T − log 2): the projection of cos(2πt/log 2) onto P_T is the natural representative, and it agrees
with the observed overlap 0.91–0.93. This is consistent with (K2) (2 yields the kernel in the log 2 band) but
**does not explain the threshold**: the central zone has length 2(T − log 2), which is 0.013 at T = 0.70, and the n = 4 term
switches on at the same T = log 2 (S_2² ≠ 0 ⟺ 2T > log 4), whereas deleting it does not change the failure (`ROUND_006` §7.3).
Concrete open question: whether the DIR threshold coincides with T*_odd (P46 thm:index, log 2 ≤ T*_odd ≤ 0.81, second
negative direction of Arch); ℓ is even, so the coincidence, if it exists, is not direct. OPEN.

## 5. Answer to (iv)

No closed formula for ℓ, θ_p, W_p is produced. What is proved is the impossibility in the class 𝒢 (Theorem 2.1),
for any number of primes (the argument only uses ΣV_p ≥ 0), so the three-prime statement of the
class is the same NO-GO. Falsifier checks: they do not apply to a NO-GO; note that Theorem 2.1 does not depend
on the weight (it holds for cΛ, for the comb without one power and for Beurling-type weights), which confirms that 𝒢 cannot
distinguish c = 1 and that, by `ROUND_006` §10.3 (positivity window in c of width ≲ 10⁻³ at T = 0.70),
any surviving formula must fall outside 𝒢 and depend on the weight with that precision.

Condition for reopening point (iv): a bound Π_p ⪯ M_{V_p} on P_T with sign-changing V_p, written from
the Tate restriction and the exact values v_2, v_3, satisfying (K1)–(K2) and (E_ℓ) at T = 0.70. None is proposed.

## 6. List of claims

| # | Claim | Label |
|---|---|---|
| 1 | Lemma 1.1, per-prime ground-state identity, with truncation | PROVED |
| 2 | The gauge of the matching regime and the chain ground state are the same Schur bound | PROVED (by 1) |
| 3 | P46 cor:Tarch: bottom of Arch on P_T < 0 for T > T*_{∞,P}, T*_{∞,P} ∈ [0.58, 0.60] | CITED |
| 4 | Theorem 2.1: the class 𝒢 (contacts bounded by potentials ≥ 0, positional φ_p, chains, θ_p(t,s), W_p(t), any number of primes) does not certify for T > T*_{∞,P} | PROVED relative to 3 |
| 5 | Corollary 2.2: the working hypothesis does not explain the threshold 0.695–0.70 | PROVED relative to 3 |
| 6 | Coverage of the previous NO-GOs (𝒦_gap, INV_N_001) of the per-prime variant: not literal | ARGUED (reading) |
| 7 | Continuous dual of the DIR split with min(Y_2, Y_3) and common density | PROVED in Galerkin; ARGUED in the continuum |
| 8 | Complementary slackness (K1)–(K3) | PROVED in Galerkin; ARGUED in the continuum |
| 9 | Equation (E_ℓ) for ℓ | PROVED in Galerkin under rank one of X; ARGUED in the continuum |
| 10 | ℓ ≈ periodic direction of period log 2 on chains | ARGUED |
| 11 | Relation of the DIR threshold with T*_odd | OPEN |
| 12 | Class of bounds with sign-changing V_p on P_T | OPEN, no object |
| 13 | Data of ROUND_006 used (threshold, ℓ, window in c) | NUMERICAL (not recomputed) |
| 14 | Global sign | OPEN |
