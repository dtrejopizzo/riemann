# Round 18, memo A: ground-state representation with sign-changing `φ` for the local split at `T ∈ (0.60, 0.69)`

Notation of `common7`: `a_T = Arch − Σ_n v_n c_F(log n)`, `Arch(F) = ∫_I W F² + ¼∬_{I×I} K(|t−s|)(F(t)−F(s))²`,
`I = [−T, T]`, `P_T = {∫F e^{±t/2} = 0}`, `e_±(t) = e^{±t/2}`. DIR split: `q_p = ∫W_pF² + ¼∬θ_pK(ΔF)² − Π_p`.

**Goal of this round, declared as LOCAL.** The assignment relaxes point (4) of the filter: the aim is the first
proof by mechanism (not by matrix certificate) of `a_T ⪰ 0` on `P_T` at some `T` above the archimedean
threshold. Nothing that follows has, or is claimed to have, any consequence for positivity at all `T`.

**Verdict.** No explicit split and no proof were obtained. The suggested mechanism (sign-changing ground
state that makes the contact square positive) has the sign the wrong way round (§2), and every ground-state
representation with all its terms manifestly `≥ 0` is impossible at any `T ∈ [0.2, 0.75]` by
a hand computation (§3). The variant that uses `P_T` through Lagrange terms fails numerically by a wide margin (§4).

## 0. Filter

**(1) Closest antecedent.** `ROUND_007_A.md` §1 Lemma 1.1 (ground-state identity per contact,
`φ > 0`) and §2 Theorem 2.1 (class 𝒢: contacts bounded by potentials `V_p ≥ 0`; NO-GO relative to P46 cor:Tarch,
`RULES_AVOID` Q1). The memo itself leaves open (§2, «What 𝒢 does not cover») the case of sign-changing `V_p`.
Also `phase-211-sign-sandbox/ROUND_005_D.md` Thm. 2.1 (global ground state `h_T`), `INV_N_001` §1 (`φ ≡ 1`),
`ROUND_017_A.md` / `RULES_AVOID` AA (wall of the per-prime split, `T_DIR ≈ 0.697`), `ROUND_006` §§7–10.
Grep for «Allegretto», «Piepenbrink», «Doob», «Perron», «estocástic» in `03-research` and the index: only
side uses (e.g. `R184_003` l. 102, parity of the ground mode); no sign-changing ground-state
representation for `a_T`.

**(2) What is new.** That `φ` changes sign, so that the induced potential `V_p` is sign-changing: this is the
gap declared open in `ROUND_007_A` §2.

**(3) Why it would avoid the antecedent.** Theorem 2.1 of `ROUND_007_A` uses only `ΣV_p ≥ 0`; with sign-changing
`φ`, `V_p` is not `≥ 0` and the argument does not apply.

**(4) Connection.** Relaxed by the assignment: local goal at a single `T`.

The result of the cross-check is that (3) does not hold (§§2–3): the sign change of `φ` does not avoid the obstacle,
it reverses it.

## 1. General ground-state identity (PROVED, elementary)

Let `Q(F) = ∫U F² − ½∬M(t,s)F(t)F(s)` with `M` a symmetric measure `≥ 0` off the diagonal (for `q_p`:
`M = θ_pK + v_n(δ_{s=t−log n} + δ_{s=t+log n})` over the contacts of `p`, plus the diagonal part absorbed into `U`).
Let `φ` be real with `φ ≠ 0` a.e. and `f = F/φ`. Then, for every `F ∈ L²(I)`,

    Q(F) = ∫ (Qφ/φ) F² + ¼∬ M(t,s) φ(t)φ(s) (f(t) − f(s))²,     Qφ := Uφ − ½Mφ.        (1.1)

*Proof.* `−½∬Mφφ f(t)f(s) = ¼∬Mφφ(f(t)−f(s))² − ½∬Mφφ f(t)²` (symmetry), and `½∬M(t,s)φ(t)φ(s)f(t)² =
∫F²·(½Mφ)/φ`. □

With `φ > 0` and `M ≥ 0` this is the Allegretto–Piepenbrink criterion; Lemma 1.1 of `ROUND_007_A` is the case of a single
contact.

## 2. Sign correction (PROVED by (1.1))

In (1.1) the coefficient of the contact square is `¼ v_n φ(t)φ(t − log n)`, **with the sign of `φφ`**. The
contact is a *positive* jump rate (`M ≥ 0`: it favours `F(t) = F(t − log n)`), not a negative one. If `φ` changes
sign between the two extreme zones `L_p`, `R_p`, the contact square gets a **negative** sign, the opposite of
what the suggested line assumed. The same happens with every pair `(t, s)` of the kernel with `θ_p > 0` and
`φ(t)φ(s) < 0`. If that square is discarded, one gets `Π_p ≥ ∫V_pF²`, a *lower* bound of the contact, which is
useless for `q_p ⪰ 0`.

## 3. Hand NO-GO for every manifest representation valid on `L²(I)` (PROVED)

**Lemma 3.1.** For `0.2 ≤ T ≤ 0.75`, `a_T(1) < 0`. Concretely

    a_T(1) ≤ ∫_I W ≤ 2T [ C_0 + 1 + log(2/T) + π/2 + T²/(72(1 − T²/12)) ],

and at `T = 0.65` the bracket is `≤ −1.67`, hence `a_T(1) ≤ −2.17`.

*Proof.* The kernel term vanishes on constants and `c_1(u) = 2T − u ≥ 0`, hence `a_T(1) ≤ ∫W`. One has
`∫_I W = 2T·C_0 + ∫_0^{2T}(π − G(u))du` and `π − G(u) = −log tanh(u/4) + 2 arctan e^{−u/2}`. Three
inequalities are used: `2 arctan e^{−u/2} ≤ π/2`; `tanh x ≥ x(1 − x²/3)` for `x ≥ 0`; and `−log(1 − y) ≤ y/(1 − y)`.
With them `π − G(u) ≤ −log(u/4) + (u²/48)/(1 − u²/48) + π/2`. Integrating:
`∫_0^{2T} −log(u/4) du = 2T(1 + log(2/T))` and `∫_0^{2T} u²/48 du ≤ (2T)³/144`, with denominator
`≥ 1 − T²/12`. For the constant: `C_0 = ψ(¼) − log π = −γ − π/2 − 3 log 2 − log π = −5.3721…` (Gauss's digamma
theorem, CITED, classical). At `T = 0.65` the summands are `−5.3721 + 2.1240 + 1.5708 + 0.0061 = −1.6712`.
For `T ∈ [0.2, 0.75]` the bracket is increasing in `T`, except for `log(2/T)`, which decreases. Hence it is convenient
to bound it at `T = 0.2`: `−5.3721 + 1 + 2.3026 + 1.5708 + 0.0006 = −0.498 < 0`. □

**Corollary 3.2.** For `T ∈ [0.2, 0.75]` there is no identity `a_T = Σ_p q_p` in which each `q_p` is
written as in (1.1), with any `φ_p` (of any sign, `≠ 0` a.e.), `θ_p ≥ 0` and `W_p`, and in which all
terms are `≥ 0`. *Proof:* (1.1) holds on all of `L²(I)`, and would give `a_T(1) ≥ 0`, contradicting Lemma 3.1. □

The same proof works for every representation «sum of squares plus potential `≥ 0`» valid on `L²(I)` without using
`P_T`. It is elementary, does not use P46 cor:Tarch and covers the sign-changing gap of `ROUND_007_A` §2 in the part where
the square is kept. It does not cover bounds `Π_p ⪯ M_{V_p}` holding **only** on `P_T`. It does not depend on the weight:
it holds equally with `c = 2`, without a prime power or with a Beurling-type weight. It is a class closure, not a
falsifier of a named step.

**Consequence.** Every local proof must use the constraints `∫F e_± = 0`, i.e. contain terms that
vanish on `P_T`, such as the Lagrange terms `2⟨F,e_±⟩⟨F,g_±⟩`, or a term that is not manifestly `≥ 0`.

## 4. Ground state after Lagrange modification (NUMERICAL)

Nyström model: `n` midpoint nodes, the contact linearly interpolated and `K` without the diagonal. This coarse
model gives a bottom `a|P_T` of `+4.8·10⁻⁸` at `T = 0.62` with `n = 160`. Its error, of order `10⁻⁶`, serves only
for orientation. Script: `scratchpad/r18.py` and `r18s.py`, temporary.

- **Perron class with Lagrange.** `Q' = a_T + e_+⊗g_+ + g_+⊗e_+ + e_−⊗g_− + g_−⊗e_−`, with free `g_±`
  (they coincide with `a_T` on `P_T`). The off-diagonal kernel is required to be `≤ 0` (Z-matrix, which admits a
  representation (1.1) with `φ > 0`) and `τ` is maximized with `Q' ⪰ τ`. Results:
  `τ = −0.28` at `T = 0.5` (`n = 100`), where `a_T ≻ 0` on `P_T` (bottom `7·10⁻⁵`), and
  `τ = −0.80` at `T = 0.62` (`n = 40, 60, 70`, stable). It fails by several orders of magnitude relative to the bottom,
  already below the threshold. Reading (ARGUED): a rank-two modification with bounded kernel does not compensate the defect
  `a_T(1)/2T ≈ −2.5` without creating positive couplings.
- **Signature gauge.** Take `σ = sign` of the bottom eigenvector of `a|P_T` and require `Q'` conjugated by
  `diag σ` to be Z. The problem is infeasible (`T = 0.62`, `n = 60`).
  **Lemma 4.1 (PROVED if `g_±` is bounded near the nodes).** If `σ` changes sign at an interior point `t_0`,
  the Z condition forces `L(t,s) ≤ −½K(|t−s|)` for the pairs `t < t_0 < s` (with `L` the Lagrange part).
  Since `K(u) ≥ 1/u`, this requires `L → −∞`, impossible for bounded `e_± g_±`. For general `g ∈ L²`: ARGUED.
- **Nodal structure** (`T = 0.62, 0.65, 0.68`). The bottom eigenvector of `a|P_T` is even, with pattern `+ − +` and
  nodes at `≈ ±0.2`. It has the **same** sign on the two extreme zones `L_3 = [−T, T − log 3]` and
  `R_3 = [−T + log 3, T]`, so the pairs of the contact of 3 have `φφ > 0`. For the contact of 2 the signs are
  mixed. The «odd across the extreme zones» shape assumed by the assignment is not observed.

## 5. What breaks, what remains, and what would be needed

- There is no formula for `θ_p`, `W_p`. `q_p ⪰ 0` was not proved at any `T`.
- The missing inequality has a precise form. Every local proof above `T*` must contain a
  non-Perron ingredient that uses `P_T`: a restricted Poincaré- or Wirtinger-type inequality,
  `¼∬K(ΔF)² + ∫W F² ≥ μ_T ‖F‖² − (terms vanishing on P_T)` with explicit `μ_T`, which the manifest part
  cannot supply (§3). An honest candidate would be that inequality with an explicit constant for the kernel `K` in
  the window, used per prime. Its relation with the P46 certificate (thm:index, cor:Tarch) is direct: P46
  obtains it by intervals. Doing it by hand was not attempted in this round.
- Controls (informative): Corollary 3.2 is blind to the weight (it holds equally at `c = 2`, with 3 deleted or with 2
  deleted), as befits a class NO-GO. The numerical part of §4 was not repeated with controls.
- What happens at `T ≈ 0.697` plays no role: the class dies earlier, at every `T ≥ 0.2`.

| # | Statement | Label |
|---|---|---|
| 1 | Identity (1.1) for `φ` of any sign | PROVED |
| 2 | The contact square carries the sign of `φ(t)φ(t−log n)`: changing sign makes it negative | PROVED |
| 3 | Lemma 3.1: `a_T(1) < 0` on `[0.2, 0.75]`, with explicit bound | PROVED (with `ψ(¼)` CITED) |
| 4 | Corollary 3.2: no manifest representation valid on `L²(I)` | PROVED |
| 5 | Perron class with Lagrange: `τ = −0.28` (0.5), `−0.80` (0.62) | NUMERICAL |
| 6 | Lemma 4.1, signature gauge with interior node | PROVED (bounded `g`); ARGUED (general) |
| 7 | Nodal structure of the bottom (even, `+ − +`, nodes `≈ ±0.2`) | NUMERICAL (coarse model) |
| 8 | Explicit split or local proof by mechanism | OPEN |
