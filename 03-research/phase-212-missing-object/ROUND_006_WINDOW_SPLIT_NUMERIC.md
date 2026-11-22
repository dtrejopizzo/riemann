# Round 6 — Window-dependent local distribution at T = 0.5925 (NUMERICAL)

Everything that follows is NUMERICAL except where indicated. It validates one point; it proves nothing. Script:
`verify_window_split.py` (arguments: T, N modes, NC cells, control iterations, nodes per cell).

## 1. Setup

T = 0.5925, primes 2 and 3 (the only contacts: log 4 > 2T). Basis s_k(t) = T^{−1/2} sin(kω(t + T)), ω = π/(2T),
k ≤ N, projected onto P_T (two moment conditions). With ε_F(u) = c_F(0) − c_F(u) = ½‖F − F_u‖²,

    Arch(F) = C_0‖F‖² + ∫_0^∞ ε_F K du = ∫ W(t)F(t)² dt + ¼ ∬_{I_T×I_T} K(|t − s|)(F(t) − F(s))² dt ds,
    W(t) = C_0 + ½[(π − G(T − t)) + (π − G(T + t))],   G(u) = log tanh(u/4) + 2 arctan e^{u/2},

(PROVED, direct computation: ¼∬_{ℝ²} = ¼∬_{I×I} + ½∫F²·∫_{s∉I}K), Π_p(F) = v_p c_F(log p), a_T = Arch − Π_2 − Π_3.
The matrix of Arch was built in both ways; with 2400 nodes they differ by 2.8·10⁻⁵ per entry.
Bottom of a_T on P_T in the model: 1.32·10⁻⁴ (N = 20), 1.26·10⁻⁴ (N = 30), 1.25·10⁻⁴ (N = 40).
Bottom of Arch − Π_2: −0.029.

## 2. Distribution classes

One maximizes τ with r_2 − Π_2 ⪰ τ and Arch − r_2 − Π_3 ⪰ τ on P_T. Ceiling: τ ≤ ½ λ_min(a_T|P_T).

- LK (phase 159, G2_B8_R5): r_2 = c_2‖F‖² + ∫_0^{2T} ϑ(u)K ε_F du, 0 ≤ ϑ ≤ 1.
- P: r_2 = ∫W_2(t)F² + ϑ·¼∬K(ΔF)², ϑ constant, W_2 free.
- M: r_2 = ∫W_2(t)F² + ¼∬ϑ(|t − s|)K(ΔF)², W_2 free.
- DIR: r_2 = ∫W_2(t)F² + ¼∬θ(t, s)K(|t − s|)(F(t) − F(s))² dt ds, 0 ≤ θ = θ(s, t) ≤ 1, W_2 free.
  θ and W_2 piecewise constant on NC equal cells.

## 3. Results

N = 20, NC = 12:

| class | τ |
|---|---|
| LK | −1.56·10⁻³ |
| P | −3.30·10⁻² |
| M | −1.60·10⁻⁴ |
| DIR | +6.5665·10⁻⁵ (equal to the ceiling) |

DIR by resolution (ceiling in parentheses):

| N | NC | τ |
|---|---|---|
| 20 | 2 | −8.4·10⁻² |
| 20 | 4 | −2.7·10⁻² |
| 20 | 6 | −3.4·10⁻³ |
| 20 | 8 | −2.3·10⁻³ |
| 20 | 12, 16 | +6.5665·10⁻⁵ (6.5665·10⁻⁵) |
| 30 | 12 | −7.2·10⁻⁵ |
| 30 | 16, 20, 24 | +6.2925·10⁻⁵ (6.2925·10⁻⁵) |
| 40 | 12 | −1.3·10⁻⁴ |
| 40 | 20, 24 | +6.253·10⁻⁵ (6.2530·10⁻⁵) |

LK with the same meshes: −1.56·10⁻³ (N = 20), −2.73·10⁻³ (N = 30), −3.03·10⁻³ (N = 40).

## 4. Reading

1. In the DIR class the distribution exists and reaches the ceiling as soon as NC ≳ N/2 (one cell per wavelength
   of the highest mode), in the three sizes tested. With fewer cells it fails.
2. The intermediate classes fail: a position-dependent potential (P) is not enough, nor is distributing the
   kernel according to distance (M). The kernel part must depend on both positions.
3. The solution found touches no bound (0 of 78 parameters at 0 or 1 with N = 20, NC = 12) and is not
   unique. Its shape has no meaning.
4. That the ceiling is reached exactly with an interior solution indicates that, once the mesh is resolved, the DIR class
   certifies whenever a_T ⪰ 0 in the model. If so in the continuum, "a DIR distribution exists" is a
   reformulation of the target in this window and not an object with a sign (reformulation pattern). It is not
   proved in either direction.
5. In terms of forms: q_p = r_p − Π_p has jump measure θ_pK + (v_p/2)δ(|t − s| − log p) ≥ 0 and a
   potential; the distribution is a partition of the jump measure and of the potential of a_T among the primes.

## 5. Duality (ARGUED; computation without a second reading)

Repeating the minimax argument of G2_B8_R5 Theorem D with the DIR class: since W_2 is free, the supremum
over W_2 is finite only if the two states have the same pointwise density ρ_{σ_2}(t) = ρ_{σ_3}(t)
(ρ_σ = Σ w_i|F_i|²), and the supremum over θ charges the pointwise maximum in (t, s) of D_p(t, s) = Σ w_i|F_i(t) −
F_i(s)|². The obstruction to a DIR distribution would be a pair of states of equal density with

    ∫Wρ + ¼∬K max(D_2, D_3) − Π_2(σ_2) − Π_3(σ_3) < 0.

The test pair of G2_B8_R5 §4 has different densities and is not admissible. For pure states of equal
density in a space of trigonometric polynomials, F_3 = ±F_2 and the value is a_T(F_2) ≥ 0; an
obstruction can only come from mixtures.

## 6. What is missing for this to be something

- A formula for θ_p(t, s) and W_p(t) that is not obtained by solving the problem (without it, it is circular:
  `RULES_AVOID.md` J3).
- The continuum: N → ∞ with arbitrary measurable θ.
- Three or more primes (T > ½ log 5) and large T.
- Controls: by construction the class cannot distinguish cΛ; it certifies exactly when the bottom is ≥ 0.

## 7. Second batch, with high-precision quadrature (NUMERICAL)

Script: `verify_window_split_canonical.py` (T, N, NC, c, mode ∈ {exist, box, canon}; environment variables
BYN = 1: one piece per prime power; NOPOW = 1: the powers p^k, k ≥ 2, are deleted; TH_LO, TH_HI: bounds
on θ in box mode). All integrands are analytic on their domain (autocorrelation with exact
limits; diagonal cells split into triangles; the total potential is obtained by subtraction), so that
Gauss quadrature converges spectrally. Bottom of a_T on P_T at T = 0.5925: 1.318997·10⁻⁴
(N = 20), 1.264204·10⁻⁴ (N = 30), 1.256310·10⁻⁴ (N = 40).

### 7.1 The smoothest distribution stabilizes

Among DIR distributions with q_2, q_3 ⪰ τ_0 (τ_0 = one quarter of the bottom) one minimizes
R = ∬|∂θ|² + ∫(W_2 − W/2)² (discretized). Maximum difference of θ_2 averaged over a common 6×6 mesh
between successive resolutions (N, NC): (20,12)→(20,24): 0.075; →(30,18): 0.031; →(30,24): 0.016;
→(40,24): 0.009. R_θ = 1.47, 1.21, 1.64, 1.76, 1.85. No parameter at a bound.

θ_2 on the 6×6 mesh (N = 40, NC = 24):

    0.57 0.40 0.39 0.45 0.52 0.58
    0.40 0.30 0.47 0.61 0.60 0.52
    0.39 0.47 0.62 0.68 0.61 0.45
    0.45 0.61 0.68 0.62 0.47 0.39
    0.52 0.60 0.61 0.47 0.30 0.40
    0.58 0.52 0.45 0.39 0.40 0.57

Features: (a) the mean by distance |t − s| is flat (0.48–0.51 up to |t − s| ≈ 0.8, rising to 0.65 at 2T);
(b) the mean by centre (t + s)/2 goes from 0.68 at the edges to 0.32 two thirds of the way and 0.62 at the
centre; (c) singular values of θ_2 − mean: 1.90, 1.87, 0.93, 0.23, 0.20, 0.05: effective rank three;
(d) W_2 − W/2 ≈ +0.41 on the two strips two thirds of the way and ≈ 0 elsewhere, stable across the five
resolutions.

### 7.2 The class does not distinguish the weight at T = 0.5925

With cΛ (N = 30, NC = 20): c = 0.80, bottom 1.88·10⁻², τ = ceiling; c = 0.95, bottom 5.97·10⁻³, τ = ceiling;
c = 1.01, 1.03, 1.10: negative bottom, τ = bottom/2.

### 7.3 The DIR class has its own threshold, near T = log 2

N = 30, NC = 20, two optimizers (one convex):

| T | bottom of a_T | τ (θ ∈ [0, 1]) |
|---|---|---|
| 0.62 | 2.28·10⁻⁵ | ceiling |
| 0.65 | 2.77·10⁻⁶ | ceiling |
| 0.67 | 7.35·10⁻⁷ | ceiling |
| 0.69 | 1.62·10⁻⁷ | ceiling |
| 0.70 | 7.37·10⁻⁸ | −7.3·10⁻⁴ |
| 0.71 | 3.22·10⁻⁸ | −8.1·10⁻³ |
| 0.72 | 1.29·10⁻⁸ | −2.6·10⁻² |
| 0.75 | 1.04·10⁻⁹ | −8.6·10⁻² |
| 0.80 | 9.2·10⁻¹² | −1.3·10⁻¹ |

Hence the DIR class with nonnegative parts is not equivalent to the target: it certifies up to a threshold
T_DIR ∈ [0.69, 0.70) and stops doing so with the form still positive. log 2 = 0.6931 is where n = 4 enters
and where a chain of three points t − log 2, t, t + log 2 fits in the window.

Controls on the cause: (i) one piece per prime power (2, 3, 4) does not repair it (τ = −6.5·10⁻⁴ at
0.70; −5.7·10⁻² at 0.75); (ii) deleting the n = 4 term, at T = 0.70 the form stays positive
(8.9·10⁻⁸) and the distribution still fails (−6.9·10⁻⁴): the n = 4 term is not the cause; (iii) with signed kernel
parts, θ ∈ [−1, 2], the distribution exists again near the ceiling (T = 0.70: 3.68·10⁻⁸;
T = 0.75: 3.6·10⁻¹⁰ against 5.2·10⁻¹⁰), and with θ ∈ [−0.2, 1.2] it exists at 0.70 and fails at 0.75. What
is lost at T ≈ log 2 is the nonnegativity of each prime's kernel part.

Side control: deleting n = 4, the bottom becomes −1.55·10⁻³ at T = 0.72 and −5.3·10⁻² at T = 0.75.

### 7.4 Limits

For T ≳ 0.85 the bottom of the model (≈ 10⁻¹⁴) is at the rounding level; one can only distinguish "fails by
a lot" from "compatible with zero". Nothing has been proved: neither existence of the distribution in the continuum for
T < log 2, nor non-existence for T > log 2, nor the identification of the threshold with log 2.

## 8. Where nonnegativity is lost past log 2 (NUMERICAL)

Mode `sdp` of `verify_window_split_canonical.py` (semidefinite program; requires cvxpy and clarabel).
`N = 30`, `NC = 20`, primes 2 and 3.

### 8.1 Third optimizer for the threshold

Maximum `τ` with `0 ≤ θ ≤ 1`: `T = 0.69`: `8.0834·10⁻⁸` (ceiling `8.0833·10⁻⁸`); `T = 0.70`: `−6.91·10⁻⁴`;
`T = 0.72`: `−2.553·10⁻²`; `T = 0.75`: `−8.582·10⁻²`. It agrees with the two optimizers of section 7.

### 8.2 Minimal borrowing

One writes `θ = u − n₂ + n₃` with `0 ≤ u ≤ 1`, `n₂, n₃ ≥ 0`, and minimizes the area fraction
`∬ (n₂ + n₃) / (2T)²` with both pieces `≥ −10⁻⁶` (relaxed margin: with margin equal to half the ceiling the
solver does not converge).

| `T` | borrowing | part `θ < 0` | part `θ > 1` |
|---|---|---|---|
| 0.69 | 0 | 0 | 0 |
| 0.70 | `4.7·10⁻³` | `4.7·10⁻³` | 0 |
| 0.72 | `5.2·10⁻²` | `2.1·10⁻²` | `3.2·10⁻²` |
| 0.75 | `1.24·10⁻¹` | `5.7·10⁻²` | `6.6·10⁻²` |

### 8.3 Localization

The borrowing is sparse: it occupies a few cells, symmetric under `(t,s) → (−s,−t)`.

- `T = 0.70`: a single cell and its mirror, `t ≈ −0.455`, `s ≈ 0.315`, `|t−s| ≈ 0.77`, `θ ≈ −0.47`.
- `T = 0.72`: `θ < 0` in three cells with `|t−s| ≈ 0.79` and `t ∈ [−0.47, −0.32]`; `θ > 1` (up to `3.85`)
  on the pair formed by the edge `t ≈ −T` and `s ≈ 0.32–0.40`, `|t−s| ≈ 1.01–1.08`, and its mirror.
- `T = 0.75`: the same picture (`θ < 0` at distance `0.75–0.83`, `θ > 1` from the edge at distance
  `1.05–1.13`), plus a second layer: `θ < 0` from the edge at distance `0.60–0.68` and `θ > 1` at
  distance `0.45`.

Reading, with cell resolution `h ≈ 0.07`: the distances lie between the contacts and not clearly on
them (`log 2 = 0.693`, `log(9/4) = 0.811`, `log 3 = 1.099`); the mesh does not allow
identifying them. The prediction "negative parts at the central points with a neighbour at distance `log 2`
on both sides" is not confirmed in that simple form: at onset (`T = 0.70`) the borrowing appears at
distance `≈ 0.77`, not at `log 2`, and far from the centre.

Caveat: minimizing an `L¹` norm favours sparse solutions by itself; sparsity is partly an
effect of the criterion. The positions are not unique by construction and the fine mesh is missing
(`N = 40`, `NC = 30` did not finish in the allotted time).

### 8.4 Fine mesh (`N = 40`, `NC = 30`, `h ≈ 0.048`)

Maximum `τ` with `0 ≤ θ ≤ 1`: `T = 0.70`: `−7.84·10⁻⁴`; `T = 0.72`: `−2.662·10⁻²`.
Minimal borrowing: `T = 0.70`: `5.3·10⁻³`; `T = 0.72`: `4.7·10⁻²` (coarse mesh: `4.7·10⁻³`, `5.2·10⁻²`).

Cells with excess (half `t + s ≤ 0`; the rest by mirror):

- `T = 0.70`: `(−0.677, 0.303)`, distance `0.980`, excess `+0.85`; `(−0.443, 0.350)`, distance `0.793`,
  excess `−0.34`.
- `T = 0.72`: `(−0.696, 0.312)`, distance `1.008`, excess `+4.04`; `(−0.456, 0.312)`, distance `0.768`,
  excess `−2.88`; `(−0.408, 0.408)`, distance `0.816`, excess `−5.00` (imposed bound `5`);
  `(−0.696, −0.072)`, distance `0.624`, excess `−0.88`.

Reading:

- Two distances persist under refinement: `≈ 0.77–0.82` with `θ < 0` and `≈ 0.98–1.01` with `θ > 1` from the
  edge. The second excludes `log 3 = 1.099` (the cell covers `±0.048`). The first is compatible with
  `log(9/4) = 0.811` without identifying it.
- The total borrowing is stable between meshes; the specific cells are not, and one value touches the bound. The
  area minimum concentrates under refinement: as a criterion it is ill-posed for reading a limiting shape.
- The localization of the borrowing does not deliver a rule. The well-defined object for `T > log 2` is the
  dual of the problem with `0 ≤ θ ≤ 1` (the pair of obstructing states), which is essentially unique and does not
  depend on a selection criterion.

## 9. The obstructing pair past log 2 (NUMERICAL)

Mode `dual` of the script: dual variables `Y₂, Y₃ ⪰ 0` of the two constraints of the program "maximum `τ`
with `0 ≤ θ ≤ 1`".

### 9.1 Verification of the duality of section 5

In all cases `tr Y₂ = tr Y₃ = ½`, the densities per cell coincide (`≤ 1.4·10⁻¹⁶`) and

`−tr(Y₂Π₂) + tr(Y₃(Arch − Π₃)) + Σ_cells max(D, 0) = τ`,  `D = ` pair energy of `Y₂` minus that of `Y₃`,

reproduces the primal value in all digits (`T = 0.70`: `−6.911123·10⁻⁴`). Duality is
checked in the discretization; it remains unproved in the continuum.

### 9.2 Shape of the states

Effective rank 4–5 each. `T = 0.70`, `N = 30`: eigenvalues of `Y₂`: `0.276, 0.185, 0.025, 0.010`;
of `Y₃`: `0.257, 0.170, 0.047, 0.026`. The two principal eigenfunctions (one even with three lobes,
one odd) nearly coincide between `Y₂` and `Y₃`. Common density with maxima at `t ≈ ±0.30` and minima at
`0` and `±0.47`. At `T = 0.75`, `Y₂` is nearly rank one (`0.469`) and `Y₃` rank two (`0.311, 0.180`).

### 9.3 Optimal distribution: all or nothing, by distance bands

`θ₂ = 1` where `D > 0`, `θ₂ = 0` where `D < 0`. The sign of `D(t,s)` depends almost only on `|t − s|`:

| band of `|t − s|` | `θ₂` | contact within the band |
|---|---|---|
| `≈ 0.15–0.55` | 1 | none |
| `≈ 0.63–0.85` (maximum of `|D|` at `0.70–0.75`) | 0 | `log 2 = 0.693` |
| `≈ 0.93–1.17` (maximum at `1.03–1.10`) | 1 | `log 3 = 1.099` |
| `≳ 1.2` (maximum at `1.3–1.4`) | 0 | `log 4 = 1.386` |

Stable at `T = 0.70, 0.72, 0.75` and on both meshes (`h ≈ 0.07` and `h ≈ 0.05`). At the transition
distances there are cells of both signs (the band edges curve towards the ends of the window)
and near the diagonal `D ≈ 0`.

Deficit values: `T = 0.70`: `−6.91·10⁻⁴` (`N=30`), `−7.84·10⁻⁴` (`N=40`); `T = 0.75`: `−8.58·10⁻²`,
`−8.30·10⁻²`. Not converged to more than one digit.

### 9.4 Reading (without proof)

Each prime gives up the kernel at the distances of its own contacts. Heuristic: the kernel at
distance `u` controls `∫(F(t) − F(t+u))²`, which is small exactly when `c_F(u)` is large; to
bound `v_p c_F(log p)` that control is useless, and that of the other distances is useful.

It does not by itself explain the threshold at `log 2`. Past the threshold, the optimum resembles a distribution that
only sees distance (class M of section 2); the positional freedom that reached the ceiling below
`log 2` does not appear in the obstructing pair.

## 10. Reopening trials after `REVIEW_006.md` (NUMERICAL)

Modes `mclass` and `transfer` of the script. `N = 30`, `NC = 20` unless indicated.

### 10.1 Class M at `T = 0.5925`

`θ = φ(|t − s|)` with `0 ≤ φ ≤ 1` and `W₂(t)` free: `τ = −6.04·10⁻⁴` (`N = 30`), `−5.75·10⁻⁴` (`N = 40`,
`NC = 30`); ceiling `6.3·10⁻⁵`. The value `−1.6·10⁻⁴` of section 3 (`N = 20`) was not converged. Class M
fails; reaching the ceiling below the threshold requires a two-position `θ`.

### 10.2 Minimal transfer between the two pieces

An arbitrary form `X` is added: `q₂ + X ⪰ −10⁻⁶`, `q₃ − X ⪰ −10⁻⁶`, with `q_p` in the DIR class, and the
nuclear norm of `X` is minimized.

| `T` | nuclear norm | eigenvalues of `X` |
|---|---|---|
| 0.695 | `1·10⁻¹⁴` | — (the distribution exists) |
| 0.70 | `2.14·10⁻²` (`N = 40`: `2.73·10⁻²`) | one positive; the rest `≤ 10⁻¹¹` |
| 0.71 | `1.21·10⁻¹` | one positive; the rest `≤ 10⁻¹⁰` |
| 0.72 | `2.39·10⁻¹` (`N = 40`: `2.46·10⁻¹`) | one positive; the rest `≤ 10⁻⁸` |
| 0.75 | `5.33·10⁻¹` | two positive: `0.449`, `0.084` |

- The threshold of the DIR class is between `0.695` and `0.70`: above `log 2 = 0.6931`, not at it.
- `X = λ ℓ ⊗ ℓ` with `ℓ` even. At the optimum `q₃ ⪰ 0` and `q₂` has a single negative eigenvalue
  (`−1.8·10⁻²` at `0.70`, `−0.20` at `0.72`; two at `0.75`: `−0.39`, `−0.059`); `ℓ` is that direction
  (overlap `0.92–0.95`).
- Shape of `ℓ` stable in `T` and in the mesh: positive at the centre, negative around `±0.4`, large
  near the edges. Overlap with the projection of `cos(2πt/log 2)` onto `P_T`: `0.91–0.93`; the
  best cosine has period `0.707–0.736`, increasing with `T`. Overlap with the lowest eigenvector
  of `a|P_T`: `0.60–0.62`; with the third: `0.35–0.42`. No candidate identifies it.
- Caveat: the nuclear norm favours low rank by itself. With `ℓ` free the format is the signed
  distribution (empty). There is no formula for `ℓ`, and the number of squares grows with `T`.

### 10.3 Dependence on the weight in these windows

Bottom of `a_T` on `P_T` with `cΛ` (primes 2, 3 and the term for 4):

| `c` | `T = 0.70` | `T = 0.75` |
|---|---|---|
| 0.98 | `−1.5·10⁻³` | `−2.9·10⁻³` |
| 0.995 | `−1.5·10⁻⁴` | `−6.6·10⁻⁴` |
| 0.999 | `+4.5·10⁻⁵` | `−1.2·10⁻⁴` |
| 1 | `+7.4·10⁻⁸` | `+1.0·10⁻⁹` |
| 1.001 | `−2.6·10⁻⁴` | `−4.7·10⁻⁴` |
| 1.005 | `−1.7·10⁻³` | `−2.5·10⁻³` |
| 1.02 | `−9.7·10⁻³` | `−1.2·10⁻²` |

The bottom of `Arch` alone is `−0.154` (`T = 0.70`). In these windows the form is positive only on an
interval of `c` of width `≲ 10⁻³` around 1. The claim "generic in `c`" of section 7.2
holds at `T = 0.5925` (where `Arch ⪰ 0` on `P_T`) and not here: every exact certificate at `T ≥ 0.70`
distinguishes `c = 1` with that precision. Resolution `N = 30`; no convergence control in `c`.

### 10.4 Clarifications after the cross-check (`ANNEX_COTEJO_NULLDIR.md`)

- Section 10.3 contributes nothing new: the narrow two-sided window in `c`, the ladder of tiny
  eigenvalues, concavity in `c` and the derivative `−Π(F*)` are in phase 211 (`ROUND_003_A.md`,
  `ROUND_002_D.md`, `ROUND_002_E.md`, `ROUND_021_A.md`) and in Paper 46. The width of the window in `c` is
  the margin up to constants.
- There is no exact contact on both sides: `Π(F*) > 0`, hence the maximum in `c` is attained at `c* < 1`
  strictly and 1 is interior to the positivity interval.
- "`Arch ⪰ 0` on `P_T` at `T = 0.5925`" is NUMERICAL: that value falls in the interval `[0.58, 0.60]` that the
  proved threshold does not decide.
