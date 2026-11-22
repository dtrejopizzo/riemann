# Round 28, memo A — Extremal state of the nonnegative free-weight problem

Everything that follows is NUMERICAL (double precision, Legendre Galerkin of P46 eq:Aform, SDP with SCS; bases 30 and 40).
The scripts and outputs are in the temporary working folder `pbp_dual/` (`dual.py`, `analyze.py`, `an_T_N.txt`,
`crho_T_N.csv`). The computation was interrupted before the reading; this memo records only what the outputs show.

## Problem

`V*_T⁺ = max_{w ≥ 0} λ_min(a^w_T)` on `P_T`. Dual variable: mixed state `ρ*` of trace 1 on the lower eigenspace,
with `c_ρ*(log n) = 0` where `w*_n > 0` and `c_ρ*(log n) ≥ 0` where `w*_n = 0` (sign according to the script's convention).
KKT verified at `T = 1.6`, basis 40: `max|c_ρ*|` over `w* > 0` equal to `1.1e-10`; complementarity `2.3e-11`.

## T = 1.6, basis 40 (`V*_T⁺ = 0.00862`)

| n | v_n | w*_n | w*/v |
|---|---|---|---|
| 2 | 0.980 | 0.853 | 0.87 |
| 3 | 1.269 | 0.919 | 0.72 |
| 4 | 0.693 | 0.432 | 0.62 |
| 5 | 1.440 | 0.721 | 0.50 |
| 6 | 0 | 0.042 | — |
| 7 | 1.471 | 0.471 | 0.32 |
| 8 | 0.490 | 0.280 | 0.57 |
| 9 | 0.732 | 0 | 0 |
| 10 | 0 | 0.170 | — |
| 11 | 1.446 | 0.135 | 0.09 |
| 12 | 0 | 0.147 | — |
| 13 | 1.423 | 0.009 | 0.006 |
| 14–24 | — | 0 | — |

- The set `{n : w*_n > 0}` is NOT that of the prime powers: it contains 6, 10, 12 and excludes 9, 16, 17, 19, 23.
  The reading "the optimum reproduces the pattern of the primes" (made on the first ten values of 212-26-A) is false.
- The optimal weight rests on `n ≤ 13` and is zero on the top layer of the window.
- `ρ*` has rank 2: one odd and one even component, with weights `0.503` and `0.497`, mean frequency `≈ 6.7` in both,
  8–9 nodes, peak at `|t| ≈ 0.88`. It is equivalent to a single complex test `G = (F_even + iF_odd)/√2` with `c_ρ* = Re c_G`.
- `c_ρ*(u)` changes sign at `u = 0.24, 0.693, 1.107, 1.387, 1.613, 1.800, 1.947, 2.080, 2.307, 2.400, 2.493, 2.573, 3.2`:
  except for the first and the last, these are `log n` for `n = 2,…,8, 10,…,13`. Between contacts it oscillates with decreasing
  spacing; `c_ρ*″(0) ≈ −49.6`; minimum `−0.654`.
- Principal cosines of the support of `ρ*` with `span{Π_T(M∗φ_j)}` (10 functions): `0.999, 0.983`; with the control without `M`:
  `0.962, 0.936`; with a random subspace of dimension 10: `0.477, 0.352` (`dim P_T = 38`). It does not discriminate.

## T = 2.4, basis 40

Not converged: in that basis the Rayleigh quotient of the true weight on `X_δ` gives `4.8e-5` instead of a
tiny value. The table shows positive weights at 6, 12, 15, 20, 21, 28, 36, 50 and zero weights at many prime powers;
it is not used.

## Reading

- The extremal state is a packet of frequency `≈ 6.7`, near where the archimedean multiplier changes sign,
  whose autocorrelation vanishes at the small `log n`. No candidate formula.
- The pattern of the primes does not appear in the support of the optimal weight.
- OPEN: behavior for `T ≥ 2` with bases that resolve the boundary; whether `w*_n/v_n → 1` at fixed `n`.
