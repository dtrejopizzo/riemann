# Round 24 A: three sign-carrying designs on the bandwidth axis, and the contact-entrance lemma

Target (★): λ_A(T) ≥ 0 for every T > 0, for the window form a_T of STATEMENT_001 §1. Notation as in STATE_002:
N = e^{2T}, c = 2πN, T_n = ½ log n, v_n = 2Λ(n)/√n, a_T(F) = Arch(F) − Π_T(F), Π_T(F) = Σ_{log n < 2T} v_n Re c_F(log n).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. No equivalence of (★) with any statement outside
STATEMENT_001 is used; no reduction to zeros; no explicit formula over zeros.

Structural facts taken as given (from the record): the margin is λ_A ≈ κ₈(1 − χ_8(c)) (NUMERICAL, P211-8E; R8 PROVED as an
upper bound given thm:ext-half); the minimiser lies in E·span{ψ_0, ψ_4, ψ_8} to 10⁻⁴ (NUMERICAL); Λ enters every route only
through the radical identity R10 (Λ ∗ 1 = log via Poisson over ℤ); T ↦ λ_A(T) is continuous and non-increasing (PROVED).

---------------------------------------------------------------------------------------------------------------------
## 0. Corpus check

Searched: ROUTES-TRIED-INDEX/README.md (all P211-* rows, REVIEW verdict blocks, phase 193 fronts E–H, the guiding semiring
principle, PROOF_L_SHARP_* rows of phase 199, PATTERN_001, MECH_001), 04_PHASES_100-189.md (flowdet, W4, R162_1902,
G4E-R170_888, R163_102a), 06_OPEN_RESIDUES (R5, R6), SURVEY_MODERN_UNTRIED (B1 interlacing, B2 Bakry–Émery), and
STATE_002 §§1–5. Keywords: Sturm, interlacing, monotonicity in c/N, Hellmann–Feynman, heat/semigroup, extremal, prolate,
Slepian, Chebyshev, floor, sawtooth, contact entrance.

Recorded neighbours and what each design must avoid:
- Variation of λ_A in T + Grönwall (P211-8C; R186_038 α.3; class 𝒦_H; lem:flowdet NO-GO "coefficient dominated by
  h*(T)²/λ_A"); differential inequality in c from the certified base with the Slepian rate (PROOF_L_SHARP_H_001: closes iff
  a virial bound (H) at the minimiser, functional of h*; "crossing q enters at second order" for a smooth fixed test).
- Leakage comparison W_T(Ef) ≥ κμ^{−A}·leak(f) (Lemma L′ NO-GO by gauge; L′♯ OPEN, REF-D).
- Positive combs / sawtooth / Chebyshev identity used linearly (W4 "wrong sign": lower bounds on the comb; R162_1902 linear
  value both signs; SPEC_A mechanism = Chebyshev identity, ADMISSIBLE as specification, OPEN, REF-D).
- MSS interlacing families on Euler-product vectors (INV_M_001 NO-GO); Bakry–Émery Γ₂ (INV_N_001 NO-GO); heat flow / dBN
  (N6, ES-15 dead).
- Contact sawtooth in κ, "drops upon entering each p" (PATTERN_001, NUMERICAL, Mori data): an observation, never analysed.

New reasons are stated per design in §§1–3. In short: none of the recorded rows isolates the *integer entrance event* of a
contact as an object with its own first-order law (PATTERN_001 only observed it; L_SHARP_H treated it for a fixed smooth
test, where it is second order); none used Chebyshev's *two-sided* floor relation at the *sharp* comb truncation log n < 2T
together with R10; none posed prolate extremality with the index-8 constraint count as the extremal problem whose
Euler–Lagrange equation is the bottom equation of a_T on E-images.

---------------------------------------------------------------------------------------------------------------------
## 1. Design A: contact-entrance ledger on the bandwidth axis

**Object.** N runs continuously; contacts enter at N = n ∈ ℕ with Λ(n) ≠ 0. Split the T-axis into contact-free segments
(T_n, T_{n'}) (n, n' consecutive prime powers). On a segment the comb set is frozen; the form changes only through the
domain I_T. At T_n one atom v_n δ_{log n} enters at the edge of the autocorrelation support [−2T, 2T].
The ledger compares (i) the entrance event, read on the near-null states through their edge values, with (ii) the
inter-contact evolution, read through the Slepian rate of the index-8 prolate defect.

**Inequality input (not equivalent to (★)).** Slepian's identity ∂_c log χ_k(c) = 2ψ_k(1)²/c for the prolates normalised on
[−1, 1] (CITED, P211-8E, REVIEW_006 reproduced), which converts edge values of prolate near-null states into the rate of
their concentration defect; plus the elementary edge Cauchy–Schwarz bound of Lemma 4.1 below.

**New reason vs P211-8C / L_SHARP_H.** Those rows bound the one-sided variation of λ_A in T as a whole (interior virial plus
edge strip) and close on a constant C in (EB_C). Here the entrance event is isolated as a separate object with an exact
first-order law (Prop 4.3), and the question asked is the one in the brief: what happens to the near-null states at an
integer entrance. If the entrance event had a positive (restoring) part, positivity could propagate through integers
without any rate constant — that would avoid the recorded failure. §4 decides this.

**Falsifier mechanism (intended).** Entrance positions are the integers; Beurling systems enter at non-integers, a_P skips
entrances below P, cΛ rescales every entrance cost, finite modification changes one entrance. A ledger in which the
restoring part were tied to the integer position would fail for (b), (c), (d) by construction, and for (a) through the
cost scaling. Outcome in §4: the entrance law is sign-definite and weight-generic, so the intended mechanism does not
exist; recorded as NO-GO for the class.

## 2. Design B: Chebyshev's two-sided floor relation at the sharp truncation

**Object.** The comb truncation log n < 2T is sharp, and c_F is supported exactly in [−2T, 2T]. R10 is Λ ∗ 1 = log; its
sharp-cutoff form is Σ_{n ≤ y} Λ(n)⌊y/n⌋ = log⌊y⌋!. Chebyshev's weights ε = (ε_1, ε_2, ε_3, ε_5, ε_30) = (1, −1, −1, −1, 1)
satisfy the integer inequality 0 ≤ Σ_k ε_k⌊y/k⌋ ≤ 1 for all y ≥ 0 (CITED, Chebyshev 1852). Design: convolve the comb measure
ν = Σ Λ(n) n^{−1/2} δ_{log n} with μ_ε = Σ_k ε_k k^{−1/2} δ_{log k} ∗ Σ_m m^{−1/2} δ_{log m}; by R10, ν ∗ μ_ε is explicit, and the
distribution function of m^{1/2}μ_ε lies in [0, 1]. Read on the edge of [−2T, 2T] this gives a two-sided bound on the
truncated comb at every resolution. This is the (ℕ, +, ·) interplay asked by the semiring principle: ⌊·⌋ is additive
(lattice), the convolution is multiplicative, and the inequality lives exactly where they meet (m ≈ kn at the cutoff).

**New reason vs W4 / R162_1902.** W4 used positive combs and sawtooth as one-sided lower bounds on the comb (wrong
direction); R162_1902 used the sawtooth linearly at the level ∫|F̂|² Re ζ. Here the *upper* half Σε_k⌊y/k⌋ ≤ 1 is used,
at the sharp cutoff where smoothing cannot reduce it to R10.

**Falsifier mechanism (by construction).** cΛ: the identity becomes c·log⌊y⌋!, off by (c − 1)y log y; a_P: off by
Σ_{p<P} log p ⌊y/p⌋ ≍ y; Beurling: ⌊·⌋ is replaced by the generalized counting function N_B, and N_B(y) − Σ ... is not
{0,1}-valued (lattice rigidity, R163_102a Thm R CITED: N_B = ⌊·⌋ + c forces ℕ); finite modification at n: off by ηy/n.

**Decisive defect (PROVED as a class statement, Prop 2.1).** The inequality fixes the comb only to relative precision O(1)
(density level), while (★) is decided at relative precision e^{−2πN}·e^{−T}. Concretely:

**Prop 2.1 (NO-GO, PROVED).** Let 𝒮 be any finite family of Chebyshev floor relations Σ_k ε_k⌊y/k⌋ ∈ [α, β] (finite ε) and
let 𝒞(𝒮) be the set of nonnegative weights w on prime powers satisfying, for all y ≥ 1, every inequality obtained from
𝒮 by summing against w ∗ 1 (i.e. Σ_n w(n) Σ_k ε_k⌊y/(kn)⌋ ∈ [Σ_k ε_k log⌊y/k⌋! − β', ...] with the Stirling margins of 𝒮).
If 𝒞(𝒮) contains Λ with slack at every y in the interior of the margins, it contains cΛ for all c in a neighbourhood of 1
on every bounded range y ≤ Y.
*Proof.* The constraints are finitely many affine inequalities in w on y ≤ Y (finitely many prime powers below Y), each
satisfied strictly by Λ by hypothesis; strict affine inequalities are open in c. ∎
Consequence: any proof of (★) on T ≤ ½ log Y whose only Λ-input is a finite set of strictly satisfied floor relations
also proves (★) for cΛ, c near 1; but λ_A(T; cΛ) < 0 for every c ≠ 1 as soon as λ_A(T; Λ) is at its interval endpoint
(J_T is a closed interval containing 1, P211-D2), and for c = 1.1 at T = 1 (Q1, certified). So the relations must be
used *with zero slack*, i.e. as identities — which is R10 again. Design B collapses to (b) of the map. NO-GO (class:
finitely many strict floor relations, any precision).

## 3. Design C: prolate extremality as the variational principle

**Object.** On E-images f ∈ L²(−1, 1) (dilated) with the four transported constraints f(0), ℱf(0), A(Ef), B(Ef), the
even-sector Courant–Fischer value of the concentration defect 1 − ‖P_c f‖²/‖f‖² on a codimension-4 even subspace is
≥ 1 − χ_8(c) (Courant–Fischer for the time-band-limiting operator, CITED; constraint count R7 PROVED). Design: exhibit
(★) on E-images as the Euler–Lagrange condition of min{ a_T(Ef) − κ(1 − ‖P_c f‖²) : constraints }, whose extremal value
is known (zero, attained on ψ_8 modulo constraints) by prolate extremality.

**Corpus status.** The inequality a_T(Ef) ≥ κ·(defect) is Lemma L′ / L′♯ (MECH_001, AUDIT_12: L′ NO-GO by gauge; L′♯ OPEN,
REF-D). The new element would be the restriction of the comparison to the index-8 constrained subspace, where the
defect is ≥ 1 − χ_8 by Courant–Fischer. But on the gauge directions (f supported in (−1/λ, 1/λ), Ef = 0) the defect is
positive while a_T(Ef) = 0, so the comparison fails exactly as L′ does; with the gauge quotient it is L′♯. No new reason
survives; Design C is a retry of L′♯ and is not pursued. ARGUED (no proof attempted).

**Ranking.** A is the only design with an unrecorded object (the entrance event) and a mechanism tied to the integer
positions; B is closed by Prop 2.1; C is L′♯. §4 attempts A.

(Remark to Prop 2.1: for y ≤ Y the floor functions and log⌊y/k⌋! are piecewise constant with finitely many jumps, so 𝒮
yields finitely many distinct affine inequalities in (w(n))_{n ≤ Y}; inequalities tight for Λ in which w appears are
identities and fall under R10.)

---------------------------------------------------------------------------------------------------------------------
## 4. Design A, first lemma: the law of a contact at its entrance

Throughout, F ∈ L²(I_T) is extended by zero, c_F(u) = ∫F(t) conj F(t − u) dt.

**Lemma 4.1 (edge Cauchy–Schwarz; PROVED).** For 0 < δ ≤ 2T,
  |c_F(2T − δ)| ≤ ‖F‖_{L²(T−δ, T)} · ‖F‖_{L²(−T, −T+δ)}.
*Proof.* The integrand F(t) conj F(t − u), u = 2T − δ, is nonzero only if t ∈ I_T and t − u ∈ I_T, i.e. t ∈ (T − δ, T) and
t − u ∈ (−T, −T + δ). Cauchy–Schwarz on (T − δ, T). ∎

**Lemma 4.2 (first-order entrance; PROVED).** If F has one-sided limits F(T⁻) and F(−T⁺), then
  c_F(2T − δ) = δ F(T⁻) conj F(−T⁺) + o(δ)   (δ ↓ 0).
If moreover F ∈ H¹(I_T), the remainder is O(δ^{3/2}) with constant ≤ ‖F′‖_{L²(I_T)}(|F(T⁻)| + |F(−T⁺)|) + δ^{1/2}‖F′‖².
*Proof.* Substituting t = T − s, c_F(2T − δ) = ∫_0^δ F(T − s) conj F(−T + δ − s) ds. Both arguments lie within δ of the
respective edge, so the integrand equals F(T⁻)conj F(−T⁺) + o(1) uniformly on s ∈ (0, δ); integrate. For H¹:
|F(T − s) − F(T⁻)| ≤ s^{1/2}‖F′‖ and likewise at −T; expand the product and integrate, ∫_0^δ s^{1/2} ds ≤ δ^{3/2}. ∎

**Proposition 4.3 (sign of an entrance; PROVED).** Let n be a prime power, T = T_n + h with 0 < h small and no other contact
in [2T_n, 2T]. Then for every F ∈ P_T,
  a_T(F) = a_T^{∖n}(F) − v_n Re c_F(log n),     log n = 2T − 2h,
where a_T^{∖n} is a_T with the atom at n deleted. If F is real-valued and even with F(T⁻) ≠ 0,
  −v_n Re c_F(log n) = −2h v_n F(T⁻)² + o(h) < 0;
if F is real-valued and odd, the same term equals +2h v_n F(T⁻)² + o(h) > 0.
*Proof.* The decomposition is the definition of Π_T. Apply Lemma 4.2 with δ = 2h; for even real F, F(−T⁺) = F(T⁻), for odd
real F, F(−T⁺) = −F(T⁻). ∎

**Corollary 4.4 (entrance never restores the even bottom; PROVED as stated, CONDITIONAL in its application).**
(i) For every T and every F ∈ P_T: a_T(F) ≤ a_T^{∖n}(F) + v_n ‖F‖_{L²(T−2h,T)}‖F‖_{L²(−T,−T+2h)} and
a_T(F) ≥ a_T^{∖n}(F) − (same) (Lemma 4.1). Hence |λ_A(T) − λ_A^{∖n}(T)| ≤ v_n · sup over the two near-minimisers of the edge
product, and the entrance is a perturbation of size v_n × (edge mass in a strip of width 2h).
(ii) Assume (R_edge): for T in a right neighbourhood of T_n the bottom of a_T on P_T is simple, attained by a real even F*_T
continuous at ±T, with T ↦ F*_T(T⁻) continuous at T_n⁺. Then the one-sided T-derivatives satisfy
  ∂_T⁺λ_A(T_n) = ∂_T⁺λ_A^{∖n}(T_n) − 2 v_n F*_{T_n}(T_n⁻)²,
so the entrance adds a non-positive jump to the right derivative, of size exactly 2v_n × (squared edge value of the
bottom state). [Proof: upper bound from F*_{T}^{∖n} as trial vector in a_T plus Prop 4.3; lower bound from F*_T as trial
vector in a_T^{∖n}; both differ from the stated value by o(h) under (R_edge). Danskin's argument is the one of P211-8C
Thm 1, with the entrance term as the only addition.] CONDITIONAL on (R_edge); (R_edge) is the regularity hypothesis
already recorded as open in P211-8C ("minimisers bounded near ±T").

**What this decides (PROVED modulo (R_edge) for (ii), unconditional for the class statement).**
- On contact-free segments the comb set is fixed and P_T ⊂ P_{T′}, a_{T′} = a_T on P_T (extension by zero; contacts with
  log n ≥ 2T see c_F(log n) = 0): λ_A is non-increasing (PROVED, known).
- At an entrance, by Prop 4.3 / Cor 4.4, the contact acts on even states with a non-positive first-order term.
  Both channels of the bandwidth flow are descents. A propagation of positivity from the certified range along N can
  therefore never come from the integer events; it needs a lower bound on the total descent rate, i.e. the inequality
  (EB_C) of P211-8C (OPEN, recorded as a restatement-class). NO-GO for the class "positivity propagated through contact
  entrances in N" (sign-definite entrance law), PROVED for the sign of the entrance term; the reduction of every
  propagation scheme to a rate bound is PROVED (monotonicity) and that rate bound is the recorded open (EB_C).
- Falsifier test of the entrance law: Prop 4.3 holds verbatim for any positive weight at any entrance position, so it
  survives (a) for c > 0, (b), (c) and (d). It is comb-generic, hence a piece, not a sign step (rule 4). This is the
  mechanism by which Design A fails: the integer position of a contact carries no sign; only its weight multiplies a
  sign-definite edge term.

**What the edge value says about the near-null states (ARGUED, with one CITED identity).** If F*_T is, to the measured
accuracy, the E-image of a self-dual prolate combination dominated by ψ_8 in the dilated variable x = t/T on [−1, 1], its
edge value satisfies, with F*(t) = T^{−1/2}ψ(t/T) and Slepian's identity ψ_8(1)² = (c/2)∂_c log χ_8(c),
F*(T)² ≈ ψ_8(1)²/T = (c/(2T))·∂_c log χ_8(c). Since 1 − χ_8(c) decays like e^{−2c} up to powers, ∂_c log χ_8 ≈ 2(1 − χ_8),
so F*(T)² ≈ (c/T)(1 − χ_8) and, with λ_A ≈ κ₈(1 − χ_8), the entrance jump of Cor 4.4(ii) is
  2v_n F*(T_n)² ≈ (2 v_n c/(T κ₈)) · λ_A(T_n).
Two readings follow: (1) the entrance cost is proportional to λ_A itself, i.e. it is a finite jump in the log-derivative
∂_T log λ_A of size ≈ 2v_n c/(Tκ₈), not an additive kick; an entrance alone can never drive λ_A through zero. This is the
log-derivative form of "no contact jump > 0.03 digit" (P211-7D) and of the κ sawtooth (PATTERN_001). (2) Consequently a
proof along N reduces exactly to a lower bound on the total log-rate (smooth part plus entrance jumps), which is (EB_C).
Reading (1) is the first
explanation in the record of why contact entrances are invisible in log λ_A; it is ARGUED (prolate dominance and
E-image edge transfer are NUMERICAL/ARGUED, not proved).

---------------------------------------------------------------------------------------------------------------------
## Result
NO-GO with PROVED pieces, for all three designs.
- Design A (contact-entrance ledger in N): the entrance law is sign-definite and weight-generic (Prop 4.3): on even states a
  newly entered contact contributes −2h v_n F(T)² + o(h) ≤ 0, on odd states the opposite sign. Both channels of the
  bandwidth flow (domain growth between contacts, entrances at integers) are descents, so positivity cannot propagate
  through integer events; every propagation scheme reduces to a lower bound on the total descent rate, (EB_C) of P211-8C.
  NO-GO (class: positivity propagated through contact entrances along N).
- Design B (Chebyshev's two-sided floor relation at the sharp truncation): any finite family of strictly satisfied floor
  relations is satisfied by cΛ for c near 1 (Prop 2.1), hence cannot separate Λ from falsifier (a); used with zero slack it
  is R10. NO-GO (class: finitely many strict floor relations).
- Design C (prolate extremality with index-8 constraint count): a retry of L′/L′♯; fails on the gauge directions like L′.
  Not pursued (ARGUED).

### What was proved
- Prop 2.1: finitely many strict Chebyshev-type floor relations define a set of weights open in c around Λ on every bounded
  range.
- Lemma 4.1 (edge Cauchy–Schwarz for c_F near ±2T), Lemma 4.2 (first-order entrance c_F(2T − δ) = δF(T⁻)conj F(−T⁺) + o(δ),
  O(δ^{3/2}) remainder in H¹), Prop 4.3 (sign of an entrance: negative on real even states, positive on real odd states).
- Cor 4.4(i): |a_T − a_T^{∖n}| ≤ v_n × edge-strip product; (ii) the right-derivative jump of λ_A at T_n equals −2v_nF*(T_n)²,
  CONDITIONAL on (R_edge) (simple bottom, edge continuity).
- ARGUED: through Slepian's identity the entrance jump is ≈ (2v_n c/(Tκ₈))·λ_A, a jump in the log-derivative proportional to
  the margin; this explains the invisibility of contacts in log λ_A (P211-7D) and the κ sawtooth (PATTERN_001).

### What failed and why
- "Integers enter discretely while N is continuous, so positivity propagates through the entrances": the entrance term has
  a fixed sign (−) on the even bottom, for every positive weight at every position; it survives falsifiers (a) c > 0, (b),
  (c), (d), so it is not a sign step, and it points the wrong way.
- "A two-sided floor inequality is the semiring input": with slack it is open in c (Prop 2.1), so it survives (a) near
  c = 1; without slack it is the identity R10. The floor relation fixes the comb only at density level.
- "Prolate extremality as variational principle": the comparison form is L′, killed by the gauge (Ef = 0, defect > 0).

### Next concrete step
Test (R_edge) and the ARGUED entrance law numerically at three entrances (n = 7, 8, 9 at T_n = ½ log n): compute the
one-sided log-derivatives of λ_A at T_n ± 10⁻⁴ (Galerkin, N = 120, 60 digits) and compare the jump with
2v_n F*(T_n)²/λ_A and with 2v_n c/(Tκ₈). If they agree, the entrance part of the rate is closed in form, and the residual
of (EB_C) is the smooth domain-growth rate alone; record that residual (a single edge-strip energy of the bottom state on a
contact-free segment) as the only remaining object on the bandwidth axis.

## Index row and ledger line
Index (05-meta-and-planning/ROUTES-TRIED-INDEX/README.md): row P211-24A. Ledger (LEDGER.md): line C48.
