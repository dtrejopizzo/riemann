# R155.016 — The comb-vanishing LP: `E_at(w) = 0` on a computable interval

*Phase 155, round 2. Executes `R155_013 §8(1)` ("Add the comb conditions to the
LP … the successor of (P3)") under Corollary D.2. Inherits `R155_013` (Theorem D, Cor. D.2),
`R155_011`/`R155_012` (class, scripts, corrected Bernstein pad), Paper 46 §5 (`lem:bern`),
§7 (Thm Z (7.2), `lem:smooth`).*

**No sign is claimed for `ζ` at any `T`. The endpoint of record is unchanged:
`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Paper 46 Thm C). Every number below is `DIAGNOSTIC`
(double precision, no interval arithmetic); scripts in `scripts/reverse/comb/`.**

---

## §0 Verdict in five lines

1. **Certificate on `ℝ` obtained: NO, at no `T`.** The comb-vanishing LP is **negative at all four
 windows**: `−1.166·10⁻²` (`½log3`), `−1.704·10⁻²` (`0.58`), `−5.193·10⁻²` (`0.62`),
 `−8.907·10⁻²` (`log 2`), best class (`M = 48`, `U = 6`, `β` free); certified grid values
 `−1.35·10⁻²…−9.16·10⁻²`, prime side confirming each argmin to `1.3·10⁻⁵…6.3·10⁻⁵`.
2. **But the interval is now honest and finite**: `τ_stop = 135.6, 182.9, 168.8, 183.1` from
 Theorem D applied to the *resulting* `w`, the LP was solved on `[0,200] ⊃ [0,τ_stop]`, and the
 Theorem-D tail bound at `τ = 200` is `L_w(200) = +1.498, +0.270, +0.467, +0.258 > 0`. This is the
 **first flat-top run in the corpus whose failure is a statement about all of `ℝ`**, not about a
 window chosen for convenience — **[amended per R155_019]** conditional on the
 `D(w)` quadrature (see §3 notes): at `0.58` and `log 2` the margin `L_w(200)` survives only a
 `≈ 29 %` underestimate of `D`.
3. **The comb equalities are always feasible** (least-squares residual `0.0` at every `(T,U,M)` up
 to `U = 8`, `450` equalities against `147` dof): they are not `450` independent conditions but a
 rank-deficient system whose null space is what the LP optimises over.
4. **New structural fact — the null space saturates.** `dim null` is `41` at `M=24` for every
 `U ≥ 5`, and `126` at `M=48` for every `U ≥ 6`: **comb-vanishing ⟹ effectively bounded support,
 `U_eff ≈ log(1/h) + const`.** Enlarging the support past `U_eff` adds equalities and no freedom.
5. **Diagnosis: both constraints bind, the comb more.** Same class, same interval `[0,115]`,
 `M = 24`: comb `−2.304·10⁻²` against no-comb `−8.590·10⁻³` (factor `2.7`); and the no-comb value
 on `[0,115]` is itself `3.0×` worse than the `R155_011` no-comb value on `[0,60]` (`−2.86·10⁻³`).
 Refining the lattice `M: 24 → 48` recovers half the comb penalty (`−2.30·10⁻² → −1.17·10⁻²`).

---

## §1 Corpus check (grep-verified)

| query | where it occurs | what it is | relation to comb-vanishing |
|---|---|---|---|
| `prime-free window` | `phase-115/115_10_LITERATURE_STATE_OF_THE_WINDOW.md`, `phase-115/scripts/115_08_prime_free_window_crosscheck.py`, `phase-118/PHASE_118_CLOSURE.md`, `THE_BACKWARD_MAP.md` | Connes–Consani's regime `supp(g*g^∨) ⊂ (½,2)`, i.e. `T < ½log2`: **no prime power lies inside the support at all**, so the prime term `K(f,f)` is *identically zero* and the explicit formula reduces to `Σ|ĝ(γ)|² = −G_∞`. Verified end-to-end in `115_08`. | **Complementary, not the same.** The prime-free window kills the comb by *shrinking the support below `log 2`*; there is then no arithmetic content and no endpoint past `log 2` (the phase-115/118 no-go). Comb-vanishing **keeps** every prime power inside `[−2T,2T]` (that is where `A_T` and the whole value live) and only forces `w` to vanish at the prime powers **outside** the window. It is the prime-free condition applied to the *complement* of the flat top, not to the whole support. |
| `Yoshida` | Paper 46 `main.tex:137,241,244,276,2020`; `phase-154/R154_013:10,20`; `phase-155/R155_001:46`; `phase-114/114_d_58…` | Yoshida 1992: strict positivity of the Hermitian form at autocorrelation support `log 2`, plus a qualitative small-window constant (Lemma 2) and a high-Fourier-complement constant (Lemma 3). `R154_013` records that the 1992 volume is **not** in `00-references` and the statements come from secondary reports. | Yoshida's `a₀` is again a *support-shrinking* statement (positivity for all sufficiently small windows), the archetype of the prime-free mechanism. Comb-vanishing is a **support-shaping** statement at fixed, large window: it does not shrink `2T` and does not make the form positive — §3 shows it makes the LP value strictly worse. Nothing in Yoshida bears on the tail: his lemmas are about the window, Theorem D/Cor. D.2 about `τ → ∞`. |
| `w(log n)=0`, `comb vanishing`, `comb-vanishing` | **only** `R155_013 §3` (Cor. D.2) and `R155_013 §8(1)` | the corollary this note executes | **No prior LP in the corpus imposes it.** `R155_005`'s `r2_d_subcomb.py` (phase-155 round 2) restricts a *sub-comb* of the lattice mass but never zeroes the weight at prime powers. |

**Conclusion of the corpus check.** The idea is new inside the corpus and is *not* the classical
prime-free window: it is its outside-the-window dual, and it exists only because Theorem D turned
the tail from `e^{E_at}` into `D^{1/2}`.

---

## §2 The LP

### 2.1 The class (and why `R155_011`'s could not be reused)

Cor. D.2 requires `supp w ⊂ [−U,U]` — otherwise `E_at(w) = Σ_{log n > 2T} v_n|w(log n)|` is an
infinite sum and "the comb equalities" is not a finite set of linear conditions. The `R155_011`
edge columns `ψ_s(v) = (1+sv+½s²v²)e^{−sv}` have infinite support, so **the whole basis had to be
rebuilt**. `comblib.WinC`:

```
w(u) = 1 |u| ≤ 2T
w(u) = B(u) + Σ_{j=2}^{J} x_j β((u−u_j)/h) u > 2T, u_j = 2T + jh, h = 2T/M
B(u) = β((u−u_{−1})/h) + β((u−u_0)/h) + β((u−u_1)/h)
```

with `β` the cardinal cubic B-spline. The three unit coefficients in `B` are **forced, and are the
unique solution**, of the `C²` matching at the window edge: from `β(0)=⅔`, `β(±1)=⅙`,
`β'(±1)=∓½`, `β''(0)=−2`, `β''(±1)=1`,

```
g(2T)=1, g'(2T)=0, g''(2T)=0 ⟺ x_{−1}=x_1, x_1=x_0, x_0=1.
```

Hence `w` is even, globally `C²` (in particular across `±2T`, which `R155_013 §1.1` shows is exactly
what makes `ν̂_w + 2ĝ₀` decay like `τ^{−2}`), and `supp w ⊂ [−U,U]` with `U = 2T + (J+2)h`. This is
a *strictly cleaner* class than `R155_011`'s: no exponential tail to truncate, `E_at` a finite sum.

**[amended per R155_019]** The free splines of the ansatz start at `j = 2`, and
`β(±2) = β'(±2) = β''(±2) = 0` for the cardinal cubic B-spline, so they do not disturb the `C²`
matching computed above: the three forced unit coefficients are the unique solution regardless of
how many free `j ≥ 2` splines are added. The three-term ansatz for `B(u)` is not a restriction.

### 2.2 The equalities, and their exact elimination

`A x = b`, `A_{n j} = β((log n − u_j)/h)`, `b_n = −B(log n)`, over the prime powers with
`2T < log n ≤ U`. `count.py` reports, for **every** `(T, U, M)` tried, least-squares residual
`‖Ax_p − b‖_∞ = 0.0` (to `3·10⁻¹⁹`): the system is **always solvable**, even with `450` equalities
against `147` unknowns. The reason is structural: `b ≠ 0` only at the `2–3` prime powers inside
`[2T, 2T+3h]` where `B` is supported, so the system is homogeneous almost everywhere, and `A` is a
banded collocation matrix whose rank is limited by the clustering of the `log n`. The LP therefore
optimises over the affine set `x = x_p + N z`, `N = null(A)`, which `lp.py` computes by SVD.

### 2.3 Saturation of the null space — comb-vanishing ⟹ effectively bounded support

`count.py`, `T = ½log3` (`U_true` in brackets):

| `M` | `U` | `m` (equalities) | dof `= J−1` | rank | **nullity** |
|---|---|---|---|---|---|
| 24 | 2.98 | 10 | 38 | 10 | 28 |
| 24 | 3.98 | 22 | 60 | 22 | 38 |
| 24 | 4.99 | 45 | 82 | 41 | **41** |
| 24 | 6.00 | 96 | 104 | 63 | **41** |
| 24 | 6.96 | 201 | 125 | 84 | **41** |
| 24 | 7.97 | 450 | 147 | 106 | **41** |
| 48 | 4.99 | 45 | 167 | 45 | 122 |
| 48 | 6.00 | 96 | 211 | 85 | **126** |
| 48 | 6.98 | 204 | 254 | 128 | **126** |
| 48 | 8.00 | 458 | 298 | 172 | **126** |

Beyond `U ≈ 5` (`M=24`) resp. `U ≈ 6` (`M=48`), **every added lattice cell is consumed exactly by
the prime powers it contains**: `+22` dof and `+22` rank per unit of `U`. The mechanism is the one
the order anticipated: consecutive prime powers are spaced `≈ 1/n = e^{−u}`, so once `e^{−u} < h`
the comb has `≥ 1` node per cell and a cubic spline with `≥ 3` consecutive interior zeros is `≈ 0`
there. The first `u` with two prime powers closer than `h` is `u = 3.434` (`M=24`) resp.
`4.615` (`M=48`) — the observed saturation sets in one to two units later, when the *density* rather
than a single pair becomes binding. The same numbers hold at `0.58, 0.62, log 2` (`count.json`).

> **Finding (F1).** For comb-vanishing weights on a lattice of step `h`, the support is effectively
> bounded: `U_eff ≈ log(1/h) + c` with `c ∈ [1.5, 2.5]`, two-lattice fit (`M=24`:
> `log(1/0.0458)=3.08`, `U_eff≈5`; `M=48`: `log(1/0.0229)=3.78`, `U_eff≈6`)
> **[amended per R155_019]**. The only way to buy freedom is to refine `h`, and
> `U_eff` grows only like `log(1/h)` while `D(w) = O(e^{U/2})` and the LP size grows like `1/h`.
> `DIAGNOSTIC` (measured); the mechanism (three consecutive interior zeros of a cubic spline in one
> cell force the local coefficients) is elementary but is not written out as a theorem here.
>
> **[amended per R155_019] Nesting argument for saturation.** A comb-vanishing `w`
> supported in `[−U,U]` is also comb-vanishing for any `U' > U` (it vanishes trivially beyond `U`),
> so `null(U) ⊆ null(U')` as spaces of weights. Once the measured `dim null` stabilises across
> increasing `U`, the equal dimensions force **equality of the spaces**: every comb-vanishing weight
> of support `≤ 8` already has support `≤ U_eff`. This upgrades (F1) from a measured coincidence to
> a finite rank computation (still double precision, SVD tolerance `10⁻⁹`), and it is this nesting —
> not mere correlation — that explains the `5·10⁻⁸` agreement of the `U=5` and `U=6` LP values
> reported in §3.

### 2.4 The program

`max c` over `z`, `(β₀−2, β₁)` (or `β = (2,0)`), `c`, subject to
`f_w(τ) ≥ c` on a `δ = 0.02` grid of `[0, TAUMAX]` with two rounds of cutting planes from a
`δ/20` refinement of the `400` worst points, `‖x‖_∞ ≤ 3`, `‖x‖₁ ≤ 60`. Zero side (oracle):
`f_w(τ) = 4∫_0^{Umax} w(u)cos(τu)Z(u)du`, `Z(u) = Σ_{γ>0}^{1000} cos(γu)`, `γ ≤ 1419.4`, ample for
`τ ≤ 200`. Prime side (check): `comblib.f_prime` — full prime-power sum to `e^{Umax}`, knot-aligned
Gauss–Legendre, **exact analytic `K`-tail beyond `Umax`**. `TAUMAX` was chosen `≥ τ_stop(w)` of the
*resulting* `w` and the choice re-verified a posteriori (§3, column `L_w(TAUMAX)`).

---

## §3 Results

`T = ½log3` first (validation of the machinery against `R155_011`), `M = 24`, `U` sweep,
`TAUMAX = 115`:

| run | `U` | `M` | `β` | comb | `m` | dof | rank | nullity | **LP value** | grid value + (non-rigorous) pad `B₂δ²/8`, `δ=0.005` **[amended per R155_019]** | `D(w)` | `τ_stop` | `L_w(TAUMAX)` | prime side at argmin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `c_log3h_U4_b` | 3.98 | 24 | free | yes | 22 | 60 | 22 | 38 | `−2.61616e−2` | `−2.77935e−2` | `1.589e4` | `97.8` | `+0.636` | `−2.61629e−2` |
| `c_log3h_U5_b` | 4.99 | 24 | free | yes | 45 | 82 | 41 | 41 | `−2.30426e−2` | `−2.47221e−2` | `1.822e4` | `103.1` | `+0.458` | `−2.30132e−2` |
| `c_log3h_U6_b` | 6.00 | 24 | free | yes | 96 | 104 | 63 | 41 | `−2.30426e−2` | `−2.47216e−2` | `1.822e4` | `103.1` | `+0.458` | `−2.30130e−2` |
| `c_log3h_U6_w` | 6.00 | 24 | `(2,0)` | yes | 96 | 104 | 63 | 41 | `−3.97534e−2` | `−4.13246e−2` | `1.727e4` | `98.9` | `+0.612` | `−3.97046e−2` |
| `c_log3h_U6_nc` | 6.00 | 24 | free | **no** | — | 104 | 0 | 104 | `−8.58975e−3` | `−1.65692e−2` | `2.405e4` | `114.9` | `+0.004` | `−8.58419e−3` |

`U = 5` and `U = 6` give the **same value to `5·10⁻⁸`** — the direct experimental confirmation of
(F1): support past `U_eff` is worthless.

The four windows, best class (`M = 48`, `U = 6`, `β` free), `TAUMAX = 200`:

| window `T` | `m` | dof | rank | nullity | **LP value** | **grid value + non-rigorous pad** [amended per R155_019] | `B₂` | pad | argmin | `D(w)` (`D_K + D_cosh`) | **`τ_stop`** | **`L_w(200)`** (tail beyond) | **prime side at argmin** | gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `½log3` | 96 | 211 | 85 | 126 | `−1.16566e−2` | `−1.34687e−2` | `579.8` | `1.812e−3` | `5.755` | `3.668e4` (`2837+33846`) | `135.6` | `+1.498` | `−1.16106e−2` | `4.6e−5` |
| `0.58` | 95 | 197 | 84 | 113 | `−1.70380e−2` | `−1.88610e−2` | `583.3` | `1.823e−3` | `7.410` | `3.653e4` (`3193+33334`) | `182.9` | `+0.270` | `−1.70248e−2` | `1.3e−5` |
| `0.62` | 95 | 181 | 82 | 99 | `−5.19331e−2` | `−5.38586e−2` | `616.1` | `1.925e−3` | `3.680` | `2.935e4` (`2501+26845`) | `168.8` | `+0.467` | `−5.19537e−2` | `2.1e−5` |
| `log 2` | 93 | 156 | 78 | 78 | `−8.90733e−2` | `−9.15936e−2` | `806.5` | `2.520e−3` | `4.425` | `3.242e4` (`2158+30263`) | `183.1` | `+0.258` | `−8.90098e−2` | `6.3e−5` |

Notes on honesty of the table.

- **`τ_stop < TAUMAX` at every row, and `L_w(TAUMAX) > 0` at every row**, so Theorem D genuinely
 closes `[TAUMAX, ∞)` for the weight that came out of the LP. (One earlier run,
 `c_log3h_U6_M48_b` with `TAUMAX = 115`, had `τ_stop = 135.6 > 115`, `L_w(115) = −0.961`: it is
 **not** a valid row and is superseded by `c_log3h_M48`, which reproduces the identical value
 `−1.16566e−2` on `[0,200]` because the binding minimum sits at `τ ≈ 5.8`.)
- **[amended per R155_019]** The renamed column is the dense `δ = 0.005` zero-side grid
 minimum minus the Bernstein pad `B₂δ²/8`, with `B₂` (`lem:bern`, `R155_012`'s correction) built
 from `Zenvelope`, i.e. from the 1000-zero model, **not** from `f_prime` — the same defect
 `R155_017` found in `amend.py`. This does not affect the verdict: a grid minimum is already an
 *upper* bound on `min_ℝ f`, and the pad only ever helps a *positivity* claim, so it is irrelevant
 to a negativity conclusion. The column is not a certificate; it is a grid value plus a
 gratuitously pessimistic, non-rigorous pad. The `δ = 2.5·10⁻⁴` prime-side
 dense enclosure of `dense.py` was **not run**: it costs `≈ 8·10⁵` prime-side points per window and
 is pointless on a value that is negative by `10⁻²`, i.e. by `7×` the pad. Declared, not hidden.
- **[amended per R155_019]** `D(w) = D_K + D_cosh` is a `du = 2·10⁻⁵` trapezoid
 quadrature of `∫|W''|`, not a rigorous enclosure, and `L_w(200)` carries the term
 `D/200² ≈ 0.91`. At `0.58` and `log 2` the margin is `L_w = +0.26…+0.27`, i.e. the all-`ℝ`
 closure at these two windows survives only a `≈ 29 %` underestimate of `D`. Plausible (the
 integrand is piecewise smooth, the grid fine) but unproved: the headline "first flat-top run
 whose failure is a statement about all of `ℝ`" is upheld **conditional on this quadrature being
 accurate to better than 29 %**.
- The prime side is evaluated at the argmin and on the `200` worst dense-grid points; it agrees with
 the zero side to `1.3·10⁻⁵…6.3·10⁻⁵` everywhere, which is the `1000`-zero truncation error.
 **The negativity is confirmed on the prime side**, so it is not an artefact of the oracle.
- **[amended per R155_019]** `E_at(w) ≤ 2.0·10⁻¹⁴`, not `= 0` exactly: the equalities
 are eliminated through an SVD null space with tolerance `10⁻⁹·σ_max`, so the returned `w`
 satisfies the comb only to rounding (measured `max_n |w(log n)| = 5.4·10⁻¹⁶…1.0·10⁻¹⁵` on the
 returned `x`). `E_at` enters `L_w` additively, so `τ_stop` scales by `e^{E_at}`: the correction
 is `≤ 2·10⁻¹⁴·τ_stop < 4·10⁻¹²` in `τ`, and `L_w(200)` drops by `≤ 2·10⁻¹⁴` — fifteen orders
 below where it bites. The counterfactual `Σ_{2T<log n≤U} v_n = 71.0…72.9` is what `E_at` would
 have cost had the equalities not been imposed at all, i.e. `τ_stop ≈ 10^{31}` — this is the whole
 point of the experiment.

---

## §4 Diagnosis: what is binding

Three comparisons on the *same* class and the *same* interval, `T = ½log3`:

| what | value on `[0,115]`, `M=24`, `U=6`, `β` free | ratio |
|---|---|---|
| no comb (control) | `−8.590e−3` | `1.0` |
| **comb**, `M = 24` | `−2.304e−2` | `2.68×` worse |
| **comb**, `M = 48` | `−1.166e−2` | `1.36×` worse |
| no comb on `[0,60]` (`R155_011 §3`, different edge basis) | `−2.863e−3` | `0.33×` |

1. **The comb equalities bind, and the penalty is a lattice-resolution artefact as much as an
 arithmetic one.** Halving `h` cuts the comb penalty from `2.68×` to `1.36×`. The extrapolation
 `M → ∞` is *not* to `0`: the comb has positive density beyond `U_eff` and the constraint
 `w ≈ 0` past `U_eff` is `h`-independent. But the measured trend says the `M = 48` numbers are
 closer to the class limit than to the `M = 24` ones, and a `M = 96` run (`≈ 400` splines,
 `≈ 4` min) would settle it. `R155_013 §8(1)`'s "honest expectation is that the comb-free class is
 *worse*" is **confirmed**, with the factor now measured.
2. **The interval also binds, and more than the comb at `M = 48`.** Lengthening `[0,60] → [0,115]`
 costs `3.0×` in the *unconstrained* class (`−2.86e−3 → −8.59e−3`); the comb then costs a further
 `1.36×`. So the dominant loss in going from "the `R155_011` headline number" to "an honest
 statement about `ℝ`" is the **interval**, not the comb. Theorem D bought the interval down from
 `10^{20}` to `10²`; `10²` is still `2×` the `[0,60]` on which the class was previously reported.
3. **[amended per R155_019]** Both controls are negative, but they are not equivalent:
 the no-comb control's binding minimum sits at `τ = 42.9`, not at small `τ`. It is the **comb**
 that moves the binding minimum down to `τ ≈ 4–8`, i.e. **inside** `[0,60]`, at every window —
 the same range `R155_013 §6` found for the bounded-profile class. So the small-`τ` failure is
 comb-induced, not a feature both constraints share independently. (No "below the first zero"
 reading is intended or supported: with argmins at `3.7–7.4`, `f_w` there is not built only from
 tails — the flat top itself contributes `∫(1−w)K` and the `2∫w cosh` term at all `τ`, and no
 decomposition here isolates a negative term below `γ₁ = 14.13`.)
4. **`β` matters, as always.** Freeing `(β₀−2, β₁)` improves `½log3` from `−3.975e−2` to
 `−2.304e−2` (`1.73×`), consistent with `R155_011 §5` ("the multipliers are decisive"). The optimal
 `β` is large (`|β₀−2| ≈ 1.1–4.2`), which pushes `τ_stop` up through `k₀, k₁` but never past `200`.
5. **`D_cosh` is `12–15×` `D_K`**, exactly as `R155_013 §4(3)`: the tail cost is the `cosh(u/2)`
 weighting of the shoulder. Comb-vanishing *reduced* `D` relative to `R155_011`
 (`3.7e4` against `5.1e4` at `½log3` for a shorter support), so the `O(e^{U/2})` of Cor. D.3 and
 the saturation (F1) work in the same direction: short support, small `D`, small `τ_stop`, small
 value.

---

## §5 Labels

| statement | label |
|---|---|
| `comblib.WinC` is even, globally `C²`, `w ≡ 1` on `[−2T,2T]`, `supp w ⊂ [−U,U]`; the three edge coefficients `x_{−1}=x_0=x_1=1` are the **unique** `C²` matching (§2.1) | **`PROVED`** (elementary, from the cardinal cubic B-spline values) |
| The class satisfies the hypotheses of Theorem D case (a) and, with the equalities imposed, of Cor. D.2 (`E_at(w) ≤ 2·10⁻¹⁴`, not exactly `0` **[amended per R155_019]**) | **`PROVED`** (by construction, up to double-precision SVD tolerance: `w` vanishes at every prime power with `2T < log n ≤ U` to within `10⁻¹⁵`, and `w ≡ 0` beyond `U`) |
| **(F1)** null-space saturation / `U_eff ≈ log(1/h) + c` | `DIAGNOSTIC` (measured for `M ∈ {24,48}`, `U ≤ 8`, four windows; mechanism identified, not proved) |
| The comb system is feasible for every `(T,U,M)` tried (residual `0`) | `DIAGNOSTIC` (least squares in double precision) |
| All LP values, certified values, `D(w)`, `τ_stop`, `L_w(200)`, prime-side values of §3 | `DIAGNOSTIC` (double precision; `D` from a `2·10⁻⁵` quadrature; the Bernstein pad is the honest `B₂δ²/8` but `B₂` itself is a double-precision envelope) |
| **A certificate on `ℝ` at any `T`** | **NOT OBTAINED.** Every window negative by `1.2·10⁻²…8.9·10⁻²`, confirmed on the prime side. |
| Any statement about `λ^W`, `λ^P`, an endpoint, or the sign of `ζ` at any `T` | **none made**; endpoint of record unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, Paper 46 Thm C) |

**What *is* new and survives.** This is the **first run in the track that is a statement about all
of `ℝ`**: for these four explicit weights, `f_w ≥ L_w > 0` on `[200, ∞)` by Theorem D (proved), and
`f_w` is measured `< −10⁻²` somewhere in `[0,200]` on **both** sides of the explicit formula. The
negative result is therefore not "on the interval we looked at"; it is a falsification of the
comb-vanishing flat-top class at these four windows, modulo the double-precision caveat and the
finite lattice.

---

## §6 Next

1. **`M = 96` at `½log3`** (`≈ 400` splines, `U = 6`, `β` free, `TAUMAX = 250`, `≈ 4` min). The only
 open quantitative question of this note is whether the comb penalty tends to `1.0` as `h → 0`.
 If it does, the comb is *free* in the limit and the wall is entirely the interval + the small-`τ`
 structural failure; if it plateaus near `1.3`, (F1) has a positive density cost that deserves a
 theorem.
2. **Attack `τ ∈ [0,10]`, not the tail.** Every run of rounds 1–2 — unconstrained, bounded-profile
 (`R155_013 §6`), comb-vanishing — fails at `τ ≈ 2–10`. The tail programme (`prop:env` →
 Theorem D → Cor. D.2) is finished: it took `10^{40}` to `10²` and the answer did not change.
 The next object is a lower bound for `min_{τ≤10} f_w` over the whole flat-top class, i.e. a
 **Toeplitz-type ceiling at small `τ`** in the style of Theorem TK (`R155_014`), which would close
 the class by a proof instead of by an LP.
3. **The graded/decay hybrid** (`R155_013 §8(2)`, Remark D.2) is untouched and remains the only
 route by which a flat-top weight could inherit `lem:F1`'s exact treatment of the comb.
4. Do **not** open a `U > 6` or `E_at > 0` variant: (F1) says the first buys nothing and
 `R155_013 §4(2)` says the second costs `10^{9}…10^{20}` in `τ_stop`.

---

*Scripts, commands, runtimes and JSON: `scripts/reverse/comb/` (`comblib.py`, `count.py`, `lp.py`,
`count.json`, `lp_*.json`, `README.md`). Total compute `≈ 6.5` min, one process at a time.
Paper 46 not touched.*
