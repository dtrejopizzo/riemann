# Round 20, memo B — The radical identity of `M` as a single linear relation between the symbol and the weights

Structural and modest note. It is not a sign attempt. Notation of P47 and of round 7:
`a_T(F) = Arch(F) − Σ_n v_n c_F(log n)`, `v_n = 2Λ(n)/√n`, `c_F(u) = ∫F(t)F(t−u)dt`, `P_T = {∫F e^{±t/2} = 0}`.
`W_*`, `D^W`, `K_Pó`, `M = −K_Pó″ + ¼K_Pó`, `X_T` as in `phase-160-row-d-infinite-T/R160_M4_R1.md` and `ROUND_019_A.md` §2.

## Four-point filter

1. **Closest antecedent.** `R160_M4_R1.md` (Theorem A, Lemma 2(a): `W_*(K_Pó,·) = 0`, l.18–37, l.74, l.88–89);
   P46 §11 (Thm 11.3, Def–Thm 11.7, Thm 11.11: radical of `I_∞`); P47 `def`/`lem:ext-mob`/`thm:ext-half`/
   `prop:ext-gauge` (main.tex l.9880–9975: the gauge `𝒢_T` is radical for `𝒲`); P47 `thm:inertia-split` (l.3614–3640);
   `phase-200-sign-object/LEMMA_I3_001.md` (I.3-a: `A_RR(c) = (1−c)C`); `ROUND_019_A.md` §3, (3.1);
   master index l.3537 (canonical class K, radical `𝓝_∞`) and l.5551 (G7D-R162_2101: «near-kernel = truncated
   radical (Pólya)»).
2. **What is new.** No construction. Only: (a) the scalar identity `Arch_*(M) = Σ_n v_n c_M(log n)` written
   explicitly with its sign table; (b) the observation of which arithmetic identities enter it,
   compared with the Guo/P47 gauge.
3. **Why it does not repeat.** It does not claim to pass the filter as a construction; it is a precise pointer.
4. **Connection with global positivity.** None directly (see §4).

## §1 The identity

**Statement (CITED: R160_M4_R1 Lemma 2(a); P46 Thm 11.3, 11.11).** For `M` in `D^W`, with `A(M) = B(M) = 0`
(moments `∫M e^{±t/2}`, which vanish because `Φ_M(0) = Φ_M(1) = 0`):

    (R)   Arch_*(M) := (1/2π)∫ m(τ)|M̂(τ)|² dτ  =  Σ_{n≥2} v_n c_M(log n),

`m(τ) = Re ψ(¼ + iτ/2) − log π` (P47 eq:symbol). It is the diagonal case of `W_*(M,G) = 0 ∀G`.

**Classical reading (PROVED as a reading; unconditional).** `(R)` is Weil's explicit formula
(P46 Thm 11.3) evaluated at the autocorrelation test `M ⋆ M`, whose Mellin transform is
`Φ_M(s)Φ_M(1−s)` with `Φ_M(s) = s(1−s)ξ(s)`. `M` is the image of the Pólya kernel under the operator
`−∂² + ¼` (which in Mellin multiplies by `s(1−s)` and kills the pole and the term at `0, 1`), and `K_Pó` is the
test whose transform is the completed function itself (`Φ_{K_Pó} = ξ`, Def–Thm 11.7). The spectral side
of the formula is the sum over zeros of `Φ_M(ρ)Φ_M(1−ρ)`, and each summand is `0` by the very definition
of `ρ`: no information about their location is used. The geometric side is `(R)`.

**Which identities enter (PROVED as an inventory).** In a single line: (i) Euler product (the prime
sum with exact `Λ`, via `−ζ′/ζ`); (ii) functional equation (symmetry `ξ(s) = ξ(1−s)`, equivalent to the
theta inversion `θ(1/x) = √x θ(x)`, Poisson on `ℤ`); (iii) the archimedean factor `Γ(s/2)π^{−s/2}`
(the symbol `m`). All three enter together, on a concrete vector, because `Φ_{K_Pó} = ξ` contains
them all.

## §2 Profile of `c_M` and table (NUMERICAL)

Quadrature on `[−6,6]`, step `10^{−4}`, analytic derivatives, `n ≤ 9` in theta, parity of `M`.
`‖M‖² ≈ 97.47`.

- **Sign of `c_M(u)` (a function of the kernel only, not of the arithmetic).** `c_M(0) > 0`; zeros at
  `u ≈ 0.240` and `u ≈ 0.738`; negative on `(0.240, 0.738)`, positive for `u > 0.738` (no further sign changes
  detected up to `u = 4`, where `c_M ≈ 10^{−130}`). `log 2 = 0.693` falls in the negative window,
  `log 3 = 1.099` in the positive one. **The alternation 2 (−), 3 (+) does not continue**: all `n ≥ 3` give `+`.
- **Decay.** `c_M(log n) ≈ e^{−(2π−o(1))n}` by the inequality `e^{2t} + n²e^{−2t} ≥ 2n`
  (ROUND_019_A §2(c)); observed `c_M(log 11)/c_M(log 13) ≈ 7·10^4`.

| `n` | `c_M(log n)` | `v_n c_M(log n)` | partial sum |
|---|---|---|---|
| 2 | −9.765 | −9.572 | −9.572 |
| 3 | +6.066 | +7.695 | −1.877 |
| 4 | +0.2346 | +0.1626 | −1.715 |
| 5 | +3.7·10⁻³ | +5.3·10⁻³ | −1.7095 |
| 7 | +2.7·10⁻⁷ | +4.0·10⁻⁷ | −1.7095 |
| 8 | +1.6·10⁻⁹ | +8·10⁻¹⁰ | |
| 9 | +8.4·10⁻¹² | +6·10⁻¹² | |
| 11, 13, 16 | 10⁻¹⁶, 10⁻²¹, 10⁻²⁹ | | |

`P(M) := Σ v_n c_M(log n) ≈ −1.7095` (ROUND_019_A gave −1.698, coarser quadrature), hence by `(R)`
`Arch_*(M) ≈ −1.71 < 0`. The identity closes in three terms (2, 3, 4) to `10⁻²`; the rest is
doubly-exponentially small. The closure is a cancellation `n = 2` against `n = 3` with negative `Arch`
(consistent with F2: `Arch` has negative directions on `P_T`).

## §3 Controls

For a weight `w`, the defect at `M` is `δ(w) := Arch_*(M) − Σ w_n c_M(log n) = −Σ (w_n − v_n) c_M(log n)`
(PROVED, subtraction of `(R)`), and `a^w_T(X_T) = δ(w) + O(e^{cT}e^{−πe^{2T}})` (ROUND_019_A (3.1)).

- `cΛ`: `δ = (1−c)P(M) = (1−c)Arch_*(M)`; `c = 2`: `+1.71`. It is exactly the pattern `A_RR(c) = (1−c)C` of
  LEMMA_I3_001 I.3-a, with `C` restricted to `span{M}`.
- Delete `p^k`: `δ = v_{p^k} c_M(k log p)`: `p = 2`: `−9.57`; `p = 3`: `+7.69`; `4`: `+0.16`; any `n ≥ 3`:
  positive. Thus, among the single deletions, only that of `2` makes `X_T` a negative witness.
- Beurling (move a generator `log 2 → u`): `δ` changes by `v_2(c_M(log 2) − c_M(u))` plus the changes in
  powers/products; sign fixed by the position of `u` relative to `0.240`/`0.738`.

The step that fails is always the same: `(R)`, i.e. `M` stops being radical. The sign of the defect is fixed by
the profile of the kernel `c_M`, not by the arithmetic.

## §4 What this gives; what is known

1. **Already known (CITED).** `M` (and `K_Pó`, `K_Pó′`) in the radical of the full form: P46 Thm 11.11,
   R160_M4_R1 Theorem A/Lemma 2(a), index l.3537, l.5551. The `(1−c)` scaling of the radical block:
   LEMMA_I3_001 I.3-a. The conclusion «the closeness to zero of `X_T` is a property of the radical, not of the sign»:
   ROUND_019_A §3.
2. **`X_T` and the gauge `𝒢_T`.** `M` is **not** an element of `𝒢_T` (P47 l.9881): `𝒢_T` are functions
   supported in `[−1/λ, 1/λ]` on the multiplicative side whose transport `Φ_φ` (Mellin `ζ(s)𝓜φ(s)`)
   vanishes outside `(−∞, −T]`; their membership in the radical (Guo Lemma 4.4) uses **only** `Λ∗1 = log`
   (rem:ext-killing (ii)) and the pole, **not** the functional equation. `M` instead is divisible by `ξ`
   (R160 Theorem C: maximal rate `e^{−πe^{2|t|}}` in the ξ-divisible radical), supported on the whole line, and
   its membership in the radical uses Euler + FE + Γ together. Both are subspaces of the same radical of `𝒲`;
   they are distinct elements. (ARGUED: I did not check whether `M` is a limit of translated gauges; the difference in
   identities used suggests it is not.)
3. **Answer to the question of O3/O12.** Yes: `X_T` is, in the corpus, the only vector **inside `P_T`** on
   which Euler, FE and Γ enter a single exact identity (with error `e^{−πe^{2T}}`). (PC) of phase 161
   has them as an operator identity but without a test in the window (ROUND_002_A §(4)); the gauge `𝒢_T`
   has them in a radical without FE. This is a pointer, not an object: the identity is **scalar in one direction**.
4. **Decomposition `a_T(F) = (≥ 0) + (radical)` via the image of `M`?** No. The radical functions
   supported in the window are only near-null (the bound B(i) is positive only as an upper bound; an exact
   radical in `P_T` would give exact `a_T = 0`, excluded by P47 `cor:void`/`thm:finmod`, CITED). The «image of `M`
   restricted to the window» is, by translations and cutoffs, a family of near-radical vectors of
   effective dimension `O(T)` (106_09 Thms 2–3: near-radical matrices of cutoffs of `K, K′, K″`), not dense
   in `P_T`; the complement is all of `P_T` except those directions, and on it the form is what must be signed.
   Writing `F = (projection onto near-radical) + remainder` is the Schur decomposition of LEMMA_I3_001 /
   `thm:parityschur`: already done, without sign. I propose no construction: it does not pass the filter.

**Verdict.** Everything is already in the corpus except the table of `c_M` and the inventory «Euler + FE + Γ on a vector of
`P_T`, versus only `Λ∗1` in `𝒢_T`». Output: pointer (R160 Thm. A, P46 Thm 11.11, P47 prop:ext-gauge,
LEMMA_I3_001 I.3-a, ROUND_019_A §3). No new route; nothing to add to the index except this cross-check note.

**For independent checking.** Rederive: (a) `A(M) = B(M) = 0` from `Φ_M(0) = Φ_M(1) = 0`; (b) that `(R)` is the
explicit formula at `M ⋆ M` without polar term and without use of zero location; (c) the zeros of `c_M` at `0.240`,
`0.738` (independent quadrature); (d) claim 2 of §4 (`M ∉ 𝒢_T` and which identities each radical uses).
