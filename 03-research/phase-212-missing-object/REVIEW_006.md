# Review of the selection gate after round 6 (rule-based splitting: distance bands and per-prime potentials)

Memo reviewed: `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §§1–9 and the proposal coming out of §9.4: prove that "to
bound from below the term of a prime p, the kernel at the distance of its own contact contributes nothing",
use it to write a rule-based splitting (each distance for the prime that has no contact there, plus
free potentials W_p(t)), compute its deficit by hand and then look for a signed correction.

**Verdict: REJECTED at the gate.** The proposed object is class M of the memo itself, whose kernel
part is exactly that of `G2_B8_R5` Def. 1; the "band rule" is the complementary slackness of Theorem D
of that antecedent and can already be read off its printed numbers; the lemma, in its literal statement, is false; there is no
sign mechanism (format affine in the weight, rule independent of the weight, signed correction without an object).
Global sign OPEN. Nothing that follows carries a sign.

Notation: I = I_T = (−T, T), u_p = log p, ε_F(u) = ‖F‖² − c_F(u) = ½‖F − F_u‖², v_p = 2 log p/√p.

## A. Antecedents

A1. **`phase-159-row-d-two-front-construction/G2_B8_R5.md`, Def. 1, Lemma 2.1, Theorem D, Theorem L″, §5.**
Read in full in the primary source.
- Def. 1: splitting (C_p, K_p) with C_p **constants** (ΣC_p = C_0) and K_p = θ_p(u)K(u), θ_p measurable, a function
  **of the distance only**, θ_p ≥ 0, Σθ_p = 1. Local form q_p = C_p‖F‖² + ∫ε_F K_p + Q_p. It admits any
  measurable θ_p(u): the all-or-nothing splittings by distance bands are inside the class.
- Theorem D, step 4 of the proof: the maximum over θ against a family of states is attained at
  θ_p(u) = 𝟙{p realizes max_q ε_{σ_q}(u)}. That is, **the optimal splitting is all-or-nothing by distance, and the
  distance u goes to the prime whose state has the largest deficit ε_{σ_p}(u)**, which is the prime whose state has
  the smallest autocorrelation at u. A prime whose state maximizes c(u_p) loses the distance u_p. This is the
  content of the table in §9.3 and of the sentence "each prime gives up the kernel at the distances of its own
  contacts".
- The numbers already printed there (§4, "Independent checks") give the same assignment: c_{F_2}(log 2) = 0.3688,
  c_{F_3}(log 2) = 0.3029, hence ε_{F_2}(log 2) = 0.631 < ε_{F_3}(log 2) = 0.697 and the distance log 2 goes to the
  prime 3; c_{F_2}(log 3) = −0.0355, c_{F_3}(log 3) = 0.0010, hence ε_{F_2}(log 3) = 1.036 > ε_{F_3}(log 3)
  = 0.999 and the distance log 3 goes to the prime 2. The "rule" of §9.3 is in the test pair of L″.
- §5 gives the reading of the failure: the sign on (T_loc, log 2] is carried by the interference between c_F(log 2) and
  c_F(log 3) within a single autocorrelation; a splitting by factors pays the maximum of the deficits.
- **Exact scope of D and L″ with respect to the proposal.** They cover θ by distance bands with constant C_p.
  **They do not cover** position-dependent W_p(t): with free W_p the dual changes (the states must have
  equal pointwise density; the pair of L″ has different densities and is not admissible), as
  `ROUND_006` §5 itself says. Nor do they cover θ(t, s) (class DIR). L″ does not exclude, as written, class M.
- Status of the antecedent: L″ is "machine-verified", without interval arithmetic, and appears unaudited in
  IDX `04_PHASES_100-189.md` rows G4A-159 (l.414), G8A-159 (l.427), G4A-R160_S5 (l.533, "DEAD [T ≥ 0.5925
  uncertified]"), G4C-R160_S5 (l.544, "joint cross-prime constraint", OPEN-RESIDUE); GRID l.239, 517, 708;
  `R159_099_SYNTHESIS.md` l.157.

A2. **`G2_B8_R4.md` §1 (l.104–110).** Without the restriction θ_p ≥ 0 (pieces that are not of Lévy type) the splitting is
empty: everything is given to one piece and existence is the target. Direct antecedent of "then look for a
signed correction".

A3. **`ROUND_005_G1.md` §3 (block "Euler factors…") and `ROUND_005_G5.md` L2 and "Next concrete
step"; `REVIEW_005.md`, "What the round leaves unexcluded", point 1; LEDGER row R5; IDX README l.2489.**
Already recorded: Lévy splitting = G2_B8, dead at T ≥ 0.5925; splitting not translation-invariant "with
its own formula" = not excluded and without object; "with free splitting its existence is equivalent to the target". Round
6 is the numerical exploration of that residue; the reviewed proposal aims to supply the formula.

A4. **Position-dependent potential and contact as jump atom.**
`phase-195-modern-tools/INV_N_001_BAKRY_EMERY_GAMMA2_GAP_CEILING_NO_GO.md` §1 (PROVED): 𝔞_T = E_T + ∫W_T F²
with −v c_F(u) = ½v∫(F(t) − F(t+u))² − v‖F‖², jump measure ν(u)du + ½Σv_nδ_{log n} and explicit W_T(s);
`phase-211-sign-sandbox/ROUND_005_D.md` §§1–2 (jump form with the comb as atomic measure,
ground-state representation; LEDGER 211 C17, class NO-GO 𝒦_gap); `phase-162…/R162_504` Thm. 1
(Beurling–Deny form); CA_I_001 Thm. 2 (Markov class closed under adding positive mass to the comb).
The reading of `ROUND_006` §4.5 ("q_p has jump measure θ_pK + (v_p/2)δ and a potential") is this
decomposition done prime by prime. The tools that would sign each q_p ⪰ 0 (maximum principle,
ground state, Hardy/Picone, gap) are those of these classes, monotone in the jump measure.

A5. **Position-dependent partition of the archimedean kernel.** `phase-188-closing-D/
L2_BUILD_004_IMS_LOCALIZATION.md` §§1–4 (localization identity with ω̃(x, y)K; "the primes are pure
coupling"; declared repetition of 106_47, 106_59 and of the rejected option of phase 121); 211
`POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION` §7 (indefinite IMS remainder). It is a partition by position in space,
not by prime: lateral antecedent, not a coincidence.

A6. **Not found** (search for "local certificate", "T_loc", "reparto", "bang-bang", "todo o nada",
"igual densidad", "cross-prime", "cede", in `03-research/` and `05-meta-and-planning/`; not exhaustive and without
value as a proof of novelty): a per-prime splitting with θ_p(t, s) depending on both positions (class
DIR); the duality with states of equal pointwise density; the threshold near log 2 of that class. These three
points of round 6 have no textual antecedent. None of them is the proposed object.

## B. The lemma "the kernel at the own contact contributes nothing"

B1. **It is not stated, proved or refuted in the corpus** as a lemma. It only appears as a heuristic in
`ROUND_006` §9.4. What is proved is its correct form: the complementary slackness of A1 (Theorem D,
step 4), which is a property of the optimal pair and not a prior rule.

B2. **Literal statement: FALSE (PROVED in the case u_p − δ < T; ARGUED outside it).** Let
q_θ(F) = ∫W_pF² + ¼∬θK(F(t) − F(s))² − v_p c_F(u_p), with θ ≥ θ_0 > 0 near the diagonal (the infimum
μ(θ) over the unit sphere of P_T is attained: the form dominates a logarithmic energy and the embedding is
compact), and let B = {(t, s) ∈ I²: ||t − s| − u_p| < δ}, E_B(F) = ¼∬_B K(F(t) − F(s))². For η > 0 let
F_η be a minimizer of q_{θ+η𝟙_B}. Then μ(θ) ≤ q_θ(F_η) = μ(θ + η𝟙_B) − ηE_B(F_η). If the kernel on B did not
contribute, μ(θ + η𝟙_B) = μ(θ) and E_B(F_η) = 0, that is F_η(t) = F_η(s) for almost every pair at distance in
(u_p − δ, u_p + δ). That makes F_η constant on (−T, T − u_p + δ) and on (−T + u_p − δ, T), with the same
value. If u_p − δ < T the two intervals overlap and F_η is constant on I, incompatible with
∫F e^{t/2} = 0 unless F = 0. Hence **μ increases strictly when kernel is added on any band around the
own contact** as soon as T > u_p − δ (for p = 2: every T ≥ 0.70, which is exactly the range where one wants to
use the rule). If u_p − δ ≥ T, equality would require a minimizer constant on the two extreme zones:
not excluded by this argument, not generic (ARGUED).

B3. **What the heuristic does contain (PROVED, elementary, and with no bearing on the infimum).** The energy at
the exact distance u_p vanishes on the F with F(t) = F(t − u_p) along the chain. At neighbouring distances
u_p + w it does not vanish: on those F one has ∫(F(t) − F(t − u_p − w))² ≈ 2ε_F(|w|), so that the band acts
as a bounded short-range kernel, K(u_p)𝟙_{|w|<δ}, against the kernel K(w) ~ 1/w already present. The
band "is worth little" in proportion ~ K(u_p)|w| and only while |w| ≲ 1/‖F′‖; with ‖F′‖² ≈ 110 (pair of L″) that
gives |w| ≲ 0.1, compatible with the band widths of §9.3. The width thus depends on the state and not on the
prime: there are no fixed bands. The computation with the boundary terms was not done (ARGUED).

B4. **Reading.** The true version is comparative ("at the optimum, the distance u goes to the prime whose
obstructing state has larger ε(u)") and its bands are {ε_{σ_p} < ε_{σ_q}}, defined by the obstructing
states, which are obtained by solving the problem. As a prior rule it is circular in the sense of
`RULES_AVOID.md` J3. With three or more primes the rule "for the prime without contact there" does not determine who
gets each distance.

## C. The four points

**(1) Antecedent.** Correct but incomplete. Missing A2 (emptiness of the signed splitting), A3 (the residue already
recorded) and A4 (jump form plus potential, classes 𝒦_M, 𝒦_gap, 𝒦_BE).

**(2) New object.** Does not hold up.
- θ_p by distance bands: inside `G2_B8_R5` Def. 1; the all-or-nothing optimum by distance is step 4
  of Theorem D.
- W_p(t): the only real difference from the antecedent. But "distance bands + free W_p(t)" is class M
  of `ROUND_006` §2, and the table in §3 of the same memo gives for M τ = −1.60·10⁻⁴ at T = 0.5925 with
  a_T ≻ 0 (NUMERICAL, a single resolution, N = 20; the delivered script does not let one identify mode M
  at a glance, it was not recomputed). The class that reaches the ceiling below log 2 is DIR, and §4.2 says it does so through the
  dependence of θ on both positions, exactly what the rule suppresses.
- The lemma: false as stated (B2); in its true form it is A1.

**(3) Why it would avoid the difficulty of the antecedent.** It does not avoid it. The argument presented ("L″ is for
invariant splittings; window-dependent potentials reach the ceiling up to log 2") attributes to
W_p(t) what the numbers attribute to θ(t, s): with W_p(t) and θ(|t − s|) the splitting no longer reaches the ceiling
at 0.5925. The difficulty of `G2_B8_R5` §5 (the prime 3 pays inside the test of the prime 2; a splitting by
factors charges the maximum of the deficits) remains intact in class M and reappears in DIR past log 2 with
the same picture (§9.3).

**(4) Link with global positivity.** Σq_p = a_T is correct and trivial; the content is in q_p ⪰ 0,
and there:
- With θ ≥ 0 the class fails for T ≥ 0.70 with a_T ≻ 0 (§§7.3, 8.1, 8.4; NUMERICAL, three optimizers). In
  the open range there is nothing to certify with it.
- The format is affine in the weight and the rule (which distance goes to which prime) does not depend on the weight: it serves equally
  for cΛ, for a_P and for any comb with the same supports. For c < 1 it certifies (§7.2); nothing in the
  rule changes at c = 1. `RULES_AVOID.md` B1/B8 and J2; `OBJECT_SPEC.md` O2, O4. The candidate cannot
  write point (5) of `OBJECT_SPEC.md` §4 (the line that breaks for cΛ and a_P).
- "Compute the deficit and look for a signed correction": with signed pieces without a bound the existence of the
  splitting is the target (A2, A3); with bounds, §7.3(iii) gives values near the ceiling without a formula. All the
  sign would remain in the correction, for which no operation is proposed. It is "another auxiliary energy without
  a sign mechanism" (A4 of `RULES_AVOID.md`) and a per-window certificate format (O5).

**Summary.** Repetition in the kernel part (G2_B8_R5 Def. 1 and Theorem D), real difference only in W_p(t),
which according to the data of the round itself is not enough; lemma false as stated and already contained, in its true
form, in the antecedent; certificate format without mechanism. No derivations of the
rule-based splitting nor computation of its deficit are authorized.

## D. Reopening condition

It is reopened only with one of these operations, written before deriving:

1. A closed formula for θ_p(t, s) (depending on both positions, not on |t − s|) and W_p(t), not
   obtained from an optimizer nor from the obstructing states, **that depends on the exact values of the weight
   in a non-affine way** or on a relation between contacts of different primes (for example the positions
   log 2, log 3, log(9/4), log(3/2) together), with the line that breaks at cΛ and at a_P identified as a loss
   of non-negativity of a concrete term; and a statement for three primes.
2. For the signed part: an identity that writes the negative piece of θ_p as a square compensated by
   a named term of another prime (coupling between q_2 and q_3 that is not a splitting), with remainder
   manifestly ≥ 0. Without that identity, "signed correction" is the target.

First check for any reopening: at T = 0.5925, N = 20, the formula must give q_2, q_3 ⪰ 0 where
class M gives −1.60·10⁻⁴; if the formula falls into M, it is falsified by that point (subject to confirming the value
of M at N = 30, 40).

## Results recorded (without sign)

R6-a (PROVED relative to `G2_B8_R5` Theorem D). The assignment "each prime gives up the distance of its contact"
is the complementary slackness of the optimal splitting; it is already in the printed values of the pair of L″.

R6-b (PROVED for T > u_p − δ; B2). Adding kernel on a band around the distance of the own contact
strictly raises the bottom of the local form. "Contributes nothing" is false.

R6-c (NUMERICAL, from `ROUND_006` §§3, 7.3; not rechecked here). Class M negative at 0.5925; class DIR with
θ ≥ 0 reaches the ceiling up to 0.69 and fails from 0.70. No proof in the continuum in either direction.

Without textual antecedent and without object: two-position θ_p(t, s) with its own formula; dual of equal
pointwise density (ARGUED in §5, checked only in the discretization).

## Reservations of this review

- No script was rerun; the values of round 6 are taken as NUMERICAL.
- L″ still lacks interval arithmetic and a recorded audit.
- B2 uses that the infimum is attained (compactness from the 1/u singularity of the kernel with θ ≥ θ_0 > 0 near
  the diagonal); in the all-or-nothing class with θ_p = 0 near the diagonal the argument applies to the piece
  that keeps the short kernel, or to the Galerkin model.
- Not cross-checked in the primary sources: phases 155–156 (per-window certificates) beyond grep, Paper 48, and the
  folders before phase 100.
