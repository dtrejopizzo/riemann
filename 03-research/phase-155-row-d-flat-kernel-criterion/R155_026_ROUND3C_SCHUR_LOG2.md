# R155.026 — round 3c: the Schur reduction at the ground state, and a proved direction at `log 2`

*Phase 155, round 3c. Executes the the round-3c order. Inherits `R155_023` (amended)
and its audit `R155_025`, `scripts/r3a/` (Galerkin assembly of `A_∞` on `P_T` and of the prime form
`Π_T`), and Paper 46 §2 (`thm:A`, `thm:S`, `lem:K`), §4 (`lem:mbounds`), §5 (`lem:bern`, the
enclosure machinery of `thm:C`), §8. **Paper 46 is not touched; `scripts/r3a`, `scripts/r3b` and
`R155_024` are not touched.** New scripts: `scripts/r3c/`.*

**No sign for `ζ` is claimed at any `T`. Endpoint of record unchanged: `λ_min(A_{½log3}) ≥
8.8577·10⁻⁵` (Paper 46 Thm C). Galerkin values are upper bounds on infima and are `DIAGNOSTIC`;
the one rigorous statement of this note is §4's enclosure, which is about **one explicit direction**,
not about the form.**

---

## §0 Verdict

**Yes — `w₁₁ > 0` is rigorous at `T = log 2`.** For the explicit degree-17 polynomial `F*` (the
`N = 18` Galerkin ground state of `A_∞|P_T` at `T = log 2`, an archimedean object: its coefficients
do not involve the primes), a two-sided enclosure of every term of the Lévy form gives

> **`w₁₁ = W_{log2}[F*] ∈ [0.0342113430, 0.0342182500]`, width `6.91·10⁻⁶`, so `w₁₁ > 0` with a
> margin of `4950` enclosure widths.[amended per R155_028]** — this is the hardened
> interval-arithmetic enclosure of `scripts/r3c/r3c_04_enclosure_iv.py` (`18.2 s`), which supersedes
> the float enclosure `[0.0341712660, 0.0342537492]` of `r3c_02_enclosure.py` and is contained in it.

This is a `PROVED` statement about **one direction at `log 2`** (`T ≤ log 2`, so it is inside the
allowed range), not a sign claim for the form. It is the cheap half of the Schur reduction proved in
§2: `W_T ≥ 0` on `P_T` fails or succeeds according to `w₁₁ > 0` *and* `S ≥ 0` on `V = F*^⊥ ∩ P_T`,
and §5 shows that the second half is not reachable by any norm inequality — it fails by `0.06`–`0.31`
even after the primes are given away for free.

Four further readings, all `DIAGNOSTIC`:

1. `w₁₁` is positive at all four windows and **shrinks monotonically**: `0.09235` (`0.58`),
 `0.06259` (`0.62`), `0.04155` (`0.65`), `0.03421` (`log 2`) — stable to `2·10⁻³` relative between
 `N = 18` and `N = 36`. The archimedean ground state is never where the form is about to fail.
2. `λ_min(S)` and `λ_min(W_T|P_T)` have the same sign at all eight runs (both `> 0`), as §2 requires;
 the ratio `λ_min(S)/λ_min(W_T|P_T)` was reported as `6.5`, `4.2`, `3.4`, `2.7` at `N = 18` —
 *[amended per R155_036] these ratios are withdrawn: both numerator and denominator
 are unstabilised Galerkin upper bounds (`N`-inconsistency: `k = 8` at `log 2` gives `9.94e−7` at
 `N = 18` vs `3.38e−5` at `N = 36`, and the bottom itself falls `9.94e−7 → 1.05e−7`; no numerical
 value of `inf W_{log2}|P_T` is supported). The sign agreement survives.*
3. **Parity halves the problem, and this is `PROVED`.** `W_T` commutes with the reflection
 `(RF)(t) = F(−t)` on `P_T`, `F*` is even (`DIAGNOSTIC`), hence the odd part of `V` decouples
 entirely: `S|_{V_odd} = W_T|_{V_odd}` and the Schur correction lives in `V_even`. Measured:
 the cross terms `W_T(F*, ·)` against odd archimedean eigenvectors are `≤ 1.3·10⁻¹⁵`, and the
 ground state of `S` is even with `99.46 %` of its **mass** on the **third** archimedean eigenvector
 (overlap amplitude `0.9973`; `0.41 %` of the mass on the fifth) **[amended per R155_028]**
 (`λ₃ = 0.46817` at `log 2`), the first one of `F*`'s own parity. The second eigenvector
 (`λ₂ = 0.14778`) is orthogonal to the whole problem.
4. **The Schur correction is enormous**: `c²/w₁₁ = 0.711, 0.681, 0.687, 0.778` at the four windows,
 against a coupled-sector gap `λ₃ = 0.647, 0.580, 0.533, 0.468`. So even the *ideal* condition
 `λ₃ − c²/w₁₁ > 0`, in which the primes are not charged at all, **fails** by `0.064, 0.101, 0.154,
 0.310`. Positivity on `V` is a cancellation, never a margin.

---

## §1 Corpus check (grep-verified, `03-research` + `04-papers`)

| query | hits | what is already there | what is new here |
|---|---|---|---|
| `Schur` **[amended per R155_028]** | `grep -rl "Schur complement" 03-research --include=*.md` returns **177 files** (654 for `Schur`); the materially close ones are `phase-116/previous-phase-114/114_d_56_PARITY_FESHBACH_INERTIA_CERTIFICATE_AND_STRUCTURAL_NOGOS.md` (= D.56), `phase-116/previous-phase-114/114_d_49_LEVY_GROUND_STATE_JET_DEFECT.md` (= D.49), `phase-124/P124_011_SCHUR_COLLAR_REDUCTION.md`, `phase-75/P75_007_009_CUTOFF_TRANSPORT_SCHUR.md` | **D.56 is the closest prior art and was not cited in the first version of this note.** On the prolate Schur core of D.55 it already does: (1) the exact reflection splitting `E_T = E_{T,e} ⊕ E_{T,o}`, `S_T = S_{T,e} ⊕ S_{T,o}` — parity commutes with every source term and splits the Schur matrix; (2) a **Feshbach (= Schur) elimination of the high modes with interval enclosures for all Feshbach entries**, including every prime power and the full Gamma term, plus a `rank one minus positive` congruence (§5) and the inertia statements `n₊(B_T) = 1`, `In(M_T B_T^{-1} M_T^*) = (1,1,0)`. D.49 is the Lévy-coordinate ground state with the crossed polar block `⟨M_T F, C M_T F⟩` and a rank-two jet defect. `P124_011` is the Schur/Douglas complement of the **Tate collar** (the `2 × 2` `(primitive, Tate)` split), concluding that Schur equality yields no hidden first-contact law; `P75_007` is a cutoff-transport estimate | **Re-argued novelty.** *Re-application, not new:* the Schur/Feshbach congruence, the parity splitting of a Schur complement, and interval enclosures of Feshbach entries are all D.56's; Prop. 3c.1 and Cor. 3c.2 are the two-line abstract form of a move already made there (D.56 states it for a finite matrix core; 3c.1 states it for an unbounded form on a form domain, which is what `A_∞` needs — a generalisation, not a first). *New here:* (i) the **pivot** — D.56 eliminates high modes (a spectral cut-off) and `P124_011` the two Tate directions, whereas here the pivot is the single **archimedean-only, prime-independent ground state `F*` of `A_∞|P_T`** inside the already-primitive `P_T`, a `1 + (dim−1)` split along the one direction the archimedean block makes negative; no note in D.49/D.55/D.56/`P124_011` takes that decomposition. (ii) the **rigorous Lévy-side enclosure of the pivot value at `T = log 2`** (Theorem 3c.3): D.56's enclosures are a *proposed* certificate ("not claimed to have been verified for every `T`") and D.49 encloses no value of the complete form, while `w₁₁ = W_{log2}[F*]` is here enclosed two-sidedly in interval arithmetic and the enclosure is run. (iii) the **even-sector obstruction numbers** `c²/w₁₁ − λ₃ = 0.064, 0.101, 0.154, 0.310`: D.56 proves *inertia* statements about the split but never measures the size of the Schur correction against the archimedean gap. The earlier claim "no overlap" is **withdrawn**. |
| `negative eigenvalue` / `n₋` | `R155_023 §4` (Prop 3), `phase-122/P122_006` | `n₋(A_∞\|P_T) ≥ 1` past `T*_{∞,P}` `PROVED`; the count `= 1` up to `T = 0.80` `DIAGNOSTIC`; the linear growth `HEURISTIC` (E5) | the `n₋ = 1` fact is here *used* as a hypothesis and the consequence (a rank-one reduction) is extracted |
| `ground state` | 24 files; relevant: `R155_023 §3` (`F*_∞`, `F*_P` and `Π_T` on them), `phase-78/E78_1_GROUND_SIMPLICITY_AUTOPSY`, `phase-83/E83_008_GROUND_VECTOR_OBSTRUCTION` | `R155_023` evaluated `Π_T(F*_P)` and `a_T(F*_P)` at three windows (`+0.09060` at `½log3`, `+0.09235` at `0.58`, `+0.03421` at `log 2`) | those three numbers are exactly `w₁₁` — `R155_023` computed the quantity without naming it or knowing it was one half of an equivalence. Here it is named, the equivalence is proved, and the `log 2` value is **enclosed rigorously** |
| `one negative direction` | 1 hit, `R155_023 §4` ("one negative direction on `P_T` from `0.5958` to `0.80`") | the honest finite-`T` statement | promoted to the standing hypothesis `(H1)` of §2 |
| `parity` on `P_T` | `phase-88/E88_004_PARITY_SCALE_SPLIT` (parity/scale split of the endpoint pencil) | parity used on a different object | the reflection-invariance of `W_T` on `P_T` and the resulting decoupling of `S` is new in row D's Galerkin setting |

Nothing in the corpus states the reduction of §2 **at this pivot**, and nothing enclosed `w₁₁` rigorously; the general Schur/Feshbach-plus-parity machinery is D.56's and is credited as such **[amended per R155_028]**.

---

## §2 The Schur reduction

### Setting and hypotheses

`P_T = {F ∈ L²(−T,T) : A(F) = B(F) = 0}`, `A(F) = ∫Fe^{t/2}`, `B(F) = ∫Fe^{−t/2}`. On `P_T` the pole
term vanishes identically, so (Paper 46 `thm:A`)

 `A_∞[F] = (1/2π)∫ m(τ)|F̂(τ)|²dτ = C₀‖F‖² + ∫₀^∞(‖F‖² − c_F(u))K(u)du`, `Π_T[F] = −Σ_{n<e^{2T}} v_n c_F(log n)`,
 `W_T = A_∞ + Π_T` on `P_T`.

*Facts used.* (F1) `A_∞` is a closed quadratic form on `P_T`, bounded below by `C₀‖F‖²` (`m ≥ m(0) = C₀`
by `lem:mbounds`(i)) and **unbounded above** (`m(τ) ~ log τ`); let `𝒜` be the associated self-adjoint
operator with form domain `Q`. `PROVED`. (F2) `Π_T` is a **bounded** symmetric operator with
`‖Π_T‖ ≤ Σ_{n<e^{2T}} v_n = A_T` (each term is `−v_n·½(τ_{log n} + τ_{log n}^*)` compressed to
`(−T,T)`, and `τ_u` is unitary), so `A_T = 2.24883` at `log 2`. `PROVED`. (The value `‖Π_T‖ ≤ 0.9` of
`R155_023 §3` is the *Galerkin* norm and is `DIAGNOSTIC`.) Hence `W = 𝒜 + Π_T` is self-adjoint on
`D(𝒜)` with the same form domain, bounded below by `C₀ − A_T`.

> **(H1) [HYPOTHESIS, not proved].** `A_∞|P_T` has exactly one negative eigenvalue `λ₁ < 0`, it is
> simple, it is isolated below the rest of the spectrum, and `0 < λ₂ ≤ λ₃ ≤ …`. `F*` denotes its
> unit ground state, `V = F*^⊥ ∩ P_T`.
> *Status.* `DIAGNOSTIC` for `T*_{∞,P} < T ≤ 0.80` (`R155_023 §3`, Galerkin `N = 18` and, here,
> `N = 36`); `n₋ ≥ 1` is `PROVED` past the threshold (`R155_023` Prop 3(i)); `n₋ = 1` is **not**
> proved, and by `R155_023` Prop 3(ii) (upper bound `PROVED`) only `n₋ ≤ 2Tτ₀/π + O(log T) + 2` is
> available, which is `≥ 3` in this range. Everything in §2 that needs only `F* ∈ D(W)` is free of
> (H1); (H1) is what makes `F*` *the* distinguished direction and `S` a perturbation of a positive
> form.

### Proposition 3c.1 (Schur reduction). `PROVED`.

Let `w` be a real quadratic form on a form domain `Q ⊂ P_T`, `e ∈ Q` a unit vector with
`w₁₁ := w[e] ≠ 0`, `V = e^⊥`, `Q_V = Q ∩ V`, `β(G) := w(e,G)` for `G ∈ Q_V`, and define the Schur
form on `Q_V`

 `s[G] := w[G] − β(G)²/w₁₁`.

Then, for every `F = x e + G ∈ Q` (`x ∈ ℝ`, `G ∈ Q_V`),

 **(★) `w[F] = w₁₁·(x + β(G)/w₁₁)² + s[G]`.**

Consequently:
**(i)** if `w₁₁ > 0`, then `w ≥ 0` on `Q` **⟺** `s ≥ 0` on `Q_V`; and, in the coercive version,
`w ≥ c‖·‖²` on `Q` for some `c > 0` **⟹** `s ≥ c‖·‖²` on `Q_V` (put `x = −β(G)/w₁₁`, so
`s[G] = w[xe+G] ≥ c‖xe+G‖² ≥ c‖G‖²` by orthogonality). The converse **⟸** is *not* unconditional:
it requires `β` **bounded**, `|β(G)| ≤ C‖G‖`, and then `s ≥ c′‖·‖²` gives `w ≥ c‖·‖²` with
`c = c(c′, w₁₁, C) > 0`. `β` is bounded under Cor. 3c.2 (`β = ⟨b,·⟩`, `b = P_V W F* ∈ V`, which
needs `F* ∈ D(W)`) but not for a general form on `Q`; so the coercive clause is stated here as `⟹`
unconditionally, and as `⟺` only under bounded `β` **[amended per R155_028]**;
**(ii)** if `w ≥ 0` on `Q` then `w₁₁ ≥ 0`, and if moreover `w₁₁ = 0` then `β ≡ 0` and
`w ≥ 0 ⟺ w|_{Q_V} ≥ 0`.
**(iii)** In particular the equivalence stated in the order — "`W_T ≥ 0` on `P_T` ⟺ (a) `w₁₁ > 0`
and (b) `S ≥ 0`" — is correct **as a statement about strictly positive forms** and, as literally
written, needs the caveat of (ii): a form with `w₁₁ = 0` can still be `≥ 0`. We adopt (i)+(ii) as the
statement.

*Proof.* (★) is the completion of the square: `w[xe + G] = x²w₁₁ + 2xβ(G) + w[G]`, and
`x²w₁₁ + 2xβ(G) = w₁₁(x + β(G)/w₁₁)² − β(G)²/w₁₁`. No topology is used: the identity is algebraic and
holds pointwise on `Q`, which is why it needs neither boundedness nor compactness of `w`.
(i) (⟸) Both terms of (★) are `≥ 0`. (⟹) Given `G`, choose `x = −β(G)/w₁₁` (admissible, `Q` is a
vector space containing `e` and `G`): then `w[F] = s[G] ≥ 0`.
(ii) Take `G = 0`, `x = 1`. If `w₁₁ = 0` and `β(G₀) ≠ 0` for some `G₀`, then
`w[xe + G₀] = 2xβ(G₀) + w[G₀] → −∞` as `x → ∓∞`, contradicting `w ≥ 0`. ∎

### Corollary 3c.2 (operator form). `PROVED` under `F* ∈ D(W)`.

If `e = F* ∈ D(W)` — which holds under (H1), since `F* ∈ D(𝒜)` as an eigenvector of `𝒜|P_T` and
`Π_T` is bounded by (F2) — then `b := P_V W F* ∈ V` is a genuine vector, `β(G) = ⟨b,G⟩`, and the Schur
form `s` is the form of the self-adjoint operator

 `S = W|_V − (b ⊗ b)/w₁₁` (a rank-one perturbation of `W|_V`, bounded below, same form domain).

Equivalently `L W L^* = w₁₁ ⊕ S` with `L = I − (1/w₁₁)(b ⊗ F*)` bounded and boundedly invertible
(`L^{-1} = I + (1/w₁₁)(b ⊗ F*)` since `⟨b,F*⟩ = 0`), i.e. the reduction is a **congruence**, which is
why it preserves the sign of the form and not its eigenvalues. *Proof:* substitute
`β(G) = ⟨W F*, G⟩ = ⟨b, G⟩` in (★) and read off the block matrix; `L` maps `D(W)` onto itself because
`b ⊗ F*` has rank one with both vectors in `D(W)`. ∎

*Remark (what is NOT claimed).* Nothing above proves `W_T ≥ 0`. The reduction is an exact
book-keeping identity; it moves the whole difficulty into `S ≥ 0` on a codimension-one subspace, and
§5 measures how much difficulty that is.

---

## §3 The single number `w₁₁` (Galerkin, `DIAGNOSTIC`)

`scripts/r3c/r3c_01_schur.py`, runtime `99 s` (both `N` together; above the `60 s` guideline —
the `N = 36` half costs `84 s` of it, and the `N = 18` half alone runs in `15 s`).
`F*` is the ground state of `A_∞|P_T` only: **prime-independent**.

*[amended per R155_036] The `λ_min(S)` and `λ_min(W_T\|P_T)` columns are
unstabilised Rayleigh–Ritz upper bounds; no numerical value of `inf W_T\|P_T` at `log 2` is
supported (`N`-inconsistency at `log 2`, `k = 8`: `9.94e−7` at `N = 18` vs `3.38e−5` at `N = 36`;
bottom falls `9.94e−7 → 1.05e−7`).*

| `T` | `N` | `λ₁(A_∞\|P_T)` | `λ₂` | `A_∞[F*]` | `Π_T[F*]` | **`w₁₁`** | `c = ‖b‖` | `‖Π_T\|_V‖` | `λ_min(S)` | `λ_min(W_T\|P_T)` |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.58 | 18 | `+0.02739` | `+0.32698` | `+0.02739` | `+0.06496` | **`+0.092350`** | 0.2563 | 0.6901 | `+1.407e−03` | `+2.155e−04` |
| 0.58 | 36 | `+0.02734` | `+0.32694` | `+0.02734` | `+0.06504` | **`+0.092375`** | 0.2601 | 0.7840 | `+1.382e−03` | `+2.115e−04` |
| 0.62 | 18 | `−0.04043` | `+0.25996` | `−0.04043` | `+0.10302` | **`+0.062590`** | 0.2065 | 0.7656 | `+1.046e−04` | `+2.478e−05` |
| 0.62 | 36 | `−0.04047` | `+0.25992` | `−0.04047` | `+0.10308` | **`+0.062607`** | 0.2097 | 0.8911 | `+7.874e−05` | `+1.862e−05` |
| 0.65 | 18 | `−0.08859` | `+0.21245` | `−0.08859` | `+0.13014` | **`+0.041547`** | 0.1689 | 0.8471 | `+1.988e−05` | `+5.928e−06` |
| 0.65 | 36 | `−0.08864` | `+0.21241` | `−0.08864` | `+0.13036` | **`+0.041719`** | 0.1806 | 0.8968 | `+7.972e−06` | `+2.398e−06` |
| `log 2` | 18 | `−0.15428` | `+0.14778` | `−0.15428` | `+0.18849` | **`+0.034212`** | 0.1632 | 0.8593 | `+2.642e−06` | `+9.942e−07` |
| `log 2` | 36 | `−0.15432` | `+0.14774` | `−0.15432` | `+0.18847` | **`+0.034152`** | 0.1688 | 0.9005 | `+2.706e−07` | `+1.049e−07` |

Readings.
1. **`w₁₁ > 0` at all four windows**, with margins `9.2·10⁻², 6.3·10⁻², 4.2·10⁻², 3.4·10⁻²` — at the three windows where the archimedean
 form is actually negative on `F*` the primes over-cover its deficit by factors
 `2.55` (`0.62`), `1.47` (`0.65`), `1.22` (`log 2`) — the margin thins as `T` grows. `w₁₁` is **not** the small quantity: it is far above every Galerkin upper bound on
 `λ_min(W_T|P_T)` — *[amended per R155_036] no value of `inf W_T|P_T` at `log 2` is
 supported, so no numerical ratio is claimed*. The bottom of `W_T` is nowhere near `F*`.
2. `w₁₁` is stable in `N` to `2.7·10⁻⁴, 2.7·10⁻⁴, 4.1·10⁻³, 1.8·10⁻³` relative — three to four digits,
 far better than `λ_min(S)` or `λ_min(W_T)`, which are unstabilised Galerkin upper bounds that lose
 an order between `N = 18` and `N = 36` at `log 2` — *[amended per R155_036]*
 (`9.94e−7 → 1.05e−7`; these are near-zero quantities and only their **sign** is being read,
 never a numerical value).
3. `T = 0.58` is below `T*_{∞,P} ≤ 0.5958`, so there `λ₁ > 0`: **(H1) does not hold at `0.58`**, and
 the row is included only for continuity. The reduction of §2 is still valid there (it needs only
 `w₁₁ ≠ 0`), but "the one negative direction" does not exist and `F*` is merely the softest
 archimedean direction.
4. **The sign consistency test of §2 passes at all eight runs:** `sign λ_min(S) = sign
 λ_min(W_T|P_T) = +` everywhere, with `λ_min(S) > λ_min(W_T|P_T)` as the congruence allows (a
 congruence preserves signs, not values).

---

## §4 The rigorous enclosure at `T = log 2` **[amended per R155_028]**

`scripts/r3c/r3c_04_enclosure_iv.py`, runtime **`18.2 s`**. This replaces the enclosure of
`scripts/r3c/r3c_02_enclosure.py` (`9.5 s`), which remains archived but is **no longer the support
of Theorem 3c.3**: per `R155_028 §2` it was rigorous in structure but not in arithmetic — it carried
a *budget* `EPS = 1e−9` instead of directed rounding, and it recomputed the coefficient vector from
`arch_core` instead of loading the archived one the theorem names. Both defects are removed below.

**Object.** `F*` is the explicit degree-`17` polynomial `F* = Σ_{k=0}^{17} a_k φ_k` on `(−T,T)`,
`φ_k` the orthonormal Legendre basis, `a = (a_k)` the double-precision vector **archived in
`scripts/r3c/r3c_02.json`**, which the new script *loads* (it computes nothing from `arch_core`).
How `a` was obtained (a Galerkin eigenvector) is irrelevant to the statement: `a` is *given data*,
read as an exact decimal, and what is proved is a property of the resulting `F*`.

**Identity used** (Paper 46 `thm:A` + `thm:S`(iii)), exact for any `F ∈ L²(−T,T)`:

 `W_T[F] = 2A(F)B(F) + C₀c(0) + ∫₀^{2T}(c(0) − c(u))K(u)du + c(0)·∫_{2T}^∞K − Σ_{n∈N_T} v_n c(log n)`,

`c = c_F` the autocorrelation, `∫_{2T}^∞K = log coth(T/2) + π − 2arctan e^{T}`, `N_{log2} = {2,3}`
(`log 4 = 2T` is excluded and `c(2T) = 0` anyway), `v_2 = 2log2/√2`, `v_3 = 2log3/√3`.

**The arithmetic.** Everything below is `mpmath` interval arithmetic (`mp.iv`, `dps = 60`), or an
inequality proved in closed form. **There is no error budget**: the only places where a width is
introduced are the exact-decimal reading of `a`, the interval evaluation of the elementary constants,
and the two proved truncation bounds named in items 5 and 6.

1. **`c` as an exact polynomial of degree `≤ 35`, in interval coefficients.** `PROVED`. Writing
 `t = Tx`, `u = Ts`, one has `F*(Tx) = p(x)/√T` with `p(x) = Σ_k a_k √((2k+1)/2)·P_k(x)`, and
 `c(Ts) = q(s) = ∫_{−1+s}^{1}p(x)p(x−s)dx`. The script builds `q` by **exact polynomial algebra**:
 the integer coefficients of `P_k` from the three-term recurrence as `Fraction`s, the binomial
 expansion of `p(x−s)`, the `x`-convolution with `p(x)`, and term-by-term integration of `x^i`
 over `[−1+s, 1]` (another binomial expansion). No quadrature, no interpolation, no Chebyshev fit
 and no residual `assert` are involved. The construction produces coefficients up to degree `52`;
 the script checks that all of them beyond degree `35` are intervals of radius `< 10⁻³⁰`
 containing `0`, which is the machine confirmation of `deg c ≤ 2N − 1 = 35`.
2. **`g := c(0) − c ≥ 0` on `[0,2T]`.** `PROVED` by Cauchy–Schwarz (`|c(u)| ≤ c(0)`). This is what
 licenses the sandwich of item 4: an enclosure of `K` may be integrated against `g` term by term.
 (`g(0) = 0` and `g ≥ 0`; note `g′(0) = (F*(T)² + F*(−T)²)/2 > 0`, so `g` is **not** `O(u²)` — the
 `c` even / `g′(0) = 0` reading of `R155_028 §2(b)` is corrected here.)
3. **`sup_{[0,2]}|dG/ds| ≤ G₁ = 4.7518`.** `PROVED`: `G(s) = q(0) − q(s)` is converted **exactly**
 (binomial shift `s = 1 + y`, then the closed monomial-to-Chebyshev formula
 `y^m = 2^{−m}Σ_j C(m,j)T_{m−2j}`) to its Chebyshev expansion on `[0,2]`, differentiated by the
 exact Chebyshev recurrence, and bounded by `Σ|coefficients|` since `|T_k| ≤ 1`. All of this is in
 interval arithmetic.
4. **The body `[δ,2]`: an affine sandwich of `K`, no quadrature rule.** `PROVED`.
 `K_s(u) = 1/(2sinh(u/2))` is **convex** on `(0,∞)` (`(1/sinh)'' = (cosh²+1)/sinh³ > 0`), and
 `K_c(u) = 1/(2cosh(u/2))` is **concave** for `u/2 < arccosh√2 = 0.88137` (`sech'' =
 sech(1 − 2sech²)`), which covers the whole range since `2T/2 = 0.6931 < 0.88137`. Hence on each
 panel `K` is squeezed between two **affine** functions of `s` — midpoint tangent and endpoint
 chord, one way round for the convex summand and the other for the concave one — and, because
 `g ≥ 0`, the panel integral is enclosed by integrating `g` against those two affine functions.
 `∫_α^β G ds` and `∫_α^β sG ds` are then evaluated **exactly** from the interval antiderivatives of
 `q` by Horner. No derivative bound on `g` and no quadrature remainder enter the body.
 With `M = 8000` geometric panels on `[10⁻⁶, 2]` this gives
 `T·∫₀²G(s)K(Ts)ds ∈ [3.1919949327, 3.1920018397]`, width `6.9·10⁻⁶`.
5. **The singular end.** `K(u) ≤ 1/u + 1/2` (`sinh x ≥ x`; `1/(2cosh) ≤ 1/2`) and `G(s) ≤ G₁ s`
 (from `G(0) = 0` and item 3), so
 `0 ≤ T∫₀^{δ}G(s)K(Ts)ds ≤ G₁(δ + Tδ²/4)` with `δ = 10⁻⁶`: an upper contribution of `4.8·10⁻⁶`
 and a lower contribution of `0` (the integrand is `≥ 0`, so omitting `[0,δ]` from below is legal).
6. **The finite terms, all in intervals.** `c(0) = q(0)`;
 `C₀ = ψ(1/4) − logπ = −γ − 3log2 − π/2 − logπ` (the closed form of `ψ(1/4)`) `∈
 [−5.3721834192, −5.3721834192]`; `∫_{2T}^∞K = log((e^T+1)/(e^T−1)) + 2arctan(e^{−T}) ∈
 [2.0259075067, 2.0259075067]`, the `arctan` from its alternating Taylor series with the
 first-omitted-term remainder bound; the atoms `−(v_2 q(log2/T) + v_3 q(log3/T)) ∈
 [0.1884923229, 0.1884923229]` with `q` evaluated by interval Horner; and the **pole defect**
 `|2A(F*)B(F*)| ≤ 2|A||B|`, with `A` and `B` themselves enclosed by exact interval integration of
 `p` against `e^{±Tx/2}` (Taylor series with a proved factorial tail bound), giving
 `|A|,|B| ≤ 1.30·10⁻¹⁴` and `|2AB| ≤ 3.4·10⁻²⁸`. The enclosure does **not** assume `F* ∈ P_T`: it
 *pays* for the defect.

> ### Theorem 3c.3 (the archived direction `F*` is `W`-positive at `log 2`). `PROVED` (interval-arithmetic enclosure, `scripts/r3c/r3c_04_enclosure_iv.py`, `18.2 s`). **[amended per R155_028]**
> For the explicit degree-`17` polynomial `F*` on `(−log 2, log 2)` with the coefficient vector
> archived in `scripts/r3c/r3c_02.json` (unit `L²` norm, `A(F*), B(F*) = O(10⁻¹⁴)`), a two-sided
> `mpmath` interval enclosure of every term of the Lévy form gives
> **`W_{log2}[F*] ∈ [0.0342113430, 0.0342182500]`**, in particular **`W_{log2}[F*] > 0.0342`**.
> This is a statement about **one explicit direction**; it is **not** a positivity statement for
> `W_{log2}`, and it does not affect the endpoint of record `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`.
> Equivalently, in the reduction of Proposition 3c.1 at `e = F*`, hypothesis (a) `w₁₁ > 0` holds
> rigorously at `T = log 2`.

*Scope, stated plainly.* This is **one direction at `log 2`, not a sign for the form**. `F*` is
**the archived direction** — the theorem does **not** say it is "the ground state": that it is the
true archimedean ground state would need (H1) plus a Galerkin-convergence statement, neither of
which is proved. The enclosure does not improve the endpoint of record. What it does give is the
first **rigorous** positivity value of the complete Weil form at `log 2` on an explicitly named
direction chosen for archimedean reasons, and it certifies the cheap half of §2 at the window where
the Galerkin bottom is `10⁻⁷`.

*Why the enclosure is cheap and the form is not.* Width `6.91·10⁻⁶` against a value `3.4·10⁻²`: a
`4950×` margin. The same machinery at the *bottom* of `W_T` would have to resolve `10⁻⁷` — an order
below this width — and would have to do it uniformly over a whole sphere. That gap is the honest
measure of the distance between Theorem 3c.3 and a theorem about the form.

*Relation to the earlier script.* `r3c_02_enclosure.py` returned `[0.0341712660, 0.0342537492]` and
is kept for the record; the hardened interval is **contained in it** and is `12×` narrower, which is
an independent cross-check of both implementations (exact polynomial algebra + affine kernel
sandwich here, versus Gauss/Chebyshev + monotone-`K` panels there).

---

## §5 The complement: where the primes must work

`scripts/r3c/r3c_03_parity.py` (`7 s`) and `r3c_04_even_ladder.py` (`23 s`).

**(a) The crude sufficient condition fails, and not narrowly.** From Cor. 3c.2,
`S ≥ (λ₂ − ‖Π_T|_V‖ − c²/w₁₁)·I` is sufficient for `S ≥ 0`. At `N = 18`:

| `T` | `λ₂` | `‖Π_T\|_V‖` | `c²/w₁₁` | `λ₂ − ‖Π_T\|_V‖ − c²/w₁₁` | with `‖Π_T‖` (full) |
|---|---|---|---|---|---|
| 0.58 | `+0.32698` | 0.6901 | 0.7111 | **`−1.074`** | `−1.078` |
| 0.62 | `+0.25996` | 0.7656 | 0.6810 | **`−1.187`** | `−1.187` |
| 0.65 | `+0.21245` | 0.8471 | 0.6868 | **`−1.321`** | `−1.321` |
| `log 2` | `+0.14778` | 0.8593 | 0.7781 | **`−1.490`** | `−1.501` |

It fails by `1.1`–`1.5`, i.e. by `10⁵`–`10⁷` times the true `λ_min(S)`. This is the §5-of-`R155_023`
phenomenon again (the trivial bound is useless by three orders): **no inequality that separates the
archimedean block from the prime block can see the positivity.**

**(b) Parity, and the exact half that is inert.** `PROVED`: `c_F(u)` is unchanged by `F ↦ RF`,
`(RF)(t) = F(−t)`, so `A_∞` and `Π_T` are `R`-invariant; `R` swaps the constraints `A(F) = 0` and
`B(F) = 0`, so `P_T` is `R`-invariant; hence `W_T = W_T^{even} ⊕ W_T^{odd}` on `P_T`. `DIAGNOSTIC`:
`F*` is **even** at all four windows (measured parity `+1.0000`), so `V = V_even ⊕ V_odd` with
`β ≡ 0` on `V_odd` (measured: `≤ 1.3·10⁻¹⁵`), and therefore

 **`S = S_even ⊕ W_T|_{V_odd}`** — *the Schur correction touches only the even sector.*

**(c) The one direction that matters.** In the even sector the first available archimedean level is
the **third** eigenvalue `λ₃` (`λ₂` is odd). The ground state of `S` sits with `99.46 %` of its **mass** on
that third archimedean eigenvector at `log 2` (`85.43 %` at `0.58`, the rest on the fifth); the
numbers `0.9973` and `0.9243` are the overlap **amplitudes**, and the earlier printing of them as
masses is corrected here **[amended per R155_028]**. So the
sharpest crude condition is `λ₃ − ‖Π_T|_{V_even}‖ − c²/w₁₁ > 0`:

| `T` | `λ₃` | `c²/w₁₁` | `λ₃ − c²/w₁₁` (primes free) | `‖Π_T\|_{even}‖` | `λ₃ − ‖Π\|_{even}‖ − c²/w₁₁` |
|---|---|---|---|---|---|
| 0.58 | `+0.64727` | 0.7111 | **`−0.0639`** | 0.6901 | `−0.7539` |
| 0.62 | `+0.58029` | 0.6810 | **`−0.1008`** | 0.7366 | `−0.8373` |
| 0.65 | `+0.53280` | 0.6868 | **`−0.1540`** | 0.7623 | `−0.9163` |
| `log 2` | `+0.46817` | 0.7781 | **`−0.3099`** | 0.8593 | `−1.1692` |

**This is the sharp reading of round 3c.** Even if one hands the primes over for free — i.e. assumes
`Π_T|_{V_even} ≥ 0`, which is false but maximally generous — the Schur correction `c²/w₁₁` alone
already exceeds the archimedean gap `λ₃` at every window, by `0.06` at `0.58` growing to `0.31` at
`log 2`. **The coupling between the negative direction `F*` and the rest of the even sector is, by
itself, larger than the archimedean positivity available in that sector.** Positivity of `S` — hence
of `W_T` — is therefore not a competition between one negative archimedean direction and the primes:
it is a cancellation *inside `V_even`*, between the rank-one Schur term `bb^*/w₁₁` and the prime form,
in a subspace where neither alone has the right sign. The measured `λ_min(S) = 2.6·10⁻⁶` at `log 2`
is the residue of two quantities of size `0.5`–`0.8` — *[amended per R155_036] an
unstabilised Galerkin upper bound; no numerical value of `inf S` (hence of `inf W_{log2}|P_T`) is
supported, only the sign*.

**(d) Consistency.** `λ_min(S)` and `λ_min(W_T|P_T)` share their sign at all eight runs (§3), as
Proposition 3c.1 forces; their ratio `2.7`–`6.5` was read as the congruence distortion —
*[amended per R155_036] this ratio is withdrawn (unstabilised Galerkin upper bounds on
both sides); only the sign agreement is supported.* This is the numerical
check that the reduction was implemented as proved.

---

## §6 Labels

| statement | label |
|---|---|
| Prop. 3c.1 (Schur reduction (★), (i)–(iii)), incl. the caveat correcting the order's "⟺" | `PROVED` (algebraic; no boundedness needed) |
| Cor. 3c.2 (operator/congruence form, `L W L^* = w₁₁ ⊕ S`) | `PROVED` under `F* ∈ D(W)` |
| `A_∞` closed and `≥ C₀` on `P_T`; `A_∞` unbounded above | `PROVED` (Paper 46 `thm:A`, `lem:mbounds`) |
| `‖Π_T‖ ≤ A_T = 2.24883` at `log 2` | `PROVED` |
| `‖Π_T‖ ≤ 0.9` | `DIAGNOSTIC` (Galerkin, `R155_023 §3`) |
| `n₋(A_∞\|P_T) = 1` on `(T*_{∞,P}, 0.80]` — hypothesis (H1) | `HYPOTHESIS` / `DIAGNOSTIC`; only `n₋ ≥ 1` is `PROVED` (`R155_023` Prop 3(i)) |
| `F*` (Galerkin) is the true archimedean ground state | **not claimed** |
| **Theorem 3c.3: `W_{log2}[F*] ∈ [0.0342113430, 0.0342182500] > 0`** for the explicit archived direction `F*` — one direction at `log 2`, **not a sign for the form** | **`PROVED` (interval-arithmetic enclosure, `mp.iv` at `dps = 60`, no error budget; `r3c_04_enclosure_iv.py`, `18.2 s`) [amended per R155_028]** |
| the superseded float enclosure `[0.0341712660, 0.0342537492]` of `r3c_02_enclosure.py` (`EPS = 1e−9` budget) | `DIAGNOSTIC` (archived cross-check; contains the hardened interval) |
| Prop. 3c.1(i) coercive clause, unconditional direction `w ≥ c‖·‖² ⟹ s ≥ c‖·‖²` | `PROVED`; the converse `⟸` only for **bounded** `β` |
| the Schur/Feshbach congruence and its parity splitting as a *method* | prior art: `114_d_56` (D.56); new here is the pivot `F*`, the run enclosure at `log 2`, and the even-sector numbers |
| `W_T` commutes with reflection on `P_T`; `S` splits by parity | `PROVED` |
| `F*` is even; `S`'s ground state carries `99.46 %` of its **mass** on the third archimedean eigenvector (amplitude `0.9973`) | `DIAGNOSTIC` |
| the four `w₁₁` values, `λ₂`, `λ₃`, `c`, `‖Π_T\|_V‖` | `DIAGNOSTIC` (Galerkin) |
| `λ_min(S)`, `λ_min(W_T\|P_T)` | `DIAGNOSTIC` — *[amended per R155_036]* unstabilised Rayleigh–Ritz upper bounds; no numerical value of `inf W_T\|P_T` at `log 2` is supported (only the sign) |
| the crude conditions fail by `1.1`–`1.5`, and by `0.06`–`0.31` even with the primes free | `DIAGNOSTIC` (from Galerkin inputs), the *conditions themselves* `PROVED` sufficient |
| any sign for `ζ`, any change to the endpoint of record | **not claimed, unchanged** |

---

## §7 Proposal for Paper 46 (not applied; Paper 46 untouched)

1. **§8, new subsection "The reduction at the ground state".** Proposition 3c.1 + Corollary 3c.2
 verbatim: two short proofs, no new machinery, and they make precise what "one negative direction"
 costs. They also correct, in print, the naive "⟺" (case `w₁₁ = 0`).
2. **§5 or §8, a remark.** Theorem 3c.3 as a *rigorous* companion to `thm:C`: the same interval
 technology (`thm:C`'s enclosures, here in the Lévy variable rather than the Fourier variable)
 applied to a single direction at `log 2`, with the explicit `F*` in an appendix or in the
 repository. It should be stated with §4's scope paragraph attached, and labelled as a statement
 about a direction, in the wording of `R155_028 §4` ("the archived direction `F*`"). Honest value: it shows the Lévy form is a *rigorously computable* functional
 on explicit polynomials — the autocorrelation is an exact polynomial, `K` is monotone, and the
 only analytic input is `lem:K`/`thm:S`(iii). That is a reusable verification route, cheaper than
 the Fourier-side cover of `prop:TAY`.
3. **§8, one paragraph on the even-sector obstruction** (§5(c)): the statement that `c²/w₁₁` exceeds
 `λ₃` at all four two-prime windows, `DIAGNOSTIC`, as the quantitative reason why Prop. TK /
 Theorem N′ ceilings bite *on `V`* and not at `F*`. In the dual language: a certificate must
 certify `w₁₁ > 0` — one direction, now proved at `log 2`, cheap — and then `S ≥ 0` on a
 codimension-one subspace whose even half admits no norm-type bound. Every class impossibility
 proved so far (TK, N′) is an impossibility for the *second* half; none of them touches the first.

---

*Deliverables: this file; `scripts/r3c/` (`README.md`, five scripts — `r3c_04_enclosure_iv.py` is the
support of Theorem 3c.3 — `r3c_01.json`, `r3c_02.json`, `r3c_03.json`, `r3c_04.json`,
`r3c_04_enclosure_iv.json`). `scripts/r3a`, `scripts/r3b`, `R155_024` and Paper 46 untouched.*
