# R162_2001 — O1901.1: two-parameter comb Type I search

Numerics. **Everything in this file is UNCERTIFIED double-precision float. Nothing here has proof status.**
Inputs: R162_1901 (Theorem 1, §3, §4 falsifier), R162_1803 (base numerics), R162_1590/1601 (tail-sign fix).
Scripts (new, in `scripts/c3/`): `t2001_typeI_search.py` (operator), `t2001_grid.py` (grid), `t2001_fine.py` (fine s₂
scans), `t2001_locate.py` (Type I root), `t2001_tmax.py` (cutoff robustness). Raw grids: `t2001_grid_K34.jsonl` (289
points), `t2001_grid_K46_partial.jsonl` (68 points, run stopped when the fine scans took priority).

**Outcome (UNCERTIFIED): the falsifier fires.** ⟨u₂,φ̂⟩ at the first even contact changes sign along a connected arc of
first contacts in the positive cone, and the zero is a Type I first contact in the sense of R162_1901 Theorem 1:
μ₂ = λ = ⟨u₂,φ̂⟩ = 0 at T_*, g(0) ≈ −0.41 < 0, N₋ = 1 → 2, f(0) continuous through T_*. This happens on a curve
s₂ = s₂^c(s₃) ≈ 0.9998–0.99995, i.e. within 2.4·10⁻⁴ of the ζ weight at 2. It is K-stable (34/46) and cutoff-stable.
If certified, R-C.b is false weight-blind and must use the arithmetic of Λ (here: the exact weight at 2).

## 0. Setup and normalisation

- Comb: a = s₂·w₂·δ_{log 2} + s₃·w₃·δ_{log 3} with w_n = 2Λ(n)/√n (the 1803 convention: s₂ = s₃ = 1 gives the ζ
  weights at 2 and 3). No other n. For T < ½log 4 = 0.6931 the case s₂ = s₃ = 1 **is** the ζ form; beyond that it is ζ
  minus n = 4, 5, ….
- A^ev_T = archimedean multiplier (digamma, fixed tail sign) − comb, Legendre–Galerkin, even Legendre modes of
  0..K−1; K = 34 and 46. φ = cosh(t/2), φ̂ = φ/‖φ‖.
- λ = bottom of A^ev on φ^⊥. T_* = first zero of λ (scan on T ∈ [0.30,1.2] step 0.01 (grid) or 0.004 (fine), then brentq).
  λ > 0 on (0,0.30] for every point (no prime below T = ½log 2).
- μ₁ < μ₂ < μ₃ eigenvalues of A^ev, u₂ normalised > 0 at t = 0⁺. r₂ = ⟨u₂,φ̂⟩². g(0) = Σ_{k≠2} r_k/μ_k,
  f(0) = g(0) + r₂/μ₂ (residues w.r.t. the unit vector φ̂). T_μ₂ = first zero of μ₂.

## 1. Grid [0,4]², step 0.25 (K = 34 full; K = 46 on 68 points). Shown at step 0.5.

**T_* (K=34)** (rows s₂, columns s₃)

| s₂ \ s₃ | 0 | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0.5958 | 0.5791 | 0.5704 | 0.5650 | 0.5613 | 0.5587 | 0.5567 | 0.5552 | 0.5540 |
| 0.5 | 0.7919 | 0.6177 | 0.5875 | 0.5747 | 0.5674 | 0.5626 | 0.5594 | 0.5571 | 0.5553 |
| 1 | 0.5927 | 0.6059 | 0.7167 | 0.5657 | 0.5603 | 0.5574 | 0.5556 | 0.5543 | 0.5533 |
| 1.5 | 0.4259 | 0.4259 | 0.4259 | 0.4259 | 0.4259 | 0.4259 | 0.4259 | 0.4259 | 0.4259 |
| 2 | 0.3960 | 0.3960 | 0.3960 | 0.3960 | 0.3960 | 0.3960 | 0.3960 | 0.3960 | 0.3960 |
| 2.5 | 0.3804 | 0.3804 | 0.3804 | 0.3804 | 0.3804 | 0.3804 | 0.3804 | 0.3804 | 0.3804 |
| 3 | 0.3709 | 0.3709 | 0.3709 | 0.3709 | 0.3709 | 0.3709 | 0.3709 | 0.3709 | 0.3709 |
| 3.5 | 0.3646 | 0.3646 | 0.3646 | 0.3646 | 0.3646 | 0.3646 | 0.3646 | 0.3646 | 0.3646 |
| 4 | 0.3602 | 0.3602 | 0.3602 | 0.3602 | 0.3602 | 0.3602 | 0.3602 | 0.3602 | 0.3602 |

**μ₂^ev(T_*) (K=34)** (rows s₂, columns s₃)

| s₂ \ s₃ | 0 | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3.8e-02 | 3.6e-02 | 3.5e-02 | 3.4e-02 | 3.3e-02 | 3.2e-02 | 3.2e-02 | 3.1e-02 | 3.1e-02 |
| 0.5 | 3.9e-02 | 9.1e-03 | 7.7e-03 | 7.2e-03 | 6.9e-03 | 6.7e-03 | 6.5e-03 | 6.3e-03 | 6.1e-03 |
| 1 | 4.2e-10 | 3.7e-10 | 2.5e-16 | 3.2e-11 | 4.4e-11 | 5.0e-11 | 5.4e-11 | 4.8e-11 | 5.8e-11 |
| 1.5 | 4.6e-04 | 4.6e-04 | 4.6e-04 | 4.6e-04 | 4.6e-04 | 4.6e-04 | 4.6e-04 | 4.6e-04 | 4.6e-04 |
| 2 | 7.9e-04 | 7.9e-04 | 7.9e-04 | 7.9e-04 | 7.9e-04 | 7.9e-04 | 7.9e-04 | 7.9e-04 | 7.9e-04 |
| 2.5 | 9.2e-04 | 9.2e-04 | 9.2e-04 | 9.2e-04 | 9.2e-04 | 9.2e-04 | 9.2e-04 | 9.2e-04 | 9.2e-04 |
| 3 | 9.5e-04 | 9.5e-04 | 9.5e-04 | 9.5e-04 | 9.5e-04 | 9.5e-04 | 9.5e-04 | 9.5e-04 | 9.5e-04 |
| 3.5 | 9.3e-04 | 9.3e-04 | 9.3e-04 | 9.3e-04 | 9.3e-04 | 9.3e-04 | 9.3e-04 | 9.3e-04 | 9.3e-04 |
| 4 | 8.8e-04 | 8.8e-04 | 8.8e-04 | 8.8e-04 | 8.8e-04 | 8.8e-04 | 8.8e-04 | 8.8e-04 | 8.8e-04 |

**⟨u₂,φ̂⟩(T_*) (K=34)** (rows s₂, columns s₃)

| s₂ \ s₃ | 0 | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | -1.4e-01 | -1.3e-01 | -1.3e-01 | -1.3e-01 | -1.3e-01 | -1.3e-01 | -1.3e-01 | -1.3e-01 | -1.3e-01 |
| 0.5 | -7.7e-02 | -6.3e-02 | -5.9e-02 | -5.8e-02 | -5.7e-02 | -5.6e-02 | -5.6e-02 | -5.5e-02 | -5.4e-02 |
| 1 | +1.3e-05 | +1.2e-05 | +2.6e-10 | +3.7e-06 | +4.4e-06 | +4.7e-06 | +4.9e-06 | +5.0e-06 | +5.0e-06 |
| 1.5 | +1.6e-02 | +1.6e-02 | +1.6e-02 | +1.6e-02 | +1.6e-02 | +1.6e-02 | +1.6e-02 | +1.6e-02 | +1.6e-02 |
| 2 | +2.2e-02 | +2.2e-02 | +2.2e-02 | +2.2e-02 | +2.2e-02 | +2.2e-02 | +2.2e-02 | +2.2e-02 | +2.2e-02 |
| 2.5 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 |
| 3 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 |
| 3.5 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 | +2.5e-02 |
| 4 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 | +2.4e-02 |

**g(0) at T_* (K=34)** (rows s₂, columns s₃)

| s₂ \ s₃ | 0 | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | -0.487 | -0.501 | -0.508 | -0.512 | -0.515 | -0.517 | -0.518 | -0.518 | -0.518 |
| 0.5 | -0.153 | -0.432 | -0.453 | -0.463 | -0.468 | -0.472 | -0.474 | -0.475 | -0.476 |
| 1 | -0.410 | -0.400 | -0.334 | -0.430 | -0.435 | -0.437 | -0.439 | -0.440 | -0.440 |
| 1.5 | -0.565 | -0.565 | -0.565 | -0.565 | -0.565 | -0.565 | -0.565 | -0.565 | -0.565 |
| 2 | -0.605 | -0.605 | -0.605 | -0.605 | -0.605 | -0.605 | -0.605 | -0.605 | -0.605 |
| 2.5 | -0.630 | -0.630 | -0.630 | -0.630 | -0.630 | -0.630 | -0.630 | -0.630 | -0.630 |
| 3 | -0.647 | -0.647 | -0.647 | -0.647 | -0.647 | -0.647 | -0.647 | -0.647 | -0.647 |
| 3.5 | -0.660 | -0.660 | -0.660 | -0.660 | -0.660 | -0.660 | -0.660 | -0.660 | -0.660 |
| 4 | -0.670 | -0.670 | -0.670 | -0.670 | -0.670 | -0.670 | -0.670 | -0.670 | -0.670 |

**T_μ₂ − T_* (K=34)** (rows s₂, columns s₃)

| s₂ \ s₃ | 0 | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 2.3e-02 | 1.1e-02 | 6.1e-03 | 3.8e-03 | 2.6e-03 | 1.7e-03 | 1.2e-03 | 8.9e-04 | 5.9e-04 |
| 0.5 | 3.4e-02 | 9.0e-03 | 3.0e-03 | 1.5e-03 | 8.7e-04 | 5.5e-04 | 3.4e-04 | 2.3e-04 | 1.6e-04 |
| 1 | 4.9e-09 | 6.1e-09 | -5.6e-11 | 4.2e-10 | 3.2e-10 | 2.4e-10 | 1.9e-10 | 1.3e-10 | 9.2e-11 |
| 1.5 | 1.6e-04 | 1.6e-04 | 1.6e-04 | 1.6e-04 | 1.6e-04 | 1.6e-04 | 1.6e-04 | 1.6e-04 | 1.6e-04 |
| 2 | 1.2e-04 | 1.2e-04 | 1.2e-04 | 1.2e-04 | 1.2e-04 | 1.2e-04 | 1.2e-04 | 1.2e-04 | 1.2e-04 |
| 2.5 | 7.9e-05 | 7.9e-05 | 7.9e-05 | 7.9e-05 | 7.9e-05 | 7.9e-05 | 7.9e-05 | 7.9e-05 | 7.9e-05 |
| 3 | 5.0e-05 | 5.0e-05 | 5.0e-05 | 5.0e-05 | 5.0e-05 | 5.0e-05 | 5.0e-05 | 5.0e-05 | 5.0e-05 |
| 3.5 | 3.2e-05 | 3.2e-05 | 3.2e-05 | 3.2e-05 | 3.2e-05 | 3.2e-05 | 3.2e-05 | 3.2e-05 | 3.2e-05 |
| 4 | 2.1e-05 | 2.1e-05 | 2.1e-05 | 2.1e-05 | 2.1e-05 | 2.1e-05 | 2.1e-05 | 2.1e-05 | 2.1e-05 |

**K-stability (K=34 vs K=46), all points where K=46 was run**

| (s₂,s₃) | T_* 34/46 | μ₂(T_*) 34/46 | ⟨u₂,φ̂⟩ 34/46 |
|---|---|---|---|
| (0.0, 0.0) | 0.59582/0.59582 | 3.836e-02/3.836e-02 | -0.1366/-0.1366 |
| (0.0, 2.0) | 0.56134/0.56128 | 3.305e-02/3.303e-02 | -0.1304/-0.1304 |
| (0.0, 4.0) | 0.55401/0.55391 | 3.061e-02/3.050e-02 | -0.1259/-0.1257 |
| (0.25, 0.0) | 0.63253/0.63252 | 2.392e-02/2.392e-02 | -0.1026/-0.1026 |
| (0.25, 2.0) | 0.56444/0.56435 | 1.720e-02/1.719e-02 | -0.0920/-0.0919 |
| (0.25, 4.0) | 0.55469/0.55456 | 1.550e-02/1.542e-02 | -0.0878/-0.0875 |
| (0.5, 0.0) | 0.79187/0.79182 | 3.930e-02/3.930e-02 | -0.0774/-0.0774 |
| (0.5, 2.0) | 0.56737/0.56728 | 6.937e-03/6.933e-03 | -0.0570/-0.0570 |
| (0.5, 4.0) | 0.55526/0.55505 | 6.139e-03/6.093e-03 | -0.0541/-0.0539 |
| (0.75, 0.0) | 0.71920/0.71910 | 6.416e-07/6.383e-07 | +0.0005/+0.0005 |
| (0.75, 2.0) | 0.57012/0.57000 | 1.490e-03/1.490e-03 | -0.0258/-0.0258 |
| (0.75, 4.0) | 0.55568/0.55540 | 1.312e-03/1.302e-03 | -0.0245/-0.0244 |

Max |Δ| over 68 K=46 points: T_* 3.1e-04, μ₂ 1.1e-04, ⟨u₂,φ̂⟩ 2.6e-04.
N₋ just before T_μ₂:  {1}  none-contact count: 0
max g0 at T_*: -0.1525921224493134

Reading of the grid:
- A contact T_* ∈ (0,1.2] exists at every grid point. N₋ = 1 just before every T_μ₂; g(0) < 0 at every T_*
  (max −0.153). So every point is on the admissible part {g(0) < 0, N₋ = 1 before} of R162_1901 §4.
- **Every grid contact is Type II** (μ₂(T_*) > 0, T_μ₂ > T_*), except that on the row s₂ = 1 the margin collapses:
  μ₂(T_*) ~ 10⁻¹⁰, ⟨u₂,φ̂⟩ ~ 10⁻⁵, T_μ₂ − T_* ~ 10⁻⁹ (the Perron–Tate near-alignment of 1803 §3 for ζ, now for every s₃).
- For s₂ ≥ 1.25 the contact occurs before ½log 3 = 0.5493, so it does not depend on s₃ (constant rows).
- Sign of ⟨u₂,φ̂⟩(T_*): negative for s₂ ≤ 0.75 (except (0.75,0)), positive for s₂ ≥ 1.25. The change happens at
  s₂ ≈ 1. (The isolated + at (0.75,0), T_* = 0.719 > ½log 4, is a second small-margin region not resolved here.)

## 2. Fine scans across s₂ = 1 (K = 34 / 46, s₃ fixed)

T_* is **continuous** in s₂ across the sign change, and T_μ₂ − T_* → 0 there. Excerpt, s₃ = 2.5:

| s₂ | T_* K=34 | T_* K=46 | μ₂(T_*) K=46 | ⟨u₂,φ̂⟩(T_*) K=34 | K=46 | g(0) | T_μ₂ − T_* K=46 |
|---|---|---|---|---|---|---|---|
| 0.985 | 0.561930 | 0.561744 | 2.59e-06 | −1.060e-03 | −1.060e-03 | −0.434 | 3.5e-06 |
| 0.995 | 0.559738 | 0.559603 | 2.51e-07 | −3.304e-04 | −3.305e-04 | −0.436 | 6.7e-07 |
| 0.999 | 0.558026 | 0.557925 | 8.42e-09 | −6.060e-05 | −6.064e-05 | −0.437 | 3.5e-08 |
| 0.9995 | 0.557740 | 0.557644 | 1.78e-09 | −2.785e-05 | −2.787e-05 | −0.437 | 7.8e-09 |
| 0.9999 | 0.557496 | 0.557402 | 7.57e-12 | −1.800e-06 | −1.819e-06 | −0.437 | 3.5e-11 |
| 1.0 | 0.557433 | 0.557340 | 4.99e-11 | +4.689e-06 | +4.672e-06 | −0.437 | 2.3e-10 |
| 1.001 | 0.556740 | 0.556655 | 1.09e-08 | +6.910e-05 | +6.910e-05 | −0.438 | 6.0e-08 |
| 1.005 | 0.552377 | 0.552271 | 2.30e-07 | +3.181e-04 | +3.181e-04 | −0.441 | 2.6e-06 |
| 1.01 | 0.538648 | 0.538555 | 8.47e-07 | +6.191e-04 | +6.191e-04 | −0.453 | 1.1e-05 |

s₃ = 0 gives the same picture (sign change between s₂ = 0.9995 and 0.9999; ⟨u₂,φ̂⟩ K=34/46 agree to 2·10⁻⁸).
s₃ = 0.9 also (between 0.9995 and 0.9999). s₃ = 1 is not resolved: there T_* rises steeply (0.66 → 0.73 for
s₂ = 0.99 → 0.9999) toward the ζ point, where n = 4 is missing; ⟨u₂,φ̂⟩ < 0 up to s₂ = 0.9999.
Along each scan μ₂(T_*) ≈ −⟨u₂,φ̂⟩²/g(0) (the Type II law of 1901 Thm 1), so μ₂(T_*) → 0 exactly as ⟨u₂,φ̂⟩ → 0.

## 3. The Type I points (brentq in s₂ on h(s₂) = ⟨u₂,φ̂⟩(T_*(s₂,s₃)))

Columns: λ, μ₂, ⟨u₂,φ̂⟩ at (s₂^c, T_c); μ₁, μ₃; N₋ at T_c ∓ 10⁻⁴; λ at T_c ∓ 10⁻⁴; dμ₂/dT; d⟨u₂,φ̂⟩/dT;
f(0) at T_c ∓ 10⁻⁴.

| K | s₃ | s₂^c | T_c | λ | μ₂ | ⟨u₂,φ̂⟩ | g(0) | μ₁ | μ₃ | N₋ | λ(∓) | dμ₂/dT | d⟨u₂,φ̂⟩/dT | f(0)(∓) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 34 | 0.0 | 0.99976734 | 0.59309766 | +7.1e-15 | +4.70e-15 | -4.3e-16 | -0.4093 | -2.3158 | +0.5460 | 1/2 | +8.84e-06/-8.91e-06 | -0.089 | +0.0307 | -0.4094/-0.4092 |
| 46 | 0.0 | 0.99976760 | 0.59303740 | +6.7e-15 | +5.68e-15 | +2.9e-16 | -0.4093 | -2.3157 | +0.5458 | 1/2 | +8.83e-06/-8.89e-06 | -0.089 | +0.0306 | -0.4094/-0.4093 |
| 34 | 0.5 | 0.99977894 | 0.60650125 | +9.3e-15 | +8.07e-15 | -3.1e-15 | -0.3997 | -2.3989 | +0.3518 | 1/2 | +6.22e-06/-6.26e-06 | -0.062 | +0.0214 | -0.3998/-0.3997 |
| 46 | 0.5 | 0.99977927 | 0.60641823 | +1.6e-14 | +1.57e-14 | -3.6e-16 | -0.3998 | -2.3986 | +0.3520 | 1/2 | +6.26e-06/-6.30e-06 | -0.063 | +0.0215 | -0.3998/-0.3997 |
| 34 | 1.5 | 0.99994287 | 0.56580460 | -2.4e-17 | -1.62e-15 | +2.1e-16 | -0.4302 | -2.2604 | +0.4338 | 1/2 | +7.65e-06/-7.68e-06 | -0.077 | +0.0268 | -0.4303/-0.4301 |
| 46 | 1.5 | 0.99994302 | 0.56571970 | -4.2e-16 | +3.32e-16 | +8.3e-17 | -0.4303 | -2.2600 | +0.4313 | 1/2 | +7.63e-06/-7.66e-06 | -0.076 | +0.0267 | -0.4303/-0.4302 |
| 34 | 2.5 | 0.99992773 | 0.55747839 | +3.9e-16 | +1.12e-15 | -3.6e-16 | -0.4370 | -2.2260 | +0.4659 | 1/2 | +2.11e-05/-2.15e-05 | -0.213 | +0.0749 | -0.4370/-0.4369 |
| 46 | 2.5 | 0.99992801 | 0.55738477 | -9.3e-17 | +4.69e-16 | +6.8e-17 | -0.4370 | -2.2256 | +0.4608 | 1/2 | +2.13e-05/-2.17e-05 | -0.215 | +0.0759 | -0.4371/-0.4369 |
| 34 | 4.0 | 0.99992219 | 0.55335677 | -3.0e-13 | -2.96e-13 | -8.6e-17 | -0.4404 | -2.2075 | +0.4291 | 1/2 | +6.17e-05/-6.56e-05 | -0.636 | +0.2252 | -0.4405/-0.4403 |
| 46 | 4.0 | 0.99992221 | 0.55323089 | +2.3e-15 | +3.92e-15 | -3.8e-16 | -0.4405 | -2.2066 | +0.4228 | 1/2 | +5.76e-05/-6.17e-05 | -0.597 | +0.2111 | -0.4406/-0.4404 |

Stability of s₂^c and T_c:
- K = 34 vs 46: |Δs₂^c| ≤ 3·10⁻⁷, |ΔT_c| ≤ 1.3·10⁻⁴.
- Frequency cutoff and quadrature (K = 34): s₂^c is unchanged to 10⁻⁸ for tmax ∈ {1500, 3000, 6000} and Gauss order
  30/40 (s₃ = 0: 0.99976733 / 0.99976734 / 0.99976734; s₃ = 2.5: 0.99992773 in all four runs). T_c moves ≤ 7·10⁻⁶.

Check against R162_1901 Theorem 1 and §3 (all in float):
- (E1) μ₂(T_c) = 0 and (E2) ⟨u₂,φ̂⟩ = 0 hold to 10⁻¹⁴. (I) holds with room: g(0) ∈ [−0.44, −0.40].
- μ₂ is simple (gaps ≥ 0.35 to μ₃ and ≥ 2.2 to μ₁). It crosses transversally (dμ₂/dT ≈ −0.06 … −0.6). ⟨u₂,φ̂⟩
  vanishes to first order in T.
- λ goes from + to − through T_c. N₋ jumps 1 → 2. f(0) stays ≈ g(0) ≈ −0.41 (it does not cross 0). This is the
  **Type I signature** of 1901 §1 (Haynsworth reading), not Type II.
- T_c is the first contact: λ > 0 on [0.30, T_c) on the scan grid, and on (0, 0.30] no prime is present.

## 4. Verdict (UNCERTIFIED)

- **The weight-blind falsifier of R162_1901 §4 fires.** On the positive two-atom cone there is a curve
  s₂ = s₂^c(s₃) (s₂^c ∈ [0.99976, 0.99995] for s₃ ∈ [0,4], s₃ ≠ 1 tested) of Type I first even contacts.
  So R-C.b cannot hold for all positive combs. Any proof of R-C.b must use arithmetic of Λ.
- **Location is not generic.** The curve sits within 2.4·10⁻⁴ of s₂ = 1, the exact ζ weight at 2. At s₂ = 1 the contact
  is a near-alignment (⟨u₂,φ̂⟩ ~ 10⁻⁵, μ₂ ~ 10⁻¹⁰), which is the Perron–Tate phenomenon of 1803 §3 / 1701 Prop. 5
  persisting for every s₃. The sign change is produced by detuning the weight at 2 by about 10⁻⁴. Away from s₂ ≈ 1
  the margin is large (|⟨u₂,φ̂⟩(T_*)| ≥ 10⁻³ for |s₂ − 1| ≥ 0.02; T_μ₂ − T_* ≥ 10⁻⁵).
- Consequence for the programme (to be checked by the audit pass): R-C.b is not a cone statement. It is at best a
  statement about the arithmetic weights, and near them it is numerically delicate. For ζ itself (s₂ = s₃ = 1, and the
  full Λ), 1803 found no contact below ½log 5, so this result does not contradict anything claimed about ζ.
- Certification target: the sign change of h(s₂) at s₃ = 0 between s₂ = 0.9995 (h = −1.5·10⁻⁵) and 1.0
  (h = +1.3·10⁻⁵), plus continuity of T_*, needs an enclosure of ⟨u₂,φ̂⟩(T_*) to about 10⁻⁶ and a proof that λ > 0 on
  (0,T_*). The margins are small but ≥ 100× the observed K and cutoff variations.

No sign is claimed. No label moves. Gate 1 stays OPEN.
