# Round 15 — D. Threshold of the DIR split, transfer vector and count of missing squares

Object: the per-prime two-position split (class DIR) of `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §§7–10,
with primes 2 and 3 (the term of `n = 4` goes in the piece of 2). Notation: `q₂, q₃` pieces on `P_T`
(discretized, `N = 30` modes, `NC = 20` cells unless stated), `a = q₂ + q₃`.

## 0. Four-point filter

1. **Closest antecedent, read in primary sources.** `phase-159-row-d-two-front-construction/G2_B8_R5.md` §2,
   Theorem D (Sion duality for the split with distance kernel `θ_p(u)`; dual = family of states with
   the pointwise maximum of the deficits; threshold `T_loc ≤ 0.5925`). In phase 212: `ROUND_006` §§7.3, 9, 10.2
   (DIR threshold in `(0.695, 0.70)`, obstructing pair, rank-one transfer) and `RULES_AVOID.md` O1–O4, P1, Q2.
   Phase 156 `R156_001_CONVERSE.md` Prop. 2.1 (polar capacity `2×2`): it is something else (boundary `e^{±t/2}` of
   `P_T`, not transfer between primes); not reused.
2. **New statements.** (a) Exact minimal-rank lemma for the transfer (§2, PROVED, linear algebra).
   (b) Discard of the cause «contact 4 enters» and of the law «missing squares = contacts in the window»
   (§§1, 4, NUMERICAL). (c) Characterization of the vector `ℓ` by a generalized pencil (§3, construction PROVED,
   identification with the optimum NUMERICAL).
3. **Why it does not repeat.** The dual characterization of the threshold (§1) **is a repetition**: it is Theorem D of
   phase 159 with position-dependent `θ` and free potentials; I say so and do not count it as progress. (a) and (b)
   do not appear in the corpus (grep «rango mínimo», «transferencia», «cuadrados faltantes» in 03-research and the index:
   only `ROUND_006` §10.2, which measures but has no lemma or test of the law).
4. **Connection with global positivity.** None directly. Everything in this note is blind to `Λ` (the lemma of §2
   holds for any pair of forms with sum `≻ 0`; with `cΛ`, `c = 2`, the sum stops being `≻ 0` and the lemma does not
   apply, which is the automatic breaking of R3-i, not a breaking of the sign). It is a diagnostic of the DIR class, not a
   sign mechanism. It does not pass the gate as a construction; it is delivered as an assigned identification task.

## 1. The threshold (task 1)

**Characterization (repetition of Theorem D, PROVED in the discretization by conic duality with Slater; ARGUED in
the continuum by the same Sion argument).** `T_DIR = sup{T : Ψ_T ≥ 0}`, with

`Ψ_T = inf { −tr(σ₂Π₂) − tr(σ₃Π₃) + ∫W ρ + ¼∬ K(|t−s|) max(E_{σ₂}, E_{σ₃})(t,s) }`,

infimum over pairs of states `σ₂, σ₃ ⪰ 0` on `P_T`, `tr σ₂ + tr σ₃ = 1`, **with equal pointwise density**
`ρ_{σ₂} = ρ_{σ₃} = ρ` (the freedom of `W_p(t)` forces the equality), `E_σ(t,s)` the pair energy and `Π_p` the
contact part of the prime `p` (`Π₂` includes `v₄ c_F(log 4)`). The pointwise maximum is complementary slackness:
`θ₂ = 1` where `E_{σ₂} > E_{σ₃}`. This is the exact equation requested («`Ψ_T = 0`»); it has no closed form in `T`
and I do not obtain it.

**The threshold is not the entry of contact 4 (NUMERICAL, existing and new data).**
- Control already recorded (`ROUND_006` §7.3 (ii)): deleting the term of `n = 4`, at `T = 0.70` the form remains
  positive and the split still fails (`−6.9·10⁻⁴` versus `−6.9·10⁻⁴` with the term). The piece of 2 does not
  fail because it has to absorb `−v₄ c_F(log 4)`.
- New: `T = 0.697` has zero transfer (nuclear norm `6.6·10⁻¹⁴`, the split exists).
- Onset: nuclear norm `0.0214, 0.121, 0.239` at `0.70, 0.71, 0.72`, approximately linear, vanishing by
  extrapolation at `≈ 0.698`; the primal deficit `−6.9·10⁻⁴, −8.1·10⁻³, −2.6·10⁻²` fits
  `−(6.7(T − 0.696))²` (quadratic onset). Hence `T_DIR ∈ (0.697, 0.699)`, delay `≈ 0.004–0.006` past
  `log 2`, with no associated geometric event (`2T_DIR ≈ 1.396`, it is not `log` of a simple rational with contacts
  ≤ 4; I do not identify it). Honest reading: close coincidence, not cause. Single resolution at `0.697`.

## 2. Minimal-rank lemma (PROVED)

**Lemma R.** Let `q₂, q₃` be real symmetric with `a = q₂ + q₃ ≻ 0`. Then

`min { rank X : q₂ + X ⪰ 0, q₃ − X ⪰ 0 } = ν₋(q₂) + ν₋(q₃)`,

and the minimum is attained with `X = X₊ − X₋`, `X₊ ⪰ 0` of rank `ν₋(q₂)`, `X₋ ⪰ 0` of rank `ν₋(q₃)`.

*Proof.* Let `B = a^{−1/2} q₂ a^{−1/2}`; then `a^{−1/2} q₃ a^{−1/2} = I − B` and, by Sylvester,
`ν₋(B) = ν₋(q₂)`, `ν₋(I − B) = ν₋(q₃)`. With `Y = a^{−1/2} X a^{−1/2}` (same rank) the conditions are
`0 ⪯ B + Y ⪯ I`. *Lower bound:* `B + Y₊ ⪰ B + Y ⪰ 0`, and adding a form `⪰ 0` of rank `r` lowers the number of
negative eigenvalues by at most `r` (Weyl interlacing); hence `rank Y₊ ≥ ν₋(B)`; likewise,
`I − B + Y₋ ⪰ 0` gives `rank Y₋ ≥ ν₋(I − B)`; and `rank Y = rank Y₊ + rank Y₋`. *Attainment:* in the eigenbasis of
`B` (eigenvalues `β_i`) take `y_i = −β_i` if `β_i < 0`, `y_i = 1 − β_i` if `β_i > 1`, `0` otherwise. ∎

**Corollary (rank one, PROVED).** If `q₃ ≻ 0` and `q₂` has a single negative eigenvalue, a transfer
`X = λ ℓℓᵀ` exists if and only if `ℓᵀ(q₂⁻¹ + q₃⁻¹)ℓ ≤ 0` (with `q₂` invertible), and `q₂⁻¹ + q₃⁻¹ = q₂⁻¹ a q₃⁻¹`
has exactly one negative eigenvalue. *Proof.* By Schur, `q₂ + λℓℓᵀ ⪰ 0 ⇔ λ ≥ −1/(ℓᵀq₂⁻¹ℓ)` with
`ℓᵀq₂⁻¹ℓ < 0`, and `q₃ − λℓℓᵀ ⪰ 0 ⇔ λ ≤ 1/(ℓᵀq₃⁻¹ℓ)`; compatible if and only if the sum is `≤ 0`. Inertia:
`q₃^{1/2}(q₂⁻¹ + q₃⁻¹)q₃^{1/2} = (C − I)⁻¹ + I`, `C = q₃^{−1/2} a q₃^{−1/2} ≻ 0`; the single eigenvalue
`c − 1 ∈ (−1, 0)` gives `1/(c − 1) + 1 < 0`. ∎

**Consequence.** «Number of missing squares» has an exact definition:
`n_miss(T) = min_{(θ,W) ∈ DIR} [ν₋(q₂) + ν₋(q₃)]`. The nuclear norm of `ROUND_006` §10.2 gives only upper
bounds on `n_miss`; `n_miss ≥ 1` for `T > T_DIR` by definition of the threshold.

## 3. The vector `ℓ` (task 2)

- **Construction (PROVED, from Lemma R):** with `q₃ ≻ 0`, `ν₋(q₂) = 1`, the direction `ℓ = q₃w ∝ a w`, `w` the
  lowest generalized vector of the pencil `a w = μ q₃ w` (`μ < 1`), gives an admissible transfer.
- **Identification (NUMERICAL,** with the stored optimal pieces, shifted `+2·10⁻⁶` by the solver floor):
  overlap of `ℓ` (nuclear optimum) with `a w`: `0.9979, 0.99994, 0.99998` at `T = 0.70, 0.71, 0.72`; with the
  negative vector of `q₂⁻¹ + q₃⁻¹`: equal to four digits; with the negative eigenvector of `q₂`: `0.925–0.935`.
  `μ = 4.9·10⁻⁴, 8.9·10⁻⁵, 4.7·10⁻⁵`. The two characterizations are not algebraically identical; they coincide because of
  the ill-conditioning of `q₃` (eigenvalue floor).
- **Closed forms:** projection of `cos(2πt/log 2)`: `0.911, 0.919, 0.922`; adding `cos(4πt/log 2)` or
  `cos(2πt/log 3)` does not improve (`≤ 0.927`); `cos(2πt/log(3/2))` rises to `0.95–0.96`, and four cosines to `0.98–0.99`
  (expected gain from degrees of freedom). **There is no closed formula**; the exact characterization available is
  that of the pencil `(a, q₃)`, which depends on the optimal split, not on an arithmetic datum. OPEN.

## 4. Meaning and the counting law (task 3)

**Exact statement (PROVED in the discretization, given the numerical split):** for `T ∈ [0.70, 0.72]`,
`a_T = (q₂ + λℓ⊗ℓ) + (q₃ − λℓ⊗ℓ)`, both `⪰ 0`; the cross term is a single square `λ⟨ℓ,F⟩²` that passes
from the piece of 3 to that of 2. I find no arithmetic expression of `ℓ` via `log 3 − log 2 = log(3/2)` or `2 log 2 − log 3 = log 4 − log 3 = log(4/3)`:
the only signal is the `0.95` with `cos(2πt/log(3/2))`, insufficient.

**Count (NUMERICAL, `N = 30`, `NC = 20`; from `0.73` status `optimal_inaccurate`):**

| `T` | eigenvalues of `X` (modulus) | rank (upper bound on `n_miss`) |
|---|---|---|
| 0.697 | `< 10⁻¹³` | 0 |
| 0.70–0.72 | one positive | 1 |
| 0.73 | `0.327, 0.027` | 2 |
| 0.74 | `0.387, 0.061` | 2 |
| 0.75 | `0.449, 0.084` | 2 |
| 0.77 | `+0.448, +0.140, −0.093, −0.003` | ≤ 4 (a negative part appears: the piece of 3 also demands) |
| 0.80 | `+0.567, +0.228, −0.069, −0.048` | ≤ 4 |

The second square is born at `≈ 0.722` (linear extrapolation of the second eigenvalue). Between `0.70` and `0.80` the
set of contacts is fixed (`2, 3, 4`; 5 enters at `½ log 5 = 0.8047`, and there the code switches to three primes and
the `transfer`/`dual` modes do not run; `½ log 6` is not reachable either, and the bottom of `a_T` is already at `10⁻¹²`).
**The law «missing squares = contacts (or near-coincidences) in the window» is refuted in this class**:
the count grows 0 → 1 → 2 → (≤4) without any contact entering. `T ≈ 0.722 ≈ ½ log(3√2)` is numerology without
mechanism; I do not propose it. Control: without the term of `n = 4` at `0.72` the program is infeasible (the form is already
negative, `−1.55·10⁻³`), consistent with `ROUND_006` §7.3.

## 5. Labels and what must be redone in an independent check

- PROVED: Lemma R and its corollary (§2); construction of `ℓ` via the pencil (§3).
- Declared repetition: dual characterization of the threshold = Theorem D of `G2_B8_R5.md` with `θ(t,s)`, `W_p(t)`.
- NUMERICAL: `T_DIR ∈ (0.697, 0.699)`; not caused by contact 4; `n_miss = 1` on `[0.70, 0.72]`; second
  square at `≈ 0.722`; refutation of the counting law; absence of a closed form for `ℓ`.
- Rederive: the lower bound of Lemma R (interlacing) and the inertia of the corollary.
- Next concrete operation: compute `n_miss(T)` as an invariant (minimize `ν₋(q₂)+ν₋(q₃)` over DIR, not the
  nuclear norm) and check whether it is monotone in `T`; if it is, `T ↦ n_miss(T)` is the staircase that a class with
  coupling between primes must pay with exactly that number of cross squares. No connection with the
  global sign is established.

Scripts: `r15_ell.py` and logs `r15_tr_*.log` in the temporary directory; they are not part of the corpus.
