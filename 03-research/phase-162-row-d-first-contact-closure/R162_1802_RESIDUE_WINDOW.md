# R162_1802 — The residue window as an object: extremal and dual forms, the one-pole hyperplane, a residue-free criterion, falsifiers

Pure mathematics, no numerics run.
Inputs: R162_1701 Thm 7, R162_902 (Thm 2.1, §3), R162_703, R162_590, Paper 47 (eq:W, line 126 primitive Weil criterion,
thm:parityschur (o),(a3), lem:monoT), R160_M4_R1 Thm B(i).

Conventions: W_T = 𝔞_T + 2AB (Paper 47 eq:W), with A(F) = Φ_F(1) = ∫F e^{t/2} and B(F) = Φ_F(0) = ∫F e^{−t/2}.
For F = F_e + F_o, A = ℓ_ev(F_e) + ℓ_odd(F_o) and B = ℓ_ev(F_e) − ℓ_odd(F_o).
W^κ := 𝔞_T + 2κAB, where κ is the residue and the prime weights are held fixed.
𝔞̃_par(T) := inf{𝔞_T(F) : F ∈ D_T^par, ℓ_par(F) = 1} ∈ [−∞, ∞). On {λ_A > 0} this is 𝔞_par (703/1701).

**Status.**
- §1 Extremal and dual forms of κ_±, extended to all T: **PROVED**.
- §2 Theorem H (the one-pole hyperplane: the window width is the residue-free Weil form on {Φ_H(0) = 0}): **PROVED**.
- §3 Theorem R (residue-free criterion: RH ⟺ for every T some residue works): **PROVED**. It is sandwiched between the
  primitive and the full Weil criterion, so it is RH-equivalent and not new as a statement of RH.
- §3 Theorem Q (quantitative transfer: a nonempty window at scale S gives near-positivity at all T ≤ S, up to an error
  that is doubly exponentially small in S): **PROVED**, conditional only on the constant in R160_M4_R1 B(i).
- §4 Lemma D (derivative transfer: the odd sector is the even sector with multiplier z²): **PROVED**.
- §4 An exact identity making "κ₋ ≤ 1 ⇒ κ₊ ≥ 1" automatic at fixed T: **NO-GO** (Prop 4.2).
- §5 Which side is easy: **PARTIAL**.
- §6 Falsifiers: the lines are stated, one prediction is declared, nothing was run.

E1 verdict: every per-T statement here that implies W_T ≥ 0 is E1. What is genuinely new is **structural**: the residue
can be removed from the problem (§§2–3), at the price of passing to the T → ∞ limit.
No sign is claimed. No label moves. Gate 1 stays OPEN.

## 1. κ_± as extremal problems, with dual forms — PROVED

**Definition (valid for all T).**
- κ₋(T) := −𝔞̃_ev(T)/2.
- κ₊(T) := 𝔞̃_odd(T)/2.
- The window is K(T) := [κ₋(T), κ₊(T)]. It is empty when either infimum is −∞.

**Prop 1.1.**
- (i) Monotonicity: κ₋ is nondecreasing and κ₊ is nonincreasing, for all T. The proof is extension by zero, as in
  lem:monoT; it needs no WP hypothesis.
- (ii) If λ_A(T) > 0, then W^κ_T ⪰ 0 ⟺ κ ∈ K(T).
- (iii) Identity with the complete form at κ = 1: κ₋ = 1 − g̃_ev/2 and κ₊ = 1 + g̃_odd/2. In other words,
  K(T) = 1 + [−g̃_ev/2, g̃_odd/2].
- (iv) Primal (test-function) bounds. Any single test gives a one-sided bound:
  - for even F with ℓ_ev(F) = 1: κ₋(T) ≥ −𝔞_T(F)/2;
  - for odd G with ℓ_odd(G) = 1: κ₊(T) ≤ 𝔞_T(G)/2.
  So window *exits* are certified by one test each. Deletion's exit at 0.4608 is certified this way.
- (v) Dual (certificate) forms, by the exact S-lemma for a single linear constraint:
  - κ₊(T) = ½ sup{t : 𝔞_T^odd − t·ℓ_odd⊗ℓ_odd ⪰ 0};
  - κ₋(T) = ½ inf{s : 𝔞_T^ev + s·ℓ_ev⊗ℓ_ev ⪰ 0}.
  Window *membership* κ₋ ≤ 1 ≤ κ₊ is certified by a PSD decomposition. These are the Paper 47 flat-top / PD
  certificates with the pole weight 2 read as a variable.
- (vi) Resolvent form. When λ_par > 0 and A^par is invertible: κ₊ = 1/(2f_odd(0;T)) and κ₋ = −1/(2f_ev(0;T)).
  Here f_par(0) = ⟨(A^par)⁻¹φ_par, φ_par⟩ is the Schur formula for the minimum under one linear constraint.
- (vii) If λ_A(T) < 0 in the sector par, then 𝔞̃_par = −∞ and K(T) = ∅.
  - Proof: take G ∈ P_T^par with 𝔞(G) < 0 and a fixed H₀ with ℓ(H₀) = 1. Then 𝔞(H₀ + xG) → −∞.

*Proof.*
- (ii) and (vi): thm:parityschur (a3) and (o).
- (iii): W = 𝔞 + 2ε_parℓ² on each sector.
- (v): for one constraint, min{𝔞(F) : ℓ(F) = 1} = sup{t : 𝔞 − tℓ² ⪰ 0}. For ⇐, if 𝔞 − tℓ² ⪰ 0, evaluate on ℓ = 1. For ⇒,
  use (a1): 𝔞(G + xh) = 𝔞(G) + 𝔞(h)x² with 𝔞|Q ⪰ 0.
- (vii): as shown. ∎

## 2. The one-pole hyperplane — PROVED

**Theorem H.** For every T,

  2(κ₊(T) − κ₋(T)) = 𝔞̃_ev(T) + 𝔞̃_odd(T) = inf{ W^κ_T(H) : H ∈ D_T, Φ_H(0) = 0, Φ_H(1) = 2 },

and the right-hand side is **the same for every κ**. On {B = 0} the pole term 2κAB is absent, so there W^κ = 𝔞_T.

*Proof.*
- B(H) = 0 ⟺ ℓ_ev(H_e) = ℓ_odd(H_o) =: c, and then A(H) = 2c. So A = 2 means c = 1.
- The form is 𝔞(H) = 𝔞(H_e) + 𝔞(H_o), because the parities are orthogonal for 𝔞 (thm:parityschur(o)).
- The two constraints decouple, and the infimum is 𝔞̃_ev + 𝔞̃_odd. ∎

**Reading.**
- The window is nonempty, i.e. *some* residue is compatible with the prime data up to e^{2T}, exactly when the Weil form
  is nonnegative on tests whose Mellin transform vanishes at s = 0 (one pole only).
- The reflection R, F(t) ↦ F(−t), swaps A and B (Paper 47 l.2613). So {Φ_H(1) = 0} gives the same number.
- This yields a per-scale hierarchy. With E_prim(T) := [λ_A(T) ≥ 0], E_half(T) := [𝔞_T ≥ 0 on {B = 0}] and
  E_full(T) := [W_T ≥ 0]:

  E_full(T) ⇒ E_half(T) ⇒ E_prim(T),

  and
  - E_half(T) ⟺ E_prim(T) ∧ K(T) ≠ ∅;
  - E_full(T) ⟺ 1 ∈ K(T).
- The residue κ = 1 is the extra datum that separates E_full from E_half.

## 3. Removing the residue: Theorems R and Q

**Theorem R (residue-free criterion) — PROVED.**
RH ⟺ K(T) ≠ ∅ for all T ⟺ for every T there is some residue κ(T) with W^{κ(T)}_T ⪰ 0 on the primitive-positive
range (equivalently, E_half(T) for all T).

*Proof.*
- ⇒: under RH, 1 ∈ K(T).
- ⇐, first route: E_half(T) ⇒ E_prim(T) for all T, and that is RH by the primitive Weil criterion (Paper 47 l.126).
- ⇐, second route, which shows where the residue comes from:
  - The windows are nonempty and nested (Prop 1.1(i)). So L₋ := sup κ₋ ≤ inf κ₊ =: L₊.
  - 902 Thm 2.1 says lim g̃_par ≤ 0 unconditionally. By Prop 1.1(iii) this gives L₊ ≤ 1 ≤ L₋.
  - Hence L₋ = L₊ = 1, so 1 ∈ K(T) for all T, i.e. W_T ⪰ 0 for all T. ∎

**What Theorem R buys, and what it does not.**
- It answers task (2) in the only exact form we found. The "1" side of the window does not have to be proved. PNT
  supplies it in the limit, and it does so from the direction that 1701 called "wrong". PNT pins L₊ ≤ 1 ≤ L₋. That is
  useless alone, but combined with nonemptiness it closes the sandwich.
- The residue therefore drops out: what remains is 𝔞̃_ev + 𝔞̃_odd ≥ 0 at every scale, a κ-free inequality that mixes the
  two parities.
- It does **not** reduce the arithmetic. Via the first route, Theorem R is a formal corollary of the primitive
  criterion. E_half is squeezed between E_prim and E_full. **E1 for the family; per T it is weaker than E_full.**
- The first route shows the reduction is not an independent weakening of RH. The second route shows the mechanism: the
  Euler product fixes the residue *only through the T = ∞ limit* (zero-free on Re s = 1).

**Theorem Q (finite-scale transfer) — PROVED given R160_M4_R1 B(i).**
Let ε(S) := C e^{cS} e^{−2π e^{2S}} be the unconditional bound g̃_par(S) ≤ ε(S). If K(S) ≠ ∅, then for every T ≤ S:

  g̃_ev(T) ≥ −2ε(S) and g̃_odd(T) ≥ −2ε(S),

i.e. λ-positivity of the complete form on the Tate slices holds up to a doubly exponentially small defect.

*Proof.*
- κ₋(T) ≤ κ₋(S) ≤ κ₊(S) = 1 + g̃_odd(S)/2 ≤ 1 + ε(S)/2.
- The same chain for κ₊ from below.
- Translate using Prop 1.1(iii). ∎

- Consequence: certifying *nonemptiness* at a large scale S certifies the complete form at every smaller scale, up to
  ε(S), without ever using the value of the residue.
- The residue enters only through the constant in ε(S), i.e. through PNT on Re s = 1.
- This is the one genuinely finite-T gain of the window picture. It does not give strict positivity; closing the ε(S)
  gap requires a margin, which is E1.
- Honesty note: B(i) is quoted from R160_M4_R1. Its constant C and its range of validity in S have not been rechecked
  here. Without B(i), the elementary 902 §2 argument gives only ε(S) → 0 with no rate.

## 4. Parity duality — Lemma D PROVED, per-T identity NO-GO

**Lemma D (derivative transfer).**
- The map D : F ↦ F′ is a bijection from even F ∈ H¹₀(I_T) onto odd G ∈ D_T. Its inverse is F(t) = ∫_{−T}^t G; this
  lies in H¹₀ because ∫G = 0 for odd G.
- ℓ_odd(F′) = −½ ℓ_ev(F).
- On the zero side (convention Φ_F(½ + iz) = F̂(z)), Ĝ(z)Ĝ(−z) = z²F̂(z)F̂(−z). At the pole, z = −i/2 and z² = −¼, which
  reproduces the pole term −2ℓ_odd².
- Hence

  κ₊(T) − 1 = ½ inf{ W_T(F′) : F even, ℓ_ev(F) = 2 },
  1 − κ₋(T) = ½ inf{ W_T(F) : F even, ℓ_ev(F) = 1 }.

- In zero terms, both window conditions live on the same even space:
  - κ₋ ≤ 1 ⟺ Σ_ρ F̂(z_ρ)² ≥ 0;
  - κ₊ ≥ 1 ⟺ Σ_ρ z_ρ² F̂(z_ρ)² ≥ 0.

*Proof.*
- Integrate by parts; the boundary terms vanish on H¹₀.
- The explicit formula is linear in Φ_FΦ_F(1−·). ∎

**Reading.** Take an off-line quadruple z₀ = γ + iy. Its contribution is 4Re F̂(z₀)² to the even side and
4Re(z₀²F̂(z₀)²) to the odd side. The two differ by the phase rotation 2 arg z₀ ≈ 2y/γ.
- So the two sides of the window detect the *same* zeros, with phases that become asymptotically equal for high zeros.
- This is the closest thing to a κ₋/κ₊ duality that exists. It is a statement about zeros, so it is not a proof tool
  (E1).

**Prop 4.2 (NO-GO for an automatic implication).** No identity valid on the structural class (a ≥ 0 combs with pole,
fixed archimedean part) can force "κ₋(T) ≤ 1 ⇒ κ₊(T) ≥ 1" at fixed T. The reason is as follows.
- Any such identity is a relation Ψ(𝔞̃_ev, 𝔞̃_odd) that holds for all admissible a. The candidates are
  κ₊ + κ₋ ≥ 2 (i.e. g̃_odd ≥ g̃_ev) and κ₊κ₋ ≥ 1.
- The residue-free content of the window is only Δ = κ₊ − κ₋ (Theorem H). Its *position* relative to 1 is fixed only by
  the T = ∞ limit (Theorem R, second route).
- Deletion a = Λ1_{n≥5} has the same pole and the same limit law (902 §5), and κ₊^del(T) < 1 on [0.4608, 0.58]
  (cor:convfail).
- Deletion therefore violates the implication at such T as soon as κ₋^del(T) ≤ 1 there.
  - For T < ½log2, deletion's comb and ζ's comb coincide (both empty), so deletion's window equals ζ's, which contains 1
    (Theorem A at log 2). κ₋^del is nondecreasing.
  - Whether κ₋^del ≤ 1 still holds at 0.4608 is **not proved**. The change Σ_{n≤4} v_n c_F(log n) has no fixed sign on
    the even minimiser.
  - Status: **PARTIAL**, with a one-test certificate declared (§6).
- Independently of deletion, the functional equation has already been used up by the parity split. What is left relates
  z-multipliers (Lemma D), not window endpoints.

## 5. Which side is easy for small T — PARTIAL

- T → 0. Both sectors are archimedean. The normalised energy diverges like log(1/T), because the pole-normalised test
  must concentrate. So κ₋ → −∞ and κ₊ → +∞ (sketch; the constants have not been written out).
- Comb effect, from 1701 §3. For pole-normalised tests that are increasing on (0,T), the odd comb **adds** energy and
  pushes κ₊ up (primes help). The even comb subtracts energy for positive-autocorrelation tests and pushes κ₋ up toward 1
  (primes hurt).
  - Odd side κ₊ ≥ 1 = "enough primes": a Chebyshev *lower* bound. This is the side that deletion breaks, the fragile side
    at small T.
  - Even side κ₋ ≤ 1 = "not too many primes": a Chebyshev *upper* bound. It is robust at small T, since explicit upper
    bounds such as ψ(x) ≤ 1.04x are available. The Perron alignment makes 𝔞_ev ≈ −2 only asymptotically
    (902 §2, 1701 Prop 5).
- Asymptotically the roles swap. PNT forces L₋ ≥ 1 ≥ L₊ (Theorem R), so both endpoints converge onto 1 from the "failing"
  side. In the limit each side is exactly as hard as the other (Lemma D phase coupling).
- Up to ½log5 both endpoints are certified (703 Thm 3.1). By Theorem Q, a certificate of *nonemptiness* only would
  already have given both, up to ε(½log5). That ε is not small (e^{2S} = 5), so there Theorem Q is weaker than the
  existing certificates.

## 6. Falsifier lines

- **Deletion Λ1_{n≥5}.**
  - Theorem R applies to deletion verbatim: pole, limit law, monotonicity.
  - Since κ₊^del(0.5) < 1 − m for some m > 0, **the window of deletion must become empty at a finite scale**, namely at
    the latest at the first S with ε_del(S) < m.
  - Declared prediction (not run): the emptying scale T_e^del, and whether it occurs before or after n = 5 enters at
    ½log5.
  - Declared certificate: one even test at T ∈ [0.4608, 0.58] with 𝔞^del(F) ≥ −2 would give κ₋^del ≤ 1 there and settle
    Prop 4.2 unconditionally.
- **κ = 1 ± δ models (ζ's primes, residue κ).**
  - They have the *same* window K(T), because 𝔞 does not depend on κ.
  - Theorem R's condition K ≠ ∅ does not see κ, so these models do not falsify it. They fail W^κ ⪰ 0 only because κ ∉ K
    at large T. That is consistent: the identification of the residue uses PNT for the *true* pairing of primes and pole.
  - Lesson: any proof of nonemptiness is automatically κ-blind. That is good, but it moves all the difficulty into Δ ≥ 0.
- **Diamond–Montgomery–Vorhauer Beurling systems** (N(x) = ρx + O(x^θ), off-line zeros).
  - Nested windows, Theorem H and Theorem R (second route, via their own zero-free region on Re s = 1) all hold.
  - Their windows must therefore empty at a finite scale.
  - So a proof of Δ(T) ≥ 0 for all T cannot use only the Chebyshev asymptotics with power error. Integrality must enter,
    exactly as in 1701 §4.
- **DH (no Euler product).** 902 §2 breaks at |y| < ½, so the second route of Theorem R is unavailable. The first route
  is still formal. There is no contradiction.

## 7. For R162_590 and the README

- New object: the residue window K(T) = 1 + [−g̃_ev/2, g̃_odd/2]. Width 2Δ = 𝔞̃_ev + 𝔞̃_odd = inf of 𝔞 on the one-pole
  hyperplane {Φ(0) = 0, Φ(1) = 2}, independent of κ (Theorem H).
- Theorem R: RH ⟺ K(T) ≠ ∅ for all T. PNT supplies the "1" from the wrong side. It is formally a corollary of the
  primitive criterion, so E1 for the family.
- Theorem Q: nonemptiness at S gives g̃_par(T) ≥ −2ε(S) for all T ≤ S (doubly exponential; B(i) constant to be
  rechecked).
- Lemma D: the odd side is the even side with multiplier z². There is no per-T implication κ₋ ≤ 1 ⇒ κ₊ ≥ 1 (Prop 4.2,
  PARTIAL via deletion).
- Open:
  - (O1802.1) κ₋^del ≤ 1 on [0.4608, 0.58] (one test);
  - (O1802.2) the emptying scale of deletion's window;
  - (O1802.3) a proof of Δ(T) ≥ 0 that uses integrality. This is not E1-free, since the family is RH.
