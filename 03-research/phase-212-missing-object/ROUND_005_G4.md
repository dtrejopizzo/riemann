# Round 5, seed G4: induction that lengthens the window with the divisor identity in the step

Notation from `../phase-211-sign-sandbox/STATEMENT_001.md`. T_n := ½ log n. For a real weight vector
v = (v_n) summable in each window, a_T^{(v)} and λ_A(T; v) are the form and the bottom with that comb; v^{(n,x)}
is v with the coordinate n replaced by x. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN /
NO-GO / NUMERICAL.

## 0. Cross-check (done first; it governs the rest)

**(1) Closest antecedent, read as primary source.**

- `phase-162-row-d-first-contact-closure/R162_802_T_EVOLUTION.md` §4 point 4 and §5. It already poses the first
  Riccati integral of Kreĭn–Bellman–Siegert for truncated convolution operators (the window as a
  flow in T) and concludes, in its meta-statement, that Λ∗1 = log is a convolution identity on the
  tests which inside the flow acts as a window shift; therefore it only produces relations
  between f(T) and f(T + ½ log m) linear in the weight, and "a monotone quantity forbidding contact would have
  to be nonlinear in the weight in the boundary traces of the switch-on; none is identified". It is
  exactly seed G4 (divisor identity in the inductive step, boundary datum, Riccati).
- `phase-162-row-d-first-contact-closure/R162_2701_TATE_CANONICAL_SYSTEM.md` §§0–1: the 2×2 canonical
  system of transfer by primes; each factor is a boost conjugated by free propagation, J-unitary
  for every value of the reflection coefficient, and the system detects no falsifier (deletion,
  arbitrary atomic weights, Beurling, Λχ₂). It is the "port datum" with exact update per crossing.
- `phase-197-barrier-theorem/BARRIER_W_001_…_NO_GO.md` §§1–6 (read in full): every invariant of the class
  𝒮 (extension by zero, concavity in the comb, continuity in T, invisibility of the entry U0,
  parity, compact resolvent) holds for a_P, truncations, cΛ, O_6 and Beurling; the only datum that reads Λ
  at a crossing is the Hellmann–Feynman pairing with the minimizer.
- `phase-211-sign-sandbox/ROUND_008_C.md` Prop. 2.3 and Prop. 5 (incoming contacts contribute 0 to all
  orders in the extension-by-zero framework; Grönwall in T = (★) plus a rate) and
  `phase-165-critical-interlacing/R165_202_NODE_FLOW.md` row 1.4 (virial variation formula).
- `ROUND_001_B.md` / LEDGER K2 (Schur parameters of the extension problem from exact Λ) and
  `REVIEW_003.md` / `RULES_AVOID.md` J8 (Riccati/Darboux with the comb as superpotential, phase 70).

**(2) New object or statement.** I did not manage to write an invariant I_T with update Φ_n satisfying
(a)–(c) of the seed. The only new things are three short lemmas (§2) explaining why requirement (a)
—"Φ_n preserves positivity when, and only when, the incoming weight is the one dictated by the divisors"—
cannot be satisfied at the instant of crossing by any invariant whose sign determines λ_A, and why
the rule "the new weight is determined by the previous ones" does not distinguish Λ from any other weight.

**(3) Why it would avoid the antecedent's difficulty.** It does not avoid it: the lemmas of §2 confirm and sharpen
the diagnosis of R162_802 §5 and of BARRIER_W_001 §6; they do not provide the quantity nonlinear in the weight that
both ask for.

**(4) Identity that would connect with global positivity.** No new one. The reformulation by admissible
intervals of §2 (Lemma 2) is a coordinate-by-coordinate rewriting of the convex set K_T of phase
197 (W2); B3 of the index: valid target, not progress.

**Verdict of the cross-check: repetition** (R162_802 §§4–5 for the Riccati flow and the use of Λ∗1 = log in the
flow; R162_2701 for the per-crossing port datum; BARRIER_W_001 for induction in the window). By
rule 3 of the brief the memo should end here; only the three lemmas of §2 are added because they are short,
complete and delimit which part of the seed is impossible as stated.

## 1. Object

There is no object. I tried three invariants; all three fall into antecedents:

- I_T = (a_T, P_T) with the extension-by-zero rule: it is 𝒮 (BARRIER_W_001 §1).
- I_T = Kreĭn transfer matrix of the window (or the boundary resolvent Γ_T(±T, ±T), Dirichlet-to-Neumann
  datum of the window) with the rank-two polar correction of the Tate conditions: it is
  R162_802 §4 point 4 and R162_2701. Its Bellman equation ∂_T Γ = −γ_T γ_T* has a forcing of fixed sign
  for **every** kernel; the weight enters only linearly in the integral equation for γ_T, and the loss of
  positivity is not an exit from a cone but a blow-up of the solution (vanishing of a determinant:
  W-det, 𝒦_W). ARGUED here; the statements are in those files.
- I_T = admissible interval of each comb coordinate given the previous ones (§2, Lemma 2): a rewriting of
  K_T.

## 2. Three lemmas on the seed (without sign)

**Lemma 1 (neutrality of the crossing; PROVED relative to continuity in T, CITED P46 lem:contA, BARRIER_W_001
(S3)).** Let I_T be any invariant such that "I_T is positive" ⟺ λ_A(T; v) ≥ 0, for all T and all v in
a class containing v^{(n,x)} for x in an interval. Then the positivity of I_{T_n+} is the same
for all those x; in particular no rule Φ_n can preserve positivity "only when" x is the
value dictated by the divisors.

*Proof.* For F ∈ L²(I_{T_n}), c_F is continuous with support in [−2T_n, 2T_n] and c_F(±2T_n) = 0, hence
the term −x Re c_F(log n) vanishes and λ_A(T_n; v^{(n,x)}) does not depend on x. By the continuity of
T ↦ λ_A(T; v^{(n,x)}) (lem:contA uses only summability of the weights, BARRIER_W_001 (S3)), the sign of
λ_A just after T_n is that of λ_A(T_n), the same for all x, except in the boundary case λ_A(T_n) = 0;
and in that case the modulus U2 (v_n C_T / log(1/2η), CITED in BARRIER_W_001 (S3)) is of the same order for all
x ≥ 0. ∎

Reading. The information of the incoming weight is not decided at the crossing but along [T_n, ∞): the
"forcing" −x Re c_F(log n) only sees functions with mass at distance ≥ log n, and grows with the collar. A pointwise Φ_n
cannot carry a sign; the inductive step has to include the subsequent archimedean evolution, and
then it ceases to be a function of the incoming weight alone.

**Lemma 2 (admissible interval; PROVED).** For fixed T and v let S_n(T) := {x ∈ ℝ : λ_A(T; v^{(n,x)}) ≥ 0}.
Then S_n(T) is a closed interval, and if λ_A(T; v) > 0 it contains [v_n − λ_A(T; v), v_n + λ_A(T; v)].

*Proof.* x ↦ a_T^{(v^{(n,x)})}(F) is affine for each F, hence x ↦ λ_A(T; v^{(n,x)}) is an infimum of
affine functions: concave and upper semicontinuous; its superlevel set {≥ 0} is a closed
interval. Since |Re c_F(log n)| ≤ ‖F‖² = 1, λ_A(T; v^{(n,x)}) ≥ λ_A(T; v) − |x − v_n|. ∎

Consequence. In every window with λ_A(T) > 0 (in particular at every T ≤ ½ log 5) the "only when" part
of (a) is false: incoming weights x with |x − v_n(Λ)| < λ_A(T) preserve positivity. This coincides with
R4-f and A1 (the verdict does not distinguish c near 1). Induction by intervals is written: (★) ⟺ for
all n, v_n(Λ) ∈ ⋂_{T ≥ T_n} S_n(T) with the other coordinates at Λ; it is a reformulation (B3).

**Lemma 3 (the divisor rule does not constrain the weight; PROVED).** For every weight a: ℕ_{≥2} → ℝ, with
L_a := a ∗ 1 (a(1) := 0), one has a(n) = L_a(n) − Σ_{d|n, d<n} a(d). Hence "the new weight is determined
by the weights at the proper divisors" is true for every a with its own L_a; the specific information
is L_Λ = log, i.e., that the coefficient of the measure μ_Λ ∗ μ_1 at the offset u = log n is u times that of
μ_1 (μ_a := Σ a(n) n^{−1/2} δ_{log n}, μ_1 with coefficients 1). *Proof:* definition of ∗. ∎

For cΛ: L = c·log; for a_P: L = log of the P-rough part; for a Beurling system: the logarithm of
its norm. The rule "Λ(n) = log n − Σ_{d<n}Λ(d)" only says L = log, which is a property of the position of the
offset, not of the previous weights. In the flow in T, the convolution μ_Λ ∗ μ_1 composes offsets (sum of
log d and log(n/d)), while the window recursion composes lengths (concatenation of
intervals, product of transfer matrices): the two operations do not coincide. That no nonlinear
dictionary exists between them is ARGUED (it is the reading of R162_802 §5: inside the flow Λ∗1 = log is a
window shift, linear in the weight).

## 3. Mechanism

None. The seed's question about the forcing has this answer (ARGUED, with the sources of §0):
in the Bellman equation for the window resolvent the Riccati term −γ_Tγ_T* has fixed sign
for every kernel, so the cone is invariant for any weight; the comb enters only in the boundary
column γ_T, linearly, as a delta at the offset log n which at T = T_n couples exactly the points
±T (J-unitary boost-type factor, R162_2701 §1, admissible for any coefficient). The divisor identity
gives no sign to the forcing because the forcing already has a fixed sign and is not what decides; what
decides is the absence of blow-up, which is the vanishing of a determinant (W-det) or n₋(T) = 0 itself
(BARRIER_W_001 W1).

## 4. Controls

There is no sign step; the three lemmas are structural and hold unchanged for c = 2, non-integer c, a_P
and Davenport–Heilbronn (Lemma 1 only uses summability and support; Lemma 2, affinity in the weight; Lemma 3, the
definition of ∗). That is what is expected of lemmas without sign and confirms that none is a mechanism. In particular
for c = 2 the weight 2Λ satisfies the divisor rule with L = 2 log = log(n²): the fixed archimedean factor
does not appear in any of the three invariants of §1 in a way that breaks it; a correct mechanism would have to
break there and this one does not.

## 5. Own verdict

**I did not manage to write an object satisfying A1–A6.** Repetition of R162_802 §§4–5, R162_2701 and BARRIER_W_001.

## Result

No new mechanism. Three lemmas without sign: Lemma 1 and Lemma 2 PROVED (relative to lem:contA and to U2, CITED);
Lemma 3 PROVED; the reading of the Riccati forcing ARGUED.

## What was proved

The requirement "preserve positivity at the crossing only with the dictated weight" is impossible for any
invariant whose sign determines λ_A (Lemmas 1–2); the divisor rule, read as an update rule,
holds for every weight with its own L_a (Lemma 3), and its content L = log is positional.

## What failed and why

Between crossings the space grows and the form does not change; at the crossing the incoming term is invisible. The sign
step would have to be a quantity nonlinear in the weight on the boundary traces of the switch-on, which
R162_802 already asked for and did not identify; the Kreĭn or Tate port datum is blind to the falsifiers.

## Concrete next step

None within this seed. The only thing not covered is a relation between the composition of offsets
(μ_Λ ∗ μ_1 = u·μ_1) and the composition of window lengths that is not linear in the weight; it requires a
written object before any derivation. Not opened as primary sources: phase 64 (thm:KEP3), phase 70
(E70_10–12), R162_503, R162_903, nor the files of phase 116/114 with "Dirichlet-to-Neumann".
