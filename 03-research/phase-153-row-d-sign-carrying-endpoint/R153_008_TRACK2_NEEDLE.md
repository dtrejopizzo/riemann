# R153.008 — Track 2 (P153.4): the `b`-needle at `T = log 2`

* Track 2.
(`track2_needle.py`, `q1b_precision.py`, `q1c_tip.py`, `q1d_branch.py`, `q2_tscan.py`, `q2b_cross.py`),
reusing the mesh-free spectral assembly of `scripts/audit/aud_spectral.py` verbatim (`basis_hat`, `moments`).*

## 0. Corpus check (run before building)

`grep -rIn "needle" 03-research 04-papers` → only phase 153 (`R153_001/002/003/005/006`) and Paper 47's
Part III review (unrelated sense); `grep -rIn "unique contact\|contact uniqueness\|b = log 3"` → only
`R153_001:193,291,307`, `R153_005:21,51,34`, `R153_006`, and `scripts/r153_q2b_shift_scan.py:20` (a print label).
**No prior file states, proves or disproves anything about the position of the maximum of `b ↦ λ_min(b)`.**
The corpus's only assertions are round 1's "sharp isolated maximum at `b = log 3` (argmax within `3·10⁻⁴`)"
(`DIAGNOSTIC-NUMERIC`, round-1 resolution) and the audit's downgrade to "peak `+1.08·10⁻⁷`, half-width `O(10⁻⁷)`".
Both are superseded below.

## 1. Object, normalisation, precision

`T = log 2`, `I_T = (−T,T)`, `P_T = ker M_− ∩ ker M_+` (Paper 42 `main.tex:4078–4087`,
`M_∓F = ∫F e^{∓t/2}`), `w_n = Λ(n)n^{−1/2}`, `m_0 = log π + γ + π/2 + 3log 2` (`main.tex:4119`), and

  `A_T(b) := G_{Γ,T} − m_0 − w_2(S_{log2}+S_{−log2}) − w_3(S_b+S_{−b})`,  `b ∈ (log 2, 2T)`,

`A_T(log 3) = A_T` of `main.tex:eq:localizedprimitiveoperator` at `T = log 2`. In Fourier,

  `⟨A_T(b)F,F⟩ = (1/2π)∫_ℝ [Re ψ(¼+iτ/2) − log π − 2w_2 cos(τ log2) − 2w_3 cos(τ b)] |F̂(τ)|² dτ`
      `= ⟨(G_{Γ,T}−m_0)F,F⟩ − 2w_2 c_F(log 2) − 2w_3 c_F(b)`,  `c_F(b) := ∫F(t)F(t+b)dt`.   (1.1)

`λ_min(b) := min{⟨A_T(b)F,F⟩/‖F‖²_{L²} : F ∈ P_T}` (L² Rayleigh normalisation, as in the audit).

**Precision of record.** Galerkin in the sine basis `sin(kπ(t+T)/2T)`, `k ≤ K`, with the two moment
constraints imposed exactly (`scipy.linalg.null_space`); the `τ`-integral on 400 graded Legendre panels to
`τ_max = 4000`. Reported eigenvalues are therefore **upper bounds** for the true `λ_min` (Rayleigh–Ritz on a
subspace of `P_T`), and they decrease monotonically in `K`. Quadrature sensitivity at `b = log 3`, `K = 160`:
`τ_max = 2000/4000/8000 → 1.06735/1.06754/1.06757 ·10⁻⁷`; `npan 400→600 → 1.06754083·10⁻⁷`;
`ng 24→32 → 1.06754018·10⁻⁷`. **Absolute numerical noise ≈ 1·10⁻¹¹** (independently visible as the residual
`1.0·10⁻¹¹` gap at the exact crossing of §3). Every number below is ≥ `10⁻⁸`, i.e. carries ≥ 3 significant digits.
Basis refinement at `b = log 3`: `K = 100/160/240/320 → 1.0993/1.0675/1.0438/1.0307 ·10⁻⁷`; a `1/K` Richardson
extrapolation gives `λ_min(A_{log2}|P_T) ≈ 9.9·10⁻⁸`, consistent with the audit's `1.08·10⁻⁷` and above Paper 42's
certified margin `8.63386·10⁻⁸`. Everything in §§2–4 is `DIAGNOSTIC-NUMERIC` unless labelled otherwise.

## 2. Question (1): the analytic explanation

### 2.1 Two exact structural facts (`PROVED`, elementary; no corpus hit)

**(a) Parity splits the problem.** Let `(RF)(t) = F(−t)`. `G_{Γ,T}` is a Fourier multiplier in `τ` with even
symbol, `S_b + S_{−b}` commutes with `R`, and `R` exchanges `M_+` and `M_−`, so `R P_T = P_T`. Hence
`A_T(b) = A_T^{ev} ⊕ A_T^{odd}` and

  `λ_min(b) = min{ λ_e(b), λ_o(b) }`,  `λ_e, λ_o` the ground eigenvalues of the two blocks.   (2.1)

(This is the same even/odd split Paper 42's certificate uses: `main.tex` reports separate even and odd margins.)

**(b) The `b`-derivative is an autocorrelation (Hellmann–Feynman / Danskin).** By (1.1), for fixed `F` the map
`b ↦ ⟨A_T(b)F,F⟩` is real-analytic with derivative `−2w_3 c'_F(b)`. If the ground eigenvalue of a block is simple
with normalised eigenvector `F_b`, then

  `dλ/db = −2 w_3 c'_{F_b}(b)`.    (2.2)

**Verification of (2.2) (numerical, 3 digits).** At `T = log2, K = 160`: the ground state of the even block at
`b = log3 − 10⁻⁵` has `c'_{F}(b) = −0.207381`, giving `dλ_e/db = +0.263077`; the measured one-sided slope of
`λ_min` there is `+0.2782/+0.2619` (left/right difference quotients, `h = 10⁻⁵`). The ground state of the odd
block at `b = log3 + 10⁻⁵` has `c'_F(b) = +0.460108`, giving `dλ_o/db = −0.583678`; the measured slope on that
side is `−0.5831`. Agreement to 3 digits confirms (2.2) as the operative identity.

### 2.2 Why there is a peak, and why it is thin

(2.2) says the two branches move in `b` at **O(1)** speed, set by the derivative of the near-minimiser's
autocorrelation at the contact — not by anything small. The scan shows they move in *opposite* directions:
`λ_e` increases (`+0.263`), `λ_o` decreases (`−0.584`). By (2.1) their crossing is a genuine **corner of
`λ_min`**, and it is a local maximum. Measured branch data at `T = log2, K = 160` (script `q1d_branch.py`),
`b* = 1.0986265908`:

| `b − b*` | `λ₁` | `λ₂` | gap | overlap of `F₁` with previous `F₁` |
|---|---|---|---|---|
| `−10⁻⁶` | `3.554053e−6` | `4.384233e−6` | `8.30e−7` | `0.999984` |
| `−10⁻⁸` | `3.798767e−6` | `3.807051e−6` | `8.28e−9` | `1.000000` |
| `0` | `3.801220e−6` | `3.801231e−6` | `1.03e−11` | `0.000036` |
| `+10⁻⁸` | `3.795390e−6` | `3.803694e−6` | `8.30e−9` | `1.000000` |
| `+10⁻⁶` | `3.218148e−6` | `4.046709e−6` | `8.29e−7` | `1.000000` |

The gap closes **linearly** to numerical zero and the ground vector rotates by 90° across `b*`: an exact crossing
of the two symmetry blocks, not an avoided crossing. `λ_min` is therefore piecewise-analytic with a true corner:

  `λ_min(b) ≈ λ_max − 0.263·(b*−b)₊ − 0.584·(b−b*)₊`,  `λ_max = λ_min(b*)`.   (2.3)

**So the "needle" is a level-set artefact, not a resonance.** The peak has ordinary `O(1)` one-sided slopes; the
*positivity set* `N = {b : λ_min(b) > 0}` is thin only because the tip barely clears zero:
`|N| ≈ λ_max(1/0.263 + 1/0.584)`. With `λ_max = 3.64·10⁻⁶` (K = 320) this gives `|N| ≈ 2.0·10⁻⁵`.
Nothing is sharply peaked; the form is merely near-critical. The round-1 "half-width `2·10⁻³`" and the audit's
"half-width `O(10⁻⁷)`" are both wrong: the first is mesh resolution, the second used the far-field slope
(`≈1.36`, valid at `|b−log3| ≈ 10⁻³`) together with the *value at `log 3`* rather than the value at the tip.

### 2.3 The autocorrelation of the near-minimiser (the question as asked)

Is `c_{F_min}(b)` locally minimal at `log 3`? **No.** For the ground state `F` of `A_{log2}(log 3)`
(`K = 100/160/240`, stable to 3 digits): `c_F(log 2) = +0.0748`, `c_F(log 3) = +0.01176`, and `c_F` is smooth,
positive and strictly decreasing through `log 3` with `c'_F(log 3) ≈ −0.26`; its only minimum on `(log2, 2T)`
is the trivial one at `b = 2T` where `c_F ≡ 0` by support. So the blueprint's guessed mechanism ("the
near-minimiser's autocorrelation has a local minimum exactly at `log 3`") is **refuted**. The correct mechanism
is (2.1)+(2.2): *two* near-minimisers, of opposite parity, with autocorrelation derivatives of opposite sign at
the contact; the peak is where they exchange. (At the tip itself the binding vector has `c_{F}(b*) = −0.0500`:
the tip state is one whose autocorrelation at the contact is *negative*, so the prime-3 term `−2w_3 c_F` is a
*gain* of `+0.063` there.)

### 2.4 The positivity interval at `T = log 2`

From `λ_e(log3) = 1.044·10⁻⁷`, `λ_o(log3) = 1.178·10⁻⁵` (K = 240) and the slopes of (2.3):

  `N(log 2) ≈ ( log 3 − 4.0·10⁻⁷ , log 3 + 2.0·10⁻⁵ )`,  `b* = log 3 + 1.39·10⁻⁵`.   (2.4)

`log 3` lies inside `N`, but at **2 % of its length from the left endpoint**, and the tip is `1.4·10⁻⁵` to its
right with `λ_min(b*) = 3.70·10⁻⁶`, i.e. **35× larger than `λ_min(log 3)`**. `K`-refinement
(`K = 100/160/240/320`): `b*−log3 = 1.488/1.430/1.390/1.367 ·10⁻⁵`, `λ_max = 3.944/3.801/3.702/3.644 ·10⁻⁶`;
`1/K`-extrapolated `b*−log3 ≈ 1.30·10⁻⁵`, `λ_max ≈ 3.47·10⁻⁶`. The displacement is ~10⁶ times the numerical
noise: **`argmax_b λ_min(b) ≠ log 3`, decisively.**

## 3. Question (2): the `T`-scan — `log 3` or `f(T)`?

Same weights `w_2, w_3`, parity-resolved, `K = 100/160/240` (script `q2_tscan.py`; the model omits `n = 4`,
which the true Weil form acquires at `T > log 2` — see §5).

| `T` | `b*(T) − log 3` (K = 100 / 160 / 240) | `λ_min(b*)` (K=240) | `λ_e(log3)` | `λ_o(log3)` |
|---|---|---|---|---|
| 0.66 | `+1.193 / +1.149 / +1.121 ·10⁻⁴` | `+2.460e−5` | `+1.258e−6` | `+9.826e−5` |
| 0.68 | `+3.279 / +3.181 / +3.119 ·10⁻⁵` | `+7.771e−6` | `+3.282e−7` | `+2.690e−5` |
| `log 2` | `+1.488 / +1.430 / +1.390 ·10⁻⁵` | `+3.702e−6` | `+1.044e−7` | `+1.178e−5` |
| 0.70 | `+7.150 / +6.329 / +5.789 ·10⁻⁶` | `+1.636e−6` | `+7.579e−8` | `+4.848e−6` |
| 0.72 | (tip below 0; min is odd throughout) | `−1.005e−2` | `−5.630e−8` | `−1.259e−2` |

`b*(T)` is a **continuous, strictly decreasing function of `T`** with `K`-variation below 7 %, far smaller than
the factor-20 variation over `T ∈ [0.66, 0.70]`. Refining (K = 160, `q2b_cross.py`):

| `T` | 0.700 | 0.702 | 0.704 | 0.706 | 0.710 | 0.714 |
|---|---|---|---|---|---|---|
| `b*−log3` | `+6.33e−6` | `+3.34e−6` | `−4.78e−7` | `−5.83e−6` | `−3.14e−5` | (tip gone) |
| `λ_min(b*)` | `+1.78e−6` | `+9.85e−7` | `−5.71e−8` | `−1.58e−6` | `−9.75e−6` | `−1.57e−4` |

So `b*(T)` **sweeps through `log 3` at `T_c ≈ 0.7036`** and keeps going; `log 3` is not a fixed point of the tip.
At that same `T_c` the tip height crosses zero, so `N(T) = ∅` for `T > T_c ≈ 0.7037`: the failure is in the
**odd** block (`λ_o(log3)` changes sign at `T ≈ 0.7038`, while `λ_e(log3)` is still `+7.5·10⁻⁸` there and only
turns negative near `T ≈ 0.717`).

**Verdict: the needle follows `T`, not `log 3`.** The position of the tip is analytic (the even/odd crossing of a
one-parameter family); the arithmetic number `log 3` enters the problem only through the *weight* `w_3 = Λ(3)/√3`,
which fixes the branch slopes, not the location of the crossing. That `b*(log 2) − log 3 = 1.3·10⁻⁵` is a
near-coincidence, and `log 3 ∈ N(log 2)` is exactly (and only) Paper 42's `thm:certifiedendpoints` at `T = log 2`.

## 4. Question (3): theorem candidate

> **Candidate (P153.4′).** `OPEN` (statement), with the arithmetic reading `WITHDRAWN`.
> For `T ∈ (0, T_c]` put `N(T) = {b ∈ (log 2, 2T) : A_T(b) ≥ 0 on P_T}`. Then (i) `A_T(b)` splits by
> parity and `λ_min = min(λ_e, λ_o)`; (ii) on a neighbourhood of `log 3`, `λ_e` is strictly increasing and `λ_o`
> strictly decreasing in `b`, with `dλ/db = −2w_3 c'_{F_b}(b)`; hence (iii) `N(T)` is a single non-degenerate
> interval `(β_e(T), β_o(T))` whose endpoints are the unique zeros of the two branches, with
> `|N(T)| → 0` as `T ↑ T_c ≈ 0.7037`; and (iv) `N(log 2) ⊂ (log3 − 5·10⁻⁷, log3 + 2.1·10⁻⁵)`,
> so `log 3` lies in `N(log 2)` within `4·10⁻⁷` of its left endpoint.
>
> **What a proof would need.** (i) is proved above (two lines). (ii) needs: simplicity of the two block ground
> eigenvalues on the relevant `b`-interval (a certified spectral-gap bound — the observed gaps are `≥ 8·10⁻⁶`
> to the *second* eigenvalue within a block, comfortable), plus a **sign statement for the ground-state
> autocorrelation derivative**: `c'_{F_b}(b) < 0` for the even ground state and `> 0` for the odd one,
> uniformly on the interval. This is the only genuinely new analytic input; it asks for pointwise control of
> `F_b` (e.g. an ODE/resolvent representation of the even and odd ground states of `G_{Γ,T} − m_0 − w_2(·)`
> perturbed by `w_3`), which the corpus does not have. (iii) follows from (i)+(ii) by the intermediate value
> theorem. (iv) requires certified two-sided enclosures of `λ_e(log3), λ_o(log3)` **and** of the two slopes —
> Paper 42 certifies only the one-sided bound `λ_min(log 3) > 8.63·10⁻⁸`; the interval-arithmetic work for the
> slopes (i.e. for `c'` of the certified near-ground-states) has not been done.
>
> **What must NOT be attempted.** Any statement of the form "`b = log 3` is the unique / the optimal contact at
> `T = log 2`" is **false**: §3 exhibits `b ≠ log 3` with `λ_min(b) = 35 λ_min(log 3)`, and §3 exhibits a `T`
> at which `b* = log 3` exactly, with no arithmetic meaning. Round 1's item "is `argmax_b λ_min(b) = log 3`
> exactly?" (`R153_001:307`) is answered **no**.

## 5. Verdict table

| # | Statement | Label |
|---|---|---|
| 1 | `A_T(b)` commutes with `t ↦ −t`; `λ_min = min(λ_e, λ_o)` (`P_T` is reflection-invariant) | `PROVED` (elementary, new to corpus) |
| 2 | `dλ/db = −2w_3 c'_{F_b}(b)` for a simple block ground eigenvalue (Hellmann–Feynman); verified to 3 digits | `PROVED` (standard) |
| 3 | The peak of `λ_min(b)` is an **exact even/odd eigenvalue crossing** (gap `1.0·10⁻¹¹` at `b*`, linear closure, eigenvector rotation by 90°), with one-sided slopes `+0.263 / −0.584` | `DIAGNOSTIC-NUMERIC` |
| 4 | The "needle width `10⁻⁷`" is a level-set artefact of near-criticality, not a resonance: `|N(log2)| ≈ 2.0·10⁻⁵` | `DIAGNOSTIC-NUMERIC`; audit item #13's width **WITHDRAWN** |
| 5 | `argmax_b λ_min(b) = log 3 + 1.30·10⁻⁵ ≠ log 3`; `λ_min(b*) = 3.5·10⁻⁶ = 35·λ_min(log3)` | `DIAGNOSTIC-NUMERIC`; R153_001 §Q2(ii) and R153_005's "the critical point sits at the arithmetic contact" **WITHDRAWN** |
| 6 | `λ_min(A_{log2}|P_T) ≈ 9.9·10⁻⁸` (`1/K` extrapolated from `1.0993/1.0675/1.0438/1.0307·10⁻⁷`), above Paper 42's certified `8.63386·10⁻⁸` | `DIAGNOSTIC-NUMERIC` (confirms audit) |
| 7 | `b*(T)` strictly decreasing, sweeping through `log 3` at `T_c ≈ 0.7036`; needle dies at `T ≈ 0.7037`, first in the **odd** block | `DIAGNOSTIC-NUMERIC` |
| 8 | **The needle follows `T`, not `log 3`** | `DIAGNOSTIC-NUMERIC` (verdict of Track 2 (2)) |
| 9 | Candidate (P153.4′) as stated in §4 | `OPEN` |
| 10 | "`b = log 3` is the unique contact making the two-prime form non-negative at `T = log 2`" | **`WITHDRAWN` (refuted)** |

**FATAL rule.** No zero-free region, no moment bound, no cancellation imported from known theorems; the outcome
is deflationary (it removes an arithmetic reading rather than adding one), so there is nothing to presume in
error. No sign is claimed for `ζ` at any `T > log 2`. Caveat on §3: for `T > log 2` the model keeps only the
contacts `{log 2, b}` and omits `n = 4` (`Λ(4) = log 2`, active once `2T > log 4`); the true Weil form there is
*more* negative, so `T_c ≈ 0.704` is an **upper** bound for any real extension of positivity and carries no
claim about `ζ`.

## 6. Consequence for the programme (one paragraph)

`R153_005` §2.4 read the needle as: "positivity at `log 2` is exactly critical *and the critical point sits at
the arithmetic contact*; whatever extends positivity past `log 2` must be arithmetic." The first half survives
and is sharpened (`λ_min ≈ 9.9·10⁻⁸`, and the positivity window in the contact position has length `2·10⁻⁵`,
with `log 3` only `4·10⁻⁷` from its edge — the endpoint is critical to five significant figures). **The second
half does not survive.** The critical point is at `log 3 + 1.3·10⁻⁵`, it moves smoothly with `T`, and it passes
through `log 3` at an arithmetically meaningless `T ≈ 0.7036`. The correct reading is the parity one: at `T =
log 2` the even and odd blocks of the two-prime form are within `10⁻⁵` of a crossing, the even block is the one
holding positivity by `10⁻⁷`, and the odd block is the one that fails first as `T` grows. Any attempt at
`(P153.3)` (positivity to `½ log 5`) should therefore be organised by parity block, and should expect the
obstruction in the odd block — a concrete redirection that `R153_005`'s reading would have sent the wrong way.
