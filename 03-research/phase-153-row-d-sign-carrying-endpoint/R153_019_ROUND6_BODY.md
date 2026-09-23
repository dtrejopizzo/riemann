# R153.019 — Round 6, builder: the prime-free body `W_T`, its facet at `w_ζ`, and the Krein bands

*Builder: Opus 5. 2026-09-20. Orders: R153_018 (lead). Scripts: `scripts/round6/` (`core.py`, `validate.py`,
`t2_axis_lemma.py`, `t2_facet.py`, `t2_support.py`, `t3_band.py`, `t3_joint.py`, `t3_apex.py`, `t4_log5.py`, `prec.py`).*

**One-line result.** The body is built and it is emphatically **not** the box: the axis projections are exactly `±cos(π/m)`
(`m = ⌈2T/a⌉+1`, PROVED), Gamma coercivity is `x_0 ≥ −0.15322`, and the resulting box bound in the direction `w_ζ` is
`−1.27763`, while the true support in that direction is `+1.0·10⁻⁷`. **All of the positivity at `log 2` — 100% of it,
`1.27763` out of `1.27763` — is joint coupling between `x_0`, `x_2`, `x_3`, and at least `0.717` of it is genuinely
three-way (no pairwise relaxation does better than `−0.7171`).** The Euler weight `w_3 = 0.634284` lies inside its Krein
band `[0.6341709, 0.6342883]` at **96.4% of the way to the upper edge**; `w_2` lies at **99.85%** of its band; and the
pair `(2w_2, 2w_3)` sits `1.7·10⁻⁵` (relative) below the **apex** of the two-dimensional admissible region, which is a
curved sliver that closes at `v_2 = 0.4901375`.

---

## 1. Corpus check (mandatory, file:line)

| item | hit | pre-existing | new here |
|---|---|---|---|
| `cos(π/m)` lemma | `03-research/phase-147-row-d-galois-ring/R147_003_BUILDER_ROUND2.md:271–290` (Lemma A.6, `PROVED`), `R147_005_LEAD_CLOSING_DECISION.md:61` | `L(m) = min_θ max_k|cos(θ+2πk/m)| = cos(π/m)` (`m` even) / `cos(π/(2m))` (`m` odd) — a **Galois-orbit min-max**, about roots of unity | the projection lemma of §3 is a **different statement** (min of the autocorrelation at lag `a` over an interval of length `L`; value `−cos(π/(⌈L/a⌉+1))`, a Jacobi-chain eigenvalue). Same closed form, different object. Recorded as **not** a re-use: proved here from scratch. |
| Krein / positive extension | `03-research/phase-136-row-d-map/MAP_1_WALLS_AND_MASTER_DOCS.md:153` (ES-14, `ABANDONED`); `R153_017:16,26` | abstract Krein extension does not identify the arithmetic kernel; no soft minorant exists (Bochner) | the **band** here is not an extension problem: it is the exact dual description `{v : λ_min(M_0 − v·S) ≥ 0}`, computed, not postulated |
| LP / autocorrelation reformulation | `R153_016_ROUND5_PHI_CONSTRUCTION.md:53–60` (`PROVED`) | `A_T ≥ 0 ⟺ ∫σ_TΦ ≥ 0` on `𝒦_{2T}`; no-soft-minorant corollary | `W_T` is the **finite-dimensional image** of that LP under the moment map `Φ ↦ (∫g Φ, Φ̌(log n))`; §2 shows the half-space question is unchanged by convexification |
| detecting cones | `03-research/phase-138-row-d-detecting-cones/R138_005_LEAD_CLOSING_DECISION.md:39,44` (D.15.4c, D.16.2‴, D.16.2′ crossing height `2πe·e^{2T}`) | different objects (polar block, translation); `2πe·e^{2T}` = round 4's `H⋆` | **RESTATEMENT** noted for R153_014's next pass, as the lead asked |
| support function | 3 files (`phase-142`, `phase-145`, `phase-151`), all about the **effective cone** of a curve | unrelated geometry | no collision |
| rate decomposition, minimiser | `R153_012_ROUND4_DECAY_LAW.md` | `λ(log 2) ≈ 9.9·10⁻⁸` Richardson, minimiser even | reproduced independently here (§6: `9.899·10⁻⁸`); the minimiser's **coordinates** `x(F_min)` are new |

Nothing below duplicates a prior result. `W_T` with the shift coordinates does not occur in the corpus.

---

## 2. (T1) Convexity, closedness, and why the question is almost vacuous

Fix `T` and the contact set `N_T = {n : n < e^{2T}}`, `d = |N_T|`. For `F` in the form domain of `G_{Γ,T}` inside `P_T`,
`‖F‖ = 1`, put `x(F) = (x_0, (x_n)_{n∈N_T})`, `x_0 = ⟨(G_{Γ,T}−m_0)F,F⟩`, `x_n = c_F(\log n)`. `W_T := x(\{‖F‖=1\})`.

**Proposition 2.1 (`PROVED`, elementary).** For any `w`, `A_T ≥ 0` on `P_T` ⟺ `W_T ⊂ H_w` ⟺ `\overline{\mathrm{conv}}\,W_T ⊂ H_w`.
*Proof.* A half-space is closed and convex. ∎
So the entire half-space question is a question about `h_{W_T}`, the support function of the closed convex hull, whatever
`W_T` itself looks like. Convexity is a convenience, not a hypothesis.

**Proposition 2.2 (`PROVED` for `d = 2`; Au-Yeung–Poon + exhaustion).** For `d = 2` (i.e. `1+d = 3` coordinates, the case
`T = \log 2`), `W_T` is convex. *Proof.* Let `V_1 ⊂ V_2 ⊂ …` be finite-dimensional subspaces of `P_T ∩ C_c^∞(I_T)` with
`\dim V_k ≥ 3` and `⋃V_k` dense in the form domain. On each `V_k` the three forms are real symmetric matrices of size
`≥ 3`, so by Au-Yeung–Poon (*Proc. AMS* **71** (1978) 55–58; real symmetric, `m = 3`, `n ≥ 3`) the joint range
`x(\{F ∈ V_k, ‖F‖=1\})` is convex. The family is nested increasing and its union is `W_T`; an increasing union of convex
sets is convex. ∎
**Not proved for `d ≥ 3`.** Au-Yeung–Poon fails for `m = 4` real forms, so at `T = ½\log 5` (four coordinates) convexity of
`W_T` is `OPEN`. By Prop. 2.1 this costs nothing.

**Closedness.** `W_T` is **not** closed and **not** bounded: `Re ψ(¼+iτ/2) − \log π → +∞`, so `x_0` is unbounded above and
`h_{W_T}(u) = +∞` for every `u` with `u_0 > 0`. The recession direction `+e_0` is in the recession cone of the closure.
Consequently the only informative directions are `u_0 ≤ 0`, and we normalise `u_0 = −1`:

  **`h_{W_T}(−1, v) = −λ_{\min}\big(M_0 − \sum_n v_n S_n \,\big|\, P_T\big)`**, `S_n` = the form `F ↦ c_F(\log n)`, `M_0` = the
  Gamma block. `A_T ≥ 0 ⟺ h_{W_T}(−1, 2w) ≤ 0`.

So the body is the epigraph `\{x_0 ≥ Ψ_T(x_2,x_3,…)\}` of a convex function `Ψ_T` whose Legendre transform is the family of
minimal eigenvalues above. This is the exact dual of the round-5 LP. `RESTATEMENT` of R153_016 §2.3 in moment coordinates.

---

## 3. (T2a) The axis projections: `±cos(π/m)` exactly

**Lemma 3.1 (`PROVED`, new here).** Let `a > 0`, `L = 2T`, `k_{\max} = ⌈L/a⌉` = the largest number of points of an
arithmetic progression of gap `a` inside an interval of length `L`. Then
  **`\sup_{\|F\|=1,\,\mathrm{supp}F⊂I_T} c_F(a) = -\inf(\cdot) = \cos\!\big(\tfrac{π}{k_{\max}+1}\big)`**,
the supremum being attained in the closure (it is the edge of the essential spectrum).
*Proof.* The form `c_F(a) = ⟨\tfrac12(S_a+S_{-a})F,F⟩` on `L²(0,L)` (after translation) commutes with the fibration
`u ↦ u \bmod a`. Writing `L²(0,L) = \int^⊕_{s∈(0,a)} \mathbb{C}^{k(s)}\,ds`, `k(s) = \#\{j ≥ 0 : s+ja < L\}`, the operator
acts fibrewise as `\tfrac12 J_{k(s)}`, `J_k` the `k×k` tridiagonal matrix with `0` on the diagonal and `1` off it, whose
eigenvalues are `2\cos(πj/(k+1))`, `j = 1..k`. Hence the spectrum is `\{\cos(πj/(k+1))\}` over the `k` values taken by
`k(s)` on a set of positive measure, and its extremes are `±\cos(π/(k_{\max}+1))`, `k_{\max} = \max_s k(s) = ⌈L/a⌉`. ∎
The two moment constraints are of codimension 2 and do not move the edge of the essential spectrum.

**Verification** (`t2_axis_lemma.py`, `K = 400`, exact shift matrices, agreement to `10` digits):

| `T` | `a` | `L/a` | `m = ⌈L/a⌉+1` | `cos(π/m)` | numerical `max c_F(a)` |
|---|---|---|---|---|---|
| `\log 2` | `\log 2` | 2.0000 | 3 | 0.5000000000 | 0.5000000000 |
| `\log 2` | `\log 3` | 1.2619 | 3 | 0.5000000000 | 0.5000000000 |
| `½\log3` | `\log 2` | 1.5850 | 3 | 0.5000000000 | 0.5000000000 |
| `½\log5` | `\log 2` | 2.3219 | 4 | 0.7071067812 | 0.7071067812 |
| `½\log5` | `\log 3` | 1.4650 | 3 | 0.5000000000 | 0.5000000000 |
| `½\log5` | `\log 4` | 1.1610 | 3 | 0.5000000000 | 0.5000000000 |
| 1.2 | `\log 2` | 3.4625 | 5 | 0.8090169944 | 0.8090169944 |
| 1.8 | `\log 2` | 5.1937 | 7 | 0.9009688679 | 0.9009688679 |
| 2.5 | `\log 2` | 7.2135 | 9 | 0.9396926208 | 0.9396926208 |

**Gamma coercivity** (`DIAGNOSTIC-NUMERIC`): `\min x_0 = λ_{\min}(G_{Γ,T}−m_0|P_T) = −0.153215` at `\log 2`
(`K = 320`; `−0.15358` at `K = 480`, drifting down; matches R153_005's `−0.153`), and `−0.30712` at `½\log5`.
At `½\log3` it is **positive** (`+0.0833` is the max of the band function; see §5).

---

## 4. (T2b) `W_{\log 2}` in `R³`: support function and the facet at `w_ζ`

Assembly: sine basis `φ_k(t) = \sin(kπ(t+L)/L)` on `I_T`; shift blocks **exact** (closed form, verified against adaptive
quadrature to `1.7·10⁻¹⁰`); Gamma block by graded Gauss–Legendre on `[0, 4000]` (400 panels × 24 nodes), the scheme of
`scripts/audit/aud_spectral.py`; moment constraints removed by an explicit null-space basis. Cross-check: this assembly
reproduces `aud_spectral`'s `a = 0` value (`2.0876·10⁻⁷ = 2 × 1.0438·10⁻⁷`) and R153_012's `λ(\log2)`.

### 4.1 Support function (`DIAGNOSTIC-NUMERIC`, `K = 320`)

`h(v) := h_{W}(−1,v) = −λ_{\min}(M_0 − v_2S_2 − v_3S_3)`. Box bound `= −\min x_0 + \tfrac12(|v_2|+|v_3|)`.

| `v_2` | `v_3` | `h(v)` | box bound | coupling gap |
|---|---|---|---|---|
| 0 | 0 | +0.15321549 | +0.15321549 | 0 |
| +0.5 | 0 | **−0.02863321** | +0.40321549 | 0.43184870 |
| 0 | +0.5 | +0.25910942 | +0.40321549 | 0.14410607 |
| +0.5 | +0.5 | +0.03711511 | +0.65321549 | 0.61610039 |
| +1 | 0 | +0.08878829 | +0.65321549 | 0.56442720 |
| 0 | +1 | +0.37439103 | +0.65321549 | 0.27882446 |
| +1 | +1 | +0.02204246 | +1.15321549 | 1.13117303 |
| −1 | +1 | +0.86171164 | +1.15321549 | 0.29150385 |
| +1 | −1 | +0.20876743 | +1.15321549 | 0.94444806 |
| −1 | −1 | +0.42559389 | +1.15321549 | 0.72762161 |
| `2w_2` = +0.98026 | 0 | +0.08282757 | +0.64334457 | 0.56051700 |
| 0 | `2w_3` = +1.26857 | +0.43944435 | +0.78749959 | 0.34805524 |
| **`2w_2`** | **`2w_3`** | **−1.03·10⁻⁷** | **+1.27762867** | **1.27762877** |
| `−2w_2` | `−2w_3` | +0.36936423 | +1.27762867 | 0.90826443 |
| +2 | +2 | +0.61313924 | +2.15321549 | 1.54007625 |
| +5 | +5 | +2.89710655 | +5.15321549 | 2.25610894 |

The entry `h(0.5,0) = −0.0286 < 0` says the body lies strictly inside `\{x_0 ≥ \tfrac12 x_2 + 0.0286\}`: a non-trivial
one-prime inequality. `w_ζ = (2w_2,2w_3)` is, to `10⁻⁷`, the **unique direction on the boundary of the dual cone** among
those tested: `h(w_ζ) = −1.03·10⁻⁷`.

### 4.2 The contact point and the facet (`DIAGNOSTIC-NUMERIC`)

Lowest eigenvalues of `A_{\log2}` (`K = 480`): `1.0160·10⁻⁷` (even), `1.1372·10⁻⁵` (odd), `2.1017·10⁻³` (even),
`6.089·10⁻²`, `0.5311`, `0.8315`. Coordinates of the corresponding unit vectors:

| eigenvector | `λ` | parity | `x_0` | `x_2` | `x_3` |
|---|---|---|---|---|---|
| `F_{\min}` | `1.0160·10⁻⁷` | even | 0.0880040 | 0.0745019 | 0.0118029 |
| `F_1` | `1.1372·10⁻⁵` | odd | 0.2728208 | 0.3432806 | −0.0502095 |
| `F_2` | `2.1017·10⁻³` | even | 0.3624782 | 0.0145765 | 0.2728177 |

(`K`-stability: 4 digits in `x_0, x_2`, 3 in `x_3` over `K = 240…480`.)

**Answer to the lead's question.** The supporting hyperplane with normal `w_ζ` touches `\overline{W}_{\log2}` at a
**single exposed point** `x(F_{\min}) = (0.08800, 0.074502, 0.011803)`, not at an edge or a facet: the minimal eigenvalue is
simple with a spectral gap of `1.14·10⁻⁵`, `112×` the eigenvalue itself. But the touching is *almost* flat: the second
extreme point `x(F_1)` lies at Euclidean distance `0.33` and is only `1.14·10⁻⁵` above the hyperplane. **So `W_{\log 2}` has
a quasi-facet: a region of diameter `≈ 0.33` in which the body deviates from the supporting plane of `w_ζ` by less than
`10⁻⁵`, with the true contact `10⁻⁷` deep inside it.** The contact point is far from every corner of the box
(`x_2 = 0.0745 ≪ 0.5`, `x_3 = 0.0118 ≪ 0.5`): the minimiser is nearly blind to the `n = 3` contact, which is exactly why
the band in `w_3` (§5) is wide and the band in `w_2` is narrow.

---

## 5. (T3) Krein bands

Because `v ↦ λ_{\min}(M_0 − v·S)` is a minimum of affine functions it is **concave**; every band and the joint region are
therefore **convex** (`PROVED`). Edges by `brentq` to `10⁻¹³`; the limiting error is `K`-truncation.

**Band in `w_3` at `T = \log 2`** (`w_2` fixed at `Λ(2)/\sqrt2`):

| `K` | `w_3^-` | `w_3^+` | width | `w_3 − w_3^-` | `w_3^+ − w_3` |
|---|---|---|---|---|---|
| 240 | 0.6341667 | 0.63428852 | `1.218·10⁻⁴` | `1.174·10⁻⁴` | `4.420·10⁻⁶` |
| 320 | 0.6341688 | 0.63428846 | `1.197·10⁻⁴` | `1.153·10⁻⁴` | `4.359·10⁻⁶` |
| 480 | 0.6341709 | 0.63428839 | `1.175·10⁻⁴` | `1.132·10⁻⁴` | `4.290·10⁻⁶` |
| 640 | — | 0.63428835 | — | — | `4.254·10⁻⁶` |
| `K→∞` (`a+b/K` fit) | — | **0.63428827** | — | — | **`4.17·10⁻⁶`** |

**`w_3 = Λ(3)/\sqrt3 = 0.63428410` lies inside the band at 96.4% of its width, i.e. `4.2·10⁻⁶` below the upper edge and
`1.13·10⁻⁴` above the lower edge.** The predicted distance `λ_{\min}/(2|x_3(F_{\min})|) = 9.899·10⁻⁸/0.023606 = 4.19·10⁻⁶`
agrees with the measured `4.17–4.29·10⁻⁶` to 1–2%: the Hellmann–Feynman slope is `dλ/dv_3 = −2x_3(F_{\min})`, `PROVED`.

**Band in `w_2` at `T = \log 2`** (`w_3` fixed, `K = 480`): `[0.4896839, 0.4901298]`, width `4.458·10⁻⁴`;
`w_2 = 0.49012907` sits `6.81·10⁻⁷` below the upper edge — **99.85% of the way up** — consistent with
`λ/(2x_2) = 9.899·10⁻⁸/0.14900 = 6.64·10⁻⁷`.

**Band in `w_2` at `T = ½\log3`** (only contact; `K = 480`): `[0, 0.4932791]`; the lower end is `0` because `G_{Γ,T} − m_0`
is already positive on `P_{½\log3}`. `w_2 = 0.4901291` sits `3.15·10⁻³` below the upper edge — **0.64% of the way down**,
i.e. a `0.64%` increase of `Λ(2)/\sqrt2` would already destroy positivity at `½\log3`. The band's argmax is at
`v_2 ≈ 0.0133` with `λ_{\max} = 8.334·10⁻²`.

**Joint admissible region at `T = \log 2`** (coefficients `v_n = 2w_n`; `K = 320`):

| `v_2` | `v_3^-` | `v_3^+` | width |
|---|---|---|---|
| 0.00, 0.10 | — | — | **empty** (`max λ = −0.1532, −0.0666`) |
| 0.20 | 0 | 0.0203361 | `2.03·10⁻²` |
| 0.30 | 0 | 0.2401317 | `2.40·10⁻¹` |
| 0.40 | 0.2164546 | 0.4529448 | `2.37·10⁻¹` |
| 0.45 | 0.4338637 | 0.5556792 | `1.22·10⁻¹` |
| 0.48 | 0.5765600 | 0.6156622 | `3.91·10⁻²` |
| 0.49 | 0.6332908 | 0.6345528 | `1.26·10⁻³` |
| **0.4901291 (`=w_2`)** | **0.6341688** | **0.6342885** | `1.20·10⁻⁴` |
| 0.4902 | — | — | **empty** (`max λ = −1.57·10⁻⁵`) |
| 0.495, 0.50, 0.52 | — | — | empty |

(The table is in the variables `(v_2, v_3)` read as *weights*, i.e. the `v` of `H_{(v_2,v_3)}` is `2v`.)

**Apex** (`t3_apex.py`, `K = 240/320/480`): the region is non-empty exactly for `v_2 ≤ v_2^*`, with
`v_2^* = 0.4901378, 0.4901377, 0.4901375`; the `v_3` at the apex is `0.6342265, 0.6342276, 0.6342287`.
**So `w_2` lies `8.5·10⁻⁶` below `v_2^*` — a relative margin of `1.7·10⁻⁵` — and `w_3` lies `5.5·10⁻⁵` above the apex's
`v_3`.** The arithmetic point is inside a sliver whose two-dimensional diameter is `10⁻⁴`, within `10⁻⁵` of its tip.

**What can and cannot be resolved.** The Gamma block's quadrature is stable to `7·10⁻¹²` absolute in `λ` (`taumax`
4000→20000, `npan` 400→600, `ng` 24→32), i.e. `7·10⁻⁵` relative at `\log 2` — far below the `K`-truncation drift of
`2.6%` from `K = 240` to `640`. Therefore: the band **widths** are resolved to ~2%, the **upper edges** to `1.3·10⁻⁷`
absolute (`2·10⁻⁷` relative), and the **margins** `w_3^+ − w_3 = 4.2·10⁻⁶`, `w_2^+ − w_2 = 6.8·10⁻⁷` to about `3%`.
Galerkin gives an **upper** bound on `λ_{\min}`, hence an **outer** bound on the band: the true band is contained in the
computed one, so "`w_3` is inside the band" is *not* certified by this computation — it is certified by Paper 42's
interval certificate, of which this is the geometric reading. `DIAGNOSTIC-NUMERIC`.

---

## 6. Reproduction of the record value

`λ_{\min}(A_{\log2}|P_T)`: `1.0675·10⁻⁷` (160), `1.0438·10⁻⁷` (240), `1.0307·10⁻⁷` (320), `1.0160·10⁻⁷` (480),
`1.0083·10⁻⁷` (640); `a + b/K` fit `→ 9.899·10⁻⁸`. R153_012's Richardson value was `9.87·10⁻⁸`: agreement to `0.3%` from
an independent assembly (exact shift blocks instead of a multiplier for the prime channel). `DIAGNOSTIC-NUMERIC`.

---

## 7. (T4) `W_{½\log5}` in `R⁴`

Contacts `2, 3, 4`; `w_4 = Λ(4)/2 = (\log 2)/2 = 0.3465736`. Axis projections (§3, exact): `x_2 ∈ [−0.70711, 0.70711]`
(`= ±\cos(π/4)`, the **first** place where the `n = 2` chain lengthens to 3), `x_3, x_4 ∈ [−0.5, 0.5]`; `\min x_0 = −0.3071`.
Box bound `= −1.77811`.

| `K` | `λ_{\min}(A_{½\log5})` | next two | `‖·‖` | roundoff floor |
|---|---|---|---|---|
| 240 | `3.3015·10⁻¹²` | `6.92·10⁻¹⁰`, `3.32·10⁻⁷` | 5.25 | `1.2·10⁻¹⁵` |
| 320 | `3.2651·10⁻¹²` | `6.80·10⁻¹⁰`, `3.27·10⁻⁷` | 5.55 | `1.2·10⁻¹⁵` |
| 480 | `3.2230·10⁻¹²` | `6.65·10⁻¹⁰`, `3.22·10⁻⁷` | 5.98 | `1.3·10⁻¹⁵` |
| 640 | `3.1954·10⁻¹²` | — | 6.28 | `1.4·10⁻¹⁵` |
| `K→∞` | `3.136·10⁻¹²` | | | |

Quadrature sensitivity `2·10⁻¹⁵` (five settings), so the value is `≈ 2000×` the numerical floor and is a genuine feature
of the Galerkin problem — **but Galerkin gives an upper bound, so all that is established is
`λ_{\min}(A_{½\log5}|P_{½\log5}) ≤ 3.20·10⁻¹²`.** (P153.3) therefore reads, after this round: *if* `ξ`-positivity extends
to `½\log5`, it does so with a margin at most `3.2·10⁻¹²`, five orders of magnitude thinner than at `\log 2`. No sign is
claimed. `DIAGNOSTIC-NUMERIC`, no certification, `FATAL` rule clean (no zeros used).

**Qualitative change of the facet.** The contact point is `x(F_{\min}) = (0.062373, 0.035278, 0.021892, 2.8·10⁻⁵)`
(`K = 480`). The **fourth coordinate is numerically zero**: the minimiser does not feel the `n = 4` contact at all. Hence
`∂λ/∂v_4 = −2x_4 = −5.6·10⁻⁵`, and the `w_4`-band is nearly flat: the argmax over `v_4` is at `0.346573` against
`w_4 = 0.3465736` — the Euler weight sits essentially **at the optimum** of its own band, not at its edge, with
`λ_{\max} = 3.32·10⁻¹¹` vs `λ(w_4) = 3.22·10⁻¹²`. The new coordinate enters as an **almost-flat direction of the body at
the contact**, not as a new constraint: the qualitative change from `R³` to `R⁴` is degeneracy, not a new facet. The
eigenvalue cascade `3.2·10⁻¹², 6.6·10⁻¹⁰, 3.2·10⁻⁷` (three near-null directions) says the contact is now close to a
three-dimensional flat. `DIAGNOSTIC`.

---

## 8. (T5) Is the body the box? No, and the coupling is three-way

Box (projections + Gamma coercivity only) vs truth at `T = \log 2`, direction `w_ζ`:

| bound | value |
|---|---|
| box: `\min x_0 − 2w_2·\tfrac12 − 2w_3·\tfrac12` | **`−1.277629`** |
| best pairwise relaxation `(x_0,x_2)` joint, `x_3` free | `−0.717112` |
| pairwise `(x_0,x_3)` joint, `x_2` free | `−0.929573` |
| pairwise `(x_2,x_3)` joint, `x_0` free | `−1.054143` |
| **truth** `λ_{\min}(A_{\log2})` | **`+1.03·10⁻⁷`** |

**Verdict (`DIAGNOSTIC-NUMERIC`, unambiguous at this precision).** The Ingham/`cos(π/m)` projections plus Gamma coercivity
describe a body `1.2776` too large in the direction `w_ζ`; the whole of the positivity is joint. Even the *best* pairwise
relaxation leaves a deficit of `0.7171`, so at least `56%` of the coupling is irreducibly **three-way** (`x_0, x_2, x_3`
together). The mechanism is visible in the contact point: the box's optimum wants `x_2 = x_3 = ½`, i.e. `F` simultaneously
in phase with its `\log 2`- and `\log 3`-translates, while `F_{\min}` achieves `(0.0745, 0.0118)` — the shift
`\log 3 − \log 2 = \log(3/2)` makes the two chain structures incompatible, exactly the lead's expectation. The coupling
gap grows with `|v|` (`1.54` at `v = (2,2)`, `2.26` at `(5,5)`), so this is not a small-`v` artefact.

**Falsifier (`Ξ_a`).** Its weights are `v_n = 2w_n(n^a+n^{-a})`: `(2.0031, 2.6762)` at `a = 0.30` and `(2.0567, 2.8536)` at
`a = 0.45`, against an admissible region that is empty for `v_2 > 0.98028` (`= 2v_2^*`). `Ξ_a` exits `H` by a factor
`> 2` in each coordinate, and does so **already in the prime coordinates alone**, before the archimedean coordinate is
changed. Confirmed by direct computation with the `Ξ_a` symbol and the four-moment space (`scripts/audit/aud_spectral.py`,
`K = 240`): `λ_{\min} = −1.6688·10⁻²` (`a = 0.30`), `−5.0694·10⁻²` (`a = 0.45`), `+2.0876·10⁻⁷` (`a = 0`, `= 2λ(A_{\log2})`).
Caveat of record: `Ξ_a` does **not** live on the same body — its Gamma coordinate is `\sum_± Reψ(¼±a/2+iτ/2) − 2\logπ` and
its constraint space `P_T^{(a)}` has four moments (`P_T^{(a)} ⊄ P_T`, R153_005). The falsifier test passes, but it is a
test of the *weight vector against a comparable region*, not a literal containment. `DIAGNOSTIC-NUMERIC`.

---

## 9. (T6) Honest statement

1. The uniform claim "`w_ζ` lies in the dual cone of `W_T` for every `T`" **is Weil's criterion**, restated in moment
coordinates. Round 6 does not weaken it and does not prove it. `RESTATEMENT`.
2. What is new is **separation geometry with numbers**: at `\log 2` the arithmetic weight vector sits at `96.4%` (in `w_3`),
`99.85%` (in `w_2`) and `1.7·10⁻⁵` relative (at the apex of the joint region) of the boundary of the admissible set, and
the admissible set itself is a curved sliver, not a box. "Criticality at `\log 2`" (R153_005 §2.4) now has a shape.
3. **Would the body's law be prime-free and explicit?** The body *is* prime-free (Lemma 3.1 is pure Fourier analysis; `M_0`
is archimedean). Its law is **not** the box, so a prime-free explicit description would have to be a closed form for the
convex function `Ψ_T(x_2,x_3)` — equivalently for `λ_{\min}(M_0 − v·S)` as a function of `v`. The data say this is a
genuine three-body spectral problem: the two shift operators `S_2, S_3` do not commute (their commutator is supported on
the boundary layers of the two chain fibrations, which are incommensurable since `\log 3/\log 2 ∉ Q`), and the contact
point moves continuously with `v` inside the sliver. **I see no evidence in this round for a closed form**, and one
negative indication: at `½\log5` the contact degenerates to a near-three-dimensional flat, so any putative law would have
to be non-smooth in `T` at the contact thresholds `T = \tfrac12\log n`. `OPEN`, and the honest expectation is negative.
4. What the round **does** buy for the programme: (i) the half-space question is exactly a support-function question on a
prime-free convex body (Prop. 2.1, PROVED) — arithmetic enters only through the point `w`; (ii) the Hellmann–Feynman
identity `∂λ/∂v_n = −2x_n(F_{\min})` turns band margins into coordinates of the minimiser, which is the only *exact*
transfer between "how much room the primes have" and "what the extremal function looks like" the corpus has; (iii) the
`cos(π/m)` projection lemma gives the exact, `T`-explicit, prime-free outer box for every `T`, and the round measures how
far it is from sufficient — a permanent negative result for every projection-only argument.

---

## 10. Labels

| item | label |
|---|---|
| Prop. 2.1 (half-space ⟺ closed convex hull) | `PROVED` |
| Prop. 2.2 (`W_T` convex for `d = 2`, via Au-Yeung–Poon + exhaustion); `d ≥ 3` | `PROVED` / `OPEN` |
| `W_T` unbounded above in `x_0`; `h = +∞` for `u_0 > 0`; dual formula `h(−1,v) = −λ_{\min}(M_0 − v·S)` | `PROVED` |
| Lemma 3.1 (axis projection `= ±\cos(π/(⌈2T/a⌉+1))`) | `PROVED` (new; distinct from R147_003's Lemma A.6) |
| concavity of `v ↦ λ_{\min}`, convexity of the bands and of the joint region | `PROVED` |
| `∂λ/∂v_n = −2x_n(F_{\min})` (simple eigenvalue) | `PROVED` |
| all numerical values (`x(F_{\min})`, bands, apex, `λ`'s, `½\log5`) | `DIAGNOSTIC-NUMERIC`, precisions in §5, §7 |
| facet at `w_ζ` = simple exposed point with a `0.33`-wide `10⁻⁵`-quasi-facet | `DIAGNOSTIC-NUMERIC` |
| `W_T ≠` box; `≥ 56%` of the coupling three-way | `DIAGNOSTIC-NUMERIC` |
| `λ_{\min}(A_{½\log5}) ≤ 3.20·10⁻¹²` (Galerkin upper bound) | `DIAGNOSTIC-NUMERIC`; (P153.3) **not** answered |
| `Ξ_a` exits `H` at `\log 2` | `DIAGNOSTIC-NUMERIC` (with the `P_T^{(a)} ⊄ P_T` caveat) |
| "`w_ζ` in the dual cone for all `T`" | `RESTATEMENT` (= Weil) |
| a prime-free closed form for `Ψ_T` | `OPEN`, expectation negative |
| D.16.2′ crossing height `2πe·e^{2T}` = R153_012's `H⋆` | `RESTATEMENT` (noted for R153_014) |

**FATAL rule: clean.** No zero-free region, no moment bound, no cancellation imported from a known theorem; zeros of `ζ`
are not used anywhere in this round. **No sign is claimed for `ζ` beyond `T ≤ \log 2`.**
