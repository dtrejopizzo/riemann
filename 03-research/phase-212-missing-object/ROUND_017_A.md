# Round 17, memo A: the log 2 wall, the DIR split wall and the split of the atoms

Notation of `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §§2, 7–10 and `ROUND_015_D.md`: `q₂, q₃` DIR pieces on `P_T`,
`a = q₂ + q₃`, `L_u(F) = ∫_{J_u} F(t)F(t+u) dt` (`J_u = [−T, T−u]`), `Π_p = Σ_k v_{p^k} L_{k log p}`.
Computations of §§3–4: temporary script `r17_lattice.py` in the temporary working directory (reuses, without
modifying it, the setup of `verify_window_split_canonical.py`; Clarabel, status `optimal_inaccurate`, precision
floor `≈ 10⁻⁹`); not part of the corpus.

## 0. Four-point filter

1. **Antecedents read in primary sources.** Phase 153 `README.md`, `R153_000_BLUEPRINT.md` §§1–2, `R153_001_ROUND1.md`
   §1.2, `R153_005_CLOSING_DECISION.md`; Paper 47 `main.tex` thm:A (l. 444), cor:mono, `subsec:schur` (prop:schur,
   thm:w11), thm:index (l. 2518), thm:log5A (l. 4680); Paper 42 `main.tex` thm:certifiedendpoints (l. 4164);
   `G2_B8_R5.md` (phase 159) summary and Theorem D; in phase 212: `ROUND_006` §§4–10, `ROUND_007_A` §§1–4,
   `ROUND_013_A`, `ROUND_015_B` §4, `ROUND_015_D`, `RULES_AVOID.md` O, Q, Y, Z.
2. **What is new.** (a) Correction of premise (1) of the assignment: the corpus has no proof by mechanism
   beyond `T*`; «Theorem A» is a conjugation identity or a rewriting, and `log 2` is the point where a
   computer certificate was run (§1, reading PROVED). (b) The DIR wall is not a chain event and does not depend on the
   resolution: `T_DIR ∈ (0.696, 0.698)` on two meshes, with and without `n = 4` (§2, NUMERICAL). (c) The class «positional
   split of the atoms» (piece of a prime with arbitrary support on its lattice `ℤ log p`) reaches the ceiling
   on `0.70–0.75` with non-negative atom fractions. A single delay suffices, `log 2` or `log 3`, and `2 log 2`
   is not needed (§3, NUMERICAL). (d) Reading: that class dissolves the prime label and its bilateral version is
   trivially exact (§3, PROVED). It is not a structural law.
3. **Why it does not repeat.** (a)–(c) do not appear in the corpus. Grep for «átomo/atom» together with «pieza/split/reparto» in
   phases 159, 211 and 212 gives only lexical uses. `ROUND_006` §4.5 names the jump measure with atoms, but does not
   split it. The signed split of the smooth kernel (`ROUND_006` §7.3(iii), O3) is another freedom. But (c)
   provides no sign mechanism. It is a class enlargement confirming the J3/O3 pattern (the class certifies when the
   bottom is `≥ 0`), and is recorded as such.
4. **Link with global positivity.** None. See §5.

## 1. «Theorem A» and the log 2 wall (question 1)

**Reading (PROVED as a reading of the sources).** There are two theorems with that name and neither is a sign mechanism:

- **Phase 153, Theorem A** (`R153_001` §1.2): `A_T^{(a)} = E_{−a}A_TE_a + E_aA_TE_{−a}`, i.e.
  `⟨A_T^{(a)}F,F⟩ = 2[⟨A_Tu,u⟩ − ⟨A_Tw,w⟩]` with `u = cosh(at)F` and `w = sinh(at)F`. It is a two-line polarization
  on the form of the falsifier `Ξ_a`, and the audit itself (`R153_002` row 3) calls it that. It does not
  decompose `a_T` or give its sign. The sign at `log 2` used by phase 153 is that of **Paper 42
  thm:certifiedendpoints**: a certificate in interval arithmetic (Arb, mesh of dimension 760, directed Feshbach,
  margins `6.5·10⁻⁴` even and `1.2·10⁻⁴` odd at `½log 3`). Its blueprint (`R153_000` l. 6, 19) says so: «archimedean
  domination (Yoshida Lemma 2 quantified)».
- **Paper 47 thm:A** («the form as a Lévy energy»): `a_T(F) = C₀‖F‖² + Lev(c_F) − Σ v_n c_F(log n)`. It is the formula of
  the form, not an inequality. Positivity up to `½log 5` is thm:log5A, also by certificate (ball
  arithmetic, prop:lowercert). At `log 2`, thm:w11 gives only the value in one direction (the easy half of prop:schur).

**Consequences.**
- There is no «decomposition of `a_T` with an inequality giving the sign» to read. The exact values of `v₂, v₃` and of
  `C₀ = −γ − 3log 2 − π/2 − log π` enter only as enclosed numerical inputs. `log 2` is not the point where
  a step fails: it is one of the windows where the Paper 42 certificate was run. Choosing it is natural, because
  there the set of contacts is still `{2, 3}` and `log 4 = 2T` does not yet enter.
- The only structural fact at `log 2` is archimedean: `n_odd(Arch|P_T) = 0` for `T ≤ log 2` (thm:index(i), with
  `log 2 ≤ T*_odd`). It is a lower bound of a threshold **certified in that window**, not an event at `log 2`.
- **Theorem A does not belong to the DIR class**, because it is not a split. **`T_DIR ≥ log 2` is not proved** by anything
  in the corpus: it is NUMERICAL (`ROUND_006` §7.3 and §2 below). Fact (1) of the assignment is false as stated.
  The two walls are not «two mechanism walls 0.005 apart»: one is a certificate window and the other a numerical threshold
  of a class.

## 2. The first cross square and the chain hypothesis (question 2)

**Exact condition at `T_DIR` (ARGUED in the continuum, PROVED in Galerkin by SDP duality with Slater; combines
`ROUND_007_A` §3.1 and `ROUND_015_D` §2).** Let `τ*(T)` be the DIR value and `λ(T)/2` the ceiling. Then `T_DIR = inf{T :
τ*(T) < λ(T)/2}`, and by the dual of `ROUND_007_A` §3.1 one has `τ*(T) = λ(T)/2` as long as the infimum of the dual functional

`Φ(Y₂,Y₃) = ∫Wρ + ¼∬K[ρ(t)+ρ(s) − 2min(Y₂,Y₃)] − tr(Y₂Π₂) − tr(Y₃Π₃)`

is attained at the diagonal pair `Y₂ = Y₃ = ½ e⊗e` (`e` the bottom of `a|P_T`). `T_DIR` is the first `T` at which there exists a
pair with `Y₂ ≠ Y₃`, equal density, `tr Y₂ + tr Y₃ = 1` and `Φ < λ/2`. With complementary slackness, at that `T` a
non-diagonal dual appears with `Y₂q₂ = 0` and `Y₃q₃ = 0`, and `θ₂ = 𝟙{Y₃ > Y₂}`. By Lemma R, on the primal side this is equivalent to
`ν₋(q₂) + ν₋(q₃) = 1` in the optimal split, i.e. to `μ(T) → 0⁺` in the pencil `a w = μ q₃ w` (with
`q₃ ⪰ 0`, `μ < 0` when `q₂` has a negative eigenvalue). First-order observation (PROVED, direct computation): a
perturbation `Y₂,₃ = ½e⊗e ± Z` with `diag Z = 0` and both `⪰ 0` forces, at first order, `Z = e⊗h + h⊗e`
with `e h ≡ 0`, i.e. `Z = 0` where `e ≠ 0`. Hence the birth of the non-diagonal pair is of **second order**, and this
fits the quadratic onset `τ* ≈ −(6.7(T − 0.696))²` measured in `ROUND_015_D` §1. I do not obtain a closed form
of the condition.

**Chain hypothesis (NUMERICAL evidence against).** The chain `t, t + log 2, t + 2log 2` fits in `I_T` if and only if
`2T ≥ 2log 2`, i.e. exactly at `T = log 2`, the same event at which contact 4 enters. Data (`N, NC`; ceiling in
parentheses):

| `T` | `(30,20)` | `(40,30)` | `(30,20)` without `n = 4` |
|---|---|---|---|
| 0.694 | ceiling (`5.73·10⁻⁸`) | ceiling (`5.41·10⁻⁸`) | ceiling |
| 0.696 | ceiling (`5.00·10⁻⁸`) | ceiling (`4.59·10⁻⁸`) | ceiling |
| 0.698 | — | `−1.45·10⁻⁴` | — |
| 0.700 | `−6.91·10⁻⁴` | `−7.84·10⁻⁴` (`ROUND_006` §8.4) | `−6.9·10⁻⁴` (`ROUND_006` §7.3) |

- The wall is in `(0.696, 0.698)` on both meshes. It does not move down towards `log 2` under refinement. The delay `0.003–0.005` is
  stable and not a discretization artifact (NUMERICAL, two resolutions).
- The double chain already fits at `0.694` and `0.696`, with or without `n = 4`, and the split reaches the ceiling. Hence
  «the window contains `t, t + log 2, t + 2log 2`» is not the cause. At most it is a necessary condition with a margin
  that nothing predicts.
- What `ROUND_007_A` Thm. 2.1 refuted: the class 𝒢. These are the certificates that **bound each contact by a potential
  `V_p ≥ 0`** (Schur/ground state, with chains of any length and any `θ_p`, `W_p`), and they die at
  `T*_{∞,P} ≤ 0.60` by the archimedean index. That theorem says nothing about the cause of the DIR wall. The reading
  «`log 2` periodicity along chains» of `ROUND_007_A` §4 already noted that the central zone measures `2(T − log 2)`
  (`0.013` at `0.70`), and left it as ARGUED without an explanation of the threshold. The data above and §3 weaken it further:
  the remedy does not need the delay `2log 2` and also works with a delay of 3 alone.

## 3. Piece with arbitrary support on its lattice (question 3)

**Class.** To DIR a positional atomic transfer `X = Σ_{u∈𝒰} Σ_i g_{u,i} L_u^{(i)}` is added, where
`L_u^{(i)}(F) = ∫_{cell i ∩ J_u} F(t)F(t+u)dt`. One takes `q₂ + X` and `q₃ − X`. For `u = log 2`, piece 2 keeps
the atom `−(v₂ − g(t))` and piece 3 receives `−g(t)`. The atom fractions are non-negative if
`0 ≤ g ≤ v₂ = 0.980`. For `u = log 3`, the condition is `−v₃ ≤ g ≤ 0` with `v₃ = 1.268`. This is exactly
«the piece of each prime is any form supported on its lattice `{0, ±log p, ±2log p}`»: since `Arch` has no
atoms, whatever one piece adds at those delays the other subtracts.

**Results (NUMERICAL, `N = 30`, `NC = 20`, maximum `τ`).**

| `T` | DIR | `log 2` alone, `g ∈ [0, v₂]` | `log 2, 2log 2`, `|g| ≤ 50` | `log 3` alone, `g ∈ [−v₃, 0]` | ceiling |
|---|---|---|---|---|---|
| 0.70 | `−6.9·10⁻⁴` | `3.683·10⁻⁸` | `3.683·10⁻⁸` | `3.683·10⁻⁸` | `3.683·10⁻⁸` |
| 0.72 | `−2.6·10⁻²` | `6.460·10⁻⁹` | `6.460·10⁻⁹` | `6.460·10⁻⁹` | `6.459·10⁻⁹` |
| 0.75 | `−8.6·10⁻²` | `5.18·10⁻¹⁰` | `5.15·10⁻¹⁰` | `5.18·10⁻¹⁰` | `5.18·10⁻¹⁰` |
| 0.80 | `−1.3·10⁻¹` | `−1.6·10⁻⁹` | `4.7·10⁻¹⁰` | `1.0·10⁻⁹` | `4.6·10⁻¹²` |

At `0.80` the ceiling is below the solver floor: «compatible with the ceiling», undecided. At `T = 0.69`,
DIR and the enlarged class coincide at the ceiling.

**Shape of the `g` (NUMERICAL).**
- `log 2` alone: `g ≈ 0.57–0.73` at `0.70`, `0.74–0.83` at `0.72`, `0.78–0.91` at `0.75`, `0.78–0.93` at `0.80`.
  Piece 3 keeps **60–95 %** of the atom of 2.
- `log 3` alone: `g ≈ −0.94` to `−1.20`. Piece 2 keeps **75–95 %** of the atom of 3.

The bounds are not touched. With `|g| ≤ 50` and both delays of 2, `|g| = 18` appears at `0.70`: there is no uniqueness.

**Reading.**
- *(PROVED, trivial.)* If both lattices are allowed with fractions `≥ 0`, the split `q₂ = q₃ = a/2`
  (`θ = ½`, `W₂ = W/2`, `g_{log 2} = v₂/2`, `g_{log 4} = v₄/2`, `g_{log 3} = −v₃/2`) is admissible and reaches the ceiling
  `λ/2` for all `T`. The bilateral class is the form itself (J3).
- *(NUMERICAL.)* The unilateral version (a single lattice) is not trivial, but reaches the ceiling over the whole measurable
  range. It does so by emptying the label: the «piece of prime 3» ends up carrying most of the contact of 2
  (or vice versa).
- The extension requested by the assignment is **not** a chain of length 2 of 2. A single delay suffices, and that of `log 3`
  suffices as much as that of `log 2`. The failure of DIR comes from requiring that **each atom stay whole in a single piece**.
  As soon as an atom can be split with a positional weight, the split returns to the ceiling. The rank-one transfer
  `λℓ⊗ℓ` of `ROUND_015_D` is replaced by a transfer concentrated at the delay of a contact.

**Closed in the corpus?** Class M (`ROUND_006` §10.1), Theorem D of phase 159 and Q1 split the smooth
kernel or bound contacts by potentials. None splits the atom with a positional weight, nor does the «per-prime
positivity» of phase 6 S2.1 (one piece per prime, whole atom). What is new is only the measurement. By the previous
point, the class falls into the J3/O3 pattern: it certifies when the bottom is `≥ 0` and provides no rule. **There is no
structural law** of the type «exact as long as…». The only structural thing is the DIR boundary, «indivisible atom», and its wall
`T_DIR ≈ 0.697` has no associated arithmetic event (§2).

## 4. Up to `½log 5`

On `(0.75, 0.8047)` the ceiling (`≤ 5·10⁻¹⁰`) drops to the solver level. «Exact up to `½log 5`» is not decidable with
this tool: it is OPEN and, by §3, of no interest as a law. It was not run with three primes.

## 5. Filter applied to what survives, and Lemma T

- Only these survive: (a) the correction of the premise (reading); (b) the DIR wall, stable in `(0.696, 0.698)` and not
  caused by chains or by `n = 4` (NUMERICAL); (c) the positional split of atoms, exact as far as measurable
  (NUMERICAL) and trivial in its bilateral version (PROVED).
- **Global link, honestly.** An exact split for all `T` would be an identity «`a_T` = sum of pieces `⪰ 0`».
  But each piece `⪰ 0` is a statement of the same type as the original, without a formula of its own (J3). None of the
  measured classes gives `θ_p`, `W_p` or `g` without solving the problem.
- **Lemma T.** For a split, the step that should fail in the controls is the **existence** of the split. With
  `cΛ` (`c = 2`), with deletion of a prime power or with Beurling, the split ceases to exist only because the
  form ceases to be `⪰ 0`. `ROUND_006` §7.2 and §10.3 show that the class follows the bottom of `a_T` and not `c = 1`.
  This is exactly the automatic breaking R3-i. It is not a named step using an arithmetic relation false in the
  controls. **It is not a legitimate step for Lemma T.**

## 6. Labels

| # | Statement | Label |
|---|---|---|
| 1 | Phase 153 Thm. A = conjugation for `Ξ_a`; P47 thm:A = Lévy formula; `log 2` = certificate window (P42) | PROVED (reading) |
| 2 | No proof by mechanism beyond `T*` in the corpus; `T_DIR ≥ log 2` not proved | PROVED (reading) / NUMERICAL |
| 3 | Dual characterization of `T_DIR` (exit from the diagonal pair) | PROVED in Galerkin, ARGUED in the continuum |
| 4 | The non-diagonal pair is born at second order (`diag Z = 0` kills the first order) | PROVED (computation) |
| 5 | `T_DIR ∈ (0.696, 0.698)` on two meshes, also without `n = 4`; not a chain event | NUMERICAL |
| 6 | Positional split of one atom (`log 2` or `log 3`, fractions `≥ 0`) reaches the ceiling on `0.70–0.75` | NUMERICAL |
| 7 | Bilateral version trivially exact (`a/2`) | PROVED |
| 8 | Structural law «exact up to `½log 5`» | OPEN, of no interest by 7 |
| 9 | Existence of the split as a Lemma T step | selection NO-GO (automatic R3-i) |

**Rederive:** 4 (diagonal `Y₂ = Y₃ = ½e⊗e` with `diag Z = 0`) and 7. **Next explicit operation:** none
from the splits. The only rigid fact is that the indivisible atom stops sufficing at `≈ 0.697` and not at
`log 2`. A real candidate would have to give the `g(t)` of §3 (unilateral, `log 3`) by a formula of its own that
breaks at `c = 2`, and I do not have it.
