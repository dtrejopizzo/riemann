# Round 029-A — Damped weight `w_n = v_n cos(kπ log n/(4T))` with an hp finite-element basis

Global label: **NUMERICAL**. Continues 212-27 (ROUND_027_A/B/C). No paper nor the index was touched.

## 1. Method
- Form `a^w_T(F) = C_0‖F‖² + ∫_0^∞(c_F(0) − c_F(u))K(u)du − Σ w_n c_F(log n)` on `P_T`
  (P47 eq:Aform, lem:K; tail `G(s) = ∫_s^∞K = log coth(s/4) + π − 2 arctan e^{s/2}`, which at `s = 2T`
  gives the formula of thm:S(iii)). Only `n` with `Λ(n) > 0`, `log n < 2T` enter.
- Basis: orthonormal Legendre of degree `p − 1` per element, discontinuous (conforming: the form is finite
  for piecewise functions, since `c_F(0) − c_F(u) = O(u)`), mesh with uniform interior of step `≤ H`
  and geometric layers of ratio `σ` towards `±T` down to `h_min = c·e^{−2T}`.
- Archimedean part by pairs of elements `(e,f)`: `∫(δ − C_ef(u))K(u)du` split at the breakpoints
  `{a_f − b_e, a_f − a_e, b_f − b_e, b_f − a_e}`; on each piece the integrand is analytic (near
  `u = 0` the factor `I − C_ee(u)` vanishes linearly); Gauss in `u` (`2p + 16` nodes) and exact Gauss
  in `t`. Diagonal: `∫_0^{h_e}(I − C_ee)K + G(h_e)I`. Arithmetic: `C(log n)` exact. `P_T` via SVD.
- Levels `L = (H, p, σ, c)`: 1 `(0.5,6,.3,.3)`, 2 `(.35,8,.25,.1)`, 3 `(.25,10,.2,.03)`, 4 `(.2,12,.18,.01)`,
  5 `(.15,14,.15,3e−3)`, 6 `(.12,16,.15,1e−3)`, 7 `(.1,18,.15,3e−4)`. Galerkin ⇒ UPPER bounds.
- Scripts and outputs: `free_weight_scripts/hp.py`, `run_hp.py`, `val_hp.py`, `qcheck.py`, `indep.py`,
  `profile.py`, `scanH.py`; outputs and vectors in `free_weight_scripts/hp_out/`.

## 2. Validation
- `λ_A(½log3)`: `9.66e−4, 9.488e−4, 9.479e−4` (p = 6, 8, 10). `λ_A(log 2)`: `3.4e−6, 1.04e−7, 9.90e−8`.
- `k = 1`, comparison with previous converged values: `T = 0.8`: `+0.012689`; `1.2`: `+0.002291`;
  `1.6`: `+3.96e−4`; `2.0`: `+9.84e−5` (L4); `2.4`: `+2.562e−5` (L4–L7 equal to 4 digits). They agree.
- Control with the true weight `v` (step 5): `|λ_min| ≤ 1.2e−13` at all `T` (0.8–3.6) and levels;
  grows with `N` like rounding. No appreciably negative value appears.
- Quadrature: `T = 3.6`, L1, `u`-nodes 28 → 60: `max|ΔA| = 1.9e−11`, `λ_min` equal to 12 digits.
- Independent evaluation of the minimizer at `T = 3.6` (L1, `k = 1`) with direct `c_F(u)` and
  adaptive quadrature in `u`: `a = −2.440775e−4`, identical; `‖F‖ = 1`, constraints `≈ 1e−14`.
  Same at `T = 3.35` (L4): `a = −1.137518e−5`, identical to the stored eigenvalue.
- Independent code (global Legendre, `taper.py`) at `T = 3.6`, `k = 1`: `−2.93e−4` (N=80),
  `−4.72e−4` (N=120). Confirms the sign.

## 3. Finding about resolution
The previous diagnosis ("the basis does not resolve the boundary `e^{−2T}`") is NOT what limits: with fixed `H`,
refining only the boundary (`c` 1e−2 → 1e−4) does not change the value; refining the INTERIOR does
(`T = 3.2`, `p = 10`: `H = .25, .12, .06, .03` → `1.88e−5, 6.12e−6, 2.138e−6, 2.053e−6`).
The positive minimizers are high-frequency packets filling the window:
`T = 2.8`: even, `ω ≈ 74`, 71 % of the mass at distance `> 1.5` from the boundary; `T = 3.2`: odd, `ω ≈ 126`.
A global basis of 240 cosines does not reach those frequencies with the full support.

## 4. Tables (λ_min, `‖F‖ = 1`)
`k = 1` by level:

| T | L1 | L2 | L3 | L4 | L5 | L6 | L7 | status |
|---|---|---|---|---|---|---|---|---|
| 2.4 | 4.68e−4 | 1.07e−4 | 4.34e−5 | 2.564e−5 | 2.562e−5 | 2.562e−5 | 2.562e−5 | POSITIVE converged |
| 2.8 | 2.79e−4 | 6.05e−5 | 2.78e−5 | 1.15e−5 | 6.955e−6 | 6.932e−6 | 6.927e−6 | POSITIVE converged (~0.1 %) |
| 3.2 | 1.89e−4 | 4.19e−5 | 1.88e−5 | 7.70e−6 | 3.71e−6 | 2.080e−6 | 2.060e−6 | POSITIVE converged (~1 %; H=.03: 2.053e−6) |
| 3.3 | — | — | 1.73e−5 | 8.06e−6 | 3.33e−6 | 8.11e−7 | 4.10e−7 | UNDECIDED (drops ×2 per level) |
| 3.35 | — | — | 1.36e−5 | −1.14e−5 | −3.33e−5 | −4.06e−5 | — | NEGATIVE |
| 3.4 | 1.87e−4 | 3.66e−5 | −4.72e−5 | −9.96e−5 | −1.287e−4 | −1.403e−4 | — | NEGATIVE |
| 3.6 | −2.44e−4 | −5.08e−4 | −7.63e−4 | −8.78e−4 | −9.73e−4 | −1.006e−3 | — | NEGATIVE |

Since these are upper bounds, each negative value already decides "crosses"; the sequence only refines the magnitude.
Extrapolation (`T = 3.6`, differences 1.15e−4, 9.5e−5, 3.3e−5): `λ ≈ −1.03e−3 ± 3e−5`.

`k = 0.9, 1.1` (best level; "c" = converged, "nc" = not converged):

| T | k = 0.9 | k = 1.0 | k = 1.1 |
|---|---|---|---|
| 2.4 | +2.076e−5 c | +2.562e−5 c | +3.099e−5 c |
| 2.8 | +5.623e−6 c | +6.927e−6 c | +8.357e−6 c |
| 3.2 | +1.676e−6 c (~1 %) | +2.060e−6 c | −5.68e−4 NEG |
| 3.3 | +1.30e−6 nc | +4.1e−7 nc | −1.08e−3 NEG |
| 3.35 | +1.29e−6 nc | −4.06e−5 NEG | −1.49e−3 NEG |
| 3.4 | +1.23e−6 nc | −1.40e−4 NEG | −2.09e−3 NEG |
| 3.6 | −4.82e−3 NEG | −1.006e−3 NEG | −4.81e−3 NEG |

## 5. Verdict by T (question: `k = 1`)
- `T = 2.4`: POSITIVE converged, `+2.562e−5`.
- `T = 2.8`: POSITIVE converged, `+6.93e−6` (the `+7.0e−6` of 240 cosines was close;
  the `+2.8e−5` of basis 130 was not).
- `T = 3.2`: POSITIVE converged, `+2.05e−6 … +2.06e−6`.
- `T = 3.3`: UNDECIDED (`+4.1e−7` at L7, without convergence).
- `T = 3.35, 3.4, 3.6`: NEGATIVE (decided by upper bound; verified with independent evaluator and code
  at 3.6). **The damping `k = 1` crosses zero between `T = 3.2` and `T = 3.35`**,
  probably near `T ≈ 3.3`.
- Decay law on the positive stretch: `2.4 → 2.8 → 3.2` gives local rates `e^{−3.27T}`, `e^{−3.04T}`
  (consistent with `≈ e^{−3.4T}` of 212-27 for `T ≤ 2.4`); the crossing does NOT follow that law: it is produced by
  another branch of eigenvectors that drops sharply (below).

## 6. Negative minimizing vector (step 3)
- `T = 3.6`, L6, `k = 1`: `λ = −1.006e−3`; `Arch = 0.12713`, damped sum `= 0.12814`
  (`‖F‖ = 1`). EVEN (odd mass `1.3e−5`); 35 % of the mass at distance `0.01–0.1` from the boundary, 20 % in
  `0.1–0.5`, 34 % in `0.5–1.5`, 12 % further in; dominant interior frequency `ω ≈ 0.95` (more
  components at `ω ≈ 14–25`). Boundary layer of width `≍ 0.01–0.1`, not `e^{−2T} ≈ 7e−4`.
- `T = 3.35`, L6: `λ = −4.06e−5`, `Arch = 1.29781`, sum `= 1.29786`; even, 40 % in `0.01–0.1` from the
  boundary, `ω ≈ 31–42`. Same type (even, boundary layer + low frequency).
- `T = 3.2`, `k = 1.1` (negative): even, 43 % in `0.01–0.1` from the boundary, `ω ≈ 1.1`. The same branch appears
  earlier for `k > 1`.
- Stored profiles: `hp_out/vec_T*_L*_k*.npz` (coefficients, mesh, `λ`, Arch, sum) and
  `*_profile.txt` (`t`, `F(t)`).

## 7. Window of `k` (step 4)
Up to `T = 2.8` the three `k` are positive and `λ` grows with `k` (high-frequency branch). From
`T = 3.2` the even boundary branch turns negative first at `k = 1.1`, then (`T ≈ 3.3`) at `k = 1`; at
`3.4` only `k = 0.9` remains positive (not converged); at `3.6` all three are negative of order `1e−3`.
`k = 1` is not an isolated point for `T ≤ 3.2`; the admissible interval shifts towards `k < 1` and
narrows; at `T = 3.6` it does not contain `0.9, 1, 1.1` (other `k` were not tried there).

## 8. Limits
- The NEGATIVES are upper bounds with independent verification; the "converged" POSITIVES
  are so empirically (stability across levels and across refinement in `H` and in `p`); there is no
  rigorous lower bound nor interval arithmetic.
- The frequency of the positive minimizer grows with `T` (`ω ≈ 74 → 126`); at larger `T` a smaller
  `H` is needed. `T = 3.3` and `k = 0.9` at `3.3–3.4` remain without convergence.
- `k` outside `{0.9, 1, 1.1}` and other damping shapes were not explored.
